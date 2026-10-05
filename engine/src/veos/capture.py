"""`veos capture <url>`: screenshot of a web page, optionally a deterministic smooth-scroll video."""
from __future__ import annotations

import re
import subprocess
from pathlib import Path
from urllib.parse import urlparse

from .core import FPS, VeosError, need_project, r3, tools


def _name(url: str) -> str:
    u = urlparse(url if "//" in url else "https://" + url)
    s = re.sub(r"[^a-zA-Z0-9]+", "-", (u.netloc + u.path).strip("/")).strip("-").lower()
    return s or "capture"


def main(args, project) -> dict:
    project = need_project(project)
    t = tools()
    from playwright.sync_api import Error as PwError
    from playwright.sync_api import sync_playwright

    url = args.url if "//" in args.url else "https://" + args.url
    name = args.name or _name(args.url)
    try:
        w, h = (int(x) for x in args.size.lower().split("x"))
    except ValueError as e:
        raise VeosError("BAD_SIZE", f"bad --size {args.size}", "Use WxH, e.g. 1440x900.") from e
    scale = 1
    if args.mobile:
        w, h, scale = 390, 844, 3
    png = project.path("work", "captures", f"{name}.png")
    mp4 = project.path("work", "captures", f"{name}.mp4") if args.scroll else None
    out: dict = {}
    try:
        with sync_playwright() as pw:
            b = pw.chromium.launch(headless=True)
            ctx = b.new_context(viewport={"width": w, "height": h}, device_scale_factor=scale, is_mobile=bool(args.mobile),
                                has_touch=bool(args.mobile))
            page = ctx.new_page()
            page.goto(url, wait_until="networkidle", timeout=45000)
            page.evaluate("document.fonts.ready.then(() => true)")
            page.add_style_tag(content="html{scroll-behavior:auto !important}")
            page.wait_for_timeout(300)
            page.screenshot(path=str(png), full_page=False)
            out["png"] = project.rel(png)
            out["viewport"] = f"{w}x{h}@{scale}x"
            if mp4:
                total = page.evaluate("Math.max(document.documentElement.scrollHeight, document.body ? document.body.scrollHeight : 0)")
                dist = max(0, int(total) - h)
                n = max(2, int(round(FPS * args.scroll)))
                ff = subprocess.Popen(
                    [t.ffmpeg, "-y", "-v", "error", "-f", "image2pipe", "-framerate", str(FPS), "-c:v", "mjpeg", "-i", "-",
                     "-vf", "scale=trunc(iw/2)*2:trunc(ih/2)*2:out_color_matrix=bt709:out_range=tv,format=yuv420p",
                     "-c:v", "libx264", "-crf", "16", "-preset", "fast", "-r", str(FPS), "-colorspace", "bt709",
                     "-color_primaries", "bt709", "-color_trc", "bt709", "-movflags", "+faststart", str(mp4)],
                    stdin=subprocess.PIPE, stderr=subprocess.PIPE)
                try:
                    for i in range(n):
                        u = i / (n - 1)
                        y = round(dist * (u * u * (3 - 2 * u)))  # smoothstep ease in/out, deterministic per frame
                        page.evaluate("y => new Promise(r => { window.scrollTo(0, y); requestAnimationFrame(() => requestAnimationFrame(r)); })", y)
                        ff.stdin.write(page.screenshot(type="jpeg", quality=92, full_page=False))
                finally:
                    ff.stdin.close()
                    err = ff.stderr.read().decode("utf-8", "replace")
                    ff.wait()
                if ff.returncode != 0:
                    raise VeosError("TOOL_FAILED", f"ffmpeg failed: {err.strip()[-200:]}", "See the capture log.")
                out.update(mp4=project.rel(mp4), frames=n, scroll_px=dist, seconds=r3(n / FPS))
            b.close()
    except PwError as e:
        msg = str(e).splitlines()[0][:200]
        raise VeosError("CAPTURE_FAILED", f"could not capture {url}: {msg}",
                        "Check the address and your internet connection; if the browser is missing run `veos doctor`.") from e
    out["png_bytes"] = png.stat().st_size
    if mp4:
        out["mp4_bytes"] = mp4.stat().st_size
    out["url"] = url
    return out


def add_args(p, cmd: str) -> None:
    p.add_argument("url")
    p.add_argument("--name", default=None, help="file name (default: derived from the URL)")
    p.add_argument("--scroll", type=float, default=0.0, help="also record a smooth scroll video of this many seconds")
    p.add_argument("--size", default="1440x900", help="viewport WxH (default 1440x900)")
    p.add_argument("--mobile", action="store_true", help="390x844 viewport at device scale 3")
