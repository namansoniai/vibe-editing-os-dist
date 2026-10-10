"""`veos capture <url>`: a screenshot of a web page (public http(s), the creator's app on localhost, or a local file),
of the visible viewport, the whole page (`--full-page`) or one element (`--selector <css>`), optionally a deterministic
smooth-scroll video. Uses the engine's bundled Playwright Chromium.

Output: `--out <file>` (.png / .jpg; relative paths resolve against the current folder), else
`work/captures/<name>.png` in the project. Fetching from the web is allowed (Naman, 10 Oct 2026): add the result to
the reel with `veos asset add <file> --source <url>`, which records where it came from.
Errors: no internet / unknown host / refused connection -> CAPTURE_OFFLINE; an HTTP error page (status >= 400) ->
CAPTURE_HTTP (never saved as if it were the page); a selector that matches nothing visible -> SELECTOR_NOT_FOUND; a page
that does not load within `--timeout` seconds -> CAPTURE_TIMEOUT.
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


OFFLINE_MARKERS = ("ERR_NAME_NOT_RESOLVED", "ERR_INTERNET_DISCONNECTED", "ERR_CONNECTION_REFUSED", "ERR_CONNECTION_RESET",
                   "ERR_ADDRESS_UNREACHABLE", "ERR_NETWORK_CHANGED", "ERR_CONNECTION_TIMED_OUT", "ERR_PROXY_CONNECTION_FAILED",
                   "ERR_NAME_RESOLUTION_FAILED", "ERR_TUNNEL_CONNECTION_FAILED", "ERR_CONNECTION_CLOSED")
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"


def _out_paths(args, project) -> tuple:
    """(screenshot path, scroll video path or None, rel(path) -> str for the summary)."""
    out = getattr(args, "out", None)
    if out:
        png = Path(out).expanduser()
        if not png.is_absolute():
            png = Path.cwd() / png
        if png.suffix.lower() not in (".png", ".jpg", ".jpeg"):
            raise VeosError("BAD_OUT", f"--out {out}: use a .png or .jpg file name", 'E.g. --out "P/plan/assets/faq.png".')
        png.parent.mkdir(parents=True, exist_ok=True)
        mp4 = png.with_suffix(".mp4") if args.scroll else None
        return png, mp4, str
    project = need_project(project)
    name = args.name or _name(args.url)
    png = project.path("work", "captures", f"{name}.png")
    mp4 = project.path("work", "captures", f"{name}.mp4") if args.scroll else None
    return png, mp4, project.rel


def capture_error(url: str, e: Exception, timeout_s: float) -> VeosError:
    """A Playwright failure as a VeosError a person can act on (offline, timeout, anything else)."""
    text = str(e) or type(e).__name__
    msg = text.splitlines()[0][:200]
    host = urlparse(url).hostname or url
    if any(m in text for m in OFFLINE_MARKERS):
        return VeosError("CAPTURE_OFFLINE", f"could not reach {host}: {msg}",
                         "Check the internet connection and the URL (for a local app, start its dev server), then retry.")
    if "Timeout" in type(e).__name__ or "Timeout" in msg:
        return VeosError("CAPTURE_TIMEOUT", f"{url} did not load within {timeout_s:g} s",
                         "Retry, or raise --timeout; for a slow page try the most direct URL (the article itself).")
    return VeosError("CAPTURE_FAILED", f"could not capture {url}: {msg}",
                     "Check the URL; if the browser is missing run `veos doctor`.")


def main(args, project) -> dict:
    url = _local_url(args.url)
    if urlparse(url).scheme not in ("http", "https", "file"):
        raise VeosError("BAD_URL", f"cannot capture {args.url}", "Use an http(s) URL, a localhost address or a local file.")
    selector = getattr(args, "selector", None)
    full = bool(getattr(args, "full_page", False))
    if selector and full:
        raise VeosError("BAD_ARGS", "--selector and --full-page do not combine",
                        "Use --selector for one element, or --full-page for the whole page.")
    if selector and args.scroll:
        raise VeosError("BAD_ARGS", "--selector and --scroll do not combine", "Capture the element, or scroll the page.")
    timeout_s = float(getattr(args, "timeout", None) or 30)
    tmo = max(1000, int(timeout_s * 1000))
    png, mp4, rel = _out_paths(args, project)
    t = tools()
    from playwright.sync_api import Error as PwError
    from playwright.sync_api import TimeoutError as PwTimeout
    from playwright.sync_api import sync_playwright

    w, h, scale = parse_size(args.size)
    if args.mobile:
        w, h, scale = 390, 844, 3
    out: dict = {}
    local = is_local(url)
    try:
        with sync_playwright() as pw:
            b = pw.chromium.launch(headless=True)
            try:
                opts = dict(viewport={"width": w, "height": h}, device_scale_factor=scale, is_mobile=bool(args.mobile),
                            has_touch=bool(args.mobile), locale="en-US")
                if not local and not args.mobile:
                    opts["user_agent"] = UA  # some sites refuse "HeadlessChrome"
                ctx = b.new_context(**opts)
                page = ctx.new_page()
                page.set_default_timeout(tmo)
                resp = page.goto(url, wait_until="load", timeout=tmo)
                if resp is not None and resp.status >= 400:
                    raise VeosError("CAPTURE_HTTP", f"{url} answered HTTP {resp.status}; nothing saved",
                                    "Open the URL in a browser (it may need a login or be gone); try another page with "
                                    "the same content.")
                try:  # wait for a quiet network when it comes; busy sites (analytics, sockets) never go idle
                    page.wait_for_load_state("networkidle", timeout=tmo if local else min(tmo, 8000))
                except PwTimeout:
                    pass
                page.evaluate("document.fonts.ready.then(() => true)")
                page.add_style_tag(content="html{scroll-behavior:auto !important}")
                page.wait_for_timeout(300)
                if selector:
                    loc = page.locator(selector).first
                    try:
                        loc.wait_for(state="visible", timeout=min(tmo, 10000))
                    except PwTimeout:
                        raise VeosError("SELECTOR_NOT_FOUND", f"no visible element matches {selector!r} on {url}",
                                        "Check the selector against the page's HTML, or capture the whole page with "
                                        "--full-page.") from None
                    loc.scroll_into_view_if_needed()
                    page.wait_for_timeout(200)
                    loc.screenshot(path=str(png))
                    out["selector"] = selector
                else:
                    page.screenshot(path=str(png), full_page=full)
                    out["full_page"] = full
                out["png"] = rel(png)
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
                    out.update(mp4=rel(mp4), frames=n, scroll_px=dist, seconds=r3(n / FPS))
            finally:
                b.close()
    except PwError as e:
        raise capture_error(url, e, timeout_s) from e
    out["png_bytes"] = png.stat().st_size
    if mp4:
        out["mp4_bytes"] = mp4.stat().st_size
    out["url"] = url
    return out


def add_args(p, cmd: str) -> None:
    p.add_argument("url")
    p.add_argument("--name", default=None, help="file name in work/captures (default: derived from the URL)")
    p.add_argument("--out", default=None, help="write the screenshot here (.png or .jpg) instead of work/captures/")
    p.add_argument("--selector", default=None, help="screenshot only the first visible element matching this CSS selector")
    p.add_argument("--full-page", dest="full_page", action="store_true", help="screenshot the whole scrolling page")
    p.add_argument("--timeout", type=float, default=30.0, help="seconds to wait for the page to load (default 30)")
    p.add_argument("--scroll", type=float, default=0.0, help="also record a smooth scroll video of this many seconds")
    p.add_argument("--size", default="1440x900", help="viewport WxH or WxH@Nx (device scale), e.g. 1080x1920 or 390x844@3x (default 1440x900)")
    p.add_argument("--mobile", action="store_true", help="390x844 viewport at device scale 3")
