"""`veos capture <url>`: screenshot of the creator's own local page (their app on localhost or a local file),
optionally a deterministic smooth-scroll video.

NC-7 / E-10: the engine never fetches anyone else's media, so capture is local-only: `file://` paths and loopback hosts
(localhost, 127.x.x.x, ::1, *.localhost). A public URL is refused (REMOTE_CAPTURE). Images and media a local page
requests from other hosts are blocked while capturing; ask the creator for their own screenshot instead.
"""
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


LOCAL_HOSTS = {"localhost", "127.0.0.1", "::1", "0.0.0.0", "[::1]"}


def is_local(url: str) -> bool:
    """True for file:// URLs, bare paths and loopback hosts; False for anything on the internet."""
    u = urlparse(url if "//" in url else "http://" + url)
    if u.scheme == "file":
        return True
    if u.scheme not in ("http", "https"):
        return False
    host = (u.hostname or "").lower()
    return host in LOCAL_HOSTS or host.endswith(".localhost") or host.startswith("127.")


def _local_url(raw: str) -> str:
    p = Path(raw).expanduser()
    if "//" not in raw and p.exists():
        return p.resolve().as_uri()
    return raw if "//" in raw else "http://" + raw


SIZE_RE = re.compile(r"^\s*(\d+)\s*[x×]\s*(\d+)\s*(?:@\s*(\d+(?:\.\d+)?)\s*x?)?\s*$", re.I)


def parse_size(size: str) -> tuple[int, int, float]:
    """`WxH` or `WxH@Nx` (CSS viewport px at device scale N) -> (w, h, scale). E.g. 1080x1920, 390x844@3x (a portrait
    phone screenshot of 1170x2532 px). The PNG is w*N x h*N px."""
    m = SIZE_RE.match(str(size or ""))
    if not m:
        raise VeosError("BAD_SIZE", f"bad --size {size}", "Use WxH or WxH@Nx, e.g. 1440x900, 1080x1920 or 390x844@3x.")
    w, h, k = int(m.group(1)), int(m.group(2)), float(m.group(3) or 1)
    if not (200 <= w <= 4000 and 200 <= h <= 4000):
        raise VeosError("BAD_SIZE", f"--size {size}: the viewport must be 200..4000 px each way", "E.g. 1080x1920 or 390x844@3x.")
    if not (1 <= k <= 4) or w * k > 8000 or h * k > 8000:
        raise VeosError("BAD_SIZE", f"--size {size}: the device scale must be 1..4 and the PNG at most 8000 px",
                        "E.g. 390x844@3x (1170x2532 px).")
    return w, h, (int(k) if k == int(k) else k)


def main(args, project) -> dict:
    project = need_project(project)
    url = _local_url(args.url)
    if not is_local(url):
        raise VeosError("REMOTE_CAPTURE", f"veos never fetches media from the internet ({args.url})",
                        "Capture only the creator's own page on localhost or a local file; for anything else ask the creator "
                        "for their own screenshot (`veos asset add <file> --origin creator`) or build a created card.")
    t = tools()
    from playwright.sync_api import Error as PwError
    from playwright.sync_api import sync_playwright

    name = args.name or _name(args.url)
    w, h, scale = parse_size(args.size)
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

            def _guard(route):   # local page, but no images / media pulled from other hosts
                rq = route.request
                if rq.resource_type in ("image", "media") and not is_local(rq.url) and not rq.url.startswith("data:"):
                    return route.abort()
                return route.continue_()
            page.route("**/*", _guard)
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
                        "Check that the local page is running (e.g. your dev server); if the browser is missing run `veos doctor`.") from e
    out["png_bytes"] = png.stat().st_size
    if mp4:
        out["mp4_bytes"] = mp4.stat().st_size
    out["url"] = url
    return out


def add_args(p, cmd: str) -> None:
    p.add_argument("url")
    p.add_argument("--name", default=None, help="file name (default: derived from the URL)")
    p.add_argument("--scroll", type=float, default=0.0, help="also record a smooth scroll video of this many seconds")
    p.add_argument("--size", default="1440x900", help="viewport WxH or WxH@Nx (device scale), e.g. 1080x1920 or 390x844@3x (default 1440x900)")
    p.add_argument("--mobile", action="store_true", help="390x844 viewport at device scale 3")
