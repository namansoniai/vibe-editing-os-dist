"""V-THEME and V-REHOOK (ENGINE-IMPLICATIONS section 2, both P0): reel-level structure rules, short-form only.

V-THEME (STYLE-PLAYBOOK-STRUCTURE section 0.5 theme packs, SW-10 `themes`)
  One theme per reel unless `profile.themes.policy` is `per_section`. The reel's theme is `meta.theme` (the reel header),
  else the first beat's `theme`, else `profile.themes.default`. Theme changes come from `beats[].theme` (a beat that names
  another theme than the one running) and `timeline.theme_flips[] = {t, theme}`.
    * policy single / per_reel / per_topic: any change of theme inside the reel fails;
    * policy per_section: each flip must land on a section boundary (a beat start where `section` changes; with no sections,
      any beat start; one frame of tolerance) and flips must be >= `min_gap_s` apart (default 5: at most 1 per 5 s);
    * a theme id outside `profile.themes.packs` (when packs are listed) fails under any policy.
  Params (validator.rules["V-THEME"]): min_gap_s.

V-REHOOK (SW-06 `duration`, section 7.4 open loops and re-hooks)
  Duration class: the class of the reel's real length (micro <= 30 s, short 30-60, standard 60-90, long 90-180), capped by
  `profile.duration.class` when the style declares one (a 24 s clip of a long-class style owes no re-hooks). A re-hook is
  a beat with `rehook`, a scene with `rehook` or kind `rehook` / `teaser` / `question-card` /
  `evidence-slide` (a numeral teaser, a question card, a new evidence slide), or an entry of `timeline.rehooks[]`
  (a time, or {t}).
    * every class: the intro (the leading run of HOOK / INTRO / SERIES / TITLE beats) is at most
      `structure.intro_max_ratio` (default 0.15) of the runtime;
    * standard: at least one re-hook in the middle of the reel (`mid` = [0.25, 0.75] of the runtime); when
      `structure.rehook_every_s` is set, no gap longer than that;
    * long: a re-hook every 20-30 s: no gap (intro end -> re-hooks -> the CTA start or the end) longer than
      `structure.rehook_every_s` (default 30).
  micro and short reels carry no re-hook obligation. Params (validator.rules["V-REHOOK"]): intro_max_ratio, mid, max_gap_s.
"""
from __future__ import annotations

from .vcommon import fail, fr, get_path

INTRO_SECTIONS = ("HOOK", "INTRO", "SERIES", "TITLE")
REHOOK_KINDS = ("rehook", "teaser", "question-card", "evidence-slide")


# --------------------------------------------------------------------------- V-THEME
def _section_starts(c) -> list[int]:
    """Frames where a section starts (a beat whose `section` differs from the previous beat's; every beat when none is named)."""
    out, prev = [], object()
    named = any(b.get("section") for b in c.beats)
    for b in c.beats:
        sec = b.get("section")
        if not named or sec != prev:
            out.append(fr(b.get("t0", 0)))
        prev = sec
    return out


def theme_flips(c) -> tuple[str | None, list[tuple[float, str, str]]]:
    """(the reel's opening theme, [(t, new theme, where)]) from beats[].theme and timeline.theme_flips[]."""
    start = c.meta.get("theme") or next((b.get("theme") for b in c.beats if b.get("theme")), None) \
        or get_path(c.style, "profile.themes.default")
    ev: list[tuple[float, str, str]] = []
    for b in c.beats:
        if b.get("theme"):
            ev.append((float(b.get("t0", 0)), str(b["theme"]), f"beat {b.get('id')}"))
    for e in c.tl.get("theme_flips") or []:
        if isinstance(e, dict) and "t" in e and e.get("theme"):
            ev.append((float(e["t"]), str(e["theme"]), "theme_flips"))
    ev.sort(key=lambda e: e[0])
    flips, cur = [], start
    for t, th, where in ev:
        if cur is None:
            cur = th
            continue
        if th != cur:
            flips.append((t, th, where))
            cur = th
    return (str(start) if start else None), flips


def rule_theme(c, p: dict):
    policy = get_path(c.style, "profile.themes.policy") or "single"
    packs = list(get_path(c.style, "profile.themes.packs") or [])
    start, flips = theme_flips(c)
    out = []
    used = ([start] if start else []) + [th for _, th, _ in flips]
    if packs:
        for th in dict.fromkeys(used):
            if th not in packs:
                out.append(fail("V-THEME", None, 0, f"theme {th} is not one of the style's packs ({', '.join(packs)})",
                                f"use a declared pack, or add {th} to profile.themes.packs"))
    c.stats_extra["theme"] = {"policy": policy, "theme": start, "flips": len(flips)}
    if policy != "per_section":
        for t, th, where in flips:
            out.append(fail("V-THEME", c.beat_id(t), t, f"{where} switches the theme to {th} at {t:.2f} s: policy {policy} allows one theme per reel",
                            f"keep {start} for the whole reel (or set profile.themes.policy: per_section)"))
        return out
    starts = set(_section_starts(c))
    gap = float(p.get("min_gap_s", 5.0))
    prev = None
    for t, th, where in flips:
        if not any(abs(fr(t) - s) <= 1 for s in starts):
            out.append(fail("V-THEME", c.beat_id(t), t, f"theme flip to {th} at {t:.2f} s is not on a section boundary",
                            "move the flip to the start of a section"))
        if prev is not None and t - prev < gap - 1e-6:
            out.append(fail("V-THEME", c.beat_id(t), t, f"theme flips at {prev:.2f} s and {t:.2f} s are {t - prev:.1f} s apart (at most 1 per {gap:g} s)",
                            f"drop one of the flips or move them at least {gap:g} s apart"))
        prev = t
    return out


