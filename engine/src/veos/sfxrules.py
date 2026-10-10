"""Validator rules S1-S6 for catalogue sound cues (`timeline.sfx` items with an `id`). Always on when the timeline has such cues.

Cue: {"t": edit s where the file's anchor lands, "id": catalogue id, "db"?, "beat"?, "on": "<scene>@<local s>|stage@<t>|camera@<t>|
transition@<t>", "why": "..."}. Legacy cues ({"file": ...}) are left to M10/M9.

S1 tied to picture   S2 vibe match   S3 palette   S4 restraint   S5 ledger   S6 catalogue
S4's density count (sounds per 10 s) is taste (vcommon.taste): validate leaves it out of its output.
`fail` comes from validate.py (imported lazily to avoid a cycle).
"""
from __future__ import annotations

import re

from .core import FPS
from .vcommon import taste

TOL_FRAMES = 3
DEFAULT_PALETTE = {  # tone.energy -> vibes the playbook's sound may use
    "calm": ["calm", "premium", "organic"],
    "premium": ["premium", "calm", "techy"],
    "playful": ["playful", "comedic", "premium", "techy"],
    "hype": ["hype", "premium", "techy", "playful", "tense"],
    "techy": ["techy", "calm", "premium"],
}
BEAT_VIBES = {"mock": {"comedic", "playful"}, "warn": {"tense"}, "awe": {"premium", "calm"},
              "explain": {"techy", "calm", "premium"}, "hype": {"hype", "premium"}, "win": {"premium", "playful"},
              "cta": {"premium", "calm"}}
MEME_ROLES = {"meme"}


def cues(c) -> list[dict]:
    return [s for s in c.sfx if "id" in s]


def _fr(t) -> int:
    return int(round(float(t) * FPS))


def _fail(*a):
    from .validate import fail
    return fail(*a)


def _beat(c, cue):
    b = next((x for x in c.beats if x.get("id") == cue.get("beat")), None) if cue.get("beat") is not None else None
    return b or c.beat_at(float(cue.get("t", 0)))


def _bid(c, cue):
    b = _beat(c, cue)
    return b.get("id") if b else cue.get("beat")


def palette_vibes(c) -> list[str]:
    snd = c.style.get("sound") or {}
    if snd.get("palette_vibes"):
        return list(snd["palette_vibes"])
    tone = c.style.get("tone") or {}
    pal = list(DEFAULT_PALETTE.get(tone.get("energy"), DEFAULT_PALETTE["hype"]))
    if tone.get("meme_sfx") and "comedic" not in pal:
        pal.append("comedic")
    return pal


# --------------------------------------------------------------------------- S1
def _resolve_on(c, on: str):
    """-> (event time, error message). Time is the real event instant in edit seconds."""
    m = re.fullmatch(r"\s*([^@\s]+)\s*@\s*(\S+)\s*", str(on or ""))
    if not m:
        return None, f"`on` is '{on}' (expected scene-id@local-seconds, stage@t, camera@t or transition@t)"
    kind, arg = m.group(1), m.group(2)
    if kind in ("stage", "camera", "transition"):
        try:
            want = float(arg)
        except ValueError:
            return None, f"`on` time '{arg}' is not a number"
        evs = {"stage": c.stage, "camera": c.camera, "transition": c.transitions}[kind]
        near = [float(e.get("t", 0)) for e in evs if abs(_fr(e.get("t", 0)) - _fr(want)) <= TOL_FRAMES]
        if not near:
            have = ", ".join(f"{float(e.get('t', 0)):.2f}" for e in evs) or "none"
            return None, f"there is no {kind} event at {want:.2f} s (the timeline has: {have})"
        return min(near, key=lambda e: abs(e - want)), None
    sc = next((s for s in c.scenes if s.get("id") == kind), None)
    if sc is None:
        return None, f"scene '{kind}' does not exist"
    t_in, t_out = float(sc.get("t_in", 0)), float(sc.get("t_out", 0))
    local = {"in": 0.0, "out": t_out - t_in}.get(arg)
    if local is None:
        try:
            local = float(arg)
        except ValueError:
            return None, f"`on` local time '{arg}' is not a number (or in / out)"
    evs = []
    for v in sc.get("events") or []:
        try:
            evs.append(float(v))
        except (TypeError, ValueError):
            pass
    cands = [0.0, t_out - t_in] + evs
    hit = [v for v in cands if abs(_fr(v) - _fr(local)) <= TOL_FRAMES]
    if not hit:
        return None, (f"scene {kind} has no event at {local:.2f} s after it starts (it has: in 0.00, "
                      + ", ".join(f"event {v:.2f}" for v in cands[2:]) + (", " if len(cands) > 2 else "") + f"out {t_out - t_in:.2f})")
    return t_in + min(hit, key=lambda v: abs(v - local)), None


