/* Vibe Editing OS worlds (E-07, structure §3.1, tokens.schema §3.6). Builds the background behind (or instead of) the
   presenter from tokens.worlds. Pure string building: loaded by player.html before core.js (window.VEOS_WORLDS) and by
   node in the engine tests (module.exports).

   tokens.worlds["W-…"] = {kind, bg, top, bottom | gradient: {stops:[...], angle} | {radial: {...}} | "<tokens.gradients id>",
     grid: {pitch, colour, alpha, width, dash:[a,b], dot: true|r, major: {every | pitch, colour, alpha, width, dash},
       fade: true | outer | {x, y, inner, outer, min} (radial fade-out; also on dots)},
     dots: {pitch | [px, py], colour, alpha, r, shape: "dot" | "dash", w, h (dash size, rounded ends)},
     disc: {cx, cy, r, centre, edge, bg: [top, bottom] | colour} (a hard-edged sun / backdrop disc, e.g. a CTA poster),
     glow: {colour, alpha, r, x, y, drift:[ax, ay, fx, fy]}, noise: 0..1, vignette: 0..1, texture: "<asset id>",
     texture_opacity, footage: {blur, brightness, pad} (kind footage: a blurred copy of the frame behind a smaller stage)}
   Colours are role names (tokens.colours) or hex. Theme packs merge into worlds in the loader (`veos tokens`).

   v1 mapping: without tokens.worlds the three v1 worlds are defined here (studio, canvas, data) from the v1 roles and
   layout.canvas_grid / layout.night_grid; they produce the same markup as the v1 hard-coded worlds, so v1 reels render
   identically. They also stay available as fallbacks when a v3 file does not define them.
*/
(function (root, factory) {
  const m = factory();
  if (typeof module === "object" && module.exports) module.exports = m; else root.VEOS_WORLDS = m;
})(typeof self !== "undefined" ? self : this, function () {
  "use strict";
  const W = 1080, H = 1920;
  const r2 = v => Math.round(v * 100) / 100;
  const isNum = v => typeof v === "number" && isFinite(v);

  function legacyDefs(T) {
    const L = (T && T.layout) || {};
    return {
      studio: { kind: "footage", bg: "ink", footage: { blur: 28, brightness: 0.45, pad: 60 }, _v1: true },
      canvas: { kind: "canvas", bg: "canvas", grid: { pitch: L.canvas_grid || 141, colour: "grid", width: 2, dash: [14, 10] }, _v1: true },
      data: { kind: "stage", bg: "night", dots: { pitch: L.night_grid || 60, colour: "data", alpha: 0.10, r: 2.2 },
        glow: { colour: "data", alpha: 0.14, r: 350, x: 540, y: 560, drift: [20, 20, 0.7, 0.5] }, _v1: true },
    };
  }

  /* env: {T, col(role)->hex|string, hexA(role, a)->rgba, asset(id)->url, noiseUrl()->dataURL|""} */
  function create(env) {
    const T = env.T || {}, col = env.col, hexA = env.hexA;
    const defs = Object.assign(legacyDefs(T), T.worlds || {});
    const ids = Object.keys(defs);
    const v3ids = Object.keys(T.worlds || {});
    const cache = {};
    const dflt = T.worlds && Object.keys(T.worlds).length ? ("studio" in T.worlds ? "studio" : v3ids[0]) : "studio";
    const rgba = (c, a) => {
      const h = String(col(c) || "");
      if (/^#[0-9a-f]{6}$/i.test(h)) return hexA(h, a);
      if (/^#[0-9a-f]{3}$/i.test(h)) return hexA("#" + h.slice(1).split("").map(x => x + x).join(""), a);
      return h;
    };
    /* a gradient stop: "role" | "#hex" | [colour, position 0..1] */
    const stopCss = c => (Array.isArray(c) ? `${col(c[0])}${isNum(c[1]) ? " " + r2(c[1] * 100) + "%" : ""}` : col(c));
    function bgCss(d) {
      let g = d.gradient;
      if (typeof g === "string" && T.gradients && T.gradients[g]) g = { stops: T.gradients[g] };
      if (!g && (d.top || d.bottom)) g = { stops: [d.top || d.bg || "#000000", d.bottom || d.bg || "#000000"], angle: 180 };
      if (g && g.radial) { // x / y in px, or fractions of the frame (<= 1)
        const R = g.radial, st = (R.stops || g.stops || []).map(stopCss).join(",");
        const px = (v, full, dflt) => (v == null ? dflt : isNum(v) && v > 0 && v <= 1 ? r2(v * full) : v);
        return `radial-gradient(circle at ${px(R.x, W, 540)}px ${px(R.y, H, 760)}px,${st})`;
      }
      if (g && Array.isArray(g.stops) && g.stops.length) return `linear-gradient(${isNum(g.angle) ? g.angle : 180}deg,${g.stops.map(stopCss).join(",")})`;
      return col(d.bg || "night");
    }
    function gridSvg(gd) {
      const p = gd.pitch || 120, off = gd.offset || p; let ln = "";
      for (let x = off; x < W; x += p) ln += `<line x1="${x}" y1="0" x2="${x}" y2="${H}"/>`;
      for (let y = off; y < H; y += p) ln += `<line x1="0" y1="${y}" x2="${W}" y2="${y}"/>`;
      const dash = Array.isArray(gd.dash) && gd.dash.length === 2 ? ` stroke-dasharray="${gd.dash[0]} ${gd.dash[1]}"` : "";
      const op = isNum(gd.alpha) && gd.alpha < 1 ? ` stroke-opacity="${gd.alpha}"` : "";
      const minor = `<svg width="${W}" height="${H}" style="position:absolute;left:0;top:0" stroke="${col(gd.colour || "grid")}" stroke-width="${gd.width || 2}"${dash}${op} fill="none">${ln}</svg>`;
      if (!gd.major) return minor;
      // a second, heavier layer: a major line every `every` px (a multiple of the pitch; blueprint grids: 30 / 120)
      const M = gd.major === true ? {} : gd.major, mp = M.every || M.pitch || p * 4;
      return minor + gridSvg({ pitch: mp, offset: M.offset || (off % mp === 0 ? off : mp), colour: M.colour || gd.colour, alpha: isNum(M.alpha) ? M.alpha : gd.alpha,
        width: M.width || (gd.width || 2) * 2, dash: M.dash || null });
    }
    /* grid.fade (fx-helpers, whiteboard-split): the pattern fades out radially from a centre. fade: true | outer (0..1 of
       the frame height) | {x, y (px, or fractions <= 1), inner, outer (px, or fractions of the frame height <= 1), min (edge alpha)} */
    function fadeSpec(f) {
      if (f == null || f === false) return null;
      const F = f === true ? {} : isNum(f) ? { outer: f } : f;
      const px = (v, full, dflt) => (!isNum(v) ? dflt : v > 0 && v <= 1 ? v * full : v);
      const x = px(F.x, W, 540), y = px(F.y, H, 960), inner = px(F.inner, H, 0.12 * H), outer = Math.max(inner + 1, px(F.outer, H, 0.55 * H));
      return { x: r2(x), y: r2(y), inner: r2(inner), outer: r2(outer), min: isNum(F.min) ? Math.min(1, Math.max(0, F.min)) : 0 };
    }
    function fadeWrap(gd, html) {
      const f = fadeSpec(gd.fade);
      if (!f) return html;
      const m = `radial-gradient(circle at ${f.x}px ${f.y}px,rgba(0,0,0,1) ${f.inner}px,rgba(0,0,0,${f.min}) ${f.outer}px)`;
      return `<div style="position:absolute;inset:0;-webkit-mask-image:${m};mask-image:${m}">${html}</div>`;
    }
    function dotsDiv(dd) {
      if (dd.shape === "dash") return dashDiv(dd);
      const r = isNum(dd.r) ? dd.r : (isNum(dd.dot) ? dd.dot : 2.2), a = isNum(dd.alpha) ? dd.alpha : 0.10;
      const p = Array.isArray(dd.pitch) ? dd.pitch[0] : dd.pitch || 60, q = Array.isArray(dd.pitch) ? dd.pitch[1] : p;
      return `<div style="position:absolute;inset:0;background-image:radial-gradient(circle,${rgba(dd.colour || "grid", a)} ${r}px,transparent ${r2(r + 0.6)}px);background-size:${p}px ${q}px;background-position:${p / 2}px ${q / 2}px"></div>`;
    }
    /* rounded dashes on an x / y pitch (lesson-frame page texture: 14 x 7 px dashes, pitch 29.5 x 24.7) */
    function dashDiv(dd) {
      const pp = Array.isArray(dd.pitch) ? dd.pitch : [dd.pitch || 28, dd.pitch || 28], px = pp[0], py = pp[1];
      const w = isNum(dd.w) ? dd.w : 14, h = isNum(dd.h) ? dd.h : 7, a = isNum(dd.alpha) ? dd.alpha : 1;
      const rx = isNum(dd.r) ? Math.min(dd.r, h / 2) : h / 2;
      const svg = `<svg xmlns='http://www.w3.org/2000/svg' width='${px}' height='${py}'><rect x='${r2((px - w) / 2)}' y='${r2((py - h) / 2)}' width='${w}' height='${h}' rx='${rx}' fill='${rgba(dd.colour || "grid", a)}'/></svg>`;
      return `<div style="position:absolute;inset:0;background-image:url(&quot;data:image/svg+xml;charset=utf-8,${encodeURIComponent(svg)}&quot;);background-size:${px}px ${py}px;background-position:${r2(px / 2)}px ${r2(py / 2)}px"></div>`;
    }
    /* a hard-edged disc (sun / colour wall) over a field: CTA poster backdrops (cinematic-vlog-type W-poster) */
    function discHTML(D) {
      const cx = isNum(D.cx) ? D.cx : 540, cy = isNum(D.cy) ? D.cy : 960, r = isNum(D.r) ? D.r : 480;
      const c0 = col(D.centre || D.colour || "accent"), c1 = col(D.edge || D.centre || D.colour || "accent");
      let s = "";
      if (D.bg) s += `<div style="position:absolute;inset:0;background:${Array.isArray(D.bg) ? `linear-gradient(180deg,${D.bg.map(stopCss).join(",")})` : col(D.bg)}"></div>`;
      s += `<div style="position:absolute;left:${r2(cx - r)}px;top:${r2(cy - r)}px;width:${r2(2 * r)}px;height:${r2(2 * r)}px;border-radius:50%;background:radial-gradient(circle at 50% 50%,${c0} 0,${c1} 100%)${D.glow ? `;box-shadow:0 0 ${D.glow}px ${rgba(c1, 0.5)}` : ""}"></div>`;
      return s;
    }
    /* static part of a world (cached per id) */
    function staticHTML(id) {
      if (cache[id] != null) return cache[id];
      const d = defs[id] || {};
      let s = `<div style="position:absolute;inset:0;background:${bgCss(d)}"></div>`;
      if (d.texture) {
        const u = env.asset ? env.asset(d.texture) : "";
        if (u) s += `<div style="position:absolute;inset:0;background:url(${u}) center/cover;opacity:${isNum(d.texture_opacity) ? d.texture_opacity : 1}"></div>`;
      }
      if (d.disc) s += discHTML(d.disc);
      const grid = d.grid && !d.grid.dot ? d.grid : null, dots = d.dots || (d.grid && d.grid.dot ? d.grid : null);
      if (grid) s += fadeWrap(grid, gridSvg(grid));
      if (dots) s += (d._v1 ? "\n" : "") + fadeWrap(dots, dotsDiv(dots));
      cache[id] = s;
      return s;
    }
    function overlayHTML(id) {
      const d = defs[id] || {};
      let s = "";
      if (isNum(d.vignette) && d.vignette > 0) s += `<div style="position:absolute;inset:0;background:radial-gradient(ellipse 75% 60% at 50% 46%,rgba(0,0,0,0) 45%,rgba(0,0,0,${r2(Math.min(d.vignette, 1))}) 100%)"></div>`;
      if (isNum(d.noise) && d.noise > 0) {
        const u = env.noiseUrl ? env.noiseUrl() : "";
        if (u) s += `<div style="position:absolute;inset:0;background:url(${u});background-size:256px 256px;opacity:${r2(Math.min(d.noise * 2.2, 0.6))};mix-blend-mode:overlay"></div>`;
      }
      return s;
    }
    /* full world markup at frame n; ctx = {fUrl} when a smaller stage window leaves the frame visible behind it */
    function html(id, n, ctx) {
      const d = defs[id] || defs[dflt] || {}, t = n / 30;
      let s = staticHTML(defs[id] ? id : dflt);
      if (d.glow) {
        const G = d.glow, dr = G.drift || [0, 0, 0, 0];
        const gx = (G.x != null ? G.x : 540) + Math.sin(t * dr[2]) * dr[0], gy = (G.y != null ? G.y : 560) + Math.cos(t * dr[3]) * dr[1];
        const a = isNum(G.alpha) ? G.alpha : 0.14;
        s += `\n<div style="position:absolute;inset:0;background:radial-gradient(circle at ${r2(gx)}px ${r2(gy)}px,${rgba(G.colour || "data", a)} 0,${rgba(G.colour || "data", 0)} ${G.r || 350}px)"></div>`;
      }
      if ((d.kind === "footage" || d.footage) && ctx && ctx.fUrl) {
        const F = d.footage || {}, pad = isNum(F.pad) ? F.pad : 60, bl = isNum(F.blur) ? F.blur : 28, br = isNum(F.brightness) ? F.brightness : 0.45;
        s += `<img data-foot="1" src="${ctx.fUrl}" style="position:absolute;left:-${pad}px;top:-${pad}px;width:${W + 2 * pad}px;height:${H + 2 * pad}px;filter:${ctx.gf ? ctx.gf + " " : ""}blur(${bl}px) brightness(${br})">`; // gf: the footage grade (E-16)
      }
      return s + overlayHTML(defs[id] ? id : dflt);
    }
    function lum(hex) {
      const h = String(col(hex) || "").replace("#", "");
      if (!/^[0-9a-f]{6}$/i.test(h)) return 0;
      const c = [0, 2, 4].map(i => { const v = parseInt(h.slice(i, i + 2), 16) / 255; return v <= 0.04045 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); });
      return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2];
    }
    /* light world = dark text on it (the v1 subtitles flip on `canvas`) */
    function isLight(id) {
      const d = defs[id];
      if (!d || d.kind === "footage") return false;
      if (d.light != null) return !!d.light;
      const stops = d.top || d.bottom ? [d.top || d.bg, d.bottom || d.bg] : [d.bg || "night"];
      return stops.reduce((a, c) => a + lum(c), 0) / stops.length > 0.4;
    }
    return { ids, v3ids, defs, dflt, has: id => id in defs, html, isLight, bgCss: id => bgCss(defs[id] || {}), kind: id => (defs[id] || {}).kind || null,
      discHTML: D => discHTML(D || {}) };
  }

  /* timeline.world[] -> [{f, world, fade_f}] and the worlds to draw at frame n: [{id, op}] (bottom first) */
  function schedule(TL, fps, dflt) {
    const W0 = (TL.world && TL.world.length ? TL.world : [{ t: 0, world: dflt || "studio" }])
      .map(w => ({ f: Math.round((+w.t || 0) * fps), world: w.world, fade_f: Math.max(0, Math.round((+w.fade || 0) * fps)) }))
      .sort((a, b) => a.f - b.f);
    return W0;
  }
  function at(SCHED, n, dflt) {
    let i = -1; for (let k = 0; k < SCHED.length; k++) if (SCHED[k].f <= n) i = k;
    if (i < 0) return { id: dflt || "studio", under: null, op: 1 };
    const cur = SCHED[i], prev = SCHED[i - 1];
    if (prev && cur.fade_f > 0 && n < cur.f + cur.fade_f) { const q = (n - cur.f + 1) / (cur.fade_f + 1); return { id: cur.world, under: prev.world, op: q * q * (3 - 2 * q) }; }
    return { id: cur.world, under: null, op: 1 };
  }
  /* a 256x256 grain tile as a PNG data URL (seeded, so every render is identical); browser only */
  let NOISE = null;
  function noiseUrl() {
    if (NOISE != null) return NOISE;
    try {
      const c = document.createElement("canvas"); c.width = c.height = 256;
      const g = c.getContext("2d"), im = g.createImageData(256, 256);
      let a = 0x2545F491;
      for (let i = 0; i < im.data.length; i += 4) {
        a = (a + 0x6D2B79F5) | 0; let t = Math.imul(a ^ (a >>> 15), 1 | a); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
        const v = ((t ^ (t >>> 14)) >>> 0) / 4294967296 * 255;
        im.data[i] = im.data[i + 1] = im.data[i + 2] = v; im.data[i + 3] = 255;
      }
      g.putImageData(im, 0, 0); NOISE = c.toDataURL("image/png");
    } catch (e) { NOISE = ""; }
    return NOISE;
  }
  return { create, schedule, at, legacyDefs, noiseUrl };
});
