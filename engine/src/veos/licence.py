"""`veos licence activate|status|validate|deactivate`: the buyer's licence on this computer.

activate --key K   normalise the key (case, dashes, O/0 and I/L look-alikes, checksum), register this computer with the
                   licence server (max 2 computers per key) and save VEOS_HOME/licence.json.
status             what is saved locally: plan (tier), computers used, last successful check, offline days left. No network.
validate           re-check with the server. Offline is fine for GRACE_DAYS since the last successful check.
deactivate         free this computer's slot on the server (to move the licence to a new laptop) and forget it here.

The gate (`require`) runs before every engine command except doctor / licence / paths (cli.py). It needs no network
while the last successful check is under RECHECK_HOURS old; after that it re-checks once, and if the server can't be
reached the buyer keeps working until GRACE_DAYS have passed since the last successful check.

Developer bypass: env VEOS_DEV=1, or running from the dev venv (VEOS_HOME/dev-venv). VEOS_DEV=0 forces the gate on
(tests).

Beta channel: only a beta build ships `_channel.json` beside this file (written by `tools/make_dist.py --channel beta`
into the dist copy; never committed to the source tree, and production builds refuse to ship it). With
`{"licence": false}` in it the gate is open: no key, no server, every template tier unlocked. Template tiers (`template.json` tier core|full) map to licence tiers in TEMPLATE_ACCESS.

Only these leave the computer: the key, a device id (a one-way hash of the machine id and the OS user name), the
computer's name (hostname) and the app version.
"""
from __future__ import annotations

import getpass
import hashlib
import hmac
import json
import os
import platform
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

from .core import VeosError, veos_home

SERVER = "https://veos-licence.shipwithoutcode.workers.dev"
FIND_KEY_URL = SERVER + "/find-key"
GRACE_DAYS = 7
RECHECK_HOURS = 24
TIMEOUT_S = 10

ALPHABET = "0123456789ABCDEFGHJKMNPQRSTVWXYZ"  # Crockford base32, same as the worker (src/keys.ts)
PREFIX = "VEOS"

TIER_NAMES = {"raw": "Raw", "roughcut": "Rough Cut", "studio": "Studio", "director": "Director's Cut"}
# licence tier -> template tiers it unlocks. Raw = the creator's own playbook only (path B).
TEMPLATE_ACCESS = {"raw": (), "roughcut": ("core",), "studio": ("core", "full"), "director": ("core", "full")}
# template tier -> the cheapest plan that unlocks it (for "upgrade to unlock")
UNLOCKED_BY = {"core": "roughcut", "full": "studio"}

SUPPORT = "email enquiry@deccansoft.com"
ACTIVATE_HINT = ("Activate your licence first: run /vibe-editing-os:setup and paste the licence key from your purchase "
                 "email (it looks like VEOS-XXXX-XXXX-XXXX-XXXX).")
LOST_KEY = f"Lost the email? Get your key at {FIND_KEY_URL} with your payment ID (pay_...) and checkout email."


# ------------------------------------------------------------------ helpers
def _now() -> datetime:
    return datetime.now(timezone.utc)