def s1(c):
    out = []
    for q in cues(c):
        t = float(q.get("t", 0))
        if not q.get("on"):
            out.append(_fail("S1", _bid(c, q), t, f"sound '{q['id']}' at {t:.2f} s is not tied to anything on screen (no `on`)",
                             "add on: a scene start/event (\"<scene>@<local s>\"), \"stage@t\", \"camera@t\" or \"transition@t\", or remove the sound"))
            continue
        ev, err = _resolve_on(c, q["on"])
        if err:
            out.append(_fail("S1", _bid(c, q), t, f"sound '{q['id']}' at {t:.2f} s: {err}",
                             "point `on` at a real visual moment (scene t_in/t_out/events, stage, camera or transition), or remove the sound"))
        elif abs(_fr(t) - _fr(ev)) > TOL_FRAMES:
            out.append(_fail("S1", _bid(c, q), t, f"sound '{q['id']}' lands at {t:.2f} s but its visual moment ({q['on']}) is at {ev:.2f} s "
                             f"({(t - ev) * 1000:+.0f} ms; at most {TOL_FRAMES} frames)",
                             f"set the cue t to {ev:.2f} (the sound's anchor lands on the picture), or move the visual"))
    return out


# --------------------------------------------------------------------------- S2
def s2(c):
    out = []
    pal = set(palette_vibes(c))
    meme_ok = bool((c.style.get("tone") or {}).get("meme_sfx"))
    for q in cues(c):
        e = c.catalog_by_id.get(q["id"]) if c.catalog_by_id else None
        if e is None:
            continue  # S6 reports it
        t, vibe, b = float(q.get("t", 0)), set(e.get("vibe") or []), _beat(c, q)
        tone = b.get("tone") if b else None
        if not vibe:
            out.append(_fail("S2", _bid(c, q), t, f"sound '{q['id']}' has no vibe tags, so it cannot be matched to the reel",
                             f"review the catalogue (veos sfx tag) or pick a tagged sound at {t:.2f} s"))
            continue
        if not (vibe & pal):
            out.append(_fail("S2", _bid(c, q), t, f"sound '{q['id']}' feels {'/'.join(sorted(vibe))}, but this playbook's sound is "
                             f"{'/'.join(sorted(pal))}",
                             f"swap the sound at {t:.2f} s for one tagged {'/'.join(sorted(pal))} (or set tokens sound.palette_vibes)"))
        want = BEAT_VIBES.get(tone)
        if want and not (vibe & want):
            out.append(_fail("S2", _bid(c, q), t, f"sound '{q['id']}' ({'/'.join(sorted(vibe))}) does not suit a '{tone}' beat "
                             f"(needs {'/'.join(sorted(want))})",
                             f"use a {'/'.join(sorted(want))} sound at {t:.2f} s, or drop it"))
        if e.get("role") in MEME_ROLES or "comedy" in (e.get("use") or []):
            if not meme_ok:
                out.append(_fail("S2", _bid(c, q), t, f"comedy/meme sound '{q['id']}' but this creator's tone has meme_sfx off",
                                 f"remove the sound at {t:.2f} s (or set tone.meme_sfx in the playbook)"))
            elif tone != "mock":
                out.append(_fail("S2", _bid(c, q), t, f"comedy/meme sound '{q['id']}' sits on a '{tone}' beat (mock beats only)",
                                 f"remove the meme sound at {t:.2f} s or move it to a mock beat"))
    return out


# --------------------------------------------------------------------------- S3
def s3(c):
    snd = c.style.get("sound") or {}
    allowed, banned = snd.get("allowed_roles"), set(snd.get("banned_roles") or [])
    out = []
    if not allowed and not banned:
        return out
    for q in cues(c):
        e = c.catalog_by_id.get(q["id"]) if c.catalog_by_id else None
        role = e.get("role") if e else None
        if role is None:
            continue
        t = float(q.get("t", 0))
        if role in banned:
            out.append(_fail("S3", _bid(c, q), t, f"'{role}' sounds are banned by this playbook (sound '{q['id']}')",
                             f"replace it at {t:.2f} s with an allowed role ({', '.join(allowed) if allowed else 'see tokens sound.banned_roles'})"))
        elif allowed and role not in allowed:
            out.append(_fail("S3", _bid(c, q), t, f"'{role}' is not one of this playbook's sound roles ({', '.join(allowed)})",
                             f"replace sound '{q['id']}' at {t:.2f} s with a {'/'.join(allowed)} sound"))
    return out


# --------------------------------------------------------------------------- S4
def _first_word(c, t0):
    ws = [float(w.get("s")) for w in ((c.words or {}).get("words") or []) if w.get("s") is not None and float(w["s"]) >= t0 - 1e-6]
    return min(ws) if ws else t0


