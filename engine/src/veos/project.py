"""`veos project init|show|set|latest`: the orchestrator state file <project>/project.json (WORKFLOW section 3/4)."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from .core import VeosError, need_project, read_json, veos_home, write_json

PHASES = ["init", "prep", "roughcut", "captions", "inputs", "plan", "storyboard", "approved", "render", "done"]
MODES = ["autopilot", "director"]


def add_args(p, cmd):
    p.add_argument("action", choices=["init", "show", "set", "latest"])
    p.add_argument("items", nargs="*", help="init: clip files/folders; set: key=value pairs")
    p.add_argument("--script", help="init: script file")
    p.add_argument("--mode", choices=MODES, help="init: autopilot (default) or director")
    p.add_argument("--playbook", help="init: playbook id (default: the folder's workspace playbook)")
    p.add_argument("--force", action="store_true", help="init: overwrite an existing project.json")
    p.add_argument("--source-type", choices=SOURCE_TYPES,
                   help="init: talking_head, voiceover_only or animated_plates (default: voiceover_only when every clip "
                        "is audio, when --voiceover is given, or when the playbook's profile says so; animated_plates "
                        "when the profile says so; else talking_head). animated_plates: the clips are animation / "
                        "puppet plates, so face detection is skipped")
    p.add_argument("--voiceover", action="append", default=None, metavar="FILE",
                   help="init: the voice-over file (audio, or a video whose picture is ignored); implies voiceover_only")
    p.add_argument("--no-voice", action="store_true",
                   help="init: nobody speaks (B-roll / screen recording / photos + music + on-screen text): no_voice")
    p.add_argument("--music", default=None, metavar="FILE",
                   help="init: the music track of a no-voice reel (its beat map drives the cut)")


SOURCE_TYPES = ["talking_head", "voiceover_only", "animated_plates", "no_voice"]


def detect_source_type(clips: list[Path], explicit: str | None, voiceover: list | None, playbook: str | None,
                       no_voice: bool = False, music: bool = False) -> tuple[str, str]:
    """(source_type, why). Explicit flag > --no-voice > --voiceover > --music > the playbook profile > only photos >
    every clip (photos aside) is audio > talking_head."""
    from .media import AUDIO_EXT
    from .novoice import is_still
    if explicit:
        return explicit, "chosen"
    if no_voice:
        return "no_voice", "no voice: the cut follows the music"
    if voiceover:
        return "voiceover_only", "voice-over file given"
    if music:
        return "no_voice", "a music track given: the cut follows the music"
    if playbook:
        try:
            from .tokens import load_playbook
            prof = (load_playbook(playbook).get("profile") or {})
            if prof.get("source_type") == "voiceover_only":
                return "voiceover_only", "the playbook is voice-over only"
            if prof.get("source_type") == "no_voice":
                return "no_voice", "the playbook's reels have no voice (clips / photos + music + text)"
            if prof.get("source_type") == "animated_plates":
                return "animated_plates", "the playbook edits animation plates (no face detection)"
        except Exception:  # noqa: BLE001 - a missing / v3 playbook must not block init
            pass
    media = [c for c in clips if not is_still(c)]
    if clips and not media:
        return "no_voice", "only photos given"
    if media and all(c.suffix.lower() in AUDIO_EXT for c in media):  # a photo next to a voice-over is its thumbnail
        return "voiceover_only", "only audio files given"
    return "talking_head", "video clips"


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


def _workspace_playbook(first: Path, root: Path) -> str:
    """Playbook for a new project: an existing project.json's (backward compat), else the clips' folder workspace, else cwd's."""
    from .workspace import find_workspace
    pj = root / "project.json"
    if pj.exists():
        try:
            if read_json(pj).get("playbook"):
                return str(read_json(pj)["playbook"])
        except ValueError:
            pass
    for start in (first if first.is_dir() else first.parent, Path.cwd()):
        ws = find_workspace(start)
        if ws:
            return ws["playbook"]
    raise VeosError("PLAYBOOK_REQUIRED", "no playbook chosen for this folder",
                    "choose a playbook first: `veos workspace get` lists them, `veos workspace set --playbook ID --dir <clips folder>` remembers one "
                    "(or pass --playbook ID).")


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
    vo = [Path(v).expanduser().resolve() for v in (getattr(args, "voiceover", None) or [])]
    for v in vo:
        if not v.exists():
            raise VeosError("INPUT_MISSING", f"voice-over not found: {v}", "Check the --voiceover path.")
    music = Path(args.music).expanduser().resolve() if getattr(args, "music", None) else None
    if music is not None and not music.exists():
        raise VeosError("INPUT_MISSING", f"music not found: {music}", "Check the --music path.")
    clips = [f for f in _collect(args.items, stills=True) if root not in f.parents]
    clips += [v for v in vo if v not in clips]
    if music is not None and music not in clips:
        clips.append(music)
    script = None
    if args.script:
        sp = Path(args.script).expanduser()
        if not sp.exists():
            raise VeosError("INPUT_MISSING", f"script not found: {args.script}", "Check the --script path.")
        script = sp.resolve().as_posix()
    pb = args.playbook or _workspace_playbook(first, root)
    stype, why = detect_source_type(clips, getattr(args, "source_type", None), vo, pb, getattr(args, "no_voice", False),
                                    music is not None)
    if stype != "no_voice":  # photos are sources only in a no-voice reel
        from .novoice import is_still
        clips = [c for c in clips if not is_still(c)]
    if not clips:
        raise VeosError("NO_MEDIA", "no video or audio files found", "Pass video files or a folder that contains them.")
    t = now()
    st = {"version": 1, "created": t, "updated": t, "clips": [c.as_posix() for c in clips], "script": script,
          "mode": args.mode or "autopilot", "playbook": pb, "source_type": stype, "inputs": None,
          "phase": "init", "approved_at": None, "last_error": None, "history": [{"t": t, "phase": "init"}]}
    if vo:
        st["voiceover"] = [v.as_posix() for v in vo]
    if music is not None:
        st["music"] = [music.as_posix()]
    root.mkdir(parents=True, exist_ok=True)
    write_json(root / "project.json", st)
    register(root, t)
    return {"path": root.as_posix(), "phase": "init", "clips": len(clips), "mode": st["mode"], "source_type": stype,
            "source_type_why": why}


