"""veos cut: EDL (source time) -> cutmap.json, words.edit.json and a 540x960 review proxy.

Voice-over reels (E-12): `veos cut --identity [--tighten]` writes the EDL itself. The cut map is the identity over the
voice-over (edit time = VO time), with the silence before the first word and after the last one trimmed (`--no-trim`
keeps the file exactly). `--tighten` also shortens every pause longer than `--max-pause` (0.35 s) to about 0.12 s, the
same rule the talking-head rough cut uses (only where the audio is silent too). The proxy shows a plain dark frame when
there is no picture.

Speed (`--speed 1.2`, else the playbook's `cut.speed`; `--speed 1` is normal speed): applied after the pauses are
tightened, per segment. A segment keeps `src_frames` source frames and plays them in `round(src_frames / speed)` edit
frames: edit frame f0 + k shows source frame in_frame + floor(k * speed + 0.5) (`src_frame`), and its sound is
time-stretched with the pitch kept (atempo). Every reader of the cut map maps edit -> source through `src_frame` /
`src_frames` / `seg_speed`, so faces, frames, cut-out, captions, the voice track and the render stay in sync. At speed 1
the cut map is exactly as before (no `speed` / `src_frames` keys).

The summary also reads the AUDIO (speechmap.py): `dead_air` (every silence >= 0.6 s in edit seconds, even under words)
and `dropped_speech` (speech the EDL leaves out, with the words there; `clipped` = a cut point inside speech). Both are
information for the cutter, never a gate. Words the transcript marked `suspect` (in a silence) are left out of
words.edit.json and listed under `suspect_words` (`--keep-suspect` keeps them).
"""
from __future__ import annotations

import re
from pathlib import Path

from .core import FPS, VeosError, filter_complex_args, need_project, r3, read_json, run, tools, write_json

PROXY_W, PROXY_H = 540, 960
GAP_S = 0.150
LEAD_S, TAIL_S = 0.04, 0.08          # cut points: start 0.04 s before a word, end 0.08 s after one (reel-roughcut rule)
VO_KINDS = ("voiceover", "audio-only")
SPEED_MIN, SPEED_MAX = 1.0, 1.5


# ---------------------------------------------------------------- speed: edit frame <-> source frame
def seg_speed(seg: dict) -> float:
    return float(seg.get("speed") or 1.0)


def _pct(speed: float) -> int:
    return int(round(float(speed) * 100))


def src_frames(seg: dict) -> int:
    """Source frames a cut-map segment covers (= its edit frames at speed 1)."""
    return int(seg.get("src_frames") or (int(seg["f1"]) - int(seg["f0"])))


def src_offset(k: int, speed: float) -> int:
    """Source frame offset of the segment's k-th edit frame: floor(k * speed + 0.5), in exact integer steps."""
    p = _pct(speed)
    return k if p == 100 else (k * p + 50) // 100


def src_frame(seg: dict, n: int) -> int:
    """The source frame edit frame `n` of this segment shows."""
    return int(seg["in_frame"]) + src_offset(int(n) - int(seg["f0"]), seg_speed(seg))


