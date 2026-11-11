"""Windows entry point. State/credentials stay outside the repository."""

import argparse
import contextlib
import json
import os
import sys
import uuid
from pathlib import Path

from ncloud_ssh_backend import Api, Backend
from ssh_acg_policy import SafeError, reconcile


def read_json(path):
    return json.loads(path.read_bytes().decode("utf-8-sig", errors="strict"))


def atomic_json(path, data):
    temp = path.with_suffix(".pending")
    with temp.open("w", encoding="utf-8", newline="\n") as stream:
        json.dump(data, stream, ensure_ascii=True, indent=2)
        stream.write("\n")
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temp, path)


@contextlib.contextmanager
def exclusive_lock(path):
    # OS byte lock is released on crashes; lock file existence is not ownership.
    import msvcrt

    with path.open("a+b") as stream:
        if stream.tell() == 0:
            stream.write(b"0")
            stream.flush()
        stream.seek(0)
        try:
            msvcrt.locking(stream.fileno(), msvcrt.LK_NBLCK, 1)
        except OSError:
            raise SafeError("Another ACG reconciliation is running; stop.") from None
        try:
            yield
        finally:
            stream.seek(0)
            msvcrt.locking(stream.fileno(), msvcrt.LK_UNLCK, 1)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--verify-only", action="store_true")
    parser.add_argument("--profile", default="ssh-acg")
    args = parser.parse_args()
    root = Path(os.environ["LOCALAPPDATA"]) / "TradingAutomation/provisioning"
    try:
        with exclusive_lock(root / "ssh-acg.lock"):
            state = read_json(root / "youtube-analyzer-state.private.json")
            inputs = read_json(root / "youtube-analyzer-inputs.private.json")
            # Credentials are read only; never copied, rewritten, or sent to the server.
            api = Api(args.profile, inputs["region"])
            backend = Backend(api, state, inputs)
            backend.ssh_args()  # Check local authentication inputs before cloud changes.
            path = root / "ssh-acg-managed.private.json"
            scope = {k: str(state["resources"][k]) for k in ("serverInstanceNo", "vpcNo", "acgNo")}
            journal = (
                read_json(path)
                if path.exists()
                else {
                    "device": uuid.uuid4().hex,
                    "scope": scope,
                    "managed": [],
                }
            )
            if journal.get("scope") != scope:
                raise SafeError("Ownership journal target changed; manual review required.")
            current = api.current_cidr()
            result = reconcile(
                backend, current, journal, lambda value: atomic_json(path, value), args.dry_run
            )
            print(json.dumps(result))  # Booleans/counts only; no identifiers or addresses.
        # Release cloud mutation lock before opening a potentially long interactive session.
        if not args.dry_run and not args.verify_only:
            return backend.connect()
        return 0
    except SafeError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    except (OSError, ValueError, KeyError, TypeError):
        print(
            "Local configuration or runtime failure; stop. Private details suppressed.",
            file=sys.stderr,
        )
        return 2


if __name__ == "__main__":
    sys.exit(main())