def _iso(t: datetime) -> str:
    return t.astimezone(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _parse(s: str | None) -> datetime | None:
    if not s:
        return None
    try:
        t = datetime.fromisoformat(str(s).replace("Z", "+00:00"))
        return t if t.tzinfo else t.replace(tzinfo=timezone.utc)
    except ValueError:
        return None


def server_url() -> str:
    return (os.environ.get("VEOS_LICENCE_URL") or SERVER).rstrip("/")


def licence_path() -> Path:
    return veos_home() / "licence.json"


def dev_mode() -> bool:
    """VEOS_DEV=1 -> on, VEOS_DEV=0 -> off; unset -> on only when running from the dev venv (VEOS_HOME/dev-venv)."""
    v = (os.environ.get("VEOS_DEV") or "").strip().lower()
    if v:
        return v not in ("0", "false", "no", "off")
    return Path(sys.prefix).name.lower() == "dev-venv"


CHANNEL_FILE = Path(__file__).with_name("_channel.json")


def channel() -> dict:
    """The build-channel marker ({} in production and in the source tree; see the module docstring)."""
    try:
        d = json.loads(CHANNEL_FILE.read_text(encoding="utf-8-sig"))
    except (OSError, ValueError):
        return {}
    return d if isinstance(d, dict) else {}


def licence_off() -> bool:
    """True only in a build whose channel marker says {"licence": false} (the beta)."""
    return channel().get("licence") is False


BETA_LINE = "beta build: no licence needed, every style unlocked"


def tier_name(tier: str | None) -> str:
    return TIER_NAMES.get(tier or "", (tier or "unknown").title())


def _checksum(body: str) -> str:
    s = 0
    for i, c in enumerate(body):
        s += ALPHABET.index(c) * (i + 1) * 7 + i
    return ALPHABET[s % 32]


def normalize_key(text: str | None) -> str | None:
    """User input -> canonical VEOS-XXXX-XXXX-XXXX-XXXX, or None if malformed / bad checksum (mirrors the worker)."""
    if not isinstance(text, str):
        return None
    s = "".join(text.strip().upper().split()).replace("-", "")
    if not s.startswith(PREFIX):
        return None
    s = s[len(PREFIX):].replace("O", "0").replace("I", "1").replace("L", "1")
    if len(s) != 16 or any(c not in ALPHABET for c in s) or _checksum(s[:15]) != s[15]:
        return None
    return f"{PREFIX}-{s[0:4]}-{s[4:8]}-{s[8:12]}-{s[12:16]}"


def mask_key(key: str | None) -> str:
    return f"{key[:9]}-****-****-{key[-4:]}" if key and len(key) == 24 else "?"


# ------------------------------------------------------------------ device identity
def _machine_id() -> str:
    import subprocess
    import uuid
    try:
        system = platform.system()
        if system == "Windows":
            import winreg
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Cryptography", 0,
                                winreg.KEY_READ | winreg.KEY_WOW64_64KEY) as k:
                return str(winreg.QueryValueEx(k, "MachineGuid")[0]).strip()
        if system == "Darwin":
            out = subprocess.run(["ioreg", "-rd1", "-c", "IOPlatformExpertDevice"], capture_output=True, text=True,
                                 timeout=10).stdout
            for line in out.splitlines():
                if "IOPlatformUUID" in line:
                    return line.split("=")[-1].strip().strip('"')
        for f in ("/etc/machine-id", "/var/lib/dbus/machine-id"):
            if Path(f).is_file():
                v = Path(f).read_text().strip()
                if v:
                    return v
    except Exception:  # noqa: BLE001 - fall back below
        pass
    return f"node-{uuid.getnode():012x}"


def _os_user() -> str:
    try:
        return getpass.getuser()
    except Exception:  # noqa: BLE001
        return os.environ.get("USERNAME") or os.environ.get("USER") or "user"


def device_id() -> str:
    """Stable per computer + OS user. A one-way hash: the machine id and user name never leave the computer."""
    raw = f"veos-device/1|{_machine_id()}|{_os_user()}"
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:32]


def device_name() -> str:
    import socket
    try:
        return (socket.gethostname() or platform.node() or "computer")[:60]
    except Exception:  # noqa: BLE001
        return "computer"


def app_version() -> str:
    try:
        from importlib.metadata import version
        return version("veos")
    except Exception:  # noqa: BLE001
        return "0"


# ------------------------------------------------------------------ server
class Offline(Exception):
    """The licence server could not be reached (no internet, timeout, proxy, server error)."""


def _post(endpoint: str, body: dict) -> tuple[int, dict]:
    """POST JSON -> (status, json). Raises Offline when there is no usable answer."""
    import urllib.error  # lazy: ~0.3 s, and only needed when talking to the server
    import urllib.request
    req = urllib.request.Request(server_url() + endpoint, data=json.dumps(body).encode("utf-8"), method="POST",
                                 headers={"content-type": "application/json", "accept": "application/json",
                                          "user-agent": f"veos/{app_version()} ({platform.system()})"})
    try:
        timeout = float(os.environ.get("VEOS_LICENCE_TIMEOUT") or TIMEOUT_S)
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, json.loads(r.read() or b"{}")
    except urllib.error.HTTPError as e:
        try:
            data = json.loads(e.read() or b"{}")
        except ValueError:
            data = {}
        if e.code >= 500 or not isinstance(data, dict) or "error" not in data:
            raise Offline(f"licence server answered HTTP {e.code}") from None
        return e.code, data
    except (urllib.error.URLError, TimeoutError, OSError, ValueError) as e:
        raise Offline(str(getattr(e, "reason", e))) from None


