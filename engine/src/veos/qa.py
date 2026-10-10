"""`veos qa <final.mp4>`: container, fps, frame count, colour, audio, loudness, black tail, sync and a contact sheet."""
from __future__ import annotations

import json
import re
from pathlib import Path

import numpy as np

from .audio import SR, decode_mono, loudness
from .core import FPS, VeosError, r3, run, tools


def _probe(path: Path, count: bool) -> dict:
    cmd = [tools().ffprobe, "-v", "error", "-show_format", "-show_streams", "-of", "json"]
    if count:
        cmd.insert(3, "-count_frames")
    r = run(cmd + [str(path)], check=False)
    if r.returncode != 0:
        raise VeosError("PROBE_FAILED", f"ffprobe could not read {path.name}", "The file may be corrupt or still rendering.")
    return json.loads(r.stdout.decode("utf-8", "replace"))


def _black_tail(path: Path, vdur: float) -> float:
    """Seconds of black at the very end of the video (0 if none)."""
    r = run([tools().ffmpeg, "-nostats", "-hide_banner", "-i", str(path), "-an", "-vf", "blackdetect=d=0.04:pix_th=0.10",
             "-f", "null", "-"], check=False)
    err = (r.stderr or b"").decode("utf-8", "replace")
    tail = 0.0
    for m in re.finditer(r"black_start:([\d.]+)\s+black_end:([\d.]+)", err):
        s, e = float(m.group(1)), float(m.group(2))
        if e >= vdur - 0.05:
            tail = max(tail, vdur - s)
    return r3(tail)


def _xcorr_lag(ref: np.ndarray, y: np.ndarray, s0: int, win: int, maxlag: int):
    """Lag (samples) at which y best matches ref[s0:s0+win]; returns (lag, normalised corr) or None if silent."""
    from scipy.signal import fftconvolve
    seg = ref[s0:s0 + win].astype(np.float64)
    a, b = s0 - maxlag, s0 + len(seg) + maxlag
    pad_l, pad_r = max(0, -a), max(0, b - len(y))
    ys = np.pad(y[max(0, a):min(len(y), b)].astype(np.float64), (pad_l, pad_r))
    if np.linalg.norm(seg) < 1e-6 or np.linalg.norm(ys) < 1e-6:
        return None
    c = fftconvolve(ys, seg[::-1], mode="valid")  # length 2*maxlag+1
    cs = np.concatenate([[0], np.cumsum(ys ** 2)])
    en = np.sqrt(np.maximum(cs[len(seg):len(seg) + len(c)] - cs[:len(c)], 1e-12))
    nc = c / (en * np.linalg.norm(seg))
    k = int(np.argmax(nc))
    # parabolic refinement for sub-sample accuracy is unnecessary at 48 kHz
    return k - maxlag, float(nc[k])


def sync_check(ref_path: Path, test_path: Path) -> dict:
    ref, y = decode_mono(ref_path), decode_mono(test_path)
    n = min(len(ref), len(y))
    win = int(min(8.0, 0.3 * n / SR) * SR)
    maxlag = int(0.1 * SR)
    lags, corrs = [], []
    for frac in (0.15, 0.5, 0.85):
        s0 = min(max(0, int(n * frac)), max(0, n - win - maxlag))
        got = _xcorr_lag(ref, y, s0, win, maxlag)
        if got:
            lags.append(got[0] / SR * 1000)
            corrs.append(got[1])
    if not lags:
        return {"lags_ms": [], "corr": [], "ok": False, "detail": "audio too quiet to correlate"}
    spread = max(lags) - min(lags)
    ok = max(abs(x) for x in lags) < 1000 / FPS and spread < 1000 / FPS / 2 and min(corrs) > 0.3
    return {"lags_ms": [round(x, 1) for x in lags], "corr": [round(c, 3) for c in corrs], "spread_ms": round(spread, 1), "ok": ok}


def contact_sheet(path: Path, out: Path, dur: float, tiles: int = 12, w: int = 216, cols: int = 6) -> Path:
    rows = (tiles + cols - 1) // cols
    out.parent.mkdir(parents=True, exist_ok=True)
    # sample at the centre of 12 equal slices of the video, decoded from the file itself
    vf = f"fps={tiles}/{max(dur, 0.1):.4f}:round=down,scale={w}:-2,tile={cols}x{rows}:padding=4:margin=4:color=0x101010"
    run([tools().ffmpeg, "-y", "-v", "error", "-i", str(path), "-vf", vf, "-frames:v", "1", "-update", "1",
         "-q:v", "3", str(out)])
    return out


