/* Vibe Editing OS object tracks and scene anchors (Package E). Pure maths, no DOM: loaded by player.html before core.js
   (window.VEOS_TRACKS) and by node in the engine tests (module.exports). Mirrors engine/src/veos/anchors.py.

   bundle.tracks: {id: {space: "edit"|"clip", mode: "box"|"point", size: [W, H], min_conf, f0, n, x[], y[], w[], h[], c[], lost[]}}
   (`veos track` -> plan/tracks/<id>.json -> `veos bundle`). Edit tracks are in FOOTAGE px (the 1080x1920 edit frame before
   the base reframe), indexed by edit frame; core maps them through the live footage->screen transform, like ctx.face().
   Clip tracks are in the clip's own px, indexed by clip frame (30 fps); the anchor's `place` puts the clip on screen.

   A scene anchor: {track, offset: [dx, dy], point: center|top|bottom|left|right, scale_with, smooth (frames, default 2),
   lost: hold|fade, fade (frames, default 6), min_conf, clip_t0, speed, place: {x, y, w}}. The centre of the scene's
   `box` lands on the track point + offset (the offset scales with the object when scale_with is on); while the object is
   lost the scene holds its last confident position (`hold`) or fades out and back in around the lost frames (`fade`).
*/
(function (root, factory) {
  if (typeof module === "object" && module.exports) module.exports = factory();
  else root.VEOS_TRACKS = factory();
})(typeof self !== "undefined" ? self : this, function () {
  const FPS = 30, SMOOTH = 2, FADE = 6, SCALE_LIM = [0.25, 4];
  const POINTS = ["center", "top", "bottom", "left", "right"], LOSTS = ["hold", "fade"];
  const isNum = v => typeof v === "number" && isFinite(v);
  const cl = (x, a, b) => Math.max(a, Math.min(b, x));

  /* anchor shape problems (registration: VEOS.scene) */
  function errors(a) {
    if (!a || typeof a !== "object" || Array.isArray(a)) return ["anchor must be an object {track, offset, ...}"];
    const e = [];
    if (typeof a.track !== "string" || !a.track) e.push("anchor.track must be a track id (plan/tracks/<id>.json)");
    if (a.offset != null && !(Array.isArray(a.offset) && a.offset.length === 2 && a.offset.every(isNum))) e.push("anchor.offset must be [dx, dy] px");
    if (a.point != null && !POINTS.includes(a.point)) e.push(`anchor.point must be one of ${POINTS.join("|")}`);
    if (a.lost != null && !LOSTS.includes(a.lost)) e.push("anchor.lost must be hold | fade");
    for (const [k, lo, hi] of [["smooth", 0, 15], ["fade", 1, 30]]) if (a[k] != null && !(isNum(a[k]) && a[k] >= lo && a[k] <= hi && Math.round(a[k]) === a[k])) e.push(`anchor.${k} must be an integer ${lo}..${hi} (frames)`);
    for (const k of ["min_conf", "max_lost"]) if (a[k] != null && !(isNum(a[k]) && a[k] >= 0 && a[k] <= 1)) e.push(`anchor.${k} must be a number 0..1`);
    if (a.scale_with != null && typeof a.scale_with !== "boolean") e.push("anchor.scale_with must be true or false");
    if (a.clip_t0 != null && !(isNum(a.clip_t0) && a.clip_t0 >= 0)) e.push("anchor.clip_t0 must be clip seconds >= 0");
    if (a.speed != null && !(isNum(a.speed) && a.speed > 0)) e.push("anchor.speed must be > 0");
    if (a.place != null && !(a.place && ["x", "y", "w"].every(k => isNum(a.place[k])) && a.place.w > 0)) e.push("anchor.place must be {x, y, w}: where the clip is drawn on screen (left, top, width px)");
    return e;
  }

  const good = (T, i, mc) => i >= 0 && i < T.n && !T.lost[i] && (T.c[i] || 0) >= mc;

  /* the track at frame f: centred moving average over confident frames within +-smooth; on a lost frame the nearest
     confident frame before it (else after it). {x, y, w, h, conf, lost, gap} or null */
  function sample(T, f, smooth, minConf) {
    if (!T || !(T.n > 0)) return null;
    const mc = minConf == null ? (T.min_conf == null ? 0.5 : T.min_conf) : minConf, sm = smooth == null ? SMOOTH : smooth;
    const i = f - T.f0;
    let ic = cl(i, 0, T.n - 1), gap = 0;
    const lost = !good(T, i, mc);
    if (lost) {
      let j = null;
      for (let d = 1; d <= T.n && j == null; d++) { if (good(T, ic - d, mc)) j = ic - d; else if (good(T, ic + d, mc)) j = ic + d; }
      if (j == null) return null;
      let back = null; for (let d = 0; d < T.n; d++) if (good(T, ic - d, mc)) { back = ic - d; break; }
      gap = Math.abs(j - ic);
      ic = back != null ? back : j;
    }
    let x = 0, y = 0, w = 0, h = 0, c = 0;
    for (let k = ic - sm; k <= ic + sm; k++) if (good(T, k, mc)) { x += T.x[k]; y += T.y[k]; w += T.w[k]; h += T.h[k]; c++; }
    if (!c) return null;
    return { x: x / c, y: y / c, w: w / c, h: h / c, conf: T.c[cl(i, 0, T.n - 1)] || 0, lost: lost || i < 0 || i >= T.n, gap };
  }

  function pointOf(s, point) {
    const { x, y, w, h } = s;
    switch (point || "center") {
      case "top": return [x + w / 2, y];
      case "bottom": return [x + w / 2, y + h];
      case "left": return [x, y + h / 2];
      case "right": return [x + w, y + h / 2];
      default: return [x + w / 2, y + h / 2];
    }
  }

  /* the track frame an anchored scene shows at edit frame n (edit: n; clip: clip_t0 + lt * speed) */
  function trackFrame(a, T, fin, n) {
    return T.space === "clip" ? Math.round(((a.clip_t0 || 0) + (n - fin) / FPS * (a.speed || 1)) * FPS) : n;
  }

  /* the anchor at edit frame n. env: {toScr(x, y) -> [sx, sy] (footage px -> screen, edit tracks), scaleAt(n) -> footage
     -> screen scale at frame n (camera x stage), visible (footage window shown)}. Returns {px, py (target point on screen),
     dx, dy (box-centre translation), s (scale about the box centre), op, lost} or null (no track data). */
  function state(a, T, fin, n, box, env) {
    if (!T) return null;
    const sm = sample(T, trackFrame(a, T, fin, n), a.smooth, a.min_conf);
    if (!sm) return null;
    let [px, py] = pointOf(sm, a.point), k = 1;
    if (T.space === "clip") {
      const pl = a.place || { x: 0, y: 0, w: T.size[0] };
      k = pl.w / T.size[0]; px = pl.x + px * k; py = pl.y + py * k;
    } else if (env && env.toScr) { [px, py] = env.toScr(px, py); }
    let s = 1;
    if (a.scale_with && T.mode !== "point") {
      const ref = sample(T, trackFrame(a, T, fin, fin), a.smooth, a.min_conf);
      if (ref && ref.w > 0 && ref.h > 0 && sm.w > 0 && sm.h > 0) {
        s = Math.sqrt(sm.w * sm.h / (ref.w * ref.h));
        if (T.space !== "clip" && env && env.scaleAt) s *= env.scaleAt(n) / (env.scaleAt(fin) || 1); // a camera punch scales it too
        s = cl(s, SCALE_LIM[0], SCALE_LIM[1]);
      }
    }
    const off = a.offset || [0, 0], tx = px + off[0] * s, ty = py + off[1] * s;
    const cx = box.x + box.w / 2, cy = box.y + box.h / 2;
    let op = 1;
    if (sm.lost && a.lost === "fade") op = 0;
    else if (a.lost === "fade") { // fade out before / back in after a lost run (pure in n: distance to the nearest lost frame)
      const F = a.fade || FADE, f = trackFrame(a, T, fin, n), mc = a.min_conf == null ? (T.min_conf == null ? 0.5 : T.min_conf) : a.min_conf;
      for (let d = 1; d < F; d++) if (!good(T, f - T.f0 - d, mc) && f - T.f0 - d >= 0 || !good(T, f - T.f0 + d, mc) && f - T.f0 + d < T.n) { op = d / F; break; }
    }
    if (env && env.visible === false && T.space !== "clip") op = 0;
    return { px: tx, py: ty, dx: tx - cx, dy: ty - cy, s, op, lost: sm.lost, cx, cy };
  }

  /* ctx.track(id) result on screen: {x, y, w, h, cx, cy, conf, lost} */
  function screenBox(T, f, o, env) {
    o = o || {};
    const sm = sample(T, f, o.smooth, o.min_conf);
    if (!sm) return null;
    let x0, y0, x1, y1;
    if (T.space === "clip") {
      const pl = o.place || { x: 0, y: 0, w: T.size[0] }, k = pl.w / T.size[0];
      x0 = pl.x + sm.x * k; y0 = pl.y + sm.y * k; x1 = x0 + sm.w * k; y1 = y0 + sm.h * k;
    } else {
      const p = [env.toScr(sm.x, sm.y), env.toScr(sm.x + sm.w, sm.y), env.toScr(sm.x, sm.y + sm.h), env.toScr(sm.x + sm.w, sm.y + sm.h)];
      x0 = Math.min(...p.map(q => q[0])); y0 = Math.min(...p.map(q => q[1])); x1 = Math.max(...p.map(q => q[0])); y1 = Math.max(...p.map(q => q[1]));
    }
    return { x: x0, y: y0, w: x1 - x0, h: y1 - y0, cx: (x0 + x1) / 2, cy: (y0 + y1) / 2, conf: sm.conf, lost: sm.lost };
  }

  return { FPS, SMOOTH, FADE, POINTS, LOSTS, errors, sample, pointOf, trackFrame, state, screenBox };
});
