/* Vibe Editing OS stage layouts (E-07, structure §3.2 / F.3). Pure geometry, no DOM: loaded by player.html before
   core.js (window.VEOS_LAYOUTS) and by node in the engine tests (module.exports).

   A stage entry (timeline.stage[]) names a layout: an engine layout (`card`, `stack`, `pip`, `letterbox`, `blurfill`, or
   the v1 `full | low | panel | inset | slide-aside | bubble | hidden`) or a token layout id (`tokens.layouts["L-…"]`, whose
   `engine` says which). Params come from, in order: engine defaults < tokens.layouts[id] < entry `p` < entry inline keys.

     card      {rect:{x,y,w,h}, radius, crop: "16:9"|"4:3"|"9:16"|"1:1", border: px|{px,colour}, shadow, glow:{colour,px}, face, eye}
     stack     {seam_y, top, bottom, hairline: px|{px,colour}, fade: px|{px,colour,side}}   top/bottom = "footage" | "graphic" |
               "source:<id>" | {src, crop:{x,y,w,h}, face, eye, fit: cover|contain|blurfill}
     pip       {shape: circle|square, d, corner: tl|tr|bl|br|tc|bc|c|{cx,cy}, ring: px|{px,colour,gradient:[...]}, radius, margin}
     letterbox {band_h, cy, fill, src}                          blurfill {band_h, cy, blur_px, luma, scale, src}
     treatment dim {blur_px, luma}   (any layout: `dim: {...}` / `dim: true` on the entry, or tokens.layouts[id].treatment.dim)

   A layout resolves per frame to a geometry G: the presenter window `g` (the fields core.js already draws: x y w h r[4]
   s ax ay Fx Fy ring sh soft op off, plus ext fields), extra windows `cells` (a second source, a faux crop), a full-frame
   backdrop `bd` (letterbox fill, blurfill copy) and seam `lines` (hairline, fade). Morphs lerp two geometries (`lerp`).
   `info()` gives scenes and the caption engine the resolved rects (ctx.layout()).
*/
(function (root, factory) {
  const m = factory();
  if (typeof module === "object" && module.exports) module.exports = m; else root.VEOS_LAYOUTS = m;
})(typeof self !== "undefined" ? self : this, function () {
  "use strict";
  const W = 1080, H = 1920;
  const cl = (x, a = 0, b = 1) => (x < a ? a : x > b ? b : x);
  const lerp = (a, b, p) => a + (b - a) * p;
  const isNum = v => typeof v === "number" && isFinite(v);
  const LEGACY = ["full", "low", "panel", "inset", "slide-aside", "bubble", "hidden"];
  const NEW = ["card", "stack", "pip", "letterbox", "blurfill"];
  const ENGINES = LEGACY.concat(NEW);
  const ASPECT = { "16:9": 16 / 9, "4:3": 4 / 3, "1:1": 1, "4:5": 4 / 5, "3:4": 3 / 4, "9:16": 9 / 16 };
  const CORNER_X = { l: 64, r: 1016, c: 540 }, CORNER_Y = { t: 150, b: 1500, c: 960 };
  /* new morphs (frames at 30 fps; tokens.stage_morphs[via] and stage[].dur override) and their default eases */
  const MORPH_FRAMES = { "fade-through": 14, "shrink-to-card": 12, "grow-from-card": 12, "slide-down": 9, "slide-up": 9, "pip-shrink": 11, "pip-grow": 10, morph: 10, dim: 8 };
  const MORPH_EASE = { "shrink-to-card": "card", "grow-from-card": "card", "slide-down": "slide", "slide-up": "slide", "pip-shrink": "pip",
    "pip-grow": "card", morph: "inOut", dim: "inOut", "fade-through": "linear" };
  /* smooth-start curves for the new morphs (peak speed about 2.6x the mean, so long travels stay G3-smooth); pip settles
     with a 1% overshoot */
  function bez(x1, y1, x2, y2) {
    return x => {
      if (x <= 0) return 0; if (x >= 1) return 1; let t = x;
      for (let i = 0; i < 16; i++) {
        const u = 1 - t, f = 3 * x1 * t * u * u + 3 * x2 * t * t * u + t * t * t - x; if (Math.abs(f) < 1e-7) break;
        const d = 3 * x1 * u * u + 6 * (x2 - x1) * t * u + 3 * (1 - x2) * t * t; if (Math.abs(d) < 1e-7) break; t = cl(t - f / d);
      }
      const u = 1 - t; return 3 * y1 * t * u * u + 3 * y2 * t * t * u + t * t * t;
    };
  }
  const CURVES = { card: bez(0.45, 0, 0.25, 1), slide: bez(0.35, 0, 0.2, 1), pip: bez(0.45, 0, 0.3, 1.12) };
  const VIAS_NEW = Object.keys(MORPH_FRAMES);
  const TARGET_VIA = { card: "shrink-to-card", stack: "slide-down", pip: "pip-shrink", letterbox: "morph", blurfill: "morph" };
  const META_KEYS = ["t", "layout", "via", "dur", "ease", "p", "offset", "id", "overshoot"];
  const TOK_META = ["engine", "presenter", "graphic", "caption", "treatment", "share", "safe", "name", "notes"];

  const DEFAULTS = {
    card: { rect: null, radius: 36, crop: "4:3", border: 0, shadow: 0.38, glow: null, face: null, eye: 0.42, src: "footage" },
    stack: { seam_y: 960, top: "graphic", bottom: "footage", hairline: 0, fade: 0 },
    pip: { shape: "circle", d: 380, corner: "br", ring: 8, radius: 40, margin: 0, face: 0.62, eye: 0.5, shadow: 0.4, src: "footage" },
    letterbox: { band_h: 608, cy: 960, fill: "#000000", face: 0.42, eye: 0.45, src: "footage" },
    blurfill: { band_h: 608, cy: 960, blur_px: 40, luma: -0.55, scale: 1.15, face: 0.42, eye: 0.45, src: "footage" },
  };
  const DIM_DEFAULT = { blur_px: 14, luma: -0.45 };

  /* ------------------------------------------------------------------ resolve: stage entry -> spec */
  function clone(o) { return o == null ? o : JSON.parse(JSON.stringify(o)); }
  function engineOf(name, T) {
    const L = (T && T.layouts) || {};
    if (L[name] && L[name].engine) return String(L[name].engine);
    if (ENGINES.includes(name)) return name;
    return null;
  }
  /* token layout -> params (tokens.schema §3.9: `presenter` holds the presenter rect and its look) */
  function fromTok(tok, engine) {
    const p = {};
    for (const k of Object.keys(tok || {})) if (!TOK_META.includes(k)) p[k] = clone(tok[k]);
    const pr = tok && tok.presenter;
    if (pr && typeof pr === "object") {
      const rect = ["x", "y", "w", "h"].some(k => pr[k] != null) ? { x: pr.x, y: pr.y, w: pr.w, h: pr.h } : null;
      for (const k of Object.keys(pr)) if (!["x", "y", "w", "h", "fade_to"].includes(k)) p[k] = clone(pr[k]);
      if (engine === "card" && rect) p.rect = rect;
      if (engine === "pip" && rect && pr.d == null) { p.d = Math.min(rect.w || 0, rect.h || 0) || undefined; if (rect.x != null) p.corner = { cx: rect.x + (rect.w || 0) / 2, cy: rect.y + (rect.h || 0) / 2 }; }
      if ((engine === "letterbox" || engine === "blurfill") && rect) { if (rect.h != null) p.band_h = rect.h; if (rect.y != null) p.cy = rect.y + (rect.h || 0) / 2; }
      if (engine === "stack" && rect && p.seam_y == null && rect.y != null) {
        const atTop = (rect.y || 0) <= 1;
        p.seam_y = atTop ? rect.y + rect.h : rect.y;
        if (p.top == null && p.bottom == null) { p.top = atTop ? "footage" : "graphic"; p.bottom = atTop ? "graphic" : "footage"; }
        if (pr.fade_to) p.fade = { px: 180, colour: pr.fade_to, side: atTop ? "bottom" : "top" };
      }
    }
    const dim = tok && tok.treatment && tok.treatment.dim;
    if (dim) p.dim = clone(dim);
    if (tok && tok.treatment === null) delete p.dim;
    return p;
  }
  function normCell(v, key) {
    if (v == null || v === false) return { key, src: "graphic" };
    if (typeof v === "string") return { key, src: v };
    const o = Object.assign({}, v); o.key = key; o.src = o.src || "footage"; return o;
  }
  function normLine(v, colour, px) {
    if (!v) return null;
    if (v === true) return { px, colour };
    if (isNum(v)) return { px: v, colour };
    const o = { px: isNum(v.px) ? v.px : px, colour: v.colour || v.color || colour, side: v.side || "both" };
    if (v.mode === "blend" || v.blend === true) o.mode = "blend"; // seam blend: the footage melts into the panel (no colour band)
    return o;
  }
  /* head breakout (card / pip): the cut-out may rise above the window's top edge by up to px (true = 160) */
  function normBreakout(v) { if (!v) return 0; if (v === true) return 160; if (isNum(v)) return Math.max(0, v); return isNum(v.px) ? Math.max(0, v.px) : 160; }
  function normDim(v) {
    if (!v) return null;
    if (v === true) return Object.assign({}, DIM_DEFAULT);
    return { blur_px: isNum(v.blur_px) ? v.blur_px : DIM_DEFAULT.blur_px, luma: isNum(v.luma) ? v.luma : DIM_DEFAULT.luma };
  }
  /* returns {id, engine, p, caption, graphic, safe} or throws Error with a plain-English message */
  function resolve(entry, T) {
    const id = String(entry.layout || "full");
    const tok = ((T && T.layouts) || {})[id] || null;
    const engine = engineOf(id, T);
    if (!engine) {
      const known = Object.keys((T && T.layouts) || {});
      throw new Error(`stage layout '${id}' is neither an engine layout (${ENGINES.join(", ")}) nor a tokens.layouts id${known.length ? ` (${known.join(", ")})` : ""}`);
    }
    if (!ENGINES.includes(engine)) throw new Error(`tokens.layouts.${id}.engine '${engine}' is not an engine layout (${ENGINES.join(", ")})`);
    const inline = {}; for (const k of Object.keys(entry)) if (!META_KEYS.includes(k)) inline[k] = entry[k];
    const p = Object.assign({}, clone(DEFAULTS[engine] || {}), tok ? fromTok(tok, engine) : {}, fromTok(entry.p || {}, engine), fromTok(inline, engine));
    p.dim = normDim(p.dim);
    if (engine === "card") {
      const asp = ASPECT[p.crop] || (isNum(p.crop) ? p.crop : ASPECT["4:3"]);
      const r = Object.assign({}, p.rect || {});
      if (!isNum(r.w) && !isNum(r.h)) r.w = 936;
      if (!isNum(r.w)) r.w = r.h * asp;
      if (!isNum(r.h)) r.h = r.w / asp;
      if (!isNum(r.x)) r.x = (W - r.w) / 2;
      if (!isNum(r.y)) r.y = (H - r.h) / 2;
      p.rect = r; p.aspect = asp;
      p.border = normLine(p.border, "paper", 4);
      if (p.face == null) p.face = Math.abs(r.w / r.h - W / H) < 0.02 ? 0 : 0.3;
      p.breakout = normBreakout(p.breakout);
    } else if (engine === "stack") {
      p.top = normCell(p.top, "top"); p.bottom = normCell(p.bottom, "bottom");
      p.hairline = normLine(p.hairline, "paper", 6);
      p.fade = normLine(p.fade, "#000000", 180);
      p.seam_y = cl(isNum(p.seam_y) ? p.seam_y : 960, 120, H - 120);
    } else if (engine === "pip") {
      const ring = p.ring;
      p.ring = ring === false || ring === 0 ? { px: 0, colour: "paper" } : isNum(ring) ? { px: ring, colour: "paper" }
        : Object.assign({ px: 8, colour: "paper" }, ring || {});
      p.d = isNum(p.d) ? p.d : 380;
      p.breakout = normBreakout(p.breakout);
    }
    const cap = tok && tok.caption ? clone(tok.caption) : null;
    const gr = tok && tok.graphic ? clone(tok.graphic) : null;
    return { id, engine, legacy: LEGACY.includes(engine), p, caption: cap, graphic: gr, safe: tok ? tok.safe || null : null };
  }
  function defaultVia(prevSpec, spec) {
    if (!spec) return null;
    if (prevSpec && prevSpec.engine === spec.engine && JSON.stringify(prevSpec.p.dim) !== JSON.stringify(spec.p.dim) &&
        (prevSpec.id === spec.id || spec.legacy)) return "dim";
    if (spec.legacy && (!prevSpec || prevSpec.legacy)) return null; // v1 -> v1: core's own table
    if (prevSpec && prevSpec.id === spec.id) return "morph";
    if (!spec.legacy) {
      if (spec.engine === "card" && prevSpec && prevSpec.engine === "card") return "morph";
      if (spec.engine === "stack" && prevSpec && prevSpec.engine === "stack") return "morph";
      return TARGET_VIA[spec.engine] || "morph";
    }
    if (prevSpec && !prevSpec.legacy) { // back to a v1 layout from a new one
      if (prevSpec.engine === "pip") return "pip-grow";
      if (prevSpec.engine === "card") return "grow-from-card";
      if (prevSpec.engine === "stack" && spec.engine === "full") return "slide-up";
      return "morph";
    }
    return null;
  }

  /* ------------------------------------------------------------------ geometry */
  const cov = (a, lo, hi) => (lo <= hi ? cl(a, lo, hi) : (lo + hi) / 2);
  /* frame a source (size sw x sh, face F {cx,cy,w,h} in source px) into rect R: scale s maps source px to screen px around F */
  function frameRect(R, F, o) {
    const sw = o.sw || W, sh = o.sh || H, fs = Math.max(1, ((F.w || 300) + (F.h || 300)) / 2);
    if (o.crop) { // explicit crop window in source px (multispeaker reframe): its centre lands on the rect centre
      const c = o.crop, s = Math.max(R.w / c.w, R.h / c.h);
      const cx = c.x + c.w / 2, cy = c.y + c.h / 2;
      return { s, ax: R.x + R.w / 2, ay: R.y + R.h / 2, Fx: cx, Fy: cy };
    }
    if (o.fit === "contain") {
      const s = Math.min(R.w / sw, R.h / sh);
      return { s, ax: R.x + R.w / 2, ay: R.y + R.h / 2, Fx: sw / 2, Fy: sh / 2 };
    }
    const coverS = Math.max(R.w / sw, R.h / sh);
    if (o.framing) { // window framing ranges (screen px, winFraming): size from face height / head-to-chin, place by the ranges
      const fr = o.framing, h = Math.max(1, F.h || 300), mid = r => (r[0] + r[1]) / 2;
      let s = null;
      if (fr.face_h) s = mid(fr.face_h) / h;
      else if (fr.head_top_y && fr.chin_y) s = (mid(fr.chin_y) - mid(fr.head_top_y)) / (1.35 * h);
      else if (fr.eye_y && fr.chin_y) s = (mid(fr.chin_y) - mid(fr.eye_y)) / (0.62 * h);
      else if (fr.head_top_y && fr.eye_y) s = (mid(fr.eye_y) - mid(fr.head_top_y)) / (0.73 * h);
      if (s == null) s = o.face ? o.face * R.h / fs : coverS;
      s = Math.min(Math.max(coverS, s), Math.max(coverS, 3));
      const ys = [];
      if (fr.head_top_y) ys.push(mid(fr.head_top_y) + 0.85 * s * h);
      if (fr.eye_y) ys.push(mid(fr.eye_y) + 0.12 * s * h);
      if (fr.chin_y) ys.push(mid(fr.chin_y) - 0.5 * s * h);
      let ay = ys.length ? ys.reduce((a, b) => a + b, 0) / ys.length : R.y + (o.eye == null ? 0.42 : o.eye) * R.h;
      let ax = fr.face_cx ? mid(fr.face_cx) : R.x + R.w / 2;
      ax = cov(ax, R.x + R.w - s * (sw - F.cx), R.x + s * F.cx);
      ay = cov(ay, R.y + R.h - s * (sh - F.cy), R.y + s * F.cy);
      return { s, ax, ay, Fx: F.cx, Fy: F.cy };
    }
    const s = Math.min(Math.max(coverS, o.face ? o.face * R.h / fs : 0), Math.max(coverS, 3));
    let ax = R.x + R.w / 2, ay = R.y + (o.eye == null ? 0.42 : o.eye) * R.h;
    ax = cov(ax, R.x + R.w - s * (sw - F.cx), R.x + s * F.cx);
    ay = cov(ay, R.y + R.h - s * (sh - F.cy), R.y + s * F.cy);
    return { s, ax, ay, Fx: F.cx, Fy: F.cy };
  }
  /* window framing (A22 inside windows): the presenter's own `framing` (fractions of the window: head_top_frac, eye_frac,
     chin_frac, face_h_frac, face_cx_frac; or screen px head_top_y / eye_y / chin_y / face_cx / face_h) or, without one,
     the reel's base framing ranges (screen px, bundle.framing.ranges) when every vertical range lies inside the window
     (a template whose setup framing describes its face card, e.g. lesson-frame's 4:3 card). -> screen-px ranges or null */
  const FR_FRAC = { head_top_frac: "head_top_y", eye_frac: "eye_y", eyes_frac: "eye_y", chin_frac: "chin_y", face_h_frac: "face_h", face_cx_frac: "face_cx" };
  const FR_PX = ["head_top_y", "eye_y", "chin_y", "face_cx", "face_h"];
  const rng2 = v => (Array.isArray(v) && v.length === 2 && isNum(v[0]) && isNum(v[1]) ? [Math.min(v[0], v[1]), Math.max(v[0], v[1])] : null);
  function winFraming(R, own, base) {
    if (own && typeof own === "object") {
      const o = {};
      for (const k of Object.keys(FR_FRAC)) {
        const r = rng2(own[k]), key = FR_FRAC[k]; if (!r || o[key]) continue;
        o[key] = key === "face_cx" ? [R.x + r[0] * R.w, R.x + r[1] * R.w] : key === "face_h" ? [r[0] * R.h, r[1] * R.h] : [R.y + r[0] * R.h, R.y + r[1] * R.h];
      }
      for (const k of FR_PX) { const r = rng2(own[k]); if (r && !o[k]) o[k] = r; }
      return Object.keys(o).length ? o : null;
    }
    if (!base || typeof base !== "object") return null;
    const vk = ["head_top_y", "eye_y", "chin_y"].filter(k => rng2(base[k]));
    if (!vk.length || !vk.every(k => { const r = rng2(base[k]); return r[0] >= R.y - 1 && r[1] <= R.y + R.h + 1; })) return null;
    const o = {}; for (const k of vk) o[k] = rng2(base[k]);
    const fx = rng2(base.face_cx); if (fx && fx[0] >= R.x - 1 && fx[1] <= R.x + R.w + 1) o.face_cx = fx;
    const fh = rng2(base.face_h); if (fh && fh[1] <= R.h) o.face_h = fh;
    return o;
  }
  const BASE = () => ({ x: 0, y: 0, w: W, h: H, r: [0, 0, 0, 0], s: 1, ax: 0, ay: 0, ring: 0, sh: 0, soft: 0, op: 1, Fx: 0, Fy: 0, off: 0 });
  const EXT = { bw: 0, shA: 0, glow: 0, blur: 0, luma: 0 };
  function ext(g) { g.ext = true; for (const k in EXT) if (g[k] == null) g[k] = EXT[k]; if (!g.cells) g.cells = []; if (!g.lines) g.lines = []; if (!g.bd) g.bd = null; return g; }
  function corner(p) {
    const d = p.d, m = p.margin || 0, c = p.corner;
    if (c && typeof c === "object") return { cx: +c.cx, cy: +c.cy };
    const s = String(c || "br");
    const v = s.length === 2 ? s[0] : (s === "c" ? "c" : s[0]), hz = s.length === 2 ? s[1] : "c";
    const X = hz === "l" ? CORNER_X.l + m + d / 2 : hz === "r" ? CORNER_X.r - m - d / 2 : CORNER_X.c;
    const Y = v === "t" ? CORNER_Y.t + m + d / 2 : v === "b" ? CORNER_Y.b - m - d / 2 : CORNER_Y.c;
    return { cx: X, cy: Y };
  }
  /* env: {face(src, n) -> {cx,cy,w,h}, size(src) -> [w,h], col(role)} ; returns geometry g (with ext fields) */
  function geom(spec, n, env) {
    const p = spec.p, F0 = env.face("footage", n), baseFr = env.framing ? env.framing() : null;
    const wf = (R, own) => winFraming(R, own, baseFr);
    const g = ext(Object.assign(BASE(), { ax: F0.cx, ay: F0.cy, Fx: F0.cx, Fy: F0.cy }));
    g.engine = spec.engine; g.id = spec.id; g.src = "footage";
    const put = (R, src, o) => {
      const F = env.face(src, n), sz = env.size(src);
      return Object.assign({ x: R.x, y: R.y, w: R.w, h: R.h }, frameRect(R, F, Object.assign({ sw: sz[0], sh: sz[1] }, o)));
    };
    const hideAt = R => { Object.assign(g, { x: R.x + R.w / 2, y: R.y + R.h / 2, w: 0, h: 0, op: 0, s: 0.3, ax: R.x + R.w / 2, ay: R.y + R.h / 2 }); };
    const cell = (key, R, c) => {
      const src = c.src || "footage", sz = env.size(src);
      const fit0 = c.fit === "letterbox" ? "contain" : c.fit; // multispeaker reframe.py spells contain "letterbox"
      const fit = fit0 || (src !== "footage" && sz[0] / sz[1] > R.w / R.h * 1.25 ? "blurfill" : "cover");
      const f = put(R, src, { face: c.face != null ? c.face : 0.3, eye: c.eye != null ? c.eye : 0.4, crop: c.crop, fit: fit === "blurfill" ? "contain" : fit });
      return Object.assign(f, { key, src, r: [0, 0, 0, 0], op: 1, fit, blur: 0, luma: 0, sw: sz[0], sh: sz[1] });
    };
    switch (spec.engine) {
      case "card": {
        const R = p.rect, rad = isNum(p.radius) ? p.radius : 36;
        Object.assign(g, put(R, "footage", { face: p.face, eye: p.eye, framing: wf(R, p.framing) }), { r: [rad, rad, rad, rad] });
        g.bw = p.border ? p.border.px : 0; g.bc = p.border ? p.border.colour : null;
        g.shA = isNum(p.shadow) ? p.shadow : 0; if (p.glow) { g.glow = p.glow.px || 40; g.glowC = p.glow.colour || "paper"; }
        if (p.breakout > 0) g.bo = p.breakout;
        break;
      }
      case "pip": {
        const c = corner(p), d = p.d, R = { x: c.cx - d / 2, y: c.cy - d / 2, w: d, h: d };
        const rad = p.shape === "square" ? Math.min(isNum(p.radius) ? p.radius : 40, d / 2) : d / 2;
        Object.assign(g, put(R, "footage", { face: p.face, eye: p.eye, framing: wf(R, p.framing) }), { r: [rad, rad, rad, rad] });
        g.ring = p.ring.px; g.ringC = p.ring.colour || "paper"; g.ringG = p.ring.gradient || null;
        g.shA = isNum(p.shadow) ? p.shadow : 0.4; g.shape = p.shape;
        if (p.breakout > 0) g.bo = p.breakout;
        break;
      }
      case "letterbox": case "blurfill": {
        const bh = p.band_h, R = { x: 0, y: p.cy - bh / 2, w: W, h: bh };
        if (p.src && p.src !== "footage") { hideAt(R); g.cells.push(cell("band", R, { src: p.src, fit: "contain" })); }
        else Object.assign(g, put(R, "footage", { face: p.face, eye: p.eye }));
        g.bd = spec.engine === "letterbox" ? { kind: "fill", colour: p.fill || "#000000", op: 1, src: p.src || "footage" }
          : { kind: "blur", px: p.blur_px, luma: p.luma, scale: p.scale, op: 1, src: p.src || "footage" };
        g.band = R;
        break;
      }
      case "stack": {
        const sy = p.seam_y, blend = p.fade && p.fade.px > 0 && p.fade.mode === "blend", bh = blend ? p.fade.px / 2 : 0;
        // seam blend: each footage band reaches px/2 past the seam and fades in over px (a mask, not a colour band)
        const RT = { x: 0, y: 0, w: W, h: sy + (blend && p.top.src !== "graphic" ? bh : 0) };
        const RB = { x: 0, y: sy - (blend && p.bottom.src !== "graphic" ? bh : 0), w: W, h: H - sy + (blend && p.bottom.src !== "graphic" ? bh : 0) };
        const cells = [[p.top, RT], [p.bottom, RB]];
        const maskOf = c => (blend && c.src !== "graphic" ? { side: c === p.top ? "bottom" : "top", px: p.fade.px } : null);
        const prim = cells.find(([c]) => c.src === "footage");
        if (prim) { Object.assign(g, put(prim[1], "footage", { face: prim[0].face != null ? prim[0].face : 0.3, eye: prim[0].eye != null ? prim[0].eye : 0.4, crop: prim[0].crop, framing: prim[0].crop ? null : wf(prim[1], prim[0].framing != null ? prim[0].framing : p.framing) }), { key: prim[0].key }); if (maskOf(prim[0])) g.mask = maskOf(prim[0]); }
        else hideAt(RB);
        for (const [c, R] of cells) if (c.src !== "graphic" && (!prim || c !== prim[0])) { const k = cell(c.key, R, c); if (maskOf(c)) k.mask = maskOf(c); if (c.grade != null) k.grade = c.grade; g.cells.push(k); }
        if (p.hairline && p.hairline.px > 0) g.lines.push({ key: "hair", kind: "line", x: 0, y: sy - p.hairline.px / 2, w: W, h: p.hairline.px, colour: p.hairline.colour, op: 1 });
        if (p.fade && p.fade.px > 0 && !blend) {
          const side = p.fade.side || "both", px = p.fade.px;
          if (side !== "bottom") g.lines.push({ key: "fadeT", kind: "fade", dir: "down", x: 0, y: sy - px, w: W, h: px, colour: p.fade.colour, op: 1 });
          if (side !== "top") g.lines.push({ key: "fadeB", kind: "fade", dir: "up", x: 0, y: sy, w: W, h: Math.min(px * 0.5, 120), colour: p.fade.colour, op: 1 });
        }
        g.seam = sy; g.topR = RT; g.botR = RB;
        const gk = [p.top, p.bottom].find(c => c.src === "graphic"); g.graphicKey = gk ? gk.key : null;
        break;
      }
      default: break;
    }
    if (p.dim) { g.blur = p.dim.blur_px; g.luma = p.dim.luma; }
    return g;
  }

  /* the dim treatment on a v1 layout (e.g. `full` under a card): its geometry becomes an ext geometry */
  function applyDim(g, spec) {
    if (!spec || !spec.p || !spec.p.dim) return g;
    ext(g); g.engine = spec.engine; g.id = spec.id; g.blur = spec.p.dim.blur_px; g.luma = spec.p.dim.luma;
    return g;
  }

  /* ------------------------------------------------------------------ morphs */
  const NUM = ["x", "y", "w", "h", "s", "ax", "ay", "Fx", "Fy", "op", "blur", "luma"];
  function lerpCell(a, b, p) {
    const o = Object.assign({}, p < 0.5 ? a : b);
    for (const k of NUM) o[k] = lerp(a[k] != null ? a[k] : b[k], b[k] != null ? b[k] : a[k], p);
    o.r = (a.r || [0, 0, 0, 0]).map((v, i) => Math.max(0, lerp(v, (b.r || [0, 0, 0, 0])[i], p)));
    o.w = Math.max(0, o.w); o.h = Math.max(0, o.h); o.op = cl(o.op);
    if (o.src !== b.src) o.src = p < 0.5 ? a.src : b.src;
    return o;
  }
  /* the stand-in for a cell / line that exists on one side only: off the top for slide morphs, else faded + shrunk */
  function ghost(c, via) {
    const o = Object.assign({}, c);
    if (via === "slide-down" || via === "slide-up") { const dy = -(c.y + c.h); o.y += dy; if (o.ay != null) o.ay += dy; }
    else { o.op = 0; if (o.kind == null && o.s != null) { const k = 0.94; o.ax = c.x + c.w / 2 + (c.ax - c.x - c.w / 2) * k; o.ay = c.y + c.h / 2 + (c.ay - c.y - c.h / 2) * k; o.x += c.w * 0.03; o.y += c.h * 0.03; o.w *= k; o.h *= k; o.s *= k; } }
    return o;
  }
  function lerpList(A, B, p, via, fn) {
    const out = [], keys = [];
    for (const c of A.concat(B)) if (!keys.includes(c.key)) keys.push(c.key);
    for (const k of keys) {
      const a = A.find(c => c.key === k), b = B.find(c => c.key === k);
      out.push(fn(a || ghost(b, via), b || ghost(a, via), p));
    }
    return out.filter(c => c.op > 0.003);
  }
  function lerpLine(a, b, p) {
    const o = Object.assign({}, p < 0.5 ? a : b);
    for (const k of ["x", "y", "w", "h", "op"]) o[k] = lerp(a[k], b[k], p);
    o.colour = b.op > 0 ? b.colour : a.colour; o.op = cl(o.op);
    return o;
  }
  /* o = core's lerped base geometry (x..off, r); adds the ext fields. a or b may be a v1 geometry (no ext). */
  function lerpExt(a, b, o, p, via) {
    const A = a.ext ? a : ext(Object.assign({}, a)), Bx = b.ext ? b : ext(Object.assign({}, b));
    ext(o);
    for (const k of ["bw", "shA", "glow", "blur", "luma"]) o[k] = Math.max(k === "luma" ? -1 : 0, lerp(A[k], Bx[k], p));
    o.bc = Bx.bw > 0 ? Bx.bc : A.bc; o.ringC = Bx.ring > 0 ? (Bx.ringC || "paper") : (A.ringC || null);
    o.ringG = Bx.ring > 0 ? Bx.ringG || null : A.ringG || null; o.glowC = Bx.glow > 0 ? Bx.glowC : A.glowC;
    o.engine = p < 0.5 ? A.engine : Bx.engine; o.id = p < 0.5 ? A.id : Bx.id; o.src = "footage";
    o.cells = lerpList(A.cells, Bx.cells, p, via, lerpCell);
    o.lines = lerpList(A.lines, Bx.lines, p, via, lerpLine);
    if (A.bd || Bx.bd) {
      const ba = A.bd || Object.assign({}, Bx.bd, { op: 0 }), bb = Bx.bd || Object.assign({}, A.bd, { op: 0 });
      o.bd = Object.assign({}, bb.op > 0 ? bb : ba, { op: cl(lerp(ba.op, bb.op, p)) });
      if (ba.kind === "blur" && bb.kind === "blur") { o.bd.px = lerp(ba.px, bb.px, p); o.bd.luma = lerp(ba.luma, bb.luma, p); }
      if (o.bd.op < 0.003) o.bd = null;
    }
    /* the seam enters / leaves from the frame edge on slide morphs (graphic band grows with it), else it appears at its place */
    const slide = via === "slide-down" || via === "slide-up";
    const sa = A.seam != null ? A.seam : (Bx.seam != null && slide ? Bx.seam * 0.5 : null), sb = Bx.seam != null ? Bx.seam : (A.seam != null && slide ? A.seam * 0.5 : null);
    o.seam = sa != null && sb != null ? lerp(sa, sb, p) : (p < 0.5 ? sa : sb);
    o.graphicKey = Bx.graphicKey || A.graphicKey || null;
    o.mask = (p < 0.5 ? A.mask : Bx.mask) || null; // seam blend mask (stack fade mode "blend")
    /* a band that exists on one side only is not reported mid-morph (anchors then follow the lerped presenter rect) */
    if (A.band && Bx.band) o.band = { x: 0, y: lerp(A.band.y, Bx.band.y, p), w: W, h: lerp(A.band.h, Bx.band.h, p) };
    else if (p >= 0.999 && Bx.band) o.band = Bx.band; else if (p <= 0.001 && A.band) o.band = A.band; else o.band = null;
    return o;
  }
  /* eased progress for a morph. legacy vias keep core's rule (elastic for bubble/pop-back, else in-out) */
  function easeOf(via, q, E, override) {
    const name = override || MORPH_EASE[via];
    if (!name) return via === "bubble-shrink" || via === "bubble-grow" || via === "pop-back" ? E.EL(q) : E.EIO(q);
    switch (name) {
      case "out": return E.EO(q);
      case "in": return E.EI(q);
      case "back": return E.BO(q, 1.25);
      case "elastic": return E.EL(q);
      case "linear": return cl(q);
      case "card": case "slide": case "pip": return CURVES[name](q);
      default: return E.EIO(q);
    }
  }
  /* vertical motion blur (px) a morph adds to moving footage: from the speed of the window's vertical travel */
  function morphBlur(via, a, b, q) {
    if (!(via === "slide-down" || via === "slide-up")) return 0; // card / pip morphs scale cleanly (as in the evidence): no smear
    const dy = Math.abs((b.y + b.h / 2) - (a.y + a.h / 2));
    return cl(dy / 300, 0, 1) * 10 * Math.sin(Math.PI * cl(q));
  }

  /* frames a morph needs so that every window stays within the G3 limits per frame (centre <= maxJump px, size <= maxRel),
     sampled on the eased curve; core uses max(this, MORPH_FRAMES[via]) when neither stage[].dur nor stage_morphs set it */
  const BASE_KEYS = ["x", "y", "w", "h", "s", "ax", "ay", "ring", "sh", "soft", "op", "Fx", "Fy", "off"];
  /* fade-through: A settles out (fades, eases 4% smaller), B settles in; the rect swap happens while nothing is visible */
  function shrinkAbout(g, k, op) {
    const o = Object.assign({}, g), cx = g.x + g.w / 2, cy = g.y + g.h / 2;
    o.x = cx - g.w * k / 2; o.y = cy - g.h * k / 2; o.w = g.w * k; o.h = g.h * k; o.s = g.s * k;
    o.ax = cx + (g.ax - cx) * k; o.ay = cy + (g.ay - cy) * k; o.r = (g.r || [0, 0, 0, 0]).map(v => v * k); o.op = (g.op == null ? 1 : g.op) * op;
    if (g.cells) o.cells = g.cells.map(c => shrinkAbout(c, k, op));
    if (g.lines) o.lines = g.lines.map(l => Object.assign({}, l, { op: l.op * op }));
    if (g.bd) o.bd = Object.assign({}, g.bd, { op: g.bd.op * op });
    if (g.ring) o.ring = g.ring * op;
    return o;
  }
  function fadeThrough(a, b, p) {
    const sm = x => x * x * (3 - 2 * x);
    const g = p < 0.5 ? shrinkAbout(a, 1 - 0.04 * sm(p * 2), 1 - sm(p * 2)) : shrinkAbout(b, 0.96 + 0.04 * sm(p * 2 - 1), sm(p * 2 - 1));
    if (a.ext || b.ext) { ext(g); if (!g.cells) g.cells = []; }
    g.mvb = 0; g.ft = { a, b, p }; // info() glides the caption anchors between the two layouts
    return g;
  }
  function lerpBase(a, b, p) {
    if (arguments[3] === "fade-through") return fadeThrough(a, b, p);
    const o = {}; for (const k of BASE_KEYS) o[k] = lerp(a[k] || 0, b[k] || 0, p);
    o.r = (a.r || [0, 0, 0, 0]).map((v, i) => Math.max(0, lerp(v, (b.r || [0, 0, 0, 0])[i], p)));
    o.w = Math.max(0, o.w); o.h = Math.max(0, o.h); o.op = cl(o.op);
    return (a.ext || b.ext) ? lerpExt(a, b, o, p, arguments[3]) : o;
  }
  function boxesOf(g) {
    const out = []; if (g.op > 0.05 && g.w > 2) out.push(["p", g.x, g.y, g.w, g.h]);
    if (g.seam != null) out.push(["seam", 0, g.seam - 1, W, 2]); // scenes ride the seam / graphic band
    for (const c of g.cells || []) if (c.op > 0.05 && c.w > 2) out.push([c.key, c.x, c.y, c.w, c.h]);
    return out;
  }
  function worstStep(ga, gb, via, d, E, override) {
    let prev = null, wj = 0, ws = 0;
    for (let k = 0; k <= d + 1; k++) {
      const q = k === 0 ? 0 : k > d ? 1 : (k + 1) / (d + 1), e = easeOf(via, q, E, override);
      const bx = boxesOf(lerpBase(ga, gb, e, via));
      if (prev) for (const b of bx) {
        const a = prev.find(x => x[0] === b[0]); if (!a) continue;
        wj = Math.max(wj, Math.hypot(b[1] + b[3] / 2 - a[1] - a[3] / 2, b[2] + b[4] / 2 - a[2] - a[4] / 2));
        ws = Math.max(ws, Math.abs(b[3] / a[3] - 1), Math.abs(b[4] / a[4] - 1));
      }
      prev = bx;
    }
    return [wj, ws];
  }
  /* -> [via, frames]: the frames a default morph needs, or fade-through when it cannot stay smooth within `cap` frames */
  function autoFrames(ga, gb, via, E, override, o) {
    o = o || {}; const lim = o.maxJump || 84, rel = o.maxRel || 0.22, cap = o.cap || 30;
    let d = Math.max(1, MORPH_FRAMES[via] || 7);
    for (; d <= cap; d++) { const [j, s] = worstStep(ga, gb, via, d, E, override); if (j <= lim && s <= rel) return [via, d]; }
    if (o.keepVia) return [via, cap];
    /* fade-through: the anchors glide on a smoothstep (peak speed 1.5x) from A's to B's: long enough to keep that G3-smooth */
    const ys = g => [g.seam, g.op > 0.05 && g.w > 2 ? g.y + g.h : null, g.band ? g.band.y + g.band.h : null].filter(v => v != null);
    const ya = ys(ga), yb = ys(gb), dist = ya.length && yb.length ? Math.max(Math.abs(ya[0] - yb[0]), Math.abs(ya[ya.length - 1] - yb[yb.length - 1])) : 0;
    return ["fade-through", Math.min(cap, Math.max(MORPH_FRAMES["fade-through"], Math.ceil(dist * 1.5 / lim) + 1))];
  }

  /* ------------------------------------------------------------------ info for scenes and captions (ctx.layout()) */
  const rr = v => Math.round(v * 10) / 10;
  const R4 = c => (c && c.w > 0.5 && c.h > 0.5 ? { x: rr(c.x), y: rr(c.y), w: rr(c.w), h: rr(c.h), r: rr((c.r && c.r[0]) || 0) } : null);
  function info(st, g, spec) {
    if (g && g.ft) { // fade-through: rects of the visible side, anchors glide from A's to B's
      const A = info(st, Object.assign({}, g.ft.a, { ft: null }), null), Bi = info(st, Object.assign({}, g.ft.b, { ft: null }), spec);
      const vis = g.ft.p < 0.5 ? A : Bi, q = g.ft.p * g.ft.p * (3 - 2 * g.ft.p), L = (u, v) => (u == null ? v : v == null ? u : rr(lerp(u, v, q)));
      const an = {};
      for (const k of ["seam", "below_card", "above_card"]) { const u = A.anchors[k], v = Bi.anchors[k]; an[k] = u || v ? { y: L(u && u.y, v && v.y) } : null; }
      const fa = A.anchors.inside_footage, fb = Bi.anchors.inside_footage;
      an.inside_footage = fa && fb ? { x: L(fa.x, fb.x), y: L(fa.y, fb.y), w: L(fa.w, fb.w), h: L(fa.h, fb.h), r: L(fa.r, fb.r) } : fa || fb;
      return Object.assign({}, vis, { morph: st.morph || null, p: st.morph ? rr(st.q) : 1, from: st.from || null, anchors: an,
        seam_y: an.seam ? an.seam.y : null, id: Bi.id, engine: vis.engine });
    }
    const engine = (g && g.engine) || (spec && spec.engine) || st.name;
    const pres = g && g.op > 0.01 && g.w > 1 && g.h > 1 ? R4(g) : null;
    const cells = {};
    for (const c of (g && g.cells) || []) cells[c.key] = R4(c);
    const seam = g && g.seam != null ? rr(g.seam) : null;
    if (spec && spec.engine !== engine) spec = null; // mid-morph, first half: the geometry still belongs to the previous layout
    let graphic = spec && spec.graphic ? Object.assign({}, spec.graphic) : null;
    if (!graphic && g && g.graphicKey && seam != null) // a stack's graphic band follows the (possibly morphing) seam
      graphic = g.graphicKey === "top" ? { x: 0, y: 0, w: W, h: seam } : { x: 0, y: seam, w: W, h: H - seam };
    const band = g && g.band ? R4(g.band) : null;
    const card = engine === "card" ? pres : null, pip = engine === "pip" ? pres : null;
    const footRect = pres || cells.band || cells.top || cells.bottom || null;
    const bottomOf = r => (r ? rr(r.y + r.h) : null);
    return {
      id: (g && g.id) || (spec && spec.id) || st.name, engine, morph: st.morph || null, p: st.morph ? rr(st.q) : 1, from: st.from || null,
      dim: g && (g.blur > 0.05 || g.luma < -0.01) ? { blur_px: rr(g.blur), luma: Math.round(g.luma * 100) / 100 } : null,
      rects: { presenter: pres, card, pip, band: band || cells.band || null, top: engine === "stack" ? (cells.top || (g.topR ? R4(g.topR) : null)) : null,
        bottom: engine === "stack" ? (cells.bottom || (g.botR ? R4(g.botR) : null)) : null, cells, graphic },
      seam_y: seam,
      anchors: { seam: seam != null ? { y: seam } : null, below_card: footRect ? { y: bottomOf(card || band || footRect) } : null,
        inside_footage: footRect, above_card: footRect ? { y: rr(footRect.y) } : null },
      caption: (spec && spec.caption) || null,
    };
  }
  /* centre y for the core's v1 auto-subtitles on a new layout (the caption engine, E-05, supersedes this) */
  function captionY(li, fallback) {
    const c = li.caption;
    if (c && isNum(c.cy) && c.anchor !== "seam") return c.cy;
    const a = li.anchors;
    if (c && c.anchor === "seam" && a.seam) return a.seam.y;
    if (c && c.anchor === "seam_above" && a.seam) return a.seam.y - (isNum(c.offset) ? c.offset : 24) - 40;
    if (c && c.anchor === "below_card" && a.below_card) return Math.min(a.below_card.y + 70, 1480);
    if (li.engine === "stack" && a.seam) return a.seam.y;
    if ((li.engine === "card" || li.engine === "letterbox" || li.engine === "blurfill") && a.below_card) return Math.min(a.below_card.y + 70, 1480);
    return fallback;
  }

  return { W, H, LEGACY, NEW, ENGINES, ASPECT, MORPH_FRAMES, MORPH_EASE, VIAS_NEW, DEFAULTS, engineOf, resolve, defaultVia, frameRect,
    geom, winFraming, applyDim, lerpExt, lerpBase, fadeThrough, autoFrames, worstStep, lerpCell, easeOf, morphBlur, info, captionY, corner };
});
