/* Faceless proof reel (voice-over slice of Naman's Reel 9: hook + prompts 1-3, 33.5 s). Built only from the VEOS.fx
   toolkit + the canvas camera: kinetic type stacks, an icon card, number cards, a morph hand-off, a hub diagram with
   redacted bars, three diagram "stations" on one canvas that the camera travels between (zoom-through, push, pull,
   dolly, orbit), and ambient paper / void worlds. Stage hidden throughout (no presenter). */

// station k lives on the world canvas: screen layout (1080x1920 at rest) + this offset
const ST = { 1: [0, 1940], 2: [1300, 1940], 3: [1300, 3040] };
const at = (k, x, y, w, h) => ({ x: x + ST[k][0], y: y + ST[k][1], w, h });

/* ---------------------------------------------------------------- worlds (z1, pinned; they follow the camera themselves) */
VEOS.fx.ambient({ id: "amb-paper-1", t_in: 0, t_out: 3.45, kind: "paper", bg: "canvas", ink: "grid" });
VEOS.fx.ambient({ id: "amb-void", t_in: 3.45, t_out: 7.65, kind: "void", glow: "accent" });
VEOS.fx.ambient({ id: "amb-paper-2", t_in: 7.65, t_out: 33.467, kind: "paper", bg: "canvas", ink: "grid", follow: 0.7 });

/* ---------------------------------------------------------------- HOOK 0-3.45: the vague prompt, struck out; kinetic stack */
VEOS.fx.card({
  id: "hook-prompt", t_in: 0, t_out: 3.45, z: 4, x: 120, y: 250, w: 840, h: 300, theme: "light", icon: "chat", accent: "primary",
  kicker: "your prompt", title: "_\"make my app better\"_", titleSize: 64, in: "rise", out: "none", roles: ["primary", "bad"], events: [2.21],
  body(ctx, lt) {
    if (lt < 2.21) return "";
    const p = Math.min(1, (lt - 2.21) * 30 / 7), bad = ctx.col("bad");
    return `<div style="position:absolute;left:236px;top:176px;width:${Math.round(520 * p)}px;height:8px;border-radius:4px;background:${bad}"></div>
      <div style="position:absolute;right:34px;top:34px;width:92px;height:92px;border-radius:50%;background:${bad};display:flex;align-items:center;justify-content:center;transform:scale(${(0.4 + 0.6 * ctx.ease.back(p)).toFixed(3)})">${VEOS.fx.icon("x", { size: 60, color: "#fff", stroke: 5 })}</div>`;
  },
});
VEOS.fx.typeStack({
  id: "hook-stack", t_in: 0, t_out: 3.45, z: 5, y: 640, anchor: "top", out: "none", roles: ["primary"],
  lines: [
    { text: "tum jo **prompts**", at: 0 },
    { text: "app banane ke liye", at: 0.6 },
    { text: "de rahe ho na,", at: 1.47 },
    { text: "usse {ghanta|primary}", at: 1.95 },
    { text: "kuch nahi hone wala.", at: 2.55 },
  ],
});

/* ---------------------------------------------------------------- PROOF 3.45-7.65: dark world, 6 months -> 4 apps */
VEOS.fx.typeStack({
  id: "proof-stack", t_in: 3.45, t_out: 7.65, z: 5, y: 300, anchor: "top", color: "paper",
  lines: [{ text: "main ye _workflow_", at: 3.45 }, { text: "use karta hoon", at: 4.27 }],
});
VEOS.fx.card({ id: "proof-6", t_in: 5.25, t_out: 7.65, z: 4, x: 110, y: 700, w: 400, h: 460, theme: "glass", layout: "stack", align: "center",
  number: "6", numberSize: 220, title: "mahine", titleSize: 56 });
VEOS.fx.card({ id: "proof-4", t_in: 6.13, t_out: 7.42, z: 4, x: 570, y: 700, w: 400, h: 460, theme: "glass", layout: "stack", align: "center",
  number: "4", numberSize: 220, title: "apps shipped", titleSize: 56, out: "none" });
// continuity: the "4 apps" card becomes the hub hexagon across the world flip (P-MORPH hand-off)
VEOS.fx.morphShape({
  id: "morph-card-hub", t_in: 7.4, t_out: 8.05, z: 3, in: "none", out: "none", dur: 0.5,
  keys: [
    { at: 7.4, shape: { kind: "rect", x: 570, y: 700, w: 400, h: 460, radius: 40 }, fill: "#2E2C2B", stroke: "#5A5856", width: 3 },
    { at: 7.5, shape: { kind: "hex", cx: 540, cy: 900, r: 160 }, fill: "#2B2421", stroke: "#2B2421", width: 0 },
  ],
});

/* ---------------------------------------------------------------- PROMISE 7.65-12.35: hub with 7 redacted bars; #7 lit */
VEOS.fx.typeStack({
  id: "promise-stack", t_in: 7.65, t_out: 11.75, z: 5, y: 250, anchor: "top",
  lines: [{ text: "ye rahe wo poore", at: 7.65 }, { text: "**commands** aur _prompts_", at: 8.43 }],
});
const HUB = { cx: 540, cy: 900, r: 340 };
const bars = Array.from({ length: 7 }, (_, k) => {
  const a = (-90 + k * 360 / 7) * Math.PI / 180;
  const n = { id: `n${k + 1}`, x: Math.round(HUB.cx + HUB.r * Math.cos(a) - 110), y: Math.round(HUB.cy + HUB.r * Math.sin(a) - 26), w: 220, h: 52,
    shape: "bar", reveal: "redact", at: 9.02 + k * 0.1 };
  if (k === 6) Object.assign(n, { label: "saves your app", size: 48, label_at: 10.4, active: [[9.85, 12.35]] });
  return n;
});
VEOS.fx.diagram({
  id: "hub", t_in: 7.95, t_out: 12.35, z: 3, out: "none", dimInactive: 0.4, roles: ["primary"],
  nodes: [{ id: "hub", x: 380, y: 740, w: 320, h: 320, shape: "hex", reveal: "fade", at: 7.98, label: "7", size: 80, sub: "prompts", fill: "ink", nodim: true }, ...bars],
  edges: bars.map(b => ({ from: "hub", to: b.id, at: b.at, dur: 0.3, dot: true })),
});

