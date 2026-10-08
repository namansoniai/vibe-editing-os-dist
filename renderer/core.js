/* Vibe Editing OS renderer core v0 (CONTRACT sections 2-4). Classic script; every frame is a pure function of n. */
(function () {
"use strict";
const W = 1080, H = 1920, FPS = 30;
const cl = (x, a = 0, b = 1) => (x < a ? a : x > b ? b : x);
const lerp = (a, b, p) => a + (b - a) * p;
const r2 = v => Math.round(v * 100) / 100;
const HASH = (i, j = 0) => { const x = Math.sin(i * 127.1 + j * 311.7 + 0.5) * 43758.5453; return x - Math.floor(x); };
function bez(x1, y1, x2, y2) {
  return x => {
    if (x <= 0) return 0; if (x >= 1) return 1; let t = x;
    for (let i = 0; i < 12; i++) {
      const u = 1 - t, f = 3 * x1 * t * u * u + 3 * x2 * t * t * u + t * t * t - x; if (Math.abs(f) < 1e-6) break;
      const d = 3 * x1 * u * u + 6 * (x2 - x1) * t * u + 3 * (1 - x2) * t * t; if (Math.abs(d) < 1e-6) break; t = cl(t - f / d);
    }
    const u = 1 - t; return 3 * y1 * t * u * u + 3 * y2 * t * t * u + t * t * t;
  };
}
const BO = (p, s = 1.70158) => { p = cl(p); const c = s + 1, q = p - 1; return 1 + c * q * q * q + s * q * q; };
function mulberry32(a) { return function () { a |= 0; a = (a + 0x6D2B79F5) | 0; let t = Math.imul(a ^ (a >>> 15), 1 | a); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; }; }
function hash32(s) { let h = 2166136261; for (let i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 16777619); } return h >>> 0; }

let EO, EI, EIO, EL; // set from tokens
const ease = { out: x => EO(x), in: x => EI(x), inOut: x => EIO(x), back: BO, elastic: x => EL(x) };

/* ---------------------------------------------------------------- scenes (CONTRACT v2): written per reel in plan/scenes.js */
const SMEAR_MAX = 48; // px: the velocity smear's largest blur (fix-visual; was a fixed 24)
const PRESET_NAMES = ["settle", "pop", "squash", "rise", "drop", "blur", "stamp", "slide-l", "slide-r", "rocket", "none"];
const SCENES = [];
const VEOS = window.VEOS = { scenes: SCENES, errors: [] };
const isNum = v => typeof v === "number" && isFinite(v);
const TRK = window.VEOS_TRACKS || null; // Package E object tracks + scene anchors (tracks.js; loaded before core.js)
let TRACKS = {};
VEOS.scene = function (d) {
  const id = d && d.id != null ? String(d.id) : "(no id)", bad = m => { VEOS.errors.push(`scene ${id}: ${m}`); return null; };
  if (!d || typeof d !== "object") return bad("VEOS.scene needs an object");
  if (d.id == null || d.id === "") return bad("missing id");
  if (SCENES.some(s => s.id === id)) return bad("duplicate id");
  if (typeof d.render !== "function") return bad("render must be a function render(ctx, lt, dur)");
  if (!isNum(d.t_in) || !isNum(d.t_out)) return bad("t_in and t_out must be numbers (edit-time seconds)");
  if (d.t_out <= d.t_in) return bad(`t_out (${d.t_out}) must be greater than t_in (${d.t_in})`);
  if (!isNum(d.z) || d.z < 1 || d.z > 11 || Math.round(d.z) !== d.z) return bad("z must be an integer 1-11");
  for (const k of ["in", "out"]) if (d[k] != null && !PRESET_NAMES.includes(d[k])) return bad(`${k}: '${d[k]}' is not a preset (${PRESET_NAMES.join("|")})`);
  if (d.box != null && !(d.box && ["x", "y", "w", "h"].every(k => isNum(d.box[k])))) return bad("box must be {x,y,w,h} numbers");
  if (d.events != null && !(Array.isArray(d.events) && d.events.every(isNum))) return bad("events must be an array of local seconds");
  if (d.cuts != null && !(Array.isArray(d.cuts) && d.cuts.every(isNum))) return bad("cuts must be an array of local seconds");
  if (d.overlaps != null && !(Array.isArray(d.overlaps) && d.overlaps.every(x => typeof x === "string"))) return bad("overlaps must be an array of scene ids");
  if (d.roles != null && !Array.isArray(d.roles)) return bad("roles must be an array of colour-role names");
  if (d.parallax != null && d.parallax !== false && !(isNum(d.parallax) && d.parallax >= 0 && d.parallax <= 1)) return bad("parallax must be a number 0..1 or false (canvas camera)");
  if (d.nodes != null && !(Array.isArray(d.nodes) && d.nodes.every(q => q && q.id != null && ["x", "y", "w", "h"].every(k => isNum(q[k]))))) return bad("nodes must be [{id, x, y, w, h}] (world px)");
  if (d.follow_footage != null && typeof d.follow_footage !== "boolean") return bad("follow_footage must be true or false (a behind scene rides the footage reframe / camera; a front scene rides the camera)");
  if (d.anchor != null && typeof d.anchor === "object") { // Package E: follow an object track (renderer/tracks.js); a string anchor is a helper's own layout option
    const ae = TRK ? TRK.errors(d.anchor) : ["tracks.js is not loaded"];
    if (!d.box) ae.push("an anchored scene needs a box (its centre lands on the track point)");
    if (d.follow_footage) ae.push("anchor and follow_footage are exclusive (an anchor already follows the footage)");
    if (ae.length) return bad(ae.join("; "));
  }
  if (d.text_px != null &&!(isNum(d.text_px) && d.text_px > 0)) return bad("text_px must be a positive number (smallest font-size in px)");
  // fx-helpers: per-scene preset lengths, stepped ("on twos") animation, velocity smear on the presets
  for (const k of ["in_frames", "out_frames"]) if (d[k] != null && !(isNum(d[k]) && Math.round(d[k]) === d[k] && d[k] >= 0 && d[k] <= 60)) return bad(`${k} must be a whole number of frames 0-60 (the ${k === "in_frames" ? "enter" : "exit"} preset's length)`);
  if (d.step_frames != null && !(isNum(d.step_frames) && Math.round(d.step_frames) === d.step_frames && d.step_frames >= 1 && d.step_frames <= 6)) return bad("step_frames must be a whole number 1-6 (2 = animate on twos)");
  if (d.step_fps != null && !(isNum(d.step_fps) && d.step_fps >= 5 && d.step_fps <= 30)) return bad("step_fps must be a number 5-30 (12 = graphics at 12 fps)");
  if (d.step_frames != null && d.step_fps != null) return bad("set step_frames or step_fps, not both");
  if (d.smear != null && typeof d.smear !== "boolean") return bad("smear must be true or false (directional motion blur on the enter/exit presets)");
  // fix-visual: the smear cap (px, default the style's motion.smear_push.motion_blur_px, else 24) and an opaque enter preset
  if (d.smear_px != null && !(isNum(d.smear_px) && d.smear_px >= 0 && d.smear_px <= SMEAR_MAX)) return bad(`smear_px must be a number 0-${SMEAR_MAX} (the velocity smear's maximum blur)`);
  if (d.in_fade != null && typeof d.in_fade !== "boolean") return bad("in_fade must be true or false (an override: travel presets arrive opaque, the others fade in)");
  if (d.grade !== undefined && !(d.grade === null || d.grade === false || typeof d.grade === "string" || (typeof d.grade === "object" && !Array.isArray(d.grade)))) return bad("grade must be a tokens.grades.scene id, a CSS filter list, a grade object, or null/\"off\" (E-16)");
  SCENES.push(d); return d;
};
VEOS.words = (a = -1e9, b = 1e9) => ((window.VEOS_BUNDLE && window.VEOS_BUNDLE.words) || []).filter(w => w.s >= a && w.s < b);
VEOS.timeline = () => (window.VEOS_BUNDLE && window.VEOS_BUNDLE.timeline) || {};
/* scenes that depend on other scenes (fx.shatter's source) bind them once every scene is registered */
VEOS.resolveScenes = () => { for (const s of SCENES.slice()) if (typeof s.resolve === "function") { try { s.resolve(SCENES); } catch (e) { VEOS.errors.push(`scene ${s.id}: ${e.message}`); } } };
VEOS.sceneMeta = () => SCENES.map(s => { const o = {}; for (const k of Object.keys(s)) if (typeof s[k] !== "function") o[k] = s[k]; return o; });

/* ---------------------------------------------------------------- E-08 data contract: figures + the number formatter
   The engine resolves plan/figures.json (bundle.figures: {figures {id: {steps [{x, at, value, computed, shown, text}],
   shown, format, scale_id, ...}}, scales {id: {max}}}) and the style's numbers profile (bundle.numbers). Usable at load
   time (VEOS.*) and in render (ctx.*). fmtNum mirrors engine numfmt.fmt_num exactly (renderer/numbers.js). */
const NUMF = window.VEOS_NUM || null;
const FIGDATA = () => ((window.VEOS_BUNDLE || {}).figures || {});
const numBase = () => { const b = window.VEOS_BUNDLE || {}; return b.numbers || (NUMF ? NUMF.profileOf(b.tokens) : {}); };
VEOS.fig = id => ((FIGDATA().figures || {})[id]) || null;
VEOS.figScale = id => ((FIGDATA().scales || {})[id]) || null;
/* fmtNum(value, figureIdOrFormat, override): a figure id (its format), a format object, or "full" | "short" | "long" | "percent" */
VEOS.fmtNum = (v, f, over) => {
  if (!NUMF) return String(v);
  const fg = typeof f === "string" ? VEOS.fig(f) : (f && f.steps && f.format ? f : null);
  const spec = NUMF.resolveSpec(fg ? fg.format : f, numBase());
  return NUMF.fmt(v, over, spec);
};
/* figAt(id, t, {roll: frames (12), from: 0}): the figure's displayed value at edit time t. Steps land at their `at` (the
   spoken word): the value rolls from the previous step over `roll` frames ENDING on `at` (counters land on the word). */
VEOS.figAt = (id, t, o = {}) => {
  const fg = typeof id === "string" ? VEOS.fig(id) : id;
  if (!fg) return { value: null, i: -1, p: 1, landed: false };
  const roll = (o.roll != null ? o.roll : 12) / 30, steps = fg.steps || [];
  let prev = o.from != null ? o.from : 0, i = -1;
  for (let k = 0; k < steps.length; k++) {
    const st = steps[k], at = st.at == null ? -1e9 : st.at;
    if (t >= at - 1e-6) { prev = st.shown; i = k; continue; }
    if (t >= at - roll) { const p = Math.min(1, Math.max(0, (t - (at - roll)) / roll)), e = 1 - Math.pow(1 - p, 3); return { value: prev + (st.shown - prev) * e, i: k, p, landed: false, from: prev, to: st.shown }; }
    break;
  }
  return { value: i >= 0 ? steps[i].shown : prev, i, p: 1, landed: i >= 0 };
};

/* ---------------------------------------------------------------- enter / exit presets */
const IN_F = { settle: 8, pop: 7, squash: 6, rise: 8, drop: 8, blur: 6, stamp: 5, "slide-l": 8, "slide-r": 8, rocket: 10, none: 0 };
const OUT_F = { rocket: 8, none: 0 };
const ID = () => ({ op: 1, sx: 1, sy: 1, dx: 0, dy: 0, rot: 0, bl: 0, vb: 0 });
function presetIn(name, p) {
  const o = ID(), e = EO(p);
  switch (name) {
    case "settle": o.op = cl(p * 2.5); o.sx = o.sy = 1.08 - 0.08 * e; o.bl = 6 * (1 - e); break;
    case "pop": o.op = cl(p * 3); o.sx = o.sy = 0.5 + 0.5 * BO(p, 2.2); break;
    case "squash": {
      o.op = cl(p * 4);
      if (p < 0.5) { const a = EO(p / 0.5); o.sx = lerp(1.2, 0.95, a); o.sy = lerp(0.7, 1.15, a); }
      else { const b = EO((p - 0.5) / 0.5); o.sx = lerp(0.95, 1, b); o.sy = lerp(1.15, 1, b); }
      break;
    }
    case "rise": o.op = cl(p * 2.5); o.dy = 70 * (1 - BO(p, 1.3)); o.vb = 8 * (1 - e); break;
    case "drop": o.op = cl(p * 3); o.dy = -40 * (1 - BO(p, 2.2)); o.vb = 8 * (1 - e); break;
    case "blur": o.op = e; o.bl = 10 * (1 - e); o.sx = o.sy = 1.04 - 0.04 * e; break;
    case "stamp": o.op = cl(p * 3); o.sx = o.sy = lerp(1.7, 1, EI(p)); o.rot = -6 * (1 - p); break;
    case "slide-l": o.op = cl(p * 4); o.dx = -700 * (1 - e); break;
    case "slide-r": o.op = cl(p * 4); o.dx = 700 * (1 - e); break;
    case "rocket": o.op = cl(p * 5); o.dy = H * 0.8 * (1 - e); o.vb = 20 * (1 - p); break;
    default: break;
  }
  return o;
}
function presetOut(name, p) {
  const o = ID(), ei = EI(p), eo = EO(p);
  switch (name) {
    case "settle": o.op = 1 - p; o.sx = o.sy = 1 - 0.04 * ei; o.bl = 6 * p; break;
    case "pop": o.op = 1 - cl(p * 1.2); o.sx = o.sy = 1 - 0.4 * ei; break;
    case "squash": o.op = 1 - p; o.sy = 1 - 0.3 * ei; o.sx = 1 + 0.15 * p; break;
    case "rise": o.op = 1 - p; o.dy = -50 * eo; o.vb = 8 * p; break;
    case "drop": o.op = 1 - p; o.dy = 70 * ei; o.vb = 8 * p; break;
    case "blur": o.op = 1 - p; o.bl = 10 * p; break;
    case "stamp": o.op = 1 - p; o.sx = o.sy = 1 + 0.15 * p; break;
    case "slide-l": o.op = 1 - cl(p * 1.5); o.dx = -700 * ei; break;
    case "slide-r": o.op = 1 - cl(p * 1.5); o.dx = 700 * ei; break;
    case "rocket": o.op = 1 - cl((p - 0.8) / 0.2); o.dy = -H * 1.1 * ei; o.vb = 24 * p; break;
    default: break;
  }
  return o;
}
/* combine in/out into a transform description; null = not visible. inFade false: the enter preset keeps its motion but
   not its fade (an opaque slide over the held frame; the default for travel presets, see inFadeOf) */
function presetState(inName, outName, k, kRemain, inF, outF, inFade) {
  let o = ID();
  if (inName !== "none" && inF > 0 && k < inF) { o = presetIn(inName, cl((k + 0.5) / inF)); if (inFade === false) o.op = 1; }
  if (outName !== "none" && outF > 0 && kRemain <= outF) {
    const q = presetOut(outName, cl((outF - kRemain + 0.5) / outF));
    o = { op: o.op * q.op, sx: o.sx * q.sx, sy: o.sy * q.sy, dx: o.dx + q.dx, dy: o.dy + q.dy, rot: o.rot + q.rot, bl: o.bl + q.bl, vb: o.vb + q.vb };
  }
  return o;
}

/* ---------------------------------------------------------------- per-frame state */
let B, T, TL, WORDS = [], FACE_RAW = [], FACE_SM = [], NF = 0;
let PIX = false, GEO = null; // measureText: pixels wanted (footage decoded) / footage->screen geometry of the last frame
let MEASURE = false, STAGE = [], CAM = [], LAYERS = [], CARDS = [], HIDE = [], Z8 = [], BANNER_Z = 10;
let FRAMES_URL = "", ASSETS = {}, VIDEOS = {}, VPEND = [], IMG = new Map(), CANVASES = [], cvUsed = 0, VBS = [];
let FOOTAGE = true, CC = null, LCAM = {}, LANC = {}; // FOOTAGE false = voice-over reel (no frames); CC = compiled canvas camera; LCAM = this frame's layer matrices
const CAMLIB = window.VEOS_CANVASCAM || null;
const LAY = window.VEOS_LAYOUTS, WLD = window.VEOS_WORLDS; // E-07 modules (layouts.js, worlds.js; loaded before core.js)
const GRD = window.VEOS_GRADES || null; // E-16 footage grades (grades.js)
let WORLDS = null, WSCHED = [], SOURCES = {}, SRC_FACE = {}, LENV = null;
let GR = { footage: null, theme: null, reel: null, reelSet: false, worlds: {}, events: [] }, GDEFS = [], GCOL = ""; // grades; this frame's SVG filters; colour-only footage grade
let FRAMING = null; // E-16b per-reel base reframe from the template's framing tokens (bundle.framing: {s, tx, ty, face, ...})

const col = r => T.colours[r] || r;
function hexA(hex, a) { hex = col(hex).replace("#", ""); return `rgba(${parseInt(hex.slice(0, 2), 16)},${parseInt(hex.slice(2, 4), 16)},${parseInt(hex.slice(4, 6), 16)},${a})`; }
const fam = slot => { const f = T.fonts[slot]; return `'${(f && f.family) || slot}','Noto Color Emoji',sans-serif`; };
const _cv = document.createElement("canvas").getContext("2d");
const measure = (s, font) => { _cv.font = font; return _cv.measureText(s).width; };
const secF = t => Math.round(t * FPS);

function prepFaces() {
  const raw = (B.face && B.face.boxes) || [];
  const N = Math.max(NF, raw.length, 1);
  let last = null; const fill = new Array(N).fill(null);
  for (let i = 0; i < N; i++) { const b = raw[i]; if (b) last = b; fill[i] = last; }
  let nxt = null; for (let i = N - 1; i >= 0; i--) { if (raw[i]) nxt = raw[i]; if (!fill[i]) fill[i] = nxt; }
  const dflt = [270, 420, 540, 600, 0];
  FACE_RAW = fill.map(b => b || dflt);
  const cuts = [0, ...(B.cuts || []), N];
  const cs = FACE_RAW.map(b => [b[0] + b[2] / 2, b[1] + b[3] / 2, b[2], b[3]]);
  FACE_SM = new Array(N);
  for (let s = 0; s < cuts.length - 1; s++) {
    const a = cuts[s], b = cuts[s + 1];
    for (let i = a; i < b; i++) {
      const lo = Math.max(a, i - 12), hi = Math.min(b - 1, i + 12); let sx = 0, sy = 0, sw = 0, sh = 0, c = 0;
      for (let j = lo; j <= hi; j++) { sx += cs[j][0]; sy += cs[j][1]; sw += cs[j][2]; sh += cs[j][3]; c++; }
      FACE_SM[i] = { cx: sx / c, cy: sy / c, w: sw / c, h: sh / c };
    }
  }
}
const faceSm = n => FACE_SM[cl(n, 0, FACE_SM.length - 1)];
const faceRaw = n => FACE_RAW[cl(n, 0, FACE_RAW.length - 1)];

/* E-16b: the reel-level face on a full stage (after the base reframe; median of the face boxes), for face-relative bands:
   {x, y, w, h, cx, cy, head_top, eye, chin} in screen px, or null (no footage / the stage is not full or low). */
let FACE_REF = null;
function faceRefInit() {
  if (!FOOTAGE) return null;
  if (FRAMING && FRAMING.face) return FRAMING.face;
  const bs = ((B.face && B.face.boxes) || []).filter(Boolean);
  if (!bs.length) return null;
  const med = k => { const v = bs.map(b => b[k]).sort((a, b) => a - b); return v[v.length >> 1]; };
  const x = med(0), y = med(1), w = med(2), h = med(3);
  return { x, y, w, h, cx: x + w / 2, cy: y + h / 2, head_top: y - 0.35 * h, eye: y + 0.38 * h, chin: y + h };
}
function faceRefAt(st) {
  if (!FACE_REF || !(st.name === "full" || st.name === "low")) return null;
  const off = st.name === "low" && st.g ? st.g.off || 0 : 0;
  if (!off) return FACE_REF;
  const o = {}; for (const k of Object.keys(FACE_REF)) o[k] = ["y", "cy", "head_top", "eye", "chin"].includes(k) ? FACE_REF[k] + off : FACE_REF[k];
  return o;
}
/* ctx.faceBand(edge, dy): the y of a face edge ("head_top" | "eye" | "chin" | "cy" | "top" | "bottom") + dy, or null */
function faceBand(edge, dy) {
  const F = FACE_REF; if (!F) return null;
  const v = { head_top: F.head_top, eye: F.eye, chin: F.chin, cy: F.cy, top: F.y, bottom: F.y + F.h }[edge || "chin"];
  return v == null ? null : v + (+dy || 0);
}
/* ctx.fitText(text, {width, slot | family, weight, italic, tracking (em), min, max}): the font size that sets one line at
   `width` px -> {size, width, font, css, html} (A11: fit-to-width blocks and lockups) */
function fitText(text, o) {
  o = o || {};
  const famS = o.family ? `'${o.family}','Noto Color Emoji',sans-serif` : fam(o.slot || "display");
  const wt = o.weight || 800, it = o.italic ? "italic " : "", trk = +o.tracking || 0, s = String(text == null ? "" : text);
  const w100 = measure(s, `${it}${wt} 100px ${famS}`) + trk * 100 * s.length;
  let size = w100 > 0 ? 100 * (+o.width || 952) / w100 : (+o.max || 120);
  size = cl(size, +o.min || 1, +o.max || 2000);
  const font = `${it}${wt} ${r2(size)}px/${o.line_height || 1} ${famS}`;
  const css = `font:${font};letter-spacing:${trk}em;white-space:nowrap;`;
  return { size: r2(size), width: r2(w100 * size / 100), font, css, html: `<div style="${css}${o.style || ""}">${esc(s)}</div>` };
}

/* ---------------------------------------------------------------- stage geometry */
function geom(name, n, ev) {
  if (ev && ev.spec && !ev.spec.legacy) { const gg = LAY.geom(ev.spec, n, LENV); for (const c of gg.cells) c.f0 = ev.f; return gg; } // E-07 layouts
  const L = T.layout, F = faceSm(n), fs = (F.w + F.h) / 2, P = L.panel || {}, R = P.radius || 64;
  const ix = (P.inset && P.inset.x) || [12, 1068], iy = (P.inset && P.inset.y) || [1008, 1881], bt = P.bleed_top || 1135;
  const bub = L.bubble || { cx: 210, cy: 1560, d: 300, ring: 8, shadow: 12 };
  const g = { x: 0, y: 0, w: W, h: H, r: [0, 0, 0, 0], s: 1, ax: F.cx, ay: F.cy, ring: 0, sh: 0, soft: 0, op: 1, Fx: F.cx, Fy: F.cy, off: 0 };
  const smin = (w, h) => Math.max(w / W, Math.min(h, H) / H);
  switch (name) {
    case "panel": {
      g.x = ix[0]; g.y = bt; g.w = ix[1] - ix[0]; g.h = H - bt + 12; g.r = [R, R, 0, 0]; g.soft = 1;
      g.s = cl(Math.max(smin(g.w, g.h - 12), 0.52 * (g.h - 12) / fs), 0, 1.6); g.ax = g.x + g.w / 2; g.ay = g.y + 0.46 * (g.h - 12); break;
    }
    case "inset": {
      g.x = ix[0]; g.y = iy[0]; g.w = ix[1] - ix[0]; g.h = iy[1] - iy[0]; g.r = [R, R, R, R]; g.soft = 1;
      g.s = cl(Math.max(smin(g.w, g.h), 0.5 * g.h / fs), 0, 1.6); g.ax = g.x + g.w / 2; g.ay = g.y + 0.46 * g.h; break;
    }
    case "slide-aside": {
      const sw = (L.slide_aside && L.slide_aside.x && L.slide_aside.x[1]) || 450;
      g.x = 0; g.y = 0; g.w = sw; g.h = H; g.r = [0, R, R, 0]; g.soft = 1;
      g.s = cl(Math.max(smin(g.w, g.h), 0.7 * g.w / fs), 0, 1.6); g.ax = g.w / 2; g.ay = F.cy; break;
    }
    case "bubble": {
      g.x = bub.cx - bub.d / 2; g.y = bub.cy - bub.d / 2; g.w = g.h = bub.d; g.r = [bub.d / 2, bub.d / 2, bub.d / 2, bub.d / 2];
      g.ring = bub.ring; g.sh = bub.shadow; g.s = cl(Math.max(smin(bub.d, bub.d), 0.8 * bub.d / fs), 0, 1.6); g.ax = bub.cx; g.ay = bub.cy; break;
    }
    case "full": { // the per-reel base reframe (framing tokens): punch in so the face sits where the template wants it
      if (FRAMING) { g.s = FRAMING.s; g.ax = FRAMING.s * F.cx + FRAMING.tx; g.ay = FRAMING.s * F.cy + FRAMING.ty; }
      break;
    }
    case "low": { // full-frame footage lowered by `offset` px; the revealed top shows a blurred backdrop
      g.off = ev && ev.offset != null ? ev.offset : 380;
      if (FRAMING) { g.s = FRAMING.s; g.ax = FRAMING.s * F.cx + FRAMING.tx; g.ay = FRAMING.s * F.cy + FRAMING.ty + g.off; }
      else g.ay = F.cy + g.off;
      break;
    }
    case "hidden": {
      g.x = bub.cx; g.y = bub.cy; g.w = 0; g.h = 0; g.s = 0.3; g.ax = bub.cx; g.ay = bub.cy; g.op = 0; break;
    }
    default: break;
  }
  if (name !== "full" && name !== "hidden" && name !== "low") { // keep the footage covering its window
    const yb = Math.min(g.y + g.h, H);
    const cov = (a, lo, hi) => (lo <= hi ? cl(a, lo, hi) : (lo + hi) / 2);
    g.ax = cov(g.ax, g.x + g.w - g.s * (W - F.cx), g.x + g.s * F.cx);
    g.ay = cov(g.ay, yb - g.s * (H - F.cy), g.y + g.s * F.cy);
  }
  return ev && ev.spec && ev.spec.p.dim ? LAY.applyDim(g, ev.spec) : g;
}
function lerpGeom(a, b, p, via) {
  const o = {};
  for (const k of ["x", "y", "w", "h", "s", "ax", "ay", "ring", "sh", "soft", "op", "Fx", "Fy", "off"]) o[k] = lerp(a[k], b[k], p);
  o.r = a.r.map((v, i) => Math.max(0, lerp(v, b.r[i], p)));
  o.w = Math.max(0, o.w); o.h = Math.max(0, o.h); o.op = cl(o.op); o.ring = Math.max(0, o.ring); o.sh = Math.max(0, o.sh);
  if (a.ext || b.ext) LAY.lerpExt(a, b, o, p, via);
  return o;
}
const DEFAULT_VIA = { low: "cut", full: "pop-back", panel: "panel-drop", inset: "panel-drop", "slide-aside": "slide-aside", bubble: "bubble-shrink", hidden: "cut" };
function stageAt(n) {
  let i = 0; for (let k = 0; k < STAGE.length; k++) if (STAGE[k].f <= n) i = k;
  const cur = STAGE[i], prev = STAGE[i - 1];
  const res = { name: cur.layout, morph: null, p: 1, from: prev ? prev.layout : cur.layout, spec: cur.spec };
  if (prev && cur.d > 0 && n < cur.f + cur.d) {
    const q = (n - cur.f + 1) / (cur.d + 1);
    const e = cur.ov != null ? overshootEase(q, cur.ov) : LAY.easeOf(cur.via, q, { EL, EIO, EO, EI, BO }, cur.ease); // fx-helpers: stage[].overshoot
    const ga = geom(prev.layout, n, prev), gb = geom(cur.layout, n, cur);
    res.morph = cur.via; res.q = q; res.g = cur.via === "fade-through" ? LAY.fadeThrough(ga, gb, e) : lerpGeom(ga, gb, e, cur.via);
    if (res.g.ext) res.g.mvb = LAY.morphBlur(cur.via, ga, gb, q);
    return res;
  }
  res.g = geom(cur.layout, n, cur);
  return res;
}
function lastStageF(n) { let f = 0; for (const s of STAGE) if (s.f <= n) f = s.f; return f; }

/* ---------------------------------------------------------------- camera
   timeline.camera[] = {t, preset, p?, crop?}. Fields resolve event `p` > tokens.camera_presets[preset]. The state is
   {s, r, dx, dy, w}: scale and roll about the pivot, the pivot's screen offset from the face anchor (dx/dy stay 0 when
   the camera zooms about the face, the v1 behaviour) and how much graphics z1-6 ride the camera (`target: "all"`).
   Camera v2 fields: ease, rotate [from, to] / from_rotate, origin (toward), from ("inherit" | scale), from_wide, land,
   crop (wide | mid | tight), target. Everything stays a pure function of the frame. */
const EXPO_IO = x => (x <= 0 ? 0 : x >= 1 ? 1 : x < 0.5 ? Math.pow(2, 20 * x - 10) / 2 : (2 - Math.pow(2, 10 - 20 * x)) / 2);
const EXPO_O = x => (x <= 0 ? 0 : x >= 1 ? 1 : 1 - Math.pow(2, -10 * x));
const CAM_EASE = { out: x => EO(x), in: x => EI(x), inOut: x => EIO(x), linear: x => cl(x), expoInOut: EXPO_IO, expoOut: EXPO_O };
const CAM_CROPS = { wide: 1, mid: 1.18, tight: 1.35 }; // tokens.camera_crops / a preset's `levels` override
const CAM_ORIGINS = ["face", "center", "device", "free_side"];
let CAMNODES = {}; // camera origin nodes (scene `nodes` + timeline.canvas_nodes): {id: {x, y}} centres, screen px
const camOpt = (ev, k) => { const p = ev.p || {}; if (p[k] !== undefined) return p[k]; const P = (T.camera_presets || {})[ev.preset]; return P ? P[k] : undefined; };
function cropScale(c, P) {
  if (isNum(c)) return c;
  const lv = P && P.levels && P.levels[c];
  if (lv != null) return Array.isArray(lv) ? (lv[0] + lv[1]) / 2 : lv;
  const tc = T.camera_crops || {};
  return isNum(tc[c]) ? tc[c] : CAM_CROPS[c];
}
/* a camera event's v2 fields: an error message, or null (core fails the boot on it; V-CAMERA reports the same) */
function camCheck(ev) {
  const P = (T.camera_presets || {})[ev.preset] || {}, src = [["p", ev.p || {}], [`camera_presets.${ev.preset}`, P]];
  for (const [w, o] of src) {
    if (o.ease != null && !CAM_EASE[o.ease]) return `${w}.ease '${o.ease}' is not one of ${Object.keys(CAM_EASE).join(" | ")}`;
    for (const k of ["origin", "toward"]) {
      const v = o[k]; if (v == null) continue;
      if (typeof v === "string") {
        if (!CAM_ORIGINS.includes(v)) return `${w}.${k} '${v}' is not one of ${CAM_ORIGINS.join(" | ")} or {x, y} / {node}`;
        if (v === "device" && !CAMNODES.device && !(T.layout && T.layout.device)) return `${w}.${k} 'device' needs a node 'device' (a scene's nodes or timeline.canvas_nodes) or tokens.layout.device {x, y}`;
      } else if (!(v && typeof v === "object" && ((isNum(v.x) && isNum(v.y)) || (v.node != null && CAMNODES[String(v.node)])))) return `${w}.${k} must be face | center | device | free_side, {x, y} screen px, or {node: id} of a known node`;
    }
    if (o.target != null && !["footage", "all"].includes(o.target)) return `${w}.target '${o.target}' is not footage | all`;
    if (o.crop != null && !(isNum(o.crop) ? o.crop > 0 : cropScale(o.crop, P) != null)) return `${w}.crop '${o.crop}' is not wide | mid | tight (or a scale)`;
    if (o.from != null && o.from !== "inherit" && !(isNum(o.from) && o.from > 0)) return `${w}.from must be "inherit" or a scale > 0`;
    if (o.from_rotate != null && !isNum(o.from_rotate)) return `${w}.from_rotate must be degrees`;
    if (Array.isArray(o.rotate) ? !(o.rotate.length === 2 && o.rotate.every(isNum)) : (o.rotate != null && !isNum(o.rotate))) return `${w}.rotate must be degrees or [from, to]`;
    if (o.from_wide != null && !(typeof o.from_wide === "boolean" || (isNum(o.from_wide) && o.from_wide > 0 && o.from_wide <= 1))) return `${w}.from_wide must be true or a scale 0..1`;
    if (o.land != null && !(typeof o.land === "boolean" || (isNum(o.land) && o.land > 0))) return `${w}.land must be true or the start scale`;
  }
  if (ev.preset == null && camOpt(ev, "crop") == null) return "needs a preset (or a crop on a cut)";
  return null;
}
/* screen offset of the event's pivot from the face anchor (g.ax, g.ay); {x: 0, y: 0} = about the face */
function camOrigin(ev, g) {
  let v = camOpt(ev, "origin"); if (v == null) v = camOpt(ev, "toward");
  if (v == null || v === "face" || !g) return { x: 0, y: 0 };
  let O;
  if (v === "center") O = { x: g.x + g.w / 2, y: g.y + g.h / 2 };
  else if (v === "free_side") O = { x: g.ax < g.x + g.w / 2 ? g.x + 0.75 * g.w : g.x + 0.25 * g.w, y: g.ay };
  else if (v === "device") O = CAMNODES.device || T.layout.device;
  else if (typeof v === "object") O = v.node != null ? CAMNODES[String(v.node)] : v;
  return O ? { x: O.x - g.ax, y: O.y - g.ay } : { x: 0, y: 0 };
}
function pivotD(s, r, o) { // translation that keeps the pivot o fixed under scale s / roll r (about the face anchor)
  if (!o.x && !o.y) return [0, 0];
  const rad = r * Math.PI / 180, cs = Math.cos(rad), sn = Math.sin(rad);
  return [o.x - s * (cs * o.x - sn * o.y), o.y - s * (sn * o.x + cs * o.y)];
}
function camTarget(ev, prev, kEnd, boundaryF, g) {
  const P = (T.camera_presets || {})[ev.preset] || {}, p = ev.p || {};
  let frames = p.frames != null ? p.frames : P.frames, toS, fromS, toR = 0, fromR = prev.r;
  if (frames === "beat") frames = cl(boundaryF - ev.f, 15, 120);
  else if (Array.isArray(frames)) frames = Math.round((frames[0] + frames[1]) / 2);
  frames = ev.preset == null && frames == null ? 0 : (frames || 4); // a preset-less crop is a cut: instant
  const sc = P.scale || [1, 1];
  fromS = sc[0] === 1 ? prev.s : sc[0]; toS = p.scale != null ? p.scale : sc[1];
  const crop = camOpt(ev, "crop"); if (crop != null && p.scale == null) toS = cropScale(crop, P);
  const fr = camOpt(ev, "from");
  if (fr === "inherit") fromS = prev.s; else if (isNum(fr)) fromS = fr;
  const land = camOpt(ev, "land"); if (isNum(land)) { fromS = land; if (p.scale == null) toS = 1; }
  const fw = camOpt(ev, "from_wide");
  if (fw) { const lo = g && g.s > 0 ? Math.min(1, 1 / g.s) : 1; fromS = Math.max(lo, fw === true ? lo : fw); } // never wider than the raw footage
  const sg = ev.preset === "crash-zoom" ? (HASH(ev.idx, 3) > 0.5 ? 1 : -1) : 1;
  if (P.rotate != null) { if (Array.isArray(P.rotate)) { fromR = P.rotate[0] * sg; toR = P.rotate[1] * sg; } else toR = P.rotate * sg; }
  if (P.from_rotate != null) fromR = P.from_rotate;
  if (p.rotate != null) { if (Array.isArray(p.rotate)) { fromR = p.rotate[0]; toR = p.rotate[1]; } else toR = p.rotate; }
  if (p.from_rotate != null) fromR = p.from_rotate;
  return { frames, fromS, toS, fromR, toR, hold: p.hold != null ? p.hold : (P.hold_frames ? Math.round((P.hold_frames[0] + P.hold_frames[1]) / 2) : null) };
}
function camEval(ev, prev, k, boundaryF, g) {
  if (ev.preset === "reset") { const e = EO(cl(k / 4)); return { s: lerp(prev.s, 1, e), r: lerp(prev.r, 0, e), dx: lerp(prev.dx, 0, e), dy: lerp(prev.dy, 0, e), w: prev.w }; }
  if (ev.preset === "shake") return prev;
  const t = camTarget(ev, prev, 0, boundaryF, g), q = t.frames > 0 ? cl(k / t.frames) : 1;
  const o = camOrigin(ev, g), p0 = pivotD(prev.s, prev.r, o), e0x = prev.dx - p0[0], e0y = prev.dy - p0[1]; // the previous pivot's residual fades out
  const en = camOpt(ev, "ease"), wT = camOpt(ev, "target") === "all" ? 1 : 0;
  const st = (s, r, e) => { const d = pivotD(s, r, o); return { s, r, dx: d[0] + e0x * (1 - e), dy: d[1] + e0y * (1 - e), w: lerp(prev.w, wT, e) }; };
  if (ev.preset === "zoom-through") { if (k >= t.frames) return { s: 1, r: 0, dx: 0, dy: 0, w: 0 }; const e = (CAM_EASE[en] || EI)(q); return st(lerp(prev.s, t.toS, e), prev.r, e); }
  const e = en ? (CAM_EASE[en] || EO)(q) : ev.preset === "push-drift" ? q : EO(q);
  let s = lerp(t.fromS, t.toS, e), r = lerp(t.fromR, t.toR, e);
  if (t.hold != null && k > t.frames + t.hold) { const b = EO(cl((k - t.frames - t.hold) / 4)); s = lerp(t.toS, 1, b); r = lerp(t.toR, 0, b); }
  return st(s, r, e);
}
function cameraAt(n, g) {
  const f0 = lastStageF(n);
  const evs = CAM.filter(e => e.f >= f0 && e.f <= n);
  const main = evs.filter(e => e.preset !== "shake");
  let st = { s: 1, r: 0, dx: 0, dy: 0, w: 0 }, vb = 0;
  for (let i = 0; i < main.length; i++) {
    const ev = main[i], nextF = i + 1 < main.length ? main[i + 1].f : Infinity;
    let bF = nextF; for (const s of STAGE) if (s.f > ev.f && s.f < bF) bF = s.f;
    const last = i === main.length - 1, k = last ? n - ev.f : Infinity;
    const next = camEval(ev, st, last ? k : 1e5, bF, g);
    if (last) { const before = camEval(ev, st, k - 1, bF, g); vb = cl(Math.abs(next.s - before.s) * 70, 0, 22); }
    st = next;
  }
  let shx = 0, shy = 0, bump = 1;
  for (const ev of evs) {
    if (ev.preset !== "shake") continue;
    const P = (T.camera_presets || {}).shake || {}, p = ev.p || {}, fr = p.frames || P.frames || 6, amp = p.amp != null ? p.amp : (P.amp || 10), k = n - ev.f;
    if (k >= 0 && k < fr) { const d = 1 - k / fr; shx += amp * d * (HASH(n + ev.idx * 7, 1) * 2 - 1); shy += amp * d * (HASH(n + ev.idx * 7, 2) * 2 - 1); bump *= 1 + ((p.bump || P.bump || 1.03) - 1) * d; vb = Math.max(vb, amp * d * 0.8); }
  }
  return { s: st.s * bump, r: st.r, dx: st.dx, dy: st.dy, w: st.w, shx, shy, vb };
}

/* ---------------------------------------------------------------- subtitles */
function buildCards() {
  const ST = T.type.subtitle || {}, lead = (T.motion && T.motion.lead_frames) || 2;
  const ws = [];
  for (const w of WORDS) {
    let txt;
    if (Object.prototype.hasOwnProperty.call(w, "caption")) { txt = w.caption; if (txt === "" || txt == null) continue; }
    else txt = String(w.w || "").toLowerCase().replace(/[.,;:!…]+$/g, "");
    if (!txt) continue;
    ws.push({ txt, s: w.s, e: w.e, spk: w.speaker || null, role: w.role || null });
  }
  const per = (ST.words_per_card && ST.words_per_card[1]) || 3, cards = [];
  let i = 0;
  while (i < ws.length) {
    let j = i + 1;
    while (j < ws.length && j - i < per && ws[j].s - ws[j - 1].e <= 0.25 && ws[j].spk === ws[i].spk) j++; // a card never mixes speakers
    if (j - i === per && j < ws.length && ws.length - j === 1 && ws[j].s - ws[j - 1].e <= 0.25 && ws[j].spk === ws[i].spk) j--;
    cards.push({ f0: Math.max(0, secF(ws[i].s) - lead), last: ws[j - 1].e, text: ws.slice(i, j).map(x => x.txt).join(" "), s: ws[i].s, spk: ws[i].spk, role: ws[i].role });
    i = j;
  }
  for (let c = 0; c < cards.length; c++) {
    const nx = cards[c + 1], hold = secF(cards[c].last) + 7;
    cards[c].f1 = nx ? Math.min(nx.f0, Math.max(hold, cards[c].f0 + 4)) : Math.max(hold, cards[c].f0 + 4);
    if (cards[c].f1 <= cards[c].f0) cards[c].f1 = cards[c].f0 + 1;
  }
  for (const o of ((TL.captions && TL.captions.overrides) || [])) {
    if (o.from != null && o.to != null) { for (const c of cards) c.text = c.text.split(" ").map(w => (w.toLowerCase() === String(o.from).toLowerCase() ? o.to : w)).join(" "); }
    else { const t = o.t != null ? o.t : o.at; if (t == null) continue; const f = secF(t); for (const c of cards) if (c.f0 <= f && f < c.f1) c.text = o.text; }
  }
  CARDS = cards;
}
function subtitleHTML(n, st, world) {
  if (!TL.captions || TL.captions.subtitles === "off" || TL.captions.subtitles === false) return "";
  for (const h of HIDE) if (n >= h[0] && n < h[1]) return "";
  for (const z of Z8) if (n >= z[0] && n < z[1]) return "";
  if (st.morph) return "";
  let card = null; for (const c of CARDS) { if (n >= c.f0 && n < c.f1) { card = c; break; } if (c.f0 > n) break; }
  if (!card) return "";
  const L = T.layout, P = L.panel || {}, bub = L.bubble || { cy: 1560, d: 300 };
  let cy = (L.caption_cy && L.caption_cy.full) || 1300, cx = W / 2, maxW = 960;
  if (st.name === "panel") cy = (P.bleed_top || 1135) - 60;
  else if (st.name === "inset") cy = ((P.inset && P.inset.y[0]) || 1008) - 60;
  else if (st.name === "slide-aside") { const sw = (L.slide_aside && L.slide_aside.x[1]) || 450; cx = (sw + W) / 2; maxW = W - sw - 60; }
  else if (st.g && st.g.ext) cy = LAY.captionY(layoutInfo(st), cy);
  const ST = T.type.subtitle || {}, size0 = (Array.isArray(ST.size) ? (ST.size[0] + ST.size[1]) / 2 : ST.size) || 58;
  const font = `${ST.weight || 800} ${size0}px ${fam(ST.slot || "body")}`;
  const w0 = measure(card.text, font), size = w0 > maxW ? Math.floor(size0 * maxW / w0) : size0;
  const shot = shotAt(n); // multi-camera reels (E-13): a stack shot puts the caption on its seam
  if (shot && shot.layout === "stack" && st.name === "full") cy = shot.seam_y || H / 2;
  const onLight = st.name !== "full" && st.name !== "low" && WORLDS.isLight(world);
  const sp = speakerStyle(card);
  const c = onLight ? col("ink") : (sp ? col(sp.colour || "paper") : col("paper"));
  const ital = sp && sp.style === "italic" ? "font-style:italic;" : "";
  const sh = onLight ? "none" : "0 3px 14px rgba(0,0,0,.55),0 1px 3px rgba(0,0,0,.45)";
  return `<div style="position:absolute;left:${r2(cx - maxW / 2)}px;width:${maxW}px;top:${r2(cy)}px;transform:translateY(-50%);text-align:center;white-space:nowrap;font:${ST.weight || 800} ${size}px/1.1 ${fam(ST.slot || "body")};color:${c};${ital}text-shadow:${sh}" data-speaker="${esc(card.spk || "")}">${esc(card.text)}</div>`;
}
/* speaker-coded captions (E-13 hook; the full caption engine E-05 reads work/words.json): style by speaker id, else by
   role, from timeline.captions.speakers > tokens captions.speakers > type.subtitle.speakers; default: the first speaker
   (or role host) paper upright, everyone else accent italic (Hormozi). null when the reel has no speaker labels. */
let SPK_MAP = null, SPK_ORDER = [];
function speakerStyle(card) {
  if (!card.spk) return null;
  if (!SPK_MAP) {
    SPK_MAP = Object.assign({}, (T.type && T.type.subtitle && T.type.subtitle.speakers) || {}, (T.captions && T.captions.speakers) || {}, (TL.captions && TL.captions.speakers) || {});
    for (const w of WORDS) if (w.speaker && !SPK_ORDER.includes(w.speaker)) SPK_ORDER.push(w.speaker);
  }
  const m = SPK_MAP[card.spk] || (card.role && SPK_MAP[card.role]);
  if (m) return m;
  if (SPK_ORDER.length < 2) return null;
  const first = card.role ? card.role === "host" : SPK_ORDER.indexOf(card.spk) === 0;
  return first ? { colour: "paper", style: "upright" } : { colour: T.colours.accent ? "accent" : "#FFE600", style: "italic" };
}
function shotAt(n) {
  const S = TL.shots; if (!S || !S.length) return null;
  const t = n / FPS; for (const s of S) if (t >= s.t0 - 1e-6 && t < s.t1 - 1e-6) return s;
  return null;
}
const esc = s => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;");

/* ---------------------------------------------------------------- worlds (worlds.js: tokens.worlds, v1 mapping) */
function worldHTML(name, n, st) { return WORLDS.html(name, n, st); }
const layoutInfo = st => LAY.info(st, st.g, st.spec);

/* ---------------------------------------------------------------- images */
function preload(url) {
  let e = IMG.get(url);
  if (!e) {
    const im = new Image(); im.src = url; e = { im, p: im.decode().catch(() => {}) }; IMG.set(url, e);
    if (IMG.size > 24) { const k = IMG.keys().next().value; IMG.delete(k); }
  }
  return e.p;
}
const fUrl = n => `${FRAMES_URL}f${String(cl(n, 0, NF - 1)).padStart(5, "0")}.jpg`;
const cUrl = n => `${FRAMES_URL}c${String(cl(n, 0, NF - 1)).padStart(5, "0")}.webp`;

/* ---------------------------------------------------------------- frame */
function vbFilter(px) { if (px < 0.4) return ""; VBS.push(px); return `filter:url(#vb${VBS.length - 1});`; }
/* fx-helpers: directional motion blur. VBS holds a number (the v1 vertical blur) or {px, a} (a = motion angle in degrees,
   0 = horizontal, 90 = vertical). Axis-aligned angles are one feGaussianBlur; any other angle is a 16-tap box blur along
   the vector (four feOffset + average doublings, centred) smoothed by a small gaussian. User-space region: never clipped. */
function dirBlur(px, ang) { if (!(px >= 0.4)) return ""; VBS.push(ang == null ? px : { px, a: +ang || 0 }); return `url(#vb${VBS.length - 1})`; }
function vbDef(v, i) {
  if (typeof v === "number") return `<filter id="vb${i}" x="-5%" y="-30%" width="110%" height="160%" color-interpolation-filters="sRGB"><feGaussianBlur stdDeviation="0 ${r2(v)}"/></filter>`;
  const px = v.px, a = ((v.a % 180) + 180) % 180 * Math.PI / 180, cs = Math.cos(a), sn = Math.sin(a), m = Math.ceil(px * 4 + 8);
  const head = `<filter id="vb${i}" filterUnits="userSpaceOnUse" x="${-m}" y="${-m}" width="${2 * W + 2 * m}" height="${2 * H + 2 * m}" color-interpolation-filters="sRGB">`;
  if (Math.abs(sn) < 0.02 || Math.abs(cs) < 0.02) return `${head}<feGaussianBlur stdDeviation="${r2(Math.abs(cs) >= 0.02 ? px : 0)} ${r2(Math.abs(sn) >= 0.02 ? px : 0)}"/></filter>`;
  const L = px * Math.sqrt(12), d = L / 15, ux = cs * d, uy = sn * d; // box of length L has the gaussian's spread px
  let f = `${head}<feOffset in="SourceGraphic" dx="${r2(-ux * 7.5)}" dy="${r2(-uy * 7.5)}" result="s0"/>`;
  for (let k = 0; k < 4; k++) f += `<feOffset in="s${k}" dx="${r2(ux * (1 << k))}" dy="${r2(uy * (1 << k))}" result="o${k}"/><feComposite in="s${k}" in2="o${k}" operator="arithmetic" k2="0.5" k3="0.5" result="s${k + 1}"/>`;
  return f + `<feGaussianBlur in="s4" stdDeviation="${r2(Math.max(0.3, d * 0.6))}"/></filter>`;
}
/* fx-helpers: the frame a stepped scene shows at frame n (step_frames: hold every k frames; step_fps: local time floored to 1/fps) */
function stepN(L, n) {
  if (L.stepF > 1) return L.fin + Math.floor((n - L.fin) / L.stepF) * L.stepF;
  if (L.stepFps) return L.fin + Math.round(Math.floor((n - L.fin) / FPS * L.stepFps + 1e-6) / L.stepFps * FPS);
  return n;
}
/* fx-helpers: a back-out ease whose peak is exactly 1 + ov (stage[].overshoot); the back constant is found once per amount */
const OVS = new Map();
function overshootEase(q, ov) {
  let s = OVS.get(ov);
  if (s == null) {
    const peak = k => { let m = 0; for (let i = 1; i <= 200; i++) m = Math.max(m, BO(i / 200, k)); return m; };
    let lo = 0, hi = 12; for (let it = 0; it < 40; it++) { const mid = (lo + hi) / 2; if (peak(mid) < 1 + ov) lo = mid; else hi = mid; }
    s = (lo + hi) / 2; OVS.set(ov, s);
  }
  return ov > 0 ? BO(cl(q), s) : EO(q);
}
/* fix-visual: the velocity smear's cap (scene smear_px > tokens motion.smear_push.motion_blur_px > 24, at most 48 px) and
   whether the enter preset fades (a travel preset, slide-l / slide-r / rocket, arrives opaque; scene in_fade overrides) */
function smearCap(d, T) {
  const sp = T && T.motion && T.motion.smear_push, tok = sp && isNum(sp.motion_blur_px) ? sp.motion_blur_px : null;
  return cl(isNum(d.smear_px) ? d.smear_px : tok != null ? tok : 24, 0, SMEAR_MAX);
}
const TRAVEL_IN = ["slide-l", "slide-r", "rocket"]; // presets that carry the scene in from far away: they arrive opaque
const inFadeOf = d => (typeof d.in_fade === "boolean" ? d.in_fade : !TRAVEL_IN.includes(d.in));
VEOS._fxh = { vbDef, stepN, overshootEase, presetState, smearCap, inFadeOf }; // pure helpers, exposed for the engine tests (node)
function layerCtx(base, L, n) {
  const c = Object.create(base);
  c.rng = seed => mulberry32(hash32(`${L.id}|${seed}|${n}`) ^ 0x9E3779B9);
  c.scene = L;
  c.rngStable = seed => mulberry32(hash32(`${L.id}|${seed}`));
  c.canvas = () => {
    if (!c._cv) { const cv = CANVASES[cvUsed] || (CANVASES[cvUsed] = (() => { const x = document.createElement("canvas"); x.width = W; x.height = H; return x; })()); cvUsed++; cv.style.cssText = ""; const g = cv.getContext("2d"); g.setTransform(1, 0, 0, 1, 0, 0); g.clearRect(0, 0, W, H); c._cv = cv; c._g = g; }
    return c._g;
  };
  c.canvasEl = () => (c._cv || (c.canvas(), c._cv)); // the layer canvas element (scenes may set its CSS transform/filter; reset every frame)
  return c;
}
function mk(style, html) { const d = document.createElement("div"); d.style.cssText = style; if (html) d.innerHTML = html; return d; }

/* ctx.videoFrame(name, seconds): URL of the frame of a video asset (veos asset add <video>) at that local time; 30 fps, frame-exact, clamped. */
function videoFrame(name, sec) {
  const v = VIDEOS[name];
  if (!v) return "";
  const k = cl(Math.floor((+sec || 0) * (v.fps || FPS) + 1e-6), 0, Math.max(0, v.frames - 1));
  const url = `${v.base_url}f${String(k).padStart(5, "0")}.jpg`;
  if (!MEASURE || PIX) VPEND.push(preload(url)); // decoded before the frame is "ready", like footage
  return url;
}

/* canvas camera (E-14): the view of one layer (parallax k) at frame n, as a ctx.camera object */
const CAM_ID = { x: W / 2, y: H / 2, s: 1, r: 0 };
function camCtx(st, stPrev, k) {
  const home = CC ? CC.home : CAM_ID, full = st || { ...home, moving: false, move: null, kind: null };
  const view = kk => (CAMLIB && st ? CAMLIB.layer(st, kk, home) : { x: home.x, y: home.y, s: home.s, r: 0 });
  const v = view(k), M = CAMLIB ? CAMLIB.matrix(v) : [1, 0, 0, 1, 0, 0];
  let speed = 0;
  if (st && stPrev && CAMLIB) { const p = CAMLIB.layer(stPrev, k, home); speed = Math.hypot(v.x - p.x, v.y - p.y) * v.s + 540 * Math.abs(Math.log(v.s / p.s)); }
  return {
    active: !!(CC && CC.active), x: v.x, y: v.y, s: v.s, r: v.r, k, moving: !!full.moving, move: full.move || null, kind: full.kind || null,
    speed, home, full: { x: full.x, y: full.y, s: full.s, r: full.r || 0 }, matrix: M, view,
    toScreen(wx, wy, kk) { const m = kk == null ? M : CAMLIB.matrix(view(kk)); return CAMLIB ? CAMLIB.apply(m, wx, wy) : [wx, wy]; },
    toWorld(sx, sy, kk) { const m = kk == null ? M : CAMLIB.matrix(view(kk)); return CAMLIB ? CAMLIB.apply(CAMLIB.invert(m), sx, sy) : [sx, sy]; },
    node(id) { const q = CC && CC.nodes[String(id)]; return q ? { x: +q.x, y: +q.y, w: +q.w, h: +q.h, cx: +q.x + q.w / 2, cy: +q.y + q.h / 2 } : null; },
  };
}

/* ---------------------------------------------------------------- E-07 drawing helpers (geometry comes from layouts.js) */
function srcInfo(src) { // "footage" | "source:<id>" | "<video asset name>"
  if (!src || src === "footage") return null;
  const id = String(src).replace(/^source:/, "");
  return SOURCES[id] ? { id, kind: "source", v: SOURCES[id] } : VIDEOS[id] ? { id, kind: "video", v: VIDEOS[id] } : { id, kind: "missing", v: null };
}
function srcSize(src) { const s = srcInfo(src); return !s ? [W, H] : s.v ? [+s.v.w || W, +s.v.h || H] : [W, H]; }
function srcFace(src, n) {
  const s = srcInfo(src); if (!s) return faceSm(n);
  const [sw, sh] = srcSize(src), boxes = s.v && s.v.face && (s.v.face.boxes || s.v.face);
  if (Array.isArray(boxes) && boxes.length) { const b = boxes[cl(n + (+s.v.offset_f || 0), 0, boxes.length - 1)] || boxes[0]; if (b) return { cx: b[0] + b[2] / 2, cy: b[1] + b[3] / 2, w: b[2], h: b[3] }; }
  return { cx: sw / 2, cy: sh * 0.4, w: sh * 0.2, h: sh * 0.2 };
}
function srcUrl(src, n, f0) {
  const s = srcInfo(src); if (!s) return fUrl(n);
  if (!s.v) { VEOS.errors.push(`stage source '${src}' not found (bundle sources / plan/assets video)`); return ""; }
  const k = s.kind === "source" ? n + (+s.v.offset_f || 0) : n - (f0 || 0);
  return `${s.v.base_url}f${String(cl(k, 0, Math.max(0, (s.v.frames || 1) - 1))).padStart(5, "0")}.jpg`;
}
function dimF(c, sharp) { // the dim treatment as a filter function list ("" = none)
  const b = c.blur || 0, l = c.luma || 0;
  if (b <= 0.05 && Math.abs(l) < 0.005) return "";
  return `${!sharp && b > 0.05 ? `blur(${r2(b)}px) ` : ""}brightness(${r2(1 + l)})`;
}
function dimCss(c, sharp) { const f = dimF(c, sharp); return f ? `filter:${f};` : ""; }
const fjoin = (...a) => { const s = a.filter(Boolean).join(" "); return s ? `filter:${s};` : ""; }; // grade + dim in one filter
/* E-16: a grade spec -> CSS filter function list for this frame (its SVG filter goes into the frame's <defs>) */
function gradeF(spec, o) {
  if (!spec || !GRD) return "";
  const r = GRD.filterOf(spec, `gr${GDEFS.length}`, o);
  if (r.def) GDEFS.push(r.def);
  return r.css;
}
/* stack seam blend (layouts.js `fade.mode: "blend"`): the window melts into what lies behind it */
function maskCss(m) {
  if (!m || !(m.px > 0)) return "";
  const g = `linear-gradient(${m.side === "bottom" ? "0deg" : "180deg"},transparent 0,#000 ${r2(m.px)}px)`;
  return `-webkit-mask-image:${g};mask-image:${g};`;
}
function decorCss(g) {
  const sh = [], bw = g.bw > 0.2 ? g.bw : 0;
  if (bw) sh.push(`0 0 0 ${r2(bw)}px ${col(g.bc || "paper")}`);
  if (g.ring > 0.3 && !g.ringG) sh.push(`0 0 0 ${r2(g.ring + bw)}px ${col(g.ringC || "paper")}`);
  if (g.sh > 0.3) sh.push(`${r2(g.sh * 0.5)}px ${r2(g.sh)}px 0 ${r2(g.ring)}px ${col("ink")}`);
  if (g.glow > 0.5) sh.push(`0 0 ${r2(g.glow)}px ${r2(g.glow * 0.2)}px ${hexA(g.glowC || "data", 0.55)}`);
  if (g.shA > 0.01) sh.push(`0 ${r2(10 + 0.02 * g.h)}px ${r2(30 + 0.05 * g.h)}px rgba(0,0,0,${r2(g.shA)})`);
  if (g.soft > 0.01) sh.push(`0 -6px 30px rgba(0,0,0,${r2(0.18 * g.soft)})`);
  return sh.length ? `box-shadow:${sh.join(",")};` : "";
}
function ringEl(g) { // gradient ring (e.g. a sky / rainbow ring around a pip): a rounded plate behind the window
  const k = g.ring + (g.bw || 0), stops = g.ringG.map(c => col(c)).join(",");
  return mk(`position:absolute;left:${r2(g.x - k)}px;top:${r2(g.y - k)}px;width:${r2(g.w + 2 * k)}px;height:${r2(g.h + 2 * k)}px;border-radius:${g.r.map(v => r2(v + k) + "px").join(" ")};opacity:${r2(g.op)};background:conic-gradient(from 200deg,${stops},${col(g.ringG[0])});box-shadow:0 ${r2(10 + 0.02 * g.h)}px ${r2(30 + 0.05 * g.h)}px rgba(0,0,0,${r2(g.shA || 0)})`);
}
function backdropEl(bd, n) { // letterbox fill / blurfill copy behind the band (above the world, below every scene)
  if (bd.kind === "fill") return mk(`position:absolute;inset:0;background:${col(bd.colour || "#000000")};opacity:${r2(bd.op)}`);
  const [sw, sh] = srcSize(bd.src), k = Math.max(W / sw, H / sh) * (bd.scale || 1.15), w = sw * k, h = sh * k, url = srcUrl(bd.src, n, 0);
  const gc = srcInfo(bd.src) && srcInfo(bd.src).kind === "video" ? "" : GCOL;
  return mk(`position:absolute;inset:0;overflow:hidden;opacity:${r2(bd.op)}`, url ? `<img data-foot="1" src="${url}" style="position:absolute;left:${r2((W - w) / 2)}px;top:${r2((H - h) / 2)}px;width:${r2(w)}px;height:${r2(h)}px;filter:${gc ? gc + " " : ""}blur(${r2(bd.px || 40)}px) brightness(${r2(1 + (bd.luma == null ? -0.55 : bd.luma))})">` : "");
}
function extraEls(frag, g, n) {
  for (const c of g.cells) {
    if (c.w < 1 || c.h < 1 || c.op < 0.01) continue;
    const url = srcUrl(c.src, n, c.f0); if (!url) continue;
    // E-16: camera sources take the footage grade (colour only); a cell's own `grade` wins (a split from one shot in two grades); B-roll video assets stay natural
    const si = srcInfo(c.src);
    let gc = si && si.kind === "video" ? "" : GCOL;
    if (c.grade != null) { try { gc = gradeF(GRD ? GRD.norm(c.grade, T) : null, { spatial: false }); } catch (e) { VEOS.errors.push(`stage cell ${c.key} grade: ${e.message}`); } }
    const win = mk(`position:absolute;left:${r2(c.x)}px;top:${r2(c.y)}px;width:${r2(c.w)}px;height:${r2(c.h)}px;border-radius:${c.r.map(v => r2(v) + "px").join(" ")};overflow:hidden;opacity:${r2(c.op)};background:#000;${maskCss(c.mask)}`.replace(/;$/, ""));
    if (c.fit === "blurfill") { const k = Math.max(c.w / c.sw, c.h / c.sh) * 1.12; win.insertAdjacentHTML("beforeend", `<img data-foot="1" src="${url}" style="position:absolute;left:${r2((c.w - c.sw * k) / 2)}px;top:${r2((c.h - c.sh * k) / 2)}px;width:${r2(c.sw * k)}px;height:${r2(c.sh * k)}px;filter:${gc ? gc + " " : ""}blur(30px) brightness(.5)">`); }
    const tx = c.ax - c.s * c.Fx - c.x, ty = c.ay - c.s * c.Fy - c.y;
    win.insertAdjacentHTML("beforeend", `<img data-foot="1" src="${url}" style="position:absolute;left:0;top:0;width:${c.sw}px;height:${c.sh}px;transform-origin:0 0;transform:matrix(${c.s.toFixed(5)},0,0,${c.s.toFixed(5)},${r2(tx)},${r2(ty)});${fjoin(gc, dimF(c))}${g.mvb > 0.4 ? vbFilter(g.mvb) : ""}">`);
    frag.appendChild(win);
  }
  for (const l of g.lines) {
    if (l.op < 0.01 || l.h < 0.3) continue;
    const bg = l.kind === "fade" ? `linear-gradient(${l.dir === "up" ? "0deg" : "180deg"},${hexA(l.colour, 0)},${hexA(l.colour, 1)})` : col(l.colour);
    frag.appendChild(mk(`position:absolute;left:${r2(l.x)}px;top:${r2(l.y)}px;width:${r2(l.w)}px;height:${r2(l.h)}px;background:${bg};opacity:${r2(l.op)}`));
  }
}

/* ---------------------------------------------------------------- footage blur + built-in transitions (transitions.js) */
const TRX = window.VEOS_TRANSITIONS || null;
let TRC = null, STG = [], FXDEFS = []; // compiled transitions / blur envelopes; this frame's stage elements; their SVG filters
const FULL = `position:absolute;left:0;top:0;width:${W}px;height:${H}px`;
const fxAt = (at, face) => (Array.isArray(at) ? at : at === "face" && face ? [face.cx, face.cy] : [W / 2, H / 2]);
const isWinEl = e => e.style && e.style.overflow === "hidden"; // a footage / cell window or the band backdrop: opaque inside
const opqOf = l => { const d = SCENES[l.order] || {}; return !!(d.opaque || d.covers_presenter || COVER_KINDS.includes(d.kind)); }; // an opaque z1 plate
function gradePulses(n, frame) { // timeline.grades[] `blur` px on the event's fade envelope (frame: true = the whole picture)
  if (!GRD || !GR.events.length) return [];
  return GRD.eventsAt(GR.events, n).filter(e => e.ev.blur > 0 && !!e.ev.frame === frame).map(e => ({ kind: "defocus", v: e.ev.blur * e.op }));
}
function cloneDeep(node) { // a copy that keeps canvas pixels
  const c = node.cloneNode(true), a = node.querySelectorAll("canvas"), b = c.querySelectorAll("canvas");
  a.forEach((cv, i) => { const d = b[i]; d.width = cv.width; d.height = cv.height; d.style.cssText = cv.style.cssText; d.getContext("2d").drawImage(cv, 0, 0); });
  return c;
}
/* blur one element's content in place: its children move into a holder; radial = 8 scaled copies about the centre
   (equal-weight average), defocus / directional = an SVG filter (opaque: refill the edge alpha, no dark halo) */
function blurEl(el, b, face, opaque) {
  if (!el || !el.childNodes || !el.childNodes.length) return;
  const ox = parseFloat(el.style.left) || 0, oy = parseFloat(el.style.top) || 0, box0 = "position:absolute;left:0;top:0;width:100%;height:100%";
  const hold = mk(box0); while (el.firstChild) hold.appendChild(el.firstChild);
  let box = hold;
  if (b.radial && b.radial.amount > 0.002) {
    const [cx, cy] = fxAt(b.radial.at, face), K = 8;
    box = mk(box0); box.appendChild(hold);
    for (let i = 1; i < K; i++) { const c = cloneDeep(hold); c.style.transformOrigin = `${r2(cx - ox)}px ${r2(cy - oy)}px`; c.style.transform = `scale(${(1 + b.radial.amount * i / (K - 1)).toFixed(4)})`; c.style.opacity = (1 / (i + 1)).toFixed(4); box.appendChild(c); }
  }
  const id = `fx${FXDEFS.length}`, f = TRX.blurFilter(id, b, opaque);
  if (f) { FXDEFS.push(f); box.style.filter = `url(#${id})`; }
  el.appendChild(box);
}
function fxMove(el, m, face) {
  if (!m) return;
  const [cx, cy] = fxAt(m.at, face);
  el.style.transformOrigin = `${r2(cx)}px ${r2(cy)}px`; el.style.transform = `translate(${r2(m.x)}px,${r2(m.y)}px) scale(${(m.s || 1).toFixed(4)})`;
}
function fxMask(el, c, face, hole) { // circle (iris) or hole (burn) mask; c.r = 0..1 of the farthest corner
  const [cx, cy] = fxAt(c.at, face), R = c.r * TRX.maxR(cx, cy), fe = hole ? 40 : (c.feather || 0);
  const g = hole ? `radial-gradient(circle at ${r2(cx)}px ${r2(cy)}px,transparent ${r2(R)}px,#000 ${r2(R + fe)}px)` : `radial-gradient(circle at ${r2(cx)}px ${r2(cy)}px,#000 ${r2(Math.max(0, R - fe))}px,transparent ${r2(R)}px)`;
  el.style.webkitMaskImage = g; el.style.maskImage = g;
}
function fxCurtain(el, c) { // the incoming frame enters with an eased clip rect (slide: it also travels)
  const D = (1 - c.e) * (c.dir === "left" || c.dir === "right" ? W : H), d = r2(D), s = c.slide;
  const m = { down: [s ? `translateY(${-d}px)` : "", s ? `inset(${d}px 0 0 0)` : `inset(0 0 ${d}px 0)`], up: [s ? `translateY(${d}px)` : "", s ? `inset(0 0 ${d}px 0)` : `inset(${d}px 0 0 0)`],
    left: [s ? `translateX(${d}px)` : "", s ? `inset(0 ${d}px 0 0)` : `inset(0 0 0 ${d}px)`], right: [s ? `translateX(${-d}px)` : "", s ? `inset(0 0 0 ${d}px)` : `inset(0 ${d}px 0 0)`] }[c.dir];
  if (m[0]) el.style.transform = m[0]; el.style.clipPath = m[1];
}
/* fix-visual: a flash fill. blend "light" (the default for white / near-white) lights the picture like an exposure: a
   colour-dodge layer at colour x op x 0.9 (shadows stay dark, highlights bloom) plus a soft veil at op^2 (full white at
   op 1); "screen" / "add" are the CSS blends; "normal" is the old flat veil. wipe {dir, r, feather}: the part the
   clear has passed (top -> bottom for dir "down") is transparent. Returns an array of elements (blends need siblings). */
function flashEls(o) {
  const c = col(o.colour), w = o.wipe;
  let m = "";
  if (w) {
    const L = w.dir === "left" || w.dir === "right" ? W : H, F = w.feather || 0, e = w.r * (L + F) - F;
    const g = `linear-gradient(${{ down: "to bottom", up: "to top", right: "to right", left: "to left" }[w.dir] || "to bottom"},transparent ${r2(e)}px,#000 ${r2(e + F)}px)`;
    m = `-webkit-mask-image:${g};mask-image:${g};`;
  }
  const hx = /^#([0-9a-f]{6})$/i.exec(String(c));
  if (o.blend === "light" && hx) {
    const v = [0, 2, 4].map(i => Math.round(parseInt(hx[1].slice(i, i + 2), 16) * o.op * 0.9));
    return [mk(`${FULL};background:rgb(${v.join(",")});mix-blend-mode:color-dodge;${m}`), mk(`${FULL};background:${c};opacity:${r2(o.op * o.op)};${m}`)];
  }
  const bm = o.blend === "screen" ? "mix-blend-mode:screen;" : o.blend === "add" ? "mix-blend-mode:plus-lighter;" : "";
  return [mk(`${FULL};background:${c};opacity:${o.op};${bm}${m}`)];
}
function fxOverlay(o, face) {
  if (o.kind === "fill") return o.blend || o.wipe ? flashEls(o) : mk(`${FULL};background:${col(o.colour)};opacity:${o.op}`);
  if (o.kind === "leak") {
    const cs = o.colours.map(col), N = cs.length, stops = cs.map((c, i) => `${c} ${r2(o.pos - 30 + 50 * i / (N - 1))}%`).join(",");
    return mk(`${FULL};mix-blend-mode:screen;pointer-events:none`, `<div style="${FULL};background:${cs[0]};opacity:${o.wash}"></div><div style="${FULL};opacity:${o.op};background:linear-gradient(${o.angle}deg,transparent ${r2(o.pos - 55)}%,${stops},transparent ${r2(o.pos + 45)}%)"></div>`);
  }
  if (o.kind === "ring") {
    const [cx, cy] = fxAt(o.at, face), R = o.r * TRX.maxR(cx, cy), c = col(o.colour), at = `circle at ${r2(cx)}px ${r2(cy)}px`;
    const g = o.hard ? `radial-gradient(${at},transparent ${r2(Math.max(0, R - o.ring))}px,${c} ${r2(Math.max(0, R - o.ring))}px,${c} ${r2(R)}px,transparent ${r2(R)}px)`
      : `radial-gradient(${at},transparent ${r2(Math.max(0, R - o.ring * 0.4))}px,${c} ${r2(R + 20)}px,${hexA(o.colour, 0)} ${r2(R + o.ring)}px)`;
    return mk(`${FULL};background:${g};opacity:${o.op};${o.hard ? "" : "mix-blend-mode:screen;"}`);
  }
  return null;
}
/* the transition / pulse / end-fade description of this frame (transitions.js frameFx) -> the root's children */
function fxCompose(fx, cur, oth) {
  const face = cur.face, out = [];
  let P = mk(FULL); P.appendChild(cur.frag); if (fx.layers === "all") P.appendChild(cur.top);
  if (fx.blur) blurEl(P, fx.blur, face, true);
  fxMove(P, fx.move, face);
  if (fx.filter && fx.filter.burn) P.style.filter = TRX.burnCss(fx.filter.burn);
  if (fx.circle) fxMask(P, fx.circle, face, false);
  if (fx.curtain) fxCurtain(P, fx.curtain);
  if (fx.glitch) { // slices of the composited frame shifted sideways, RGB split + posterise over all of it
    const G = mk(FULL); G.appendChild(P);
    for (const s of fx.glitch.slices) { if (Math.abs(s.dx) < 0.5) continue; const c = cloneDeep(P); c.style.clipPath = `inset(${r2(s.y)}px 0 ${r2(Math.max(0, H - s.y - s.h))}px 0)`; c.style.transform = `translateX(${r2(s.dx)}px)`; G.appendChild(c); }
    if (fx.glitch.rgb > 0.3 || fx.glitch.levels >= 2) { const id = `fx${FXDEFS.length}`; FXDEFS.push(TRX.glitchFilter(id, fx.glitch)); G.style.filter = `url(#${id})`; }
    P = G;
  }
  let O = null;
  if (oth && fx.other) {
    const o = fx.other; O = mk(FULL); O.appendChild(oth.frag);
    if (o.blur) blurEl(O, o.blur, face, true);
    fxMove(O, o.move, face);
    if (o.circle) fxMask(O, o.circle, face, false);
    if (o.hole) fxMask(O, o.hole, face, true);
    if (o.filter && o.filter.burn) O.style.filter = TRX.burnCss(o.filter.burn);
    if (o.op < 1) O.style.opacity = o.op;
    for (const q of o.overlays || []) { const e = fxOverlay(q, face); if (e) [].concat(e).forEach(x => O.appendChild(x)); } // the flash that lit the frozen frame
  }
  if (O && fx.other.pos === "under") out.push(O);
  out.push(P);
  if (O && fx.other.pos !== "under") out.push(O);
  for (const o of fx.overlays) { const e = fxOverlay(o, face); if (e) out.push(...[].concat(e)); }
  if (fx.layers !== "all") out.push(cur.top);
  if (fx.fade) out.push(mk(`${FULL};background:${col(fx.fade.colour)};opacity:${fx.fade.op}`));
  return out;
}

async function composeFrame(n) { // one frame's layers -> {frag: world .. z6, top: captions + z7..11, face}; renderFrameImpl draws them
  const t = n / FPS;
  const st = stageAt(n), g = st.g;
  const wst = WLD.at(WSCHED, n, WORLDS.dflt), world = wst.id;
  const cam = cameraAt(n, g), Fs = faceSm(n), Fr = faceRaw(n);
  const active = LAYERS.filter(l => n >= l.fin && n < l.fout);
  const behind = active.filter(l => l.behind);
  const showWin = g.op > 0.01 && g.w > 1 && g.h > 1;
  const breakout = showWin && !st.morph && g.bo > 0.5 && FOOTAGE; // head breakout over the window's top edge (card / pip `breakout`)
  const needCut = showWin && (behind.length > 0 || breakout);
  let urls = { f: fUrl(n), c: cUrl(n) };
  GEO = null; GCOL = ""; STG = [];
  // E-16 grades: the base grade (scene > world > timeline.grade > theme > grades.footage) and the timeline.grades[] events
  let gBase = null;
  { const gs = active.filter(l => l.gset).sort((a, b) => a.z - b.z || a.order - b.order);
    if (gs.length) gBase = gs[gs.length - 1].gspec;
    else if (Object.prototype.hasOwnProperty.call(GR.worlds, world)) gBase = GR.worlds[world];
    else if (GR.reelSet) gBase = GR.reel;
    else gBase = GR.theme || GR.footage; }
  const gEv = GRD && GR.events.length ? GRD.eventsAt(GR.events, n).filter(e => e.ev.spec) : []; // (blur-only events: transitions.js pulses)
  const fz = gEv.find(e => e.ev.freeze); // a freeze holds the footage AND the cut-out on the event's first frame
  if (fz) urls = { f: fUrl(fz.ev.f0), c: cUrl(fz.ev.f0) };
  const evUrls = gEv.map(() => urls);
  if ((!MEASURE || PIX) && showWin) { // measure only needs layout, not pixels (measureText with pixels does)
    const pl = [preload(urls.f)]; if (needCut) pl.push(preload(urls.c));
    for (const u of evUrls) if (u !== urls) { pl.push(preload(u.f)); if (needCut) pl.push(preload(u.c)); }
    await Promise.all(pl);
  }
  const ccS = CC && CC.active ? CAMLIB.stateAt(CC, n) : null, ccP = ccS && n > 0 ? CAMLIB.stateAt(CC, n - 1) : null;
  LCAM = {}; LANC = {};

  // footage -> screen transform (+ banner clamp)
  const S = g.s * cam.s, rad = cam.r * Math.PI / 180, cs = Math.cos(rad), sn = Math.sin(rad);
  let tx = g.ax + cam.dx + cam.shx, ty = g.ay + cam.dy + cam.shy; // dx/dy: an origin other than the face (0 otherwise)
  const toScr = (px, py) => { const dx = (px - g.Fx) * S, dy = (py - g.Fy) * S; return [tx + dx * cs - dy * sn, ty + dx * sn + dy * cs]; };
  const rectScr = b => { const pts = [toScr(b[0], b[1]), toScr(b[0] + b[2], b[1]), toScr(b[0] + b[2], b[1] + b[3]), toScr(b[0], b[1] + b[3])]; const xs = pts.map(p => p[0]), ys = pts.map(p => p[1]); const x = Math.min(...xs), y = Math.min(...ys); return { x, y, w: Math.max(...xs) - x, h: Math.max(...ys) - y }; };
  if (showWin && st.name === "full" && !st.morph && (cam.s !== 1 || cam.r !== 0 || cam.shx || cam.shy) && active.some(l => l.z === BANNER_Z)) {
    // the camera may not push the face under the banner: shift the footage down (never past the footage top edge)
    const lay = T.layout, limit = (lay.banner_top || 150) + 2 * 78 * 1.02 + 56 + (lay.face_clearance || 40);
    const natTop = g.ay + (Fr[1] - g.Fy) * g.s, cur = rectScr(Fr).y, need = Math.min(natTop, limit);
    if (cur < need) ty += Math.min(need - cur, Math.max(0, -(ty - S * g.Fy)));
  }
  if (showWin && cam.s < 1 && cam.r === 0) { // camera v2 from_wide: wider than the base framing, but the footage still covers the window
    const fr = rectScr([0, 0, W, H]);
    if (fr.w >= g.w) { if (fr.x > g.x) tx -= fr.x - g.x; else if (fr.x + fr.w < g.x + g.w) tx += g.x + g.w - fr.x - fr.w; }
    if (fr.h >= g.h) { if (fr.y > g.y) ty -= fr.y - g.y; else if (fr.y + fr.h < g.y + g.h) ty += g.y + g.h - fr.y - fr.h; }
  }
  // camera v2: graphics that ride the camera (front follow_footage scenes: all of it; z1-6 by cam.w after target "all").
  // The camera part only (not the base reframe), as a CSS matrix at weight w; null = identity
  const camM = w => {
    if (!(w > 0.001) || (cam.s === 1 && cam.r === 0 && tx === g.ax && ty === g.ay)) return null;
    const cw = Math.pow(cam.s, w), rw = cam.r * w * Math.PI / 180, a = cw * Math.cos(rw), b = cw * Math.sin(rw);
    return [a, b, -b, a, g.ax + (tx - g.ax) * w - (a * g.ax - b * g.ay), g.ay + (ty - g.ay) * w - (b * g.ax + a * g.ay)];
  };
  const mA = cs * S, mB = sn * S, mC = -sn * S, mD = cs * S;
  const mE = tx - (mA * g.Fx + mC * g.Fy), mF = ty - (mB * g.Fx + mD * g.Fy);
  const exact = S === 1 && cam.r === 0;
  const faceOut = showWin ? (() => { const r = rectScr(Fr); return { x: r.x, y: r.y, w: r.w, h: r.h, cx: r.x + r.w / 2, cy: r.y + r.h / 2 }; })() : null;
  // E-16: the footage grade as filter functions. The vignette follows the WINDOW, mapped into footage px (the images' own
  // space), so the frame, the cut-out and the breakout share one filter and the person matches the footage exactly.
  let gFoot = "", gEvF = [];
  if (showWin && GRD) {
    const det = mA * mD - mB * mC || 1, inv = (x, y) => { const X = x - mE, Y = y - mF; return [(mD * X - mC * Y) / det, (-mB * X + mA * Y) / det]; };
    const cs4 = [inv(g.x, g.y), inv(g.x + g.w, g.y), inv(g.x, g.y + g.h), inv(g.x + g.w, g.y + g.h)];
    const rx = Math.min(...cs4.map(p => p[0])), ry = Math.min(...cs4.map(p => p[1]));
    const wr = [rx, ry, Math.max(...cs4.map(p => p[0])) - rx, Math.max(...cs4.map(p => p[1])) - ry];
    gFoot = gradeF(gBase, { rect: wr }); GCOL = gradeF(gBase, { spatial: false });
    gEvF = gEv.map(e => gradeF(e.ev.spec, { rect: wr }));
  } else if (GRD) GCOL = gradeF(gBase, { spatial: false });

  // shared ctx
  const base = {
    n, t, fps: FPS, W, H, tokens: T, safe: T.layout.safe, face: () => faceOut,
    ease, lerp, clamp: cl, measure, asset: id => (ASSETS[id] ? ASSETS[id].url : ""), videoFrame, word: i => WORDS[i] || null,
    // the decoded <img> of an image asset (preloaded at boot; for canvas / WebGL textures), and the layout-only measure flag
    assetImage: id => (ASSETS[id] && ASSETS[id]._im) || null, measuring: MEASURE && !PIX,
    wordsBetween: (a, b) => WORDS.filter(w => w.s >= a && w.s < b), html: s => s, blur: (px, ang) => (ang == null ? (VBS.push(px), `url(#vb${VBS.length - 1})`) : dirBlur(px, ang) || "none"),
    fam, col, hexA, esc, stageName: st.name, world, footage: FOOTAGE, layout: () => layoutInfo(st),
    fmtNum: VEOS.fmtNum, fig: VEOS.fig, figScale: VEOS.figScale, figAt: (id, tt, o) => VEOS.figAt(id, tt == null ? t : tt, o),
    // E-16b: the reel's base reframe ({s, tx, ty, setup, face {x,y,w,h,cx,head_top,eye,chin}} on a full stage, or null)
    framing: FRAMING, faceRef: () => faceRefAt(st), faceBand,
    // E-16: a grade (tokens.grades.scene id, CSS list or spec) as a `filter:...;` declaration for a scene's own clip/image
    grade: (spec, o) => { if (!GRD) return ""; let s; try { s = GRD.norm(spec, T); } catch (e) { VEOS.errors.push(`ctx.grade: ${e.message}`); return ""; } const f = gradeF(s, Object.assign({ spatial: false }, o || {})); return f ? `filter:${f};` : ""; },
    gradeId: gBase ? gBase.id : null,
    fitText, worldHTML: (id, o) => (WORLDS.has(id) ? WORLDS.html(id, n, o || null) : ""),
    // Package E: an object track on screen at this frame ({x,y,w,h,cx,cy,conf,lost}) or null; clip tracks: o {t (clip s), place}
    track: (id, o) => { const Tk = TRACKS[id]; if (!TRK || !Tk) return null; o = o || {};
      if (Tk.space === "clip") return TRK.screenBox(Tk, Math.round((+o.t || 0) * FPS), o, null);
      return showWin ? TRK.screenBox(Tk, n, o, { toScr }) : null; },
  };
  base.V = (lt, inDur, outAt, o = {}) => {
    const inF = secF(inDur), outF = o.dout != null ? o.dout : (OUT_F[o.out] != null ? OUT_F[o.out] : 5), k = Math.round(lt * FPS);
    const kRem = outAt == null ? 1e9 : Math.round((outAt - lt) * FPS) + outF;
    if (lt < -1e-6) return null; if (outAt != null && lt >= outAt + outF / FPS) return null;
    const s = presetState(o.in || "blur", o.out || "blur", k, kRem, inF || IN_F[o.in || "blur"], outF, TRAVEL_IN.includes(o.in) ? false : undefined); // travel presets arrive opaque
    return styleOf(s, "50% 50%", o.op);
  };
  function styleOf(s, origin, op) {
    const extra = s.vb > 0.4 ? vbFilter(s.vb) : (s.bl > 0.05 ? `filter:blur(${r2(s.bl)}px);` : "");
    return `opacity:${r2(s.op * (op == null ? 1 : op))};transform-origin:${origin};transform:translate(${r2(s.dx)}px,${r2(s.dy)}px) rotate(${r2(s.rot)}deg) scale(${s.sx.toFixed(4)},${s.sy.toFixed(4)});${extra}`;
  }

  const renderLayer = L => {
    const nq = stepN(L, n), lt = (nq - L.fin) / FPS, dur = (L.fout - L.fin) / FPS; // nq: the held frame of a stepped scene
    const ctx = layerCtx(base, L, nq);
    if (nq !== n) { ctx.n = nq; ctx.t = nq / FPS; }
    const cam = camCtx(ccS, ccP, ccS ? L.k : 0); ctx.camera = cam;
    let html;
    try { html = L.render(ctx, lt, dur); } catch (e) { VEOS.errors.push(`${L.id} @${n}: ${e && e.stack || e}`); throw new Error(`scene ${L.id} failed at frame ${n}: ${e && e.message}`); }
    const box = L.box || { x: 0, y: 0, w: W, h: H };
    const inN = L.in || "settle", outN = L.out || "none";
    const inF = L.inF != null ? L.inF : (IN_F[inN] || 0), outF = L.outF != null ? L.outF : (OUT_F[outN] != null ? OUT_F[outN] : 5);
    const s = MEASURE ? ID() : presetState(inN, outN, nq - L.fin, L.fout - nq, inF, outF, L.inFade);
    const org = `${r2(box.x + box.w / 2)}px ${r2(box.y + box.h / 2)}px`;
    let sty = styleOf(s, org);
    if (L.smear && !MEASURE) { // velocity smear: the preset's own travel since the previous (held) frame, along its direction
      const p0 = presetState(inN, outN, nq - L.fin - (L.stepF || 1), L.fout - nq + (L.stepF || 1), inF, outF, L.inFade), vx = s.dx - p0.dx, vy = s.dy - p0.dy, v = Math.hypot(vx, vy);
      if (v > 2) sty = sty.replace(/filter:[^;]*;/, "") + `filter:${dirBlur(Math.min(L.smearPx, v * 0.3), Math.atan2(vy, vx) * 180 / Math.PI)};`;
    }
    const el = mk(`position:absolute;left:0;top:0;width:${W}px;height:${H}px;${sty}`, typeof html === "string" ? html : "");
    el.dataset.scene = L.id; if (ctx._cv) { el.dataset.canvas = "1"; el.appendChild(ctx._cv); }
    if (L.anchor && TRK) { // Package E: the box centre follows the track point (+ offset), scaled with the object; hold / fade when lost
      const A = TRK.state(L.anchor, TRACKS[L.anchor.track], L.fin, n, L.box, { toScr, visible: showWin, scaleAt: m => { const q = cl(m, 0, NF - 1); return stageAt(q).g.s * cameraAt(q).s; } });
      if (!A) return mk(`position:absolute;left:0;top:0;width:${W}px;height:${H}px;opacity:0`);
      LANC[L.id] = A;
      const wrap = mk(`position:absolute;left:0;top:0;width:${W}px;height:${H}px;transform-origin:${r2(A.cx)}px ${r2(A.cy)}px;transform:translate(${r2(A.dx)}px,${r2(A.dy)}px) scale(${A.s.toFixed(4)});opacity:${r2(A.op)}`);
      wrap.dataset.anchor = L.anchor.track; wrap.appendChild(el); return wrap;
    }
    if (L.follow && !L.behind) { // follow_footage on a front scene: footage px -> screen (base reframe, stage layout, camera)
      const wrap = mk(`position:absolute;left:0;top:0;width:${W}px;height:${H}px;transform-origin:0 0;transform:matrix(${[mA, mB, mC, mD].map(v => v.toFixed(5)).join(",")},${r2(mE)},${r2(mF)});${showWin ? "" : "opacity:0;"}`);
      wrap.dataset.follow = "1"; wrap.appendChild(el); return wrap;
    }
    if (ccS && L.k > 0) { // the canvas camera moves this world layer (captions, chrome, z>=7 and behind scenes never move)
      const M = cam.matrix; LCAM[L.id] = M;
      const bl = MEASURE ? 0 : cl((cam.speed - 18) / 10, 0, 8);
      const wrap = mk(`position:absolute;left:0;top:0;width:${W}px;height:${H}px;transform-origin:0 0;transform:matrix(${M.map(v => v.toFixed(5)).join(",")});${bl > 0.3 ? `filter:blur(${r2(bl)}px);` : ""}`);
      wrap.dataset.ccam = "1"; wrap.appendChild(el); return camWrap(L, wrap);
    }
    return camWrap(L, el);
  };
  // camera v2: front follow_footage scenes ride the camera, z1-6 scenes ride it while target "all" (never captions or
  // z7+ unless they follow). Behind scenes in screen space ride it with target "all" too (fix-visual: the depth-sandwich
  // card zooms with the composition); behind follow_footage scenes already ride the footage transform. Measure sees the
  // resting position.
  function camWrap(L, el) {
    if (MEASURE || (L.behind && L.follow)) return el;
    const M = camM(L.behind ? cam.w : L.follow ? 1 : (L.z <= 6 ? cam.w : 0));
    if (!M) return el;
    const wrap = mk(`position:absolute;left:0;top:0;width:${W}px;height:${H}px;transform-origin:0 0;transform:matrix(${M.map(v => v.toFixed(5)).join(",")})`);
    wrap.dataset.fcam = "1"; wrap.appendChild(el); return wrap;
  }

  const root = document.getElementById("root"), frag = document.createDocumentFragment();
  // world
  const wctx = showWin && !(g.x <= 0 && g.y <= 0 && g.x + g.w >= W && g.y + g.h >= H) ? (GCOL ? { fUrl: urls.f, gf: GCOL } : { fUrl: urls.f }) : null;
  const w = mk(`position:absolute;inset:0;overflow:hidden`, wst.under ? worldHTML(wst.under, n, wctx) + `<div style="position:absolute;inset:0;opacity:${r2(wst.op)}">${worldHTML(world, n, wctx)}</div>` : worldHTML(world, n, wctx));
  frag.appendChild(w);
  if (g.ext && g.bd) STG.push(frag.appendChild(backdropEl(g.bd, n)));
  const below = active.filter(l => !l.behind && l.z <= 3), above = active.filter(l => !l.behind && l.z > 3);
  for (const l of below) { const e = frag.appendChild(renderLayer(l)); if (l.z === 1) { e.__opq = opqOf(l); STG.push(e); } } // z1 plates take the footage blur
  const stg0 = frag.childNodes.length; // footage window .. second sources: the stage (footage blur)
  // footage group
  if (showWin) {
    const corner = g.r.map(v => r2(v) + "px").join(" ");
    let shadow = "";
    if (g.ext) { shadow = decorCss(g); if (g.ringG && g.ring > 0.3) frag.appendChild(ringEl(g)); }
    else if (g.ring > 0.3) shadow = `box-shadow:0 0 0 ${r2(g.ring)}px ${col("paper")},${r2(g.sh * 0.5)}px ${r2(g.sh)}px 0 ${r2(g.ring)}px ${col("ink")};`;
    else if (g.soft > 0.01 && world !== "studio") shadow = `box-shadow:0 -6px 30px rgba(0,0,0,${r2(0.18 * g.soft)});`;
    const win = mk(`position:absolute;left:${r2(g.x)}px;top:${r2(g.y)}px;width:${r2(g.w)}px;height:${r2(g.h)}px;border-radius:${corner};overflow:hidden;opacity:${r2(g.op)};${shadow}${maskCss(g.mask)}`);
    const mvb = st.morph && (st.morph === "panel-drop" || st.morph === "pop-back") ? 22 * Math.sin(Math.PI * cl(st.q)) : (g.mvb || 0);
    const gvb = Math.max(cam.vb, mvb);
    const mtx = dy => (exact ? `translate(${r2(mE)}px,${r2(mF - dy)}px)` : `matrix(${mA.toFixed(5)},${mB.toFixed(5)},${mC.toFixed(5)},${mD.toFixed(5)},${r2(mE)},${r2(mF - dy)})`);
    const mkGrp = dy => mk(`position:absolute;left:${r2(-g.x)}px;top:${r2(-g.y)}px;width:${W}px;height:${H}px;transform-origin:0 0;transform:${mtx(dy)};${vbFilter(gvb)}`);
    const imgPos = `position:absolute;left:0;top:0;width:${W}px;height:${H}px;`;
    const imgStyle = imgPos + (g.ext ? fjoin(gFoot, dimF(g)) : fjoin(gFoot));
    // E-16 grade events: a graded copy of the footage / cut-out (frozen at the event start with `freeze`) over the base
    const evImgs = which => gEv.map((e, i) => `<img data-foot="1" src="${evUrls[i][which]}" style="${imgPos}${g.ext ? fjoin(gEvF[i], dimF(g)) : fjoin(gEvF[i])}opacity:${r2(e.op)}">`).join("");
    const off = g.off || 0;
    if (off > 0.5) { // "low" layout: blurred, darkened copy of the frame fills the revealed area
      win.insertAdjacentHTML("beforeend", `<img data-foot="1" src="${urls.f}" style="position:absolute;left:${r2(-W * 0.075 - g.x)}px;top:${r2(-H * 0.075 - g.y)}px;width:${r2(W * 1.15)}px;height:${r2(H * 1.15)}px;filter:${GCOL ? GCOL + " " : ""}blur(40px) brightness(.45)">`);
    }
    // depth sandwich: footage (lowered) -> behind layers -> cut-out (lowered). A behind scene stays in SCREEN space: the
    // base reframe, a camera punch and the `low` offset never move it (what it declares is where it lands). Only
    // `follow_footage: true` rides the footage transform (an object pinned to a spot in the room).
    const grp = mkGrp(0);
    if (g.ext && g.blur > 0.05) grp.insertAdjacentHTML("beforeend", `<img data-foot="1" src="${urls.f}" style="${imgPos}${fjoin(gFoot, dimF(g, true))}">`); // sharp under-copy: no see-through blur edges
    grp.insertAdjacentHTML("beforeend", `<img data-foot="1" src="${urls.f}" style="${imgStyle}">` + evImgs("f"));
    win.appendChild(grp);
    const bFollow = behind.filter(l => l.follow), bScreen = behind.filter(l => !l.follow);
    if (bFollow.length) { const gb = off > 0.5 ? mkGrp(off) : grp; for (const l of bFollow) gb.appendChild(renderLayer(l)); if (gb !== grp) win.appendChild(gb); }
    if (bScreen.length) { // screen space, still clipped to the window: undo only the window's own offset
      const gs = mk(`position:absolute;left:${r2(-g.x)}px;top:${r2(-g.y)}px;width:${W}px;height:${H}px`); gs.dataset.behind = "screen";
      for (const l of bScreen) gs.appendChild(renderLayer(l));
      win.appendChild(gs);
    }
    if (needCut && behind.length) { const gc = off > 0.5 || bScreen.length ? mkGrp(0) : grp; gc.insertAdjacentHTML("beforeend", `<img data-foot="1" src="${urls.c}" style="${imgStyle}">` + evImgs("c")); if (gc !== grp) win.appendChild(gc); }
    frag.appendChild(win);
    if (breakout) { // E-16c head breakout: the cut-out above the window's top edge (clipped to the window's columns)
      const top = Math.max(0, g.y - g.bo), bot = g.y + 1; // inside the window the cut-out equals the footage: only the part above the edge shows
      const clip = mk(`position:absolute;left:0;top:0;width:${W}px;height:${H}px;opacity:${r2(g.op)};clip-path:inset(${r2(top)}px ${r2(Math.max(0, W - g.x - g.w))}px ${r2(Math.max(0, H - bot))}px ${r2(Math.max(0, g.x))}px)`);
      const gr = mk(`position:absolute;left:0;top:0;width:${W}px;height:${H}px;transform-origin:0 0;transform:${mtx(0)};${vbFilter(gvb)}`);
      gr.insertAdjacentHTML("beforeend", `<img data-foot="1" src="${urls.c}" style="${imgStyle}">` + evImgs("c"));
      clip.appendChild(gr); clip.dataset.breakout = "1"; frag.appendChild(clip);
    }
    GEO = { m: [mA, mB, mC, mD, mE, mF], win: [g.x, g.y, g.w, g.h], cut: needCut ? urls.c : null };
  }
  if (g.ext) extraEls(frag, g, n); // second sources / faux crops, seam hairline and fades (layouts.js)
  for (let i = stg0; i < frag.childNodes.length; i++) STG.push(frag.childNodes[i]);
  const CAPS = window.VEOS_CAPTIONS, subs = CAPS && CAPS.active ? CAPS.html(n, { st, world, g, face: faceOut }) : subtitleHTML(n, st, world); // E-05
  const items = above.map(l => ({ z: l.z, order: l.order, l })).concat([{ z: 7, order: 1e6, sub: true }]).sort((a, b) => a.z - b.z || a.order - b.order);
  const top = document.createDocumentFragment(); // captions and z7+ (kept above a transition unless it takes `layers: "all"`)
  for (const it of items) { const into = it.z >= 7 ? top : frag; if (it.sub) { if (subs) { const sd = mk(`position:absolute;left:0;top:0;width:${W}px;height:${H}px`, subs); sd.dataset.scene = "__subtitles"; into.appendChild(sd); } } else into.appendChild(renderLayer(it.l)); }
  if (!MEASURE && TRC) { const sb = TRX.stageBlurAt(TRC, n, gradePulses(n, false)); if (sb) for (const e of STG) blurEl(e, sb, faceOut, e.__opq != null ? e.__opq : isWinEl(e)); }
  return { frag, top, face: faceOut };
}
async function renderFrameImpl(n) {
  n = cl(Math.round(n), 0, NF - 1);
  VBS = []; cvUsed = 0; VPEND = []; GDEFS = []; FXDEFS = [];
  const fx = !MEASURE && TRC ? TRX.frameFx(TRC, n, gradePulses(n, true)) : null;
  const oth = fx && fx.other ? await composeFrame(cl(fx.other.n, 0, NF - 1)) : null; // the outgoing frame (frozen) first: this frame's GEO / LCAM win
  const cur = await composeFrame(n);
  const root = document.getElementById("root");
  // filters
  let defs = ""; VBS.forEach((v, i) => { defs += vbDef(v, i); });
  const kids = fx ? fxCompose(fx, cur, oth) : [cur.frag, cur.top];
  defs += GDEFS.join("") + FXDEFS.join("");
  const svg = mk(`position:absolute;width:0;height:0`, `<svg width="0" height="0" style="position:absolute"><defs>${defs}</defs></svg>`);
  root.replaceChildren(svg, ...kids);
  await Promise.all([...root.querySelectorAll("img")].filter(i => !(MEASURE && !PIX && i.dataset.foot)).map(i => i.decode().catch(() => {})).concat(VPEND));
  await document.fonts.ready;
  if (!MEASURE || PIX) await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));
  return true;
}

