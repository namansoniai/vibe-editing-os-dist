"""`veos captions apply|status`: write/inspect the per-word `caption` field in work/words.edit.json."""
from __future__ import annotations

import re
from pathlib import Path

from .core import VeosError, need_project, read_json, write_json

DEVANAGARI = re.compile(r"[ऀ-ॿ]")
LOW_P = 0.5


def add_args(p, cmd):
    p.add_argument("action", choices=["apply", "status"])
    p.add_argument("map", nargs="?", help='apply: JSON file {"<i>": "caption text"}; "" hides the word')


def _load(pr):
    f = pr.work / "words.edit.json"
    if not f.exists():
        raise VeosError("NO_WORDS_EDIT", "work/words.edit.json missing", "Run the rough cut (`veos cut`) first.")
    return f, read_json(f)


def _is_dev(w: dict) -> bool:
    return w.get("script") == "devanagari" or bool(DEVANAGARI.search(w.get("w", "")))


def _status(words: list[dict]) -> dict:
    no = [w for w in words if "caption" not in w]
    return {"words": len(words), "with_caption": len(words) - len(no),
            "devanagari_no_caption": sum(1 for w in no if _is_dev(w)),
            "low_confidence_no_caption": sum(1 for w in no if (w.get("p") if w.get("p") is not None else 1) < LOW_P)}


def main(args, project) -> dict:
    pr = need_project(project)
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