def _server_error(code: str, data: dict | None = None) -> VeosError:
    """A server rejection -> a plain-language error with the next step."""
    data = data or {}
    if code == "KEY_INVALID_FORMAT":
        return VeosError("KEY_INVALID", "That doesn't look like a Vibe Editing OS licence key.",
                         "Copy the key from your purchase email exactly; it looks like VEOS-XXXX-XXXX-XXXX-XXXX. " + LOST_KEY)
    if code == "KEY_NOT_FOUND":
        return VeosError("KEY_INVALID", "That licence key isn't recognised.",
                         "Check it against your purchase email (copy and paste works best). " + LOST_KEY)
    if code == "KEY_DISABLED":
        return VeosError("KEY_DISABLED", "This licence key has been switched off.",
                         f"Contact support ({SUPPORT}) and we'll sort it out.")
    if code == "DEVICE_LIMIT":
        n = data.get("max_devices") or 2
        return VeosError("DEVICE_LIMIT", f"Your licence is already active on {n} computers.",
                         "Deactivate one first: on the old computer, ask Claude to 'move my licence'. If you can't use "
                         f"the old computer any more, contact support ({SUPPORT}) and we'll free a slot.")
    if code == "DEVICE_NOT_REGISTERED":
        return VeosError("DEVICE_NOT_REGISTERED", "This computer is no longer activated for your licence "
                         "(it was moved to another computer or reset).", ACTIVATE_HINT)
    if code == "DEVICE_ID_REQUIRED":
        return VeosError("UNEXPECTED", "The licence request was missing this computer's id.", "This is a bug; please report it.")
    return VeosError("LICENCE_ERROR", f"The licence server said: {code}.", f"Try again in a minute; if it persists, contact support ({SUPPORT}).")


def _offline_error(why: str) -> VeosError:
    return VeosError("LICENCE_OFFLINE", "Couldn't reach the licence server.",
                     f"Check your internet connection and try again. Once activated, you can keep using it offline for "
                     f"{GRACE_DAYS} days. ({why})")


# ------------------------------------------------------------------ local file
def _sign(rec: dict) -> str:
    body = json.dumps({k: v for k, v in rec.items() if k != "sig"}, sort_keys=True, separators=(",", ":"))
    return hmac.new(("veos-licence/1|" + str(rec.get("device_id"))).encode(), body.encode(), hashlib.sha256).hexdigest()


def _save(rec: dict) -> dict:
    rec = {k: v for k, v in rec.items() if k != "sig"}
    rec["sig"] = _sign(rec)
    p = licence_path()
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(f".tmp{os.getpid()}")
    tmp.write_text(json.dumps(rec, indent=1), encoding="utf-8")
    os.replace(tmp, p)
    return rec


def load() -> tuple[dict | None, str]:
    """-> (record, state). state: missing | corrupt | other_device | ok."""
    p = licence_path()
    if not p.is_file():
        return None, "missing"
    try:
        rec = json.loads(p.read_text(encoding="utf-8-sig"))
        if not isinstance(rec, dict) or not normalize_key(rec.get("key")):
            return None, "corrupt"
    except (OSError, ValueError):
        return None, "corrupt"
    if not hmac.compare_digest(str(rec.get("sig", "")), _sign(rec)):
        return rec, "corrupt"
    if rec.get("device_id") != device_id():
        return rec, "other_device"
    return rec, "ok"


def _age(rec: dict) -> timedelta | None:
    """Time since the last successful check; None when unknown or in the future (a changed clock)."""
    t = _parse(rec.get("last_validated"))
    if not t:
        return None
    a = _now() - t
    return a if a >= timedelta(0) else None


def _grace_left(rec: dict) -> float:
    a = _age(rec)
    return 0.0 if a is None else max(0.0, GRACE_DAYS - a.total_seconds() / 86400)


def _apply(rec: dict, data: dict) -> dict:
    for k in ("tier", "features", "devices_used", "max_devices"):
        if k in data:
            rec[k] = data[k]
    rec["last_validated"] = _iso(_now())
    rec.pop("rejected", None)
    return rec


