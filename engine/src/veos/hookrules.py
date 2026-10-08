"""V-F0: frame-0 requirements by hook archetype (structure Part F.1) + payoff-by (ST-6). Replaces M1.

The reel's archetype is `timeline.meta.hook_archetype`, else the style's `hooks.default` (v1 files: HA-01).
Each archetype lists requirements: named predicates over the scenes, stage, captions and camera, checked at frame 0 or
"by N s". A scene satisfies a requirement by its `kind` (vocabulary below) or explicitly with `satisfies: ["<name>"]`.
The payoff scene is the one tagged `payoff: true`, else the first scene matching the archetype's payoff requirement.

HA-01 in legacy mode (v1 `rules_v0: M1`) is exactly the old M1: banner + result visual + speaker + motion at f0, no
payoff check, the same messages.

Extension points: add a requirement to REQS (name -> (description, predicate(c, t), fix)), and an archetype row to
ARCHETYPES; `hooks.f0.require` / `forbid` in tokens may name any requirement.
"""
from __future__ import annotations

from .vcommon import HEADLINE_KINDS, SUBTITLE_Z, fail, fr, get_path

TOL_S = 0.1  # caption "at f0": the first chunk/word may start up to 3 frames in

K = {  # requirement -> scene kinds that satisfy it
    "proof": ("proof", "card", "counter", "phone", "screenshot", "device", "ui", "result"),
    "number": ("counter", "number", "figure", "data_row", "ledger", "hero_number", "stat"),
    "topic": ("topic", "tile", "title") + HEADLINE_KINDS,
    "lockup": ("lockup", "chip", "pill", "plate", "banner", "headline", "promise"),
    "title": ("title", "title_card") + HEADLINE_KINDS,
    "diagram": ("diagram", "framework", "flowchart"),
    "hero": ("hero", "hero_number", "hero_text"),
    "evidence": ("evidence", "source_card", "screenshot", "article", "document", "headline_card", "proof"),
    "stamp": ("stamp", "label", "evidence_label", "highlight"),
    "subject": ("subject", "footage", "broll", "clip", "archive", "video"),
    "archive": ("archive", "still", "photo", "footage", "broll", "clip"),
    "device": ("device", "phone", "product", "laptop", "screen"),
    "clip": ("clip", "footage", "broll", "video", "quote_card", "quote"),
    "post": ("post", "post_header", "tweet", "quote_card"),
    "pill": ("pill", "quote", "quote_pill"),
    "footage_scene": ("footage", "broll", "clip", "archive", "video", "subject"),
    "caption_scene": ("caption", "captions", "subtitle"),
}


# --------------------------------------------------------------------------- primitives
def _sid_ok(s: dict, name: str, kinds) -> bool:
    return s.get("kind") in kinds or name in (s.get("satisfies") or [])


def _active_at(c, s: dict, t: float) -> bool:
    return fr(s.get("t_in", 0)) <= fr(t) < fr(s.get("t_out", 0))


def _first(c, name: str, kinds, by: float, pred=None):
    """First scene matching (kind or satisfies) that is on screen at some frame <= by."""
    for s in sorted(c.scenes, key=lambda x: x.get("t_in", 0)):
        if not _sid_ok(s, name, kinds):
            continue
        if fr(s.get("t_in", 0)) <= fr(by) and fr(s.get("t_out", 0)) > 0 and (pred is None or pred(s)):
            return s
    return None


def _moving(c, s: dict) -> bool:
    """The scene animates around its entry: an entrance, internal events, or continuous motion."""
    return (s.get("in", "settle") not in (None, "none") or bool(s.get("events")) or bool(s.get("continuous"))
            or s.get("motion") in ("continuous", "ambient") or bool(s.get("ambient")))


def caption_at(c, t: float) -> bool:
    """Captions (or a caption-kind scene) are showing at time t."""
    if any(_sid_ok(s, "caption", K["caption_scene"]) and _active_at(c, s, t) for s in c.scenes):
        return True
    if get_path(c.style, "profile.captions.mode") == "off":
        return False
    caps = c.tl.get("captions") or {}
    for a, b in (caps.get("hide") or []):
        try:
            if float(a) - 1e-6 <= t < float(b) - 1e-6:
                return False
        except (TypeError, ValueError):
            continue
    if c.caption_chunks is not None:
        return any(ch["t0"] <= t + TOL_S and ch["t1"] > t for ch in c.caption_chunks)
    if caps.get("subtitles") not in ("auto", True):
        return False
    words = (c.words or {}).get("words") if isinstance(c.words, dict) else None
    if words:
        return any(float(w.get("s", 1e9)) <= t + TOL_S and float(w.get("e", -1)) + 0.5 > t and w.get("caption", "x") != ""
                   for w in words)
    return True  # auto subtitles on, no word timings loaded: assume they run (warned in stats)


