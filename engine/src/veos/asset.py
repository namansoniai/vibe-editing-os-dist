"""`veos asset add|list`: per-reel assets (logos, images, screen recordings, B-roll) in <project>/plan/assets.

Images (png/jpg/webp/svg/...) are copied to plan/assets/<name>.<ext>  -> ctx.asset("<name>").
Videos are conformed to 30 fps and extracted as JPEG frames plan/assets/<name>/f%05d.jpg (zero-based, scaled to fit
1080 px wide, never upscaled) + plan/assets/<name>/meta.json {frames, fps, w, h, duration} -> ctx.videoFrame("<name>", seconds).
"""
from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

from .core import FPS, VeosError, need_project, read_json, run, tools, write_json

IMAGE_EXT = {".png", ".jpg", ".jpeg", ".webp", ".svg", ".avif"}
VIDEO_EXT = {".mp4", ".mov", ".mkv", ".webm", ".m4v", ".avi", ".gif"}
MAX_W = 1080


def add_args(p, cmd):
    p.add_argument("action", choices=["add", "list"])
    p.add_argument("file", nargs="?", help="add: image or video file")
    p.add_argument("--name", help="add: asset name (default: file name without extension)")


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


def _list(pr) -> dict:
    adir = pr.root / "plan" / "assets"
    items = []
    if adir.is_dir():
        for f in sorted(adir.iterdir()):
            if f.is_dir() and (f / "meta.json").exists():
                items.append({"name": f.name, "kind": "video", **read_json(f / "meta.json")})
            elif f.is_file():
                items.append({"name": f.stem, "kind": "image" if f.suffix.lower() in IMAGE_EXT else "file", "file": f.name})
    return {"assets": items}


def main(args, project) -> dict:
    pr = need_project(project)
    if args.action == "list":
        return _list(pr)
    if not args.file:
        raise VeosError("NO_FILE", "asset add needs a file", "Example: veos asset add demo.mp4 --project P --name demo")
    src = Path(args.file).expanduser()
    if not src.is_file():
        raise VeosError("INPUT_MISSING", f"not found: {args.file}", "Check the path (quote paths with spaces).")
    name = _clean(args.name or src.stem)
    ext = src.suffix.lower()
    if ext in VIDEO_EXT:
        return _add_video(pr, src, name)
    if ext in IMAGE_EXT:
        return _add_image(pr, src, name)
    raise VeosError("BAD_ASSET_TYPE", f"{ext or 'this file'} is not a supported image or video",
                    "Use png/jpg/webp/svg images or mp4/mov/mkv/webm videos.")
