/* Vibe Editing OS renderer: lit 3D objects (VEOS.fx.three). Classic script, loaded by player.html after fx.js and
   vendor/three.min.js (three.js r186, MIT, global THREE; no CDN, no network) and before plan/scenes.js.

     VEOS.fx.three(o)       scene factory: extruded text / SVG logos, globe, tower, box, device slab, sphere; a fixed,
                            turntable or orbit camera; key / fill / rim lights, emissive glow, shadows on a ground plane.
                            Transparent background: it composites over worlds, footage and other scenes like any canvas scene.
     VEOS.fx.three.info()   {ok, renderer, version}: WebGL probe (headless Chromium runs it on SwiftShader, software)
     VEOS.fx.three.stats()  {frames, ms_last, ms_max, ms_avg}: GL render time of this page (the render-time budget)

   Determinism: the scene graph is built once per scene (lazily, at its first frame) and EVERY transform, light and camera
   value is set from `lt` on every frame; nothing reads a clock (no requestAnimationFrame, no THREE.Clock, no
   AnimationMixer), and no loader fetches anything (textures come from preloaded plan/assets images, text outlines are
   traced from the loaded font slots). Software rendering (SwiftShader) is bit-stable, so a frame renders the same in
   every worker. Recipes and options: SCENES-API.md section 13. */
