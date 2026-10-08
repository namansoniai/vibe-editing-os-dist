"""V-CADENCE: weighted state-change cadence (structure §0 Definitions "State change", tokens `cadence`). Replaces M7.

State changes (SC), one per frame (several events on one frame = one SC with the largest weight); frame 0 and exits
never count:
  cut           work/cutmap.json segment joins, timeline.shots[] starts, scene `cuts`         weight 1
  enter         a z3-10 scene entering (t_in)                                                 weight 1
  event         a declared scene `events` time                                                weight 1
  stage         a stage layout change                                                         weight 1
  camera        a footage camera move starting                                                weight 1
  recrop        a jump re-crop / jump-cut zoom (camera preset "recrop-*" or a 0-1 frame move)  weight 1
  canvas_camera a canvas camera move starting (timeline.canvas_camera[], when present)        weight 1
  world         a world / theme / grade flip (timeline.world[] after the first, theme_flips, grades)  weight 1
  transition    a timeline transition marker                                                  weight 1
  caption       a caption chunk swap (work/captions.json chunks; else approximated from words)   cadence.caption_weight
Continuous motion (live presenter footage, footage/B-roll/continuous/ambient scenes, push-drift camera holds, stage morphs
and canvas moves in progress) satisfies max_static_s but not max_gap_s.

Checks (each only when its token is set): sc_per_10s [lo, hi] (sliding 10 s window over the body), hook_sc_3s (weighted
SCs in 0-3 s), max_gap_s (+ hook_max_gap_s in the HOOK section; weight >= 1 SCs), max_static_s, cuts_per_min,
median_shot_s. `stats.cadence` reports every measure.

Legacy mode (v1 `rules_v0: M7`): the old M7 exactly (visual events incl. exits, no captions, gap checks only).
"""
from __future__ import annotations

import statistics
from pathlib import Path

from .core import FPS, read_json
from .vcommon import as_range, fail, fr, get_path

CONTINUOUS_KINDS = ("footage", "broll", "clip", "video", "archive_video", "ken_burns", "particles", "ambient")
CUT_KINDS = ("cut", "transition")
PAUSE_S = 0.3
WINDOW_S = 10.0
STEP_S = 0.5


# --------------------------------------------------------------------------- captions
def load_caption_chunks(proj, tl: dict, style: dict, words, warnings: list) -> tuple[list[dict] | None, str]:
    """Caption chunks [{text, t0, t1}] for cadence and V-F0: work/captions.json (the caption engine's export, E-05) when
    present; else approximated from work/words.edit.json and the caption profile's word limits; else None."""
    if get_path(style, "profile.captions.mode") == "off":
        return [], "off"
    caps = tl.get("captions") or {}
    hide = []
    for h in caps.get("hide") or []:
        try:
            hide.append((float(h[0]), float(h[1])))
        except (TypeError, ValueError, IndexError):
            continue

    def visible(ch):
        return not any(a - 1e-6 <= ch["t0"] < b - 1e-6 for a, b in hide)
    cp = Path(proj.work) / "captions.json" if proj is not None else None
    if cp is not None and cp.exists():
        try:
            d = read_json(cp)
            raw = d.get("chunks") if isinstance(d, dict) else d
            chunks = [{"text": str(x.get("text", "")), "t0": float(x["t0"]), "t1": float(x["t1"])}
                      for x in raw or [] if isinstance(x, dict) and "t0" in x and "t1" in x]
            return sorted([c for c in chunks if visible(c)], key=lambda c: c["t0"]), "captions.json"
        except (ValueError, TypeError, KeyError) as e:
            warnings.append(f"work/captions.json could not be read ({e}); caption swaps approximated")
    if caps and caps.get("subtitles") not in ("auto", True):
        return [], "none"
    ws = (words or {}).get("words") if isinstance(words, dict) else None
    if not ws:
        return None, "none"
    prof_id = get_path(style, "captions.default") or "CS-1"
    wr = get_path(style, f"captions.profiles.{prof_id}.words") or get_path(style, "type.subtitle.words_per_card") or [2, 3]
    mx = int(wr[1] if isinstance(wr, (list, tuple)) and len(wr) > 1 else (wr[0] if isinstance(wr, (list, tuple)) else wr))
    mx = max(1, mx)
    chunks, cur = [], []
    for k, w in enumerate(ws):
        if w.get("caption") == "":
            continue
        cur.append(w)
        nxt = ws[k + 1] if k + 1 < len(ws) else None
        gap = (float(nxt["s"]) - float(w["e"])) if nxt else 0
        if len(cur) >= mx or gap >= PAUSE_S or nxt is None or str(w.get("w", "")).rstrip()[-1:] in ".?!,":
            chunks.append({"text": " ".join(str(x.get("caption", x.get("w", ""))) for x in cur),
                           "t0": float(cur[0]["s"]), "t1": float(cur[-1]["e"])})
            cur = []
    return [c for c in chunks if visible(c)], "words-approx"


