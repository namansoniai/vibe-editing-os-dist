"""`veos validate`: check plan/timeline.json + the reel's scenes against the playbook's hard rules (CONTRACT v2 section 5).

Inputs: plan/timeline.json (beats, stage, camera, sfx, ...), plan/scenes.meta.json (the registered scenes' metadata;
rebuilt by `veos scenes-meta` when missing or older than plan/scenes.js), plan/measure.json when present (real rendered
rects; preferred over each scene's declared `box`), plan/measure.text.json when present (text sizes, contrast, clipping,
E1 occlusion for V-TYPE / V-EXC), work/face.edit.json, work/cutmap.json and work/captions.json when
present (cadence), playbooks/<id>/tokens.json resolved for the reel (`tokens.effective_style`: v1 as-is; v3 with the
reel's `meta.format` / `meta.theme` and plan/tokens.override.json).

Scene meta fields the rules use: id, t_in, t_out, z, behind, in, box, roles, events (local seconds of internal visual
changes), cuts, text (carries text), may_overlap_face, kind ("banner" | "cta-keyword" | "meme" | a headline kind |
hook-archetype kinds, see hookrules.py), satisfies, payoff, text_content, chips, lines, opaque / covers_presenter,
continuous / ambient / motion, exception, text_class, figure / figures / lands / scale (V-DATA, E-08), onword_lead
(V-ONWORD declared early start), smear / handoff (G2 push overlap), depicts (V-DEPICT / V-POINT: what the scene
pictures), illustrative (made-up numbers: V-DATA / V-NUMFMT skip the scene).

Output (summary dict; cli prints it as one JSON line and `plan/validate.json` gets the same content):
  ok       always true when the command itself ran (a failed *rule* is not a failed command)
  passed   true only when `failures` is empty
  failures [{rule, beat, t, msg, fix, playbook_rule?}]   advice [same shape]   warnings [str]   stats {...}

Two levels (Naman, 8 Oct 2026: directions, not limits). `failures` are facts and block the reel: an accidental overlap
(G1), a jump instead of a move (G3), something in front covering the face (V-FACE), text too small or faint to read
(V-TYPE), a number or quote that doesn't match what was said (the fact parts of V-DATA / V-INSERTS / V-CITE), a broken
promise count (V-PROMISE from meta.count), the code not matching the plan (V-PLAN), a malformed effect or anchor field,
an unknown sound id (S6), a missing person cut-out (V-CUTOUT). Everything else is `advice`: direction for the
Director while it plans, never a fix loop, never a block (BLOCKING below; a rule marks a finding advice with
vcommon.advice()). V-DEPICT (a beat showing only words) and V-POINT (the speaker points with words, no picture on
screen) are advice on every reel, plan and code (depictrules.py).
`rule` is the stable registry id (V-...; G1-G3; S1-S6). `playbook_rule` is the playbook's own id when it cites the rule:
the v1 alias (M1, M7, M12...) for reference playbooks, or the H-id a v3 playbook's §2 maps to the V-id.
Expected errors (missing timeline/scenes/playbook, unparsable JSON, invalid v3 tokens) raise VeosError -> ok=false, exit 1.

The scene plan (sceneplan.py): `--plan` judges plan/scenes.plan.json before any code (declared boxes, + V-PLAN
completeness; writes plan/validate.plan.json); without `--plan`, a present plan/scenes.plan.json adds V-PLAN fidelity
(the registered scenes must match the plan).
V-CUTOUT (cutout.py): a reel that draws the person cut-out (a scene behind the presenter, a head breakout) fails until
the cut-out covers the kept frames and its frames are prepared; the plan check only notes it.

Rule registry v2 (ENGINE-IMPLICATIONS §2): REGISTRY maps a V-id to `rule(ctx, params) -> [failure]`. The enabled set
and the params come from `validator.rules` in the tokens (v1: `rules_v0` mapped through tokens.V1_RULE_MAP with
`legacy: true`, which reproduces the old M-rules exactly). Ids listed in PENDING belong to later engine waves.
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Callable

from .caprule import rule_caption
from .cadence import load_caption_chunks, measure as cadence_measure, params_from_tokens, rule_cadence
from .core import FPS, VeosError, need_project, read_json, write_json
from .datarules import rule_data, rule_numfmt
from .globalchecks import GLOBAL_CHECKS
from .hookrules import archetype_of, rule_f0
from .insertrules import rule_cite, rule_inserts
from .layoutrules import engine_of, rule_layout
from . import sceneplan
from .profilecheck import rule_presence, rule_profile
from .structurerules import rule_rehook, rule_theme
from .typefloors import rule_exc, rule_type
from .vcommon import (HEADLINE_KINDS, SUBTITLE_Z, advice, enter_frames, exit_frames, expand, fail, fr, get_path,  # noqa: F401 (re-exported)
                      norm_box, overlap, settled_at)

NON_BRIGHT = {"ink", "paper", "canvas", "grid", "night"}
EMOJI_RE = re.compile("[\U0001F000-\U0001FAFF☀-➿⭐⭕←-⇿⌀-⏿⬀-⯿]")
SAMPLE_EVERY = 5
NC5 = {"top": 110, "bottom_y": 1540, "right_x": 970, "right_y": (900, 1540)}   # structure NC-5 IG UI bands
END_CARD_KINDS = ("end-card", "endcard", "end_card")
KEYWORD_DEVICES = {"comment_keyword", "dm"}
NO_GRAPHICS = ("passthrough", "pass", "none")   # profile.graphics values that may ship a plan with zero scenes


def add_args(p, cmd):
    p.add_argument("--timeline", default=None, help="timeline file (default <project>/plan/timeline.json)")
    p.add_argument("--skip-motion", action="store_true",
                   help="do not (re)measure per-frame motion for G3; use whatever plan/measure*.json already holds")
    p.add_argument("--plan", action="store_true",
                   help="check the plan before any scene code: scenes from plan/scenes.plan.json with their declared "
                        "boxes + the V-PLAN completeness checks -> plan/validate.plan.json (sceneplan.py)")


# --------------------------------------------------------------------------- helpers
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
        self.legacy_sfx = [s for s in self.sfx if "id" not in s]   # {"file": ...} cues: V-LEDGER / V-COMEDY (cues with an `id`: S1-S6)
        self.catalog_by_id: dict | None = None
        self.budgets = style.get("budgets", {})
        self.layout = style.get("layout", {})
        self.cutmap: dict | None = None            # work/cutmap.json (cadence: hard cuts)
        self.caption_chunks: list | None = None    # [{text, t0, t1}] (cadence, V-F0)
        self.caption_source = "none"
        self.stats_extra: dict = {}                # rules add their measures here (stats.cadence, stats.presence...)
        self.text_measure: dict | None = None      # plan/measure.text.json frames {n: {texts, items, slots}} (V-TYPE, V-EXC)
        self.caption_raw: list | None = None       # work/captions.json chunks as exported (size, class...) for V-TYPE
        # measured rects: {frame: {scene id: (x0,y0,x1,y1)}}
        self.measured: dict[int, dict[str, tuple]] = {}
        self.measured_world: dict[int, dict[str, tuple]] = {}  # canvas-camera scenes in world space (V-SAFE)
        self.framing: dict | None = None            # E-16b base reframe record (window framing ranges)
        self.face_raw: list | None = None           # face boxes before the E-16b base reframe (None: same as face)
        for k, v in ((measure or {}).get("frames") or {}).items():
            try:
                self.measured[int(k)] = {sid: tuple(float(x) for x in r) for sid, r in v.items() if isinstance(r, (list, tuple)) and len(r) >= 4}
                wd = v.get("__world") if isinstance(v, dict) else None
                if isinstance(wd, dict):  # canvas-camera layers: the camera-at-rest rect (measureDOM `__world`)
                    self.measured_world[int(k)] = {sid: tuple(float(x) for x in r) for sid, r in wd.items()
                                                   if isinstance(r, (list, tuple)) and len(r) >= 4}
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

    def settled_rect(self, s: dict, world: bool = False):
        """Union of the measured rects in the scene's settled hold (vcommon.settled_at: past its entrance window, before
        its exit window); all measured frames when none is settled; else the declared box. `world`: a canvas-camera
        scene's camera-at-rest rect where measure recorded one (the push of the camera is not the layout)."""
        sid = s.get("id")
        rs = [(n, (self.measured_world.get(n) or {}).get(sid) if world and sid in (self.measured_world.get(n) or {})
               else m[sid]) for n, m in self.measured.items() if sid in m]
        if world:  # a canvas-camera scene seen at rest at the base framing or wider (a home of 0.8, a hub growing
            rest = self._cam_rest_frames(s, [n for n, _ in rs])  # 0.8 -> 1.0): judge what is on screen there
            if rest:
                rs = [(n, self.measured[n][sid]) for n in rest]
        fin, fout = fr(s.get("t_in", 0)), fr(s.get("t_out", 0))
        if fin + enter_frames(s) >= fout - exit_frames(s):
            # too short for a settled hold (an end card that slams 2.6x -> 1 in 3 f and holds 7 f): judge the frames
            # after its entrance window, else its last measured frame (the resting state, not the slam)
            done = [(n, r) for n, r in rs if n >= fin + enter_frames(s)]
            keep = [r for _, r in done] or [r for _, r in sorted(rs)[-1:]]
        else:
            keep = [r for n, r in rs if settled_at(s, n)] or [r for _, r in rs]
        if not keep:
            return self.box(s)
        return (min(r[0] for r in keep), min(r[1] for r in keep), max(r[2] for r in keep), max(r[3] for r in keep))

    def _cam_rest_frames(self, s: dict, frames: list[int]) -> list[int]:
        """Frames (of `frames`, settled) where the canvas camera is not moving and shows this layer at scale <= 1."""
        if not any(s.get("id") in (self.measured_world.get(n) or {}) for n in frames):
            return []
        from .canvascam import camera_for, layer, parallax_of, state_at
        cam = camera_for(self)  # no moves: the camera holds its home framing (state_at)
        if not cam["active"] and abs(float(cam["home"].get("s", 1)) - 1) < 1e-6:
            return []  # nothing to mirror: the world rect stands
        k = parallax_of(s)
        out = []
        for n in frames:
            st = state_at(cam, n)
            if not st.get("moving") and layer(st, k, cam["home"])["s"] <= 1 + 1e-6 and settled_at(s, n):
                out.append(n)
        return out

    def active(self, s: dict, n: int) -> bool:
        return fr(s.get("t_in", 0)) <= n < fr(s.get("t_out", 0))

    def is_text(self, s: dict) -> bool:
        return bool(s.get("text"))

    def roles(self, s: dict) -> set[str]:
        known = set(self.style.get("roles", {}))
        return {r for r in (s.get("roles") or []) if r in known}

    def of_kind(self, kind: str) -> list[dict]:
        return [s for s in self.scenes if s.get("kind") == kind]

    def of_kinds(self, kinds) -> list[dict]:
        return sorted((s for s in self.scenes if s.get("kind") in kinds), key=lambda s: s.get("t_in", 0))

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

    def stage_engine_at(self, t: float) -> str:
        """Engine layout at t (a tokens.layouts id resolves to its `engine`; unknown ids count as full)."""
        lid = self.stage_at(t)
        return engine_of(self.style, lid) or "full"

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
        """Frames at which something visibly changes (subtitle card changes are not counted). Legacy M7 input."""
        ev = {0, fr(self.duration)}
        for s in self.scenes:
            ev.add(fr(s.get("t_in", 0)))
            ev.add(fr(s.get("t_out", 0)))
        ev |= {fr(e.get("t", 0)) for e in self.stage}
        ev |= {fr(e.get("t", 0)) for e in self.camera}
        ev |= {fr(e.get("t", 0)) for e in self.transitions}
        ev |= {fr(t) for t in self.internal_events()}
        ev |= {fr(e.get("t", 0)) for e in self.tl.get("canvas_camera") or []}  # E-14 hook (feat/faceless): a canvas-camera move start is a state change
        return sorted(ev)

    def shot_cuts(self) -> list[float]:
        """Seconds of the camera-angle cuts in timeline.shots (multicam / re-cut reels: every shot start but the first)."""
        out = []
        for s in self.tl.get("shots") or []:
            if not isinstance(s, dict):
                continue
            try:  # `t0` (shots plan / §13.2 re-cut contract); `t` accepted as written by hand
                t = float(s.get("t0", s.get("t")))
            except (TypeError, ValueError):
                continue
            if t > 1e-6:
                out.append(t)
        return out

    def cut_events(self) -> list[float]:
        """Seconds of the hard cuts in work/cutmap.json (segment joins: jump cuts are visible events too)."""
        out = []
        for seg in ((self.cutmap or {}).get("segments") or [])[1:]:
            try:
                out.append(float(seg.get("t0")))
            except (TypeError, ValueError, AttributeError):
                continue
        return out

    def grade_pulses(self) -> list[float]:
        """Seconds of the grade-event blur pulses (timeline.grades[] with `blur` > 0): a defocus pulse is a visible change
        of the whole picture (cinematic-list-montage lands its title on one)."""
        out = []
        for g in self.tl.get("grades") or []:
            if not isinstance(g, dict):
                continue
            try:
                t, px = float(g.get("t")), float(g.get("blur") or 0)
            except (TypeError, ValueError):
                continue
            if px > 0:
                out.append(t)
        return out

    def start_events(self) -> list[float]:
        """Seconds at which a scene, stage change, camera event (re-crops included), shot cut, cutmap jump cut or grade
        blur pulse *starts* (for on-the-word checks)."""
        return sorted([float(s.get("t_in", 0)) for s in self.scenes]
                      + [float(e.get("t", 0)) for e in self.stage]
                      + [float(e.get("t", 0)) for e in self.camera]
                      + self.shot_cuts()
                      + self.cut_events()
                      + self.internal_events()
                      + self.grade_pulses())

    # v3 helpers
    @property
    def schema(self) -> int:
        return int((self.style.get("_resolved") or {}).get("schema", 1))

    def presence(self) -> str:
        return str(get_path(self.style, "profile.presenter.presence", "anchor") or "anchor")


