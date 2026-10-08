"""`veos look`: look at the cut before planning it (a fast overview pass), and close looks on demand.

    veos look --project P                              overview of the cut (edit time, after the rough cut)
    veos look --project P --at 12.4-13.6               close look: every frame (span <= 1 s) or every 2nd frame (<= 2 s)
    veos look --project P --at 12.4,13.0,13.5          close look: just these moments
    veos look --project P --src A --at 3.1,3.6,4.0     the same on a raw clip (a source id or a video file), source time

**Overview: frames are picked by meaning, not by the clock.** Candidates:
  * one frame per sentence, on its key content word (the longest / most content-bearing non-stopword; numbers and names
    weigh more, fillers and function words never count);
  * one frame just after every cut or take change (the cut map's segments and the sources' own setup changes);
  * the peaks of a cheap frame-difference signal (ONE gray decode of the cut proxy, 160 px wide at 10 fps), so a prop
    raised, a screen appearing or a big gesture between sentences is not missed; the frame sits where the movement
    settles, so it shows the result;
  * gap fill: no gap between chosen frames longer than GAP_MAX (2.5 s).
Frames closer than DEDUPE_S (0.6 s) inside one shot are merged (sentence > cut > motion > gap; the reasons are kept), so
motion peaks yield to sentence frames. That gives about one frame per 1.5-2 s; a cap of duration / 1.2 only bounds
pathological input. The chosen frames come out of ONE more decode of the proxy (an ffmpeg select), straight into the
sheets: two ffmpeg processes in all, never one per frame.

Writes review/look/sheet_NN.jpg (4 x 4 tiles, 270 px wide; each tile labelled with its number, timecode, why it was
picked and a few words of what is said there; tiles just after a cut have a yellow frame) and review/look/look.json:

LOOK FORMAT (version 1; one frame / sentence / cut per line)
  {"version": 1, "duration", "fps", "video": "work/cut_proxy.mp4", "note",
   "frames": [{"n", "t", "f", "why": ["sentence"|"cut"|"motion"|"gap", ...], "sentence": id|null, "after_cut",
               "sheet", "tile", "src", "setup", "shot": "tight"|"medium"|"wide"|"none", "face": [x, y, w, h]|null,
               "face_h", "motion", "motion_level", "said"}],
   "sentences": [{"id", "t0", "t1", "text", "key", "key_t", "i0", "i1", "pause_after"}],
   "cuts": [{"t", "src", "setup", "kind": "start"|"take"|"setup"}],
   "motion": {"fps", "unit", "levels", "per_s": [mean per second], "max_s": [max per second], "peaks": [{"t", "v"}]}}
  `face` is the face box in edit-frame px (1080 x 1920, before any reframe), `face_h` its height / 1920; `shot` comes
  from it (tight >= 0.30 = framing.CLOSE, medium >= 0.15, else wide); `setup` is the source's own setup (selfie /
  tripod / ...). `motion` is the mean absolute gray difference to the previous sample (0-255, 160 px, 10 fps);
  `motion_level` still < 1.5 <= low < 4 <= medium < 8 <= high.

Close looks (`--at`) write review/look/at_<span>.jpg (edit time, from the cut proxy) or review/look/<src>_at_<span>.jpg
(a raw clip: work/src/<id>.mp4 for a source id, else the file), each tile labelled with its time, frame and the word
spoken there. Ranges are capped at 2 s (AT_MAX_S); lists at 30 moments.
"""
from __future__ import annotations

import bisect
import json
import math
import os
import re
import subprocess
import time
import unicodedata
from pathlib import Path

import numpy as np

from .core import FPS, VeosError, need_project, r3, read_json, tools

# ---------------------------------------------------------------- tunables
GAP_MAX = 2.5        # s: no gap between chosen frames longer than this
DEDUPE_S = 0.6       # s: frames closer than this inside one shot are merged
CAP_DIV = 1.2        # safety cap: at most duration / CAP_DIV frames (bounds pathological input only)
CAP_MIN = 8
CUT_AFTER = 0.2      # s: the "after the cut" frame sits this far into the new shot (at most half the shot)
KEY_LEAD = 0.2       # s: a sentence frame sits on its key word's onset + min(KEY_LEAD, half the word)
PRIORITY = {"sentence": 0, "cut": 1, "motion": 2, "gap": 3}

PAUSE_S = 0.5        # s: a pause this long ends a sentence
MAX_SENT_S = 5.0     # s: longer "sentences" split at their best inner boundary (a comma, the longest pause)
END_RE = re.compile(r"[.!?।॥…]+[\"'”’»)\]]*$")
SOFT_RE = re.compile(r"[,;:–—]+[\"'”’»)\]]*$")

MOTION_FPS = 10      # samples per second of the frame-difference signal
MOTION_W = 160       # px width of the gray analysis decode
PEAK_K = 2.5         # a peak is above median + PEAK_K * robust sigma (1.4826 * MAD) ...
PEAK_MIN = 4.0       # ... and never below this (mean |diff| in gray levels)
PEAK_WIN_S = 0.5     # s: a peak is the largest sample within +-PEAK_WIN_S
PEAK_GAP_S = 1.0     # s: of two peaks closer than this, the stronger one wins
SETTLE_S = 0.6       # s: a motion frame sits where the movement falls below half its peak, at most this late
CUT_MASK_S = 0.05    # s: samples whose difference spans a cut are not motion
LEVELS = ((1.5, "still"), (4.0, "low"), (8.0, "medium"), (float("inf"), "high"))

TIGHT, MEDIUM = 0.30, 0.15   # face height / frame height (framing.CLOSE = 0.30: a face already close)
FW, FH = 1080, 1920

