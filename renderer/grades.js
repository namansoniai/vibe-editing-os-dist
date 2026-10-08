/* Vibe Editing OS footage grades (E-16, tokens.schema §3.12). Pure string building, no DOM: loaded by player.html before
   core.js (window.VEOS_GRADES) and by node in the engine tests (module.exports).

   A grade is drawn ON THE FOOTAGE LAYER: core.js puts it in the `filter` of every footage image (the frame, the cut-out
   matte, the head breakout, the sharp under-copy) so the graphics above stay ungraded and the cut-out person matches the
   footage exactly. Grade specs (tokens.grades.footage, tokens.grades.scene["GR-…"], a theme's `grade`, a world's `grade`,
   a scene's `grade`, timeline.grade and timeline.grades[] events):

     "GR-id"                         a tokens.grades.scene id
     "grayscale(1) contrast(1.1)"    a CSS filter list
     {preset: "GR-id", lift, gamma, gain, warmth, saturation, contrast, brightness, bloom, vignette,
      filter | css: "<CSS filter list>", blend: "color|saturation|multiply|…", fill: "#hex", opacity, prefer: "filter"}

   Numbers win over the CSS list (lift/gamma/gain are exact in an SVG feComponentTransfer: out = lift + (gain - lift) *
   in^(1/gamma)); `prefer: "filter"` keeps the list. warmth -1..1 (R up / B down), saturation and contrast are factors (1 =
   unchanged), bloom 0..1 (blurred highlights screened back), vignette 0..1 (a radial falloff on the footage WINDOW, in
   the filter, so the cut-out gets the same falloff), blend + fill + opacity = a tint (B&W via a grey `saturation` fill,
   a colour flash via `color`). Spatial parts (vignette, bloom) can be switched off for backdrop copies.

   Which grade is on the footage at frame n (core.js, `pick`): an active scene with `grade` > the current world's `grade`
   > timeline.grade (per reel; "off" / null removes the base grade) > the theme's grade > tokens.grades.footage.
   timeline.grades[] = [{t, t1 | dur, grade | id, fade (s), freeze: true}] are events drawn ON TOP of the base: a graded
   copy of the footage (frozen at t when `freeze`) with an opacity envelope. Without `t1`/`dur` the event lasts the
   grade's own `frames` ([a, b] -> the mean) or 1 s. `blur: px` adds a blur pulse on the event's envelope (the footage
   layer; `frame: true` = the whole picture, graphics too: transitions.js); a blur-only event needs no grade (4 f default).
*/
(function (root, factory) {
  const m = factory();
  if (typeof module === "object" && module.exports) module.exports = m; else root.VEOS_GRADES = m;
})(typeof self !== "undefined" ? self : this, function () {
  "use strict";
  const isNum = v => typeof v === "number" && isFinite(v);
  const r4 = v => Math.round(v * 10000) / 10000;
  const cl = (x, a, b) => (x < a ? a : x > b ? b : x);
  const NUMK = ["lift", "gamma", "gain", "warmth", "saturation", "contrast", "brightness"];
  const OFF = v => v == null || v === false || v === "off" || v === "none" || v === "";

  function hexRgb(c) {
    const m = /^#([0-9a-f]{3}|[0-9a-f]{6})$/i.exec(String(c || "").trim());
    if (!m) return null;
    let h = m[1]; if (h.length === 3) h = h.split("").map(x => x + x).join("");
    return [0, 2, 4].map(i => parseInt(h.slice(i, i + 2), 16) / 255);
  }

  /* x -> normalised spec {id, css, num {lift..brightness}|null, bloom, vignette, tint {fill, blend, opacity}|null, frames}
     or null (no grade). T = resolved tokens (grades.scene, colours). Throws on an unknown id. */
  function norm(x, T, depth) {
    if (OFF(x)) return null;
    depth = depth || 0;
    if (depth > 4) throw new Error("grade presets nest too deeply");
    const scene = (T && T.grades && T.grades.scene) || {};
    if (typeof x === "string") {
      if (scene[x]) return Object.assign(norm(scene[x], T, depth + 1) || blank(), { id: x });
      if (/\(/.test(x)) return Object.assign(blank(), { css: x.trim() });
      throw new Error(`unknown grade '${x}' (tokens.grades.scene: ${Object.keys(scene).join(", ") || "none"})`);
    }
    if (typeof x !== "object") throw new Error(`grade must be an id, a CSS filter list or an object (got ${typeof x})`);
    const base = x.preset ? (norm(x.preset, T, depth + 1) || blank()) : blank();
    const o = Object.assign({}, base, { id: x.id || base.id || null });
    const num = Object.assign({}, base.num || {});
    let any = false;
    for (const k of NUMK) if (isNum(x[k])) { num[k] = x[k]; any = true; }
    const css = x.filter != null ? x.filter : x.css != null ? x.css : null;
    if (css != null && String(css).trim() && String(css).trim() !== "none") o.css = String(css).trim();
    else if (css === "none") o.css = null;
    if (any || base.num) o.num = num;
    if (o.num && o.css) { if (x.prefer === "filter") o.num = null; else o.css = null; }
    if (isNum(x.bloom)) o.bloom = cl(x.bloom, 0, 1);
    if (isNum(x.vignette)) o.vignette = cl(x.vignette, 0, 1);
    if (x.blend && x.fill) {
      const fill = (T && T.colours && T.colours[x.fill]) || x.fill;
      o.tint = { fill, blend: String(x.blend), opacity: isNum(x.opacity) ? cl(x.opacity, 0, 1) : 1 };
    }
    if (Array.isArray(x.frames) && x.frames.length === 2 && x.frames.every(isNum)) o.frames = Math.round((x.frames[0] + x.frames[1]) / 2);
    else if (isNum(x.frames)) o.frames = Math.round(x.frames);
    return o;
  }
  function blank() { return { id: null, css: null, num: null, bloom: 0, vignette: 0, tint: null, frames: null }; }
  function isIdentity(s) {
    if (!s) return true;
    const n = s.num;
    const numId = !n || ((n.lift || 0) === 0 && (n.gamma == null || n.gamma === 1) && (n.gain == null || n.gain === 1) &&
      !(n.warmth) && (n.saturation == null || n.saturation === 1) && (n.contrast == null || n.contrast === 1) && (n.brightness == null || n.brightness === 1));
    return numId && !s.css && !(s.bloom > 0) && !(s.vignette > 0) && !s.tint;
  }
  /* does the spec need an SVG filter (numbers, bloom, vignette, tint)? spatial false = colour only */
  function needsSvg(s, spatial) {
    if (!s) return false;
    return !!(s.num || s.tint || (spatial !== false && (s.bloom > 0 || s.vignette > 0)));
  }

  /* SVG <filter> markup. o: {spatial (default true), rect: [x, y, w, h] the window in the image's own px (vignette)} */
  function svg(id, s, o) {
    o = o || {};
    const spatial = o.spatial !== false;
    let f = "", last = "SourceGraphic", k = 0;
    const step = (body, resName) => { const r = resName || `g${k++}`; f += body.replace("%IN%", last).replace("%OUT%", r); last = r; return r; };
    const n = s.num;
    if (n) {
      const lift = isNum(n.lift) ? n.lift : 0, gain = isNum(n.gain) ? n.gain : 1, gamma = isNum(n.gamma) && n.gamma > 0 ? n.gamma : 1;
      const bri = isNum(n.brightness) ? n.brightness : 1;
      if (lift !== 0 || gain !== 1 || gamma !== 1 || bri !== 1) {
        const amp = r4((gain - lift) * bri), ex = r4(1 / gamma), off = r4(lift * bri);
        const fn = c => `<feFunc${c} type="gamma" amplitude="${amp}" exponent="${ex}" offset="${off}"/>`;
        step(`<feComponentTransfer in="%IN%" result="%OUT%">${fn("R")}${fn("G")}${fn("B")}</feComponentTransfer>`);
      }
      if (isNum(n.warmth) && n.warmth !== 0) {
        const w = cl(n.warmth, -1, 1), rr = r4(1 + 0.5 * w), gg = r4(1 + 0.1 * w), bb = r4(1 - 0.5 * w);
        step(`<feColorMatrix in="%IN%" type="matrix" values="${rr} 0 0 0 0 0 ${gg} 0 0 0 0 0 ${bb} 0 0 0 0 0 1 0" result="%OUT%"/>`);
      }
      if (isNum(n.saturation) && n.saturation !== 1) step(`<feColorMatrix in="%IN%" type="saturate" values="${r4(Math.max(0, n.saturation))}" result="%OUT%"/>`);
      if (isNum(n.contrast) && n.contrast !== 1) {
        const c = r4(n.contrast), b = r4(0.5 - 0.5 * n.contrast), fn = ch => `<feFunc${ch} type="linear" slope="${c}" intercept="${b}"/>`;
        step(`<feComponentTransfer in="%IN%" result="%OUT%">${fn("R")}${fn("G")}${fn("B")}</feComponentTransfer>`);
      }
    }
    if (s.tint) { // the fill blended onto the picture (color / saturation / multiply...), mixed back at `opacity`
      const t = s.tint, rgb = hexRgb(t.fill) || [0.5, 0.5, 0.5];
      const src = last;
      f += `<feFlood flood-color="rgb(${rgb.map(v => Math.round(v * 255)).join(",")})" result="tf"/>`;
      f += `<feBlend in="tf" in2="${src}" mode="${t.blend}" result="tb"/>`;
      const a = r4(t.opacity);
      step(`<feComposite in="tb" in2="${src}" operator="arithmetic" k1="0" k2="${a}" k3="${r4(1 - a)}" k4="0" result="%OUT%"/>`);
    }
    if (spatial && s.bloom > 0) {
      const b = s.bloom, sl = r4(2.4 * b), ic = r4(-2.4 * b * 0.55), src = last;
      f += `<feGaussianBlur in="${src}" stdDeviation="${r4(10 + 16 * b)}" edgeMode="duplicate" result="bb"/>`;
      f += `<feComponentTransfer in="bb" result="bh"><feFuncR type="linear" slope="${sl}" intercept="${ic}"/><feFuncG type="linear" slope="${sl}" intercept="${ic}"/><feFuncB type="linear" slope="${sl}" intercept="${ic}"/></feComponentTransfer>`;
      step(`<feBlend in="bh" in2="${src}" mode="screen" result="%OUT%"/>`);
    }
    if (spatial && s.vignette > 0) {
      const R = o.rect || [0, 0, 1080, 1920], v = r4(Math.min(1, s.vignette) * 0.85);
      const e = Math.round(255 * (1 - v));
      const g = `<svg xmlns='http://www.w3.org/2000/svg' width='${Math.max(1, Math.round(R[2]))}' height='${Math.max(1, Math.round(R[3]))}'><defs><radialGradient id='v' cx='50%' cy='46%' r='75%'><stop offset='0.42' stop-color='white'/><stop offset='1' stop-color='rgb(${e},${e},${e})'/></radialGradient></defs><rect width='100%' height='100%' fill='url(#v)'/></svg>`;
      f += `<feImage href="data:image/svg+xml;charset=utf-8,${encodeURIComponent(g)}" x="${r4(R[0])}" y="${r4(R[1])}" width="${r4(R[2])}" height="${r4(R[3])}" preserveAspectRatio="none" result="vg"/>`;
      step(`<feBlend in="vg" in2="${last}" mode="multiply" result="%OUT%"/>`);
    }
    if (last === "SourceGraphic") return "";
    f += `<feComposite in="${last}" in2="SourceAlpha" operator="in"/>`; // keep the image's own alpha (cut-out silhouette)
    return `<filter id="${id}" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB">${f}</filter>`;
  }

  /* -> {css: "filter function list" (no `filter:`), def: svg filter markup or ""} */
  function filterOf(s, id, o) {
    if (!s || isIdentity(s)) return { css: "", def: "" };
    const def = needsSvg(s, o && o.spatial) ? svg(id, s, o) : "";
    const css = [s.css || "", def ? `url(#${id})` : ""].filter(Boolean).join(" ");
    return { css, def };
  }

  /* timeline.grades[] -> [{f0, f1, fade, spec, freeze}] (frames; f1 exclusive). Throws with the event index. */
  function compile(TL, T, fps) {
    fps = fps || 30;
    const out = [];
    (TL && Array.isArray(TL.grades) ? TL.grades : []).forEach((e, i) => {
      if (!e || typeof e !== "object" || !isNum(e.t)) throw new Error(`timeline.grades[${i}] needs {t, grade} (edit seconds)`);
      let spec;
      try { spec = norm(e.grade != null ? e.grade : e.id, T); } catch (err) { throw new Error(`timeline.grades[${i}]: ${err.message}`); }
      const blur = isNum(e.blur) && e.blur > 0 ? e.blur : 0; // a blur pulse (transitions.js): footage, or the whole picture with frame: true
      if (!spec && !blur) return;
      const f0 = Math.round(e.t * fps);
      const f1 = isNum(e.t1) ? Math.round(e.t1 * fps) : isNum(e.dur) ? f0 + Math.max(1, Math.round(e.dur * fps)) : f0 + ((spec && spec.frames) || (spec ? fps : 4));
      if (f1 <= f0) throw new Error(`timeline.grades[${i}]: t1 must be after t`);
      const ev = { f0, f1, fade: Math.max(0, Math.round((isNum(e.fade) ? e.fade : 0) * fps)), spec, freeze: e.freeze === true || !!(spec && spec.freeze === true), i };
      if (blur) { ev.blur = blur; ev.frame = e.frame === true; }
      out.push(ev);
    });
    return out.sort((a, b) => a.f0 - b.f0);
  }
  /* active events at frame n with their opacity (fade in and out over `fade` frames) */
  function eventsAt(EV, n) {
    const out = [];
    for (const e of EV) {
      if (n < e.f0 || n >= e.f1) continue;
      let op = 1;
      if (e.fade > 0) op = Math.min(1, (n - e.f0 + 1) / (e.fade + 1), (e.f1 - n) / (e.fade + 1));
      out.push({ ev: e, op: cl(op, 0, 1) });
    }
    return out;
  }
  /* the base grade source at frame n: scene > world > timeline.grade > theme > grades.footage. Each `T`-level spec is
     normalised once by the caller (ctx = {scene, world, reel, reelSet, theme, footage}); returns {spec, from} */
  function pick(c) {
    if (c.scene) return { spec: c.scene, from: "scene" };
    if (c.world) return { spec: c.world, from: "world" };
    if (c.reelSet) return { spec: c.reel, from: "timeline" };
    if (c.theme) return { spec: c.theme, from: "theme" };
    if (c.footage) return { spec: c.footage, from: "footage" };
    return { spec: null, from: null };
  }
  return { norm, isIdentity, needsSvg, svg, filterOf, compile, eventsAt, pick, OFF };
});
