"""Deterministic policy tests. Never contact Ncloud or a live account."""

import copy
import sys
import tempfile
import unittest
import urllib.error
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from connect_developer import atomic_json, exclusive_lock, read_json
from ncloud_ssh_backend import Api, Backend
from ssh_acg_policy import SafeError, host_cidr, ipv4, plan, reconcile

DEVICE = "a" * 32
MARKER = "trading-ssh:" + DEVICE
OLD, NEW = "8.8.8.8/32", "1.1.1.1/32"


def rule(cidr, description=MARKER):
    return {
        "ipBlock": cidr,
        "protocolType": {"code": "TCP"},
        "portRange": "22",
        "accessControlGroupRuleType": {"code": "INBND"},
        "accessControlGroupRuleDescription": description,
    }


class FakeBackend:
    def __init__(self, rules):
        self.items = copy.deepcopy(rules)
        self.events = []
        self.fail = None
        self.source = NEW

    def validate(self):
        self.events.append("validate")
        if self.fail == "validate":
            raise SafeError("Target invalid.")

    def rules(self):
        if self.fail == "rules":
            raise SafeError("API failure.")
        return copy.deepcopy(self.items)

    def wait_ready(self):
        if self.fail == "wait":
            raise SafeError("Propagation failure.")

    def add(self, cidr, marker):
        self.events.append("add")
        self.items.append(rule(cidr, marker))
        if self.fail == "add_timeout":
            raise SafeError("Uncertain add.")

    def verify_connection(self):
        self.events.append("verify")
        if self.fail == "verify":
            raise SafeError("Connection failure.")

    def current_cidr(self):
        return self.source

    def remove(self, cidr):
        self.events.append("remove")
        if self.fail == "remove":
            raise SafeError("Removal denied.")
        self.items = [r for r in self.items if r["ipBlock"] != cidr]