def s4(c):
    out = []
    qs = sorted(cues(c), key=lambda q: float(q.get("t", 0)))
    snd = c.style.get("sound") or {}
    cap = c.budgets.get("sfx_per_10s", 6)
    flagged = -99.0
    for i, q in enumerate(qs):
        t = float(q["t"])
        n = sum(1 for r in qs[i:] if float(r["t"]) < t + 10 - 1e-6)
        if n > cap and t > flagged + 10:
            flagged = t
            out.append(taste(_fail("S4", _bid(c, q), t, f"{n} sounds in the 10 s from {t:.1f} s (max {cap})",
                                   f"remove {n - cap} sound(s) between {t:.1f} and {t + 10:.1f} s: keep the ones on the biggest moments")))
    for a, b in zip(qs, qs[1:]):
        if float(b["t"]) - float(a["t"]) < 0.25 - 1e-6:
            ra = (c.catalog_by_id or {}).get(a["id"], {}).get("role")
            rb = (c.catalog_by_id or {}).get(b["id"], {}).get("role")
            if {ra, rb} == {"sub-hit", "impact"}:
                continue
            out.append(_fail("S4", _bid(c, b), float(b["t"]), f"sounds '{a['id']}' and '{b['id']}' are only "
                             f"{(float(b['t']) - float(a['t'])) * 1000:.0f} ms apart (min 250 ms, unless a sub-hit under an impact)",
                             f"drop one of them, or move the later one to its own visual moment"))
    if snd.get("silence_before_cta", True):
        for t0, _t1 in c.section_range(lambda s: s.upper() == "CTA")[:1]:
            fw = _first_word(c, t0)
            for q in qs:
                if fw - 1.0 - 1e-6 <= float(q["t"]) < fw - 1e-6:
                    out.append(_fail("S4", _bid(c, q), float(q["t"]), f"sound '{q['id']}' plays in the 1 s of silence before the CTA "
                                     f"(first CTA word at {fw:.2f} s)",
                                     "remove it; the CTA starts from silence"))
    if snd.get("dry_hook"):
        for t0, t1 in c.section_range(lambda s: s.upper() == "HOOK"):
            for q in qs:
                if t0 - 1e-6 <= float(q["t"]) < t1 - 1e-6:
                    out.append(_fail("S4", _bid(c, q), float(q["t"]), f"sound '{q['id']}' in the hook, but this playbook keeps the hook dry",
                                     "remove the sound from the hook"))
    return out


# --------------------------------------------------------------------------- S5
def s5(c):
    out = []
    mx = c.budgets.get("sfx_max_uses_per_file", 2)
    n_items = len(c.item_numbers())
    qs = sorted(cues(c), key=lambda q: float(q.get("t", 0)))
    uses: dict[str, list[dict]] = {}
    for q in qs:
        uses.setdefault(q["id"], []).append(q)
    list_used = False
    for cid, us in uses.items():
        if len(us) <= mx:
            continue
        e = (c.catalog_by_id or {}).get(cid, {})
        tagged = "list-cue" in (e.get("use") or []) or all(u.get("role") == "list-cue" for u in us)
        list_cue = tagged and all(("list-cue" in (e.get("use") or [])) or u.get("role") == "list-cue" for u in us) and len(us) <= n_items
        if list_cue and not list_used:
            list_used = True
            continue
        why = "only one sound may exceed it, as the list cue (tagged use list-cue, at most one use per item)" \
            if tagged else "only a list-cue sound may be repeated more"
        out.append(_fail("S5", us[mx].get("beat"), float(us[mx]["t"]), f"'{cid}' is used {len(us)} times (max {mx}; {why})",
                         f"replace the use at {float(us[mx]['t']):.2f} s (and any later ones) with a different sound of the same role"))
    for a, b in zip(qs, qs[1:]):
        if a["id"] == b["id"]:
            out.append(_fail("S5", _bid(c, b), float(b["t"]), f"'{b['id']}' is on two consecutive cues",
                             f"swap the cue at {float(b['t']):.2f} s for a different sound with the same role"))
    return out


# --------------------------------------------------------------------------- S6
def s6(c):
    out = []
    if c.catalog_by_id is None:
        q = cues(c)[0]
        return [_fail("S6", _bid(c, q), float(q.get("t", 0)), "the sound-effects catalogue (catalog.json) was not found",
                      "run `veos paths` to find sfx_pack, then `veos sfx catalog --draft` and review it")]
    warned = set()
    for q in cues(c):
        e = c.catalog_by_id.get(q["id"])
        t = float(q.get("t", 0))
        if e is None:
            out.append(_fail("S6", _bid(c, q), t, f"sound id '{q['id']}' is not in the catalogue",
                             "use an id from catalog.json (or re-run `veos sfx catalog`)"))
        elif e.get("excluded"):
            out.append(_fail("S6", _bid(c, q), t, f"sound '{q['id']}' is marked do-not-use in the pack description",
                             "replace it with another sound (excluded sounds cannot be used)"))
        elif e.get("tags_from") != "reviewed" and q["id"] not in warned:
            warned.add(q["id"])
            c.warnings.append(f"S6: sound '{q['id']}' still has draft tags; review them (veos sfx tag)")
    return out


def check_sfx(c) -> list:
    if not cues(c):
        return []
    out = []
    for fn in (s1, s2, s3, s4, s5, s6):
        out.extend(fn(c))
    return out