# --------------------------------------------------------------------------- V-TITLE (M4)
def read_words(read_s: float, per_word: float) -> int:
    """Words a headline may carry inside the style's read time. The budget is counted in whole words, rounded to the
    nearest word: a title at the limit passes (1.2 s at 0.25 s/word fits 5 words, it used to fail at "1.2 s vs 1.2 s")."""
    if per_word <= 0:
        return 10 ** 6
    return int(read_s / per_word + 0.5 + 1e-9)


def rule_title(c: Ctx, p: dict):
    legacy = bool(p.get("legacy"))
    if legacy:
        tb = c.style.get("type", {}).get("banner", {})
        kinds, noun = ("banner",), "banner"
        max_words, max_lines, max_emoji, chips_rule, read_s = tb.get("max_words", 9), tb.get("max_lines", 2), 2, "one_or_bad_good", None
    else:
        hd = (c.style.get("type") or {}).get("headline") or {}
        if hd.get("kind") == "none" and not p.get("kinds"):
            return []
        kinds, noun = tuple(p.get("kinds") or HEADLINE_KINDS), "headline"
        g = lambda k, d: p.get(k, hd.get(k, d))  # noqa: E731
        max_words, max_lines, max_emoji = g("max_words", 9), g("max_lines", 2), g("max_emoji", 2)
        chips_rule = g("chips", None)
        read_s = g("read_s", get_path(c.style, "hooks.stopper.read_s"))
    per_word = float((c.style.get("motion") or {}).get("text_hold_per_word_s", 0.25))
    out = []
    for s in c.of_kinds(kinds):
        t0 = s.get("t_in", 0)
        text = str(s.get("text_content", ""))
        chips = banner_chips(s)
        lines = s.get("lines")
        words, emoji = count_words_emoji(text)
        bid = c.beat_id(t0)
        if max_words is not None and words > max_words:
            out.append(fail("V-TITLE", bid, t0, f"{noun} {s.get('id')} has {words} words (max {max_words})",
                            f"shorten the {noun} to {max_words} words or fewer (emoji don't count)"))
        if max_lines is not None and isinstance(lines, (int, float)) and lines > max_lines:
            out.append(fail("V-TITLE", bid, t0, f"{noun} {s.get('id')} uses {int(lines)} lines (max {max_lines})",
                            f"rewrite the {noun} to fit on {max_lines} lines"))
        if chips_rule == "one_or_bad_good" and s.get("kind") == "banner":
            roles = sorted(str(r) for _, r in chips)
            if not (len(chips) == 1 or (len(chips) == 2 and roles == ["bad", "good"])):
                out.append(fail("V-TITLE", bid, t0, f"{noun} {s.get('id')} has {len(chips)} keyword chips (need exactly 1, "
                                "or 2 when one is role bad and the other good)",
                                "declare one CAPS keyword chip in the banner scene meta: chips: [{text, role}]"
                                if len(chips) != 2 else "give the two chips the roles bad and good, or keep only one chip"))
        if max_emoji is not None and emoji > max_emoji:
            out.append(fail("V-TITLE", bid, t0, f"{noun} {s.get('id')} has {emoji} emoji (max {max_emoji})",
                            f"keep at most {max_emoji} emoji in the {noun}"))
        if read_s and words > read_words(float(read_s), per_word):
            out.append(fail("V-TITLE", bid, t0, f"{noun} {s.get('id')} needs {words * per_word:.2f} s to read "
                            f"({words} words at {per_word:g} s each); the style's read time {read_s} s fits "
                            f"{read_words(float(read_s), per_word)} words",
                            f"cut the {noun} to {read_words(float(read_s), per_word)} words or fewer"))
    return out


