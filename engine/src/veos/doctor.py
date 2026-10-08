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


# fx.three (renderer/fx3d.js) needs a WebGL2 context; headless Chromium provides one on SwiftShader (software) without a GPU
WEBGL_PROBE = """() => { const g = document.createElement('canvas').getContext('webgl2'); if (!g) return null;
  const d = g.getExtension('WEBGL_debug_renderer_info'); return d ? g.getParameter(d.UNMASKED_RENDERER_WEBGL) : g.getParameter(g.RENDERER); }"""


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

    # licence (local file only, no network): one line
    from . import licence
    lic_ok, lic_line, lic_hint = licence.doctor_check()
    add("licence", lic_ok, lic_line, lic_hint)

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
                from .render import CHROME_ARGS
                b = pw.chromium.launch(headless=True, args=CHROME_ARGS)
                pg = b.new_page()
                pg.set_content("<p>ok</p>")
                webgl = pg.evaluate(WEBGL_PROBE)
                b.close()
            add("chromium launch", True, f"headless launch ok in {time.time() - t0:.1f} s")
            add("webgl (3D scenes)", bool(webgl), webgl or "no WebGL2 context",
                "fx.three scenes need WebGL; headless Chromium uses SwiftShader (software). Re-run /reel-setup to reinstall the browser.")
        except Exception as e:  # noqa: BLE001
            add("chromium launch", False, f"{type(e).__name__}: {str(e)[:120]}",
                "The browser is installed but will not start; re-run /reel-setup or restart the PC.")

    # models
    models = home / "models"
    rvm = sorted((models / "rvm").glob("*.onnx")) if (models / "rvm").exists() else []
    add("model: background matte (RVM)", bool(rvm), rvm[0].name if rvm else "missing",
        "Run /reel-setup to download the background-removal model.")
    # face detector chain (mediapipe -> yunet -> haar): ok when any backend works
    from . import facedet
    if args.quick:
        st = facedet.read_state()
        if st is None:
            add("face detector", True, "not self-tested yet (run `veos doctor` for the full check)")
        else:
            add("face detector", bool(st.get("backend")), f"{st.get('backend')} (cached self-test)" if st.get("backend")
                else "no backend works", "No face detector works; run `veos doctor`, then re-run /reel-setup.")
    else:
        st = facedet.run_selftests()
        det = "; ".join(f"{n}: {'ok' if r['ok'] else 'FAILED ' + r['detail']}" for n, r in st["results"].items())
        add("face detector", bool(st["backend"]), f"active: {st['backend']} ({det})" if st["backend"] else det,
            "No face detector works; re-run /reel-setup (downloads the models and repairs the packages).")
    hf = Path(os.environ.get("HF_HOME", models / "hf"))
    wh = sorted((hf / "hub").glob("models--*faster-whisper-large-v3-turbo*")) if (hf / "hub").exists() else []
    wok = any(list(p.glob("snapshots/*/model.bin")) for p in wh)
    add("model: speech-to-text (whisper turbo)", wok, wh[0].name if wok else "missing",
        "Run /reel-setup to download the transcription model (about 1.6 GB).")

    # speaker labels for multi-speaker reels (E-13): local ONNX models, no account or token
    from . import diarize
    dp = diarize.model_paths(fetch=False)
    have = [k for k, v in dp.items() if v.exists()]
    add("model: speaker labels (diarisation)", len(have) == 2,
        f"pyannote segmentation-3.0 + CAM++ ({sum(diarize.MODELS_MB.values()):.0f} MB) in {dp['embedding'].parent}"
        if len(have) == 2 else f"missing: {', '.join(k for k in dp if k not in have)}",
        "Run /vibe-editing-os:setup update to download the speaker-label models (~34 MB; needed for conversation "
        "clips with two or more people).")

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
    return {"status": status, "ready": not problems, "licence": f"licence: {lic_line}", "licence_ok": lic_ok,
            "machine_ready": all(c["ok"] for c in checks if c["name"] != "licence"), "machine": machine, "home": str(home), "checks": checks,
            "problems": problems, "quick": bool(args.quick)}


def add_args(p, cmd: str) -> None:
    p.add_argument("--quick", action="store_true", help="fast file-presence check only (no launches); for a SessionStart hook")
