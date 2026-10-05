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
const PRESET_NAMES = ["settle", "pop", "squash", "rise", "drop", "blur", "stamp", "slide-l", "slide-r", "rocket", "none"];
const SCENES = [];
const VEOS = window.VEOS = { scenes: SCENES, errors: [] };
const isNum = v => typeof v === "number" && isFinite(v);
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
  SCENES.push(d); return d;
};
VEOS.sceneMeta = () => SCENES.map(s => { const o = {}; for (const k of Object.keys(s)) if (typeof s[k] !== "function") o[k] = s[k]; return o; });

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
/* combine in/out into a transform description; null = not visible */
function presetState(inName, outName, k, kRemain, inF, outF) {
  let o = ID();
  if (inName !== "none" && inF > 0 && k < inF) o = presetIn(inName, cl((k + 0.5) / inF));
  if (outName !== "none" && outF > 0 && kRemain <= outF) {
    const q = presetOut(outName, cl((outF - kRemain + 0.5) / outF));
    o = { op: o.op * q.op, sx: o.sx * q.sx, sy: o.sy * q.sy, dx: o.dx + q.dx, dy: o.dy + q.dy, rot: o.rot + q.rot, bl: o.bl + q.bl, vb: o.vb + q.vb };
  }
  return o;
}

/* ---------------------------------------------------------------- per-frame state */
let B, T, TL, WORDS = [], FACE_RAW = [], FACE_SM = [], NF = 0;
let MEASURE = false, STAGE = [], WORLD = [], CAM = [], LAYERS = [], CARDS = [], HIDE = [], Z8 = [], BANNER_Z = 10;
let FRAMES_URL = "", ASSETS = {}, VIDEOS = {}, VPEND = [], IMG = new Map(), CANVASES = [], cvUsed = 0, VBS = [];

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

