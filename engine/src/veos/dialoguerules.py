"""V-SPEAKER (structure §20): captions and cuts follow the diarised speaker on multi-speaker reels.

Registry hook (feat/v3-foundation): `from .dialoguerules import RULES as DIALOGUE_RULES; REGISTRY.update(DIALOGUE_RULES)`
and drop "V-SPEAKER" from PENDING. Signature `rule(ctx, params) -> [failure]` with failure
{rule, beat, t, msg, fix}. The rule only reads `ctx.tl` (timeline: `shots`, `captions`, `beats`), `ctx.words`
(edit-time words with `speaker`), `ctx.style` / `ctx.tokens` (playbook tokens: `dialogue`, `captions.speakers`) and
`ctx.beat_id(t)` when present, so it runs on today's Ctx, the foundation's Ctx and the stand-alone `DialogueCtx` below
(`veos shots check`). It is a no-op on reels without speaker labels and shots.

Checks (params override `dialogue.cut_rules` tokens, which override the defaults):
  SPK-1 labels      >= 95% of the words carry a speaker label (when 2+ speakers talk)
  SPK-2 colours     every speaker has a caption style and no two speakers share one (colour + italic)
  SPK-3 handover    a cut within +-`handover_tol_f` (3) frames of every new speaker's first word, when the shot on
                    either side is full-frame
  SPK-4 on screen   a full-frame shot shows the speaker (reaction cutaways excepted, which last <= reaction max +0.5 s
                    and never span a handover); in a stack the speaker is on top (the host with
                    `dialogue.stack.top: "host"`: the host never sits in the bottom half)
  SPK-5 no cut inside a word
  SPK-6 hold        no full shot longer than `max_hold_s` + 1 s, no stack longer than `stack_max_s` + 1 s
"""
from __future__ import annotations

from .turnrules import DEFAULTS, turns

FPS = 30


def _fail(rule_id, c, t, msg, fix):
    beat = None
    try:
        beat = c.beat_id(t)
    except Exception:  # noqa: BLE001
        pass
    return {"rule": "V-SPEAKER", "check": rule_id, "beat": beat, "t": round(float(t), 3), "msg": msg, "fix": fix}


def _get(d, path, default=None):
    cur = d
    for k in path.split("."):
        if not isinstance(cur, dict) or k not in cur:
            return default
        cur = cur[k]
    return cur


def speaker_styles(tl: dict, tokens: dict) -> dict:
    """{speaker id or role: {colour, style}} from timeline.captions.speakers, then tokens captions.speakers."""
    out = {}
    for src in (_get(tokens, "captions.speakers"), _get(tokens, "type.subtitle.speakers"), _get(tl, "captions.speakers")):
        if isinstance(src, dict):
            out.update({k: v for k, v in src.items() if isinstance(v, dict)})
    return out


def word_list(words) -> list[dict]:
    """The word dicts of `ctx.words`, which is the whole work/words.edit.json document ({"words": [...]}) inside
    `veos validate` and a plain list in `veos shots check`."""
    if isinstance(words, dict):
        words = words.get("words")
    return [w for w in words or [] if isinstance(w, dict) and w.get("w") and "s" in w and "e" in w]


def stack_top(tokens: dict) -> str:
    """`dialogue.stack.top`: "speaker" (default: whoever talks is on top) or "host" (the host stays on top, as in
    Hormozi's clips)."""
    st = _get(tokens, "dialogue.stack")
    top = st.get("top") if isinstance(st, dict) else None
    return "host" if str(top or "").lower() == "host" else "speaker"


def host_ids(words: list[dict]) -> set[str]:
    """Speaker ids whose role is host (the word labels written by `veos speakers`)."""
    return {str(w["speaker"]) for w in words if w.get("speaker") and str(w.get("role") or "").lower() == "host"}


