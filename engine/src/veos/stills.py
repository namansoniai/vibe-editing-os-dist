"""`veos stills`: review stills of a reel's scenes, at the moments the scenes themselves declare (what was coded).

    veos stills --project P                  every scene's key moments -> review/stills/sheet_NN.jpg + stills.json
    veos stills --project P --scenes a,b     only these scenes' moments (the re-check after a fix)
    veos stills --project P --at 4.9,14.9    exactly these moments (edit seconds)

Moments per scene, from plan/scenes.meta.json (the registered scenes; rebuilt when older than plan/scenes.js):
  * "<id> in":   settled after its entry (t_in + the entry window + 2 f);
  * "<id>@<e>":  every internal event e, EVENT_LAG frames after it (the change is visible, not just starting);
  * "<id> out":  the last calm frame before its exit (t_out - the exit window - 2 f), when that is at least
                 OUT_GAP frames after its previous moment;
plus "first frame" (frame 0: the hook must read on it). Moments of different scenes closer than MERGE frames share one
still (the later frame; every reason kept). Over CAP stills, the merge window doubles until they fit.

The frames render through the real player (the `veos render --test` path) into sheets of COLS x ROWS tiles, TILE_W px
wide (sized so a sheet is read without downscaling), each labelled "#NN fNNN m:ss.s" and the moments it shows.
review/stills/stills.json:
  {"version": 1, "fps", "frames": [{"n", "t", "why": [...], "active": [scene ids on screen], "sheet", "tile"}],
   "sheets": [...]}
The `vibe-editing-os:frame-reviewer` agent reads the sheets against each scene's brief (plan/scene-briefs.md).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path

from .core import FPS, VeosError, need_project, r3, read_json, tools
from .vcommon import enter_frames, exit_frames

EVENT_LAG = 4        # f after an event: the change has happened
SETTLE_PAD = 2       # f after the entry window
OUT_GAP = 6          # f: an "out" still only when the scene has been calm this long since its previous moment
MERGE = 2            # f: moments closer than this share a still
CAP = 60             # stills per run
TILE_W, COLS, ROWS = 300, 5, 2


def add_args(p, cmd):
    p.add_argument("--scenes", default=None, help="comma list of scene ids: only their moments")
    p.add_argument("--at", default=None, help="comma list of edit seconds: exactly these moments")
    p.add_argument("--workers", type=int, default=None, help="parallel browsers (default as `veos render`)")


def _f(t: float) -> int:
    return int(round(float(t) * FPS))


def moments(scenes: list[dict], frames: int) -> list[tuple[int, str]]:
    """[(frame, reason)] for every scene's settle, events and pre-exit, inside its life and the reel."""
    out: list[tuple[int, str]] = []
    for s in scenes:
        sid = s.get("id")
        try:
            a, b = _f(s.get("t_in", 0)), _f(s.get("t_out", 0))
        except (TypeError, ValueError):
            continue
        b = min(b, frames)
        if not sid or b <= a:
            continue
        last = b - 1
        mine = [(min(a + enter_frames(s) + SETTLE_PAD, last), f"{sid} in")]
        for e in s.get("events") or []:
            if isinstance(e, (int, float)) and not isinstance(e, bool):
                mine.append((min(a + _f(e) + EVENT_LAG, last), f"{sid}@{e:g}"))
        mine.sort()
        calm = b - exit_frames(s) - SETTLE_PAD
        if calm - mine[-1][0] >= OUT_GAP:
            mine.append((calm, f"{sid} out"))
        out += [(max(a, min(n, last)), why) for n, why in mine]
    return out


def group(ms: list[tuple[int, str]], window: int) -> list[tuple[int, list[str]]]:
    """Merge moments closer than `window` frames into one still at the run's last frame."""
    runs: list[list[tuple[int, str]]] = []
    for n, why in sorted(ms):
        if runs and n - runs[-1][0][0] < window:
            runs[-1].append((n, why))
        else:
            runs.append([(n, why)])
    out = []
    for r in runs:
        whys = list(dict.fromkeys(w for _, w in r))
        out.append((r[-1][0], whys))
    return out


def pick(scenes: list[dict], frames: int, only: set[str] | None = None, cap: int = CAP) -> list[tuple[int, list[str]]]:
    sel = [s for s in scenes if only is None or s.get("id") in only]
    ms = moments(sel, frames)
    if only is None:
        ms.append((0, "first frame"))
    window = MERGE
    stills = group(ms, window)
    while len(stills) > cap:
        window *= 2
        stills = group(ms, window)
    return stills


def active_at(scenes: list[dict], n: int) -> list[str]:
    t = n / FPS
    return [s["id"] for s in scenes if s.get("id") and float(s.get("t_in", 0)) <= t < float(s.get("t_out", 0))]