# --------------------------------------------------------------------------- events
def caption_weight(c, p: dict) -> float:
    w = p.get("caption_weight", get_path(c.style, "cadence.caption_weight"))
    if w is None:
        w = 1.0 if get_path(c.style, "profile.captions.role") == "primary" else 0.5
    return float(w)


def sc_events(c, p: dict) -> list[tuple[float, float, str]]:
    """Raw (t, weight, kind) state-change events (not yet merged per frame)."""
    ev: list[tuple[float, float, str]] = []
    for seg in ((c.cutmap or {}).get("segments") or [])[1:]:
        ev.append((float(seg.get("t0", 0)), 1.0, "cut"))
    for sh in (c.tl.get("shots") or [])[1:]:
        if isinstance(sh, dict) and ("t" in sh or "t0" in sh):
            ev.append((float(sh.get("t", sh.get("t0", 0))), 1.0, "cut"))
    for s in c.scenes:
        z, a = s.get("z", 0), float(s.get("t_in", 0))
        if 3 <= z <= 10:
            ev.append((a, 1.0, "enter"))
        for key, kind in (("events", "event"), ("cuts", "cut")):
            for v in s.get(key) or []:
                try:
                    t = a + float(v)
                except (TypeError, ValueError):
                    continue
                if a - 1e-9 <= t <= float(s.get("t_out", 0)) + 1e-9:
                    ev.append((t, 1.0, kind))
    ev += [(float(e.get("t", 0)), 1.0, "stage") for e in c.stage[1:]]
    presets = c.style.get("camera_presets") or {}
    for e in c.camera:  # every camera event; jump re-crops / jump-cut zooms (a 0-1 frame scale change) are labelled recrop
        pr = presets.get(e.get("preset")) or {}
        jump = "recrop" in str(e.get("preset", "")) or (isinstance(pr.get("frames"), (int, float)) and pr["frames"] <= 1)
        ev.append((float(e.get("t", 0)), 1.0, "recrop" if jump else "camera"))
    ev += [(float(e.get("t", 0)), 1.0, "canvas_camera") for e in (c.tl.get("canvas_camera") or []) if isinstance(e, dict)]
    ev += [(float(e.get("t", 0)), 1.0, "world") for e in (c.tl.get("world") or [])[1:] if isinstance(e, dict)]
    for key in ("theme_flips", "themes", "grades"):
        ev += [(float(e.get("t", 0)), 1.0, "world") for e in (c.tl.get(key) or []) if isinstance(e, dict) and "t" in e]
    ev += [(float(e.get("t", 0)), 1.0, "transition") for e in c.transitions]
    if c.caption_chunks:
        w = caption_weight(c, p)
        ev += [(ch["t0"], w, "caption") for ch in c.caption_chunks]
    return ev


