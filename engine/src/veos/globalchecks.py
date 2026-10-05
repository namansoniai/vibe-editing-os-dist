"""Global quality checks G1-G3 for `veos validate`: always on, for every playbook (they are not in a playbook's rules_v0).

They read the measured rects (plan/measure.json + plan/measure.motion.json, merged by validate) and the scene meta.
`veos measure` records the auto-subtitles under the id "__subtitles".

G1 NO OVERLAP     text-bearing scenes, z>=5 non-behind scenes and the subtitles must not intersect by more than 2% of the
                  smaller rect, unless one declares `overlaps: ["<other id>"]`; z11 light passes are exempt.
G2 NO CLUTTER     at most 4 active scenes with z 3..10 (not behind, not z11) and at most 3 text elements (subtitles included).
G3 SMOOTH MOTION  a scene's rect centre may not jump > 90 px, nor its width/height change > 25%, between two consecutive
                  frames, except within 2 frames of t_in / t_out / a declared `events` time / a declared `cuts` time
                  (`cuts` and `events` are LOCAL seconds after t_in). z11 and the subtitles are exempt.
"""
from __future__ import annotations

from typing import Any, Callable

FPS = 30
SUBS = "__subtitles"
G1_OVERLAP = 0.02
G2_MAX_SCENES = 4
G2_MAX_TEXT = 3
G3_JUMP_PX = 90
G3_SIZE = 0.25
G3_GRACE = 2
SAMPLE_EVERY = 5


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


def _name(i: str) -> str:
    return "the subtitles" if i == SUBS else f"'{i}'"


def g1(c) -> list[dict]:
    out, seen = [], set()
    byid = {s.get("id"): s for s in c.scenes}
    for n in sorted(c.measured):
        items = []
        for sid, r in c.measured[n].items():
            if sid == SUBS:
                items.append((SUBS, None, r))
                continue
            s = byid.get(sid)
            if s is None or not c.active(s, n) or s.get("z") == 11:
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


def g2(c) -> list[dict]:
    out = []
    frames = sorted(c.measured) if c.measured else list(range(0, max(c.frames, 1), SAMPLE_EVERY))
    bad = {"scenes": [], "text": []}
    for n in frames:
        act = [s for s in c.scenes if c.active(s, n)]
        panels = [s["id"] for s in act if 3 <= s.get("z", 0) <= 10 and not s.get("behind")]
        texts = [s["id"] for s in act if c.is_text(s) and s.get("z", 0) < 11]
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
        if s.get("z") == 11:
            continue
        fin, fout = _fr(s.get("t_in", 0)), _fr(s.get("t_out", 0))
        allowed = [fin, fout]
        for key in ("events", "cuts"):
            for v in s.get(key) or []:
                try:
                    allowed.append(fin + _fr(v))
                except (TypeError, ValueError):
                    pass
        pts = sorted((n, m[sid]) for n, m in c.measured.items() if sid in m)
        hits = []
        for (n0, r0), (n1, r1) in zip(pts, pts[1:]):
            if n1 != n0 + 1 or any(abs(n1 - a) <= G3_GRACE or abs(n0 - a) <= G3_GRACE for a in allowed):
                continue
            w0, h0, w1, h1 = r0[2] - r0[0], r0[3] - r0[1], r1[2] - r1[0], r1[3] - r1[1]
            dx = ((r1[0] + r1[2]) - (r0[0] + r0[2])) / 2
            dy = ((r1[1] + r1[3]) - (r0[1] + r0[3])) / 2
            jump = (dx * dx + dy * dy) ** 0.5
            size = max(abs(w1 / w0 - 1) if w0 > 1 else 0, abs(h1 / h0 - 1) if h0 > 1 else 0)
            if jump > G3_JUMP_PX or size > G3_SIZE:
                hits.append((n1, jump, size))
        if hits:
            n1, jump, size = hits[0]
            t = n1 / FPS
            what = f"jumps {int(round(jump))} px" if jump > G3_JUMP_PX else f"changes size by {int(round(size * 100))}%"
            more = f" ({len(hits)} such frames)" if len(hits) > 1 else ""
            out.append(_fail(
                "G3", c.beat_id(t), t,
                f"'{sid}' {what} in a single frame at {t:.2f} s (frame {n1}){more}",
                f"animate '{sid}' over at least 6 frames with ctx.ease instead of snapping; if the cut is deliberate declare "
                f"cuts: [{round(t - float(s.get('t_in', 0)), 2)}] (or events) on the scene"))
    return out


GLOBAL_CHECKS: dict[str, Callable[[Any], list]] = {"G1": g1, "G2": g2, "G3": g3}
