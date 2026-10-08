"""V-DEPICT and V-POINT: show the thing, not the word (Naman, 8 Oct 2026). Advice only, never a block.

V-DEPICT  a beat whose scenes are all words (text cards, type, lockups) and no picture of what is said: no object,
          screen or app, diagram, footage or numbers in motion. Talking-head beats (no scenes) are fine.
V-POINT   a moment where the speaker points with words ("this, this and this", "from this to this", "ye dekho";
          veos.pointers) with no picture on screen while it is said. The moments come from plan/inserts.scan.json
          `pointers` (`veos inserts scan`), else straight from the edit-time words. A moment the creator said needs
          nothing (plan/inserts.json `pointers: [{id, show: "none"}]`) is skipped.

A scene counts as a picture when the planner says so (`depicts`: what it shows, e.g. "a phone with a voice-note
waveform"; the scene coder copies it into the scene, and V-PLAN fidelity holds it to the plan), or when it plainly is
one: it carries no text, shows a figure (figure / figures / lands, a data kind), the creator's media or a created
insert (insert, asset), follows a tracked object (anchor), or is a diagram, clip, shape or meme. Ignored on both sides:
the banner slab, the CTA keyword, captions, ambient texture, flashes / streaks / shatters, legal and decorative text.
Both rules run in plan mode (`veos validate --plan`, on plan/scenes.plan.json) and after the code; a style whose
graphics are switched off (passthrough / none) skips them.
"""
from __future__ import annotations

from .core import read_json
from .datarules import DATA_KINDS
from .pointers import find_pointers
from .vcommon import advice, fail

IGNORED_KINDS = {"banner", "cta-keyword", "transition", "end-card", "subtitle", "caption"}
IGNORED_FX = {"ambient", "flash", "streak", "shatter"}
IGNORED_CLASSES = {"TC-subtitle", "TC-legal", "TC-decorative"}
PICTURE_FX = {"diagram", "clip", "morphShape"}
PICTURE_KINDS = {"meme", "diagram", "device", "screen", "ui", "icon", "image", "photo", "clip", "broll", "b-roll"}
PICTURE_KEYS = ("depicts", "figure", "figures", "lands", "insert", "asset", "assets", "anchor")
POINT_LEAD_S = 0.5   # s: a picture may appear this long before the pointing words
POINT_TAIL_S = 1.0   # s: ... or up to this long after them


def classify(s: dict) -> str:
    """'picture' | 'text' | 'ignored' for one scene (see the module doc)."""
    sid = str(s.get("id", ""))
    fx = str(s.get("fx") or "")
    if sid.startswith("__") or s.get("kind") in IGNORED_KINDS or fx in IGNORED_FX or s.get("ambient"):
        return "ignored"
    if any(s.get(k) for k in PICTURE_KEYS) or fx.startswith("insert:") or fx in PICTURE_FX:
        return "picture"
    if s.get("kind") in DATA_KINDS or s.get("kind") in PICTURE_KINDS:
        return "picture"
    if not s.get("text"):
        return "picture"
    if s.get("text_class") in IGNORED_CLASSES:
        return "ignored"
    return "text"


def _graphics_off(c) -> bool:
    prof = ((c.style or {}).get("profile") or {}).get("graphics")
    return str(prof or "") in ("passthrough", "pass", "none")


def _beat_scenes(c, b: dict) -> list[dict]:
    ids = {str(x) for x in (b.get("layers") or [])}
    if ids:
        return [s for s in c.scenes if str(s.get("id")) in ids]
    t0, t1 = float(b.get("t0", 0)), float(b.get("t1", 0))
    return [s for s in c.scenes if float(s.get("t_in", 0)) < t1 - 1e-6 and float(s.get("t_out", 0)) > t0 + 1e-6]


def rule_depict(c) -> list[dict]:
    """V-DEPICT: beats that show only words."""
    if _graphics_off(c):
        return []
    out = []
    n_text_only = 0
    for b in c.beats:
        got = [(s, classify(s)) for s in _beat_scenes(c, b)]
        texts = [s for s, k in got if k == "text"]
        if not texts or any(k == "picture" for _, k in got):
            continue
        n_text_only += 1
        t = float(b.get("t0", 0))
        ids = ", ".join(str(s.get("id")) for s in texts[:4])
        out.append(advice(fail(
            "V-DEPICT", b.get("id"), t,
            f"beat {b.get('id')} shows only words ({ids}): nothing pictures what is said",
            "show the thing, not the word: an object, a screen or app, a diagram, numbers in motion, in this style's own "
            "look; keep the words as support. Set `depicts` on the scene that pictures it (plan and code)")))
    c.stats_extra.setdefault("depict", {})["text_only_beats"] = n_text_only
    return out


def _pointers(c) -> tuple[list[dict], dict]:
    """(pointing moments, {pointer id: the creator's / planner's answer})."""
    proj = getattr(c, "project", None)
    ptrs, answers = None, {}
    if proj is not None:
        sp = proj.root / "plan" / "inserts.scan.json"
        if sp.exists():
            try:
                got = (read_json(sp) or {}).get("pointers")
                ptrs = got if isinstance(got, list) else None
            except ValueError:
                ptrs = None
        ip = proj.root / "plan" / "inserts.json"
        if ip.exists():
            try:
                for a in (read_json(ip) or {}).get("pointers") or []:
                    if isinstance(a, dict) and a.get("id"):
                        answers[str(a["id"])] = a
            except ValueError:
                pass
    if ptrs is None:
        w = c.words.get("words") if isinstance(c.words, dict) else c.words
        ptrs = find_pointers(w or [])
    return [p for p in ptrs if isinstance(p, dict) and isinstance(p.get("t0"), (int, float))], answers


def rule_point(c) -> list[dict]:
    """V-POINT: pointing moments with no picture on screen."""
    if _graphics_off(c):
        return []
    ptrs, answers = _pointers(c)
    out = []
    shown = 0
    for p in ptrs:
        ans = answers.get(str(p.get("id")), {})
        if str(ans.get("show") or "").strip().lower() == "none":
            continue
        t0 = float(p["t0"])
        t1 = float(p.get("t1", t0))
        pics = [s for s in c.scenes if classify(s) == "picture"
                and float(s.get("t_in", 0)) < t1 + POINT_TAIL_S and float(s.get("t_out", 0)) > t0 - POINT_LEAD_S]
        if pics:
            shown += 1
            continue
        want = f" (the plan says: {ans['show']})" if ans.get("show") else ""
        out.append(advice(fail(
            "V-POINT", c.beat_id(t0), t0,
            f"at {t0:.2f} s the speaker points with words (\"{p.get('phrase', '')}\" in \"…{p.get('context', '')}…\") "
            f"but no picture is on screen{want}",
            "show what they point at: the creator's answer from the one question round, else the most likely thing "
            "(made-up but realistic numbers and names are fine); set `depicts` on that scene")))
    c.stats_extra.setdefault("depict", {}).update({"pointers": len(ptrs), "pointers_shown": shown})
    return out