# --------------------------------------------------------------------------- V-ONWORD (M6)
def _isint(v) -> bool:
    return isinstance(v, (int, float)) and not isinstance(v, bool) and float(v) == int(v)


def onword_leads(c: Ctx, lead_max: int) -> tuple[list[float], list[dict]]:
    """Declared early starts (`onword_lead` on a scene): the on-word times they stand for, plus failures for bad values.

    `onword_lead: 12` = the scene's start and every `events` time begin 12 frames before the word they belong to (a
    highlight box that starts tracing ~12 f early and closes on its word); `onword_lead: [{at: <local s>, frames: 12}]`
    = only those events (at 0 = the start). Not needed for a lead-in up to ONWORD_LEAD_IN_F (accepted by default);
    still accepted. Each lead must be a whole number of frames, 1..`onword_lead_max` (V-ONWORD param or
    motion.onword_lead_max when a style declares one, else ONWORD_LEAD_IN_F)."""
    times, out = [], []
    for s in c.scenes:
        spec = s.get("onword_lead")
        if spec is None:
            continue
        t_in = float(s.get("t_in", 0))
        starts = [0.0] + [float(v) for v in (s.get("events") or []) if isinstance(v, (int, float)) and not isinstance(v, bool)]
        if isinstance(spec, list):
            pairs = [(x.get("at"), x.get("frames")) if isinstance(x, dict) else (None, None) for x in spec]
        else:
            pairs = [(v, spec) for v in dict.fromkeys(starts)]
        mine = []
        for at, n in pairs:
            bad = None
            if not isinstance(at, (int, float)) or isinstance(at, bool) or not _isint(n) or int(n) < 1:
                bad = f"onword_lead must be a whole number of frames >= 1, or [{{at: local s, frames}}] (got {spec!r})"
            elif int(n) > lead_max:
                bad = f"declares onword_lead {int(n)} f, more than the style's onword_lead_max {lead_max} f"
            if bad:
                out.append(fail("V-ONWORD", c.beat_id(t_in), t_in, f"scene {s.get('id')} {bad}",
                                f"start {s.get('id')} at most {max(lead_max, 0)} f before its word, or drop onword_lead"))
                mine = []  # one message per scene; none of its declared leads count
                break
            mine.append(t_in + float(at) + int(n) / FPS)
        times += mine
    return times, out


def _shot_opens(c: Ctx, b: dict, at: float) -> bool:
    """A timeline.shots cut opens this beat (within 2 f of its t0) and comes before the trigger word: the re-cut's
    picture change for the beat (the master cut on the turn / sentence, before the beat's key word)."""
    t0 = float(b.get("t0", 0))
    return any(abs(fr(x) - fr(t0)) <= 2 and x <= at + 1e-6 for x in c.shot_cuts())


def _f0_opener(c: Ctx, b: dict, at: float) -> bool:
    """The hook archetype opens before speech (hookrules ARCHETYPES `before_speech`: HA-03, HA-14): frame 0 is the event
    of the first beat's trigger word, when that word is spoken by the archetype's payoff time and something is up at f0
    (a scene starting on frame 0, or the live footage)."""
    from .hookrules import ARCHETYPES, presenter_on
    ha = ARCHETYPES.get(archetype_of(c, {})) or {}
    if not ha.get("before_speech") or fr(b.get("t0", 0)) > 0 or at > float(ha["payoff"][1]) + 1e-6:
        return False
    return any(fr(s.get("t_in", 0)) == 0 and fr(s.get("t_out", 0)) > 0 for s in c.scenes) or presenter_on(c, 0)


ONWORD_LEAD_IN_F = 15  # a scene may start up to 15 f before its trigger word (a lead-in), by default


def rule_onword(c: Ctx, p: dict):
    """An event on every beat's trigger word. Accepted by default: an event from ONWORD_LEAD_IN_F frames before the word
    (a lead-in) to land_frames after it; a timeline.shots cut opening the beat; the f0 opener of a before-speech hook.
    Beyond the lead-in, nothing counts. (`onword_lead`, `onword_lead_max`, `shot_opens_beat` are accepted, not needed.)
    `legacy` (v1 M6) keeps the old window: lead_frames + 0.1 s, shot cuts only when declared."""
    legacy = bool(p.get("legacy"))
    out = []
    lead_f = p.get("lead_frames", c.style.get("motion", {}).get("lead_frames", 2))
    lead, land = lead_f / FPS, p.get("land_frames", 5) / FPS
    lead_max = p.get("onword_lead_max", (c.style.get("motion") or {}).get("onword_lead_max", ONWORD_LEAD_IN_F))
    lead_max = int(lead_max) if _isint(lead_max) and int(lead_max) > 0 else ONWORD_LEAD_IN_F
    early, out = onword_leads(c, lead_max)
    ev = c.start_events() + early
    for b in c.beats:
        trig = b.get("trigger") or {}
        if trig.get("at") is None:
            continue
        at = float(trig["at"])
        lo, hi = at - (lead + 0.1 if legacy else max(lead + 0.1, ONWORD_LEAD_IN_F / FPS)), at + land
        if any(lo - 1e-6 <= e <= hi + 1e-6 for e in ev):
            continue
        if ((not legacy or p.get("shot_opens_beat")) and _shot_opens(c, b, at)) or _f0_opener(c, b, at):
            continue
        near = min(ev, key=lambda e: abs(e - at)) if ev else None
        off = f"nearest event is {near - at:+.2f} s from the word" if near is not None else "no events at all"
        out.append(fail("V-ONWORD", b.get("id"), at,
                        f"nothing starts on the trigger word '{trig.get('word', '')}' at {at:.2f} s ({off})",
                        f"start the matching scene, scene event, stage change, camera move or shot cut between {lo:.2f} and {at + land:.2f} s "
                        f"(about {at - lead:.2f} s is ideal)"))
    return out


# --------------------------------------------------------------------------- V-SAFE / V-FACE (M12)
def _safe_box(c: Ctx, s: dict, legacy: bool):
    safe = c.layout.get("safe", {"x": [64, 1016], "y": [110, 1500]})
    x0, x1, y0, y1 = safe["x"][0], safe["x"][1], safe["y"][0], safe["y"][1]
    if s.get("kind") == "banner" and (legacy or "banner_x" in c.layout):
        bx, btop = c.layout.get("banner_x", [40, 1040]), c.layout.get("banner_top", 150) - 10
        x0, x1, y0 = bx[0], bx[1], btop
    if not legacy:
        lay = (c.style.get("layouts") or {}).get(c.stage_at(float(s.get("t_in", 0)))) or {}
        ls = lay.get("safe") if isinstance(lay, dict) else None
        if isinstance(ls, dict) and "x" in ls and "y" in ls:  # a layout may narrow the box, never widen it
            x0, x1, y0, y1 = max(x0, ls["x"][0]), min(x1, ls["x"][1]), max(y0, ls["y"][0]), min(y1, ls["y"][1])
        e5 = (c.style.get("exceptions") or {}).get("E5")
        if s.get("exception") == "E5" and e5:
            m = float(e5.get("min_margin", 24))
            x0, x1 = m, 1080 - m
    return x0, x1, y0, y1


