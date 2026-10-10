"""`veos context`: the compact planning context (sources, face free-space, word list, script, cut info).

The planning model reads ONLY this about the footage, so every number here earns its tokens.
"""
from __future__ import annotations

import json
import statistics
from pathlib import Path

import numpy as np

from .core import FPS, VeosError, need_project, r3, read_json, write_json

SAFE_X, SAFE_Y = (64, 1016), (110, 1500)
CLEAR = 40            # px kept clear of the face
HEAD_UP = 0.35        # head top = face y - 0.35 * h
FREE_FRAC = 0.90      # a region must be clear in >= 90 % of a setup's frames
PAUSE = 0.3
STEP = 10             # px grid for the occupancy maps
MIN_BAND = 80         # ignore free bands thinner than this (px)
MIN_SIDE = 120        # ignore side strips narrower than this (px)


def add_args(p, cmd):
    p.add_argument("--part", choices=["sources", "faces", "words", "beats", "all"], default="all")


# ------------------------------------------------------------------ faces
def _runs(mask, lo: int, min_len: int) -> list[list[int]]:
    """contiguous True runs of `mask` (index i = pixel lo + i*STEP) as [start_px, end_px]."""
    out, start = [], None
    for i, v in enumerate(list(mask) + [False]):
        if v and start is None:
            start = i
        elif not v and start is not None:
            a, b = lo + start * STEP, lo + i * STEP
            if b - a >= min_len:
                out.append([a, b])
            start = None
    return out


def face_stats(boxes: list, f0: int, f1: int) -> dict | None:
    bs = np.array([b[:4] for b in boxes[f0:f1] if b], dtype=float)
    n_frames = max(1, f1 - f0)
    if len(bs) == 0:
        return None
    st = {k: [int(bs[:, j].min()), int(statistics.median(bs[:, j])), int(bs[:, j].max())]
          for j, k in enumerate(("x", "y", "w", "h"))}
    st["head_top_y"] = int(statistics.median(bs[:, 1] - HEAD_UP * bs[:, 3]))
    st["coverage"] = round(len(bs) / n_frames, 2)
    # occupancy grid over the safe zone: a cell is occupied in a frame if the face (+clearance, incl. head top) hits it
    gx = np.arange(SAFE_X[0], SAFE_X[1], STEP)
    gy = np.arange(SAFE_Y[0], SAFE_Y[1], STEP)
    occ = np.zeros((len(gy), len(gx)), dtype=np.int32)
    for x, y, w, h in bs:
        x0, x1 = x - CLEAR, x + w + CLEAR
        y0, y1 = y - HEAD_UP * h - CLEAR, y + h + CLEAR
        ix = (gx + STEP > x0) & (gx < x1)
        iy = (gy + STEP > y0) & (gy < y1)
        occ[np.ix_(iy, ix)] += 1
    free = occ <= (1 - FREE_FRAC) * len(bs)
    full_rows = free.all(axis=1)
    st["free_bands"] = _runs(full_rows, SAFE_Y[0], MIN_BAND)       # y ranges clear across the full safe width
    rows = np.where(~full_rows)[0]
    if rows.size:                                                  # the rows the face touches
        cols = free[~full_rows].all(axis=0)                        # columns clear on every one of those rows
        ya, yb = SAFE_Y[0] + int(rows.min()) * STEP, SAFE_Y[0] + (int(rows.max()) + 1) * STEP
        st["free_sides"] = {"y": [ya, yb], "x": _runs(cols, SAFE_X[0], MIN_SIDE)}
    else:
        st["free_sides"] = {"y": [], "x": []}
    return st


def _setups(s: dict) -> list[tuple[float, float, str]]:
    segs = s.get("segments") or []
    return [(g["start"], g["end"], g["setup"]) for g in segs] or [(0.0, s.get("duration", 0.0), "other")]


def faces_part(pr, sources: list[dict]) -> dict:
    out = {}
    for s in sources:
        f = pr.work / "face" / f"{s['id']}.json"
        if not f.exists() or s.get("kind") != "talking-head":
            continue
        d = read_json(f)
        fps = d.get("fps", FPS)
        for a, b, label in _setups(s):
            st = face_stats(d["boxes"], int(round(a * fps)), int(round(b * fps)))
            if st:
                out[f"{s['id']}:{label}"] = st
    return out


# ------------------------------------------------------------------ words
def _word_text(w: dict) -> str:
    t = w.get("caption") if "caption" in w else w.get("w", "")
    return "-" if t == "" else t.replace(" ", "_")


def words_lines(words: list[dict]) -> list[str]:
    lines, cur = [], []
    for k, w in enumerate(words):
        low = "?" if (w.get("p") if w.get("p") is not None else 1) < 0.5 else ""
        cur.append(f"{w['i']}:{_word_text(w)}{low}@{w['s']:.2f}")
        gap = (words[k + 1]["s"] - w["e"]) if k + 1 < len(words) else 0
        if gap >= PAUSE:
            cur.append(f"|pause {gap:.2f}|")
            lines.append(" ".join(cur))
            cur = []
        elif len(cur) >= 14:
            lines.append(" ".join(cur))
            cur = []
    if cur:
        lines.append(" ".join(cur))
    return lines


