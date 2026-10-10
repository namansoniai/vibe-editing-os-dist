"""`veos asset add|list`: per-reel assets (logos, images, screen recordings, B-roll) in <project>/plan/assets.

Images (png/jpg/webp/svg/...) are copied to plan/assets/<name>.<ext>  -> ctx.asset("<name>").
Videos are conformed to 30 fps and extracted as JPEG frames plan/assets/<name>/f%05d.jpg (zero-based, scaled to fit
1080 px wide, never upscaled) + plan/assets/<name>/meta.json {frames, fps, w, h, duration} -> ctx.videoFrame("<name>", seconds).

Origin (E-10): every asset is recorded in plan/assets.json `{version, assets: {name: {origin, kind, src, sha256, added,
source?}}}` with `--origin creator` (the creator's own file, or one they hold and hand over; the default),
`--origin created` (a visual Claude made locally) or `--source <url>` (a file fetched from the web: origin `fetched`, the
URL recorded as `source`). `asset add` takes a local file: download first (curl) or `veos capture <url>`, then add it.
"""
from __future__ import annotations

import hashlib
import json
import re
import shutil
import time
from pathlib import Path

from .core import FPS, VeosError, need_project, read_json, run, tools, write_json

IMAGE_EXT = {".png", ".jpg", ".jpeg", ".webp", ".svg", ".avif"}
VIDEO_EXT = {".mp4", ".mov", ".mkv", ".webm", ".m4v", ".avi", ".gif"}
MAX_W = 1080
ORIGINS = ("creator", "created", "fetched")
URL_RE = re.compile(r"^[a-z][a-z0-9+.-]*://", re.I)


def add_args(p, cmd):
    p.add_argument("action", choices=["add", "list"])
    p.add_argument("file", nargs="?", help="add: image or video file")
    p.add_argument("--name", help="add: asset name (default: file name without extension)")
    p.add_argument("--origin", choices=ORIGINS, default=None,
                   help="add: creator (the creator's own or handed-over file; default), created (made locally by Claude) "
                        "or fetched (from the web; needs --source)")
    p.add_argument("--source", default=None,
                   help="add: the URL the file was fetched from (sets origin fetched and records the URL)")


def _clean(name: str) -> str:
    s = re.sub(r"[^A-Za-z0-9_-]+", "-", name).strip("-")
    if not s:
        raise VeosError("BAD_NAME", f"'{name}' is not a usable asset name", "Use letters, digits, - or _.")
    return s


def _probe_wh(ffprobe: str, f: Path) -> tuple[int, int]:
    r = run([ffprobe, "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height", "-of", "json", str(f)])
    s = json.loads(r.stdout.decode())["streams"][0]
    return int(s["width"]), int(s["height"])


def _add_video(pr, src: Path, name: str) -> dict:
    t = tools()
    out = pr.root / "plan" / "assets" / name
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    vf = f"fps={FPS},scale='min({MAX_W},iw)':-2:flags=lanczos,format=yuvj420p"
    run([t.ffmpeg, "-v", "error", "-y", "-i", str(src), "-an", "-vf", vf, "-start_number", "0", "-q:v", "3",
         str(out / "f%05d.jpg")], pr, "asset")
    frames = len(list(out.glob("f*.jpg")))
    if frames < 1:
        raise VeosError("NO_FRAMES", f"no frames could be extracted from {src.name}", "Check that the file is a playable video.")
    w, h = _probe_wh(t.ffprobe, out / "f00000.jpg")
    meta = {"frames": frames, "fps": FPS, "w": w, "h": h, "duration": round(frames / FPS, 3)}
    write_json(out / "meta.json", meta)
    return {"name": name, "kind": "video", **meta, "dir": pr.rel(out)}


def _add_image(pr, src: Path, name: str) -> dict:
    dest = pr.path("plan", "assets", name + src.suffix.lower())
    shutil.copy2(src, dest)
    size = None
    if src.suffix.lower() != ".svg":
        try:
            size = list(_probe_wh(tools().ffprobe, dest))
        except Exception:  # noqa: BLE001 - size is informational only
            size = None
    return {"name": name, "kind": "image", "size": size, "file": pr.rel(dest)}


