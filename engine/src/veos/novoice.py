"""No-voice reels: B-roll + music + on-screen text, a screen recording + text, photos/slides + music.

Nobody speaks, so the cut follows the music instead of the words. The rest of the pipeline is the normal one:

- `veos project init <folder|files> --no-voice [--music F] [--script F]` -> project.json `source_type: "no_voice"`
  (also chosen when every picture given is a photo, or the playbook's `profile.source_type` is `no_voice`).
- `veos ingest` (no-voice project): clips are B-roll / screen recordings (never a talking head); photos and slides
  (jpg, png, webp, bmp, tif; heic when ffmpeg can decode it) become sources of kind `still`: the image (EXIF rotation
  applied) is held in a short silent 30 fps clip `work/stills/<id>.mp4`, so every reader (the cut proxy, `look --src`,
  conform, prep-frames, the renderer's footage and camera moves) treats it like any other clip. The music is source `M`
  (kind `music`; `M2`... for more): project.json `music`, else the audio-only files given.
- `veos beats` (beats.py) -> work/beats.json, the music's beat map.
- `veos cut <edl.json> [--snap-beats [beats|bars]] [--snap-tol 0.3] [--audio music|clips|none]` -> the usual cutmap,
  an empty words.edit.json (no speech), the cut's sound as work/voice.wav (the music trimmed / looped / faded to the
  cut, the clips' own sound, or silence) and the proxy with that sound. EDL extras (see `normalise_edl`):
  `{"src": "S3", "still": true, "dur": 2.5, "fit": "auto|cover|contain|blur"}` holds a photo; `"snap": false` keeps a
  segment's end off the beat grid; top-level `"audio"`, `"music": {"src": "M", "in": 12.0, "fade_out": 1.0}` and
  `"free_order": true` (screen-recording segments otherwise play in their recorded order).
- `veos voice` writes the same bed; `veos mix` treats its input as a bed (no voice chain, no SFX-under-voice gate,
  the same -14 LUFS master); `veos qa` skips the voice sync check; `veos context` lists the beats in edit time.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np

from .core import FPS, VeosError, r3, read_json, run, tools, write_json

NO_VOICE = "no_voice"
STILL_KIND = "still"
MUSIC_KIND = "music"
NO_PICTURE_KINDS = ("voiceover", "audio-only", MUSIC_KIND)
STILL_EXT = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tif", ".tiff", ".heic", ".heif"}
STILL_HOLD_S = 12.0          # a photo's clip length at ingest (grown on demand when the cut holds it longer)
STILL_DEFAULT_S = 2.5        # a photo's hold when the EDL gives no `dur`
STILL_MAX_PX = 2560          # long side of a photo kept at its own aspect (cover): room for camera push-ins
CANVAS = (1080, 1920)
FITS = ("auto", "cover", "contain", "blur")
COVER_KEEP = 0.8             # auto: cover when the 9:16 crop keeps >= 80 % of the photo both ways, else blur
AUDIO_MODES = ("music", "clips", "none")
SNAP_TOL_S = 0.3
MIN_SEG_F = 6                # snapping never makes a segment shorter than 0.2 s
FADE_OUT_S = 1.0
FADE_IN_S = 0.01
LOOP_XFADE_S = 0.05
SR = 48000
ENCODE = ["-c:v", "libx264", "-crf", "16", "-preset", "veryfast", "-tune", "stillimage", "-pix_fmt", "yuv420p",
          "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709", "-color_range", "tv"]


# ------------------------------------------------------------------ project type
def is_still(path: str | Path) -> bool:
    return Path(path).suffix.lower() in STILL_EXT


def source_type(pr) -> str | None:
    """sources.json `source_type`, else project.json's."""
    for f in (pr.work / "sources.json", pr.root / "project.json"):
        if f.exists():
            try:
                st = read_json(f).get("source_type")
            except (ValueError, OSError):
                continue
            if st:
                return st
    return None


def is_no_voice(pr) -> bool:
    return pr is not None and source_type(pr) == NO_VOICE


