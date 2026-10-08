"""Global quality checks G1-G3 for `veos validate`: always on, for every playbook (they are not in a playbook's rules_v0).

They read the measured rects (plan/measure.json + plan/measure.motion.json, merged by validate) and the scene meta.
`veos measure` records the auto-subtitles under the id "__subtitles".

G1 NO OVERLAP     text-bearing scenes, z>=5 non-behind scenes and the subtitles must not intersect by more than 2% of the
                  smaller rect, unless one declares `overlaps: ["<other id>"]`; z11 light passes are exempt. E-06: `ambient`
                  items (E4 field texture) and a declared E2 chaos burst (one element, NC-2 relaxed inside it) are exempt.
G2 NO CLUTTER     at most 4 active scenes with z 3..10 (not behind, not z11, not `ambient`) and at most 3 text elements
                  (subtitles included; TC-legal, TC-decorative and `ambient` items not counted). Frames inside a declared
                  E2 chaos burst are not counted (V-EXC checks the burst's own limits and the clean frame after it).
G3 SMOOTH MOTION  a scene's rect centre may not jump > 90 px, nor its width/height change > 25%, between two consecutive
                  frames, except inside the scene's entrance / exit window (vcommon.enter_frames / exit_frames: the
                  declared `enter_s` / `exit_s`, else the preset's length, at least 6 / 4 frames) and within 2 frames
                  of a declared `events` time / a declared `cuts` time (`cuts` and `events` are LOCAL seconds after t_in).
                  G1 likewise skips frames where either scene is still entering or already leaving. z11 and the subtitles are exempt, and so are the
                  content swaps of a scene using a declared E6 hard swap (V-EXC holds its container rect to +-4 px).
                  A stepped scene (`step_frames` / `step_fps`, poses held k frames) is judged per pose: k x 90 px, 1.25^k size.
"Declared" = the scene sets `exception: "E2"/"E6"` and the playbook's resolved `exceptions` has that id.

Transitions (feat/fix-validate2): a `kind: "transition"` scene without text that lasts <= 1 s (shards, streaks: a
momentary pass over the cut) is exempt from G1 and G3. G2 does not count an outgoing scene during a declared transition
overlap: the outgoing scene is in its exit window, the incoming one (active, in its entrance window) starts <= 3 frames
before the outgoing one ends, and the push is declared (`smear: true` on both, or the outgoing scene's
`handoff: "<incoming id>"`). Text never stops counting anywhere else.
"""
from __future__ import annotations

import math
from typing import Any, Callable

from .canvascam import uncam_rect  # E-14 hook (feat/faceless): G3 judges a scene's own motion, not the canvas camera's
from .typefloors import g2_uncounted_text, uses
from .vcommon import enter_frames, exit_frames, settled_at, step_of

FPS = 30
SUBS = "__subtitles"
G1_OVERLAP = 0.02
G2_MAX_SCENES = 4
G2_MAX_TEXT = 3
G3_JUMP_PX = 90
G3_SIZE = 0.25
G3_GRACE = 2
SAMPLE_EVERY = 5
TRANSITION_MAX_S = 1.0   # a transition scene longer than this is a graphic, not a pass over the cut
HANDOFF_MAX_F = 3        # a declared push in/out may overlap the outgoing and incoming scenes by up to 3 frames


def _fr(t: Any) -> int:
    return int(round(float(t) * FPS))


def _fail(rule, beat, t, msg, fix):
    return {"rule": rule, "beat": beat, "t": round(float(t), 3), "msg": msg, "fix": fix}


def _area(r) -> float:
    return max(0.0, r[2] - r[0]) * max(0.0, r[3] - r[1])


def _inter(a, b) -> float:
    return max(0.0, min(a[2], b[2]) - max(a[0], b[0])) * max(0.0, min(a[3], b[3]) - max(a[1], b[1]))


def _declares(s: dict | None, other: str) -> bool:
    ov = (s or {}).get("overlaps")
    return isinstance(ov, (list, tuple)) and other in [str(x) for x in ov]


def is_transition(s: dict | None) -> bool:
    """A momentary transition pass (kind transition, no text, <= TRANSITION_MAX_S): exempt from G1 and G3."""
    if not s or s.get("kind") != "transition" or s.get("text"):
        return False
    try:
        return float(s.get("t_out", 0)) - float(s.get("t_in", 0)) <= TRANSITION_MAX_S + 1e-6
    except (TypeError, ValueError):
        return False