def rule_speaker(c, p: dict | None = None) -> list[dict]:
    p = p or {}
    tl = getattr(c, "tl", {}) or {}
    tokens = getattr(c, "style", None) or getattr(c, "tokens", None) or {}
    words = word_list(getattr(c, "words", None))
    shots = sorted(tl.get("shots") or [], key=lambda s: s.get("t0", 0))
    spk_ids = sorted({w["speaker"] for w in words if w.get("speaker")})
    if len(spk_ids) < 2 and not shots:
        return []
    cr = {**DEFAULTS, **(_get(tokens, "dialogue.cut_rules") or {}), **p}
    tol = cr["handover_tol_f"] / FPS
    out = []
    # SPK-1 labels
    if words and len(spk_ids) >= 2:
        lab = sum(1 for w in words if w.get("speaker")) / len(words)
        if lab < 0.95:
            first = next(w for w in words if not w.get("speaker"))
            out.append(_fail("SPK-1", c, first["s"], f"only {lab:.0%} of the words have a speaker label",
                             "Run `veos speakers` (and `veos cut` or `veos shots plan` again) so every word is labelled."))
    # SPK-2 caption styles
    caps_on = _get(tl, "captions.subtitles", "auto") not in ("off", False)
    styles = speaker_styles(tl, tokens)
    if caps_on and styles and len(spk_ids) >= 2:
        roles = {}
        for w in words:
            if w.get("speaker"):
                roles.setdefault(w["speaker"], w.get("role"))
        seen = {}
        for s in spk_ids:
            st = styles.get(s) or styles.get(roles.get(s) or "")
            if not st:
                out.append(_fail("SPK-2", c, 0.0, f"speaker {s} ({roles.get(s) or 'no role'}) has no caption style",
                                 "Add the speaker (or its role: host/guest) to captions.speakers {colour, style}."))
                continue
            key = (str(st.get("colour", "")).upper(), st.get("style", "upright"))
            if key in seen:
                out.append(_fail("SPK-2", c, 0.0, f"speakers {seen[key]} and {s} share the same caption style {key}",
                                 "Give each speaker its own caption colour or style (e.g. host white upright, guest yellow italic)."))
            seen[key] = s
    if not shots:
        return out
    cuts = [s["t0"] for s in shots[1:]]

    def shot_at(t):
        for s in shots:
            if s["t0"] - 1e-6 <= t < s["t1"] - 1e-6:
                return s
        return shots[-1]

    floor, _ = turns(words, cr["backchannel_max_s"])
    # SPK-3 handover cuts
    for prev, cur in zip(floor, floor[1:]):
        t = cur["t0"]
        before, after = shot_at(t - 0.2), shot_at(t + 0.05)
        if before["layout"] != "full" and after["layout"] != "full":
            continue
        pe = prev["words"][-1]["e"] if prev.get("words") else t
        lo = min(t - tol - cr.get("lead_f", 1) / FPS, max(pe, t - 1.0))   # in the pause before the first word counts
        near = [x for x in cuts if lo <= x <= t + tol]
        if not near:
            out.append(_fail("SPK-3", c, t, f"{cur['speaker']} starts talking at {t:.2f}s but there is no cut within "
                                             f"{cr['handover_tol_f']} frames",
                             f"Cut to {cur['speaker']} on their first word (shot boundary at {t:.2f}s)."))
    # SPK-4 speaker on screen (in a stack: the speaker on top, or the host when dialogue.stack.top is "host")
    top_rule = stack_top(tokens)
    hosts = host_ids(words) if top_rule == "host" else set()
    for s in shots:
        talk = {}
        for w in words:
            if w.get("speaker") and s["t0"] <= w["s"] < s["t1"]:
                talk[w["speaker"]] = talk.get(w["speaker"], 0.0) + (w["e"] - w["s"])
        if not talk:
            continue
        main = max(talk, key=talk.get)
        if s["layout"] == "stack":
            if hosts:
                top = s.get("top_subject")
                if top and top not in hosts and s.get("bottom_subject") in hosts:
                    out.append(_fail("SPK-4", c, s["t0"], f"stack {s['t0']:.2f}-{s['t1']:.2f}s shows {top} on top; "
                                                          "dialogue.stack.top is host", "Put the host in the top half."))
                continue
            if s.get("top_subject") and s["top_subject"] != main and talk[main] > 0.6 * sum(talk.values()):
                out.append(_fail("SPK-4", c, s["t0"], f"stack {s['t0']:.2f}-{s['t1']:.2f}s shows {s['top_subject']} on "
                                                      f"top while {main} talks", "Put the speaker in the top half."))
            continue
        if s.get("subject") == main or s.get("subject") is None:
            continue
        if s.get("cut_reason") == "reaction":
            mx = cr["reaction_s"][1] + 0.5
            if s["t1"] - s["t0"] > mx:
                out.append(_fail("SPK-4", c, s["t0"], f"reaction shot on {s['subject']} holds {s['t1'] - s['t0']:.1f}s "
                                                      f"(max {mx:.1f}s)", "Shorten the cutaway and return to the speaker."))
            if any(s["t0"] + 0.1 < f["t0"] < s["t1"] - 0.1 for f in floor):
                out.append(_fail("SPK-4", c, s["t0"], "a reaction cutaway spans a speaker handover",
                                 "End the reaction before the next speaker starts and cut to them on their first word."))
            continue
        if talk[main] > 0.6 * sum(talk.values()):
            out.append(_fail("SPK-4", c, s["t0"], f"full shot {s['t0']:.2f}-{s['t1']:.2f}s shows {s.get('subject')} "
                                                  f"while {main} talks", f"Show {main}, or mark it cut_reason: reaction."))
    # SPK-5 never inside a word
    for x in cuts:
        w = next((w for w in words if w["s"] + 1.5 / FPS < x < w["e"] - 1.5 / FPS), None)
        if w:
            out.append(_fail("SPK-5", c, x, f"cut at {x:.2f}s lands inside the word '{w['w']}' ({w['s']:.2f}-{w['e']:.2f})",
                             f"Move the cut to {w['s']:.2f}s or {w['e']:.2f}s."))
    # SPK-6 holds
    for s in shots:
        d = s["t1"] - s["t0"]
        mx = (cr["stack_max_s"] if s["layout"] == "stack" else cr["max_hold_s"]) + 1.0
        if d > mx:
            out.append(_fail("SPK-6", c, s["t0"], f"{s['layout']} shot holds {d:.1f}s (max {mx:.1f}s)",
                             "Split it with a reaction cutaway or a jump re-crop (veos shots plan does this)."))
    return out


RULES = {"V-SPEAKER": rule_speaker}


class DialogueCtx:
    """Minimal context for running V-SPEAKER outside `veos validate` (veos shots check)."""

    def __init__(self, tl: dict, words: list[dict], tokens: dict):
        self.tl, self.words, self.style, self.tokens = tl, words, tokens, tokens
        self.beats = sorted(tl.get("beats", []), key=lambda b: b.get("t0", 0))

    def beat_id(self, t: float):
        for b in self.beats:
            if b.get("t0", 0) <= t < b.get("t1", 0):
                return b.get("id")
        return None
