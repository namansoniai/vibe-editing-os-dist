"""The scene plan: every decision about a reel's scenes, made by the planner before any scene code exists.

The planner (Opus) decides; the scene coder (a Sonnet agent) only turns the decisions into plan/scenes.js. Two files carry
the decisions:

  plan/scenes.plan.json   a JSON list, one entry per scene, in the shape `veos scenes-meta` writes for the registered
                          scenes (plan/scenes.meta.json): id, t_in, t_out, z, behind, kind, in / out (+ in_frames /
                          out_frames), box, roles, text, text_class, text_content, overlaps, cuts, events (local s), and
                          when used figure(s) / lands, insert, anchor, chips, lines ... Planner notes may ride along in
                          `beat`, `pattern`, `playbook_lines`, `note` (never compared with the code), and `extent`: the
                          area a scene really paints when that is smaller than its box (the plan check judges it; after
                          the code the measured rects do).
  plan/scene-briefs.md    one section per scene: a `#` heading naming its id (one section may cover a few ids), what it
                          looks like, the moments on its words, and a "Done when" line the result is checked against.

Two checks, both inside `veos validate`:
  plan mode   `veos validate --plan` (before the code): scenes come from plan/scenes.plan.json with their declared boxes
              (no measure), so face, safe zone, overlap, clutter, hues, on-word, sound anchors, data and the playbook's
              rules judge the plan itself; `plan_checks` adds V-PLAN: a well-formed plan, every beat layer planned, every
              planned scene in a beat (and, as advice only, a "Done when" line per scene when plan/scene-briefs.md
              exists or the scene carries `done_when`). Writes plan/validate.plan.json. Without plan/scenes.plan.json
              (the one-file flow: timeline.json + scenes.js) there is no V-PLAN and `--plan` judges the code.
  code mode   plain `veos validate` (after the code), whenever plan/scenes.plan.json exists: `fidelity` adds V-PLAN for
              every difference between the registered scenes and the plan: missing or extra scenes, timing (±1 frame),
              z, behind, kind, presets and their effective entry / exit windows, box (±2 px), roles, text, overlaps,
              cuts, events (±1 frame), every other field the plan sets, and the rule-relaxing fields (may_overlap_face,
              exception, ambient ...) the plan did not set.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from .core import FPS, VeosError, read_json
from .vcommon import advice, enter_frames, exit_frames, fail, norm_box

PLAN_FILE = ("plan", "scenes.plan.json")
BRIEFS_FILE = ("plan", "scene-briefs.md")
FRAME_TOL = 1.0 / FPS + 1e-6   # s: timing tolerance (one frame)
BOX_TOL = 2.0                  # px: declared box tolerance
SIZE = (1080, 1920)
NOTES = {"beat", "pattern", "playbook_lines", "note", "notes", "why", "brief", "extent",   # planner-only, not scene fields
         "intent", "look", "moments", "done_when"}
TIMES = ("t_in", "t_out")
TIME_LISTS = ("events", "cuts")
# compared even when the plan leaves them out (absent = the default), because each one changes what a rule allows:
# a coder must not loosen a rule the plan did not loosen.
ALWAYS = {"z": 0, "behind": False, "text": False, "kind": None, "in": "settle", "out": "none"}
GUARDED = ("may_overlap_face", "exception", "opaque", "covers_presenter", "onword_lead", "ambient", "continuous",
           "motion", "satisfies", "payoff", "smear", "handoff", "step_frames", "step_fps")
# the entry / exit windows (frames the overlap and smoothness checks treat as "passing by") are compared as the
# effective frame counts (vcommon.enter_frames / exit_frames), not field by field
WINDOW_FIELDS = ("in_frames", "out_frames", "enter_s", "settle_s", "exit_s")
FIX_CODE = ("Make plan/scenes.js match plan/scenes.plan.json (the plan is final). If the plan itself is wrong, "
            "report it to the planner instead of changing it.")


# ---------------------------------------------------------------- loading
def plan_path(pr) -> Path:
    return pr.path(*PLAN_FILE)


def has_plan(pr) -> bool:
    return plan_path(pr).exists()


def load_plan(pr) -> list[dict]:
    """plan/scenes.plan.json as a list of scene dicts; a missing or malformed file raises VeosError."""
    p = plan_path(pr)
    if not p.exists():
        raise VeosError("NO_SCENE_PLAN", f"{p} not found",
                        "Write plan/scenes.plan.json (one entry per scene: id, t_in, t_out, z, box, roles, events ...).")
    try:
        data = read_json(p)
    except ValueError as e:
        raise VeosError("BAD_SCENE_PLAN", f"plan/scenes.plan.json is not valid JSON: {e}", "Fix the JSON syntax.")
    if isinstance(data, dict) and isinstance(data.get("scenes"), list):
        data = data["scenes"]
    if not isinstance(data, list) or not all(isinstance(s, dict) and isinstance(s.get("id"), str) and s["id"]
                                             for s in data):
        raise VeosError("BAD_SCENE_PLAN", "plan/scenes.plan.json must be a list of scenes, each with a string `id`",
                        "Write [{\"id\": \"h-banner\", \"t_in\": 0, \"t_out\": 7.6, ...}, ...].")
    return data


# ---------------------------------------------------------------- helpers
def _num(v) -> bool:
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def _beat_of(tl: dict, sid: str, t: float) -> str | None:
    beats = tl.get("beats") or []
    for b in beats:
        if sid in (b.get("layers") or []):
            return b.get("id")
    for b in beats:
        if b.get("t0", 0) <= t < b.get("t1", 0):
            return b.get("id")
    return None


def _show(v) -> str:
    s = json.dumps(v, ensure_ascii=False, separators=(",", ":")) if not isinstance(v, str) else repr(v)
    return s if len(s) <= 80 else s[:77] + "..."


def _same(a, b, tol: float = FRAME_TOL) -> bool:
    """Structural equality; numbers within `tol`."""
    if _num(a) and _num(b):
        return abs(float(a) - float(b)) <= tol
    if isinstance(a, dict) and isinstance(b, dict):
        return a.keys() == b.keys() and all(_same(a[k], b[k], tol) for k in a)
    if isinstance(a, (list, tuple)) and isinstance(b, (list, tuple)):
        return len(a) == len(b) and all(_same(x, y, tol) for x, y in zip(a, b))
    return a == b


def _times(v) -> list[float]:
    return sorted(float(x) for x in (v or []) if _num(x))


# ---------------------------------------------------------------- the briefs
_HEAD = re.compile(r"^(#{1,6})\s+(.*)$")


def _names(sid: str, heading: str) -> bool:
    return re.search(r"(?<![\w-])" + re.escape(sid) + r"(?![\w-])", heading) is not None


def brief_sections(text: str, ids=()) -> list[tuple[str, str]]:
    """[(heading, body)] for every markdown heading. A body runs to the next heading of the same or a higher level, or
    to a nested heading that names a scene (of `ids`): a shared section ("2a. The card frame (shared by a, b)") does
    not swallow the briefs written under it."""
    lines = text.splitlines()
    heads = [(i, len(m.group(1)), m.group(2)) for i, ln in enumerate(lines) if (m := _HEAD.match(ln))]
    out = []
    for k, (i, lvl, title) in enumerate(heads):
        end = next((j for j, l2, t2 in heads[k + 1:] if l2 <= lvl or any(_names(x, t2) for x in ids)), len(lines))
        out.append((title, "\n".join(lines[i + 1:end])))
    return out


def brief_for(sections: list[tuple[str, str]], sid: str) -> str | None:
    """The body of the section whose heading names `sid`: the first one with a "Done when" line (shared-geometry
    sections name several scenes too), else the first one; None when no heading names it."""
    mine = [body for title, body in sections if _names(sid, title)]
    return next((b for b in mine if "done when" in b.lower()), mine[0] if mine else None)


# ---------------------------------------------------------------- plan mode
def plan_checks(tl: dict, plan: list[dict], briefs: str | None, duration: float) -> list[dict]:
    """V-PLAN before the code: the plan is complete and consistent with the timeline and the briefs."""
    out: list[dict] = []

    def add(sid, t, msg, fix):
        out.append(fail("V-PLAN", _beat_of(tl, sid, t), t, msg, fix))

    seen: set[str] = set()
    for s in plan:
        sid = s["id"]
        t_in, t_out = s.get("t_in"), s.get("t_out")
        t0 = float(t_in) if _num(t_in) else 0.0
        if sid in seen:
            add(sid, t0, f"scene '{sid}' is planned twice", "Give every scene its own id.")
        seen.add(sid)
        if not (_num(t_in) and _num(t_out)):
            add(sid, t0, f"'{sid}' needs numeric t_in and t_out", "Set both, in edit seconds.")
            continue
        if not (0 <= t_in < t_out <= duration + FRAME_TOL):
            add(sid, t0, f"'{sid}' runs {t_in}-{t_out} s, outside 0-{duration:.3f} s or empty",
                "Keep 0 <= t_in < t_out <= the reel's duration.")
        if not _num(s.get("z")):
            add(sid, t0, f"'{sid}' has no z", "Set z (behind-the-presenter cards 1-4, front graphics 5-10).")
        b = norm_box(s.get("box"))
        if b is None or b[2] <= b[0] or b[3] <= b[1]:
            add(sid, t0, f"'{sid}' has no usable box", "Set box {x, y, w, h} in screen px: where it rests.")
        elif b[2] <= 0 or b[3] <= 0 or b[0] >= SIZE[0] or b[1] >= SIZE[1]:
            add(sid, t0, f"'{sid}' box is entirely off the {SIZE[0]}x{SIZE[1]} frame", "Place its resting box on screen.")
        if not isinstance(s.get("roles"), list):
            add(sid, t0, f"'{sid}' has no roles list", "List the colour roles it uses ([] for neutral-only scenes).")
        dur = float(t_out) - float(t_in)
        for k in TIME_LISTS:
            v = s.get(k)
            if v is None:
                continue
            if not isinstance(v, list) or not all(_num(x) for x in v):
                add(sid, t0, f"'{sid}' {k} must be a list of seconds", f"Write {k} as local seconds after t_in.")
            elif k == "events" and any(x < 0 or x > dur + FRAME_TOL for x in v):
                add(sid, t0, f"'{sid}' has events outside its own life (0-{dur:.3f} s local)",
                    "Events are local seconds after the scene's t_in; keep them inside the scene.")

    layered: dict[str, str] = {}
    for b in tl.get("beats") or []:
        for lid in b.get("layers") or []:
            layered.setdefault(lid, b.get("id"))
            if lid not in seen:
                out.append(fail("V-PLAN", b.get("id"), b.get("t0", 0),
                                f"beat {b.get('id')} lists layer '{lid}', which the plan has no scene for",
                                "Plan the scene in plan/scenes.plan.json, or take it out of the beat's layers."))
    for s in plan:
        if s["id"] not in layered:
            add(s["id"], float(s.get("t_in") or 0), f"'{s['id']}' is not in any beat's layers",
                "Add it to the layers of the beat it belongs to in plan/timeline.json.")

    # the briefs are direction, not build integrity: optional (the one-file plan carries `done_when` on the scene itself),
    # and a missing brief or "Done when" line is advice
    if briefs is None:
        return out
    sections = brief_sections(briefs, [s["id"] for s in plan])
    for s in plan:
        sid, t = s["id"], float(s.get("t_in") or 0)
        if s.get("done_when"):
            continue
        body = brief_for(sections, sid)
        if body is None:
            out.append(advice(fail("V-PLAN", _beat_of(tl, sid, t), t, f"'{sid}' has no brief in plan/scene-briefs.md",
                                   "Add a section whose heading names the id, or a `done_when` on the scene.")))
        elif "done when" not in body.lower():
            out.append(advice(fail("V-PLAN", _beat_of(tl, sid, t), t, f"the brief for '{sid}' has no 'Done when' line",
                                   "End the brief with what the finished scene must show, on which words.")))
    return out


def declared_measure(plan: list[dict], frames: int, every: int = 3) -> dict:
    """A measure.json stand-in from the plan (plan mode), so the face, safe-zone and G1 / G2 checks judge the planned
    layout: each scene's `extent` (where it really paints, when that is smaller than its box: the words on a card-sized
    box) or else its `box`."""
    out: dict[str, dict] = {}
    for n in range(0, max(frames, 1), every):
        t = n / FPS
        row = {}
        for s in plan:
            b = norm_box(s.get("extent")) or norm_box(s.get("box"))
            if b is not None and _num(s.get("t_in")) and _num(s.get("t_out")) and s["t_in"] <= t < s["t_out"]:
                row[s["id"]] = list(b)
        out[str(n)] = row
    return {"every": every, "frames": out}


# ---------------------------------------------------------------- code mode
def fidelity(tl: dict, plan: list[dict], code: list[dict]) -> list[dict]:
    """V-PLAN after the code: every difference between the registered scenes and the plan."""
    out: list[dict] = []
    got = {s.get("id"): s for s in code}
    want = {s["id"]: s for s in plan}

    def add(sid, t, msg, fix=FIX_CODE):
        out.append(fail("V-PLAN", _beat_of(tl, sid, t), t, msg, fix))

    for sid, p in want.items():
        t = float(p.get("t_in") or 0)
        c = got.get(sid)
        if c is None:
            add(sid, t, f"'{sid}' is planned but plan/scenes.js does not register it",
                "Build it as its brief in plan/scene-briefs.md describes.")
            continue
        diffs: list[str] = []
        for k in TIMES:
            if _num(p.get(k)) and not (_num(c.get(k)) and abs(float(c[k]) - float(p[k])) <= FRAME_TOL):
                diffs.append(f"{k} {_show(c.get(k))} (plan {_show(p[k])})")
        for k in TIME_LISTS:
            a, b = _times(c.get(k)), _times(p.get(k))
            if len(a) != len(b) or any(abs(x - y) > FRAME_TOL for x, y in zip(a, b)):
                diffs.append(f"{k} {_show(a)} (plan {_show(b)})")
        for k, dflt in ALWAYS.items():
            a, b = c.get(k, dflt), p.get(k, dflt)
            if k in ("behind", "text"):
                a, b = bool(a), bool(b)
            elif k in ("in", "out"):
                a, b = a or dflt, b or dflt
            if not _same(a, b):
                diffs.append(f"{k} {_show(a)} (plan {_show(b)})")
        for k in GUARDED:
            a, b = c.get(k), p.get(k)
            if (a in (None, False, [], {}, "", 0)) and (b in (None, False, [], {}, "", 0)):
                continue
            if not _same(a, b):
                diffs.append(f"{k} {_show(a)} (plan {_show(b)})")
        a, b = enter_frames(c), enter_frames(p)
        if a != b:
            diffs.append(f"entry window {a} f (plan {b} f)")
        a, b = exit_frames(c), exit_frames(p)
        if a != b:
            diffs.append(f"exit window {a} f (plan {b} f)")
        a, b = sorted(c.get("roles") or []), sorted(p.get("roles") or [])
        if a != b:
            diffs.append(f"roles {_show(a)} (plan {_show(b)})")
        a, b = sorted(c.get("overlaps") or []), sorted(p.get("overlaps") or [])
        if a != b:
            diffs.append(f"overlaps {_show(a)} (plan {_show(b)})")
        if "box" in p:
            pb, cb = norm_box(p.get("box")), norm_box(c.get("box"))
            if pb is not None and (cb is None or any(abs(x - y) > BOX_TOL for x, y in zip(cb, pb))):
                diffs.append(f"box {_show(c.get('box'))} (plan {_show(p.get('box'))})")
        skip = NOTES | set(TIMES) | set(TIME_LISTS) | set(ALWAYS) | set(GUARDED) | set(WINDOW_FIELDS) | {
            "id", "roles", "overlaps", "box"}
        for k, v in p.items():
            if k in skip:
                continue
            if not _same(c.get(k), v):
                diffs.append(f"{k} {_show(c.get(k))} (plan {_show(v)})")
        if diffs:
            add(sid, t, f"'{sid}' differs from the plan: " + "; ".join(diffs))
    for sid, c in got.items():
        if sid not in want:
            add(sid, float(c.get("t_in") or 0), f"'{sid}' is registered in plan/scenes.js but is not in the plan",
                "Remove it. A scene the reel needs goes to the planner first (plan/scenes.plan.json + a brief).")
    return out
