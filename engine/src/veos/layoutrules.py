"""V-LAYOUT (E-07, ENGINE-IMPLICATIONS §2): stage layouts against the style's layout library and schedule.

Inputs: timeline.stage[] (`layout` = an engine layout or a tokens.layouts id), the resolved style (`layouts`, the format's
layout list in `_resolved.layouts`), words.edit.json (switch-on words).

Checks (each a failure with a fix):
  * every stage layout resolves (an engine layout, or a tokens.layouts id whose `engine` is an engine layout);
  * a layout outside the reel format's layout list (formats.<F>.layouts) when that list is set;
  * share of runtime per layout within `layouts.<id>.share` [min, max] (fractions 0-1, or percent when max > 1), for the
    layouts of the format (or every layout with a share when the format lists none); a listed layout never used counts 0;
  * `layouts.schedule.max_s` / `min_s` per run of one layout (consecutive entries of the same id, e.g. a dim toggle, are one
    run; the last run is exempt from min_s because the reel end cuts it);
  * `layouts.schedule.switch_on`: every layout switch lands on a word (|switch - word start| <= tol_s, default 0.25 s) of
    one of the classes: claim, but, number, sentence (first word of a sentence), pause (>= 0.25 s silence before it),
    any, or a literal word.
Params (validator.rules["V-LAYOUT"]): tol_s, share_tolerance (absolute fraction, default 0.02), check_format (default true).

Taste, not checks (Naman, 9 Oct 2026): the shares, the schedule min / max and the switch-on words are marked
vcommon.taste() and `veos validate` leaves them out of its output (the code and `stats.layouts` stay). Sync of a switch
to the words is V-ONWORD's job. What V-LAYOUT still says: a layout that does not resolve, a layout outside the
format, a malformed overshoot.
"""
from __future__ import annotations

import re

from .vcommon import fail, fr, taste

ENGINES = ("full", "low", "panel", "inset", "slide-aside", "bubble", "hidden", "card", "stack", "pip", "letterbox", "blurfill")
LAYOUT_META = ("schedule",)
BUT = {"but", "however", "yet", "though", "although", "instead", "except", "lekin", "par", "magar"}
CLAIM = BUT | {"then", "so", "because", "actually", "never", "always", "only", "every", "everyone", "nobody", "nothing", "zero",
               "most", "best", "worst", "first", "last", "biggest", "secret", "truth", "problem", "reason", "mistake", "why",
               "how", "now", "don't", "dont", "can't", "cant", "isn't", "won't", "stop", "imagine", "wait",
               "today", "finally", "suddenly", "matlab", "isliye", "kyunki", "toh", "phir"}
NUM_WORDS = set("zero one two three four five six seven eight nine ten eleven twelve twenty thirty forty fifty hundred thousand "
                "million billion lakh lakhs crore crores half double triple".split())
# Hinglish (romanised) and Hindi (Devanagari) switch words: contrast, claim / connective, numbers. Ambiguous with English
# words ("do" = two, "par" = but) only count when the reel's speech is Hinglish or Hindi (HI_ONLY).
BUT_HI = {"lekin", "par", "magar", "parantu", "kintu", "balki", "warna", "varna", "fir bhi", "phirbhi",
          "लेकिन", "पर", "मगर", "परंतु", "परन्तु", "किंतु", "बल्कि", "वरना"}
CLAIM_HI = {"aur", "toh", "to", "matlab", "isliye", "kyunki", "kyonki", "phir", "fir", "ab", "abhi", "sirf", "bas", "kabhi",
            "hamesha", "sabse", "pehla", "pehle", "aakhri", "asli", "sach", "dekho", "suno", "socho", "samjho", "yaani",
            "यानी", "और", "तो", "मतलब", "इसलिए", "क्योंकि", "फिर", "अब", "सिर्फ", "बस", "कभी", "हमेशा", "सबसे", "पहला",
            "पहले", "असली", "सच", "देखो", "सुनो", "सोचो"}
NUM_HI = {"ek", "do", "teen", "char", "chaar", "paanch", "panch", "chhe", "chah", "che", "saat", "aath", "nau", "das",
          "gyarah", "barah", "bees", "tees", "chalis", "pachas", "pachaas", "sau", "hazaar", "hazar", "hajaar", "aadha", "dugna",
          "एक", "दो", "तीन", "चार", "पांच", "पाँच", "छह", "छः", "सात", "आठ", "नौ", "दस", "बीस", "पचास", "सौ", "हज़ार", "हजार",
          "लाख", "करोड़", "आधा", "दुगना"}
HI_ONLY = {"par", "do", "to", "che", "das", "ab", "char", "bas", "sach"}  # English words too: only for Hinglish / Hindi speech
DEVA_DIGIT = re.compile(r"[०-९]")


def library(style: dict) -> dict:
    return {k: v for k, v in (style.get("layouts") or {}).items() if k not in LAYOUT_META and isinstance(v, dict)}


def engine_of(style: dict, layout: str) -> str | None:
    """Engine layout behind a stage layout id (None when it does not resolve)."""
    lib = library(style)
    if layout in lib:
        eng = lib[layout].get("engine")
        return eng if eng in ENGINES else None
    return layout if layout in ENGINES else None