# ------------------------------------------------------------------ stills
def _open_image(f: Path, scratch: Path):
    """A PIL RGB image with the EXIF rotation applied; HEIC (or anything PIL can't read) goes through ffmpeg first."""
    from PIL import Image, ImageOps
    try:
        im = Image.open(f)
        im.load()
    except Exception:  # noqa: BLE001 - not a format PIL reads (heic): let ffmpeg decode it
        png = scratch / f"{f.stem}.decoded.png"
        r = run([tools().ffmpeg, "-v", "error", "-y", "-i", str(f), "-frames:v", "1", str(png)], check=False)
        if r.returncode != 0 or not png.exists():
            raise VeosError("STILL_DECODE_FAILED", f"can't read the photo {f.name}",
                            "Save it as JPG or PNG (HEIC needs a newer video tool) and run ingest again.")
        im = Image.open(png)
        im.load()
    im = ImageOps.exif_transpose(im)
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        bg = Image.new("RGB", im.size, (16, 16, 16))
        bg.paste(im, mask=im.split()[-1])
        im = bg
    return im.convert("RGB")


def auto_fit(w: int, h: int) -> str:
    a, t = w / h, CANVAS[0] / CANVAS[1]
    keep = t / a if a > t else a / t
    return "cover" if keep >= COVER_KEEP else "blur"


