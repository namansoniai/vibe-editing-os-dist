"""`veos prep-frames` and `veos bundle` (renderer CONTRACT section 1).

prep-frames: for each edit frame n of cutmap.json write work/frames/f%05d.jpg (conformed footage frame, JPEG q~90),
plus work/face.edit.json; and, for a source that has a person cut-out (work/matte/<id>.mp4: `veos matte`, only when
the reel needs it), work/frames/c%05d.webp (the same frame as RGBA, alpha = luma of the matte). Each ffmpeg job seeks
once, decodes src (+ matte) once, and writes its outputs from one filter graph (no per-frame seeking); jobs run in
parallel. Existing frames are skipped, so a re-run after `veos matte` only adds the cut-out frames.
work/frames/frames.json remembers the cut map and the mattes the frames were made from: a new cut drops every frame,
a new matte drops the cut-out frames, so nothing stale is ever reused.

bundle: writes work/render/bundle.js (`window.VEOS_BUNDLE = {...}`) for renderer/player.html?bundle=<file URL>.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
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
        p.add_argument("--workers", type=int, default=None, help="parallel ffmpeg jobs (default min(4, max(1, cpus//4)), or VEOS_WORKERS)")
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
    if not d["matte"]:  # no cut-out for this source: the footage frames only
        vf = (f"[0:v]scale={W}:{H}:force_original_aspect_ratio=increase:flags=bicubic:in_color_matrix=bt709:in_range=tv,"
              f"crop={W}:{H},format=rgb24[a]")
        cmd = [ff, "-y", "-v", "error", "-ss", f"{seek:.5f}", "-i", d["src"], "-filter_complex", vf,
               "-map", "[a]", "-frames:v", str(d["count"]), "-q:v", JPEG_Q, "-start_number", str(d["n0"]),
               str(Path(d["dir"]) / "f%05d.jpg")]
        r = subprocess.run(cmd, capture_output=True)
        err = r.stderr.decode("utf-8", "replace").strip()
        return {"d": d, "rc": r.returncode, "err": err[-600:], "s": time.perf_counter() - t0}
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


def _stamp(pr, cm_path: Path, sids) -> dict:
    """What the frames are made from: the cut map's content and each source's matte (size + time), or None."""
    import hashlib
    mattes = {}
    for sid in sorted(sids):
        m = pr.work / "matte" / f"{sid}.mp4"
        mattes[sid] = [m.stat().st_size, m.stat().st_mtime_ns] if m.exists() else None
    return {"version": 1, "cutmap": hashlib.sha1(cm_path.read_bytes()).hexdigest(), "mattes": mattes}


def _drop_stale(fdir: Path, old: dict | None, new: dict) -> str | None:
    """Delete frames made from another cut (all) or another matte (the cut-out frames); say what was dropped."""
    if not old:
        return None
    if old.get("cutmap") != new["cutmap"]:
        for f in list(fdir.glob("f*.jpg")) + list(fdir.glob("c*.webp")):
            f.unlink(missing_ok=True)
        return "the cut changed since the frames were made: all frames rebuilt"
    changed = [sid for sid, v in new["mattes"].items() if (old.get("mattes") or {}).get(sid) != v and v is not None]
    gone = [sid for sid, v in new["mattes"].items() if v is None and (old.get("mattes") or {}).get(sid)]
    if changed or gone:
        for f in fdir.glob("c*.webp"):
            f.unlink(missing_ok=True)
        return "the person cut-out changed since the frames were made: cut-out frames rebuilt"
    return None


def _prep(args, project):
    pr = need_project(project)
    from . import compose  # multi-camera reels (E-13): frames come from work/multicam/footage.mp4
    if compose.composed_ready(pr):
        return compose.prep_frames(pr, args)
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
    vo_ids = voiceover_ids(pr)
    sids = {seg["src"] for seg in cm["segments"] if seg["src"] not in vo_ids}
    stamp = _stamp(pr, cm_path, sids)
    sp = fdir / "frames.json"
    try:
        old = read_json(sp) if sp.exists() else None
    except ValueError:
        old = None
    dropped = _drop_stale(fdir, old, stamp)
    if dropped:
        warnings.append(dropped)

    def have(n: int, cut: bool) -> bool:
        f, c = fdir / f"f{n:05d}.jpg", fdir / f"c{n:05d}.webp"
        return f.exists() and f.stat().st_size > 2000 and (not cut or (c.exists() and c.stat().st_size > 200))

    jobs, skipped = [], 0
    fix_cache: dict[str, str] = {}
    with_cut: set[str] = set()
    for seg in cm["segments"]:
        sid = seg["src"]
        if sid in vo_ids:  # a voice-over span has no picture: no footage frames, no cut-out (the stage stays hidden)
            continue
        src, matte = pr.work / "src" / f"{sid}.mp4", pr.work / "matte" / f"{sid}.mp4"
        if not src.exists():
            raise VeosError("INPUT_MISSING", f"missing {pr.rel(src)}", "Run `veos conform` first.")
        cut = matte.exists()  # the person cut-out is made only when the reel needs it (`veos matte --if-needed`)
        if cut:
            with_cut.add(sid)
            if sid not in fix_cache:
                fix_cache[sid] = _alpha_fix(t.ffmpeg, matte)
                if fix_cache[sid]:
                    warnings.append(f"matte {sid} looks limited-range; expanding (v-16)/219")
        lo, hi = max(seg["f0"], a), min(seg["f1"], b)
        n = lo
        while n < hi:
            if not args.force and have(n, cut):
                skipped += 1
                n += 1
                continue
            m = n
            while m < hi and m - n < CHUNK and (args.force or not have(m, cut)):
                m += 1
            jobs.append({"src": str(src), "matte": str(matte) if cut else None, "in_frame": seg["in_frame"] + (n - seg["f0"]),
                         "n0": n, "count": m - n, "dir": str(fdir), "alpha_fix": fix_cache.get(sid, "")})
            n = m

    # gentle default so a laptop stays usable during prep; --workers or VEOS_WORKERS raise it
    workers = args.workers or int(os.environ.get("VEOS_WORKERS") or 0) or min(4, max(1, (os.cpu_count() or 2) // 4))
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

    # verify every wanted frame exists (voice-over spans have none; cut-out frames only for sources with a matte)
    vo_frames = {n for seg in cm["segments"] if seg["src"] in vo_ids for n in range(seg["f0"], seg["f1"])}
    cut_frames = {n for seg in cm["segments"] if seg["src"] in with_cut for n in range(seg["f0"], seg["f1"])}
    missing = [n for n in range(a, b) if n not in vo_frames and
               (not (fdir / f"f{n:05d}.jpg").exists() or (n in cut_frames and not (fdir / f"c{n:05d}.webp").exists()))]
    if missing:
        raise VeosError("PREP_INCOMPLETE", f"{len(missing)} frames missing (first {missing[0]})",
                        "Source/matte may be shorter than the cutmap says; re-run `veos prep-frames`.")
    write_json(sp, stamp)

    footage = any(seg["src"] not in vo_ids for seg in cm["segments"])
    face = _face_edit(pr, cm, t.ffprobe) if footage else {"file": None, "with_box": 0, "of": int(cm["frames"]),
                                                          "note": "voice-over reel: no presenter, no face boxes"}
    secs = time.perf_counter() - t0
    mb = sum(f.stat().st_size for f in fdir.iterdir() if f.suffix in (".jpg", ".webp")) / 1e6
    out = {"frames": b - a, "written": done, "cached": skipped, "jobs": len(jobs), "workers": workers,
           "mb_total": r3(mb), "seconds": r3(secs), "ms_per_frame_written": r3(1000 * secs / max(done, 1)),
           "face": face, "frames_dir": pr.rel(fdir), "warnings": warnings,
           "cutout": sorted(with_cut) if with_cut else "none (no matte: footage frames only)"}
    if vo_frames:
        out["voiceover_frames"] = len(vo_frames & set(range(a, b)))
        if not footage:
            out["note"] = "voice-over reel: no footage frames needed (the picture is built from scenes)"
    return out


def voiceover_ids(pr) -> set[str]:
    """Source ids whose picture is not used (voice-over sources; E-12)."""
    sp = pr.work / "sources.json"
    if not sp.exists():
        return set()
    try:
        return {s["id"] for s in read_json(sp).get("sources", []) if s.get("kind") in ("voiceover", "audio-only")}
    except (ValueError, KeyError, TypeError):
        return set()


def has_footage(pr, cut: dict | None) -> bool:
    """True when some edit span shows a source's picture (False for a voice-over reel)."""
    segs = (cut or {}).get("segments") or []
    if not segs:
        return True
    vo = voiceover_ids(pr)
    return any(s.get("src") not in vo for s in segs)


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


