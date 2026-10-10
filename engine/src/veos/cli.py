"""`veos` command-line entry point. Each command module exposes `add_args(parser, cmd)` and `main(args, project) -> dict`.

`main` returns the summary dict (printed as one JSON line by this dispatcher) or raises VeosError.
"""
from __future__ import annotations

import argparse
import importlib
import sys
import time
import traceback

from .core import Project, emit, fail

# command -> module (in veos/). Modules not yet built are reported as NOT_BUILT.
COMMANDS = {
    "doctor": "doctor", "ingest": "ingest", "conform": "conform", "transcribe": "transcribe",
    "cut": "cut", "matte": "matte", "faces": "matte", "capture": "capture", "render": "render", "assemble": "render",
    "sheet": "sheet", "storyboard": "storyboard", "sfx": "audio", "mix": "audio", "qa": "qa", "validate": "validate",
    "tokens": "tokens", "prep-frames": "prep", "bundle": "prep",
    "project": "project", "voice": "voice", "context": "context", "captions": "captions", "paths": "paths",
    "scenes-meta": "scenes", "measure": "scenes",
    "workspace": "workspace", "playbook": "workspace", "learn": "learn", "asset": "asset", "inserts": "inserts",
    "templates": "templates",
    "figures": "figures",
}
# multi-speaker / multi-camera (E-13, E-13b): session sync, speaker labels, angle registry, shots + compositor
COMMANDS.update({"sync": "sync", "speakers": "speakers", "angles": "angles", "shots": "shots"})
COMMANDS.update({"licence": "licence", "license": "licence"})
COMMANDS.update({"track": "track"})  # Package E: object / point tracking -> plan/tracks/<id>.json
COMMANDS.update({"look": "look"})  # see the cut before planning: frames by meaning -> review/look/ (+ --at close looks)
COMMANDS.update({"roughcut-candidates": "roughcut"})  # sentence-level take / false-start / pause list for the rough cut
COMMANDS.update({"stills": "stills"})  # review stills at every scene's declared moments -> review/stills/
COMMANDS.update({"beats": "beats"})  # no-voice reels: the music's beat map -> work/beats.json
# commands that run without an activated licence (licence.py); every other command needs one (LICENCE_REQUIRED)
UNGATED = {"doctor", "licence", "license", "paths"}


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    for s in (sys.stdout, sys.stderr):  # JSON summaries are UTF-8 (Windows pipes default to cp1252)
        try:
            s.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass
    if not argv or argv[0] in ("-h", "--help") or argv[0] not in COMMANDS:
        print("usage: veos <command> [args] --project DIR\ncommands: " + ", ".join(COMMANDS))
        return 0 if argv and argv[0] in ("-h", "--help") else 2
    cmd = argv[0]
    started = time.time()
    try:
        mod = importlib.import_module(f".{COMMANDS[cmd]}", __package__)
    except ModuleNotFoundError as e:
        return fail(cmd, RuntimeError(f"command '{cmd}' is not built yet ({e.name})"))
    p = argparse.ArgumentParser(prog=f"veos {cmd}")
    p.add_argument("--project", default=None, help="project folder for this video (required by project commands)")
    mod.add_args(p, cmd)
    args = p.parse_args(argv[1:])
    args.cmd = cmd
    proj = Project(args.project) if args.project else None
    try:
        if cmd not in UNGATED:
            from .licence import require
            require()
        summary = mod.main(args, proj)
    except Exception as e:  # noqa: BLE001 - every failure becomes one JSON line
        if proj:
            proj.log(cmd, traceback.format_exc())
        return fail(cmd, e)
    emit(cmd, started, **(summary or {}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
