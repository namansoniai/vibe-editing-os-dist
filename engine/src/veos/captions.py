"""`veos captions apply|status|build`.

apply|status: write / inspect the per-word `caption` field in work/words.edit.json.
build: run the caption profile engine (E-05, capengine.py) and write work/captions.json, the chunk list the renderer,
V-CADENCE, V-F0, V-CAPTION, V-TYPE and the storyboard read. `veos bundle` rebuilds it too, so it never goes stale.
Script text for `captions.transform`: --script FILE, else plan/captions.script.md|txt (the caption-language text for
translate), else the project's script (project.json `script`, or script.md next to the project / its clips).
"""
from __future__ import annotations

import re
from pathlib import Path

from .core import VeosError, need_project, read_json, write_json

DEVANAGARI = re.compile(r"[ऀ-ॿ]")
LOW_P = 0.5


def add_args(p, cmd):
    p.add_argument("action", choices=["apply", "status", "build"])
    p.add_argument("map", nargs="?", help='apply: JSON file {"<i>": "caption text"}; "" hides the word')
    p.add_argument("--script", help="build: script text for captions.transform (transliterate / translate)")
    p.add_argument("--timeline", help="build: timeline (default plan/timeline.json; optional)")


def _load(pr):
    f = pr.work / "words.edit.json"
    if not f.exists():
        raise VeosError("NO_WORDS_EDIT", "work/words.edit.json missing", "Run the rough cut (`veos cut`) first.")
    return f, read_json(f)


def _is_dev(w: dict) -> bool:
    return w.get("script") == "devanagari" or bool(DEVANAGARI.search(w.get("w", "")))


def _status(words: list[dict]) -> dict:
    no = [w for w in words if "caption" not in w]
    from .langs import script_of
    regional: dict[str, int] = {}
    for w in no:
        sc = script_of(str(w.get("w", "")))
        if sc not in ("latin", "devanagari", "other"):
            regional[sc] = regional.get(sc, 0) + 1
    return {"words": len(words), "with_caption": len(words) - len(no),
            "devanagari_no_caption": sum(1 for w in no if _is_dev(w)),
            "regional_script_no_caption": regional,
            "low_confidence_no_caption": sum(1 for w in no if (w.get("p") if w.get("p") is not None else 1) < LOW_P)}


def _script_text(pr, explicit: str | None, transform: str) -> list[str] | None:
    from .captext import parse_script
    cands = []
    if explicit:
        cands.append(Path(explicit))
    cands += [pr.root / "plan" / "captions.script.md", pr.root / "plan" / "captions.script.txt"]
    if transform != "translate":
        pj = pr.root / "project.json"
        try:
            sp = read_json(pj).get("script") if pj.exists() else None
        except ValueError:
            sp = None
        if sp:
            cands.append(pr.abs(sp))
        cands += [pr.root / "script.md", pr.root.parent / "script.md"]
    for c in cands:
        if c and Path(c).exists():
            txt = Path(c).read_text(encoding="utf-8-sig")
            sents = parse_script(txt) if Path(c).suffix.lower() == ".md" else [x.strip() for x in txt.splitlines() if x.strip()]
            if sents:
                return sents
    return None


def build_project(pr, tl: dict | None = None, *, script: str | None = None, write: bool = True) -> dict:
    """Build work/captions.json for a project (used by `veos captions build` and `veos bundle`)."""
    from . import capengine
    from .glossary import load_glossary
    if tl is None:
        tp = pr.root / "plan" / "timeline.json"
        tl = read_json(tp) if tp.exists() else {}
    tok_p = pr.work / "tokens.json"
    if not tok_p.exists():
        raise VeosError("NO_TOKENS", "work/tokens.json missing", "Run `veos tokens --project P` first.")
    tokens = read_json(tok_p)
    inp = tl.get("inputs") or {}
    wp = pr.abs(inp.get("words") or "work/words.edit.json")
    words = read_json(wp) if wp.exists() else {"words": []}
    face = None
    fp = pr.abs(inp.get("face") or "work/face.edit.json")
    if fp.exists():
        try:
            fd = read_json(fp)
            face = fd.get("boxes") if isinstance(fd, dict) else fd
        except ValueError:
            face = None
    from .framing import apply_boxes, for_reel  # E-16b: face boxes as the reframed full stage shows them
    face = apply_boxes(face, for_reel(tokens, tl, face))
    scenes = None
    sm = pr.root / "plan" / "scenes.meta.json"
    if sm.exists():
        try:
            d = read_json(sm)
            scenes = d.get("scenes") if isinstance(d, dict) else d
        except ValueError:
            scenes = None
    frames = pr.abs(inp.get("frames") or "work/frames/")
    cfg = capengine.resolve_config(tokens, tl)
    # Latin-script captions read the script too: it spells the Devanagari words Whisper wrote (capengine.caption_words)
    sents = _script_text(pr, script, cfg.transform) if cfg.transform in ("transliterate", "translate") or cfg.latin else None
    gl = load_glossary(pr.root / "plan" / "glossary.json" if (pr.root / "plan" / "glossary.json").exists() else None)
    out = capengine.build(tokens, tl, words, face=face, scenes=scenes, frames_dir=frames if frames.exists() else None,
                          script=sents, glossary_terms=gl.get("terms"))
    out["inputs"] = {"words": pr.rel(wp), "script": bool(sents)}
    if write:
        write_json(pr.work / "captions.json", out)
    return out


def main(args, project) -> dict:
    pr = need_project(project)
    if args.action == "build":
        tl = None
        if getattr(args, "timeline", None):
            tp = Path(args.timeline) if Path(args.timeline).exists() else pr.root / args.timeline
            tl = read_json(tp)
        out = build_project(pr, tl, script=getattr(args, "script", None))
        return {"out": "work/captions.json", "mode": out["mode"], "legacy": out["legacy"], "default": out["default"],
                "chunks": len(out["chunks"]), "stats": out.get("stats"), "warnings": out.get("warnings", [])}
    f, data = _load(pr)
    words = data.get("words", [])
    if args.action == "status":
        return _status(words)
    if not args.map:
        raise VeosError("NO_MAP", "captions apply needs a map.json", "Pass a JSON file like {\"3\": \"website\"}.")
    mp = Path(args.map)
    if not mp.exists():
        raise VeosError("INPUT_MISSING", f"map not found: {args.map}", "Check the path.")
    m = read_json(mp)
    if not isinstance(m, dict):
        raise VeosError("BAD_MAP", "map must be a JSON object {\"<i>\": \"text\"}", "")
    by_i = {w["i"]: w for w in words}
    missing = []
    for k, v in m.items():
        try:
            i = int(k)
        except ValueError:
            missing.append(k)
            continue
        if i not in by_i:
            missing.append(i)
        elif not isinstance(v, str):
            raise VeosError("BAD_MAP", f"caption for {k} must be a string", "Use \"\" to hide a word.")
    if missing:
        raise VeosError("MISSING_INDICES", f"{len(missing)} word index(es) not in words.edit.json: {missing[:20]}",
                        f"Valid indices are 0..{max(by_i) if by_i else -1}. Nothing was written.")
    for k, v in m.items():
        by_i[int(k)]["caption"] = v
    write_json(f, data)
    st = _status(words)
    return {"applied": len(m), "missing": [], "total": len(m), "words": st["words"],
            "still_without_caption": st["words"] - st["with_caption"]}
