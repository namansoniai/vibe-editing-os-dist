/* Vibe Editing OS renderer: figure-bound data helpers (E-08, structure §18). Classic script, loaded by player.html after
   core.js. Every number they show comes from plan/figures.json (resolved by the engine into the bundle) and is written by
   ctx.fmtNum, so V-DATA / V-NUMFMT can check it. Each factory registers a normal VEOS.scene with honest metadata:
   `figure` / `figures` (binding), `lands` (counter landings, edit seconds), `scale` ({id, max}: the shared axis),
   `events`, `text`, `text_content` (every value it will show), `text_px`, `text_class`, `box`.

     VEOS.data.counter(o)   a number that counts up and lands on each step's spoken word (hero number, ledger)
     VEOS.data.bars(o)      horizontal bars for several figures on ONE shared scale, value roll-ups, a leader chip
     VEOS.data.slider(o)    a parameter axis (years 2/4/6/8/10) whose handle jumps to the step being spoken
   Render helpers: VEOS.data.valueAt(id, t, o) (= ctx.figAt), VEOS.data.width(value, scaleId, w).
   Pass in, out, roles, kind, overlaps, parallax, extra: {...} through like VEOS.fx. Pure functions of the frame. */
(function () {
"use strict";
const VEOS = window.VEOS;
if (!VEOS) return;
const FPS = 30;
const cl = (x, a = 0, b = 1) => (x < a ? a : x > b ? b : x);
const r2 = v => Math.round(v * 100) / 100;
const esc = s => String(s == null ? "" : s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
const backOut = (p, s = 1.70158) => { p = cl(p); const c = s + 1, q = p - 1; return 1 + c * q * q * q + s * q * q; };
const D = VEOS.data = { version: 1 };
const C = (ctx, v, d) => { const x = v == null ? d : v; return (ctx.tokens.colours && ctx.tokens.colours[x]) || x; };
const slotOf = (ctx, s) => { const F = ctx.tokens.fonts || {}; return [s, "display", "body"].find(k => F[k]) || Object.keys(F).find(k => k !== "emoji") || s; };
const ff = (ctx, s) => ctx.fam(slotOf(ctx, s));

function need(id, what) {
  const f = VEOS.fig(id);
  if (!f) VEOS.errors.push(`${what}: figure '${id}' is not in plan/figures.json (run \`veos bundle\` after writing it)`);
  return f;
}
function scene(o, d) {
  const s = Object.assign({}, d, o.extra || {});
  for (const k of ["in", "out", "behind", "follow_footage", "parallax", "may_overlap_face", "overlaps", "cuts", "kind", "roles", "exception", "depicts", "illustrative"]) if (o[k] !== undefined) s[k] = o[k];
  if (o.events) s.events = [...new Set([...(s.events || []), ...o.events])].sort((a, b) => a - b);
  return VEOS.scene(s);
}
const local = (ts, t_in, t_out) => [...new Set(ts.filter(t => t != null).map(t => Math.round((t - t_in) * 1000) / 1000)
  .filter(v => v > 0.02 && v < t_out - t_in - 0.02))].sort((a, b) => a - b);
const stepIdx = (f, which) => (which == null || which === "all" ? f.steps.map((_, i) => i) : [].concat(which));

D.valueAt = (id, t, o) => VEOS.figAt(id, t, o);
D.width = (value, scaleId, w) => { const sc = VEOS.figScale(scaleId); const mx = sc && sc.max > 0 ? sc.max : Math.abs(value) || 1; return w * cl(Math.abs(value) / mx); };

/* counter: {id, figure, t_in, t_out, z=5, x, y, w=760, h, align center|left|right, size=150, font ('numeric' slot, else
   display), color role ('paper'), label, labelSize=44, labelColor, roll=12 frames, from=0, format (fmtNum override),
   steps: 'all' | [indices] (which landings it shows), glow (role)}. The count rolls into each step and lands ON the step's
   `at` (the spoken number word): V-DATA checks the landing against the transcript (+-5 frames). */
D.counter = function (o) {
  const f = need(o.figure, `data.counter ${o.id}`);
  if (!f) return null;
  const idx = stepIdx(f, o.steps), size = o.size || 150, ls = o.labelSize || 44;
  const w = o.w || 760, h = o.h || Math.round(size * 1.15 + (o.label ? ls * 1.5 : 0)), x = o.x, y = o.y;
  const texts = idx.map(i => VEOS.fmtNum(f.steps[i].shown, f, o.format));
  const lands = idx.filter(i => f.steps[i].at != null).map(i => ({ t: f.steps[i].at, step: i, figure: f.id, value: f.steps[i].shown }));
  const roll = o.roll != null ? o.roll : 12;
  // one state change per landing (a short roll leads into it); a long roll (>= 20 f) is a visible change of its own
  const evs = local(lands.flatMap(L => (roll >= 20 ? [L.t - roll / FPS, L.t] : [L.t])), o.t_in, o.t_out);
  return scene(o, {
    id: o.id, t_in: o.t_in, t_out: o.t_out, z: o.z || 5, in: "settle", out: "blur", figure: f.id, lands,
    text: true, text_content: [o.label, ...texts].filter(Boolean).join(" "), text_px: Math.min(size, o.label ? ls : size),
    text_class: o.text_class || "TC-display", fx: "data.counter", box: { x, y, w, h }, events: evs,
    render(ctx) {
      const st = ctx.figAt(f.id, ctx.t, { roll, from: o.from != null ? o.from : 0 });
      const first = idx.length ? f.steps[idx[0]] : null;
      const show = first && first.at != null && ctx.t < first.at - roll / FPS ? (o.from != null ? o.from : 0) : st.value;
      const txt = ctx.fmtNum(show, f.id, o.format), fg = C(ctx, o.color, "paper");
      const glow = o.glow ? `text-shadow:0 0 28px ${ctx.hexA(o.glow, 0.55)};` : "";
      const pop = st.landed && st.i >= 0 && f.steps[st.i].at != null ? 1 + 0.06 * Math.max(0, 1 - (ctx.t - f.steps[st.i].at) * FPS / 6) : 1;
      const al = o.align || "center";
      return ctx.html(`<div style="position:absolute;left:${x}px;top:${y}px;width:${w}px;height:${h}px;display:flex;flex-direction:column;justify-content:center;align-items:${al === "left" ? "flex-start" : al === "right" ? "flex-end" : "center"}">
        <div style="font:700 ${size}px/1 ${ff(ctx, o.font || "numeric")};font-variant-numeric:tabular-nums;color:${fg};${glow}white-space:nowrap;transform:scale(${r2(pop)});transform-origin:50% 60%">${esc(txt)}</div>
        ${o.label ? `<div style="margin-top:${Math.round(ls * 0.35)}px;font:600 ${ls}px/1.1 ${ff(ctx, "display")};color:${C(ctx, o.labelColor, o.color || "paper")};opacity:.82">${esc(o.label)}</div>` : ""}</div>`);
    },
  });
};

/* bars: {id, figures: [ids], t_in, t_out, z=4, x, y, w=1000, rowH=118, gap=30, scale (scale id; default the figures'
   shared scale_id), labels {id: text}, colors {id: role}, track (role or rgba), card (role, the row background), roll=10,
   valueSize=52, labelSize=46, leader: {text, role, by: 'max' | 'min'} (a chip on the row that is ahead now),
   steps: 'all' | [indices]}. Every bar's length is value / scale.max of the SHARED scale, so compared bars share axes. */
D.bars = function (o) {
  const figs = (o.figures || []).map(id => need(id, `data.bars ${o.id}`)).filter(Boolean);
  if (!figs.length) return null;
  const sid = o.scale || figs[0].scale_id;
  if (figs.some(f => f.scale_id !== sid)) VEOS.errors.push(`data.bars ${o.id}: figures ${figs.map(f => f.id).join(", ")} must share scale_id '${sid}' (same axes)`);
  const sc = VEOS.figScale(sid), smax = sc && sc.max > 0 ? sc.max : Math.max(...figs.flatMap(f => f.steps.map(s => Math.abs(s.shown || 0))), 1);
  const rowH = o.rowH || 118, gap = o.gap || 30, w = o.w || 1000, x = o.x, y = o.y, vs = o.valueSize || 52, ls = o.labelSize || 46;
  const roll = o.roll != null ? o.roll : 10, h = figs.length * rowH + (figs.length - 1) * gap;
  const texts = figs.flatMap(f => stepIdx(f, o.steps).map(i => VEOS.fmtNum(f.steps[i].shown, f)));
  const lands = figs.flatMap(f => stepIdx(f, o.steps).filter(i => f.steps[i].at != null).map(i => ({ t: f.steps[i].at, step: i, figure: f.id, value: f.steps[i].shown })));
  const labels = figs.map(f => (o.labels && o.labels[f.id]) || f.label || f.id);
  return scene(o, {
    id: o.id, t_in: o.t_in, t_out: o.t_out, z: o.z || 4, in: "rise", out: "blur", figures: figs.map(f => f.id), lands,
    scale: { id: sid, max: smax }, text: true, text_content: [...labels, ...texts, o.leader && o.leader.text].filter(Boolean).join(" "),
    text_px: Math.min(vs, ls), text_class: o.text_class || "TC-label", fx: "data.bars", box: { x, y, w, h },
    events: local(lands.map(L => L.t), o.t_in, o.t_out),
    render(ctx) {
      const cur = figs.map(f => ctx.figAt(f.id, ctx.t, { roll, from: 0 }).value || 0);
      const lead = o.leader ? cur.indexOf((o.leader.by === "min" ? Math.min : Math.max)(...cur)) : -1;
      const anyShown = cur.some(v => v > 0);
      let html = "";
      figs.forEach((f, k) => {
        const ry = y + k * (rowH + gap), labW = Math.round(ls * 2.9), bx = x + labW + 28, bw = w - labW - 28 - Math.round(vs * 4.6);
        const v = cur[k], len = bw * cl(Math.abs(v) / smax), col = C(ctx, o.colors && o.colors[f.id], k ? "ink" : "primary");
        const val = v > 0 || f.steps.some(s => s.at != null && ctx.t >= s.at) ? ctx.fmtNum(v, f) : "";
        html += `<div style="position:absolute;left:${x}px;top:${ry}px;width:${w}px;height:${rowH}px;border-radius:${Math.round(rowH * 0.2)}px;background:${C(ctx, o.card, "paper")};box-shadow:0 10px 30px rgba(0,0,0,.18)"></div>
          <div style="position:absolute;left:${x + 14}px;top:${ry + 14}px;width:${labW}px;height:${rowH - 28}px;border-radius:${Math.round(rowH * 0.14)}px;background:${col};color:${(ctx.tokens.text_on || {})[(o.colors && o.colors[f.id]) || (k ? "ink" : "primary")] || "#fff"};display:flex;align-items:center;justify-content:center;font:800 ${ls}px/1 ${ff(ctx, "display")};white-space:nowrap">${esc(labels[k])}</div>
          <div style="position:absolute;left:${bx}px;top:${ry + rowH / 2 - 10}px;width:${bw}px;height:20px;border-radius:10px;background:${C(ctx, o.track, "rgba(0,0,0,.12)")}"></div>
          <div style="position:absolute;left:${bx}px;top:${ry + rowH / 2 - 10}px;width:${r2(len)}px;height:20px;border-radius:10px;background:${col}"></div>
          <div style="position:absolute;left:${x + w - Math.round(vs * 4.6) - 10}px;top:${ry}px;width:${Math.round(vs * 4.6)}px;height:${rowH}px;display:flex;align-items:center;justify-content:flex-end;font:800 ${vs}px/1 ${ff(ctx, o.font || "numeric")};font-variant-numeric:tabular-nums;color:${C(ctx, "ink")};white-space:nowrap">${esc(val)}</div>`;
        if (k === lead && anyShown && o.leader) {
          html += `<div data-tc="TC-label" style="position:absolute;left:${x + w - 300}px;top:${ry - 34}px;width:280px;height:50px;display:flex;justify-content:flex-end"><span style="padding:4px 16px;border-radius:12px;background:${C(ctx, o.leader.role, "bad")};color:${(ctx.tokens.text_on || {})[o.leader.role || "bad"] || "#fff"};font:800 40px/1.05 ${ff(ctx, "display")};white-space:nowrap">${esc(o.leader.text)}</span></div>`;
        }
      });
      return ctx.html(html);
    },
  });
};

/* slider: {id, figure (its steps' x are the ticks), t_in, t_out, z=4, x, y, w=960, label ('Yr'), size=40, color role
   ('paper'), handle role ('paper'), roll=8}. The handle sits on the step being spoken (moves over `roll` frames into `at`). */
D.slider = function (o) {
  const f = need(o.figure, `data.slider ${o.id}`);
  if (!f) return null;
  const xs = f.steps.map(s => s.x), w = o.w || 960, x = o.x, y = o.y, size = o.size || 40, roll = o.roll != null ? o.roll : 8;
  const n = xs.length, pos = i => x + (n > 1 ? (w * i) / (n - 1) : w / 2);
  const ticks = xs.map(v => (v == null ? "" : VEOS.fmtNum(v, { currency: "", style: "full", unit: "" })));
  return scene(o, {
    id: o.id, t_in: o.t_in, t_out: o.t_out, z: o.z || 4, in: "rise", out: "blur", figure: f.id,
    text: true, text_content: [o.label, ...ticks].filter(Boolean).join(" "), text_px: size, text_class: o.text_class || "TC-label",
    fx: "data.slider", box: { x: x - 40, y: y - 40, w: w + 80, h: size * 2.6 + 50 },
    events: local(f.steps.map(s => s.at), o.t_in, o.t_out),
    render(ctx) {
      let i = -1, p = 1;
      f.steps.forEach((s, k) => { if (s.at == null || ctx.t >= s.at) i = k; });
      const nx = f.steps.findIndex(s => s.at != null && ctx.t < s.at && ctx.t >= s.at - roll / FPS);
      let hx = pos(Math.max(i, 0));
      if (nx >= 0) { p = cl((ctx.t - (f.steps[nx].at - roll / FPS)) / (roll / FPS)); const e = 1 - Math.pow(1 - p, 3); hx = pos(Math.max(i, 0)) + (pos(nx) - pos(Math.max(i, 0))) * e; }
      const fg = C(ctx, o.color, "paper"), hd = C(ctx, o.handle, "paper");
      let html = `<div style="position:absolute;left:${x}px;top:${y - 3}px;width:${w}px;height:6px;border-radius:3px;background:${ctx.hexA(o.color || "paper", 0.45)}"></div>`;
      xs.forEach((v, k) => { html += `<div style="position:absolute;left:${r2(pos(k) - 60)}px;top:${y + 26}px;width:120px;text-align:center;font:600 ${size}px/1 ${ff(ctx, "display")};color:${fg};opacity:${k === i ? 1 : 0.7}">${esc(ticks[k])}</div>`; });
      if (o.label) html += `<div style="position:absolute;left:${x - 40}px;top:${y - size - 22}px;font:600 ${size}px/1 ${ff(ctx, "display")};color:${fg};opacity:.8">${esc(o.label)}</div>`;
      if (i >= 0 || nx >= 0) html += `<div style="position:absolute;left:${r2(hx - 18)}px;top:${y - 18}px;width:36px;height:36px;border-radius:18px;background:${hd};box-shadow:0 4px 14px rgba(0,0,0,.35);transform:scale(${r2(nx >= 0 ? 1 + 0.15 * Math.sin(Math.PI * p) : backOut(1))})"></div>`;
      return ctx.html(html);
    },
  });
};
})();