def presenter_on(c, t: float) -> bool:
    return get_path(c.style, "profile.presenter.presence") != "none" and c.stage_engine_at(t) != "hidden"


def footage_moving(c, t: float) -> bool:
    """Live footage at t: the presenter's live take, or a footage/B-roll/clip scene, or a continuous-motion scene."""
    if presenter_on(c, t):
        return True
    return any(_active_at(c, s, t) and (s.get("kind") in K["footage_scene"] or "footage" in (s.get("satisfies") or [])
                                        or s.get("continuous") or s.get("motion") == "continuous") for s in c.scenes)


def motion_f0(c) -> bool:
    """M1's motion test: a scene entrance starting at frame 0 or a camera event at frame 0."""
    anim = any(fr(s.get("t_in", 0)) == 0 and s.get("in", "settle") not in (None, "none") for s in c.scenes)
    return anim or any(fr(e.get("t", 0)) == 0 for e in c.camera)


def live_motion_f0(c) -> bool:
    return (motion_f0(c) or footage_moving(c, 0)
            or any(_active_at(c, s, 0) and _moving(c, s) and fr(s.get("t_in", 0)) <= 3 for s in c.scenes)
            or any(_active_at(c, s, 0) and (s.get("continuous") or s.get("ambient")) for s in c.scenes))


def _cut_by(c, t: float) -> bool:
    cuts = [e.get("t", 0) for e in c.transitions] + [e.get("t", 0) for e in c.stage[1:]]
    for s in c.scenes:
        cuts += [float(s.get("t_in", 0)) + float(v) for v in (s.get("cuts") or []) if isinstance(v, (int, float))]
    cuts += [seg.get("t0", 0) for seg in ((c.cutmap or {}).get("segments") or [])[1:]]
    return any(0 < fr(x) <= fr(t) for x in cuts)


def _headline_kinds(c, legacy: bool):
    return ("banner",) if legacy else HEADLINE_KINDS


def _words(text: str) -> int:
    return len([w for w in str(text or "").split() if any(ch.isalnum() for ch in w)])


# requirement name -> (description, predicate(c, by_s, legacy) -> bool, fix(by_s) -> str)
def _scene_req(name, kinds, desc, fix, pred=None):
    return (desc, lambda c, by, lg: _first(c, name, kinds, by, (lambda s: pred(c, s)) if pred else None) is not None, fix)