def rule_safe(c: Ctx, p: dict):
    """Meaning text inside the safe box (measured union over the sampled frames, else the declared box); v3 also NC-5."""
    legacy = bool(p.get("legacy"))
    out = []
    for s in c.scenes:
        if not c.is_text(s) or (not legacy and s.get("text_class") == "TC-decorative"):
            continue
        bb = c.union_rect(s) if legacy else c.settled_rect(s, world=True)  # v3: the settled hold, not the entrance animation
        if bb is None:
            continue
        ins = s.get("text_inset", 0) or 0  # containers (cards) whose text sits inset from the edge
        if ins:
            bb = (bb[0] + ins, bb[1] + ins, bb[2] - ins, bb[3] - ins)
        x0, x1, y0, y1 = _safe_box(c, s, legacy)
        if bb[0] < x0 - 4 or bb[2] > x1 + 4 or bb[1] < y0 - 4 or bb[3] > y1 + 4:  # 4 px: rotation / AA slack
            out.append(fail("V-SAFE", c.beat_id(s.get("t_in", 0)), s.get("t_in", 0),
                            f"text scene {s.get('id')} rect {tuple(int(v) for v in bb)} leaves the safe zone "
                            f"x {x0}-{x1}, y {y0}-{y1}",
                            f"move or shrink {s.get('id')} so its content sits inside the safe zone"))
            continue
        if legacy:
            continue
        band = None
        if bb[1] < NC5["top"] - 4:
            band = f"the top {NC5['top']} px"
        elif bb[3] > NC5["bottom_y"] + 4:
            band = f"the bottom band (y > {NC5['bottom_y']})"
        elif bb[2] > NC5["right_x"] + 4 and bb[1] < NC5["right_y"][1] and bb[3] > NC5["right_y"][0]:
            band = f"the right button column (x > {NC5['right_x']}, y {NC5['right_y'][0]}-{NC5['right_y'][1]})"
        if band:
            out.append(fail("V-SAFE", c.beat_id(s.get("t_in", 0)), s.get("t_in", 0),
                            f"text scene {s.get('id')} rect {tuple(int(v) for v in bb)} enters {band} (NC-5 IG UI)",
                            f"move {s.get('id')} out of the Instagram UI band"))
    return out


FACE_EXEMPT_KINDS = END_CARD_KINDS + ("transition", "wash", "flash", "sweep", "light-pass")


def rule_face(c: Ctx, p: dict):
    """NC-1: nothing drawn in front of the speaker covers their face, judged where the face really is on screen
    (presenter.screen_face: card / pip / stack / split windows, the panel and `low` stages, the measured footage
    transform; frames where no face shows are skipped). Behind-the-speaker scenes, z < 5, z11 light passes,
    transitions and end cards never count. No clearance margin: a graphic may sit right next to the face."""
    if c.face is None or (not p.get("legacy") and c.presence() == "none"):
        return []
    from .presenter import screen_face
    out = []
    frames = sorted(c.measured) if c.measured else list(range(0, c.frames, SAMPLE_EVERY))
    seen = set()
    for n in frames:
        raw = c.face[n] if n < len(c.face) else None
        src = c.face_raw[n] if c.face_raw is not None and n < len(c.face_raw) else raw
        fb = screen_face(c, n, raw, src) if raw else None
        if fb is None:
            continue
        for s in c.scenes:
            if s.get("id") in seen or s.get("z", 0) < 5 or s.get("behind") or not c.active(s, n):
                continue
            if s.get("z", 0) >= 11 or s.get("kind") in FACE_EXEMPT_KINDS or s.get("transition"):
                continue
            bb = c.rect(s, n)
            if bb is not None and overlap(bb, fb):
                seen.add(s.get("id"))
                src_kind = "measured" if n in c.measured and s.get("id") in c.measured[n] else "declared"
                out.append(fail("V-FACE", c.beat_id(n / FPS), n / FPS,
                                f"scene {s.get('id')} covers the face from frame {n} ({src_kind} rect)",
                                f"move {s.get('id')} off the face, or put it behind the speaker (behind: true)"))
    return out


# --------------------------------------------------------------------------- V-CAMERA (N5-zoom)
def _scale_span(spec: dict) -> float:
    sc = spec.get("scale")
    if isinstance(sc, (list, tuple)) and len(sc) == 2:
        return abs(float(sc[1]) - float(sc[0]))
    return 0.0


# camera v2 (renderer/core.js camCheck mirrors these): per-event `p` over the preset's own fields
CAM_EASES = ("out", "in", "inOut", "linear", "expoInOut", "expoOut")
CAM_ORIGINS = ("face", "center", "device", "free_side")
CAM_CROPS = {"wide": 1.0, "mid": 1.18, "tight": 1.35}
LAND_MAX = 1.5  # a landing (settle-out to the base framing from a cut / f0) may start up to 1.5x away


def _isnum(v) -> bool:
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def _cam_opt(e: dict, spec: dict, k: str):
    pp = e.get("p") or {}
    if k == "crop" and e.get("crop") is not None and pp.get("crop") is None:
        return e["crop"]
    return pp[k] if pp.get(k) is not None else spec.get(k)


def _crop_scale(crop, spec: dict, style: dict):
    if _isnum(crop):
        return float(crop)
    lv = (spec.get("levels") or {}).get(crop) if isinstance(spec.get("levels"), dict) else None
    if lv is not None:
        return (float(lv[0]) + float(lv[1])) / 2 if isinstance(lv, list) and len(lv) == 2 else float(lv) if _isnum(lv) else None
    tc = style.get("camera_crops") or {}
    if _isnum(tc.get(crop)):
        return float(tc[crop])
    return CAM_CROPS.get(crop) if isinstance(crop, str) else None


def _camera_v2_errors(c: Ctx, e: dict, spec: dict, where_p: str) -> list[str]:
    nodes = {str(k) for k in (c.tl.get("canvas_nodes") or {})}
    for s in c.scenes:
        nodes |= {str(n.get("id")) for n in (s.get("nodes") or []) if isinstance(n, dict)}
    device = "device" in nodes or isinstance((c.style.get("layout") or {}).get("device"), dict)
    errs = []
    if e.get("crop") is not None:
        srcs = [("crop", {"crop": e["crop"]})]
    else:
        srcs = []
    srcs += [("p", e.get("p") or {}), (where_p, spec)]
    for w, o in srcs:
        if not isinstance(o, dict):
            continue
        if o.get("ease") is not None and o["ease"] not in CAM_EASES:
            errs.append(f"{w}.ease '{o['ease']}' is not one of {' | '.join(CAM_EASES)}")
        for k in ("origin", "toward"):
            v = o.get(k)
            if v is None:
                continue
            if isinstance(v, str):
                if v not in CAM_ORIGINS:
                    errs.append(f"{w}.{k} '{v}' is not one of {' | '.join(CAM_ORIGINS)} or {{x, y}} / {{node}}")
                elif v == "device" and not device:
                    errs.append(f"{w}.{k} 'device' needs a node 'device' (a scene's nodes or timeline.canvas_nodes) "
                                "or tokens.layout.device {x, y}")
            elif not (isinstance(v, dict) and ((_isnum(v.get("x")) and _isnum(v.get("y")))
                                               or (v.get("node") is not None and str(v["node"]) in nodes))):
                errs.append(f"{w}.{k} must be face | center | device | free_side, {{x, y}} screen px, or {{node: id}} of a known node")
        if o.get("target") is not None and o["target"] not in ("footage", "all"):
            errs.append(f"{w}.target '{o['target']}' is not footage | all")
        if o.get("crop") is not None and (_crop_scale(o["crop"], spec, c.style) or 0) <= 0:
            errs.append(f"{w}.crop '{o['crop']}' is not wide | mid | tight (or a scale)")
        if o.get("from") is not None and o["from"] != "inherit" and not (_isnum(o["from"]) and o["from"] > 0):
            errs.append(f'{w}.from must be "inherit" or a scale > 0')
        if o.get("from_rotate") is not None and not _isnum(o["from_rotate"]):
            errs.append(f"{w}.from_rotate must be degrees")
        rot = o.get("rotate")
        if rot is not None and not (_isnum(rot) or (isinstance(rot, list) and len(rot) == 2 and all(_isnum(x) for x in rot))):
            errs.append(f"{w}.rotate must be degrees or [from, to]")
        fw = o.get("from_wide")
        if fw is not None and not (isinstance(fw, bool) or (_isnum(fw) and 0 < fw <= 1)):
            errs.append(f"{w}.from_wide must be true or a scale 0..1")
        ld = o.get("land")
        if ld is not None and not (isinstance(ld, bool) or (_isnum(ld) and ld > 0)):
            errs.append(f"{w}.land must be true or the start scale")
    return errs


