# Proof Dashboard Style Playbook (template v1)

**Purpose.** This playbook makes you (Claude, the editor) cut hype, proof-first explainers: {{BV-01.name|the creator}} sits at a desk, matted onto a dark virtual set that changes with the section, and every claim is proven on screen with a real app screen, a counter or a pair of cards. The input is one talking-head take (SW-01 `talking_head`), plus the creator's screen recordings and results screens (SW-12 `medium`). When those are missing, you build labelled, generic stand-ins (§12.3, §12.5). The glow banner is set in **Montserrat Black** (font slot `banner`; matched to the real letterforms in the 2026-10-06 audit).

**Style DNA** `[DNA]`. A creator on a night-city or neon set with a huge two-line banner glowing at chest height on frame 0. Under it, phone-shaped cards prove the claim: the loser floods red, the winner flashes gold and its view counter rolls. Then the reel becomes a dashboard: real screens with a glowing cyan cursor orb tapping exactly what is being said, caps captions of 1–4 words with one glowing keyword, and neon colour that always means something (red wrong, green right, gold winner). It looks like a creator-economy control room, not a vlog.

**Copy these 5 things** (if a reel lacks any of them, it is not this style):
1. **The glow banner at the chest on frame 0**: two fit-width lines, one white and one glowing (either order), centred at y ≈ 1010 (§5.2, §6.2, P-GLOW-BANNER).
2. **Proof cards with counters under it**: phone-shaped cards, loser red, winner gold, view counter rolling to the real number (§8.3 B-2, §18).
3. **UI proof with the cursor orb**: the exact screen, a cyan orb that travels, presses and ripples on the spoken verb (§8.3 B-3, §17.2).
4. **The meaning axis**: red = wrong, green = right, gold = winner; colour lands on the verdict word (§4, B-4).
5. **The swapped virtual set + glowing-keyword caps captions** (§3.1 P-SET-SWAP, §5.3 CS-1).

### Fidelity audit corrections (2026-10-06, full-resolution check of v01-v05)
Override older figures below. Evidence: `docs/audit/proof-dashboard/audit.md`.
- **Banner face is Montserrat Black**, not Unbounded; block cy ≈ 1010, 820 px wide; either line can glow (platform gradient word often on top).
- **Captions are bigger:** ≈ 96-110 px, 1-2 words per chunk; box treatments (cyan feature box, yellow hype box) exist next to the glow.
- **DM / comment pill** is sentence case, medium weight, avatar + violet send button (not bold caps + heart).
- **The set is a photographic, blurred night city** (bokeh window lights), never a dotted pixel skyline: use the creator's own blurred backdrop plate (`texture`) when supplied; otherwise paint soft bokeh discs (Ø 20-60 px, warm #FFB65C / #FFE2B0 at 20-45 %) on the gradient, not a dot grid.

### Motion corrections (2026-10-07 completeness pass, every frame of 25 bursts across v01-v05)
Measured at full frame rate; these override the older motion figures below. Evidence: `docs/audit/proof-dashboard/completeness.md`.
- **Caption swaps are hard cuts** (0 f, no pop); chunks of 2-4 words on 2 lines held 0.4-1.6 s, with 1-word punches ("SO"). CS-SOFT fades (6 f in, 8-10 f out).
- **Set relights are hard cuts** (0 f) on a phrase boundary, on the same frame as the caption swap, often with a reframe punch or hidden behind a sweeping graphic. No cross-fade.
- **Verdict floods are 1-2 f** (loser red, winner gold) plus a glow bloom, not 6 f.
- **The presenter camera is a cut reframe, not a 3 f zoom:** jump-reframes of 1.15-1.35 on a phrase boundary, smooth pushes of about +14 % over 13 f, and pull-outs of about −19 % over 16 f. The lounge/sofa reels (v03, v04) move about 3-4 times per 10 s; the desk reels (v01, v02) barely move.
- **Glitch is a transition family**, not only the banner exit: 2-5 f glitch cuts (RGB slices, pixel blocks, scanline blur) bring the reel back from UI to the presenter 1-3 times per minute (§9.1 T-12).
- **Three transitions were missing:** the white resolve into light UIs (T-2), the iris that closes on the highlighted phrase and carries it out as the step pill (T-13), and the graphic sweep that hides a relight (T-14).

### Directives `[DNA]`
| # | Directive | Where it lives |
|---|---|---|
| D1 | **The banner is built on frame 0.** Two lines at the chest, line 1 white, line 2 glowing, ≤ 5 words, gone by 3.6 s | §5.2, §6.2 |
| D2 | **Every claim gets proof within 1.5 s:** a real screen, a counter, a card pair, an article, a result. A claim with no proof is cut or proven | §2 H5, §8.4 |
| D3 | **Colour is meaning, never decoration.** Red wrong, green right, gold winner, cyan = the tool / the tap. One verdict colour per beat | §4.2 |
| D4 | **Show the exact screen.** Real recordings first; the orb taps on the spoken verb (±2 f); the tapped row is the only bright thing | §8.3 P-SCREENREC-ORB, §17.2 |
| D5 | **The presenter lives on a virtual set** that swaps or relights with the section; the real room never shows | §3.1, §12.4 |
| D6 | **Captions are 1–4 caps words with one glowing keyword**; swearing is masked (SH*T) everywhere: captions, banner, labels | §5.3 |
| D7 | **Illustration is never presented as proof.** every number traces to the script or the creator's own screen | §2 H10, §12.5, §18 |
| D8 | **One CTA: a keyword typed into a DM or comment pill**, held ≥ 1.5 s, at the end | §6.7 |

Buyer directives (`BD1…`) `[VAR]` may only make this stricter or more specific. Buyer never-list items are `BN1…` (§2.4).

### Quick index
| § | What | Status |
|---|---|---|
| §0 | Style profile | ON |
| §1 | Procedure (P1–P13, craft step P8a "claim → proof pairing") | ON |
| §2 | Hard rules, exceptions (E6), NEVER list | ON |
| §3 | Worlds (sets W-set-*, UI, stage, verdict), layouts L-set / L-set-dim / L-ui / L-bubble / L-in-app, stage moves | ON |
| §4 | Colour: the neon meaning axis | ON (single theme) |
| §5 | Type: glow banner, CS-1 captions + CS-BAD/GOOD/DATA/WIN/SOFT, labels | ON |
| §6 | Hook: HA-02 Headline + proof (alternates HA-01, HA-07, HA-05, HA-18), CTA | ON |
| §7 | Structure (tutorial / teardown), cadence | ON |
| §8 | Visual system: 51 patterns in 7 families | ON |
| §9 | Transitions T-1…T-14 | ON (§9.3 OFF) |
| §10 | Motion, zoom Z-1…Z-5, layers, finishing | ON |
| §11 | Sound contract | ON (minimal) |
| §12 | Footage, shot list SH-1…SH-7, fallbacks, inserts | ON |
| §13 | Output contract | ON |
| §14 | Worked examples (3) | ON |
| §15 | QA checklist | ON |
| §16 Chrome OFF · §17 Running state & anchors **ON** · §18 Data **ON** · §19 Citations OFF · §20 Dialogue OFF · §21 Canvas camera OFF · §22 Ink OFF · §23 Continuity OFF · §24 Series OFF · §25 Brand OFF | | |
| Formats | F-A "Proof Dashboard" (single format) | |

---

## §0 Style profile `[REQ]`

```yaml
profile:                         # mirrored in tokens.json -> profile
  source_type: talking_head
  presenter: {presence: host, share: [35, 65], max_absence_s: 10}
  spine: talking_head
  captions: {mode: full, role: support, mute_policy: mute_safe}
  graphics: primary
  duration: {class: standard, target_s: [45, 90]}
  language: {speech: en, captions: {lang: en, script: Latn, transform: verbatim}, on_screen: en, post_title: en,
             supported: [[en, en, Latn], [hinglish, hinglish, Latn], [hi, hi, Deva]]}
  numbers: {grouping: international, currency: "$", compact: k_m_b, units: metric, decimals: 0, style: short, compact_decimals: 1}
  tone: {energy: hype, comedy: light, comedy_max: light}
  themes: {policy: single, packs: [], default: null}
  formats: {list: [F-A], default: F-A}
  footage_dependency: medium
  cta: {devices: [comment_keyword, dm], placement: end}
  modules: {chrome: false, running_state: true, anchors: true, data_figures: true, citations: false,
            dialogue: false, canvas_camera: false, ink: false, continuity: false, series: false, brand: false}
```