REQS: dict[str, tuple] = {
    "headline": ("a headline element (banner, pill, lockup, chip, plate or title card)",
                 lambda c, by, lg: _first(c, "headline", _headline_kinds(c, lg), by) is not None,
                 lambda by: "add the style's headline scene (kind banner/pill/lockup/chip/plate/title_card) starting at t 0"),
    "result": ("a result visual besides the headline and captions",
               lambda c, by, lg: any(_active_at(c, s, 0) and s.get("kind") not in _headline_kinds(c, lg)
                                     and s.get("z") not in SUBTITLE_Z and s.get("z", 0) < 10 for s in c.scenes),
               lambda by: "add a card, mock or result-visual scene starting at t 0"),
    "presenter": ("the presenter on screen",
                  lambda c, by, lg: any(presenter_on(c, x / 30) for x in range(0, fr(by) + 1)),
                  lambda by: "set the stage layout at t 0 to full, panel, inset, slide-aside or bubble"
                  if by <= 0 else f"bring the presenter on screen by {by:.1f} s"),
    "motion": ("an element moving on frame 0", lambda c, by, lg: motion_f0(c),
               lambda by: "give the headline an entrance (in: settle or pop) starting at t 0, or add a camera event at t 0"),
    "live_motion": ("something moving at frame 0 (live footage, an entrance, a camera move or continuous motion)",
                    lambda c, by, lg: live_motion_f0(c),
                    lambda by: "start the reel on live footage, an entrance animation or a camera move at t 0"),
    "footage": ("moving footage at frame 0", lambda c, by, lg: footage_moving(c, 0),
                lambda by: "open on the live take or a footage/B-roll scene (kind footage, broll, clip) at t 0"),
    "caption": ("captions running at frame 0", lambda c, by, lg: caption_at(c, 0),
                lambda by: "let the captions run from the first word (do not hide them at 0, start the cut on speech)"),
    "claim": ("a claim caption or headline at frame 0",
              lambda c, by, lg: caption_at(c, 0) or _first(c, "claim", _headline_kinds(c, lg), by) is not None
              or _first(c, "headline", _headline_kinds(c, lg), by) is not None,
              lambda by: "show the claim as a caption or headline at t 0"),
    "text_beat": ("a first type beat (caption or text scene)",
                  lambda c, by, lg: caption_at(c, by) or any(caption_at(c, x / 30) for x in range(0, fr(by) + 1))
                  or any(s.get("text") and fr(s.get("t_in", 0)) <= fr(by) for s in c.scenes),
                  lambda by: f"bring the first type beat (a caption or text scene) in by {by:.1f} s"),
    "proof": _scene_req("proof", K["proof"], "a proof element (card, counter, phone, screenshot)",
                        lambda by: "add the proof scene (kind proof/card/counter/phone/screenshot) at t 0"),
    "number": _scene_req("number", K["number"], "a number or data row moving",
                         lambda by: "start a counter/number/data_row scene with an entrance or events at t 0",
                         pred=lambda c, s: _moving(c, s)),
    "data_row_moving": _scene_req("data_row_moving", K["number"], "a number or data row moving",
                                  lambda by: "start a counter/number/data_row scene with an entrance or events at t 0",
                                  pred=lambda c, s: _moving(c, s)),
    "topic": _scene_req("topic", K["topic"], "the topic tile or title", lambda by: f"build the topic tile/title by {by:.1f} s"),
    "lockup": _scene_req("lockup", K["lockup"], "the claim lockup or promise chip",
                         lambda by: f"make the lockup/chip readable by {by:.1f} s"),
    "title": _scene_req("title", K["title"], "a title", lambda by: "add the title scene at t 0"),
    "diagram": _scene_req("diagram", K["diagram"], "the diagram skeleton starting",
                          lambda by: "start the diagram (kind diagram) at t 0"),
    "hero": ("the hero text or number (behind the head)",
             lambda c, by, lg: _first(c, "hero", K["hero"], by) is not None
             or any(s.get("behind") and s.get("text") and fr(s.get("t_in", 0)) <= fr(by) for s in c.scenes),
             lambda by: f"bring the hero text/number in by {by:.1f} s"),
    "evidence": _scene_req("evidence", K["evidence"], "the evidence panel",
                           lambda by: f"slide the evidence panel (kind evidence/source_card/screenshot) in by {by:.1f} s"),
    "stamp": _scene_req("stamp", K["stamp"], "the evidence label or stamp", lambda by: f"land the label/stamp by {by:.1f} s"),
    "subject": _scene_req("subject", K["subject"], "the subject full-frame",
                          lambda by: f"cut to the subject (kind subject/footage/broll) by {by:.1f} s"),
    "archive": _scene_req("archive", K["archive"], "an archive image", lambda by: "open on an archive image or clip at t 0"),
    "boxed_caption": ("a boxed caption", lambda c, by, lg: caption_at(c, 0) or _first(c, "boxed_caption", ("plate", "caption", "pill"), by) is not None,
                      lambda by: "show the boxed caption at t 0"),
    "moving_object": ("a striking moving object",
                      lambda c, by, lg: any(_active_at(c, s, 0) and not s.get("text") and _moving(c, s) for s in c.scenes)
                      or any("moving_object" in (s.get("satisfies") or []) and _active_at(c, s, 0) for s in c.scenes),
                      lambda by: "open on a non-text object in motion (entrance, events or continuous: true)"),
    "moving_subject": ("a moving subject",
                       lambda c, by, lg: footage_moving(c, 0) or any(_active_at(c, s, 0) and not s.get("text") and _moving(c, s) for s in c.scenes),
                       lambda by: "open on live footage or a moving subject"),
    "question": ("the question or title", lambda c, by, lg: caption_at(c, 0) or _first(c, "question", _headline_kinds(c, lg), by) is not None,
                 lambda by: "show the question/title at t 0"),
    "device": _scene_req("device", K["device"], "the device on screen", lambda by: "show the device (kind device/phone/product) at t 0"),
    "clip": _scene_req("clip", K["clip"], "the clip (creator-supplied) or a created quote card",
                       lambda by: f"show the clip or quote card by {by:.1f} s"),
    "post": _scene_req("post", K["post"], "the post header", lambda by: "add the post header (kind post/tweet) at t 0"),
    "pill": _scene_req("pill", K["pill"], "the quote pill", lambda by: f"show the quote pill by {by:.1f} s"),
    "two_faces": ("two faces (stack layout)", lambda c, by, lg: c.stage_engine_at(0) == "stack" or any(
        "two_faces" in (s.get("satisfies") or []) and _active_at(c, s, 0) for s in c.scenes),
        lambda by: "open on the stack layout with both speakers"),
    "one_word": ("one word or a chip", lambda c, by, lg: any(
        _active_at(c, s, 0) and s.get("text") and (_words(s.get("text_content")) <= 2 or s.get("kind") == "chip") for s in c.scenes),
        lambda by: "show one word (or a chip) over the opening clip"),
    "cut": ("the first cut", lambda c, by, lg: _cut_by(c, by), lambda by: f"make the first cut by {by:.1f} s"),
    "whip": ("the whip into the device", lambda c, by, lg: any(0 < fr(e.get("t", 0)) <= fr(by) for e in c.camera + c.transitions),
             lambda by: f"whip into the device (camera move or transition) by {by:.1f} s"),
}

