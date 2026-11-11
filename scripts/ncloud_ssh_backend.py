"""Restricted Ncloud API and local SSH adapters. Never log raw responses or commands."""

import base64
import configparser
import hashlib
import hmac
import json
import os
import socket
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

from ssh_acg_policy import SafeError, ipv4

ALLOWED = {
    "getServerInstanceList",
    "getNetworkInterfaceList",
    "getAccessControlGroupList",
    "getAccessControlGroupRuleList",
    "addAccessControlGroupInboundRule",
    "removeAccessControlGroupInboundRule",
}


class Api:
    def __init__(self, profile, region):
        config = configparser.ConfigParser(interpolation=None)
        config.read(Path.home() / ".ncloud/configure", encoding="utf-8-sig")
        if not config.has_section(profile):
            raise SafeError(
                "API profile missing. Prepare dedicated ssh-acg credentials; no fallback."
            )
        self.access = config[profile].get("ncloud_access_key_id")
        self.secret = config[profile].get("ncloud_secret_access_key")
        if not self.access or not self.secret:
            raise SafeError("API credentials missing. Prepare dedicated ssh-acg credentials.")
        self.region = region
        # Direct HTTPS prevents a proxy from reporting a different public source for ipify.
        self.opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))

    def call(self, action, **params):
        if action not in ALLOWED:
            raise SafeError("API operation is not allowed by this tool.")
        query = {"regionCode": self.region, **params, "responseFormatType": "json"}
        uri = "/vserver/v2/" + action + "?" + urllib.parse.urlencode(query)
        ts = str(int(time.time() * 1000))
        signature = base64.b64encode(
            hmac.new(
                self.secret.encode(), f"GET {uri}\n{ts}\n{self.access}".encode(), hashlib.sha256
            ).digest()
        ).decode()
        request = urllib.request.Request(
            "https://ncloud.apigw.ntruss.com" + uri,
            headers={
                "x-ncp-apigw-timestamp": ts,
                "x-ncp-iam-access-key": self.access,
                "x-ncp-apigw-signature-v2": signature,
            },
        )
        try:
            with self.opener.open(request, timeout=20) as response:
                data = json.load(response)
        except urllib.error.HTTPError as exc:
            if exc.code in (401, 403):
                raise SafeError(
                    "API authorization denied; stop and requery. See dedicated auth setup."
                ) from None
            raise SafeError(
                "API HTTP failure; do not retry mutation blindly. Requery next run."
            ) from None
        except (OSError, ValueError):
            raise SafeError(
                "API transport/response failure; stop and requery before retry."
            ) from None
        body = data.get(action + "Response") if isinstance(data, dict) else None
        if not isinstance(body, dict) or str(body.get("returnCode")) != "0":
            raise SafeError(
                "API rejected request; stop and check auth permissions/source restrictions."
            )
        return body

    def rows(self, action, key, **params):
        body = self.call(action, **params)
        rows = body.get(key)
        if not isinstance(rows, list) or int(body.get("totalRows", len(rows))) != len(rows):
            raise SafeError("Incomplete API list; no further changes allowed.")
        return rows

    def current_cidr(self):
        try:
            with self.opener.open("https://api.ipify.org", timeout=15) as response:
                value = response.read(65).decode("ascii").strip()
        except (OSError, ValueError):
            raise SafeError("Public IPv4 lookup failed; stop and requery before retry.") from None
        return ipv4(value) + "/32"


