"""`veos learn add|list|remove`: per-playbook learned feedback (<playbook>/learned.md + learned.json).

Learned rules override the playbook body, never the global rules. Entries are never deleted: `remove` sets active:false.

Template copies (path A, `kind: style_copy`): `add --change PATH=VALUE` classifies the rule against the copy's `locks`
(lineage.py). Buyers can change anything: VAR / TUNE in range are applied and logged in `lineage.tuned`; DNA (or TUNE
out of range) is applied too and recorded as DV-n in `lineage.deviations` (no confirmation step, no warning). Only the
global quality guarantees (NC, or `--nc NC-n` for a prose rule) are refused, in one line with the nearest allowed
alternative; nothing is saved then.
Without --change the rule is saved as prose, as for every other playbook. `remove` deactivates a rule; token changes it
applied stay (undo them with a new change).
"""
from __future__ import annotations

from datetime import date

from . import lineage, paths
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
    p.add_argument("--change", action="append", default=None, metavar="PATH=VALUE",
                   help="add (template copies): the token change this rule makes, e.g. captions.profiles.CS-1.skin.size=42 "
                        "(repeatable; VALUE is JSON when it parses)")
    p.add_argument("--confirm", action="store_true", help="add: accepted for old callers; changes apply without it")
    p.add_argument("--reason", help="add: why (kept with a change that moves away from the style, DV-n)")
    p.add_argument("--source", choices=["learned", "buyer"], default="learned",
                   help="add: learned = feedback while editing (lineage source learned:L-n); buyer = a direct 'change my playbook'")
    p.add_argument("--nc", help="add: the rule as worded breaks this never-bendable rule (e.g. NC-1); it is refused")


def _line(e: dict) -> str:
    src = []
    if e.get("reel"):
        src.append(f"from: {e['reel']}")
    if e.get("quote"):
        src.append(f'said: "{e["quote"]}"')
    if e.get("changes"):
        src.append(("applied: " if e.get("class") else "changes: ") + ", ".join(f"{c['path']} = {lineage.fmt(c['to'])}" + (f" [{c['dv']}]" if c.get("dv") else "")
                                            for c in e["changes"]))
    tail = f" ({'; '.join(src)})" if src else ""
    cls = f" · {e['class']}" if e.get("class") else ""
    return f"{e['id']} · {e['date']} · {e['area']}{cls} · {e['text']}{tail}"


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
        res = None
        try:
            tok = read_json(d / "tokens.json")
        except (OSError, ValueError):
            tok = {}
        if lineage.is_style_copy(tok if isinstance(tok, dict) else {}) and (args.change or args.nc):
            changes = [lineage.parse_change(c) for c in (args.change or [])]
            src = "buyer" if args.source == "buyer" else f"learned:{e['id']}"
            res = lineage.apply_changes(d, changes, source=src, reason=args.reason or args.quote, confirm=args.confirm,
                                        nc=args.nc)
            if res["status"] != "applied":
                return {"playbook": args.playbook, "saved": False, **res}
            e["class"] = res["class"]
            e["changes"] = [{k: c[k] for k in ("path", "from", "to", "class", "dv") if k in c} for c in res["changes"]]
        elif args.change:
            e["changes"] = [{"path": p, "to": v} for p, v in (lineage.parse_change(c) for c in args.change)]
        entries.append(e)
        _save(d, entries)
        out = {"playbook": args.playbook, "saved": True, "entry": e, "line": _line(e), "file": (d / "learned.md").as_posix()}
        if res:
            out.update({k: v for k, v in res.items() if k != "changes"})
        elif lineage.is_style_copy(tok if isinstance(tok, dict) else {}):
            out["hint"] = ("saved as a prose rule; when it changes a token value, pass --change PATH=VALUE so it is checked "
                           "against the style's locks and logged in the copy's lineage")
        return out
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