# archetype -> {f0: [req or (req, by_s)], payoff: (req | None, seconds), before_speech?}  (structure Part F.1)
# `before_speech`: the archetype's opener is up on frame 0, before the first word (HA-03's quote pill / stack opener,
# HA-14's cold in-point 1-3 f before speech), so V-ONWORD counts frame 0 as the event of the first beat's trigger word
# when that word is spoken by the archetype's payoff time.
ARCHETYPES: dict[str, dict] = {
    "HA-01": {"name": "Result pair", "f0": ["headline", "result", "presenter", "motion"], "payoff": ("result", 2.0)},
    "HA-02": {"name": "Headline + proof", "f0": ["headline", "proof"], "payoff": ("proof", 2.5)},
    "HA-03": {"name": "Quote pill over conversation", "f0": ["pill", "two_faces"], "payoff": ("pill", 1.0),
              "before_speech": True},
    "HA-04": {"name": "Topic build", "f0": ["presenter", ("topic", 1.0)], "payoff": ("topic", 1.8)},
    "HA-05": {"name": "Claim lockup / promise chip", "f0": ["presenter", ("lockup", 0.7)], "payoff": ("lockup", 0.7)},
    "HA-06": {"name": "Framework build", "f0": ["title", "diagram"], "payoff": ("diagram", 2.5)},
    "HA-07": {"name": "Live number / ledger open", "f0": ["number", "claim"], "payoff": ("number", 1.0)},
    "HA-08": {"name": "Prop + hero", "f0": ["presenter", ("hero", 1.7)], "payoff": ("hero", 1.7)},
    "HA-09": {"name": "Evidence slide", "f0": ["presenter", ("evidence", 1.5)], "payoff": ("stamp", 2.0)},
    "HA-10": {"name": "Host flash -> subject", "f0": ["presenter", "caption"], "payoff": ("subject", 0.7)},
    "HA-11": {"name": "Thesis montage", "f0": ["archive", "boxed_caption"], "payoff": (None, 3.0)},
    "HA-12": {"name": "Thesis typography", "f0": ["live_motion", ("text_beat", 0.7)], "payoff": (None, 3.0)},
    "HA-13": {"name": "Cold action", "f0": ["footage", "caption", ("cut", 2.1)], "payoff": (None, 2.3)},
    "HA-14": {"name": "Cold authority", "f0": ["caption", "footage"], "payoff": (None, 1.0), "before_speech": True},
    "HA-15": {"name": "Atmosphere", "f0": ["moving_object"], "payoff": ("text_beat", 5.0)},
    "HA-16": {"name": "Diegetic", "f0": ["moving_subject"], "payoff": (None, 5.0)},
    "HA-17": {"name": "Device whip", "f0": ["question", "device"], "payoff": ("whip", 2.5)},
    "HA-18": {"name": "Borrowed clip", "f0": ["clip", "post", ("presenter", 8.0)], "payoff": ("clip", 3.0)},
    "HA-19": {"name": "Mood montage", "f0": ["footage", "one_word"], "payoff": (None, 3.0)},
}