def sc_frames(c, p: dict) -> dict[int, tuple[float, set]]:
    """frame -> (weight, kinds) after merging same-frame events; frame 0 and frames past the end are dropped."""
    out: dict[int, tuple[float, set]] = {}
    for t, w, k in sc_events(c, p):
        n = fr(t)
        if n <= 0 or n >= c.frames:
            continue
        pw, ks = out.get(n, (0.0, set()))
        out[n] = (max(pw, w), ks | {k})
    return out


def motion_spans(c) -> list[tuple[int, int]]:
    """Frame spans [a, b) of continuous motion."""
    spans: list[tuple[int, int]] = []
    presence = get_path(c.style, "profile.presenter.presence")
    if presence != "none":  # live presenter footage moves whenever the stage shows it
        cur = None
        for n in range(c.frames + 1):
            on = n < c.frames and c.stage_engine_at(n / FPS) != "hidden"
            if on and cur is None:
                cur = n
            elif not on and cur is not None:
                spans.append((cur, n))
                cur = None
    for s in c.scenes:
        if (s.get("kind") in CONTINUOUS_KINDS or s.get("continuous") or s.get("ambient")
                or s.get("motion") in ("continuous", "ambient")):
            spans.append((fr(s.get("t_in", 0)), fr(s.get("t_out", 0))))
    presets = c.style.get("camera_presets") or {}
    cams = sorted(c.camera, key=lambda e: e.get("t", 0))
    for i, e in enumerate(cams):
        frames = (presets.get(e.get("preset")) or {}).get("frames")
        a = fr(e.get("t", 0))
        if frames == "beat":
            nxt = fr(cams[i + 1]["t"]) if i + 1 < len(cams) else None
            b = c.beat_at(float(e.get("t", 0)))
            end = fr(b["t1"]) if b else c.frames
            spans.append((a, min(x for x in (nxt, end) if x is not None)))
        elif isinstance(frames, (int, float)):
            spans.append((a, a + int(frames)))
        elif isinstance(frames, list) and frames:
            spans.append((a, a + int(max(frames))))
    morphs = c.style.get("stage_morphs") or {}
    for e in c.stage:
        d = morphs.get(e.get("via"))
        if isinstance(d, (int, float)) and d > 0:
            spans.append((fr(e.get("t", 0)), fr(e.get("t", 0)) + int(d)))
    for e in c.tl.get("canvas_camera") or []:
        if isinstance(e, dict):
            a = fr(e.get("t", 0))
            b = fr(e["t1"]) if "t1" in e else a + int(e.get("frames", 0) or 0)
            spans.append((a, b))
    return spans


def _hook_end(c) -> float:
    hooks = c.section_range(lambda s: s.upper() == "HOOK")
    return max((b for _, b in hooks), default=min(3.0, c.duration))


