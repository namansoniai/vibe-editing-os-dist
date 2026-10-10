"""veos conform: constant-30-fps H.264 working copies + mono 48 kHz wav per source.

Three modes:
  `--audio-only`   before the cut (prep): only work/audio/<id>.wav, nothing visual. The frame count the conformed copy
                   will have is computed from the clip's timeline (rawsrc.grid, exact) and stored as `frames`, so the
                   rough cut, the cut map and the review proxy (built straight from the original, rawsrc) use the same
                   frame indices as before.
  default          with a cut map (after the cut): only the frames the cut keeps (+ the faces / cut-out margins,
                   matte.kept_ranges) are converted at full quality; the rest of work/src/<id>.mp4 is black, so every
                   reader keeps indexing it by the cut map's source frame exactly as before. Sources the cut doesn't use
                   get no video. A full conform made earlier (older projects, conversation reels) is kept as it is.
                   Without a cut map: every frame, as always.
  `--all`          every frame of every video source, cut map or not.
`ensure(project, sid)` runs whichever is needed before a command reads work/src/<id>.mp4.
"""
from __future__ import annotations

import time
from pathlib import Path

from . import media, rawsrc
from .core import FPS, VeosError, filter_complex_args, need_project, r3, read_json, run, tools, write_json

BT601 = rawsrc.BT601
ENCODE = ["-c:v", "libx264", "-crf", "16", "-preset", "veryfast", "-pix_fmt", "yuv420p",
          "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709", "-color_range", "tv"]


def add_args(p, cmd):
    p.add_argument("--id", default=None, help="conform only this source id")
    p.add_argument("--force", action="store_true", help="redo even if outputs are up to date")
    p.add_argument("--audio-only", action="store_true",
                   help="before the cut: only the sound (work/audio/<id>.wav) and the frame count; no video")
    p.add_argument("--all", action="store_true", help="every frame of every video source, even when a cut map exists")


def _fresh(out: Path, src: Path) -> bool:
    return out.exists() and out.stat().st_size > 0 and out.stat().st_mtime >= src.stat().st_mtime


def _count_frames(path: Path) -> int:
    r = run([tools().ffprobe, "-v", "error", "-count_packets", "-select_streams", "v:0",
             "-show_entries", "stream=nb_read_packets", "-of", "csv=p=0", str(path)])
    return int(r.stdout.decode().strip().split(",")[0])


def _colorspace(path: Path) -> str:
    r = run([tools().ffprobe, "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=color_space",
             "-of", "csv=p=0", str(path)], check=False)
    return r.stdout.decode().strip()


def video_mode(s: dict, proj) -> str | None:
    """'full' (every frame converted, also older projects), 'kept' (the cut's ranges) or None (no video yet)."""
    c = s.get("conformed")
    if c is None:  # nothing recorded (made by hand or by an old engine): a file there is a full copy
        return "full" if (proj.work / "src" / f"{s.get('id')}.mp4").exists() else None
    vid = proj.abs(c["video"]) if c.get("video") else None
    if vid is None or not vid.exists():
        return None
    return c.get("mode") or "full"


def _covers(done: list, want: list) -> bool:
    return all(any(a >= x and b <= y for x, y in done) for a, b in want)


def _full_video(proj, src: Path, vid: Path, pr: dict, a_idx: int) -> None:
    ff = tools().ffmpeg
    vf = [f"fps={FPS}"]
    if _colorspace(src) in BT601:
        vf.append("scale=in_color_matrix=bt601:out_color_matrix=bt709:out_range=tv")
    cmd = [ff, "-v", "error", "-y", "-i", str(src), "-map", "0:v:0", "-vf", ",".join(vf), "-fps_mode", "cfr", *ENCODE]
    if pr["audio"]:
        a = pr["audio"][a_idx]
        cmd += ["-map", f"0:a:{a_idx}", "-c:a", "copy" if a["codec"] == "aac" else "aac", "-b:a", "192k"]
    tmp = vid.with_suffix(".tmp.mp4")
    cmd += ["-movflags", "+faststart", str(tmp)]
    run(cmd, proj, "conform")
    tmp.replace(vid)