# old M1 messages, kept verbatim for the legacy alias
M1_MSG = {
    "headline": "no banner scene (kind: 'banner') is on screen at frame 0",
    "result": "frame 0 has no result visual besides the banner and captions",
    "presenter": "the speaker is hidden at frame 0",
    "motion": "nothing is moving on frame 0",
}
M1_FIX = {
    "headline": "add a scene with kind 'banner', t_in 0, so the headline is readable on the first frame",
    "result": "add a card, mock or result-visual scene starting at t 0",
    "presenter": "set the stage layout at t 0 to full, panel, inset, slide-aside or bubble",
    "motion": "give the banner an entrance (in: settle or pop) starting at t 0, or add a camera event at t 0",
}


def expected(ha: str, hooks: dict | None = None) -> str:
    """The engine's definition of an archetype, for messages: its registry name, the f0 requirements and the payoff;
    plus the name the style gives the id when it differs (`hooks.names` / `hooks.variants`)."""
    a = ARCHETYPES[ha]
    reqs = []
    for item in a["f0"]:
        name, by = _req(item)
        reqs.append(REQS[name][0] + ("" if by <= 0 else f" by {by:g} s"))
    pay, secs = a["payoff"]
    txt = f"the engine's {ha} is '{a['name']}': frame 0 needs {'; '.join(reqs)}"
    txt += f"; payoff ({REQS[pay][0]}) by {secs:g} s" if pay else f"; payoff by {secs:g} s"
    named = {}
    for key in ("names", "variants"):
        v = (hooks or {}).get(key)
        if isinstance(v, dict):
            named.update({str(k): str(x) for k, x in v.items() if isinstance(x, str)})
    own = named.get(ha)
    if own and own.strip().lower() != a["name"].lower():
        txt += f" (this style calls {ha} '{own}'; if that hook is a different device, give it the matching engine id)"
    return txt


def archetype_of(c, p: dict) -> str:
    return str(p.get("archetype") or (c.meta or {}).get("hook_archetype") or get_path(c.style, "hooks.default") or "HA-01")


# A still hook slab is a valid stopper: a readable hook text element (headline slab, banner, title) fully on screen at
# frame 0 satisfies these motion requirements by default, even when nothing moves. Every other f0 requirement still
# applies. `hooks.f0_still: true` (older styles) is still accepted and also counts any still scene at f0.
STILL_OK = ("motion", "live_motion")
SLAB_KINDS = HEADLINE_KINDS + ("title", "hero_text")
FRAME_W, FRAME_H, EDGE_SLACK = 1080, 1920, 4


def still_slab_f0(c) -> dict | None:
    """The readable hook text slab fully on screen at frame 0 (kind headline / banner / title..., or satisfies
    headline / title; with text; its frame-0 rect, else its box, inside the frame), or None."""
    for s in c.scenes:
        if not (_active_at(c, s, 0) and s.get("text") and s.get("z", 0) not in SUBTITLE_Z and s.get("z", 0) < 11):
            continue
        if not (s.get("kind") in SLAB_KINDS or {"headline", "title"} & set(s.get("satisfies") or [])):
            continue
        r = c.rect(s, 0) if hasattr(c, "rect") else None
        if r is None:
            continue
        if r[0] >= -EDGE_SLACK and r[1] >= -EDGE_SLACK and r[2] <= FRAME_W + EDGE_SLACK and r[3] <= FRAME_H + EDGE_SLACK:
            return s
    return None


def _still_at_f0(c) -> bool:
    """A scene (not the subtitles, not a z11 light pass) is on screen at frame 0: the declared still slab."""
    return any(_active_at(c, s, 0) and s.get("z", 0) not in SUBTITLE_Z and s.get("z", 0) < 11 for s in c.scenes)


def _req(item):
    return (item, 0.0) if isinstance(item, str) else (item[0], float(item[1]))