def _pushes(a: dict, b: dict) -> bool:
    """`a` hands off to `b` by a declared push (smear on both, or a.handoff == b.id) overlapping <= HANDOFF_MAX_F."""
    if not ((a.get("smear") and b.get("smear")) or str(a.get("handoff", "")) == str(b.get("id"))) or a is b:
        return False
    ov = _fr(a.get("t_out", 0)) - _fr(b.get("t_in", 0))
    return 0 < ov <= HANDOFF_MAX_F and _fr(b.get("t_in", 0)) > _fr(a.get("t_in", 0))


def handing_off(act: list[dict], s: dict, n: int) -> bool:
    """Scene `s` is the outgoing side of a declared transition overlap at frame n (G2 does not count it)."""
    if str(s.get("out") or "none") == "none" or n < _fr(s.get("t_out", 0)) - exit_frames(s):
        return False
    return any(_pushes(s, b) and str(b.get("in") or "none") != "none" and n < _fr(b.get("t_in", 0)) + enter_frames(b)
               for b in act)


def _name(i: str) -> str:
    return "the subtitles" if i == SUBS else f"'{i}'"


def g1(c) -> list[dict]:
    out, seen = [], set()
    byid = {s.get("id"): s for s in c.scenes}
    burst = {s.get("id") for s in c.scenes if uses(c, s, "E2")}
    for n in sorted(c.measured):
        items = []
        for sid, r in c.measured[n].items():
            if sid == SUBS:
                items.append((SUBS, None, r))
                continue
            s = byid.get(sid)
            if s is None or not c.active(s, n) or s.get("z") == 11 or s.get("ambient") or sid in burst or is_transition(s):
                continue
            if not settled_at(s, n):  # an entrance / exit animation passing by is not an overlap
                continue
            if c.is_text(s) or (s.get("z", 0) >= 5 and not s.get("behind")):
                items.append((sid, s, r))
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                (ia, sa, ra), (ib, sb, rb) = items[i], items[j]
                key = tuple(sorted((ia, ib)))
                if key in seen or _declares(sa, ib) or _declares(sb, ia):
                    continue
                small = min(_area(ra), _area(rb))
                if small <= 0 or _inter(ra, rb) <= G1_OVERLAP * small:
                    continue
                seen.add(key)
                # the later-starting scene moves; the subtitles never move
                if ia == SUBS or (ib != SUBS and (sa.get("t_in", 0), ia) <= (sb.get("t_in", 0), ib)):
                    fixed, mover, rf, rm = ia, ib, ra, rb
                else:
                    fixed, mover, rf, rm = ib, ia, rb, ra
                down, up = rf[3] - rm[1] + 16, rm[3] - rf[1] + 16
                if down <= up:
                    move = f"move {_name(mover)} below {_name(fixed)} by about {int(round(down))} px"
                else:
                    move = f"move {_name(mover)} above {_name(fixed)} by about {int(round(up))} px"
                top = mover if mover != SUBS else fixed
                under = fixed if mover != SUBS else mover
                t = n / FPS
                out.append(_fail(
                    "G1", c.beat_id(t), t,
                    f"{_name(ia)} and {_name(ib)} overlap ({round(100 * _inter(ra, rb) / small)}% of the smaller one) "
                    f"from {t:.2f} s (frame {n})",
                    f"{move}, or show them at different times; if the overlap is deliberate (e.g. a chip pinned on its card) "
                    f"add overlaps: [\"{under}\"] to '{top}'"))
    return out


def g2_counts_text(c, s: dict) -> bool:
    """Does this scene count toward the G2 text limit? Every text scene below z11, except TC-legal and TC-decorative text
    and E4 `ambient` items (structure Definitions)."""
    return c.is_text(s) and s.get("z", 0) < 11 and not g2_uncounted_text(s)


