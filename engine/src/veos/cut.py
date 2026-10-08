"""veos cut: EDL (source time) -> cutmap.json, words.edit.json and a 540x960 review proxy.

Voice-over reels (E-12): `veos cut --identity [--tighten]` writes the EDL itself. The cut map is the identity over the
voice-over (edit time = VO time), with the silence before the first word and after the last one trimmed (`--no-trim`
keeps the file exactly). `--tighten` also shortens every pause longer than `--max-pause` (0.35 s) to about 0.12 s, the
same rule the talking-head rough cut uses. The proxy shows a plain dark frame when there is no picture.
"""
from __future__ import annotations

import re
from pathlib import Path

from .core import FPS, VeosError, need_project, r3, read_json, run, tools, write_json

PROXY_W, PROXY_H = 540, 960
GAP_S = 0.150
LEAD_S, TAIL_S = 0.04, 0.08          # cut points: start 0.04 s before a word, end 0.08 s after one (reel-roughcut rule)
VO_KINDS = ("voiceover", "audio-only")


def add_args(p, cmd):
    p.add_argument("edl", nargs="?", default=None, help="path to edl.json (omit with --identity)")
    p.add_argument("--no-proxy", action="store_true", help="skip rendering cut_proxy.mp4")
    p.add_argument("--identity", action="store_true",
                   help="voice-over reels: build the EDL from the voice-over itself (edit time = VO time); writes work/edl.json")
    p.add_argument("--tighten", action="store_true", help="with --identity: shorten pauses longer than --max-pause to ~0.12 s")
    p.add_argument("--max-pause", type=float, default=0.35, help="with --tighten: longest pause kept as is (s, default 0.35)")
    p.add_argument("--no-trim", action="store_true", help="with --identity: keep the silence before the first and after the last word")
    p.add_argument("--end-hold", type=float, default=0.4, help="with --identity: seconds kept after the last word (default 0.4)")


# ---------------------------------------------------------------- identity EDL (voice-over reels)
def identity_edl(sources: list[dict], words: dict[str, list[dict]], *, tighten: bool = False, max_pause: float = 0.35,
                 trim: bool = True, end_hold: float = 0.4) -> dict:
    """EDL covering each voice-over source in order (V, V2, ...). Words are source-time {s, e} per source id.

    Without words (or with trim off and no tighten) a source is kept whole. Leading silence is cut to LEAD_S before the
    first word, trailing silence to `end_hold` after the last word of the last source (TAIL_S for earlier parts).
    """
    vos = [s for s in sources if s.get("kind") in VO_KINDS]
    if not vos:
        raise VeosError("NO_VOICEOVER", "no voice-over source in sources.json",
                        "Run `veos ingest --audio <voice-over>` first (or write the EDL yourself for talking-head clips).")
    segs: list[dict] = []
    for k, s in enumerate(vos):
        dur = float(s.get("duration") or 0.0)
        ws = sorted((w for w in words.get(s["id"], []) if w.get("e", 0) > w.get("s", 0)), key=lambda w: w["s"])
        last_part = k == len(vos) - 1
        if not ws or (not trim and not tighten):
            if tighten and not ws:
                raise VeosError("NO_WORDS", f"--tighten needs the words of {s['id']}", "Run `veos transcribe` first.")
            segs.append({"src": s["id"], "in": 0.0, "out": r3(dur), "note": "voice-over (identity)"})
            continue
        a = max(0.0, ws[0]["s"] - LEAD_S) if trim else 0.0
        b = min(dur, ws[-1]["e"] + (end_hold if last_part else TAIL_S)) if trim else dur
        if not tighten:
            segs.append({"src": s["id"], "in": r3(a), "out": r3(b), "note": "voice-over (identity, ends trimmed)"})
            continue
        cur = a
        for w0, w1 in zip(ws, ws[1:]):
            if w1["s"] - w0["e"] > max_pause:
                end, nxt = w0["e"] + TAIL_S, w1["s"] - LEAD_S
                if end - cur >= 1.0 / FPS and nxt > end:
                    segs.append({"src": s["id"], "in": r3(cur), "out": r3(end), "note": f"pause {w1['s'] - w0['e']:.2f}s tightened"})
                    cur = nxt
        segs.append({"src": s["id"], "in": r3(cur), "out": r3(b), "note": "voice-over"})
    return {"version": 1, "fps": FPS, "auto": "identity" + ("+tighten" if tighten else ""), "segments": segs}