# --------------------------------------------------------------------------- V-REHOOK
CLASSES = ("micro", "short", "standard", "long")


def length_class(d: float) -> str:
    return "micro" if d <= 30 else "short" if d <= 60 else "standard" if d <= 90 else "long"


def duration_class(c) -> str:
    """The class whose re-hook rules apply to this reel: the class of its real length, capped by the style's declared
    `profile.duration.class`. A 24 s clip of a long-class style (a conversation clip, a stills sample) is micro and
    owes no re-hooks; a reel longer than its style's class keeps the style's (lighter) rules."""
    by_len = length_class(c.duration)
    cls = get_path(c.style, "profile.duration.class")
    if cls in CLASSES:
        return CLASSES[min(CLASSES.index(cls), CLASSES.index(by_len))]
    return by_len


def intro_end(c) -> float:
    """End of the leading run of intro beats (0 when the reel opens on something else)."""
    end = 0.0
    for b in c.beats:
        sec = str(b.get("section", "")).upper().replace("_", "-").split("-")[0]
        if sec in INTRO_SECTIONS and float(b.get("t0", 0)) <= end + 1e-6:
            end = float(b.get("t1", end))
        else:
            break
    return end


def rehooks(c) -> list[float]:
    ts = [float(b.get("t0", 0)) for b in c.beats if b.get("rehook")]
    ts += [float(s.get("t_in", 0)) for s in c.scenes if s.get("rehook") or s.get("kind") in REHOOK_KINDS]
    for e in c.tl.get("rehooks") or []:
        try:
            ts.append(float(e.get("t") if isinstance(e, dict) else e))
        except (TypeError, ValueError):
            pass
    return sorted(set(round(t, 3) for t in ts))


def rule_rehook(c, p: dict):
    out = []
    dur = c.duration
    if dur <= 0:
        return out
    cls = duration_class(c)
    ie = intro_end(c)
    ratio = float(p.get("intro_max_ratio", get_path(c.style, "structure.intro_max_ratio") or 0.15))
    if ie / dur > ratio + 1e-6:
        out.append(fail("V-REHOOK", c.beat_id(0), 0, f"the intro runs {ie:.1f} s = {ie / dur:.0%} of the {dur:.1f} s reel (max {ratio:.0%})",
                        f"cut the hook / series card to {ratio * dur:.1f} s or less"))
    hooks = rehooks(c)
    every = get_path(c.style, "structure.rehook_every_s")
    c.stats_extra["rehook"] = {"class": cls, "intro_s": round(ie, 2), "intro_ratio": round(ie / dur, 3), "rehooks": hooks}
    if cls in ("micro", "short"):
        return out
    if cls == "standard":
        lo, hi = p.get("mid") or [0.25, 0.75]
        if not any(lo * dur - 1e-6 <= t <= hi * dur + 1e-6 for t in hooks):
            out.append(fail("V-REHOOK", c.beat_id(dur / 2), dur / 2,
                            f"a standard reel ({dur:.0f} s) needs one re-hook in the middle ({lo * dur:.0f}-{hi * dur:.0f} s); none found",
                            "add a numeral teaser, a question card or a new evidence slide there (beat.rehook, or a scene of kind 'rehook')"))
        limit = p.get("max_gap_s", every)
    else:
        limit = p.get("max_gap_s", every if every else 30)
        if not hooks:
            out.append(fail("V-REHOOK", c.beat_id(dur / 2), dur / 2,
                            f"a long reel ({dur:.0f} s) needs a re-hook every {float(limit):g} s; none found",
                            "add re-hooks (numeral teaser, question card, new evidence slide)"))
    if limit:
        limit = float(limit)
        cta = [b["t0"] for b in c.beats if str(b.get("section", "")).upper() == "CTA"]
        end = min(cta) if cta else dur
        pts = [ie] + [t for t in hooks if ie < t < end] + [end]
        for a, b in zip(pts, pts[1:]):
            if b - a > limit + 1e-6:
                out.append(fail("V-REHOOK", c.beat_id(a), a, f"no re-hook between {a:.1f} s and {b:.1f} s ({b - a:.1f} s; max {limit:g} s)",
                                f"add a re-hook by {a + limit:.0f} s"))
    return out
