"""`veos project init|show|set|latest`: the orchestrator state file <project>/project.json (WORKFLOW section 3/4)."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from .core import VeosError, need_project, read_json, veos_home, write_json

PHASES = ["init", "prep", "roughcut", "captions", "plan", "storyboard", "approved", "render", "done"]
MODES = ["autopilot", "director"]


def add_args(p, cmd):
    p.add_argument("action", choices=["init", "show", "set", "latest"])
    p.add_argument("items", nargs="*", help="init: clip files/folders; set: key=value pairs")
    p.add_argument("--script", help="init: script file")
    p.add_argument("--mode", choices=MODES, help="init: autopilot (default) or director")
    p.add_argument("--playbook", help="init: playbook id (default naman)")
    p.add_argument("--force", action="store_true", help="init: overwrite an existing project.json")


def now() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def _registry() -> Path:
    return veos_home() / "projects.json"


def _load_registry() -> list[dict]:
    try:
        return list(read_json(_registry()).get("projects", []))
    except (OSError, ValueError):
        return []


def register(root: Path, updated: str) -> None:
    items = [e for e in _load_registry() if Path(e["path"]) != root]
    items.append({"path": root.as_posix(), "updated": updated})
    write_json(_registry(), {"version": 1, "projects": items})


def _state(root: Path) -> dict:
    f = root / "project.json"
    if not f.exists():
        raise VeosError("NO_PROJECT_FILE", f"no project.json in {root}", "Run `veos project init <clips> --project P` first.")
    return read_json(f)


def _brief(root: Path, st: dict) -> dict:
    return {"path": root.as_posix(), "phase": st.get("phase"), "mode": st.get("mode"), "updated": st.get("updated")}


def _init(args, project) -> dict:
    from .ingest import _collect  # lazy: pulls numpy
    if not args.items:
        raise VeosError("NO_CLIPS", "project init needs at least one clip file or folder", "Pass the clips or their folder.")
    first = Path(args.items[0]).expanduser()
    if not first.exists():
        raise VeosError("INPUT_MISSING", f"not found: {args.items[0]}", "Check the path (quote paths with spaces).")
    root = project.root if project else (first if first.is_dir() else first.parent).resolve() / "vibe-edit"
    if (root / "project.json").exists() and not args.force:
        raise VeosError("PROJECT_EXISTS", f"{root / 'project.json'} already exists",
                        "Resume it, or pass --force to start over.")
    clips = [f for f in _collect(args.items) if root not in f.parents]
    if not clips:
        raise VeosError("NO_MEDIA", "no video or audio files found", "Pass video files or a folder that contains them.")
    script = None
    if args.script:
        sp = Path(args.script).expanduser()
        if not sp.exists():
            raise VeosError("INPUT_MISSING", f"script not found: {args.script}", "Check the --script path.")
        script = sp.resolve().as_posix()
    t = now()
    st = {"version": 1, "created": t, "updated": t, "clips": [c.as_posix() for c in clips], "script": script,
          "mode": args.mode or "autopilot", "playbook": args.playbook or "naman",
          "phase": "init", "approved_at": None, "last_error": None, "history": [{"t": t, "phase": "init"}]}
    root.mkdir(parents=True, exist_ok=True)
    write_json(root / "project.json", st)
    register(root, t)
    return {"path": root.as_posix(), "phase": "init", "clips": len(clips), "mode": st["mode"]}


def _coerce(v: str):
    return None if v == "null" else v


def _set(args, project) -> dict:
    pr = need_project(project)
    st = _state(pr.root)
    if not args.items:
        raise VeosError("NO_PAIRS", "project set needs key=value pairs", "Example: veos project set phase=prep --project P")
    for kv in args.items:
        if "=" not in kv:
            raise VeosError("BAD_PAIR", f"'{kv}' is not key=value", "Use key=value (value 'null' clears it).")
        k, v = kv.split("=", 1)
        k = k.strip()
        if k in ("version", "created", "history", "updated"):
            raise VeosError("READONLY_KEY", f"'{k}' is managed by the engine", "")
        val = _coerce(v)
        if k == "phase":
            if val not in PHASES:
                raise VeosError("BAD_PHASE", f"phase '{v}' is not one of {', '.join(PHASES)}", "Use one of the listed phases.")
            if val != st.get("phase"):
                st.setdefault("history", []).append({"t": now(), "phase": val})
        elif k == "mode" and val not in MODES:
            raise VeosError("BAD_MODE", f"mode '{v}' must be autopilot or director", "")
        elif k == "approved_at" and val == "now":
            val = now()
        elif k == "clips" and val is not None:
            val = [c for c in v.split(";") if c]
        st[k] = val
    st["updated"] = now()
    write_json(pr.root / "project.json", st)
    register(pr.root, st["updated"])
    return {"state": {k: v for k, v in st.items() if k not in ("history", "clips")}, "clips": len(st.get("clips") or [])}


def _latest() -> dict:
    best = None
    for e in _load_registry():
        root = Path(e["path"])
        f = root / "project.json"
        if not f.exists():
            continue
        try:
            st = read_json(f)
        except ValueError:
            continue
        key = st.get("updated") or e.get("updated") or ""
        if best is None or key > best[0]:
            best = (key, root, st)
    if best is None:
        raise VeosError("NO_PROJECTS", "no registered project found", "Start one with `veos project init <clips>`.")
    return _brief(best[1], best[2])


def main(args, project) -> dict:
    if args.action == "init":
        return _init(args, project)
    if args.action == "latest":
        return _latest()
    if args.action == "set":
        return _set(args, project)
    pr = need_project(project)
    st = _state(pr.root)
    return {"state": {**{k: v for k, v in st.items() if k not in ("history", "clips")}, "clips": len(st.get("clips") or [])},
            "history": [f"{h['phase']}@{h['t']}" for h in st.get("history", [])][-6:]}