(function () {
"use strict";
const VEOS = window.VEOS;
if (!VEOS || !VEOS.fx) return;
const fx = VEOS.fx, W = 1080, H = 1920;
const cl = (x, a = 0, b = 1) => (x < a ? a : x > b ? b : x);
const lerp = (a, b, p) => a + (b - a) * p;
const isNum = v => typeof v === "number" && isFinite(v);
const D2R = Math.PI / 180;
const EASE = {
  linear: p => p, out: p => 1 - Math.pow(1 - p, 3), in: p => p * p * p, inOut: p => (p < 0.5 ? 4 * p * p * p : 1 - Math.pow(-2 * p + 2, 3) / 2),
  expoOut: p => (p >= 1 ? 1 : 1 - Math.pow(2, -10 * p)), back: p => { const c = 1.70158 + 1, q = p - 1; return 1 + c * q * q * q + 1.70158 * q * q; },
  sine: p => 0.5 - 0.5 * Math.cos(Math.PI * p),
};
const KINDS = ["text", "svg", "globe", "tower", "box", "device", "sphere", "cylinder", "custom"];
const C = (ctx, v, dflt) => { const x = v == null ? dflt : v; return (ctx.tokens.colours && ctx.tokens.colours[x]) || x; };

/* ---------------------------------------------------------------- one shared WebGL renderer per page */
const GLS = {}, GL_ERRS = {}; let GL_ERR = null; // one shared WebGL renderer per page and antialias setting
const STATS = { frames: 0, ms_last: 0, ms_max: 0, ms_sum: 0 };
function gl(aa) {
  const k = aa ? "aa" : "plain";
  if (GLS[k] || GL_ERRS[k]) { GL_ERR = GL_ERRS[k] || null; return GLS[k] || null; }
  const T = window.THREE, fail = m => { GL_ERR = GL_ERRS[k] = m; return null; };
  if (!T) return fail("three.js is not loaded (renderer/vendor/three.min.js missing from player.html)");
  try {
    // MSAA is off by default: on SwiftShader it costs ~30-40 % per frame; quality.aa: true opts in (hero shots)
    const cv = document.createElement("canvas"); cv.width = 2; cv.height = 2;
    const opts = { alpha: true, antialias: !!aa, preserveDrawingBuffer: true, premultipliedAlpha: true };
    const probe = cv.getContext("webgl2", opts);
    if (!probe) return fail("WebGL2 is not available in this browser (headless Chromium normally falls back to SwiftShader; check `veos doctor`)");
    const r = new T.WebGLRenderer(Object.assign({ canvas: cv, context: probe, powerPreference: "default" }, opts));
    r.setPixelRatio(1); r.setClearColor(0x000000, 0);
    r.outputColorSpace = T.SRGBColorSpace; r.toneMapping = T.ACESFilmicToneMapping; r.toneMappingExposure = 1;
    r.shadowMap.enabled = true; r.shadowMap.type = T.PCFSoftShadowMap; r.shadowMap.autoUpdate = true;
    const dbg = probe.getExtension("WEBGL_debug_renderer_info");
    GLS[k] = { r, T, cv, name: dbg ? probe.getParameter(dbg.UNMASKED_RENDERER_WEBGL) : probe.getParameter(probe.RENDERER) };
  } catch (e) { return fail(`WebGL renderer failed to start: ${e && e.message || e}`); }
  return GLS[k];
}
fx.three = function (o) { return three(o); };
fx.three.info = () => { const g = gl(); return g ? { ok: true, renderer: g.name, version: window.THREE.REVISION } : { ok: false, error: GL_ERR }; };
fx.three.stats = () => ({ frames: STATS.frames, ms_last: +STATS.ms_last.toFixed(1), ms_max: +STATS.ms_max.toFixed(1), ms_avg: STATS.frames ? +(STATS.ms_sum / STATS.frames).toFixed(1) : 0 });

/* ---------------------------------------------------------------- text outlines: trace the font slot's glyphs
   The text is drawn once on a 2D canvas with the playbook's loaded font, then the alpha edge is traced (marching squares,
   sub-pixel interpolated), simplified (Douglas-Peucker) and nested into outer contours + holes for ExtrudeGeometry. Any
   font slot works, no typeface JSON or font parsing needed. */
function traceText(text, font, res) {
  const m = document.createElement("canvas").getContext("2d"); m.font = font;
  const tw = Math.ceil(m.measureText(text).width), pad = Math.ceil(res * 0.25);
  const cw = tw + 2 * pad, ch = Math.ceil(res * 1.5) + 2 * pad;
  const cv = document.createElement("canvas"); cv.width = cw; cv.height = ch;
  const g = cv.getContext("2d", { willReadFrequently: true }); g.font = font; g.textBaseline = "alphabetic"; g.fillStyle = "#fff";
  const base = pad + Math.round(res * 1.08);
  g.fillText(text, pad, base);
  return { loops: traceAlpha(g.getImageData(0, 0, cw, ch).data, cw, ch), w: cw, h: ch, ink: [pad, base - res, tw, res] };
}
function traceAlpha(px, w, h) {
  const A = (x, y) => (x < 0 || y < 0 || x >= w || y >= h ? 0 : px[(y * w + x) * 4 + 3]), thr = 128;
  const P = new Map(), adj = new Map();
  const ept = (x0, y0, x1, y1) => { // the iso point on the grid edge (x0,y0)-(x1,y1); keyed by the edge
    const key = y1 === y0 ? (y0 * (w + 1) + x0) * 2 : (y0 * (w + 1) + x0) * 2 + 1;
    if (!P.has(key)) { const a = A(x0, y0), b = A(x1, y1), t = a === b ? 0.5 : cl((thr - a) / (b - a)); P.set(key, [x0 + (x1 - x0) * t, y0 + (y1 - y0) * t]); }
    return key;
  };
  const link = (a, b) => { (adj.get(a) || adj.set(a, []).get(a)).push(b); (adj.get(b) || adj.set(b, []).get(b)).push(a); };
  for (let y = -1; y < h; y++) for (let x = -1; x < w; x++) {
    const tl = A(x, y) >= thr, tr = A(x + 1, y) >= thr, br = A(x + 1, y + 1) >= thr, bl = A(x, y + 1) >= thr;
    const c = (tl ? 8 : 0) | (tr ? 4 : 0) | (br ? 2 : 0) | (bl ? 1 : 0);
    if (c === 0 || c === 15) continue;
    const T_ = () => ept(x, y, x + 1, y), R_ = () => ept(x + 1, y, x + 1, y + 1), B_ = () => ept(x, y + 1, x + 1, y + 1), L_ = () => ept(x, y, x, y + 1);
    const mid = (A(x, y) + A(x + 1, y) + A(x + 1, y + 1) + A(x, y + 1)) / 4 >= thr;
    switch (c) {
      case 1: case 14: link(L_(), B_()); break;
      case 2: case 13: link(B_(), R_()); break;
      case 3: case 12: link(L_(), R_()); break;
      case 4: case 11: link(T_(), R_()); break;
      case 6: case 9: link(T_(), B_()); break;
      case 7: case 8: link(T_(), L_()); break;
      case 5: if (mid) { link(T_(), L_()); link(B_(), R_()); } else { link(T_(), R_()); link(L_(), B_()); } break;
      case 10: if (mid) { link(T_(), R_()); link(L_(), B_()); } else { link(T_(), L_()); link(B_(), R_()); } break;
    }
  }
  const seen = new Set(), loops = [];
  for (const start of adj.keys()) {
    if (seen.has(start)) continue;
    const loop = []; let prev = null, cur = start;
    while (cur != null && !seen.has(cur)) {
      seen.add(cur); loop.push(P.get(cur));
      const nb = adj.get(cur) || []; const nx = nb[0] !== prev ? nb[0] : nb[1];
      prev = cur; cur = nx;
    }
    if (loop.length >= 4) loops.push(simplify(loop, 0.3));
  }
  return loops.filter(l => l.length >= 3 && Math.abs(area(l)) > 6);
}
function area(l) { let s = 0; for (let i = 0, j = l.length - 1; i < l.length; j = i++) s += (l[j][0] - l[i][0]) * (l[j][1] + l[i][1]); return s / 2; }
function inside(pt, l) { let c = false; for (let i = 0, j = l.length - 1; i < l.length; j = i++) { const a = l[i], b = l[j]; if ((a[1] > pt[1]) !== (b[1] > pt[1]) && pt[0] < (b[0] - a[0]) * (pt[1] - a[1]) / (b[1] - a[1]) + a[0]) c = !c; } return c; }
function dpOpen(pts, tol) { // Douglas-Peucker on an open polyline (iterative)
  const keep = new Uint8Array(pts.length), st = [[0, pts.length - 1]]; keep[0] = keep[pts.length - 1] = 1;
  while (st.length) {
    const [i, j] = st.pop(), p = pts[i], q = pts[j], dx = q[0] - p[0], dy = q[1] - p[1], L = Math.hypot(dx, dy) || 1;
    let mi = -1, md = tol;
    for (let k = i + 1; k < j; k++) { const d = Math.abs(dy * pts[k][0] - dx * pts[k][1] + q[0] * p[1] - q[1] * p[0]) / L; if (d > md) { md = d; mi = k; } }
    if (mi >= 0) { keep[mi] = 1; st.push([i, mi], [mi, j]); }
  }
  return pts.filter((_, k) => keep[k]);
}
function simplify(pts, tol) { // closed loop: split at the point farthest from the first, simplify both halves
  let far = 0, fd = -1; for (let i = 1; i < pts.length; i++) { const d = (pts[i][0] - pts[0][0]) ** 2 + (pts[i][1] - pts[0][1]) ** 2; if (d > fd) { fd = d; far = i; } }
  const a = dpOpen(pts.slice(0, far + 1), tol), b = dpOpen(pts.slice(far).concat([pts[0]]), tol);
  return a.concat(b.slice(1, -1));
}
/* loops (px, y down) -> THREE.Shape[] (world units, y up), centred on the ink box */
function loopsToShapes(T, loops, k, cx, cy) {
  const info = loops.map(l => ({ l, a: Math.abs(area(l)), depth: 0, parent: null }));
  for (const q of info) for (const r of info) if (q !== r && r.a > q.a && inside(q.l[0], r.l)) { q.depth++; if (!q.parent || r.a < q.parent.a) q.parent = r; }
  const v = p => new T.Vector2((p[0] - cx) * k, -(p[1] - cy) * k), shapes = new Map();
  for (const q of info) if (q.depth % 2 === 0) shapes.set(q, new T.Shape(q.l.map(v)));
  for (const q of info) if (q.depth % 2 === 1 && q.parent && shapes.has(q.parent)) shapes.get(q.parent).holes.push(new T.Path(q.l.map(v)));
  return [...shapes.values()];
}

/* ---------------------------------------------------------------- textures (no loaders: canvases and preloaded assets) */
function imgTexture(T, ctx, id) {
  const im = ctx.assetImage ? ctx.assetImage(id) : null;
  if (!im || !im.naturalWidth) throw new Error(`fx.three: asset '${id}' is not a loaded image (put it in plan/assets/)`);
  const t = new T.Texture(im); t.colorSpace = T.SRGBColorSpace; t.anisotropy = 4; t.needsUpdate = true; return t;
}
function graticule(T, sea, line, land) { // procedural equirect: ocean, latitude / longitude lines, seeded dot "continents"
  const cv = document.createElement("canvas"); cv.width = 1024; cv.height = 512; const g = cv.getContext("2d");
  g.fillStyle = sea; g.fillRect(0, 0, 1024, 512);
  if (land) { let s = 0x9E3779B9; const rnd = () => { s = (s + 0x6D2B79F5) | 0; let t = Math.imul(s ^ (s >>> 15), 1 | s); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; };
    const blobs = Array.from({ length: 9 }, () => [rnd() * 1024, 110 + rnd() * 290, 60 + rnd() * 110, 40 + rnd() * 70]);
    g.fillStyle = land;
    for (let y = 6; y < 512; y += 12) for (let x = 6; x < 1024; x += 12) if (blobs.some(b => ((x - b[0]) / b[2]) ** 2 + ((y - b[1]) / b[3]) ** 2 < 1 || ((x + 1024 - b[0]) / b[2]) ** 2 + ((y - b[1]) / b[3]) ** 2 < 1)) { g.beginPath(); g.arc(x, y, 3.6, 0, 7); g.fill(); } }
  g.strokeStyle = line; g.lineWidth = 2; g.globalAlpha = 0.55;
  for (let i = 1; i < 12; i++) { g.beginPath(); g.moveTo(0, i * 512 / 12); g.lineTo(1024, i * 512 / 12); g.stroke(); }
  for (let i = 0; i < 24; i++) { g.beginPath(); g.moveTo(i * 1024 / 24, 0); g.lineTo(i * 1024 / 24, 512); g.stroke(); }
  const t = new T.CanvasTexture(cv); t.colorSpace = T.SRGBColorSpace; t.anisotropy = 4; return t;
}
function glowTexture(T) {
  const cv = document.createElement("canvas"); cv.width = cv.height = 128; const g = cv.getContext("2d");
  const gr = g.createRadialGradient(64, 64, 0, 64, 64, 64); gr.addColorStop(0, "rgba(255,255,255,1)"); gr.addColorStop(0.35, "rgba(255,255,255,.45)"); gr.addColorStop(1, "rgba(255,255,255,0)");
  g.fillStyle = gr; g.fillRect(0, 0, 128, 128); return new T.CanvasTexture(cv);
}

/* ---------------------------------------------------------------- studio environment (reflections for metal / chrome)
   A metal surface shows only what it reflects; with lights alone it renders near-black. The environment is built here,
   procedurally, as a small three.js scene (a graded sky dome: bright top, darker band under the horizon, plus HDR softbox
   panels, the large one BEHIND the camera so flat front faces read bright, white at the top to `tint` at the bottom),
   pre-filtered once per WebGL renderer with PMREMGenerator.fromScene. No HDR file, no loader, no network. */
function gradTexture(T, stops, w = 4, h = 256) {
  const cv = document.createElement("canvas"); cv.width = w; cv.height = h; const g = cv.getContext("2d"), gr = g.createLinearGradient(0, 0, 0, h);
  for (const [at, c] of stops) gr.addColorStop(at, c);
  g.fillStyle = gr; g.fillRect(0, 0, w, h); const t = new T.CanvasTexture(cv); t.colorSpace = T.SRGBColorSpace; return t;
}
function envScene(T, tint) {
  const sc = new T.Scene();
  const dome = new T.Mesh(new T.SphereGeometry(20, 32, 16), new T.MeshBasicMaterial({ side: T.BackSide, map: gradTexture(T,
    [[0, "#FFFFFF"], [0.3, "#DDE6F2"], [0.5, "#7F8896"], [0.56, "#1E222A"], [0.75, "#3A404C"], [1, "#5A6170"]]) }));
  sc.add(dome);
  const panel = (w, h, pos, k, stops) => { // an HDR softbox facing the origin
    const m = new T.MeshBasicMaterial({ map: gradTexture(T, stops), side: T.DoubleSide }); m.color.setScalar(k);
    const p = new T.Mesh(new T.PlaneGeometry(w, h), m); p.position.set(...pos); p.lookAt(0, 0, 0); sc.add(p);
  };
  // behind the camera, centred on the horizon: what flat front faces reflect. White above a soft steel horizon line, the
  // tint below it (a face spans only a few degrees of it, so the stops sit close to the middle): white -> tint chrome
  panel(16, 7, [0, 0, 9], 1.6, [[0, "#FFFFFF"], [0.44, "#F4F8FF"], [0.49, "#D2DDEE"], [0.505, "#9AA9C2"], [0.53, tint], [1, "#7FA3E0"]]);
  panel(10, 3, [0, 9, 1], 3.0, [[0, "#FFFFFF"], [1, "#FFFFFF"]]);                 // overhead strip: bevel highlights
  panel(3, 10, [-9, 1, 2], 2.2, [[0, "#FFFFFF"], [1, tint]]);                    // side strips: edge glints
  panel(3, 10, [9, 1, 2], 1.4, [[0, "#FFFFFF"], [1, tint]]);
  return sc;
}
function envMap(G, tint) { // one PMREM texture per WebGL renderer and tint, built on first use (~100-300 ms on SwiftShader)
  const cache = G.env || (G.env = {});
  if (cache[tint]) return cache[tint];
  const T = G.T, pm = new T.PMREMGenerator(G.r), sc = envScene(T, tint);
  const tex = pm.fromScene(sc, 0.03).texture; pm.dispose();
  sc.traverse(m => { if (m.geometry) m.geometry.dispose(); if (m.material) { if (m.material.map) m.material.map.dispose(); m.material.dispose(); } });
  return (cache[tint] = tex);
}

/* ---------------------------------------------------------------- objects */
// material presets: `material: "chrome"` = a bright polished chrome (white -> tint face, deep side) lit by the environment
// (a flat face reflects only a few degrees of the environment, so the white -> ice-blue fall-off is a vertical `grad` on the face)
const PRESETS = { chrome: { color: "#FFFFFF", side: "#AFC2DC", metal: 1, rough: 0.12, env_k: 1.15, grad: ["#FFFFFF", "#9FC2FF"] } };
function material(T, ctx, ob, dflt) {
  const pr = PRESETS[ob.material] || {};
  const m = new T.MeshStandardMaterial({ color: new T.Color(C(ctx, ob.color, pr.color || dflt)), metalness: isNum(ob.metal) ? ob.metal : isNum(pr.metal) ? pr.metal : 0.15, roughness: isNum(ob.rough) ? ob.rough : isNum(pr.rough) ? pr.rough : 0.42 });
  if (ob.emissive) { m.emissive = new T.Color(C(ctx, ob.emissive)); m.emissiveIntensity = isNum(ob.emissive_k) ? ob.emissive_k : 1; }
  m.userData.env_k = isNum(ob.env_k) ? ob.env_k : pr.env_k || 1;
  return m;
}
function roundRect(T, w, h, r) { // a centred rounded rectangle Shape (circular corners)
  r = Math.max(0, Math.min(r, w / 2 - 1e-4, h / 2 - 1e-4)); const s = new T.Shape(), x = -w / 2, y = -h / 2, P = Math.PI;
  s.moveTo(x + r, y); s.lineTo(x + w - r, y); if (r) s.absarc(x + w - r, y + r, r, -P / 2, 0);
  s.lineTo(x + w, y + h - r); if (r) s.absarc(x + w - r, y + h - r, r, 0, P / 2);
  s.lineTo(x + r, y + h); if (r) s.absarc(x + r, y + h - r, r, P / 2, P);
  s.lineTo(x, y + r); if (r) s.absarc(x + r, y + r, r, P, 1.5 * P);
  return s;
}
function flatShape(T, shape, w, h, segs) { // ShapeGeometry with 0..1 UVs over its w x h box (for screen textures)
  const g = new T.ShapeGeometry(shape, segs || 12), p = g.attributes.position, uv = g.attributes.uv;
  for (let i = 0; i < p.count; i++) uv.setXY(i, p.getX(i) / w + 0.5, p.getY(i) / h + 0.5);
  uv.needsUpdate = true; return g;
}
function buildObject(T, ctx, ob, sceneId) {
  let mesh;
  const sh = ob.shadow !== false;
  switch (ob.kind) {
    case "text": case "svg": {
      let shapes;
      const size = ob.size || 1;
      if (ob.kind === "text") {
        const slot = ob.slot || "display", res = cl(ob.res || 220, 60, 600), fam = ctx.fam(slot), wt = ob.weight || 800;
        const tr = traceText(String(ob.text), `${ob.italic ? "italic " : ""}${wt} ${res}px ${fam}`, res);
        if (!tr.loops.length) throw new Error(`fx.three ${sceneId}: text '${ob.text}' traced no outline (font slot '${slot}' loaded?)`);
        shapes = loopsToShapes(T, tr.loops, size / res, tr.ink[0] + tr.ink[2] / 2, tr.ink[1] + tr.ink[3] / 2);
      } else {
        const svg = ob.svg || `<svg>${[].concat(ob.path).map(d => `<path d="${d}"/>`).join("")}</svg>`;
        const data = new T.SVGLoader().parse(svg); shapes = [];
        for (const p of data.paths) shapes.push(...T.SVGLoader.createShapes(p));
        if (!shapes.length) throw new Error(`fx.three ${sceneId}: the svg has no filled paths`);
        const bb = new T.Box2(); for (const s of shapes) for (const q of s.getPoints()) bb.expandByPoint(q);
        const k = size / Math.max(1e-6, bb.max.y - bb.min.y), cx = (bb.min.x + bb.max.x) / 2, cy = (bb.min.y + bb.max.y) / 2;
        shapes = shapes.map(s => { const f = q => new T.Vector2((q.x - cx) * k, -(q.y - cy) * k); const n = new T.Shape(s.getPoints(12).map(f)); n.holes = s.holes.map(hh => new T.Path(hh.getPoints(12).map(f))); return n; });
      }
      const depth = isNum(ob.depth) ? ob.depth : size * 0.28, bev = isNum(ob.bevel) ? ob.bevel : size * 0.035;
      const geo = new T.ExtrudeGeometry(shapes, { depth, curveSegments: 6, bevelEnabled: bev > 0, bevelThickness: bev, bevelSize: bev * 0.8, bevelSegments: 3 });
      geo.translate(0, 0, -depth / 2); geo.computeVertexNormals();
      const grad = ob.grad || (PRESETS[ob.material] || {}).grad;
      if (grad) { // vertical face gradient (vertex colours, top -> bottom of the ink), multiplied with the face colour
        geo.computeBoundingBox(); const y0 = geo.boundingBox.min.y, y1 = geo.boundingBox.max.y, pa = geo.attributes.position;
        const ct = new T.Color(C(ctx, grad[0])), cb = new T.Color(C(ctx, grad[1])), col = new Float32Array(pa.count * 3), c = new T.Color();
        for (let i = 0; i < pa.count; i++) { c.copy(cb).lerp(ct, cl((pa.getY(i) - y0) / Math.max(1e-6, y1 - y0))); col[i * 3] = c.r; col[i * 3 + 1] = c.g; col[i * 3 + 2] = c.b; }
        geo.setAttribute("color", new T.BufferAttribute(col, 3));
      }
      const face = material(T, ctx, ob, "paper"), side = material(T, ctx, Object.assign({}, ob, { color: ob.side || (PRESETS[ob.material] || {}).side || ob.color }), "ink");
      if (grad) face.vertexColors = true;
      mesh = new T.Mesh(geo, [face, side]);
      break;
    }
    case "globe": case "sphere": {
      const r = ob.radius || 1, geo = new T.SphereGeometry(r, 96, 64), m = material(T, ctx, ob, ob.kind === "globe" ? "#FFFFFF" : "primary");
      if (ob.kind === "globe") { m.map = ob.texture ? imgTexture(T, ctx, ob.texture) : graticule(T, C(ctx, ob.sea, "#1B2B4A"), C(ctx, ob.line, "#9FC3FF"), ob.land === false ? null : C(ctx, ob.land, "#E8F0FF")); m.color = new T.Color(0xffffff); }
      mesh = new T.Mesh(geo, m);
      if (ob.atmosphere) { const a = new T.Mesh(new T.SphereGeometry(r * 1.06, 64, 48), new T.MeshBasicMaterial({ color: new T.Color(C(ctx, ob.atmosphere)), transparent: true, opacity: 0.18, side: T.BackSide, depthWrite: false })); mesh.add(a); }
      break;
    }
    case "tower": case "cylinder": { // base at y 0, so scale y grows it out of the ground
      const h = ob.height || 3, geo = ob.kind === "tower" && ob.shape !== "cyl" ? new T.BoxGeometry(ob.width || 0.8, h, ob.depth || ob.width || 0.8, 1, Math.max(1, ob.floors || 1), 1) : new T.CylinderGeometry(ob.radius_top != null ? ob.radius_top : ob.radius || 0.5, ob.radius || 0.5, h, 64);
      geo.translate(0, h / 2, 0);
      mesh = new T.Mesh(geo, material(T, ctx, ob, "primary"));
      if (ob.floors > 1 && ob.lines !== false) { const e = new T.LineSegments(new T.EdgesGeometry(geo), new T.LineBasicMaterial({ color: new T.Color(C(ctx, ob.lines || "ink")), transparent: true, opacity: 0.5 })); mesh.add(e); }
      break;
    }
    case "box": {
      const s = ob.dims || [1, 1, 1], geo = ob.radius ? new T.RoundedBoxGeometry(s[0], s[1], s[2], 4, ob.radius) : new T.BoxGeometry(s[0], s[1], s[2]);
      mesh = new T.Mesh(geo, material(T, ctx, ob, "primary"));
      break;
    }
    case "device": { // phone / tablet slab: a metal frame with rounded corners in the screen plane and rounded edges, a black
      // glass front, a screen with rounded corners (image asset) and a dynamic island or notch. Defaults are phone-like.
      const s = ob.dims || [1.0, 2.05, 0.09], w = s[0], h = s[1], d = s[2], u = Math.min(w, h);
      const rr = isNum(ob.radius) ? ob.radius : u * 0.14;            // corner radius (iPhone-like 0.14 x width)
      const bz = isNum(ob.bezel) ? ob.bezel : u * 0.045;             // body edge -> screen edge
      const ev = Math.min(d * 0.45, u * 0.03);                       // edge roundover of the frame
      const geo = new T.ExtrudeGeometry(roundRect(T, w - 2 * ev, h - 2 * ev, rr - ev), { depth: Math.max(1e-3, d - 2 * ev), curveSegments: 16, bevelEnabled: true, bevelThickness: ev, bevelSize: ev, bevelSegments: 4 });
      geo.translate(0, 0, -Math.max(1e-3, d - 2 * ev) / 2);
      mesh = new T.Mesh(geo, material(T, ctx, Object.assign({ metal: 0.55, rough: 0.3 }, ob), "#1A1A1C"));
      const fr = Math.min(bz * 0.5, ev * 0.8), z0 = d / 2;           // the black glass covers all but a thin metal rim
      const glass = new T.Mesh(new T.ShapeGeometry(roundRect(T, w - 2 * fr, h - 2 * fr, rr - fr), 16), new T.MeshStandardMaterial({ color: 0x050506, roughness: 0.1, metalness: 0 }));
      glass.position.z = z0 + 0.001; mesh.add(glass);
      const sw = w - 2 * bz, sh = h - 2 * bz, sr = Math.max(0, rr - bz);
      const sm = ob.screen ? new T.MeshBasicMaterial({ map: imgTexture(T, ctx, ob.screen), toneMapped: false }) : new T.MeshStandardMaterial({ color: 0x0a0a0c, roughness: 0.15, metalness: 0.2 });
      const scr = new T.Mesh(flatShape(T, roundRect(T, sw, sh, sr), sw, sh, 16), sm); scr.position.z = z0 + 0.002; mesh.add(scr);
      const notch = ob.notch !== undefined ? ob.notch : (h / w >= 1.6 ? "island" : "none");
      if (notch === "island" || notch === "notch") {
        const blk = new T.MeshBasicMaterial({ color: 0x000000 });
        const nw = notch === "island" ? sw * 0.31 : sw * 0.48, nh = notch === "island" ? sw * 0.092 : sw * 0.085;
        const shp = notch === "island" ? roundRect(T, nw, nh, nh / 2) : roundRect(T, nw, nh * 2, nh * 0.6); // a notch hangs from the top edge
        const n = new T.Mesh(new T.ShapeGeometry(shp, 12), blk);
        n.position.set(0, notch === "island" ? sh / 2 - sw * 0.03 - nh / 2 : sh / 2, z0 + 0.003); mesh.add(n);
      }
      break;
    }
    case "custom": {
      mesh = ob.build(T, ctx);
      if (!mesh || !mesh.isObject3D) throw new Error(`fx.three ${sceneId}: custom build() must return a THREE.Object3D`);
      break;
    }
  }
  mesh.traverse(m => { if (m.isMesh) { m.castShadow = sh; m.receiveShadow = !!ob.receive; } });
  const grp = new T.Group(); grp.add(mesh);
  if (ob.glow) { // emissive halo: an additive sprite placed BEHIND the object along the view ray every frame (glowPose), so a
    // spinning object never swings it in front of itself; no bloom pass (cheap and stable on SwiftShader)
    const gw = typeof ob.glow === "object" ? ob.glow : {};
    const sp = new T.Sprite(new T.SpriteMaterial({ map: glowTexture(T), color: new T.Color(C(ctx, gw.color || ob.emissive || ob.color, "primary")), transparent: true, opacity: isNum(gw.strength) ? gw.strength : 0.7, blending: T.AdditiveBlending, depthWrite: false }));
    sp.renderOrder = -1; sp.userData = { size: gw.size || 3, y: gw.y || 0, behind: isNum(gw.behind) ? gw.behind : 1, op: sp.material.opacity };
    grp.userData.glow = sp;
  }
  return grp;
}

/* ---------------------------------------------------------------- animation: keys + spin, pure in lt */
const v3 = (v, d) => (Array.isArray(v) ? [v[0], v[1], v[2]] : isNum(v) ? [v, v, v] : d.slice());
function track(base, keys, lt, prop, dflt) { // value of `prop` at lt: base, then keys [{at, <prop>, ease}] eased in sequence
  let val = v3(base[prop], dflt);
  if (!keys || !keys.length) return val;
  const ks = keys.filter(k => k[prop] != null);
  if (!ks.length) return val;
  let prev = { at: -1e9, v: val };
  if (ks[0].at <= 0 || base[prop] == null) prev = { at: ks[0].at, v: v3(ks[0][prop], dflt) };
  for (const k of ks) {
    const kv = v3(k[prop], dflt);
    if (lt < k.at) { if (prev.at <= -1e8) return prev.v; const dt = k.at - prev.at, p = dt > 0 ? (EASE[k.ease || "out"] || EASE.out)(cl((lt - prev.at) / dt)) : 1; return prev.v.map((a, i) => lerp(a, kv[i], p)); }
    prev = { at: k.at, v: kv };
  }
  return prev.v;
}
function place(o3, ob, lt) {
  const p = track(ob, ob.keys, lt, "pos", [0, 0, 0]), r = track(ob, ob.keys, lt, "rot", [0, 0, 0]), s = track(ob, ob.keys, lt, "scale", [1, 1, 1]);
  const spin = isNum(ob.spin) ? ob.spin * lt : 0; // deg/s turntable around the object's own y
  o3.position.set(p[0], p[1], p[2]); o3.rotation.set(r[0] * D2R, (r[1] + spin) * D2R, r[2] * D2R, "YXZ");
  o3.scale.set(Math.max(1e-4, s[0]), Math.max(1e-4, s[1]), Math.max(1e-4, s[2]));
  const op = ob.keys ? track(ob, ob.keys, lt, "opacity", [1, 1, 1])[0] : (isNum(ob.opacity) ? ob.opacity : 1);
  o3.visible = op > 0.004;
  o3.traverse(m => { // fade: every material's own opacity x op (original values kept on first touch)
    if (m.material) for (const mt of [].concat(m.material)) {
      if (mt._op == null) { mt._op = mt.opacity; mt._tr = mt.transparent; }
      const want = mt._op * cl(op), tr = mt._tr || want < 0.999;
      if (mt.transparent !== tr) { mt.transparent = tr; mt.needsUpdate = true; }
      mt.opacity = want;
    }
  });
}
function glowPose(T, g, cam) { // the halo sits behind the object's centre (seen from the camera), scaled and faded with it
  const sp = g.userData.glow; if (!sp) return;
  const u = sp.userData, p = new T.Vector3(0, u.y, 0); p.multiply(g.scale).add(g.position);
  const dir = p.clone().sub(cam.position).normalize(), k = (g.scale.x + g.scale.y + g.scale.z) / 3;
  sp.position.copy(p).addScaledVector(dir, u.behind * k); sp.scale.set(u.size * k, u.size * k, 1);
  sp.visible = g.visible; const m = g.children[0] && [].concat(g.children[0].material)[0];
  sp.material.opacity = u.op * (m && m._op ? m.opacity / m._op : 1);
}
/* camera fit: the distance (along the camera's direction to its target) at which the objects' rest-pose bounding box fills
   `fit` of the box height or width, whichever binds first; exact for the objects' own vertices (sampled to <= ~40k points),
   computed once at build. */
const restAt = ob => Math.max(0, ...((ob.keys || []).map(k => k.at)));
function fitCamera(T, objs, obs, c, aspect) {
  const pts = [], bb = new T.Box3();
  objs.forEach((g, i) => { place(g, Object.assign({}, obs[i], { spin: 0 }), restAt(obs[i])); g.updateMatrixWorld(true); });
  for (const g of objs) g.traverse(m => {
    const pa = m.isMesh && m.geometry && m.geometry.attributes.position; if (!pa) return;
    const step = Math.max(1, Math.ceil(pa.count / 40000));
    for (let i = 0; i < pa.count; i += step) { const v = new T.Vector3().fromBufferAttribute(pa, i).applyMatrix4(m.matrixWorld); pts.push(v); bb.expandByPoint(v); }
  });
  if (!pts.length) return null;
  const tgt = c.target ? new T.Vector3(...c.target) : bb.getCenter(new T.Vector3());
  const p0 = new T.Vector3(...(c.pos || [0, 0.6, 8])), dir = p0.clone().sub(tgt); if (dir.lengthSq() < 1e-9) dir.set(0, 0, 1); dir.normalize();
  const right = new T.Vector3().crossVectors(new T.Vector3(0, 1, 0), dir); if (right.lengthSq() < 1e-9) right.set(1, 0, 0); right.normalize();
  const up = new T.Vector3().crossVectors(dir, right).normalize();
  const fit = isNum(c.fit) ? c.fit : 0.9, ty = Math.tan((c.fov || 35) * D2R / 2), tx = ty * aspect;
  let D = 0.5;
  for (const v of pts) {
    const q = v.clone().sub(tgt), z = q.dot(dir); D = Math.max(D, z + Math.abs(q.dot(up)) / (fit * ty), z + Math.abs(q.dot(right)) / (fit * tx));
  }
  return { pos: tgt.clone().addScaledVector(dir, D).toArray(), target: tgt.toArray() };
}
function cameraAt(cam, o, lt, dur, fitted) {
  const c = o.camera || {}, tgt = fitted ? fitted.target : track(c, c.keys, lt, "target", [0, 0, 0]);
  let pos;
  if (fitted) pos = fitted.pos;
  else if (c.orbit) { // turntable / orbit: angle from `from` to `to` over the scene (eased), or `from + speed * lt`
    const ob = c.orbit, r = ob.radius || 8, h = ob.height != null ? ob.height : 1.5;
    const a = isNum(ob.speed) ? (ob.from || 0) + ob.speed * lt : lerp(ob.from || 0, ob.to != null ? ob.to : 60, (EASE[ob.ease || "inOut"] || EASE.inOut)(cl(lt / Math.max(dur, 1e-3))));
    pos = [tgt[0] + r * Math.sin(a * D2R), tgt[1] + h, tgt[2] + r * Math.cos(a * D2R)];
  } else pos = track(c, c.keys, lt, "pos", [0, 0.6, 8]);
  const fov = track(c, c.keys, lt, "fov", [c.fov || 35, 0, 0])[0];
  cam.position.set(pos[0], pos[1], pos[2]); cam.up.set(0, 1, 0); cam.lookAt(tgt[0], tgt[1], tgt[2]);
  if (c.roll) cam.rotateZ(c.roll * D2R);
  if (cam.fov !== fov) { cam.fov = fov; cam.updateProjectionMatrix(); }
}

/* lights: key (casts the ground shadow), fill, rim, ambient; any of them overridable or switched off (false) */
const LIGHT_DFLT = { key: { color: "#FFFFFF", intensity: 2.6, pos: [4, 7, 6] }, fill: { color: "#DCE6FF", intensity: 0.7, pos: [-6, 2, 4] },
  rim: { color: "#FFFFFF", intensity: 2.2, pos: [-2, 4, -7] }, ambient: { color: "#FFFFFF", ground: "#202028", intensity: 0.55 } };
function buildLights(T, ctx, o, scene) {
  const L = {}, cfg = o.lights || {}, gr = o.ground;
  for (const k of ["key", "fill", "rim"]) {
    if (cfg[k] === false) continue;
    const d = Object.assign({}, LIGHT_DFLT[k], cfg[k] || {});
    const l = new T.DirectionalLight(new T.Color(C(ctx, d.color)), d.intensity); l.position.set(...d.pos);
    if (k === "key" && gr !== false && gr) {
      const s = gr.size || 8, q = cl(Math.round(((o.quality || {}).shadow) || 1024), 256, 2048);
      l.castShadow = true; l.shadow.mapSize.set(q, q); l.shadow.bias = -0.0004; l.shadow.normalBias = 0.02; l.shadow.radius = gr.soft || 4;
      Object.assign(l.shadow.camera, { left: -s, right: s, top: s, bottom: -s, near: 0.5, far: 40 }); l.shadow.camera.updateProjectionMatrix();
    }
    scene.add(l); scene.add(l.target); L[k] = l;
  }
  if (cfg.ambient !== false) { const d = Object.assign({}, LIGHT_DFLT.ambient, cfg.ambient || {}); scene.add(new T.HemisphereLight(new T.Color(C(ctx, d.color)), new T.Color(C(ctx, d.ground)), d.intensity)); }
  return L;
}

/* ---------------------------------------------------------------- the factory */
function check(o) {
  const bad = [], id = o && o.id != null ? o.id : "(no id)";
  if (!o || typeof o !== "object") return ["fx.three needs an options object"];
  if (!Array.isArray(o.objects) || !o.objects.length) bad.push("objects must be a non-empty array of {kind, ...}");
  (o.objects || []).forEach((ob, i) => {
    const w = `objects[${i}]`;
    if (!ob || !KINDS.includes(ob.kind)) { bad.push(`${w}.kind must be one of ${KINDS.join("|")}`); return; }
    if (ob.kind === "text" && !(typeof ob.text === "string" && ob.text.trim())) bad.push(`${w}: text needs a non-empty text`);
    if (ob.kind === "svg" && !(typeof ob.svg === "string" || typeof ob.path === "string" || Array.isArray(ob.path))) bad.push(`${w}: svg needs svg (markup) or path (d string / array)`);
    if (ob.kind === "custom" && typeof ob.build !== "function") bad.push(`${w}: custom needs build(THREE, ctx) returning an Object3D`);
    for (const k of ["pos", "rot", "scale"]) if (ob[k] != null && !(isNum(ob[k]) || (Array.isArray(ob[k]) && ob[k].length === 3 && ob[k].every(isNum)))) bad.push(`${w}.${k} must be [x, y, z] (or one number)`);
    for (const k of ["size", "depth", "bevel", "radius", "height", "spin", "metal", "rough"]) if (ob[k] != null && !isNum(ob[k])) bad.push(`${w}.${k} must be a number`);
    if (ob.keys != null && !(Array.isArray(ob.keys) && ob.keys.every(k => k && isNum(k.at) && (k.ease == null || EASE[k.ease])))) bad.push(`${w}.keys must be [{at (local s), pos?, rot?, scale?, opacity?, ease?}] with ease ${Object.keys(EASE).join("|")}`);
  });
  const c = o.camera || {};
  if (c.orbit && typeof c.orbit !== "object") bad.push("camera.orbit must be {radius, height, from, to | speed, ease}");
  if (c.orbit && c.orbit.ease && !EASE[c.orbit.ease]) bad.push(`camera.orbit.ease must be ${Object.keys(EASE).join("|")}`);
  if (c.fov != null && !(isNum(c.fov) && c.fov >= 8 && c.fov <= 100)) bad.push("camera.fov must be 8..100 degrees");
  if (c.fit != null && !(isNum(c.fit) && c.fit >= 0.2 && c.fit <= 1)) bad.push("camera.fit must be 0.2..1 (the share of the box the objects fill)");
  if (c.fit != null && (c.orbit || c.keys)) bad.push("camera.fit is for a fixed camera: drop orbit / keys, or drop fit");
  const e = o.env;
  if (e != null && typeof e !== "boolean" && !(typeof e === "object" && (e.intensity == null || (isNum(e.intensity) && e.intensity >= 0 && e.intensity <= 4)) && (e.tint == null || typeof e.tint === "string"))) bad.push("env must be true, false or {intensity (0..4), tint (role or hex)}");
  (o.objects || []).forEach((ob, i) => {
    if (!ob) return;
    if (ob.material != null && !PRESETS[ob.material]) bad.push(`objects[${i}].material must be one of ${Object.keys(PRESETS).join("|")}`);
    if (ob.env_k != null && !(isNum(ob.env_k) && ob.env_k >= 0 && ob.env_k <= 4)) bad.push(`objects[${i}].env_k must be 0..4`);
    if (ob.grad != null && !(Array.isArray(ob.grad) && ob.grad.length === 2 && ob.grad.every(x => typeof x === "string"))) bad.push(`objects[${i}].grad must be [top, bottom] colours (role or hex)`);
    if (ob.kind === "device" && ob.notch != null && !["island", "notch", "none", false].includes(ob.notch)) bad.push(`objects[${i}].notch must be "island", "notch" or "none"`);
    if (ob.kind === "device" && ob.dims != null && !(Array.isArray(ob.dims) && ob.dims.length === 3 && ob.dims.every(v => isNum(v) && v > 0))) bad.push(`objects[${i}].dims must be [w, h, depth] > 0`);
    for (const k of ["bezel", "env_k"]) if (ob[k] != null && !isNum(ob[k])) bad.push(`objects[${i}].${k} must be a number`);
  });
  if (o.box && !["x", "y", "w", "h"].every(k => isNum(o.box[k]) && o.box[k] >= (k === "w" || k === "h" ? 16 : -W))) bad.push("box must be {x, y, w, h} px (w, h >= 16)");
  const q = o.quality || {};
  if (q.aa != null && typeof q.aa !== "boolean") bad.push("quality.aa must be true or false (MSAA; ~1.4x the GL time)");
  if (q.shadow != null && !(isNum(q.shadow) && q.shadow >= 256 && q.shadow <= 2048)) bad.push("quality.shadow must be 256..2048 (shadow map px)");
  if (q.scale != null && !(isNum(q.scale) && q.scale >= 0.25 && q.scale <= 2)) bad.push("quality.scale must be 0.25..2 (render resolution / box size)");
  return bad.map(m => `fx.three ${id}: ${m}`);
}

const STATE = new Map(); // scene id -> {scene, cam, objs}: built at the scene's first frame, then only re-posed
const OWN_KEYS = ["objects", "camera", "lights", "ground", "quality", "env", "update", "extra"]; // 3D-only options (not scene meta)
function three(o) {
  const errs = check(o);
  if (errs.length) { for (const m of errs) VEOS.errors.push(`scene ${o && o.id != null ? o.id : "(no id)"}: ${m}`); return null; }
  const box = o.box || { x: 0, y: 0, w: W, h: H }, q = o.quality || {}, scale = q.scale || 1;
  const texts = o.objects.filter(ob => ob.kind === "text").map(ob => ob.text), camo = o.camera || {};
  // camera fit: explicit camera.fit, or by default for a device scene whose camera has no pos / keys / orbit
  const fitOn = camo.fit != null || (!camo.pos && !camo.keys && !camo.orbit && o.objects.some(ob => ob.kind === "device"));
  // environment: env true/{...} = every lit material; default (env unset) = only metal >= 0.5 materials; env false = none
  const envAll = o.env === true || (o.env && typeof o.env === "object"), envOff = o.env === false;
  const envUsed = !envOff && (envAll || o.objects.some(ob => (isNum(ob.metal) ? ob.metal : (PRESETS[ob.material] || {}).metal || (ob.kind === "device" ? 0.55 : 0)) >= 0.5));
  // every standard scene key (text_class, insert, exception, anchor, smear, grade, ...) passes through like VEOS.scene;
  // only the 3D-only options and functions stay here
  const pass = {};
  for (const k of Object.keys(o)) if (!OWN_KEYS.includes(k) && typeof o[k] !== "function") pass[k] = o[k];
  return VEOS.scene(Object.assign({
    text: texts.length ? true : undefined, text_content: texts.length ? texts.join(" ") : undefined, text_class: texts.length ? "TC-display" : undefined,
  }, o.extra || {}, pass, {
    id: o.id, t_in: o.t_in, t_out: o.t_out, z: o.z || 3, in: o.in || "none", out: o.out || "none", box,
    fx: "three", three: { objects: o.objects.map(ob => ob.kind), camera: camo.orbit ? "orbit" : fitOn ? "fit" : "fixed", shadow: !!o.ground, scale, env: envUsed },
    render(ctx, lt, dur) {
      const g2 = ctx.canvas();
      if (ctx.measuring) return ""; // layout-only measure: the declared box is the rect; skip the GL work
      const G = gl(q.aa);
      if (!G) throw new Error(`fx.three ${o.id}: ${GL_ERR}`);
      const T = G.T, t0 = performance.now(); // performance.now only times the render for stats(); it never drives the picture
      let st = STATE.get(o.id);
      if (!st) {
        const scene = new T.Scene(), cam = new T.PerspectiveCamera((o.camera || {}).fov || 35, box.w / box.h, 0.1, 200);
        const lights = buildLights(T, ctx, o, scene);
        if (o.ground) { const gs = o.ground.size || 8, pl = new T.Mesh(new T.PlaneGeometry(gs * 4, gs * 4), new T.ShadowMaterial({ color: 0x000000, opacity: isNum(o.ground.shadow) ? o.ground.shadow : 0.35 }));
          pl.rotation.x = -Math.PI / 2; pl.position.y = o.ground.y || 0; pl.receiveShadow = true; scene.add(pl); }
        const objs = o.objects.map(ob => { const g = buildObject(T, ctx, ob, o.id); scene.add(g); if (g.userData.glow) scene.add(g.userData.glow); return g; });
        if (envUsed) { // reflections: the procedural studio environment on metal materials (or all, with env: true / {...})
          const eo = typeof o.env === "object" && o.env ? o.env : {}, tex = envMap(G, C(ctx, eo.tint, "#B9D3FF")), k = isNum(eo.intensity) ? eo.intensity : 1;
          for (const g of objs) g.traverse(m => { if (m.isMesh) for (const mt of [].concat(m.material)) if (mt.isMeshStandardMaterial && (envAll || mt.metalness >= 0.5)) { mt.envMap = tex; mt.envMapIntensity = k * (mt.userData.env_k || 1); mt.needsUpdate = true; } });
        }
        const fitted = fitOn ? fitCamera(T, objs, o.objects, camo, box.w / box.h) : null;
        st = { scene, cam, objs, lights, fitted }; STATE.set(o.id, st);
      }
      st.objs.forEach((g, i) => place(g, o.objects[i], lt));
      cameraAt(st.cam, o, lt, dur, st.fitted);
      for (const g of st.objs) glowPose(T, g, st.cam);
      if (typeof o.update === "function") o.update(T, st.scene, lt, dur, ctx); // bespoke per-frame posing (must stay a pure function of lt)
      const rw = Math.max(16, Math.round(box.w * scale)), rh = Math.max(16, Math.round(box.h * scale));
      if (G.cv.width !== rw || G.cv.height !== rh) G.r.setSize(rw, rh, false);
      if (st.cam.aspect !== box.w / box.h) { st.cam.aspect = box.w / box.h; st.cam.updateProjectionMatrix(); }
      G.r.render(st.scene, st.cam);
      g2.imageSmoothingEnabled = true; g2.imageSmoothingQuality = "high";
      g2.drawImage(G.cv, 0, 0, rw, rh, box.x, box.y, box.w, box.h);
      const ms = performance.now() - t0; STATS.frames++; STATS.ms_last = ms; STATS.ms_sum += ms; if (ms > STATS.ms_max) STATS.ms_max = ms;
      return "";
    },
  }));
}
})();