NO_GRAPHICS = ("passthrough", "pass", "none")   # profile.graphics values that may ship a plan with zero scenes


def graphics_passthrough(pr) -> bool:
    """True when the project's style draws nothing of its own (profile.graphics passthrough / none, e.g. long-form-recut):
    such a reel may have no plan/scenes.js and zero registered scenes."""
    try:
        from .tokens import load_playbook, project_playbook
        tp = pr.root / "plan" / "timeline.json"
        meta = (read_json(tp).get("meta") or {}) if tp.exists() else {}
        raw = load_playbook(project_playbook(pr, None, meta))
    except Exception:  # noqa: BLE001 - no playbook: fall back to the resolved tokens
        tk = pr.work / "tokens.json"
        try:
            raw = read_json(tk) if tk.exists() else {}
        except ValueError:
            raw = {}
    return str(((raw or {}).get("profile") or {}).get("graphics") or "") in NO_GRAPHICS


def check_scenes_js(pr) -> Path:
    """plan/scenes.js must exist and parse (`node --check`). Raises VeosError with the node message. A passthrough style
    (graphics_passthrough) without one gets an empty plan/scenes.js (zero scenes is a valid plan there)."""
    sj = pr.root / "plan" / "scenes.js"
    if not sj.exists() and graphics_passthrough(pr):
        sj.parent.mkdir(parents=True, exist_ok=True)
        sj.write_text("/* passthrough style (profile.graphics): this reel draws no scenes of its own */\n", encoding="utf-8")
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
    from .tokens import refresh as refresh_tokens
    stale = refresh_tokens(pr)  # the playbook / style copy changed since `veos tokens`: never bundle stale settings
    if stale:
        print(f"veos: warning: {stale}", file=sys.stderr)
    sj = check_scenes_js(pr)
    inp = tl.get("inputs") or {}
    words_p, face_p = pr.abs(inp.get("words") or "work/words.edit.json"), pr.abs(inp.get("face") or "work/face.edit.json")
    cut_p = pr.abs(inp.get("cutmap") or "work/cutmap.json")
    frames_dir = pr.abs(inp.get("frames") or "work/frames/")
    words = read_json(words_p).get("words", []) if words_p.exists() else []
    face = read_json(face_p) if face_p.exists() else None
    cut = read_json(cut_p) if cut_p.exists() else {}
    frames = int((tl.get("meta") or {}).get("frames") or cut.get("frames") or 0)
    warnings = [stale] if stale else []

    assets, videos = {}, {}
    adir = pr.root / "plan" / "assets"
    if adir.is_dir():  # plan/assets/<file>: addressable as ctx.asset("<stem>") and ctx.asset("<file name>")
        for d in sorted(adir.rglob("meta.json")):  # video assets (veos asset add <video>): plan/assets/<name>/f%05d.jpg + meta.json
            try:
                m = read_json(d)
                base = d.parent.resolve().as_uri().rstrip("/") + "/"
                videos[d.parent.name] = {"frames": int(m["frames"]), "fps": m.get("fps", FPS), "w": m.get("w"), "h": m.get("h"),
                                         "duration": m.get("duration"), "base_url": base}
                assets[d.parent.name] = {"type": "video", "url": base + "f00000.jpg"}
            except (ValueError, KeyError, TypeError):
                warnings.append(f"plan/assets/{d.parent.name}/meta.json is not a valid video-asset meta; ignored")
        vdirs = [adir / n for n in videos]
        for f in sorted(adir.rglob("*")):
            if f.is_file() and not any(v in f.parents for v in vdirs):
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
    # E-05 caption engine: chunks rebuilt with the bundle (and written to work/captions.json) so they never go stale
    captions = None
    try:
        from .captions import build_project
        captions = build_project(pr, tl)
        warnings += [f"captions: {w}" for w in captions.get("warnings", [])]
    except Exception as e:  # noqa: BLE001 - the renderer falls back to its built-in auto-subtitles
        warnings.append(f"captions: the caption engine failed ({getattr(e, 'message', e)}); built-in subtitles used")
    # E-08 data contract: resolved plan/figures.json (ctx.fig) and the style's numbers profile (ctx.fmtNum)
    from .figures import for_bundle
    figures, numbers = for_bundle(pr, tl, warnings)
    footage = has_footage(pr, cut)
    if not footage:
        face = None  # no presenter: ctx.face() is null and the stage stays hidden
    tok = read_json(tokens_p)
    # E-16b per-reel base reframe from the template's framing tokens (the renderer, captions and validator share it)
    from .framing import for_reel
    framing = for_reel(tok, tl, (face or {}).get("boxes") if isinstance(face, dict) else face) if footage else None
    if framing and framing.get("capped"):
        warnings.append(f"framing: the face can't reach the template's framing within the {framing['cap']}x punch-in cap "
                        f"(residual {framing['residual_px']} px); the shot list asks for a tighter take")
    # fonts the scenes name (ctx.fitText({family: "Archivo Black"}), inline CSS) beyond the tokens' slots and fonts_extra
    from .tokens import REPO as TREPO, font_entry, referenced_families
    fonts_scenes = {}
    try:
        fj = read_json(TREPO / "assets" / "fonts" / "fonts.json")
        have = {v.get("family") for v in (tok.get("fonts") or {}).values() if isinstance(v, dict)} | set(tok.get("fonts_extra") or {})
        for fam in referenced_families(None, fj, sj.read_text(encoding="utf-8")):
            if fam not in have:
                files = font_entry(fam, fj, warnings)
                if files:
                    fonts_scenes[fam] = files
    except (OSError, ValueError):
        pass
    # Package E: object tracks (plan/tracks/*.json) for scene anchors and ctx.track (renderer/tracks.js)
    from .anchors import for_bundle as tracks_for_bundle
    tracks = tracks_for_bundle(pr, warnings)
    bundle = {"timeline": tl, "tokens": tok, "words": words, "face": face, "frames_url": frames_url, "framing": framing,
              "tracks": tracks,
              "fonts_extra": fonts_scenes,
              "frames": frames, "cuts": [s["f0"] for s in cut.get("segments", [])[1:]] if footage else [],
              "scenes": [sj.resolve().as_uri()], "assets": assets, "videos": videos, "footage": footage, "captions": captions,
              "figures": figures, "numbers": numbers}
    if getattr(args, "out", None):
        out = Path(args.out).expanduser().resolve() / "bundle.js"
        out.parent.mkdir(parents=True, exist_ok=True)
    else:
        out = pr.path("work", "render", "bundle.js")
    out.write_text("window.VEOS_BUNDLE = " + json.dumps(bundle, ensure_ascii=False) + ";\n", encoding="utf-8")
    return {"out": pr.rel(out), "url": out.resolve().as_uri(), "frames": frames, "scenes_js": pr.rel(sj),
            "assets": len(assets), "video_assets": len(videos), "footage": footage, "bytes": out.stat().st_size,
            "warnings": warnings}


def ensure_bundle(pr, warnings: list | None = None) -> str:
    """Rebuild the bundle (cheap) and return its file URL; runs `veos tokens` first when work/tokens.json is missing,
    and again when it is stale (tokens.refresh; the warning line is appended to `warnings`)."""
    from argparse import Namespace
    if not (pr.work / "tokens.json").exists():
        from . import tokens
        tokens.main(Namespace(playbook=None), pr)
    res = _bundle(Namespace(timeline=None, out=None), pr)
    if warnings is not None:
        warnings.extend(w for w in res["warnings"] if w.startswith("work/tokens.json was stale"))
    return res["url"]


def main(args, project):
    return _prep(args, project) if args.cmd == "prep-frames" else _bundle(args, project)
