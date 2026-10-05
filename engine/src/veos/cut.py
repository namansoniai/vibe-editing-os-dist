"""veos cut: EDL (source time) -> cutmap.json, words.edit.json and a 540x960 review proxy."""
from __future__ import annotations

import re
from pathlib import Path

from .core import FPS, VeosError, need_project, r3, read_json, run, tools, write_json

PROXY_W, PROXY_H = 540, 960
GAP_S = 0.150


def add_args(p, cmd):
    p.add_argument("edl", help="path to edl.json")
    p.add_argument("--no-proxy", action="store_true", help="skip rendering cut_proxy.mp4")


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
    inputs, has_audio = [], {}
    for sid in ids:
        c = (sources[sid].get("conformed") or {})
        vp = proj.abs(c["video"]) if c.get("video") else proj.work / "src" / f"{sid}.mp4"
        if not vp.exists():
            raise VeosError("NOT_CONFORMED", f"work/src/{sid}.mp4 is missing", "Run `veos conform` first.")
        inputs.append(vp)
        has_audio[sid] = bool(sources[sid].get("audio"))
    parts, labels = [], []
    for k, sg in enumerate(cutmap["segments"]):
        j = ids.index(sg["src"])
        a, n = sg["in_frame"], sg["f1"] - sg["f0"]
        d = n / FPS
        parts.append(f"[{j}:v]trim=start_frame={a}:end_frame={a + n},setpts=PTS-STARTPTS,fps={FPS},"
                     f"scale={PROXY_W}:{PROXY_H}:force_original_aspect_ratio=decrease,"
                     f"pad={PROXY_W}:{PROXY_H}:(ow-iw)/2:(oh-ih)/2,setsar=1,format=yuv420p[v{k}]")
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
    edl_path = Path(args.edl)
    if not edl_path.is_absolute() and not edl_path.exists() and (proj.root / args.edl).exists():
        edl_path = proj.root / args.edl
    if not edl_path.exists():
        raise VeosError("EDL_MISSING", f"EDL not found: {args.edl}", "Pass the path to edl.json.")
    edl = read_json(edl_path)
    sources = {s["id"]: s for s in read_json(sp)["sources"]}
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
