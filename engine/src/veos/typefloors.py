"""V-TYPE (type floors, NC-4 / G4) and V-EXC (declared exceptions E1-E6, structure Part C) for `veos validate` (E-06, E-21).

Both always run, for every playbook (NC-4 and the closed exception registry cannot be switched off). They read
plan/measure.text.json (`veos measure`, textmeasure.py) through `ctx.text_measure` {frame: {texts, items, slots, pixels}},
the measured rects (`ctx.measured`), the scene meta and the resolved `style["exceptions"]` (limits already clamped to the
registry by tokens.check_exceptions).

Text class of a measured element: the node's `data-tc` marker, else (caption chunks, scene ids starting with "__") the
chunk's `class` from work/captions.json or the caption profile's `skin.text_class` (default TC-subtitle), else the scene's
`text_class`, else TC-display for headline / hero kinds and TC-label otherwise (= the G4 40 px floor).

V-TYPE  per measured element: the class floor (Definitions table); E3 quiet type (subtitles 36-53 px only with E3 declared
        and weight, lines, characters per line and contrast >= contrast_min, or >= pill_contrast_min on a painted
        container; labels 28-39 px only with E3 and `redundant`); contrast >= 4.5 (3.0 for display >= 96 px); no clipped
        glyphs. TC-decorative is exempt. Only settled samples are judged (settled(): an element caught mid-fade is
        judged at its opaque samples; text under 30% opacity is a passing ghost), and a frame-edge crop while the
        canvas camera moves that layer is motion (V-CANVAS's job). Without measure.text.json: the caption chunk sizes
        of work/captions.json, and always the playbook's own caption-profile / type sizes against the floors.
V-EXC   `exception` ids: one per scene, in the registry, declared in the tokens. An `ambient: true` scene at z3-10
        needs E4. Then each exception's limits (see the rule functions below). Advice only (validate's levels): it
        never blocks a reel. Text behind the speaker needs no exception.
"""
from __future__ import annotations

from .vcommon import FRAME_H, FRAME_W, HEADLINE_KINDS, expand, fail, fr, get_path, overlap, settled_at

FLOORS = {"TC-display": 40, "TC-subtitle": 54, "TC-label": 40, "TC-legal": 22, "TC-decorative": 0}
ABS_FLOORS = {"TC-display": 40, "TC-subtitle": 36, "TC-label": 28, "TC-legal": 22, "TC-decorative": 0}
CLASSES = tuple(FLOORS)
G2_UNCOUNTED = ("TC-legal", "TC-decorative")
CONTRAST_MIN = 4.5
BIG_DISPLAY = (96, 3.0)          # TC-display >= 96 px may sit at >= 3:1
DISPLAY_KINDS = tuple(HEADLINE_KINDS) + ("hero", "hero_number", "counter", "kinetic", "title", "cta-keyword")
OPAQUE, GHOST = 0.95, 0.3      # V-TYPE: settled vs mid-fade samples (see settled())
VISIBLE_LETTER = 0.5             # E1: a first/last letter counts as visible at >= 50% of its box
E6_ENTRY_F, E6_EXIT_F = 14, 10   # E6: the container's own entry / exit frames are G3's business, not the slot check
E2_CLEAN_MAX = 2
E3_MAX_CHARS = 44                # E3 registry cap on characters per caption line (tokens.EXC_REGISTRY)


# --------------------------------------------------------------------------- helpers
def _count(v, default: int) -> int:
    """An int from a measured / exported count; a list (e.g. a chunk's `lines` as word-index lists) counts its items."""
    if isinstance(v, (list, tuple)):
        return len(v)
    try:
        return int(v) if v not in (None, "") and not isinstance(v, bool) else default
    except (TypeError, ValueError):
        return default


def exc_id(s: dict):
    """The scene's exception as a registry id (token names accepted), the raw value when unknown, None when absent."""
    from .tokens import EXC_BY_NAME, EXC_REGISTRY
    e = s.get("exception")
    if e is None or e is False:
        return None
    if isinstance(e, str):
        return e if e in EXC_REGISTRY else EXC_BY_NAME.get(e, e)
    return e


def limits(c, eid: str) -> dict | None:
    v = (c.style.get("exceptions") or {}).get(eid)
    return v if isinstance(v, dict) else None


def uses(c, s: dict, eid: str) -> bool:
    """The scene relies on a declared exception `eid`."""
    return exc_id(s) == eid and limits(c, eid) is not None


def scene_class(s: dict | None) -> str:
    if not s:
        return "TC-label"
    tc = s.get("text_class")
    if tc in CLASSES:
        return tc
    return "TC-display" if s.get("kind") in DISPLAY_KINDS else "TC-label"


def caption_profile(c) -> dict:
    pid = get_path(c.style, "captions.default") or "CS-1"
    return get_path(c.style, f"captions.profiles.{pid}") or {}