class PolicyTests(unittest.TestCase):
    def setUp(self):
        self.journal = {"device": DEVICE, "managed": [OLD]}
        self.saved = []

    def run_policy(self, backend, dry=False):
        return reconcile(
            backend, NEW, self.journal, lambda data: self.saved.append(copy.deepcopy(data)), dry
        )

    def test_rotation_verifies_before_deleting_and_preserves_foreign(self):
        manual = rule("9.9.9.9/32", "manual")
        foreign = rule("4.2.2.2/32", "trading-ssh:" + "b" * 32)
        backend = FakeBackend([rule(OLD), manual, foreign])
        self.run_policy(backend)
        self.assertEqual(backend.items, [manual, foreign, rule(NEW)])
        self.assertLess(backend.events.index("verify"), backend.events.index("remove"))
        self.assertIn(NEW, self.saved[0]["managed"])

    def test_same_ip_has_no_mutations(self):
        backend = FakeBackend([rule(NEW)])
        self.journal["managed"] = [NEW]
        self.run_policy(backend)
        self.assertNotIn("add", backend.events)
        self.assertNotIn("remove", backend.events)

    def test_existing_manual_current_rule_never_becomes_owned(self):
        backend = FakeBackend([rule(NEW, "manual")])
        self.run_policy(backend)
        self.assertNotIn(NEW, self.journal["managed"])
        self.assertNotIn("add", backend.events)

    def test_legacy_rule_is_not_adopted_or_removed(self):
        backend = FakeBackend([rule(OLD, "device SSH")])
        self.run_policy(backend)
        self.assertIn(rule(OLD, "device SSH"), backend.items)

    def test_dry_run_does_not_write_or_mutate(self):
        backend = FakeBackend([rule(OLD)])
        before = copy.deepcopy(self.journal)
        result = self.run_policy(backend, True)
        self.assertEqual(result, {"add": True, "remove_count": 1, "dry_run": True})
        self.assertEqual(self.journal, before)
        self.assertFalse(self.saved)
        self.assertNotIn("add", backend.events)

    def test_failed_validation_preserves_old_rules(self):
        for stage in ("validate", "rules", "wait", "verify", "add_timeout", "remove"):
            with self.subTest(stage=stage):
                backend = FakeBackend([rule(OLD)])
                backend.fail = stage
                with self.assertRaises(SafeError):
                    self.run_policy(backend)
                self.assertIn(rule(OLD), backend.items)

    def test_uncertain_add_retry_does_not_duplicate(self):
        backend = FakeBackend([rule(OLD)])
        backend.fail = "add_timeout"
        with self.assertRaises(SafeError):
            self.run_policy(backend)
        backend.fail = None
        self.run_policy(backend)
        self.assertEqual(backend.events.count("add"), 1)
        self.assertEqual(backend.items, [rule(NEW)])

    def test_hotspot_changes_before_delete_preserves_old(self):
        backend = FakeBackend([rule(OLD)])
        backend.source = "9.9.9.9/32"
        with self.assertRaises(SafeError):
            self.run_policy(backend)
        self.assertIn(rule(OLD), backend.items)

    def test_bad_public_sources_and_wide_cidr_are_rejected(self):
        for value in ("127.0.0.1", "10.0.0.1", "224.0.0.1", "::1", "not-an-ip", "1.1.1.1\n"):
            with self.subTest(value=value), self.assertRaises(SafeError):
                ipv4(value)
        with self.assertRaises(SafeError):
            host_cidr("0.0.0.0/0")

    def test_description_must_match_even_if_cidr_is_in_journal(self):
        self.assertEqual(plan([rule(OLD, "manual")], NEW, self.journal)["remove"], [])

    def test_duplicate_current_rule_stops(self):
        with self.assertRaises(SafeError):
            plan([rule(NEW), rule(NEW, "manual")], NEW, self.journal)

    def test_journal_write_failure_prevents_cloud_add(self):
        backend = FakeBackend([rule(OLD)])

        def fail_save(_):
            raise OSError("disk unavailable")

        with self.assertRaises(OSError):
            reconcile(backend, NEW, self.journal, fail_save)
        self.assertNotIn("add", backend.events)
        self.assertIn(rule(OLD), backend.items)

    def test_api_failure_after_add_preserves_old(self):
        backend = FakeBackend([rule(OLD)])
        original_add = backend.add

        def add_then_fail(cidr, marker):
            original_add(cidr, marker)
            backend.fail = "rules"

        backend.add = add_then_fail
        with self.assertRaises(SafeError):
            self.run_policy(backend)
        self.assertIn(rule(OLD), backend.items)
        self.assertNotIn("remove", backend.events)

    def test_rule_changed_to_manual_before_delete_is_preserved(self):
        backend = FakeBackend([rule(OLD)])
        original_verify = backend.verify_connection

        def verify_then_manual_edit():
            original_verify()
            backend.items[0]["accessControlGroupRuleDescription"] = "manual"

        backend.verify_connection = verify_then_manual_edit
        with self.assertRaises(SafeError):
            self.run_policy(backend)
        self.assertIn(rule(OLD, "manual"), backend.items)
        self.assertNotIn("remove", backend.events)

    def test_lost_ip_lookup_preserves_old(self):
        backend = FakeBackend([rule(OLD)])

        def failed_lookup():
            raise SafeError("IP lookup failed")

        backend.current_cidr = failed_lookup
        with self.assertRaises(SafeError):
            self.run_policy(backend)
        self.assertIn(rule(OLD), backend.items)

    def test_new_rule_disappears_before_removal_preserves_old(self):
        backend = FakeBackend([rule(OLD)])

        def connection_then_concurrent_delete():
            backend.events.append("verify")
            backend.items = [r for r in backend.items if r["ipBlock"] != NEW]

        backend.verify_connection = connection_then_concurrent_delete
        with self.assertRaises(SafeError):
            self.run_policy(backend)
        self.assertIn(rule(OLD), backend.items)
        self.assertNotIn("remove", backend.events)

    def test_current_manual_rule_arriving_before_add_is_not_reported_as_added(self):
        backend = FakeBackend([rule(OLD)])
        calls = 0
        original_rules = backend.rules

        def rules_with_concurrent_add():
            nonlocal calls
            calls += 1
            if calls == 2:
                backend.items.append(rule(NEW, "manual"))
            return original_rules()

        backend.rules = rules_with_concurrent_add
        result = self.run_policy(backend)
        self.assertFalse(result["add"])
        self.assertNotIn("add", backend.events)
        self.assertIn(rule(NEW, "manual"), backend.items)

    def test_old_rule_removed_externally_is_not_counted_as_tool_removal(self):
        backend = FakeBackend([rule(OLD)])

        def verify_and_external_cleanup():
            backend.events.append("verify")
            backend.items = [r for r in backend.items if r["ipBlock"] != OLD]

        backend.verify_connection = verify_and_external_cleanup
        result = self.run_policy(backend)
        self.assertEqual(result["remove_count"], 0)
        self.assertNotIn("remove", backend.events)