def _still_picture(im, fit: str):
    """The picture the still clip holds: the photo itself (cover; the 9:16 crop happens later like any clip) or the
    photo whole on a 1080x1920 canvas (contain: dark; blur: a blurred, dimmed fill of itself)."""
    from PIL import Image, ImageEnhance, ImageFilter
    w, h = im.size
    if fit == "cover":
        s = min(1.0, STILL_MAX_PX / max(w, h))
        nw, nh = max(2, int(round(w * s / 2)) * 2), max(2, int(round(h * s / 2)) * 2)
        return im.resize((nw, nh), Image.LANCZOS) if (nw, nh) != (w, h) else im
    W, H = CANVAS
    if fit == "blur":
        c = max(W / w, H / h)
        bg = im.resize((max(1, round(w * c)), max(1, round(h * c))), Image.LANCZOS)
        x0, y0 = (bg.width - W) // 2, (bg.height - H) // 2
        bg = bg.crop((x0, y0, x0 + W, y0 + H)).filter(ImageFilter.GaussianBlur(48))
        canvas = ImageEnhance.Brightness(bg).enhance(0.55)
    else:
        canvas = Image.new("RGB", (W, H), (16, 16, 16))
    s = min(W / w, H / h)
    fg = im.resize((max(1, round(w * s)), max(1, round(h * s))), Image.LANCZOS)
    canvas.paste(fg, ((W - fg.width) // 2, (H - fg.height) // 2))
    return canvas


def make_still_clip(image: Path, out: Path, hold: float, fit: str) -> dict:
    """Write the silent 30 fps clip that holds `image` for `hold` seconds; returns {width, height, fit, frames, size}."""
    out.parent.mkdir(parents=True, exist_ok=True)
    im = _open_image(image, out.parent)
    fit_used = auto_fit(*im.size) if fit in (None, "auto") else fit
    pic = _still_picture(im, fit_used)
    png = out.with_suffix(".png")
    pic.save(png)
    n = max(1, int(round(hold * FPS)))
    tmp = out.with_suffix(".tmp.mp4")
    run([tools().ffmpeg, "-v", "error", "-y", "-loop", "1", "-framerate", str(FPS), "-i", str(png),
         "-vf", "scale=out_color_matrix=bt709:out_range=tv,format=yuv420p", "-frames:v", str(n), "-r", str(FPS),
         *ENCODE, "-movflags", "+faststart", str(tmp)])
    tmp.replace(out)
    return {"width": pic.width, "height": pic.height, "fit": fit_used, "frames": n, "image_size": list(im.size)}


def still_source(f: Path, sid: str, proj, fit: str = "auto", hold: float = STILL_HOLD_S) -> dict:
    """A sources.json entry for a photo / slide: kind `still`, path = its held clip work/stills/<id>.mp4."""
    clip = proj.path("work", "stills", f"{sid}.mp4")
    info = make_still_clip(f, clip, hold, fit)
    dur = r3(info["frames"] / FPS)
    return {"id": sid, "path": proj.rel(clip), "image": proj.rel(f), "kind": STILL_KIND, "duration": dur,
            "frames": info["frames"], "width": info["width"], "height": info["height"], "rotation": 0,
            "fps_in": f"{FPS}/1", "vfr": False, "audio": None,
            "segments": [{"start": 0.0, "end": dur, "setup": "other"}], "face_ratio": 0.0,
            "fit": info["fit"], "fit_asked": fit or "auto", "image_size": info["image_size"],
            "notes": [f"photo held as a clip ({info['fit']})"]}


def ensure_still(proj, s: dict, need_s: float, fit: str | None) -> bool:
    """Grow a still's clip to hold at least `need_s` seconds and/or re-make it with another fit. True when re-made
    (its conformed copy is dropped, so the next reader converts the new picture)."""
    want_fit = fit or s.get("fit_asked") or "auto"
    resolved = auto_fit(*s["image_size"]) if want_fit == "auto" and s.get("image_size") else want_fit
    long_enough = float(s.get("duration") or 0) >= need_s - 1e-6
    if long_enough and resolved == s.get("fit"):
        return False
    hold = max(float(s.get("duration") or 0), need_s + 1.0, STILL_HOLD_S)
    new = still_source(proj.abs(s["image"]), s["id"], proj, want_fit, hold)
    s.clear()
    s.update(new)
    (proj.work / "src" / f"{new['id']}.mp4").unlink(missing_ok=True)
    return True


# ------------------------------------------------------------------ music
def music_source(f: Path, sid: str, proj) -> dict:
    from . import media
    from .ingest import _best_audio
    pr = media.probe(f)
    notes: list[str] = []
    audio = _best_audio(f, pr, notes)
    if audio is None:
        raise VeosError("MUSIC_NO_AUDIO", f"{f.name} has no sound", "Give the music as an audio file (mp3, wav, m4a).")
    if audio["lufs"] is None:
        notes.append("the music file is silent")
    adur = max((a["duration"] for a in pr["audio"]), default=0.0) or pr["duration"]
    if pr["video"] is not None:
        notes.append("video file: only its sound is used (picture ignored)")
    return {"id": sid, "path": proj.rel(f), "kind": MUSIC_KIND, "duration": r3(adur), "frames": int(round(adur * FPS)),
            "audio": audio, "picture_ignored": pr["video"] is not None, "segments": [], "face_ratio": 0.0, "notes": notes}


def music_id(k: int) -> str:
    return "M" if k == 0 else f"M{k + 1}"


def pick_music(files: list[Path], declared=None) -> list[Path]:
    """The music file(s): project.json `music` when set, else the audio-only files given."""
    from .media import AUDIO_EXT
    if declared:
        want = [Path(d).expanduser().resolve() for d in ([declared] if isinstance(declared, str) else declared)]
        return [f for f in files if f in want] or [w for w in want if w.exists()]
    return [f for f in files if f.suffix.lower() in AUDIO_EXT]


# ------------------------------------------------------------------ the EDL
def _bad(code: str, msg: str, hint: str):
    return VeosError(code, msg, hint)


def normalise_edl(edl: dict, sources: dict[str, dict]) -> tuple[dict, list[str], dict[str, tuple[float, str | None]]]:
    """Resolve photos (`still` / `dur` / `fit`) to in/out and put screen-recording segments back in recorded order.

    Returns (edl copy, notes, {still id: (longest hold, fit)})."""
    segs = edl.get("segments")
    if not isinstance(segs, list) or not segs:
        raise _bad("EDL_EMPTY", "the EDL has no segments", "Add at least one segment {src, in, out} or {src, still, dur}.")
    out, notes, needs = [], [], {}
    for k, sg in enumerate(segs):
        sg = dict(sg)
        sid = sg.get("src")
        s = sources.get(sid)
        if s is None:
            raise _bad("EDL_BAD_SRC", f"segment {k}: unknown source '{sid}'", f"Known ids: {', '.join(sources)}.")
        if s.get("kind") in NO_PICTURE_KINDS:
            raise _bad("EDL_BAD_SRC", f"segment {k}: '{sid}' is {s.get('kind')} (no picture)",
                       "The music plays under the cut (EDL `music`); segments are clips and photos.")
        if s.get("kind") == STILL_KIND:
            if sg.get("dur") is not None:
                d = float(sg["dur"])
            elif sg.get("in") is not None and sg.get("out") is not None:
                d = float(sg["out"]) - float(sg["in"])
            else:
                d = STILL_DEFAULT_S
            if d < 1.0 / FPS:
                raise _bad("EDL_BAD_RANGE", f"segment {k}: a photo needs a hold of at least one frame (dur {d})",
                           "Give `dur` in seconds, e.g. 2.5.")
            fit = sg.get("fit")
            if fit is not None and fit not in FITS:
                raise _bad("EDL_BAD_FIT", f"segment {k}: fit '{fit}' is not one of {', '.join(FITS)}", "Use auto, cover, contain or blur.")
            prev = needs.get(sid)
            if prev and fit and prev[1] and prev[1] != fit:
                notes.append(f"{sid} is used with two fits; the clip uses '{prev[1]}'")
                fit = prev[1]
            needs[sid] = (max(d, prev[0] if prev else 0.0), (prev[1] if prev and prev[1] else fit))
            sg.update({"in": 0.0, "out": r3(d), "still": True})
        else:
            if sg.get("still"):
                raise _bad("EDL_BAD_SEGMENT", f"segment {k}: '{sid}' is a video clip, not a photo",
                           "Give `in` and `out` for a clip; `still`/`dur` are for photos and slides.")
            if sg.get("in") is None or sg.get("out") is None:
                raise _bad("EDL_BAD_RANGE", f"segment {k}: a clip segment needs `in` and `out` (source seconds)",
                           "Add them, e.g. {\"src\": \"S1\", \"in\": 2.0, \"out\": 4.5}.")
        out.append(sg)
    if not edl.get("free_order"):
        for sid in sorted({sg["src"] for sg in out if sources[sg["src"]].get("kind") == "screen-recording"}):
            idx = [i for i, sg in enumerate(out) if sg["src"] == sid]
            ordered = sorted((out[i] for i in idx), key=lambda sg: float(sg["in"]))
            if [id(x) for x in ordered] != [id(out[i]) for i in idx]:
                for i, sg in zip(idx, ordered):
                    out[i] = sg
                notes.append(f"screen recording {sid}: its segments play in recorded order (set \"free_order\": true to reorder)")
    return {**edl, "segments": out}, notes, needs


def audio_spec(edl: dict, mode: str | None, sources: dict[str, dict]) -> dict:
    """The cut's sound: {mode, src, in, fade_in, fade_out, loop_len, duration} (music) or {mode} (clips / none)."""
    musics = [s for s in sources.values() if s.get("kind") == MUSIC_KIND]
    m = edl.get("music") or {}
    mode = mode or edl.get("audio") or ("music" if musics else "clips")
    if mode not in AUDIO_MODES:
        raise _bad("BAD_AUDIO", f"audio '{mode}' is not one of {', '.join(AUDIO_MODES)}", "Use music, clips or none.")
    if mode != "music":
        return {"mode": mode}
    if not musics:
        raise _bad("NO_MUSIC", "this cut wants music but the project has none",
                   "Add it: `veos project init ... --no-voice --music <file> --force` and ingest again, or cut with "
                   "--audio clips.")
    src = m.get("src") or musics[0]["id"]
    s = sources.get(src)
    if not s or s.get("kind") != MUSIC_KIND:
        raise _bad("EDL_BAD_SRC", f"music '{src}' is not a music source", f"Music ids: {', '.join(x['id'] for x in musics)}.")
    t_in = float(m.get("in") or 0.0)
    dur = float(s.get("duration") or 0.0)
    if not 0 <= t_in < dur - 0.5:
        raise _bad("EDL_BAD_RANGE", f"music in ({t_in}) is outside the track (0-{dur:.1f}s)", "Pick a start inside the track.")
    return {"mode": "music", "src": src, "in": r3(t_in), "fade_in": r3(float(m.get("fade_in", FADE_IN_S))),
            "fade_out": r3(float(m.get("fade_out", FADE_OUT_S))), "loop_len": r3(dur - t_in), "duration": r3(dur)}


def snap_edl(edl: dict, targets: list[float], tol: float, sources: dict[str, dict]) -> tuple[dict, dict]:
    """Move each segment's end (edit time) onto the nearest target (beat or bar) within `tol` seconds, by trimming or
    extending that segment (a photo's hold, a clip's out point when the clip has the frames). In frames, so the cut
    lands exactly on the grid. Returns (edl, report)."""
    tf = sorted({int(round(t * FPS)) for t in targets})
    tol_f = int(round(tol * FPS))
    F, moved, ends, out = 0, [], [], []
    for k, sg in enumerate(edl["segments"]):
        sg = dict(sg)
        s = sources[sg["src"]]
        i0 = int(round(float(sg["in"]) * FPS))
        n = int(round(float(sg["out"]) * FPS)) - i0
        total = int(s.get("frames") or round(float(s["duration"]) * FPS))
        end = F + n
        if sg.get("snap", True) and tf:
            room_up = 10 ** 9 if s.get("kind") == STILL_KIND else total - (i0 + n)
            cands = sorted((t for t in tf if abs(t - end) <= tol_f), key=lambda t: abs(t - end))
            for t in cands:
                d = t - end
                if n + d >= MIN_SEG_F and d <= room_up:
                    n += d
                    if d:
                        moved.append([k, r3(d / FPS)])
                    break
        sg["in"] = r3(i0 / FPS)
        sg["out"] = r3((i0 + n) / FPS)
        if s.get("kind") == STILL_KIND:
            sg["dur"] = sg["out"]
        out.append(sg)
        F += n
        ends.append(F)
    grid = set(tf)
    off = [k for k, e in enumerate(ends) if e not in grid]
    rep = {"moved": len(moved), "on_grid": len(ends) - len(off), "of": len(ends), "shifts": moved[:12], "off_grid": off}
    return {**edl, "segments": out}, rep


def identity_edl(src_list: list[dict]) -> dict:
    """Every picture source in order: clips whole, photos held STILL_DEFAULT_S."""
    segs = []
    for s in src_list:
        if s.get("kind") in NO_PICTURE_KINDS:
            continue
        if s.get("kind") == STILL_KIND:
            segs.append({"src": s["id"], "still": True, "dur": STILL_DEFAULT_S, "note": "photo"})
        else:
            segs.append({"src": s["id"], "in": 0.0, "out": r3(float(s["duration"])), "note": "whole clip"})
    if not segs:
        raise _bad("NO_PICTURE", "no clips or photos to cut", "Ingest the clips / photos first.")
    return {"version": 1, "fps": FPS, "auto": "identity", "segments": segs}


# ------------------------------------------------------------------ the cut's sound
def _music_samples(pr, s: dict) -> np.ndarray:
    from .audio import decode_mono
    wav = pr.work / "audio" / f"{s['id']}.wav"
    return decode_mono(wav if wav.exists() else pr.abs(s["path"]), SR)


def music_bed(y: np.ndarray, n: int, t_in: float, fade_in: float, fade_out: float) -> tuple[np.ndarray, bool]:
    """`n` samples of music from `t_in`, looped (with a short crossfade) when the track runs out, faded in / out."""
    seg = y[int(round(t_in * SR)):].astype(np.float32)
    looped = False
    if len(seg) == 0:
        return np.zeros(n, np.float32), False
    out = seg[:n].copy()
    x = int(LOOP_XFADE_S * SR)
    while len(out) < n:
        looped = True
        nxt = seg[: n - len(out) + x].copy()
        k = min(x, len(out), len(nxt))
        if k > 0:
            ramp = np.linspace(0.0, 1.0, k, dtype=np.float32)
            out[-k:] = out[-k:] * (1 - ramp) + nxt[:k] * ramp
        out = np.concatenate([out, nxt[k:]])
    out = out[:n]
    fi, fo = min(n, int(fade_in * SR)), min(n // 3, int(fade_out * SR))
    if fi > 0:
        out[:fi] *= np.linspace(0.0, 1.0, fi, dtype=np.float32)
    if fo > 0:
        out[-fo:] *= np.linspace(1.0, 0.0, fo, dtype=np.float32) ** 2
    return out, looped


def build_bed(pr, cutmap: dict, sources: dict[str, dict] | None = None) -> tuple[np.ndarray, dict]:
    """The cut's sound (mono 48 kHz): its music bed, the clips' own sound, or silence (cutmap `audio`)."""
    from .voice import _load, assemble
    if sources is None:
        sources = {s["id"]: s for s in read_json(pr.work / "sources.json").get("sources") or []}
    spec = cutmap.get("audio") or {"mode": "clips"}
    n = int(round(float(cutmap["duration"]) * SR))
    info = {"mode": spec["mode"]}
    if spec["mode"] == "music":
        y = _music_samples(pr, sources[spec["src"]])
        x, looped = music_bed(y, n, float(spec.get("in") or 0), float(spec.get("fade_in", FADE_IN_S)),
                              float(spec.get("fade_out", FADE_OUT_S)))
        info.update(src=spec["src"], music_in=spec.get("in"), looped=looped)
        return x, info
    if spec["mode"] == "none":
        return np.zeros(n, np.float32), info
    cache: dict = {}

    def load(sid):
        s = sources.get(sid) or {}
        if not s.get("audio"):
            return np.zeros(1, np.float32)
        return _load(pr, sid, cache)
    return assemble(cutmap, load), info


# ------------------------------------------------------------------ cut
def _read_edl(args, proj) -> dict:
    if not args.edl:
        raise VeosError("EDL_MISSING", "no EDL given", "Pass the path to edl.json, or --identity to keep every clip whole.")
    p = Path(args.edl)
    if not p.is_absolute() and not p.exists() and (proj.root / args.edl).exists():
        p = proj.root / args.edl
    if not p.exists():
        raise VeosError("EDL_MISSING", f"EDL not found: {args.edl}", "Pass the path to edl.json.")
    try:
        return read_json(p)
    except ValueError:
        doc = Path(p).read_text(encoding="utf-8-sig")  # a byte-order mark from a Windows editor
        import json
        return json.loads(doc)


def _swap_audio(proxy: Path, wav: Path, proj) -> None:
    tmp = proxy.with_suffix(".tmp.mp4")
    run([tools().ffmpeg, "-v", "error", "-y", "-i", str(proxy), "-i", str(wav), "-map", "0:v", "-map", "1:a",
         "-c:v", "copy", "-c:a", "aac", "-b:a", "128k", "-shortest", "-movflags", "+faststart", str(tmp)], proj, "cut")
    tmp.replace(proxy)


def cut_main(args, proj) -> dict:
    """`veos cut` for a no-voice project (cut.main hands over here)."""
    from . import cut as C
    from .beats import edit_map
    from .voice import write_wav
    sp = proj.work / "sources.json"
    sdoc = read_json(sp)
    src_list = sdoc["sources"]
    sources = {s["id"]: s for s in src_list}
    if getattr(args, "identity", False):
        edl = identity_edl(src_list)
        write_json(proj.path("work", "edl.json"), edl)
    else:
        edl = _read_edl(args, proj)
    edl, notes, needs = normalise_edl(edl, sources)
    remade = [sid for sid, (d, fit) in needs.items() if ensure_still(proj, sources[sid], d, fit)]
    if remade:
        write_json(sp, sdoc)
    spec = audio_spec(edl, getattr(args, "audio", None), sources)
    snap_rep = None
    warnings: list[str] = list(notes)
    snap = getattr(args, "snap_beats", None)
    if snap:
        bp = proj.work / "beats.json"
        if not bp.exists():
            raise VeosError("NO_BEATS", "work/beats.json not found", "Run `veos beats` first (it maps the music).")
        doc = read_json(bp)
        est = sum(float(sg["out"]) - float(sg["in"]) for sg in edl["segments"]) + float(args.snap_tol) + 2.0
        em = edit_map(doc, spec, est)
        if not em["mapped"]:
            warnings.append("the beat map is not of this cut's music: nothing snapped (run `veos beats` again)")
        else:
            edl, snap_rep = snap_edl(edl, em["downbeats" if snap == "bars" else "beats"], float(args.snap_tol), sources)
            snap_rep["to"] = snap
    write_json(proj.path("work", "edl.cut.json"), edl)
    cutmap, w2 = C.build_cutmap(edl, sources, proj)
    warnings += w2
    cutmap["audio"] = spec
    stills = {sid: {"fit": sources[sid].get("fit"), "frames": sources[sid].get("frames")}
              for sid in sorted({sg["src"] for sg in cutmap["segments"]}) if sources[sid].get("kind") == STILL_KIND}
    if stills:
        cutmap["stills"] = stills  # a re-made photo changes the cut map, so prep-frames drops its old frames
    write_json(proj.path("work", "cutmap.json"), cutmap)
    write_json(proj.path("work", "words.edit.json"),
               {"version": 1, "source": "edit", "model": None, "language": None, "words": [], "silences": [],
                "note": "no-voice reel: no speech"})
    bed, binfo = build_bed(proj, cutmap, sources)
    vw = proj.path("work", "voice.wav")
    write_wav(vw, bed)
    used = {sg["src"] for sg in cutmap["segments"]}
    removed = sum(max(0.0, float(sources[i]["duration"]) - sum(g["f1"] - g["f0"] for g in cutmap["segments"]
                                                             if g["src"] == i) / FPS)
                  for i in used if sources[i].get("kind") != STILL_KIND)
    summary = {"source_type": NO_VOICE, "duration": cutmap["duration"], "frames": cutmap["frames"],
               "segments": len(cutmap["segments"]), "removed_s": r3(removed), "words_remapped": 0,
               "audio": {k: v for k, v in binfo.items()}, "edl_cut": "work/edl.cut.json", "voice": proj.rel(vw)}
    if edl.get("auto"):
        summary["edl"] = {"auto": edl["auto"], "file": "work/edl.json"}
    if snap_rep:
        summary["snapped"] = snap_rep
    if remade:
        summary["stills_remade"] = remade
    if (proj.work / "beats.json").exists():
        em = edit_map(read_json(proj.work / "beats.json"), spec, cutmap["duration"])
        if em["mapped"]:
            summary["beats_in_cut"] = len(em["beats"])
            summary["cuts_on_beat"] = _on_grid(cutmap, em["beats"])
    if not args.no_proxy:
        proxy = proj.path("work", "cut_proxy.mp4")
        C.render_proxy(cutmap, sources, proj, proxy)
        if binfo["mode"] != "clips":
            _swap_audio(proxy, vw, proj)
        got = C._proxy_frames(proxy)
        if got != cutmap["frames"]:
            raise VeosError("FRAME_MISMATCH", f"proxy has {got} frames, cutmap says {cutmap['frames']}",
                            "This is a bug in the proxy render; do not use this cut. See logs/cut.log.")
        summary["proxy"] = proj.rel(proxy)
        summary["proxy_frames"] = got
    summary["warnings"] = warnings
    return summary


def _on_grid(cutmap: dict, beats: list[float]) -> str:
    """How many cut points (segment starts after the first) sit on a beat (within one frame)."""
    bf = {int(round(b * FPS)) for b in beats}
    cuts = [g["f0"] for g in cutmap["segments"][1:]]
    on = sum(1 for f in cuts if any(abs(f - b) <= 1 for b in bf))
    return f"{on}/{len(cuts)}"


# ------------------------------------------------------------------ context
def context_part(pr, cut: dict | None) -> dict:
    """What `veos context` shows of the music for a no-voice reel: tempo, beats / bars / sections / hits in edit time
    (or music time before the cut), and the energy per bar."""
    bp = pr.work / "beats.json"
    if not bp.exists():
        return {"note": "no beat map yet: run `veos beats`"}
    from .beats import edit_map
    doc = read_json(bp)
    out = {"tempo": doc.get("tempo"), "beat_period": doc.get("beat_period"), "meter": doc.get("meter"),
           "downbeat_confidence": doc.get("downbeat_confidence")}
    if cut:
        em = edit_map(doc, cut.get("audio"), float(cut["duration"]))
        if em["mapped"]:
            out.update(time="edit", beats=em["beats"], bars=em["downbeats"], sections=em["sections"], hits=em["hits"])
            shift = float((cut.get("audio") or {}).get("in") or 0.0) if doc.get("time") == "music" else 0.0
            be = doc.get("bar_energy") or []
            downs = doc.get("downbeats") or []
            out["bar_energy"] = [[r3(t - shift), e] for t, e in zip(downs, be) if 0 <= t - shift <= float(cut["duration"])]
            out["note"] = ("edit seconds; bars = bar starts (beat 1); sections = where the music changes (up = it gets "
                           "bigger, down = it drops away); hits = the strongest accents; bar_energy 0..1")
            return out
        out["note"] = "the beat map is not of this cut's sound (another track, or no music): run `veos beats` again"
    out.update(time=doc.get("time"), beats=doc.get("beats"), bars=doc.get("downbeats"), sections=doc.get("sections"),
               hits=doc.get("hits"), bar_energy=doc.get("bar_energy"))
    out.setdefault("note", f"{doc.get('time')} seconds (no cut yet); music `in` shifts them into the cut")
    return out