def _manifest_path(pr) -> Path:
    return pr.root / "plan" / "assets.json"


def _record(pr, name: str, kind: str, src: Path, origin: str, source: str | None = None) -> dict:
    """Write the asset's origin to plan/assets.json (read by V-INSERTS)."""
    mp = _manifest_path(pr)
    data = read_json(mp) if mp.exists() else {}
    if not isinstance(data, dict):
        data = {}
    h = hashlib.sha256()
    with open(src, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    rec = {"origin": origin, "kind": kind, "src": src.name, "sha256": h.hexdigest(),
           "added": time.strftime("%Y-%m-%dT%H:%M:%S")}
    if source:
        rec["source"] = source
    data = {"version": 1, "assets": {**(data.get("assets") or {}), name: rec}}
    write_json(mp, data)
    return rec


def _list(pr) -> dict:
    adir = pr.root / "plan" / "assets"
    mp = _manifest_path(pr)
    origins = (read_json(mp).get("assets") or {}) if mp.exists() else {}
    items = []
    if adir.is_dir():
        for f in sorted(adir.iterdir()):
            if f.is_dir() and (f / "meta.json").exists():
                items.append({"name": f.name, "kind": "video", **read_json(f / "meta.json")})
            elif f.is_file():
                items.append({"name": f.stem, "kind": "image" if f.suffix.lower() in IMAGE_EXT else "file", "file": f.name})
    for it in items:
        rec = origins.get(it["name"]) or {}
        it["origin"] = rec.get("origin")
        if rec.get("source"):
            it["source"] = rec["source"]
    return {"assets": items}


def main(args, project) -> dict:
    pr = need_project(project)
    if args.action == "list":
        return _list(pr)
    if not args.file:
        raise VeosError("NO_FILE", "asset add needs a file", "Example: veos asset add demo.mp4 --project P --name demo")
    if URL_RE.match(str(args.file)):
        raise VeosError("NOT_A_FILE", "asset add takes a local file, not a URL",
                        f"Download it into the project first (curl.exe -L -o <file> \"{args.file}\"), or screenshot the page "
                        f"with `veos capture \"{args.file}\" --out <file>`, then `veos asset add <file> --source \"{args.file}\"`.")
    source = (getattr(args, "source", None) or "").strip() or None
    origin = getattr(args, "origin", None) or ("fetched" if source else "creator")
    if origin not in ORIGINS:
        raise VeosError("BAD_ORIGIN", f"origin '{origin}' is not allowed", "Use --origin creator, --origin created or --source <url>.")
    if origin == "fetched" and not source:
        raise VeosError("NO_SOURCE", "a fetched asset records where it came from",
                        "Add --source <url> (the page or file URL it was fetched from).")
    if source and origin != "fetched":
        raise VeosError("BAD_ORIGIN", f"--source records a fetched file, but --origin is {origin}",
                        "Drop --origin (a --source file is origin fetched), or drop --source for the creator's own file.")
    src = Path(args.file).expanduser()
    if not src.is_file():
        raise VeosError("INPUT_MISSING", f"not found: {args.file}", "Check the path (quote paths with spaces).")
    name = _clean(args.name or src.stem)
    ext = src.suffix.lower()
    if ext in VIDEO_EXT:
        out = _add_video(pr, src, name)
    elif ext in IMAGE_EXT:
        out = _add_image(pr, src, name)
    else:
        out = None
    if out is not None:
        rec = _record(pr, name, out["kind"], src, origin, source)
        out["origin"] = rec["origin"]
        if source:
            out["source"] = source
        return out
    raise VeosError("BAD_ASSET_TYPE", f"{ext or 'this file'} is not a supported image or video",
                    "Use png/jpg/webp/svg images or mp4/mov/mkv/webm videos.")