TILE_W, COLS, PER, LABEL_H = 270, 4, 16, 40
AT_MAX_S, AT_MAX_N = 2.0, 30
WHY_COLOUR = {"sentence": (255, 255, 255), "cut": (255, 214, 0), "motion": (0, 205, 255), "gap": (165, 165, 165)}
CUT_COLOUR = (255, 214, 0)

# function words and fillers never carry a sentence (English, romanised Hindi / Hinglish, Devanagari)
STOP = set("""
a an the and or but so to of in on at for with from by as is are was were be been being am do does did done have has had
it its it's this that these those i i'm you you're he she we they me my your our their him her them us what which who
whom whose when where why how not no yes if then than just very really also too can could will would shall should may
might must about into over under up down out off again more most some any all each every there here now only own same
such both few other ok okay um uh umm hmm mm like basically actually literally right yeah yep well oh hey guys get got
let let's gonna wanna one thing things way
hai hain ho hoga hogi honge hote hota hoti tha thi the thhe ke ka ki ko se me mein mai main mujhe mera meri mere hum ham
humne hamara humara tum tumhe tumko tumhara tumhari tumhare tu tera teri tere aap aapka aapki apna apne apni ye yeh yah
wo woh vo voh unka uska uski iska iski isko usko inhe unhe aur ya jo jab tab kya kyu kyun kyon kaise kaisa kaun kahan
kab yaha yahan waha wahan isse usse iss us is un in kar karo kare karna karke karte karta karti kiya kiye diya diye de do
dena deta dete deti di dunga dungi le lo lena leta liya liye lie wala wali wale waala waali waale bhi hi nahi nahin nhi
mat koi kuch sab ek eek pe par tak ne rahe raha rahi gaya gayi gaye ja jao jaa jaake jake ab phir fir abhi bahut bohot
bahot zyada jyada kam sirf toh to na haan han ha accha acha achha matlab bas arey arre are yaar bhai bro dekho chalo
है हैं हो होगा था थी थे के का की को से में मैं मुझे मेरा मेरी मेरे हम हमारा तुम तुम्हें तुम्हारा तुम्हारी आप अपना अपने अपनी यह ये वो
वह उस इस उसे इसे उनका उसका इसका और या जो जब तब क्या क्यों कैसे कौन कहाँ कर करो करे करना करके करते करता करती किया दिया दे दो
देना दूँगा दूंगा ले लो लिया लिए वाला वाली वाले भी ही नहीं मत कोई कुछ सब एक पे पर तक ने रहे रहा रही गया गई गए जा अब फिर
अभी बहुत ना तो हाँ अच्छा मतलब बस यार भाई
""".split())


# ---------------------------------------------------------------- args
def add_args(p, cmd):
    p.add_argument("--at", default=None,
                   help="close look: 'T0-T1' (<= 2 s: every frame up to 1 s, else every 2nd) or 'T1,T2,...' (<= 30 moments)")
    p.add_argument("--src", default=None,
                   help="with --at: a raw clip (source id from sources.json, or a video file); times are its own seconds")
    p.add_argument("--workers", type=int, default=None,
                   help="ffmpeg decode threads (default min(4, max(1, cpus//4)), or VEOS_WORKERS)")


