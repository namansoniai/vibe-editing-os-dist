"""`veos scenes-meta` and `veos measure` (renderer CONTRACT v2): inspect plan/scenes.js in the real player.

scenes-meta: load the player headless (`?meta=1`, registration only), read every registered scene's metadata (all fields
except `render`) -> plan/scenes.meta.json (a list). Registration errors are reported with the scene id.

measure: render sampled frames headless (no screenshots) and record, per active scene, the union bounding rect
(1080x1920 px, resting position: enter/exit presets neutralised) of its painted DOM -> plan/measure.json
{"every": N, "frames": {"<n>": {"<scene id>": [x0, y0, x1, y1]}}}. Canvas-only scenes fall back to their declared box.
"""
from __future__ import annotations

import json
import time
from pathlib import Path

from .core import FPS, VeosError, need_project, read_json, write_json
from .prep import check_scenes_js, ensure_bundle

REPO = Path(__file__).resolve().parents[3]
PLAYER = REPO / "renderer" / "player.html"


def add_args(p, cmd):
    if cmd == "measure":
        p.add_argument("--every", type=int, default=10, help="sample every N-th frame (default 10)")
        p.add_argument("--range", nargs=2, type=int, metavar=("A", "B"), help="only frames A..B-1")


def _chrome_args() -> list[str]:
    from .render import CHROME_ARGS
    return CHROME_ARGS


def _open(url_bundle: str, extra: str = ""):
    from .core import tools
    tools()  # sets PLAYWRIGHT_BROWSERS_PATH
    from playwright.sync_api import sync_playwright
    pw = sync_playwright().start()
    br = pw.chromium.launch(headless=True, args=_chrome_args())
    pg = br.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=1)
    logs: list[str] = []
    pg.on("console", lambda m: logs.append(m.text) if m.type in ("error", "warning") else None)
    pg.on("pageerror", lambda e: logs.append(f"pageerror: {e}"))
    pg.goto(PLAYER.resolve().as_uri() + "?bundle=" + url_bundle + extra)
    pg.wait_for_function("window.READY===true || !!window.VEOS_BOOT_ERROR", timeout=90000)
    return pw, br, pg, logs


def scenes_meta(pr) -> dict:
    """Run the headless registration pass and write plan/scenes.meta.json. Raises VeosError listing broken scenes."""
    check_scenes_js(pr)
    url = ensure_bundle(pr)
    pw, br, pg, logs = _open(url, "&meta=1")
    try:
        boot = pg.evaluate("window.VEOS_BOOT_ERROR || null")
        meta = pg.evaluate("window.VEOS_SCENES_META || []")
        errs = pg.evaluate("window.VEOS_REG_ERRORS || []")
    finally:
        br.close()
        pw.stop()
    if boot:
        raise VeosError("SCENES_BOOT", "player failed to load: " + str(boot)[:800], "Check work/tokens.json and the bundle.")
    if errs:
        raise VeosError("SCENES_INVALID", "scenes.js has problems: " + " | ".join(errs)[:1500],
                        "Fix the listed scene(s) in plan/scenes.js (each message starts with the scene id).")
    if not meta:
        raise VeosError("NO_SCENES", "plan/scenes.js registered no scenes", "Call VEOS.scene({...}) at least once.")
    dest = pr.path("plan", "scenes.meta.json")
    write_json(dest, meta)
    return {"file": pr.rel(dest), "scenes": len(meta), "ids": [m.get("id") for m in meta]}


def load_scenes_meta(pr, auto: bool = True) -> list[dict]:
    """plan/scenes.meta.json, regenerated first when missing or older than plan/scenes.js (when `auto`)."""
    mp, sj = pr.root / "plan" / "scenes.meta.json", pr.root / "plan" / "scenes.js"
    if auto and sj.exists() and (not mp.exists() or mp.stat().st_mtime < sj.stat().st_mtime):
        scenes_meta(pr)
    if not mp.exists():
        raise VeosError("NO_SCENES", f"{mp} not found and no plan/scenes.js to build it from",
                        "Write plan/scenes.js, then run `veos scenes-meta --project P`.")
    data = read_json(mp)
    if not isinstance(data, list):
        raise VeosError("BAD_SCENES_META", "scenes.meta.json must be a list of scene objects", "Re-run `veos scenes-meta`.")
    return data


def measure(pr, every: int, rng: tuple[int, int] | None) -> dict:
    check_scenes_js(pr)
    url = ensure_bundle(pr)
    tl = read_json(pr.root / "plan" / "timeline.json")
    frames = int((tl.get("meta") or {}).get("frames") or 0)
    if frames < 1:
        raise VeosError("NO_FRAMES", "timeline meta.frames missing", "Set meta.frames in plan/timeline.json.")
    a, b = rng if rng else (0, frames)
    every = max(1, every)
    ns = sorted({n for n in range(a, min(b, frames), every)} | ({frames - 1} if not rng else set()))
    out: dict[str, dict] = {}
    t0 = time.perf_counter()
    pw, br, pg, logs = _open(url)
    try:
        boot = pg.evaluate("window.VEOS_BOOT_ERROR || null")
        if boot:
            raise VeosError("SCENES_BOOT", "player failed to load: " + str(boot)[:1200],
                            "Fix plan/scenes.js (run `veos scenes-meta` for per-scene errors).")
        for n in ns:
            try:
                out[str(n)] = pg.evaluate("n => window.measureFrame(n)", n)
            except Exception as e:  # noqa: BLE001
                msg = str(e).splitlines()[0][:400]
                raise VeosError("SCENE_RENDER_FAILED", f"frame {n}: {msg}", "Fix the scene named in the message.") from None
    finally:
        br.close()
        pw.stop()
    data = {"version": 1, "every": every, "size": [1080, 1920], "fps": FPS, "frames": out}
    write_json(pr.path("plan", "measure.json"), data, indent=None)
    seen = sorted({sid for f in out.values() for sid in f})
    return {"file": "plan/measure.json", "frames_sampled": len(ns), "scenes_seen": seen,
            "ms_per_frame": round(1000 * (time.perf_counter() - t0) / max(len(ns), 1), 1)}


def main(args, project):
    pr = need_project(project)
    if args.cmd == "scenes-meta":
        return scenes_meta(pr)
    return measure(pr, args.every, tuple(args.range) if args.range else None)