/* ---------------------------------------------------------------- the three stations (world canvas) */
VEOS.fx.diagram({
  id: "st1", t_in: 12.35, t_out: 22.2, z: 3, out: "none", roles: ["primary", "good"],
  nodes: [
    { id: "s1-num", ...at(1, 96, 300, 120, 120), shape: "circle", fill: "primary", ink: "ink", label: "1", size: 72, at: 12.4 },
    { id: "s1-title", ...at(1, 250, 300, 600, 120), shape: "pill", fill: "ink", label: "/init", size: 72, reveal: "type", at: 12.45, label_at: 13.15 },
    { id: "s1-dir", ...at(1, 96, 520, 888, 250), shape: "rect", fill: "night", icon: "folder", label: "code directory", sub: "Claude reads your project", size: 64, at: 14.45 },
    { id: "s1-mem", ...at(1, 96, 860, 888, 250), shape: "rect", fill: "paper", outline: "ink", ink: "ink", icon: "file", label: "CLAUDE.md", sub: "a memory file", size: 64, at: 15.28, active: [[16.4, 20.6]] },
    { id: "s1-c1", ...at(1, 96, 1150, 420, 84), shape: "pill", fill: "paper", outline: "ink", ink: "ink", label: "every context", size: 48, at: 17.35, active: [[19.86, 20.6]] },
    { id: "s1-c2", ...at(1, 564, 1150, 420, 84), shape: "pill", fill: "paper", outline: "ink", ink: "ink", label: "every session", size: 48, at: 18.76, active: [[19.86, 20.6]] },
  ],
  edges: [{ from: "s1-dir", to: "s1-mem", at: 15.4, dur: 0.4, style: "arrow" }],
});
VEOS.fx.diagram({
  id: "st2", t_in: 20.6, t_out: 27.9, z: 3, out: "none", roles: ["primary"],
  nodes: [
    { id: "s2-num", ...at(2, 96, 300, 120, 120), shape: "circle", fill: "primary", ink: "ink", label: "2", size: 72, at: 21.0 },
    { id: "s2-title", ...at(2, 250, 300, 600, 120), shape: "pill", fill: "ink", label: "PRD prompt", size: 64, reveal: "type", at: 21.05, label_at: 21.42 },
    { id: "s2-idea", ...at(2, 96, 520, 400, 330), shape: "rect", fill: "paper", outline: "ink", ink: "ink", icon: "bulb", label: "app idea", size: 64, at: 22.64, active: [[23.3, 24.15]] },
    { id: "s2-doc", ...at(2, 584, 520, 400, 330), shape: "rect", fill: "night", icon: "doc", label: "PRD", sub: "features + screens", size: 64, at: 25.08 },
    { id: "s2-fz", ...at(2, 390, 436, 300, 70), shape: "none", label: "formalize", size: 48, at: 24.15 },
  ],
  edges: [{ from: "s2-idea", to: "s2-doc", at: 24.15, dur: 0.5, style: "arrow" }],
});
VEOS.fx.diagram({
  id: "st3", t_in: 26.3, t_out: 33.467, z: 3, out: "none", roles: ["primary", "good"],
  nodes: [
    { id: "s3-num", ...at(3, 96, 300, 120, 120), shape: "circle", fill: "primary", ink: "ink", label: "3", size: 72, at: 26.95 },
    { id: "s3-title", ...at(3, 250, 300, 600, 120), shape: "pill", fill: "ink", label: "Plan Mode", size: 64, reveal: "type", at: 27.0, label_at: 27.28 },
    { id: "s3-keys", ...at(3, 210, 560, 660, 160), shape: "none", at: 28.46 },
    { id: "s3-shift", ...at(3, 210, 560, 290, 160), shape: "rect", radius: 30, fill: "paper", outline: "ink", ink: "ink", label: "Shift", size: 64, at: 28.72 },
    { id: "s3-plus", ...at(3, 500, 560, 80, 160), shape: "none", label: "+", size: 64, at: 28.6 },
    { id: "s3-tab", ...at(3, 580, 560, 290, 160), shape: "rect", radius: 30, fill: "paper", outline: "ink", ink: "ink", label: "Tab", size: 64, at: 28.46 },
    { id: "s3-plan", ...at(3, 96, 880, 888, 300), shape: "rect", fill: "night", icon: "list", label: "the full app plan", sub: "before any code", size: 64, at: 30.75, active: [[31.95, 33.467]] },
    { id: "s3-done", ...at(3, 846, 910, 100, 100), shape: "circle", fill: "good", icon: "check", ink: "ink", size: 48, at: 32.9 },
  ],
  edges: [{ from: "s3-keys", to: "s3-plan", at: 30.75, dur: 0.4, style: "arrow" }],
});