# ---------------------------------------------------------------- cutmap
def build_cutmap(edl: dict, sources: dict, proj) -> tuple[dict, list[str]]:
    """Validate the EDL and snap to frames. `sources` maps id -> sources.json entry."""
    warnings: list[str] = []
    segs = edl.get("segments")
    if not isinstance(segs, list) or not segs:
        raise VeosError("EDL_EMPTY", "the EDL has no segments", "Add at least one segment {src, in, out}.")
    out, f = [], 0
    for k, sg in enumerate(segs):
        sid = sg.get("src")
        if sid not in sources:
            raise VeosError("EDL_BAD_SRC", f"segment {k}: unknown source '{sid}'",
                            f"Known ids: {', '.join(sources)}.")
        s = sources[sid]
        a, b = float(sg["in"]), float(sg["out"])
        if not a < b:
            raise VeosError("EDL_BAD_RANGE", f"segment {k}: in ({a}) must be before out ({b})", "Fix the times in the EDL.")
        if a < 0:
            raise VeosError("EDL_BAD_RANGE", f"segment {k}: in is negative ({a})", "Times are source seconds from 0.")
        total = s.get("frames") or int(round(s["duration"] * FPS))
        i0, i1 = int(round(a * FPS)), int(round(b * FPS))
        if i1 > total:
            if i1 - total <= 1:
                warnings.append(f"segment {k}: out clamped to the last frame of {sid}")
                i1 = total
            else:
                raise VeosError("EDL_BAD_RANGE", f"segment {k}: out ({b}s) is past the end of {sid} ({total / FPS:.3f}s)",
                                "Keep times within the source duration.")
        if i1 <= i0:
            raise VeosError("EDL_BAD_RANGE", f"segment {k}: shorter than one frame", "Make the segment at least 1/30 s.")
        n = i1 - i0
        out.append({"t0": r3(f / FPS), "t1": r3((f + n) / FPS), "f0": f, "f1": f + n, "src": sid,
                    "in": r3(a), "in_frame": i0})
        f += n
    return {"version": 1, "fps": FPS, "duration": r3(f / FPS), "frames": f, "segments": out}, warnings


# ---------------------------------------------------------------- words
def remap_words(cutmap: dict, proj) -> dict | None:
    wdir = proj.work / "words"
    if not wdir.exists():
        return None
    cache, words, silences = {}, [], []
    for sg in cutmap["segments"]:
        sid = sg["src"]
        if sid not in cache:
            p = wdir / f"{sid}.json"
            cache[sid] = read_json(p) if p.exists() else None
        wf = cache[sid]
        if wf is None:
            continue
        lo = sg["in_frame"] / FPS
        hi = lo + (sg["f1"] - sg["f0"]) / FPS
        shift = sg["t0"] - lo
        for w in wf.get("words", []):
            dur = max(w["e"] - w["s"], 1e-6)
            inside = min(w["e"], hi) - max(w["s"], lo)
            if inside / dur >= 0.5:
                nw = dict(w)
                nw["si"] = w.get("i")
                nw["src"] = sid
                nw["s"] = r3(max(w["s"], lo) + shift)
                nw["e"] = r3(min(w["e"], hi) + shift)
                words.append(nw)
        for a, b in wf.get("silences", []):
            a2, b2 = max(a, lo), min(b, hi)
            if b2 - a2 > 1e-3:
                silences.append([r3(a2 + shift), r3(b2 + shift)])
    if not words and not any(cache.values()):
        return None
    for i, w in enumerate(words):
        w["i"] = i
    first = next((v for v in cache.values() if v), {})
    return {"version": 1, "source": "edit", "model": first.get("model"), "language": first.get("language"),
            "words": words, "silences": silences}