/* ---------------------------------------------------------------- stage geometry */
function geom(name, n, ev) {
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
    case "low": { // full-frame footage lowered by `offset` px; the revealed top shows a blurred backdrop
      g.off = ev && ev.offset != null ? ev.offset : 380; g.ay = F.cy + g.off; break;
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
  return g;
}
function lerpGeom(a, b, p) {
  const o = {};
  for (const k of ["x", "y", "w", "h", "s", "ax", "ay", "ring", "sh", "soft", "op", "Fx", "Fy", "off"]) o[k] = lerp(a[k], b[k], p);
  o.r = a.r.map((v, i) => Math.max(0, lerp(v, b.r[i], p)));
  o.w = Math.max(0, o.w); o.h = Math.max(0, o.h); o.op = cl(o.op); o.ring = Math.max(0, o.ring); o.sh = Math.max(0, o.sh);
  return o;
}
const DEFAULT_VIA = { low: "cut", full: "pop-back", panel: "panel-drop", inset: "panel-drop", "slide-aside": "slide-aside", bubble: "bubble-shrink", hidden: "cut" };
function stageAt(n) {
  let i = 0; for (let k = 0; k < STAGE.length; k++) if (STAGE[k].f <= n) i = k;
  const cur = STAGE[i], prev = STAGE[i - 1];
  const res = { name: cur.layout, morph: null, p: 1, from: prev ? prev.layout : cur.layout };
  if (prev && cur.d > 0 && n < cur.f + cur.d) {
    const q = (n - cur.f + 1) / (cur.d + 1);
    const e = cur.via === "bubble-shrink" || cur.via === "bubble-grow" || cur.via === "pop-back" ? EL(q) : EIO(q);
    res.morph = cur.via; res.q = q; res.g = lerpGeom(geom(prev.layout, n, prev), geom(cur.layout, n, cur), e);
    return res;
  }
  res.g = geom(cur.layout, n, cur);
  return res;
}
function lastStageF(n) { let f = 0; for (const s of STAGE) if (s.f <= n) f = s.f; return f; }

/* ---------------------------------------------------------------- camera */
function camTarget(ev, prev, kEnd, boundaryF) {
  const P = (T.camera_presets || {})[ev.preset] || {}, p = ev.p || {};
  let frames = p.frames != null ? p.frames : P.frames, toS, fromS, toR = 0;
  if (frames === "beat") frames = cl(boundaryF - ev.f, 15, 120);
  else if (Array.isArray(frames)) frames = Math.round((frames[0] + frames[1]) / 2);
  frames = frames || 4;
  const sc = P.scale || [1, 1];
  fromS = sc[0] === 1 ? prev.s : sc[0]; toS = p.scale != null ? p.scale : sc[1];
  if (P.rotate != null) toR = P.rotate * (ev.preset === "crash-zoom" ? (HASH(ev.idx, 3) > 0.5 ? 1 : -1) : 1);
  if (p.rotate != null) toR = p.rotate;
  return { frames, fromS, toS, toR, hold: p.hold != null ? p.hold : (P.hold_frames ? Math.round((P.hold_frames[0] + P.hold_frames[1]) / 2) : null) };
}
function camEval(ev, prev, k, boundaryF) {
  if (ev.preset === "reset") { const e = EO(cl(k / 4)); return { s: lerp(prev.s, 1, e), r: lerp(prev.r, 0, e) }; }
  if (ev.preset === "shake") return { s: prev.s, r: prev.r };
  const t = camTarget(ev, prev, 0, boundaryF), q = cl(k / t.frames);
  if (ev.preset === "zoom-through") { if (k >= t.frames) return { s: 1, r: 0 }; return { s: lerp(prev.s, t.toS, EI(q)), r: prev.r }; }
  const e = ev.preset === "push-drift" ? q : EO(q);
  let s = lerp(t.fromS, t.toS, e), r = lerp(prev.r, t.toR, e);
  if (t.hold != null && k > t.frames + t.hold) { const b = EO(cl((k - t.frames - t.hold) / 4)); s = lerp(t.toS, 1, b); r = lerp(t.toR, 0, b); }
  return { s, r };
}
function cameraAt(n) {
  const f0 = lastStageF(n);
  const evs = CAM.filter(e => e.f >= f0 && e.f <= n);
  const main = evs.filter(e => e.preset !== "shake");
  let st = { s: 1, r: 0 }, vb = 0;
  for (let i = 0; i < main.length; i++) {
    const ev = main[i], nextF = i + 1 < main.length ? main[i + 1].f : Infinity;
    let bF = nextF; for (const s of STAGE) if (s.f > ev.f && s.f < bF) bF = s.f;
    const last = i === main.length - 1, k = last ? n - ev.f : Infinity;
    const next = camEval(ev, st, last ? k : 1e5, bF);
    if (last) { const before = camEval(ev, st, k - 1, bF); vb = cl(Math.abs(next.s - before.s) * 70, 0, 22); }
    st = next;
  }
  let shx = 0, shy = 0, bump = 1;
  for (const ev of evs) {
    if (ev.preset !== "shake") continue;
    const P = (T.camera_presets || {}).shake || {}, p = ev.p || {}, fr = p.frames || P.frames || 6, amp = p.amp != null ? p.amp : (P.amp || 10), k = n - ev.f;
    if (k >= 0 && k < fr) { const d = 1 - k / fr; shx += amp * d * (HASH(n + ev.idx * 7, 1) * 2 - 1); shy += amp * d * (HASH(n + ev.idx * 7, 2) * 2 - 1); bump *= 1 + ((p.bump || P.bump || 1.03) - 1) * d; vb = Math.max(vb, amp * d * 0.8); }
  }
  return { s: st.s * bump, r: st.r, shx, shy, vb };
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
    ws.push({ txt, s: w.s, e: w.e });
  }
  const per = (ST.words_per_card && ST.words_per_card[1]) || 3, cards = [];
  let i = 0;
  while (i < ws.length) {
    let j = i + 1;
    while (j < ws.length && j - i < per && ws[j].s - ws[j - 1].e <= 0.25) j++;
    if (j - i === per && j < ws.length && ws.length - j === 1 && ws[j].s - ws[j - 1].e <= 0.25) j--;
    cards.push({ f0: Math.max(0, secF(ws[i].s) - lead), last: ws[j - 1].e, text: ws.slice(i, j).map(x => x.txt).join(" "), s: ws[i].s });
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
  const ST = T.type.subtitle || {}, size0 = (Array.isArray(ST.size) ? (ST.size[0] + ST.size[1]) / 2 : ST.size) || 58;
  const font = `${ST.weight || 800} ${size0}px ${fam(ST.slot || "body")}`;
  const w0 = measure(card.text, font), size = w0 > maxW ? Math.floor(size0 * maxW / w0) : size0;
  const onLight = st.name !== "full" && st.name !== "low" && world === "canvas";
  const c = onLight ? col("ink") : col("paper");
  const sh = onLight ? "none" : "0 3px 14px rgba(0,0,0,.55),0 1px 3px rgba(0,0,0,.45)";
  return `<div style="position:absolute;left:${r2(cx - maxW / 2)}px;width:${maxW}px;top:${r2(cy)}px;transform:translateY(-50%);text-align:center;white-space:nowrap;font:${ST.weight || 800} ${size}px/1.1 ${fam(ST.slot || "body")};color:${c};text-shadow:${sh}">${esc(card.text)}</div>`;
}
const esc = s => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;");

/* ---------------------------------------------------------------- worlds */
let CANVAS_GRID = "";
function worldHTML(name, n, st) {
  const t = n / FPS, L = T.layout;
  if (name === "canvas") {
    if (!CANVAS_GRID) {
      const g = L.canvas_grid || 141; let ln = "";
      for (let x = g; x < W; x += g) ln += `<line x1="${x}" y1="0" x2="${x}" y2="${H}"/>`;
      for (let y = g; y < H; y += g) ln += `<line x1="0" y1="${y}" x2="${W}" y2="${y}"/>`;
      CANVAS_GRID = `<div style="position:absolute;inset:0;background:${col("canvas")}"></div><svg width="${W}" height="${H}" style="position:absolute;left:0;top:0" stroke="${col("grid")}" stroke-width="2" stroke-dasharray="14 10" fill="none">${ln}</svg>`;
    }
    return CANVAS_GRID;
  }
  if (name === "data") {
    const p = L.night_grid || 60, gx = 540 + Math.sin(t * 0.7) * 20, gy = 560 + Math.cos(t * 0.5) * 20;
    return `<div style="position:absolute;inset:0;background:${col("night")}"></div>
<div style="position:absolute;inset:0;background-image:radial-gradient(circle,${hexA("data", 0.10)} 2.2px,transparent 2.8px);background-size:${p}px ${p}px;background-position:${p / 2}px ${p / 2}px"></div>
<div style="position:absolute;inset:0;background:radial-gradient(circle at ${r2(gx)}px ${r2(gy)}px,${hexA("data", 0.14)} 0,${hexA("data", 0)} 350px)"></div>`;
  }
  // studio: footage itself (full) or a dimmed blurred copy behind a smaller stage window
  return `<div style="position:absolute;inset:0;background:${col("ink")}"></div>` + (st ? `<img data-foot="1" src="${st.fUrl}" style="position:absolute;left:-60px;top:-60px;width:${W + 120}px;height:${H + 120}px;filter:blur(28px) brightness(.45)">` : "");
}

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
  if (!MEASURE) VPEND.push(preload(url)); // decoded before the frame is "ready", like footage
  return url;
}

