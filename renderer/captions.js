/* Vibe Editing OS caption renderer (E-05). Classic script, loaded by player.html before core.js.
 *
 * Draws the chunk list that the engine's caption profile engine (engine/src/veos/capengine.py) put in the bundle
 * (`VEOS_BUNDLE.captions`, also work/captions.json). Python decides the words, chunks, lines, fonts, sizes, colours,
 * emphasis and timing; this file only lays the block out (measured with the loaded fonts), anchors it to the stage
 * (fixed_y, seam, seam_above, below_card, chest, inside_footage, top_left), animates swaps / word reveals / karaoke / kinetic
 * stacks, and applies the hide rules. Every frame is a pure function of n.
 *
 * Captions are drawn in screen space at z7 by core.js (`__subtitles`): stage morphs, footage camera presets and the
 * canvas camera never move them. A v1 playbook gets the `legacy` profile, drawn exactly like the old auto-subtitles.
 */
(function () {
"use strict";
const W = 1080, H = 1920;
const cl = (x, a = 0, b = 1) => (x < a ? a : x > b ? b : x);
const r2 = v => Math.round(v * 100) / 100;
const esc = s => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;");
const eOut = p => 1 - Math.pow(1 - cl(p), 3);
const eBack = p => { p = cl(p); const s = 1.70158, q = p - 1; return 1 + (s + 1) * q * q * q + s * q * q; };
const HASH = (i, j = 0) => { const x = Math.sin(i * 127.1 + j * 311.7 + 0.5) * 43758.5453; return x - Math.floor(x); };
const DEV = /[ऀ-ॿ]/;

let C = null, E = null, ALL = [], HIDES = [], LIVE = [], STACK = new Map();
const _cv = typeof document !== "undefined" ? document.createElement("canvas").getContext("2d") : null;
// node (engine tests) has no canvas: an average-advance estimate keeps the layout maths testable
const measure = (s, font) => {
  if (_cv) { _cv.font = font; return _cv.measureText(s).width; }
  const m = /(\d+(?:\.\d+)?)px/.exec(font); return String(s).length * 0.55 * (m ? +m[1] : 56);
};
const segs = s => (typeof Intl !== "undefined" && Intl.Segmenter) ? Array.from(new Intl.Segmenter().segment(s), x => x.segment) : Array.from(s);

/* directional blur (the `smear` swap): an SVG gaussian with a per-axis stdDeviation. Package D adds a shared ctx.blur;
   this is the caption copy. Each frame collects the filters it uses in DEFS and emits them once with the captions. */
let DEFS = new Map();
function dirBlur(px, ang) {
  px = Math.round(px * 10) / 10; ang = Math.round(+ang || 0);
  if (px < 0.1) return "";
  const a = ang * Math.PI / 180, sx = r2(Math.abs(Math.cos(a)) * px), sy = r2(Math.abs(Math.sin(a)) * px);
  const id = `vcap-db-${String(px).replace(".", "_")}-${ang < 0 ? "m" + -ang : ang}`;
  if (!DEFS.has(id)) DEFS.set(id, `<filter id="${id}" x="-100%" y="-100%" width="300%" height="300%" color-interpolation-filters="sRGB"><feGaussianBlur stdDeviation="${sx} ${sy}"/></filter>`);
  return `url(#${id})`;
}
const defsHTML = () => DEFS.size ? `<svg width="0" height="0" style="position:absolute;width:0;height:0" aria-hidden="true"><defs>${[...DEFS.values()].join("")}</defs></svg>` : "";

/* wipe mask: `reveal` grows the visible part in `dir`; `erase` moves the edge in `dir` and hides what it passes.
   v = progress 0..1, F = feather px. Fully hidden at v = 0 (reveal) and v = 1 (erase). A mask only covers its element's
   box, so a masked element gets WIPE_PAD px of padding above and below (cancelled by an equal negative margin: nothing
   moves) and letter tails (p, g, y) that paint below the line box are not cut while the wipe runs (fix-visual). */
const WIPE_PAD = 48, WIPE_PAD_CSS = `padding-top:${WIPE_PAD}px;padding-bottom:${WIPE_PAD}px;margin-top:-${WIPE_PAD}px;margin-bottom:-${WIPE_PAD}px;`;
const GRAD = { right: "to right", left: "to left", down: "to bottom", up: "to top" };
const OPP = { right: "left", left: "right", down: "up", up: "down" };
function wipeMask(dir, v, F, erase) {
  const d = GRAD[dir] ? dir : "right";
  const g = erase ? GRAD[OPP[d]] : GRAD[d], s = cl(erase ? 1 - v : v);
  const m = `linear-gradient(${g},#000 calc(${r2(s * 100)}% - ${r2((1 - s) * F)}px),transparent calc(${r2(s * 100)}% + ${r2(s * F)}px))`;
  return `-webkit-mask-image:${m};mask-image:${m};-webkit-mask-repeat:no-repeat;mask-repeat:no-repeat;`;
}

function hexRgb(c) {
  const m = /^#([0-9a-f]{3}|[0-9a-f]{6})$/i.exec(String(c || "").trim());
  if (!m) return null;
  let h = m[1]; if (h.length === 3) h = h.split("").map(x => x + x).join("");
  return [parseInt(h.slice(0, 2), 16), parseInt(h.slice(2, 4), 16), parseInt(h.slice(4, 6), 16)];
}
function rgba(c, a) { const v = hexRgb(c); return v ? `rgba(${v[0]},${v[1]},${v[2]},${a})` : c; }
function mix(c1, c2, p) {
  const a = hexRgb(c1), b = hexRgb(c2); if (!a || !b) return p < 0.5 ? c1 : c2;
  return `rgb(${Math.round(a[0] + (b[0] - a[0]) * p)},${Math.round(a[1] + (b[1] - a[1]) * p)},${Math.round(a[2] + (b[2] - a[2]) * p)})`;
}
/* "0 2 6 rgba(0,0,0,.6), 0 0 12 #000" -> px units; "none" -> "" */
function cssShadow(s) {
  if (!s || s === "none") return "";
  const parts = []; let depth = 0, cur = "";
  for (const ch of String(s)) { if (ch === "(") depth++; if (ch === ")") depth--; if (ch === "," && depth === 0) { parts.push(cur); cur = ""; } else cur += ch; }
  parts.push(cur);
  return parts.map(p => p.trim().replace(/(^|\s)(-?\d*\.?\d+)(?=\s|$)/g, (m, sp, num) => `${sp}${num}px`)).join(", ");
}
const famStack = f => `'${f}','Noto Sans Devanagari','Noto Color Emoji',sans-serif`;
const fontOf = (w, size) => `${w.it && !w.dev ? "italic " : ""}${w.wt} ${r2(size == null ? w.sz : size)}px ${w.dev ? `'${w.dfam || "Noto Sans Devanagari"}',${famStack(w.fam)}` : famStack(w.fam)}`;

/* ------------------------------------------------------------------------------------------- init */
function init(B, env) {
  C = B && B.captions;
  if (!C || !(C.chunks || C.legacy)) return null;
  E = env;
  API.active = true;
  ALL = (C.chunks || []).concat(C.hidden_chunks || []).sort((a, b) => a.f0 - b.f0);
  const sec = t => Math.round(t * 30);
  HIDES = (C.hide || []).map(h => [sec(h[0]), sec(h[1]), h[2]]);
  const hideSet = new Set(Object.values(C.profiles || {}).flatMap(p => p.hide || []));
  LIVE = [];
  for (const s of env.scenes || []) {
    const a = sec(s.t_in), b = Math.max(sec(s.t_out), a + 1);
    if (s.z === 8 && hideSet.has("under_z8")) LIVE.push([a, b, "z8"]);
    if (hideSet.has("E2") && /^(E2|chaos_burst)$/i.test(String(s.exception || ""))) LIVE.push([a, b, "E2"]);
  }
  STACK = new Map();
  for (const c of ALL) if (c.stack) { if (!STACK.has(c.stack.id)) STACK.set(c.stack.id, []); STACK.get(c.stack.id).push(c); }
  const loads = [];
  for (const f of C.fallback_fonts || []) for (const x of f.files || []) {
    const ff = new FontFace(f.family, `url("${x.src}")`, { weight: x.weight || "400", style: x.style || "normal" });
    loads.push(ff.load().then(y => { document.fonts.add(y); }).catch(() => {}));
  }
  return Promise.all(loads).then(async () => {
    const fams = new Set(ALL.flatMap(c => (c.words || []).map(w => w.fam).filter(Boolean)));
    for (const f of fams) { await document.fonts.load(`400 40px '${f}'`, "Aa1").catch(() => {}); await document.fonts.load(`italic 400 40px '${f}'`, "Aa1").catch(() => {}); }
    // Indic-script fallbacks (Devanagari, Telugu, Tamil, ...) load with a sample of their own script
    for (const f of C.fallback_fonts || []) if (f.sample || /Devanagari/.test(f.family)) await document.fonts.load(`400 40px '${f.family}'`, f.sample || "कार").catch(() => {});
  });
}

/* ------------------------------------------------------------------------------------------- legacy (v1) */
// core.js subtitleHTML, unchanged: the v1 mapping profile renders exactly as the old auto-subtitles.
function legacyHTML(n, st, world) {
  const TL = E.TL, T = E.T, W0 = E.W;
  if (!TL.captions || TL.captions.subtitles === "off" || TL.captions.subtitles === false) return "";
  for (const h of E.HIDE) if (n >= h[0] && n < h[1]) return "";
  for (const z of E.Z8) if (n >= z[0] && n < z[1]) return "";
  if (st.morph && (((C.profiles || {})["CS-1"] || {}).position || {}).hide_on_morph !== false) return "";
  let card = null; for (const c of C.legacy_cards || []) { if (n >= c[0] && n < c[1]) { card = { text: c[2] }; break; } if (c[0] > n) break; }
  if (!card) return "";
  const L = T.layout, P = L.panel || {};
  let cy = (L.caption_cy && L.caption_cy.full) || 1300, cx = W0 / 2, maxW = 960;
  if (st.name === "panel") cy = (P.bleed_top || 1135) - 60;
  else if (st.name === "inset") cy = ((P.inset && P.inset.y[0]) || 1008) - 60;
  else if (st.name === "slide-aside") { const sw = (L.slide_aside && L.slide_aside.x[1]) || 450; cx = (sw + W0) / 2; maxW = W0 - sw - 60; }
  const ST = T.type.subtitle || {}, size0 = (Array.isArray(ST.size) ? (ST.size[0] + ST.size[1]) / 2 : ST.size) || 58;
  const font = `${ST.weight || 800} ${size0}px ${E.fam(ST.slot || "body")}`;
  const w0 = E.measure(card.text, font), size = w0 > maxW ? Math.floor(size0 * maxW / w0) : size0;
  const onLight = st.name !== "full" && st.name !== "low" && world === "canvas";
  const c = onLight ? E.col("ink") : E.col("paper");
  const sh = onLight ? "none" : "0 3px 14px rgba(0,0,0,.55),0 1px 3px rgba(0,0,0,.45)";
  return `<div style="position:absolute;left:${r2(cx - maxW / 2)}px;width:${maxW}px;top:${r2(cy)}px;transform:translateY(-50%);text-align:center;white-space:nowrap;font:${ST.weight || 800} ${size}px/1.1 ${E.fam(ST.slot || "body")};color:${c};text-shadow:${sh}">${esc(card.text)}</div>`;
}

/* ------------------------------------------------------------------------------------------- swaps */
const FLICKER = [1, 0, 0, 1, 0, 1]; // capengine.FLICKER_PATTERN: 3 flashes in 6 f (no flash limit)
/* swap-in state at frame k of `frames`: op(acity), dy, sc(ale), bl(ur, isotropic) and, for the Package C swaps,
   dx, sx (x-stretch), db (directional blur px at angle ang) and wipe {v, dir, F}. */
function swapState(type, k, frames, sw) {
  const o = { op: 1, dy: 0, sc: 1, bl: 0, dx: 0, sx: 1, db: 0, ang: 0, wipe: null };
  if (type === "hard" || !frames || k >= frames) return o;
  const p = cl((k + 1) / (frames + 1));
  if (type === "fade") o.op = eOut(p);
  else if (type === "blur") { o.op = eOut(p); o.bl = (sw.blur_px || 10) * (1 - eOut(p)); }
  else if (type === "rise") { o.op = eOut(p); o.dy = (sw.rise_px || 24) * (1 - eOut(p)); o.bl = (sw.blur_px || 0) * (1 - eOut(p)); }
  else if (type === "pop") { o.op = cl(p * 2); o.sc = 0.72 + 0.28 * eBack(p); }
  else if (type === "flicker") { const pat = sw.pattern || FLICKER; o.op = k < pat.length ? cl(+pat[k]) : 1; }
  else if (type === "wipe") o.wipe = { v: eOut(p), dir: sw.dir || "right", F: sw.feather_px != null ? +sw.feather_px : 40, erase: false };
  else if (type === "smear") smear(o, 1 - eOut(p), sw, -1);
  return o;
}
/* smear amount q (1 = fully smeared): a directional blur along `angle`, an x-stretch and a travel offset. side -1 = it
   arrives from behind its direction (in), +1 = it leaves ahead (out). */
function smear(o, q, sw, side) {
  const ang = +sw.angle || 0, dir = sw.dir === "left" ? -1 : 1;
  o.op = cl(1.25 - q);
  o.db = (sw.smear_px != null ? +sw.smear_px : 24) * q; o.ang = ang;
  o.sx = 1 + ((sw.stretch != null ? +sw.stretch : 1.6) - 1) * q;
  o.dx = side * dir * (sw.travel_px != null ? +sw.travel_px : 40) * q;
}
/* swap-out state with `rem` frames left (1 = the last visible frame) of an out swap of `outF` frames: wipe erases in
   out_dir (default the opposite of dir: in L->R, out R->L), smear leaves along its direction; others fade (as before). */
function swapOut(type, rem, outF, sw) {
  const o = { op: 1, dy: 0, sc: 1, bl: 0, dx: 0, sx: 1, db: 0, ang: 0, wipe: null };
  const p = cl((outF - rem + 1) / (outF + 1));
  if (type === "wipe") o.wipe = { v: eOut(p), dir: sw.out_dir || OPP[sw.dir || "right"], F: sw.feather_px != null ? +sw.feather_px : 40, erase: true };
  else if (type === "smear") smear(o, eOut(p), sw, 1);
  else o.op = eOut(cl(rem / outF));
  return o;
}
/* the filter (directional + isotropic blur) and wipe-mask CSS of a swap state. noPad: the element has its own padding (a
   pill / box chunk: its padding already holds the descenders), so the wipe pad is not added */
function stateCss(s, isotropic, noPad) {
  let css = "";
  const filt = [s.db > 0.1 ? dirBlur(s.db, s.ang) : "", isotropic > 0.05 ? `blur(${r2(isotropic)}px)` : ""].filter(Boolean).join(" ");
  if (filt) css += `filter:${filt};`;
  if (s.wipe) css += wipeMask(s.wipe.dir, s.wipe.v, s.wipe.F, s.wipe.erase) + (noPad ? "" : WIPE_PAD_CSS);
  return css;
}

/* ------------------------------------------------------------------------------------------- layout */
function wordWidth(w, trk) {
  let x = measure(w.t, fontOf(w)) + (w.dev ? 0 : trk * w.sz * w.t.length);
  if (w.fx && w.fx.chip) x += 2 * ((w.fx.chip.pad || [2, 10])[1]);
  return x;
}
function layoutChunk(c, prof) {
  const sk = prof.skin || {}, trk = +sk.tracking || 0, lh = +sk.line_height || 1.15;
  const cont = sk.container || {}, ctype = cont.type || "none", pad = cont.padding || [0, 0];
  const tiers = prof.tiers || {}, lb = c.line_box || [];
  const lpad = tiers.connector_container ? (tiers.connector_container.padding || [6, 16]) : pad;
  const lines = (c.lines && c.lines.length ? c.lines : [c.words.map((_, k) => k)]).map((idx, li) => {
    const ws = idx.map(k => c.words[k]);
    const maxSz = Math.max(...ws.map(w => w.sz));
    const base = ws[0] || { sz: sk.size, wt: sk.weight, fam: sk.fam };
    const space = measure(" ", fontOf({ ...base, it: false, dev: false }, maxSz * 0.5 + base.sz * 0.5));
    let w = 0; ws.forEach((x, k) => { w += wordWidth(x, trk) + (k ? space : 0); });
    const boxed = ctype === "box_per_line" || !!lb[li];
    const bp = boxed ? (lb[li] ? lpad : pad) : [0, 0];
    return { ws, idx, w: w + 2 * bp[1], h: maxSz * lh + 2 * bp[0], maxSz, space, boxed, bp };
  });
  const blockPad = (ctype === "pill" || ctype === "box") ? pad : [0, 0];
  // skin.line_fit (block justify): each line grows to the widest line (`block`) or to max_w (`max_w`), at most
  // max_scale (1.6) x; the engine already scaled the sizes, this evens out the rest with the loaded fonts
  const lf = sk.line_fit;
  if (lf && (lines.length > 1 || (lf.to || lf) === "max_w")) {
    const to = lf.to || lf, ms = +lf.max_scale || 1.6;
    const cw = l => l.w - 2 * l.bp[1];
    const target = to === "max_w" ? (+((prof.position || {}).max_w) || 952) - 2 * blockPad[1] - 2 * (lines[0] ? lines[0].bp[1] : 0) : Math.max(...lines.map(cw));
    lines.forEach((l, li) => {
      const k = cl(target / Math.max(1, cw(l)), 1, ms);
      if (k <= 1.0005) return;
      l.ws = l.ws.map(w => ({ ...w, sz: w.sz * k }));
      l.maxSz *= k; l.space *= k;
      let w = 0; l.ws.forEach((x, j) => { w += wordWidth(x, trk) + (j ? l.space : 0); });
      l.w = w + 2 * l.bp[1]; l.h = l.maxSz * lh + 2 * l.bp[0];
    });
  }
  const gap =(prof.stack && prof.stack.gap_px) || (ctype === "box_per_line" ? 0 : 0);
  const bw = Math.max(...lines.map(l => l.w)) + 2 * blockPad[1];
  const bh = lines.reduce((a, l) => a + l.h, 0) + gap * Math.max(0, lines.length - 1) + 2 * blockPad[0];
  return { lines, bw, bh, blockPad, ctype, cont, trk, lh };
}

function anchorTop(c, prof, bh, fr) {
  const pos = prof.position || {}, safe = (E.T.layout && E.T.layout.safe) || { x: [64, 1016], y: [110, 1500] };
  const a = c.anchor || pos.anchor || "fixed_y", off = c.offset != null ? +c.offset : (+pos.offset || 0), g = fr.g;
  const win = g && g.op > 0.01 && g.w > 1 && g.h > 1;
  let top = null;
  if ((a === "chest" || c.avoided) && c.top != null) top = c.top;
  else if (a === "seam" && win) top = (g.y > 1 ? g.y : g.y + g.h) + (+pos.dy || 0) - bh / 2;
  else if (a === "seam_above" && win) top = (g.y > 1 ? g.y : g.y + g.h) - off - bh; // bottom edge `offset` px above the seam (clear of the head)
  else if (a === "below_card" && win) top = g.y + g.h + off;
  else if (a === "inside_footage" && win) top = Math.min(g.y + g.h, H) - off - bh;
  else if (a === "top_left") top = safe.y[0] + off;
  if (top == null) top = (c.cy != null ? +c.cy : (+pos.cy || 1300)) - bh / 2;
  return cl(top, safe.y[0], safe.y[1] - bh);
}

/* ------------------------------------------------------------------------------------------- words */
function wordStyle(w, prof, extra) {
  const sk = prof.skin || {};
  const trk = w.dev ? 0 : (+sk.tracking || 0);
  let sh = cssShadow(extra.shadow != null ? extra.shadow : sk.shadow); // a chunk may override the skin (ink flip: no dark shadow)
  let css = `font:${fontOf(w)};color:${extra.colour || w.c};letter-spacing:${r2(trk)}em;`;
  if (sk.stroke) css += `-webkit-text-stroke:${r2(2 * sk.stroke)}px ${sk.stroke_colour || "#000"};paint-order:stroke fill;`;
  if (w.fx && w.fx.glow) { const g = w.fx.glow; sh = `0 0 ${r2(g.r)}px ${rgba(g.c, 0.9)}, 0 0 ${r2(g.r * 2.2)}px ${rgba(g.c, 0.55)}` + (sh ? ", " + sh : ""); }
  if (sh) css += `text-shadow:${sh};`;
  if (w.fx && w.fx.chip) { // chip / box emphasis: a filled box behind the word (A18: CS-BOX cyan with glow, CS-HYPE yellow)
    const ch = w.fx.chip, p = ch.pad || [2, 10];
    css += `background:${ch.fill};border-radius:${ch.r != null ? ch.r : 8}px;padding:${p[0]}px ${p[1]}px;text-shadow:none;`;
    if (ch.glow) css += `box-shadow:0 0 ${r2(ch.glow)}px ${rgba(ch.fill, 0.75)};`;
    if (p[0] > 4) css += `margin:${-p[0]}px 0;`; // a tall box keeps the line's own height (the box overhangs the line)
  }
  if (w.fx && w.fx.underline) { const u = w.fx.underline; css += `background:linear-gradient(${u.c},${u.c}) 0 100%/100% ${u.h}px no-repeat;padding-bottom:${Math.round(u.h * 0.6)}px;`; }
  return css;
}

function chunkHTML(c, n, fr, opt) {
  const prof = C.profiles[c.profile] || {};
  const sk = prof.skin || {}, sw = prof.swap || {};
  const Lo = layoutChunk(c, prof);
  const maxW = +((prof.position || {}).max_w) || 952;
  const fit = Math.min(1, maxW / Math.max(1, Lo.bw));
  let top = opt.top != null ? opt.top : anchorTop(c, prof, Lo.bh * fit, fr);
  const pos = prof.position || {}, safe = (E.T.layout && E.T.layout.safe) || { x: [64, 1016] };
  const left = (c.anchor === "top_left" || pos.align === "left") ? safe.x[0] : W / 2 - Lo.bw / 2;
  // block enter / exit
  const word = prof.reveal === "word", chars = prof.reveal === "char";
  const type = c.swap_type || sw.type || "hard"; // a chunk's own swap_type wins over the profile
  // a chunk shorter than its swap-in still lands fully opaque on its last frame (a 1-frame word is never a 50% ghost);
  // the engine shortens the swap of fast chunks (chunk.swap_frames, capengine.swap_frames_for): settled from the 2nd frame
  const swf = c.swap_frames != null ? +c.swap_frames : (sw.frames | 0);
  let st = (word || chars) ? { op: 1, dy: 0, sc: 1, bl: 0 } : swapState(type, n - c.f0, Math.min(swf, Math.max(0, c.f1 - c.f0 - 1)), sw);
  if (opt.enter) st = opt.enter;
  let op = st.op;
  const outF = sw.out_frames | 0;
  if (outF && !opt.stack) {
    const nx = ALL.find(d => d.f0 >= c.f1);
    if (!nx || nx.f0 > c.f1) {
      const rem = c.f1 - n;
      if ((type === "wipe" || type === "smear") && rem <= outF) { // wipe / smear leave with their own out swap
        const so = swapOut(type, rem, outF, sw);
        st = { ...st, dx: so.dx, sx: so.sx, db: so.db, ang: so.ang, wipe: so.wipe }; op *= so.op;
      } else op *= eOut(cl(rem / outF));
    }
  }
  if (opt.op != null) op *= opt.op;
  const bl = Math.max(st.bl, opt.bl || 0);
  const rot = +sk.rotate || 0;
  const kar = prof.karaoke;
  let html = "";
  Lo.lines.forEach((l, li) => {
    let inner = "";
    l.ws.forEach((w, k) => {
      let colour = w.c, wop = 1, wdy = 0, wsc = 1, wbl = 0, ws2 = null;
      if (kar) {
        const fr0 = w.f, kf = kar.frames || 3;
        if (kar.mode === "current") {
          const nxw = c.words[l.idx[k] + 1];
          const on = n >= fr0 && (!nxw || n < nxw.f);
          colour = on ? mix(kar.queued, kar.active, cl((n - fr0 + 1) / kf)) : kar.queued;
        } else colour = n >= fr0 ? mix(kar.queued, kar.active, cl((n - fr0 + 1) / kf)) : kar.queued;
        if (w.emph || w.tier === 2) colour = w.c;
      }
      if (word) {
        if (n < w.f) { wop = 0; } else {
          const s2 = swapState(w.st || sw.type || "fade", n - w.f, w.sf != null ? +w.sf : (sw.frames || 3), sw);
          wop = s2.op; wdy = s2.dy; wsc = s2.sc; wbl = s2.bl;
          if (s2.db > 0.1 || s2.wipe || s2.sx !== 1 || s2.dx) ws2 = s2; // a smear / wipe word
        }
      }
      let css = wordStyle(w, prof, { colour, shadow: c.shadow });
      let text = esc(w.t);
      if (chars) { // per-character type-on (reveal: char): typed glyphs show, the rest keeps its place, hidden
        const g = w.dev ? [w.t] : segs(w.t), tf = Math.max(1, w.tf != null ? +w.tf : Math.ceil(g.length * 30 / (+prof.cps || 30)));
        const shown = n < w.f ? 0 : Math.min(g.length, Math.ceil(g.length * (n - w.f + 1) / tf));
        if (shown < g.length) text = esc(g.slice(0, shown).join("")) + `<span style="visibility:hidden">${esc(g.slice(shown).join(""))}</span>`;
      }
      const anim = wop < 1 || wdy || wsc !== 1 || wbl > 0.05 || !!ws2;
      if (anim || (w.fx && w.fx.chip)) css += `display:inline-block;`;
      if (ws2) css += `opacity:${r2(wop)};transform:translate(${r2(ws2.dx)}px,${r2(wdy)}px) scale(${r2(wsc)}) scaleX(${r2(ws2.sx)});${stateCss(ws2, wbl)}`;
      else if (anim) css += `opacity:${r2(wop)};transform:translateY(${r2(wdy)}px) scale(${r2(wsc)});${wbl > 0.05 ? `filter:blur(${r2(wbl)}px);` : ""}`;
      inner += (k ? " " : "") + `<span style="${css}">${text}</span>`;
    });
    const lineCss = `height:${r2(l.h)}px;line-height:${r2(l.h - 2 * l.bp[0])}px;white-space:nowrap;text-align:${pos.align === "left" ? "left" : "center"};font:${fontOf({ ...(l.ws[0] || {}), it: false, dev: false }, l.maxSz)};`;
    if (l.boxed) {
      const cc = (prof.tiers && prof.tiers.connector_container && c.line_box && c.line_box[li]) ? prof.tiers.connector_container : Lo.cont;
      const fill = rgba(cc.fill_hex || cc.fill || "#000", cc.opacity == null ? 1 : cc.opacity);
      html += `<div style="${lineCss}"><span style="display:inline-block;background:${fill};border-radius:${cc.radius || 0}px;padding:${l.bp[0]}px ${l.bp[1]}px;line-height:${r2(l.h - 2 * l.bp[0])}px">${inner}</span></div>`;
    } else html += `<div style="${lineCss}">${inner}</div>`;
  });
  let box = "";
  if (Lo.ctype === "pill" || Lo.ctype === "box") {
    const cc = Lo.cont, fill = rgba(cc.fill, cc.opacity == null ? 1 : cc.opacity);
    const rad = Lo.ctype === "pill" ? (cc.radius != null ? cc.radius : 999) : (cc.radius || 0);
    const bsh = cssShadow(cc.shadow);
    box = `background:${fill};border-radius:${rad}px;padding:${Lo.blockPad[0]}px ${Lo.blockPad[1]}px;${bsh ? `box-shadow:${bsh};` : ""}`;
  }
  // smear / wipe (Package C) add an x travel + stretch, a directional blur and a mask; other swaps keep the old CSS
  const pc = (st.dx || (st.sx != null && st.sx !== 1) || st.db > 0.1 || st.wipe);
  const tf = pc ? `translate(${r2(st.dx || 0)}px,${r2(st.dy + (opt.dy || 0))}px) scale(${r2(fit * st.sc)}) scaleX(${r2(st.sx || 1)})${rot ? ` rotate(${rot}deg)` : ""}`
    : `translateY(${r2(st.dy + (opt.dy || 0))}px) scale(${r2(fit * st.sc)})${rot ? ` rotate(${rot}deg)` : ""}`;
  const filt = pc ? stateCss(st, bl, !!box) : (bl > 0.05 ? `filter:blur(${r2(bl)}px);` : "");
  return `<div data-cap="${esc(c.id)}" style="position:absolute;left:${r2(left)}px;top:${r2(top - (Lo.bh - Lo.bh * fit) / 2)}px;width:${r2(Lo.bw)}px;transform-origin:50% 50%;transform:${tf};opacity:${r2(cl(op))};${filt}${box}box-sizing:border-box">${html}</div>`;
}

/* kinetic stack: lines accumulate top-down from stack.top; each rises in with a blur; the stack clears at once */
function stackHTML(lines, n, fr) {
  const c0 = lines[0], prof = C.profiles[c0.profile] || {}, S = prof.stack || {}, sk = prof.skin || {};
  const fEnd = c0.stack.f_end, clear = c0.stack.clear || S.clear_frames || 6, frames = S.frames || 9;
  const shown = lines.filter(c => c.f0 <= n);
  if (!shown.length) return "";
  const safe = (E.T.layout && E.T.layout.safe) || { y: [110, 1500] };
  let y = S.top != null ? +S.top : (c0.cy != null ? c0.cy : (+((prof.position || {}).cy) || 1000));
  const gap = S.gap_px || 0;
  let q = 1, cbl = 0;
  if (n >= fEnd - clear) { const p = cl((n - (fEnd - clear) + 1) / (clear + 1)); q = 1 - eOut(p); cbl = (S.blur_px || 6) * eOut(p); }
  let out = "";
  const rr = Array.isArray(S.rise_px) ? S.rise_px : [S.rise_px || 60, S.rise_px || 60];
  for (const c of shown) {
    const Lo = layoutChunk(c, prof);
    const k = n - c.f0, p = cl((k + 1) / (frames + 1));
    const rise = rr[0] + (rr[1] - rr[0]) * HASH(c.f0, 7);
    const enter = { op: eOut(p), dy: rise * (1 - eOut(p)), sc: 1, bl: (S.blur_px || 6) * (1 - eOut(p)) };
    const top = Math.min(y, safe.y[1] - Lo.bh);
    out += chunkHTML(c, n, fr, { top, enter, op: q, bl: cbl, stack: true });
    y += Lo.bh + gap;
  }
  return out;
}

/* ------------------------------------------------------------------------------------------- frame */
function html(n, fr) {
  if (!C) return "";
  if (C.legacy) return legacyHTML(n, fr.st, fr.world);
  if (C.mode === "off") return "";
  for (const h of HIDES) if (n >= h[0] && n < h[1]) return "";
  for (const h of LIVE) if (n >= h[0] && n < h[1]) return "";
  const TLc = E.TL.captions || {};
  if (TLc.subtitles === "off" || TLc.subtitles === false) return "";
  DEFS = new Map();
  let out = "";
  const seen = new Set();
  for (const c of ALL) {
    if (c.f0 > n) break;
    if (c.stack) {
      if (seen.has(c.stack.id) || n >= c.stack.f_end) continue;
      seen.add(c.stack.id);
      if (fr.st.morph && (C.profiles[c.profile].position || {}).hide_on_morph !== false) continue;
      out += stackHTML(STACK.get(c.stack.id), n, fr);
      continue;
    }
    if (n >= c.f1) continue;
    if (fr.st.morph && (C.profiles[c.profile].position || {}).hide_on_morph !== false) continue;
    out += chunkHTML(c, n, fr, {});
  }
  return out + defsHTML();
}

const API = { active: false, init, html, chunks: () => ALL };
if (typeof window !== "undefined") window.VEOS_CAPTIONS = API;
// node (engine tests): the pure swap maths and a frame of HTML from a bundle's captions block, no fonts
if (typeof module !== "undefined" && module.exports) {
  module.exports = { swapState, swapOut, wipeMask, stateCss, dirBlur, segs,
    frame(B, env, n, fr) { C = B.captions; E = env; ALL = (C.chunks || []).slice().sort((a, b) => a.f0 - b.f0); HIDES = []; LIVE = []; STACK = new Map(); return html(n, fr); } };
}
})();