def _kept_video(proj, g: rawsrc.Grid, vid: Path, ranges: list[list[int]], total: int) -> None:
    """work/src/<id>.mp4 with `total` frames: the grid frames of `ranges` from the original, black elsewhere."""
    ff = tools().ffmpeg
    inputs: list[str] = []
    parts, labels, f, k = [], [], 0, 0
    pieces: list[tuple[str, int, int]] = []
    for a, b in ranges:
        if a > f:
            pieces.append(("gap", f, a - f))
        pieces.append(("keep", a, b - a))
        f = b
    if total > f:
        pieces.append(("gap", f, total - f))
    for kind, a, n in pieces:
        if kind == "keep":
            pre, ch = rawsrc.chain(g, a, n)
            inputs += [*pre, "-i", str(g.path)]
            # exactly n frames even at the very end of the clip (the last one repeats if the clip runs short)
            parts.append(f"[{k}:v]{ch},setpts=PTS-STARTPTS,setsar=1,format=yuv420p,"
                         f"tpad=stop_mode=clone:stop={n},trim=end_frame={n}[p{len(labels)}]")
            k += 1
        else:
            parts.append(f"color=c=black:s={g.width}x{g.height}:r={FPS},trim=end_frame={n},setpts=PTS-STARTPTS,"
                         f"setsar=1,format=yuv420p[p{len(labels)}]")
        labels.append(f"[p{len(labels)}]")
    parts.append("".join(labels) + f"concat=n={len(labels)}:v=1:a=0[v]")
    script = proj.path("work", "conform_filter.txt")
    script.write_text(";\n".join(parts), encoding="utf-8")
    tmp = vid.with_suffix(".tmp.mp4")
    cmd = [ff, "-v", "error", "-y", *inputs, *filter_complex_args(script, ff), "-map", "[v]", "-fps_mode", "cfr",
           "-r", str(FPS), *ENCODE, "-movflags", "+faststart", str(tmp)]
    run(cmd, proj, "conform")
    got = _count_frames(tmp)
    if got != total:
        raise VeosError("FRAME_MISMATCH", f"{vid.name}: {got} frames, expected {total}",
                        "This is a bug in the kept-range conform; see logs/conform.log.")
    tmp.replace(vid)


def _wanted(proj, sid: str, frames: int) -> list[list[int]] | None:
    """The frame ranges the cut keeps for `sid` (faces / cut-out margins included); None without a cut map."""
    cp = proj.work / "cutmap.json"
    if not cp.exists():
        return None
    from .matte import kept_ranges
    return kept_ranges(read_json(cp), sid, frames)


