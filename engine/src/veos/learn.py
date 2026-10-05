"""`veos learn add|list|remove`: per-playbook learned feedback (<playbook>/learned.md + learned.json).

Learned rules override the playbook body, never the global rules. Entries are never deleted: `remove` sets active:false.
"""
from __future__ import annotations

from datetime import date

from . import paths
from .core import VeosError, read_json, write_json

AREAS = ["plan", "visuals", "captions", "sound", "cut", "pacing", "other"]
HEADER = "# Learned rules (from the creator's feedback; these override the playbook body, never the global rules)\n\n"


def add_args(p, cmd):
    p.add_argument("action", choices=["add", "list", "remove"])
    p.add_argument("--playbook", required=True, help="playbook id")
    p.add_argument("--text", help="add: the rule, one sentence")
    p.add_argument("--area", choices=AREAS, help="add: what it applies to")
    p.add_argument("--reel", help="add: project name the feedback came from")
    p.add_argument("--quote", help="add: the creator's own words")
    p.add_argument("--id", help="remove: entry id, e.g. L3")


def _line(e: dict) -> str:
    src = []
    if e.get("reel"):
        src.append(f"from: {e['reel']}")
    if e.get("quote"):
        src.append(f'said: "{e["quote"]}"')
    tail = f" ({'; '.join(src)})" if src else ""
    return f"{e['id']} · {e['date']} · {e['area']} · {e['text']}{tail}"


def _render(entries: list[dict]) -> str:
    return HEADER + "".join(_line(e) + "\n" for e in entries if e.get("active", True))


def _dir(pid: str):
    d = paths.find_playbook_dir(pid)
    if d is None:
        raise VeosError("PLAYBOOK_MISSING", f"playbook '{pid}' does not exist", "Check the id with `veos workspace get`.")
    return d


def _load(d) -> list[dict]:
    f = d / "learned.json"
    if not f.exists():
        return []
    try:
        data = read_json(f)
    except ValueError:
        raise VeosError("BAD_LEARNED", f"{f} is not valid JSON", "Fix or delete it.")
    return data if isinstance(data, list) else []


def _save(d, entries: list[dict]) -> None:
    write_json(d / "learned.json", entries)
    (d / "learned.md").write_text(_render(entries), encoding="utf-8", newline="\n")


def main(args, project) -> dict:
    d = _dir(args.playbook)
    entries = _load(d)
    if args.action == "add":
        if not args.text or not args.area:
            raise VeosError("MISSING_ARGS", "learn add needs --text and --area", f"--area is one of {', '.join(AREAS)}")
        nums = [int(str(e["id"])[1:]) for e in entries if str(e.get("id", ""))[1:].isdigit()]
        e = {"id": f"L{1 + max(nums or [0])}", "date": date.today().isoformat(), "area": args.area, "text": args.text.strip(),
             "reel": args.reel, "quote": args.quote, "active": True}
        entries.append(e)
        _save(d, entries)
        return {"playbook": args.playbook, "entry": e, "line": _line(e), "file": (d / "learned.md").as_posix()}
    if args.action == "list":
        return {"playbook": args.playbook, "entries": entries, "active": sum(1 for e in entries if e.get("active", True))}
    if not args.id:
        raise VeosError("MISSING_ARGS", "learn remove needs --id", "Example: --id L3")
    hit = next((e for e in entries if e.get("id") == args.id), None)
    if hit is None:
        raise VeosError("NO_SUCH_ENTRY", f"no learned entry {args.id}", "List them with `veos learn list --playbook ID`.")
    hit["active"] = False
    _save(d, entries)
    return {"playbook": args.playbook, "removed": args.id}