/* ---------------------------------------------------------------- measure: union rect of each scene's painted DOM (resting position, presets neutralised) */
/* Non-text full-frame wrappers (a scaled `inset:0` diagram wrapper, a full-frame SVG arrow layer, a painted backdrop) are
   not the scene's footprint: an element covering >= 85 % of the frame in both directions only counts when the scene has
   nothing else (a plate) or covers the presenter by declaration (opaque / covers_presenter / full-frame footage kinds).
   Canvas-camera layers: the rect is the on-screen part (clipped to the frame) and `__world` holds the camera-at-rest
   rect (what V-SAFE judges: a push into a hub is the camera's move, not a layout outside the safe zone). */
const COVER_KINDS = ["broll", "footage", "clip", "archive", "video"];
const bigEl = r => r.width >= 0.85 * W && r.height >= 0.85 * H;
function invRect(M, q) { // world rect of a screen rect under the canvas-camera matrix M = [a, b, c, d, e, f]
  const [a, b, c, d, e, f] = M, det = a * d - b * c || 1;
  const inv = (x, y) => { const X = x - e, Y = y - f; return [(d * X - c * Y) / det, (-b * X + a * Y) / det]; };
  const ps = [inv(q[0], q[1]), inv(q[2], q[1]), inv(q[0], q[3]), inv(q[2], q[3])];
  return [Math.min(...ps.map(p => p[0])), Math.min(...ps.map(p => p[1])), Math.max(...ps.map(p => p[0])), Math.max(...ps.map(p => p[1]))];
}
function measureDOM() {
  const out = {}, world = {};
  for (const el of document.querySelectorAll("#root [data-scene]")) {
    const id = el.dataset.scene; let x0 = 1e9, y0 = 1e9, x1 = -1e9, y1 = -1e9, any = false;
    const meta = SCENES.find(s => String(s.id) === id) || {};
    const cover = !!(meta.opaque || meta.covers_presenter || COVER_KINDS.includes(meta.kind));
    const big = [];
    const add = (r, text) => {
      if (r.width < 0.5 || r.height < 0.5) return;
      if (!text && !cover && bigEl(r)) { big.push(r); return; }
      any = true; x0 = Math.min(x0, r.left); y0 = Math.min(y0, r.top); x1 = Math.max(x1, r.right); y1 = Math.max(y1, r.bottom);
    };
    const addBox = b => { let q = [b.x, b.y, b.x + b.w, b.y + b.h]; if (LCAM[id] && CAMLIB) q = CAMLIB.rect(LCAM[id], q);
      if (LANC[id]) { const A = LANC[id], m = (v, c, d) => c + (v - c) * A.s + d; q = [m(q[0], A.cx, A.dx), m(q[1], A.cy, A.dy), m(q[2], A.cx, A.dx), m(q[3], A.cy, A.dy)]; } add({ width: q[2] - q[0], height: q[3] - q[1], left: q[0], top: q[1], right: q[2], bottom: q[3] }); };
    const eff = e => { let o = 1; for (let p = e; p && p !== el; p = p.parentElement) { const cs = getComputedStyle(p); if (cs.display === "none" || cs.visibility === "hidden") return 0; o *= parseFloat(cs.opacity); } return o; };
    const walk = e => {
      const cs = getComputedStyle(e);
      if (cs.display === "none") return;
      if (eff(e) < 0.02) return;
      const tag = e.tagName.toLowerCase();
      if (tag === "img" || tag === "svg" || tag === "video") { add(e.getBoundingClientRect()); return; }
      if (tag === "canvas") { if (L_BOX[id]) addBox(L_BOX[id]); return; }
      const paints = (cs.backgroundColor && !/rgba\(0, 0, 0, 0\)|transparent/.test(cs.backgroundColor)) || cs.backgroundImage !== "none" || parseFloat(cs.borderTopWidth) > 0 || parseFloat(cs.borderBottomWidth) > 0 || parseFloat(cs.borderLeftWidth) > 0 || cs.boxShadow !== "none";
      if (paints && e !== el) add(e.getBoundingClientRect());
      for (const c of e.childNodes) {
        if (c.nodeType === 3 && c.nodeValue.trim()) { const r = document.createRange(); r.selectNodeContents(c); add(r.getBoundingClientRect(), true); }
        else if (c.nodeType === 1) walk(c);
      }
    };
    walk(el);
    const d = LAYERS.find(l => l.id === id);
    if (!any && el.dataset.canvas && d && d.box) addBox(d.box);
    if (!any && big.length) for (const r of big) { any = true; x0 = Math.min(x0, r.left); y0 = Math.min(y0, r.top); x1 = Math.max(x1, r.right); y1 = Math.max(y1, r.bottom); } // a plate: its full frame is its footprint
    if (!any) continue;
    const r1 = v => Math.round(v * 10) / 10;
    if (LCAM[id]) { // canvas camera: on-screen part + the camera-at-rest (world) rect
      world[id] = invRect(LCAM[id], [x0, y0, x1, y1]).map(r1);
      x0 = Math.max(0, x0); y0 = Math.max(0, y0); x1 = Math.min(W, x1); y1 = Math.min(H, y1);
      if (x1 - x0 < 0.5 || y1 - y0 < 0.5) continue; // wholly off screen this frame
    }
    out[id] = [r1(x0), r1(y0), r1(x1), r1(y1)];
  }
  if (Object.keys(world).length) out.__world = world;
  return out;
}
/* ---------------------------------------------------------------- measureText (E-06): every painted text element of a frame
   (resting position, like measureFrame) for `veos measure` -> plan/measure.text.json. Per element (a parent element of
   text nodes): rendered font size (CSS size x the accumulated transform scale, so a camera or canvas-camera transform on an
   ancestor counts), weight, fill / stroke / shadows, effective opacity, the nearest painted container, rect, per-line
   character counts and glyph clipping (scrollWidth > clientWidth in a clipping or painted box, an overflow-hidden ancestor,
   or the frame edge). Scene HTML may mark nodes: data-tc="TC-..." (text class), data-redundant, data-slot (the E6 slot
   container), data-item (an E4 field item). o: {pixels, chars: [scene ids] (per-character boxes, E1 occlusion),
   items: [scene ids] (E4 item rects)}. SVG and canvas text are not measured. */