def _threads(args) -> int:
    return (getattr(args, "workers", None) or int(os.environ.get("VEOS_WORKERS") or 0)
            or min(4, max(1, (os.cpu_count() or 2) // 4)))


# ---------------------------------------------------------------- words and sentences
def _text(w: dict) -> str:
    """What the creator sees for a word: its caption when set ("" = hidden), else the transcript word."""
    c = w.get("caption")
    return c if isinstance(c, str) else str(w.get("w") or "")


def norm(raw: str) -> str:
    """Lower-case letters, marks and digits only (punctuation and quotes dropped); keeps the rupee and per-cent signs."""
    return "".join(ch for ch in str(raw).lower() if unicodedata.category(ch)[0] in "LMN" or ch in "₹%")


def key_word(ws: list[dict]) -> dict:
    """The most content-bearing word of a sentence: the longest non-stopword, numbers +6, a capitalised word inside the
    sentence (a name, a brand) +2. Earliest wins ties. All function words -> the longest word."""
    best, bw = None, None
    for k, w in enumerate(ws):
        raw = _text(w) or str(w.get("w") or "")
        t = norm(raw)
        if not t or t in STOP:
            continue
        score = len(t)
        if any(ch.isdigit() for ch in t) or "₹" in raw or "%" in raw:
            score += 6
        if k > 0 and raw[:1].isupper():
            score += 2
        if best is None or score > best:
            best, bw = score, w
    if bw is None:
        bw = max(ws, key=lambda w: len(norm(_text(w) or str(w.get("w") or ""))))
    return bw


def _ends(w: dict) -> bool:
    return bool(END_RE.search(str(w.get("w") or "")) or END_RE.search(_text(w)))


def _soft(w: dict) -> bool:
    return bool(SOFT_RE.search(str(w.get("w") or "")) or SOFT_RE.search(_text(w)))


def _split_long(g: list[dict], max_s: float) -> list[list[dict]]:
    if len(g) < 4 or g[-1]["e"] - g[0]["s"] <= max_s:
        return [g]
    t0, t1 = g[0]["s"], g[-1]["e"]
    best, bj = None, 2
    for j in range(2, len(g) - 1):  # both halves keep >= 2 words
        a, b = g[j - 1], g[j]
        score = 4.0 * max(0.0, b["s"] - a["e"]) + (1.0 if _soft(a) else 0.0)
        score -= 0.5 * abs((a["e"] - t0) / max(1e-6, t1 - t0) - 0.5)  # prefer the middle
        if best is None or score > best:
            best, bj = score, j
    return _split_long(g[:bj], max_s) + _split_long(g[bj:], max_s)


def sentences(words: list[dict], pause: float = PAUSE_S, max_s: float = MAX_SENT_S) -> list[dict]:
    """Edit-time words -> sentences: end on . ? ! । … or a pause >= `pause`; longer than `max_s` -> split at a comma /
    the longest pause. Each: {id, t0, t1, text, key, key_t, i0, i1, pause_after}."""
    ws = sorted((w for w in words if isinstance(w.get("s"), (int, float)) and isinstance(w.get("e"), (int, float))),
                key=lambda w: (w["s"], w["e"]))
    groups, cur = [], []
    for k, w in enumerate(ws):
        cur.append(w)
        nxt = ws[k + 1] if k + 1 < len(ws) else None
        if nxt is None or _ends(w) or nxt["s"] - w["e"] >= pause:
            groups.append(cur)
            cur = []
    out: list[dict] = []
    for g in (x for grp in groups for x in _split_long(grp, max_s)):
        kw = key_word(g)
        kt = kw["s"] + min(KEY_LEAD, max(0.0, kw["e"] - kw["s"]) / 2)
        out.append({"id": len(out), "t0": r3(g[0]["s"]), "t1": r3(g[-1]["e"]),
                    "text": " ".join(t for t in (_text(w) for w in g) if t),
                    "key": _text(kw) or str(kw.get("w") or ""), "key_t": r3(kt),
                    "i0": g[0].get("i"), "i1": g[-1].get("i"), "pause_after": None})
    for a, b in zip(out, out[1:]):
        a["pause_after"] = r3(max(0.0, b["t0"] - a["t1"]))
    return out


def said_near(words: list[dict], t: float, n: int = 4, max_chars: int = 30, around: float = 0.6) -> str:
    """A few words spoken around `t` (centred on the nearest word), or '' in a pause."""
    ws = [w for w in words if _text(w)]
    if not ws:
        return ""
    k = min(range(len(ws)), key=lambda i: 0.0 if ws[i]["s"] <= t <= ws[i]["e"] else min(abs(ws[i]["s"] - t), abs(ws[i]["e"] - t)))
    w = ws[k]
    if not (w["s"] - around <= t <= w["e"] + around):
        return ""
    lo = max(0, k - n // 2)
    picked = ws[lo:lo + n]
    txt = " ".join(_text(x) for x in picked)
    return txt if len(txt) <= max_chars else txt[:max_chars - 1].rstrip() + "…"


# ---------------------------------------------------------------- cuts
def cut_points(cut: dict, sources: dict) -> list[dict]:
    """Shot starts in edit time: the reel start, every cut-map segment start (a take change) and every setup change inside
    a source (sources.json segments). Each: {t, src, setup, kind: start | take | setup}."""
    from .context import _edit_setups
    pts = [{"t": r3(seg["t0"]), "src": seg["src"], "kind": "start" if k == 0 else "take"}
           for k, seg in enumerate(cut.get("segments") or [])]
    starts = {round(p["t"], 2) for p in pts}
    spans = _edit_setups(cut, sources)
    for a, _b, tag in spans:
        if round(a, 2) not in starts:
            pts.append({"t": r3(a), "src": tag.split(":")[0], "kind": "setup"})
    pts.sort(key=lambda p: p["t"])
    for p in pts:
        p["setup"] = setup_at(spans, p["t"] + 1e-3)
    return pts


def setup_at(spans: list, t: float) -> str | None:
    for a, b, tag in spans:
        if a <= t < b:
            return tag.split(":", 1)[1] if ":" in tag else tag
    return spans[-1][2].split(":", 1)[-1] if spans and t >= spans[-1][1] else None


# ---------------------------------------------------------------- motion
def motion_signal(path: Path, size: tuple[int, int], threads: int, fps: int = MOTION_FPS,
                  width: int = MOTION_W) -> tuple[np.ndarray, np.ndarray]:
    """(times, values): mean |gray difference| to the previous sample, from ONE ffmpeg decode at `width` px and `fps`.
    The analysis decode skips H.264 deblocking (`-skip_loop_filter all`): ~30 % faster, irrelevant at 160 px."""
    w = width - width % 2
    h = max(2, round(size[1] * w / max(1, size[0]) / 2) * 2)
    cmd = [tools().ffmpeg, "-v", "error", "-threads", str(threads), "-skip_loop_filter", "all", "-i", str(path),
           "-an", "-sn", "-vf", f"fps={fps},scale={w}:{h}:flags=area", "-pix_fmt", "gray", "-f", "rawvideo", "-"]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    prev, vals = None, []
    try:
        while True:
            buf = p.stdout.read(w * h)
            if len(buf) < w * h:
                break
            a = np.frombuffer(buf, np.uint8).astype(np.int16)
            vals.append(0.0 if prev is None else float(np.abs(a - prev).mean()))
            prev = a
    finally:
        p.stdout.close()
        p.wait()
    v = np.array(vals, dtype=float)
    return np.arange(len(v)) / fps, v


def mask_cuts(times: np.ndarray, vals: np.ndarray, cut_times: list[float], fps: int = MOTION_FPS) -> np.ndarray:
    """Zero the samples whose difference spans a cut (a cut is a cut, not motion)."""
    v = vals.copy()
    for tc in cut_times:
        hit = (times - 1.0 / fps - CUT_MASK_S < tc) & (tc <= times + CUT_MASK_S)
        v[hit] = 0.0
    return v


def motion_peaks(times: np.ndarray, vals: np.ndarray, fps: int = MOTION_FPS) -> list[dict]:
    """Bursts of movement: local maxima above max(PEAK_MIN, median + PEAK_K * robust sigma), one per PEAK_GAP_S.
    Each: {t (where the movement settles: below half the peak, at most SETTLE_S later), peak_t, v}."""
    n = len(vals)
    if n < 3:
        return []
    med = float(np.median(vals))
    sigma = 1.4826 * float(np.median(np.abs(vals - med)))
    thr = max(PEAK_MIN, med + PEAK_K * sigma)
    win, gap, settle = int(round(PEAK_WIN_S * fps)), PEAK_GAP_S, int(round(SETTLE_S * fps))
    cand = [k for k in range(n) if vals[k] >= thr and vals[k] == vals[max(0, k - win):k + win + 1].max()]
    kept: list[int] = []
    for k in sorted(cand, key=lambda k: (-vals[k], k)):
        if all(abs(times[k] - times[j]) >= gap for j in kept):
            kept.append(k)
    out = []
    for k in sorted(kept):
        j = k
        while j < min(n - 1, k + settle) and vals[j] >= 0.5 * vals[k]:
            j += 1
        out.append({"t": r3(times[j]), "peak_t": r3(times[k]), "v": round(float(vals[k]), 1)})
    return out


def per_second(times: np.ndarray, vals: np.ndarray, duration: float) -> tuple[list[float], list[float]]:
    secs = max(1, int(math.ceil(duration - 1e-6)))
    mean, mx = [], []
    for s in range(secs):
        sel = vals[(times >= s) & (times < s + 1)]
        mean.append(round(float(sel.mean()), 1) if sel.size else 0.0)
        mx.append(round(float(sel.max()), 1) if sel.size else 0.0)
    return mean, mx


def level(v: float) -> str:
    return next(name for lim, name in LEVELS if v < lim)


# ---------------------------------------------------------------- frame selection (pure)
def select_frames(duration: float, sents: list[tuple[float, int]], cuts: list[float], peaks: list[dict], *,
                  gap_max: float = GAP_MAX, dedupe: float = DEDUPE_S, cap_div: float = CAP_DIV) -> list[dict]:
    """Pick the overview frames. sents: [(key time, sentence id)]; cuts: shot start times (the reel start included; a
    frame goes min(CUT_AFTER, half the shot) into each); peaks: [{t, v}] motion peaks.

    Candidates closer than `dedupe` inside one shot merge into the higher-priority one (sentence > cut > motion > gap;
    stronger motion first), keeping every reason. Then gaps longer than `gap_max` (from 0 to the end) get evenly spaced
    fill frames. A cap of max(CAP_MIN, duration / cap_div) drops the lowest-priority frames of pathological input.
    Returns [{t, why, sentence, after_cut}] sorted by time."""
    last = max(0.0, duration - 1.0 / FPS)
    bounds = sorted({float(c) for c in cuts if 0.0 <= c < duration})

    def shot(t: float) -> int:
        return bisect.bisect_right(bounds, t + 1e-9)

    cands = [{"t": min(last, max(0.0, float(t))), "why": ["sentence"], "sentence": sid, "after_cut": False, "score": 0.0}
             for t, sid in sents if 0.0 <= t <= duration]
    for k, c in enumerate(bounds):
        nxt = bounds[k + 1] if k + 1 < len(bounds) else duration
        cands.append({"t": min(last, c + min(CUT_AFTER, max(0.0, nxt - c) / 2)), "why": ["cut"], "sentence": None,
                      "after_cut": True, "score": 0.0})
    for pk in peaks:
        if 0.0 <= pk["t"] <= duration:
            cands.append({"t": min(last, float(pk["t"])), "why": ["motion"], "sentence": None, "after_cut": False,
                          "score": float(pk.get("v", 0.0))})
    cands.sort(key=lambda c: (PRIORITY[c["why"][0]], -c["score"], c["t"]))
    kept: list[dict] = []
    for c in cands:
        s = shot(c["t"])
        hit = next((k for k in kept if shot(k["t"]) == s and abs(k["t"] - c["t"]) < dedupe), None)
        if hit is None:
            kept.append(c)
            continue
        for w in c["why"]:
            if w not in hit["why"]:
                hit["why"].append(w)
        hit["after_cut"] = hit["after_cut"] or c["after_cut"]
        if hit["sentence"] is None and c["sentence"] is not None:
            hit["sentence"] = c["sentence"]
    kept.sort(key=lambda c: c["t"])
    edges = [0.0] + [c["t"] for c in kept] + [duration]
    fills = []
    for a, b in zip(edges, edges[1:]):
        if b - a > gap_max + 1e-9:
            n = math.ceil((b - a) / gap_max - 1e-9) - 1
            fills += [{"t": min(last, a + (b - a) * i / (n + 1)), "why": ["gap"], "sentence": None, "after_cut": False,
                       "score": 0.0} for i in range(1, n + 1)]
    frames = sorted(kept + fills, key=lambda c: c["t"])
    cap = max(CAP_MIN, int(duration / cap_div))
    if len(frames) > cap:
        keep = {id(c) for c in sorted(frames, key=lambda c: (PRIORITY[c["why"][0]], -c["score"], c["t"]))[:cap]}
        frames = [c for c in frames if id(c) in keep]
    return [{"t": r3(c["t"]), "why": c["why"], "sentence": c["sentence"], "after_cut": c["after_cut"]} for c in frames]


# ---------------------------------------------------------------- faces
class EditFaces:
    """Face box at an edit frame, in edit-frame px (1080 x 1920 cover of the source), from work/face/<id>.json through
    the cut map (the same mapping as prep-frames' work/face.edit.json, computed fresh so it always matches the cut)."""

    def __init__(self, pr, cut: dict):
        from .prep import _cover, _dims
        self.segs = cut.get("segments") or []
        self.f0s = [s["f0"] for s in self.segs]
        self.boxes, self.tf = {}, {}
        ffprobe = None
        for s in self.segs:
            sid = s["src"]
            if sid in self.boxes:
                continue
            fp = pr.work / "face" / f"{sid}.json"
            try:
                self.boxes[sid] = read_json(fp).get("boxes") or [] if fp.exists() else []
            except ValueError:
                self.boxes[sid] = []
            src = pr.work / "src" / f"{sid}.mp4"
            if self.boxes[sid] and src.exists():
                ffprobe = ffprobe or tools().ffprobe
                self.tf[sid] = _cover(*_dims(ffprobe, src))
            else:
                self.tf[sid] = None

    def at(self, f: int):
        k = bisect.bisect_right(self.f0s, f) - 1
        if k < 0:
            return None
        s = self.segs[k]
        if not (s["f0"] <= f < s["f1"]):
            return None
        bs, tf = self.boxes.get(s["src"]) or [], self.tf.get(s["src"])
        i = s["in_frame"] + (f - s["f0"])
        b = bs[i] if 0 <= i < len(bs) else None
        if not b or not tf:
            return None
        sc, ox, oy = tf
        return [round(b[0] * sc + ox), round(b[1] * sc + oy), round(b[2] * sc), round(b[3] * sc)]


def shot_size(face_h: float | None) -> str:
    if face_h is None:
        return "none"
    return "tight" if face_h >= TIGHT else "medium" if face_h >= MEDIUM else "wide"


# ---------------------------------------------------------------- decoding the chosen frames
def _dims_of(path: Path) -> tuple[int, int]:
    from .media import probe
    v = (probe(path) or {}).get("video")
    if not v:
        raise VeosError("NO_PICTURE", f"{path.name} has no video stream", "Pass a video clip.")
    return int(v["disp_w"]), int(v["disp_h"])


CHUNK_N = 400        # frames per select expression (keeps the ffmpeg command line short on any cut length)


def _decode(path: Path, pre: list[str], sel: str, want: int, tw: int, th: int, threads: int) -> list[np.ndarray]:
    cmd = [tools().ffmpeg, "-v", "error", "-threads", str(threads), *pre, "-i", str(path), "-an", "-sn",
           "-vf", f"select='{sel}',scale={tw}:{th}:flags=area", "-fps_mode", "passthrough",
           "-pix_fmt", "rgb24", "-f", "rawvideo", "-"]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    size, out = tw * th * 3, []
    try:
        while len(out) < want:
            buf = p.stdout.read(size)
            if len(buf) < size:
                break
            out.append(np.frombuffer(buf, np.uint8).reshape(th, tw, 3))
    finally:
        p.stdout.close()
        err = p.stderr.read().decode("utf-8", "replace") if p.stderr else ""
        p.wait()
    if not out:
        raise VeosError("DECODE_FAILED", f"no frames decoded from {path.name}",
                        (err.strip().splitlines() or ["the file may be unreadable"])[-1])
    return out


def grab_frames(path: Path, targets: list, tw: int, th: int, threads: int, by: str = "n") -> list[np.ndarray]:
    """RGB tw x th frames, one ffmpeg decode per CHUNK_N frames (one in practice), seeking to the first target and
    stopping after the last. by="n": `targets` are frame numbers of a CFR 30 fps file (exact: the seek lands half a
    frame early, as in track.decode_run); by="t": seconds of any file (the first frame at or after each time)."""
    if not targets:
        return []
    out: list[np.ndarray] = []
    if by == "n":
        for part in _clusters(sorted({int(n) for n in targets}), SPLIT_S * FPS):
            base = max(0, part[0] - 1)
            pre = (["-ss", f"{(base - 0.5) / FPS:.4f}"] if base > 0 else []) + ["-t", f"{(part[-1] - base + 2) / FPS:.4f}"]
            sel = "+".join(f"eq(n\\,{n - base})" for n in part)
            out += _decode(path, pre, sel, len(part), tw, th, threads)
        return out
    for tg in _clusters(sorted({float(x) for x in targets}), SPLIT_S):
        seek = max(0.0, tg[0] - 0.5)
        pre = (["-ss", f"{seek:.4f}"] if seek > 0 else []) + ["-t", f"{tg[-1] - seek + 0.5:.4f}"]
        sel = "+".join(f"gte(t\\,{x - seek:.4f})*(lt(prev_t\\,{x - seek:.4f})+isnan(prev_t))" for x in tg)
        out += _decode(path, pre, sel, len(tg), tw, th, threads)
    return out


SPLIT_S = 10.0       # targets further apart than this are decoded by separate seeks (never decode a long stretch for nothing)


def _clusters(xs: list, gap: float) -> list[list]:
    """Sorted targets -> runs with no inner gap > `gap`, each at most CHUNK_N long."""
    runs: list[list] = []
    for x in xs:
        if runs and x - runs[-1][-1] <= gap and len(runs[-1]) < CHUNK_N:
            runs[-1].append(x)
        else:
            runs.append([x])
    return runs


# ---------------------------------------------------------------- sheets
def _font(size: int):
    from PIL import ImageFont
    from . import paths
    for name in ("NotoSansDevanagari-VF.ttf", "InterTight-VF.ttf"):  # Devanagari + Latin labels
        f = paths.app_root() / "assets" / "fonts" / name
        if f.exists():
            try:
                return ImageFont.truetype(str(f), size)
            except OSError:
                continue
    try:
        return ImageFont.load_default(size=size)
    except TypeError:
        return ImageFont.load_default()


def compose(tiles: list[dict], cols: int, tw: int, th: int, out: Path, font_size: int = 15) -> None:
    """tiles: [{img, l1, l2, colour, cut}] -> one JPEG sheet (labels under each picture; yellow frame on cut tiles)."""
    from PIL import Image, ImageDraw
    font = _font(font_size)
    rows = max(1, -(-len(tiles) // cols))
    sheet = Image.new("RGB", (cols * tw, rows * (th + LABEL_H)), (24, 24, 28))
    dr = ImageDraw.Draw(sheet)
    for i, tl in enumerate(tiles):
        x, y = (i % cols) * tw, (i // cols) * (th + LABEL_H)
        sheet.paste(Image.fromarray(tl["img"]), (x, y))
        if tl.get("cut"):
            dr.rectangle([x + 1, y + 1, x + tw - 2, y + th - 2], outline=CUT_COLOUR, width=4)
        dr.line([x + tw - 1, y, x + tw - 1, y + th + LABEL_H], fill=(0, 0, 0), width=1)
        dr.text((x + 5, y + th + 2), tl["l1"], fill=tl.get("colour", (255, 255, 255)), font=font)
        dr.text((x + 5, y + th + 20), tl["l2"], fill=(205, 205, 205), font=font)
    out.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out, quality=82)


def tc(t: float) -> str:
    return f"{int(t // 60)}:{t % 60:04.1f}"


def _fit(s: str, n: int) -> str:
    return s if len(s) <= n else s[:n - 1].rstrip() + "…"


# ---------------------------------------------------------------- look.json
def write_look(path: Path, doc: dict) -> None:
    """Readable and compact: one line per frame / sentence / cut."""
    keys = list(doc)
    lines = ["{"]
    for i, k in enumerate(keys):
        v, comma = doc[k], ("," if i < len(keys) - 1 else "")
        if isinstance(v, list) and v and isinstance(v[0], dict):
            lines.append(f" {json.dumps(k)}: [")
            lines += ["  " + json.dumps(x, ensure_ascii=False, separators=(",", ":")) + ("," if j < len(v) - 1 else "")
                      for j, x in enumerate(v)]
            lines.append(" ]" + comma)
        else:
            lines.append(f" {json.dumps(k)}: " + json.dumps(v, ensure_ascii=False, separators=(",", ":")) + comma)
    lines.append("}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


# ---------------------------------------------------------------- overview
def _sources(pr) -> dict:
    sp = pr.work / "sources.json"
    try:
        return {s["id"]: s for s in (read_json(sp).get("sources") or [])} if sp.exists() else {}
    except (ValueError, KeyError, TypeError):
        return {}


def overview(pr, args) -> dict:
    t_start = time.time()
    cp = pr.work / "cutmap.json"
    if not cp.exists():
        raise VeosError("NO_CUTMAP", "work/cutmap.json missing: the overview looks at the cut",
                        "Run the rough cut (`veos cut`) first; to look at a raw clip use --src <id> --at T0-T1.")
    cut = read_json(cp)
    dur, nfr = float(cut["duration"]), int(cut["frames"])
    by_id = _sources(pr)
    vo = {i for i, s in by_id.items() if s.get("kind") in ("voiceover", "audio-only")}
    out_dir = pr.root / "review" / "look"
    for old in out_dir.glob("sheet_*.jpg") if out_dir.exists() else []:
        old.unlink()
    segs = cut.get("segments") or []
    if segs and all(s["src"] in vo for s in segs):
        write_look(out_dir / "look.json", {"version": 1, "duration": dur, "fps": FPS, "skipped": "voice-over reel: no picture",
                                           "frames": []})
        return {"skipped": True, "reason": "voice-over reel: the cut has no picture to look at",
                "json": pr.rel(out_dir / "look.json")}
    warnings: list[str] = []
    proxy = pr.work / "cut_proxy.mp4"
    if not proxy.exists() or proxy.stat().st_mtime < cp.stat().st_mtime:
        from .cut import render_proxy
        render_proxy(cut, by_id, pr, proxy)
        warnings.append("work/cut_proxy.mp4 was missing or older than the cut map; rebuilt it")
    threads = _threads(args)
    wp = pr.work / "words.edit.json"
    words = (read_json(wp).get("words") or []) if wp.exists() else []
    if not words:
        warnings.append("no work/words.edit.json words: no sentence frames (cuts, motion and gap fill only)")
    sents = sentences(words)
    cuts = cut_points(cut, by_id)
    from .context import _edit_setups
    spans = _edit_setups(cut, by_id)

    t0 = time.time()
    size = _dims_of(proxy)
    mt, mv_raw = motion_signal(proxy, size, threads)
    mv = mask_cuts(mt, mv_raw, [c["t"] for c in cuts if c["kind"] != "start"])
    peaks = motion_peaks(mt, mv)
    t_motion = time.time() - t0

    frames = select_frames(dur, [(s["key_t"], s["id"]) for s in sents], [c["t"] for c in cuts], peaks)
    faces = EditFaces(pr, cut)
    seg_f0 = [s["f0"] for s in segs]
    sent_t0 = [s["t0"] for s in sents]
    for k, fr in enumerate(frames):
        f = min(nfr - 1, int(round(fr["t"] * FPS)))
        if fr["sentence"] is None and sents:
            j = bisect.bisect_right(sent_t0, fr["t"]) - 1
            if j >= 0 and sents[j]["t0"] - 0.05 <= fr["t"] <= sents[j]["t1"] + 0.15:
                fr["sentence"] = sents[j]["id"]
        sg = segs[max(0, bisect.bisect_right(seg_f0, f) - 1)] if segs else {}
        box = faces.at(f)
        fh = round(box[3] / FH, 3) if box else None
        mi = min(len(mv) - 1, int(round(fr["t"] * MOTION_FPS))) if len(mv) else -1
        mval = round(float(mv[mi]), 1) if mi >= 0 else 0.0
        primary = fr["why"][0]
        said = sents[fr["sentence"]]["key"] if primary == "sentence" and fr["sentence"] is not None else ""
        near = said_near(words, sents[fr["sentence"]]["key_t"] if said else fr["t"])
        fr.update({"n": k + 1, "f": f, "sheet": k // PER + 1, "tile": k % PER + 1, "src": sg.get("src"),
                   "setup": setup_at(spans, fr["t"]), "shot": shot_size(fh), "face": box, "face_h": fh,
                   "motion": mval, "motion_level": level(mval), "said": near})

    t1 = time.time()
    th = max(2, round(TILE_W * size[1] / max(1, size[0]) / 2) * 2)
    imgs = grab_frames(proxy, [fr["f"] for fr in frames], TILE_W, th, threads, by="n")
    t_extract = time.time() - t1
    if len(imgs) < len(frames):
        warnings.append(f"decoded {len(imgs)} of {len(frames)} frames (the proxy is shorter than the cut map)")
    t2 = time.time()
    sheets = []
    for s in range(0, len(imgs), PER):
        tiles = []
        for fr, img in zip(frames[s:s + PER], imgs[s:s + PER]):
            why = "+".join(fr["why"])
            tiles.append({"img": img, "l1": f"#{fr['n']:02d} {tc(fr['t'])} {why}", "l2": _fit(fr["said"] or "(pause)", 34),
                          "colour": WHY_COLOUR.get(fr["why"][0], (255, 255, 255)), "cut": fr["after_cut"]})
        out = out_dir / f"sheet_{s // PER + 1:02d}.jpg"
        compose(tiles, COLS, TILE_W, th, out)
        sheets.append(pr.rel(out))
    t_sheets = time.time() - t2

    per_s, max_s = per_second(mt, mv, dur)
    order = ["n", "t", "f", "why", "sentence", "after_cut", "sheet", "tile", "src", "setup", "shot", "face", "face_h",
             "motion", "motion_level", "said"]
    doc = {"version": 1, "duration": dur, "fps": FPS, "video": pr.rel(proxy),
           "note": ("frames picked by meaning (sentence key word, just after a cut, motion peak, gap fill <= 2.5 s); "
                    "face in edit px 1080x1920; shot from face_h (tight >= 0.30, medium >= 0.15); motion = mean |gray diff| "
                    "0-255 at 160 px / 10 fps (still < 1.5 <= low < 4 <= medium < 8 <= high)"),
           "frames": [{k: fr[k] for k in order} for fr in frames],
           "sentences": sents,
           "cuts": cuts,
           "motion": {"fps": MOTION_FPS, "unit": "mean |gray diff| 0-255", "levels": {n: lim for lim, n in LEVELS[:-1]},
                      "per_s": per_s, "max_s": max_s, "peaks": [{"t": p["peak_t"], "v": p["v"]} for p in peaks]}}
    write_look(out_dir / "look.json", doc)
    by_reason: dict[str, int] = {}
    for fr in frames:
        for w in fr["why"]:
            by_reason[w] = by_reason.get(w, 0) + 1
    return {"duration": dur, "frames": len(frames), "s_per_frame": round(dur / max(1, len(frames)), 2),
            "by_reason": by_reason, "sentences": len(sents), "cuts": len(cuts), "motion_peaks": len(peaks),
            "sheets": sheets, "json": pr.rel(out_dir / "look.json"),
            "seconds": {"motion": round(t_motion, 2), "extract": round(t_extract, 2), "sheets": round(t_sheets, 2),
                        "total": round(time.time() - t_start, 2)},
            "warnings": warnings}


# ---------------------------------------------------------------- close look
AT_RANGE = re.compile(r"^\s*(\d+(?:\.\d+)?)\s*-\s*(\d+(?:\.\d+)?)\s*$")


def parse_at(spec: str) -> tuple[str, list[float]]:
    """'T0-T1' -> every frame (span <= 1 s) or every 2nd frame (<= AT_MAX_S); 'T1,T2,...' -> those moments."""
    m = AT_RANGE.match(spec or "")
    if m:
        a, b = float(m.group(1)), float(m.group(2))
        if b <= a:
            raise VeosError("BAD_AT", f"--at {spec}: the end must be after the start", "Example: --at 12.4-13.6")
        if b - a > AT_MAX_S + 1e-6:
            raise VeosError("AT_TOO_LONG", f"--at {spec} spans {b - a:.2f} s (max {AT_MAX_S:g} s)",
                            "Close looks are for one beat; the overview (`veos look` without --at) covers the whole cut.")
        step = 1 if b - a <= 1.0 + 1e-6 else 2
        f0, f1 = int(round(a * FPS)), int(round(b * FPS))
        return f"{a:.2f}-{b:.2f}", [f / FPS for f in range(f0, f1 + 1, step)]
    try:
        ts = [float(x) for x in str(spec).split(",") if x.strip()]
    except ValueError:
        raise VeosError("BAD_AT", f"--at {spec} is not a time range or a list of times",
                        "Use --at 12.4-13.6 (<= 2 s) or --at 12.4,13.0,13.5 (seconds).") from None
    if not ts or any(t < 0 for t in ts):
        raise VeosError("BAD_AT", f"--at {spec}: give times in seconds (>= 0)", "Example: --at 3.1,3.6,4.0")
    if len(ts) > AT_MAX_N:
        raise VeosError("BAD_AT", f"--at lists {len(ts)} moments (max {AT_MAX_N})", "Split it, or use a range.")
    ts = sorted(set(ts))
    return (f"{ts[0]:.2f}" + (f"+{len(ts) - 1}" if len(ts) > 1 else "")), ts


def close_look(pr, args) -> dict:
    tag, times = parse_at(args.at)
    threads = _threads(args)
    by_id = _sources(pr)
    words: list[dict] = []
    face_of = None
    if args.src:
        sid = args.src
        if sid in by_id:
            s = by_id[sid]
            if s.get("kind") in ("voiceover", "audio-only"):
                raise VeosError("NO_PICTURE", f"source {sid} is a voice-over (no picture)", "Pass a clip with picture.")
            video = pr.work / "src" / f"{sid}.mp4"
            cfr = video.exists()
            if not cfr:
                video = Path(s.get("path") or "")
            wp = pr.work / "words" / f"{sid}.json"
            words = (read_json(wp).get("words") or []) if wp.exists() else []
            fp = pr.work / "face" / f"{sid}.json"
            fb = (read_json(fp).get("boxes") or []) if fp.exists() and cfr else []
            dur = float(s.get("duration") or 0.0)
            name = re.sub(r"[^A-Za-z0-9_-]+", "_", sid)
        else:
            video = Path(sid).expanduser()
            if not video.is_absolute() and not video.exists() and (pr.root / video).exists():
                video = pr.root / video
            if re.match(r"^[a-z][a-z0-9+.-]*://", sid, re.I):
                raise VeosError("NO_FETCH", "close looks are made from local footage only", "Pass a source id or a video file.")
            cfr, fb, dur = False, [], 0.0
            name = re.sub(r"[^A-Za-z0-9_-]+", "_", video.stem)[:40] or "clip"
        if not video.is_file():
            raise VeosError("BAD_CLIP", f"--src '{sid}' is not a source id or a video file",
                            f"Known sources: {', '.join(sorted(by_id)) or 'none'}.")
        size = _dims_of(video)
        if fb:
            def face_of(f):  # noqa: E306 - source px -> face height fraction of the source frame
                b = fb[f] if 0 <= f < len(fb) else None
                return round(b[3] / size[1], 3) if b else None
        out = pr.root / "review" / "look" / f"{name}_at_{tag}.jpg"
    else:
        cp = pr.work / "cutmap.json"
        if not cp.exists():
            raise VeosError("NO_CUTMAP", "work/cutmap.json missing (edit-time close looks need the cut)",
                            "Run `veos cut` first, or look at a raw clip with --src <id>.")
        cut = read_json(cp)
        video = pr.work / "cut_proxy.mp4"
        if not video.exists() or video.stat().st_mtime < cp.stat().st_mtime:
            from .cut import render_proxy
            render_proxy(cut, by_id, pr, video)
        cfr, dur = True, float(cut["duration"])
        wp = pr.work / "words.edit.json"
        words = (read_json(wp).get("words") or []) if wp.exists() else []
        faces = EditFaces(pr, cut)

        def face_of(f):  # noqa: E306
            b = faces.at(f)
            return round(b[3] / FH, 3) if b else None
        size = _dims_of(video)
        out = pr.root / "review" / "look" / f"at_{tag}.jpg"
    if dur:
        last = dur - 1.0 / FPS
        if min(times) > last + 1e-6:
            raise VeosError("BAD_AT", f"--at {args.at} is past the end ({dur:.2f} s)", "Times are seconds from the start.")
        times = sorted({min(t, last) for t in times})
    n = len(times)
    tw = 360 if n <= 4 else 270 if n <= 16 else 180
    cols = n if n <= 4 else 4 if n <= 16 else 6
    th = max(2, round(tw * size[1] / max(1, size[0]) / 2) * 2)
    fnums = [int(round(t * FPS)) for t in times]
    if cfr:
        uniq = sorted(set(fnums))
        imgs = grab_frames(video, uniq, tw, th, threads, by="n")
        times, fnums = [f / FPS for f in uniq[:len(imgs)]], uniq[:len(imgs)]
    else:
        imgs = grab_frames(video, times, tw, th, threads, by="t")
        times, fnums = times[:len(imgs)], fnums[:len(imgs)]
    rows, tiles = [], []
    for t, f, img in zip(times, fnums, imgs):
        w = next((x for x in words if x["s"] - 0.02 <= t <= x["e"] + 0.02 and _text(x)), None)
        word = _text(w) if w else ""
        fh = face_of(f) if face_of else None
        rows.append({"t": r3(t), "f": f, "word": word, "face_h": fh})
        tiles.append({"img": img, "l1": f"{t:.2f}s f{f}" + ("" if fh or not face_of else "  no face"),
                      "l2": _fit(word or "(between words)", 30 if tw > 200 else 18), "colour": (255, 255, 255)})
    compose(tiles, cols, tw, th, out, font_size=15 if tw > 200 else 13)
    span = (min(times), max(times)) if times else (0.0, 0.0)
    res = {"mode": "close", "src": (name if args.src else "edit"), "sheet": pr.rel(out), "n": len(rows),
           "span": [r3(span[0]), r3(span[1])]}
    if "-" in tag:  # a range: what is said across it (a list's moments are far apart; their words are per frame)
        res["said"] = _fit(" ".join(_text(x) for x in words
                                    if x["e"] >= span[0] - 0.05 and x["s"] <= span[1] + 0.05 and _text(x)), 160)
    if len(rows) <= 6:
        res["frames"] = rows
    else:  # keep stdout small: word onsets and the face range instead of one row per frame
        onsets, prev = [], None
        for r in rows:
            if r["word"] and r["word"] != prev:
                onsets.append(f"{r['t']:.2f} {r['word']}")
            prev = r["word"]
        res["words_at"] = " | ".join(onsets)
        fhs = [r["face_h"] for r in rows if r["face_h"]]
        res["face_h"] = [min(fhs), max(fhs)] if fhs else None
        res["no_face_at"] = [r["t"] for r in rows if face_of and not r["face_h"]][:8]
    return res


# ---------------------------------------------------------------- command
def main(args, project) -> dict:
    pr = need_project(project)
    if args.at:
        return close_look(pr, args)
    if args.src:
        raise VeosError("BAD_ARGS", "--src needs --at (the overview looks at the cut)",
                        "Example: veos look --project P --src A --at 3.1,3.6,4.0")
    return overview(pr, args)