# --------------------------------------------------------------------------- measures
def measure(c, p: dict) -> dict:
    """Every cadence number (also used for stats when the rule is off)."""
    scf = sc_frames(c, p)
    frames = sorted(scf)
    total_w = sum(w for w, _ in scf.values())
    by_kind: dict[str, int] = {}
    for _, ks in scf.values():
        for k in ks:
            by_kind[k] = by_kind.get(k, 0) + 1
    hook_end = _hook_end(c)
    # sliding windows over the body
    body0, body1 = hook_end, c.duration
    wins = []
    if body1 - body0 >= WINDOW_S:
        s = body0
        while s + WINDOW_S <= body1 + 1e-9:
            a, b = fr(s), fr(s + WINDOW_S)
            wins.append((s, sum(scf[n][0] for n in frames if a <= n < b)))
            s += STEP_S
    elif body1 - body0 > 1.0:
        a = fr(body0)
        tot = sum(scf[n][0] for n in frames if n >= a)
        wins.append((body0, tot * WINDOW_S / (body1 - body0)))
    hook3 = sum(scf[n][0] for n in frames if n <= fr(3.0))
    # gaps between weight >= 1 SCs
    strong = [0] + [n for n in frames if scf[n][0] >= 1.0 - 1e-9] + [c.frames]
    gaps = [(a, b) for a, b in zip(strong, strong[1:]) if b > a]
    # static spans: no SC of any weight and no continuous motion
    moving = bytearray(c.frames + 1)
    for a, b in motion_spans(c):
        for n in range(max(0, a), min(c.frames, b)):
            moving[n] = 1
    sc_set = set(frames)
    statics, cur = [], None
    for n in range(c.frames + 1):
        still = n < c.frames and not moving[n] and n not in sc_set and n != 0
        if still and cur is None:
            cur = n
        elif not still and cur is not None:
            statics.append((cur, n))
            cur = None
    cuts = sorted(n for n in frames if scf[n][1] & set(CUT_KINDS))
    shots = [b - a for a, b in zip([0] + cuts, cuts + [c.frames]) if b > a]
    return {
        "scf": scf, "windows": wins, "gaps": gaps, "statics": statics, "cuts": cuts, "hook_end": hook_end,
        "stats": {
            "sc": len(frames), "weighted": round(total_w, 2), "by_kind": by_kind,
            "caption_chunks": len(c.caption_chunks) if c.caption_chunks is not None else None,
            "caption_source": c.caption_source, "caption_weight": caption_weight(c, p),
            "sc_per_10s": ({"min": round(min(w for _, w in wins), 2), "max": round(max(w for _, w in wins), 2),
                            "mean": round(sum(w for _, w in wins) / len(wins), 2)} if wins else None),
            "hook_sc_3s": round(hook3, 2),
            "max_gap_s": round(max((b - a for a, b in gaps), default=0) / FPS, 2),
            "max_static_s": round(max((b - a for a, b in statics), default=0) / FPS, 2),
            "cuts_per_min": round(len(cuts) / (c.duration / 60), 2) if c.duration else 0,
            "median_shot_s": round(statistics.median(shots) / FPS, 2) if shots else None,
        },
    }


def params_from_tokens(c, p: dict) -> dict:
    cad = dict(c.style.get("cadence") or {})
    cad.update({k: v for k, v in p.items() if k not in ("from", "playbook_rule", "legacy")})
    return cad