Why each switch has this value:
- **source_type: talking_head**, because every evidence reel is one continuous seated take with overlays (3–10 hard cuts per video, v01–v05 cuts.json).
- **presenter: host, 35–65%**: face on screen 30–65% (v01 30%, v04 65%); the template floor is 35% so the creator stays the anchor. **max_absence_s: 10**: UI walkthroughs ran 14–16 s with no face (v01 @0:39–0:53, v05 @0:05–0:21); the template caps a run at 10 s and puts the face in a bubble (L-bubble) for anything longer.
- **spine: talking_head**: the take is the timeline; UI and cards are inserted on its words.
- **captions: full / support / mute_safe**: captions on every talking section (all five), but the proof carries the story; the banner and the orb taps keep the reel readable on mute.
- **graphics: primary**: UI, cards and data fill 35–70% of runtime and carry the argument.
- **duration: standard 45–90 s**: evidence 36–103 s, median 76 s; the template keeps one mid-reel re-hook (§7.4).
- **language**: English speech and captions in the evidence (transcripts were unavailable, so `(unverified)`); Hinglish and Hindi are supported buyer choices (§5.5).
- **numbers: international, K/M compact, 1 decimal**: every counter is "1.2M", "540K", "12.5K" (v01, v02, v04). Indian buyers switch to `indian / ₹ / lakh_crore` (BV-06).
- **tone: hype / light**: big gestures, "YOU FINALLY DID IT!", fireworks, thought bubbles (v02, v04), but no roasting with meme sounds.
- **themes: single**: the colour system is one fixed meaning axis; variety comes from sets (§3.1), not theme packs.
- **formats: one**: all five reels share one grammar (hook banner → proof → UI → verdict → keyword CTA).
- **footage_dependency: medium**: screen recordings, results screens and own thumbnails are what make it real (§12.2).
- **cta: comment_keyword + dm, end**: DM input pills typing a keyword close v02, v03, v04.
- **modules**: running_state (counters, countdown, progress bar), anchors (the cursor orb and highlight targets), data_figures (every counter is a figure; a deliberate deviation from STYLE-COVERAGE, which listed only the first two, because V-DATA must recompute the counters that are this style's proof). Everything else is off; series and brand are buyer switches.

### 0.4 Format `[DNA]`
| Field | F-A "Proof Dashboard" |
|---|---|
| when | Every reel: a feature, setting, tactic, mistake or result, explained by the creator and proven on screen |
| profile overrides | none |
| layouts | L-set, L-set-dim, L-ui, L-bubble, L-in-app |
| hooks.default | HA-02 Headline + proof |
| structure | `tutorial` (the teardown variant §7.1 is the same type with the verdict order) |
| shared DNA | matted presenter on a swapped dark set, the chest glow banner on f0, neon red/green/gold meaning, UI proof with a cursor orb, 1–4-word caps captions with one glowing keyword |

### 0.5 Theme packs
OFF (`themes.policy = single`). The set (§3.1) changes per section; the role colours never do.

---

## §1 Procedure (follow in order) `[REQ] [DNA]`

1. **P1 Inventory.** `ffprobe` every input. Conform VFR to 30 fps CFR. Register every file with `veos asset add <file> --origin creator` and tag it: `take` (setup A/B), `rec` (screen recording, SH-1), `proof` (results screen, SH-2), `thumb` (own covers, SH-3), `article` (SH-4), `teardown` (SH-5), `object` (SH-7). Note each recording's app, screen and the taps visible in it.
2. **P2 Prepare the matte (required).** Generate the person matte for the whole take (the cut-out frames `c%05d.webp` come from `veos prep-frames` once a `behind` scene exists). QA the hair edge at 200% on 3 frames (start, a gesture, the end). A matte with holes or a halo > 3 px on the hair fails: use FB-0 (§12.3).
3. **P3 Transcribe** with word timestamps. Apply `language.captions.transform`, the glossary (app names, menu names, the creator's product names: exact case), and the **profanity mask** (`inner`: S**T, F**K). The same mask applies to the banner, labels and the transcript blocks you type.
4. **P4 Segment** into `HOOK` (0 to banner exit), `PROBLEM` (why it matters / the wrong way), `REHOOK` (§7.4), `STEP-n` (one per screen / setting / action) or, in a teardown, `CLIP`, `WRONG`, `RIGHT`, then `PROOF` (the result) and `CTA`. Mark jump-cut points on word boundaries (±1 f).
5. **P5 Classify** every sentence with a line type (§8.4) and mark its trigger word (the noun, number or verb the visual lands on).
6. **P6 Tone-tag** every sentence: `hype` · `explain` · `proof` · `wrong` · `right` · `win` · `story` · `cta`. The tone picks the caption profile, the set light and the camera move (§10.2, tokens `tone_treatment`).
7. **P7 Hook plan.** Pick the archetype (HA-02 default; §6.3 for when an alternate wins). Write **3 banner variants** (§6.5) and the hook pair (§6.4). Run the stopper tests (§6.1).
8. **P8a Claim → proof pairing (this style's craft step).** For every claim sentence, name its proof: which screen, card pair, counter, article or result shows it, and the exact word the proof lands on. Every claim gets one; a claim you can't prove is flagged at the checkpoint (H5). Rank the proof sources: the creator's own recording > the creator's own screenshot > a created generic UI (labelled) > a stated number on a card.
9. **P8b Visual plan.** A pattern per line (§8.4); the set plan (which W-set-* per section, ≤ 3 swaps per minute); the meaning axis per beat (`axis: bad | good | winner | none`).
10. **P8c Data and state plan.** Every number shown goes into `plan/figures.json` (§18) with its provenance; counters, the countdown and the progress bar get state ops (§17.1).
11. **P8d Anchor pass.** For every screen recording, read its frames (`veos sheet`) and write the orb keyframes and highlight boxes in `plan/anchors.json` (§17.2): one keyframe per tap target, in recording pixels converted to screen pixels.
12. **P9 Beat sheet** (§13): one beat per trigger, meeting §7.6 cadence. Each beat names layout, set, pattern, axis, caption profile, camera, transition and the moments that may carry a cue (§11).
13. **P10 Transition map and cue moments** (§9, §11). The SFX pack chooses the sounds; you only mark the moments.
14. **P11 Assets and inserts.** Ask the creator once for the third-party moments (§12.5), build every created substitute, resolve the missing shots with §12.3 fallbacks and list which were used.
15. **P12 Checkpoint** (§13.5), then **wait for approval.**
16. **P13 Build.** Write `plan/timeline.json` + `plan/scenes.js` act by act; `veos scenes-meta` → `veos measure --every 10` → `veos validate`; preview and QA (§15, max 3 passes); render.

---

## §2 Hard rules `[REQ] [DNA]`

### 2.1 Editing rules (every style)
The ten editing rules in `playbooks/_global/GLOBAL-RULES.md` apply. They are directions, not limits: smooth, seamless motion; nothing overlaps by accident; keep the face clear (behind the speaker is fair game, text included); readable at a glance; one idea at a time; show the thing, not the word; say what was said; hook titles hook; pace like the style, not like a timer; the style decides the look.
- **Facts the engine checks:** accidental overlaps, jumps, the face covered, unreadable text, numbers and quotes that don't match what was said, the promised count. Every count, timing and budget this playbook gives is direction for the edit, not a limit.
- **Picture first, in this style's own look:** every key beat shows the thing being said (an object, a screen or app, a diagram, numbers in motion), not just its word; text supports the picture and never replaces it. When the speaker points with words ("this, this and this", "from this to this", "ye dekho"), show what they mean. Illustrations may use made-up but realistic numbers and names ("212 views", "1.2M views"), with no label; a number or quote the speaker says is shown as said. This overrides any rule below that bans made-up numbers or asks for an example tag: those rules now cover claims (the creator's results, prices, benchmarks, testimonials), not illustrations.
- **Hook titles hook:** the on-screen title promises the viewer something (an outcome, a curiosity gap, who it's for) and is true to what the reel delivers; it need not repeat the spoken words. This playbook sets its shape (§5.2, §6.5: lines, sizes, word limits, case), never its voice (§6).
- **Retired (8 Oct 2026), whatever this playbook says below:** no REPRESENTATIONAL or example labels on made-up cards, no credit lines, no flash limit (flash as often as this style calls for; any "NC-11" cap below no longer applies), and text may sit behind the speaker without an exception.

### 2.2 Declared exceptions
| ID | Style limits | DNA reason | Evidence |
|---|---|---|---|
| E6 Hard swap | Counter digits, the countdown digits and the typed DM keyword change inside a fixed container (`data-slot`, rect constant ±4 px). The container's own entry/exit stays eased | View counters "3 → 001K → 1.2M" and "72:00:00 → 71:59:59" swap digits in place | v02 @0:08–0:11, v04 @0:10–0:11 |

No other exception is used. The banner sits **in front of** the chest, not behind the head (no E1); there are no chaos bursts (no E2); every caption and label is ≥ its default floor (no E3).

### 2.3 MUST rules
- **H1 Frame 0.** f0 shows the presenter on a set, the glow banner fully built and readable, and the proof element already entering (a scene of kind `proof`/`card`/`phone`/`counter`/`ui` with `t_in` 0). `check: V-F0`
- **H2 Cadence.** Body: 4–8 weighted state changes per 10 s; no gap > 2.0 s between weight-1 changes; nothing static > 2.5 s (the live presenter counts as motion). `check: V-CADENCE`
- **H3 Payoff by 2.5 s.** The proof's verdict (winner card flash, counter landing, toggle on, the result screen) lands by 2.5 s. `check: V-F0`
- **H4 Banner limits.** ≤ 5 words, exactly 2 lines, no emoji, reads in ≤ 1.25 s, lifetime 2.6–3.6 s, profanity masked. `check: V-TITLE`
- **H5 Proof for every claim.** Every claim sentence has its proof on screen by 1.5 s after the claim's trigger word; an unproven claim is listed at the checkpoint and either proven or cut. `check: review`
- **H6 On the word.** Visuals land 2 f before the trigger word and are fully on within ±5 f; orb taps land within ±2 f of the spoken action verb ("tap", "turn on", "hit", "go to"). `check: V-ONWORD`
- **H7 Face.** Nothing is drawn in front of the face box; graphics keep 40 px clear; the banner top stays ≥ 80 px below the chin. Side cards go in the half of the frame away from the face. `check: V-FACE`
- **H8 Presence.** Presenter share 35–65% (L-set, L-set-dim, L-bubble, L-in-app count); the longest absence is ≤ 10 s. `check: V-PRESENCE`
- **H9 Promise.** Counts in the banner match items shown; every "I'll show you" is shown; the CTA keyword is on screen in the pill ≥ 1.5 s. `check: V-PROMISE`
- **H10 Truth.** Every number on screen is in `plan/figures.json` with provenance `script`, `creator` (their own screen) or `spoken@t`. Created UIs; illustrative values carry EXAMPLE. No invented metrics ("VIRAL RATE 79%"), no invented revenue, testimonials, payment receipts or DMs from real people. `check: V-DATA` + `V-INSERTS`
- **H11 Captions.** CS profiles only (never hand-written cards), ≤ 150 ms lead, 1–4 words, ≤ 2 lines, exact brand and menu names, profanity masked. `check: V-CAPTION`
- **H12 Dead air.** ≤ 1 gap ≥ 150 ms per 15 s, except one deliberate ≤ 0.3 s beat before the re-hook or the verdict. Cuts on word boundaries ±1 f. `check: review`
- **H13 Hues.** ≤ 3 bright hues per frame (yellow/primary, cyan, red, green, gold, blue each count). A red-vs-gold card pair takes CS-BAD or CS-WIN captions, never a fourth hue. `check: V-HUES`
- **H14 Audio.** −14 LUFS integrated, true peak ≤ −1.5 dBTP, bed ≥ 18 dB under the voice, hard end ≤ 6 f after the last word (NC-8). `check: review`
- **H15 Determinism.** Every particle, flare and glitch slice comes from `ctx.rng(seed)`; no `Math.random`, timers or CSS animations in scenes (NC-9). `check: review`

### 2.4 NEVER list
- **N1** Fake proof: invented dashboards, counters, follower numbers, revenue, payouts (no "You've received $5,000" unless it is the creator's own real notification), testimonials or DMs presented as real (NC-6).
- **N2** A real person's name, face or handle in a created DM, comment or notification. Created chats use initials avatars and generic names ("Viewer 1").
- **N3** A platform logo you drew. Brand glyphs appear only as a file the creator supplies; otherwise the platform name is set in type (in its brand gradient, `gradients.platform`, on that word only).
- **N4** Stock clichés: a stock hand holding a phone, hooded hackers, money rain, rocket emojis. Use the created phone mock (P-IN-HAND) or the creator's own clip.
- **N5** Red, green or gold used for decoration. Neutral emphasis uses the primary glow; verdict colours appear only on verdict beats.
- **N6** Captions on top of the screen being tapped: during L-ui runs captions are hidden and the step pill carries the words.
- **N7** Raw, unlabelled full-bleed screenshots of somebody else's content. A screenshot the creator holds goes through `fx.shot` with its highlight; a missing one becomes a created card.
- **N8** The real room behind the presenter (the set always replaces it), a green-screen fringe, or a set brighter than the presenter's face.
- **N9** More than one glitch-shatter banner exit per reel, more than 3 glitch cuts (T-12) per minute, more than one P-CELEBRATE, more than one verdict-world pair (P-VERDICT-WORLD).
- **N10** Personal identifiers on screen: emails, phone numbers, account IDs, payment details, other people's handles and avatars in DMs or comments. Blur them for their whole time (NC-14).
- **N11** Text in the IG bands (top 110 px, bottom 380 px, the right 110 px between y 900 and 1540) (NC-5).
- **N12** RGB-split packs, film burns, lens-flare PNGs, light leaks. RGB slices appear only inside the seeded glitch devices (P-BANNER-GLITCH, T-12). The only flash is T-2 (≤ 1 per 20 s).
- **N14** Money rain, stock bills or confetti flying through the lens (v04 @ 0:10 uses one; that's the N4 cliché). Use T-14 with the reel's own graphic instead.
- **N13** An emoji in the banner. (Glyphs like → ✓ ⚠ are type, allowed in captions and labels.)

---

## §3 Worlds, layouts, stage moves, safe zones `[REQ] [DNA; coordinates TUNE ±5%]`

### 3.1 Worlds
| ID | Kind | Look | Carries | Enter / exit |
|---|---|---|---|---|
| **W-set-skyline** (default) | backdrop | Night city: vertical gradient `#070B16 → #101A33 → #1B2240`, a warm glow `#FFB65C` at 10% (r 520, x 760, y 520) drifting ±12 px, soft bokeh discs (28-40, Ø 20-60 px, `#FFB65C` / `#FFE2B0` at 20-45 %, blurred 6-14 px, upper 60 % of the frame; NOT a regular dot grid), or the creator's own blurred city plate as `texture`, noise 0.03, vignette 0.35 | Hook, claims, opinions, the CTA | P-SET-SWAP: hard switch (0 f) on a cut point or phrase boundary |
| **W-set-neon-red** | backdrop | Studio with red rim light: radial `#7A0F1A → #2A060A → #0B0204` centred (540, 560), red glow `#FF2D2D` 16% | The wrong way, warnings, "never do this" | P-SET-RELIGHT, hard (0 f) from any set |
| **W-set-neon-blue** | backdrop | Same studio, blue rim: radial `#123E8C → #081A3A → #02060E`, glow `#2F80FF` 16% | The fix, the feature, "here's what you do" | P-SET-RELIGHT, hard (0 f) |
| **W-set-warm** | backdrop | Warm room (kitchen / lounge feel): `#2B1E14 → #3A2A1C → #140E09`, warm glow `#FFB65C` 12% at (300, 600) | Personal story, lifestyle asides, CS-SOFT sections | P-SET-SWAP |
| **W-ui-dark** | stage | `#08090D` flat | Screen recordings and created dark UIs (L-ui), the thumbnail wall | T-3 / T-5 / T-10 |
| **W-ui-light** | canvas | `#F6F7F9` flat (light: text flips to ink) | Articles, light-mode app screens | T-3 |
| **W-stage** | stage | `#0B0B10` + cyan glow 8% at (540, 860) | Funnels, donuts, countdowns, hero counters, people grids | T-3 / T-4 |
| **W-verdict-red** / **W-verdict-green** | void | Radial red `#5C0610 → #060001` / green `#0B5C1C → #010602` around (540, 900) | The verdict pair (P-VERDICT-WORLD): what's wrong, then what's right | T-8 hard flip on the verdict word |

**How a set is drawn.** With the stage `full`, the world never shows, so a set is a **`behind: true` scene** (`z: 1`, full frame 1080×1920) painted from the world's tokens (`ctx.tokens.worlds["W-set-…"]`: gradient, glow, dots); the engine draws the presenter's cut-out over it. The scene sits inside the footage group, so camera punches scale the set with the presenter like a real room. Paint bokeh and window lights with `ctx.rngStable(seed)` positions (static) and a ≤ 0.3 px/frame drift. During L-set-dim, draw the set at 60% glow. Never paint text in a set.

### 3.2 Layout library
| ID | Engine | Presenter | Graphic area | Caption | Treatment | Share of runtime |
|---|---|---|---|---|---|---|
| **L-set** | `full` | Full frame, matted on the set; head top y 300–420, chin y 700–820 | Chest band y 900–1100 (banner, captions, verdict words); proof band y 1130–1500; side halves x 64–364 / 716–1016 at y 360–894 (side cards) | `fixed_y` cy 1000 | none | 35–65% |
| **L-set-dim** | `full` | Full frame, dimmed (blur 10 px, luma −0.4) | One chest card y 860–1300, x 120–960 (profile chip, UI card, transcript block) | `fixed_y` cy 1420 | `dim` | 0–20% |
| **L-ui** | `hidden` | none | Full bleed: the recording or created UI, 1080 wide, y 0–1920; step pill at y 150–230 | hidden (step pill carries the words) | none | 15–50% |
| **L-bubble** | `pip` circle | Ø 400 at (540, 560), 3 px paper ring, shadow 0.5 | Under the bubble: the dimmed clip being torn down (full frame, 45% luma) and the transcript block y 860–1200 | `fixed_y` cy 1380 when no block is up | none | 0–25% |
| **L-in-app** | `card` | x 90, y 640, w 900, h 1280, radius 40 (bleeds into the bottom band, footage only) | y 120–620: created platform chrome above the presenter (story bar, feed header, stat pill) | `inside_footage` cy 1360 | none | 0–15% |

**Layout schedule rule.** L-set is home. Leave it on a proof noun or an action verb; return on the payoff word. An L-ui run lasts 3–10 s; an L-set run lasts 1.5–8 s; L-bubble ≤ 25 s per teardown with the bubble always present.

### 3.3 Stage moves
| ID | Move | Recipe | Use |
|---|---|---|---|
| **G-1** | Cut to UI | `via: cut` from L-set to L-ui on a word boundary, paired with T-3 or T-5 on the recording scene (10 f) | Into every step |
| **G-2** | Return | `via: cut` back to L-set + Z-1 cut reframe on the payoff word (or T-12 in place of the plain cut) | After every step's proof |
| **G-3** | Dim under card | `via: dim` 8 f: presenter dims as the chest card rises 40 px + fades in 8 f | Profile chips, UI cards over the presenter |
| **G-4** | Bubble shrink / grow | `pip-shrink` 10 f (ease back): footage shrinks into the Ø 400 circle at (540, 560) while the clip under it fades up from 0 → 45% luma | Teardowns, long UI runs that need the face |
| **G-5** | Into the app | `shrink-to-card` 12 f to L-in-app; the platform chrome (story bar, stat pill) settles in above in 8 f | "You post it and…" lines, feed / story talk |
| **G-6** | Set swap / relight | P-SET-SWAP / P-SET-RELIGHT: a **hard switch (0 f)** on the phrase boundary, on the caption-swap frame (v01 @ 23.58 blue → red; v04 @ 6.2 red → blue with a reframe) | Section changes, the wrong → right turn |

### 3.4 Layout diagrams
```
L-set (home)                                L-ui (screen proof)
┌─────────────────────────┐ 0              ┌─────────────────────────┐ 0
│  IG top UI (keep clear) │ ← y 0–110      │  IG top UI              │ ← y 0–110
│     virtual set         │                │   ╭ Step pill ╮         │ ← y 150–230
│   (side card x 716–1016 │ ← y 360–894    │   recording / created UI│
│    away from the face)  │                │   full bleed, push 1.00 │
│      ( presenter )      │ ← head 300–420 │   → 1.06 per step       │
│      (   face    )      │   chin 700–820 │        ◉ orb Ø 84       │
│ ═══ GLOW BANNER / CAPS ═│ ← chest band   │   rows outside the      │
│ ═══  LINE 2 (GLOW)  ════│   y 900–1100   │   target dim to 35%     │
│  ┌────┐   ┌────┐        │ ← proof band   │                         │
│  │card│   │card│ 1.2M   │   y 1130–1500  │                         │
│  └────┘   └────┘        │                │                         │
│  (desk, hands)          │ ← y 1540+ UI   │  (UI band, no text)     │
└─────────────────────────┘ 1920           └─────────────────────────┘ 1920

L-bubble (teardown)                         L-set-dim (card over presenter)
┌─────────────────────────┐ 0              ┌─────────────────────────┐ 0
│   dimmed clip (45%)     │                │  set + presenter dimmed │
│        ╭──────╮         │ ← Ø 400 at     │       ( face )          │ ← face stays clear
│        │ face │         │   (540, 560)   │                         │
│        ╰──────╯         │                │  ╭────────────────────╮ │ ← chest card
│ IF YOU'RE A SNACKER AND │ ← transcript   │  │ ◯ Name | Niche     │ │   y 860–1300
│ YOU SHOP AT THE STORE   │   block        │  │  151  164K  162    │ │
│ ▌BLESS YOU WITH SOME ⚠ │   y 860–1200   │  ╰────────────────────╯ │
│                         │                │      CAPTION cy 1420    │
└─────────────────────────┘ 1920           └─────────────────────────┘ 1920
```

### 3.5 Safe zones and bands
- Meaning text: x 64–1016, y 110–1500 (NC-5 limits; TUNE inside them).
- **Chest band:** cy 1000 (TUNE 940–1080), 200 px tall: the banner in the hook, captions after it, verdict words and the re-hook card. One occupant at a time.
- **Proof band:** y 1130–1500: card pairs, carousels, stat pills, the DM pill (when not at the chest).
- **Side card slots:** 300×534 at x 64 or x 716, y 360: only in the half away from the face centre (face cx < 540 → right slot; > 540 → left slot); when the face is centred (cx 440–640), side cards are not used; put the proof in the proof band instead.
- **Step pill:** y 150–230, centred.

### 3.6 Presenter rules
- Share 35–65% (TUNE ±10 pts); longest absence 10 s. An L-ui run that must go past 10 s cuts back to L-set for ≥ 1.5 s or switches to L-bubble.
- Return by G-2 (cut + Z-1). Never fade the presenter back.
- Crops: L-set as shot (scale 1.0–1.18; 1.35 only with a 4K source). L-bubble: face fills 65% of the circle. L-in-app: head top at card top + 90.
- Behind the head: only the set (a non-text `behind` scene). No text behind the head (no E1).

---

## §4 Colour `[REQ] [meanings DNA; brandable hex VAR]`

### 4.1 Role palette
| Role | Hex | Its one job | Text on it | Contrast | Lock |
|---|---|---|---|---|---|
| `primary` **Signature glow** | `{{BV-02.primary|#F5F000}}` | The banner's glow line and the default caption keyword glow. **Type only**, never a card fill | `ink` | 16.2:1 | brandable (VAR) |
| `accent` **UI accent** | `{{BV-02.accent|#1F6FEB}}` | Step pills, toggles switched on, highlighter boxes, the DM send button | `paper` | 4.6:1 | brandable (VAR) |
| `data` **Orb cyan** | `#5CE1E6` | The cursor orb, tap ripples, link glyphs, the tech / feature keyword glow (CS-DATA) | `ink` | 12.5:1 | TUNE (cyan–sky hue) |
| `winner` **Gold** | `#FFC83D` | The winning card, number or option: gold border, gold counter, flare sweep. Proof elements only | `ink` | 12.7:1 | fixed (DNA) |
| `bad` **Wrong red** | `#FF2D2D` | The wrong way, the losing card, ⚠ icons, the red verdict | `ink` | 5.3:1 | fixed (DNA) |
| `good` **Right green** | `#39FF4A` | The fix, ✓ marks, the green verdict | `ink` | 14.6:1 | fixed (DNA) |
| `ink` | `#0B0B10` | Text on bright fills, deep shadows | — | — | TUNE |
| `paper` | `#FFFFFF` | Caption and banner white, light UI cards | — | — | DNA |
| `night` / `panel` | `#08090D` / `#16181F` | UI world; dark UI surfaces (phone cards, pills, notifications) | `paper` | 19.9 / 17.7:1 | TUNE |
| `muted` | `#8B9099` | Ghost cards before the verdict, inactive rows, the loser's counter at rest | — | — | TUNE |
| `canvas` | `#F6F7F9` | The light article world | `ink` | 18.3:1 | TUNE |

Gradients: `platform` `#F58529 → #DD2A7B → #8134AF` (only on the word naming a platform that uses it; VAR), `winner` `#FFF1B8 → #FFC83D → #C98A00` (gold borders and flares), `good` and `bad` ramps for glows.

### 4.2 Meanings
- **The axis is red → green, and gold crowns the winner.** Wrong = red, right = green, the best result = gold. A verdict colour lands on its verdict word (±2 f) as a 1-2 f hard flood with a glow bloom that settles over 6 f, never before (v02 @ 1.50 red, @ 2.21 gold).
- **Primary (yellow) = "read this"**: the neutral keyword, the banner's glow when the banner has no verdict.
- **Cyan = the tool and the tap**: the orb, ripples, links, feature names.
- **Blue accent = the interface**: pills, toggles, highlighters, send buttons.
- **Brand colours only on brand names** (the platform gradient on "INSTAGRAM"); never on cards or captions otherwise.
- **The banner's line-2 colour is chosen by meaning:** a warning ("NEVER POST") → `bad`; a result or win ("DID IT!") → `good`; a secret / feature ("CHEATCODE", "UPDATE") → `primary` or the platform gradient on the platform word; a pair ("BAD → GOOD") → each word in its own role.

### 4.3 Theme packs
OFF (single). Sets (§3.1) are worlds, not themes: they never change a role.

### 4.4 Grades
None. Footage is not regraded; only exposure and white balance are matched to the set (warm sets get a +200 K white balance nudge at most). The "relight" is the set's glow (P-SET-RELIGHT), never a grade on the face.

### 4.5 Rules
- ≤ 3 bright hues per frame (`max_bright_per_frame: 3`, NC-10 allows 4).
- Red and green text sit on dark ground only. Measured against the set centres: `bad` text is 4.7:1 on W-set-skyline, 5.0:1 on W-set-neon-red, 4.6:1 on W-set-neon-blue but **3.7:1 on W-set-warm**, so a `wrong` beat always relights to W-set-neon-red first (never red text on the warm set). On `W-ui-light`, verdict words go inside a filled chip (`bad`/`good` fill, `ink` text).
- Glow is the style's finish: type glows (`text-shadow 0 0 18px <role>, 0 0 42px <role>@50%`), cards glow by border (`box-shadow 0 0 28px <role>@60%`). Nothing else glows.

---

## §5 Type & caption system `[REQ]`

### 5.1 Font map `[slots DNA; families TUNE within the class]`
| Slot | Family | Weights | Class (the TUNE boundary) | Used for |
|---|---|---|---|---|
| `banner` | **Montserrat** | 900 | geometric heavy caps, tracking −0.01 | Glow banner (the hook headline) |
| `display` | **Montserrat** | 900 | geometric / extended heavy caps 800–900 | Verdict words, re-hook card, outline stats |
| `body` | **Montserrat** | 800 | geometric heavy sans 700–900 | Captions CS-1…CS-WIN, transcript blocks |
| `ui` | **Plus Jakarta Sans** | 500–800 | neutral UI grotesk | Recreated UIs, step pills, notifications, DM pill, CS-SOFT |
| `numeric` | **Inter Tight** | 500–800, tabular | tabular grotesk | View counters, hero counters, countdown, donut % |
| `script` | **Pinyon Script** | 400 | formal script | The one celebration word (P-CELEBRATE) |
| `mono` | **JetBrains Mono** | 500 | monospace | Viewfinder REC / timecode (decorative) |

The evidence banner face is Montserrat Black (v01 "NEVER POST INSTAGRAM", v05 "INSTAGRAM", v04 "YOU FINALLY DID IT!"; checked against renders at full resolution); only single words like "CHEATCODE" use a techno face, which has no bundled match (keep Montserrat). Brand wordmarks and app glyphs are image files from the creator, never fonts.

### 5.2 Headline element: the glow banner (`kind: banner`, z 8) `[DNA recipe; NICHE text]`
| Property | Spec |
|---|---|
| Block | Centred at **x 540, cy 1010** (TUNE 940–1080; measured 1011 v05, 1025 v01, 1053 v04), width **820 px** (TUNE 720–860). No slab, no stroke, no box: type and glow only |
| Line order | Either line may carry the glow: white over colour (v01, v02, v04) or the platform word in the platform's gradient on top with a white line under it (v03, v05). The white line may be a smaller second tier (0.55×, v03 "BIG D*CK UPDATE") |
| Line 1 | `paper` (or the glowing line, see order), Montserrat 900, caps, tracking −1%, **auto-sized so the line spans 780 px**, clamped 64–120 px |
| Line 2 | Same face, auto-sized to 780 px (clamped 64–120 px), colour by meaning (§4.2), glow `0 0 18px` + `0 0 42px @50%` in that colour |
| Both lines | `line-height 0.98`, drop shadow `0 6 18 rgba(0,0,0,.55)`. Fit-width means a short line gets bigger type: "YOU FINALLY" ≈ 92 px over "DID IT!" ≈ 120 px |
| Words | ≤ 5 words total, exactly 2 lines, no emoji; `→ ✓` allowed as glyphs; profanity masked (S**T) |
| Brand glyph | Optional, only the creator's logo file: an 88 px square after the longer line, 16 px gap, same glow |
| f0 | Fully built and readable on frame 0. It **floats** ±6 px on a 2 s sine (it rides with the presenter) |
| Life | One event in the hook: **P-BANNER-IGNITE** (the word floods to its colour in 1 f, glow bump 0 → 42 → 30 px over 8 f) on its spoken word, or **P-BANNER-TILT** (−4° over 3 f, back over 4 f; v03 @ 1.23-1.43) on a punch word. v03 does both on the same word; that's the one allowed stack |
| Exit | Between 2.1 and 3.6 s: **P-BANNER-GLITCH** (17 f, for warning / news hooks, ≤ 1 per reel; v01 @ 2.12-2.83) or **P-BANNER-BLUR-UP** (6 f, default) |
| Lifetime | `hook` only. After the hook the chest band belongs to captions |
| Captions | Hidden while the banner is up (CS hide `under_z8`) |
| Text class | TC-display (≥ 64 px; contrast ≥ 3:1 at ≥ 96 px and 4.5:1 below, against the set) |

`kind: "banner"` scene fields: `z: 8` (not 10: the core's top-banner camera clamp must not push the face), `text_content` = both lines, `lines: 2`, `chips: [{text: <line 2>, role: <its role>}]` (documentation; the chip count isn't enforced in this style).

### 5.3 Caption profiles (CS) `[DNA mechanics; fonts TUNE; language VAR]`
All profiles extend `lib:devin` and differ only in the emphasis colour (or the skin, for CS-SOFT).

| Group | CS-1 (default) |
|---|---|
| Mode | `full`, `support`, `mute_safe` |
| Chunking | `group`, 1–4 words: mostly a 2-line chunk of 2–4 words ("HOW SHOULD / YOU USE IT?", "THIS FEATURE / SO GOOD?"), with 1-word punches ("SO", "EVERYTIME"); ≤ 12 characters per line, ≤ 2 lines; never split a name, number or unit; punctuation breaks; a pause ≥ 0.9 s always breaks; end punctuation stripped |
| Timing | lead 1 f; ≥ 0.25 s per word; chunks hold 0.4–1.6 s; tail 0.12 s; **swap `hard` (0 f): the next chunk replaces the last on one frame, no pop, no scale** (v01 @ 22.00, 23.58); no pause hold |
| Skin | Montserrat 800, **96 px** (TUNE 84–112; measured ≈ 110 px for one-word chunks, v05 @ 0:30 / 0:35), CAPS (lower-case chunks also occur, v05 "everytime"), tracking +1%, line-height 1.0, `paper`, shadow `0 4 14 rgba(0,0,0,.65)`, no container |
| Position | `fixed_y` **cy 1000** (the chest band) on L-set; cy 1420 on L-set-dim; cy 1380 on L-bubble (when no transcript block); `inside_footage` cy 1360 on L-in-app; **hidden on L-ui**. `avoid_face: true` (a chunk that would touch the face moves under the chin) |
| Emphasis | `glow` in `primary`, glow 18 px, size ×1.08, span `phrase` (the glow runs across the keyword's adjacent content words, so line 2 often glows whole: "SERIES POSTS"; the glowing line has a vertical gradient fill, a pale tint of the role on top to the full role colour at the bottom, v01 @ 21.0 "SO GOOD?"). About every other chunk has no keyword at all (plain white), select number > name > glossary > topic noun, never stop-words, ≤ 1 per chunk, ≤ 1 per 2 s |
| Keyword boxes | Two box treatments replace the glow on chosen chunks: **CS-BOX** (a feature / product name: white Plus Jakarta 600 64 px in a cyan-blue box #2AAEEB, radius 10, soft glow; v01 @ 0:08 "Linking Reels") and **CS-HYPE** (one payoff word per reel: Montserrat 900 88 px `ink` caps in a flat yellow box #DCD22C; v01 @ 0:10 "LEGENDARY"). A masked swear word may sit above CS-HYPE in the marker face (Permanent Marker) |
| Hide | under z8 scenes (banner, verdict words, re-hook card), during transitions and stage morphs |
| Language | Latin script; English terms kept verbatim; **profanity mask `inner`** (S**T, F**K, D**N) (VAR: `vowel`, `full` or off); glossary = app, menu and product names |

| Profile | Differs from CS-1 | Used on tone |
|---|---|---|
| **CS-BAD** | emphasis `bad`, glow 20, key verbs selectable | `wrong` |
| **CS-GOOD** | emphasis `good`, glow 20, key verbs selectable | `right` |
| **CS-DATA** | emphasis `data` (cyan) | `proof` (feature / tool lines) |
| **CS-WIN** | emphasis `winner`, glow 22, ×1.10 | `win` (the result number) |
| **CS-SOFT** | Plus Jakarta Sans 700, 66 px, as spoken (sentence case), one line, 1–3 words, the whole chunk in `primary` with a soft glow, no keyword; **swap `fade`**: 6 f in, 8–10 f out (v03 @ 34.7, 37.2) | `story` (personal asides on W-set-warm) |

Switching profiles: write `captions.overrides: [{t: [a, b], profile: "CS-BAD"}]` per tone run (never per word). Keep a profile ≥ 2 chunks.

### 5.4 Other text systems
| System | Class | Recipe | Hold |
|---|---|---|---|
| **Step pill** (SM-1) | TC-label | `accent` fill, radius 18, padding 12/28, Plus Jakarta Sans 700 46 px `paper`, glow 24 px accent@60%, centred at y 190; pop 7 f (scale 0.7 → 1.06 → 1). After an article, the highlighted phrase itself **becomes the pill**: T-13 carries it out onto the presenter at the chest, and it drifts about 1 px/f (v01 @ 8.13-8.50) | ≥ 1.0 s; swaps on each new screen with a 4 f cross-fade |
| **Card counter** | TC-label | Eye glyph + compact number, Inter Tight 700 48 px, in a `panel` chip (radius 14) at 64% of the card height; loser `muted` → `bad`, winner `paper` → `winner` | Rolls 18 f, lands on the spoken number |
| **Hero counter** | TC-display | Inter Tight 700, 120–200 px, `paper` with a 22 px glow in its role; unit word under it, Plus Jakarta Sans 600 48 px | ≥ 1.2 s after landing |
| **Transcript block** | TC-label | Montserrat 800 44 px caps, left-aligned at x 120, 3–6 lines, 1.15 line height; each line becomes a red or green box (`bad`/`good` 3 px border + 18 px glow + 15% fill) on its verdict | The whole teardown section |
| **Verdict word** | TC-display | Montserrat 900 72–110 px caps, role colour + glow 16–36 px, centred in the chest band | ≥ 0.8 s |
| **Celebration word** | TC-display | Pinyon Script 120–150 px, `winner` + 20 px glow | 1.5–2.0 s, ≤ 1 per reel |
| **Countdown** | TC-display | Inter Tight 500 150 px, tracking +6%, `paper`; unit labels HOURS / MINUTES / SECONDS Plus Jakarta Sans 600 40 px `muted` | ≥ 1.5 s |
| **Notification card** | TC-label | `panel` card 900×150, radius 32, glyph square 72 px, title 40 px 700, body 40 px 500 | ≥ 1.5 s |
| **DM / comment pill** | TC-display | `panel` pill 820×120, radius 60, avatar 76 px, keyword Plus Jakarta Sans 700 58 px, send button `accent` Ø 76 | Keyword fully typed ≥ 1.5 s |
| **Legal label** | TC-legal | EXAMPLE, Plus Jakarta Sans 700 24 px caps, tracking 12%, `paper`@80% (dark) or `ink`@70% (light), inside the created element's bottom-left corner, 24 px in | As long as the element |
| **UI chrome** | TC-decorative | Menu text, status bars and body copy inside a recording or created UI | — (never carries the point; the pill or caption does) |
| **Viewfinder** | TC-decorative | JetBrains Mono 500 26 px: ● REC, HD 4K, 00:00:00:00 | Section texture |

### 5.5 Language and number rules
- App, menu and button names exact, in the app's own case ("Professional dashboard", "Trial"), in pills and captions. Add them to the glossary at P3.
- Numbers: international grouping, K / M compact with 1 decimal ("1.2M", "540K", "12.5K"); currency `$` by default. Indian buyers: `indian`, `₹`, `lakh_crore` ("₹12.5 L") through BV-06; counters and labels follow `ctx.fmtNum`.
- Hinglish captions (`hinglish/Latn`): CAPS stays; keep English UI terms in English. Hindi (`Deva`): captions in Noto Sans Devanagari 800 (no caps), emphasis glow unchanged; the banner stays English unless the buyer says otherwise (`on_screen`).
- The profanity mask runs on every text system, not only captions.

---

## §6 Hook system `[REQ]`

**Hook title (every style, 8 Oct 2026; above anything below):** the on-screen title promises the viewer something: an outcome they want, a curiosity gap, or who it's for ("How to go viral as a doctor creating content", not the label "Reels for Doctors"). It doesn't have to repeat the spoken words; it has to be true to what the reel delivers. A title shown as someone's words (in quotes) is still word for word. This section sets the title's shape (lines, sizes, word limits, case, the keyword device), never its voice. Write 8–10 candidates from the formulas below plus the proven patterns ("How to X as a Y", "Why your X isn't working", "The X nobody tells you", "Stop doing X", "Your X vs mine", a number or a contrast), score them on outcome, curiosity, who it's for and brevity, check the best against the stopper tests, and pick; any "write 3" below means this, and the next two go to the storyboard as alternates. A style with no on-screen title applies this to its post title.

### 6.1 Stopper tests
| Test | This style's number |
|---|---|
| ST-1 Thumbnail | At 25% scale the banner lines are ≥ 16 px tall and the proof (two cards or a toggle) is visible |
| ST-2 Mute | The first 3 s read without sound: the banner says the topic, the proof shows the verdict (red loser, gold winner, toggle on) |
| ST-3 Motion at f0 | The proof element is entering on f0; the banner floats |
| ST-4 Read time | ≤ 5 words → ≤ 1.25 s |
| ST-5 Change count | ≥ 4 weighted state changes in 0–3 s |
| ST-6 Payoff-by | The verdict (winner flash / counter landing / toggle on) by 2.5 s |

### 6.2 Default archetype: HA-02 Headline + proof `[DNA]`
| t | Visual | Caption | Layout / camera | Cue moment |
|---|---|---|---|---|
| **f0 (0.00)** | Presenter on W-set-skyline (or the set of the topic). **Glow banner fully built** at the chest. **Proof element entering** under it in the proof band: a phone-card pair, ghosted (`muted` tint, 55% opacity), rising 40 px | — (hidden under the banner) | L-set; no camera move | hook (f0 hit) |
| 0.00–0.27 | Cards land (8 f rise + fade, second card 3 f later) | — | — | — |
| 0.3–1.4 | The presenter says the claim; the banner floats ±6 px. Optional P-SETTING-REVEAL (a settings row unblurring over 24 f) or P-CARD-CAROUSEL settling | — | — | — |
| **≈ 1.5** (the "bad" word) | **Loser lands:** the left card floods red (2 f, v02 @ 1.46-1.54), its counter rolls to its small number (or stays at "0"). Or P-BANNER-IGNITE when the banner carries the verdict | — | Z-1 cut reframe only if the banner doesn't tilt | reveal |
| **1.9–2.5** (the "good" word / the number) | **Winner lands:** a hard gold flood on one frame with a wide gold bloom (halo ≈ 1.5× the card) that settles over 6 f (v02 @ 2.21), gold border 4 px + 28 px glow, its counter **rolls 18 f to the real number**, a flare sweeps across it (12 f). Payoff ≤ 2.5 s | — | — | reveal (counter landing) |
| 2.5–3.0 | Hold the verdict; one banner event (P-BANNER-TILT on the punch word) if none happened yet | — | — | — |
| **2.6–3.6** | Banner exits (P-BANNER-BLUR-UP, or P-BANNER-GLITCH for warnings / news). Cards either slide down 60 px + fade (6 f) or **evolve** into beat 1 (T-11 the winner card grows into L-ui) | First caption chunk cuts on (hard) on the next word | T-3 / T-11 into beat 1 | transition |

Weighted SCs in 0–3 s: cards enter (1) + loser flood (1) + winner flash (1) + counter landing (1) + banner event (1) = 5 (≥ 4). Hook length 2.6–3.6 s; intro ≤ 12% of runtime.

### 6.3 Allowed alternates `[DNA list; VAR choice per reel]`
| ID | Use it when | f0 | Payoff | Table |
|---|---|---|---|---|
| **HA-01 Result pair** | The reel compares a bad and a good version of the same thing (a weak vs a strong opener, a bad vs a good budget) | Banner line 2 = "BAD → GOOD" with each word in its role (SH*T → GOLD) + the ghosted card pair + presenter | Gold winner ≤ 2.5 s (the bad state ≤ 1.7 s) | Same as §6.2; the loser's word is red in the banner from f0, the winner's word ignites gold on its spoken word |
| **HA-07 Live number** | A result or milestone is the story ("you finally went viral") | Banner + **P-CARD-CAROUSEL** sliding in at f0 (counters visible from 0.3 s) | The winning counter centred and gold by 1.0 s | 0.0 carousel slides in from the right, motion blur 10 f · 0.5 settles, counters readable · 1.0 the winner centres, scales 1.0 → 1.15 over 8 f, gold border · 1.3–2.8 flare sweeps, others dim 45% · 3.0 P-CELEBRATE or exit |
| **HA-05 Claim lockup** | A hidden setting / feature / "cheat code": the proof is a switch, not a number | Presenter + banner + **one settings row** (blurred, toggle off) in the proof band | Toggle flips on (P-TOGGLE-FLIP) ≤ 2.0 s | 0.0 row blurred 14 px · 0.0–0.8 unblurs (P-SETTING-REVEAL) · 1.0 banner float · 2.0 toggle flips on: knob 6 f, `accent` fill, 4 sparks · 3.0 T-2 bloom flash out of the toggle into beat 1 |
| **HA-18 Borrowed clip** | A teardown of a clip (the creator's own, or one they hold and supply) | The clip in a 9:16 side/centre card with its view counter + banner; presenter ≤ 8 s (L-bubble from ≈ 3 s) | The clip's counter lands ≤ 3.0 s | 0.0 clip card plays, counter at "0" · 1.5 counter rolls to its views · 2.5 banner exits · 3.0 G-4 bubble shrink: the presenter's face in the Ø 400 bubble over the dimmed clip. Created fallback: P-TEARDOWN-BUBBLE with the clip's words as a transcript block (`quote_card`) |

### 6.4 Hook pairs by topic `[NICHE: example]`
Pair type for HA-02 / HA-05 is **promise → proof**; for HA-01 it's **bad → good result**; for HA-07 **subject → reveal**. Niche A = social-media growth; Niche B = personal-finance apps.

| Niche | Topic | Banner (line 1 / line 2) | Proof visual | Payoff word |
|---|---|---|---|---|
| A | A hidden posting setting | INSTAGRAM / CHEATCODE | Settings row → toggle on (P-SETTING-REVEAL + P-TOGGLE-FLIP) | "on" |
| A | Weak opener vs strong opener | YOUR HOOK / SH*T → GOLD | Two cards of the creator's own posts: "3" views red vs "1.2M" gold | "million" |
| A | A new platform feature | INSTAGRAM / BIG UPDATE | The creator's article screenshot, highlighter on the feature name (else a headline card) | the feature name |
| A | A post went viral | YOU FINALLY / DID IT! | Carousel of the creator's posts, the viral one gold | the number |
| B | A bank auto-save rule | YOUR BANK / HIDES THIS | The app's settings row → "Round-ups" toggle on | "round-ups" |
| B | Two ways to save | SAVINGS / BAD → GOOD | Two cards: a flat balance (red) vs the balance with the rule (gold), both from the creator's own screenshots | the amount |
| B | A fee you're paying | STOP PAYING / THIS FEE | The statement line highlighted red, then the setting that removes it (green) | the fee amount |

At P7 of every reel, write this reel's row and append it to the copy's table.

### 6.5 Banner writing `[DNA formula; NICHE examples]`
**Formula:** line 1 (white) = the subject the viewer already knows (the platform, the thing, "YOU"); line 2 (glow) = the twist: the verdict, the secret, the result. 2–5 words in total, every word in caps.

| Template | Example (niche-neutral slots) |
|---|---|
| Warning | NEVER POST / [THING] |
| Secret | [PLATFORM] / CHEATCODE · [APP] / HIDDEN SETTING |
| Pair | [THING] / BAD → GOOD |
| Result | YOU FINALLY / DID IT! |
| News | [PLATFORM] / BIG UPDATE |
| Stop | STOP [HABIT] / [CONSEQUENCE] |

- Write 3; pick by ST-1 and ST-4. The line-2 colour follows §4.2.
- Banned: emoji, more than 5 words, "game changer", a count you don't deliver, a claim the reel doesn't prove, unmasked swearing.

### 6.6 Hook sound
The hook may carry cues (§11): an f0 hit, the loser flood, the winner flash / counter landing, and the banner exit. The bed enters after the banner exits.

### 6.7 CTA `[DNA device set; VAR values]`
| Device | Spoken pattern | On screen | Hold / placement |
|---|---|---|---|
| `dm` (default) | "DM me **{{BV-08.keyword|KEYWORD}}** and I'll send you {{BV-08.deliverable|the full guide}}" | **P-DM-KEYWORD**: the input pill at the chest band (cy 1000), already on screen on the frame the reel glitch-cuts (T-12) back to the presenter: avatar 76 px, the keyword types at **one character per 4 f (≈ 8 characters/s)** from the spoken keyword (v04 @ 44.80-45.13), the `accent` send button pulses (1.0 → 1.12 → 1.0, 6 f) and the pill sends: it rises 60 px and fades (8 f) | The typed keyword holds ≥ 1.5 s; last 2–4 s of the reel |
| `comment_keyword` | "Comment **{{BV-08.keyword|KEYWORD}}** below" | **P-COMMENT-PILL**: the same pill with a comment glyph and a heart instead of the send button; the heart fills `bad` on send | Same |

The CTA beat is on L-set with a Z-3 pull-out; captions hide while the pill shows the keyword. No silence is needed before it; the voice stays dry over the pill. The keyword is `meta.keyword` (V-PROMISE).

---

## §7 Structure & cadence `[REQ] [DNA]`

### 7.1 Structure type: `tutorial`
| Variant | Arc | Evidence |
|---|---|---|
| **Walkthrough** (default) | HOOK (claim + proof) → PROBLEM (why the usual way fails, red) → REHOOK ("HERE'S WHAT YOU DO") → STEP-1…n (screen + orb, each ending in proof) → PROOF (the result counter / before-after) → CTA | v01, v05 |
| **Teardown** | HOOK (pair) → CLIP (what it is, its numbers) → WHY IT WORKS → WRONG (red) → RIGHT (green rewrite) → WHO IT'S FOR (people grid) → CTA | v02 |
| **Funnel / framework** | HOOK → the model (P-FUNNEL, one layer lit per section) → each layer's tactic with proof → CTA | v03 |
| **Result → cash in** | HOOK (the win) → the warning (red) → the countdown (P-COUNTDOWN) → the steps → proof → CTA | v04 |

### 7.2 Markers
**SM-1 Step pill**: at every step the pill names the screen or setting ("Settings → Trial"), on the screen's name ±2 f. No numerals: Devin never numbers steps; the colour axis marks the teardown's turns instead (red section → green section). `numbering: none`.

### 7.3 Unit ritual (every STEP, in frames)
1. **Claim on L-set** (CS-1 or CS-DATA): the keyword glows; a Z-1 cut reframe or a Z-2 push on it (not both).
2. **Step pill** pops at y 190, 2 f before the screen's name (7 f pop).
3. **Into L-ui** on the action verb: G-1 cut + T-3 whip-in (4 f), T-2 into a light page, or T-5 (6 f) between two recordings.
4. **Orb:** travels to the target (10–16 f, ease in-out) → the rest of the screen dims to 35% (6 f, P-FOCUS-DIM) → **press + ripple on the spoken verb ±2 f** (6 f press, 10 f ripple) → the result state (toggle on, sheet up, number visible).
5. **Proof holds ≥ 1.0 s** (a counter rolls, a toggle is on, a sheet is open).
6. **Return** to L-set on the payoff word by **T-12 glitch cut** (default, v01 @ 37.42, v04 @ 44.73), **T-13 iris carry** after an article, G-2 (a plain cut + Z-1), or **T-11**, which shrinks the screen into a side card that stays beside the presenter for 1.5–3 s.

### 7.4 Open loops and re-hooks
- Loops used: the **promise loop** ("here's how" → the steps), the **countdown loop** ("you have 72 hours" → the clock), the **verdict loop** (red first, green paid later).
- **Re-hook (standard class: one mandatory, 25–75% of runtime):** **P-HERE-CARD** "HERE'S WHAT YOU DO" (or "BUT HERE'S THE CATCH" / "HERE IS THE PART THAT…"). Measured, it's quieter than a card: a T-12 glitch cut back from the UI, a 1-word chunk "SO" held ≈ 0.3 s, then the line as a plain 2-line CS-1 chunk (v01 @ 37.42-37.88), or with a relight and a reframe on the same frame (v04 @ 6.2) when a new section starts. Reels over 80 s add a second re-hook (P-COUNTDOWN, a new proof pair, or P-HERE-CARD) so no gap exceeds 40 s (`rehook_every_s: 40`). Mark the beat `rehook: true` (kind `rehook` on the card).
- **Intro cap:** the hook ends by 3.6 s and ≤ 12% of runtime.
- Every promise is paid on screen; the CTA deliverable is named in the pill's spoken line.

### 7.5 Rhythm and energy curve
- Hype from frame 0, steady explaining in the steps, a peak at the proof (the biggest counter, the gold card, P-CELEBRATE once), a clean, confident CTA.
- **Light comedy** (`comedy: light`): at most one gag beat per 20 s: a thought bubble (P-THOUGHT-BUBBLE), the celebration word, an object cut-out. Gags carry information (the viewer's real thought, the real dish). No meme sounds, no stickers on faces.
- The last step escalates: a full proof screen (L-ui with the result), the hero counter, or the verdict world.

### 7.6 Cadence (state changes)
| Token | Value | Why |
|---|---|---|
| `sc_per_10s` | **4–8** | Overlays change 15–25 times a minute plus caption chunks (~0.5 s each, weight 0.5) |
| `hook_sc_3s` | **4** | Evidence hooks carry 3–5 events in 0–3 s |
| `max_gap_s` | 2.0 (hook 1.2) | |
| `max_static_s` | 2.5 | The live presenter counts as motion |
| `caption_weight` | 0.5 | support captions |
| `cuts_per_min` | not DNA | 2.4–7.9 cuts/min is a side effect of overlay editing |
| measured (2026-10-07) | — | Scene cuts 5–10/min, median shot 2.6–7.9 s (p90 10–20 s); visual events 5.5–7.9 per 10 s; caption chunks 0.4–1.6 s; the longest still stretch on the presenter is ≈ 3 s (v01 @ 67) |

---

## §8 Visual system `[REQ]`

### 8.1 Graphics role and budget
- `graphics: primary`: graphics and UI carry the argument; 35–70% of runtime shows a proof element.
- **51 patterns** in 7 families; ≥ 8 distinct patterns and ≥ 4 families per 60 s.
- **Numbers become proof**: a spoken number is a counter, a card pair, a donut or a people grid, landing on the number word. Never a bare number in a caption alone when it is the claim.
- **One proof idea per screen**: one pair, one screen, one chart. The previous proof exits before the next enters.

### 8.2 Families
| ID | Family | Source class | The creator supplies | Created substitute when missing |
|---|---|---|---|---|
| **B-1** | Glow type (banner, verdict words, re-hook card) | engine | — | — |
| **B-2** | Proof cards & counters | engine + creator (thumbnails, real numbers) | SH-2 results screens, SH-3 own covers | Dark gradient cards with the post title in type; numbers only from the script (FB-2, FB-3) |
| **B-3** | Screen proof (recordings, orb, UI chrome) | creator (recordings) / engine (orb, pills, created UIs) | SH-1 recordings, SH-4 articles | `fx.appUI` settings / list / chat / browser (FB-1); `fx.headlineCard` (FB-4) |
| **B-4** | Verdict (red / green marks, transcript blocks, grids, funnels, progress) | engine | SH-5 the clip being torn down | Transcript block of the clip's verbatim words + silhouette (FB-5) |
| **B-5** | Beat devices (re-hook card, countdown, celebration, outline stat, viewfinder) | engine | — | — |
| **B-6** | Set & camera (sets, relight, thumbnail wall, punches, object cut-outs) | engine + creator (matte, thumbnails, object photos) | SH-3, SH-7 | Set painted from tokens; icon card for objects (FB-7) |
| **B-7** | CTA pills | engine | — | — |

### 8.3 Pattern specs
All motion at 30 fps. "f" = frames. Box coordinates are on the 1080×1920 frame.

**B-1 Glow type**
| ID | Type | On screen | Motion recipe | When | Text class / needs |
|---|---|---|---|---|---|
| **P-GLOW-BANNER** | overlay | The two-line banner of §5.2 at cy 1000 | Built on f0; float `y = 1000 + 6·sin(2π·t/2)`; lifetime 2.6–3.6 s | Every hook | TC-display, z 8, kind `banner` |
| **P-BANNER-IGNITE** | overlay event | Line 2 floods from `muted` to its role colour, glow 0 → 42 → 30 px, scale 1.0 → 1.06 → 1.0 | 6 f colour flood + 8 f scale, on line 2's spoken word | The banner holds the verdict (warning, result) | event on the banner scene |
| **P-BANNER-TILT** | overlay event | The whole banner tilts | 0 → −4° over 4 f (ease out), back to 0 over 6 f (ease back) | A punch word in the hook ("BIG", "NEVER") | event |
| **P-BANNER-GLITCH** | exit | Both lines flip to `bad` (red fill + red glow) on one frame; thin dark fracture lines spread through the letters; then the block breaks into 7 seeded horizontal slices with RGB fringes and is gone | 17 f (v01 @ 2.12-2.83, 24 fps): f0 hard red flip · f1–13 fractures grow (the banner keeps floating) · f14–16 slices shift ±24 px with ±6 px R/B offsets · f17 gone | Exit of warning / news banners; ≤ 1 per reel | `cuts` declared at the exit |
| **P-BANNER-BLUR-UP** | exit | The banner rises 40 px, blurs 0 → 12 px and fades | 6 f ease-in | Default exit | — |
| **P-VERDICT-WORD** | overlay | One or two verdict words at the chest ("WRONG DESIRE", "PROBLEM SOLVED ✓") in `bad`/`good` with glow | Pop 7 f (0.7 → 1.06 → 1) + colour flood 6 f; out blur 5 f | The verdict sentence of a teardown or a step | TC-display, z 8 |

**B-2 Proof cards & counters**
| ID | Type | On screen | Motion recipe | When | Text class / needs |
|---|---|---|---|---|---|
| **P-PHONE-PAIR** | figure | Two 9:16 cards 208×370, radius 22, `panel` with a 2 px `muted`@40% border, centred with a 56 px gap (x 290–498 and 582–790), y 1130–1500; each shows a creator cover (SH-3) or a dark gradient + the post title; a counter chip at 64% height | Rise 40 px + fade 8 f (stagger 3 f), ghosted 55% + desaturated until the verdict; loser: `bad` flood 35% + border + 16 px glow in 2 f; winner: a 1 f `winner` flood (30%), 4 px border, a 28 px glow that blooms to ≈ 1.5× the card and settles over 6 f, counter rolls 18 f; flare sweep 12 f (a 60 px white bar at 20°, 40% opacity) | Comparing two versions, the hook proof | figures for both counters; one scene |
| **P-CARD-CAROUSEL** | figure | 4–6 cards 200×356, gap 24, in the proof band; one winner | Strip slides in from x +600 with 14 → 0 px horizontal blur over 10 f (`ctx.blur(px, 0)`, directional); settles 4 f; the winner centres and scales 1.0 → 1.15 over 8 f, gold border; others dim to 45% | A result among results ("one of these went viral") | figures; one scene |
| **P-COUNTER-ROLL** | state | Eye glyph + compact number in a fixed-width chip | Each digit column scrolls with an 8 px vertical blur, 18 f, lands on the spoken number ±5 f; optional Z-4 shake on landing | Any view / follower / money number | E6 (`data-slot` chip), figure, `lands` |
| **P-LINKED-CARDS** | figure | Two cards joined by a glowing chain-link glyph (`data`, 120 px) that pulses 1.0 → 1.12 → 1.0 every 1 s | Cards rise 8 f; link draws 8 f; the right card's counter rolls when "linked" is said. **Card push:** on W-ui-dark the scene pushes 1.0 → 1.45 over 18 f (ease in-out) and pans onto the card being named, then pulls back over 18 f (v01 @ 14.5, 16.6). Exit: the cards shrink to the centre (1 → 0.4, 4 f) while the link glyph sweeps in (T-14) | "Connect X to Y", "link this to that" | figures |
| **P-HERO-COUNTER** | figure | A big centred counter (120–200 px) + unit word, over the blurred thumbnail wall (P-THUMB-WALL) on W-ui-dark | Steps roll 18 f each on their number words (6K → 9K → 81K) | Growth over time | figure with steps, `lands` |
| **P-STAT-PILL** | figure | A `bad`-filled notification pill (radius 32) with 2–3 icon counts (comments / likes / follows) above a feed card or the L-in-app frame | Pop 7 f (spring), counts roll 12 f | "Your comments / likes blew up" (real numbers only) | figures |
| **P-DONUT-SHIFT** | figure | A ring Ø 260 (28 px stroke) + its percent (Inter Tight 700 64 px) + a label (48 px), beside a phone mock | Ring sweeps 18 f; on the shift word the ring recolours (`accent` → `data`) and re-sweeps to the new percent | "Who sees it" splits, any share that changes | figure (percent) |
| **P-VERSUS-TAG** | figure | Two labelled cards ("Normal" / "Trial") and a tilted tag on the winner ("FREE", "BETTER") | Tag stamps: scale 1.6 → 1.0 in 5 f, rotate −20°, `winner` fill | Two options, one wins | figures if numbers show |
| **P-SIDE-PROOF** | overlay | One 9:16 card 300×534 in the side slot away from the face (§3.5), the post / screen being described, optional gold border | Slide 40 px from the outer edge + fade 8 f; out 5 f | "Like this post", "this one did X" while the presenter keeps talking | creator asset or created card |
| **P-IN-HAND** | overlay | A created phone mock (rounded 64 px, 12 px bezel) tilted 6°, floating ±8 px, playing the creator's own clip | Rise 12 f with a 6° → 0° → 6° settle | Stands in for "a phone in a hand" (no stock hands) | creator clip (`ctx.videoFrame`) |

**B-3 Screen proof**
| ID | Type | On screen | Motion recipe | When | Text class / needs |
|---|---|---|---|---|---|
| **P-SCREENREC-ORB** | overlay + anchor | L-ui: the creator's recording full-bleed (1080 wide), slow push 1.00 → 1.06 per step; the **cursor orb**: Ø 84 (measured ≈ 80-100 px with its ring, v05 @ 0:07), white core 40%, `data` ring 4 px, a wide 48 px `data` glow halo, opacity 0.9; the recording is pushed in so the tapped row is ≥ 60 px tall | Orb travels between keyframes (10–16 f, ease in-out, ≤ 84 px/frame); idle drift ±3 px; **press**: scale 1 → 0.82 → 1 (6 f); **ripple**: a `data` ring Ø 64 → 160, opacity 0.8 → 0 (10 f) | Every "go to / tap / turn on / select" | anchors (§17.2), insert record (origin creator) |
| **P-FOCUS-DIM** | annotation | Everything except the target row / button dims to 35% luma; the target keeps full brightness and a 2 px `data` outline | 6 f in, before the tap; holds until the next target | Every tap on a busy screen | anchor `focus_row` |
| **P-TAP-RIPPLE** | annotation | The orb's ripple on a created UI (no recording) | As above | Taps inside `fx.appUI` | anchor |
| **P-TOGGLE-FLIP** | state | An iOS-style switch 120×72 (or the real one highlighted): knob slides, track fills `accent`, 4 white sparks | Knob 6 f (ease back), fill 6 f, sparks 8 f | "Turn this on" | event on the spoken "on" |
| **P-UI-GLITCH-SWAP** | state | One UI label inside the recording (a button or a row) glitches into the creator's aside ("Post" → "Wait! ✋") while the orb rests on it | 7 f of seeded RGB slices (±8 px) on that element only, then the new label holds ≥ 1 s (v05 @ 7.00-7.23) | A "but wait / don't tap yet" beat during a step; ≤ 1 per reel | E6 (`data-slot` = the button) |
| **P-SETTING-REVEAL** | overlay | A settings row (icon + label + switch) blurred 14 px | Unblurs 14 → 0 px over 24 f; the label is sharp before the switch flips | Hook of HA-05, "a setting you didn't know" | TC-label row (≥ 40 px) |
| **P-PILL-LABEL** | overlay | The step pill (SM-1) at y 190 | Pop 7 f; text swaps with a 4 f cross-fade | Every new screen; replaces captions on L-ui | TC-label |
| **P-ARTICLE-HIGHLIGHT** | overlay | The creator's article screenshot via `fx.shot` on W-ui-light (or `fx.headlineCard` created); an `accent` highlighter box wipes over the spoken phrase | Enters by T-2 (a white resolve); a slow drift 1.0 → 1.25 over ≈ 0.75 s, then a **fast push to ≈ 4×** onto the phrase over 18 f (ease in-out, motion blur in the middle 6 f); the highlighter wipes L → R in 8 f once the push lands (glowing `accent` box); hold ≥ 0.6 s; exit **T-13 iris carry** (v01 @ 5.5-8.3) | "Instagram announced…", "the bank's own page says…" | insert record; `source` on the beat |
| **P-PROFILE-CHIP** | overlay | A glass chip at the chest (L-set-dim): avatar Ø 96, "Name &#124; Niche" 40 px, three stats 40 px; a `winner` highlighter wipes over the niche phrase | Rise 10 f; highlighter 8 f on its word | Introducing an account (the creator's own, or a created example labelled EXAMPLE) | TC-label; numbers in figures |
| **P-TIMER-RING** | state | A ring stopwatch Ø 120 beside the chip: 01:00 → 00:59, the ring depletes | 1 tick per second (E6 digits), ring sweep linear | Only when the script states a time ("in 60 seconds") | E6, figure |
| **P-NOTIFY** | overlay | A generic notification card 900×150 at y 240, app glyph square (the creator's logo file, or initials), title + body | Drops from y 110 to 240 with a spring (10 f), holds ≥ 1.5 s, slides up 6 f | A real event from the creator's own screen; created only from the script's words | TC-label; insert record |
| **P-IN-APP** | stage | L-in-app: the presenter in a 900×1280 card at y 640, platform chrome above (story progress bar, an avatar row, a P-STAT-PILL) | G-5 shrink-to-card 12 f; chrome settles 8 f | "When you post it…", "people see this in their feed" | created chrome |
| **P-DM-THREAD** | overlay | `fx.appUI(kind: "chat")`: bubbles type in, `accent` bubbles for "me", grey for others, initials avatars | One bubble per spoken line (typing dots 8 f → bubble pop 6 f) | "They DM you…", "reply with…" | created; no real names |
| **P-SHEET-SLIDE** | state | A bottom sheet slides up inside a created UI (rounded 36 px top, `panel`) with 3–5 options; the chosen one gets the orb | Sheet 10 f (ease out); option highlight 4 f | Menus and pickers in created UIs | created |

**B-4 Verdict**
| ID | Type | On screen | Motion recipe | When | Text class / needs |
|---|---|---|---|---|---|
| **P-WRONG-MARK** | annotation | A glowing `bad` square 120×120 (3 px border, 18 px glow) with ⚠ beside the wrong element; the element gets a `bad` box | Square pops 7 f; box draws 8 f (perimeter) on the wrong word | "This is the mistake" | event |
| **P-RIGHT-MARK** | annotation | The same in `good` with ✓ | Same, on the fix word | "This is the fix" | event |
| **P-TRANSCRIPT-BLOCK** | overlay | The clip's or claim's words as a 3–6 line caps block at x 120, y 860–1200 (L-bubble / L-set-dim); a neon underline (4 px `primary`) runs under the active line | Words type in on their spoken onsets (from the clip's transcript or the script); verdict lines turn into `bad`/`good` boxes (8 f) | Teardowns, quoting a caption or script | TC-label; quote verbatim (NC-13) |
| **P-TEARDOWN-BUBBLE** | stage | L-bubble over the dimmed clip (45% luma) + P-TRANSCRIPT-BLOCK | G-4 10 f; the clip keeps playing underneath | Teardown sections | insert record (creator or created) |
| **P-VERDICT-WORLD** | stage | World flips to W-verdict-red, then to W-verdict-green, carrying the B-4 graphic of that verdict | T-8 hard flip on the verdict word + 4 f flash (≤ 40% luma change) | The one big wrong → right turn of a reel; ≤ 1 pair | — |
| **P-PEOPLE-GRID** | figure | A 12×14 grid of person icons (24 px, `muted`), a bracket label above ("ALL WANT TO LOSE WEIGHT", 40 px), a subset lit in the verdict colour | Icons fade in by row (1 f stagger); the subset lights 8 f; the bracket draws 8 f | "Who this is for", audience splits | countable: the lit count is a stated number, else the grid is labelled EXAMPLE |
| **P-THOUGHT-BUBBLE** | overlay (light comedy) | A cloud bubble 300×200 beside the head (above the shoulder, never over the face): the viewer's doubt in `bad` ("HEALTHY SWAPS?"), then the real desire in `good` ("I WANT SKINNY") | Squash pop 7 f; the text swaps with a 6 f colour flood | The audience's inner thought | TC-label 44 px |
| **P-PROGRESS-BAR** | state | A video timeline bar at the chest (x 120–960, 10 px track, playhead dot) with "END"; label above: "PROBLEM SOLVED ✓" (`good`) | The playhead runs to END (24 f), the track fills `good`; then a `bad` segment grows past END with "NEW PROBLEM ⚠" | Open loops: "solve one problem, raise the next" | progress state var |
| **P-FUNNEL** | figure | 3 stacked trapezoids (top 520 wide, 120 tall each, 16 px gaps) labelled from the script (VIEWS / FOLLOWS / SALES), the active layer lit (`accent` / `data` / `good`) with ▶ ◀ arrows, others ghosted 30% | Layers drop in 6 f stagger; the active layer lights 6 f and scales 1.06; **never fully still**: the whole funnel drifts in 3D (tilts 5–10°, the layers spread 10–20 px over 0.6–1 s, ease in-out; v03 @ 60.8-61.5) | Models and stages; one layer per section | TC-label labels ≥ 44 px |

**B-5 Beat devices**
| ID | Type | On screen | Motion recipe | When | Text class / needs |
|---|---|---|---|---|---|
| **P-HERE-CARD** | overlay (re-hook) | "HERE'S WHAT YOU DO" (or "BUT HERE'S THE CATCH") as a plain 2-line caps chunk at the chest, the CS-1 skin, white | Hard on (0 f) after a 1-word "SO" beat (≈ 0.3 s); holds ≥ 0.8 s; a relight and a Z-1 reframe on the same frame only when a section starts (§7.4) | The mid-reel re-hook | TC-display, kind `rehook` |
| **P-COUNTDOWN** | state | W-stage black: "72:00:00" in the countdown type, unit labels under it | Swipe in with a 10 f blur slide; ticks 1 per second (E6) | Only a time limit the script states | E6, figure / state `countdown` |
| **P-CELEBRATE** | overlay (light comedy) | The script word ("Congratulations") at the chest in `winner`, 24 seeded spark bursts at the top corners (y 150–400, away from the face) | Word writes on with a 10 f L → R mask; sparks burst 18 f | The win, once per reel | TC-display |
| **P-OUTLINE-STAT** | figure | A huge outline percent ("99%", 4 px `paper` stroke, no fill, 220 px) + a two-line caps label to its right | Stroke draws 10 f, label pops 7 f | A shocking share from the script | figure (stated value) |
| **P-VIEWFINDER** | overlay (texture) | Camera brackets in the 4 corners (60 px arms, 4 px `paper`@70%), "● REC" (red dot), "HD 4K", a running timecode | Fade 6 f; the REC dot blinks 15 f on / 15 f off | Talking about filming / content creation sections | TC-decorative, z 5 |

**B-6 Set & camera**
| ID | Type | On screen | Motion recipe | When | Text class / needs |
|---|---|---|---|---|---|
| **P-SET-SWAP** | stage | The `behind` set scene changes world (W-set-*) | Hard switch (0 f) on a cut point or phrase boundary | Section changes; 1–3 per minute | matte |
| **P-SET-RELIGHT** | stage | The set's glow colour changes (neutral → `bad` red rim, → blue rim) | **Hard switch (0 f)** on the caption-swap frame (v01 @ 23.58, 31.13; v04 @ 6.2); stack it with a Z-1 reframe, or hide it behind a T-14 sweep. Never cross-fade | Wrong / right turns, a new section | matte |
| **P-THUMB-WALL** | stage | The set becomes a 3-column wall of the creator's own covers (SH-3), blurred 4 px, at 45% brightness, drifting up 0.3 px/frame | 8 f cross-fade in; behind the presenter | "My content", "these posts", "people like me" | creator media only |
| **P-PUNCH** | camera | Z-1 cut reframe on a phrase boundary; Z-2 push / Z-3 pull between them | Z-1 1.0 → 1.18 on one frame (1.35 with 4K), held; Z-2 +14 % over 13 f; Z-3 −15–20 % over 16 f (§10.2) | 2–4 per 10 s on lounge/sofa takes, 0–1 on desk takes | — |
| **P-OBJECT-CUTOUT** | overlay | The creator's object photo (cut out) at the chest, in front of the body, never the face; soft shadow 0 20 40 rgba(0,0,0,.5) | Drop 30 px + fade 8 f; float ±4 px | The script names a physical thing (a product, a dish, a device) | creator asset (SH-7) or icon card |

**B-7 CTA**
| ID | Type | On screen | Motion recipe | When | Text class / needs |
|---|---|---|---|---|---|
| **P-DM-KEYWORD** | overlay | The DM input pill at the chest (§6.7): the creator's avatar (Ø 84) left, a dark translucent pill (#1B1B1B @ 85%, radius 48, x 200-940, cy ≈ 980), the keyword in **sentence case, Plus Jakarta 500 58 px** as typed, and a violet send button (#6060E0, 124 × 84) right (v04 @ 0:46) | Pill is on when the T-12 cut lands (or rises 10 f after a plain cut); the keyword types one character per 4 f, ≈ 8 cps (E6 inside the pill); send pulses 6 f; sends: rise 60 px + fade 8 f | CTA (`dm`) | kind `cta-keyword`, TC-display |
| **P-COMMENT-PILL** | overlay | The comment variant (comment glyph + heart) | Same; the heart fills `bad` on send | CTA (`comment_keyword`) | kind `cta-keyword` |

### 8.4 Line → pattern lookup `[NICHE: example]`
| Line type | Example line (Niche A / Niche B) | Primary | Alternates |
|---|---|---|---|
| The claim / promise | "This one setting tripled my reach" / "This one toggle saves you $40 a month" | P-PHONE-PAIR + P-COUNTER-ROLL | P-HERO-COUNTER, P-VERSUS-TAG |
| A result over time | "6K, then 9K, then 81K followers" / "from $0 to $3.1K saved" | P-HERO-COUNTER | P-CARD-CAROUSEL |
| A setting / feature exists | "There's a setting called Trial" / "Your app has Round-ups" | P-SETTING-REVEAL → P-TOGGLE-FLIP | P-PILL-LABEL |
| Where to click | "Go to your Professional dashboard" / "Open Settings, then Savings" | P-PILL-LABEL + P-SCREENREC-ORB + P-FOCUS-DIM | P-SHEET-SLIDE (created UI) |
| A platform / company announced it | "Instagram is rolling out…" / "The bank's own help page says…" | P-ARTICLE-HIGHLIGHT | `fx.headlineCard` (created) |
| A specific post / item | "Like this post right here" / "This transaction" | P-SIDE-PROOF | P-IN-HAND |
| The wrong way | "Most people post it like this" / "Most people leave it in checking" | CS-BAD + P-WRONG-MARK (+ P-SET-RELIGHT red) | P-VERDICT-WORD, P-PROGRESS-BAR (new problem) |
| The right way | "Instead, do this" / "Move it here instead" | CS-GOOD + P-RIGHT-MARK (+ relight blue) | P-VERDICT-WORD "PROBLEM SOLVED ✓" |
| Quoting a caption / script / clip | "His hook says: if you're a snacker…" / "The ad says: zero fees" | P-TEARDOWN-BUBBLE + P-TRANSCRIPT-BLOCK | P-TRANSCRIPT-BLOCK on L-set-dim |
| What the viewer thinks | "You're thinking: healthy swaps?" / "You think: I'll save later" | P-THOUGHT-BUBBLE | P-VERDICT-WORD |
| Who it's for | "Everyone in your audience wants X" / "9 in 10 savers…" | P-PEOPLE-GRID | P-OUTLINE-STAT |
| A model / stages | "Views, then follows, then sales" / "Earn, save, invest" | P-FUNNEL | P-PROGRESS-BAR |
| A share or percent shifts | "83% followers → 100% non-followers" / "from 2% to 4.5%" | P-DONUT-SHIFT | P-OUTLINE-STAT |
| Two options, one wins | "Normal vs Trial" / "Debit vs credit" | P-VERSUS-TAG | P-PHONE-PAIR |
| Linking two things | "Link your new reel to the old one" / "Link your card to the savings pot" | P-LINKED-CARDS | P-SCREENREC-ORB |
| A time limit | "You have 72 hours" / "before the 30th" | P-COUNTDOWN | P-TIMER-RING |
| An incoming event / payment | "They'll DM you", "you get a notification" / "your refund lands" | P-NOTIFY (the creator's real one) | P-DM-THREAD (created) |
| Your content / you as the example | "Look at my page" / "my own account" | P-THUMB-WALL | P-PROFILE-CHIP |
| A physical object | "a salad", "this mic" / "your card" | P-OBJECT-CUTOUT | `fx.card` icon card |
| The win | "You finally did it" / "you're debt-free" | P-CELEBRATE (once) | P-HERO-COUNTER + CS-WIN |
| Personal aside / story | "Last year I…" | P-SET-SWAP to W-set-warm + CS-SOFT | SH-6 aside clip |
| Filming / creating talk | "When you record your video…" | P-VIEWFINDER | — |
| The re-hook | "Here's what you do" / "But here's the catch" | P-HERE-CARD | P-COUNTDOWN |
| CTA | "DM me GUIDE" | P-DM-KEYWORD | P-COMMENT-PILL |

New line types found in a reel are mapped to existing patterns at P5 and appended here (D.6); up to 10 niche patterns may be added from these families.

### 8.5 Data and truth rules
- Every on-screen number comes from `plan/figures.json` (§18): the script (`from: script`), the creator's own screen (`from: creator`) or a spoken number (`spoken@t`).
- Card pairs and versus tags compare like with like: same metric, same period, same scale.
- **Illustrative UIs** (a created profile "Your Name | Your Niche", a created settings page); any number inside them that isn't the creator's carries EXAMPLE and is in figures.json as `illustrative: true`. Never a made-up "viral rate", engagement score, payout or follower count.

### 8.6 Comedy layer (`comedy: light`)
- Allowed gags: P-THOUGHT-BUBBLE, P-CELEBRATE, P-OBJECT-CUTOUT used playfully, a P-BANNER-TILT. Each carries information.
- Budget: ≤ 1 gag per 20 s, ≤ 3 per reel, never two in a row, never in the CTA, never covering the face. No meme sounds (§11), no stickers, no freeze-frame roasts.

### 8.7 Asset rules
- Real captures first: the creator's recordings and results screens beat any created UI (P8a ranking).
- Created UIs are generic and unbranded (`fx.device`, `fx.appUI`): no look-alike logos, no real usernames;.
- Logos only as files the creator supplies; otherwise `fx.logoPlate` (the name set in type).
- Redact personal identifiers in every recording (blur 18 px, whole on-screen time): emails, phone numbers, account numbers, card numbers, other people's handles, faces and DMs (NC-14).
- Third-party moments use the ask-then-create flow (§12.5).

### 8.8 Density and variety
- A visible event every 0.8–2.0 s (captions included at weight 0.5).
- ≥ 8 distinct patterns and ≥ 4 families per 60 s; the same pattern ≤ 2 beats in a row, except the step ritual (P-PILL-LABEL + P-SCREENREC-ORB repeat per step by design).
- Set swaps 1–3 per minute; relights don't count toward that budget.

---

## §9 Transitions & shot grammar `[REQ] [DNA]`

### 9.1 Library
| ID | Transition | Frames | Recipe | Cue role |
|---|---|---|---|---|
| **T-1** | Hard cut | 0 | On a word boundary ±1 f; set swaps and L-ui ↔ L-set returns | — |
| **T-2** | Bloom flash + white resolve | 5 + 6 | A UI element (toggle, pill) blooms into a white glare: glare scale 1 → 4, opacity 0 → 0.95 over 5 f, then cut to white; the next page **resolves out of the white** over 6 f (content opacity 0 → 1, blur 12 → 0 px, scale 0.92 → 1) (v01 @ 4.29-4.75). Into a light page without a glowing element, the white resolve alone follows a hard cut (v03 @ 9.43-9.60). **Built-in:** the white is a core `flash` transition, `{"t": <cut>, "type": "flash", "colour": "#FFFFFF", "peak": 0.95, "pre": 5, "frames": 11}` (rises over the 5 f glare, peaks on the cut, decays over the 6 f resolve); the glare sprite on the UI element and the page's own 6 f entry (blur 12 → 0, scale 0.92 → 1) stay in the scenes. ≤ 1 bloom per 20 s (; the renderer softens a 4th luminous transition in any second) | transition |
| **T-3** | Whip-in | 4 | The incoming screen slides in from the right edge over 4 f with 40 → 0 px horizontal motion blur, over the outgoing frame, which holds (v04 @ 19.03). **Built-in:** the incoming scene takes `in: "slide-r", in_frames: 4` (opaque from its first frame, over the held outgoing frame) and paints its own directional blur, `filter:${ctx.blur(40 * (1 - e), 0)}` (e = the entry's eased progress); the outgoing scene's `t_out` sits 4 f after the incoming `t_in`. `smear: true` is the quick form, but its velocity smear caps at 24 px | transition |
| **T-4** | Scale-blur push | 6 | Outgoing scales 1 → 1.25 with 0 → 16 px blur and fades; incoming 0.85 → 1 with 12 → 0 px blur | transition |
| **T-5** | Screen cross-fade | 6 | Two recordings / UI states cross-fade (the orb stays on top, continuous) | — |
| **T-6** | Dim down | 8 | `via: dim` (G-3) while the chest card rises | — |
| **T-7** | Bubble shrink / grow | 10 | `pip-shrink` / `pip-grow` (G-4), ease back | transition |
| **T-8** | Verdict flip | 0 + 4 | World hard-flips red ↔ green on the verdict word; a 4 f luminance pulse of ≤ 40%: built-in `{"t": <verdict word>, "type": "flash", "peak": 0.4, "pre": 0, "frames": 4}` | reveal |
| **T-9** | Glitch shatter | 12 | P-BANNER-GLITCH (banner exit only) | transition |
| **T-10** | Zoom-through | 10–12 | The camera dives into a phone card 1 → 5× (radial blur on the last 4 f: the `zoom-through` preset's built-in radial camera `blur`, keyed to its last 4 frames); the card's screen becomes the L-ui recording | transition |
| **T-11** | Shrink-to-card | 12 | The L-ui screen shrinks into a 9:16 side card (P-SIDE-PROOF) as the stage cuts back to L-set; G3-safe ≤ 84 px/frame | — |
| **T-12** | Glitch cut | 2–5 | Over the cut: 5–9 seeded horizontal slices shift ±30 px with ±8 px R/B fringes, plus one or two 8 px pixel-mosaic blocks; the last frame is clean (v01 @ 37.42 2 f, v05 @ 21.83 5 f). **Built-in** (core draws it over the composited frame, under the captions): `{"t": <cut>, "type": "glitch", "frames": 2-5, "pre": 1-2, "slices": 7, "offset": 30, "rgb": 8, "posterize": 0}` (posterize off: the measured picture stays near-clean, so the slices and the RGB split carry the cut; the 8 px mosaic blocks are not drawn). Variant when leaving a chat or DM screen: 3 f of scanlines + 10 px blur (v04 @ 44.73) = built-in `{"type": "blur-through", "px": 10, "frames": 3, "pre": 1}` | transition |
| **T-13** | Iris carry | 4 | A circle mask centred on the highlighted phrase shrinks the article (Ø ≈ 800 → 0 in 4 f, ease-in) to reveal the presenter underneath; the highlight box itself stays and becomes the step pill at the chest (v01 @ 8.13-8.29) | transition |
| **T-14** | Graphic sweep | 6 | The next beat's own icon (a link glyph, an arrow, a card) whips diagonally across the frame, top-right → chest, with motion blur (the glyph scene paints `filter:${ctx.blur(px, angle)}` along its travel: angle ≈ 117°, px ≈ 0.3 × its per-frame travel, ≤ 40); the outgoing graphic shrinks to the centre (4 f) and the set relight or cut happens on the frame it passes the face (v01 @ 30.83-31.17) | transition |

### 9.2 Grammar
| Boundary | Use | Never |
|---|---|---|
| Frame 0 | The banner already built + the proof entering | A fade-in from black, a static first frame |
| Hook → beat 1 | T-9 (warning / news) or T-3; T-11 evolve when the winner card becomes the first screen | A crossfade of the whole frame |
| L-set → L-ui (into a step) | T-3; T-2 into an article / light page; T-10 into a phone card | A slow dissolve |
| Screen → screen | T-5 (orb persists), a hard cut on the tap result, or T-3 | T-2 twice in a row |
| L-ui → L-set (proof done) | **T-12** (default), T-13 after an article, T-1 + Z-1, or T-11 | A fade back to the face |
| Graphic → graphic on the presenter, with a relight | T-14 | Two sweeps in a row |
| Into a card over the presenter | T-6 | Covering the face |
| Into / out of a teardown | T-7 | — |
| The wrong → right turn | T-8 (with P-VERDICT-WORLD) or P-SET-RELIGHT | Cutting the verdict colour before its word |
| Set change | P-SET-SWAP / RELIGHT, hard, on the caption-swap frame at a section boundary | A swap mid-sentence, a cross-fade |
| Last word | Hard end ≤ 6 f after the last word | A black tail > 0.2 s |

### 9.3 Shot grammar
OFF (`spine: talking_head`, `source_type: talking_head`).

### 9.4 Budget (per 60 s)
6–10 transitions. T-2 ≤ 3 (and ≤ 1 per 20 s); T-9 ≤ 1 per reel; T-12 1–3; T-13 ≤ 1 per article; T-14 ≤ 2; T-8 ≤ 2 per reel (one pair); T-10 ≤ 2. The same transition never 3× in a row, except T-5 inside one multi-screen step.

---

## §10 Motion, camera, layers, finishing `[REQ] [DNA; motion tokens TUNE ±15%]`

### 10.1 Motion tokens (30 fps)
| Token | Value |
|---|---|
| Lead | 2 f before the trigger word |
| Entries | `cubic-bezier(0.22, 1, 0.36, 1)`, 6–10 f |
| Exits | `cubic-bezier(0.64, 0, 0.78, 0)`, 5–6 f |
| Pop / back | `cubic-bezier(0.34, 1.56, 0.64, 1)`, 7 f, overshoot 6% |
| Card rise | 40 px + fade, 8 f, stagger 3 f |
| Colour flood | 1–2 f hard, then the glow bloom settles over 6 f |
| Caption swap | 0 f (hard); CS-SOFT fades 6 f in, 8–10 f out |
| Set relight / swap | 0 f, on the caption-swap frame |
| Glitch cut / white resolve / iris / whip-in | 2–5 f / 6 f / 4 f / 4 f |
| Graphic drift (W-stage, W-ui-dark) | Never fully still: 3D tilt 5–10° and layer spread 10–20 px over 0.6–1 s, ease in-out |
| Flare sweep | 12 f, 60 px white bar at 20°, 40% |
| Counter roll | 18 f (hero steps 18 f each), lands ±5 f on the number word |
| Orb travel | 10–16 f, ease in-out, ≤ 84 px/frame |
| Orb press / ripple | 6 f / 10 f |
| Toggle | 6 f knob + 6 f fill + 8 f sparks |
| Glitch (banner exit) | 17 f: red flip, fractures, 3 f slice shatter |
| Typewriter | 1 character per 4 f (≈ 8 characters/s) |
| Banner float | ±6 px, 2 s sine |
| Holds | titles ≥ 10 f after built; text ≥ 0.25 s per word |

### 10.2 Footage camera (`zoom_policy: presets`)
| ID | Preset | Recipe | Tone / use |
|---|---|---|---|
| **Z-1** | `snap-punch` | A **cut reframe**: 1.00 → 1.18 on one frame, pushed **off-centre toward the free side** (preset `origin: "free_side"`, built-in; measured 1.15–1.35, v03 @ 35.4, v04 @ 6.2), held to the next move; no zoom tween, no blur | `hype`, `win`, `right`; a section start (with the relight and caption swap on the same frame) |
| **Z-2** | `push-drift` | 1.00 → 1.14 over 13 f, ease out (preset `ease: "out"`; the engine's push-drift is linear otherwise) (v03 @ 34.7) | `explain`, `story`, a claim building |
| **Z-3** | `pull-out` | −15–20 % over 16 f, ease out (v03 @ 37.0). After a Z-1 on a cut it eases the punch back to 1.0 over 15–17 f (v04 @ 6.2-6.7); preset `from: "inherit"` starts it from the current crop and pivot, so no snap | Releasing a punch, the CTA, revealing a side card |
| **Z-4** | `shake` | ±8 px, 6 f, 1.02 bump | A `wrong` verdict landing, a counter landing on a big win |
| **Z-5** | `zoom-through` | = T-10 | Into a phone card |

Rules: frequency follows the take. Lounge or sofa takes with gestures (v03, v04): 2–4 moves per 10 s, alternating in → out (Z-1 or Z-2, then Z-3). Desk takes (v01, v02): 0–1 per 10 s, because the graphics carry the motion. Never a 3 f zoom tween with blur (not in the evidence); never the same preset twice in a row; never two moves within 0.4 s; a punch never pushes the chin below y 880 (it would collide with the chest band) and never above 1.18 on a 1080p source (1.35 needs 4K, §12.4). The set scales with the presenter (it is drawn inside the footage group).

### 10.3 Canvas camera
OFF (§21).

### 10.4 Layer order (back to front)
1. Set backdrop: `behind: true` scene, z 1, inside the footage group
2. Footage, then the presenter cut-out (engine)
3. World (visible only when the stage is `hidden` / `pip` / `card`); L-ui recordings and created UIs at z 3
4. Proof cards, charts, chest cards (z 3–4)
5. Counter chips, step pill, labels (z 5); viewfinder texture (z 5)
6. Cursor orb, ripples, ⚠ / ✓ squares, highlighter boxes (z 6)
7. Captions (z 7)
8. Glow banner, verdict words, re-hook card, DM pill (z 8)
9. Light comedy: thought bubble, celebration (z 9)
10. Flare sweeps, glitch sparks on single elements (z 11, momentary). T-2 / T-8 flashes and T-12 glitch cuts are core transitions (`timeline.transitions[]` with a `type`), drawn over the picture under the captions: never z 11 scenes

### 10.5 Finishing
- Glow only on type (banner, verdict words, caption keywords), proof borders (winner / loser / right / wrong), the orb and the step pill.
- The sets carry noise 0.02–0.04 and a 0.35–0.45 vignette; footage gets no grain and no grade.
- Cards: radius 22 (phone cards), 32–40 (chips, UI cards); soft shadows `0 20 50 rgba(0,0,0,.55)`; no hard offset shadows.

---

## §11 Sound contract (minimal) `[REQ] [VAR]`
| Line | Decision |
|---|---|
| **Cue moments** | `hook` (the f0 hit, loser flood, winner flash), `reveals` (counter landings, toggles on, verdict colours, the celebration), `transitions` (T-2 riser into the white, T-3 / T-14 whoosh, T-9 / T-12 glitch, T-10 whoosh), `cta` (a key tick per typed character and the send). Orb taps take a cue only when they change the screen. No list cue |
| **Meme cues** | Off (`comedy: light`) |
| **Music bed** | On; enters when the banner exits (after the hook) |
| **Ducking** | The bed sits ≥ 18 dB under the voice; the audio of a creator-supplied clip in a teardown plays ducked under the voice only when the presenter is silent |
| **Loudness** | −14 LUFS integrated, true peak ≤ −1.5 dBTP, hard end ≤ 6 f after the last word |

The bundled SFX pack and its global rules (S1–S6) choose the sounds; every cue sits on a visible event you declared in a scene's `events`.

---

## §12 Footage, shot list, fallbacks, inserts `[REQ]`

### 12.1 Setups `[DNA what the style assumes; VAR the buyer's setups]`
| Setup | Spec |
|---|---|
| **A (main)** | Seated at a desk, chest-up, lens at eye height ~1 m away. Head top y 300–420, chin y 700–820, face centre x 420–660 on the 1080×1920 frame. Key light 45°, a rim light behind (it sells the matte against the dark set). Plain dark top (no stripes, no green). Any background: it is replaced. 30 fps, 4K preferred (punches) |
| **B (aside, optional)** | The creator using their phone, or in a second room: 2–4 s clips for story asides |

### 12.2 Shot list
| ID | Shot | Spec | Count per 60 s | Must / optional |
|---|---|---|---|---|
| SH-1 | Screen recordings of the app / tool taught | Portrait, native resolution, dark mode if the app has it, notifications off, one recording per step, 4–12 s each, no fast scrolling | 2–4 | must |
| SH-2 | Own proof screens | Analytics, dashboards, results with the real numbers being claimed (screenshot or recording) | 1–3 | must |
| SH-3 | Own covers / thumbnails | 6–20 images of the creator's own posts | 0–6 | optional |
| SH-4 | Article / announcement screenshot | A page the creator holds, full width | 0–1 | optional |
| SH-5 | The clip being torn down | The creator's own clip, or one they hold and hand over | 0–1 | optional |
| SH-6 | Aside clip (setup B) | 2–4 s | 0–1 | optional |
| SH-7 | Object photo | PNG or plain background, the object the script names | 0–1 | optional |

### 12.3 Fallbacks
| ID | For | What the engine does instead | Fidelity cost | Result |
|---|---|---|---|---|
| FB-0 | The matte (P2) | Keep the real room: no set swap; P-SET-RELIGHT becomes a 20% colour wash over the frame edges (vignette mask, face untouched) | The virtual set is lost | degraded |
| FB-1 | SH-1 | `fx.appUI` (settings / list / browser / chat) recreating the described screen generically, orb taps on the named rows | Not the real product UI; exact menu positions can't be copied | degraded |
| FB-2 | SH-2 | Counters and cards only from numbers stated in the script (`from: script`), neutral dark card faces | No real screenshot behind the number | degraded |
| FB-3 | SH-3 | Dark gradient cards with the post's title in type (the creator's own titles from the script) | Covers read as a pattern, not a portfolio | degraded |
| FB-4 | SH-4 | `fx.headlineCard`: outlet set in type, the verbatim headline from the script, `accent` highlight bars | No real masthead | holds |
| FB-5 | SH-5 | `fx.quoteCard` / transcript block of the clip's verbatim lines + `fx.silhouette` for the person | No moving source clip | degraded |
| FB-6 | SH-6 | P-SET-SWAP to W-set-warm + Z-1 on setup A | No second location | holds |
| FB-7 | SH-7 | `fx.card` icon illustration of the object on a glass card at the chest | No photographic object | holds |

At the checkpoint, list every fallback used and why.

### 12.4 Props, reaction bank, matte, resolution
- **Props:** the creator's phone (to hold up on "this app": then P-IN-HAND isn't needed).
- **Reaction bank** (2 s each, recorded at the shoot): an excited "you did it" grin, a wince, pointing down at the chest band, pointing to the side (the side-card side), counting on fingers.
- **Matte:** required (P2). Feather 2 px, choke 1 px, temporal smoothing; QA hair at 200%.
- **Resolution:** a 1080p source allows punches ≤ 1.18 (≤ 1.35 is the hard limit); 1.35 and the tight reframes of the evidence (≈ 1.5×) need a 4K source.

### 12.5 Third-party inserts: ask, then create `[REQ]`
Never fetch anyone else's media (NC-7). Per reel:
1. Run `veos inserts scan` and refine the list. This style's usual moments: **an announcement / article** (P-ARTICLE-HIGHLIGHT), **another creator's clip** (P-TEARDOWN-BUBBLE), **an app's UI** you didn't record (P-SCREENREC-ORB), **a notification or payment** (P-NOTIFY), **a DM or comment thread** (P-DM-THREAD), **a brand logo**.
2. **Ask once:** "For these N moments, do you have a screenshot or recording? (drop the files, or say no)".
3. **Supplied:** use it as given (crop, frame, highlight, redact identifiers), never altered to say something it doesn't.
4. **Not supplied, create:** article → `fx.headlineCard` (verbatim headline from the script); clip → transcript block + `fx.silhouette` / `fx.quoteCard`; app UI → `fx.appUI`; notification → generic `P-NOTIFY` with the script's words; DM → `fx.appUI(kind: "chat")` with initials avatars; logo → `fx.logoPlate`. 
5. **Record** every moment in `plan/inserts.json` (`origin: creator | created`, `recipe`, `substitute_of`, `scene`).

### 12.6 Frame rate and audio
30 fps CFR, 1080×1920, BT.709. One voice track: high-pass 80 Hz, de-ess, light compression, −14 LUFS.

---

## §13 Output contract `[REQ] [DNA]`

### 13.1 Core beat fields
`id`, `section`, `t0`/`t1`, `spoken`, `trigger {word, at}`, `tone`, `line_type`, `layout`, `visual` (one sentence), `layers` (scene ids), `pattern`, `sfx` (moment only; the pack picks the file).

### 13.2 Conditional fields used by this style
| Field | Content |
|---|---|
| `caption` | `{profile: CS-1 \| CS-BAD \| CS-GOOD \| CS-DATA \| CS-WIN \| CS-SOFT, emphasis: [...]}` |
| `set` | The world of the `behind` set scene this beat (W-set-skyline / -neon-red / -neon-blue / -warm / P-THUMB-WALL) |
| `axis` | `bad` · `good` · `winner` · `none`: the verdict colour this beat lands, and its word |
| `state_ops` | `[{var: views \| countdown \| progress, op: set \| tick_to, value, at}]` |
| `anchor` | `{target: orb \| tap \| highlight \| focus_row, keyframes: "plan/anchors.json#<id>"}` |
| `figure_id` | Every counter, donut, grid count and hero number |
| `shot_id`, `fallback_used` | SH-n / FB-n |
| `insert` | `{id, origin: creator \| created}` |
| `exception` | `E6` on counter / countdown / typing scenes |
| `rehook` | `true` on the re-hook beat |

### 13.3 Reel header
```yaml
meta:
  format: F-A
  theme: null
  hook_archetype: HA-02          # or HA-01 / HA-07 / HA-05 / HA-18
  structure: tutorial            # variant: walkthrough | teardown | funnel | result-cash-in
  keyword: "{{BV-08.keyword|KEYWORD}}"
  sets: [W-set-skyline, W-set-neon-red, W-set-neon-blue]
  figures: [views_a, views_b]
  state: {views: counter, countdown: null, progress: null}
  mask_words: []                 # extra words to mask beyond the default list
```

### 13.4 Hook proposals (3 required)
```yaml
- name: "Hidden setting, toggle proof"
  archetype: HA-05
  banner: {line1: "INSTAGRAM", line2: "CHEATCODE", line2_role: primary, platform_gradient_on: "INSTAGRAM"}
  pair: {promise: "a setting that shows your reel to non-followers first", proof: "Settings row -> Trial toggle on"}
  stoppers: [glow banner f0, settings row unblurring, toggle flip 2.0 s]
  captions: hidden until 3.0 s (banner), then CS-DATA
  storyboard: "f0 banner + blurred row | 0.8 row sharp | 2.0 toggle on + sparks | 3.0 T-2 bloom into L-ui"
  sound: [hook hit f0, reveal on the toggle, transition on the bloom]
  stopper_test: {thumbnail: pass, mute: pass, read_s: 0.5, changes_3s: 5, payoff_s: 2.0}
```

### 13.5 Checkpoint (before building)
1. 3 hooks with banners, pairs and stopper results.
2. The beat sheet with tones, layouts, sets and axis colours.
3. The **claim → proof table** (P8a): every claim, its proof, its source (recording / screenshot / created / stated number); unproven claims flagged.
4. The transition map and the cue moments.
5. The figure and state plan (counters with provenance, countdown, progress).
6. The anchor plan (orb keyframes per recording).
7. The inserts record (creator-supplied vs created) and the fallbacks used.
8. Style stills: f0, the winner flash (≈ 2.3 s), one L-ui tap, one verdict beat, the re-hook, the CTA pill.

**Wait for approval.**

---

## §14 Worked examples `[REQ] [NICHE: example]`
Times are estimates; replace them with `words.edit.json` onsets. The personaliser rewrites these from the buyer's first approved reel (D.6).

### 14.1 Niche A (social-media growth), walkthrough, HA-05: "The setting that shows your post to strangers first"
**Banner:** INSTAGRAM / CHEATCODE (line 2 `primary`; "INSTAGRAM" in the platform gradient). **Keyword:** TRIAL. **Length:** ≈ 48 s. **Assets:** SH-1 two recordings (settings, drafts), SH-2 one insights screenshot with the two view numbers.

| t (s) | Spoken | Tone | Visual | Caption | Camera / layout | Cue moment |
|---|---|---|---|---|---|---|
| f0 | — | hype | W-set-skyline; banner built; settings row "Trial" blurred under it (P-SETTING-REVEAL) | — | L-set | hook |
| 0.0–0.8 | "There's a setting on Instagram…" | hype | Row unblurs 24 f | — | — | — |
| 1.3 | "…almost nobody uses" | hype | P-BANNER-TILT on "nobody" | — | — | — |
| 2.0 | "…and it's free reach" | proof | **P-TOGGLE-FLIP** on "free": knob, `accent` fill, sparks | — | — | reveal |
| 3.0 | "You didn't even know…" | hype | T-2 bloom out of the toggle; banner blur-up; P-SET-RELIGHT to blue | CS-1 "YOU DIDN'T / EVEN KNOW" | Z-1 | transition |

| Section | Spoken (gist) | Tone | Layout / set | Patterns |
|---|---|---|---|---|
| PROBLEM 3–9 s | "Normally your post goes to followers first, and if they don't bite, it's dead" | wrong | L-set, W-set-neon-red relight | CS-BAD; P-DONUT-SHIFT (followers share from SH-2, `from: creator`) beside the face in the side slot; P-WRONG-MARK on "dead" |
| REHOOK 9–11 s | "Here's what you do" | hype | L-set, relight blue | **P-HERE-CARD** + Z-1 (`rehook: true`, 21% of runtime) |
| STEP-1 11–19 s | "Make your reel, hit next, scroll down" | explain | L-ui (SH-1 #1) | P-PILL-LABEL "New reel → Next"; P-SCREENREC-ORB: orb to "Next" (14 f), press on "hit"; T-5 to the options screen; P-FOCUS-DIM on "Trial" |
| STEP-2 19–25 s | "Turn on Trial" | right | L-ui | Orb press on "turn on" → the real toggle; P-TOGGLE-FLIP highlight; step pill "Trial: ON" |
| PROOF 25–34 s | "Same post. Normal got 34K, Trial got 134K" | win | T-11 back to L-set; side card → then proof band | **P-VERSUS-TAG** Normal vs Trial cards, both counters roll (figures `from: creator`), "FREE" tag stamps on Trial; CS-WIN |
| WHY 34–42 s | "Because strangers see it first, so it's judged on the content, not your follower count" | explain | L-set, W-set-skyline | P-DONUT-SHIFT 83% followers → 100% non-followers (stated), CS-DATA |
| CTA 42–48 s | "DM me TRIAL and I'll send you my posting checklist" | cta | L-set, Z-3 | **P-DM-KEYWORD** "TRIAL", typed ≥ 1.5 s |

State / figures: `views_normal` (34,000, creator), `views_trial` (134,000, creator), `share_followers` (83%, script), `share_non` (100%, script). Created inserts: none (all creator-supplied).

### 14.2 Niche B (personal-finance apps), result pair, HA-01: "Your bank app hides this toggle"
**Banner:** SAVINGS / BAD → GOOD ("BAD" red from f0, "GOOD" ignites gold on its word). **Keyword:** ROUNDUP. **Length:** ≈ 62 s. **Assets:** SH-2 two balance screenshots (the creator's own savings pot before and after six months, $0 and $406), no recording of the settings (→ FB-1, created settings UI).

| t (s) | Spoken | Tone | Visual | Caption | Camera / layout | Cue moment |
|---|---|---|---|---|---|---|
| f0 | — | hype | W-set-skyline; banner; **P-PHONE-PAIR** ghosted: left = the empty savings pot, right = the same pot six months later | — | L-set | hook |
| 0.0–0.27 | — | — | Cards land | — | — | — |
| 1.4 | "This is my savings pot before…" | wrong | Left card floods red, counter "$0" | — | — | reveal |
| 2.2 | "…and this is it six months after one toggle" | win | Right card: white flash → gold, counter rolls to "$406" (`from: creator`), flare sweep; "GOOD" ignites | — | Z-1 on "toggle" | reveal |
| 3.2 | — | hype | Banner blur-up; cards slide down 60 px + fade | CS-1 "ONE / TOGGLE" | — | transition |

| Section | Spoken (gist) | Tone | Layout / set | Patterns |
|---|---|---|---|---|
| PROBLEM 3–12 s | "Most people say they'll save what's left at the end of the month. There's never anything left" | wrong | L-set → W-set-neon-red relight | CS-BAD; P-THOUGHT-BUBBLE: "I'LL SAVE LATER" (red) → "THERE'S NOTHING LEFT" stays red (gag 1); P-PROGRESS-BAR: month runs to END, balance segment empty |
| REHOOK 12–14 s | "But here's the catch" | hype | relight blue | **P-HERE-CARD** "BUT HERE'S / THE CATCH" (`rehook`; 20% of runtime) |
| STEP-1 14–24 s | "Open your app, go to Settings, then Savings" | explain | L-ui, **created** settings UI (FB-1) | P-PILL-LABEL "Settings → Savings"; `fx.appUI(kind: settings)` + P-TAP-RIPPLE on each spoken menu; P-SHEET-SLIDE |
| STEP-2 24–31 s | "Turn on round-ups. Every purchase rounds up to the next dollar" | right | L-ui (created) → L-set-dim | P-TOGGLE-FLIP on "on"; then T-6 → P-PROFILE-CHIP-style chest card showing "Coffee $3.40 → $4.00, +$0.60 saved" (numbers from the script, EXAMPLE label) |
| WHY 31–43 s | "60 cents doesn't feel like anything. That's the point. 26 purchases a week…" | explain | L-set, W-set-skyline | CS-DATA; **P-HERO-COUNTER** steps $15.60 a week → $68 a month → $406 by month six (figures: `per_period` from the script's inputs; the six-month step is the creator's screenshot value, and 26 weeks × $15.60 = $405.60 rounds to it) |
| PROOF 43–52 s | "And that's my actual pot" | win | T-11 the hero counter → side card of SH-2 "after" screenshot (gold border) | P-SIDE-PROOF; CS-WIN; P-CELEBRATE "Finally" is **not** used (keep it for a bigger win) |
| ASIDE 52–56 s | "I didn't change a single habit" | story | W-set-warm swap | CS-SOFT |
| CTA 56–62 s | "Comment ROUNDUP and I'll send you the 3 settings I turn on first" | cta | L-set, Z-3, W-set-skyline | **P-COMMENT-PILL** "ROUNDUP" |

Figures: `pot_before` 0 (creator), `pot_after` 406 (creator screenshot), `per_buy` 0.60 (script), `buys_week` 26 (script); `week` = 0.60 × 26 = 15.60; `month` = `per_period` (52 / 12) → 67.60, shown "$68" (`round_to` 1); `six_months` = 15.60 × 26 weeks = 405.60, shown "$406" and equal to `pot_after` at display precision. Created inserts: I1 settings UI (`recreated_ui`, substitute of the bank app's settings screen).

### 14.3 Niche C (fitness coaching), teardown, HA-18: "Why this coach's clip got 1.2M views"
**Banner:** CLIENT HOOK / SH*T → GOLD. **Keyword:** HOOKS. **Length:** ≈ 75 s. **Assets:** SH-5 the creator's own client's clip (supplied, with permission: origin creator), its view count from the creator's screenshot (1.2M), the client's first version of the clip (3 views).

| t (s) | Spoken | Tone | Visual | Caption | Camera / layout | Cue moment |
|---|---|---|---|---|---|---|
| f0 | — | hype | W-set-skyline; banner (SH*T red, GOLD `muted` until its word); **P-PHONE-PAIR** ghosted: version 1 / version 2 of the client's clip, both playing (`ctx.videoFrame`) | — | L-set | hook |
| 1.5 | "Same coach, same video: this one got 3 views…" | wrong | Left card red, counter "3" | — | — | reveal |
| 2.2 | "…this one got 1.2 million" | win | Right card gold, counter rolls to "1.2M"; "GOLD" ignites | — | — | reveal |
| 3.0 | "The only difference? The hook" | hype | Banner blur-up; the gold card scales up to fill the frame (12 f) and becomes the dimmed clip under the bubble as the stage shrinks to L-bubble | CS-1 "THE / HOOK" | G-4 at 3.4 | transition |

| Section | Spoken (gist) | Tone | Layout / set | Patterns |
|---|---|---|---|---|
| CLIP 3–14 s | The client's opening line plays, then "Listen to how it starts" | proof | **L-bubble** over the dimmed clip | **P-TEARDOWN-BUBBLE** + P-TRANSCRIPT-BLOCK typing the clip's verbatim words; P-PROFILE-CHIP of the client (their own account, supplied) with the niche highlighted |
| WRONG 14–26 s | "Version one opens with 'healthy swaps'. Nobody wakes up wanting healthy swaps" | wrong | L-bubble | Transcript line "HEALTHY SWAPS" turns into a red box + P-WRONG-MARK; **P-VERDICT-WORD** "WRONG DESIRE" |
| THOUGHT 26–31 s | "What they actually think is: I want to look good" | right | T-1 to L-set (setup B aside if supplied, else setup A) | **P-THOUGHT-BUBBLE**: "HEALTHY SWAPS?" red → "I WANT TO LOOK GOOD" green (gag 1) |
| RIGHT 31–44 s | "Version two says: 'low-calorie snacks that actually taste good'" | right | L-bubble | Transcript block re-types the new line, green boxes + P-RIGHT-MARK; CS-GOOD when the presenter speaks over it |
| REHOOK 44–46 s | "And here's why that matters" | hype | L-set, relight blue | **P-HERE-CARD** "HERE'S / WHY" (`rehook`, 59% of runtime) |
| WHO 46–62 s | "Out of everyone who sees it, only some are snackers… but all of them want to lose weight" | explain → right | **P-VERDICT-WORLD**: W-verdict-red then W-verdict-green | P-PEOPLE-GRID: the lit subset in red is EXAMPLE (no stated count), the full grid lights green on "all of them" (T-8) |
| PROOF 62–69 s | "Speak to the desire, not the method" | win | L-set, W-set-skyline | P-SIDE-PROOF of the gold card; CS-WIN |
| CTA 69–75 s | "DM me HOOKS and I'll send you 20 openers like this" | cta | L-set, Z-3 | **P-DM-KEYWORD** "HOOKS" |

Inserts: I1 client clip (`creator`, file supplied), I2 client profile chip (`creator` screenshot). Without them: I1 → transcript block + `fx.silhouette` (FB-5); counters only from the creator's stated numbers (FB-2).

---

## §15 QA checklist `[REQ] [DNA]`

**1. Profile conformance**
- [ ] Format F-A; no theme; duration 45–90 s (standard). `V-PROFILE`
- [ ] Presenter share 35–65%; no absence > 10 s. `V-PRESENCE`
- [ ] Layouts are only L-set, L-set-dim, L-ui, L-bubble, L-in-app, within their shares. `V-LAYOUT`

**2. Hook**
- [ ] f0: presenter on a set + the glow banner fully built + the proof element entering. `V-F0`
- [ ] Banner: 2 lines, ≤ 5 words, no emoji, fit-width 780 px at cy 1000, masked, exits 2.6–3.6 s. `V-TITLE` / review
- [ ] Verdict / payoff by 2.5 s; ≥ 4 weighted SCs in 0–3 s; the mute test passes. `V-F0` / `V-CADENCE`

**3. Body and cadence**
- [ ] 4–8 SC per 10 s, no gap > 2.0 s, nothing static > 2.5 s. `V-CADENCE`
- [ ] Every claim has its proof by 1.5 s (the P8a table is fully ticked). review
- [ ] Every step follows the ritual: pill → L-ui → orb tap on the verb (±2 f) → proof ≥ 1.0 s → return with Z-1. `V-ONWORD` / review
- [ ] One mid-reel re-hook (25–75%); no gap > 40 s between re-hooks; intro ≤ 12%. `V-REHOOK`
- [ ] Set swaps 1–3 per minute, on section boundaries; the real room never shows. review
- [ ] Zooms 3–5 per minute, never the same preset twice in a row, ≤ 1.18 on 1080p. `V-CAMERA`

**4. Captions**
- [ ] CS profiles only, 1–4 caps words, ≤ 2 lines, lead ≤ 150 ms, one glowing keyword per chunk at most. `V-CAPTION`
- [ ] The right profile per tone run (CS-BAD on wrong, CS-GOOD on right, CS-WIN on the result). review
- [ ] Hidden under the banner, under z8 cards and on L-ui; exact app / menu names; profanity masked everywhere. `V-CAPTION` / review
- [ ] Floors: captions 72 px, labels ≥ 40 px, legal ≥ 22 px; contrast ≥ 4.5:1. `V-TYPE`

**5. Modules**
- [ ] §17: counters, countdown and progress show the running state; orb keyframes sit on the real targets; the orb never covers the face. `V-STATE` (pending) / review
- [ ] §18: every number is in figures.json with provenance; counters land ±5 f on the number word; K/M formatting. `V-DATA` / `V-NUMFMT`

**6. Truth and inserts**
- [ ] Every third-party moment is creator-supplied or created and recorded; created UIs; example values carry EXAMPLE. `V-INSERTS`
- [ ] No invented metrics, receipts, testimonials or DMs; identifiers blurred. review (NC-6, NC-14)
- [ ] Quotes and transcript blocks are verbatim. `V-INSERTS` / review (NC-13)

**7. Colour and sound**
- [ ] ≤ 3 bright hues per frame; verdict colours only on verdict words; primary only in type. `V-HUES` / review
- [ ] Cues only on declared moments (hook, reveals, transitions, CTA); no meme cues; the bed enters after the banner. S1–S6
- [ ] −14 LUFS, true peak ≤ −1.5 dBTP, bed ≥ 18 dB under the voice. review

**8. End and export**
- [ ] The keyword is typed in the pill ≥ 1.5 s; it equals `meta.keyword`. `V-PROMISE`
- [ ] Hard end ≤ 6 f after the last word; 1080×1920, 30 fps. review

---

## §16 Frame template / chrome
OFF (`profile.modules.chrome = false`): nothing persists across the reel; the chest band is a position, not a slot.

## §17 Running state & anchored graphics `[COND: modules.running_state, modules.anchors] [DNA mechanics]`

### 17.1 State variables
| Var | Type | Display | Rules |
|---|---|---|---|
| `views` | counter | P-COUNTER-ROLL chips, P-HERO-COUNTER | One value per card; a counter only changes on an op on its number word; it never shows a value the creator didn't show or say |
| `countdown` | timer (`time_base: set`, no jumps) | P-COUNTDOWN, P-TIMER-RING | Starts at the stated limit ("72 hours" → 72:00:00) and ticks down 1 per second of edit time; shown only while the limit is the topic |
| `progress` | progress | P-PROGRESS-BAR | 0 → 100% across its beat; the "new problem" segment is a second op |

Ops per beat: `state_ops [{var, op: set | tick_to, value, at}]`.

### 17.2 Anchors
- **Targets:** `orb` (the cursor position per tap), `tap` (the tapped element's box), `highlight` (an article phrase's box), `focus_row` (the row kept bright by P-FOCUS-DIM).
- **Mode `keyframes`:** in the anchor pass (P8d) read each recording's frames with `veos sheet`, and for every tap write `{t, x, y, w, h}` of the target in screen pixels into `plan/anchors.json` (the recording is 1080 wide on L-ui, so recording px × (1080 / recording width) = screen px; add the push scale of P-SCREENREC-ORB). The orb scene interpolates between keyframes with the orb travel recipe.
- **Fallback** (`static_near_target`): when a target moves (a scroll), place the orb at the target's position at the tap time and hold it there; don't track.
- **Face:** anchored elements stay 40 px clear of the face box (only matters on L-bubble and L-in-app, where the face shares the frame).
- `track` (live tracking) waits for E-15; keyframes are the method today.

### 17.3 Validator
`V-STATE` (pending in this engine; checked by review): displayed counter values equal the state and the figures; the countdown is monotonic; orb keyframes land within 24 px of the tapped element in the sampled frames.

## §18 Data contract `[COND: modules.data_figures] [DNA rules]`
- Every counter, donut, outline stat, hero number and people-grid count is a figure in `plan/figures.json`.
- **Provenance:** `creator` (their own screen; the screenshot asset is named in the input's `said`), `script` (`said` = the words), `spoken@t`. A view count from somebody else's post is shown only from the creator's own screenshot of it.
- **Formulas:** `sum`, `diff`, `ratio`, `percent_change`, `per_period`, `unit_convert`; most counters are `none` (stated values).
- **Same scale:** a card pair or a versus tag compares one metric over one period; two bars share a `scale_id`.
- **Format:** `profile.numbers` (K / M with 1 decimal, `$`; Indian buyers ₹ lakh / crore). Write numbers with `ctx.fmtNum`, never typed.
- **Illustrative:** a created example ("Coffee $3.40 → $4.00") is `illustrative: true` with the EXAMPLE label.
- `V-DATA` recomputes; counters land within ±5 f of the spoken number word; `V-NUMFMT` checks the format.

## §19 Evidence & citations
OFF (`modules.citations = false`). Article proof is handled per beat by P-ARTICLE-HIGHLIGHT through §12.5 (the creator's screenshot via `fx.shot`, else `fx.headlineCard`); such a beat still carries `source {masthead, date, headline}` and `highlight_spans`, and V-CITE checks it.

## §20 Dialogue
OFF (`modules.dialogue = false`; single presenter).

## §21 Canvas camera
OFF (`modules.canvas_camera = false`): pushes into articles and recordings are scene-level scale (`fx.shot` push, P-SCREENREC-ORB push), not a canvas camera.

## §22 Ink & annotation layer
OFF (`modules.ink = false`): highlights, ⚠ / ✓ squares and boxes are B-3 / B-4 patterns, not hand-drawn ink.

## §23 Continuity
OFF (`modules.continuity = false`).

## §24 Series furniture
OFF by default (`modules.series = false`, VAR). When a buyer turns it on: a "PART {n}" step-pill-style tag at y 150 for the first 2 s after the banner exits (counts toward the intro cap).

## §25 Sponsor, brand & end cards
OFF by default (`modules.brand = false`, VAR). When on: a sponsor appears as a P-NOTIFY card with the brand's supplied logo file + the "Paid partnership" TC-legal line held ≥ 2 s (NC-12); no end card (the DM pill is the end).

---

## Part C. Exceptions and the non-overridable core

### C.1 Non-overridable core
NC-1…NC-14 apply unchanged (STYLE-PLAYBOOK-STRUCTURE Part C.1). The ones this style leans on hardest:
- **NC-1** The face: side cards go away from the face; the chest band starts ≥ 80 px under the chin; the L-set-dim card stays at the chest.
- **NC-6** Truth: created UIs labelled, illustrative values labelled, no invented metrics (the style's evidence contained several; the template forbids them).
- **NC-7** Creator-owned media: teardown clips and articles only from the creator.
- **NC-14** Redaction of identifiers in recordings and DMs.

### C.2 Declared exceptions
| ID | Token | Limits | Scenes that use it |
|---|---|---|---|
| E6 Hard swap | `"E6": {"slot_tolerance_px": 4}` | Content swaps only inside a fixed container (`data-slot`); container entry/exit eased | P-COUNTER-ROLL chips, P-COUNTDOWN digits, P-TIMER-RING digits, P-DM-KEYWORD / P-COMMENT-PILL typing |

A buyer may switch E6 off (VAR); counters then roll with declared `events` instead.

---

## Part D. Personalisation

### D.1 Asked at setup (one round)
| ID | Question | Default | Lands on |
|---|---|---|---|
| BV-01 | Your name and handle | "the creator", "@yourhandle" | `creator.name`, `creator.handle` |
| BV-02 | One or two brand colours | keep `primary` #F5F000 and `accent` #1F6FEB | `roles.primary.default`, `roles.accent.default` (contrast-nudged). Red, green, gold and cyan never change |
| BV-05 | The language you speak; caption language and script | English ({{BV-05.speech|en}} → {{BV-05.captions|en}}) | `profile.language`, always asked: **English** → English captions (default) · **Hinglish** → romanised Hinglish captions · **Hindi** → Devanagari captions; numbers follow (BV-06) |
| BV-08 | Your CTA: DM keyword or comment keyword, the word, what you send | DM, KEYWORD, "the full guide" | `profile.cta.chosen`, `creator.cta` |

### D.2 Lock map (summary; full map in `tokens.json → locks`)
| Area | Lock |
|---|---|
| Style DNA, "Copy these 5", D1–D8, §1, §2 rules, §9, §13, §15 | DNA |
| Banner recipe (kind, 2 lines, chest position, glow, z 8) | DNA; size, cy (940–1080), block width (720–860), read time TUNE |
| Meaning roles (`bad`, `good`, `winner`), `paper` | DNA (fixed) |
| `primary`, `accent` | VAR (brand) |
| `data` (orb cyan) | TUNE (a cyan–sky hue) |
| Sets (W-set-*) | TUNE (dark, one glow); verdict worlds DNA |
| Fonts | TUNE within each slot's class |
| Caption mechanics (unit, case, glow emphasis, profile set) | DNA; size 64–84 and cy 960–1100 TUNE; profanity mask VAR |
| Cadence, motion, budgets | TUNE ±15% |
| Camera presets / zoom policy | DNA (punch scale TUNE 1.12–1.25) |
| Footage setups, props, reaction bank | VAR |
| Shot list, fallbacks, matte | DNA |
| Series, brand modules | VAR |
| §6.4, §8.4, §14, App. A | NICHE |

### D.3 Defaulted, changeable later
BV-03 fonts (inside each class), BV-04 niche (inferred per reel), BV-06 number format (₹ / lakh for Indian languages), BV-07 captions full ↔ keywords, BV-11 humour (off / light), BV-13 series, BV-14 sponsor disclosure wording, BV-15 never-on-screen list, BV-16 logo files (the platform glyph in the banner needs one), BV-17 duration within 45–90 s.

### D.4 NICHE slots, filled per reel
§6.4 hook pairs (P7), §8.4 line types (P5/P8), §14 (after the first approved reel), App. A (approved banners), the caption glossary (confirmed app and menu names).

---

## Part E. Deviations from the architects' row (STYLE-COVERAGE #8)
| Item | Coverage said | Template does | Why |
|---|---|---|---|
| Modules | running_state, anchors | + **data_figures** | Every counter is the style's proof; V-DATA must recompute them (NC-6) |
| Presence | host 30–65 | host **35–65**, max absence 10 s | The evidence UI runs of 14–16 s break the presence floor; the template splits them with L-bubble |
| Captions | 62–74 px, glow keyword | **72 px**, 2 lines, `span: phrase`, 5 colour profiles + CS-SOFT | Measured 70–90 px cap lines, two-line chunks with a whole coloured second line (v01 @0:25, v02 @1:30); per-tone colour comes from profile switches |
| Banner font | extended heavy sans | Unbounded 800–900 + fit-width | resolved: Unbounded is bundled |
| Illustrative UIs | labelled per NC-6 | labelled, and **invented metrics banned** | v02's "VIRAL RATE 79%", v04's receipts and DMs would fail NC-6 as real |

## Part F. ID index
| Prefix | IDs in this playbook |
|---|---|
| D | D1–D8 |
| H / N | H1–H15 / N1–N14 |
| W | W-set-skyline, W-set-neon-red, W-set-neon-blue, W-set-warm, W-ui-dark, W-ui-light, W-stage, W-verdict-red, W-verdict-green |
| L / G | L-set, L-set-dim, L-ui, L-bubble, L-in-app / G-1…G-6 |
| CS | CS-1, CS-BAD, CS-GOOD, CS-DATA, CS-WIN, CS-SOFT |
| HA / ST | HA-02 (default), HA-01, HA-07, HA-05, HA-18 / ST-1…ST-6 |
| SM | SM-1 Step pill |
| B / P | B-1…B-7 / 51 patterns (§8.3) |
| T / Z | T-1…T-14 / Z-1…Z-5 |
| SH / FB | SH-1…SH-7 / FB-0…FB-7 |
| F | F-A |
| E | E6 |

---

## App. A Headline & hook bank `[NICHE: example]`
Slots in brackets are filled per reel. Line 1 / line 2 (glow colour).

| # | Banner | Archetype | Niche example |
|---|---|---|---|
| 1 | NEVER POST / [THING] (`bad`) | HA-02 | A: NEVER POST / AT NIGHT · B: NEVER PAY / THIS FEE |
| 2 | [PLATFORM] / CHEATCODE (`primary`) | HA-05 | A: INSTAGRAM / CHEATCODE · B: YOUR BANK / CHEATCODE |
| 3 | [THING] / BAD → GOOD (`bad` → `winner`) | HA-01 | A: YOUR HOOK / SH*T → GOLD · B: SAVINGS / BAD → GOOD |
| 4 | YOU FINALLY / DID IT! (`good`) | HA-07 | A: a viral post · B: first $10K saved |
| 5 | [PLATFORM] / BIG UPDATE (`primary`) | HA-02 | A: INSTAGRAM / BIG UPDATE · B: YOUR APP / BIG UPDATE |
| 6 | STOP [HABIT] / [RESULT] (`bad`) | HA-02 | A: STOP DELETING / OLD POSTS · B: STOP USING / DEBIT CARDS |
| 7 | [N] VIEWS / → [M] VIEWS (`winner`) | HA-01 | A: 3 VIEWS / → 1.2M VIEWS (real numbers only) |
| 8 | HIDDEN / [FEATURE] (`data`) | HA-05 | A: HIDDEN / TRIAL MODE · B: HIDDEN / ROUND-UPS |
| 9 | WHY THIS / WENT VIRAL (`winner`) | HA-18 | A or C: a teardown of a supplied clip |
| 10 | [TIME] TO / CASH IN (`primary`) | HA-07 | A: 72 HOURS / TO CASH IN · B: 30 DAYS / TO CLAIM IT |

## App. B Evidence map
The full source map, with timestamps for every DNA rule and the `(unverified)` list, is in `evidence.md` (templates only). Summary: banner on f0 at the chest (v01–v05 @0:00–0:03); red/gold card pair (v02 @0:00–0:03, v04 @0:00–0:03, v01 @0:13–0:19); cursor orb recordings (v01 @0:39–0:53, v04 @0:40, v05 @0:05–0:21); sets and relights (v01 red → blue @0:00–0:04, v03 skyline → kitchen @0:21); glowing-keyword caps captions (v01 @0:20–1:15, v02 @1:23–1:39); DM keyword pills (v02 @1:40, v03 @1:08, v04 @0:45).
