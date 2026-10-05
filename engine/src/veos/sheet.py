"""`veos sheet`: labelled contact sheets from t_NNNN.png frames, any images, or frames of an MP4."""
from __future__ import annotations

import re
import shutil
import tempfile
from pathlib import Path

from .core import FPS, VeosError, run, tools

IMG = {".png", ".jpg", ".jpeg", ".webp", ".bmp"}


def add_args(p, cmd):
    p.add_argument("paths", nargs="+", help="DIR OUT_PREFIX  (or just OUT_PREFIX when --video is used)")
    p.add_argument("--per", type=int, default=28, help="tiles per sheet")
    p.add_argument("--cols", type=int, default=7)
    p.add_argument("--tile", type=int, default=216, help="tile width in px")
    p.add_argument("--fps", type=float, default=FPS, help="fps used for the time label")
    p.add_argument("--video", help="MP4 to sample frames from (with --frames)")
    p.add_argument("--frames", help="comma list of frame numbers to take from --video")


def _extract(video: str, frames: list[int], tmp: Path) -> list[tuple[int, Path]]:
    nums = sorted(set(frames))
    sel = "+".join(f"eq(n\\,{n})" for n in nums)
    run([tools().ffmpeg, "-v", "error", "-y", "-i", video, "-vf", f"select='{sel}'", "-fps_mode", "passthrough",
         str(tmp / "x_%05d.png")])
    return list(zip(nums, sorted(tmp.glob("x_*.png"))))


def main(args, project):
    from PIL import Image, ImageDraw, ImageFont
    tmp = None
    try:
        if args.video:
            if not args.frames:
                raise VeosError("NO_FRAMES", "--video needs --frames", "Pass e.g. --frames 0,30,60.")
            out_prefix = args.paths[-1]
            tmp = Path(tempfile.mkdtemp(prefix="veos_sheet_"))
            items = _extract(args.video, [int(x) for x in args.frames.split(",") if x.strip()], tmp)
        else:
            if len(args.paths) != 2:
                raise VeosError("BAD_ARGS", "sheet needs DIR OUT_PREFIX", "e.g. veos sheet frames/ out/sheet")
            d, out_prefix = Path(args.paths[0]), args.paths[1]
            if not d.is_dir():
                raise VeosError("NO_DIR", f"not a folder: {d}", "Pass the folder of t_NNNN.png frames.")
            files = sorted(f for f in d.iterdir() if f.suffix.lower() in IMG)
            items = []
            for i, f in enumerate(files):
                m = re.match(r"^[A-Za-z_]*?(\d+)$", f.stem)
                items.append((int(m.group(1)) if m else i, f))
        if not items:
            raise VeosError("NO_IMAGES", "no images found", "Check the folder / --frames list.")
        Path(out_prefix).parent.mkdir(parents=True, exist_ok=True)
        tw, per, cols, lab = args.tile, args.per, args.cols, 22
        try:
            font = ImageFont.load_default(size=14)
        except TypeError:
            font = ImageFont.load_default()
        paths = []
        for s in range(0, len(items), per):
            chunk = items[s:s + per]
            with Image.open(chunk[0][1]) as first:
                th = round(tw * first.height / first.width)
            rows = -(-len(chunk) // cols)
            sheet = Image.new("RGB", (cols * tw, rows * (th + lab)), (40, 40, 40))
            dr = ImageDraw.Draw(sheet)
            for i, (n, f) in enumerate(chunk):
                with Image.open(f) as im:
                    im = im.convert("RGB").resize((tw, th), Image.LANCZOS)
                x, y = (i % cols) * tw, (i // cols) * (th + lab)
                sheet.paste(im, (x, y + lab))
                dr.text((x + 4, y + 3), f"{n}  {n / args.fps:.2f}s", fill=(255, 255, 0), font=font)
            p = f"{out_prefix}_{s // per}.jpg"
            sheet.save(p, quality=88)
            paths.append(project.rel(p) if project else Path(p).resolve().as_posix())
        return {"images": len(items), "sheets": paths}
    finally:
        if tmp:
            shutil.rmtree(tmp, ignore_errors=True)
