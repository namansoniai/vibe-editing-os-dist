"""`veos doctor [--quick]`: is this machine ready to edit? Needs no project."""
from __future__ import annotations

import os
import platform
import shutil
import subprocess
import sys
import time
from pathlib import Path

from .core import _find, r3, read_json, veos_home


def _ram_gb() -> float | None:
    try:
        if platform.system() == "Windows":
            import ctypes

            class MS(ctypes.Structure):
                _fields_ = [("l", ctypes.c_ulong), ("load", ctypes.c_ulong), ("total", ctypes.c_ulonglong),
                            ("avail", ctypes.c_ulonglong), ("a", ctypes.c_ulonglong), ("b", ctypes.c_ulonglong),
                            ("c", ctypes.c_ulonglong), ("d", ctypes.c_ulonglong), ("e", ctypes.c_ulonglong)]

            m = MS()
            m.l = ctypes.sizeof(MS)
            ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(m))
            return m.total / 2 ** 30
        return os.sysconf("SC_PHYS_PAGES") * os.sysconf("SC_PAGE_SIZE") / 2 ** 30
    except Exception:  # noqa: BLE001
        return None


def _cpu_name() -> str:
    try:
        if platform.system() == "Windows":
            import winreg
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"HARDWARE\DESCRIPTION\System\CentralProcessor\0") as k:
                return str(winreg.QueryValueEx(k, "ProcessorNameString")[0]).strip()
    except Exception:  # noqa: BLE001
        pass
    return platform.processor() or platform.machine()


def _version(exe: str | None) -> str | None:
    if not exe:
        return None
    try:
        out = subprocess.run([exe, "-version"], capture_output=True, timeout=10).stdout.decode("utf-8", "replace")
        return out.split("\n")[0].split(" Copyright")[0].replace("ffmpeg version ", "").replace("ffprobe version ", "").strip()
    except Exception:  # noqa: BLE001
        return None


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[3]  # engine/src/veos -> repo root


def main(args, project) -> dict:
    home = veos_home()
    checks: list[dict] = []

    def add(name: str, ok: bool, detail: str, hint: str = "") -> None:
        checks.append({"name": name, "ok": bool(ok), "detail": detail, **({} if ok else {"hint": hint})})

    # machine
    ram = _ram_gb()
    anchor = home if home.exists() else next((p for p in home.parents if p.exists()), Path.home())
    du = shutil.disk_usage(anchor)
    free_gb = du.free / 2 ** 30
    machine = {"os": f"{platform.system()} {platform.release()} ({platform.version()})", "cpu": _cpu_name(),
               "cores": os.cpu_count(), "ram_gb": round(ram, 1) if ram else None, "disk_free_gb": round(free_gb, 1)}
    add("disk space", free_gb >= 20, f"{free_gb:.0f} GB free on {anchor.drive or anchor}",
        "Free up disk space; renders and models need about 20 GB.")
    add("memory", ram is None or ram >= 8, f"{ram:.0f} GB RAM" if ram else "unknown",
        "Under 8 GB of RAM: renders will be slow; close other programs.")
    add("VEOS_HOME", home.exists(), str(home), "Run /reel-setup to create the tools folder.")
    add("python", sys.version_info >= (3, 11), platform.python_version(), "Use Python 3.11 or newer.")

    # ffmpeg
    ff, fp = _find("ffmpeg", home), _find("ffprobe", home)
    fv, pv = _version(ff), _version(fp)
    add("ffmpeg", bool(fv), fv or "not found", "Run /reel-setup to install ffmpeg (the video tool).")
    add("ffprobe", bool(pv), pv or "not found", "Run /reel-setup to install ffprobe (comes with ffmpeg).")

    # browser
    br = Path(os.environ.get("PLAYWRIGHT_BROWSERS_PATH", home / "browsers"))
    chromium = sorted(br.glob("chromium-*")) + sorted(br.glob("chromium_headless_shell-*")) if br.exists() else []
    add("chromium", bool(chromium), ", ".join(p.name for p in chromium) or f"none in {br}",
        "Run /reel-setup to download the browser used for rendering.")
    if chromium and not args.quick:
        t0 = time.time()
        try:
            os.environ.setdefault("PLAYWRIGHT_BROWSERS_PATH", str(br))
            from playwright.sync_api import sync_playwright
            with sync_playwright() as pw:
                b = pw.chromium.launch(headless=True)
                pg = b.new_page()
                pg.set_content("<p>ok</p>")
                b.close()
            add("chromium launch", True, f"headless launch ok in {time.time() - t0:.1f} s")
        except Exception as e:  # noqa: BLE001
            add("chromium launch", False, f"{type(e).__name__}: {str(e)[:120]}",
                "The browser is installed but will not start; re-run /reel-setup or restart the PC.")

    # models
    models = home / "models"
    rvm = sorted((models / "rvm").glob("*.onnx")) if (models / "rvm").exists() else []
    add("model: background matte (RVM)", bool(rvm), rvm[0].name if rvm else "missing",
        "Run /reel-setup to download the background-removal model.")
    mp = sorted((models / "mediapipe").glob("*.tflite")) if (models / "mediapipe").exists() else []
    face = [p for p in mp if "face" in p.name]
    add("model: face detector (mediapipe)", bool(face), face[0].name if face else "missing",
        "Run /reel-setup to download the face detection model.")
    hf = Path(os.environ.get("HF_HOME", models / "hf"))
    wh = sorted((hf / "hub").glob("models--*faster-whisper-large-v3-turbo*")) if (hf / "hub").exists() else []
    wok = any(list(p.glob("snapshots/*/model.bin")) for p in wh)
    add("model: speech-to-text (whisper turbo)", wok, wh[0].name if wok else "missing",
        "Run /reel-setup to download the transcription model (about 1.6 GB).")

    # fonts
    fdir = Path(os.environ.get("VEOS_FONTS", _repo_root() / "assets" / "fonts"))
    fj = fdir / "fonts.json"
    if fj.exists():
        try:
            want = [f for k, v in read_json(fj).items() if isinstance(v, dict) for f in v.get("files", [])]
            miss = [f for f in want if not (fdir / f).exists()]
            add("fonts", not miss, f"{len(want) - len(miss)}/{len(want)} files in {fdir}",
                f"Missing font files: {', '.join(miss[:4])}. Re-download the repo's assets/fonts.")
        except Exception as e:  # noqa: BLE001
            add("fonts", False, f"fonts.json unreadable ({e})", "Re-download the repo's assets/fonts.")
    else:
        add("fonts", False, f"no fonts.json in {fdir}", "The assets/fonts folder is missing; re-download the repo.")

    problems = [f"{c['name']}: {c['detail']}. {c['hint']}" for c in checks if not c["ok"]]
    if problems:
        status = f"veos: {len(problems)} problem(s): " + "; ".join(c["name"] for c in checks if not c["ok"]) + " (run `veos doctor`)"
    else:
        status = f"veos: ready (ffmpeg {fv.split()[0] if fv else '?'}, {len(checks)} checks ok)"
    return {"status": status, "ready": not problems, "machine": machine, "home": str(home), "checks": checks,
            "problems": problems, "quick": bool(args.quick)}


def add_args(p, cmd: str) -> None:
    p.add_argument("--quick", action="store_true", help="fast file-presence check only (no launches); for a SessionStart hook")
