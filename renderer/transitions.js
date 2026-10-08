/* Vibe Editing OS footage blur + built-in transitions (Package A). Pure maths, no DOM: loaded by player.html before
   core.js (window.VEOS_TRANSITIONS) and by node in the engine tests (module.exports). core.js turns the per-frame
   descriptions below into DOM (SVG blur filters, scaled copies, masks, overlays); engine/src/veos/fxrules.py mirrors
   check() for `veos validate` (V-FX, V-FLASH).

   1. Footage blur ("stage blur"): blurs the stage only (the footage window, its cut-out and breakout, second sources,
      the band backdrop and z1 plate scenes); graphics z2+ and captions stay sharp. A blur envelope:
        {kind: "defocus" | "directional" | "radial", px (defocus / directional smear, default 12), angle (directional,
         degrees, 0 = horizontal), amount (radial: the zoom spread, 0.12 = copies up to 1.12x), at: "face" | [x, y]
         (radial centre, default the frame centre), frames (default 8), shape: "pulse" | "decay" | "rise" | "hold",
         keys: [[frame, 0..1], ...] (a per-frame multiplier of px / amount; overrides frames + shape)}
      Sources: timeline.blur [{t, ...envelope}], camera events `blur: {...}` (or `p.blur`, or the preset's own
      `camera_presets.<id>.blur`; frames default to the move's frames, shape "pulse"), timeline.grades[] `blur: px`
      (a defocus pulse on the grade event's fade envelope) and transitions with `layers: "stage"`.
   2. Built-in transitions: timeline.transitions[] entries WITH a `type` (entries without one stay markers):
        {t (the cut, edit s), type, frames, pre (frames before the cut), layers: "picture" | "stage" | "all", ...}
      "picture" (default) = everything under the captions (world, footage, scenes z1-6); "all" adds captions and z7+.
   3. Frame blur pulse: timeline.grades[] `blur: px, frame: true` blurs the whole picture (graphics too).
   4. timeline.end_fade: frames (or {frames, colour}) to black at the end of the reel, over everything.
*/
(function (root, factory) {
  const m = factory();
  if (typeof module === "object" && module.exports) module.exports = m; else root.VEOS_TRANSITIONS = m;
})(typeof self !== "undefined" ? self : this, function () {
  "use strict";
  const isNum = v => typeof v === "number" && isFinite(v);
  const cl = (x, a, b) => (x < a ? a : x > b ? b : x);
  const r3 = v => Math.round(v * 1000) / 1000;
  const HASH = (i, j) => { const x = Math.sin(i * 127.1 + j * 311.7 + 0.5) * 43758.5453; return x - Math.floor(x); };
  const HEX = /^#([0-9a-f]{3}|[0-9a-f]{6})$/i;

  /* ------------------------------------------------------------------------------------------ declarations */
  // per type: default frames, frames before the cut, and whether it needs the outgoing frame (two-source, frozen at c-1)
  const TYPES = {
    "flash": { frames: 7, pre: 2 },
    "leak": { frames: 16, pre: 9 },
    "blur-through": { frames: 10, pre: 5 },
    "zoom-blur": { frames: 8, pre: 4 },
    "whip": { frames: 8, pre: 4, two: true },
    "glitch": { frames: 6, pre: 3 },
    "burn": { frames: 14, pre: 2, two: true },
    "iris": { frames: 10, pre: 0, two: true },
    "curtain": { frames: 12, pre: 0, two: true },
    "push": { frames: 12, pre: 0, two: true },
  };
  const LUMINOUS = ["flash", "leak", "burn"]; // full-frame luminance changes (no limit: a style may flash freely)
  const KINDS = ["defocus", "directional", "radial"], SHAPES = ["pulse", "decay", "rise", "hold"];
  const LAYERS = ["picture", "stage", "all"];
  const DIRS = ["left", "right", "up", "down"];
  const BLENDS = ["light", "normal", "screen", "add"], CLEARS = ["fade", "wipe"]; // flash: how it lights the picture, how it clears
  // allowed numeric params per type: [min, max]
  const NUM = {
    common: { frames: [1, 90], pre: [0, 90] },
    flash: { peak: [0, 1], decay: [0.2, 6], clear_frames: [1, 90], feather: [0, 960] },
    leak: { peak: [0, 1], angle: [-360, 360] },
    "blur-through": { px: [0, 80] },
    "zoom-blur": { amount: [0, 0.6], punch: [0, 0.4] },
    whip: { angle: [-360, 360], px: [0, 200], travel: [0, 1080], blend: [0, 6] },
    glitch: { slices: [0, 16], offset: [0, 300], rgb: [0, 60], posterize: [0, 16], seed: [-1e9, 1e9] },
    burn: { peak: [0, 1], ring: [0, 400] },
    iris: { ring: [0, 240], feather: [0, 200] },
    curtain: {},
    push: {},
  };
  const ENV_NUM = { px: [0, 80], angle: [-360, 360], amount: [0, 0.6], frames: [1, 300] };

  /* a blur envelope -> list of problems (strings) */
  function checkEnv(b, where) {
    const out = [];
    if (!b || typeof b !== "object" || Array.isArray(b)) return [`${where} must be an object {kind, px | amount, frames, shape | keys}`];
    if (b.kind != null && !KINDS.includes(b.kind)) out.push(`${where}.kind '${b.kind}' is not one of ${KINDS.join(" | ")}`);
    if (b.shape != null && !SHAPES.includes(b.shape)) out.push(`${where}.shape '${b.shape}' is not one of ${SHAPES.join(" | ")}`);
    for (const k of Object.keys(ENV_NUM)) if (b[k] != null && !(isNum(b[k]) && b[k] >= ENV_NUM[k][0] && b[k] <= ENV_NUM[k][1])) out.push(`${where}.${k} must be a number ${ENV_NUM[k][0]}..${ENV_NUM[k][1]}`);
    if (b.at != null && !(b.at === "face" || b.at === "centre" || (Array.isArray(b.at) && b.at.length === 2 && b.at.every(isNum)))) out.push(`${where}.at must be "face", "centre" or [x, y]`);
    if (b.keys != null && !(Array.isArray(b.keys) && b.keys.length && b.keys.every(k => Array.isArray(k) && k.length === 2 && isNum(k[0]) && k[0] >= 0 && isNum(k[1]) && k[1] >= 0 && k[1] <= 1))) out.push(`${where}.keys must be [[frame >= 0, 0..1], ...]`);
    return out;
  }
  /* one transitions[] entry -> list of problems; entries without `type` are markers (always fine here) */
  function checkTransition(tr, i) {
    const w = `timeline.transitions[${i}]`, out = [];
    if (!tr || typeof tr !== "object" || tr.type == null) return out;
    if (!TYPES[tr.type]) return [`${w}.type '${tr.type}' is not a built-in transition (${Object.keys(TYPES).join(" | ")})`];
    if (!isNum(tr.t) || tr.t < 0) out.push(`${w} needs t (the cut, edit seconds >= 0)`);
    const lim = Object.assign({}, NUM.common, NUM[tr.type]);
    for (const k of Object.keys(lim)) if (tr[k] != null && !(isNum(tr[k]) && tr[k] >= lim[k][0] && tr[k] <= lim[k][1])) out.push(`${w}.${k} must be a number ${lim[k][0]}..${lim[k][1]}`);
    const fr = tr.frames != null ? tr.frames : TYPES[tr.type].frames;
    if (isNum(tr.pre) && isNum(fr) && tr.pre > fr) out.push(`${w}.pre (${tr.pre}) must not exceed frames (${fr})`);
    if (tr.layers != null && !LAYERS.includes(tr.layers)) out.push(`${w}.layers '${tr.layers}' is not one of ${LAYERS.join(" | ")}`);
    if (tr.layers === "stage" && !["blur-through", "zoom-blur", "whip"].includes(tr.type)) out.push(`${w}.layers "stage" only applies to blur-through, zoom-blur and whip`);
    for (const k of ["colour", "color"]) if (tr[k] != null && typeof tr[k] !== "string") out.push(`${w}.${k} must be a hex colour or a colour role`);
    if (tr.colours != null && !(Array.isArray(tr.colours) && tr.colours.length >= 2 && tr.colours.length <= 5 && tr.colours.every(c => typeof c === "string"))) out.push(`${w}.colours must be 2-5 hex colours or roles`);
    if (tr.dir != null && !DIRS.includes(tr.dir)) out.push(`${w}.dir '${tr.dir}' is not one of ${DIRS.join(" | ")}`);
    if (tr.type === "flash" && tr.blend != null && !BLENDS.includes(tr.blend)) out.push(`${w}.blend '${tr.blend}' is not one of ${BLENDS.join(" | ")}`);
    if (tr.type === "flash" && tr.clear != null && !CLEARS.includes(tr.clear)) out.push(`${w}.clear '${tr.clear}' is not one of ${CLEARS.join(" | ")}`);
    if (tr.type === "iris" && tr.reveal != null && !["next", "open"].includes(tr.reveal)) out.push(`${w}.reveal must be "next" (the old shot collapses in a circle) or "open"`);
    if (tr.at != null && !(tr.at === "face" || tr.at === "centre" || (Array.isArray(tr.at) && tr.at.length === 2 && tr.at.every(isNum)))) out.push(`${w}.at must be "face", "centre" or [x, y]`);
    if (tr.slide != null && typeof tr.slide !== "boolean") out.push(`${w}.slide must be true or false`);
    return out;
  }
  /* the whole timeline (+ tokens camera presets) -> list of problems */
  function check(TL, T) {
    const out = [];
    (Array.isArray(TL.transitions) ? TL.transitions : []).forEach((tr, i) => out.push(...checkTransition(tr, i)));
    if (TL.blur != null) {
      if (!Array.isArray(TL.blur)) out.push("timeline.blur must be a list [{t, kind, px | amount, frames, ...}]");
      else TL.blur.forEach((b, i) => { if (!b || !isNum(b.t)) out.push(`timeline.blur[${i}] needs t (edit seconds)`); out.push(...checkEnv(b, `timeline.blur[${i}]`)); });
    }
    (Array.isArray(TL.camera) ? TL.camera : []).forEach((c, i) => {
      const b = c && (c.blur != null ? c.blur : c.p && c.p.blur);
      if (b != null) out.push(...checkEnv(b, `timeline.camera[${i}].blur`));
    });
    const P = (T && T.camera_presets) || {};
    for (const id of Object.keys(P)) if (P[id] && P[id].blur != null) out.push(...checkEnv(P[id].blur, `camera_presets.${id}.blur`));
    (Array.isArray(TL.grades) ? TL.grades : []).forEach((g, i) => {
      if (!g) return;
      if (g.blur != null && !(isNum(g.blur) && g.blur >= 0 && g.blur <= 60)) out.push(`timeline.grades[${i}].blur must be px 0..60`);
      if (g.frame != null && typeof g.frame !== "boolean") out.push(`timeline.grades[${i}].frame must be true or false`);
    });
    if (TL.end_fade != null) {
      const ef = TL.end_fade, fr = isNum(ef) ? ef : ef && ef.frames;
      if (!(isNum(fr) && Math.round(fr) === fr && fr >= 1 && fr <= 300)) out.push("timeline.end_fade must be frames 1..300 (or {frames, colour})");
      if (ef && typeof ef === "object" && ef.colour != null && typeof ef.colour !== "string") out.push("timeline.end_fade.colour must be a hex colour or a role");
    }
    return out;
  }

  /* ------------------------------------------------------------------------------------------ compile */
  const PLAIN = { EO: x => 1 - Math.pow(1 - x, 3), EI: x => x * x * x, EIO: x => (x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2) };
  /* timeline -> {trs, blurs, end}. fps 30; E = {EO, EI, EIO} (core passes the token eases). Throws the check() list. */
  function compile(TL, T, fps, E) {
    TL = TL || {}; fps = fps || 30;
    const errs = check(TL, T);
    if (errs.length) throw new Error(errs.join("; "));
    const f = t => Math.round(t * fps);
    const trs = [];
    (Array.isArray(TL.transitions) ? TL.transitions : []).forEach((tr, i) => {
      if (!tr || tr.type == null) return;
      const D = TYPES[tr.type], frames = Math.round(tr.frames != null ? tr.frames : D.frames), pre = Math.round(cl(tr.pre != null ? tr.pre : Math.min(D.pre, frames), 0, frames));
      const c = f(tr.t);
      trs.push({ i, type: tr.type, c, a: c - pre, b: c - pre + frames, pre, post: frames - pre, two: !!D.two, layers: tr.layers || "picture", p: tr, limit: 1 });
    });
    trs.sort((x, y) => x.a - y.a);
    const blurs = [];
    (Array.isArray(TL.blur) ? TL.blur : []).forEach(b => blurs.push({ f0: f(b.t), env: b }));
    const P = (T && T.camera_presets) || {};
    (Array.isArray(TL.camera) ? TL.camera : []).forEach(c => {
      if (!c) return;
      const pr = P[c.preset] || {}, b = c.blur != null ? c.blur : (c.p && c.p.blur != null ? c.p.blur : pr.blur);
      if (b == null || b === false) return;
      let fr = c.p && c.p.frames != null ? c.p.frames : pr.frames;
      if (Array.isArray(fr)) fr = Math.round((fr[0] + fr[1]) / 2);
      blurs.push({ f0: f(c.t), env: Object.assign({ frames: isNum(fr) ? fr : 8, shape: "pulse" }, b) });
    });
    let end = null;
    if (TL.end_fade != null) end = { frames: Math.round(isNum(TL.end_fade) ? TL.end_fade : TL.end_fade.frames), colour: (TL.end_fade && TL.end_fade.colour) || "#000000" };
    return { trs, blurs, end, E: Object.assign({}, PLAIN, E || {}), fps };
  }

  /* ------------------------------------------------------------------------------------------ blur envelopes */
  /* the 0..1 multiplier of an envelope k frames after its start, or 0 */
  function envAt(env, k) {
    if (k < 0) return 0;
    if (Array.isArray(env.keys) && env.keys.length) {
      const ks = env.keys.slice().sort((a, b) => a[0] - b[0]), last = ks[ks.length - 1];
      if (k > last[0]) return 0;
      if (k <= ks[0][0]) return ks[0][1];
      for (let j = 1; j < ks.length; j++) if (k <= ks[j][0]) { const a = ks[j - 1], b = ks[j], q = (k - a[0]) / Math.max(1e-6, b[0] - a[0]); return a[1] + (b[1] - a[1]) * q; }
      return 0;
    }
    const N = Math.max(1, Math.round(env.frames != null ? env.frames : 8));
    if (k >= N) return 0;
    switch (env.shape || "pulse") {
      case "decay": return 1 - k / N;
      case "rise": return (k + 1) / N;
      case "hold": return 1;
      default: return Math.sin(Math.PI * (k + 1) / (N + 1));
    }
  }
  const NONE = () => ({ defocus: 0, dir: null, radial: null });
  /* merge one blur component into an accumulator (defocus adds, directional / radial keep the stronger) */
  function addBlur(acc, kind, v, o) {
    if (!(v > 0)) return acc;
    if (kind === "directional") { if (!acc.dir || v > acc.dir.px) acc.dir = { px: r3(v), angle: o.angle || 0 }; }
    else if (kind === "radial") { if (!acc.radial || v > acc.radial.amount) acc.radial = { amount: r3(v), at: o.at || "centre" }; }
    else acc.defocus = r3(acc.defocus + v);
    return acc;
  }
  const isBlur = b => !!b && (b.defocus > 0.05 || (b.dir && b.dir.px > 0.3) || (b.radial && b.radial.amount > 0.002));
  /* the stage (footage) blur at frame n: {defocus, dir {px, angle}, radial {amount, at}} or null.
     extra: [{kind, v, ...}] from core (grade-event pulses). Transitions with layers "stage" add their blur part. */
  function stageBlurAt(C, n, extra) {
    const acc = NONE();
    for (const b of C.blurs) {
      const m = envAt(b.env, n - b.f0); if (!(m > 0)) continue;
      const kind = b.env.kind || "defocus";
      addBlur(acc, kind, m * (kind === "radial" ? (b.env.amount != null ? b.env.amount : 0.12) : (b.env.px != null ? b.env.px : 12)), b.env);
    }
    for (const x of extra || []) addBlur(acc, x.kind || "defocus", x.v, x);
    for (const tr of C.trs) if (tr.layers === "stage" && n >= tr.a && n < tr.b) { const d = trFx(C, tr, n); if (d.blur) mergeInto(acc, d.blur); }
    return isBlur(acc) ? acc : null;
  }
  function mergeInto(acc, b) {
    if (!b) return acc;
    addBlur(acc, "defocus", b.defocus, {});
    if (b.dir) addBlur(acc, "directional", b.dir.px, b.dir);
    if (b.radial) addBlur(acc, "radial", b.radial.amount, b.radial);
    return acc;
  }

  /* ------------------------------------------------------------------------------------------ transitions */
  /* intensity around the cut: rises over `pre` frames, 1 on the cut frame, falls over `post` frames */
  function inten(tr, n, decay) {
    if (n < tr.c) return (n - tr.a + 1) / (tr.pre + 1);
    if (tr.post <= 0) return 0;
    return Math.pow(1 - (n - tr.c) / tr.post, decay || 1);
  }
  const vIn = (tr, n) => (tr.post <= 0 ? 1 : cl((n - tr.c + 1) / tr.post, 0, 1)); // progress of the after-cut part, 1 on its last frame
  /* a white or near-white hex colour (Rec. 709 luma >= 0.85): the flash defaults to the light blend. Roles stay "normal". */
  const isLight = c => { if (!HEX.test(String(c))) return false; let h = String(c).slice(1); if (h.length === 3) h = h.replace(/./g, x => x + x);
    const v = [0, 2, 4].map(i => parseInt(h.slice(i, i + 2), 16) / 255); return 0.2126 * v[0] + 0.7152 * v[1] + 0.0722 * v[2] >= 0.85; };
  const dirVec = (d, ang) => { if (d) return { left: [-1, 0], right: [1, 0], up: [0, -1], down: [0, 1] }[d]; const a = (ang || 0) * Math.PI / 180; return [Math.cos(a), Math.sin(a)]; };
  /* one transition at frame n -> its frame description (see frameFx) */
  function trFx(C, tr, n) {
    const p = tr.p, E = C.E, d = { blur: null, move: null, clip: null, filter: null, other: null, overlays: [], glitch: null };
    const I = inten(tr, n, 1), after = n >= tr.c;
    switch (tr.type) {
      case "flash": {
        const peak = (p.peak != null ? p.peak : 0.85) * tr.limit, decay = p.decay != null ? p.decay : 1.6, colour = p.colour || p.color || "#FFFFFF";
        const blend = p.blend || (isLight(colour) ? "light" : "normal");
        // a flash that ends on the cut (post 0) reaches its peak on its last frame (it used to stop one step short)
        const Ipre = tr.post <= 0 ? (n - tr.a + 1) / Math.max(1, tr.pre) : I;
        let op = after ? peak * inten(tr, n, decay) : peak * E.EI(cl(Ipre, 0, 1)), wipe = null;
        if (after && p.clear === "wipe") { // full on the cut, then it clears top -> bottom (dir) over clear_frames and is gone
          const cf = Math.max(1, Math.round(p.clear_frames != null ? p.clear_frames : tr.post - 1)), j = n - tr.c;
          op = j > cf ? 0 : peak;
          if (j > 0) wipe = { dir: p.dir || "down", r: r3(j / (cf + 1)), feather: p.feather != null ? p.feather : 160 };
        }
        if (op > 0.003) d.overlays.push(Object.assign({ kind: "fill", colour, op: r3(op) }, blend !== "normal" ? { blend } : {}, wipe ? { wipe } : {}));
        break;
      }
      case "leak": {
        const peak = (p.peak != null ? p.peak : 0.9) * tr.limit, q = (n - tr.a + 0.5) / (tr.b - tr.a);
        const cols = p.colours || ["#E6902A", "#FCF88B", "#FFFDE0", "#C04129"];
        d.overlays.push({ kind: "leak", colours: cols, angle: p.angle != null ? p.angle : 35, pos: r3(-40 + 180 * E.EIO(q)), op: r3(peak * Math.sin(Math.PI * cl(I, 0, 1) / 2)), wash: r3(0.35 * peak * I) });
        break;
      }
      case "blur-through": d.blur = { defocus: r3((p.px != null ? p.px : 24) * E.EIO(cl(I, 0, 1))), dir: null, radial: null }; break;
      case "zoom-blur": {
        const amt = (p.amount != null ? p.amount : 0.15) * I, punch = p.punch != null ? p.punch : 0.06;
        d.blur = { defocus: 0, dir: null, radial: { amount: r3(amt), at: p.at || "centre" } };
        d.move = { x: 0, y: 0, s: r3(1 + punch * E.EI(cl(I, 0, 1))), at: p.at || "centre" };
        break;
      }
      case "whip": {
        const v = dirVec(p.dir, p.angle), travel = p.travel != null ? p.travel : 160, px = p.px != null ? p.px : 60, blend = Math.round(p.blend != null ? p.blend : 2);
        const ang = Math.atan2(v[1], v[0]) * 180 / Math.PI;
        // out: the picture accelerates along the whip; in: the next shot arrives from the opposite side and settles
        const off = after ? -travel * E.EI(I) : travel * E.EI(I);
        d.move = { x: r3(v[0] * off), y: r3(v[1] * off), s: 1 };
        d.blur = { defocus: 0, dir: { px: r3(px * I), angle: r3(ang) }, radial: null };
        if (after && n - tr.c < blend) { const j = n - tr.c + 1, o = travel * (1 + j / Math.max(1, tr.post)); d.other = { n: tr.c - 1, pos: "over", op: r3(1 - j / (blend + 1)), move: { x: r3(v[0] * o), y: r3(v[1] * o), s: 1 }, blur: { defocus: 0, dir: { px: r3(px), angle: r3(ang) }, radial: null } }; }
        break;
      }
      case "glitch": {
        const N = Math.round(p.slices != null ? p.slices : 7), off = p.offset != null ? p.offset : 60, seed = p.seed != null ? p.seed : tr.i * 17 + 3, slices = [];
        for (let k = 0; k < N; k++) {
          const y = HASH(seed + k * 3, n) * 1920, h = 20 + HASH(seed + k * 5, n + 1) * 160, s = HASH(seed + k * 7, n + 2) * 2 - 1;
          slices.push({ y: r3(y), h: r3(h), dx: r3(s * off * I) });
        }
        d.glitch = { slices, rgb: r3((p.rgb != null ? p.rgb : 12) * I), levels: I > 0.45 ? Math.round(p.posterize != null ? p.posterize : 4) : 0 };
        break;
      }
      case "burn": {
        const peak = (p.peak != null ? p.peak : 1) * tr.limit, colour = p.colour || p.color || "#FF6A00";
        if (!after) { d.filter = { burn: r3(0.6 * I * peak) }; break; }
        const v = vIn(tr, n), e = E.EIO(v), ring = p.ring != null ? p.ring : 140;
        d.other = { n: tr.c - 1, pos: "over", op: 1, hole: { r: r3(e), ring, at: p.at || "centre" }, filter: { burn: r3(peak * (0.6 + 0.4 * v)) } };
        d.overlays.push({ kind: "ring", colour, r: r3(e), ring, at: p.at || "centre", op: r3(peak * Math.sin(Math.PI * cl(v, 0, 1)) * 0.9) });
        break;
      }
      case "iris": {
        if (!after) break;
        const e = E.EIO(vIn(tr, n)), reveal = p.reveal || "next", feather = p.feather != null ? p.feather : 2, at = p.at || "centre";
        if (reveal === "next") d.other = { n: tr.c - 1, pos: "over", op: 1, circle: { r: r3(1 - e), feather, at } };
        else { d.other = { n: tr.c - 1, pos: "under", op: 1 }; d.circle = { r: r3(e), feather, at }; }
        if (p.ring) d.overlays.push({ kind: "ring", colour: p.colour || p.color || "#FFFFFF", r: r3(reveal === "next" ? 1 - e : e), ring: p.ring, at, op: 1, hard: true });
        break;
      }
      case "curtain": {
        if (!after) break;
        const e = E.EIO(vIn(tr, n)), dir = p.dir || "down", slide = p.slide !== false;
        d.other = { n: tr.c - 1, pos: "under", op: 1 };
        d.curtain = { dir, e: r3(e), slide };
        break;
      }
      case "push": {
        if (!after) break;
        const e = E.EIO(vIn(tr, n)), v = dirVec(p.dir || "left");
        // the old frame (footage window and world together) leaves along dir; the new one follows it in
        d.other = { n: tr.c - 1, pos: "under", op: 1, move: { x: r3(v[0] * e * 1080), y: r3(v[1] * e * 1920), s: 1 } };
        d.move = { x: r3(-v[0] * (1 - e) * 1080), y: r3(-v[1] * (1 - e) * 1920), s: 1 };
        break;
      }
      default: break;
    }
    return d;
  }
  /* the frame description at n, or null (nothing to do):
     {layers: "picture" | "all", blur, move {x, y, s, at}, filter {burn}, circle, curtain, glitch, other {n, pos, op, move,
      blur, circle, hole, filter}, overlays [...], pulse: px (frame blur), fade {op, colour}}.
     pulses: [{v, frame}] grade-event blur pulses with frame: true (core reads them from grades.js). */
  function frameFx(C, n, pulses) {
    let d = null;
    const act = C.trs.filter(tr => tr.layers !== "stage" && n >= tr.a && n < tr.b);
    if (act.length) {
      const tr = act[0];
      d = trFx(C, tr, n); d.layers = tr.layers; d.type = tr.type;
      for (const x of act.slice(1)) d.overlays.push(...trFx(C, x, n).overlays); // overlapping transitions: only overlays stack
      // a two-source freeze shows the outgoing frame as it was: with the flash / leak that lit it on that frame
      if (d.other) {
        const m = d.other.n, lit = C.trs.filter(x => x !== tr && x.layers !== "stage" && (x.type === "flash" || x.type === "leak") && m >= x.a && m < x.b);
        const ov = [].concat(...lit.map(x => trFx(C, x, m).overlays));
        if (ov.length) d.other.overlays = ov;
      }
    }
    const pv = (pulses || []).reduce((m, x) => Math.max(m, x.v || 0), 0);
    if (pv > 0.05) { d = d || base(); d.blur = mergeInto(d.blur || NONE(), { defocus: pv }); }
    if (C.end && C.end.frames > 0) {
      const N = C.lastFrame != null ? C.lastFrame : null;
      if (N != null && n > N - C.end.frames) { d = d || base(); d.fade = { op: r3(cl((n - (N - C.end.frames)) / C.end.frames, 0, 1)), colour: C.end.colour }; }
    }
    if (d && d.blur && !isBlur(d.blur)) d.blur = null;
    if (d && !d.blur && !d.move && !d.filter && !d.circle && !d.curtain && !d.glitch && !d.other && !d.overlays.length && !d.fade) return null;
    return d;
  }
  const base = () => ({ layers: "picture", blur: null, move: null, clip: null, filter: null, other: null, overlays: [], glitch: null });

  /* ------------------------------------------------------------------------------------------ SVG / CSS builders */
  /* SVG filter for a defocus and/or directional blur. opaque: re-fill the alpha the blur pulled in at the edges (the
     colour is the average of the opaque neighbours: no dark halo at the frame or window edge). */
  function blurFilter(id, b, opaque) {
    let s = `<filter id="${id}" x="-25%" y="-25%" width="150%" height="150%" color-interpolation-filters="sRGB">`, last = "SourceGraphic", k = 0;
    if (b.dir && b.dir.px > 0.3) {
      const T = cl(Math.round(b.dir.px / 4), 3, 12), a = b.dir.angle * Math.PI / 180, ux = Math.cos(a), uy = Math.sin(a);
      for (let i = 0; i < T; i++) { const t = -b.dir.px / 2 + b.dir.px * i / (T - 1); s += `<feOffset in="SourceGraphic" dx="${r3(ux * t)}" dy="${r3(uy * t)}" result="o${i}"/>`; }
      s += `<feComposite in="o0" in2="o0" operator="arithmetic" k1="0" k2="${r3(1 / T)}" k3="0" k4="0" result="a0"/>`;
      for (let i = 1; i < T; i++) s += `<feComposite in="o${i}" in2="a${i - 1}" operator="arithmetic" k1="0" k2="${r3(1 / T)}" k3="1" k4="0" result="a${i}"/>`;
      const sm = r3(b.dir.px / T / 2);
      s += `<feGaussianBlur in="a${T - 1}" stdDeviation="${r3(Math.abs(ux) * sm + 0.3)} ${r3(Math.abs(uy) * sm + 0.3)}" result="d"/>`; last = "d"; k++;
    }
    if (b.defocus > 0.05) { s += `<feGaussianBlur in="${last}" stdDeviation="${r3(b.defocus)}" result="g"/>`; last = "g"; k++; }
    if (opaque) s += `<feComponentTransfer in="${last}"><feFuncA type="linear" slope="40" intercept="0"/></feComponentTransfer>`;
    return k ? s + "</filter>" : "";
  }
  /* SVG filter for the glitch: RGB split (px) + posterise (levels) */
  function glitchFilter(id, g) {
    let s = `<filter id="${id}" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB">`;
    const o = g.rgb;
    s += `<feOffset in="SourceGraphic" dx="${r3(-o)}" dy="0" result="o1"/><feColorMatrix in="o1" type="matrix" values="1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0" result="r"/>`;
    s += `<feColorMatrix in="SourceGraphic" type="matrix" values="0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 1 0" result="g"/>`;
    s += `<feOffset in="SourceGraphic" dx="${r3(o)}" dy="0" result="o3"/><feColorMatrix in="o3" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 1 0" result="b"/>`;
    s += `<feComposite in="r" in2="g" operator="arithmetic" k2="1" k3="1" result="rg"/><feComposite in="rg" in2="b" operator="arithmetic" k2="1" k3="1" result="rgb"/>`;
    if (g.levels >= 2) { const L = g.levels, tv = Array.from({ length: L }, (_, i) => r3(i / (L - 1))).join(" "); s += `<feComponentTransfer in="rgb"><feFuncR type="discrete" tableValues="${tv}"/><feFuncG type="discrete" tableValues="${tv}"/><feFuncB type="discrete" tableValues="${tv}"/></feComponentTransfer>`; }
    return s + "</filter>";
  }
  /* the burn treatment of a frame as CSS filter functions (k 0..1: posterised, hotter, hue-shifted) */
  const burnCss = k => (k > 0.01 ? `contrast(${r3(1 + 0.8 * k)}) saturate(${r3(1 + 1.2 * k)}) sepia(${r3(0.5 * k)}) hue-rotate(${r3(-25 * k)}deg) brightness(${r3(1 + 0.25 * k)})` : "");
  const maxR = (cx, cy) => Math.max(Math.hypot(cx, cy), Math.hypot(1080 - cx, cy), Math.hypot(cx, 1920 - cy), Math.hypot(1080 - cx, 1920 - cy));

  return { BLENDS, CLEARS, isLight, TYPES, LUMINOUS, KINDS, SHAPES, check, checkEnv, checkTransition, compile, envAt, stageBlurAt, frameFx, isBlur, blurFilter, glitchFilter, burnCss, maxR };
});