def rule_f0(c, p: dict) -> list[dict]:
    legacy = bool(p.get("legacy"))
    ha = archetype_of(c, p)
    hooks = c.style.get("hooks") or {}
    bid = c.beat_id(0)
    c.stats_extra["hook"] = {"archetype": ha}
    if ha not in ARCHETYPES:
        return [fail("V-F0", bid, 0, f"unknown hook archetype '{ha}'",
                     f"set meta.hook_archetype to one of the style's archetypes ({', '.join(hooks.get('allowed') or [hooks.get('default', 'HA-01')])})")]
    out = []
    allowed = list(hooks.get("allowed") or []) + ([hooks["default"]] if hooks.get("default") else [])
    if not legacy and allowed and ha not in allowed:
        out.append(fail("V-F0", bid, 0, f"hook archetype {ha} ({ARCHETYPES[ha]['name']}) is not one this style uses "
                        f"({', '.join(dict.fromkeys(allowed))})", f"pick an archetype from hooks.allowed: {', '.join(dict.fromkeys(allowed))}"))
    reqs = [_req(x) for x in ARCHETYPES[ha]["f0"]]
    f0 = hooks.get("f0") or {}
    if not legacy and ha == hooks.get("default"):
        for name in f0.get("require") or []:
            if name not in REQS:
                c.warnings.append(f"hooks.f0.require names unknown requirement '{name}' (known: {', '.join(REQS)})")
            elif name not in [r for r, _ in reqs]:
                reqs.append((name, 0.0))
    f0_still = None if legacy else hooks.get("f0_still")
    if f0_still is not None and not isinstance(f0_still, bool):
        out.append(fail("V-F0", bid, 0, f"hooks.f0_still must be true or false (got {f0_still!r})",
                        "set hooks.f0_still: true only when the creator's real frame 0 is a still slab"))
        f0_still = None
    for name, by in reqs:
        desc, pred, fix = REQS[name]
        if pred(c, by, legacy):
            continue
        if name in STILL_OK and not legacy and (still_slab_f0(c) or (f0_still and _still_at_f0(c))):
            c.stats_extra["hook"]["f0_still"] = True  # a still hook slab at f0 is a valid stopper
            continue
        if legacy:
            out.append(fail("V-F0", bid, 0, M1_MSG[name], M1_FIX[name]))
        else:
            when = "at frame 0" if by <= 0 else f"by {by:.1f} s"
            out.append(fail("V-F0", bid, by, f"{ha} {ARCHETYPES[ha]['name']}: {desc} is missing {when} "
                            f"({expected(ha, hooks)})", fix(by)))
    if legacy:
        return out
    for name in f0.get("forbid") or []:
        if name in REQS and REQS[name][1](c, 0.0, legacy):
            out.append(fail("V-F0", bid, 0, f"frame 0 shows {REQS[name][0]}, which this style forbids at f0",
                            f"remove it from frame 0 (hooks.f0.forbid: {name})"))
    out.extend(_payoff(c, ha, hooks))
    return out


def _payoff(c, ha: str, hooks: dict) -> list[dict]:
    req, secs = ARCHETYPES[ha]["payoff"]
    stop = (hooks.get("stopper") or {}).get("payoff_by_s")
    by = float(stop) if stop is not None and ha == hooks.get("default") else float(secs)
    c.stats_extra["hook"]["payoff_by_s"] = by
    tagged = sorted((s for s in c.scenes if s.get("payoff")), key=lambda s: s.get("t_in", 0))
    if tagged:
        t = float(tagged[0].get("t_in", 0))
        c.stats_extra["hook"]["payoff_t"] = round(t, 3)
        if fr(t) > fr(by):
            return [fail("V-F0", c.beat_id(t), t, f"the payoff scene {tagged[0].get('id')} lands at {t:.2f} s ({ha} payoff by {by:.1f} s)",
                         f"bring {tagged[0].get('id')} forward so it starts by {by:.1f} s, or tighten the hook")]
        return []
    if req is None:
        c.warnings.append(f"V-F0: {ha} payoff-by {by:.1f} s not checked; tag the payoff scene with payoff: true")
        return []
    desc, pred, fix = REQS[req]
    if pred(c, by, False):
        return []
    return [fail("V-F0", c.beat_id(by), by, f"{ha} payoff: {desc} has not landed by {by:.1f} s ({expected(ha, hooks)})",
                 f"{fix(by)} (or tag the payoff scene with payoff: true)")]