const RGBA_RE = /rgba?\([^)]+\)/g;
function rgba(s) { const m = /rgba?\(([^)]+)\)/.exec(s || ""); if (!m) return null; const p = m[1].split(/[ ,/]+/).filter(Boolean).map(parseFloat); return [p[0], p[1], p[2], p.length > 3 ? p[3] : 1]; }
function textDOM(o) {
  const chars = new Set(o.chars || []), itemsFor = new Set(o.items || []), out = { texts: [], items: {}, slots: {}, geo: GEO };
  const root = document.getElementById("root");
  const r1 = v => Math.round(v * 10) / 10, r3 = v => Math.round(v * 1000) / 1000;
  const rr = r => [r1(r.left), r1(r.top), r1(r.right), r1(r.bottom)];
  const effOp = e => { let v = 1; for (let p = e; p && p !== root; p = p.parentElement) { const cs = getComputedStyle(p); if (cs.display === "none" || cs.visibility === "hidden") return 0; v *= parseFloat(cs.opacity); } return v; };
  const scaleOf = e => { // sqrt|det| of the accumulated 2D transform (origins move, they do not scale)
    let a = 1, b = 0, c = 0, d = 1;
    for (let p = e; p && p !== root; p = p.parentElement) {
      const t = getComputedStyle(p).transform;
      if (t && t !== "none") { const m = new DOMMatrixReadOnly(t); [a, b, c, d] = [m.a * a + m.c * b, m.b * a + m.d * b, m.a * c + m.c * d, m.b * c + m.d * d]; }
    }
    return Math.sqrt(Math.abs(a * d - b * c));
  };
  const blurOf = e => { let px = 0; for (let p = e; p && p !== root; p = p.parentElement) { const m = /blur\(([\d.]+)px\)/.exec(getComputedStyle(p).filter || ""); if (m) px = Math.max(px, parseFloat(m[1])); } return px; };
  const painted = cs => { const bg = rgba(cs.backgroundColor); return (bg && bg[3] >= 0.6) || cs.backgroundImage !== "none"; };
  for (const sc of root.querySelectorAll("[data-scene]")) {
    const sid = sc.dataset.scene;
    const slot = sc.querySelector("[data-slot]");
    if (slot && !(sid in out.slots)) out.slots[sid] = rr(slot.getBoundingClientRect());
    if (itemsFor.has(sid)) {
      let its = [...sc.querySelectorAll("[data-item]")];
      if (!its.length) its = [...sc.querySelectorAll("img,svg,canvas")];
      out.items[sid] = its.filter(e => effOp(e) >= 0.02).map(e => ({ rect: rr(e.getBoundingClientRect()), op: r3(effOp(e)), blur: blurOf(e) }));
    }
    const groups = new Map(), tw = document.createTreeWalker(sc, NodeFilter.SHOW_TEXT);
    for (let t = tw.nextNode(); t; t = tw.nextNode()) {
      const pe = t.parentElement;
      if (!t.nodeValue.trim() || !pe || pe.closest("svg")) continue;
      if (!groups.has(pe)) groups.set(pe, []);
      groups.get(pe).push(t);
    }
    for (const [pe, nodes] of groups) {
      const cs = getComputedStyle(pe), op = effOp(pe);
      if (op < 0.02) continue;
      const fill = rgba(cs.webkitTextFillColor) || rgba(cs.color) || [0, 0, 0, 1];
      if (fill[3] * op < 0.02) continue;
      const boxes = [], gaps = []; // glyph boxes; inter-word spaces (they count as characters per line)
      for (const t of nodes) {
        const s = t.nodeValue;
        for (let i = 0; i < s.length && boxes.length < 600; i++) {
          const wide = s.codePointAt(i) > 0xFFFF;
          const r = document.createRange(); r.setStart(t, i); r.setEnd(t, i + (wide ? 2 : 1));
          const b = r.getBoundingClientRect();
          if (b.width >= 0.3 && b.height >= 0.3) (s[i].trim() ? boxes : gaps).push([b.left, b.top, b.right, b.bottom]);
          if (wide) i++;
        }
      }
      if (!boxes.length) continue;
      const x0 = Math.min(...boxes.map(b => b[0])), y0 = Math.min(...boxes.map(b => b[1]));
      const x1 = Math.max(...boxes.map(b => b[2])), y1 = Math.max(...boxes.map(b => b[3]));
      const lines = [];
      for (const b of boxes) { const cy = (b[1] + b[3]) / 2, hh = (b[3] - b[1]) / 2; const L = lines.find(l => Math.abs(l.cy - cy) < hh); if (L) { L.n++; L.x0 = Math.min(L.x0, b[0]); L.x1 = Math.max(L.x1, b[2]); } else lines.push({ cy, hh, n: 1, x0: b[0], x1: b[2] }); }
      for (const b of gaps) { const cy = (b[1] + b[3]) / 2, L = lines.find(l => Math.abs(l.cy - cy) < l.hh && b[0] > l.x0 && b[2] < l.x1); if (L) L.n++; }
      const scale = scaleOf(pe), css = parseFloat(cs.fontSize);
      if (x1 <= 0 || y1 <= 0 || x0 >= W || y0 >= H) continue; // wholly off-frame (e.g. a canvas-camera world beyond the view): not on screen
      // character boxes are em boxes (ascent + descent), not ink: allow the empty bearing / ascender space before calling it cut
      const tx = Math.max(1, 0.06 * css * scale), ty = Math.max(1, 0.22 * css * scale);
      let clip = null;
      if (pe.clientWidth > 0 && pe.scrollWidth > pe.clientWidth + 1 && (cs.overflowX !== "visible" || painted(cs))) clip = "text wider than its box";
      for (let p = pe; p && p !== sc && !clip; p = p.parentElement) {
        const ps = getComputedStyle(p);
        if (ps.overflowX !== "visible" || ps.overflowY !== "visible") {
          const r = p.getBoundingClientRect();
          if (x0 < r.left - tx || x1 > r.right + tx || y0 < r.top - ty || y1 > r.bottom + ty) clip = "cut by an overflow-hidden box";
        }
      }
      if (!clip && !sc.closest("[data-ccam]") && (x0 < -tx || y0 < -ty || x1 > W + tx || y1 > H + ty)) clip = "outside the frame edge"; // (a canvas-camera push crops world layers at the frame edge by design)
      let box = null;
      for (let p = pe; p && p !== sc; p = p.parentElement) { const ps = getComputedStyle(p); if (painted(ps)) { box = { colour: rgba(ps.backgroundColor), image: ps.backgroundImage !== "none", rect: rr(p.getBoundingClientRect()) }; break; } }
      const shadows = (String(cs.textShadow || "").match(RGBA_RE) || []).map(rgba);
      const tcEl = pe.closest("[data-tc]"), redEl = pe.closest("[data-redundant]");
      const rec = {
        scene: sid, text: nodes.map(t => t.nodeValue).join(" ").replace(/\s+/g, " ").trim().slice(0, 120),
        size: r1(css * scale), css_size: css, scale: r3(scale), weight: parseInt(cs.fontWeight, 10) || 400,
        colour: fill, opacity: r3(op), stroke: r1(parseFloat(cs.webkitTextStrokeWidth || "0") * scale), stroke_colour: rgba(cs.webkitTextStrokeColor),
        shadows, rect: [x0, y0, x1, y1].map(r1), lines: lines.length, max_chars_line: Math.max(...lines.map(l => l.n)),
        clipped: clip, box, tc: tcEl && sc.contains(tcEl) ? tcEl.dataset.tc : null, redundant: !!(redEl && sc.contains(redEl)),
      };
      if (chars.has(sid)) rec.chars = boxes.map(b => b.map(r1));
      out.texts.push(rec);
    }
  }
  return out;
}
const L_BOX = new Proxy({}, { get: (_, id) => (LAYERS.find(l => l.id === id) || {}).box });

