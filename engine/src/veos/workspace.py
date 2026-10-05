"""`veos workspace get|set` and `veos playbook new-id`: a folder remembers its playbook (one engine, many playbooks).

workspace get [--dir D]            walk up from D (default cwd) for `.vibe-editing-os.json`; also lists available playbooks.
workspace set --playbook ID [--dir D]   write D/.vibe-editing-os.json {"version":1,"playbook","created","updated"}.
playbook new-id --name "Aria Mehta" [--handle @x]   a unique kebab-case id that never collides with an existing playbook folder.
"""
from __future__ import annotations

import re
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

from . import paths
from .core import VeosError, read_json, write_json

MARKER = ".vibe-editing-os.json"


def add_args(p, cmd):
    if cmd == "workspace":
        p.add_argument("action", choices=["get", "set"])
        p.add_argument("--playbook", help="set: playbook id")
        p.add_argument("--dir", help="folder (default: current directory)")
    else:
        p.add_argument("action", choices=["new-id"])
        p.add_argument("--name", required=True, help="creator name, e.g. 'Aria Mehta'")
        p.add_argument("--handle", help="creator handle, e.g. @fitwitharia (used when the name gives no usable id)")


def _now() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def find_workspace(start: Path | None = None) -> dict | None:
    """Nearest `.vibe-editing-os.json` at or above `start` (a file's parent is used when `start` is a file)."""
    d = (Path(start) if start else Path.cwd()).expanduser().resolve()
    if d.is_file():
        d = d.parent
    for cand in [d, *d.parents]:
        f = cand / MARKER
        if f.is_file():
            try:
                data = read_json(f)
            except ValueError:
                continue
            if isinstance(data, dict) and data.get("playbook"):
                return {"dir": cand.as_posix(), "playbook": str(data["playbook"]), "created": data.get("created")}
    return None


def list_playbooks() -> list[dict]:
    base = paths.playbooks_dir()
    out = []
    if base.is_dir():
        for d in sorted(base.iterdir()):
            tk = d / "tokens.json"
            if d.name.startswith("_") or not tk.is_file():
                continue
            try:
                cr = (read_json(tk) or {}).get("creator") or {}
            except ValueError:
                cr = {}
            pm = d / "playbook.md"
            mt = max(tk.stat().st_mtime, pm.stat().st_mtime if pm.exists() else 0)
            out.append({"id": d.name, "name": cr.get("name"), "handle": cr.get("handle"),
                        "updated": datetime.fromtimestamp(mt).astimezone().isoformat(timespec="seconds")})
    return out


def _get(args) -> dict:
    found = find_workspace(Path(args.dir) if args.dir else None)
    return {"found": bool(found), "dir": found["dir"] if found else None,
            "playbook": found["playbook"] if found else None, "created": found["created"] if found else None,
            "playbooks": list_playbooks()}


def _set(args) -> dict:
    if not args.playbook:
        raise VeosError("NO_PLAYBOOK", "workspace set needs --playbook ID", "Example: veos workspace set --playbook naman")
    if paths.find_playbook_dir(args.playbook) is None:
        have = ", ".join(p["id"] for p in list_playbooks()) or "(none)"
        raise VeosError("PLAYBOOK_MISSING", f"playbook '{args.playbook}' does not exist", f"Use one of: {have}; or create it first.")
    d = (Path(args.dir) if args.dir else Path.cwd()).expanduser().resolve()
    if not d.is_dir():
        raise VeosError("DIR_MISSING", f"folder not found: {d}", "Pass an existing folder with --dir.")
    f = d / MARKER
    created = _now()
    if f.is_file():
        try:
            created = (read_json(f) or {}).get("created") or created
        except ValueError:
            pass
    write_json(f, {"version": 1, "playbook": args.playbook, "created": created, "updated": _now()})
    return {"dir": d.as_posix(), "playbook": args.playbook, "file": f.as_posix()}


def slug(text: str) -> str:
    s = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def _new_id(args) -> dict:
    base = slug(args.name) or slug((args.handle or "").lstrip("@")) or "creator"
    taken = set()
    for b in {paths.playbooks_dir(), paths.app_root() / "playbooks"}:
        if b.is_dir():
            taken |= {d.name.lower() for d in b.iterdir()}
    cand, i = base, 1
    while cand in taken:
        i += 1
        cand = f"{base}-{i}"
    return {"id": cand, "path": (paths.playbooks_dir() / cand).as_posix()}


def main(args, project) -> dict:
    if args.cmd == "playbook":
        return _new_id(args)
    return _get(args) if args.action == "get" else _set(args)