def edit_frames(n_src: int, speed: float) -> int:
    """Edit frames that play `n_src` source frames at `speed` (round(n_src / speed))."""
    p = _pct(speed)
    return n_src if p == 100 else max(1, (2 * n_src * 100 + p) // (2 * p))


def select_expr(speed: float, offset: int = 0) -> str:
    """ffmpeg `select` keeping exactly the source frames src_offset(k) picks, for input frame n = offset + 0, 1, ..."""
    p = _pct(speed)
    r = f"(n+{offset})" if offset else "n"
    return f"select='lt(ceil((100*{r}-50)/{p})*{p},100*{r}+50)'"


def check_speed(v) -> float:
    try:
        sp = round(float(v), 2)
    except (TypeError, ValueError):
        raise VeosError("BAD_SPEED", f"--speed {v!r} is not a number", "Pass e.g. --speed 1.2 (1.0 to 1.5).") from None
    if not SPEED_MIN - 1e-9 <= sp <= SPEED_MAX + 1e-9:
        raise VeosError("BAD_SPEED", f"speed {sp} is outside {SPEED_MIN}-{SPEED_MAX}", "Pick 1.0 (normal) to 1.5.")
    return sp


def add_args(p, cmd):
    p.add_argument("edl", nargs="?", default=None, help="path to edl.json (omit with --identity)")
    p.add_argument("--no-proxy", action="store_true", help="skip rendering cut_proxy.mp4")
    p.add_argument("--identity", action="store_true",
                   help="voice-over reels: build the EDL from the voice-over itself (edit time = VO time); writes work/edl.json")
    p.add_argument("--tighten", action="store_true", help="with --identity: shorten pauses longer than --max-pause to ~0.12 s")
    p.add_argument("--max-pause", type=float, default=0.35, help="with --tighten: longest pause kept as is (s, default 0.35)")
    p.add_argument("--no-trim", action="store_true", help="with --identity: keep the silence before the first and after the last word")
    p.add_argument("--end-hold", type=float, default=0.4, help="with --identity: seconds kept after the last word (default 0.4)")
    p.add_argument("--speed", type=float, default=None,
                   help="play the cut faster, pitch kept: 1.0-1.5 (default: the playbook's cut.speed, else 1.0); "
                        "speech reels only")
    p.add_argument("--keep-suspect", action="store_true",
                   help="keep words the transcript marked suspect (lying in a silence) in words.edit.json")
    # no-voice reels (novoice.py): the cut follows the music
    p.add_argument("--snap-beats", nargs="?", const="beats", choices=["beats", "bars"], default=None,
                   help="no-voice reels: move each segment's end onto the nearest beat (or bar start) of work/beats.json")
    p.add_argument("--snap-tol", type=float, default=0.3, help="with --snap-beats: furthest a cut moves (s, default 0.3)")
    p.add_argument("--audio", choices=["music", "clips", "none"], default=None,
                   help="no-voice reels: the cut's sound (default: the EDL's `audio`, else music when there is some)")


# ---------------------------------------------------------------- identity EDL (voice-over reels)
def identity_edl(sources: list[dict], words: dict[str, list[dict]], *, tighten: bool = False, max_pause: float = 0.35,
                 trim: bool = True, end_hold: float = 0.4, silences: dict[str, list] | None = None) -> dict:
    """EDL covering each voice-over source in order (V, V2, ...). Words are source-time {s, e} per source id.

    Without words (or with trim off and no tighten) a source is kept whole. Leading silence is cut to LEAD_S before the
    first word, trailing silence to `end_hold` after the last word of the last source (TAIL_S for earlier parts).
    `silences` (audio silences per source id): a pause is tightened only where the audio is silent, and the cut points
    sit on that silence, never inside speech.
    """
    vos = [s for s in sources if s.get("kind") in VO_KINDS]
    if not vos:
        raise VeosError("NO_VOICEOVER", "no voice-over source in sources.json",
                        "Run `veos ingest --audio <voice-over>` first (or write the EDL yourself for talking-head clips).")
    segs: list[dict] = []
    for k, s in enumerate(vos):
        dur = float(s.get("duration") or 0.0)
        ws = sorted((w for w in words.get(s["id"], []) if w.get("e", 0) > w.get("s", 0) and not w.get("suspect")),
                    key=lambda w: w["s"])
        sil = None if silences is None else silences.get(s["id"])
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
                if sil is not None:  # the audio decides: tighten each real silence, cut on its edges, keep any sound
                    quiet = sorted((max(x, w0["s"]), min(y, w1["e"])) for x, y in sil
                                   if min(y, w1["e"]) - max(x, w0["s"]) > max_pause)
                    for qa, qb in quiet:
                        end, nxt = qa + TAIL_S, qb - LEAD_S
                        if end - cur >= 1.0 / FPS and nxt > end:
                            segs.append({"src": s["id"], "in": r3(cur), "out": r3(end),
                                         "note": f"silence {qb - qa:.2f}s tightened"})
                            cur = nxt
                    continue
                end, nxt = w0["e"] + TAIL_S, w1["s"] - LEAD_S
                if end - cur >= 1.0 / FPS and nxt > end:
                    segs.append({"src": s["id"], "in": r3(cur), "out": r3(end), "note": f"pause {w1['s'] - w0['e']:.2f}s tightened"})
                    cur = nxt
        segs.append({"src": s["id"], "in": r3(cur), "out": r3(b), "note": "voice-over"})
    return {"version": 1, "fps": FPS, "auto": "identity" + ("+tighten" if tighten else ""), "segments": segs}


# ---------------------------------------------------------------- cutmap
def build_cutmap(edl: dict, sources: dict, proj, speed: float = 1.0) -> tuple[dict, list[str]]:
    """Validate the EDL and snap to frames. `sources` maps id -> sources.json entry. `speed` > 1: each segment plays its
    source frames in fewer edit frames (`speed` / `src_frames` on the segment and `speed` on the map)."""
    fast = _pct(speed) != 100
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
        n_src = i1 - i0
        n = edit_frames(n_src, speed)
        seg = {"t0": r3(f / FPS), "t1": r3((f + n) / FPS), "f0": f, "f1": f + n, "src": sid, "in": r3(a), "in_frame": i0}
        if fast:
            seg.update(speed=round(float(speed), 2), src_frames=n_src)
        out.append(seg)
        f += n
    cm = {"version": 1, "fps": FPS, "duration": r3(f / FPS), "frames": f, "segments": out}
    if fast:
        cm["speed"] = round(float(speed), 2)
    return cm, warnings


# ---------------------------------------------------------------- words
def remap_words(cutmap: dict, proj, keep_suspect: bool = False) -> dict | None:
    """work/words/<id>.json (source time) -> words.edit.json (edit time, speed included). Words marked `suspect` are
    left out (listed under `suspect_words`, recoverable with `keep_suspect`)."""
    wdir = proj.work / "words"
    if not wdir.exists():
        return None
    cache, words, silences, speech, suspect = {}, [], [], [], []
    for sg in cutmap["segments"]:
        sid = sg["src"]
        if sid not in cache:
            p = wdir / f"{sid}.json"
            cache[sid] = read_json(p) if p.exists() else None
        wf = cache[sid]
        if wf is None:
            continue
        lo = sg["in_frame"] / FPS
        hi = lo + src_frames(sg) / FPS
        sp = seg_speed(sg)
        shift = sg["t0"] - lo

        def ed(x: float) -> float:
            return r3(x + shift) if sp == 1.0 else r3(min(sg["t1"], sg["t0"] + (x - lo) / sp))
        for w in wf.get("words", []):
            dur = max(w["e"] - w["s"], 1e-6)
            inside = min(w["e"], hi) - max(w["s"], lo)
            if inside / dur >= 0.5:
                nw = dict(w)
                nw.pop("orig", None)
                nw["si"] = w.get("i")
                nw["src"] = sid
                nw["s"] = ed(max(w["s"], lo))
                nw["e"] = ed(min(w["e"], hi))
                if w.get("suspect") and not keep_suspect:
                    suspect.append(nw)
                else:
                    words.append(nw)
        for key, dest in (("silences", silences), ("speech", speech)):
            for a, b in wf.get(key) or []:
                a2, b2 = max(a, lo), min(b, hi)
                if b2 - a2 > 1e-3:
                    dest.append([ed(a2), ed(b2)])
    if not words and not any(cache.values()):
        return None
    for i, w in enumerate(words):
        w["i"] = i
    first = next((v for v in cache.values() if v), {})
    doc = {"version": 1, "source": "edit", "model": first.get("model"), "language": first.get("language"),
           "words": words, "silences": silences}
    if any(v and "speech" in v for v in cache.values()):
        doc["speech"] = speech
    if cutmap.get("speed"):
        doc["speed"] = cutmap["speed"]
    if suspect:
        doc["suspect_words"] = [{k: w[k] for k in ("w", "s", "e", "p", "src", "si", "suspect") if k in w} for w in suspect]
    return doc


def gaps_from_words(words: list[dict]) -> list[list[float]]:
    ws = sorted(words, key=lambda w: w["s"])
    return [[r3(a["e"]), r3(b["s"])] for a, b in zip(ws, ws[1:]) if b["s"] - a["e"] >= GAP_S - 1e-9]


# ---------------------------------------------------------------- proxy
def render_proxy(cutmap: dict, sources: dict, proj, out: Path) -> None:
    """The review proxy (540x960, with sound) of exactly the cut. A source with an older full conform plays from it, as
    before; otherwise each kept segment comes straight from the original clip on the conform grid (rawsrc: frame-exact,
    only the kept stretch is decoded) with its sound from work/audio/<id>.wav, so nothing has to be converted first."""
    from . import rawsrc
    from .conform import video_mode
    inputs: list[list[str]] = []

    def add(opts: list[str], path: Path) -> int:
        inputs.append([*opts, "-i", str(path)])
        return len(inputs) - 1

    full_in: dict[str, int] = {}
    wav_in: dict[str, int] = {}
    grids: dict[str, rawsrc.Grid] = {}
    fit = (f"scale={PROXY_W}:{PROXY_H}:force_original_aspect_ratio=decrease,"
           f"pad={PROXY_W}:{PROXY_H}:(ow-iw)/2:(oh-ih)/2,setsar=1,format=yuv420p")

    def wav(sid: str) -> int | None:
        if sid not in wav_in:
            c = sources[sid].get("conformed") or {}
            wp = proj.abs(c["audio"]) if c.get("audio") else proj.work / "audio" / f"{sid}.wav"
            if not wp.exists():
                raise VeosError("NOT_CONFORMED", f"work/audio/{sid}.wav is missing", "Run `veos conform --audio-only` first.")
            wav_in[sid] = add([], wp)
        return wav_in[sid]

    def sound(j: int | None, a: int, d: float, k: int, sp: float = 1.0, ns: int = 0) -> str:
        if j is None:
            return f"anullsrc=r=48000:cl=stereo,atrim=duration={d:.6f}[a{k}]"
        if _pct(sp) == 100:
            return (f"[{j}:a]atrim=start={a / FPS:.6f}:duration={d:.6f},asetpts=PTS-STARTPTS,"
                    f"aresample=48000,aformat=channel_layouts=stereo,apad=whole_dur={d:.6f},"
                    f"atrim=duration={d:.6f}[a{k}]")
        return (f"[{j}:a]atrim=start={a / FPS:.6f}:duration={ns / FPS:.6f},asetpts=PTS-STARTPTS,"
                f"aresample=48000,aformat=channel_layouts=stereo,atempo={sp:.2f},apad=whole_dur={d:.6f},"
                f"atrim=duration={d:.6f}[a{k}]")

    def faster(sp: float, n: int) -> str:  # source frames -> the edit frames this speed shows (empty at speed 1)
        return "" if _pct(sp) == 100 else f"setpts=PTS-STARTPTS,{select_expr(sp)},setpts=N/({FPS}*TB),"

    parts, labels = [], []
    for k, sg in enumerate(cutmap["segments"]):
        sid = sg["src"]
        s = sources[sid]
        a, n = sg["in_frame"], sg["f1"] - sg["f0"]
        sp, ns = seg_speed(sg), src_frames(sg)
        d = n / FPS
        has_audio = bool(s.get("audio"))
        if s.get("kind") in VO_KINDS:  # a voice-over has no picture: a plain frame over its conformed audio
            parts.append(f"color=c=0x16161c:s={PROXY_W}x{PROXY_H}:r={FPS},trim=end_frame={n},setpts=PTS-STARTPTS,"
                         f"setsar=1,format=yuv420p[v{k}]")
            parts.append(sound(wav(sid) if has_audio else None, a, d, k, sp, ns))
        elif video_mode(s, proj) == "full":  # an older full conform: its own picture and sound, as before
            c = s.get("conformed") or {}
            if sid not in full_in:
                full_in[sid] = add([], proj.abs(c["video"]))
            j = full_in[sid]
            if _pct(sp) == 100:
                parts.append(f"[{j}:v]trim=start_frame={a}:end_frame={a + n},setpts=PTS-STARTPTS,fps={FPS},{fit}[v{k}]")
            else:
                parts.append(f"[{j}:v]trim=start_frame={a}:end_frame={a + ns},{faster(sp, n)}fps={FPS},{fit},"
                             f"tpad=stop_mode=clone:stop={n},trim=end_frame={n}[v{k}]")
            parts.append(sound(j if has_audio else None, a, d, k, sp, ns))
        else:  # straight from the original clip, only this segment
            src = proj.abs(s["path"])
            if sid not in grids:
                grids[sid] = rawsrc.grid(src)
            pre, ch = rawsrc.chain(grids[sid], a, ns)
            j = add(pre, src)
            parts.append(f"[{j}:v]{ch},setpts=PTS-STARTPTS,{faster(sp, n)}{fit},tpad=stop_mode=clone:stop={n},"
                         f"trim=end_frame={n}[v{k}]")
            parts.append(sound(wav(sid) if has_audio else None, a, d, k, sp, ns))
        labels.append(f"[v{k}][a{k}]")
    parts.append("".join(labels) + f"concat=n={len(labels)}:v=1:a=1[v][a]")
    script = proj.path("work", "cut_filter.txt")
    script.write_text(";\n".join(parts), encoding="utf-8")
    cmd = [tools().ffmpeg, "-v", "error", "-y"]
    for opts in inputs:
        cmd += opts
    cmd += [*filter_complex_args(script), "-map", "[v]", "-map", "[a]", "-r", str(FPS),
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
        raise VeosError("NO_SOURCES", "work/sources.json not found", "Run `veos ingest` and `veos conform --audio-only` first.")
    sdoc = read_json(sp)
    if sdoc.get("source_type") == "no_voice":  # B-roll / screen recording / photos + music: novoice.py
        from .novoice import cut_main
        out = cut_main(args, proj)
        if getattr(args, "speed", None) not in (None, 1, 1.0):  # speed is for speech; the music keeps its tempo
            out.setdefault("warnings", []).append(f"--speed {args.speed} ignored: a no-voice cut plays at normal speed "
                                                  "(the music keeps its tempo; pick shorter clips for a faster reel)")
        return out
    if getattr(args, "snap_beats", None) or getattr(args, "audio", None):
        raise VeosError("BAD_ARGS", "--snap-beats and --audio are for no-voice reels",
                        "This project has speech: its cut follows the words.")
    src_list = sdoc["sources"]
    from . import langs
    pb_cut = langs.cut_settings(proj)
    if getattr(args, "speed", None) is not None:
        speed, speed_from = check_speed(args.speed), "--speed"
    elif pb_cut["speed"] is not None:
        speed, speed_from = check_speed(pb_cut["speed"]), "playbook cut.speed"
    else:
        speed, speed_from = 1.0, "default"
    if getattr(args, "identity", False):
        wd, sil = {}, {}
        for s in src_list:
            wp = proj.work / "words" / f"{s['id']}.json"
            if wp.exists():
                wd[s["id"]] = read_json(wp).get("words", [])
            if args.tighten and s.get("kind") in VO_KINDS:
                m = _speech_map(proj, s)
                if m is not None:
                    sil[s["id"]] = m.get("silences") or []
        edl = identity_edl(src_list, wd, tighten=args.tighten, max_pause=args.max_pause, trim=not args.no_trim,
                           end_hold=args.end_hold, silences=sil or None)
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
    cutmap, warnings = build_cutmap(edl, sources, proj, speed)
    warnings = pb_cut["warnings"] + warnings
    write_json(proj.path("work", "cutmap.json"), cutmap)
    words = remap_words(cutmap, proj, keep_suspect=getattr(args, "keep_suspect", False))
    if words is not None:
        write_json(proj.path("work", "words.edit.json"), words)
    removed = 0.0
    for sid in {sg["src"] for sg in cutmap["segments"]}:
        used = sum(src_frames(sg) for sg in cutmap["segments"] if sg["src"] == sid) / FPS
        removed += max(0.0, sources[sid]["duration"] - used)
    summary = {"duration": cutmap["duration"], "frames": cutmap["frames"], "segments": len(cutmap["segments"]),
               "removed_s": r3(removed), "words_remapped": None if words is None else len(words["words"]),
               "speed": cutmap.get("speed", 1.0), "speed_from": speed_from}
    if words is not None and words.get("suspect_words"):
        summary["suspect_words"] = len(words["suspect_words"])
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
    try:
        summary.update(audio_report(proj, cutmap, sources))
    except Exception as e:  # noqa: BLE001 - information only
        summary.update(dead_air=None, dropped_speech=None)
        warnings.append(f"audio report unavailable: {type(e).__name__}: {e}")
    summary["warnings"] = warnings
    return summary


def _speech_map(proj, s: dict) -> dict | None:
    from . import speechmap
    try:
        return speechmap.for_source(proj, s["id"], s.get("duration"))
    except Exception:  # noqa: BLE001 - the audio report is information, never a reason to fail the cut
        return None


def audio_report(proj, cutmap: dict, sources: dict) -> dict:
    """`dead_air` (edit seconds, every silence >= 0.6 s by the audio) and `dropped_speech` (speech the cut leaves out)."""
    from . import speechmap
    maps, words = {}, {}
    for sid in dict.fromkeys(sg["src"] for sg in cutmap["segments"]):
        m = _speech_map(proj, sources[sid])
        if m is not None:
            maps[sid] = m
        wp = proj.work / "words" / f"{sid}.json"
        if wp.exists():
            try:
                words[sid] = read_json(wp).get("words") or []
            except ValueError:
                pass
    if not maps:
        return {"dead_air": None, "dropped_speech": None, "speech_map": "unavailable (no audio)"}
    dead = speechmap.dead_air(cutmap, maps)
    dropped = speechmap.dropped_speech(cutmap, maps, words)
    return {"dead_air": dead, "dead_air_s": r3(sum(d["dur"] for d in dead)), "dropped_speech": dropped,
            "dropped_speech_clipped": sum(1 for d in dropped if d.get("clipped")),
            "speech_map": sorted({m.get("method", "?") for m in maps.values()})}