def main(args, project) -> dict:
    final = Path(args.final)
    if not final.exists():
        raise VeosError("FILE_MISSING", f"not found: {final}", "Pass the path of the finished MP4.")
    try:
        want_w, want_h = (int(x) for x in args.size.lower().split("x"))
    except ValueError as e:
        raise VeosError("BAD_SIZE", f"bad --size {args.size}", "Use WxH, e.g. 1080x1920.") from e
    pr = _probe(final, count=True)
    vs = next((s for s in pr["streams"] if s["codec_type"] == "video"), None)
    au = next((s for s in pr["streams"] if s["codec_type"] == "audio"), None)
    if not vs:
        raise VeosError("NO_VIDEO", "no video stream in the file", "This is not a finished video.")
    checks: list[dict] = []
    from .novoice import is_no_voice
    no_voice = is_no_voice(project)  # nobody speaks: no voice to sync against

    def add(name: str, ok: bool, value, need: str = "") -> None:
        checks.append({"check": name, "pass": bool(ok), "value": value, "need": need})

    add("codec", vs.get("codec_name") == "h264", vs.get("codec_name"), "h264")
    add("pixel format", vs.get("pix_fmt") == "yuv420p", vs.get("pix_fmt"), "yuv420p")
    add("size", (vs["width"], vs["height"]) == (want_w, want_h), f"{vs['width']}x{vs['height']}", f"{want_w}x{want_h}")
    num, den = (int(x) for x in vs.get("r_frame_rate", "0/1").split("/"))
    fps = num / den if den else 0.0
    ann, dnn = (int(x) for x in vs.get("avg_frame_rate", "0/1").split("/"))
    avg = ann / dnn if dnn else 0.0
    add("fps", abs(fps - FPS) < 0.001 and abs(avg - FPS) < 0.01, f"{fps:g} (avg {avg:.3f})", str(FPS))
    frames = int(vs.get("nb_read_frames") or vs.get("nb_frames") or 0)
    vdur = float(vs.get("duration") or pr["format"].get("duration") or 0)
    if args.expect_frames is not None:
        exp, how = args.expect_frames, "expected"
    else:
        exp, how = int(round(vdur * FPS)), "round(duration*30)"
    add("frame count", frames == exp, frames, f"{exp} ({how})")
    tags = (vs.get("color_primaries"), vs.get("color_transfer"), vs.get("color_space"))
    add("colour tags bt709", all(t == "bt709" for t in tags), "/".join(str(t) for t in tags), "bt709/bt709/bt709")
    if au:
        add("audio stereo 48 kHz", au.get("channels") == 2 and int(au.get("sample_rate", 0)) == SR,
            f"{au.get('channels')}ch {au.get('sample_rate')} Hz", "2ch 48000 Hz")
        L = loudness(final)
        if no_voice and L["lufs"] <= -70:  # a no-voice reel cut with no sound at all (cut --audio none, no effects)
            add("loudness", True, "silent (no-voice reel without sound)", "-14 +/-1")
        else:
            add("loudness", abs(L["lufs"] - (-14)) <= 1.0, f"{L['lufs']} LUFS", "-14 +/-1")
            add("true peak", L["tp"] <= -1.5, f"{L['tp']} dBTP", "<= -1.5")
        adur = float(au.get("duration") or 0)
        add("audio/video length", abs(adur - vdur) <= 0.05, f"audio {adur:.3f}s vs video {vdur:.3f}s", "within 50 ms")
    else:
        add("audio stereo 48 kHz", False, "no audio stream", "2ch 48000 Hz")
    tail = _black_tail(final, vdur)
    add("black tail", tail <= 0.2, f"{tail:.2f} s", "<= 0.2 s")
    if args.ref_audio and not no_voice:
        ref = Path(args.ref_audio)
        if not ref.exists():
            raise VeosError("FILE_MISSING", f"reference audio not found: {ref}", "Check --ref-audio.")
        if au:
            sc = sync_check(ref, final)
            add("sync vs reference", sc["ok"], f"lags {sc['lags_ms']} ms", "constant, < 33 ms")

    if project is not None:
        report = project.path("out", "qa-report.md")
        sheet = project.path("out", "qa-sheet.jpg")
    else:
        report = final.with_suffix(".qa.md")
        sheet = final.with_suffix(".sheet.jpg")
    contact_sheet(final, sheet, vdur)

    passed = [c for c in checks if c["pass"]]
    failed = [c for c in checks if not c["pass"]]
    lines = [f"# QA report: {final.name}", "", f"**{len(passed)}/{len(checks)} checks passed**"
             + ("" if not failed else ", failing: " + ", ".join(c["check"] for c in failed)), "",
             "| Check | Result | Value | Required |", "|---|---|---|---|"]
    for c in checks:
        lines.append(f"| {c['check']} | {'PASS' if c['pass'] else '**FAIL**'} | {c['value']} | {c['need']} |")
    lines += ["", f"Duration {vdur:.3f} s, {frames} frames.", "", f"Contact sheet (decoded from the file): `{sheet.name}`",
              "", f"![contact sheet]({sheet.name})", ""]
    report.write_text("\n".join(lines), encoding="utf-8")
    rel = project.rel if project is not None else (lambda p: Path(p).as_posix())
    return {"pass": len(passed), "total": len(checks), "fail": [f"{c['check']}: {c['value']} (need {c['need']})" for c in failed],
            "all_pass": not failed, "report": rel(report), "sheet": rel(sheet), "frames": frames, "duration": r3(vdur),
            **({"sync": "skipped: no-voice reel (no voice to sync)"} if no_voice and args.ref_audio else {})}


def add_args(p, cmd: str) -> None:
    p.add_argument("final", help="finished MP4 to check")
    p.add_argument("--expect-frames", type=int, default=None, help="expected frame count (default round(duration*30))")
    p.add_argument("--ref-audio", default=None, help="reference WAV (source voice) for the sync check")
    p.add_argument("--size", default="1080x1920", help="expected WxH")
