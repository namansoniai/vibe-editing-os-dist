"""Synthetic two-person conversation built from two single-speaker reels, with known ground truth (tests + proof).

Real multi-person footage is not available, so a conversation is spliced: speaker A's phrases come from reel A, speaker
B's from reel B, alternating in turns (short, medium and long turns, two back-channels spoken *over* the other person,
one overlapping handover). Every file is generated on a 30 fps frame grid so lips stay in sync with the audio:

  camA.mp4 / camB.mp4   1080x1920 "angle" of each person: their footage while they talk, a held frame while they listen;
                        scratch audio of the room; camA starts 1.7 s BEFORE session 0, camB 2.35 s AFTER it
  micA.wav / micB.wav   per-person mics with -17/-16 dB bleed of the other voice; micA starts 0.9 s before session 0,
                        micB 0.4 s after it and its clock runs 60 ppm fast (drift)
  wide.mp4              3840x2160 two-shot "wide" (both people side by side) for faux angles; starts 0.5 s before 0
  truth.json            utterances [{speaker, t0, t1}] in session time, turns, per-file offset/drift

variant "distinct": B's voice is pitch/formant-shifted by 0.82 (sounds like another, deeper voice; lip sync kept).
variant "same": B is the creator's own unshifted voice (the same person as A: voice-only diarisation cannot separate
them; per-mic labelling still can). What this cannot prove: real room acoustics, real cross-talk, real listener
reactions (listeners are frozen frames), two different faces.
"""
from __future__ import annotations

import json
import math
import subprocess
from pathlib import Path

import numpy as np

from .core import run, tools, veos_home
from .testing import FOOTAGE

FPS = 30
SR = 48000
REELS = {"A": FOOTAGE / "Reel 7" / "reel 7.mp4", "B": FOOTAGE / "Reel 9" / "raw.mp4"}   # the two raw (unedited) takes
OFFSETS = {"camA": -1.7, "camB": 2.35, "micA": -0.9, "micB": 0.4, "wide": -0.5}   # file t=0 in session time
DRIFT = {"micB": 60e-6}
PITCH_B = 0.82


def _dec(path: Path, af: str | None = None, sr: int = SR) -> np.ndarray:
    cmd = [tools().ffmpeg, "-v", "error", "-i", str(path), "-vn", "-ac", "1"] + (["-af", af] if af else []) + \
          ["-ar", str(sr), "-f", "f32le", "-"]
    return np.frombuffer(subprocess.run(cmd, capture_output=True, check=True).stdout, np.float32).copy()


def utterances(x: np.ndarray, sr: int = SR, min_gap: float = 0.06, min_len: float = 0.35, under_db: float = 18.0) -> list[tuple[float, float]]:
    """Phrases between dips >= min_gap (20 ms RMS, `under_db` under the 95th percentile; the reels are tightly
    jump-cut, so dips are short), frame-snapped."""
    h = int(0.02 * sr)
    n = len(x) // h
    db = 20 * np.log10(np.sqrt((x[: n * h].reshape(n, h).astype(np.float64) ** 2).mean(1)) + 1e-9)
    on = db > np.percentile(db, 95) - under_db
    runs, i = [], 0
    while i < n:
        if not on[i]:
            i += 1
            continue
        j = i
        while j < n and on[j]:
            j += 1
        runs.append([i * 0.02, j * 0.02])
        i = j
    merged: list[list[float]] = []
    for a, b in runs:
        if merged and a - merged[-1][1] < min_gap:
            merged[-1][1] = b
        else:
            merged.append([a, b])
    out = []
    for a, b in merged:
        a, b = math.floor(max(0, a - 0.04) * FPS) / FPS, math.ceil((b + 0.06) * FPS) / FPS
        if b - a >= min_len:
            out.append((round(a, 4), round(b, 4)))
    return out


