"""Does this reel need the person cut-out, and is it ready? One answer for `veos matte --if-needed`, `veos validate`
and the plugin.

The renderer draws the cut-out (work/frames/c*.webp, made by `veos prep-frames` from work/matte/<id>.mp4) only on a
frame that shows the footage AND has a scene behind the presenter (`behind: true`: the depth sandwich, E1
behind-subject text included) or a card / pip stage whose `breakout` lets the head rise over the window's top edge
(renderer/core.js composeFrame: needCut). Nothing else reads it: grades, freezes and the footage blur only re-use the
cut-out where it is drawn anyway, and textmeasure's E1 occlusion pass needs it for those same behind scenes.
A voice-over reel has no presenter, and a conversation reel's composed multi-camera footage has no cut-out layer.
"""
from __future__ import annotations

from pathlib import Path

from .core import FPS, read_json

BREAKOUT_ENGINES = ("card", "pip")


def _read(path: Path, default=None):
    try:
        return read_json(path) if path.exists() else default
    except ValueError:
        return default


def _f(t) -> int:
    return int(round(float(t) * FPS))


def plan_scenes(pr) -> list[dict]:
    """The scenes the reel will have: the planner's plan/scenes.plan.json, else the registered plan/scenes.meta.json."""
    for name in ("scenes.plan.json", "scenes.meta.json"):
        d = _read(pr.root / "plan" / name)
        if isinstance(d, dict) and isinstance(d.get("scenes"), list):
            d = d["scenes"]
        if isinstance(d, list):
            return [s for s in d if isinstance(s, dict)]
    return []


def _breakout(v) -> bool:
    if isinstance(v, dict):
        v = v.get("px", True)
    return v is True or (isinstance(v, (int, float)) and not isinstance(v, bool) and v > 0)


def breakout_spans(tl: dict, tokens: dict | None) -> list[tuple[int, int]]:
    """Edit-frame spans [a, b) whose stage is a card / pip window with a head breakout (layouts.js resolve: the
    layout's tokens, then the entry's `p`, then its inline keys; `presenter.breakout` counts too)."""
    layouts = (tokens or {}).get("layouts") or {}
    stage = [e for e in (tl.get("stage") or []) if isinstance(e, dict)]
    stage.sort(key=lambda e: float(e.get("t") or 0))
    end = _f((tl.get("meta") or {}).get("duration") or 0) or int((tl.get("meta") or {}).get("frames") or 0)
    spans = []
    for i, e in enumerate(stage):
        lid = str(e.get("layout") or "full")
        tok = layouts.get(lid) if isinstance(layouts.get(lid), dict) else {}
        engine = lid if lid in BREAKOUT_ENGINES else tok.get("engine")
        if engine not in BREAKOUT_ENGINES:
            continue
        p = e.get("p") if isinstance(e.get("p"), dict) else {}
        cands = [tok.get("breakout"), (tok.get("presenter") or {}).get("breakout") if isinstance(tok.get("presenter"), dict) else None,
                 p.get("breakout"), (p.get("presenter") or {}).get("breakout") if isinstance(p.get("presenter"), dict) else None,
                 e.get("breakout")]
        on = next((c for c in reversed(cands) if c is not None), None)  # the later source wins, as in layouts.js
        if _breakout(on):
            a = _f(e.get("t") or 0)
            b = _f(stage[i + 1].get("t") or 0) if i + 1 < len(stage) else end
            if b > a:
                spans.append((a, b))
    return spans


def needs_cutout(pr, scenes: list[dict] | None = None, tl: dict | None = None) -> dict:
    """{"needed", "why": [plain sentences], "behind": [scene ids], "breakout_at": [s], "frames": [[a, b), ...] edit
    frames that draw the cut-out, "style": tokens footage.matte, "unavailable": True for a conversation reel that asks
    for it}."""
    tl = tl if tl is not None else _read(pr.root / "plan" / "timeline.json", {}) or {}
    scenes = scenes if scenes is not None else plan_scenes(pr)
    tokens = _read(pr.work / "tokens.json")
    style = ((tokens or {}).get("footage") or {}).get("matte")
    out = {"needed": False, "why": [], "behind": [], "breakout_at": [], "frames": [], "style": style}
    sources = _read(pr.work / "sources.json", {}) or {}
    if sources.get("source_type") == "voiceover_only":
        out["why"] = ["voice-over reel: there is no presenter to cut out"]
        return out
    behind = [s for s in scenes if s.get("behind") and s.get("id")]
    spans = breakout_spans(tl, tokens)
    frames = sorted({(_f(s.get("t_in") or 0), _f(s.get("t_out") or 0)) for s in behind} | set(spans))
    out.update({"behind": [s["id"] for s in behind], "breakout_at": [round(a / FPS, 3) for a, _ in spans],
                "frames": [list(x) for x in frames if x[1] > x[0]]})
    if not behind and not spans:
        out["why"] = ["no scene sits behind the presenter and no stage lets the head break out of its window"]
        return out
    why = []
    if behind:
        names = ", ".join(f"'{i}'" for i in out["behind"][:6]) + (" ..." if len(behind) > 6 else "")
        why.append(f"{len(behind)} scene{'s' if len(behind) > 1 else ''} sit{'' if len(behind) > 1 else 's'} behind the presenter ({names})")
    if spans:
        why.append("the stage lets the head break out of its window at " + ", ".join(f"{t:g} s" for t in out["breakout_at"][:4]))
    from .compose import composed_ready
    if composed_ready(pr):
        out.update({"unavailable": True,
                    "why": why + ["but a conversation reel's multi-camera footage has no cut-out layer"]})
        return out
    out.update({"needed": True, "why": why})
    return out


def cutout_ready(pr, need: dict, tl: dict | None = None) -> list[str]:
    """What is missing for the frames `need` says draw the cut-out: [] when it is ready. Checks that every footage
    source the cut uses has a cut-out covering the frames the cut keeps, and that work/frames has the cut-out frames."""
    from .matte import _matte_done, covers, kept_ranges
    tl = tl if tl is not None else _read(pr.root / "plan" / "timeline.json", {}) or {}
    cut = _read(pr.work / "cutmap.json")
    sources = {s.get("id"): s for s in (_read(pr.work / "sources.json", {}) or {}).get("sources", []) if isinstance(s, dict)}
    if not cut or not sources:
        return []  # no footage project (a test plan, or nothing cut yet): nothing to check against
    missing = []
    for sid in sorted({seg.get("src") for seg in cut.get("segments") or []}):
        src = sources.get(sid) or {}
        if src.get("kind") != "talking-head":
            continue
        done = _matte_done(pr, sid)
        want = kept_ranges(cut, sid, int(src.get("frames") or 10**9))
        if done is None:
            missing.append(f"source {sid} has no cut-out yet")
        elif not covers(done, want):
            missing.append(f"the cut-out of source {sid} does not cover the frames the cut keeps now (the cut changed)")
    if missing:
        return missing
    fdir = pr.abs(((tl.get("inputs") or {}).get("frames")) or "work/frames/")
    nf = int(cut.get("frames") or 0)
    lacking = [n for a, b in need.get("frames") or [] for n in range(max(0, a), min(nf, b))
               if not (Path(fdir) / f"c{n:05d}.webp").exists()]
    if lacking:
        missing.append(f"{len(lacking)} frames have no cut-out picture yet (first: frame {lacking[0]})")
    return missing


FIX = "Run `veos matte --if-needed --project P`, then `veos prep-frames --project P`."
