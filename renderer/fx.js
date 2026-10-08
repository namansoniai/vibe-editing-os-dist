/* Vibe Editing OS renderer: the faceless toolkit (VEOS.fx). Classic script, loaded by player.html after core.js and
   before plan/scenes.js. Building blocks for reels made from a voice-over (and useful in any reel):

     scene factories (each one registers a VEOS.scene with honest metadata: box, text, text_content, text_px,
     text_class, events, nodes):
       VEOS.fx.typeStack   kinetic type: lines that rise with a vertical blur and stack (sans / italic serif)
       VEOS.fx.diagram     nodes + edges in world px (hub, flow, list); nodes are canvas-camera targets
       VEOS.fx.card        icon / illustration card (light, dark, glass, outline, glow)
       VEOS.fx.clip        a creator clip, screen recording or image (card or full-bleed, Ken Burns, view chip)
       VEOS.fx.morphShape  one object that morphs through shapes (continuity hand-off across beats)
       VEOS.fx.ambient     backgrounds: paper dots, grid, void bloom, aurora, particles, card rain
       VEOS.fx.flash / VEOS.fx.streak / VEOS.fx.shatter   light flash (no flash limit), light streaks, shard break

     render helpers (use inside your own scenes):
       VEOS.fx.icon(name, o)  VEOS.fx.device(kind, o)  VEOS.fx.typewriter(text, lt, o)  VEOS.fx.shape(kind, o)
       VEOS.fx.typeOn(text, lt, o)  VEOS.fx.resolve(text, lt, o)  (per-glyph drop-in type-on, letter-resolve scramble)
       VEOS.fx.morph(a, b, p)  VEOS.fx.path(points)  VEOS.fx.handoff(rectA, rectB, p)  VEOS.fx.mix(c1, c2, p)
       VEOS.fx.linesFromWords(t0, t1, o)  (load time: transcript words -> typeStack lines)

   Everything is a pure function of the frame (no Math.random, Date, timers). Colours are playbook roles (or hex for
   neutrals); fonts are playbook slots. See SCENES-API.md section 10 for recipes. */