def _cut_frames(c: Ctx) -> list[int]:
    cuts = [fr(x.get("t", 0)) for x in c.transitions + c.stage]
    cuts += [fr(seg.get("t0", 0)) for seg in ((c.cutmap or {}).get("segments") or [])]
    for s in c.scenes:
        cuts += [fr(float(s.get("t_in", 0)) + float(v)) for v in (s.get("cuts") or []) if isinstance(v, (int, float))]
    return cuts


def _camera_spans(c: Ctx, presets: dict) -> dict[int, tuple[float, float, bool]]:
    """Per camera event index: (from scale, to scale, uses v2 scale fields), simulating the chain like core camEval
    (the camera resets at stage changes; hold / reset / zoom-through return to 1). from_wide: true counts as 1/1.5."""
    stage_f = sorted(fr(x.get("t", 0)) for x in c.stage)
    out, cur, last_stage = {}, 1.0, None
    for i, e in enumerate(c.camera):
        pr = e.get("preset")
        if pr == "shake":
            continue
        f = fr(e.get("t", 0))
        st0 = max([k for k in stage_f if k <= f], default=0)
        if st0 != last_stage:
            cur, last_stage = 1.0, st0
        spec = presets.get(pr) or {}
        pp = e.get("p") or {}
        if pr == "reset":
            out[i] = (cur, 1.0, False)
            cur = 1.0
            continue
        sc = spec.get("scale") if isinstance(spec.get("scale"), list) and len(spec["scale"]) == 2 else [1, 1]
        frm = cur if float(sc[0]) == 1 else float(sc[0])
        to = float(pp["scale"]) if _isnum(pp.get("scale")) else float(sc[1])
        v2 = False
        crop = _cam_opt(e, spec, "crop")
        if crop is not None and not _isnum(pp.get("scale")):
            to, v2 = (_crop_scale(crop, spec, c.style) or to), True
        f_ = _cam_opt(e, spec, "from")
        if f_ == "inherit":
            frm, v2 = cur, True
        elif _isnum(f_):
            frm, v2 = float(f_), True
        ld = _cam_opt(e, spec, "land")
        if _isnum(ld) and not isinstance(ld, bool):
            frm, v2 = float(ld), True
            if not _isnum(pp.get("scale")):
                to = 1.0
        fw = _cam_opt(e, spec, "from_wide")
        if fw:
            frm, v2 = (1 / LAND_MAX if fw is True else max(1 / LAND_MAX, float(fw))), True
        out[i] = (frm, to, v2)
        holds = pp.get("hold") is not None or spec.get("hold_frames") is not None or pr == "zoom-through"
        cur = 1.0 if holds else to
    return out


def rule_camera(c: Ctx, p: dict):
    legacy = bool(p.get("legacy"))
    out, prev = [], None
    presets = c.style.get("camera_presets", {})
    if not legacy:
        policy = p.get("zoom_policy", c.style.get("zoom_policy", "presets")) or "presets"
        zooms = [e for e in c.camera if e.get("preset") != "shake"]
        for e in c.camera:
            if e.get("preset") is None and e.get("crop", (e.get("p") or {}).get("crop")) is not None:
                pass  # camera v2: a preset-less crop on a cut
            elif e.get("preset") not in presets and e.get("preset") != "shake":
                out.append(fail("V-CAMERA", c.beat_id(e.get("t", 0)), e.get("t", 0),
                                f"camera preset '{e.get('preset')}' is not defined in this style's camera_presets",
                                f"use one of: {', '.join(presets) or '(none: this style has no camera moves)'}"))
        if policy in ("none", "source_only") and zooms:
            e = zooms[0]
            out.append(fail("V-CAMERA", c.beat_id(e.get("t", 0)), e.get("t", 0),
                            f"{len(zooms)} camera move(s) but the style's zoom policy is '{policy}' (no engine zooms)",
                            "remove the camera events" + (" (zoom only inside the source footage)" if policy == "source_only" else "")))
        for e in c.camera:  # camera v2 fields (ease, origin, crop, from, rotate, land, target): reject bad values
            if e.get("preset") == "shake":
                continue
            for m in _camera_v2_errors(c, e, presets.get(e.get("preset")) or {}, f"camera_presets.{e.get('preset')}"):
                out.append(fail("V-CAMERA", c.beat_id(e.get("t", 0)), e.get("t", 0),
                                f"camera event at {e.get('t', 0):.2f} s: {m}", "fix the value (renderer/SCENES-API.md section 4c)"))
        if policy == "slow_push":
            spans = _camera_spans(c, presets)
            cuts = set(_cut_frames(c)) | {0}
            for i, e in enumerate(c.camera):
                if e.get("preset") == "shake":
                    continue
                spec = presets.get(e.get("preset")) or {}
                fr_ = spec.get("frames")
                frm, to, v2 = spans.get(i, (1.0, 1.0, False))
                span = abs(to - frm) if v2 else _scale_span(spec)
                if not (span > 0.12 or (isinstance(fr_, (int, float)) and fr_ < 15)):
                    continue
                land = _cam_opt(e, spec, "land") or _cam_opt(e, spec, "from_wide")
                if land:  # the landing exemption: an eased settle to the base framing that starts on a cut / f0, <= 1.5x
                    on_cut = any(abs(fr(e.get("t", 0)) - k) <= 2 for k in cuts)
                    ratio = max(frm, to) / max(min(frm, to), 1e-6)
                    if on_cut and abs(to - 1) <= 0.005 and ratio <= LAND_MAX + 1e-9:
                        continue
                    why = ("it does not start on a cut or f0" if not on_cut else
                           f"it ends at {to:.2f}, not on the base framing (1.0)" if abs(to - 1) > 0.005 else
                           f"it starts {ratio:.2f}x away (max {LAND_MAX}x)")
                    out.append(fail("V-CAMERA", c.beat_id(e.get("t", 0)), e.get("t", 0),
                                    f"camera landing '{e.get('preset')}' at {e.get('t', 0):.2f} s is not exempt under slow_push: {why}",
                                    "start the landing on a cut (or f0), settle to scale 1.0, from at most 1.5x"))
                    continue
                out.append(fail("V-CAMERA", c.beat_id(e.get("t", 0)), e.get("t", 0),
                                f"camera preset '{e.get('preset')}' is a punch, but the zoom policy is slow_push",
                                "use a slow push (scale change <= 0.12 over a beat), or a landing (p.land) on a cut"))
        elif policy == "crop_on_cut":
            cuts = _cut_frames(c)
            for e in zooms:
                if not any(abs(fr(e.get("t", 0)) - k) <= 2 for k in cuts):
                    out.append(fail("V-CAMERA", c.beat_id(e.get("t", 0)), e.get("t", 0),
                                    f"camera change at {e.get('t', 0):.2f} s is not on a cut (zoom policy crop_on_cut)",
                                    "move the crop change onto a cut (within 2 frames)"))
        if policy in ("none", "source_only"):
            return out
    for e in c.camera:
        pr = e.get("preset")
        if pr == "shake" or pr is None:  # a preset-less crop is a re-crop on a cut, not a move
            continue
        if prev is not None and pr == prev:
            out.append(fail("V-CAMERA", c.beat_id(e.get("t", 0)), e.get("t", 0),
                            f"camera preset '{pr}' is used twice in a row",
                            f"change the camera move at {e.get('t', 0):.2f} s to a different preset (or remove it)"))
        prev = pr
    counts: dict[str, int] = {}
    for e in c.camera:
        counts[e.get("preset")] = counts.get(e.get("preset"), 0) + 1
    for pr, n in counts.items():
        mx = (presets.get(pr) or {}).get("max_per_reel")
        if mx and n > mx:
            out.append(fail("V-CAMERA", None, 0, f"camera preset '{pr}' is used {n} times (max {mx} per reel)",
                            f"remove {n - mx} use(s) of '{pr}'"))
    return out