def record_class(c, rec: dict, byid: dict) -> str:
    if rec.get("tc") in CLASSES:
        return rec["tc"]
    sid = str(rec.get("scene", ""))
    if sid.startswith("__"):
        ch = rec.get("chunk") or {}
        if ch.get("class") in CLASSES:
            return ch["class"]
        tc = get_path(caption_profile(c), "skin.text_class")
        return tc if tc in CLASSES else "TC-subtitle"
    return scene_class(byid.get(sid))


def text_records(c):
    """[(frame, record)] from plan/measure.text.json, in frame order."""
    out = []
    for n, f in sorted((c.text_measure or {}).items()):
        for rec in f.get("texts") or []:
            out.append((n, rec))
    return out


def camera_moving(c):
    """f(scene, frame) -> True while the canvas camera (E-14) is moving that scene's layer; frame-edge crops of world
    content travelling past the edge are motion, not clipped type (V-CANVAS judges the move)."""
    if not (c.tl.get("canvas_camera") or []):
        return lambda s, n: False
    try:
        from .canvascam import camera_for, parallax_of, state_at
        cam = camera_for(c)
    except Exception:  # noqa: BLE001 - no canvas-camera module / bad moves: judge every crop
        return lambda s, n: False
    return lambda s, n: bool(s) and parallax_of(s) > 0 and bool(state_at(cam, n).get("moving"))


def settled(recs):
    """Drop samples caught mid-fade. Per element (scene, text): when it reaches full opacity (>= 0.95) in some sample, only
    those samples are judged; otherwise only its most opaque samples (its resting opacity). Text under 30% opacity is a
    passing ghost, not reading text. Returns (kept, skipped count)."""
    best: dict = {}
    for _, r in recs:
        k = (r.get("scene"), r.get("text"))
        best[k] = max(best.get(k, 0.0), float(r.get("opacity", 1)))
    kept = []
    for n, r in recs:
        op, top = float(r.get("opacity", 1)), best[(r.get("scene"), r.get("text"))]
        if op >= GHOST and (op >= OPAQUE or op >= top - 1e-6):
            kept.append((n, r))
    return kept, len(recs) - len(kept)


def past_entrance(recs, byid: dict):
    """Drop the samples taken inside a scene's entrance / exit window (vcommon.settled_at) when the same element has a
    sample in its settled hold: a slam or slide-in caught mid-move is neither clipped nor low-contrast type."""
    def ok(n, r):
        s = byid.get(r.get("scene"))
        return s is None or settled_at(s, n)
    has = {(r.get("scene"), r.get("text")) for n, r in recs if ok(n, r)}
    kept = [(n, r) for n, r in recs if ok(n, r) or (r.get("scene"), r.get("text")) not in has]
    return kept, len(recs) - len(kept)


def _name(sid: str) -> str:
    return "the captions" if str(sid).startswith("__") else f"'{sid}'"


def _e3_for(c, rec: dict, s: dict | None) -> dict | None:
    """E3 limits when this element may use quiet type: captions inherit E3 from the profile, scenes declare it."""
    e3 = limits(c, "E3")
    if e3 is None:
        return None
    if str(rec.get("scene", "")).startswith("__"):
        ex = (rec.get("chunk") or {}).get("exception") or caption_profile(c).get("exception")
        return e3 if ex in (None, "E3", "quiet_type") else None
    return e3 if s is not None and exc_id(s) == "E3" else None


class _Issues:
    """Collect per (scene, issue) the first time, the count and the worst value, then emit one failure each."""

    def __init__(self):
        self.d: dict = {}

    def add(self, key, n, worst, msg, fix):
        """worst: the measured value (lower is worse) or None; the failure reports the first frame and the worst sample."""
        cur = self.d.get(key)
        if cur is None:
            self.d[key] = {"n": n, "count": 1, "worst": worst, "msg": msg, "fix": fix}
            return
        cur["count"] += 1
        if worst is not None and cur["worst"] is not None and worst < cur["worst"]:
            cur["worst"], cur["msg"], cur["fix"] = worst, msg, fix

    def emit(self, c, rule):
        out = []
        for k, v in self.d.items():
            t = v["n"] / c.fps if v["n"] is not None else 0.0
            more = f" ({v['count']} measured samples)" if v["count"] > 1 else ""
            out.append(fail(rule, c.beat_id(t) if v["n"] is not None else None, t, v["msg"] + more, v["fix"]))
        return out