def gaps_from_words(words: list[dict]) -> list[list[float]]:
    ws = sorted(words, key=lambda w: w["s"])
    return [[r3(a["e"]), r3(b["s"])] for a, b in zip(ws, ws[1:]) if b["s"] - a["e"] >= GAP_S - 1e-9]


# ---------------------------------------------------------------- proxy
def render_proxy(cutmap: dict, sources: dict, proj, out: Path) -> None:
    ids = []
    for sg in cutmap["segments"]:
        if sg["src"] not in ids:
            ids.append(sg["src"])
    inputs, has_audio, picture = [], {}, {}
    for sid in ids:
        c = (sources[sid].get("conformed") or {})
        picture[sid] = sources[sid].get("kind") not in VO_KINDS
        if picture[sid]:
            vp = proj.abs(c["video"]) if c.get("video") else proj.work / "src" / f"{sid}.mp4"
            if not vp.exists():
                raise VeosError("NOT_CONFORMED", f"work/src/{sid}.mp4 is missing", "Run `veos conform` first.")
        else:  # a voice-over has no picture: its conformed audio is the input, the proxy frame is plain
            vp = proj.abs(c["audio"]) if c.get("audio") else proj.work / "audio" / f"{sid}.wav"
            if not vp.exists():
                raise VeosError("NOT_CONFORMED", f"work/audio/{sid}.wav is missing", "Run `veos conform` first.")
        inputs.append(vp)
        has_audio[sid] = bool(sources[sid].get("audio"))
    parts, labels = [], []
    for k, sg in enumerate(cutmap["segments"]):
        j = ids.index(sg["src"])
        a, n = sg["in_frame"], sg["f1"] - sg["f0"]
        d = n / FPS
        if picture[sg["src"]]:
            parts.append(f"[{j}:v]trim=start_frame={a}:end_frame={a + n},setpts=PTS-STARTPTS,fps={FPS},"
                         f"scale={PROXY_W}:{PROXY_H}:force_original_aspect_ratio=decrease,"
                         f"pad={PROXY_W}:{PROXY_H}:(ow-iw)/2:(oh-ih)/2,setsar=1,format=yuv420p[v{k}]")
        else:
            parts.append(f"color=c=0x16161c:s={PROXY_W}x{PROXY_H}:r={FPS},trim=end_frame={n},setpts=PTS-STARTPTS,"
                         f"setsar=1,format=yuv420p[v{k}]")
        if has_audio[sg["src"]]:
            parts.append(f"[{j}:a]atrim=start={a / FPS:.6f}:duration={d:.6f},asetpts=PTS-STARTPTS,"
                         f"aresample=48000,aformat=channel_layouts=stereo,apad=whole_dur={d:.6f},"
                         f"atrim=duration={d:.6f}[a{k}]")
        else:
            parts.append(f"anullsrc=r=48000:cl=stereo,atrim=duration={d:.6f}[a{k}]")
        labels.append(f"[v{k}][a{k}]")
    parts.append("".join(labels) + f"concat=n={len(labels)}:v=1:a=1[v][a]")
    script = proj.path("work", "cut_filter.txt")
    script.write_text(";\n".join(parts), encoding="utf-8")
    cmd = [tools().ffmpeg, "-v", "error", "-y"]
    for p in inputs:
        cmd += ["-i", str(p)]
    cmd += ["-/filter_complex", str(script), "-map", "[v]", "-map", "[a]", "-r", str(FPS),
            "-c:v", "libx264", "-crf", "28", "-preset", "veryfast", "-pix_fmt", "yuv420p",
            "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709",
            "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", str(out)]
    run(cmd, proj, "cut")


def _proxy_frames(path: Path) -> int:
    r = run([tools().ffprobe, "-v", "error", "-count_packets", "-select_streams", "v:0",
             "-show_entries", "stream=nb_read_packets", "-of", "csv=p=0", str(path)])
    return int(r.stdout.decode().strip().split(",")[0])