class Backend:
    def __init__(self, api, state, inputs):
        self.api, self.state, self.inputs = api, state, inputs
        resources = state["resources"]
        self.server = str(resources["serverInstanceNo"])
        self.vpc = str(resources["vpcNo"])
        self.acg = str(resources["acgNo"])
        self.host = ipv4(state["server_public_ip"])

    def validate(self):
        servers = self.api.rows(
            "getServerInstanceList",
            "serverInstanceList",
            **{
                "serverInstanceNoList.1": self.server,
                "pageNo": 1,
                "pageSize": 1000,
            },
        )
        if len(servers) != 1:
            raise SafeError("Designated server is not uniquely identified.")
        server = servers[0]
        if (
            str(server.get("serverInstanceNo")) != self.server
            or str(server.get("vpcNo")) != self.vpc
            or server.get("serverInstanceStatus", {}).get("code") != "RUN"
            or server.get("publicIp") != self.host
        ):
            raise SafeError("Server stopped or target changed; never auto-start or retarget.")
        nics = self.api.rows(
            "getNetworkInterfaceList",
            "networkInterfaceList",
            instanceNo=self.server,
            pageNo=1,
            pageSize=1000,
        )
        attached = [
            n
            for n in nics
            if str(n.get("instanceNo")) == self.server
            and n.get("isDefault") is True
            and n.get("networkInterfaceStatus", {}).get("code") == "USED"
            and self.acg in [str(x) for x in n.get("accessControlGroupNoList", [])]
        ]
        if not attached:
            raise SafeError("Designated ACG is not on an actual server NIC; no changes.")
        groups = self.groups()
        if (
            len(groups) != 1
            or str(groups[0].get("vpcNo")) != self.vpc
            or str(groups[0].get("accessControlGroupNo")) != self.acg
        ):
            raise SafeError("Designated ACG/VPC identity mismatch.")

    def groups(self):
        return self.api.rows(
            "getAccessControlGroupList",
            "accessControlGroupList",
            vpcNo=self.vpc,
            **{"accessControlGroupNoList.1": self.acg, "pageNo": 1, "pageSize": 1000},
        )

    def wait_ready(self):
        for _ in range(15):
            groups = self.groups()
            if (
                len(groups) == 1
                and str(groups[0].get("accessControlGroupNo")) == self.acg
                and groups[0].get("accessControlGroupStatus", {}).get("code") == "RUN"
            ):
                return
            time.sleep(2)
        raise SafeError("ACG propagation timed out; stop and requery before retry.")

    def rules(self):
        return self.api.rows(
            "getAccessControlGroupRuleList",
            "accessControlGroupRuleList",
            vpcNo=self.vpc,
            accessControlGroupNo=self.acg,
        )

    def mutate(self, action, cidr, description=None):
        params = {
            "accessControlGroupRuleList.1.protocolTypeCode": "TCP",
            "accessControlGroupRuleList.1.ipBlock": cidr,
            "accessControlGroupRuleList.1.portRange": "22",
        }
        if description:
            params["accessControlGroupRuleList.1.accessControlGroupRuleDescription"] = description
        self.api.call(action, vpcNo=self.vpc, accessControlGroupNo=self.acg, **params)

    def add(self, cidr, marker):
        self.wait_ready()
        self.mutate("addAccessControlGroupInboundRule", cidr, marker)

    def remove(self, cidr):
        self.mutate("removeAccessControlGroupInboundRule", cidr)

    def current_cidr(self):
        return self.api.current_cidr()

    def ssh_args(self):
        if not self.state.get("ssh_hostkey_verified"):
            raise SafeError("Host key has not been verified; stop.")
        public = Path(self.inputs["user_public_key_file"])
        if public.suffix != ".pub":
            raise SafeError("Unexpected developer public-key path.")
        key = public.with_suffix("")
        known = Path(self.state["ssh_known_hosts_file"])
        if not key.is_file() or not known.is_file():
            raise SafeError(
                "Existing developer key/known_hosts missing; no authentication changes."
            )
        ssh = Path(os.environ.get("WINDIR", "C:/Windows")) / "System32/OpenSSH/ssh.exe"
        return [
            str(ssh),
            "-F",
            "none",
            "-o",
            "StrictHostKeyChecking=yes",
            "-o",
            "UpdateHostKeys=no",
            "-o",
            "HostKeyAlgorithms=ssh-ed25519",
            "-o",
            "IdentitiesOnly=yes",
            "-o",
            "PasswordAuthentication=no",
            "-o",
            "KbdInteractiveAuthentication=no",
            "-o",
            "ConnectTimeout=12",
            "-o",
            f"UserKnownHostsFile={known}",
            "-i",
            str(key),
        ]

    def verify_connection(self):
        try:
            with socket.create_connection((self.host, 22), timeout=12):
                pass
            result = subprocess.run(
                self.ssh_args() + ["-o", "BatchMode=yes", "developer@" + self.host, "true"],
                capture_output=True,
                timeout=25,
            )
        except (OSError, subprocess.TimeoutExpired):
            raise SafeError("TCP/SSH verification failed; stop and requery before retry.") from None
        if result.returncode:
            raise SafeError("Pinned-host developer key authentication failed; stop and requery.")

    def connect(self):
        # Interactive terminal output is the user's SSH session, not an automation log.
        status = subprocess.call(
            self.ssh_args() + ["developer@" + self.host], stderr=subprocess.DEVNULL
        )
        if status:
            raise SafeError("SSH session ended with an error; connection details suppressed.")
        return status
