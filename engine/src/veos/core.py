"""Shared helpers for every veos command: tool paths, JSON output, errors, project folders, ffmpeg runs."""
from __future__ import annotations

import json
import os
import platform
import shutil
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

FPS = 30
SIZE = (1080, 1920)


class VeosError(Exception):
    """An expected failure with a plain-language hint for the user."""

    def __init__(self, code: str, message: str, hint: str = ""):
        super().__init__(message)
        self.code, self.message, self.hint = code, message, hint


def veos_home() -> Path:
    env = os.environ.get("VEOS_HOME")
    if env:
        return Path(env)
    if platform.system() == "Windows":
        return Path(os.environ.get("LOCALAPPDATA", Path.home() / "AppData" / "Local")) / "VibeEditingOS"
    if platform.system() == "Darwin":
        return Path.home() / "Library" / "Application Support" / "VibeEditingOS"
    return Path.home() / ".local" / "share" / "VibeEditingOS"


@dataclass(frozen=True)
class Tools:
    home: Path
    ffmpeg: str
    ffprobe: str
    models: Path
    browsers: Path
    scratch: Path


def _find(name: str, home: Path) -> str | None:
    exe = name + (".exe" if platform.system() == "Windows" else "")
    local = home / "tools" / "ffmpeg" / "bin" / exe
    if local.exists():
        return str(local)
    return shutil.which(name)


def tools() -> Tools:
    home = veos_home()
    ff, fp = _find("ffmpeg", home), _find("ffprobe", home)
    if not ff or not fp:
        raise VeosError("FFMPEG_MISSING", "ffmpeg/ffprobe not found",
                        "Run /reel-setup (or `veos doctor`) to install the video tools.")
    browsers = Path(os.environ.get("PLAYWRIGHT_BROWSERS_PATH", home / "browsers"))
    os.environ.setdefault("PLAYWRIGHT_BROWSERS_PATH", str(browsers))
    os.environ.setdefault("HF_HOME", str(home / "models" / "hf"))
    os.environ.setdefault("HF_HUB_DISABLE_SYMLINKS_WARNING", "1")
    return Tools(home, ff, fp, home / "models", browsers, home / "scratch")


def need_project(project: "Project | None") -> "Project":
    if project is None:
        raise VeosError("NO_PROJECT", "this command needs --project DIR", "Pass the video's project folder with --project.")
    return project


class Project:
    """A project folder for one video. Sub-folders are created lazily, only when something is written."""

    def __init__(self, root: str | Path):
        self.root = Path(root).resolve()

    @property
    def work(self) -> Path:
        return self.root / "work"

    def path(self, *parts: str) -> Path:
        p = self.root.joinpath(*parts)
        p.parent.mkdir(parents=True, exist_ok=True)
        return p

    def rel(self, p: str | Path) -> str:
        p = Path(p).resolve()
        try:
            return p.relative_to(self.root).as_posix()
        except ValueError:
            return p.as_posix()

    def abs(self, p: str) -> Path:
        q = Path(p)
        return q if q.is_absolute() else self.root / q

    def log(self, cmd: str, text: str) -> None:
        if not self.root.exists():  # never create a project folder just to log (e.g. `veos doctor`)
            return
        (self.root / "logs").mkdir(exist_ok=True)
        with open(self.root / "logs" / f"{cmd}.log", "a", encoding="utf-8") as f:
            f.write(text.rstrip() + "\n")


def read_json(p: str | Path) -> Any:
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def write_json(p: str | Path, data: Any, indent: int | None = 1) -> None:
    Path(p).parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, ensure_ascii=False, indent=indent)


def run(cmd: list[str], project: Project | None = None, log_as: str = "", check: bool = True,
        capture: bool = True, input: bytes | None = None) -> subprocess.CompletedProcess:
    """Run a tool; on failure raise VeosError with the tail of stderr (full output goes to the log)."""
    r = subprocess.run(cmd, capture_output=capture, input=input)
    if project and log_as:
        err = (r.stderr or b"").decode("utf-8", "replace")
        project.log(log_as, "$ " + " ".join(cmd) + "\n" + err[-4000:])
    if check and r.returncode != 0:
        tail = (r.stderr or b"").decode("utf-8", "replace").strip().splitlines()[-3:]
        raise VeosError("TOOL_FAILED", f"{Path(cmd[0]).name} failed: {' | '.join(tail)}",
                        "See the log in <project>/logs for details.")
    return r


def r3(x: float) -> float:
    return round(float(x), 3)


def sec_to_frame(t: float, fps: int = FPS) -> int:
    return int(round(t * fps))


def emit(cmd: str, started: float, **summary: Any) -> None:
    """Print the single-line JSON result for a successful command."""
    out = {"ok": True, "cmd": cmd, **summary}
    out.setdefault("warnings", [])
    out["elapsed_s"] = round(time.time() - started, 2)
    sys.stdout.write(json.dumps(out, ensure_ascii=False, separators=(",", ":")) + "\n")


def fail(cmd: str, e: Exception) -> int:
    if isinstance(e, VeosError):
        err = {"code": e.code, "message": e.message, "hint": e.hint}
    else:
        err = {"code": "UNEXPECTED", "message": f"{type(e).__name__}: {e}", "hint": "This is a bug; the log has details."}
    sys.stdout.write(json.dumps({"ok": False, "cmd": cmd, "error": err}, ensure_ascii=False) + "\n")
    return 1