# ------------------------------------------------------------------ main
def _edit_setups(cut: dict, sources: dict[str, dict]) -> list[list]:
    """edit-time spans per camera setup: every cut segment is split where its source crosses a setup boundary."""
    out: list[list] = []
    for seg in cut.get("segments", []):
        s = sources.get(seg["src"])
        sp = float(seg.get("speed") or 1.0)
        in0, in1 = seg["in"], seg["in"] + (seg["t1"] - seg["t0"]) * sp
        spans = [(max(a, in0), min(b, in1), lab) for a, b, lab in (_setups(s) if s else [(in0, in1, "other")])
                 if min(b, in1) - max(a, in0) > 1e-6] or [(in0, in1, "other")]
        for a, b, lab in spans:
            t0, t1 = seg["t0"] + (a - in0) / sp, seg["t0"] + (b - in0) / sp
            tag = f"{seg['src']}:{lab}"
            if out and out[-1][2] == tag and abs(out[-1][1] - t0) < 0.05:
                out[-1][1] = r3(t1)
            else:
                out.append([r3(t0), r3(t1), tag])
    return out


def build(pr, part: str) -> dict:
    sj = pr.work / "sources.json"
    if not sj.exists():
        raise VeosError("NO_SOURCES", "work/sources.json missing", "Run `veos ingest` first.")
    sdoc = read_json(sj)
    sources = sdoc["sources"]
    by_id = {s["id"]: s for s in sources}
    cut_p, we_p = pr.work / "cutmap.json", pr.work / "words.edit.json"
    cut = read_json(cut_p) if cut_p.exists() else None
    edit_time = bool(cut and we_p.exists())
    ctx: dict = {"time": "edit" if edit_time else "source", "fps": FPS,
                 "source_type": sdoc.get("source_type", "talking_head")}
    if ctx["source_type"] == "voiceover_only":
        ctx["voiceover"] = ("no presenter: the stage is hidden throughout and every frame is built from scenes "
                            "(one scene per sentence, no gaps); the whole safe box is free (no face)")
    if ctx["source_type"] == "no_voice":  # novoice.py: the music is the spine, as the words are for speech
        ctx["no_voice"] = ("nobody speaks: no subtitles; the music's beats carry the rhythm and on-screen text carries the "
                           "story; footage (clips and photos) fills the stage")
        cut_p0 = pr.work / "cutmap.json"
        if part in ("beats", "words", "all"):
            from .novoice import context_part
            ctx["music"] = context_part(pr, read_json(cut_p0) if cut_p0.exists() else None)
    if part in ("sources", "all"):
        ctx["sources"] = [{"id": s["id"], "kind": s["kind"], "duration": s["duration"],
                           "setups": [[r3(a), r3(b), lab] for a, b, lab in _setups(s)]} for s in sources]
        if cut:
            used = {g["src"] for g in cut["segments"]}
            removed = sum(by_id[i]["duration"] for i in used if i in by_id) - cut["duration"]
            ctx["cut"] = {"edit_duration": cut["duration"], "segments": len(cut["segments"]),
                          "removed_s": r3(max(0.0, removed)), "edit_setups": _edit_setups(cut, by_id)}
        else:
            ctx["cut"] = None
    if part in ("faces", "all"):
        ctx["frame"] = {"size": [1080, 1920], "safe_y": list(SAFE_Y), "safe_x": list(SAFE_X), "clearance": CLEAR,
                        "note": "free_bands: y ranges clear across the whole safe width. free_sides: y span of the "
                                "face rows + x ranges clear beside the face. Clear in >=90% of the setup's frames."}
        ctx["faces"] = faces_part(pr, sources)
    if part in ("words", "all"):
        if edit_time:
            words = read_json(we_p).get("words", [])
            ctx["words"] = words_lines(words)
            ctx["word_count"] = len(words)
            ctx["words_note"] = "i:word@t (edit-time s); ?=low confidence; -=hidden; caption text shown when set"
        else:
            ctx["words_by_source"] = {}
            for s in sources:
                wf = pr.work / "words" / f"{s['id']}.json"
                if wf.exists():
                    ctx["words_by_source"][s["id"]] = words_lines(read_json(wf).get("words", []))
            ctx["words_note"] = "i:word@t (source-time s); ?=low confidence; no cut yet"
        pj = pr.root / "project.json"
        script = read_json(pj).get("script") if pj.exists() else None
        if script and Path(script).exists():
            txt = Path(script).read_text(encoding="utf-8-sig", errors="replace").strip()
            ctx["script"] = {"chars": len(txt), "excerpt": txt[:600]}
    return ctx


def main(args, project) -> dict:
    pr = need_project(project)
    ctx = build(pr, args.part)
    tokens = len(json.dumps(ctx, ensure_ascii=False, separators=(",", ":"))) // 4
    dur = (ctx.get("cut") or {}).get("edit_duration") or sum(s["duration"] for s in ctx.get("sources", [])) or None
    out = pr.path("work", f"context.{args.part}.json")
    write_json(out, ctx, indent=None)
    res = {"part": args.part, "context": ctx, "token_estimate": tokens, "file": pr.rel(out)}
    if dur:
        res["tokens_per_min"] = round(tokens / (dur / 60))
    return res