def runs(c) -> list[tuple[str, float, float]]:
    """[(layout id, t0, t1)] over the reel; consecutive entries with the same id merge into one run."""
    st = [e for e in c.stage if isinstance(e, dict)]
    if not st or fr(st[0].get("t", 0)) > 0:
        st = [{"t": 0, "layout": "full"}] + st
    out: list[list] = []
    for e in st:
        lid, t = str(e.get("layout", "full")), float(e.get("t", 0))
        if out and out[-1][0] == lid:
            continue
        if out:
            out[-1][2] = t
        out.append([lid, t, c.duration])
    return [(a, b, d) for a, b, d in out if d > b - 1e-9]


def _word_list(c) -> list[dict] | None:
    w = c.words
    if isinstance(w, dict):
        w = w.get("words")
    return [x for x in w if isinstance(x, dict) and x.get("s") is not None] if isinstance(w, list) else None


def _clean(w: str) -> str:
    """Lower-case word without punctuation; Devanagari vowel signs and nasal marks are kept (they are not word characters)."""
    return re.sub(r"[^\w'ऀ-ॿ]+", "", str(w or "").lower()).replace("।", "").replace("॥", "")


def speech_lang(c) -> str:
    """The reel's spoken language from the style profile ('en', 'hinglish', 'hi', ...)."""
    st = getattr(c, "style", None) or {}
    return str(((st.get("profile") or {}).get("language") or {}).get("speech") or "en").lower()


def word_classes(words: list[dict], i: int, lang: str = "en") -> set[str]:
    """Classes of word i for the switch-on rule. Hinglish / Hindi words (romanised or Devanagari) always count; words
    that are also common English words (HI_ONLY: "do", "par", "to"...) only when the speech is Hinglish or Hindi."""
    w = words[i]
    raw = str(w.get("w", w.get("caption", "")) or "")
    tok = _clean(raw)
    cls = {"any", tok}
    hi = str(lang or "en").lower() in ("hinglish", "hi", "hin", "hindi")
    hi_ok = hi or tok not in HI_ONLY
    if tok in BUT or (hi_ok and tok in BUT_HI):
        cls |= {"but", "claim"} if tok in BUT_HI else {"but"}
    if tok in CLAIM or (hi_ok and tok in CLAIM_HI):
        cls.add("claim")
    if (re.search(r"\d", raw) or DEVA_DIGIT.search(raw) or tok in NUM_WORDS or (hi_ok and tok in NUM_HI)
            or re.search(r"[₹$€£%]", raw)):
        cls |= {"number", "claim"}
    prev = words[i - 1] if i > 0 else None
    if prev is None or re.search(r"[.?!…।]\s*$", str(prev.get("w", ""))):
        cls.add("sentence")
    if prev is None or float(w["s"]) - float(prev.get("e", prev["s"])) >= 0.25:
        cls.add("pause")
    return cls


FOOTAGE_KINDS = ("broll", "screen-recording", "footage", "pov", "device")


def footage_supplied(c) -> bool | None:
    """Did the creator supply footage besides the talking-head take? True when work/sources.json has a non-talking-head
    source (B-roll, screen recording, a POV take) or plan/assets.json a creator video; None when the project is unknown."""
    proj = getattr(c, "project", None)
    if proj is None:
        return None
    from .core import read_json
    try:
        sp = proj.work / "sources.json"
        if sp.exists():
            for s in (read_json(sp).get("sources") or []):
                if isinstance(s, dict) and str(s.get("kind", "")).lower() in FOOTAGE_KINDS:
                    return True
        ap = proj.root / "plan" / "assets.json"
        if ap.exists():
            for a in (read_json(ap).get("assets") or {}).values():
                if isinstance(a, dict) and a.get("kind") == "video" and a.get("origin", "creator") == "creator":
                    return True
    except (ValueError, OSError, AttributeError):
        return None
    return False


def missing_footage(c, layouts: list[str]) -> list[tuple[str, str]]:
    """[(layout id, what it needs)] for the format's layouts that show creator footage (`layouts.<id>.needs_footage`)
    when the creator supplied none: a talking-head-only buyer cannot reach their share targets."""
    lib = library(c.style)
    need = [(lid, str(lib[lid]["needs_footage"])) for lid in layouts if lid in lib and lib[lid].get("needs_footage")]
    return need if need and footage_supplied(c) is False else []