def _coerce(v: str):
    return None if v == "null" else v


def _json_value(k: str, v: str):
    """`inputs=@file.json` loads a JSON file; `inputs={"a":1}` parses inline JSON."""
    if v.startswith("@"):
        f = Path(v[1:]).expanduser()
        if not f.is_file():
            raise VeosError("INPUT_MISSING", f"JSON file not found: {v[1:]}", f"Check the path after @ for {k}.")
        try:
            return json.loads(f.read_text(encoding="utf-8-sig"))
        except ValueError as e:
            raise VeosError("BAD_JSON", f"{f.name} is not valid JSON: {e}", "Fix the JSON syntax.")
    if v == "null":
        return None
    try:
        return json.loads(v)
    except ValueError as e:
        raise VeosError("BAD_JSON", f"value for {k} is not valid JSON: {e}", "Pass JSON, or @file.json.")


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
        val = _json_value(k, v) if k == "inputs" else _coerce(v)
        if k == "phase":
            if val not in PHASES:
                raise VeosError("BAD_PHASE", f"phase '{v}' is not one of {', '.join(PHASES)}", "Use one of the listed phases.")
            if val != st.get("phase"):
                st.setdefault("history", []).append({"t": now(), "phase": val})
        elif k == "mode" and val not in MODES:
            raise VeosError("BAD_MODE", f"mode '{v}' must be autopilot or director", "")
        elif k == "source_type" and val not in SOURCE_TYPES:
            raise VeosError("BAD_SOURCE_TYPE", f"source_type '{v}' must be one of {', '.join(SOURCE_TYPES)}", "")
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
