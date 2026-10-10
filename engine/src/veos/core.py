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


def has_engine(home: Path) -> bool:
    """A Windows VEOS_HOME with an installed engine (the installer's venv, or a dev-venv)."""
    return any((home / v / "Scripts" / "python.exe").is_file() for v in ("venv", "dev-venv"))


def windows_homes() -> tuple[Path, Path]:
    """(new, legacy) default homes on Windows. The new one sits in the user profile, outside AppData: a packaged app (the
    Claude desktop app from the Store / claude.ai is MSIX) has its %LOCALAPPDATA% writes silently redirected to
    %LOCALAPPDATA%/Packages/Claude_*/LocalCache, which broke uv's Python links. 0.6.0 and earlier installed in the legacy one."""
    profile = Path(os.environ.get("USERPROFILE") or Path.home())
    local = Path(os.environ.get("LOCALAPPDATA") or profile / "AppData" / "Local")
    return profile / "VibeEditingOS", local / "VibeEditingOS"


def veos_home() -> Path:
    """VEOS_HOME env -> (Windows) %USERPROFILE%/VibeEditingOS if it exists -> legacy %LOCALAPPDATA%/VibeEditingOS if it holds
    an engine (installs from 0.6.0 and earlier keep working) -> %USERPROFILE%/VibeEditingOS. Same order in install.ps1 and
    plugin/bin/veos(.cmd), so the installer and the engine always agree."""
    env = os.environ.get("VEOS_HOME")
    if env:
        return Path(env)
    if platform.system() == "Windows":
        new, legacy = windows_homes()
        if new.exists() or not has_engine(legacy):
            return new
        return legacy
    if platform.system() == "Darwin":
        return Path.home() / "Library" / "Application Support" / "VibeEditingOS"
    return Path.home() / ".local" / "share" / "VibeEditingOS"


def home_env(home: Path | None = None) -> dict[str, str]:
    """Everything the engine downloads, caches or scratches lives inside VEOS_HOME, never in AppData / the system temp:
    browsers, model caches, temp files. The values the `veos` wrappers set; `python -m veos` applies them at start."""
    h = Path(home or veos_home())
    tmp = str(h / "tmp")
    return {"VEOS_HOME": str(h), "PLAYWRIGHT_BROWSERS_PATH": str(h / "browsers"), "HF_HOME": str(h / "models" / "hf"),
            "TORCH_HOME": str(h / "models" / "torch"), "MPLCONFIGDIR": str(h / "cache" / "matplotlib"),
            "PIP_CACHE_DIR": str(h / "cache" / "pip"), "HF_HUB_DISABLE_SYMLINKS_WARNING": "1",
            "TMP": tmp, "TEMP": tmp, "TMPDIR": tmp}


def apply_home_env() -> Path:
    """Set home_env() for this process (temp dirs always; the caches only where not already set, so a wrapper or a test
    can point them elsewhere). Creates VEOS_HOME/tmp; leaves the temp vars alone if it can't."""
    home = veos_home()
    env = home_env(home)
    try:
        Path(env["TMP"]).mkdir(parents=True, exist_ok=True)
        for k in ("TMP", "TEMP", "TMPDIR"):
            os.environ[k] = env[k]
        import tempfile
        tempfile.tempdir = None  # re-read on next use
    except OSError:
        pass
    for k, v in env.items():
        if k not in ("TMP", "TEMP", "TMPDIR"):
            os.environ.setdefault(k, v)
    return home


def packaged_app() -> str | None:
    """Windows: the package this process runs inside (e.g. the Claude desktop app's MSIX package), or None. Inside one,
    %LOCALAPPDATA% writes are redirected to %LOCALAPPDATA%/Packages/<package>/LocalCache."""
    if platform.system() != "Windows":
        return None
    try:
        import ctypes
        k32 = ctypes.windll.kernel32
        n = ctypes.c_uint32(0)
        if k32.GetCurrentPackageFullName(ctypes.byref(n), None) == 15700:  # APPMODEL_ERROR_NO_PACKAGE
            return None
        buf = ctypes.create_unicode_buffer(max(n.value, 1))
        if k32.GetCurrentPackageFullName(ctypes.byref(n), buf) == 0:
            return buf.value or "unknown package"
    except Exception:  # noqa: BLE001 - very old Windows / no kernel32 export
        return None
    return None


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
    """A JSON file, with or without a UTF-8 byte-order mark (Windows PowerShell's Out-File / Set-Content write one)."""
    with open(p, encoding="utf-8-sig") as f:
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


_FILTER_FORM: dict[str, str] = {}
INLINE_MAX = 24000  # chars: a filter graph longer than this never goes on the command line (Windows caps it at 32767)


def filter_form(ffmpeg: str) -> str:
    """How this ffmpeg reads a filter graph from a file: "-/filter_complex" (ffmpeg 7+; recent nightlies removed
    -filter_complex_script), "-filter_complex_script" (ffmpeg 6 and older), or "inline". Probed once per binary on a
    1-frame null source."""
    if ffmpeg in _FILTER_FORM:
        return _FILTER_FORM[ffmpeg]
    import tempfile
    form = "inline"
    with tempfile.TemporaryDirectory() as d:
        f = Path(d) / "probe.txt"
        f.write_text("[0:v]null[v]", encoding="utf-8")
        for opt in ("-/filter_complex", "-filter_complex_script"):
            try:
                r = subprocess.run([ffmpeg, "-v", "error", "-f", "lavfi", "-i", "nullsrc=s=16x16:d=0.04", opt, str(f),
                                    "-map", "[v]", "-frames:v", "1", "-f", "null", "-"], capture_output=True, timeout=30)
            except (OSError, subprocess.SubprocessError):
                continue
            if r.returncode == 0:
                form = opt
                break
    _FILTER_FORM[ffmpeg] = form
    return form


def filter_complex_args(script: Path, ffmpeg: str | None = None) -> list[str]:
    """ffmpeg arguments that apply the filter graph written in `script`, in the form this ffmpeg supports (see
    filter_form); the graph goes inline only when neither file form works and it is short enough."""
    form = filter_form(ffmpeg or tools().ffmpeg)
    if form != "inline":
        return [form, str(script)]
    graph = Path(script).read_text(encoding="utf-8-sig")
    if len(graph) > INLINE_MAX:
        raise VeosError("FFMPEG_FILTER_FILE", "this ffmpeg reads filter graphs neither from -/filter_complex nor "
                        "-filter_complex_script, and the graph is too long for the command line",
                        "Update the engine (`veos doctor`) so it uses its bundled ffmpeg.")
    return ["-filter_complex", graph.replace("\n", "")]


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