def g2(c) -> list[dict]:
    out = []
    frames = sorted(c.measured) if c.measured else list(range(0, max(c.frames, 1), SAMPLE_EVERY))
    bad = {"scenes": [], "text": []}
    bursts = [s for s in c.scenes if uses(c, s, "E2")]
    for n in frames:
        if any(c.active(b, n) for b in bursts):
            continue
        act = [s for s in c.scenes if c.active(s, n)]
        act = [s for s in act if not handing_off(act, s, n)]  # the outgoing card of a declared push in/out
        panels = [s["id"] for s in act if 3 <= s.get("z", 0) <= 10 and not s.get("behind") and not s.get("ambient")]
        texts = [s["id"] for s in act if g2_counts_text(c, s)]
        if SUBS in c.measured.get(n, {}):
            texts.append("the subtitles")
        if len(panels) > G2_MAX_SCENES:
            bad["scenes"].append((n, panels))
        if len(texts) > G2_MAX_TEXT:
            bad["text"].append((n, texts))
    for kind, limit, noun in (("scenes", G2_MAX_SCENES, "scenes"), ("text", G2_MAX_TEXT, "text elements")):
        groups: list[list] = []
        for n, ids in bad[kind]:
            if groups and n - groups[-1][-1][0] <= 12:
                groups[-1].append((n, ids))
            else:
                groups.append([(n, ids)])
        for g in groups:
            ids = sorted({i for _, l in g for i in l})
            t0, t1 = g[0][0] / FPS, g[-1][0] / FPS
            peak = max(len(l) for _, l in g)
            out.append(_fail(
                "G2", c.beat_id(t0), t0,
                f"too much on screen: {peak} {noun} at once between {t0:.2f} s and {t1:.2f} s (max {limit}): {', '.join(ids)}",
                f"remove or shorten one of {', '.join(ids)} so at most {limit} {noun} show together "
                "(merge two text elements into one, or move one to a later time)"))
    return out


def g3(c) -> list[dict]:
    out = []
    for s in c.scenes:
        sid = s.get("id")
        if s.get("z") == 11 or uses(c, s, "E6") or isinstance(s.get("anchor"), dict):  # anchored: the motion is the tracked object's (V-ANCHOR)
            continue
        if is_transition(s):  # shards / streaks fly across the cut by design
            continue
        fin, fout = _fr(s.get("t_in", 0)), _fr(s.get("t_out", 0))
        ent, ext = fin + enter_frames(s), fout - exit_frames(s)
        allowed = [fin, fout]
        for key in ("events", "cuts"):
            for v in s.get(key) or []:
                try:
                    allowed.append(fin + _fr(v))
                except (TypeError, ValueError):
                    pass
        pts = sorted((n, m[sid]) for n, m in c.measured.items() if sid in m)
        pts = [(n, uncam_rect(c, s, n, r)) for n, r in pts]  # E-14 hook (feat/faceless): camera motion is V-CANVAS's job
        # fx-helpers: a stepped scene (step_frames / step_fps) holds each pose k frames and moves once per pose, so the
        # per-frame limits apply per pose: up to k x 90 px and (1.25^k - 1) size change on the frame the pose changes
        k = step_of(s)
        lim_jump, lim_size = G3_JUMP_PX * math.ceil(k), (1 + G3_SIZE) ** math.ceil(k) - 1
        hits = []
        for (n0, r0), (n1, r1) in zip(pts, pts[1:]):
            if n1 != n0 + 1 or any(abs(n1 - a) <= G3_GRACE or abs(n0 - a) <= G3_GRACE for a in allowed):
                continue
            if n1 <= ent or n0 >= ext:  # the entrance / exit animation
                continue
            w0, h0, w1, h1 = r0[2] - r0[0], r0[3] - r0[1], r1[2] - r1[0], r1[3] - r1[1]
            dx = ((r1[0] + r1[2]) - (r0[0] + r0[2])) / 2
            dy = ((r1[1] + r1[3]) - (r0[1] + r0[3])) / 2
            jump = (dx * dx + dy * dy) ** 0.5
            size = max(abs(w1 / w0 - 1) if w0 > 1 else 0, abs(h1 / h0 - 1) if h0 > 1 else 0)
            if jump > lim_jump or size > lim_size:
                hits.append((n1, jump, size))
        if hits:
            n1, jump, size = hits[0]
            t = n1 / FPS
            what = f"jumps {int(round(jump))} px" if jump > lim_jump else f"changes size by {int(round(size * 100))}%"
            more = f" ({len(hits)} such frames)" if len(hits) > 1 else ""
            out.append(_fail(
                "G3", c.beat_id(t), t,
                f"'{sid}' {what} in a single frame at {t:.2f} s (frame {n1}){more}",
                f"animate '{sid}' over at least 6 frames with ctx.ease instead of snapping; if the cut is deliberate declare "
                f"cuts: [{round(t - float(s.get('t_in', 0)), 2)}] (or events) on the scene"))
    return out


GLOBAL_CHECKS: dict[str, Callable[[Any], list]] = {"G1": g1, "G2": g2, "G3": g3}
