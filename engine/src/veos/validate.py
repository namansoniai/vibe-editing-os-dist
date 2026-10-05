"""`veos validate`: check plan/timeline.json + the reel's scenes against the playbook's hard rules (CONTRACT v2 section 5).

Inputs: plan/timeline.json (beats, stage, camera, sfx, ...), plan/scenes.meta.json (the registered scenes' metadata;
rebuilt by `veos scenes-meta` when missing or older than plan/scenes.js), plan/measure.json when present (real rendered
rects; preferred over each scene's declared `box`), work/face.edit.json, playbooks/<id>/tokens.json (budgets, layout, rules_v0).

Scene meta fields the rules use: id, t_in, t_out, z, behind, in, box, roles, events (local seconds of internal visual
changes), text (carries text), may_overlap_face, kind ("banner" | "cta-keyword" | "meme"), text_content (the text it
shows, as one string), chips ([{text, role}], banner only), lines (int, banner only).

Output (summary dict; cli prints it as one JSON line and `plan/validate.json` gets the same content):
  ok       always true when the command itself ran (a failed *rule* is not a failed command)
  passed   true only when `failures` is empty
  failures [{rule, beat, t, msg, fix}]   warnings [str]   stats {...}
Expected errors (missing timeline/scenes/playbook, unparsable JSON) raise VeosError -> ok=false, exit 1.

Sound cues with a catalogue `id` are checked by sfxrules.py (S1-S6, always on); legacy {"file"} cues by M10 / M9.

Rules: one function per rule id, registered in RULES. The enabled set is the playbook's `rules_v0`.
Every rule function has the signature `rule(ctx) -> list[failure dict]`.
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Callable

from .core import FPS, VeosError, need_project, read_json, write_json
from .globalchecks import GLOBAL_CHECKS

NON_BRIGHT = {"ink", "paper", "canvas", "grid", "night"}
NUM_WORDS = {w: i for i, w in enumerate(
    "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen "
    "sixteen seventeen eighteen nineteen twenty".split())}
EMOJI_RE = re.compile("[\U0001F000-\U0001FAFF☀-➿⭐⭕←-⇿⌀-⏿⬀-⯿]")
SAMPLE_EVERY = 5
SUBTITLE_Z = (7, 8)


def add_args(p, cmd):
    p.add_argument("--timeline", default=None, help="timeline file (default <project>/plan/timeline.json)")
    p.add_argument("--skip-motion", action="store_true",
                   help="do not (re)measure per-frame motion for G3; use whatever plan/measure*.json already holds")


# --------------------------------------------------------------------------- helpers
def fr(t: float) -> int:
    return int(round(float(t) * FPS))


def norm_box(b: Any) -> tuple[float, float, float, float] | None:
    """Return (x0, y0, x1, y1) from {x,y,w,h} or [x,y,w,h]."""
    try:
        if isinstance(b, dict):
            x, y, w, h = (float(b[k]) for k in ("x", "y", "w", "h"))
        elif isinstance(b, (list, tuple)) and len(b) >= 4:
            x, y, w, h = (float(v) for v in b[:4])
        else:
            return None
    except (KeyError, TypeError, ValueError):
        return None
    return (x, y, x + w, y + h)


def overlap(a, b) -> bool:
    return a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]


def expand(b, m):
    return (b[0] - m, b[1] - m, b[2] + m, b[3] + m)


def count_words_emoji(text: str) -> tuple[int, int]:
    emoji = len(EMOJI_RE.findall(text))
    clean = EMOJI_RE.sub(" ", text).replace("️", " ").replace("‍", " ")
    return sum(1 for w in clean.split() if re.search(r"\w", w)), emoji


def banner_chips(s: dict) -> list[tuple[str, str | None]]:
    out = []
    for c in s.get("chips") or []:
        if isinstance(c, dict):
            out.append((str(c.get("text", "")), c.get("role")))
        else:
            out.append((str(c), None))
    return out


class Ctx:
    """Everything a rule needs, with small helpers."""

    def __init__(self, tl, style, tokens, words, face, scenes, measure, warnings):
        self.tl, self.style, self.tokens, self.words, self.face = tl, style, tokens, words, face
        self.warnings = warnings
        self.meta = tl.get("meta", {})
        self.beats = sorted(tl.get("beats", []), key=lambda b: b.get("t0", 0))
        self.scenes = scenes
        self.stage = sorted(tl.get("stage", []), key=lambda e: e.get("t", 0))
        self.camera = sorted(tl.get("camera", []), key=lambda e: e.get("t", 0))
        self.transitions = tl.get("transitions", [])
        self.sfx = sorted(tl.get("sfx", []), key=lambda e: e.get("t", 0))
        self.legacy_sfx = [s for s in self.sfx if "id" not in s]   # {"file": ...} cues: M10 / M9 (cues with an `id`: S1-S6)
        self.catalog_by_id: dict | None = None
        self.budgets = style.get("budgets", {})
        self.layout = style.get("layout", {})
        # measured rects: {frame: {scene id: (x0,y0,x1,y1)}}
        self.measured: dict[int, dict[str, tuple]] = {}
        for k, v in ((measure or {}).get("frames") or {}).items():
            try:
                self.measured[int(k)] = {sid: tuple(float(x) for x in r) for sid, r in v.items() if isinstance(r, (list, tuple)) and len(r) >= 4}
            except (ValueError, TypeError):
                continue
        fps = self.meta.get("fps", FPS) or FPS
        dur = self.meta.get("duration")
        if dur is None:
            dur = max([b.get("t1", 0) for b in self.beats] + [s.get("t_out", 0) for s in self.scenes] + [0])
        self.duration = float(dur)
        self.frames = int(self.meta.get("frames") or fr(self.duration))
        self.fps = fps

    def beat_at(self, t: float) -> dict | None:
        for b in self.beats:
            if b.get("t0", 0) - 1e-6 <= t < b.get("t1", 0) - 1e-6:
                return b
        return self.beats[-1] if self.beats and abs(t - self.beats[-1].get("t1", -1)) < 1e-6 else None

    def beat_id(self, t: float):
        b = self.beat_at(t)
        return b.get("id") if b else None

    def scene_beats(self, s: dict) -> list[dict]:
        """Beats that list this scene, else the beat at its start."""
        mine = [b for b in self.beats if s.get("id") in (b.get("layers") or [])]
        if mine:
            return mine
        b = self.beat_at(s.get("t_in", 0))
        return [b] if b else []

    def box(self, s: dict):
        """Declared footprint (x0,y0,x1,y1) or None."""
        return norm_box(s.get("box"))

    def rect(self, s: dict, n: int | None = None):
        """Measured rect at sampled frame n when available, else the declared box."""
        if n is not None and n in self.measured and s.get("id") in self.measured[n]:
            return self.measured[n][s["id"]]
        return self.box(s)

    def union_rect(self, s: dict):
        """Union of all measured rects for the scene (else the declared box)."""
        rs = [m[s["id"]] for m in self.measured.values() if s.get("id") in m]
        if not rs:
            return self.box(s)
        return (min(r[0] for r in rs), min(r[1] for r in rs), max(r[2] for r in rs), max(r[3] for r in rs))

    def active(self, s: dict, n: int) -> bool:
        return fr(s.get("t_in", 0)) <= n < fr(s.get("t_out", 0))

    def is_text(self, s: dict) -> bool:
        return bool(s.get("text"))

    def roles(self, s: dict) -> set[str]:
        known = set(self.style.get("roles", {}))
        return {r for r in (s.get("roles") or []) if r in known}

    def of_kind(self, kind: str) -> list[dict]:
        return [s for s in self.scenes if s.get("kind") == kind]

    def section_range(self, pred: Callable[[str], bool]):
        return [(b["t0"], b["t1"]) for b in self.beats if pred(str(b.get("section", "")))]

    def item_numbers(self) -> set[str]:
        out = set()
        for b in self.beats:
            m = re.match(r"ITEM[-_ ]?(\w+)", str(b.get("section", "")), re.I)
            if m:
                out.add(m.group(1))
        return out

    def stage_at(self, t: float) -> str:
        cur = "full"
        for e in self.stage:
            if fr(e.get("t", 0)) <= fr(t):
                cur = e.get("layout", cur)
        return cur

    def internal_events(self) -> list[float]:
        """Absolute times of scene.events (LOCAL seconds after t_in), clipped to [t_in, t_out]."""
        out = []
        for s in self.scenes:
            a, b = float(s.get("t_in", 0)), float(s.get("t_out", 0))
            for v in s.get("events") or []:
                try:
                    v = float(v)
                except (TypeError, ValueError):
                    continue
                if a - 1e-9 <= a + v <= b + 1e-9:
                    out.append(a + v)
        return out

    def visual_events(self) -> list[int]:
        """Frames at which something visibly changes (subtitle card changes are not counted)."""
        ev = {0, fr(self.duration)}
        for s in self.scenes:
            ev.add(fr(s.get("t_in", 0)))
            ev.add(fr(s.get("t_out", 0)))
        ev |= {fr(e.get("t", 0)) for e in self.stage}
        ev |= {fr(e.get("t", 0)) for e in self.camera}
        ev |= {fr(e.get("t", 0)) for e in self.transitions}
        ev |= {fr(t) for t in self.internal_events()}
        return sorted(ev)

    def start_events(self) -> list[float]:
        """Seconds at which a scene, stage change or camera event *starts* (for on-the-word checks)."""
        return sorted([float(s.get("t_in", 0)) for s in self.scenes]
                      + [float(e.get("t", 0)) for e in self.stage]
                      + [float(e.get("t", 0)) for e in self.camera]
                      + self.internal_events())


def fail(rule, beat, t, msg, fix):
    return {"rule": rule, "beat": beat, "t": round(float(t), 3), "msg": msg, "fix": fix}


# --------------------------------------------------------------------------- rules
def rule_m1(c: Ctx):
    out = []
    at0 = [s for s in c.scenes if fr(s.get("t_in", 0)) <= 0 < fr(s.get("t_out", 0))]
    bid = c.beat_id(0)
    if not any(s.get("kind") == "banner" for s in at0):
        out.append(fail("M1", bid, 0, "no banner scene (kind: 'banner') is on screen at frame 0",
                        "add a scene with kind 'banner', t_in 0, so the headline is readable on the first frame"))
    if not any(s.get("kind") != "banner" and s.get("z") not in SUBTITLE_Z and s.get("z", 0) < 10 for s in at0):
        out.append(fail("M1", bid, 0, "frame 0 has no result visual besides the banner and captions",
                        "add a card, mock or result-visual scene starting at t 0"))
    if c.stage_at(0) == "hidden":
        out.append(fail("M1", bid, 0, "the speaker is hidden at frame 0",
                        "set the stage layout at t 0 to full, panel, inset, slide-aside or bubble"))
    anim = any(fr(s.get("t_in", 0)) == 0 and s.get("in", "settle") not in (None, "none") for s in c.scenes)
    anim = anim or any(fr(e.get("t", 0)) == 0 for e in c.camera)
    if not anim:
        out.append(fail("M1", bid, 0, "nothing is moving on frame 0",
                        "give the banner an entrance (in: settle or pop) starting at t 0, or add a camera event at t 0"))
    return out


def rule_m7(c: Ctx):
    out = []
    every, hook_every = c.budgets.get("change_every_s", 1.5), c.budgets.get("hook_change_every_s", 1.0)
    max_static = c.budgets.get("max_static_s", 2.5)
    hooks = c.section_range(lambda s: s.upper() == "HOOK")
    ev = c.visual_events()
    for a, b in zip(ev, ev[1:]):
        gap = (b - a) / FPS
        ta = a / FPS
        in_hook = any(h0 - 1e-6 <= ta < h1 - 1e-6 for h0, h1 in hooks)
        limit = hook_every if in_hook else every
        if gap > max_static + 1e-6:
            msg = f"nothing changes for {gap:.1f} s ({ta:.1f} to {b / FPS:.1f}); the maximum static time is {max_static} s"
        elif gap > limit + 1e-6:
            msg = f"nothing changes for {gap:.1f} s ({ta:.1f} to {b / FPS:.1f}); {'hook' if in_hook else 'body'} limit is {limit} s"
        else:
            continue
        mid = (a + b) / 2 / FPS
        out.append(fail("M7", c.beat_id(ta), ta, msg,
                        f"add a scene, scene event, camera move or stage change around {mid:.1f} s (between {ta:.1f} and {b / FPS:.1f})"))
    return out


def rule_m4(c: Ctx):
    out = []
    tb = c.style.get("type", {}).get("banner", {})
    max_words, max_lines = tb.get("max_words", 9), tb.get("max_lines", 2)
    for s in c.of_kind("banner"):
        t0 = s.get("t_in", 0)
        text = str(s.get("text_content", ""))
        chips = banner_chips(s)
        lines = s.get("lines")
        words, emoji = count_words_emoji(text)
        bid = c.beat_id(t0)
        if words > max_words:
            out.append(fail("M4", bid, t0, f"banner {s.get('id')} has {words} words (max {max_words})",
                            f"shorten the banner to {max_words} words or fewer (emoji don't count)"))
        if isinstance(lines, (int, float)) and lines > max_lines:
            out.append(fail("M4", bid, t0, f"banner {s.get('id')} uses {int(lines)} lines (max {max_lines})",
                            f"rewrite the banner to fit on {max_lines} lines"))
        roles = sorted(str(r) for _, r in chips)
        if not (len(chips) == 1 or (len(chips) == 2 and roles == ["bad", "good"])):
            out.append(fail("M4", bid, t0, f"banner {s.get('id')} has {len(chips)} keyword chips (need exactly 1, "
                            "or 2 when one is role bad and the other good)",
                            "declare one CAPS keyword chip in the banner scene meta: chips: [{text, role}]"
                            if len(chips) != 2 else "give the two chips the roles bad and good, or keep only one chip"))
        if emoji > 2:
            out.append(fail("M4", bid, t0, f"banner {s.get('id')} has {emoji} emoji (max 2)",
                            "keep at most 2 emoji in the banner"))
    return out


def rule_m6(c: Ctx):
    out = []
    lead, land = c.style.get("motion", {}).get("lead_frames", 2) / FPS, 5 / FPS
    ev = c.start_events()
    for b in c.beats:
        trig = b.get("trigger") or {}
        if trig.get("at") is None:
            continue
        at = float(trig["at"])
        lo, hi = at - lead - 0.1, at + land
        if any(lo - 1e-6 <= e <= hi + 1e-6 for e in ev):
            continue
        near = min(ev, key=lambda e: abs(e - at)) if ev else None
        off = f"nearest event is {near - at:+.2f} s from the word" if near is not None else "no events at all"
        out.append(fail("M6", b.get("id"), at,
                        f"nothing starts on the trigger word '{trig.get('word', '')}' at {at:.2f} s ({off})",
                        f"start the matching scene, scene event, stage change or camera move between {lo:.2f} and {at + land:.2f} s "
                        f"(about {at - lead:.2f} s is ideal)"))
    return out


def rule_m12(c: Ctx):
    out = []
    clr = c.layout.get("face_clearance", 40)
    safe = c.layout.get("safe", {"x": [64, 1016], "y": [110, 1500]})
    bx, btop = c.layout.get("banner_x", [40, 1040]), c.layout.get("banner_top", 150) - 10
    # text inside the safe zone (measured union over the sampled frames, else the declared box)
    for s in c.scenes:
        if not c.is_text(s):
            continue
        bb = c.union_rect(s)
        if bb is None:
            continue
        ins = s.get("text_inset", 0) or 0  # containers (cards) whose text sits inset from the edge
        if ins:
            bb = (bb[0] + ins, bb[1] + ins, bb[2] - ins, bb[3] - ins)
        if s.get("kind") == "banner":
            x0, x1, y0 = bx[0], bx[1], btop
        else:
            x0, x1, y0 = safe["x"][0], safe["x"][1], safe["y"][0]
        if bb[0] < x0 - 4 or bb[2] > x1 + 4 or bb[1] < y0 - 4 or bb[3] > safe["y"][1] + 4:  # 4 px: rotation / AA slack
            out.append(fail("M12", c.beat_id(s.get("t_in", 0)), s.get("t_in", 0),
                            f"text scene {s.get('id')} rect {tuple(int(v) for v in bb)} leaves the safe zone "
                            f"x {x0}-{x1}, y {y0}-{safe['y'][1]}",
                            f"move or shrink {s.get('id')} so its content sits inside the safe zone"))
    # face clearance, per sampled frame
    if c.face is None:
        return out
    frames = sorted(c.measured) if c.measured else list(range(0, c.frames, SAMPLE_EVERY))
    seen = set()
    for n in frames:
        fb = c.face[n] if n < len(c.face) else None
        fb = norm_box(fb) if fb else None
        if fb is None:
            continue
        zone = expand(fb, clr)
        for s in c.scenes:
            if s.get("id") in seen or s.get("z", 0) < 5 or s.get("behind") or not c.active(s, n):
                continue
            if s.get("may_overlap_face"):
                continue
            bb = c.rect(s, n)
            if bb is not None and overlap(bb, zone):
                seen.add(s.get("id"))
                src = "measured" if n in c.measured and s.get("id") in c.measured[n] else "declared"
                out.append(fail("M12", c.beat_id(n / FPS), n / FPS,
                                f"scene {s.get('id')} covers the face (plus {clr}px clearance) from frame {n} ({src} rect)",
                                f"move {s.get('id')} so its content stays {clr}px clear of the face, "
                                f"or drop its z below 5 / set behind: true / may_overlap_face: true"))
    return out


def rule_n5_zoom(c: Ctx):
    out, prev = [], None
    presets = c.style.get("camera_presets", {})
    for e in c.camera:
        p = e.get("preset")
        if p == "shake":
            continue
        if prev is not None and p == prev:
            out.append(fail("N5-zoom", c.beat_id(e.get("t", 0)), e.get("t", 0),
                            f"camera preset '{p}' is used twice in a row",
                            f"change the camera move at {e.get('t', 0):.2f} s to a different preset (or remove it)"))
        prev = p
    counts: dict[str, int] = {}
    for e in c.camera:
        counts[e.get("preset")] = counts.get(e.get("preset"), 0) + 1
    for p, n in counts.items():
        mx = (presets.get(p) or {}).get("max_per_reel")
        if mx and n > mx:
            out.append(fail("N5-zoom", None, 0, f"camera preset '{p}' is used {n} times (max {mx} per reel)",
                            f"remove {n - mx} use(s) of '{p}'"))
    return out


def rule_n6(c: Ctx):
    out = []
    mx = c.style.get("max_bright_per_frame", 3)
    flagged = False
    for n in range(0, c.frames, SAMPLE_EVERY):
        bright = set()
        for s in c.scenes:
            if c.active(s, n) and s.get("z", 0) < 11:  # z 11 = momentary light passes (sweep, flash), not a hue element
                bright |= c.roles(s) - NON_BRIGHT
        if len(bright) > mx and not flagged:
            flagged = True
            out.append(fail("N6", c.beat_id(n / FPS), n / FPS,
                            f"{len(bright)} bright colours at once from frame {n}: {', '.join(sorted(bright))} (max {mx})",
                            f"recolour or remove scenes around {n / FPS:.1f} s so only {mx} bright roles show together"))
    for s in c.scenes:
        if "comedy" in c.roles(s):
            bad = [b for b in c.scene_beats(s) if b.get("tone") != "mock"]
            if bad:
                out.append(fail("N6", bad[0].get("id"), s.get("t_in", 0),
                                f"comedy colour on scene {s.get('id')} in a '{bad[0].get('tone')}' beat",
                                f"use the beat's own colour role for {s.get('id')}, or move it to a mock beat"))
    return out


def rule_m10(c: Ctx):
    out = []
    mx = c.budgets.get("sfx_max_uses_per_file", 2)
    n_items = len(c.item_numbers())
    uses: dict[str, list[dict]] = {}
    for s in c.legacy_sfx:
        uses.setdefault(s.get("file"), []).append(s)
    over_ok_used = False
    for f, us in uses.items():
        if len(us) > mx:
            list_cue = all(u.get("role") == "list-cue" for u in us) and len(us) <= n_items
            if list_cue and not over_ok_used:
                over_ok_used = True
                continue
            why = "only one file may exceed it, as the list cue" if list_cue else "not allowed unless it is the list cue"
            out.append(fail("M10", us[mx].get("beat"), us[mx].get("t", 0),
                            f"{f} is used {len(us)} times (max {mx}; {why})",
                            f"replace the use at {us[mx].get('t', 0):.2f} s (and any later ones) with another file from the same pool"))
        if any(u.get("role") == "meme" for u in us) and len(us) > 1:
            out.append(fail("M10", us[1].get("beat"), us[1].get("t", 0), f"meme file {f} is used {len(us)} times (once only)",
                            "use a different meme file for the repeat"))
    for a, b in zip(c.legacy_sfx, c.legacy_sfx[1:]):
        if a.get("file") == b.get("file"):
            out.append(fail("M10", b.get("beat"), b.get("t", 0), f"{b.get('file')} is on two consecutive cues",
                            f"swap the cue at {b.get('t', 0):.2f} s for a different file in the same pool"))
    return out


def rule_m9(c: Ctx):
    out = []
    mx, gap = c.budgets.get("meme_max_per_reel", 4), c.budgets.get("meme_min_gap_s", 4)
    memes = [s for s in c.legacy_sfx if s.get("role") == "meme"]
    wins = 0
    for s in memes:
        b = next((x for x in c.beats if x.get("id") == s.get("beat")), None) or c.beat_at(s.get("t", 0))
        tone = b.get("tone") if b else None
        if tone == "win" and wins == 0:
            wins += 1
        elif tone != "mock":
            out.append(fail("M9", b.get("id") if b else None, s.get("t", 0),
                            f"meme sound {s.get('file')} sits on a '{tone}' beat (mock only; one win allowed)",
                            f"remove the meme sound at {s.get('t', 0):.2f} s or move it to a mock beat"))
    if len(memes) > mx:
        out.append(fail("M9", memes[mx].get("beat"), memes[mx].get("t", 0), f"{len(memes)} meme sounds (max {mx})",
                        f"remove {len(memes) - mx} meme sound(s)"))
    for a, b in zip(memes, memes[1:]):
        if b.get("t", 0) - a.get("t", 0) < gap - 1e-6:
            out.append(fail("M9", b.get("beat"), b.get("t", 0),
                            f"meme sounds at {a.get('t', 0):.1f} s and {b.get('t', 0):.1f} s are under {gap} s apart",
                            f"move or remove the meme sound at {b.get('t', 0):.2f} s so memes are at least {gap} s apart"))
    for s in c.scenes:
        if s.get("kind") == "meme" and "comedy" in c.roles(s):  # meme visuals (stamps, stickers) are mock-beat only
            bad = [b for b in c.scene_beats(s) if b.get("tone") != "mock"]
            if bad:
                out.append(fail("M9", bad[0].get("id"), s.get("t_in", 0),
                                f"meme scene {s.get('id')} is on a '{bad[0].get('tone')}' beat",
                                f"remove {s.get('id')} or move it to a mock beat"))
    return out


def rule_m13(c: Ctx):
    out = []
    items = len(c.item_numbers())
    banner = next(iter(c.of_kind("banner")), None)
    if banner is not None and items > 0:
        text = str(banner.get("text_content", ""))
        cands = [int(m) for m in re.findall(r"(?<![\w,.])(\d{1,2})(?![\w,.]\d)", text) if int(m) <= 20]
        cands += [NUM_WORDS[w] for w in re.findall(r"[a-z]+", text.lower()) if w in NUM_WORDS]
        count = c.meta.get("count")
        expected = int(count) if count is not None else (cands[0] if cands else None)
        if expected is not None and expected != items:
            out.append(fail("M13", None, banner.get("t_in", 0),
                            f"the promise says {expected} but the beats show {items} item section(s)",
                            f"make the number of ITEM sections equal {expected}, or change the banner/meta.count to {items}"))
        elif count is not None and cands and int(count) not in cands:
            out.append(fail("M13", None, banner.get("t_in", 0),
                            f"banner number {cands[0]} does not match meta.count {count}",
                            f"change the banner number to {count}"))
    kw = c.meta.get("keyword")
    if kw:
        cta = c.section_range(lambda s: s.upper() == "CTA")
        found = False
        for s in c.of_kind("cta-keyword"):
            if not any(fr(s.get("t_in", 0)) < fr(t1) and fr(s.get("t_out", 0)) > fr(t0) for t0, t1 in cta):
                continue
            if str(kw).lower() in str(s.get("text_content", "")).lower():
                found = True
                break
        if not found:
            t = cta[0][0] if cta else 0
            out.append(fail("M13", c.beat_id(t), t, f"the CTA keyword '{kw}' is never on screen in the CTA section",
                            f"add a scene with kind 'cta-keyword' and text_content containing '{kw}' during the CTA section"))
    return out


RULES: dict[str, Callable[[Ctx], list]] = {
    "M1": rule_m1, "M7": rule_m7, "M4": rule_m4, "M6": rule_m6, "M12": rule_m12,
    "N5-zoom": rule_n5_zoom, "N6": rule_n6, "M10": rule_m10, "M9": rule_m9, "M13": rule_m13,
}


# --------------------------------------------------------------------------- command
def _load_optional(path: Path, label: str, warnings: list, skip_note: str = ""):
    if path.exists():
        try:
            return read_json(path)
        except ValueError as e:
            warnings.append(f"{label} is not valid JSON ({e}); ignored")
            return None
    warnings.append(f"{label} not found ({path.name}){'; ' + skip_note if skip_note else ''}")
    return None


def _with_motion(proj, tl, scenes, measure, warnings, skip) -> dict | None:
    """Merge plan/measure.json with plan/measure.motion.json (every frame where a z3-10 scene is active, for G3).

    The motion file is (re)built headless when plan/scenes.js exists and it is missing or older than scenes.js / timeline.json
    and measure.json does not already cover those frames (e.g. `veos measure --every 1`). Cost: see SPEC section 4.
    """
    from .scenes import MOTION_CAP, measure_motion, motion_frames
    frames_data = dict((measure or {}).get("frames") or {})
    sj, tp, mo = proj.root / "plan" / "scenes.js", proj.root / "plan" / "timeline.json", proj.root / "plan" / "measure.motion.json"
    nframes = int((tl.get("meta") or {}).get("frames") or 0)
    if nframes < 1:
        return measure
    need, truncated = motion_frames(scenes, nframes)
    if truncated:
        warnings.append(f"G3 smooth-motion checked only the first {MOTION_CAP} frames ({MOTION_CAP // FPS} s); the reel is longer")
    missing = [n for n in need if str(n) not in frames_data]
    if missing and sj.exists() and not skip:
        stale = not mo.exists() or mo.stat().st_mtime < max(sj.stat().st_mtime, tp.stat().st_mtime)
        if stale:
            try:
                measure_motion(proj, scenes)
            except Exception as e:  # noqa: BLE001 - no browser, broken scene...: a warning, the other rules still run
                warnings.append(f"G3 smooth-motion skipped: could not measure frames ({getattr(e, 'message', str(e))[:200]})")
    if mo.exists():
        extra = _load_optional(mo, "plan/measure.motion.json", warnings)
        if extra:
            frames_data.update(extra.get("frames") or {})
    elif missing:
        warnings.append("G3 smooth-motion not checked: no per-frame measure (run `veos measure --motion`, or `veos validate` with scenes.js present)")
    if not frames_data:
        return measure
    return {**(measure or {}), "frames": frames_data}


def main(args, project):
    from .scenes import load_scenes_meta
    from .tokens import load_playbook, project_playbook
    proj = need_project(project)
    tpath = Path(args.timeline) if args.timeline else proj.root / "plan" / "timeline.json"
    if args.timeline and not tpath.exists() and (proj.root / args.timeline).exists():
        tpath = proj.root / args.timeline
    if not tpath.exists():
        raise VeosError("NO_TIMELINE", f"timeline not found: {tpath}", "Write plan/timeline.json first (see renderer/CONTRACT.md §2).")
    try:
        tl = read_json(tpath)
    except ValueError as e:
        raise VeosError("BAD_TIMELINE", f"timeline is not valid JSON: {e}", "Fix the JSON syntax in the timeline file.")
    if not isinstance(tl, dict) or not isinstance(tl.get("beats"), list):
        raise VeosError("BAD_TIMELINE", "timeline needs a `beats` list", "See renderer/CONTRACT.md §2 for the format.")

    warnings: list[str] = []
    if tl.get("layers"):
        warnings.append("timeline.layers is ignored (v2): visuals are scenes in plan/scenes.js; beats[].layers lists scene ids")
    style = load_playbook(project_playbook(proj, None, tl.get("meta")))
    scenes = load_scenes_meta(proj)

    tokens = _load_optional(proj.work / "tokens.json", "work/tokens.json", warnings) if (proj.work / "tokens.json").exists() else None
    words = _load_optional(proj.work / "words.edit.json", "work/words.edit.json", warnings) if (proj.work / "words.edit.json").exists() else None
    face = None
    fpath = proj.abs((tl.get("inputs") or {}).get("face") or "work/face.edit.json")
    fdata = _load_optional(fpath, "work/face.edit.json", warnings, "face rules skipped")
    if fdata is not None:
        face = fdata.get("boxes") if isinstance(fdata, dict) else fdata
        if not isinstance(face, list):
            warnings.append("face file has no `boxes` list; face rules skipped")
            face = None

    measure = None
    mp = proj.root / "plan" / "measure.json"
    if mp.exists():
        measure = _load_optional(mp, "plan/measure.json", warnings)
        sj = proj.root / "plan" / "scenes.js"
        if measure and sj.exists() and mp.stat().st_mtime < sj.stat().st_mtime:
            warnings.append("plan/measure.json is older than plan/scenes.js; re-run `veos measure` for real rects")
    else:
        warnings.append("plan/measure.json not found; using declared scene boxes (run `veos measure` for real positions)")

    measure = _with_motion(proj, tl, scenes, measure, warnings, getattr(args, "skip_motion", False))
    ctx = Ctx(tl, style, tokens, words, face, scenes, measure, warnings)
    sfx_failures = []
    if any("id" in s for s in ctx.sfx):  # S1-S6: always on when the timeline has catalogue cues
        from .sfxlib import load_catalog
        try:
            cat = load_catalog()
        except VeosError as e:
            warnings.append(e.message)
            cat = None
        ctx.catalog_by_id = {e["id"]: e for e in cat} if cat is not None else None
        from .sfxrules import check_sfx
        sfx_failures = check_sfx(ctx)
    enabled = style.get("rules_v0") or list(RULES)
    failures: list[dict] = []
    for rid in enabled:
        fn = RULES.get(rid)
        if fn is None:
            warnings.append(f"rule {rid} is enabled in the playbook but not implemented")
            continue
        failures.extend(fn(ctx))
    gstats = {}
    for gid, fn in GLOBAL_CHECKS.items():
        got = fn(ctx)
        gstats[gid] = len(got)
        failures.extend(got)
    failures.extend(sfx_failures)
    failures.sort(key=lambda f: (f["t"], f["rule"]))

    ev = ctx.visual_events()
    stats = {
        "beats": len(ctx.beats), "scenes": len(ctx.scenes), "duration_s": round(ctx.duration, 3),
        "visual_events": len(ev) - 2 if len(ev) > 2 else 0,
        "events_per_s": round(max(len(ev) - 2, 0) / ctx.duration, 2) if ctx.duration else 0,
        "camera_events": len(ctx.camera), "sfx_cues": len(ctx.sfx), "sfx_rules": len(sfx_failures),
        "rules_run": [r for r in enabled if r in RULES], "global_checks": gstats, "measured_frames": len(ctx.measured),
        "face_checked": face is not None, "measured": bool(ctx.measured), "words_loaded": words is not None,
        "tokens_loaded": tokens is not None,
    }
    result = {"ok": True, "passed": not failures, "failures": failures, "warnings": warnings, "stats": stats}
    write_json(proj.path("plan", "validate.json"), result)
    return result
