/* Vibe Editing OS canvas camera (E-14, structure §21). Pure maths, no DOM: loaded by player.html before core.js
   (window.VEOS_CANVASCAM) and by node in the engine tests (module.exports). engine/src/veos/canvascam.py mirrors it
   number for number; keep the two in step (tests/test_canvascam.py runs both and compares).

   timeline.canvas_camera = [{t, move, to?, dur?, ease?, p?}]     edit seconds; moves C-1..C-5 (names below)
   timeline.canvas_nodes  = {id: {x, y, w, h}}                    world px (scenes may also carry `nodes: [{id,x,y,w,h}]`)
   timeline.canvas_home   = {x, y, s}                             optional resting view (default the frame: 540, 960, 1)

   The camera looks at world point (x, y) at zoom s and roll r (deg); that point lands on the frame centre (540, 960).
   A scene with parallax k (0..1) sees the camera scaled toward home: x_k = hx + (x - hx) k, s_k = s^k, r_k = r k.
*/
(function (root, factory) {
  const m = factory();
  if (typeof module === "object" && module.exports) module.exports = m; else root.VEOS_CANVASCAM = m;
})(typeof self !== "undefined" ? self : this, function () {
  "use strict";
  const W = 1080, H = 1920, FPS = 30, CX = W / 2, CY = H / 2;
  const cl = (x, a = 0, b = 1) => (x < a ? a : x > b ? b : x);
  const lerp = (a, b, p) => a + (b - a) * p;
  function bez(x1, y1, x2, y2) {
    return x => {
      if (x <= 0) return 0; if (x >= 1) return 1; let t = x;
      for (let i = 0; i < 12; i++) {
        const u = 1 - t, f = 3 * x1 * t * u * u + 3 * x2 * t * t * u + t * t * t - x; if (Math.abs(f) < 1e-9) break;
        const d = 3 * x1 * u * u + 6 * (x2 - x1) * t * u + 3 * (1 - x2) * t * t; if (Math.abs(d) < 1e-9) break; t = cl(t - f / d);
      }
      const u = 1 - t; return 3 * y1 * t * u * u + 3 * y2 * t * t * u + t * t * t;
    };
  }
  /* fixed curves (not from tokens) so the Python mirror and the validator see exactly what is rendered */
  const EASE = {
    inOut: bez(0.65, 0, 0.35, 1), out: bez(0.25, 0.46, 0.45, 0.94), in: bez(0.55, 0.055, 0.675, 0.19),
    sine: bez(0.37, 0, 0.63, 1), linear: x => cl(x),
    // camera v2: exponential curves (a snap push lands ~80 % of its zoom in the middle third; an expo settle)
    expoInOut: x => (x <= 0 ? 0 : x >= 1 ? 1 : x < 0.5 ? Math.pow(2, 20 * x - 10) / 2 : (2 - Math.pow(2, 10 - 20 * x)) / 2),
    expoOut: x => (x <= 0 ? 0 : x >= 1 ? 1 : 1 - Math.pow(2, -10 * x)),
  };
  /* move name -> [code, kind]. §21: C-1 push to node, C-2 pull out, C-3 pan / drift, C-4 zoom-through, C-5 orbit.
     Aliases: zoom-in = push, zoom-out = pull, settle = pull back to home, dolly = pan between nodes with a pull-back arc. */
  const MOVES = {
    "C-1": ["C-1", "push"], push: ["C-1", "push"], "zoom-in": ["C-1", "push"],
    "C-2": ["C-2", "pull"], pull: ["C-2", "pull"], "zoom-out": ["C-2", "pull"], settle: ["C-2", "settle"],
    "C-3": ["C-3", "pan"], pan: ["C-3", "pan"], drift: ["C-3", "drift"], dolly: ["C-3", "dolly"],
    "C-4": ["C-4", "zoom-through"], "zoom-through": ["C-4", "zoom-through"],
    "C-5": ["C-5", "orbit"], orbit: ["C-5", "orbit"],
  };
  const DEF = { // default duration (s) and easing per kind
    push: [0.8, "inOut"], pull: [0.7, "inOut"], settle: [0.6, "out"], pan: [0.8, "inOut"], dolly: [1.0, "inOut"],
    drift: [3.0, "sine"], "zoom-through": [0.8, "in"], orbit: [2.0, "sine"],
  };
  const r3 = v => Math.round(v * 1000) / 1000;
  /* camera v2 roll (deg) a move ends on: p.roll (number, or [from, to]) or to.r; 0 otherwise (a move rolls back level) */
  function rollTo(mv) {
    const p = mv.p || {}, to = mv.to;
    if (Array.isArray(p.roll)) return +p.roll[1] || 0;
    if (p.roll != null) return +p.roll || 0;
    if (to && typeof to === "object" && to.r != null) return +to.r || 0;
    return 0;
  }

  function nodeMap(timeline, scenes) {
    const out = {};
    for (const s of scenes || []) for (const nd of (s && s.nodes) || []) if (nd && nd.id != null) out[String(nd.id)] = nd;
    const tn = (timeline && timeline.canvas_nodes) || {};
    for (const k of Object.keys(tn)) out[k] = tn[k];
    return out;
  }
  function homeOf(timeline) {
    const h = (timeline && timeline.canvas_home) || {};
    return { x: h.x != null ? +h.x : CX, y: h.y != null ? +h.y : CY, s: h.s != null ? +h.s : 1, r: 0 };
  }
  /* a target view from `to` ({node, fill?, keep?: [ids]} frames the node plus its `keep` neighbours) and the state the move starts from */
  function target(mv, st, nodes, home) {
    const to = mv.to, p = mv.p || {};
    if (mv.kind === "settle" || to === "home" || (to == null && mv.kind === "pull" && !p.by && !p.scale)) return { ...home };
    let x = st.x, y = st.y, s = st.s;
    if (to && typeof to === "object") {
      if (to.node != null) {
        const nd = nodes[String(to.node)];
        if (nd) {
          // to.keep: ids of neighbouring nodes that must stay in frame too (their text would otherwise be cut by the frame edge
          // at the settled view); the camera frames the union of the node and these. Missing ids are ignored.
          let x0 = +nd.x, y0 = +nd.y, x1 = +nd.x + (+nd.w || 0), y1 = +nd.y + (+nd.h || 0);
          for (const k of Array.isArray(to.keep) ? to.keep : []) {
            const kn = nodes[String(k)];
            if (!kn) continue;
            x0 = Math.min(x0, +kn.x); y0 = Math.min(y0, +kn.y); x1 = Math.max(x1, +kn.x + (+kn.w || 0)); y1 = Math.max(y1, +kn.y + (+kn.h || 0));
          }
          x = (x0 + x1) / 2; y = (y0 + y1) / 2;
          const fill = to.fill != null ? +to.fill : (p.fill != null ? +p.fill : 0.7);
          const keep = (mv.kind === "pan" || mv.kind === "drift") && to.fill == null && p.fill == null; // a pan keeps its zoom
          if (to.s == null && !keep) s = fill * Math.min(W / Math.max(x1 - x0, 1), H / Math.max(y1 - y0, 1));
        }
      }
      if (to.x != null) x = +to.x; if (to.y != null) y = +to.y; if (to.s != null) s = +to.s;
      if (to.by) { x = st.x + (+to.by.x || 0); y = st.y + (+to.by.y || 0); }
    }
    if (p.by && !(to && to.by)) { x = st.x + (+p.by.x || 0); y = st.y + (+p.by.y || 0); }
    if (p.scale != null && !(to && to.s != null) && mv.kind !== "zoom-through") s = st.s * +p.scale;
    if ((to == null || (typeof to === "object" && to.s == null && to.node == null)) && p.scale == null) {
      if (mv.kind === "push") s = st.s * 1.5;
      if (mv.kind === "pull") s = st.s / 1.5;
    }
    return { x, y, s: Math.max(0.05, s), r: rollTo(mv) };
  }
  /* normalise + sort the moves; unknown names are kept with kind null (rendered as holds, reported by V-CANVAS) */
  function compile(timeline, scenes) {
    const tl = timeline || {}, list = (tl.canvas_camera || []).map((m, i) => ({ ...m, i }));
    list.sort((a, b) => (+a.t || 0) - (+b.t || 0) || a.i - b.i);
    const nodes = nodeMap(tl, scenes), home = homeOf(tl);
    const moves = list.map(m => {
      const mm = MOVES[String(m.move)] || [null, null], kind = mm[1], d = DEF[kind] || [0.8, "inOut"];
      const dur = m.dur != null ? +m.dur : d[0], ease = m.ease || d[1];
      return { code: mm[0], kind, name: String(m.move), t: +m.t || 0, f0: Math.round((+m.t || 0) * FPS),
               F: Math.max(1, Math.round(dur * FPS)), dur, ease, to: m.to, p: m.p || {}, i: m.i };
    });
    return { moves, nodes, home, active: moves.length > 0 };
  }
  function easeOf(name) { return EASE[name] || EASE.inOut; }
  /* state of one started move at frame n (n >= f0) */
  function evalMove(m, n) {
    const st = m.start, tg = m.target, q = cl((n - m.f0) / m.F), e = easeOf(m.ease)(q), P = m.p || {};
    switch (m.kind) {
      case "zoom-through": {
        if (n >= m.f0 + m.F) return { ...m.after };
        const k = P.scale != null ? +P.scale : 6, fx = tg.x, fy = tg.y;
        return { x: lerp(st.x, fx, e), y: lerp(st.y, fy, e), s: st.s * Math.pow(k, e), r: st.r };
      }
      case "orbit": {
        const R = P.radius != null ? +P.radius : 60, deg = P.deg != null ? +P.deg : 3, a = 2 * Math.PI * e;
        return { x: st.x + R * Math.sin(a), y: st.y + R * 0.5 * (1 - Math.cos(a)), s: st.s, r: st.r + deg * Math.sin(a) };
      }
      case "push": case "pull": case "settle": case "pan": case "dolly": case "drift": {
        let s = Math.exp(lerp(Math.log(st.s), Math.log(tg.s), e));
        if (m.kind === "dolly") s *= 1 - (P.arc != null ? +P.arc : 0.18) * Math.sin(Math.PI * e);
        return { x: lerp(st.x, tg.x, e), y: lerp(st.y, tg.y, e), s, r: lerp(st.r, tg.r, e) };
      }
      default: return { ...st };
    }
  }
  /* camera at frame n: moves run in order; a move starts from wherever the previous one is at its start frame */
  function stateAt(cam, n) {
    let prev = null;
    for (const mv of cam.moves) {
      if (n < mv.f0) break;
      const start = prev ? evalMove(prev, mv.f0) : { ...cam.home };
      if (Array.isArray((mv.p || {}).roll)) start.r = +mv.p.roll[0] || 0; // roll [from, to]: starts at from
      const tg = target(mv, start, cam.nodes, cam.home);
      const after = mv.kind === "zoom-through" ? (mv.p.then ? target({ kind: "push", to: mv.p.then, p: {} }, start, cam.nodes, cam.home) : { ...cam.home }) : null;
      prev = { ...mv, start, target: tg, after };
    }
    const st = prev ? evalMove(prev, n) : { ...cam.home };
    const moving = !!prev && n < prev.f0 + prev.F && prev.kind != null;
    return { x: st.x, y: st.y, s: st.s, r: st.r || 0, moving, move: moving ? prev.code : null, kind: moving ? prev.kind : null };
  }
  /* the view a layer with parallax k sees */
  function layer(st, k, home) {
    k = cl(+k || 0);
    return { x: home.x + (st.x - home.x) * k, y: home.y + (st.y - home.y) * k, s: Math.pow(st.s, k), r: (st.r || 0) * k };
  }
  /* world -> screen affine [a, b, c, d, e, f] (CSS matrix order) */
  function matrix(v) {
    const rad = (v.r || 0) * Math.PI / 180, a = v.s * Math.cos(rad), b = v.s * Math.sin(rad), c = -b, d = a;
    return [a, b, c, d, CX - (a * v.x + c * v.y), CY - (b * v.x + d * v.y)];
  }
  const apply = (M, x, y) => [M[0] * x + M[2] * y + M[4], M[1] * x + M[3] * y + M[5]];
  function invert(M) {
    const det = M[0] * M[3] - M[1] * M[2] || 1e-12;
    const a = M[3] / det, b = -M[1] / det, c = -M[2] / det, d = M[0] / det;
    return [a, b, c, d, -(a * M[4] + c * M[5]), -(b * M[4] + d * M[5])];
  }
  function rect(M, r) { // axis-aligned bounds of a transformed [x0,y0,x1,y1]
    const p = [apply(M, r[0], r[1]), apply(M, r[2], r[1]), apply(M, r[2], r[3]), apply(M, r[0], r[3])];
    const xs = p.map(q => q[0]), ys = p.map(q => q[1]);
    return [Math.min(...xs), Math.min(...ys), Math.max(...xs), Math.max(...ys)];
  }
  /* default parallax by z: backgrounds are pinned (they follow ctx.camera themselves), glow 0.8, z3-6 the world; z>=7 never */
  function parallaxOf(scene) {
    if (!scene || scene.behind || (+scene.z || 0) >= 7) return 0;
    const v = scene.parallax;
    if (v === false) return 0;
    if (typeof v === "number" && isFinite(v)) return cl(v);
    const z = +scene.z || 0;
    return z <= 1 ? 0 : z === 2 ? 0.8 : 1;
  }
  return { W, H, FPS, EASE, MOVES, DEF, compile, stateAt, layer, matrix, apply, invert, rect, parallaxOf, nodeMap, homeOf, r3 };
});