class LocalAndAdapterTests(unittest.TestCase):
    def test_atomic_journal_round_trip(self):
        with tempfile.TemporaryDirectory() as root:
            path = Path(root) / "journal.private.json"
            atomic_json(path, {"device": DEVICE, "managed": [NEW]})
            self.assertEqual(read_json(path)["managed"], [NEW])
            self.assertFalse(path.with_suffix(".pending").exists())

    @unittest.skipUnless(sys.platform == "win32", "Windows OS byte lock test")
    def test_duplicate_execution_rejected_then_lock_released(self):
        with tempfile.TemporaryDirectory() as root:
            path = Path(root) / "lock"
            with exclusive_lock(path):
                with self.assertRaises(SafeError):
                    with exclusive_lock(path):
                        self.fail("Must reject concurrent lock")
            with exclusive_lock(path):
                pass

    def test_no_provisioning_fallback(self):
        with patch("ncloud_ssh_backend.configparser.ConfigParser.read"):
            with self.assertRaisesRegex(SafeError, "no fallback"):
                Api("missing", "KR")

    def test_no_server_start_or_other_api_allowed(self):
        api = object.__new__(Api)
        for action in ("startServerInstances", "removeAccessControlGroupOutboundRule"):
            with self.assertRaises(SafeError):
                api.call(action)

    def test_stopped_server_prevents_nic_and_rule_calls(self):
        api = unittest.mock.Mock()
        api.rows.return_value = [
            {
                "serverInstanceNo": "server",
                "vpcNo": "vpc",
                "serverInstanceStatus": {"code": "STOP"},
                "publicIp": "8.8.8.8",
            }
        ]
        state = {
            "resources": {"serverInstanceNo": "server", "vpcNo": "vpc", "acgNo": "acg"},
            "server_public_ip": "8.8.8.8",
        }
        with self.assertRaises(SafeError):
            Backend(api, state, {}).validate()
        self.assertEqual(api.rows.call_count, 1)

    def test_wrong_nic_acg_prevents_rule_access(self):
        api = unittest.mock.Mock()
        api.rows.side_effect = [
            [
                {
                    "serverInstanceNo": "server",
                    "vpcNo": "vpc",
                    "serverInstanceStatus": {"code": "RUN"},
                    "publicIp": "8.8.8.8",
                }
            ],
            [
                {
                    "instanceNo": "server",
                    "isDefault": True,
                    "networkInterfaceStatus": {"code": "USED"},
                    "accessControlGroupNoList": ["other-acg"],
                }
            ],
        ]
        state = {
            "resources": {"serverInstanceNo": "server", "vpcNo": "vpc", "acgNo": "acg"},
            "server_public_ip": "8.8.8.8",
        }
        with self.assertRaises(SafeError):
            Backend(api, state, {}).validate()
        self.assertEqual(api.rows.call_count, 2)

    def test_incomplete_api_list_stops(self):
        api = object.__new__(Api)
        api.call = unittest.mock.Mock(return_value={"totalRows": 2, "items": [{}]})
        with self.assertRaises(SafeError):
            api.rows("getNetworkInterfaceList", "items")

    def test_http_auth_denial_does_not_expose_response_details(self):
        api = object.__new__(Api)
        api.region, api.access, api.secret = "KR", "test-access", "test-secret"
        api.opener = unittest.mock.Mock()
        api.opener.open.side_effect = urllib.error.HTTPError(
            "https://example.invalid/private-target", 403, "private-response", None, None
        )
        with self.assertRaises(SafeError) as caught:
            api.call("getServerInstanceList")
        self.assertIn("authorization denied", str(caught.exception))
        self.assertNotIn("private-response", str(caught.exception))
        self.assertNotIn("private-target", str(caught.exception))


if __name__ == "__main__":
    unittest.main()