async function renderFrameImpl(n) {
  n = cl(Math.round(n), 0, NF - 1);
  const t = n / FPS;
  VBS = []; cvUsed = 0; VPEND = [];
  const st = stageAt(n), g = st.g;
  const world = (() => { let w = "studio"; for (const k of WORLD) if (k.f <= n) w = k.world; return w; })();
  const cam = cameraAt(n), Fs = faceSm(n), Fr = faceRaw(n);
  const active = LAYERS.filter(l => n >= l.fin && n < l.fout);
  const behind = active.filter(l => l.behind);
  const showWin = g.op > 0.01 && g.w > 1 && g.h > 1;
  const needCut = showWin && behind.length > 0;
  const urls = { f: fUrl(n), c: cUrl(n) };
  if (!MEASURE) { const pl = [preload(urls.f)]; if (needCut) pl.push(preload(urls.c)); await Promise.all(pl); } // measure only needs layout, not pixels

  // footage -> screen transform (+ banner clamp)
  const S = g.s * cam.s, rad = cam.r * Math.PI / 180, cs = Math.cos(rad), sn = Math.sin(rad);
  let tx = g.ax + cam.shx, ty = g.ay + cam.shy;
  const toScr = (px, py) => { const dx = (px - g.Fx) * S, dy = (py - g.Fy) * S; return [tx + dx * cs - dy * sn, ty + dx * sn + dy * cs]; };
  const rectScr = b => { const pts = [toScr(b[0], b[1]), toScr(b[0] + b[2], b[1]), toScr(b[0] + b[2], b[1] + b[3]), toScr(b[0], b[1] + b[3])]; const xs = pts.map(p => p[0]), ys = pts.map(p => p[1]); const x = Math.min(...xs), y = Math.min(...ys); return { x, y, w: Math.max(...xs) - x, h: Math.max(...ys) - y }; };
  if (showWin && st.name === "full" && !st.morph && (cam.s !== 1 || cam.r !== 0 || cam.shx || cam.shy) && active.some(l => l.z === BANNER_Z)) {
    // the camera may not push the face under the banner: shift the footage down (never past the footage top edge)
    const lay = T.layout, limit = (lay.banner_top || 150) + 2 * 78 * 1.02 + 56 + (lay.face_clearance || 40);
    const natTop = g.ay + (Fr[1] - g.Fy) * g.s, cur = rectScr(Fr).y, need = Math.min(natTop, limit);
    if (cur < need) ty += Math.min(need - cur, Math.max(0, -(ty - S * g.Fy)));
  }
  const mA = cs * S, mB = sn * S, mC = -sn * S, mD = cs * S;
  const mE = tx - (mA * g.Fx + mC * g.Fy), mF = ty - (mB * g.Fx + mD * g.Fy);
  const exact = S === 1 && cam.r === 0;
  const faceOut = showWin ? (() => { const r = rectScr(Fr); return { x: r.x, y: r.y, w: r.w, h: r.h, cx: r.x + r.w / 2, cy: r.y + r.h / 2 }; })() : null;

  // shared ctx
  const base = {
    n, t, fps: FPS, W, H, tokens: T, safe: T.layout.safe, face: () => faceOut,
    ease, lerp, clamp: cl, measure, asset: id => (ASSETS[id] ? ASSETS[id].url : ""), videoFrame, word: i => WORDS[i] || null,
    wordsBetween: (a, b) => WORDS.filter(w => w.s >= a && w.s < b), html: s => s, blur: px => { VBS.push(px); return `url(#vb${VBS.length - 1})`; },
    fam, col, hexA, esc, stageName: st.name, world,
  };
  base.V = (lt, inDur, outAt, o = {}) => {
    const inF = secF(inDur), outF = o.dout != null ? o.dout : (OUT_F[o.out] != null ? OUT_F[o.out] : 5), k = Math.round(lt * FPS);
    const kRem = outAt == null ? 1e9 : Math.round((outAt - lt) * FPS) + outF;
    if (lt < -1e-6) return null; if (outAt != null && lt >= outAt + outF / FPS) return null;
    const s = presetState(o.in || "blur", o.out || "blur", k, kRem, inF || IN_F[o.in || "blur"], outF);
    return styleOf(s, "50% 50%", o.op);
  };
  function styleOf(s, origin, op) {
    const extra = s.vb > 0.4 ? vbFilter(s.vb) : (s.bl > 0.05 ? `filter:blur(${r2(s.bl)}px);` : "");
    return `opacity:${r2(s.op * (op == null ? 1 : op))};transform-origin:${origin};transform:translate(${r2(s.dx)}px,${r2(s.dy)}px) rotate(${r2(s.rot)}deg) scale(${s.sx.toFixed(4)},${s.sy.toFixed(4)});${extra}`;
  }

  const renderLayer = L => {
    const lt = (n - L.fin) / FPS, dur = (L.fout - L.fin) / FPS;
    const ctx = layerCtx(base, L, n);
    let html;
    try { html = L.render(ctx, lt, dur); } catch (e) { VEOS.errors.push(`${L.id} @${n}: ${e && e.stack || e}`); throw new Error(`scene ${L.id} failed at frame ${n}: ${e && e.message}`); }
    const box = L.box || { x: 0, y: 0, w: W, h: H };
    const inN = L.in || "settle", outN = L.out || "none";
    const s = MEASURE ? ID() : presetState(inN, outN, n - L.fin, L.fout - n, IN_F[inN] || 0, OUT_F[outN] != null ? OUT_F[outN] : 5);
    const org = `${r2(box.x + box.w / 2)}px ${r2(box.y + box.h / 2)}px`;
    const el = mk(`position:absolute;left:0;top:0;width:${W}px;height:${H}px;${styleOf(s, org)}`, typeof html === "string" ? html : "");
    el.dataset.scene = L.id; if (ctx._cv) { el.dataset.canvas = "1"; el.appendChild(ctx._cv); }
    return el;
  };

  const root = document.getElementById("root"), frag = document.createDocumentFragment();
  // world
  const w = mk(`position:absolute;inset:0;overflow:hidden`, worldHTML(world, n, showWin && !(g.x <= 0 && g.y <= 0 && g.x + g.w >= W && g.y + g.h >= H) ? { fUrl: urls.f } : null));
  frag.appendChild(w);
  const below = active.filter(l => !l.behind && l.z <= 3), above = active.filter(l => !l.behind && l.z > 3);
  for (const l of below) frag.appendChild(renderLayer(l));
  // footage group
  if (showWin) {
    const corner = g.r.map(v => r2(v) + "px").join(" ");
    let shadow = "";
    if (g.ring > 0.3) shadow = `box-shadow:0 0 0 ${r2(g.ring)}px ${col("paper")},${r2(g.sh * 0.5)}px ${r2(g.sh)}px 0 ${r2(g.ring)}px ${col("ink")};`;
    else if (g.soft > 0.01 && world !== "studio") shadow = `box-shadow:0 -6px 30px rgba(0,0,0,${r2(0.18 * g.soft)});`;
    const win = mk(`position:absolute;left:${r2(g.x)}px;top:${r2(g.y)}px;width:${r2(g.w)}px;height:${r2(g.h)}px;border-radius:${corner};overflow:hidden;opacity:${r2(g.op)};${shadow}`);
    const mvb = st.morph && (st.morph === "panel-drop" || st.morph === "pop-back") ? 22 * Math.sin(Math.PI * cl(st.q)) : 0;
    const gvb = Math.max(cam.vb, mvb);
    const mkGrp = dy => mk(`position:absolute;left:${r2(-g.x)}px;top:${r2(-g.y)}px;width:${W}px;height:${H}px;transform-origin:0 0;transform:${exact ? `translate(${r2(mE)}px,${r2(mF - dy)}px)` : `matrix(${mA.toFixed(5)},${mB.toFixed(5)},${mC.toFixed(5)},${mD.toFixed(5)},${r2(mE)},${r2(mF - dy)})`};${vbFilter(gvb)}`);
    const imgStyle = `position:absolute;left:0;top:0;width:${W}px;height:${H}px;`;
    const off = g.off || 0;
    if (off > 0.5) { // "low" layout: blurred, darkened copy of the frame fills the revealed area
      win.insertAdjacentHTML("beforeend", `<img data-foot="1" src="${urls.f}" style="position:absolute;left:${r2(-W * 0.075 - g.x)}px;top:${r2(-H * 0.075 - g.y)}px;width:${r2(W * 1.15)}px;height:${r2(H * 1.15)}px;filter:blur(40px) brightness(.45)">`);
    }
    // depth sandwich: footage (lowered) -> behind layers (not lowered) -> cut-out (lowered)
    const grp = mkGrp(0);
    grp.insertAdjacentHTML("beforeend", `<img data-foot="1" src="${urls.f}" style="${imgStyle}">`);
    win.appendChild(grp);
    if (behind.length) { const gb = off > 0.5 ? mkGrp(off) : grp; for (const l of behind) gb.appendChild(renderLayer(l)); if (gb !== grp) win.appendChild(gb); }
    if (needCut) { const gc = off > 0.5 ? mkGrp(0) : grp; gc.insertAdjacentHTML("beforeend", `<img data-foot="1" src="${urls.c}" style="${imgStyle}">`); if (gc !== grp) win.appendChild(gc); }
    frag.appendChild(win);
  }
  const subs = subtitleHTML(n, st, world);
  const items = above.map(l => ({ z: l.z, order: l.order, l })).concat([{ z: 7, order: 1e6, sub: true }]).sort((a, b) => a.z - b.z || a.order - b.order);
  for (const it of items) { if (it.sub) { if (subs) { const sd = mk(`position:absolute;left:0;top:0;width:${W}px;height:${H}px`, subs); sd.dataset.scene = "__subtitles"; frag.appendChild(sd); } } else frag.appendChild(renderLayer(it.l)); }
  // filters
  let defs = ""; VBS.forEach((px, i) => { defs += `<filter id="vb${i}" x="-5%" y="-30%" width="110%" height="160%" color-interpolation-filters="sRGB"><feGaussianBlur stdDeviation="0 ${r2(px)}"/></filter>`; });
  const svg = mk(`position:absolute;width:0;height:0`, `<svg width="0" height="0" style="position:absolute"><defs>${defs}</defs></svg>`);
  root.replaceChildren(svg, frag);
  await Promise.all([...root.querySelectorAll("img")].filter(i => !(MEASURE && i.dataset.foot)).map(i => i.decode().catch(() => {})).concat(VPEND));
  await document.fonts.ready;
  if (!MEASURE) await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));
  return true;
}