/* ---------------------------------------------------------------- init */
function loadScript(src) {
  return new Promise((res, rej) => {
    const s = document.createElement("script"); s.src = src;
    const onErr = ev => { if (ev.filename && ev.filename.indexOf(src) < 0) return; VEOS.errors.push(`${src.split("/").pop()}: ${ev.message} (line ${ev.lineno})`); };
    window.addEventListener("error", onErr);
    s.onload = () => { window.removeEventListener("error", onErr); res(); };
    s.onerror = () => { window.removeEventListener("error", onErr); rej(new Error("failed to load " + src)); };
    document.head.appendChild(s);
  });
}

async function boot() {
  const q = new URLSearchParams(location.search), bu = q.get("bundle");
  if (!bu) throw new Error("player.html needs ?bundle=<file URL of work/render/bundle.js>");
  await loadScript(bu);
  B = window.VEOS_BUNDLE; T = B.tokens; TL = B.timeline;
  for (const c of B.scenes || []) await loadScript(c);
  VEOS.resolveScenes(); // e.g. fx.shatter binds the scene under its box (and ends it on the break frame)
  window.VEOS_SCENES_META = VEOS.sceneMeta(); window.VEOS_REG_ERRORS = VEOS.errors.slice();
  if (q.get("meta")) { window.READY = true; return; } // scenes-meta: registration only, no fonts / frames
  if (VEOS.errors.length) throw new Error("scenes.js problems:\n" + VEOS.errors.join("\n"));
  MEASURE = false;
  const mo = T.motion || {};
  EO = bez(...(mo.ease_entry || [0.22, 1, 0.36, 1])); EI = bez(...(mo.ease_exit || [0.64, 0, 0.78, 0])); EIO = bez(...(mo.ease_in_out || [0.65, 0, 0.35, 1])); EL = bez(...(mo.elastic || [0.34, 1.56, 0.64, 1]));
  FRAMES_URL = B.frames_url; ASSETS = B.assets || {}; VIDEOS = B.videos || {}; WORDS = B.words || [];
  FOOTAGE = B.footage !== false; // a voice-over reel has no footage frames: the stage stays hidden throughout
  NF = (TL.meta && TL.meta.frames) || B.frames || (B.face && B.face.frames) || 1;
  const root = document.getElementById("root"); root.style.width = W + "px"; root.style.height = H + "px";
  // stage / world / camera / layers
  const sk = (TL.stage && TL.stage.length ? TL.stage.slice() : [{ t: 0, layout: "full" }]).sort((a, b) => a.t - b.t);
  if (secF(sk[0].t) > 0) sk.unshift({ t: 0, layout: "full" });
  if (!FOOTAGE) sk.splice(0, sk.length, { t: 0, layout: "hidden" });
  // stage: engine layouts or tokens.layouts ids (layouts.js resolves params, default morphs and frames)
  SOURCES = B.sources || {};
  LENV = { face: (src, n) => (src === "footage" ? faceSm(n) : srcFace(src, n)), size: srcSize, col,
    framing: () => (FOOTAGE && B.framing && B.framing.ranges) || null }; // window framing (layouts.js winFraming)
  let prevSpec = null;
  STAGE = sk.map((s, i) => {
    let spec; try { spec = LAY.resolve(s, T); } catch (e) { throw new Error(`timeline.stage[${i}] (t ${s.t}): ${e.message}`); }
    const via = s.via || (i === 0 ? "cut" : LAY.defaultVia(prevSpec, spec) || DEFAULT_VIA[spec.engine] || "cut");
    const sm = T.stage_morphs || {}, d = s.dur != null ? s.dur : (sm[via] != null ? sm[via] : (LAY.MORPH_FRAMES[via] != null ? LAY.MORPH_FRAMES[via] : 7));
    const auto = i > 0 && s.dur == null && sm[via] == null && LAY.MORPH_FRAMES[via] != null ? (s.via ? "frames" : "via") : null; // sized after prepFaces (G3-safe travel)
    prevSpec = spec;
    return { f: secF(s.t), offset: s.offset, layout: spec.engine, id: spec.id, spec, via, ease: s.ease, d: i === 0 ? 0 : d, auto, ov: isNum(s.overshoot) ? cl(s.overshoot, 0, 0.3) : null };
  });
  // worlds: tokens.worlds (+ the v1 studio / canvas / data mapping), timeline.world[] with optional cross-fades
  WORLDS = WLD.create({ T, col, hexA, asset: id => (ASSETS[id] ? ASSETS[id].url : ""), noiseUrl: WLD.noiseUrl });
  WSCHED = WLD.schedule(TL, FPS, WORLDS.dflt);
  for (const w of WSCHED) if (!WORLDS.has(w.world)) throw new Error(`timeline.world: unknown world '${w.world}' (known: ${WORLDS.ids.join(", ")})`);
  CAMNODES = {}; // camera v2 origins: scene nodes + timeline.canvas_nodes, by centre
  for (const s of SCENES) for (const q of s.nodes || []) CAMNODES[String(q.id)] = { x: q.x + q.w / 2, y: q.y + q.h / 2 };
  for (const [k, q] of Object.entries(TL.canvas_nodes || {})) if (q && isNum(q.x) && isNum(q.y)) CAMNODES[k] = { x: q.x + (q.w || 0) / 2, y: q.y + (q.h || 0) / 2 };
  CAM = (TL.camera || []).map((c, i) => ({ f: secF(c.t), preset: c.preset, p: c.crop != null ? Object.assign({ crop: c.crop }, c.p) : c.p, idx: i })).sort((a, b) => a.f - b.f);
  for (const ev of CAM) { const m = camCheck(ev); if (m) throw new Error(`timeline.camera[${ev.idx}] (${ev.preset || "crop"}): ${m}`); }
  LAYERS = SCENES.map((d, i) => ({ id: String(d.id), fin: secF(d.t_in), fout: Math.max(secF(d.t_out), secF(d.t_in) + 1), z: d.z, behind: !!d.behind, follow: !!d.follow_footage, anchor: d.anchor && typeof d.anchor === "object" ? d.anchor : null, render: d.render, in: d.in, out: d.out, box: d.box, order: i,
    k: CAMLIB && !(d.anchor && typeof d.anchor === "object") && !(d.follow_footage && !d.behind) ? CAMLIB.parallaxOf(d) : 0, gset: d.grade !== undefined, gspec: null,
    inF: d.in_frames, outF: d.out_frames, stepF: d.step_frames || 0, stepFps: d.step_fps || 0, smear: !!d.smear, // fx-helpers
    smearPx: smearCap(d, T), inFade: inFadeOf(d) })); // fix-visual
  // E-16 grades: normalised once (unknown ids fail the boot with the place they come from)
  if (GRD) {
    const nn = (x, where) => { try { return GRD.norm(x, T); } catch (e) { throw new Error(`${where}: ${e.message}`); } };
    const G0 = T.grades || {};
    GR = { footage: nn(G0.footage, "tokens.grades.footage"), theme: nn(T.theme && T.theme.grade, `theme ${(T.theme && T.theme.id) || ""} grade`),
      reelSet: Object.prototype.hasOwnProperty.call(TL, "grade"), reel: nn(TL.grade, "timeline.grade"), worlds: {}, events: [] };
    for (const id of WORLDS.ids) { // a world's grade (null = not set; "off" = this world shows the footage ungraded)
      const gv = WORLDS.defs[id] && WORLDS.defs[id].grade;
      if (gv !== undefined && gv !== null) GR.worlds[id] = nn(gv, `tokens.worlds.${id}.grade`);
    }
    try { GR.events = GRD.compile(TL, T, FPS); } catch (e) { throw new Error(e.message); }
    for (const l of LAYERS) if (l.gset) l.gspec = nn(SCENES[l.order].grade, `scene ${l.id} grade`);
  }
  // footage blur, built-in transitions, grade blur pulses, end fade (transitions.js); null = none (the v2 frame path)
  if (TRX) {
    try { TRC = TRX.compile(TL, T, FPS, { EO, EI, EIO }); } catch (e) { throw new Error(e.message); }
    TRC.lastFrame = NF - 1;
    if (!TRC.trs.length && !TRC.blurs.length && !TRC.end && !GR.events.some(e => e.blur > 0)) TRC = null;
  }
  FRAMING = FOOTAGE && B.framing && isNum(B.framing.s) ? B.framing : null;
  TRACKS = B.tracks || {}; // Package E: plan/tracks/*.json (veos track), compacted by the bundle
  for (const l of LAYERS) if (l.anchor && !TRACKS[l.anchor.track]) throw new Error(`scene ${l.id}: anchor.track '${l.anchor.track}' is not in plan/tracks (known: ${Object.keys(TRACKS).join(", ") || "none"}; run veos track, then veos bundle)`);
  CC = CAMLIB && (TL.canvas_camera || []).length ? CAMLIB.compile(TL, SCENES) : null;
  Z8 = LAYERS.filter(l => l.z === 8).map(l => [l.fin, l.fout]);
  HIDE = ((TL.captions && TL.captions.hide) || []).map(h => [secF(h[0]), secF(h[1])]);
  prepFaces(); buildCards(); FACE_REF = faceRefInit();
  for (let i = 1; i < STAGE.length; i++) if (STAGE[i].auto) { const a = STAGE[i - 1], c = STAGE[i]; [c.via, c.d] = LAY.autoFrames(geom(a.layout, c.f, a), geom(c.layout, c.f, c), c.via, { EL, EIO, EO, EI, BO }, c.ease, { keepVia: c.auto === "frames" }); }
  // E-05 caption engine (renderer/captions.js) replaces the built-in auto-subtitles when the bundle carries captions
  const CAPS = window.VEOS_CAPTIONS, capLoad = CAPS ? CAPS.init(B, { T, TL, W, H, FPS, HIDE, Z8, scenes: SCENES, fam, col, measure }) : null;
  // fonts
  const loads = capLoad ? [capLoad] : [];
  for (const slot of Object.keys(T.fonts)) for (const f of T.fonts[slot].files || []) {
    const ff = new FontFace(T.fonts[slot].family, `url("${f.src}")`, { weight: f.weight, style: f.style });
    loads.push(ff.load().then(x => document.fonts.add(x)));
  }
  // every other bundled family the tokens (tokens.fonts_extra) or the scenes (bundle.fonts_extra) name: never a fallback face
  const FX = Object.assign({}, T.fonts_extra || {}, B.fonts_extra || {});
  for (const famX of Object.keys(FX)) for (const f of FX[famX] || []) {
    const ff = new FontFace(famX, `url("${f.src}")`, { weight: f.weight, style: f.style });
    loads.push(ff.load().then(x => document.fonts.add(x)).catch(e => VEOS.errors.push(`font ${famX}: ${e && e.message || e}`)));
  }
  await Promise.all(loads);
  for (const famX of Object.keys(FX)) await document.fonts.load(`800 40px '${famX}'`, "Aa1").catch(() => {});
  // assets
  await Promise.all(Object.values(ASSETS).map(a => { const im = new Image(); im.src = a.url; a._im = im; return im.decode().catch(() => {}); }));
  // glyph / emoji warm-up in every slot
  const GL = "Aa1₹€$£✓✕→–—…🤢🔥💀🎁🚀✅", wu = mk("position:absolute;left:0;top:0;opacity:0.01;pointer-events:none");
  for (const slot of Object.keys(T.fonts)) { if (slot === "emoji") continue; wu.insertAdjacentHTML("beforeend", `<div style="font:800 40px ${fam(slot)}">${GL}</div><div style="font:italic 400 40px ${fam(slot)}">${GL}</div>`); }
  root.appendChild(wu);
  for (const slot of Object.keys(T.fonts)) if (slot !== "emoji") await document.fonts.load(`800 40px '${T.fonts[slot].family}'`, GL).catch(() => {});
  await document.fonts.load("400 40px 'Noto Color Emoji'", GL).catch(() => {});
  await document.fonts.ready;
  await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r))); await new Promise(r => setTimeout(r, 300));
  root.replaceChildren();
  window.renderFrame = renderFrameImpl;
  window.measureFrame = async n => { MEASURE = true; try { await renderFrameImpl(n); return measureDOM(); } finally { MEASURE = false; } };
  window.measureText = async (n, o) => { MEASURE = true; PIX = !!(o && o.pixels); try { await renderFrameImpl(n); return textDOM(o || {}); } finally { MEASURE = false; PIX = false; } };
  window.READY = true;
}
VEOS.boot = () => boot().catch(e => { window.VEOS_BOOT_ERROR = String(e && e.stack || e); console.error(window.VEOS_BOOT_ERROR); });
VEOS.cards = () => CARDS;
VEOS.layout = n => layoutInfo(stageAt(cl(Math.round(n), 0, Math.max(0, NF - 1)))); // resolved layout rects at frame n (captions, tools)
})();