# --------------------------------------------------------------------------- V-TYPE
def _check_size(c, iss: _Issues, n, rec, s, cls) -> None:
    sid, size = rec.get("scene"), float(rec.get("size") or 0)
    txt = (rec.get("text") or "")[:40]
    where = f"{_name(sid)} \"{txt}\" at {n / c.fps:.2f} s"
    if size >= FLOORS[cls]:
        return
    e3 = _e3_for(c, rec, s)
    if cls == "TC-subtitle" and e3 is not None and size >= float(e3.get("subtitle_min_px", 36)):
        bad = []
        if float(rec.get("weight") or 0) < float(e3.get("weight_min", 500)):
            bad.append(f"weight {rec.get('weight')} < {e3.get('weight_min', 500)}")
        n_lines, mcl = _count(rec.get("lines"), 1), _count(rec.get("max_chars_line"), 0)
        if n_lines > int(e3.get("max_lines", 2)):
            bad.append(f"{n_lines} lines > {e3.get('max_lines', 2)}")
        if mcl > int(e3.get("max_chars_line", E3_MAX_CHARS)):
            bad.append(f"{mcl} characters per line > {e3.get('max_chars_line', E3_MAX_CHARS)}")
        k = rec.get("contrast")
        need = float(e3.get("pill_contrast_min", 4.5) if rec.get("box") else e3.get("contrast_min", 7.0))
        if k is not None and float(k) < need:
            bad.append(f"contrast {k}:1 < {need}:1" + (" on its container" if rec.get("box") else " (no pill/box)"))
        if bad:
            iss.add((sid, "e3"), n, size, f"{where}: E3 quiet-type caption at {size:g} px breaks the E3 conditions: {', '.join(bad)}",
                    f"at {size:g} px a caption needs weight >= {e3.get('weight_min', 500)}, <= {e3.get('max_lines', 2)} lines, "
                    f"<= {e3.get('max_chars_line', E3_MAX_CHARS)} characters per line and contrast >= {e3.get('contrast_min', 7.0)}:1 "
                    f"(>= {e3.get('pill_contrast_min', 4.5)}:1 on a pill/box); or raise it to {FLOORS[cls]} px")
        return
    redundant = bool(rec.get("redundant") or (s or {}).get("redundant"))
    if cls == "TC-label" and e3 is not None and size >= float(e3.get("label_min_px", 28)) and redundant:
        return
    absolute = ABS_FLOORS[cls]
    if size < absolute:
        why = f"below the absolute {cls} floor of {absolute} px (NC-4; no exception can lower it)"
    elif cls == "TC-subtitle":
        why = (f"below the {FLOORS[cls]} px caption floor; 36-53 px is quiet type (E3), which "
               + ("this element does not use" if limits(c, "E3") else "this playbook does not declare"))
    elif cls == "TC-label":
        why = (f"below the {FLOORS[cls]} px label floor; 28-39 px labels need E3 and `redundant: true` "
               "(the same words spoken or shown larger)")
    else:
        why = f"below the {FLOORS[cls]} px {cls} floor"
    iss.add((sid, "size"), n, size, f"{where}: {cls} text is {size:g} px, {why}",
            f"raise {_name(sid)} to >= {FLOORS[cls]} px rendered size (font-size x any scale), or shorten the text so it fits"
            + ("; for a caption, shorten the chunk (the auto-fit shrinks long cards)" if str(sid).startswith("__") else ""))


def rule_type(c, p: dict):
    byid = {s.get("id"): s for s in c.scenes}
    iss = _Issues()
    allrecs = text_records(c)
    recs, mid_fade = settled(allrecs)
    recs, entering = past_entrance(recs, byid)
    stats = {"elements": len(allrecs), "frames": len(c.text_measure or {}), "source": "measure.text.json" if allrecs else "declared",
             "mid_fade_skipped": mid_fade, "entrance_skipped": entering, "contrast_checked": sum(1 for _, r in recs if r.get("contrast") is not None),
             "by_class": {}, "min_px": {}}
    if c.text_measure is None:
        c.warnings.append("V-TYPE: plan/measure.text.json not found; only declared sizes checked "
                          "(run `veos measure` for rendered sizes, contrast and clipping)")
    moving = camera_moving(c)
    for n, rec in recs:
        sid = rec.get("scene")
        s = byid.get(sid)
        cls = record_class(c, rec, byid)
        stats["by_class"][cls] = stats["by_class"].get(cls, 0) + 1
        size = float(rec.get("size") or 0)
        stats["min_px"][cls] = min(stats["min_px"].get(cls, size), size)
        if cls == "TC-decorative":
            continue
        _check_size(c, iss, n, rec, s, cls)
        k = rec.get("contrast")
        need = BIG_DISPLAY[1] if cls == "TC-display" and size >= BIG_DISPLAY[0] else CONTRAST_MIN
        if k is not None and float(k) < need:
            iss.add((sid, "contrast"), n, float(k),
                    f"{_name(sid)} \"{(rec.get('text') or '')[:40]}\" contrast is {k}:1 against its background at {n / c.fps:.2f} s "
                    f"(min {need}:1 for {cls}{' >= 96 px' if need == BIG_DISPLAY[1] else ''})",
                    f"give {_name(sid)} a darker/lighter fill, a stroke or shadow, or a pill/box behind it")
        if rec.get("clipped") and not (rec["clipped"] == "outside the frame edge" and moving(s, n)):
            iss.add((sid, "clip"), n, None, f"{_name(sid)} \"{(rec.get('text') or '')[:40]}\" has clipped glyphs at "
                                           f"{n / c.fps:.2f} s ({rec['clipped']})",
                    f"make {_name(sid)}'s box wide/tall enough for its text (or shrink the text) and keep it inside the frame")
    out = iss.emit(c, "V-TYPE")
    if not any(str(r.get("scene", "")).startswith("__") for _, r in allrecs):
        out += _declared_captions(c)
    out += _token_floors(c)
    if c.schema >= 3:
        missing = sorted({s.get("id") for s in c.scenes if c.is_text(s) and s.get("text_class") not in CLASSES})
        if missing:
            c.warnings.append("V-TYPE: text scenes without a valid text_class (treated by kind: headline kinds TC-display, "
                              f"else TC-label): {', '.join(map(str, missing))}")
    c.stats_extra["type"] = stats
    return out