# --------------------------------------------------------------------------- rule
def rule_cadence(c, p: dict) -> list[dict]:
    if p.get("legacy"):
        return rule_m7(c, p)
    q = params_from_tokens(c, p)
    m = measure(c, q)
    c.stats_extra["cadence"] = m["stats"]
    out = []
    rng = as_range(q.get("sc_per_10s"))
    if rng and m["windows"]:
        lo, hi = rng
        low = min(m["windows"], key=lambda x: x[1])
        high = max(m["windows"], key=lambda x: x[1])
        if lo is not None and low[1] < lo - 1e-6:
            s = low[0]
            out.append(fail("V-CADENCE", c.beat_id(s), s,
                            f"only {low[1]:.1f} weighted state changes in the 10 s from {s:.1f} s (style range {lo}-{hi if hi is not None else '...'})",
                            f"add state changes between {s:.1f} and {s + WINDOW_S:.1f} s: scene events, a caption swap, a camera move, "
                            "a layout change or a cut"))
        if hi is not None and high[1] > hi + 1e-6:
            s = high[0]
            out.append(fail("V-CADENCE", c.beat_id(s), s,
                            f"{high[1]:.1f} weighted state changes in the 10 s from {s:.1f} s (style range {lo}-{hi}); too busy for this style",
                            f"merge or drop some changes between {s:.1f} and {s + WINDOW_S:.1f} s (fewer entrances/events, longer caption chunks)"))
    need = q.get("hook_sc_3s")
    if need is not None and m["stats"]["hook_sc_3s"] < float(need) - 1e-6:
        out.append(fail("V-CADENCE", c.beat_id(0), 0,
                        f"the hook has {m['stats']['hook_sc_3s']:.1f} weighted state changes in 0-3 s (needs {need})",
                        "add state changes in the first 3 s: scene events, caption swaps, a camera move or a cut"))
    gap, hook_gap = q.get("max_gap_s"), q.get("hook_max_gap_s")
    if gap is not None or hook_gap is not None:
        hook_end = m["hook_end"]
        for a, b in m["gaps"]:
            ta, tb, g = a / FPS, b / FPS, (b - a) / FPS
            in_hook = ta < hook_end - 1e-6
            limit = hook_gap if in_hook and hook_gap is not None else gap
            if limit is None or g <= float(limit) + 1e-6:
                continue
            out.append(fail("V-CADENCE", c.beat_id(ta), ta,
                            f"no full-weight state change for {g:.1f} s ({ta:.1f} to {tb:.1f}); {'hook' if in_hook else 'body'} "
                            f"max gap is {limit} s" + (" (caption swaps alone don't fill a gap)" if any(
                                a < n < b for n in m['scf'] if m['scf'][n][0] < 1) else ""),
                            f"add a scene, scene event, camera move, layout change or cut around {(ta + tb) / 2:.1f} s"))
    st = q.get("max_static_s")
    if st is not None:
        for a, b in m["statics"]:
            if (b - a) / FPS > float(st) + 1e-6:
                ta = a / FPS
                out.append(fail("V-CADENCE", c.beat_id(ta), ta,
                                f"the frame is static for {(b - a) / FPS:.1f} s ({ta:.1f} to {b / FPS:.1f}): no state change and no "
                                f"continuous motion (max {st} s)",
                                "add continuous motion (push-drift, ambient drift, Ken Burns) or a state change in that span"))
    cpm = as_range(q.get("cuts_per_min"))
    if cpm:
        lo, hi = cpm
        v = m["stats"]["cuts_per_min"]
        if (lo is not None and v < lo - 1e-6) or (hi is not None and v > hi + 1e-6):
            out.append(fail("V-CADENCE", None, 0, f"{v:.1f} cuts per minute (style range {lo}-{hi if hi is not None else '...'})",
                            "re-cut so the shot rhythm matches the style"))
    msh = as_range(q.get("median_shot_s"))
    if msh and m["stats"]["median_shot_s"] is not None:
        lo, hi = msh if isinstance(q.get("median_shot_s"), list) else (None, msh[0])
        v = m["stats"]["median_shot_s"]
        if (lo is not None and v < lo - 1e-6) or (hi is not None and v > hi + 1e-6):
            out.append(fail("V-CADENCE", None, 0, f"median shot length {v:.2f} s (style {q.get('median_shot_s')})",
                            "re-cut so the median shot length matches the style"))
    return out


# --------------------------------------------------------------------------- legacy M7
def rule_m7(c, p: dict) -> list[dict]:
    """The reference M7, unchanged: gaps between visual events (scene in/out, stage, camera, transitions, events)."""
    out = []
    b = c.budgets
    every, hook_every = b.get("change_every_s", 1.5), b.get("hook_change_every_s", 1.0)
    max_static = b.get("max_static_s", 2.5)
    hooks = c.section_range(lambda s: s.upper() == "HOOK")
    ev = c.visual_events()
    for a, bb in zip(ev, ev[1:]):
        gap = (bb - a) / FPS
        ta = a / FPS
        in_hook = any(h0 - 1e-6 <= ta < h1 - 1e-6 for h0, h1 in hooks)
        limit = hook_every if in_hook else every
        if gap > max_static + 1e-6:
            msg = f"nothing changes for {gap:.1f} s ({ta:.1f} to {bb / FPS:.1f}); the maximum static time is {max_static} s"
        elif gap > limit + 1e-6:
            msg = f"nothing changes for {gap:.1f} s ({ta:.1f} to {bb / FPS:.1f}); {'hook' if in_hook else 'body'} limit is {limit} s"
        else:
            continue
        mid = (a + bb) / 2 / FPS
        out.append(fail("V-CADENCE", c.beat_id(ta), ta, msg,
                        f"add a scene, scene event, camera move or stage change around {mid:.1f} s (between {ta:.1f} and {bb / FPS:.1f})"))
    return out
