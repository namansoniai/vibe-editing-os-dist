"""`veos workspace get|set` and `veos playbook new-id`: a folder remembers its playbook (one engine, many playbooks).

workspace get [--dir D]            walk up from D (default cwd) for `.vibe-editing-os.json`; also lists available playbooks.
workspace set --playbook ID [--dir D]   write D/.vibe-editing-os.json {"version":1,"playbook","created","updated"}.
playbook new-id --name "Aria Mehta" [--handle @x]   a unique kebab-case id that never collides with an existing playbook folder.
playbook index --project P | --playbook ID [--out F] [--force]   the reading guide (pbindex.py; directions, not rules).
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
        p.add_argument("action", choices=["new-id", "index"])
        p.add_argument("--name", help="new-id: creator name, e.g. 'Aria Mehta'")
        p.add_argument("--handle", help="new-id: creator handle, e.g. @fitwitharia (used when the name gives no usable id)")
        p.add_argument("--playbook", help="index: playbook / style template id (default: the project's playbook)")
        p.add_argument("--out", help="index: output file (default P/work/playbook-index.md, or VEOS_HOME/cache/playbook-index/ID.md)")
        p.add_argument("--force", action="store_true", help="index: rebuild even when the cached index is fresh")


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
                tok = read_json(tk) or {}
            except ValueError:
                tok = {}
            cr = tok.get("creator") or {}
            pm = d / "playbook.md"
            mt = max(tk.stat().st_mtime, pm.stat().st_mtime if pm.exists() else 0)
            rec = {"id": d.name, "name": cr.get("name"), "handle": cr.get("handle"),
                   "updated": datetime.fromtimestamp(mt).astimezone().isoformat(timespec="seconds")}
            if tok.get("kind") == "style_copy":  # path A copy: which template it came from (fidelity stays internal)
                lin = tok.get("lineage") or {}
                rec.update({"kind": "style_copy", "template": (lin.get("template") or {}).get("id"),
                            "style": (tok.get("style") or {}).get("name")})
            out.append(rec)
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
        if args.action == "index":
            from .pbindex import main as index_main
            return index_main(args, project)
        if not args.name:
            raise VeosError("BAD_ARGS", "playbook new-id needs --name", 'Example: veos playbook new-id --name "Aria Mehta"')
        return _new_id(args)
    return _get(args) if args.action == "get" else _set(args)
