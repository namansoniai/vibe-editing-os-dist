"""veos ingest: register source files, classify them and detect camera-setup segments.

Voice-over reels (E-12, `source_type: voiceover_only`): `veos ingest --audio vo.wav [--script script.md]` registers the
voice-over as source `V` (kind `voiceover`; a video file is accepted and its picture is ignored). The same happens with
no `--audio` when project.json says `source_type: voiceover_only` (the VO is project.json `voiceover`, else the
audio-only file, else the longest file with sound). In a voice-over project every other clip is supplementary (B-roll /
screen recording, never a talking head).

No-voice reels (`source_type: no_voice`, novoice.py): clips are B-roll / screen recordings, photos become `still`
sources (held in work/stills/<id>.mp4), and the music (project.json `music`, else the audio-only files) is source `M`.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np

from . import facedet, media
from .core import FPS, VeosError, need_project, r3, read_json, tools, write_json

SPEECH_LUFS = -45.0       # quieter than this is treated as "no speech"
FACE_TH = 0.5             # face_ratio needed for talking-head
SELFIE_W = 0.35           # face width / frame width at or above this = selfie
WIDE_W = 0.10             # below this = wide
MIN_SEG_S = 2.0


def add_args(p, cmd):
    p.add_argument("inputs", nargs="*", help="video/audio files and/or folders (searched recursively); "
                   "default: the clips stored in project.json")
    p.add_argument("--audio", action="append", default=None, metavar="FILE",
                   help="a voice-over (wav/mp3/m4a/..., or a video whose picture is ignored): makes this a voice-over "
                        "project (source V); repeat for a VO recorded in parts (V, V2, ...)")
    p.add_argument("--script", default=None, help="the voice-over's script (stored; transcribe aligns the words to it)")


# ---------------------------------------------------------------- face detection
class FaceFinder:
    """Face detection via facedet (MediaPipe on tiled square windows, else YuNet / Haar on the whole frame)."""

    def __init__(self):
        facedet.backend_name()

    def find(self, gray: np.ndarray):
        """-> (w, h, cx, cy, score) as fractions of the frame, or None."""
        import cv2
        H, W = gray.shape
        rgb = cv2.cvtColor(np.ascontiguousarray(gray), cv2.COLOR_GRAY2RGB)
        r = facedet.detect(rgb, tiled=True, min_score=0.5)
        if not r:
            return None
        x, y, w, h, sc = r[0]
        return (w / W, h / H, (x + w / 2) / W, (y + h / 2) / H, sc)


# ---------------------------------------------------------------- analysis
def _flatness(g: np.ndarray) -> tuple[float, float]:
    """(edge density, flat-pixel fraction) of a gray frame."""
    import cv2
    e = cv2.Canny(g, 60, 160)
    gi = g.astype(np.int16)
    gx = np.abs(np.diff(gi, axis=1))[:-1]
    gy = np.abs(np.diff(gi, axis=0))[:, :-1]
    return float((e > 0).mean()), float(((gx < 2) & (gy < 2)).mean())


def analyse_video(path: Path, duration: float, finder: FaceFinder | None) -> dict:
    step = max(0.5, duration / 360)
    ts, faces, motion, edge, flat = [], [], [], [], []
    prev = None
    for t, g in media.iter_gray_frames(path, step, width=288):
        ts.append(t)
        faces.append(finder.find(g) if finder else None)
        gi = g.astype(np.int16)
        motion.append(0.0 if prev is None else float(np.abs(gi - prev).mean()))
        prev = gi
        e, f = _flatness(g)
        edge.append(e)
        flat.append(f)
    return {"t": ts, "face": faces, "motion": motion, "edge": edge, "flat": flat, "step": step}


def _label(face_w: float | None, motion: float) -> str:
    if face_w is None:
        return "other"
    if face_w >= SELFIE_W:
        return "selfie"
    if face_w >= WIDE_W:
        return "selfie" if (face_w >= 0.26 and motion > 20) else "tripod"
    return "wide"


def segment_setups(an: dict, cuts: list[float], duration: float) -> list[dict]:
    """Per-sample label from smoothed face width (+ camera motion); boundaries snap to nearby scene cuts."""
    ts, n = an["t"], len(an["t"])
    if n == 0:
        return [{"start": 0.0, "end": r3(duration), "setup": "other"}]
    w = np.array([f[0] if f else np.nan for f in an["face"]])
    mot = np.array(an["motion"])
    k = 2
    labels = []
    for i in range(n):
        lo, hi = max(0, i - k), min(n, i + k + 1)
        ww = w[lo:hi]
        ww = ww[~np.isnan(ww)]
        fw = float(np.median(ww)) if len(ww) >= max(1, (hi - lo) // 3) else None
        labels.append(_label(fw, float(np.median(mot[lo:hi]))))
    runs: list[list] = []  # [label, first_idx, last_idx]
    for i, lab in enumerate(labels):
        if runs and runs[-1][0] == lab:
            runs[-1][2] = i
        else:
            runs.append([lab, i, i])
    min_n = max(2, int(round(MIN_SEG_S / an["step"])))
    changed = True
    while changed and len(runs) > 1:
        changed = False
        for j, r in enumerate(runs):
            if r[2] - r[1] + 1 < min_n:
                if j == 0:
                    nb = 1
                elif j == len(runs) - 1:
                    nb = j - 1
                else:
                    nb = j - 1 if (runs[j - 1][2] - runs[j - 1][1]) >= (runs[j + 1][2] - runs[j + 1][1]) else j + 1
                runs[nb][1], runs[nb][2] = min(runs[nb][1], r[1]), max(runs[nb][2], r[2])
                runs.pop(j)
                changed = True
                break
        merged: list[list] = []
        for r in runs:
            if merged and merged[-1][0] == r[0]:
                merged[-1][2] = r[2]
            else:
                merged.append(r)
        runs = merged
    bounds = [0.0]
    for a, b in zip(runs, runs[1:]):
        lo, hi = ts[a[2]], ts[b[1]]
        near = [c for c in cuts if lo - 1.0 <= c <= hi + 1.0]
        bounds.append(min(near, key=lambda c: abs(c - (lo + hi) / 2)) if near else (lo + hi) / 2)
    bounds.append(duration)
    return [{"start": r3(s), "end": r3(e), "setup": r[0]} for r, s, e in zip(runs, bounds, bounds[1:])]


def classify(an: dict, lufs: float | None, has_audio: bool) -> tuple[str, float, list[str]]:
    faces = an["face"]
    ratio = sum(1 for f in faces if f) / max(1, len(faces))
    notes: list[str] = []
    speech = has_audio and lufs is not None and lufs > SPEECH_LUFS
    if ratio >= FACE_TH and speech:
        return "talking-head", ratio, notes
    if ratio >= FACE_TH:
        notes.append("face present but no speech-level audio")
        return "broll", ratio, notes
    edge, flat = float(np.mean(an["edge"])), float(np.mean(an["flat"]))
    if flat > 0.55 and edge > 0.012:
        return "screen-recording", ratio, notes
    return "broll", ratio, notes


# ---------------------------------------------------------------- command
def _collect(inputs: list[str], stills: bool = False) -> list[Path]:
    """Media files in `inputs` (folders searched recursively); `stills` also takes photos (no-voice reels)."""
    from .novoice import STILL_EXT
    out, seen = [], set()
    exts = media.VIDEO_EXT | media.AUDIO_EXT | (STILL_EXT if stills else set())
    for s in inputs:
        p = Path(s).expanduser()
        if not p.exists():
            raise VeosError("INPUT_MISSING", f"not found: {s}", "Check the path (quote paths that contain spaces).")
        if p.is_dir():
            files = sorted((q for q in p.rglob("*") if q.is_file() and q.suffix.lower() in exts),
                           key=lambda q: [c.lower() for c in q.parts])
        else:
            files = [p]
        for f in files:
            r = f.resolve()
            if r not in seen:
                seen.add(r)
                out.append(r)
    if not out:
        raise VeosError("NO_MEDIA", "no video or audio files found", "Pass video files or a folder that contains them.")
    return out


def _talking_id(n: int) -> str:
    return chr(ord("A") + n) if n < 26 else f"A{n - 25}"


VO_KIND = "voiceover"


def _best_audio(f: Path, pr: dict, notes: list[str]) -> dict | None:
    if not pr["audio"]:
        return None
    best = None
    for a in pr["audio"]:
        lufs, tp = media.loudness(f, a["stream"])
        if best is None or (lufs if lufs is not None else -999) > (best[1] if best[1] is not None else -999):
            best = (a, lufs, tp)
    a, lufs, tp = best
    if len(pr["audio"]) > 1:
        notes.append(f"{len(pr['audio'])} audio streams; stream {a['stream']} is the loudest")
    if lufs is None:
        notes.append("audio is silent")
    return {"stream": a["stream"], "channels": a["channels"], "lufs": lufs, "tp": tp}


def voiceover_source(f: Path, sid: str, proj) -> dict:
    """A voice-over source entry: audio only; a video's picture is ignored (no frames, no faces)."""
    pr = media.probe(f)
    notes: list[str] = []
    audio = _best_audio(f, pr, notes)
    if audio is None:
        raise VeosError("VO_NO_AUDIO", f"{f.name} has no audio stream",
                        "Give the voice-over as an audio file (wav, mp3, m4a) or a video with sound.")
    if audio["lufs"] is None or audio["lufs"] <= SPEECH_LUFS:
        notes.append(f"voice-over is very quiet ({audio['lufs']} LUFS); check it is the right file")
    adur = max((a["duration"] for a in pr["audio"]), default=0.0) or pr["duration"]
    if pr["video"] is not None:
        notes.append("video file: only its sound is used (picture ignored)")
    return {"id": sid, "path": proj.rel(f), "kind": VO_KIND, "duration": r3(adur), "frames": int(round(adur * FPS)),
            "audio": audio, "picture_ignored": pr["video"] is not None, "segments": [], "face_ratio": 0.0, "notes": notes}