(function () {
"use strict";
const VEOS = window.VEOS;
if (!VEOS) return;
const W = 1080, H = 1920, FPS = 30;
const cl = (x, a = 0, b = 1) => (x < a ? a : x > b ? b : x);
const lerp = (a, b, p) => a + (b - a) * p;
const r2 = v => Math.round(v * 100) / 100;
const esc = s => String(s == null ? "" : s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
const backOut = (p, s = 1.70158) => { p = cl(p); const c = s + 1, q = p - 1; return 1 + c * q * q * q + s * q * q; };
const expoOut = p => (p >= 1 ? 1 : 1 - Math.pow(2, -10 * cl(p)));
const sineIO = p => 0.5 - 0.5 * Math.cos(Math.PI * cl(p));
const fx = VEOS.fx = { version: 1 };

/* colour: a playbook role, else the value itself (hex / rgba for neutrals) */
const C = (ctx, v, dflt) => { const x = v == null ? dflt : v; return (ctx.tokens.colours && ctx.tokens.colours[x]) || x; };
function hexRgb(h) { h = String(h).replace("#", ""); if (h.length === 3) h = h.split("").map(c => c + c).join(""); return [0, 2, 4].map(i => parseInt(h.slice(i, i + 2), 16) || 0); }
fx.mix = (a, b, p) => { const x = hexRgb(a), y = hexRgb(b); return "#" + x.map((v, i) => Math.round(lerp(v, y[i], cl(p))).toString(16).padStart(2, "0")).join(""); };
/* ---- text legibility. V-TYPE wants >= 4.5:1 text contrast (3:1 for display text >= 96 px). A role colour that is right as a
   fill (the orange accent) is often too light as text on paper / cream, so text goes through legible(): same hue and
   saturation, lightness lowered (or raised on dark) until the contrast holds. Colours that already pass are untouched. */
function parseCol(c) {
  c = String(c == null ? "" : c).trim(); let m;
  if (/^#([0-9a-f]{3}|[0-9a-f]{6})$/i.test(c)) return [...hexRgb(c), 1];
  if ((m = /^rgba?\(([^)]+)\)/i.exec(c))) { const v = m[1].split(",").map(parseFloat); return [v[0], v[1], v[2], v.length > 3 ? v[3] : 1]; }
  return null;
}
const hex2 = v => Math.round(cl(v, 0, 255)).toString(16).padStart(2, "0");
const toHex = q => "#" + hex2(q[0]) + hex2(q[1]) + hex2(q[2]);
function lum(q) { const f = v => { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); }; return 0.2126 * f(q[0]) + 0.7152 * f(q[1]) + 0.0722 * f(q[2]); }
const over = (fg, bg) => [0, 1, 2].map(i => fg[i] * fg[3] + bg[i] * (1 - fg[3])); // fg (with alpha) composited on an opaque bg
fx.contrast = (a, b) => { const A = parseCol(a), B = parseCol(b); if (!A || !B) return null; const x = lum(over(A, B)), y = lum(B); return (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05); };
function rgb2hsl(q) { const r = q[0] / 255, g = q[1] / 255, b = q[2] / 255, mx = Math.max(r, g, b), mn = Math.min(r, g, b), l = (mx + mn) / 2, d = mx - mn; let h = 0, s = 0;
  if (d) { s = d / (1 - Math.abs(2 * l - 1)); h = mx === r ? ((g - b) / d) % 6 : mx === g ? (b - r) / d + 2 : (r - g) / d + 4; h *= 60; if (h < 0) h += 360; } return [h, s, l]; }
function hsl2rgb(h, s, l) { const c = (1 - Math.abs(2 * l - 1)) * s, x = c * (1 - Math.abs(((h / 60) % 2) - 1)), m = l - c / 2; const [r, g, b] = h < 60 ? [c, x, 0] : h < 120 ? [x, c, 0] : h < 180 ? [0, c, x] : h < 240 ? [0, x, c] : h < 300 ? [x, 0, c] : [c, 0, x]; return [(r + m) * 255, (g + m) * 255, (b + m) * 255]; }
/* text colour fg on bg at >= min:1 (a hex / rgba string, or fg itself when it already passes or bg is unknown) */
function legible(fg, bg, min) {
  const F = parseCol(fg), B = parseCol(bg);
  if (!F || !B || B[3] < 1) return fg;
  const flat = F[3] < 1 ? over(F, B) : F, k = v => (Math.max(lum(v), lum(B)) + 0.05) / (Math.min(lum(v), lum(B)) + 0.05);
  if (k(flat) >= min) return F[3] < 1 ? toHex(flat) : fg;
  const [h, s, l0] = rgb2hsl(flat), darker = lum(B) > 0.18; // light ground: darken the text; dark ground: lighten it
  let best = flat;
  for (let i = 1; i <= 100; i++) { const l = darker ? l0 * (1 - i / 100) : l0 + (1 - l0) * i / 100; best = hsl2rgb(h, s, l); if (k(best) >= min) break; }
  return toHex(best);
}
fx.legible = legible;
const needContrast = px => (px >= 96 ? 3 : 4.5);
const SAFE = 0.35;  // margin over the floor: the measured ground carries paper dots / grid lines, which darken it a little
fx.textColour = (ctx, fg, bg, px) => legible(C(ctx, fg), bg, needContrast(px) + SAFE);
/* ambient backgrounds register here, so text scenes can ask what lies under them: bgAt(ctx, t) -> hex or null */
const AMBIENT = [];
function bgAt(ctx, t) {
  for (let i = AMBIENT.length - 1; i >= 0; i--) { const a = AMBIENT[i]; if (t >= a.t_in - 1e-6 && t < a.t_out - 1e-6) { const c = C(ctx, a.bg, a.dflt); const q = parseCol(c); return q ? toHex(q) : null; } }
  return null;
}
fx.bgAt = bgAt;
const rgba = (ctx, v, a) => { const c = C(ctx, v); if (!/^#/.test(c)) return c; const q = hexRgb(c); return `rgba(${q[0]},${q[1]},${q[2]},${a})`; };
fx.rgba = rgba;
const plain = s => String(s || "").replace(/\*\*(.+?)\*\*/g, "$1").replace(/_(.+?)_/g, "$1").replace(/~(.+?)~/g, "$1").replace(/\{(.+?)\|[\w#-]+\}/g, "$1");
fx.plain = plain;
function scene(o, d) { // register with the factory defaults, then the caller's extra fields
  const s = Object.assign({}, d, o.extra || {});
  for (const k of ["id", "t_in", "t_out", "z", "in", "out", "behind", "follow_footage", "parallax", "may_overlap_face", "overlaps", "cuts", "kind", "roles",
    "in_frames", "out_frames", "step_frames", "step_fps", "smear"]) if (o[k] !== undefined) s[k] = o[k];
  // a track anchor is an object {track, ...}; helpers like typeStack use `anchor: "top"` for text layout, which stays theirs
  if (o.anchor && typeof o.anchor === "object" && !Array.isArray(o.anchor)) s.anchor = o.anchor;
  if (o.events) s.events = [...new Set([...(s.events || []), ...o.events])].sort((a, b) => a - b);
  return VEOS.scene(s);
}
const ev = (list, t_in, t_out) => [...new Set(list.map(a => Math.round((a - t_in) * 1000) / 1000).filter(v => v > 0.02 && v < t_out - t_in - 0.02))].sort((a, b) => a - b);

/* ================================================================ icons: 48-unit line icons, drawn for VEOS (no icon font) */
const ICON = {
  check: "M10 25 L19 34 L38 14", x: "M13 13 L35 35 M35 13 L13 35", plus: "M24 9 V39 M9 24 H39", minus: "M9 24 H39",
  "arrow-right": "M7 24 H39 M29 14 L39 24 L29 34", "arrow-up": "M24 40 V9 M14 19 L24 9 L34 19", "arrow-down": "M24 8 V39 M14 29 L24 39 L34 29",
  bolt: "M27 5 L11 27 H23 L20 43 L37 19 H25 Z",
  heart: "M24 40 C8 29 4 19 10 12 C15 7 21 9 24 14 C27 9 33 7 38 12 C44 19 40 29 24 40 Z",
  clock: "M24 8 A16 16 0 1 1 23.99 8 Z M24 15 V24 L31 28",
  eye: "M4 24 C12 12 36 12 44 24 C36 36 12 36 4 24 Z M24 18 A6 6 0 1 1 23.99 18 Z",
  lock: "M12 21 H36 V40 H12 Z M16 21 V15 A8 8 0 0 1 32 15 V21 M24 28 V33",
  key: "M16 17 A7 7 0 1 1 15.99 17 Z M23 24 H42 M36 24 V31 M41 24 V29",
  file: "M13 6 H29 L37 14 V42 H13 Z M29 6 V14 H37 M18 23 H32 M18 29 H32 M18 35 H27",
  folder: "M5 13 H19 L23 18 H43 V39 H5 Z",
  terminal: "M5 9 H43 V39 H5 Z M12 19 L18 24 L12 29 M22 30 H32",
  code: "M17 14 L7 24 L17 34 M31 14 L41 24 L31 34 M27 10 L21 38",
  bulb: "M17 30 C11 26 10 19 13 14 C16 8 24 6 30 9 C37 13 38 22 32 29 C30 31 30 33 30 35 H18 C18 33 18 31 17 30 Z M19 40 H29 M21 44 H27",
  chat: "M6 10 H42 V32 H22 L13 40 V32 H6 Z", user: "M24 9 A7 7 0 1 1 23.99 9 Z M9 41 C10 31 17 27 24 27 C31 27 38 31 39 41",
  users: "M18 11 A6 6 0 1 1 17.99 11 Z M5 38 C6 30 11 26 18 26 C25 26 30 30 31 38 M32 12 A5 5 0 1 1 31.99 12 Z M33 24 C39 24 43 28 44 35",
  phone: "M14 4 H34 V44 H14 Z M21 39 H27", laptop: "M9 10 H39 V30 H9 Z M4 36 H44 L41 40 H7 Z",
  globe: "M24 6 A18 18 0 1 1 23.99 6 Z M24 6 C15 12 15 36 24 42 C33 36 33 12 24 6 M6 24 H42 M9 15 H39 M9 33 H39",
  search: "M21 9 A12 12 0 1 1 20.99 9 Z M30 30 L41 41", chart: "M8 40 H40 M13 34 V24 M21 34 V16 M29 34 V20 M37 34 V10",
  trend: "M6 36 L18 24 L26 30 L42 12 M32 12 H42 V22", target: "M24 6 A18 18 0 1 1 23.99 6 Z M24 13 A11 11 0 1 1 23.99 13 Z M24 20 A4 4 0 1 1 23.99 20 Z",
  flag: "M11 44 V6 M11 8 H35 L30 16 L35 24 H11",
  rocket: "M24 4 C33 11 35 22 31 32 H17 C13 22 15 11 24 4 Z M17 26 L10 34 H17 M31 26 L38 34 H31 M20 36 L24 44 L28 36 M24 14 A4 4 0 1 1 23.99 14 Z",
  git: "M14 6 A4 4 0 1 1 13.99 6 Z M14 34 A4 4 0 1 1 13.99 34 Z M34 14 A4 4 0 1 1 33.99 14 Z M14 14 V34 M34 22 C34 30 22 28 14 34",
  undo: "M18 12 L8 22 L18 32 M8 22 H30 C37 22 42 27 42 33 C42 39 37 43 30 43 H22",
  layers: "M24 6 L43 16 L24 26 L5 16 Z M5 24 L24 34 L43 24 M5 32 L24 42 L43 32",
  list: "M17 12 H42 M17 24 H42 M17 36 H42 M8 12 H9 M8 24 H9 M8 36 H9",
  sparkle: "M24 4 C26 16 32 22 44 24 C32 26 26 32 24 44 C22 32 16 26 4 24 C16 22 22 16 24 4 Z",
  shield: "M24 4 L40 10 V22 C40 33 33 40 24 44 C15 40 8 33 8 22 V10 Z", play: "M24 6 A18 18 0 1 1 23.99 6 Z M20 15 L33 24 L20 33 Z",
  mic: "M18 11 A6 6 0 0 1 30 11 V21 A6 6 0 0 1 18 21 Z M11 22 C11 30 17 35 24 35 C31 35 37 30 37 22 M24 35 V43 M17 43 H31",
  camera: "M5 15 H14 L18 9 H30 L34 15 H43 V39 H5 Z M24 19 A8 8 0 1 1 23.99 19 Z", mail: "M5 11 H43 V37 H5 Z M6 13 L24 27 L42 13",
  calendar: "M6 9 H42 V42 H6 Z M6 18 H42 M15 5 V13 M33 5 V13",
  link: "M20 28 L28 20 M17 21 L13 25 C9 29 9 35 13 39 C17 43 23 43 27 39 L31 35 M31 27 L35 23 C39 19 39 13 35 9 C31 5 25 5 21 9 L17 13",
  cursor: "M10 6 L38 22 L25 25 L32 40 L27 42 L20 27 L10 36 Z", home: "M6 22 L24 6 L42 22 M11 18 V42 H37 V18",
  cloud: "M14 38 C7 38 4 33 5 28 C6 23 11 21 15 22 C16 14 23 10 30 12 C36 14 39 19 38 24 C43 24 45 29 44 33 C43 36 41 38 37 38 Z",
  database: "M8 11 C8 3 40 3 40 11 C40 19 8 19 8 11 Z M8 11 V37 C8 45 40 45 40 37 V11 M8 24 C8 32 40 32 40 24",
  hourglass: "M12 5 H36 M12 43 H36 M14 5 C14 17 34 19 34 24 C34 29 14 31 14 43 M34 5 C34 17 14 19 14 24 C14 29 34 31 34 43",
  infinity: "M24 24 C18 15 7 15 7 24 C7 33 18 33 24 24 C30 15 41 15 41 24 C41 33 30 33 24 24 Z",
  coin: "M24 6 A18 18 0 1 1 23.99 6 Z M29 17 C27 14 20 14 19 18 C18 23 30 23 29 29 C28 33 21 34 18 31 M24 11 V37",
  dot: "M24 18 A6 6 0 1 1 23.99 18 Z", star: "", gear: "", brain: "",
  doc: "M10 5 H38 V43 H10 Z M15 13 H33 M15 20 H33 M15 27 H33 M15 34 H26",
  window: "M5 8 H43 V40 H5 Z M5 16 H43 M10 12 H11 M15 12 H16 M20 12 H21",
  cmd: "M18 18 V30 M30 18 V30 M18 18 H30 M18 30 H30 M18 18 C18 11 9 11 9 16 C9 21 14 18 18 18 M30 18 C30 11 39 11 39 16 C39 21 34 18 30 18 M18 30 C18 37 9 37 9 32 C9 27 14 30 18 30 M30 30 C30 37 39 37 39 32 C39 27 34 30 30 30",
  tab: "M6 14 H42 M6 14 V38 H42 V14 M30 26 H14 M20 20 L14 26 L20 32 M38 20 V32",
};
(function genIcons() {
  let st = "M"; for (let i = 0; i < 10; i++) { const a = -Math.PI / 2 + i * Math.PI / 5, r = i % 2 ? 8 : 19; st += `${r2(24 + r * Math.cos(a))} ${r2(25 + r * Math.sin(a))} ${i < 9 ? "L" : "Z"}`; }
  ICON.star = st;
  let g = ""; const T = 8; for (let i = 0; i < T * 4; i++) { const a = (i / (T * 4)) * Math.PI * 2, r = (i % 4 < 2) ? 18 : 13; g += `${i ? "L" : "M"}${r2(24 + r * Math.cos(a))} ${r2(24 + r * Math.sin(a))} `; }
  ICON.gear = g + "Z M24 18 A6 6 0 1 1 23.99 18 Z";
  ICON.brain = "M24 8 C19 4 11 7 11 13 C6 14 5 21 8 24 C5 28 7 35 12 36 C13 42 20 44 24 40 C28 44 35 42 36 36 C41 35 43 28 40 24 C43 21 42 14 37 13 C37 7 29 4 24 8 Z M24 8 V40 M17 18 C20 18 22 20 22 23 M31 30 C28 30 26 28 26 25";
})();
const FILLED = new Set(["dot"]);
fx.icons = () => Object.keys(ICON);
/* SVG markup of a line icon. o: {size, color, stroke (in 48-unit space, default 3), fill (colour for solid shapes), glow (px), opacity} */
fx.icon = function (name, o = {}) {
  const d = ICON[name] || ICON.dot, size = o.size || 96, col = o.color || "currentColor", sw = o.stroke || 3;
  const fill = o.fill || (FILLED.has(name) ? col : "none");
  const glow = o.glow ? `filter:drop-shadow(0 0 ${o.glow}px ${col});` : "";
  return `<svg width="${size}" height="${size}" viewBox="0 0 48 48" style="display:block;overflow:visible;${glow}${o.opacity != null ? `opacity:${o.opacity};` : ""}${o.style || ""}"><path d="${d}" fill="${fill}" stroke="${col}" stroke-width="${sw}" stroke-linecap="round" stroke-linejoin="round"/></svg>`;
};

/* ================================================================ text helpers */
/* tiny markup: **bold**  _serif italic_  ~ghost~  {word|role} (colour) */
function parseMarks(text) {
  const out = []; const re = /\*\*(.+?)\*\*|_(.+?)_|~(.+?)~|\{(.+?)\|([\w#-]+)\}/g; let i = 0, m;
  const s = String(text || "");
  while ((m = re.exec(s))) {
    if (m.index > i) out.push({ t: s.slice(i, m.index) });
    if (m[1] != null) out.push({ t: m[1], bold: true }); else if (m[2] != null) out.push({ t: m[2], serif: true });
    else if (m[3] != null) out.push({ t: m[3], ghost: true }); else out.push({ t: m[4], role: m[5] });
    i = re.lastIndex;
  }
  if (i < s.length) out.push({ t: s.slice(i) });
  return out;
}
fx.parseMarks = parseMarks;
/* typewriter: the first chars typed at `cps` from local second `at`, with a blinking caret while typing.
   flare: true | {color='#FFFFFF', px=18 (glow radius), frames=6 (decay), scale=1.25}: the newest letter lands as a bright
   blurred glyph that cools to the text colour (science-flash typed letter flare) */
fx.typewriter = function (text, lt, o = {}) {
  const s = String(text || ""), at = o.at || 0, cps = o.cps || 28, n = Math.max(0, Math.min(s.length, Math.floor((lt - at) * cps + 1e-6)));
  const typing = n < s.length, k = Math.round(lt * FPS), on = typing || (o.caret === "hold" && Math.floor(k / 15) % 2 === 0);
  const caret = on && o.caret !== false ? `<span style="display:inline-block;width:0.08em;height:0.95em;margin-left:0.04em;vertical-align:-0.1em;background:currentColor"></span>` : "";
  if (o.flare && n > 0) {
    const F = o.flare === true ? {} : o.flare, frames = F.frames || 6, age = (lt - (at + n / cps)) * FPS; // frames since the newest letter landed
    const f = cl(1 - (age + 0.5) / frames);
    if (f > 0.01) {
      const c = F.color || "#FFFFFF", px = (F.px != null ? F.px : 18) * f, sc = 1 + ((F.scale != null ? F.scale : 1.25) - 1) * f, last = s.charAt(n - 1);
      return esc(s.slice(0, n - 1)) + `<span style="display:inline-block;white-space:pre;transform:scale(${r2(sc)});transform-origin:50% 70%;color:${f > 0.5 ? c : "inherit"};text-shadow:0 0 ${r2(px)}px ${c},0 0 ${r2(px * 2.2)}px ${c}">${esc(last)}</span>` + caret;
    }
  }
  return esc(s.slice(0, n)) + caret;
};
/* small deterministic hash (fx text helpers): same inputs, same number in 0..1 */
const hashN = (...a) => { let h = 2166136261; const s = a.join("|"); for (let i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 16777619); } h ^= h >>> 13; h = Math.imul(h, 0x5bd1e995); h ^= h >>> 15; return (h >>> 0) / 4294967296; };
/* per-glyph type-on with a drop-in stretch (stunt-compression ER-11): every glyph (spaces count) starts at at + i / cps and
   drops in over `frames`, stretched tall then settling. Glyphs not yet typed keep their place (opacity 0), so the text box
   never moves. o: {at=0, cps=20, frames=6, drop=0.45 (em above), stretch=0.4 (extra scaleY at the start), blur=0 (px)} */
fx.typeOn = function (text, lt, o = {}) {
  const s = Array.from(String(text || "")), at = o.at || 0, cps = o.cps || 20, fr = o.frames || 6;
  const drop = o.drop != null ? o.drop : 0.45, st = o.stretch != null ? o.stretch : 0.4, bl = o.blur || 0;
  return s.map((ch, i) => {
    const k = (lt - at - i / cps) * FPS, p = cl((k + 0.5) / fr), e = expoOut(p);
    if (ch === " ") return " ";
    if (p >= 1) return `<span style="display:inline-block;white-space:pre">${esc(ch)}</span>`;
    if (k < 0) return `<span style="display:inline-block;white-space:pre;opacity:0">${esc(ch)}</span>`;
    return `<span style="display:inline-block;white-space:pre;opacity:${r2(cl(p * 2.5))};transform-origin:50% 100%;transform:translateY(${r2(-drop * (1 - e))}em) scaleY(${r2(1 + st * (1 - e))})${bl ? `;filter:blur(${r2(bl * (1 - e))}px)` : ""}">${esc(ch)}</span>`;
  }).join("");
};
/* letter-resolve scramble (archive-explainer outlet / tagline): from `at` every glyph shows seeded random characters,
   re-rolled every `every` frames, and locks to its real letter in `order` (ltr | rtl | random | center) over `dur` s.
   Spaces and punctuation never scramble; case is kept. With {ctx, font} each glyph keeps its final width (no jitter).
   o: {at=0, dur=0.6, every=2, order='ltr', seed=1, charset, ghost=0.55 (opacity of unresolved glyphs), color (unresolved)} */
const RESOLVE_SET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#%&*+=?";
fx.resolve = function (text, lt, o = {}) {
  const s = Array.from(String(text || "")), at = o.at || 0, dur = o.dur != null ? o.dur : 0.6, every = Math.max(1, o.every || 2);
  const set = o.charset || RESOLVE_SET, seed = o.seed != null ? o.seed : 1, order = o.order || "ltr", N = s.length;
  const rank = s.map((_, i) => order === "rtl" ? N - 1 - i : order === "center" ? Math.abs(i - (N - 1) / 2) * 2 : order === "random" ? hashN(seed, "r", i) * (N - 1) : i);
  const maxR = Math.max(1, ...rank), k = Math.floor((lt - at) * FPS + 1e-6), bucket = Math.floor(k / every);
  const wfix = (ch) => (o.ctx && o.font ? `width:${r2(o.ctx.measure(ch, o.font))}px;text-align:center;` : "");
  if (lt < at - 1e-6) return s.map(ch => `<span style="display:inline-block;white-space:pre;opacity:0;${wfix(ch)}">${esc(ch)}</span>`).join("");
  return s.map((ch, i) => {
    const lock = at + (rank[i] / maxR) * dur;
    if (!/[A-Za-z0-9À-ɏऀ-ॿ]/.test(ch) || lt >= lock - 1e-6) return `<span style="display:inline-block;white-space:pre;${wfix(ch)}">${esc(ch)}</span>`;
    let r = set.charAt(Math.floor(hashN(seed, i, bucket) * set.length));
    if (ch === ch.toLowerCase() && ch !== ch.toUpperCase()) r = r.toLowerCase();
    return `<span style="display:inline-block;white-space:pre;opacity:${o.ghost != null ? o.ghost : 0.55};${o.color ? `color:${o.color};` : ""}${wfix(ch)}">${esc(r)}</span>`;
  }).join("");
};
fx.resolvedAt = (text, o = {}) => (o.at || 0) + (o.dur != null ? o.dur : 0.6); // local second the last glyph locks (declare it in events)
fx.typedChars = (text, lt, o = {}) => Math.max(0, Math.min(String(text || "").length, Math.floor((lt - (o.at || 0)) * (o.cps || 28) + 1e-6)));

/* load time: transcript words (caption text when set) between t0 and t1 -> [{text, at}] lines of <= maxWords */
fx.linesFromWords = function (t0, t1, o = {}) {
  const maxW = o.maxWords || 3, gap = o.breakGap != null ? o.breakGap : 0.22, lead = o.lead != null ? o.lead : 2 / FPS;
  const ws = VEOS.words(t0 - 1e-6, t1).map(w => ({ t: ("caption" in w) ? w.caption : w.w, s: w.s, e: w.e })).filter(w => w.t !== "" && w.t != null);
  const lines = []; let cur = null;
  for (const w of ws) {
    const brk = !cur || cur.n >= maxW || w.s - cur.e > gap || /[.,!?;:]$/.test(cur.text);
    if (brk) { cur = { text: String(w.t), at: Math.max(t0, w.s - lead), e: w.e, n: 1 }; lines.push(cur); }
    else { cur.text += " " + w.t; cur.e = w.e; cur.n++; }
  }
  return lines.map(l => ({ text: o.strip === false ? l.text : l.text.replace(/[.,;:]+$/, ""), at: Math.round(l.at * 1000) / 1000 }));
};

/* ================================================================ kinetic type stack */
const STACK_STYLES = {
  sans: { slot: "display", weight: 800, size: 92, track: -0.02 },
  serif: { slot: "serif", weight: 400, size: 104, italic: true, track: -0.01 },
  cond: { slot: "numeric", weight: 400, size: 120, track: 0.01, upper: true },
  mono: { slot: "mono", weight: 500, size: 56, track: 0 },
  small: { slot: "display", weight: 600, size: 52, track: -0.01 },
};
fx.stackStyles = STACK_STYLES;
/* o: {id, t_in, t_out, z=5, lines:[{text, at (edit s), style, size, color}], x=540, y=960, anchor center|top|bottom,
       align center|left, maxW=920, alternate=true (sans/serif), styles{}, color='ink', gap=6, lh=1.06, rise=64,
       blurPx=10, inFrames=9, glide=8, maxLines=5 (1 = replace mode), outFrames=6, text_class,
       blurAngle (motion-blur direction in degrees; default the vertical smear), keepTween (a line keeps its own entry tween
       when the next line arrives instead of snapping to rest)} */
fx.typeStack = function (o) {
  const styles = Object.assign({}, STACK_STYLES, o.styles || {});
  const t_in = o.t_in, t_out = o.t_out, alt = o.alternate !== false;
  const lines = (o.lines || []).map((l, i) => {
    const st = Object.assign({}, styles[l.style || (alt ? (i % 2 ? "serif" : "sans") : "sans")] || styles.sans);
    if (l.size) st.size = l.size;
    return { text: String(l.text), at: l.at != null ? +l.at : t_in + i * 0.4, st, color: l.color, f: 0 };
  }).sort((a, b) => a.at - b.at);
  lines.forEach(l => { l.f = Math.max(0, Math.round((l.at - t_in) * FPS)); });
  const x = o.x != null ? o.x : 540, y = o.y != null ? o.y : 960, anchor = o.anchor || "center", align = o.align || "center";
  const maxW = o.maxW || 920, gap = o.gap != null ? o.gap : 6, lh = o.lh || 1.06, rise = o.rise != null ? o.rise : 64;
  const blurPx = o.blurPx != null ? o.blurPx : 10, inF = o.inFrames || 9, glide = o.glide || 8, maxL = Math.max(1, o.maxLines || 5), outF = o.outFrames || 6;
  const hOf = l => l.st.size * lh;
  const maxH = (() => { const hs = lines.map(hOf).sort((a, b) => b - a).slice(0, maxL); return hs.reduce((a, b) => a + b, 0) + gap * Math.max(0, hs.length - 1); })();
  const left = align === "center" ? x - maxW / 2 : x;
  const top0 = anchor === "top" ? y : anchor === "bottom" ? y - maxH : y - maxH / 2;
  const layout = idx => { // idx: visible line indices -> {i: top}
    const hs = idx.map(i => hOf(lines[i])), tot = hs.reduce((a, b) => a + b, 0) + gap * Math.max(0, idx.length - 1);
    let t = anchor === "top" ? y : anchor === "bottom" ? y - tot : y - tot / 2; const out = {};
    idx.forEach((i, j) => { out[i] = t; t += hs[j] + gap; }); return out;
  };
  const visIdx = c => { const a = []; for (let i = Math.max(0, c - maxL); i < c; i++) a.push(i); return a; };
  const texts = lines.map(l => plain(l.text));
  const evs = [];
  lines.forEach((l, i) => { evs.push(l.at); });
  return scene(o, {
    id: o.id, t_in, t_out, z: o.z || 5, in: "none", out: o.out || "blur", text: true, text_content: texts.join(" / "),
    text_px: Math.min(...lines.map(l => l.st.size)), text_class: o.text_class || "TC-display", fx: "typeStack",
    box: { x: Math.round(left), y: Math.round(top0), w: maxW, h: Math.round(maxH) }, events: ev(evs, t_in, t_out),
    render(ctx, lt) {
      const kf = Math.round(lt * FPS); let c = 0; while (c < lines.length && lines[c].f <= kf) c++;
      if (!c) return "";
      const cur = layout(visIdx(c)), prev = c > 1 ? layout(visIdx(c - 1)) : {};
      const dk = kf - lines[c - 1].f, pg = expoOut(dk / glide);
      let html = "";
      const lineHTML = (i, top, op, vb) => {
        const l = lines[i], st = l.st, bgc = bgAt(ctx, t_in + lt), col0 = C(ctx, l.color, o.color || "ink");
        const segs = parseMarks(l.text);
        const fontOf = sg => {
          const s2 = sg.serif ? styles.serif : st;
          return `${s2.italic || sg.serif ? "italic " : ""}${sg.bold ? 900 : s2.weight} ${s2.size}px ${ctx.fam(s2.slot)}`;
        };
        const tw = segs.reduce((a, sg) => a + ctx.measure(st.upper ? sg.t.toUpperCase() : sg.t, fontOf(sg)), 0);
        const k = tw > maxW ? maxW / tw : 1;
        const col = bgc ? legible(col0, bgc, needContrast(st.size * k) + SAFE) : col0;
        const inner = segs.map(sg => {
          const s2 = sg.serif ? styles.serif : st, sz = r2(s2.size * k);
          return `<span style="font:${s2.italic || sg.serif ? "italic " : ""}${sg.bold ? 900 : s2.weight} ${sz}px/${lh} ${ctx.fam(s2.slot)};letter-spacing:${s2.track || 0}em;${sg.ghost ? "opacity:.42;" : ""}${sg.role ? `color:${bgc ? legible(C(ctx, sg.role), bgc, needContrast(sz) + SAFE) : C(ctx, sg.role)};` : ""}">${esc(st.upper ? sg.t.toUpperCase() : sg.t)}</span>`;
        }).join("");
        const filt = vb > 0.4 ? `filter:${ctx.blur(vb, o.blurAngle)};` : "";
        return `<div style="position:absolute;left:${r2(left)}px;top:${r2(top)}px;width:${maxW}px;height:${r2(hOf(l))}px;text-align:${align};white-space:nowrap;color:${col};opacity:${r2(op)};${filt}">${inner}</div>`;
      };
      for (const i of visIdx(c)) {
        if (i === c - 1) { const p = expoOut((dk + 0.5) / inF); html += lineHTML(i, cur[i] + rise * (1 - p), cl(p * 1.6), blurPx * (1 - p)); }
        else if (o.keepTween) { // each line finishes its own rise even when the next one arrives (faceless v01 @ 1.2-1.9)
          const pi = expoOut((kf - lines[i].f + 0.5) / inF);
          html += lineHTML(i, lerp(prev[i] != null ? prev[i] : cur[i], cur[i], pg) + rise * (1 - pi), cl(pi * 1.6), blurPx * (1 - pi));
        } else html += lineHTML(i, lerp(prev[i] != null ? prev[i] : cur[i], cur[i], pg), 1, 0);
      }
      if (c > maxL && dk < outF) { const d = c - 1 - maxL, pe = sineIO((dk + 0.5) / outF); html += lineHTML(d, (prev[d] != null ? prev[d] : top0) - 44 * pe, 1 - pe, 8 * pe); }
      return ctx.html(html);
    },
  });
};

/* ================================================================ diagrams on the canvas (world px) */
function shapePath(nd, w, h) { // node-local path centred on 0,0
  const r = Math.min(w, h) / 2;
  switch (nd.shape) {
    case "hex": { let d = ""; for (let i = 0; i < 6; i++) { const a = -Math.PI / 2 + i * Math.PI / 3; d += `${i ? "L" : "M"}${r2(r * Math.cos(a))} ${r2(r * Math.sin(a))}`; } return d + "Z"; }
    case "circle": return `M${-r} 0 A${r} ${r} 0 1 0 ${r} 0 A${r} ${r} 0 1 0 ${-r} 0 Z`;
    case "diamond": return `M0 ${-h / 2} L${w / 2} 0 L0 ${h / 2} L${-w / 2} 0 Z`;
    default: { const rr = nd.shape === "pill" ? h / 2 : nd.shape === "bar" ? 4 : (nd.radius != null ? nd.radius : 26); const x = -w / 2, y = -h / 2, q = Math.min(rr, w / 2, h / 2);
      return `M${x + q} ${y} H${x + w - q} Q${x + w} ${y} ${x + w} ${y + q} V${y + h - q} Q${x + w} ${y + h} ${x + w - q} ${y + h} H${x + q} Q${x} ${y + h} ${x} ${y + h - q} V${y + q} Q${x} ${y} ${x + q} ${y} Z`; }
  }
}
function edgeEnds(a, b) { // shorten a centre-to-centre line to the node outlines (rect/ellipse approximation)
  const ax = a.x + a.w / 2, ay = a.y + a.h / 2, bx = b.x + b.w / 2, by = b.y + b.h / 2, dx = bx - ax, dy = by - ay, L = Math.hypot(dx, dy) || 1;
  const cut = (n, sx, sy) => { const round = n.shape === "circle" || n.shape === "hex"; if (round) return Math.min(n.w, n.h) / 2 + 6; const tx = Math.abs(sx) > 1e-6 ? (n.w / 2) / Math.abs(sx) : 1e9, ty = Math.abs(sy) > 1e-6 ? (n.h / 2) / Math.abs(sy) : 1e9; return Math.min(tx, ty) * L / L + 6; };
  const ux = dx / L, uy = dy / L, ca = cut(a, ux, uy), cb = cut(b, ux, uy);
  return [ax + ux * ca, ay + uy * ca, bx - ux * cb, by - uy * cb];
}
/* o: {id, t_in, t_out, z=3, nodes:[{id, x, y, w, h, shape hex|circle|pill|rect|bar|diamond|none, label, sub, icon, at, label_at,
       reveal pop|fade|type|redact, fill, ink (label colour), size (label px), label_pos center|below|above|left|right,
       active:[[t0,t1],...], ring}], edges:[{from, to, at, dur=0.45, style line|arrow|dashed, dot, color}],
       dimInactive (opacity of nodes outside their active span while another node is active), stroke='ink', parallax} */
fx.diagram = function (o) {
  const t_in = o.t_in, t_out = o.t_out, nodes = (o.nodes || []).map(n => Object.assign({ shape: "rect", reveal: "pop", w: 200, h: 120 }, n));
  const byId = {}; nodes.forEach(n => { byId[n.id] = n; n.at = n.at != null ? +n.at : t_in; n.label_at = n.label_at != null ? +n.label_at : n.at; });
  const edges = (o.edges || []).filter(e => byId[e.from] && byId[e.to]).map(e => Object.assign({ dur: 0.45, style: "line" }, e, { at: e.at != null ? +e.at : t_in }));
  const pad = 40, xs0 = Math.min(...nodes.map(n => n.x)) - pad, ys0 = Math.min(...nodes.map(n => n.y)) - pad;
  const xs1 = Math.max(...nodes.map(n => n.x + n.w)) + pad, ys1 = Math.max(...nodes.map(n => n.y + n.h)) + pad;
  const subPx = n => Math.max(40, Math.round((n.size || 52) * 0.75)); // diagram text is TC-label: never under 40 px
  const sizes = [...nodes.filter(n => n.label).map(n => n.size || 52), ...nodes.filter(n => n.sub).map(subPx)];
  const labels = nodes.filter(n => n.label || n.sub).map(n => [n.label, n.sub].filter(Boolean).join(" "));
  const evs = [...nodes.map(n => n.at), ...nodes.map(n => n.label_at), ...edges.map(e => e.at), ...edges.map(e => e.at + e.dur)];
  nodes.forEach(n => (n.active || []).forEach(a => evs.push(a[0], a[1])));
  return scene(o, {
    id: o.id, t_in, t_out, z: o.z || 3, in: "none", out: o.out || "blur", text: labels.length > 0, text_content: labels.join(" / "),
    text_px: sizes.length ? Math.min(...sizes) : undefined, text_class: o.text_class || "TC-label", fx: "diagram",
    nodes: nodes.map(n => ({ id: n.id, x: n.x, y: n.y, w: n.w, h: n.h })),
    box: { x: Math.round(xs0), y: Math.round(ys0), w: Math.round(xs1 - xs0), h: Math.round(ys1 - ys0) }, events: ev(evs, t_in, t_out),
    render(ctx, lt) {
      const t = t_in + lt, ink = C(ctx, o.stroke, "ink"), sw = o.strokeWidth || 4;
      const anyActive = nodes.some(n => (n.active || []).some(a => t >= a[0] && t < a[1]));
      // the svg covers only what is visible now, so the measured rect (G1/G2/G3) follows the build-up
      let vx0 = 1e9, vy0 = 1e9, vx1 = -1e9, vy1 = -1e9;
      for (const n of nodes) if (t >= n.at && n.shape !== "none") { const m = n.shape === "hex" || n.ring ? 22 : 12; vx0 = Math.min(vx0, n.x - m); vy0 = Math.min(vy0, n.y - m); vx1 = Math.max(vx1, n.x + n.w + m); vy1 = Math.max(vy1, n.y + n.h + m); }
      for (const e of edges) if (t > e.at) { const q = edgeEnds(byId[e.from], byId[e.to]); vx0 = Math.min(vx0, q[0] - 8, q[2] - 8); vy0 = Math.min(vy0, q[1] - 8, q[3] - 8); vx1 = Math.max(vx1, q[0] + 8, q[2] + 8); vy1 = Math.max(vy1, q[1] + 8, q[3] + 8); }
      const xs0 = vx0 < 1e8 ? vx0 : 0, ys0 = vy0 < 1e8 ? vy0 : 0, xs1 = vx0 < 1e8 ? vx1 : 0, ys1 = vy0 < 1e8 ? vy1 : 0;
      let svg = "", html = "";
      for (const e of edges) {
        const p = cl((t - e.at) / e.dur); if (p <= 0) continue;
        const [x1, y1, x2, y2] = edgeEnds(byId[e.from], byId[e.to]), L = Math.hypot(x2 - x1, y2 - y1), q = sineIO(p);
        const col = C(ctx, e.color, o.edgeColor || o.stroke || "ink");
        const dash = e.style === "dashed" ? `stroke-dasharray="10 10"` : `stroke-dasharray="${r2(L)}" stroke-dashoffset="${r2(L * (1 - q))}"`;
        const ex = lerp(x1, x2, q), ey = lerp(y1, y2, q);
        svg += `<path d="M${r2(x1 - xs0)} ${r2(y1 - ys0)} L${r2((e.style === "dashed" ? ex : x2) - xs0)} ${r2((e.style === "dashed" ? ey : y2) - ys0)}" stroke="${col}" stroke-width="${e.width || 3}" fill="none" stroke-linecap="round" ${dash}/>`;
        if (e.dot !== false) svg += `<circle cx="${r2(x1 - xs0)}" cy="${r2(y1 - ys0)}" r="6" fill="${col}"/>`;
        if (q > 0.98 && (e.dot || e.style === "arrow")) {
          if (e.style === "arrow") { const a = Math.atan2(y2 - y1, x2 - x1), s = 16; svg += `<path d="M${r2(x2 - xs0)} ${r2(y2 - ys0)} L${r2(x2 - xs0 - s * Math.cos(a - 0.45))} ${r2(y2 - ys0 - s * Math.sin(a - 0.45))} M${r2(x2 - xs0)} ${r2(y2 - ys0)} L${r2(x2 - xs0 - s * Math.cos(a + 0.45))} ${r2(y2 - ys0 - s * Math.sin(a + 0.45))}" stroke="${col}" stroke-width="${e.width || 3}" stroke-linecap="round"/>`; }
          else svg += `<circle cx="${r2(x2 - xs0)}" cy="${r2(y2 - ys0)}" r="6" fill="${col}"/>`;
        }
      }
      for (const n of nodes) {
        const lt2 = t - n.at; if (lt2 < 0) continue;
        const pin = n.reveal === "fade" ? 1 : backOut((lt2 * FPS + 0.5) / 9, 1.4), op = cl(lt2 * FPS / 5);
        const act = (n.active || []).some(a => t >= a[0] && t < a[1]);
        const dim = anyActive && !act && !n.nodim && o.dimInactive != null ? o.dimInactive : 1;
        const cx = n.x + n.w / 2 - xs0, cy = n.y + n.h / 2 - ys0, sc = r2(Math.max(0.01, (n.reveal === "fade" ? 1 : lerp(0.6, 1, pin))) * (act ? 1.04 : 1));
        const fill = n.shape === "none" ? "none" : C(ctx, n.fill, n.shape === "bar" ? "ink" : (o.fill || "ink"));
        const redacting = n.reveal === "redact" && (t < n.label_at || !n.label), bare = n.reveal === "redact" && !n.keepShape; // P-REDACT-REVEAL: the bar gives way to typed text
        if (n.shape !== "none" && (!bare || redacting)) {
          svg += `<g transform="translate(${r2(cx)} ${r2(cy)}) scale(${sc})" opacity="${r2(op * dim)}">`;
          if (n.ring !== false && (n.shape === "hex" || n.ring)) svg += `<path d="${shapePath(n, n.w + 34, n.h + 34)}" fill="none" stroke="${n.ringColor ? C(ctx, n.ringColor) : ink}" stroke-opacity="${n.ringColor ? 1 : 0.35}" stroke-width="2"/>`;
          if (act) svg += `<path d="${shapePath(n, n.w + 18, n.h + 18)}" fill="none" stroke="${C(ctx, o.activeColor, "primary")}" stroke-width="6"/>`;
          svg += `<path d="${shapePath(n, n.w, n.h)}" fill="${redacting ? C(ctx, "ink") : fill}" ${n.outline ? `stroke="${C(ctx, n.outline)}" stroke-width="${sw}"` : ""}/></g>`;
        }
        if (!(n.label || n.sub || n.icon)) continue;
        if (t < n.label_at) continue; // a redacted node shows its dark bar until the label types in
        const size = n.size || 52, tcol0 = C(ctx, n.ink, n.shape === "none" || n.shape === "bar" || bare ? "ink" : "paper");
        const ground = n.shape === "none" || bare ? bgAt(ctx, t) : (parseCol(fill) ? toHex(parseCol(fill)) : null); // what the label sits on (null: unknown, left as authored)
        const tcol = ground ? legible(tcol0, ground, needContrast(size) + SAFE) : tcol0;
        const subCol = ground ? legible(fx.mix(tcol, ground, 0.2), ground, 4.5 + SAFE) : tcol; // sublabel: a softer solid tint of the label colour, never opacity
        const lab = n.label ? (n.reveal === "type" || n.reveal === "redact" ? fx.typewriter(n.label, t - n.label_at, { cps: n.cps || 26 }) : esc(n.label)) : "";
        const pos = n.label_pos || "center", bw = Math.max(n.w, ctx.measure(n.label || "", `800 ${size}px ${ctx.fam(o.font || "display")}`) + 20);
        let lx = n.x - xs0 + n.w / 2 - bw / 2, ly = n.y - ys0, lw = bw, lh = n.h, va = "center", ta = "center";
        if (pos === "below") { ly = n.y - ys0 + n.h + 14; lh = size * 2.4; va = "flex-start"; }
        else if (pos === "above") { ly = n.y - ys0 - size * 2.4 - 14; lh = size * 2.4; va = "flex-end"; }
        else if (pos === "right") { lx = n.x - xs0 + n.w + 22; lw = Math.max(320, bw); ta = "left"; }
        else if (pos === "left") { lw = Math.max(320, bw); lx = n.x - xs0 - lw - 22; ta = "right"; }
        const scl = n.shape === "none" || pos !== "center" ? 1 : sc;
        const ic = n.icon ? `<div style="margin-bottom:${r2(size * 0.18)}px">${fx.icon(n.icon, { size: Math.round(size * 1.3), color: tcol, stroke: 3 })}</div>` : "";
        html += `<div style="position:absolute;left:${r2(lx + xs0)}px;top:${r2(ly + ys0)}px;width:${r2(lw)}px;height:${r2(lh)}px;display:flex;flex-direction:column;justify-content:${va};align-items:${ta === "center" ? "center" : ta === "left" ? "flex-start" : "flex-end"};text-align:${ta};color:${tcol};opacity:${r2(op * dim)};transform:scale(${scl});white-space:nowrap">${ic}${lab ? `<div style="font:800 ${size}px/1.08 ${ctx.fam(o.font || "display")};letter-spacing:-0.02em">${lab}</div>` : ""}${n.sub ? `<div style="font:500 ${subPx(n)}px/1.2 ${ctx.fam(o.subFont || "display")};color:${subCol};margin-top:6px">${esc(n.sub)}</div>` : ""}</div>`;
      }
      return ctx.html((svg ? `<svg width="${r2(xs1 - xs0)}" height="${r2(ys1 - ys0)}" style="position:absolute;left:${r2(xs0)}px;top:${r2(ys0)}px;overflow:visible">${svg}</svg>` : "") + html);
    },
  });
};

/* ================================================================ icon / illustration cards */
const THEMES = {
  light: { bg: "paper", fg: "ink", sub: "ink", chip: "primary", chipFg: null, border: null, shadow: "0 24px 60px rgba(0,0,0,.14),0 4px 14px rgba(0,0,0,.08)" },
  dark: { bg: "night", fg: "paper", sub: "paper", chip: "primary", chipFg: null, border: null, shadow: "0 26px 70px rgba(0,0,0,.45)" },
  glass: { bg: "rgba(255,255,255,.10)", fg: "paper", sub: "paper", chip: "primary", chipFg: null, border: "rgba(255,255,255,.22)", shadow: "0 30px 80px rgba(0,0,0,.35)" },
  outline: { bg: "rgba(0,0,0,0)", fg: "ink", sub: "ink", chip: "ink", chipFg: "paper", border: "ink", shadow: "none" },
  glow: { bg: "rgba(0,0,0,.55)", fg: "paper", sub: "paper", chip: "paper", chipFg: "night", border: "rgba(255,255,255,.55)", shadow: "0 0 50px rgba(255,255,255,.18),0 0 120px rgba(255,255,255,.08)" },
};
/* o: {id, t_in, t_out, z=4, x, y, w, h, theme light|dark|glass|outline|glow, icon, iconColor, accent (role), kicker, title, sub,
       number (big figure: a number is written by ctx.fmtNum with `format`; or figure: id binds a plan/figures.json figure), titleSize=58, subSize=40, align left|center, radius=40, device: {kind, ...} (illustration instead of an icon),
       body(ctx, lt, dur) -> html (extra content), in='rise',
       grow: 'fit-text' (the card's width follows its title as it types: typeAt (local s), cps=18, minW; w is the final max.
         A title wider than w wraps by words and the card grows taller line by line: h is the one-line height),
       titleWeight (default the font slot's `weight`, else 800), titleTracking (em; default the slot's `tracking`, else -0.02)} */
/* fit-text card title -> lines [{t, s (index of its first char in the title)}], greedy by words within maxW px */
function cardLines(T0, mw, maxW) {
  const words = T0.split(" "), out = []; let cur = null, s = 0;
  for (const wd of words) {
    if (cur == null) { cur = { t: wd, s }; }
    else if (mw(cur.t + " " + wd) <= maxW) cur.t += " " + wd;
    else { out.push(cur); cur = { t: wd, s }; }
    s += wd.length + 1;
  }
  if (cur) out.push(cur);
  return out;
}
fx.card = function (o) {
  const th = Object.assign({}, THEMES[o.theme || "light"], o.colors || {});
  const x = o.x, y = o.y, w = o.w || 760, h = o.h || 300, ts = o.titleSize || 58, ss = o.subSize || 40, align = o.align || "left";
  // number: a figure (o.figure: its shown value), a raw number (formatted by ctx.fmtNum with o.format), or literal text
  const fig = o.figure && VEOS.fig ? VEOS.fig(o.figure) : null;
  if (o.figure && !fig) VEOS.errors.push(`fx.card ${o.id}: figure '${o.figure}' is not in plan/figures.json`);
  const number = fig ? VEOS.fmtNum(fig.shown, fig, o.format) : (typeof o.number === "number" && VEOS.fmtNum ? VEOS.fmtNum(o.number, o.format) : o.number);
  const sizes = [o.title && ts, o.sub && ss, o.kicker && (o.kickerSize || 40), number && (o.numberSize || 150)].filter(Boolean);
  const txt = [o.kicker, number, o.title, o.sub].filter(Boolean).map(plain).join(" ");
  return scene(o, {
    id: o.id, t_in: o.t_in, t_out: o.t_out, z: o.z || 4, in: o.in || "rise", out: o.out || "blur", text: !!txt, text_content: txt,
    ...(fig ? { figure: fig.id } : {}),
    text_px: sizes.length ? Math.min(...sizes) : undefined, text_class: o.text_class || "TC-label", fx: "card", roles: o.roles || (o.accent ? [o.accent] : undefined),
    box: { x, y, w, h }, events: o.events,
    render(ctx, lt, dur) {
      const fg = C(ctx, th.fg), acc = C(ctx, o.accent || th.chip), pIc = backOut((lt * FPS - 3) / 9, 1.6);
      const bg = C(ctx, th.bg), border = th.border ? `border:3px solid ${C(ctx, th.border)};` : "";
      // the opaque ground under the card text: the card fill, composited over the ambient world when the fill is translucent
      const wb = parseCol(bgAt(ctx, o.t_in + lt)), cb = parseCol(bg), ground = cb ? (cb[3] >= 1 ? toHex(cb) : wb ? toHex(over(cb, wb)) : null) : null;
      const onCard = (c, px) => (ground ? legible(c, ground, needContrast(px) + SAFE) : c);
      const pad = o.pad || 44, icS = o.iconSize || 92;
      const icon = o.icon ? `<div style="flex:none;width:${icS + 36}px;height:${icS + 36}px;border-radius:${Math.round((icS + 36) * 0.3)}px;background:${acc};display:flex;align-items:center;justify-content:center;transform:scale(${r2(cl(pIc, 0, 1.2))})">${fx.icon(o.icon, { size: icS, color: C(ctx, o.iconColor, th.chipFg || ((ctx.tokens.text_on || {})[o.accent || th.chip]) || "#000"), stroke: 3.2 })}</div>` : "";
      const dev = o.device ? fx.device(o.device.kind, Object.assign({ ctx, w: o.device.w || w - 2 * pad, h: o.device.h || Math.round(h * 0.55) }, o.device)) : "";
      const body = o.body ? o.body(ctx, lt, dur) : "";
      const textCol = `<div style="display:flex;flex-direction:column;gap:${Math.round(ss * 0.3)}px;min-width:0;align-items:${align === "center" ? "center" : "flex-start"}">
        ${o.kicker ? `<div style="font:700 ${o.kickerSize || 40}px/1.1 ${ctx.fam(o.kickerFont || "display")};letter-spacing:.06em;text-transform:uppercase;color:${onCard(acc, o.kickerSize || 40)}">${esc(o.kicker)}</div>` : ""}
        ${number ? `<div style="font:400 ${o.numberSize || 150}px/0.95 ${ctx.fam(o.numberFont || "numeric")};color:${fg};font-variant-numeric:tabular-nums">${esc(number)}</div>` : ""}
        ${o.title ? `<div style="font:800 ${ts}px/1.08 ${ctx.fam(o.titleFont || "display")};letter-spacing:-0.02em;color:${fg}">${parseMarks(o.title).map(sg => `<span style="${sg.serif ? `font-family:${ctx.fam("serif")};font-style:italic;font-weight:400;` : ""}${sg.role ? `color:${onCard(C(ctx, sg.role), ts)};` : ""}${sg.ghost ? "opacity:.45;" : ""}">${esc(sg.t)}</span>`).join("")}</div>` : ""}
        ${o.sub ? `<div style="font:500 ${ss}px/1.25 ${ctx.fam(o.subFont || "display")};color:${ground ? legible(fx.mix(C(ctx, th.sub), ground, 0.2), ground, 4.5 + SAFE) : C(ctx, th.sub)}">${esc(o.sub)}</div>` : ""}</div>`;
      const dir = o.layout === "stack" || align === "center" ? "column" : "row";
      if (o.grow === "fit-text" && o.title) { // illustrated-desk: the card grows with its typed title (left / centre anchored)
        // weight / tracking: the options, else the font slot's own (tokens font_slots.<slot>.weight / .tracking), else 800 / -0.02
        const slot = ((ctx.tokens && ctx.tokens.fonts) || {})[o.titleFont || "display"] || {};
        const wt = o.titleWeight != null ? o.titleWeight : slot.weight != null ? slot.weight : 800;
        const trkSet = o.titleTracking != null || slot.tracking != null, trk = o.titleTracking != null ? +o.titleTracking : slot.tracking != null ? +slot.tracking : -0.02;
        const tf = `${wt} ${ts}px ${ctx.fam(o.titleFont || "display")}`, T0 = plain(o.title), at = o.typeAt || 0, cps = o.cps || 18;
        const mw = str => ctx.measure(str, tf) + (trkSet ? trk * ts * Array.from(str).length : 0); // (an unset tracking keeps the v1 measure)
        const xq = Math.max(0, (lt - at) * cps), nn = Math.min(T0.length, Math.floor(xq + 1e-6)), fr = nn < T0.length ? expoOut(xq - nn) : 0;
        const extra = (o.icon ? icS + 36 + Math.round(pad * 0.75) : 0) + 2 * pad + ts * 0.3; // icon + gap + padding + caret
        const LH = 1.08, lines = cardLines(T0, mw, w - extra), radius = o.radius != null ? o.radius : 40;
        const shell = (cx, cw, ch, inner) => ctx.html(`<div style="position:absolute;left:${r2(cx)}px;top:${y}px;width:${cw}px;height:${r2(ch)}px;box-sizing:border-box;padding:${pad}px;border-radius:${radius}px;background:${bg};${border}box-shadow:${th.shadow};display:flex;flex-direction:row;align-items:center;justify-content:${align === "center" ? "center" : "flex-start"};gap:${Math.round(pad * 0.75)}px;overflow:hidden">${icon}${inner}</div>`);
        const minW = o.minW || Math.min(w, 2 * pad + ts);
        if (lines.length < 2) { // one line: the width follows the typed text (v1)
          const tw = lerp(mw(T0.slice(0, nn)), mw(T0.slice(0, Math.min(T0.length, nn + 1))), fr);
          const cw = Math.round(cl(tw + extra, minW, w)), cx = align === "center" ? x + (w - cw) / 2 : x;
          return shell(cx, cw, h, `<div style="font:${tf};line-height:${LH};letter-spacing:${trk}em;color:${fg};white-space:nowrap">${fx.typewriter(T0, lt, { at, cps })}</div>`);
        }
        // several lines: the card widens with the first line, then grows taller as each new line starts typing
        let li = 0; while (li + 1 < lines.length && nn >= lines[li + 1].s) li++;
        const L0 = lines[li], typedL = T0.slice(L0.s, Math.min(L0.s + L0.t.length, nn)), nextL = T0.slice(L0.s, Math.min(L0.s + L0.t.length, nn + 1));
        let tw = lerp(mw(typedL), mw(nextL), fr);
        for (let j = 0; j < li; j++) tw = Math.max(tw, mw(lines[j].t));
        const cw = Math.round(cl(tw + extra, minW, w)), cx = align === "center" ? x + (w - cw) / 2 : x;
        const hN = k => Math.max(h, 2 * pad + k * ts * LH), hp = li > 0 ? expoOut(cl((xq - L0.s) / 3)) : 1;
        const ch = li > 0 ? lerp(hN(li), hN(li + 1), hp) : h;
        const rows = lines.slice(0, li + 1).map((l, j) => `<div>${j < li ? esc(l.t) : fx.typewriter(l.t, lt, { at: at + l.s / cps, cps })}</div>`).join("");
        return shell(cx, cw, ch, `<div style="font:${tf};line-height:${LH};letter-spacing:${trk}em;color:${fg};white-space:nowrap;text-align:${align === "center" ? "center" : "left"}">${rows}</div>`);
      }
      return ctx.html(`<div style="position:absolute;left:${x}px;top:${y}px;width:${w}px;height:${h}px;box-sizing:border-box;padding:${pad}px;border-radius:${o.radius != null ? o.radius : 40}px;background:${bg};${border}box-shadow:${th.shadow};display:flex;flex-direction:${dir};align-items:center;justify-content:${align === "center" ? "center" : "flex-start"};gap:${Math.round(pad * 0.75)}px;text-align:${align};overflow:hidden">${icon}${dev}${textCol}${body}</div>`);
    },
  });
};

/* illustration frames for created visuals (recreated generic UI; never a third-party look-alike):
   kind browser|terminal|phone|doc|chat|note; o: {ctx, w, h, title, lines:[...], theme light|dark, accent, highlight (line index)} */
fx.device = function (kind, o = {}) {
  const ctx = o.ctx, w = o.w || 600, h = o.h || 360, dark = o.theme === "dark" || kind === "terminal";
  const bg = dark ? "#16161a" : "#ffffff", fg = dark ? "#f2f2f2" : "#1d1d1f", mute = dark ? "rgba(255,255,255,.45)" : "rgba(0,0,0,.38)";
  const acc = ctx ? C(ctx, o.accent, "primary") : "#ffcc00", mono = ctx ? ctx.fam("mono") : "monospace", ui = ctx ? ctx.fam(o.font || "display") : "sans-serif";
  const lines = o.lines || [], fs = o.size || 34, hl = o.highlight;
  const dots = `<div style="display:flex;gap:10px">${["#ff5f57", "#febc2e", "#28c840"].map(c => `<span style="width:16px;height:16px;border-radius:50%;background:${c}"></span>`).join("")}</div>`;
  const row = (t, i, font) => `<div style="font:${font};color:${i === hl ? (dark ? "#000" : fg) : fg};${i === hl ? `background:${acc};margin:0 -10px;padding:2px 10px;border-radius:8px;` : ""}white-space:nowrap;overflow:hidden;text-overflow:clip">${t}</div>`;
  if (kind === "terminal" || kind === "browser") {
    const bar = kind === "browser" ? `<div style="flex:1;height:40px;border-radius:20px;background:${dark ? "#2a2a30" : "#f0f0f2"};display:flex;align-items:center;padding:0 18px;font:500 24px ${ui};color:${mute};white-space:nowrap;overflow:hidden">${esc(o.title || "")}</div>` : `<div style="flex:1;text-align:center;font:500 24px ${mono};color:${mute}">${esc(o.title || "terminal")}</div>`;
    const body = lines.map((t, i) => row((kind === "terminal" ? `<span style="color:${acc}">${o.prompt || "&gt;"}</span> ` : "") + esc(t), i, `500 ${fs}px/1.5 ${kind === "terminal" ? mono : ui}`)).join("");
    return `<div style="width:${w}px;height:${h}px;border-radius:26px;background:${bg};overflow:hidden;box-shadow:0 20px 60px rgba(0,0,0,.25);display:flex;flex-direction:column;flex:none">
      <div style="display:flex;align-items:center;gap:18px;padding:16px 20px;border-bottom:2px solid ${dark ? "rgba(255,255,255,.08)" : "rgba(0,0,0,.06)"}">${dots}${bar}</div>
      <div style="padding:22px 28px;display:flex;flex-direction:column;gap:6px">${body}${o.html || ""}</div></div>`;
  }
  if (kind === "phone") {
    return `<div style="width:${w}px;height:${h}px;border-radius:${Math.round(w * 0.14)}px;background:#0d0d10;padding:${Math.round(w * 0.035)}px;box-sizing:border-box;box-shadow:0 30px 70px rgba(0,0,0,.3);flex:none">
      <div style="position:relative;width:100%;height:100%;border-radius:${Math.round(w * 0.11)}px;background:${dark ? "#1b1b20" : "#f6f5f2"};overflow:hidden">
      <div style="position:absolute;left:50%;top:14px;width:${Math.round(w * 0.3)}px;height:${Math.round(w * 0.07)}px;transform:translateX(-50%);border-radius:40px;background:#0d0d10"></div>
      <div style="position:absolute;inset:${Math.round(w * 0.16)}px 26px 26px;display:flex;flex-direction:column;gap:12px">${lines.map((t, i) => row(esc(t), i, `600 ${fs}px/1.3 ${ui}`)).join("")}${o.html || ""}</div></div></div>`;
  }
  if (kind === "chat") {
    return `<div style="width:${w}px;display:flex;flex-direction:column;gap:14px;flex:none">${lines.map((m, i) => { const me = typeof m === "object" && m.who === "me", t = typeof m === "object" ? m.text : m;
      return `<div style="align-self:${me ? "flex-end" : "flex-start"};max-width:78%;padding:16px 24px;border-radius:30px;${me ? `border-bottom-right-radius:8px;background:${acc};color:#000` : `border-bottom-left-radius:8px;background:${dark ? "#2a2a30" : "#ececf0"};color:${fg}`};font:600 ${fs}px/1.3 ${ui}">${esc(t)}</div>`; }).join("")}</div>`;
  }
  // doc / note: a sheet with a title and skeleton lines (decorative bars carry no meaning, TC-decorative)
  const skel = (o.skeleton != null ? o.skeleton : 5);
  return `<div style="width:${w}px;height:${h}px;border-radius:22px;background:${kind === "note" ? "#fff6c9" : bg};box-shadow:0 18px 50px rgba(0,0,0,.18);padding:34px 36px;box-sizing:border-box;display:flex;flex-direction:column;gap:16px;overflow:hidden;flex:none">
    ${o.title ? `<div style="font:800 ${Math.round(fs * 1.2)}px/1.15 ${ui};color:${fg}">${esc(o.title)}</div>` : ""}
    ${lines.map((t, i) => row(esc(t), i, `500 ${fs}px/1.35 ${ui}`)).join("")}
    ${Array.from({ length: skel }, (_, i) => `<div style="height:16px;border-radius:8px;background:${dark ? "rgba(255,255,255,.12)" : "rgba(0,0,0,.08)"};width:${[92, 80, 86, 64, 74, 58][i % 6]}%"></div>`).join("")}${o.html || ""}</div>`;
};

/* ================================================================ creator clips, screen recordings and images */
/* o: {id, t_in, t_out, z=3, asset, x=0, y=0, w=1080, h=1920 (full-bleed), radius=0, speed=1, offset=0 (s into the clip),
       kenburns:[from, to] scale, focus:[fx, fy] (0..1), chip ('6.7M' view count), dim (0..1), border (role), shadow,
       land: {from=1.2, frames=14, ease out|inOut|linear} (P-LAND: an eased pull-back from `from` on entry, then a hold; the
       default `in` becomes "none" so a full-bleed clip never fades up from black),
       rotate: [from, to] degrees (a dolly roll: eased with `land` when set, else over the whole scene; the image is scaled
       to keep covering the frame unless cover: false)} */
fx.clip = function (o) {
  const x = o.x || 0, y = o.y || 0, w = o.w || W, h = o.h || H, kb = o.kenburns || [1, 1];
  const land = o.land ? Object.assign({ from: 1.2, frames: 14, ease: "out" }, o.land === true ? {} : o.land) : null, rot = o.rotate;
  if (rot != null && !(Array.isArray(rot) && rot.length === 2 && rot.every(v => typeof v === "number" && isFinite(v)))) VEOS.errors.push(`fx.clip ${o.id}: rotate must be [from, to] degrees`);
  if (land && !(land.from > 0 && land.from <= 3 && land.frames >= 1)) VEOS.errors.push(`fx.clip ${o.id}: land needs {from: 0-3 (scale), frames >= 1}`);
  const landP = k => { const p = cl((k + 0.5) / land.frames); return land.ease === "linear" ? p : land.ease === "inOut" ? sineIO(p) : expoOut(p); };
  return scene(o, {
    id: o.id, t_in: o.t_in, t_out: o.t_out, z: o.z || 3, in: o.in || (land ? "none" : o.w ? "rise" : "blur"), out: o.out || "blur", fx: "clip",
    text: !!o.chip, text_content: o.chip || undefined, text_px: o.chip ? 40 : undefined, box: { x, y, w, h }, events: o.events,
    render(ctx, lt, dur) {
      const src = ctx.videoFrame(o.asset, (o.offset || 0) + lt * (o.speed || 1)) || ctx.asset(o.asset);
      let s = lerp(kb[0], kb[1], sineIO(lt / Math.max(dur, 0.01))), tr = "";
      const f = o.focus || [0.5, 0.5], k = Math.round(lt * FPS);
      if (land) s *= lerp(land.from, 1, landP(k));
      if (Array.isArray(rot)) {
        const r = lerp(rot[0], rot[1], land ? landP(k) : sineIO(lt / Math.max(dur, 0.01))), a = Math.abs(r) * Math.PI / 180;
        if (o.cover !== false) s *= Math.cos(a) + Math.sin(a) * Math.max(w / h, h / w); // the rotated image still covers the window
        tr = ` rotate(${r2(r)}deg)`;
      }
      const chip = o.chip ? `<div style="position:absolute;left:22px;bottom:22px;padding:8px 20px;border-radius:30px;background:rgba(0,0,0,.6);color:#fff;font:700 40px/1.1 ${ctx.fam("display")};display:flex;align-items:center;gap:10px">${fx.icon("eye", { size: 34, color: "#fff", stroke: 3.4 })}${esc(o.chip)}</div>` : "";
      return ctx.html(`<div style="position:absolute;left:${x}px;top:${y}px;width:${w}px;height:${h}px;border-radius:${o.radius || 0}px;overflow:hidden;${o.border ? `border:5px solid ${C(ctx, o.border)};box-sizing:border-box;` : ""}${o.shadow !== false && o.w ? "box-shadow:0 26px 70px rgba(0,0,0,.28);" : ""}">
        <div style="position:absolute;inset:0;background:url('${src}') ${f[0] * 100}% ${f[1] * 100}%/cover;transform-origin:${f[0] * 100}% ${f[1] * 100}%;transform:scale(${s.toFixed(4)})${tr}"></div>
        ${o.dim ? `<div style="position:absolute;inset:0;background:rgba(0,0,0,${o.dim})"></div>` : ""}${chip}</div>`);
    },
  });
};

/* ================================================================ shapes, morphs, continuity */
const N_PTS = 96;
fx.shape = function (kind, o = {}) {
  const n = o.n || N_PTS, cx = o.cx != null ? o.cx : (o.x != null ? o.x + (o.w || 0) / 2 : 540), cy = o.cy != null ? o.cy : (o.y != null ? o.y + (o.h || 0) / 2 : 960);
  const pts = [], rot = (o.rot || 0) * Math.PI / 180;
  const polar = rf => { for (let i = 0; i < n; i++) { const a = -Math.PI / 2 + rot + (i / n) * 2 * Math.PI, r = rf(a, i); pts.push([cx + r * Math.cos(a), cy + r * Math.sin(a)]); } return pts; };
  const poly = verts => { // resample a closed polygon (list of [x, y]) to n points by arc length, starting at the top
    const segs = verts.map((p, i) => [p, verts[(i + 1) % verts.length]]), lens = segs.map(([a, b]) => Math.hypot(b[0] - a[0], b[1] - a[1])), L = lens.reduce((a, b) => a + b, 0);
    for (let i = 0; i < n; i++) { let d = (i / n) * L, k = 0; while (k < segs.length - 1 && d > lens[k]) { d -= lens[k]; k++; } const [a, b] = segs[k], q = lens[k] ? d / lens[k] : 0; pts.push([lerp(a[0], b[0], q), lerp(a[1], b[1], q)]); }
    return pts;
  };
  const r = o.r != null ? o.r : Math.min(o.w || 200, o.h || 200) / 2;
  switch (kind) {
    case "circle": case "dot": return polar(() => r);
    case "ring": return polar(() => r);
    case "poly": case "hex": case "tri": case "diamond": {
      const sides = kind === "hex" ? 6 : kind === "tri" ? 3 : kind === "diamond" ? 4 : (o.sides || 5), v = [];
      for (let i = 0; i < sides; i++) { const a = -Math.PI / 2 + rot + i * 2 * Math.PI / sides; v.push([cx + r * Math.cos(a), cy + r * Math.sin(a)]); }
      return poly(v);
    }
    case "star": { const k = o.points || 5, ri = o.inner != null ? o.inner : r * 0.45, v = []; for (let i = 0; i < k * 2; i++) { const a = -Math.PI / 2 + rot + i * Math.PI / k, rr = i % 2 ? ri : r; v.push([cx + rr * Math.cos(a), cy + rr * Math.sin(a)]); } return poly(v); }
    case "line": { const x1 = o.x1 != null ? o.x1 : cx - r, x2 = o.x2 != null ? o.x2 : cx + r, y1 = o.y1 != null ? o.y1 : cy, y2 = o.y2 != null ? o.y2 : cy, t = (o.t || 4) / 2;
      const a = Math.atan2(y2 - y1, x2 - x1) + Math.PI / 2, dx = t * Math.cos(a), dy = t * Math.sin(a); return poly([[x1 + dx, y1 + dy], [x2 + dx, y2 + dy], [x2 - dx, y2 - dy], [x1 - dx, y1 - dy]]); }
    default: { // rect / roundrect {x, y, w, h, radius}
      const w = o.w || 2 * r, h = o.h || 2 * r, x = cx - w / 2, y = cy - h / 2, q = Math.min(o.radius || 0, w / 2, h / 2), v = [];
      if (q < 1) return poly([[cx, y], [x + w, y], [x + w, y + h], [x, y + h], [x, y]].slice(0, 5));
      const arc = (ax, ay, a0) => { for (let i = 0; i <= 6; i++) { const a = a0 + (i / 6) * Math.PI / 2; v.push([ax + q * Math.cos(a), ay + q * Math.sin(a)]); } };
      v.push([cx, y]); arc(x + w - q, y + q, -Math.PI / 2); arc(x + w - q, y + h - q, 0); arc(x + q, y + h - q, Math.PI / 2); arc(x + q, y + q, Math.PI); v.push([cx - 0.01, y]);
      return poly(v);
    }
  }
};
const ALIGN = new Map();
fx.morph = function (a, b, p) { // point lists of equal length; b is cyclically shifted once (cached) to minimise travel
  const key = a.length + ":" + r2(a[0][0]) + "," + r2(a[0][1]) + "|" + r2(b[0][0]) + "," + r2(b[0][1]) + ":" + r2(b[7 % b.length][0]);
  let sh = ALIGN.get(key);
  if (sh == null) { let best = 1e18; sh = 0; for (let k = 0; k < b.length; k += 2) { let d = 0; for (let i = 0; i < a.length; i += 3) { const q = b[(i + k) % b.length]; d += (a[i][0] - q[0]) ** 2 + (a[i][1] - q[1]) ** 2; } if (d < best) { best = d; sh = k; } } ALIGN.set(key, sh); if (ALIGN.size > 400) ALIGN.clear(); }
  const e = cl(p); return a.map((pt, i) => { const q = b[(i + sh) % b.length]; return [lerp(pt[0], q[0], e), lerp(pt[1], q[1], e)]; });
};
fx.path = pts => "M" + pts.map(p => `${r2(p[0])} ${r2(p[1])}`).join(" L") + " Z";
fx.handoff = (a, b, p) => { const e = cl(p); return { x: lerp(a.x, b.x, e), y: lerp(a.y, b.y, e), w: lerp(a.w, b.w, e), h: lerp(a.h, b.h, e), r: lerp(a.r || 0, b.r || 0, e) }; };
/* one continuous object through several shapes (Dan Koe's morph chain, peter's hub that becomes the next card).
   o: {id, t_in, t_out, z=3, keys:[{at (edit s), shape:{kind, ...fx.shape opts}, fill, stroke, width, glow, opacity}], dur=0.5 (morph to each key), parallax} */
fx.morphShape = function (o) {
  const keys = (o.keys || []).map(k => Object.assign({}, k, { at: k.at != null ? +k.at : o.t_in, pts: fx.shape(k.shape.kind, k.shape) })).sort((a, b) => a.at - b.at);
  const all = keys.flatMap(k => k.pts), pad = 60;
  const bx = Math.min(...all.map(p => p[0])) - pad, by = Math.min(...all.map(p => p[1])) - pad, bw = Math.max(...all.map(p => p[0])) + pad - bx, bh = Math.max(...all.map(p => p[1])) + pad - by;
  const dur = o.dur || 0.5;
  return scene(o, {
    id: o.id, t_in: o.t_in, t_out: o.t_out, z: o.z || 3, in: o.in || "blur", out: o.out || "blur", fx: "morphShape", text: false,
    box: { x: Math.round(bx), y: Math.round(by), w: Math.round(bw), h: Math.round(bh) }, events: ev(keys.map(k => k.at), o.t_in, o.t_out),
    render(ctx, lt) {
      const t = o.t_in + lt; let i = 0; while (i + 1 < keys.length && keys[i + 1].at <= t) i++;
      const a = keys[Math.max(0, i - 1)], b = keys[i], p = i === 0 ? 1 : (o.ease === "out" ? expoOut : sineIO)((t - b.at) / dur);
      const pts = i === 0 ? b.pts : fx.morph(a.pts, b.pts, p);
      const fill = (k) => (k.fill ? C(ctx, k.fill) : "none"), stroke = k => (k.stroke ? C(ctx, k.stroke) : "none");
      const f = a.fill && b.fill && /^#/.test(fill(a)) && /^#/.test(fill(b)) ? fx.mix(fill(a), fill(b), p) : (p < 0.5 ? fill(a) : fill(b));
      const s = a.stroke && b.stroke && /^#/.test(stroke(a)) && /^#/.test(stroke(b)) ? fx.mix(stroke(a), stroke(b), p) : (p < 0.5 ? stroke(a) : stroke(b));
      const wd = lerp(a.width || 0, b.width || 0, p), gl = lerp(a.glow || 0, b.glow || 0, p), op = lerp(a.opacity != null ? a.opacity : 1, b.opacity != null ? b.opacity : 1, p);
      const glowCol = s !== "none" ? s : f;
      return ctx.html(`<svg width="${r2(bw)}" height="${r2(bh)}" viewBox="${r2(bx)} ${r2(by)} ${r2(bw)} ${r2(bh)}" style="position:absolute;left:${r2(bx)}px;top:${r2(by)}px;overflow:visible;opacity:${r2(op)};${gl > 0.5 ? `filter:drop-shadow(0 0 ${r2(gl)}px ${glowCol}) drop-shadow(0 0 ${r2(gl * 2.4)}px ${glowCol});` : ""}"><path d="${fx.path(pts)}" fill="${f}" stroke="${s}" stroke-width="${r2(wd)}" stroke-linejoin="round"/></svg>`);
    },
  });
};

/* ================================================================ light passes and breaks (naman T-19 / T-20, tech-countdown) */
/* fx.flash: a full-frame light flash (z11, kind "flash"). o: {id, at (edit s; or t_in), up=2, hold=1, decay=6 (frames),
   color='#FFFFFF', peak=0.85 (0..1), blend (CSS mix-blend-mode, e.g. 'screen')}. Flashes are free: any number, any
   length (a style that strobes, strobes). */
const FLASHES = [];
fx.flash = function (o) {
  const at = o.at != null ? +o.at : +o.t_in, up = Math.max(1, o.up || 2), hold = Math.max(0, o.hold != null ? o.hold : 1), decay = Math.max(1, o.decay || 6);
  const F = up + hold + decay, peak = cl(o.peak != null ? o.peak : 0.85), col0 = o.color || "#FFFFFF";
  FLASHES.push({ id: o.id, at });
  const opAt = k => (k < up ? peak * (k + 1) / up : k < up + hold ? peak : peak * Math.pow(1 - cl((k - up - hold + 1) / decay), 2));
  return scene(o, {
    id: o.id, t_in: at, t_out: at + F / FPS, z: o.z || 11, in: "none", out: "none", fx: "flash", kind: o.kind || "flash", text: false,
    box: { x: 0, y: 0, w: W, h: H }, flash: { peak, frames: F },
    render(ctx, lt) {
      const k = Math.round(lt * FPS), op = opAt(k);
      return op > 0.004 ? ctx.html(`<div style="position:absolute;inset:0;background:${C(ctx, col0)};opacity:${r2(op)};${o.blend ? `mix-blend-mode:${o.blend};` : ""}"></div>`) : "";
    },
  });
};
fx.flashes = () => FLASHES.slice();
/* fx.streak: light streaks sweeping across the frame (a whip / transition accent). o: {id, at, frames=8, y=960, angle=0
   (degrees, the travel direction), color='#FFFFFF', width=16 (thickness px), length=0.7 (of the frame width), count=3,
   spread=140 (px across the travel), seed=1, glow=24 (px), opacity=0.9, core (the hot centre line: white by default on a
   coloured streak; 'none' = no core)}.
   A streak is even by default: the lead lane starts on `at` at full strength and every lane holds its strength for the
   whole sweep (a plateau, with a short fade at the ends: none up to 9 frames, 2 frames from 10, 3 from 20) and travels
   near-linearly. Rare overrides: fade (the end-fade length in frames), ease ('soft' (default) | 'expo' | 'linear' |
   'sine': the travel), bar (true: a light bar ACROSS the travel, spanning the frame, `width` px thick along the travel). */
const STREAK_EASE = { expo: expoOut, linear: p => cl(p), sine: sineIO, soft: p => lerp(cl(p), sineIO(p), 0.3) };
const isWhite = c => /^#?f{3}(f{3})?$/i.test(String(c || "").trim()) || /^(white|paper)$/i.test(String(c || ""));
fx.streak = function (o) {
  const at = o.at != null ? +o.at : +o.t_in, F = Math.max(2, o.frames || 8), N = Math.max(1, o.count || 3), seed = o.seed || 1;
  const cy = o.y != null ? o.y : 960, ang = o.angle || 0, th = o.width || 16, len = (o.length || 0.7) * W, spread = o.spread != null ? o.spread : 140;
  const fade = o.fade != null ? Math.max(0, +o.fade) : F >= 20 ? 3 : F >= 10 ? 2 : 1, bar = !!o.bar;
  const ez = STREAK_EASE[o.ease || "soft"];
  if (!ez) VEOS.errors.push(`fx.streak ${o.id}: ease '${o.ease}' is not one of ${Object.keys(STREAK_EASE).join(" | ")}`);
  const lanes = Array.from({ length: N }, (_, i) => ({ dy: i === 0 ? 0 : (hashN(seed, "y", i) - 0.5) * 2 * spread, lag: i === 0 ? 0 : hashN(seed, "l", i) * 0.35, k: 0.6 + hashN(seed, "w", i) * 0.8, op: i === 0 ? 1 : 0.55 + hashN(seed, "o", i) * 0.45 }));
  const BAR_H = 2 * Math.hypot(W, H); // a bar spans the rotated frame
  return scene(o, {
    id: o.id, t_in: at, t_out: at + F / FPS, z: o.z || 11, in: "none", out: "none", fx: "streak", kind: o.kind || "sweep", text: false,
    box: bar ? { x: 0, y: 0, w: W, h: H } : { x: 0, y: Math.round(cy - spread - th), w: W, h: Math.round(2 * (spread + th)) },
    render(ctx, lt) {
      const k = Math.round(lt * FPS), c = C(ctx, o.color, "#FFFFFF"), D = W * 1.3 + len; let h = "";
      const core = o.core === "none" || o.core === false ? null : o.core != null ? C(ctx, o.core) : isWhite(c) ? null : "#FFFFFF";
      const glow = o.glow != null ? o.glow : 24;
      for (const l of lanes) {
        const p = cl(((k + 0.5) / F - l.lag) / (1 - l.lag)); if (p <= 0 || p >= 1) continue;
        const Fl = F * (1 - l.lag), kl = p * Fl, env = fade < 1 ? 1 : cl(Math.min((kl + 0.5) / fade, (Fl - kl + 0.5) / fade));
        const e = (ez || STREAK_EASE.soft)(p), a = l.op * (o.opacity != null ? o.opacity : 0.9) * env;
        if (bar) { // a bar across the travel: crosses from just off the left edge to just off the right edge
          const xb = -th - W * 0.15 + (W * 1.3 + th) * e;
          const g = core ? `${rgba(ctx, c, 0)},${rgba(ctx, c, 1)} 35%,${rgba(ctx, core, 1)} 50%,${rgba(ctx, c, 1)} 65%,${rgba(ctx, c, 0)}` : `${rgba(ctx, c, 0)},${rgba(ctx, c, 1)} 50%,${rgba(ctx, c, 0)}`;
          h += `<div style="position:absolute;left:${r2(xb)}px;top:${r2(cy + l.dy - BAR_H / 2)}px;width:${r2(th)}px;height:${r2(BAR_H)}px;background:linear-gradient(90deg,${g});opacity:${r2(a)};box-shadow:0 0 ${glow}px ${rgba(ctx, c, 0.6)}"></div>`;
          continue;
        }
        const L = len * l.k, xx = -L - W * 0.15 + D * e, ct = Math.max(2, Math.round(th * 0.38));
        const coreDiv = core ? `<div style="position:absolute;left:${r2(L * 0.12)}px;top:${r2((th - ct) / 2)}px;width:${r2(L * 0.86)}px;height:${ct}px;border-radius:${ct}px;background:linear-gradient(90deg,${rgba(ctx, core, 0)},${rgba(ctx, core, 1)} 80%,${rgba(ctx, core, 0)})"></div>` : "";
        h += `<div style="position:absolute;left:${r2(xx)}px;top:${r2(cy + l.dy - th / 2)}px;width:${r2(L)}px;height:${th}px;border-radius:${th}px;background:linear-gradient(90deg,${rgba(ctx, c, 0)},${rgba(ctx, c, 1)} 80%,${rgba(ctx, c, 0)});opacity:${r2(a)};box-shadow:0 0 ${glow}px ${rgba(ctx, c, 0.6)}">${coreDiv}</div>`;
      }
      return h ? ctx.html(`<div style="position:absolute;inset:0;overflow:hidden"><div style="position:absolute;inset:0;transform-origin:540px ${r2(cy)}px;transform:rotate(${r2(ang)}deg)">${h}</div></div>`) : "";
    },
  });
};
/* fx.shatter: whatever sits under a box breaks into seeded shards that fly out from an impact point, spin and fall.
   o: {id, at, frames=14, hold=0 (frames intact before the break), x, y, w, h (default the source scene's box, else the full
   frame), cx, cy (impact; default the rect centre), cols=5, rows=8, spread=700 (px), spin=90 (deg), gravity=900 (px), seed=1,
   z (default: the source scene's z, else 10)} -> kind "transition" (a momentary break, exempt from the face rule).
   The source, by default: the topmost visible scene overlapping the box at the break frame (at + hold); flashes, streaks,
   shatters and ambient backgrounds are skipped. Its own markup is shattered (each shard a clone of it clipped to a
   polygon, drawn as it was on the break frame) and the source scene ends on the break frame by itself.
   Rare overrides: scene (a scene id or the object a factory returned), html (string or (ctx, lt) -> html in frame px),
   asset (an image / video asset name) or fill (a colour plate). With none of these and no scene under the box, the
   box breaks as a 'paper' plate. */
const sceneOf = v => (v && typeof v === "object" ? v : v != null ? (VEOS.scenes || []).find(q => String(q.id) === String(v)) || null : null);
const NOT_SOURCE_FX = ["flash", "streak", "shatter", "ambient"];
/* the topmost scene on screen under the rect around [t0, tb] (registration order breaks z ties: later draws on top) */
function sceneUnder(list, self, rect, t0, tb) {
  const e = 0.5 / FPS; let best = null, bi = -1;
  (list || []).forEach((q, i) => {
    if (!q || q === self || String(q.id) === String(self.id) || NOT_SOURCE_FX.includes(q.fx) || q.kind === "ambient" || typeof q.render !== "function") return;
    if (!(q.t_in <= tb + e && q.t_out >= t0 - e)) return;
    const b = q.box || { x: 0, y: 0, w: W, h: H };
    if (!(b.x < rect.x + rect.w && rect.x < b.x + b.w && b.y < rect.y + rect.h && rect.y < b.y + b.h)) return;
    if (!best || (q.z || 0) > (best.z || 0) || ((q.z || 0) === (best.z || 0) && i > bi)) { best = q; bi = i; }
  });
  return best;
}
fx.shatter = function (o) {
  const at = o.at != null ? +o.at : +o.t_in, hold = o.hold || 0, F = Math.max(2, o.frames || 14), seed = o.seed || 1;
  const src0 = sceneOf(o.scene), sb = src0 && src0.box && o.x == null && o.y == null && o.w == null && o.h == null ? src0.box : null;
  if (o.scene != null && !src0 && typeof o.scene !== "string") VEOS.errors.push(`fx.shatter ${o.id}: scene must be a scene id or a scene object`);
  const x = sb ? sb.x : o.x || 0, y = sb ? sb.y : o.y || 0, w = sb ? sb.w : o.w || W, h = sb ? sb.h : o.h || H, cols = Math.max(1, o.cols || 5), rows = Math.max(1, o.rows || 8);
  const auto = o.scene == null && o.html == null && !o.asset && o.fill == null; // break whatever is under the box
  const icx = o.cx != null ? o.cx : x + w / 2, icy = o.cy != null ? o.cy : y + h / 2, spread = o.spread != null ? o.spread : 700, spin = o.spin != null ? o.spin : 90, grav = o.gravity != null ? o.gravity : 900;
  const P = []; // jittered lattice (edges stay on the rect)
  for (let r = 0; r <= rows; r++) { const row = []; for (let c = 0; c <= cols; c++) { const jx = c > 0 && c < cols ? (hashN(seed, "x", r, c) - 0.5) * 0.7 : 0, jy = r > 0 && r < rows ? (hashN(seed, "y", r, c) - 0.5) * 0.7 : 0; row.push([x + (c + jx) * w / cols, y + (r + jy) * h / rows]); } P.push(row); }
  const shards = [];
  for (let r = 0; r < rows; r++) for (let c = 0; c < cols; c++) {
    const a = P[r][c], b = P[r][c + 1], d = P[r + 1][c + 1], e = P[r + 1][c], diag = hashN(seed, "d", r, c) < 0.5;
    for (const tri of diag ? [[a, b, d], [a, d, e]] : [[a, b, e], [b, d, e]]) {
      const gx = (tri[0][0] + tri[1][0] + tri[2][0]) / 3, gy = (tri[0][1] + tri[1][1] + tri[2][1]) / 3, dx = gx - icx, dy = gy - icy, dist = Math.hypot(dx, dy) || 1, i = shards.length;
      const v = spread * (0.55 + hashN(seed, "v", i) * 0.9) * (0.6 + 0.4 * Math.min(1, 400 / dist));
      shards.push({ tri, gx, gy, vx: dx / dist * v, vy: dy / dist * v, rot: (hashN(seed, "s", i) - 0.5) * 2 * spin, delay: Math.min(0.35, dist / Math.hypot(w, h) * 0.5) });
    }
  }
  const tb = at + hold / FPS; // the break frame: the source is frozen as it was then
  let picked = null, bound = false;
  const self = scene(o, {
    id: o.id, t_in: at, t_out: at + (hold + F) / FPS, z: o.z || (src0 && src0.z) || 10, in: "none", out: "none", fx: "shatter", kind: o.kind || "transition", text: false,
    box: { x, y, w, h }, events: o.events,
    /* called by core once every scene is registered (and lazily on the first frame): bind the scene under the box and
       end it on the break frame, so the intact source does not stay on screen under the flying shards */
    resolve(list) {
      if (!auto || bound) return picked; bound = true;
      picked = sceneUnder(list || VEOS.scenes, this || self, { x, y, w, h }, at, tb);
      if (picked) {
        if (picked.t_out > tb + 1e-6 && tb > picked.t_in + 1e-6) picked.t_out = tb;
        if (o.z == null && self && picked.z != null) self.z = picked.z;
      }
      return picked;
    },
    render(ctx, lt) {
      const k = Math.round(lt * FPS) - hold;
      // a live scene / markup: clones of the frame-space markup, each clipped to its shard (no rasterising)
      const sc = o.scene != null ? sceneOf(o.scene) : auto ? (bound ? picked : self && self.resolve ? self.resolve() : null) : null;
      if (o.scene != null && !sc) VEOS.errors.push(`fx.shatter ${o.id}: scene '${o.scene}' is not registered`);
      if (sc || o.html != null) {
        let mk = "";
        if (sc) { const d = sc.t_out - sc.t_in, sl = Math.max(0, Math.min(tb - sc.t_in, d - 1 / FPS)); mk = sc.render(ctx, sl, d) || ""; }
        else mk = typeof o.html === "function" ? o.html(ctx, Math.max(0, Math.min(lt, hold / FPS))) || "" : String(o.html);
        const full = `position:absolute;left:0;top:0;width:${W}px;height:${H}px`;
        if (k < 0) return auto ? "" : ctx.html(`<div style="${full}">${mk}</div>`); // intact: the source itself (bound: it still draws itself), no seams
        let s = "";
        for (const sh of shards) {
          const p = cl(((k + 0.5) / F - sh.delay) / (1 - sh.delay)), e = expoOut(p), op = 1 - p * p;
          if (op <= 0.01) continue;
          const poly = sh.tri.map(q => `${r2(q[0])}px ${r2(q[1])}px`).join(",");
          s += `<div style="${full};clip-path:polygon(${poly});transform-origin:${r2(sh.gx)}px ${r2(sh.gy)}px;transform:translate(${r2(sh.vx * e)}px,${r2(sh.vy * e + grav * p * p)}px) rotate(${r2(sh.rot * e)}deg);opacity:${r2(op)}">${mk}</div>`;
        }
        return ctx.html(s);
      }
      const src = o.asset ? (ctx.videoFrame(o.asset, (o.offset || 0) + lt) || ctx.asset(o.asset)) : "";
      const paint = src ? `background:url('${src}') center/cover no-repeat` : `background:${C(ctx, o.fill, "paper")}`; // the same picture fx.clip shows in the rect
      if (k < 0) return ctx.html(`<div style="position:absolute;left:${x}px;top:${y}px;width:${w}px;height:${h}px;${paint}"></div>`); // intact: no seams
      let s = "";
      for (const sh of shards) {
        const p = cl(((k + 0.5) / F - sh.delay) / (1 - sh.delay)), e = expoOut(p), op = k < 0 ? 1 : 1 - p * p;
        if (op <= 0.01) continue;
        const tx = k < 0 ? 0 : sh.vx * e, ty = k < 0 ? 0 : sh.vy * e + grav * p * p, rr = k < 0 ? 0 : sh.rot * e;
        const poly = sh.tri.map(q => `${r2(q[0] - x)}px ${r2(q[1] - y)}px`).join(",");
        s += `<div style="position:absolute;left:${x}px;top:${y}px;width:${w}px;height:${h}px;clip-path:polygon(${poly});${paint};transform-origin:${r2(sh.gx - x)}px ${r2(sh.gy - y)}px;transform:translate(${r2(tx)}px,${r2(ty)}px) rotate(${r2(rr)}deg);opacity:${r2(op)}"></div>`;
      }
      return ctx.html(s);
    },
  });
  return self;
};

/* text areas at frame n: the live caption chunks (renderer/captions.js) plus any rects the caller passes */
fx.textRectsAt = function (n, extra) {
  const out = (extra || []).filter(q => q && isFinite(q.x) && isFinite(q.y)).map(q => ({ x: +q.x, y: +q.y, w: +q.w || 0, h: +q.h || 0 }));
  const cap = typeof window !== "undefined" && window.VEOS_CAPTIONS;
  if (cap && cap.active && cap.chunks) for (const c of cap.chunks() || []) if (c && c.rect && c.f0 <= n && n < c.f1) out.push(c.rect);
  return out;
};

/* ================================================================ ambient backgrounds (z1, full frame, pinned; they follow the canvas camera themselves) */
/* o: {id, t_in, t_out, kind paper|dots|grid|void|aurora|particles|cards, bg, ink, glow, spacing, dot, follow (0..1, how much the
       pattern follows the canvas camera; default 1 for paper/dots/grid, 0.25 otherwise), drift:[vx, vy] px/s, count, seed, assets:[names], opacity,
       text_rects:[{x,y,w,h}] (cards: extra text areas to dim under; live captions are found by themselves)}
   The registered scene is kind "ambient" (continuous motion for the cadence and hook checks) and keeps the pattern in `ambient`. */
const RAIN_SPEED = [24, 40, 56], RAIN_DIM = 0.5, RAIN_PAD = 40; // card rain: px/s per depth (E4 max 60), opacity kept under text
fx.ambient = function (o) {
  const kind = o.kind || "paper";
  AMBIENT.push({ t_in: o.t_in, t_out: o.t_out, bg: o.bg, dflt: kind === "void" || kind === "particles" ? "night" : "canvas" });
  return scene(Object.assign({}, o, { kind: undefined }), {
    id: o.id, t_in: o.t_in, t_out: o.t_out, z: 1, in: o.in || "none", out: o.out || "none", parallax: false, fx: "ambient", text: false,
    kind: "ambient", ambient: kind, continuous: true,
    ...(kind === "cards" ? { speed_px_s: RAIN_SPEED[2], dim_under_text: 1 - RAIN_DIM } : {}),
    box: { x: 0, y: 0, w: W, h: H }, cuts: o.cuts,
    render(ctx, lt) {
      const t = ctx.t, follow = o.follow != null ? o.follow : (["paper", "dots", "grid"].includes(kind) ? 1 : 0.25);
      const v = ctx.camera.view(follow), dr = o.drift || [0, 0];
      const sx = (wx) => (wx - v.x) * v.s + W / 2, sy = (wy) => (wy - v.y) * v.s + H / 2;
      const bg = C(ctx, o.bg, kind === "void" || kind === "particles" ? "night" : "canvas"), ink = C(ctx, o.ink, kind === "void" ? "paper" : "grid");
      if (kind === "paper" || kind === "dots" || kind === "grid") {
        const g = (o.spacing || 36) * v.s, ox = ((sx(dr[0] * t) % g) + g) % g, oy = ((sy(dr[1] * t) % g) + g) % g, d = (o.dot || 2.2) * Math.max(0.6, Math.min(v.s, 2.2));
        const pat = kind === "grid"
          ? `linear-gradient(${ink} ${r2(Math.max(1, v.s * 1.5))}px,transparent 0),linear-gradient(90deg,${ink} ${r2(Math.max(1, v.s * 1.5))}px,transparent 0)`
          : `radial-gradient(circle,${ink} ${r2(d)}px,transparent ${r2(d + 0.8)}px)`;
        return ctx.html(`<div style="position:absolute;inset:0;background:${bg}"></div><div style="position:absolute;inset:0;opacity:${o.opacity != null ? o.opacity : 1};background-image:${pat};background-size:${r2(g)}px ${r2(g)}px;background-position:${r2(ox - (kind === "grid" ? 0 : g / 2))}px ${r2(oy - (kind === "grid" ? 0 : g / 2))}px"></div>`);
      }
      if (kind === "void" || kind === "aurora") {
        const glow = C(ctx, o.glow, kind === "void" ? "paper" : "primary"), blobs = kind === "void" ? [[0.5, 0.42, 520, 0.10], [0.3, 0.7, 380, 0.05]] : [[0.25, 0.3, 620, 0.32], [0.78, 0.55, 560, 0.26], [0.45, 0.85, 520, 0.22]];
        let h = `<div style="position:absolute;inset:0;background:${bg}"></div>`;
        blobs.forEach((b, i) => {
          const px = sx(b[0] * W + Math.sin(t * 0.21 + i * 2.1) * 90), py = sy(b[1] * H + Math.cos(t * 0.17 + i * 1.3) * 120), rr = b[2] * Math.sqrt(v.s);
          h += `<div style="position:absolute;inset:0;background:radial-gradient(circle at ${r2(px)}px ${r2(py)}px,${rgba(ctx, glow, b[3])} 0,${rgba(ctx, glow, 0)} ${r2(rr)}px)"></div>`;
        });
        return ctx.html(h);
      }
      if (kind === "particles") {
        const g = ctx.canvas(), rnd = ctx.rngStable("pts" + (o.seed || 1)), N = o.count || 70, col = C(ctx, o.ink, "paper");
        g.fillStyle = bg; g.fillRect(0, 0, W, H);
        for (let i = 0; i < N; i++) {
          const x0 = rnd() * W, y0 = rnd() * H, sp = 6 + rnd() * 18, rr = 1 + rnd() * 2.6, a = 0.15 + rnd() * 0.45;
          const px = ((sx(x0 + dr[0] * t) % W) + W) % W, py = ((sy(y0 - sp * t + dr[1] * t) % H) + H) % H;
          g.globalAlpha = a; g.fillStyle = col; g.beginPath(); g.arc(px, py, rr * Math.min(2, v.s), 0, Math.PI * 2); g.fill();
        }
        g.globalAlpha = 1; return "";
      }
      // cards: P-CARD-RAIN (E4 ambient field): rounded tiles drifting up in three depths (<= 56 px/s, E4 max 60);
      // creator thumbnails when given. A tile under live text (+40 px) keeps only half its opacity (E4 dim_under_text).
      const rnd = ctx.rngStable("cards" + (o.seed || 1)), N = o.count || 24, assets = o.assets || [], tile = C(ctx, o.ink, "grid");
      const under = fx.textRectsAt(Math.round(t * 30), o.text_rects);
      let h = `<div style="position:absolute;inset:0;background:${bg}"></div>`;
      for (let i = 0; i < N; i++) {
        const depth = i % 3, w = [150, 190, 230][depth], hh = Math.round(w * 16 / 9), sp = RAIN_SPEED[depth];
        const x0 = rnd() * (W + 200) - 100, y0 = rnd() * (H + hh * 2);
        const py = ((y0 - sp * t) % (H + hh * 2) + (H + hh * 2)) % (H + hh * 2) - hh, px = x0 + (v.x - W / 2) * -0.15 * (depth + 1);
        const img = assets.length ? `background:url('${ctx.asset(assets[i % assets.length])}') center/cover` : `background:${tile}`;
        const lit = under.some(q => px + w / 2 > q.x - RAIN_PAD && px - w / 2 < q.x + q.w + RAIN_PAD && py + hh > q.y - RAIN_PAD && py < q.y + q.h + RAIN_PAD);
        const op = [0.35, 0.6, 0.9][depth] * (lit ? RAIN_DIM : 1);
        h += `<div data-item="1" style="position:absolute;left:${r2(px - w / 2)}px;top:${r2(py)}px;width:${w}px;height:${hh}px;border-radius:18px;${img};opacity:${r2(op)};box-shadow:0 10px 30px rgba(0,0,0,.12)"></div>`;
      }
      return ctx.html(h);
    },
  });
};
})();