def plan_conversation(ua: list, ub: list, seed: int = 7) -> list[dict]:
    """Turn plan -> placements [{speaker, src_in, src_out, t0, t1, kind}] in session time (frame grid)."""
    rng = np.random.default_rng(seed)
    pat = [("B", 3), ("A", 8), ("B", 2.5), ("A", 13), ("B", 4), ("A", 3), ("B", 14), ("A", 2), ("B", 6), ("A", 5), ("B", 5)]
    ia = ib = 0
    t = 0.5
    out = []
    bc_done = 0
    for k, (spk, target) in enumerate(pat):
        pool, idx = (ua, ia) if spk == "A" else (ub, ib)
        start = t
        got = 0.0
        while got < target and idx < len(pool):
            a, b = pool[idx]
            idx += 1
            d = round((b - a) * FPS) / FPS
            out.append({"speaker": spk, "src_in": a, "src_out": round(a + d, 4), "t0": round(t, 4), "t1": round(t + d, 4),
                        "kind": "speech"})
            t += d
            got += d
            # back-channel from the listener in the middle of a long turn (spoken over the speaker)
            if target >= 12 and bc_done < 2 and got > target * 0.45 and not any(o.get("bc_turn") == k for o in out):
                other, opool = ("B", ub) if spk == "A" else ("A", ua)
                oi = ib if other == "B" else ia
                short = [u for u in opool[oi:] if u[1] - u[0] <= 1.1]
                if short:
                    u = short[0]
                    d2 = round((u[1] - u[0]) * FPS) / FPS
                    t0 = round((t - d * 0.5) * FPS) / FPS
                    out.append({"speaker": other, "src_in": u[0], "src_out": round(u[0] + d2, 4), "t0": t0,
                                "t1": round(t0 + d2, 4), "kind": "backchannel", "bc_turn": k})
                    bc_done += 1
                    if other == "B":
                        ib = opool.index(u) + 1
                    else:
                        ia = opool.index(u) + 1
            t += round(float(rng.uniform(0.12, 0.3)) * FPS) / FPS
        if spk == "A":
            ia = idx
        else:
            ib = idx
        gap = float(rng.uniform(0.25, 0.7))
        if k == 4:                       # one overlapping handover: the next speaker starts 0.3 s early
            gap = -0.3
        t = round((t + gap) * FPS) / FPS
        t = max(t, out[-1]["t1"] - 0.3)
    return out