# --------------------------------------------------------------------------- V-HUES (N6)
def rule_hues(c: Ctx, p: dict):
    out = []
    legacy = bool(p.get("legacy"))
    mx = p.get("max_bright_per_frame", c.style.get("max_bright_per_frame", 3))
    if not legacy:
        mx = min(int(mx), 4)  # NC-10
    non_bright = set(NON_BRIGHT) | {r for r, v in (c.style.get("roles") or {}).items()
                                    if isinstance(v, dict) and v.get("bright") is False}
    flagged = False
    for n in range(0, c.frames, SAMPLE_EVERY):
        bright = set()
        for s in c.scenes:
            if c.active(s, n) and s.get("z", 0) < 11:  # z 11 = momentary light passes (sweep, flash), not a hue element
                bright |= c.roles(s) - non_bright
        if len(bright) > mx and not flagged:
            flagged = True
            out.append(fail("V-HUES", c.beat_id(n / FPS), n / FPS,
                            f"{len(bright)} bright colours at once from frame {n}: {', '.join(sorted(bright))} (max {mx})",
                            f"recolour or remove scenes around {n / FPS:.1f} s so only {mx} bright roles show together"))
    for s in c.scenes:
        if "comedy" in c.roles(s):
            bad = [b for b in c.scene_beats(s) if b.get("tone") != "mock"]
            if bad:
                out.append(fail("V-HUES", bad[0].get("id"), s.get("t_in", 0),
                                f"comedy colour on scene {s.get('id')} in a '{bad[0].get('tone')}' beat",
                                f"use the beat's own colour role for {s.get('id')}, or move it to a mock beat"))
    return out


# --------------------------------------------------------------------------- V-LEDGER (M10)
def rule_ledger(c: Ctx, p: dict):
    out = []
    mx = p.get("sfx_max_uses_per_file", c.budgets.get("sfx_max_uses_per_file", 2))
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
            out.append(fail("V-LEDGER", us[mx].get("beat"), us[mx].get("t", 0),
                            f"{f} is used {len(us)} times (max {mx}; {why})",
                            f"replace the use at {us[mx].get('t', 0):.2f} s (and any later ones) with another file from the same pool"))
        if any(u.get("role") == "meme" for u in us) and len(us) > 1:
            out.append(fail("V-LEDGER", us[1].get("beat"), us[1].get("t", 0), f"meme file {f} is used {len(us)} times (once only)",
                            "use a different meme file for the repeat"))
    for a, b in zip(c.legacy_sfx, c.legacy_sfx[1:]):
        if a.get("file") == b.get("file"):
            out.append(fail("V-LEDGER", b.get("beat"), b.get("t", 0), f"{b.get('file')} is on two consecutive cues",
                            f"swap the cue at {b.get('t', 0):.2f} s for a different file in the same pool"))
    return out


# --------------------------------------------------------------------------- V-COMEDY (M9)
def _comedy_m9(c: Ctx, p: dict):
    out = []
    mx = p.get("meme_max_per_reel", c.budgets.get("meme_max_per_reel", 4))
    gap = p.get("meme_min_gap_s", c.budgets.get("meme_min_gap_s", 4))
    memes = [s for s in c.legacy_sfx if s.get("role") == "meme"]
    wins = 0
    for s in memes:
        b = next((x for x in c.beats if x.get("id") == s.get("beat")), None) or c.beat_at(s.get("t", 0))
        tone = b.get("tone") if b else None
        if tone == "win" and wins == 0:
            wins += 1
        elif tone != "mock":
            out.append(fail("V-COMEDY", b.get("id") if b else None, s.get("t", 0),
                            f"meme sound {s.get('file')} sits on a '{tone}' beat (mock only; one win allowed)",
                            f"remove the meme sound at {s.get('t', 0):.2f} s or move it to a mock beat"))
    if len(memes) > mx:
        out.append(fail("V-COMEDY", memes[mx].get("beat"), memes[mx].get("t", 0), f"{len(memes)} meme sounds (max {mx})",
                        f"remove {len(memes) - mx} meme sound(s)"))
    for a, b in zip(memes, memes[1:]):
        if b.get("t", 0) - a.get("t", 0) < gap - 1e-6:
            out.append(fail("V-COMEDY", b.get("beat"), b.get("t", 0),
                            f"meme sounds at {a.get('t', 0):.1f} s and {b.get('t', 0):.1f} s are under {gap} s apart",
                            f"move or remove the meme sound at {b.get('t', 0):.2f} s so memes are at least {gap} s apart"))
    for s in c.scenes:
        if s.get("kind") == "meme" and "comedy" in c.roles(s):  # meme visuals (stamps, stickers) are mock-beat only
            bad = [b for b in c.scene_beats(s) if b.get("tone") != "mock"]
            if bad:
                out.append(fail("V-COMEDY", bad[0].get("id"), s.get("t_in", 0),
                                f"meme scene {s.get('id')} is on a '{bad[0].get('tone')}' beat",
                                f"remove {s.get('id')} or move it to a mock beat"))
    return out


def rule_comedy(c: Ctx, p: dict):
    if p.get("legacy"):
        return _comedy_m9(c, p)
    comedy = p.get("comedy", get_path(c.style, "profile.tone.comedy", "off"))
    if comedy == "roast":
        return _comedy_m9(c, p)
    out = []
    for s in c.legacy_sfx:
        if s.get("role") == "meme":
            out.append(fail("V-COMEDY", s.get("beat"), s.get("t", 0),
                            f"meme sound {s.get('file')}: this style's comedy is '{comedy}' (meme sounds need roast)",
                            f"remove the meme sound at {s.get('t', 0):.2f} s"))
    if comedy == "off":
        for s in c.scenes:
            if s.get("kind") == "meme":
                out.append(fail("V-COMEDY", c.beat_id(s.get("t_in", 0)), s.get("t_in", 0),
                                f"meme scene {s.get('id')}: this style has no comedy layer (tone.comedy off)",
                                f"remove {s.get('id')}"))
    return out


# --------------------------------------------------------------------------- V-PROMISE (M13)
def rule_promise(c: Ctx, p: dict):
    """The reel keeps its promise: the planner's `meta.count` (the number the hook promises) equals the ITEM
    sections (blocks). The CTA keyword on screen and the end-card length are advice."""
    legacy = bool(p.get("legacy"))
    out = []
    items = len(c.item_numbers())
    try:
        count = int(c.meta.get("count")) if c.meta.get("count") is not None else None
    except (TypeError, ValueError):
        count = None
    if count is not None and items > 0 and count != items:
        out.append(fail("V-PROMISE", None, 0, f"the hook promises {count} but the beats show {items} item section(s)",
                        f"make the number of ITEM sections equal {count}, or set meta.count to {items} and say so"))
    kw = c.meta.get("keyword")
    devices = set(get_path(c.style, "profile.cta.devices", []) or [])
    if kw and (legacy or not devices or devices & KEYWORD_DEVICES):
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
            out.append(advice(fail("V-PROMISE", c.beat_id(t), t, f"the CTA keyword '{kw}' is never on screen in the CTA section",
                                   f"consider a scene with kind 'cta-keyword' showing '{kw}' during the CTA section")))
    if not legacy:
        mx = p.get("endcard_max_s", get_path(c.style, "brand.endcard.max_s"))
        for s in c.of_kinds(END_CARD_KINDS):
            d = float(s.get("t_out", 0)) - float(s.get("t_in", 0))
            if mx is not None and d > float(mx) + 1e-6:
                out.append(advice(fail("V-PROMISE", c.beat_id(s.get("t_in", 0)), s.get("t_in", 0),
                                       f"end card {s.get('id')} holds {d:.1f} s (the style suggests {mx} s)",
                                       f"consider shortening {s.get('id')} to about {mx} s")))
    return out