# ------------------------------------------------------------------ commands
def activate(key_text: str) -> dict:
    key = normalize_key(key_text)
    if not key:
        raise _server_error("KEY_INVALID_FORMAT")
    did = device_id()
    try:
        status, data = _post("/activate", {"key": key, "device_id": did, "device_name": device_name(),
                                            "app_version": app_version()})
    except Offline as e:
        raise _offline_error(str(e)) from None
    if not data.get("ok"):
        raise _server_error(str(data.get("error") or f"HTTP_{status}"), data)
    old, _ = load()
    rec = {"key": key, "device_id": did, "device_name": device_name(), "activated_at": _iso(_now())}
    if old and old.get("key") == key and old.get("activated_at"):
        rec["activated_at"] = old["activated_at"]
    rec = _save(_apply(rec, data))
    replaced = mask_key(old.get("key")) if old and old.get("key") not in (None, key) else None
    return {**summary(rec), "message": f"Licence activated: {tier_name(rec['tier'])} plan, this computer is "
                                       f"{rec.get('devices_used', '?')} of {rec.get('max_devices', 2)}.",
            **({"replaced_key": replaced} if replaced else {})}


def summary(rec: dict) -> dict:
    a = _age(rec)
    return {"active": True, "key": mask_key(rec.get("key")), "tier": rec.get("tier"), "tier_name": tier_name(rec.get("tier")),
            "devices_used": rec.get("devices_used"), "max_devices": rec.get("max_devices"),
            "device_name": rec.get("device_name"), "activated_at": rec.get("activated_at"),
            "last_validated": rec.get("last_validated"),
            "days_since_check": round(a.total_seconds() / 86400, 1) if a is not None else None,
            "offline_days_left": round(_grace_left(rec), 1), "templates": list(TEMPLATE_ACCESS.get(rec.get("tier"), ("core", "full")))}


def status() -> dict:
    """Local only (no network)."""
    if dev_mode():
        rec, state = load()
        return {"active": True, "dev": True, "line": "developer mode (no licence needed)",
                **({"saved": summary(rec)} if rec and state == "ok" else {})}
    if licence_off():
        return {"active": True, "beta": True, "channel": channel().get("channel", "beta"), "line": BETA_LINE}
    rec, state = load()
    if state != "ok":
        why = {"missing": "not activated on this computer", "corrupt": "the saved licence file is damaged",
               "other_device": "the saved licence belongs to another computer"}[state]
        return {"active": False, "state": state, "line": f"licence: {why}", "hint": ACTIVATE_HINT}
    s = summary(rec)
    if rec.get("rejected"):
        return {**s, "active": False, "state": "rejected", "line": f"licence: rejected by the server ({rec['rejected']})",
                "hint": ACTIVATE_HINT}
    ok = s["offline_days_left"] > 0
    when = "never" if s["days_since_check"] is None else (
        "today" if s["days_since_check"] < 1 else f"{int(s['days_since_check'])} day(s) ago")
    line = (f"licence: {s['tier_name']} plan, {s['devices_used']} of {s['max_devices']} computers used, last checked {when}"
            + ("" if ok else " (needs an online check)"))
    return {**s, "active": ok, "state": "ok" if ok else "stale", "line": line}


def validate() -> dict:
    """Online check. Within the offline grace a network failure is a warning, not an error."""
    if dev_mode():
        return {"valid": True, "dev": True, "line": "developer mode (no licence needed)"}
    if licence_off():
        return {"valid": True, "beta": True, "line": BETA_LINE}
    rec, state = load()
    if state != "ok":
        raise _required(state)
    try:
        status_, data = _post("/validate", {"key": rec["key"], "device_id": rec["device_id"]})
    except Offline:
        left = _grace_left(rec)
        if left > 0 and not rec.get("rejected"):
            return {**summary(rec), "valid": True, "offline": True,
                    "message": f"Couldn't reach the licence server; check your internet. You can keep using Vibe Editing "
                               f"OS offline for {max(1, round(left))} more day(s)."}
        raise _offline_expired(rec) from None
    if not data.get("ok"):
        code = str(data.get("error") or f"HTTP_{status_}")
        rec["rejected"] = code
        _save(rec)
        raise _server_error(code, data)
    rec = _save(_apply(rec, data))
    return {**summary(rec), "valid": True, "offline": False,
            "message": f"Licence OK: {tier_name(rec['tier'])} plan, {rec.get('devices_used')} of {rec.get('max_devices')} computers."}


def deactivate() -> dict:
    rec, state = load()
    if state == "missing" or rec is None:
        return {"deactivated": False, "message": "This computer has no licence activated, so there is nothing to free."}
    did = rec.get("device_id") if state == "ok" else device_id()
    try:
        status_, data = _post("/deactivate", {"key": rec["key"], "device_id": did})
    except Offline as e:
        raise VeosError("LICENCE_OFFLINE", "Couldn't reach the licence server, so this computer is still counted.",
                        f"Check your internet connection and try again. ({e})") from None
    if not data.get("ok"):
        raise _server_error(str(data.get("error") or f"HTTP_{status_}"), data)
    licence_path().unlink(missing_ok=True)
    return {"deactivated": True, "devices_used": data.get("devices_used"), "max_devices": data.get("max_devices"),
            "message": f"This computer is deactivated; your licence is now on {data.get('devices_used')} of "
                       f"{data.get('max_devices')} computers. Activate it on the new computer with the same key."}