def gaps_from_audio(path: Path, proj) -> list[list[float]]:
    r = run([tools().ffmpeg, "-hide_banner", "-nostats", "-i", str(path), "-vn", "-af",
             f"silencedetect=noise=-35dB:d={GAP_S}", "-f", "null", "-"], proj, "cut")
    txt = r.stderr.decode("utf-8", "replace")
    starts = [float(x) for x in re.findall(r"silence_start:\s*(-?[\d.]+)", txt)]
    ends = [float(x) for x in re.findall(r"silence_end:\s*(-?[\d.]+)", txt)]
    return [[r3(max(a, 0)), r3(b)] for a, b in zip(starts, ends)]


# ---------------------------------------------------------------- command
def main(args, project) -> dict:
    proj = need_project(project)
    sp = proj.work / "sources.json"
    if not sp.exists():
        raise VeosError("NO_SOURCES", "work/sources.json not found", "Run `veos ingest` and `veos conform` first.")
    src_list = read_json(sp)["sources"]
    if getattr(args, "identity", False):
        wd = {}
        for s in src_list:
            wp = proj.work / "words" / f"{s['id']}.json"
            if wp.exists():
                wd[s["id"]] = read_json(wp).get("words", [])
        edl = identity_edl(src_list, wd, tighten=args.tighten, max_pause=args.max_pause, trim=not args.no_trim,
                           end_hold=args.end_hold)
        write_json(proj.path("work", "edl.json"), edl)
    else:
        if not args.edl:
            raise VeosError("EDL_MISSING", "no EDL given", "Pass the path to edl.json, or --identity for a voice-over reel.")
        edl_path = Path(args.edl)
        if not edl_path.is_absolute() and not edl_path.exists() and (proj.root / args.edl).exists():
            edl_path = proj.root / args.edl
        if not edl_path.exists():
            raise VeosError("EDL_MISSING", f"EDL not found: {args.edl}", "Pass the path to edl.json.")
        edl = read_json(edl_path)
    sources = {s["id"]: s for s in src_list}
    cutmap, warnings = build_cutmap(edl, sources, proj)
    write_json(proj.path("work", "cutmap.json"), cutmap)
    words = remap_words(cutmap, proj)
    if words is not None:
        write_json(proj.path("work", "words.edit.json"), words)
    removed = 0.0
    for sid in {sg["src"] for sg in cutmap["segments"]}:
        used = sum(sg["f1"] - sg["f0"] for sg in cutmap["segments"] if sg["src"] == sid) / FPS
        removed += max(0.0, sources[sid]["duration"] - used)
    summary = {"duration": cutmap["duration"], "frames": cutmap["frames"], "segments": len(cutmap["segments"]),
               "removed_s": r3(removed), "words_remapped": None if words is None else len(words["words"])}
    if edl.get("auto"):
        summary["edl"] = {"auto": edl["auto"], "file": "work/edl.json"}
    if not args.no_proxy:
        proxy = proj.path("work", "cut_proxy.mp4")
        render_proxy(cutmap, sources, proj, proxy)
        got = _proxy_frames(proxy)
        if got != cutmap["frames"]:
            raise VeosError("FRAME_MISMATCH", f"proxy has {got} frames, cutmap says {cutmap['frames']}",
                            "This is a bug in the proxy render; do not use this cut. See logs/cut.log.")
        summary["proxy"] = proj.rel(proxy)
        summary["proxy_frames"] = got
    if words is not None:
        gaps = gaps_from_words(words["words"])
        summary["gaps_source"] = "words"
    elif not args.no_proxy:
        gaps = gaps_from_audio(proxy, proj)
        summary["gaps_source"] = "silencedetect"
    else:
        gaps = None
    if gaps is not None:
        summary["gaps_ge_150ms"] = len(gaps)
        summary["gaps_total_s"] = r3(sum(b - a for a, b in gaps))
        summary["longest_gaps"] = sorted(gaps, key=lambda g: g[0] - g[1])[:5]
    summary["warnings"] = warnings
    return summary