def _vo_id(k: int) -> str:
    return "V" if k == 0 else f"V{k + 1}"


def pick_voiceover(files: list[Path], declared=None) -> list[Path]:
    """The VO file(s) of a voice-over project: project.json `voiceover` when set, else the audio-only files, else the
    longest file that has sound."""
    if declared:
        want = [Path(d).expanduser().resolve() for d in ([declared] if isinstance(declared, str) else declared)]
        return [f for f in files if f in want] or [w for w in want if w.exists()]
    audio = [f for f in files if f.suffix.lower() in media.AUDIO_EXT]
    if audio:
        return audio
    best, dur = None, -1.0
    for f in files:
        pr = media.probe(f)
        d = pr["duration"] if pr["audio"] else -1.0
        if d > dur:
            best, dur = f, d
    return [best] if best else []


def main(args, project) -> dict:
    proj = need_project(project)
    inputs = list(args.inputs or [])
    pj = proj.root / "project.json"
    pstate = read_json(pj) if pj.exists() else {}
    vo_args = list(getattr(args, "audio", None) or [])
    voice_mode = bool(vo_args) or pstate.get("source_type") == "voiceover_only"
    plates = not voice_mode and pstate.get("source_type") == "animated_plates"  # puppets / animation: no face detection
    no_voice = not voice_mode and pstate.get("source_type") == "no_voice"  # clips / photos + music (novoice.py)
    if not inputs and not vo_args:  # default to the clips registered by `veos project init`
        inputs = pstate.get("clips") or []
        if not inputs:
            raise VeosError("NO_INPUT", "no files given and project.json has no clips",
                            "Pass files/folders (or --audio <voice-over>), or run `veos project init <clips> --project P` first.")
    files = _collect(inputs, stills=no_voice) if inputs else []
    vo_files: list[Path] = []
    music_files: list[Path] = []
    if no_voice:
        from . import novoice
        music_files = novoice.pick_music(files, pstate.get("music"))
        files = [f for f in files if f not in music_files]
    if voice_mode:
        vo_files = _collect(vo_args) if vo_args else pick_voiceover(files, pstate.get("voiceover"))
        if not vo_files:
            raise VeosError("VO_MISSING", "this is a voice-over project but no voice-over file was found",
                            "Pass it with --audio <file> (an audio file, or a video whose picture is ignored).")
        files = [f for f in files if f not in vo_files]
    script = getattr(args, "script", None)
    if script:
        sp = Path(script).expanduser()
        if not sp.exists():
            raise VeosError("SCRIPT_MISSING", f"script file not found: {script}", "Check the --script path.")
        script = sp.resolve().as_posix()
    elif pstate.get("script"):
        script = pstate["script"]
    finder = None
    sources, summary, warnings = [], [], []
    for k, f in enumerate(vo_files):
        entry = voiceover_source(f, _vo_id(k), proj)
        sources.append(entry)
        summary.append({"id": entry["id"], "file": f.name, "kind": VO_KIND, "duration": entry["duration"],
                        "picture_ignored": entry["picture_ignored"]})
        warnings += [f"{f.name}: {n}" for n in entry["notes"] if "quiet" in n or "silent" in n]
    for k, f in enumerate(music_files):
        entry = novoice.music_source(f, novoice.music_id(k), proj)
        sources.append(entry)
        summary.append({"id": entry["id"], "file": f.name, "kind": entry["kind"], "duration": entry["duration"]})
        warnings += [f"{f.name}: {n}" for n in entry["notes"] if "silent" in n]
    nth, ns = 0, 0
    for f in files:
        if no_voice and novoice.is_still(f):  # a photo / slide: held in a short clip, like any other clip after this
            ns += 1
            entry = novoice.still_source(f, f"S{ns}", proj)
            sources.append(entry)
            summary.append({"id": entry["id"], "file": f.name, "kind": entry["kind"], "fit": entry["fit"],
                            "size": entry["image_size"]})
            continue
        pr = media.probe(f)
        v = pr["video"]
        notes: list[str] = []
        audio = _best_audio(f, pr, notes)
        entry: dict = {"path": proj.rel(f)}
        if v is None:
            kind, ratio, segs = "audio-only", 0.0, []
            entry.update(duration=r3(pr["duration"]), frames=int(round(pr["duration"] * FPS)))
        elif plates:
            dur = v["duration"] or pr["duration"]
            kind, ratio = "talking-head", 0.0  # the plate carries the picture and its own sound (the reel's main track)
            segs = [{"start": 0.0, "end": r3(dur), "setup": "plate"}]
            notes.append("animated plate: face detection skipped")
            frames = v["frames"] or int(round(dur * (v["fps"] or FPS)))
            entry.update(duration=r3(dur), frames=frames, width=v["disp_w"], height=v["disp_h"],
                         rotation=v["rotation"], fps_in=v["fps_in"], vfr=v["vfr"])
            if v["vfr"]:
                warnings.append(f"{f.name}: variable frame rate (conform makes it a constant 30 fps)")
        else:
            if finder is None and not no_voice:  # no-voice: no presenter to find, only B-roll vs screen recording
                finder = FaceFinder()
            dur = v["duration"] or pr["duration"]
            an = analyse_video(f, dur, finder)
            kind, ratio, n2 = classify(an, audio["lufs"] if audio else None, audio is not None)
            notes += n2
            if kind == "talking-head":
                segs = segment_setups(an, media.scene_cuts(f, 0.3), dur)
            else:
                segs = [{"start": 0.0, "end": r3(dur), "setup": "screen" if kind == "screen-recording" else "other"}]
            frames = v["frames"] or int(round(dur * (v["fps"] or FPS)))
            entry.update(duration=r3(dur), frames=frames, width=v["disp_w"], height=v["disp_h"],
                         rotation=v["rotation"], fps_in=v["fps_in"], vfr=v["vfr"])
            if v["vfr"]:
                warnings.append(f"{f.name}: variable frame rate (conform makes it a constant 30 fps)")
        if (voice_mode or no_voice) and kind == "talking-head":  # no presenter: extra clips are B-roll
            kind = "broll"
            notes.append(("no-voice" if no_voice else "voice-over") + " project: used as B-roll, not as a talking head")
            segs = [{"start": 0.0, "end": entry["duration"], "setup": "other"}]
        if kind == "talking-head":
            sid = _talking_id(nth)
            nth += 1
        else:
            ns += 1
            sid = f"S{ns}"
        src = {"id": sid, **entry, "kind": kind, "audio": audio, "segments": segs,
               "face_ratio": round(ratio, 2), "notes": notes}
        order = ["id", "path", "kind", "duration", "frames", "width", "height", "rotation", "fps_in", "vfr",
                 "audio", "segments", "face_ratio", "notes"]
        sources.append({k: src[k] for k in order if k in src})
        summary.append({"id": sid, "file": f.name, "kind": kind, "duration": entry["duration"],
                        "segments": [[s["start"], s["end"], s["setup"]] for s in segs],
                        "vfr": entry.get("vfr", False)})
    doc = {"version": 1, "fps": FPS, "source_type": "voiceover_only" if voice_mode else "animated_plates" if plates
           else "no_voice" if no_voice else "talking_head", "sources": sources}
    if script:
        doc["script"] = script
    write_json(proj.path("work", "sources.json"), doc)
    if pj.exists() and voice_mode:  # remember the branch (and the script) for the skills and later commands
        st = read_json(pj)
        new = {"source_type": "voiceover_only", "voiceover": [f.as_posix() for f in vo_files]}
        if script and not st.get("script"):
            new["script"] = script
        if any(st.get(k) != v for k, v in new.items()):
            st.update(new)
            write_json(pj, st)
    proj.log("ingest", f"ingested {len(sources)} sources ({doc['source_type']})")
    out = {"source_type": doc["source_type"], "sources": summary, "warnings": warnings}
    if script:
        out["script"] = Path(script).name
    return out