# ------------------------------------------------------------------ gate
def _required(state: str) -> VeosError:
    msg = {"missing": "No licence is activated on this computer.",
           "corrupt": "The saved licence on this computer is damaged.",
           "other_device": "The saved licence was activated on another computer."}.get(state, "A licence is required.")
    return VeosError("LICENCE_REQUIRED", msg, ACTIVATE_HINT)


def _offline_expired(rec: dict) -> VeosError:
    if rec.get("rejected"):
        e = _server_error(rec["rejected"])
        return VeosError("LICENCE_REQUIRED", e.message, e.hint + " (The licence server can't be reached right now either; "
                         "check your internet.)")
    return VeosError("LICENCE_REQUIRED", f"Your licence hasn't been checked for over {GRACE_DAYS} days and the licence "
                     "server can't be reached.", "Check your internet connection, then try again: it only needs to be "
                     f"online for a moment once every {GRACE_DAYS} days.")


def require() -> dict:
    """Raise LICENCE_REQUIRED unless this computer may run engine commands. Network only once a day at most."""
    if dev_mode():
        return {"dev": True}
    if licence_off():
        return {"beta": True}
    rec, state = load()
    if state != "ok":
        raise _required(state)
    a = _age(rec)
    if not rec.get("rejected") and a is not None and a < timedelta(hours=RECHECK_HOURS):
        return rec
    try:
        status_, data = _post("/validate", {"key": rec["key"], "device_id": rec["device_id"]})
    except Offline:
        if not rec.get("rejected") and _grace_left(rec) > 0:
            return rec  # offline grace
        raise _offline_expired(rec) from None
    if not data.get("ok"):
        code = str(data.get("error") or f"HTTP_{status_}")
        rec["rejected"] = code
        _save(rec)
        e = _server_error(code, data)
        raise VeosError("LICENCE_REQUIRED", e.message, e.hint)
    return _save(_apply(rec, data))


# ------------------------------------------------------------------ template tiers
def template_access() -> dict:
    """Which template tiers this install may use. Local only (the gate already checked the licence)."""
    if dev_mode():
        return {"dev": True, "tier": None, "tier_name": "developer", "allowed": ["core", "full"]}
    if licence_off():
        return {"dev": False, "beta": True, "tier": None, "tier_name": "beta (everything unlocked)", "allowed": ["core", "full"]}
    rec, state = load()
    tier = rec.get("tier") if rec and state == "ok" and not rec.get("rejected") else None
    allowed = list(TEMPLATE_ACCESS.get(tier, ("core", "full"))) if tier else []
    return {"dev": False, "tier": tier, "tier_name": tier_name(tier) if tier else None, "allowed": allowed}


def unlock_plan(template_tier: str | None) -> str:
    """The plan name that unlocks a template tier, e.g. 'Rough Cut'."""
    return tier_name(UNLOCKED_BY.get(template_tier or "full", "studio"))


# ------------------------------------------------------------------ doctor
def doctor_check() -> tuple[bool, str, str]:
    """(ok, one-line detail, hint) for `veos doctor`. Local only."""
    s = status()
    if s.get("dev") or s.get("beta"):
        return True, s["line"], ""
    return bool(s["active"]), s["line"].removeprefix("licence: "), (
        "" if s["active"] else s.get("hint") or "Check your internet connection, then run `veos licence validate`.")


# ------------------------------------------------------------------ cli
def add_args(p, cmd):
    p.add_argument("action", choices=["activate", "status", "validate", "deactivate"])
    p.add_argument("--key", help="activate: the licence key from the purchase email (VEOS-XXXX-XXXX-XXXX-XXXX)")


def main(args, project) -> dict:
    a = args.action
    if a == "activate":
        if not args.key:
            raise VeosError("MISSING_ARGS", "activate needs the licence key",
                            "Example: veos licence activate --key VEOS-XXXX-XXXX-XXXX-XXXX")
        return activate(args.key)
    if a == "status":
        return status()
    if a == "validate":
        return validate()
    return deactivate()