# --------------------------------------------------------------------------- registry v2
REGISTRY: dict[str, Callable[[Ctx, dict], list]] = {
    "V-PROFILE": rule_profile, "V-F0": rule_f0, "V-CADENCE": rule_cadence, "V-TITLE": rule_title,
    "V-ONWORD": rule_onword, "V-SAFE": rule_safe, "V-FACE": rule_face, "V-PRESENCE": rule_presence,
    "V-CAMERA": rule_camera, "V-HUES": rule_hues, "V-LEDGER": rule_ledger, "V-COMEDY": rule_comedy,
    "V-PROMISE": rule_promise, "V-TYPE": rule_type, "V-EXC": rule_exc, "V-CAPTION": rule_caption, "V-LAYOUT": rule_layout,
    "V-DATA": rule_data, "V-NUMFMT": rule_numfmt, "V-THEME": rule_theme, "V-REHOOK": rule_rehook,
    "V-INSERTS": rule_inserts, "V-CITE": rule_cite,
}
# registry ids that later engine waves build (ENGINE-IMPLICATIONS §2): accepted in tokens, reported as pending
from .dialoguerules import RULES as _DIALOGUE_RULES  # V-SPEAKER (E-13)
REGISTRY.update(_DIALOGUE_RULES)
PENDING = {"V-CHROME": "E-07",
           "V-STATE": "E-09", "V-CONTINUITY": "E-19",
           "V-GRADE": "E-16"}
# built rules that run from their own hook in main() whenever the plan uses the feature (not from the registry), so a
# playbook listing them is neither pending nor unknown: V-CANVAS (timeline.canvas_camera), V-FX (built-in transitions,
# blur, end fade), V-ANCHOR (a scene `anchor`), V-DEPICT / V-POINT (every reel: advice, depictrules.py). V-FLASH is
# retired (no flash limit) but stays accepted in old registries.
HOOKED = ("V-CANVAS", "V-FX", "V-FLASH", "V-ANCHOR", "V-PLAN", "V-CUTOUT", "V-DEPICT", "V-POINT")
# rules a v3 style switches off by its profile
OFF_BY_PRESENCE_NONE = ("V-PRESENCE", "V-FACE")
# never-bendable core (structure C.1 NC-4 legibility; C.3 the exception registry): run for every playbook, even when the
# playbook's registry omits them (v1 files included) or switches them off
ALWAYS_ON = ("V-TYPE", "V-EXC", "V-INSERTS", "V-CITE")  # + NC-7 / NC-13 (E-10): no-ops without inserts or sources
RULES = REGISTRY  # back-compat name
# the rules whose findings are facts and block the reel; every other rule (and any finding marked advice) is advice
BLOCKING = frozenset({"G1", "G3", "V-FACE", "V-TYPE", "V-DATA", "V-INSERTS", "V-CITE", "V-PROMISE", "V-PLAN", "V-FX",
                      "S6", "V-ANCHOR", "V-CUTOUT"})


def is_advice(f: dict) -> bool:
    return bool(f.get("advice")) or f.get("rule") not in BLOCKING


def split_levels(found: list[dict]) -> tuple[list[dict], list[dict]]:
    """(failures, advice) from every finding; the `advice` marker is dropped so both lists share one shape."""
    fails, adv = [], []
    for f in found:
        (adv if is_advice(f) else fails).append(f)
        f.pop("advice", None)
    return fails, adv


def plan_rules(style: dict, warnings: list) -> tuple[list[tuple[str, dict, str | None]], dict]:
    """[(V-id, params, playbook_rule)] in run order, plus {pending, off, unknown, aliases}."""
    from .tokens import V1_RULE_MAP
    val = style.get("validator") or {}
    rules = val.get("rules") or {}
    aliases = dict(val.get("aliases") or {})
    cites: dict[str, list[str]] = {}
    for h, vid in (val.get("cites") or {}).items():
        cites.setdefault(str(vid), []).append(str(h))
    if not rules:  # a v3 file without a registry: every built rule with its token params
        rules = {vid: True for vid in REGISTRY}
    plan, info = [], {"pending": [], "off": [], "unknown": [], "aliases": {}}
    presence_none = get_path(style, "profile.presenter.presence") == "none"
    for rid, spec in rules.items():
        vids = [rid]
        if rid in V1_RULE_MAP:  # an M-id inside a v3 registry: run its V-ids, cite the M-id
            vids = list(V1_RULE_MAP[rid])
            for v in vids:
                aliases.setdefault(v, rid)
        for vid in vids:
            if spec in (False, None):
                info["off"].append(vid)
                continue
            if presence_none and vid in OFF_BY_PRESENCE_NONE:
                info["off"].append(vid)
                continue
            params = dict(spec) if isinstance(spec, dict) else {}
            if vid not in REGISTRY:
                if vid in HOOKED:
                    continue
                if vid in PENDING:
                    info["pending"].append(vid)
                else:
                    info["unknown"].append(vid)
                    warnings.append(f"rule {vid} is enabled in the playbook but not implemented")
                continue
            pr = params.pop("playbook_rule", None) or aliases.get(vid) or ("/".join(cites[vid]) if vid in cites else None)
            if pr:
                info["aliases"][vid] = pr
            plan.append((vid, params, pr))
    planned = {v for v, _, _ in plan}
    for vid in ALWAYS_ON:
        if vid in planned:
            continue
        if vid in info["off"]:
            info["off"].remove(vid)
            warnings.append(f"{vid} cannot be switched off (non-overridable core NC-4 / exception registry); it runs")
        pr = aliases.get(vid) or ("/".join(cites[vid]) if vid in cites else None)
        if pr:
            info["aliases"][vid] = pr
        plan.append((vid, {}, pr))
    if info["pending"]:
        warnings.append("rules not built yet (later engine waves): " +
                        ", ".join(f"{v} ({PENDING[v]})" for v in info["pending"]))
    return plan, info


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


def _load_text_measure(proj, warnings: list) -> tuple[dict | None, list | None]:
    """plan/measure.text.json frames keyed by int (None when missing) and the raw work/captions.json chunks."""
    tm = None
    tp = proj.root / "plan" / "measure.text.json"
    if tp.exists():
        d = _load_optional(tp, "plan/measure.text.json", warnings)
        if isinstance(d, dict):
            tm = {}
            for k, v in (d.get("frames") or {}).items():
                try:
                    tm[int(k)] = v if isinstance(v, dict) else {}
                except ValueError:
                    continue
            sj = proj.root / "plan" / "scenes.js"
            if sj.exists() and tp.stat().st_mtime < sj.stat().st_mtime:
                warnings.append("plan/measure.text.json is older than plan/scenes.js; re-run `veos measure` for current text sizes")
    raw = None
    cp = proj.work / "captions.json"
    if cp.exists():
        try:
            d = read_json(cp)
            ch = d.get("chunks") if isinstance(d, dict) else d
            raw = [x for x in ch or [] if isinstance(x, dict)]
        except (ValueError, AttributeError):
            raw = None
    return tm, raw


def load_style(proj, tl: dict, warnings: list) -> dict:
    """The playbook resolved for this reel (tokens.effective_style); invalid v3 tokens raise BAD_TOKENS."""
    from .tokens import effective_style, load_playbook, project_playbook, schema_version
    meta = tl.get("meta") or {}
    raw = load_playbook(project_playbook(proj, None, meta))
    override = None
    op = proj.root / "plan" / "tokens.override.json"
    if schema_version(raw) == 3 and op.exists():
        override = _load_optional(op, "plan/tokens.override.json", warnings)
    errors: list[str] = []
    style = effective_style(raw, fmt=meta.get("format"), theme=meta.get("theme"), override=override,
                            warnings=warnings, errors=errors)
    if errors:
        raise VeosError("BAD_TOKENS", "playbook tokens are invalid: " + "; ".join(errors),
                        "Fix the listed keys in tokens.json (see playbooks/_styles/tokens.schema.md).")
    return style


def run_rules(ctx: Ctx, warnings: list) -> tuple[list[dict], list[str], dict]:
    plan, info = plan_rules(ctx.style, warnings)
    failures: list[dict] = []
    for vid, params, pr in plan:
        for f in REGISTRY[vid](ctx, params):
            if pr:
                f["playbook_rule"] = pr
            failures.append(f)
    return failures, [v for v, _, _ in plan], info