def conform_source(proj, s: dict, *, audio_only: bool = False, every: bool = False, force: bool = False) -> dict:
    """Conform one sources.json entry in place; returns its summary row."""
    t0 = time.time()
    src = proj.abs(s["path"])
    if not src.exists():
        raise VeosError("SOURCE_MISSING", f"source file not found: {src}", "Move it back or re-run `veos ingest`.")
    pr = media.probe(src)
    v = pr["video"]
    if s.get("kind") in ("voiceover", "music"):  # a voice-over / music track: only its sound is used (picture ignored)
        v = None
    vid = proj.path("work", "src", f"{s['id']}.mp4")
    wav = proj.path("work", "audio", f"{s['id']}.wav")
    a_idx = (s.get("audio") or {}).get("stream", 0)
    notes = [n for n in s.get("notes", []) if not n.startswith("conform:")]
    old = dict(s.get("conformed") or {})
    status: list[str] = []
    info: dict = {"fps": FPS}
    if v is not None:
        g = rawsrc.grid(src)
        frames = g.frames
        mode = video_mode(s, proj)
        fresh = _fresh(vid, src)
        if audio_only:
            info.update(video=proj.rel(vid) if mode else None, frames=frames, mode=mode or "audio")
            if mode == "kept":
                info["ranges"] = old.get("ranges") or []
            status.append("video later (after the cut)" if not mode else "video kept")
        else:
            want = None if every else _wanted(proj, s["id"], frames)
            if want is None or mode == "full" and fresh and not force:
                if not force and mode == "full" and fresh:
                    status.append("video cached")
                else:
                    _full_video(proj, src, vid, pr, a_idx)
                    status.append("video done")
                frames = _count_frames(vid)
                info.update(video=proj.rel(vid), frames=frames, mode="full")
            elif not want:  # the cut keeps nothing of this source: no picture needed
                info.update(video=None, frames=frames, mode="audio")
                status.append("video skipped (not in the cut)")
            else:
                if not force and mode == "kept" and fresh and _covers(old.get("ranges") or [], want) \
                        and old.get("frames") == frames:
                    status.append("video cached")
                    want = old.get("ranges")
                else:
                    _kept_video(proj, g, vid, want, frames)
                    status.append(f"video done ({sum(b - a for a, b in want)} of {frames} frames)")
                info.update(video=proj.rel(vid), frames=frames, mode="kept", ranges=want)
        s["frames"] = info["frames"]
        s["duration"] = r3(info["frames"] / FPS)
    if pr["audio"]:
        if not force and _fresh(wav, src):
            status.append("audio cached")
        else:
            if len(pr["audio"]) > 1:
                notes.append(f"conform: used audio stream {a_idx} of {len(pr['audio'])} (loudest non-silent)")
            tmp = wav.with_suffix(".tmp.wav")
            run([tools().ffmpeg, "-v", "error", "-y", "-i", str(src), "-map", f"0:a:{a_idx}", "-ac", "1", "-ar", "48000",
                 "-c:a", "pcm_s16le", "-f", "wav", str(tmp)], proj, "conform")
            tmp.replace(wav)
            status.append("audio done")
        info["audio"] = proj.rel(wav)
    if s.get("kind") == "voiceover" and wav.exists():  # the voice-over's timeline length is its conformed audio
        import wave
        with wave.open(str(wav), "rb") as w:
            adur = w.getnframes() / float(w.getframerate())
        s["duration"] = r3(adur)
        s["frames"] = int(round(adur * FPS))
        info["frames"] = s["frames"]
    s["conformed"] = info
    s["notes"] = notes
    cached = all("cached" in x or "later" in x or "kept" == x.split()[-1] for x in status) and bool(status)
    row = {"id": s["id"], "frames": info.get("frames"), "fps": FPS, "lufs": (s.get("audio") or {}).get("lufs"),
           "video": info.get("mode"), "status": "cached" if cached else ", ".join(status), "s": round(time.time() - t0, 1)}
    if not pr["audio"]:
        row["warning"] = f"{s['id']}: no audio stream"
    return row


def ensure(project, sid: str, every: bool = False) -> dict | None:
    """Make work/src/<sid>.mp4 readable for the frames the cut keeps (every frame without a cut map, or with `every`)
    before a command decodes it. Returns the conform row when something was done, None when it already was."""
    proj = need_project(project)
    sp = proj.work / "sources.json"
    if not sp.exists():
        return None
    data = read_json(sp)
    s = next((x for x in data.get("sources") or [] if x.get("id") == sid), None)
    if s is None or s.get("kind") in ("voiceover", "audio-only", "session", "music"):  # no picture, or sync's session proxy
        return None
    src = proj.abs(s["path"]) if s.get("path") else None
    if src is None or not src.exists():  # nothing to convert from: the reader reports what is missing
        return None
    mode = video_mode(s, proj)
    if mode == "full" and _fresh(proj.abs((s.get("conformed") or {}).get("video") or f"work/src/{sid}.mp4"), src):
        return None
    if mode == "kept" and not every:
        want = _wanted(proj, sid, int(s.get("frames") or 0))
        if want is not None and _covers((s.get("conformed") or {}).get("ranges") or [], want):
            return None
    row = conform_source(proj, s, every=every)
    write_json(sp, data)
    return row


def main(args, project) -> dict:
    proj = need_project(project)
    sp = proj.work / "sources.json"
    if not sp.exists():
        raise VeosError("NO_SOURCES", "work/sources.json not found", "Run `veos ingest <files>` first.")
    data = read_json(sp)
    todo = [s for s in data["sources"] if args.id in (None, s["id"])]
    if not todo:
        raise VeosError("NO_SUCH_ID", f"no source with id {args.id}", "See work/sources.json for the ids.")
    if getattr(args, "audio_only", False) and getattr(args, "all", False):
        raise VeosError("BAD_ARGS", "--audio-only and --all exclude each other", "Pick one.")
    out_summary, warnings = [], []
    for s in todo:
        row = conform_source(proj, s, audio_only=getattr(args, "audio_only", False), every=getattr(args, "all", False),
                             force=args.force)
        if row.pop("warning", None):
            warnings.append(f"{s['id']}: no audio stream")
        out_summary.append(row)
        write_json(sp, data)  # per source: a long run that stops halfway keeps what it finished
    return {"sources": out_summary, "warnings": warnings}