def rule_layout(c, p: dict) -> list:
    out = []
    style = c.style
    lib = library(style)
    sched = (style.get("layouts") or {}).get("schedule") or {}
    res = style.get("_resolved") or {}
    fmt, fmt_layouts = res.get("format"), list(res.get("layouts") or [])
    # 1. resolution and format membership
    for e in c.stage:
        lid = str(e.get("layout", "full"))
        t = float(e.get("t", 0))
        ov = e.get("overshoot")  # fx-helpers: the morph's back-out peak past its target (0.10 = 10 %)
        if ov is not None and (isinstance(ov, bool) or not isinstance(ov, (int, float)) or not 0 <= ov <= 0.3):
            out.append(fail("V-LAYOUT", c.beat_id(t), t, f"stage overshoot {ov!r} at {t:.2f} s is not a number 0-0.3",
                            "set overshoot to the peak past the target, e.g. 0.1 for a pop-back that lands at 110 % and settles"))
        if engine_of(style, lid) is None:
            known = ", ".join(sorted(lib)) or "none"
            out.append(fail("V-LAYOUT", c.beat_id(t), t, f"stage layout '{lid}' is not an engine layout or a tokens.layouts id",
                            f"use one of the style's layouts ({known}) or an engine layout ({', '.join(ENGINES)})"))
        elif p.get("check_format", True) and fmt_layouts and lid in lib and lid not in fmt_layouts:
            out.append(fail("V-LAYOUT", c.beat_id(t), t, f"layout '{lid}' is not part of format {fmt} ({', '.join(fmt_layouts)})",
                            f"use a layout of format {fmt}, or switch the reel's format"))
    rs = runs(c)
    dur = max(c.duration, 1e-6)
    # 2. shares of runtime
    tot: dict[str, float] = {}
    for lid, a, b in rs:
        tot[lid] = tot.get(lid, 0.0) + (b - a)
    tol = float(p.get("share_tolerance", 0.02))
    check = [lid for lid in (fmt_layouts or list(lib)) if lid in lib and isinstance(lib[lid].get("share"), (list, tuple))]
    # no B-roll / device footage from the creator: the share targets assume it, so they become warnings naming it
    missing = missing_footage(c, fmt_layouts or list(lib))
    for lid in check:
        lo, hi = (float(x) for x in lib[lid]["share"][:2])
        if hi > 1.0 + 1e-9:
            lo, hi = lo / 100.0, hi / 100.0
        sh = tot.get(lid, 0.0) / dur
        if sh < lo - tol or sh > hi + tol:
            more = sh < lo
            msg = f"layout '{lid}' holds {sh:.0%} of the runtime (target {lo:.0%}-{hi:.0%}{' for ' + fmt if fmt else ''})"
            if missing:  # (taste: the share is the Director's call; kept as a measure, never said)
                msg += ("; the share targets need creator footage that this project does not have: "
                        + "; ".join(f"{w} for {lid2}" for lid2, w in missing))
            out.append(taste(fail("V-LAYOUT", None, 0.0, msg,
                                  f"{'use' if more else 'cut back'} '{lid}' to about {(lo if more else hi) * dur:.1f} s "
                                  f"({'+' if more else '-'}{abs((lo if more else hi) - sh) * dur:.1f} s)")))
    # 3. schedule min / max per run
    mx, mn = sched.get("max_s") or {}, sched.get("min_s") or {}
    for k, (lid, a, b) in enumerate(rs):
        d = b - a
        if lid in mx and d > float(mx[lid]) + 1e-6:
            out.append(taste(fail("V-LAYOUT", c.beat_id(a), a, f"layout '{lid}' holds {d:.1f} s from {a:.1f} s (max {mx[lid]} s)",
                                  f"switch layout before {a + float(mx[lid]):.1f} s (on a claim word)")))
        if lid in mn and k < len(rs) - 1 and d < float(mn[lid]) - 1e-6:
            out.append(taste(fail("V-LAYOUT", c.beat_id(a), a, f"layout '{lid}' holds only {d:.2f} s from {a:.1f} s (min {mn[lid]} s)",
                                  f"hold '{lid}' at least {mn[lid]} s, or drop this switch")))
    # 4. switch-on words
    want = [str(x).lower() for x in (sched.get("switch_on") or [])]
    if want and len(rs) > 1:
        words = _word_list(c)
        if words is None:
            c.warnings.append("V-LAYOUT: layouts.schedule.switch_on not checked (no words.edit.json)")
        else:
            ttol = float(p.get("tol_s", 0.25))
            for lid, a, _ in rs[1:]:
                near = [i for i, w in enumerate(words) if abs(float(w["s"]) - a) <= ttol]
                if not near:
                    out.append(taste(fail("V-LAYOUT", c.beat_id(a), a, f"the switch to '{lid}' at {a:.2f} s is not on a word",
                                          f"move the switch onto the start of a {'/'.join(want)} word")))
                    continue
                if not any(set(want) & word_classes(words, i, speech_lang(c)) for i in near):
                    heard = ", ".join(repr(str(words[i].get("w", ""))) for i in near)
                    out.append(taste(fail("V-LAYOUT", c.beat_id(a), a,
                                          f"the switch to '{lid}' at {a:.2f} s lands on {heard}, not a {'/'.join(want)} word",
                                          f"move it to the nearest {'/'.join(want)} word (e.g. but / lekin, then / phir, so / toh, a number)")))
    c.stats_extra["layouts"] = {"runs": [[lid, round(a, 2), round(b, 2)] for lid, a, b in rs],
                                "share": {k: round(v / dur, 3) for k, v in sorted(tot.items())}, "format": fmt}
    return out