def main(args, project):
    from .scenes import load_scenes_meta
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
    style = load_style(proj, tl, warnings)
    plan_mode = bool(getattr(args, "plan", False))
    planned = sceneplan.load_plan(proj) if plan_mode or sceneplan.has_plan(proj) else None
    try:
        scenes = planned if plan_mode else load_scenes_meta(proj)
    except VeosError as e:
        # "silence of graphics": a style whose graphics profile is passthrough (or none) may draw nothing at all
        if e.code != "NO_SCENES" or str(get_path(style, "profile.graphics") or "") not in NO_GRAPHICS:
            raise
        scenes = []
        warnings.append(f"no scenes (plan/scenes.js registers none or is absent): allowed, the style's graphics "
                        f"profile is {get_path(style, 'profile.graphics')}")
    presence_none = get_path(style, "profile.presenter.presence") == "none"

    tokens = _load_optional(proj.work / "tokens.json", "work/tokens.json", warnings) if (proj.work / "tokens.json").exists() else None
    words = _load_optional(proj.work / "words.edit.json", "work/words.edit.json", warnings) if (proj.work / "words.edit.json").exists() else None
    face = face_raw = rf_reel = None
    if presence_none:
        warnings.append("profile.presenter.presence is none: face and presence rules are off")
    else:
        fpath = proj.abs((tl.get("inputs") or {}).get("face") or "work/face.edit.json")
        fdata = _load_optional(fpath, "work/face.edit.json", warnings, "face rules skipped")
        if fdata is not None:
            face = fdata.get("boxes") if isinstance(fdata, dict) else fdata
            if not isinstance(face, list):
                warnings.append("face file has no `boxes` list; face rules skipped")
                face = None
            elif tokens:  # E-16b: the face where the base reframe puts it on a full stage
                from .framing import apply_boxes, for_reel
                face_raw = face
                rf_reel = for_reel(tokens, tl, face)
                face = apply_boxes(face, rf_reel)

    measure = None
    mp = proj.root / "plan" / "measure.json"
    if plan_mode:  # no code yet: the declared boxes stand in for measured rects; G3 and text sizes wait for the code
        measure = sceneplan.declared_measure(scenes, int((tl.get("meta") or {}).get("frames") or 0))
        warnings.append("plan check: judged on the declared boxes; G3 smooth motion, measured text sizes and the "
                        "overlap with the subtitles are checked after the code (plain `veos validate`)")
    elif mp.exists():
        measure = _load_optional(mp, "plan/measure.json", warnings)
        sj = proj.root / "plan" / "scenes.js"
        if measure and sj.exists() and mp.stat().st_mtime < sj.stat().st_mtime:
            warnings.append("plan/measure.json is older than plan/scenes.js; re-run `veos measure` for real rects")
    else:
        warnings.append("plan/measure.json not found; using declared scene boxes (run `veos measure` for real positions)")

    if not plan_mode:
        measure = _with_motion(proj, tl, scenes, measure, warnings, getattr(args, "skip_motion", False))
    ctx = Ctx(tl, style, tokens, words, face, scenes, measure, warnings)
    ctx.face_raw = face_raw  # footage-space boxes: the card / pip / stack windows and the measured transform start from them
    ctx.framing = rf_reel  # E-16b base reframe record: its ranges also frame card / pip / stack windows (presenter.win_framing)
    ctx.text_measure, ctx.caption_raw = _load_text_measure(proj, warnings)
    if plan_mode:
        ctx.text_measure = None
    ctx.project = proj  # V-CAPTION reads work/captions.json
    cm = proj.work / "cutmap.json"
    if cm.exists():
        try:
            ctx.cutmap = read_json(cm)
        except ValueError:
            warnings.append("work/cutmap.json is not valid JSON; cuts not counted for cadence")
    ctx.caption_chunks, ctx.caption_source = load_caption_chunks(proj, tl, style, words, warnings)
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
    failures, ran, info = run_rules(ctx, warnings)
    gstats = {}
    for gid, fn in GLOBAL_CHECKS.items():
        got = fn(ctx)
        gstats[gid] = len(got)
        failures.extend(got)
    failures.extend(sfx_failures)
    # --- E-14 hook (feat/faceless): V-CANVAS runs when the timeline has canvas-camera moves. Foundation: register
    # veos.canvascam.rule_v_canvas in the V-rule registry (signature rule(ctx) -> [failure]) and drop this block.
    if tl.get("canvas_camera"):
        from .canvascam import rule_v_canvas
        gstats["V-CANVAS"] = len(vc := rule_v_canvas(ctx))
        failures.extend(vc)
    # --- end E-14 hook
    # footage blur / built-in transitions / blur pulses / end fade (Package A): V-FX + V-FLASH (NC-11), only when used
    from .fxrules import rule_fx, uses_fx
    if uses_fx(tl, style):
        gstats["V-FX"] = len(fxf := rule_fx(ctx))
        failures.extend(fxf)
    # --- Package E: V-ANCHOR runs when a scene follows a track (anchors.rule_v_anchor)
    if any(isinstance(s.get("anchor"), dict) for s in scenes):
        from .anchors import rule_v_anchor
        gstats["V-ANCHOR"] = len(va := rule_v_anchor(ctx))
        failures.extend(va)
    # the scene plan (sceneplan.py): complete before the code, and the code true to it after
    if plan_mode:
        bp = proj.path(*sceneplan.BRIEFS_FILE)
        briefs = bp.read_text(encoding="utf-8") if bp.exists() else None
        gstats["V-PLAN"] = len(vp := sceneplan.plan_checks(tl, scenes, briefs, ctx.duration))
        failures.extend(vp)
    elif planned is not None:
        gstats["V-PLAN"] = len(vp := sceneplan.fidelity(tl, planned, scenes))
        failures.extend(vp)
    # the person cut-out (cutout.py): drawn only where a scene sits behind the presenter or the head breaks out
    from .cutout import FIX as CUT_FIX, cutout_ready, needs_cutout
    need = needs_cutout(proj, scenes, tl)
    vc: list[dict] = []
    t_cut = need["frames"][0][0] / FPS if need["frames"] else 0
    if need.get("unavailable"):
        vc.append(fail("V-CUTOUT", ctx.beat_id(t_cut), t_cut, "; ".join(need["why"]),
                       "Plan those scenes in front of the speakers (no `behind`, no `breakout`)."))
    elif need["needed"] and plan_mode:
        warnings.append("this plan needs the person cut-out (" + "; ".join(need["why"]) + "): before the scenes are built, "
                        + CUT_FIX[0].lower() + CUT_FIX[1:])
    elif need["needed"]:
        vc = [fail("V-CUTOUT", ctx.beat_id(t_cut), t_cut,
                   f"this reel draws the person cut-out ({'; '.join(need['why'])}), but {m}", CUT_FIX)
              for m in cutout_ready(proj, need, tl)]
    if need["needed"] or need.get("unavailable"):
        gstats["V-CUTOUT"] = len(vc)
        failures.extend(vc)
    # show the thing, not the word (depictrules.py): text-only beats and unshown pointing moments, advice only
    # (counts in stats.depict: text_only_beats, pointers, pointers_shown)
    from .depictrules import rule_depict, rule_point
    failures.extend(rule_depict(ctx) + rule_point(ctx))
    failures.sort(key=lambda f: (f["t"], f["rule"]))
    failures, adv = split_levels(failures)

    if "cadence" not in ctx.stats_extra:  # informational even when V-CADENCE is off or legacy
        ctx.stats_extra["cadence"] = cadence_measure(ctx, params_from_tokens(ctx, {}))["stats"]
    ev = ctx.visual_events()
    res = style.get("_resolved") or {}
    stats = {
        "beats": len(ctx.beats), "scenes": len(ctx.scenes), "duration_s": round(ctx.duration, 3),
        "visual_events": len(ev) - 2 if len(ev) > 2 else 0,
        "events_per_s": round(max(len(ev) - 2, 0) / ctx.duration, 2) if ctx.duration else 0,
        "camera_events": len(ctx.camera), "sfx_cues": len(ctx.sfx), "sfx_rules": len(sfx_failures),
        "rules_run": ran, "rule_aliases": info["aliases"], "rules_pending": info["pending"], "rules_off": info["off"],
        "global_checks": gstats, "measured_frames": len(ctx.measured),
        "face_checked": face is not None, "measured": bool(ctx.measured), "words_loaded": words is not None,
        "tokens_loaded": tokens is not None,
        "style": {"schema": res.get("schema", 1), "format": res.get("format"), "theme": res.get("theme"),
                  "hook_archetype": archetype_of(ctx, {}), "presence": ctx.presence()},
        **ctx.stats_extra,
    }
    stats["advice"] = len(adv)
    result = {"ok": True, "passed": not failures, "failures": failures, "advice": adv, "warnings": warnings, "stats": stats}
    if plan_mode:
        result["mode"] = "plan"
    write_json(proj.path("plan", "validate.plan.json" if plan_mode else "validate.json"), result)
    return result