def _tc(t: float) -> str:
    return f"{int(t // 60)}:{t % 60:04.1f}"


def _fit(s: str, n: int) -> str:
    return s if len(s) <= n else s[:n - 1].rstrip() + "…"


def main(args, project):
    import numpy as np
    from PIL import Image
    from . import render
    from .look import compose
    from .prep import ensure_bundle
    from .scenes import PLAYER, load_scenes_meta

    pr = need_project(project)
    tlp = pr.root / "plan" / "timeline.json"
    if not tlp.exists():
        raise VeosError("NO_TIMELINE", f"{tlp} not found", "Write plan/timeline.json first.")
    frames = int((read_json(tlp).get("meta") or {}).get("frames") or 0)
    if frames < 1:
        raise VeosError("NO_FRAMES", "timeline meta.frames missing", "Set meta.frames in plan/timeline.json.")
    scenes = load_scenes_meta(pr)
    ids = {s.get("id") for s in scenes}

    if args.at:
        try:
            ts = [float(x) for x in args.at.split(",") if x.strip()]
        except ValueError:
            raise VeosError("BAD_AT", f"--at {args.at!r} is not a list of seconds", "Use e.g. --at 4.9,14.9") from None
        stills = [(min(max(_f(t), 0), frames - 1), [f"at {t:g} s"]) for t in ts[:CAP]]
    else:
        only = None
        if args.scenes:
            only = {x.strip() for x in args.scenes.split(",") if x.strip()}
            unknown = sorted(only - ids)
            if unknown:
                raise VeosError("UNKNOWN_SCENE", f"no registered scene {', '.join(unknown)}",
                                "Use ids from plan/scenes.meta.json (`veos scenes-meta`).")
        stills = pick(scenes, frames, only)
    if not stills:
        raise VeosError("NO_STILLS", "no moments to show (no scenes, or none inside the reel)", "Check plan/scenes.js.")

    warnings: list[str] = []
    url = ensure_bundle(pr, warnings)
    scratch = tools().scratch / "stills" / hashlib.sha1(str(pr.root).encode("utf-8")).hexdigest()[:12]
    shutil.rmtree(scratch, ignore_errors=True)
    scratch.mkdir(parents=True)
    want = sorted({n for n, _ in stills})
    ns = argparse.Namespace(html=str(PLAYER), frames=frames, test=",".join(map(str, want)), range=None,
                            workers=args.workers, out=str(scratch), size="1080x1920", query=["bundle=" + url],
                            preset="medium", crf="14")
    out_dir = pr.root / "review" / "stills"
    out_dir.mkdir(parents=True, exist_ok=True)
    for old in out_dir.glob("sheet_*.jpg"):
        old.unlink()
    th = round(TILE_W * 1920 / 1080)
    per = COLS * ROWS
    try:
        res = render._render(ns, pr)
        tiles, rows = [], []
        for i, (n, why) in enumerate(stills):
            png = scratch / f"t_{n:04d}.png"
            if not png.exists():
                raise VeosError("RENDER_FAILED", f"frame {n} did not render", "See logs/render.log.")
            with Image.open(png) as im:
                img = np.asarray(im.convert("RGB").resize((TILE_W, th), Image.LANCZOS))
            t = n / FPS
            sheet = f"review/stills/sheet_{i // per + 1:02d}.jpg"
            tiles.append({"img": img, "l1": f"#{i + 1:02d} f{n} {_tc(t)}", "l2": _fit(" · ".join(why), 44)})
            rows.append({"n": n, "t": r3(t), "why": why, "active": active_at(scenes, n), "sheet": sheet, "tile": i % per + 1})
        sheets = []
        for k in range(0, len(tiles), per):
            dest = out_dir / f"sheet_{k // per + 1:02d}.jpg"
            compose(tiles[k:k + per], COLS, TILE_W, th, dest, font_size=16)
            sheets.append(pr.rel(dest))
    finally:
        shutil.rmtree(scratch, ignore_errors=True)
    lines = ["{", f' "version": 1, "fps": {FPS},', ' "frames": [']
    lines += ["  " + json.dumps(r, ensure_ascii=False, separators=(",", ":")) + ("," if j < len(rows) - 1 else "")
              for j, r in enumerate(rows)]
    lines += [" ],", f' "sheets": {json.dumps(sheets)}', "}"]
    (out_dir / "stills.json").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    summary = {"stills": len(rows), "sheets": sheets, "file": "review/stills/stills.json",
               "ms_per_frame": res.get("ms_per_frame")}
    if warnings or res.get("warnings"):
        summary["warnings"] = warnings + list(res.get("warnings") or [])
    return summary