def _track(place: list[dict], spk: str, src: np.ndarray, dur: float) -> np.ndarray:
    y = np.zeros(int(math.ceil(dur * SR)) + SR, np.float32)
    for p in place:
        if p["speaker"] != spk:
            continue
        a, b = int(round(p["src_in"] * SR)), int(round(p["src_out"] * SR))
        seg = src[a:b].copy()
        f = min(len(seg) // 2, int(0.008 * SR))
        if f:
            ramp = np.linspace(0, 1, f, dtype=np.float32)
            seg[:f] *= ramp
            seg[-f:] *= ramp[::-1]
        o = int(round(p["t0"] * SR))
        y[o:o + len(seg)] += seg[: len(y) - o]
    return y


def _file_signal(sig: np.ndarray, offset: float, drift: float, dur_file: float) -> np.ndarray:
    """File sample i plays session time offset + (i/SR)(1+drift)."""
    n = int(round(dur_file * SR))
    ts = offset + np.arange(n) / SR * (1 + drift)
    pos = ts * SR
    out = np.zeros(n, np.float32)
    ok = (pos >= 0) & (pos < len(sig) - 1)
    out[ok] = np.interp(pos[ok], np.arange(len(sig)), sig).astype(np.float32)
    return out


def _write_wav(path: Path, x: np.ndarray) -> None:
    import wave
    pcm = (np.clip(x, -1, 1) * 32767).round().astype("<i2")
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(pcm.tobytes())


def _video_edl(place: list[dict], spk: str, t_from: float, t_to: float) -> list[tuple]:
    """[(kind, a, b, frames)] in the person's reel: 'play' a..b or 'hold' frame a for N frames, covering the file span."""
    own = sorted([p for p in place if p["speaker"] == spk], key=lambda p: p["t0"])
    segs = []
    cur = t_from
    last_frame = own[0]["src_in"] if own else 0.0
    for p in own:
        if p["t0"] > cur:
            segs.append(("hold", last_frame, None, int(round((p["t0"] - cur) * FPS))))
            cur = p["t0"]
        a = p["src_in"] + max(0.0, cur - p["t0"])
        n = int(round((p["t1"] - cur) * FPS))
        if n > 0:
            segs.append(("play", a, a + n / FPS, n))
            cur = p["t1"]
            last_frame = a + (n - 1) / FPS
    if t_to > cur:
        segs.append(("hold", last_frame, None, int(round((t_to - cur) * FPS))))
    return [s for s in segs if s[3] > 0]


def _render_person(reel: Path, edl: list, audio_wav: Path, out: Path) -> None:
    parts, lab = [], []
    for k, (kind, a, b, n) in enumerate(edl):
        if kind == "play":
            parts.append(f"[0:v]trim=start={a:.5f}:end={b + 0.5 / FPS:.5f},setpts=PTS-STARTPTS,fps={FPS},"
                         f"trim=end_frame={n},setpts=PTS-STARTPTS[v{k}]")
        else:
            parts.append(f"[0:v]trim=start={a:.5f}:end={a + 1.5 / FPS:.5f},setpts=PTS-STARTPTS,fps={FPS},"
                         f"trim=end_frame=1,tpad=stop_mode=clone:stop={n - 1},setpts=PTS-STARTPTS[v{k}]")
        lab.append(f"[v{k}]")
    parts.append("".join(lab) + f"concat=n={len(lab)}:v=1:a=0,format=yuv420p[v]")
    script = out.with_suffix(".filter.txt")
    script.write_text(";\n".join(parts), encoding="utf-8")
    run([tools().ffmpeg, "-v", "error", "-y", "-i", str(reel), "-i", str(audio_wav), "-/filter_complex", str(script),
         "-map", "[v]", "-map", "1:a", "-r", str(FPS), "-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
         "-c:a", "aac", "-b:a", "160k", "-shortest", str(out)])
    script.unlink(missing_ok=True)


def build(variant: str = "distinct", out_dir: Path | None = None, video: bool = True, seed: int = 7) -> Path:
    """Generate the fixture (cached by variant + video flag). Returns the folder with truth.json."""
    for r in REELS.values():
        if not r.exists():
            raise FileNotFoundError(f"test footage missing: {r}")
    out = out_dir or (veos_home() / "scratch" / "dialogue-fixture" / f"{variant}{'' if video else '-audio'}")
    tj = out / "truth.json"
    if tj.exists() and (not video or (out / "wide.mp4").exists()):
        return out
    out.mkdir(parents=True, exist_ok=True)
    srcA = _dec(REELS["A"])
    srcB = _dec(REELS["B"], f"asetrate={SR}*{PITCH_B},aresample={SR},atempo={1 / PITCH_B:.6f}" if variant == "distinct" else None)
    ua, ub = utterances(srcA), utterances(_dec(REELS["B"]))
    place = plan_conversation(ua, ub, seed)
    dur = math.ceil((max(p["t1"] for p in place) + 0.6) * FPS) / FPS
    A, B = _track(place, "A", srcA, dur), _track(place, "B", srcB, dur)
    rng = np.random.default_rng(seed + 1)
    from scipy.signal import butter, sosfilt
    room = (A + B) * 0.55
    room = sosfilt(butter(2, [120 / (SR / 2), 6500 / (SR / 2)], btype="band", output="sos"), room).astype(np.float32)
    noise = lambda n, lvl: (rng.standard_normal(n) * lvl).astype(np.float32)  # noqa: E731
    files = {}
    for name, sig, extra in (("micA", A + 0.14 * B, 0.0), ("micB", B + 0.16 * A, 0.0)):
        off, dr = OFFSETS[name], DRIFT.get(name, 0.0)
        span = dur - off + (1.0 if name == "micA" else 0.0)
        x = _file_signal(sig, off, dr, span)
        x += noise(len(x), 0.0015)
        _write_wav(out / f"{name}.wav", x)
        files[name] = {"offset": off, "drift_ppm": dr * 1e6, "duration": round(len(x) / SR, 3)}
    truth = {"variant": variant, "duration": dur, "fps": FPS, "pitch_b": PITCH_B if variant == "distinct" else None,
             "reels": {k: str(v) for k, v in REELS.items()}, "utterances": place, "files": files,
             "note": __doc__.split("\n\n")[1] if __doc__ else ""}
    if video:
        for name, spk, reel in (("camA", "A", REELS["A"]), ("camB", "B", REELS["B"])):
            off = OFFSETS[name]
            t_to = dur + (0.8 if name == "camA" else 0.0)
            scratch = _file_signal(room, off, 0.0, t_to - off) + noise(int(round((t_to - off) * SR)), 0.003)
            wav = out / f"{name}.scratch.wav"
            _write_wav(wav, scratch)
            _render_person(reel, _video_edl(place, spk, off, t_to), wav, out / f"{name}.mp4")
            wav.unlink(missing_ok=True)
            files[name] = {"offset": off, "drift_ppm": 0.0, "duration": round(t_to - off, 3)}
        # 4K two-shot: both people side by side on a dark set, from the camera files (shifted onto the wide's clock)
        off = OFFSETS["wide"]
        wdur = dur - off
        scratch = _file_signal(room, off, 0.0, wdur) + noise(int(round(wdur * SR)), 0.003)
        wav = out / "wide.scratch.wav"
        _write_wav(wav, scratch)
        sa = off - OFFSETS["camA"]          # wide t=0 is camA t=sa
        sb = OFFSETS["camB"] - off          # camB starts sb seconds into the wide
        fc = (f"color=c=0x1b1d24:s=3840x2160:r={FPS}:d={wdur:.4f},format=yuv420p,"
              f"drawbox=x=0:y=1500:w=3840:h=660:color=0x2a2d38:t=fill[bg];"
              f"[0:v]trim=start={sa:.4f},setpts=PTS-STARTPTS,scale=1215:2160[a];"
              f"[1:v]tpad=start_duration={sb:.4f}:start_mode=clone,scale=1215:2160[b];"
              f"[bg][a]overlay=x=520:y=0:shortest=0:eof_action=repeat[t];[t][b]overlay=x=2105:y=0:eof_action=repeat[v]")
        run([tools().ffmpeg, "-v", "error", "-y", "-i", str(out / "camA.mp4"), "-i", str(out / "camB.mp4"), "-i", str(wav),
             "-filter_complex", fc, "-map", "[v]", "-map", "2:a", "-t", f"{wdur:.4f}", "-r", str(FPS),
             "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-c:a", "aac", "-b:a", "160k", str(out / "wide.mp4")])
        wav.unlink(missing_ok=True)
        files["wide"] = {"offset": off, "drift_ppm": 0.0, "duration": round(wdur, 3),
                         "layout": {"A_face_x": 520 + 607, "B_face_x": 2105 + 607}}
    tj.write_text(json.dumps(truth, indent=1), encoding="utf-8")
    return out


def truth_turns(truth: dict) -> list[dict]:
    """Utterances as frame-label turns for scoring (A -> 'A', B -> 'B'); back-channels overlap the speaker."""
    return [{"speaker": u["speaker"], "t0": u["t0"], "t1": u["t1"], "kind": u["kind"]} for u in truth["utterances"]]


def truth_frames(truth: dict, hop: float = 0.01, offset: float = 0.0) -> np.ndarray:
    """[T] reference label per frame (0 = A, 1 = B, -1 silence); where both talk, the main (non-back-channel) speaker.
    `offset` shifts truth (session time) into the evaluated timeline (e.g. the master's)."""
    dur = truth["duration"] + max(0.0, offset) + 1.0
    T = int(math.ceil(dur / hop))
    y = np.full(T, -1)
    for u in sorted(truth["utterances"], key=lambda u: u["kind"] == "speech"):  # speech last: it wins in overlaps
        a, b = int(round((u["t0"] + offset) / hop)), int(round((u["t1"] + offset) / hop))
        y[max(0, a):max(0, b)] = 0 if u["speaker"] == "A" else 1
    return y


def evaluate(project_root: Path, truth: dict, shift: float) -> dict:
    """Score a project built from this fixture. `shift` = truth time - master time (session 0 vs the master's 0).
    -> word accuracy (speaker of the truth utterance under each word's midpoint), DER, handover-cut errors."""
    from . import diarize as D
    from .core import read_json
    pr = Path(project_root)
    spk = read_json(pr / "work" / "speakers.json")
    words = read_json(pr / "work" / "words" / f"{spk['master']}.json")["words"]
    utts = truth["utterances"]

    def truth_at(t: float):
        hits = [u for u in utts if u["t0"] <= t < u["t1"]]
        if not hits:
            return None
        main = [u for u in hits if u["kind"] == "speech"] or hits
        return main[0]["speaker"]

    pairs = [(truth_at((w["s"] + w["e"]) / 2 + shift), w.get("speaker")) for w in words]
    pairs = [(a, b) for a, b in pairs if a and b]
    ids = sorted({b for _, b in pairs})
    best, mapping = -1, {}
    import itertools
    for perm in itertools.permutations(["A", "B"], len(ids)):
        m = dict(zip(ids, perm))
        ok = sum(1 for a, b in pairs if m[b] == a)
        if ok > best:
            best, mapping = ok, m
    ref = truth_frames(truth, offset=-shift)
    hyp = np.full(len(ref), -1)
    idx = {sid: k for k, sid in enumerate(ids)}
    for sid, segs in spk["segments"].items():
        for a, b in segs:
            hyp[int(a / 0.01):int(b / 0.01)] = idx.get(sid, -1)
    n = min(len(ref), len(hyp))
    der = D.speaker_error(ref[:n], hyp[:n], 2, len(ids))
    out = {"words": len(pairs), "word_accuracy": round(best / max(1, len(pairs)), 4),
           "mapping": mapping, "der": der["der"], "confusion": der["confusion"], "miss": der["miss"],
           "false_alarm": der["false_alarm"], "mode": spk["mode"]}
    cm_p, sh_p = pr / "work" / "cutmap.json", pr / "plan" / "shots.json"
    if cm_p.exists() and sh_p.exists():
        cm = read_json(cm_p)
        seg = cm["segments"][0]
        e2t = lambda te: seg["in"] + te + shift  # noqa: E731 (single-segment EDL: edit -> truth time)
        cuts = [e2t(s["t0"]) for s in read_json(sh_p)["shots"][1:]]
        speech = sorted([u for u in utts if u["kind"] == "speech"], key=lambda u: u["t0"])
        hand = [b["t0"] for a, b in zip(speech, speech[1:]) if a["speaker"] != b["speaker"]]
        lo, hi = e2t(0), e2t(cm["duration"])
        err = [min(abs(c - h) for c in cuts) for h in hand if lo + 0.5 < h < hi - 0.5]
        out["handovers"] = len(err)
        out["handover_cut_within_3f"] = round(sum(1 for e in err if e <= 0.1 + 1e-6) / max(1, len(err)), 3)
        out["handover_cut_median_ms"] = round(float(np.median(err)) * 1000, 1) if err else None
    return out
