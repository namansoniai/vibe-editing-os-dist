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
    "cut": "cut", "matte": "matte", "capture": "capture", "render": "render", "assemble": "render",
    "sheet": "sheet", "storyboard": "storyboard", "sfx": "audio", "mix": "audio", "qa": "qa", "validate": "validate",
    "tokens": "tokens", "prep-frames": "prep", "bundle": "prep",
    "project": "project", "voice": "voice", "context": "context", "captions": "captions", "paths": "paths",
    "scenes-meta": "scenes", "measure": "scenes",
}


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
        summary = mod.main(args, proj)
    except Exception as e:  # noqa: BLE001 - every failure becomes one JSON line
        if proj:
            proj.log(cmd, traceback.format_exc())
        return fail(cmd, e)
    emit(cmd, started, **(summary or {}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
