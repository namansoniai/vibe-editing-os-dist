"""`veos prep-frames` and `veos bundle` (renderer CONTRACT section 1).

prep-frames: for each edit frame n of cutmap.json write work/frames/f%05d.jpg (conformed footage frame, JPEG q~90)
and work/frames/c%05d.webp (the same frame as RGBA, alpha = luma of work/matte/<id>.mp4), plus work/face.edit.json.
Each ffmpeg job seeks once, decodes src + matte once, and writes both outputs from one filter graph (no per-frame
seeking); jobs run in parallel. Existing frames are skipped.

bundle: writes work/render/bundle.js (`window.VEOS_BUNDLE = {...}`) for renderer/player.html?bundle=<file URL>.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from .core import FPS, VeosError, need_project, r3, read_json, run, tools, write_json

REPO = Path(__file__).resolve().parents[3]
W, H = 1080, 1920
CHUNK = 60
JPEG_Q = "3"      # mjpeg qscale 3 ~ libjpeg quality 90
WEBP_Q = "88"


def add_args(p, cmd):
    if cmd == "prep-frames":
        p.add_argument("--range", nargs=2, type=int, metavar=("A", "B"), help="only edit frames A..B-1")
        p.add_argument("--workers", type=int, default=None, help="parallel ffmpeg jobs (default min(8, cpus//2))")
        p.add_argument("--force", action="store_true", help="re-create frames that already exist")
    else:
        p.add_argument("--timeline", help="timeline file (default <project>/plan/timeline.json)")
        p.add_argument("--out", metavar="DIR", help="folder for bundle.js (default <project>/work/render)")


# ------------------------------------------------------------------ prep-frames
def _dims(ffprobe: str, path: Path) -> tuple[int, int]:
    r = subprocess.run([ffprobe, "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height",
                        "-of", "csv=p=0:s=x", str(path)], capture_output=True, text=True)
    try:
        w, h = r.stdout.strip().split("x")[:2]
        return int(w), int(h)
    except ValueError:
        return W, H


def _cover(sw: int, sh: int) -> tuple[float, float, float]:
    """scale + crop offsets mapping source pixels to the 1080x1920 output (cover)."""
    s = max(W / sw, H / sh)
    return s, (W - sw * s) / 2, (H - sh * s) / 2


def _job(ff: str, d: dict) -> dict:
    t0 = time.perf_counter()
    cover = f"scale={W}:{H}:force_original_aspect_ratio=increase:flags=bicubic,crop={W}:{H}"
    seek = max(0.0, (d["in_frame"] - 0.5) / FPS)
    vf = (f"[0:v]scale={W}:{H}:force_original_aspect_ratio=increase:flags=bicubic:in_color_matrix=bt709:in_range=tv,"
          f"crop={W}:{H},format=rgb24,split[a][b];"
          f"[1:v]{cover},format=gray{d['alpha_fix']}[m];"
          f"[b]format=gbrp[bg];[bg][m]alphamerge,format=bgra[c]")
    cmd = [ff, "-y", "-v", "error", "-ss", f"{seek:.5f}", "-i", d["src"], "-ss", f"{seek:.5f}", "-i", d["matte"],
           "-filter_complex", vf,
           "-map", "[a]", "-frames:v", str(d["count"]), "-q:v", JPEG_Q, "-start_number", str(d["n0"]),
           str(Path(d["dir"]) / "f%05d.jpg"),
           "-map", "[c]", "-frames:v", str(d["count"]), "-c:v", "libwebp", "-quality", WEBP_Q, "-compression_level", "2",
           "-start_number", str(d["n0"]), str(Path(d["dir"]) / "c%05d.webp")]
    r = subprocess.run(cmd, capture_output=True)
    err = r.stderr.decode("utf-8", "replace").strip()
    return {"d": d, "rc": r.returncode, "err": err[-600:], "s": time.perf_counter() - t0}


def _alpha_fix(ffmpeg: str, matte: Path) -> str:
    """Detect a limited-range matte (min~16, max~235) from one mid frame; return the extra filter to expand it."""
    try:
        r = subprocess.run([ffmpeg, "-v", "error", "-i", str(matte), "-vf", "select=eq(n\\,30)+eq(n\\,60),format=gray",
                            "-frames:v", "2", "-f", "rawvideo", "-"], capture_output=True)
        b = r.stdout
        if len(b) < 1000:
            return ""
        import numpy as np
        a = np.frombuffer(b, np.uint8)
        lo, hi = int(a.min()), int(a.max())
        if lo >= 10 and hi <= 240:
            return ",lutyuv=y='clip((val-16)*255/219,0,255)'"
    except Exception:  # noqa: BLE001
        pass
    return ""


def _prep(args, project):
    pr = need_project(project)
    t = tools()
    cm_path = pr.work / "cutmap.json"
    if not cm_path.exists():
        raise VeosError("NO_CUTMAP", "work/cutmap.json missing", "Run `veos cut` first.")
    cm = read_json(cm_path)
    n_total = int(cm["frames"])
    a, b = (args.range if args.range else (0, n_total))
    a, b = max(0, a), min(n_total, b)
    fdir = pr.work / "frames"
    fdir.mkdir(parents=True, exist_ok=True)
    t0 = time.perf_counter()
    warnings: list[str] = []

    jobs, skipped = [], 0
    fix_cache: dict[str, str] = {}
    for seg in cm["segments"]:
        sid = seg["src"]
        src, matte = pr.work / "src" / f"{sid}.mp4", pr.work / "matte" / f"{sid}.mp4"
        for pth in (src, matte):
            if not pth.exists():
                raise VeosError("INPUT_MISSING", f"missing {pr.rel(pth)}", "Run `veos conform` and `veos matte` first.")
        if sid not in fix_cache:
            fix_cache[sid] = _alpha_fix(t.ffmpeg, matte)
            if fix_cache[sid]:
                warnings.append(f"matte {sid} looks limited-range; expanding (v-16)/219")
        lo, hi = max(seg["f0"], a), min(seg["f1"], b)
        n = lo
        while n < hi:
            have = (not args.force) and (fdir / f"f{n:05d}.jpg").exists() and (fdir / f"c{n:05d}.webp").exists() \
                and (fdir / f"f{n:05d}.jpg").stat().st_size > 2000 and (fdir / f"c{n:05d}.webp").stat().st_size > 200
            if have:
                skipped += 1
                n += 1
                continue
            m = n
            while m < hi and m - n < CHUNK and not (not args.force and (fdir / f"f{m:05d}.jpg").exists()
                                                    and (fdir / f"c{m:05d}.webp").exists()):
                m += 1
            jobs.append({"src": str(src), "matte": str(matte), "in_frame": seg["in_frame"] + (n - seg["f0"]),
                         "n0": n, "count": m - n, "dir": str(fdir), "alpha_fix": fix_cache[sid]})
            n = m

    workers = args.workers or min(8, max(1, (os.cpu_count() or 2) // 2))
    done, failed = 0, []
    if jobs:
        with ThreadPoolExecutor(max_workers=workers) as ex:
            for res in ex.map(lambda d: _job(t.ffmpeg, d), jobs):
                if res["rc"] != 0:
                    failed.append(f"frames {res['d']['n0']}+{res['d']['count']}: {res['err']}")
                else:
                    done += res["d"]["count"]
                pr.log("prep-frames", f"job n0={res['d']['n0']} count={res['d']['count']} rc={res['rc']} {res['s']:.1f}s {res['err']}")
    if failed:
        raise VeosError("PREP_FAILED", "; ".join(failed[:3]), "See logs/prep-frames.log; re-run to resume (cached frames are skipped).")

    # verify every wanted frame exists
    missing = [n for n in range(a, b) if not (fdir / f"f{n:05d}.jpg").exists() or not (fdir / f"c{n:05d}.webp").exists()]
    if missing:
        raise VeosError("PREP_INCOMPLETE", f"{len(missing)} frames missing (first {missing[0]})",
                        "Source/matte may be shorter than the cutmap says; re-run `veos prep-frames`.")

    face = _face_edit(pr, cm, t.ffprobe)
    secs = time.perf_counter() - t0
    mb = sum(f.stat().st_size for f in fdir.iterdir() if f.suffix in (".jpg", ".webp")) / 1e6
    return {"frames": b - a, "written": done, "cached": skipped, "jobs": len(jobs), "workers": workers,
            "mb_total": r3(mb), "seconds": r3(secs), "ms_per_frame_written": r3(1000 * secs / max(done, 1)),
            "face": face, "frames_dir": pr.rel(fdir), "warnings": warnings}


def _face_edit(pr, cm, ffprobe) -> dict:
    boxes = [None] * int(cm["frames"])
    cache, dims, found = {}, {}, 0
    for seg in cm["segments"]:
        sid = seg["src"]
        if sid not in cache:
            fp = pr.work / "face" / f"{sid}.json"
            cache[sid] = read_json(fp)["boxes"] if fp.exists() else []
            dims[sid] = _dims(ffprobe, pr.work / "src" / f"{sid}.mp4")
        sw, sh = dims[sid]
        s, ox, oy = _cover(sw, sh)
        for n in range(seg["f0"], seg["f1"]):
            i = seg["in_frame"] + (n - seg["f0"])
            bx = cache[sid][i] if 0 <= i < len(cache[sid]) else None
            if bx:
                x, y, w, h = bx[:4]
                boxes[n] = [round(x * s + ox, 1), round(y * s + oy, 1), round(w * s, 1), round(h * s, 1),
                            bx[4] if len(bx) > 4 else 1.0]
                found += 1
    out = {"version": 1, "fps": FPS, "size": [W, H], "frames": len(boxes), "boxes": boxes}
    write_json(pr.work / "face.edit.json", out, indent=None)
    return {"file": "work/face.edit.json", "with_box": found, "of": len(boxes)}


# ------------------------------------------------------------------ bundle
def _resolve_asset(pr, src: str) -> Path | None:
    p = Path(src)
    for cand in ([p] if p.is_absolute() else [pr.root / p, REPO / p]):
        if cand.exists():
            return cand
    return None


ASSET_EXT = {".png": "image", ".jpg": "image", ".jpeg": "image", ".webp": "image", ".svg": "image", ".gif": "image",
             ".avif": "image"}


def check_scenes_js(pr) -> Path:
    """plan/scenes.js must exist and parse (`node --check`). Raises VeosError with the node message."""
    sj = pr.root / "plan" / "scenes.js"
    if not sj.exists():
        raise VeosError("SCENES_MISSING", f"{sj} not found",
                        "Write plan/scenes.js (VEOS.scene({...}) calls); see renderer/SCENES-API.md.")
    node = shutil.which("node")
    if node:
        r = subprocess.run([node, "--check", str(sj)], capture_output=True, text=True)
        if r.returncode:
            lines = [l for l in r.stderr.strip().splitlines() if l.strip()]
            raise VeosError("SCENES_SYNTAX", "plan/scenes.js has a syntax error: " + " | ".join(lines[:5])[:600],
                            "Fix the syntax error (line shown above) and re-run.")
    return sj


def _bundle(args, project):
    pr = need_project(project)
    tl_path = Path(args.timeline) if args.timeline else pr.root / "plan" / "timeline.json"
    if not tl_path.exists():
        raise VeosError("NO_TIMELINE", f"{tl_path} missing", "Write plan/timeline.json first.")
    tl = read_json(tl_path)
    tokens_p = pr.work / "tokens.json"
    if not tokens_p.exists():
        raise VeosError("NO_TOKENS", "work/tokens.json missing", "Run `veos tokens --project P` first.")
    sj = check_scenes_js(pr)
    inp = tl.get("inputs") or {}
    words_p, face_p = pr.abs(inp.get("words") or "work/words.edit.json"), pr.abs(inp.get("face") or "work/face.edit.json")
    cut_p = pr.abs(inp.get("cutmap") or "work/cutmap.json")
    frames_dir = pr.abs(inp.get("frames") or "work/frames/")
    words = read_json(words_p).get("words", []) if words_p.exists() else []
    face = read_json(face_p) if face_p.exists() else None
    cut = read_json(cut_p) if cut_p.exists() else {}
    frames = int((tl.get("meta") or {}).get("frames") or cut.get("frames") or 0)
    warnings = []

    assets = {}
    adir = pr.root / "plan" / "assets"
    if adir.is_dir():  # plan/assets/<file>: addressable as ctx.asset("<stem>") and ctx.asset("<file name>")
        for f in sorted(adir.rglob("*")):
            if f.is_file():
                a = {"type": ASSET_EXT.get(f.suffix.lower(), "file"), "url": f.resolve().as_uri()}
                assets.setdefault(f.stem, a)
                assets[f.name] = a
    for aid, a in (tl.get("assets") or {}).items():
        f = _resolve_asset(pr, a.get("src", ""))
        if not f:
            warnings.append(f"asset '{aid}': file not found ({a.get('src')})")
            continue
        assets[aid] = {"type": a.get("type", "image"), "url": f.resolve().as_uri()}

    frames_url = frames_dir.resolve().as_uri().rstrip("/") + "/"
    bundle = {"timeline": tl, "tokens": read_json(tokens_p), "words": words, "face": face, "frames_url": frames_url,
              "frames": frames, "cuts": [s["f0"] for s in cut.get("segments", [])[1:]],
              "scenes": [sj.resolve().as_uri()], "assets": assets}
    if getattr(args, "out", None):
        out = Path(args.out).expanduser().resolve() / "bundle.js"
        out.parent.mkdir(parents=True, exist_ok=True)
    else:
        out = pr.path("work", "render", "bundle.js")
    out.write_text("window.VEOS_BUNDLE = " + json.dumps(bundle, ensure_ascii=False) + ";\n", encoding="utf-8")
    return {"out": pr.rel(out), "url": out.resolve().as_uri(), "frames": frames, "scenes_js": pr.rel(sj),
            "assets": len(assets), "bytes": out.stat().st_size, "warnings": warnings}


def ensure_bundle(pr) -> str:
    """Rebuild the bundle (cheap) and return its file URL; runs `veos tokens` first when work/tokens.json is missing."""
    from argparse import Namespace
    if not (pr.work / "tokens.json").exists():
        from . import tokens
        tokens.main(Namespace(playbook=None), pr)
    return _bundle(Namespace(timeline=None, out=None), pr)["url"]


def main(args, project):
    return _prep(args, project) if args.cmd == "prep-frames" else _bundle(args, project)
