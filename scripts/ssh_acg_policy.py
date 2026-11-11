"""SSH rule reconciliation; no network or credential access in this module."""

import ipaddress
import re


class SafeError(Exception):
    """Only static, non-sensitive messages may cross the CLI boundary."""


def ipv4(value):
    try:
        addr = ipaddress.IPv4Address(value)
    except (ValueError, TypeError):
        raise SafeError("Invalid public IPv4; no old rule removed.") from None
    if not addr.is_global or addr.is_multicast or str(addr) != value:
        raise SafeError("Non-public IPv4; no old rule removed.")
    return str(addr)


def host_cidr(value):
    if not isinstance(value, str) or not value.endswith("/32"):
        raise SafeError("Managed source must be a public IPv4 /32.")
    return ipv4(value[:-3]) + "/32"


def ssh_rule(rule):
    return (
        rule.get("accessControlGroupRuleType", {}).get("code") == "INBND"
        and rule.get("protocolType", {}).get("code") in ("TCP", "6")
        and str(rule.get("portRange")) == "22"
        and not rule.get("accessControlGroupSequence")
    )


def ownership(journal):
    device = journal.get("device", "")
    if not re.fullmatch(r"[a-f0-9]{32}", device):
        raise SafeError("Invalid device ownership journal.")
    for cidr in journal.get("managed", []):
        host_cidr(cidr)
    return "trading-ssh:" + device


def plan(rules, current, journal):
    """Foreign/manual rules never become owned just because their source matches."""
    target = host_cidr(current)
    marker = ownership(journal)
    owned = set(journal.get("managed", []))
    matches = [r for r in rules if ssh_rule(r) and r.get("ipBlock") == target]
    if len(matches) > 1:
        raise SafeError("Ambiguous current SSH rules; manual review required.")
    old = [
        r["ipBlock"]
        for r in rules
        if ssh_rule(r)
        and r.get("ipBlock") in owned
        and r["ipBlock"] != target
        and r.get("accessControlGroupRuleDescription") == marker
    ]
    return {"add": not matches, "remove": sorted(set(old))}


def reconcile(backend, current, journal, save, dry_run=False):
    """Persist intent before add; verify reachability before each exact owned delete."""
    target = host_cidr(current)
    backend.validate()
    backend.wait_ready()
    initial = backend.rules()
    result = plan(initial, target, journal)
    if dry_run:
        return {"add": result["add"], "remove_count": len(result["remove"]), "dry_run": True}
    marker = ownership(journal)
    added = False
    removed = 0
    if result["add"]:
        # A timeout after acceptance is resolved by listing rules on the next run.
        # A rule already present before this request was never added to this journal.
        journal["managed"] = sorted(set(journal.get("managed", [])) | {target})
        save(journal)
        backend.validate()
        latest = backend.rules()
        if not any(ssh_rule(r) and r.get("ipBlock") == target for r in latest):
            backend.add(target, marker)
            added = True
    backend.wait_ready()
    backend.validate()
    rules = backend.rules()
    if not any(ssh_rule(r) and r.get("ipBlock") == target for r in rules):
        raise SafeError("New SSH rule was not observed; stop and requery before retry.")
    backend.verify_connection()
    # Detect hotspot changes during the operation, before deleting any old source.
    if backend.current_cidr() != target:
        raise SafeError("Public IPv4 changed during validation; stop and requery before retry.")
    for old in result["remove"]:
        backend.validate()
        backend.wait_ready()
        fresh = backend.rules()
        if not any(ssh_rule(r) and r.get("ipBlock") == target for r in fresh):
            raise SafeError("Current SSH rule disappeared; stop and requery before retry.")
        candidates = [r for r in fresh if ssh_rule(r) and r.get("ipBlock") == old]
        if not candidates:
            continue
        if len(candidates) != 1 or candidates[0].get("accessControlGroupRuleDescription") != marker:
            raise SafeError("Rule ownership changed; stop without deleting that rule.")
        if backend.current_cidr() != target:
            raise SafeError("Public IPv4 changed; stop and requery before retry.")
        backend.verify_connection()
        backend.remove(old)
        backend.wait_ready()
        if any(ssh_rule(r) and r.get("ipBlock") == old for r in backend.rules()):
            raise SafeError("Deletion not confirmed; stop and requery next run.")
        removed += 1
    backend.validate()
    backend.verify_connection()
    # Retain intent for every managed source, including pending/uncertain operations.
    save(journal)
    return {"add": added, "remove_count": removed, "dry_run": False}