def chunk_lines(ch: dict) -> tuple[int, int]:
    """(line count, characters on the longest line) of a work/captions.json chunk. The export writes `lines` as a list
    of word-index lists ([[0, 1], [2]]) over `words` [{t}], older files an int; `veos measure` is not needed."""
    text = str(ch.get("text", ""))
    lines = ch.get("lines")
    words = [str(w.get("t", "")) if isinstance(w, dict) else str(w) for w in ch.get("words") or []]
    if isinstance(lines, list) and lines:
        chars = []
        for ln in lines:
            if isinstance(ln, list) and words and all(isinstance(k, int) and 0 <= k < len(words) for k in ln):
                chars.append(len(" ".join(words[k] for k in ln)))
            elif isinstance(ln, str):
                chars.append(len(ln))
        n = len(lines)
        mcl = max(chars) if chars else len(text)
    else:
        try:
            n = max(1, int(lines)) if lines is not None and not isinstance(lines, bool) else 1
        except (TypeError, ValueError):
            n = 1
        mcl = len(text) if n <= 1 else -(-len(text) // n)
    if isinstance(ch.get("max_chars_line"), (int, float)) and not isinstance(ch.get("max_chars_line"), bool):
        mcl = int(ch["max_chars_line"])
    return n, mcl


def _declared_captions(c) -> list:
    """Fallback without measured captions: work/captions.json chunk sizes (E-05 export)."""
    out = []
    prof = caption_profile(c)
    for ch in getattr(c, "caption_raw", None) or []:
        size = ch.get("size")
        if not isinstance(size, (int, float)):
            continue
        n_lines, mcl = chunk_lines(ch)
        rec = {"scene": "__captions", "size": float(size), "text": ch.get("text", ""),
               "weight": ch.get("weight", get_path(prof, "skin.weight", 800)), "chunk": ch, "lines": n_lines,
               "max_chars_line": mcl, "box": ch.get("box")}
        iss = _Issues()
        _check_size(c, iss, fr(float(ch.get("t0", 0))) + 1, rec, None, record_class(c, rec, {}))
        out += iss.emit(c, "V-TYPE")
    return out


def _min_size(v):
    if isinstance(v, (int, float)) and not isinstance(v, bool):
        return float(v)
    if isinstance(v, (list, tuple)) and v and all(isinstance(x, (int, float)) for x in v):
        return float(min(v))
    return None


def _token_floors(c) -> list:
    """The playbook's own declared sizes: caption-profile skins and `type` entries with a text class."""
    out = []
    e3 = limits(c, "E3")
    for pid, prof in (get_path(c.style, "captions.profiles") or {}).items():
        skin = (prof or {}).get("skin") or {}
        size, cls = _min_size(skin.get("size")), skin.get("text_class", "TC-subtitle")
        if size is None or cls not in CLASSES or size >= FLOORS[cls]:
            continue
        floor = ABS_FLOORS[cls]
        if cls == "TC-subtitle" and e3 is not None and prof.get("exception") in (None, "E3", "quiet_type"):
            floor = float(e3.get("subtitle_min_px", 36))
            if size >= floor and float(skin.get("weight", 800)) < float(e3.get("weight_min", 500)):
                out.append(fail("V-TYPE", None, 0, f"caption profile {pid} is {size:g} px at weight {skin.get('weight')} "
                                f"(E3 quiet type needs weight >= {e3.get('weight_min', 500)})",
                                f"set captions.profiles.{pid}.skin.weight >= {e3.get('weight_min', 500)} or the size >= 54"))
                continue
        elif cls == "TC-subtitle":
            floor = FLOORS[cls]
        if size < floor:
            out.append(fail("V-TYPE", None, 0, f"caption profile {pid} is {size:g} px, below the {floor:g} px {cls} floor"
                            + ("" if e3 else " (36-53 px needs E3 quiet type declared in exceptions)"),
                            f"raise captions.profiles.{pid}.skin.size to >= {floor:g}"))
    for key, ent in (c.style.get("type") or {}).items():
        if not isinstance(ent, dict) or ent.get("text_class") not in CLASSES:
            continue
        size, cls = _min_size(ent.get("size")), ent["text_class"]
        if size is not None and size < ABS_FLOORS[cls]:
            out.append(fail("V-TYPE", None, 0, f"type.{key} is {size:g} px, below the absolute {cls} floor of "
                            f"{ABS_FLOORS[cls]} px (NC-4)", f"raise type.{key}.size to >= {ABS_FLOORS[cls]}"))
    return out


# --------------------------------------------------------------------------- V-EXC
def _records_of(c, sid):
    return [(n, r) for n, r in text_records(c) if r.get("scene") == sid]


def _active_frames(s):
    return range(fr(s.get("t_in", 0)), max(fr(s.get("t_out", 0)), fr(s.get("t_in", 0)) + 1))


def _cta_ranges(c):
    return c.section_range(lambda x: x.upper() == "CTA")


def _e1(c, lim, scs) -> list:
    out = []
    for s in scs:
        sid, t0 = s.get("id"), float(s.get("t_in", 0))
        bid = c.beat_id(t0)
        if not s.get("behind"):
            out.append(fail("V-EXC", bid, t0, f"'{sid}' declares E1 (behind-subject text) but is not behind: true",
                            f"set behind: true on '{sid}' (text between the footage and the person cut-out) or drop the exception"))
        if scene_class(s) != "TC-display":
            out.append(fail("V-EXC", bid, t0, f"'{sid}' uses E1 with text class {scene_class(s)}; E1 is display text only",
                            f"set text_class: \"TC-display\" (a big word / number) or bring '{sid}' in front of the subject"))
        hold = float(s.get("t_out", 0)) - t0
        if hold + 1e-6 < float(lim.get("min_hold_s", 0.6)):
            out.append(fail("V-EXC", bid, t0, f"'{sid}' holds {hold:.2f} s behind the subject (E1 min {lim.get('min_hold_s', 0.6)} s)",
                            f"hold '{sid}' for at least {lim.get('min_hold_s', 0.6)} s"))
        occ = [(n, r["occlusion"]) for n, r in _records_of(c, sid) if isinstance(r.get("occlusion"), dict)
               and r["occlusion"].get("visible") is not None]
        if not occ:
            c.warnings.append(f"V-EXC: E1 occlusion of '{sid}' not measured (run `veos measure` with the cut-out frames "
                              "work/frames/c*.webp present)")
            continue
        mv = float(lim.get("min_visible", 0.65))
        low = [(n, o) for n, o in occ if o["visible"] + 1e-9 < mv]
        if low:
            n, o = min(low, key=lambda x: x[1]["visible"])
            out.append(fail("V-EXC", c.beat_id(n / c.fps), n / c.fps,
                            f"'{sid}' is only {round(100 * o['visible'])}% visible behind the subject at {n / c.fps:.2f} s "
                            f"(E1 needs >= {round(100 * mv)}% of the glyph area for the whole hold; {len(low)} sample(s))",
                            f"move or enlarge '{sid}' so the head covers less of it (or shorten the word)"))
        hid = [(n, o) for n, o in occ if min(o.get("first", 1), o.get("last", 1)) < VISIBLE_LETTER]
        if hid:
            n, o = hid[0]
            which = "first" if o.get("first", 1) < VISIBLE_LETTER else "last"
            out.append(fail("V-EXC", c.beat_id(n / c.fps), n / c.fps,
                            f"the {which} letter of '{sid}' is hidden behind the subject at {n / c.fps:.2f} s "
                            "(E1: the word stays readable, first and last letters visible)",
                            f"shift '{sid}' so the head sits between letters, not over the word's ends"))
    out += _at_once(c, scs, int(lim.get("max_at_once", 1)), "E1", "behind-subject text elements")
    return out


def _at_once(c, scs, mx, eid, noun) -> list:
    cnt: dict[int, list] = {}
    for s in scs:
        for n in _active_frames(s):
            cnt.setdefault(n, []).append(s.get("id"))
    over = sorted(n for n, ids in cnt.items() if len(ids) > mx)
    if not over:
        return []
    n = over[0]
    return [fail("V-EXC", c.beat_id(n / c.fps), n / c.fps,
                 f"{len(cnt[n])} {noun} at once at {n / c.fps:.2f} s: {', '.join(map(str, cnt[n]))} ({eid} allows {mx})",
                 f"show at most {mx} at a time")]


def _e2(c, lim, scs) -> list:
    out = []
    starts = sorted(float(s.get("t_in", 0)) for s in scs)
    mx_reel, mx60 = int(lim.get("max_per_reel", 2)), int(lim.get("max_per_60s", 1))
    if len(scs) > mx_reel:
        out.append(fail("V-EXC", c.beat_id(starts[mx_reel]), starts[mx_reel],
                        f"{len(scs)} chaos bursts in the reel (E2 allows {mx_reel})", "remove the extra bursts"))
    for i, t in enumerate(starts):
        win = [x for x in starts if t - 1e-6 <= x < t + 60 - 1e-6]
        if len(win) > mx60:
            out.append(fail("V-EXC", c.beat_id(win[mx60]), win[mx60],
                            f"{len(win)} chaos bursts within 60 s from {t:.2f} s (E2 allows {mx60} per 60 s)",
                            "space the bursts at least 60 s apart"))
            break
    cta = _cta_ranges(c)
    hide = [(float(h[0]), float(h[1])) for h in ((c.tl.get("captions") or {}).get("hide") or []) if isinstance(h, (list, tuple)) and len(h) >= 2]
    z8 = [(float(s.get("t_in", 0)), float(s.get("t_out", 0))) for s in c.scenes if s.get("z") == 8]
    for s in scs:
        sid, a, b = s.get("id"), float(s.get("t_in", 0)), float(s.get("t_out", 0))
        bid = c.beat_id(a)
        if b - a > float(lim.get("max_s", 1.5)) + 1e-6:
            out.append(fail("V-EXC", bid, a, f"chaos burst '{sid}' lasts {b - a:.2f} s (E2 max {lim.get('max_s', 1.5)} s)",
                            f"shorten '{sid}' to {lim.get('max_s', 1.5)} s"))
        snip = max([len(v) for v in _by_frame(_records_of(c, sid)).values()] or [0])
        decl = s.get("snippets")
        decl = len(decl) if isinstance(decl, (list, tuple)) else decl
        snip = max(snip, int(decl) if isinstance(decl, (int, float)) else 0)
        if snip > int(lim.get("max_snippets", 6)):
            out.append(fail("V-EXC", bid, a, f"chaos burst '{sid}' shows {snip} text snippets (E2 max {lim.get('max_snippets', 6)})",
                            f"cut '{sid}' to {lim.get('max_snippets', 6)} snippets"))
        if any(a < y and x < b for x, y in cta):
            out.append(fail("V-EXC", bid, a, f"chaos burst '{sid}' runs during the CTA (E2: never during the CTA)",
                            f"move '{sid}' out of the CTA section"))
        subs = [n for n in c.measured if fr(a) <= n < fr(b) and any(str(k).startswith("__") for k in c.measured[n])]
        cap = [ch for ch in (c.caption_chunks or []) if ch["t0"] < b - 1e-6 and ch["t1"] > a + 1e-6
               and not any(x - 1e-6 <= max(a, ch["t0"]) and min(b, ch["t1"]) <= y + 1e-6 for x, y in hide + z8)]
        if subs or cap:
            t = subs[0] / c.fps if subs else max(a, cap[0]["t0"])
            out.append(fail("V-EXC", c.beat_id(t), t, f"captions show during chaos burst '{sid}' ({a:.2f}-{b:.2f} s; E2 hides them)",
                            f"add [{a:.2f}, {b:.2f}] to timeline captions.hide"))
        clean = float(lim.get("clean_after_s", 1.0))
        for n in range(fr(b), fr(b + clean)):
            els = [x.get("id") for x in c.scenes if x is not s and c.active(x, n) and 3 <= x.get("z", 0) <= 10
                   and not x.get("behind") and not x.get("ambient")]
            if any(ch["t0"] - 1e-6 <= n / c.fps < ch["t1"] for ch in (c.caption_chunks or [])):
                els.append("captions")
            if len(els) > E2_CLEAN_MAX:
                out.append(fail("V-EXC", c.beat_id(n / c.fps), n / c.fps,
                                f"{len(els)} elements within {clean:g} s after chaos burst '{sid}' ({', '.join(map(str, els))}); "
                                f"E2 needs a clean frame (<= {E2_CLEAN_MAX} elements) after it",
                                f"start the next elements at least {clean:g} s after '{sid}' ends"))
                break
    return out


def _by_frame(recs):
    d: dict = {}
    for n, r in recs:
        d.setdefault(n, []).append(r)
    return d


def _e4(c, lim, scs) -> list:
    out = []
    area_max, n_max = float(lim.get("max_item_area", 0.12)), int(lim.get("max_items", 30))
    speed_max, dim, blur = float(lim.get("max_speed_px_s", 60)), float(lim.get("dim_under_text", 0.4)), float(lim.get("blur_px", 6))
    frame_area = float(FRAME_W * FRAME_H)
    for s in scs:
        sid, a, b = s.get("id"), float(s.get("t_in", 0)), float(s.get("t_out", 0))
        bid = c.beat_id(a)
        if b - a > float(lim.get("max_s", 5)) + 1e-6:
            out.append(fail("V-EXC", bid, a, f"ambient field '{sid}' lasts {b - a:.2f} s (E4 max {lim.get('max_s', 5)} s per occurrence)",
                            f"shorten '{sid}'"))
        if s.get("z", 0) >= 3 and not s.get("ambient"):
            out.append(fail("V-EXC", bid, a, f"ambient field '{sid}' is drawn at z{s.get('z')} without ambient: true",
                            f"draw '{sid}' at z1-2 or flag it ambient: true"))
        recs = _records_of(c, sid)
        if recs:
            n, r = recs[0]
            out.append(fail("V-EXC", c.beat_id(n / c.fps), n / c.fps, f"ambient field '{sid}' carries text (\"{(r.get('text') or '')[:30]}\"); E4 items have no text",
                            f"remove the text from '{sid}' (texture only) or make it its own element"))
        items = {n: f["items"][sid] for n, f in (c.text_measure or {}).items() if sid in (f.get("items") or {})}
        if not items:
            ni, ar = s.get("items"), s.get("item_area")
            if isinstance(ni, (int, float)) and ni > n_max:
                out.append(fail("V-EXC", bid, a, f"ambient field '{sid}' declares {int(ni)} items (E4 max {n_max})", f"use <= {n_max} items"))
            if isinstance(ar, (int, float)) and ar > area_max:
                out.append(fail("V-EXC", bid, a, f"ambient field '{sid}' items cover {ar:.0%} of the frame each (E4 max {area_max:.0%})",
                                "make the items smaller"))
            sp = s.get("speed_px_s")
            if isinstance(sp, (int, float)) and sp > speed_max:
                out.append(fail("V-EXC", bid, a, f"ambient field '{sid}' moves {sp:g} px/s (E4 max {speed_max:g})", "slow the drift"))
            if ni is None:
                c.warnings.append(f"V-EXC: E4 items of '{sid}' not measured (run `veos measure`; mark items with data-item)")
            continue
        worst_n = max(items, key=lambda k: len(items[k]))
        if len(items[worst_n]) > n_max:
            out.append(fail("V-EXC", c.beat_id(worst_n / c.fps), worst_n / c.fps,
                            f"ambient field '{sid}' has {len(items[worst_n])} items at {worst_n / c.fps:.2f} s (E4 max {n_max})",
                            f"use <= {n_max} items"))
        big = [(n, it) for n, its in items.items() for it in its
               if (it["rect"][2] - it["rect"][0]) * (it["rect"][3] - it["rect"][1]) / frame_area > area_max + 1e-9]
        if big:
            n, it = big[0]
            ar = (it["rect"][2] - it["rect"][0]) * (it["rect"][3] - it["rect"][1]) / frame_area
            out.append(fail("V-EXC", c.beat_id(n / c.fps), n / c.fps,
                            f"an item of ambient field '{sid}' covers {ar:.0%} of the frame (E4 max {area_max:.0%} per item)",
                            "make the field items smaller"))
        fast = None
        for n in sorted(items):
            nx = items.get(n + 1)
            if nx is None or len(nx) != len(items[n]):
                continue
            for p0, p1 in zip(items[n], nx):
                r0, r1 = p0["rect"], p1["rect"]
                v = (((r1[0] + r1[2]) - (r0[0] + r0[2])) ** 2 + ((r1[1] + r1[3]) - (r0[1] + r0[3])) ** 2) ** 0.5 / 2 * c.fps
                if v > speed_max + 1e-6 and (fast is None or v > fast[1]):
                    fast = (n, v)
        if fast:
            out.append(fail("V-EXC", c.beat_id(fast[0] / c.fps), fast[0] / c.fps,
                            f"ambient field '{sid}' items move {fast[1]:.0f} px/s (E4 max {speed_max:g})", "slow the drift"))
        # under the active text rect + 40 px: dimmed >= dim or blurred >= blur_px (or the scene declares it does so)
        if float(s.get("dim_under_text") or 0) >= dim or float(s.get("blur_under_text") or 0) >= blur:
            continue
        for n, its in sorted(items.items()):
            texts = [r for r in ((c.text_measure or {}).get(n, {}).get("texts") or []) if r.get("scene") != sid]
            hit = None
            for r in texts:
                zone = expand(tuple(r["rect"]), 40)
                for it in its:
                    if overlap(tuple(it["rect"]), zone) and it.get("op", 1) > 1 - dim + 1e-6 and float(it.get("blur") or 0) < blur:
                        hit = r
                        break
                if hit:
                    break
            if hit:
                out.append(fail("V-EXC", c.beat_id(n / c.fps), n / c.fps,
                                f"ambient field '{sid}' is not dimmed under {_name(hit.get('scene'))} at {n / c.fps:.2f} s "
                                f"(E4: items within 40 px of active text dimmed >= {dim:.0%} or blurred >= {blur:g} px)",
                                f"lower the opacity of '{sid}' items near the text to <= {1 - dim:.2f} (or blur them), "
                                "or declare dim_under_text on the scene when a mask does it"))
                break
    return out


def _e5(c, lim, scs) -> list:
    out = []
    m, mn = float(lim.get("min_margin", 24)), float(lim.get("min_display_px", 180))
    for s in scs:
        sid, a = s.get("id"), float(s.get("t_in", 0))
        bid = c.beat_id(a)
        if scene_class(s) != "TC-display":
            out.append(fail("V-EXC", bid, a, f"'{sid}' uses E5 edge bleed with text class {scene_class(s)} (display only)",
                            f"set text_class: \"TC-display\" or drop the exception"))
        recs = _records_of(c, sid)
        if recs:
            n, r = min(recs, key=lambda x: float(x[1].get("size") or 0))
            if float(r.get("size") or 0) + 1e-6 < mn:
                out.append(fail("V-EXC", c.beat_id(n / c.fps), n / c.fps,
                                f"'{sid}' bleeds to the edge at {float(r.get('size') or 0):g} px (E5 needs display type >= {mn:g} px)",
                                f"make '{sid}' >= {mn:g} px or keep the 64 px margin"))
            clip = [(n, r) for n, r in recs if r.get("clipped")]
            if clip:
                n, r = clip[0]
                out.append(fail("V-EXC", c.beat_id(n / c.fps), n / c.fps, f"'{sid}' glyphs are cropped ({r['clipped']}); E5 never crops glyphs",
                                f"pull '{sid}' inside the frame"))
        else:
            c.warnings.append(f"V-EXC: E5 size of '{sid}' not measured (run `veos measure`)")
        bb = c.union_rect(s)
        if bb is not None and (bb[0] < m - 1 or bb[1] < m - 1 or bb[2] > FRAME_W - m + 1 or bb[3] > FRAME_H - m + 1):
            out.append(fail("V-EXC", bid, a, f"'{sid}' rect {tuple(int(v) for v in bb)} is closer than {m:g} px to the frame edge (E5)",
                            f"keep '{sid}' >= {m:g} px from every edge"))
    out += _at_once(c, scs, int(lim.get("max_at_once", 1)), "E5", "edge-bleed elements")
    return out


def _e6(c, lim, scs) -> list:
    out = []
    tol = float(lim.get("slot_tolerance_px", 4))
    for s in scs:
        sid = s.get("id")
        fin, fout = fr(s.get("t_in", 0)), fr(s.get("t_out", 0))
        inner = lambda n: fin + E6_ENTRY_F <= n < fout - E6_EXIT_F  # noqa: E731
        rects = {n: tuple(f["slots"][sid]) for n, f in (c.text_measure or {}).items() if sid in (f.get("slots") or {}) and inner(n)}
        src = "slot"
        if not rects:
            rects = {n: m[sid] for n, m in c.measured.items() if sid in m and inner(n)}
            src = "rendered rect"
        if len(rects) < 2:
            continue
        ns = sorted(rects)
        ref = rects[ns[0]]
        for n in ns[1:]:
            dev = max(abs(rects[n][k] - ref[k]) for k in range(4))
            if dev > tol + 1e-6:
                out.append(fail("V-EXC", c.beat_id(n / c.fps), n / c.fps,
                                f"'{sid}' hard-swaps content (E6) but its {src} moves {dev:.0f} px at {n / c.fps:.2f} s "
                                f"(the container must stay constant +-{tol:g} px)",
                                f"keep '{sid}''s container fixed (fixed width/height; mark it data-slot) and change only its content"))
                break
    return out


EXC_CHECKS = {"E1": _e1, "E2": _e2, "E4": _e4, "E5": _e5, "E6": _e6}   # E3 is checked by V-TYPE


def rule_exc(c, p: dict):
    from .tokens import EXC_REGISTRY
    out = []
    declared = c.style.get("exceptions") or {}
    groups: dict[str, list] = {}
    for s in c.scenes:
        e = s.get("exception")
        if e is None or e is False:
            continue
        sid, t0 = s.get("id"), float(s.get("t_in", 0))
        bid = c.beat_id(t0)
        if not isinstance(e, str):
            out.append(fail("V-EXC", bid, t0, f"'{sid}' exception {e!r}: a scene names one exception id (a string)",
                            "use one id, e.g. exception: \"E3\" (split the scene if it needs two)"))
            continue
        eid = exc_id(s)
        if eid not in EXC_REGISTRY:
            out.append(fail("V-EXC", bid, t0, f"'{sid}' uses exception '{e}', which is not in the exception registry (E1-E6)",
                            "use a registry id, or add the new exception to STYLE-PLAYBOOK-STRUCTURE Part C.2 first"))
            continue
        if eid not in declared:
            out.append(fail("V-EXC", bid, t0, f"'{sid}' uses exception {eid}, which this playbook does not declare",
                            f"remove the exception from '{sid}' and meet the normal rule, or declare {eid} in tokens.json "
                            "`exceptions` (and playbook §2.2) for this style"))
            continue
        groups.setdefault(eid, []).append(s)
    for s in c.scenes:
        sid, t0 = s.get("id"), float(s.get("t_in", 0))
        # text behind the speaker is simply allowed (Naman, 8 Oct 2026): no exception needed
        if s.get("ambient") and 3 <= s.get("z", 0) <= 10 and exc_id(s) != "E4":
            out.append(fail("V-EXC", c.beat_id(t0), t0, f"'{sid}' is flagged ambient at z{s.get('z')} without declaring E4",
                            f"set exception: \"E4\" on '{sid}' (ambient field) or draw it at z1-2"))
    for eid, scs in groups.items():
        fn = EXC_CHECKS.get(eid)
        if fn:
            out += fn(c, declared[eid], scs)
    c.stats_extra["exceptions"] = {"declared": sorted(declared), "used": {k: [s.get("id") for s in v] for k, v in groups.items()}}
    return out


# --------------------------------------------------------------------------- global-check helpers
def g2_uncounted_text(s: dict) -> bool:
    return s.get("text_class") in G2_UNCOUNTED or bool(s.get("ambient"))