/* ---------------------------------------------------------------- measure: union rect of each scene's painted DOM (resting position, presets neutralised) */
function measureDOM() {
  const out = {};
  for (const el of document.querySelectorAll("#root [data-scene]")) {
    const id = el.dataset.scene; let x0 = 1e9, y0 = 1e9, x1 = -1e9, y1 = -1e9, any = false;
    const add = r => { if (r.width < 0.5 || r.height < 0.5) return; any = true; x0 = Math.min(x0, r.left); y0 = Math.min(y0, r.top); x1 = Math.max(x1, r.right); y1 = Math.max(y1, r.bottom); };
    const eff = e => { let o = 1; for (let p = e; p && p !== el; p = p.parentElement) { const cs = getComputedStyle(p); if (cs.display === "none" || cs.visibility === "hidden") return 0; o *= parseFloat(cs.opacity); } return o; };
    const walk = e => {
      const cs = getComputedStyle(e);
      if (cs.display === "none") return;
      if (eff(e) < 0.02) return;
      const tag = e.tagName.toLowerCase();
      if (tag === "img" || tag === "svg" || tag === "video") { add(e.getBoundingClientRect()); return; }
      if (tag === "canvas") { if (L_BOX[id]) { const b = L_BOX[id]; add({ width: b.w, height: b.h, left: b.x, top: b.y, right: b.x + b.w, bottom: b.y + b.h }); } return; }
      const paints = (cs.backgroundColor && !/rgba\(0, 0, 0, 0\)|transparent/.test(cs.backgroundColor)) || cs.backgroundImage !== "none" || parseFloat(cs.borderTopWidth) > 0 || parseFloat(cs.borderBottomWidth) > 0 || parseFloat(cs.borderLeftWidth) > 0 || cs.boxShadow !== "none";
      if (paints && e !== el) add(e.getBoundingClientRect());
      for (const c of e.childNodes) {
        if (c.nodeType === 3 && c.nodeValue.trim()) { const r = document.createRange(); r.selectNodeContents(c); add(r.getBoundingClientRect()); }
        else if (c.nodeType === 1) walk(c);
      }
    };
    walk(el);
    const d = LAYERS.find(l => l.id === id);
    if (!any && el.dataset.canvas && d && d.box) { const b = d.box; add({ width: b.w, height: b.h, left: b.x, top: b.y, right: b.x + b.w, bottom: b.y + b.h }); }
    if (any) out[id] = [Math.round(x0 * 10) / 10, Math.round(y0 * 10) / 10, Math.round(x1 * 10) / 10, Math.round(y1 * 10) / 10];
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
  window.VEOS_SCENES_META = VEOS.sceneMeta(); window.VEOS_REG_ERRORS = VEOS.errors.slice();
  if (q.get("meta")) { window.READY = true; return; } // scenes-meta: registration only, no fonts / frames
  if (VEOS.errors.length) throw new Error("scenes.js problems:\n" + VEOS.errors.join("\n"));
  MEASURE = false;
  const mo = T.motion || {};
  EO = bez(...(mo.ease_entry || [0.22, 1, 0.36, 1])); EI = bez(...(mo.ease_exit || [0.64, 0, 0.78, 0])); EIO = bez(...(mo.ease_in_out || [0.65, 0, 0.35, 1])); EL = bez(...(mo.elastic || [0.34, 1.56, 0.64, 1]));
  FRAMES_URL = B.frames_url; ASSETS = B.assets || {}; VIDEOS = B.videos || {}; WORDS = B.words || [];
  NF = (TL.meta && TL.meta.frames) || B.frames || (B.face && B.face.frames) || 1;
  const root = document.getElementById("root"); root.style.width = W + "px"; root.style.height = H + "px";
  // stage / world / camera / layers
  const sk = (TL.stage && TL.stage.length ? TL.stage.slice() : [{ t: 0, layout: "full" }]).sort((a, b) => a.t - b.t);
  if (secF(sk[0].t) > 0) sk.unshift({ t: 0, layout: "full" });
  STAGE = sk.map((s, i) => { const via = s.via || (i === 0 ? "cut" : DEFAULT_VIA[s.layout] || "cut"); const d = s.dur != null ? s.dur : ((T.stage_morphs || {})[via] != null ? T.stage_morphs[via] : 7); return { f: secF(s.t), offset: s.offset, layout: s.layout, via, d: i === 0 ? 0 : d }; });
  WORLD = (TL.world && TL.world.length ? TL.world : [{ t: 0, world: "studio" }]).map(w => ({ f: secF(w.t), world: w.world })).sort((a, b) => a.f - b.f);
  CAM = (TL.camera || []).map((c, i) => ({ f: secF(c.t), preset: c.preset, p: c.p, idx: i })).sort((a, b) => a.f - b.f);
  LAYERS = SCENES.map((d, i) => ({ id: String(d.id), fin: secF(d.t_in), fout: Math.max(secF(d.t_out), secF(d.t_in) + 1), z: d.z, behind: !!d.behind, render: d.render, in: d.in, out: d.out, box: d.box, order: i }));
  Z8 = LAYERS.filter(l => l.z === 8).map(l => [l.fin, l.fout]);
  HIDE = ((TL.captions && TL.captions.hide) || []).map(h => [secF(h[0]), secF(h[1])]);
  prepFaces(); buildCards();
  // fonts
  const loads = [];
  for (const slot of Object.keys(T.fonts)) for (const f of T.fonts[slot].files || []) {
    const ff = new FontFace(T.fonts[slot].family, `url("${f.src}")`, { weight: f.weight, style: f.style });
    loads.push(ff.load().then(x => document.fonts.add(x)));
  }
  await Promise.all(loads);
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
  window.READY = true;
}
VEOS.boot = () => boot().catch(e => { window.VEOS_BOOT_ERROR = String(e && e.stack || e); console.error(window.VEOS_BOOT_ERROR); });
VEOS.cards = () => CARDS;
})();
