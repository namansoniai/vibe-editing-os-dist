# Monochrome Metaphor Style Playbook (template v1)

**Purpose.** You (Claude) receive either a **voice-over** (F-B, the default: an audio file plus its script, no camera footage) or a **seated talking-head take** (F-A) from {{BV-01.name|the creator}}. Use this playbook to turn one spoken idea into a calm, premium, black-and-white reel: in F-B every frame is built by the engine as **one evolving glowing metaphor** that morphs scene to scene without a cut; in F-A the creator sits still on camera, introduced by a text-only black card. Expected input: a VO of 25–55 s (F-B), or one continuous seated take of 30–50 s (F-A), plus the script.

**Inspired by:** Dan Koe (evidence `analysis/short/dan-koe.md`, v01–v03; full map in `evidence.md`).

### Style DNA `[DNA]`
A Monochrome Metaphor reel reads in one glance as **quiet, near-monochrome and expensive**: a pure black void, white light and grey line art, one slowly evolving object per idea that *becomes* the next object instead of cutting to it, a single white dot that stands for "you" and travels through every scene, and small type that whispers at the bottom of the frame. Nothing flashes, nothing punches in, nothing is ever fully still. In the seated format the same restraint holds: a black card with white serif words, then one static, softly lit take with small gold lowercase serif captions on the chest.

**Copy these 5 things and it reads as this style:**
1. **Black void, greyscale light.** Every F-B pixel is black, white or grey; the only warm note in the whole style is the F-A caption gold (§4, §3.1).
2. **One continuous morph chain.** F-B has zero hard cuts: each scene is born from the previous scene's object (morph, push-through, sink or hand-off), or, in screen-and-game chains, switches off and on with a quiet power flicker (§9, §23).
3. **One literal metaphor object per idea**, centred, 35–55% of the frame width, doing the mechanism of the sentence (§8.3, §8.4).
4. **Quiet small type with no emphasis**: 44 px light-medium sans (F-B) or 60 px gold lowercase Garamond (F-A), one line, never bold, never coloured mid-line (§5.3).
5. **Slow, eased, almost never-static motion**: soft in-out easing, 12–48 f morphs, breathing glows, at most one held-still beat ≤ 0.9 s, no overshoot, no shake, no zoom on footage (§10, §7.6).

### Fidelity audit corrections (2026-10-06, full-resolution check of v01-v03)
These override older figures below. Evidence: `docs/audit/monochrome-metaphor/audit.md`.
- **The F-B void is flat pure black** (#000 sampled everywhere away from objects); no ground glow or vignette. Light lives only in the objects (bloom, beams, rim light).
- **No gold in F-B.** Gold (`#FCC31E`, more saturated than before) is the F-A seated caption colour only; the F-B CTA keyword is white with bloom.
- **CS-B** is really Poppins 400 ~43 px #F4F4F4 at cy ~1537; the template keeps 500 (E3 floor) and cy 1470 (safe band).
- **End line** "NOW AVAILABLE ON / AMAZON" is Montserrat 500 caps ~60 px (cap 48), two lines cy 180 / 262, letters assembling from scattered positions.
- **Line art** is ~4 px white core with ~20 px bloom (thicker and brighter than 3 px); the motif dot Ø 40 with ~24 px glow is confirmed.

### Motion corrections (2026-10-07, every frame of v01-v03 measured)
These override older motion figures below. Evidence: `docs/audit/monochrome-metaphor/completeness.md` and `evidence.md` (Motion).
- **F-B captions wipe as a chunk:** the whole chunk is revealed left → right in 5–7 f (not word by word on each onset), held, then erased right → left in 4–6 f, with 3–4 empty frames before the next chunk (v03 @ 0:00.13, 0:01.77, 0:06.05). Shipped as CS-B `reveal: chunk` + the built-in `wipe` swap (6 f in L → R, 5 f out R → L, 40 px feather).
- **F-A captions and card phrases swap hard** (0 frames, v01 @ 0:00.71, 0:06.06); the cold-open card is perfectly still between swaps (up to 1.6 s).
- **F-B has two transition voices.** Lit-object chains (v03) morph, push through, sink or collapse into the dot; screen-and-game chains (v02) switch scenes with a **power flicker** through 0.2–0.45 s of black, a **CRT collapse** out of screens, or a **flicker swap** in which a shared shape survives (the grown dot becomes the nail head). Both stay quiet: object-level, never a full-frame strobe.
- **Push-through is two moves:** the object contracts to ~0.65× over ~12 f while its pupil collapses to a dot, then the camera pushes ≥ 4× in 9 f (ease-in), with a 2 f dissolve into dark before the next object grows from the ground (v03 @ 0:01.70–0:02.57).
- **The one flare is a reveal:** a horizontal slit opens into a bow-tie and a grey wash in 3 f (peak frame mean luma 37%), then decays over 8 f to show the new object (v03 @ 0:00.67–0:01.0).
- **Pacing:** F-B scenes median ~4 s (v03 2.4 s, v02 5.9 s), p90 ~8.5 s; v03 changes on 89% of frames; the longest true hold is the lone dot, perfectly still for 0.87 s (v02 @ 0:01.64). F-A camera is locked (median 0 px drift, p95 0.7 px/frame, scale 1.000).

### Directives `[DNA]`
| # | Directive | Where it lives |
|---|---|---|
| D1 | **One idea, one object.** Every sentence gets exactly one hero object, and that object is the noun or mechanism of the sentence (a clock for time, a hammer for one tool). Nothing on screen decorates | §8.3, §8.4, H7 |
| D2 | **Never cut in F-B.** Every scene enters *from* something already on screen: a morph, a push-through into the object, a sink, or the dot handing itself over. The only parentless exit is the quiet power flicker (T-FLICKER / T-CRT-OFF, ≤ 4 per reel), never a hard cut | §9, §23, H4 |
| D3 | **Light is the only colour.** Meaning is carried by brightness: dim = the cost, lit = the way out. Chroma appears only as the F-A caption gold and the end-card keyword | §4, H8 |
| D4 | **The dot is the viewer.** One white glowing dot (Ø 40 px) is "you" in every reel and appears in at least 60% of F-B scenes | §23.2, H5 |
| D5 | **Type whispers.** One line, 1–5 words, small, no emphasis, no stroke, no box | §5.3, H9 |
| D6 | **Motion never stops and never hurries.** Something drifts, breathes or morphs on almost every frame (one held-still beat ≤ 0.9 s is allowed); objects move like a slow exhale (no overshoot, no shake). The fast moments are brief and singular: one 3 f flare reveal, a 9 f push-through, object-level flickers | §10, §7.6, H2 |
| D7 | **The voice carries the argument; the picture carries the feeling; the captions carry every word** so a muted viewer still gets the essay | §5.3, §6.1 |
| D8 | **End quietly.** A product card, a keyword card or nothing. Never a hype outro, never a "follow for more" stack | §6.7, §25 |

Buyer directives are added below as **BD1…** `[VAR]`; they may only make the style stricter or more specific.

### Quick index
| § | What | Status |
|---|---|---|
| §0 | Style profile, formats F-B (default) and F-A | ON |
| §1 | Procedure (voice-over branch and seated branch) | ON |
| §2 | Hard rules, exceptions E3 + E4 | ON |
| §3 | Worlds W-void / W-card / W-studio, layouts L-void / L-card / L-seated | ON |
| §4 | Colour: monochrome roles, one warm accent | ON |
| §5 | Type and caption profiles CS-B, CS-A, CS-A0 | ON |
| §6 | Hook system: HA-15 (F-B), HA-12 (F-A), alternates | ON |
| §7 | Structure (essay) and cadence | ON |
| §8 | Visual system: 45 patterns P-… | ON |
| §9 | Transitions T-… (morphs, no cuts in F-B) | ON |
| §10 | Motion, canvas camera pointer, layers, bloom | ON |
| §11 | Sound contract | ON |
| §12 | Footage, inserts | ON |
| §13 | Output contract | ON |
| §14 | Worked examples (3) | ON |
| §15 | QA checklist | ON |
| §16 | Frame template / chrome | OFF |
| §17 | Running state & anchors | OFF |
| §18 | Data contract | OFF |
| §19 | Evidence & citations | OFF |
| §20 | Dialogue | OFF |
| §21 | Canvas camera | ON (F-B) |
| §22 | Ink & annotation | OFF |
| §23 | Continuity: morph chain, the dot | ON (F-B) |
| §24 | Series furniture | OFF (VAR) |
| §25 | Product card, keyword card, handle card | ON |
| Parts C–F | Exceptions, personalisation, template decisions (TD), ID registry | ON |
| App. A–B | Headline bank, evidence map | ON |

---

## §0 Style profile `[REQ]`

```yaml
profile:                         # §0, mirrored in tokens.json -> profile (the default format F-B)
  source_type: voiceover_only
  presenter: {presence: none, share: [0, 0], max_absence_s: null}
  spine: audio
  captions: {mode: full, role: support, mute_policy: mute_safe}
  graphics: primary
  duration: {class: short, target_s: [25, 55]}
  language: {speech: en, captions: {lang: en, script: Latn, transform: verbatim}, on_screen: en, post_title: en,
             supported: [[en, en, Latn], [hinglish, hinglish, Latn], [hi, hi, Deva]]}
  numbers: {grouping: international, currency: "$", compact: k_m_b, units: metric, decimals: 0}
  tone: {energy: calm, comedy: off, comedy_max: off}
  themes: {policy: single, packs: [], default: null}
  formats: {list: [F-B, F-A], default: F-B}
  footage_dependency: none
  cta: {devices: [product_card, comment_keyword, link_bio, none], placement: end}
  modules: {chrome: false, running_state: false, anchors: false, data_figures: false, citations: false,
            dialogue: false, canvas_camera: true, ink: false, continuity: true, series: false, brand: true}

formats.F-A.profile:             # overrides for the seated format
  source_type: talking_head
  presenter: {presence: anchor, share: [80, 92], max_absence_s: 6}
  spine: talking_head
  graphics: minimal
  footage_dependency: low
  modules: {canvas_camera: false, continuity: false}
```

Why each value:
- **source_type: voiceover_only**, because two of the three evidence reels contain no footage of the creator at all (v02 50 s, v03 25 s); F-A (`talking_head`) covers v01.
- **presenter: none** (F-B) / **anchor 80–92%** (F-A), because v02/v03 show 0% face and v01 shows the face 87% of runtime after a 5.1 s text card.
- **spine: audio** (F-B), because the picture is chosen sentence by sentence to the VO; F-A's spine is the single take.
- **captions: full / support / mute_safe.** v03 captions 84% of runtime in 1–4-word groups; v02 shows text only in 0–2 s, which fails a muted viewer (analysis gap D7). The template takes v03's model and makes it the rule. This deviates from the coverage table (`keywords→off / sound_on`); see Part E.
- **graphics: primary** (F-B: 100% engine-built) / **minimal** (F-A: only the cold-open card, captions and an optional end card).
- **duration: short, 25–55 s**, from the evidence range 25.1–50.3 s.
- **language: en**, from the burned-in captions (no transcript existed; the speech language is listed as unverified). Hinglish and Hindi are supported combinations for buyers (§5.5).
- **tone: calm, comedy off**: no gag, sticker or meme moment in 113 s of evidence.
- **themes: single**: monochrome is the theme; there are no packs.
- **footage_dependency: none** (F-B) / **low** (F-A: one seated take).
- **cta**: v03 ends on a product card; v01/v02 end with no CTA. Keyword and link-in-bio are the quiet variants of the same end card (§25).
- **modules**: `continuity` (morph chain + the dot) and `canvas_camera` (push-throughs) carry F-B; `brand` holds the end cards. F-A switches both F-B modules off (PV-5: canvas camera needs `graphics: primary`).

### 0.4 Formats `[DNA set; VAR enable]`

| Field | F-B "Metaphor animation" (default) | F-A "Seated essay" |
|---|---|---|
| when | A voice-over essay: one idea, told as one evolving metaphor. Use it whenever the creator has no footage, or the idea is abstract (time, attention, choices, identity, growth) | The creator wants to be seen; the essay is a single sentence-chain spoken to camera from a chair |
| profile overrides | none (it is the base profile) | `talking_head`, `anchor [80,92]`, `max_absence_s 6`, `graphics minimal`, `footage low`, canvas camera and continuity off |
| layouts | L-void (100%) | L-card (8–20%, the cold open and an optional end card), L-seated (80–92%) |
| captions | CS-B (Poppins 500, 44 px, y 1470, chunk wipe: 6 f in L → R, 5 f out R → L) | CS-A0 on the card (EB Garamond 68 px white, y 960, hard swaps), CS-A seated (EB Garamond 62 px gold #FCC31E, y 1372, hard swaps) |
| default hook | HA-15 Atmosphere | HA-12 Thesis typography (text-only cold open) |
| cadence | SC/10 s 3–9, hook 3, max gap 3.0 s, **max static 0** | SC/10 s 1.5–4, hook 1.0, no max gap (a static take is DNA), max static 2.5 |
| structure | essay | essay |
| shared DNA | Black, greyscale light, small quiet lowercase-or-sentence-case type with no emphasis, zero punch-ins, one thought per reel, a quiet end | same |

A reel uses exactly one format, declared in the reel header (§13.3). The five "Copy these 5" traits hold in both formats (in F-A, trait 2 becomes "one take, one cut: card → face" and trait 3 becomes "the face is the object").

### 0.5 Theme packs
OFF (`themes.policy: single`): the monochrome palette is the theme; the buyer's colour (BV-02) only changes the accent (§4.1).

---

## §1 Procedure (follow in order) `[REQ] [DNA]`

This style's craft is **P8a metaphor casting** (one noun → one object that performs the sentence) and **P8b chain design** (how each object becomes the next). Spend your thinking there.

**F-B (voice-over) — the default**
1. **P1 Inventory.** `veos project init --voiceover <vo.wav> --script <script.md>`: the VO is source `V`, the cut map is the VO's own timeline, the stage is `hidden` throughout. ffprobe the VO (mono or stereo, 48 kHz, duration). Register any creator files (product cover, wordmark, screenshots) with `veos asset add --origin creator`.
2. **P2 Prepare.** Skipped (no footage, no matte).
3. **P3 Transcribe** the VO with word timestamps; apply `language.captions.transform` (verbatim for `en`); fix brand spellings against the glossary.
4. **P4 Segment** into essay units (§7.1): `THESIS` (the first sentence), `CLAUSE-n` (each supporting clause), `COST`, `TURN`, `PAYOFF`, `CTA`. One unit = one sentence or one breath group of 2–5 s.
5. **P5 Classify** every sentence with a line type L-01…L-26 (§8.4) and mark its **trigger word**: the noun the object stands for ("hours", "scrolling", "tool", "door").
6. **P6 Tone-tag** every sentence: `state` · `cost` · `turn` · `resolve` · `cta` (§4.2, `tone_treatment`). The tone sets the light level, not the colour.
7. **P7 Hook plan.** Default HA-15 (§6.2). Write **3 hook variants** (different opening objects, or HA-12 with a split title), run ST-1/2/3/5/6 (§6.1), recommend one.
8. **P8 Visual plan.**
   - **P8a Metaphor casting:** for every unit pick one pattern from §8.3 through the lookup §8.4; write the object, its action and the word it acts on ("the gear starts turning on *work*").
   - **P8b Chain design:** for every boundary write `morph_out` of scene N and `morph_in` of scene N+1 using only T-MORPH, T-PUSH-THROUGH, T-HANDOFF, T-SINK, T-FLICKER-SWAP, T-COLLAPSE-DOT, (≤ 4 per reel) T-FLICKER / T-CRT-OFF or (≤ 2 per reel) T-BLOOM-DISSOLVE (§9, §23). Write the dot's state per scene (`motif_state`, §23.2).
   - **P8c Light plan:** per tone, the glow level and the camera move (§4.2, §21).
   - Third-party moments: the §12.5 flow (ask once, else a created substitute).
9. **P9 Beat sheet** (§13): one beat per trigger word; every beat names its pattern, `morph_in`, `morph_out`, `motif_state` and canvas-camera move; check the cadence numbers (§7.6) and the no-orphan rule.
10. **P10 SFX ledger** (§11, only the allowed cue moments) and the **transition map** (§9.3 format).
11. **P11 Assets.** Build every object as scene code (fx blocks or bespoke SVG, §8.3); collect creator files; list the lit 3D objects (`VEOS.fx.three`, §8.2 B-4) and check that no two are on screen at once.
12. **P12 Checkpoint** (§13.5), then **wait for approval.**
13. **P13 Build:** `plan/timeline.json` (stage `[{"t": 0, "layout": "L-void"}]`, `canvas_camera`, `canvas_nodes`) + `plan/scenes.js`, act by act → `veos scenes-meta` → `veos measure --every 10` → `veos validate` → preview stills of every boundary (the chain is reviewed by eye until V-CONTINUITY ships, Part F) → QA (§15, ≤ 3 passes) → render.

**F-A (seated) — branch insertions**
- **P1** registers the single take; conform VFR to 30 fps CFR (v01 was 24 fps: conform, never speed-change).
- **P2** skipped (no matte: nothing goes behind the head).
- **P4** marks the **cold-open boundary**: the end of the first sentence (or first two short sentences) that falls between 3.0 and 6.0 s. That word boundary is the reel's only cut (T-CARD-CUT, §9).
- **P8** is short: L-card from 0 to the boundary, L-seated after it, optional end card (§25). There is no metaphor casting and no chain.
- **P9** beats are the caption chunks; check that no caption chunk straddles the cold-open boundary (a chunk that starts on the card and ends on the face splits mid-phrase: move the boundary to the sentence end).

**Module steps**

| Module | Step |
|---|---|
| `continuity` (F-B) | P8b chain design: `enter_from` / `exit_to` per scene, motif state per scene, the bloom-dissolve budget (≤ 2) |
| `canvas_camera` (F-B) | P8c: one camera move per turn or push-through, spacing ≥ 0.4 s (§21) |
| `brand` | Sponsor check (disclosure line and hold, NC-12) and the end-card choice (§25); the product cover is the creator's file or the card is not used |

---

## §2 Hard rules `[REQ] [DNA]`

### 2.1 Editing rules (every style)
The ten editing rules in `playbooks/_global/GLOBAL-RULES.md` apply. They are directions, not limits: smooth, seamless motion; nothing overlaps by accident; keep the face clear (behind the speaker is fair game, text included); readable at a glance; one idea at a time; show the thing, not the word; say what was said; hook titles hook; pace like the style, not like a timer; the style decides the look.
- **Facts the engine checks:** accidental overlaps, jumps, the face covered, unreadable text, numbers and quotes that don't match what was said, the promised count. Every count, timing and budget this playbook gives is direction for the edit, not a limit.
- **Picture first, in this style's own look:** every key beat shows the thing being said (an object, a screen or app, a diagram, numbers in motion), not just its word; text supports the picture and never replaces it. When the speaker points with words ("this, this and this", "from this to this", "ye dekho"), show what they mean. Illustrations may use made-up but realistic numbers and names ("212 views", "1.2M views"), with no label; a number or quote the speaker says is shown as said. This overrides any rule below that bans made-up numbers or asks for an example tag: those rules now cover claims (the creator's results, prices, benchmarks, testimonials), not illustrations.
- **Hook titles hook:** the on-screen title promises the viewer something (an outcome, a curiosity gap, who it's for) and is true to what the reel delivers; it need not repeat the spoken words. This playbook sets its shape (§5.2, §6.5: lines, sizes, word limits, case), never its voice (§6).
- **Retired (8 Oct 2026), whatever this playbook says below:** no REPRESENTATIONAL or example labels on made-up cards, no credit lines, no flash limit (flash as often as this style calls for; any "NC-11" cap below no longer applies), and text may sit behind the speaker without an exception.

### 2.2 Declared exceptions

| E-id | Style limits (never looser than the registry) | DNA reason | Evidence |
|---|---|---|---|
| **E3** Quiet type | F-B captions (CS-B) 40–53 px (shipped 44), weight ≥ 500, 1 line, ≤ 24 characters, contrast ≥ 7:1 (shipped #F4F4F4 on #000 = 19:1). Labels 32–39 px only when `redundant: true`. Display text stays ≥ 40 px. F-A captions are 60 px and do **not** use E3 | Small, quiet type is trait 4: the picture leads, the words whisper | v03 captions measured ~43 px Poppins at y ≈ 1543 (v03 @ 0:04–0:20); analysis D4 |
| **E4** Ambient field | P-ICON-SWIRL and P-DOT-FIELD backgrounds only: ≤ 24 items, each ≤ 4% of the frame, no text, ≤ 60 px/s, ≤ 3.0 s per occurrence, ≤ 2 occurrences per reel, dimmed ≥ 40% within 40 px of the caption rect, drawn at z2 with `ambient: true` | A swirl of the world's pulls around the dot is texture, not content | v03 @ 0:00–0:00.5 (line icons spiralling in around a dot); v02 @ 0:26–0:32 (dot field) |

No other exception is used. E1, E2, E5 and E6 are never allowed in this style.

### 2.3 Style MUST rules
- **H1 Frame 0 (F-B, HA-15):** a non-text object is already moving on f0 (entrance, drift or breathing glow) and at least 25% of the frame width is lit object or motif; no presenter. *(F-A, HA-12):* f0 is the black card with the first caption chunk visible within 3 f; the presenter is **not** on screen at f0. check: V-F0
- **H2 Cadence:** F-B 3–9 weighted SCs per 10 s, ≥ 3 in 0–3 s, no full-weight gap > 3.0 s (hook 2.0 s), **0 s static** for the validator (the continuous void ambient runs under every frame) while the picture itself may hold the lone dot perfectly still once, ≤ 0.9 s (v02 @ 0:01.64); F-A 1.5–4 per 10 s, ≥ 1.0 in 0–3 s, static ≤ 2.5 s (the live take moves). check: V-CADENCE
- **H3 Payoff by:** the thesis sentence is fully captioned by 3.0 s in F-B (first caption chunk by 0.7 s) and the cold-open card has stated the thesis by 6.0 s in F-A. check: V-F0
- **H4 No orphan scenes (F-B):** every scene boundary is T-MORPH, T-PUSH-THROUGH, T-HANDOFF, T-SINK, T-FLICKER-SWAP, T-COLLAPSE-DOT or T-BLOOM-DISSOLVE (≤ 2 per reel); T-FLICKER / T-CRT-OFF ≤ 4 per reel together; 0 hard cuts; F-A has exactly 1 cut (card → face). check: V-CONTINUITY (pending) + review
- **H5 The motif:** the dot (Ø 30–48 px, default 40, white core, 24 px glow) appears in ≥ 60% of F-B scenes and is never duplicated (one "you" per frame, except P-DOT-AMONG where it is the only *lit* dot). check: V-CONTINUITY (pending) + review
- **H6 On the word:** each object's defining action (gear turns, beam opens, X draws) starts 2 f before its trigger word and is complete within ±5 f of it. check: V-ONWORD
- **H7 One object per idea:** one hero object on screen per sentence (G2 counts it as one element even when it has parts); objects sit centred in the object zone x 96–984, y 330–1330, 35–55% of the frame width (hard limits 15–80%). check: review + G2
- **H8 Monochrome:** in F-B every graphic pixel is neutral (OKLCH chroma < 0.02) except the end-card accent; F-A adds only the caption gold. `max_bright_per_frame` 2. check: V-HUES + review
- **H9 Captions:** one line, 1–4 words (F-B) / 3–5 words (F-A), no emphasis, no stroke, no container, synced ≤ 0.15 s lead; F-B captions never rise above y 1420 or fall below y 1520. check: V-CAPTION + V-TYPE
- **H10 Presence (F-A):** presenter share 80–92%, longest absence ≤ 6 s (the cold open ≤ 6.0 s, an end card ≤ 4 s). check: V-PRESENCE
- **H11 Dead air:** F-B (`spine: audio`): VO pauses are kept as spoken (they are the breath of the essay) but no pause exceeds 1.2 s, and during any pause ≥ 0.6 s an object action or camera drift continues. F-A: ≤ 1 gap ≥ 150 ms per 15 s, except one deliberate ≤ 0.8 s pause before the payoff line. check: review
- **H12 No footage zoom:** `zoom_policy: none`. F-A is never punched, pushed, cropped or shaken; F-B moves only the canvas camera (§21). check: V-CAMERA
- **H13 Truth:** every number on screen is spoken in the script, and is drawn as a countable set (40 hours = 40 ticks), never as a figure card; illustrative objects carry no invented statistics. check: review (NC-6)
- **H14 Promise integrity:** if the VO promises a resource or a product, the end card shows it; the CTA keyword on the keyword card equals the spoken keyword {{BV-08.keyword|KEYWORD}}. check: V-PROMISE
- **H15 Inserts:** a third-party moment is the creator's own file or a created quiet substitute (P-QUIET-QUOTE / PLATE / SCREEN), recorded in `plan/inserts.json`. check: V-INSERTS
- **H16 Spelling, audio, determinism:** brand names exact (glossary); −14 LUFS, true peak ≤ −1.5 dBTP, hard end ≤ 6 f after the last word (NC-8); every particle, grain and swirl is seeded from the frame (`ctx.rng`) (NC-9). check: V-CAPTION + review

### 2.4 NEVER
- **N1** Colour in F-B graphics: no blue glows, no gold objects, no tinted gradients, no brand colours on objects. The accent appears only on the end card.
- **N2** Hard cuts, whip pans, RGB-split or datamosh glitches, film burns, light-leak PNGs, full-frame white flash frames. (The quiet object-level power flicker of §9 is not a glitch: it dims and blinks the object only, in greys, ≤ 3 blinks.)
- **N3** Overshoot, bounce, elastic, squash-pop, shake, crash zooms or any footage zoom (F-A is a locked-off shot).
- **N4** Emoji, stickers, memes, comedy marks, arrows with labels, chips, pills, boxes behind captions.
- **N5** Stock footage, stock 3D renders, AI-generated photos, glossy "productivity" clip art, brain-with-lightning icons, rocket ships, money rain, gym-bro silhouettes. Objects are line art, light shapes or lit 3D objects built in the renderer (`VEOS.fx.three`, B-4), never imported renders.
- **N6** Bold or coloured words inside captions; ALL CAPS captions; two-line captions; captions inside the IG bottom band (y > 1520).
- **N7** Two hero objects competing (a clock *and* a phone *and* a gear as equals). Supporting parts (the gear behind the eye) sit at ≤ 50% opacity and are part of one object.
- **N8** Fake dashboards, fake revenue numbers, fake follower counts, fake UIs presented as real (NC-6). A phone mock is generic: grey cards, no app names, no logos.
- **N9** Full-frame luminance flashes: the one allowed light burst (P-FLARE-BOWTIE) peaks at ≤ 40% mean frame luminance, ramps 3 f, decays ≥ 8 f, once per reel.
- **N10** A black tail > 0.2 s; an outro louder than the voice; music with lyrics.
- **N11** In F-A: graphics over the face, lower-thirds, B-roll cutaways, jump cuts, a second camera angle, a bright or busy background.
- **N12** Text above the object zone during F-B body beats (the top 330 px stay empty; the split title and the end-card line are the only exceptions).
- **N13** Numbers presented as data (axes, % cards, counters) — this style shows quantity as countable things only.
- **N14** Metaphors that need a label to be understood. If the object needs a caption other than the VO caption to make sense, choose another object.

Buyers may add **BN1…** `[VAR]`.

---

## §3 Worlds, layouts, stage moves, safe zones `[REQ] [DNA; coordinates TUNE ±5%]`

### 3.1 Worlds
| ID | Kind | Look | Carries | Enter / exit |
|---|---|---|---|---|
| **W-void** | void | `night` #000000, **pure black, flat** (sampled 0,0,0 away from objects in v02 @ 0:17 / 0:30 and v03 @ 0:12); no ground glow, no noise, no vignette: any haze is the lit object's own bloom | Every F-B frame | The reel starts and ends in it; never exits. Drawn by `VEOS.fx.ambient({kind: "void", glow: "night", extra: {continuous: true}})` (glow coloured like the ground = invisible; keeps the continuous-motion registration) for the full runtime |
| **W-card** | void | #000000, no glow, no noise | The F-A cold open and the F-A end card | Entered at f0; left by T-CARD-CUT |
| **W-studio** | footage | The creator's own seated set (§12.1): dark slate wall, two soft vertical light strips, black tee | F-A body | Entered by the one cut; left by a cut to W-card for the end card (optional) |

### 3.2 Layout library
| ID | Engine | Presenter rect | Graphic rect | Caption band | Treatment | Share |
|---|---|---|---|---|---|---|
| **L-void** | `hidden` | — | object zone x 96–984, y 330–1330 | CS-B, centre y 1470 (band y 1420–1520) | — | F-B 100% |
| **L-card** | `hidden` | — | the card is empty black; text only | CS-A0, centre y 960 | — | F-A 8–20% |
| **L-seated** | `full` | full frame, head top y 220–300, eyes y 600–660, chin y 880–960 | none | CS-A, centre y 1372 (on the chest) | none (no dim, no zoom) | F-A 80–92% |

Layout schedule: F-B never changes layout. F-A is exactly `L-card → L-seated` (→ `L-card` for an optional end card).

### 3.3 Stage moves
| ID | Move | Recipe | Use |
|---|---|---|---|
| **G-1** | Card → seated (T-CARD-CUT) | `{"t": <boundary>, "layout": "L-seated", "via": "cut"}`: a hard cut on the word boundary that ends the cold-open sentence, between 3.0 and 6.0 s. The card captions end on that frame; the seated captions start on the next word | F-A, once |
| **G-2** | Seated → end card | `{"t": <last word end + 6 f>, "layout": "L-card", "via": "fade-through", "dur": 10}`: the face fades through black over 10 f, the end card settles in | F-A, only when a CTA end card is used |
| **G-3** | None in F-B | The stage is `hidden` for the whole reel; all movement is scenes and the canvas camera | F-B |

### 3.4 Layout diagrams
```
L-void (F-B)                          L-seated (F-A)                       L-card (F-A cold open)
┌─────────────────────────┐ 0         ┌─────────────────────────┐ 0         ┌─────────────────────────┐ 0
│ (IG top UI, keep clear) │ ← 0–110   │  dark wall  ▌      ▐    │           │                         │
│                         │           │  light strip   light    │           │                         │
│   (empty black; split   │ ← 110–330 │        ╭───╮            │ ← head    │                         │
│    title line 1 @ 746)  │           │        │o o│            │   top     │                         │
│ ┌ object zone ─────────┐│ ← 330     │        │ ‿ │            │   220–300 │                         │
│ │                      ││           │        ╰─┬─╯            │ ← chin    │   the fastest way       │ ← CS-A0
│ │      ◉  hero object  ││ ← centre  │      ╭───┴───╮          │   880–960 │   (white serif 68 px)   │   cy 960
│ │      (540, 960)      ││   y 960   │      │ black │          │           │                         │
│ │                      ││           │      │  tee  │          │           │                         │
│ └──────────────────────┘│ ← 1330    │  you change the places  │ ← CS-A    │                         │
│   (gap 90 px)           │           │      (gold serif 60)    │   cy 1372 │                         │
│   with endless scrolling│ ← CS-B    │      hands / desk       │           │                         │
│                         │   cy 1470 │                         │           │                         │
│ (IG bottom UI)          │ ← > 1540  │ (IG bottom UI)          │           │ (IG bottom UI)          │
└─────────────────────────┘ 1920      └─────────────────────────┘ 1920      └─────────────────────────┘ 1920
```
End card (both formats): line "NOW AVAILABLE" cy 230 (TC-label 60 px caps; two lines at cy 180 / 262), product cover x 220–860, y 360–1320 on an `ash` panel with a 2 px white rim light; keyword or handle line cy 1430 (captions hidden during the end card).

### 3.5 Safe zones and bands
- **Meaning-text box:** x 64–1016, y 110–1500 (NC-5). The right 110 px between y 900 and 1540 hold no text.
- **Object zone (F-B):** x 96–984, y 330–1330, centre (540, 960). Objects may glow past it; their solid parts stay inside it.
- **Caption band:** F-B y 1420–1520 (centre 1470) is reserved: nothing brighter than `slate` sits in it while a caption shows, and bloom from objects is masked to ≤ 0.25 luminance there. F-A centre 1372 on the chest.
- **Split-title band (HA-12 alternate only):** line 1 centre y 746, line 2 centre y 1160, straddling the motif row at y 960.
- **End-card line:** centre y 230.

### 3.6 Presenter rules `[COND: presence ≠ none]` (F-A only)
- Share 80–92% of runtime; the longest absence is the cold open (≤ 6.0 s) or the end card (≤ 4.0 s).
- The presenter returns from the card with one hard cut (G-1) and never leaves mid-body.
- Crop: none. The take is used as shot, centred, head top y 220–300. If the buyer's take frames the head higher than y 180 or the chin lower than y 1000, reframe once by scaling ≤ 1.10× (a 1080p source allows it) for the whole take, never per sentence.
- Nothing is drawn in front of or behind the head (no E1). The only overlay is the caption on the chest, ≥ 40 px below the chin.

---

## §4 Colour `[REQ] [roles' meanings DNA; accent VAR]`

### 4.1 Role palette
| Role | Hex | One job | Text on it | Contrast | Brandable |
|---|---|---|---|---|---|
| `night` | #000000 | The void (every F-B frame, the F-A card) | `paper` | 19.1:1 | no (DNA) |
| `primary` | #FFFFFF | Light: glow cores, the dot, beam cores, the lit state | `ink` | 19.8:1 | no (DNA) |
| `mist` | #D8D8D8 | Outlines at rest, split title, in-object words | `ink` | 14.7:1 on night | no (TUNE grey) |
| `smoke` | #8A8A8A | Inactive outlines, struck-out options, threads, handle line | `ink` | 6.1:1 on night (never caption text) | no (TUNE grey) |
| `slate` | #4A4A4A | Filled surfaces: phone cards, bar track, shadow side of lit objects | `paper` | 8.0:1 | no |
| `ash` | #141414 | End-card panel, product-card back, ground ellipse | `paper` | 17.5:1 | no |
| `grid` | #3A3A3A | Dots of P-DOT-FIELD at rest | — | — | no |
| `bad` | #6E6E6E | The dimmed state: the cost, the old way (grey, never red) | `paper` | — | no (fixed meaning) |
| `good` | #FFFFFF | The lit state: the chosen path (white + full glow) | `ink` | — | no (fixed meaning) |
| `accent` | **{{BV-02.accent|#FCC31E}}** | F-A caption gold; in F-B only the end-card keyword or handle | `ink` | 9.5:1 on #0B0B0B | **yes (BV-02)** |
| `paper` | #F4F4F4 | White text on black (cold-open card, end-card line) | — | 19.1:1 on night | no |
| `ink` | #0A0A0A | Text on light fills (rare) | — | — | no |

F-B caption colour is a fixed light grey #F4F4F4 (19:1 on black), not a role, so a buyer's accent never tints the essay.

### 4.2 Meanings
- **The axis is brightness, not hue:** dark → lit = cost → way out, old → new, lost → found. `cost` beats dim objects to `smoke` / `bad` and drop glow to 0–8 px; `turn` beats light the dot as a source (glow 90 px) or open a beam; `resolve` beats leave only the chosen object lit.
- **White core = alive**, grey outline = present but inactive, slate fill = surface, black = nothing.
- **The accent means "the creator speaks to you directly"**: the F-A captions and the end-card keyword. It never marks an object.
- Brand colours never appear (a product cover is the creator's own image and may carry its own colours on the end card only).

### 4.3 Theme packs
OFF (`themes.policy: single`).

### 4.4 Grades
OFF for scenes. F-A footage is not regraded: the look (cool, low saturation, blacks lifted to about #0B0B0B, warm skin) comes from the buyer's set (§12.1). Exposure and white balance only.

### 4.5 Rules
- `max_bright_per_frame` 2 (NC-10); in practice F-B has 0 chromatic hues and F-A has 1.
- Glow is white only: `drop-shadow(0 0 Npx rgba(255,255,255,a))` with N 8–40 px and a 0.25–0.6; a bloom halo 20–60 px at ~40% opacity on the hero object only (§10.5).
- Grey-on-black text needs ≥ 7:1 (E3): only `mist`, `paper`, #F4F4F4 or `primary` may carry text; `smoke` carries only the TC-legal handle.
- Footage (F-A) is never tinted; the gold caption is the only colour added.

---

## §5 Type & caption system `[REQ]`

### 5.1 Font map `[slots DNA; families TUNE within the font class]`
| Slot | Family | Weights | Font class (TUNE boundary) | Used for |
|---|---|---|---|---|
| `serif` | **EB Garamond** | 400 | old-style Garamond text serif (EB Garamond, Source Serif 4, Instrument Serif) | F-A captions (gold), the cold-open card (white) |
| `body` | **Poppins** | 500 (captions), 400 (handle, legal) | light geometric sans (Poppins, Jost, Plus Jakarta Sans, Montserrat) | F-B captions, CTA line, handle |
| `display` | **Montserrat** | 400 / 500 / 700 | tracked geometric caps (Montserrat, Jost, Poppins) | Split title, in-object words, end-card line, CTA keyword |

All three are bundled (`assets/fonts`). Devanagari: Poppins carries Devanagari natively; EB Garamond falls back to Noto Sans Devanagari (§5.5). Wordmarks and book covers are image assets, never fonts.

### 5.2 Headline element `[COND: headline kind ≠ none] [DNA recipe; NICHE text]`
F-B: `title_card` **P-SPLIT-TITLE**, used only with the HA-12 alternate. F-A: `none` (the cold-open caption card is the stopper).

| Property | P-SPLIT-TITLE |
|---|---|
| Fill / stroke / shadow / radius / rotation | none / none / none / none / 0° |
| Type | Montserrat 500, 50 px (TUNE 46–56), caps, tracking +0.04 em, `mist` #D8D8D8 |
| Layout | Two lines, centred: line 1 centre y 746, line 2 centre y 1160; the motif row (or the dot) sits between them at y 960 |
| Words / lines | ≤ 8 words total, 2–5 per line, exactly 2 lines; no chip, no emoji |
| f0 | 2 f of black, then **T-FLICKER on** with the dot row (9 f: dim 25% → 50% → dim → off 1 f → dim → full; v02 @ 0:00.07–0:00.33). Not a blur: the "blur" in the 1 fps sheet was a dim flicker frame |
| Life | Static; the object between the lines acts (dots eaten, the dot breathes) |
| Lifetime | `hook`: 1.0–2.0 s (v02: 1.33 s) |
| Exit | **T-FLICKER off** (8 f: off, one 1 f flash back, off) together with the uneaten dots, leaving the lone motif dot (v02 @ 0:01.33–0:01.57); the captions take over |
| Read | ≤ 1.5 s (ST-4) |

### 5.3 Caption profiles `[DNA mechanics; fonts TUNE; language VAR]`
Captions are generated by the caption engine from `words.edit.json`; never write cards by hand. `captions.default` is CS-B (F-B) or CS-A (F-A); `by_layout` switches L-card to CS-A0 automatically.

| Group | **CS-B** (F-B, `extends: lib:dankoe_b`) | **CS-A** (F-A seated, `extends: lib:dankoe_a`) | **CS-A0** (F-A cold-open card) |
|---|---|---|---|
| Mode | full / support / mute_safe | full / support / mute_safe | same |
| Chunking | `group`, 1–4 words, ≤ 24 characters, 1 line; never split a name, number or unit; break on punctuation and pauses ≥ 0.9 s | `group`, 3–5 words, ≤ 28 characters, 1 line | `group`, 3–5 words, ≤ 26 characters, 1 line |
| Timing | lead 2 f; ≥ 0.25 s per word; **reveal: chunk**. A soft left → right wipe of the whole chunk, erased right → left, 3–4 empty frames between chunks (v03 @ 0:00.13–0:00.27, 0:01.77–0:01.90): swap `{"type": "wipe", "frames": 6, "out_frames": 5, "dir": "right", "feather_px": 40}` (the exit erases toward the left by default); pause hold 0.6 s; tail 0.12 s | lead 2 f; ≥ 0.25 s/word; swap **`hard`** (0 f, v01 @ 0:06.06); pause hold 0.5 s | lead 2 f; swap **`hard`** (0 f, v01 @ 0:00.71, 0:02.96); the card is fully still between phrases; pause hold 0.8 s |
| Skin | Poppins **500**, **44 px** (TC-subtitle under E3; TUNE 40–53), case `sentence`, tracking 0, colour #F4F4F4, no stroke, no shadow, no container | EB Garamond 400, **62 px** (TC-subtitle, no exception; TUNE 56–68), case `lower`, colour `accent` {{BV-02.accent|#FCC31E}}, shadow 0 2 12 rgba(0,0,0,.45) (invisible on the black tee; protects contrast on lighter fabric), no stroke, no container | EB Garamond 400, **68 px** (TUNE 60–76), `lower`, `paper` #F4F4F4, no shadow |
| Punctuation | `strip_end` (no full stops at chunk ends; mid-chunk commas stay) | `strip_end` | `strip_end` |
| Position | `fixed_y` centre **1470** (band 1420–1520; TUNE 1440–1480), centred, max width 900 | `fixed_y` centre **1372** (TUNE 1340–1420), centred; `avoid_face` on | `fixed_y` centre **960** |
| Emphasis | **none** | **none** | **none** |
| Variants | karaoke, tiers, duet, stack: none | none | none |
| Hide | under z8 scenes; during declared transitions; during the end card (`captions.hide` over the end-card span) and while P-SPLIT-TITLE is up | under z8; during the end card | — |
| Language | Latn, keep English terms, normalise spelling, profanity masked `inner` (S**T), on by default; glossary from the creator | same | same |

Rules:
- One caption profile per format. CS-B never appears in F-A and CS-A never in F-B.
- Lowercase in F-A is DNA (v01: every chunk lowercase, including "i"); sentence case in F-B (v03: "You weren't born", "Numb your mind").
- The cold-open boundary must fall on a chunk boundary (P4): no chunk may run from the card onto the face.

### 5.4 Other text systems
| Element | Class | Recipe | Hold |
|---|---|---|---|
| **In-object word** (P-OBJECT-WORD, e.g. a word on one feed card) | TC-label 40 px, `redundant: true` only when it repeats a spoken word | Montserrat 700 caps, tracking +0.08 em, `mist`, inside its object; fades in 6 f | ≥ 1.0 s; ≤ 1 per reel |
| **End-card line** ("NOW AVAILABLE", "LINK IN BIO") | TC-label 60 px | Montserrat 500 caps, tracking +0.02, `paper`, centre y 230, 1–2 lines; starts ~0.8 s after the card lands; **letters flicker on in place in a seeded random order** (each letter blinks 1–3 times, 2 f on / 1–2 f off, before it stays), whole line done in 30–36 f (v03 @ 0:21.83–0:23.0) | until the end |
| **CTA keyword** | TC-display 88 px (TUNE 72–110) | Montserrat 700 caps, tracking +0.06, `accent`, centre y 900 on the keyword card | ≥ 1.5 s |
| **CTA line** ("comment") | TC-label 44 px | Poppins 500 sentence case, `mist`, centre y 780 | with the keyword |
| **Handle** {{BV-01.handle|@yourhandle}} | TC-legal 30 px | Poppins 400, `smoke`, centre y 1430 on end cards | with the end card |
| **Legal / disclosure** | TC-legal 24 px | Poppins 400 caps, tracking +0.06, `smoke`, top-left x 64, y 140 | ≥ 2 s (NC-12) |
| Numbers inside objects | — | Not used: quantities are counted objects (H13). A lock-screen time is shown only when the script says a time | — |

### 5.5 Language and number rules
- **Spelling:** captions verbatim from the VO (`transform: verbatim` for `en`); brand names exact from the glossary.
- **Hinglish (`hinglish/hinglish/Latn`):** romanised as spoken, English terms kept verbatim; CS-B case stays `sentence`, CS-A stays `lower`.
- **Hinglish → English captions (`hinglish/en/Latn`):** `transform: translate`, keep the chunk sizes; the translation keeps the speaker's word order where it can so the word-reveal still lands on the right beat.
- **Hindi (`hi/hi/Deva`):** Poppins renders Devanagari for CS-B; CS-A/CS-A0 fall back to Noto Sans Devanagari (no italic, no case); sizes stay the same; check the matra clearance in the 1420–1520 band.
- **Numbers:** international grouping, `$`, K/M/B compact (Indian grouping and ₹ when BV-06 follows an Indian language). Numbers appear only in captions; on screen a quantity is a count of objects.

---

## §6 Hook system `[REQ]`

**Hook title (every style, 8 Oct 2026; above anything below):** the on-screen title promises the viewer something: an outcome they want, a curiosity gap, or who it's for ("How to go viral as a doctor creating content", not the label "Reels for Doctors"). It doesn't have to repeat the spoken words; it has to be true to what the reel delivers. A title shown as someone's words (in quotes) is still word for word. This section sets the title's shape (lines, sizes, word limits, case, the keyword device), never its voice. Write 8–10 candidates from the formulas below plus the proven patterns ("How to X as a Y", "Why your X isn't working", "The X nobody tells you", "Stop doing X", "Your X vs mine", a number or a contrast), score them on outcome, curiosity, who it's for and brevity, check the best against the stopper tests, and pick; any "write 3" below means this, and the next two go to the storyboard as alternates. A style with no on-screen title applies this to its post title.

### 6.1 Stopper tests
| Test | F-B (HA-15) | F-A (HA-12) |
|---|---|---|
| **ST-1 Thumbnail** at 25% scale | One lit object or the dot + its glow fills ≥ 25% of the frame width and reads as a *thing* (an eye, a lighthouse, a row of dots) | The white serif phrase on black reads at 25% (68 px → 17 px) |
| **ST-2 Mute** | The first caption chunk is on screen by 0.7 s and the thesis sentence is fully captioned by 3.0 s | The cold-open card shows the whole thesis sentence by 6.0 s |
| **ST-3 Motion at f0** | A non-text object moves on f0 (entrance, spiral, breathing glow, drift) | The ambient void and the first chunk's fade-in |
| **ST-4 Read time** | Split title (HA-12 only) reads in ≤ 1.5 s (≤ 8 words) | Each card phrase holds ≥ 0.25 s per word |
| **ST-5 Change count** | ≥ 3 weighted SCs in 0–3 s (`hook_sc_3s` 3) | ≥ 1.0 (two card phrase swaps) |
| **ST-6 Payoff by** | The thesis claim is spoken and captioned by 3.0 s; the first object transformation lands by 2.5 s | Thesis on the card by 6.0 s; face by 6.0 s |

### 6.2 Default archetypes `[DNA]`

**F-B default: HA-15 Atmosphere ("the striking object").** The first frame is a beautiful, moving, monochrome object that is already the metaphor; the thesis arrives in the captions; the object transforms on the thesis noun and hands the viewer into the essay. Modelled on v03 @ 0:00–0:03 (icon swirl → clock → eye → push-through into the pupil → lighthouse) and v02 @ 0:00–0:03 (dots eaten → lone dot → emitters).

| t | Beat | Visual (pattern) | Caption (CS-B) | Camera | SFX cue allowed |
|---|---|---|---|---|---|
| **f0** | Stopper | **The opening object already on screen and moving**: a dim, drifting cluster of line icons around a dot (P-ICON-SWIRL, E4, ≤ 3 s; v03 f0 is a cluster, not an empty frame), or P-DOT-ROW-EATEN (flickering on after 2 black frames), or the thesis object itself breathing. Centre (540, 960), 40–55% width | — | C-3 drift (6–10 px/s) from f0 | `hook`: one soft cue on f0 (pad swell or low tone), optional |
| 0.13–0.27 | First words | The icons drift; the centre dots begin to gather | First chunk wipes in L → R over 4–5 f ("You weren't born") | drift | — |
| 0.2–0.5 | First transformation | The centre dots **snap into the thesis object** in 4 f (the clock gauge, v03 @ 0:00.20–0:00.30); at 0.47 its bloom swells over 2 f and wipes the icon field away | — | drift | `reveals`: soft cue on the landing |
| 0.67–1.0 | **Flare reveal** (≤ 1 per reel) | P-FLARE-BOWTIE: a horizontal slit opens into a bow-tie and a grey wash in 3 f, decays over 8 f and leaves the object transformed (the clock is now the pupil of an eye, v03 @ 0:00.67–0:01.0) | thesis chunk | — | `reveals`: one `shine`, optional |
| 1.0–1.7 | Thesis noun | The object gains its second part on the trigger word (the gear fades in behind at 35%, threads radiate) | "to work 40" | — | — |
| 1.7–2.43 | Hand-off | **T-PUSH-THROUGH**: the object contracts to ~0.65× over 12 f while the pupil-clock collapses to a dot, then the camera pushes ≥ 4× into it in 9 f (ease-in); a 2 f dissolve into dark (v03 @ 0:01.70–0:02.47). Or T-HANDOFF of the dot | "hours a week" | object scale, then C-4 | `transitions`: one soft `whoosh` on the push, optional |
| 2.47–3.0 | Payoff / clause 1 | The first clause object grows out of the dark: the ground ellipse widens over 3 f, the tower rises from 2.57 (v03) | next chunk | home | — |

**F-A default: HA-12 Thesis typography (text-only cold open).** Modelled on v01 @ 0:00–0:05.12.

| t | Beat | Visual | Caption | Camera | SFX cue allowed |
|---|---|---|---|---|---|
| **f0** | Stopper | W-card black; the first phrase of the thesis is already on f0 (no fade) in white EB Garamond 68 px at y 960; the card is pixel-still (v01 frame diff 0.000 between swaps); a z1 void ambient at zero glow (`extra: {continuous: true}`) only satisfies V-F0 and stays invisible | CS-A0 chunk 1 ("the fastest way") | none | `hook`: optional soft tone |
| 0.7–1.4 | Phrase 2 | Hard swap (0 f) to phrase 2; phrases hold 0.7–1.6 s, 5 phrases in 5.1 s | CS-A0 chunk 2 ("to change your life") | none | — |
| 1.5–3.5 | Phrase 3 | Phrase 3 holds while spoken (a longer phrase may hold 1.5–2 s) | CS-A0 chunk 3 ("is to rip yourself out") | none | — |
| 3.5–6.0 | Rest of the thesis | Further phrases until the first sentence ends (2–5 phrases in total) | CS-A0 | none | — |
| boundary (3.0–6.0) | **The one cut** | T-CARD-CUT to L-seated on the sentence-end word boundary; the creator is already mid-gesture, static framing | CS-A starts on the next word, gold, y 1372 | none (never) | `transitions`: none (the cut is silent) |

### 6.3 Allowed alternates `[DNA list; VAR choice per reel]`

**HA-12 in F-B: split title over the motif row** (v02 @ 0:00–0:01.5). Use when the thesis is a short imperative ("Turn your life into a game").

| t | Visual | Caption |
|---|---|---|
| f0–0.33 | 2 black frames, then P-SPLIT-TITLE and a row of 9 dots at y 960 **flicker on** together (T-FLICKER, 9 f) | captions hidden while the title is up |
| 0.67–1.33 | The chomper enters from the left edge and eats the dots at ~7–8 f per dot (≈ 4 dots per second) | — |
| 1.33–1.57 | The title and the uneaten dots flicker off (8 f); the last dot is left alone at (540, 960) | captions start |
| 1.57–2.5 | The lone dot is **held perfectly still** (≤ 0.9 s, the style's one static beat) | CS-B |
| 2.74 | The first clause object pops on around it within 2 f (three emitters, v02) and begins to orbit at ~0.43°/f | CS-B |

Examples: money & work: "YOUR SALARY / IS RENTED TIME", the dots are paydays eaten by the month; health & fitness: "YOU DON'T LACK / MOTIVATION", the dots are days eaten by skipped workouts.

**HA-14 in F-A: cold authority** (no card; open mid-sentence on the seated take). Use only when the creator's first line is already a striking claim and the buyer wants the face at f0 (the default f0 rule "no presenter" is lifted for this archetype only).

| t | Visual | Caption |
|---|---|---|
| f0 | L-seated, the creator mid-sentence, static | CS-A gold chunk on screen at f0 |
| 0–1.0 | The strongest line of the essay first | CS-A |
| 1.0+ | The essay continues; there is no card | CS-A |

Examples: money & work: "nobody gets rich from a salary" on frame 0; health & fitness: "you don't need more motivation" on frame 0.

### 6.4 Hook pairs by topic `[NICHE: example]` (pair type: thesis → scene promise)
| Niche | Topic | Thesis (spoken, ≤ 12 words) | Opening object (f0) | The object that carries it by 2.5 s |
|---|---|---|---|---|
| Money & work | Salary trap | "Your salary was designed to keep you exactly where you are" | P-DOT-ORBIT: the dot circling a large grey ring | The ring becomes a clock face; the dot is its second hand (P-CLOCK-SWEEP) |
| Money & work | Lifestyle creep | "Every raise you get, your lifestyle quietly eats" | P-DOT-ROW-EATEN: 9 dots (raises) | The chomper grows a little with every dot it eats |
| Money & work | Ownership | "You weren't born to rent your hours to someone else's dream" | P-ICON-SWIRL around the dot | P-EYE-CLOCK → push-through → P-BEAM-SWEEP (your own direction) |
| Money & work | Skill stacking | "One skill, sharpened for a year, beats ten you dabble in" | P-TOOL-STRIKE: the hammer idle above one nail | The nail sinks a little on each strike; ten faint nails beside it stay untouched |
| Health & fitness | Consistency | "You don't lack motivation. You lack a default." | The dot alone, breathing | P-LADDER-CLIMB: the dot climbs one step per spoken day |
| Health & fitness | Sleep | "You're not tired from work. You're tired from never switching off." | P-FEED-PHONE glowing in the dark | The phone dims; P-HOURGLASS-LOOP: the night's sand runs out |
| Health & fitness | Habits | "Your body is the sum of what you repeat" | P-DOT-FIELD: 12 × 9 days | A cluster of lit days drifts and settles into one bright block |
| Health & fitness | Environment | "Change your room before you try to change yourself" | P-DOOR-SPILL: a closed door outline | The door opens; light spills over the dot |

At P7 of each reel, write this pair for the reel's own topic and append it to this table (Part D.4).

### 6.5 Headline writing `[DNA formula; NICHE examples]`
The style has no banner; the "headline" is the **thesis sentence**, spoken first and captioned (F-B) or carded (F-A). P-SPLIT-TITLE uses a compressed version.
- **Formula:** `[a quiet universal claim about the viewer's life] + [the cost or the hidden mechanism]`, second person, present tense, ≤ 12 spoken words; the split title is the same claim in ≤ 8 words split 2–5 / 2–5.
- **Templates:** "You weren't born to ___." · "The fastest way to ___ is to ___." · "Your ___ is ___ in disguise." · "Life is a ___, but you aren't ___." · "Nobody ___ by ___." · "The reason you ___ is ___."
- **Case:** F-B captions sentence case; the F-A card and captions lowercase; the split title caps.
- **Banned:** hype words ("insane", "game-changer", "secret"), questions to the viewer ("Did you know…?"), numbers as the hook ("3 tips…"), emoji, exclamation marks, "POV:", "Stop scrolling".
- **Write 3 and pick by the stopper tests** (ST-1 the object, ST-2 the thesis captioned by 3.0 s).

### 6.6 Hook sound
The hook may carry one soft cue on f0 and one on the first push-through (§11). The music bed (an ambient pad) runs from f0, ducked ≥ 18 dB under the voice.

### 6.7 CTA `[DNA device set; VAR values]`
| Device | Spoken pattern | On screen | Hold | Where | Silence before |
|---|---|---|---|---|---|
| `product_card` (default when the creator has a product) | "My book / course ___ is out now", or no spoken CTA at all | P-PRODUCT-CARD (§25): the creator's cover image on an `ash` panel, rim light, the line "NOW AVAILABLE" (+ where) at y 230 | 2.5–4.0 s | end | none; it follows the last essay word after a 0.3–0.6 s breath |
| `comment_keyword` | "Comment {{BV-08.keyword|KEYWORD}} and I'll send you ___" | P-KEYWORD-CARD: "comment" (44 px, `mist`) above the keyword (88 px Montserrat 700, `primary` white); the dot sits under it and breathes | 1.5–4.0 s | end | 0.3 s |
| `link_bio` | "It's linked in my bio" | P-HANDLE-CARD: the "LINK IN BIO" line at y 230 + the handle {{BV-01.handle|@yourhandle}} + the dot | 2.0–3.0 s | end | 0.3 s |
| `none` | — | The reel ends on the last object (or the dot alone) dimming over 12 f after the last word; the hard end follows ≤ 6 f later | — | — | — |

Exactly one device per reel. No mid-reel CTA (`placement: end`).

---

## §7 Structure & cadence `[REQ] [DNA]`

### 7.1 Structure type: `essay` (both formats)
**claim → clauses → cost → turn → payoff, in one breath.** The essay is one continuous thought, never a list.

| Unit | Share of runtime | What it does | F-B light level |
|---|---|---|---|
| `THESIS` | 8–15% | The claim, the hook (§6.2) | `state` |
| `CLAUSE-1…n` (2–5 clauses) | 40–55% | Each clause adds one image of the problem or the mechanism ("you stop living the same day… you change the places you go… the books you read") | `state` |
| `COST` | 10–20% | What it costs to stay, or what the change will cost ("it's going to be difficult and uncomfortable") | `cost` (dim) |
| `TURN` | 8–15% | The insight, the way out ("but if you're able to stick with it…") | `turn` (light event) |
| `PAYOFF` | 5–10% | The closing line that completes the thesis ("…that is exactly how you change your life extremely fast") | `resolve` |
| `CTA` | 0–12% | §6.7 | `cta` |

### 7.2 Markers
`markers: none (spoken only)`. No numbers, chips, step badges or progress rails: the morph chain itself shows progress.

### 7.3 Unit ritual (every clause in F-B)
1. **Enter (12–24 f):** the clause object is born from the previous object (T-MORPH / T-PUSH-THROUGH / T-HANDOFF), landing 2 f before its trigger word.
2. **Act (1.5–4.0 s):** the object performs the mechanism with ≥ 1 internal event every ≤ 3.0 s (a strike, a sweep, a hop, a fill), and something drifts or breathes on every frame.
3. **Dot check:** the dot is present in its declared state (§23.2) or deliberately absent (≤ 40% of scenes).
4. **Hand off (12–24 f):** the object's shape, its centre or the dot becomes the next scene's starting point; the next caption chunk is already revealing.

F-A has no visual ritual: each caption chunk hard-swaps to the next over a still, locked-off take.

### 7.4 Open loops and re-hooks
- **The only loop is the thesis:** the payoff line completes or answers the first sentence, and in F-B the final object is the *lit* version of the opening object, or the dot as a source (P-DOT-SOURCE).
- **Re-hooks:** none (duration class `short`; a buyer may tune only to `micro` or `short`).
- **Intro cap:** the HA-15 thesis ≤ 15% of runtime; the F-A cold open ≤ 15% and ≤ 6.0 s.

### 7.5 Rhythm and energy curve
Energy stays **calm and flat**; the curve is a **light curve**: a steady glow through the clauses → dimmest at COST (outlines `smoke`, glow ≤ 8 px, a slow pull-out) → the brightest event of the reel at TURN (the dot becomes a source, a beam opens, P-FLARE-BOWTIE at most once) → everything that stays fully lit at PAYOFF → the quiet end card. No comedy beats.

### 7.6 Cadence (state changes)
| Token | F-B | F-A | Why |
|---|---|---|---|
| `sc_per_10s` | **3–9** | **1.5–4** | F-B: ~4–5 weighted caption swaps (0.5 each, ~1 chunk per second, v03) + 1–2 scene entries + 1–2 object events per 10 s. F-A: a caption chunk every 1.2–2.0 s at weight 0.5 (v01) |
| `hook_sc_3s` | **3** | **1.0** | v02 hook ≈ 3 (chomper, lone dot, emitters); v03 hook ≈ 8 (swirl, clock, flare, eye, gear, push-through, lighthouse). The floor is v02 |
| `max_gap_s` (weight ≥ 1) | **3.0** (hook 2.0) | **none** | F-B: an object event or a morph at least every 3 s (v02 scenes last ~4.5 s but carry internal events every 1–2 s). F-A: a locked-off take with captions only is the DNA (v01: one cut, zero zooms in 38 s) |
| `max_static_s` | **0** | **2.5** | F-B motion never stops: the W-void ambient (marked continuous) runs under every frame, plus drifting objects. F-A: the live take is continuous motion |
| `caption_weight` | 0.5 | 0.5 | support captions |
| cuts per minute | 0 (no cuts) | ≤ 2 (the one card cut + an optional end-card fade) | evidence 0 / 0 / 1.6 |
| `continuous_motion_required` | true | false | |

Scenes per 60 s (F-B): 12–24 (v02 ≈ 12, v03 ≈ 19). Morph or push-through boundaries per 60 s: 12–24.

Measured pacing (every frame): F-B scene length median ~4 s (v03 2.4 s, v02 5.9 s), p90 ~8.5 s, shortest 0.75 s (hook beats); a long scene (the 8.8 s spotlight, v03 @ 0:11.8–0:20.6) carries an internal event every 1–2 s (wedge sweeps, a cluster lit, an X drawn). Pixels change on 89% of v03 frames and 49% of v02 frames: v03 is the busier model, v02 the slower one; both are valid. F-A: one cut in 38 s, a caption swap every 1.2–2.0 s, the card still for up to 1.6 s.

---

## §8 Visual system `[REQ]`

### 8.1 Graphics role and budget
- **F-B `graphics: primary`:** 100% of runtime is engine-built graphics on W-void. 45 named patterns below; 8–14 distinct patterns and 4–6 families per 60 s.
- **F-A `graphics: minimal`:** 3 recurring devices only: the cold-open card (P-COLD-OPEN), the gold captions over the static take (P-SEATED-HOLD) and the end card (§25). ≤ 15% of runtime is non-caption graphics.
- **Numbers become pictures, quietly:** a spoken quantity becomes a countable set of objects (40 hours → 40 tick marks on a clock rim; 9 days → 9 dots), never a figure card.

### 8.2 Families
| ID | Family | Source class | Engine blocks | Buyer supplies |
|---|---|---|---|---|
| **B-1** | **The motif** (the dot and its states) | engine | `VEOS.fx.morphShape` (kind `dot` / `circle` / `ring`), `fx.handoff` | nothing |
| **B-2** | **Line-art metaphor objects** (3 px white/mist outlines with glow) | engine | `VEOS.fx.icon(name, {size, color, stroke, glow})` for clock, eye, gear, hourglass, infinity, phone, globe, users, user, target, doc, laptop, lock, key; bespoke SVG paths (recipes below) for hammer, nail, megaphone, chomper, ladder, balance, door, chain, tree, maze, road | nothing |
| **B-3** | **Light machines** (beams, cones, wedges, flares, spirals) | engine | `ctx.canvas()` wedges with `createRadialGradient` / `createConicGradient`, or CSS `conic-gradient`; at most one `filter: blur(6–10px)` layer | nothing |
| **B-4** | **Lit 3D objects** (tower, globe, sphere) | engine | `VEOS.fx.three` (tokens `three`): greyscale materials, a white rim light from the right, a shadow-only ground, a white `glow` halo for the bloom. The look is "frosted grey sculpture". **One 3D scene on screen at a time** (45–150 ms per frame); its `box` sized to the object | nothing |
| **B-5** | **Fields** (dot grid, icon swirl, grains, crowd dots) | engine | `ctx.canvas()` with `ctx.rng` seeds; E4 when it is ambient texture | nothing |
| **B-6** | **Generic device and bar** (phone outline with grey cards, progress bar, screen) | engine | `VEOS.fx.device("phone", …)` restyled in greys; rect morphs via `fx.morphShape` | nothing |
| **B-7** | **Quiet type objects** (split title, in-object word) | engine | `VEOS.fx.typeStack({maxLines: 1})` with the `display` slot, or a bespoke scene | nothing |
| **B-8** | **End cards** (product, keyword, handle) | engine + **buyer-owned** (the product cover, an optional wordmark) | bespoke scene + `ctx.asset("cover")` | the product cover PNG/JPG (≥ 1000 px tall) for `product_card` |
| **B-9** | **Created substitutes** for third-party moments (§12.5) | engine (created) or creator-supplied third-party | `VEOS.fx.quoteCard`, `fx.logoPlate`, `fx.appUI` with `theme: "dark"`, recoloured to greys | the creator's own screenshot or clip, if they have one |
| **B-10** | **The seated take** (F-A) | buyer-owned | stage `full` | one seated take (§12.1) |

### 8.3 Pattern specs
Frames at 30 fps. "Object zone" = x 96–984, y 330–1330, centre (540, 960). All line art: stroke 3 px `mist` (rest) or `primary` (active), `drop-shadow(0 0 12px rgba(255,255,255,.45))`; the cores of active parts are `primary` with a 24 px glow. Every pattern enters by the transition named in its beat's `morph_in` (§9) unless it says otherwise. Every F-B scene sets `extra: {morph_in, morph_out, motif_state}` so the beat sheet, the storyboard and the future V-CONTINUITY can read the chain.

**A. The motif (B-1)**

| ID | Name | Type | On screen | Motion recipe (30 fps) | Use | Class / needs |
|---|---|---|---|---|---|---|
| **P-DOT-SELF** | The dot alone | stage | The motif: a white disc Ø 40 at (540, 960), glow 24 px, on W-void | Breathes scale 1.00 ↔ 1.04 over 90 f (sine); drifts ≤ 8 px/s; any move to a new position eases over ≥ 18 f | "you", a pause, the reset between ideas, the opening and the ending | no text · motif `idle` |
| **P-DOT-ROW-EATEN** | Row consumed | overlay | 9 dots Ø 30–43, pitch 118 px, a row at y 960 from x 68 to 1012; a chomper (a white wedge disc Ø 70 whose mouth opens and closes every 5 f) | The chomper enters from x −60 at 0.67 s and moves 118 px per 7–8 f (≈ 15 px/f, one dot per ~7.7 f); each eaten dot shrinks 1 → 0 in 3 f; after 5–6 dots the rest flicker off with the title and the last dot is left as the motif (v02 @ 0:00.67–0:01.57) | days, paydays, chances being consumed; time eaten by something | no text · events per dot · motif: the survivor |
| **P-DOT-GROW** | Pressure builds | state | The dot grows Ø 40 → 120 → 216 as forces converge on it | Two growth steps, each 18 f ease-in-out, on two trigger words; glow 24 → 40 px; at Ø 216 it is a flat white disc (v02 @ 0:07–0:09) | attention, pressure, obsession, a problem getting bigger | events per step · motif `grown` |
| **P-DOT-DIM** | The cost | state | The dot loses its glow and turns `bad` grey #6E6E6E; the surrounding outlines drop to `smoke` | A 24 f ease-in-out fade of glow 24 → 0 and white → grey; C-2 pull-out 1.00 → 0.85 over 36 f | regret, waking up late, the price of staying | motif `dim` · tone `cost` |
| **P-DOT-SOURCE** | The turn | state | The dot becomes a light source: white core, glow 90 px, 6–8 soft rays (1 px lines, alpha .3, 200–420 px long) turning 0.3°/f | Glow 24 → 90 px over 18 f on the trigger word; the rays fade in over 12 f; optional C-1 push 1.0 → 1.2 over 24 f | the insight, the decision, "but…", becoming the person who… | motif `source` · tone `turn` |
| **P-DOT-SEED** | Planted | state | The dot falls (Ø 40 → 30) from y 700 to a ground line at y 1180 (1 px `smoke`, x 240–840); a 2 px shoot grows up from it | Fall 15 f ease-in, a 3 f settle (no squash); the shoot grows 0 → 260 px over 30 f | starting small, a first step, a habit begun | motif `seed` |
| **P-DOT-AMONG** | One of many | overlay | 60–90 grey dots (`grid` #3A3A3A, Ø 14–20) drifting left → right across the object zone; the motif is the only lit dot | The crowd drifts 10 px/s; on the trigger word the motif stops (the others keep moving) or moves against the flow | standing out, not following the crowd, the default path | one element, no text · motif `idle` |
| **P-DOT-ORBIT** | Routine gravity | overlay | A large `smoke` ring (Ø 560, 2 px) centred; the dot orbits on it | One revolution per 3 s with a trail of 6 fading copies (alpha .3 → 0); on "break free" the dot leaves on a tangent over 24 f | routines, loops, being kept in place, comfort zones | event on escape · motif `idle` |

**B. Line-art metaphor objects (B-2)**

| ID | Name | Type | On screen | Motion recipe (30 fps) | Use | Class / needs |
|---|---|---|---|---|---|---|
| **P-TOOL-STRIKE** | One tool, one point | overlay | A bespoke hammer (head 120 × 44, handle 18 × 200) above a nail (head Ø 34, shaft 140 px) at (560, 1040); ~180 px tall, deliberately small (v02 @ 0:10–0:15) | Enters by T-FLICKER-SWAP from the grown dot, which shrinks into the nail head (v02 @ 0:09.53–0:09.77). Idle sway ±6° over 60 f; a strike rotates −40° → +10° in 6 f (ease-in); the nail sinks 12 px per strike; a 1-frame white tick at contact (no flash); 1 strike per trigger word. Exit: the hammer vanishes and the nail head falls as the dot (v02 @ 0:16.0–0:17.2) | focus, one skill, deliberate effort, "do one thing" | events per strike |
| **P-EMITTERS-CONVERGE** | Many voices | overlay | 3 outline megaphones (60 × 60) on a Ø 520 circle around the dot; each emits 4–8 concentric arcs (1 px `smoke`, 30° spread) toward the dot | The megaphones appear together within 2 f (v02 @ 0:02.74) and the whole group orbits the dot at 0.43°/f (13°/s, measured), drifting slightly inward (scale 1 → 0.9 over 2 s, v02 @ 0:05–0:07); arcs are emitted every 8 f, travel 4 px/f and tighten; the dot answers with P-DOT-GROW (v02 @ 0:03–0:09.5) | noise, other people's opinions, ads, demands on your attention | events per growth step |
| **P-EYE-CLOCK** | Attention for time | overlay | `fx.icon("eye")` 420 px wide whose pupil is `fx.icon("clock")` (Ø 120, hands turning); 20–30 curved threads (1 px, alpha .25) radiating from the eye; `fx.icon("gear")` Ø 560 behind at 35% opacity | Minute hand 6°/f; the threads drift (seeded sine, ±12 px); the gear fades in over 12 f on its word and turns 1°/f; one blink (scaleY 1 → 0.1 → 1, 8 f) on the trigger (v03 @ 0:00.67–0:01.67) | selling your time, jobs, being watched, the attention economy | events: gear in, blink |
| **P-HOURGLASS-LOOP** | Time running | overlay | `fx.icon("hourglass")` or `fx.icon("infinity")` as a 300 × 460 outline; 120–200 seeded grains (Ø 2–3, white) falling through the neck; the bulbs filled with the `lit_sphere` grey gradient (2D, inside the line-art icon) | Grains fall 6 px/f with seeded jitter; the top bulb's level drops on the trigger over 30 f; an optional 180° turn over 24 f to "start again" (v03 @ 0:07–0:10) | time running out, repetition, "where did the time go" | event on the turn |
| **P-CLOCK-SWEEP** | Hours pass | overlay | A clock face Ø 600 (2 px `mist` rim; N tick marks where N is the spoken quantity, else 12), hands `primary` | The hands sweep fast (minute hand 18°/f) during the clause and slow to a stop over 18 f on the last word | hours, years, deadlines, "every day the same" | event on stop |
| **P-LADDER-CLIMB** | Step by step | overlay | A bespoke stair outline (5–9 steps, 80 px rise, 120 px run) rising left → right; the dot on the first step | The dot hops one step per trigger (arc 14 f, ease-in-out, no bounce); passed steps brighten `mist` → `primary` | progress, consistency, levelling up | events per hop · motif `idle` |
| **P-SCALE-TIP** | Trade-off | overlay | A bespoke balance: beam 560 px, two pans; the left pan holds the dot, the right a small object (a coin, phone or clock icon at 80 px) | The beam tips ±8° over 24 f ease-in-out on the trigger and settles with no overshoot | cost vs benefit, comfort vs growth, choices | event on tip |
| **P-DOOR-SPILL** | Opportunity | overlay | A door outline 280 × 520 at (540, 900); light behind it (a `beam` trapezoid) | The door leaf opens (perspective skew 0 → 70°, 24 f); the light spills as a trapezoid over the floor line and onto the dot, opacity 0 → .28 over 18 f | a new chance, leaving, beginning | event on open |
| **P-CHAIN-BREAK** | Breaking free | overlay | 5 chain links (ellipses 90 × 52) in a horizontal line through the dot | The middle link cracks (a 1 px gap opens) and the halves drift 40 px apart over 18 f; the dot rises 120 px over 24 f | quitting a habit, freedom, leaving a job | event on break |
| **P-MAZE-THREAD** | Clarity | overlay | A square maze 640 × 640 (2 px `smoke` walls, 8 × 8 cells, seeded); the dot at the entrance | On the trigger a 3 px white path draws through the maze over 30–45 f (stroke-dashoffset); the walls dim to 40% | confusion → clarity, finding your path | events: path start and end |
| **P-ROAD-VANISH** | The long game | overlay | A perspective road (two 2 px lines converging to (540, 620)) with a dashed centre line; the dot on the road | The dashes stream toward the viewer at 6 px/f; the dot travels toward the vanishing point, shrinking Ø 40 → 12 over the clause | the long term, patience, the journey | continuous |
| **P-WAVE-SETTLE** | Noise to signal | overlay | 5 overlapping sine waves (1–2 px, `smoke`) across x 120–960, amplitude 60–140 px | On the trigger all the waves damp into one flat white line over 30 f; the dot rides the line | focus, calm, cutting the noise | event on settle |
| **P-SEED-TREE** | Compounding | overlay | From P-DOT-SEED's shoot a line tree grows: 3 levels of branches (2 px), 8–16 tiny white leaf dots | Each level grows over 24 f on successive trigger words; the leaves appear by opacity only (no scale overshoot) | compounding, growth, patience paying off | events per level |
| **P-MIRROR-HORIZON** | Who you could be | overlay | A horizon line (1 px `smoke`) at y 1060; the dot above it, its reflection below at 40% opacity | On the trigger the reflection changes (grows a glow ring, or moves ahead) over 24 f | identity, potential, the gap between you and who you could be | event |
| **P-PICTOGRAM-TRIAD** | The options | overlay | 3 outline pictogram clusters (people at a desk, a lifter, a reader; built from `fx.icon("users")`, `"user"`, `"doc"`, `"laptop"` at 90–120 px) on an arc 300–400 px from the dot | They fade in staggered by 8 f and bob ±4 px; used with P-SPIRAL-SPOTLIGHT and P-STRIKE-X (v03 @ 0:12–0:20) | the paths people take, distractions, what everyone else does | events |

**C. Light machines (B-3)**

| ID | Name | Type | On screen | Motion recipe (30 fps) | Use | Class / needs |
|---|---|---|---|---|---|---|
| **P-BEAM-SWEEP** | Direction | overlay | P-LIT-TOWER (3D) on its ground disc; a conic beam (`beam` gradient, 26° spread, 900 px long, alpha .28 → 0) from the lamp, a 2D canvas scene one z above the tower | The ground ellipse widens over 3 f, the tower rises from it over 18 f (v03 @ 0:02.47–0:03.1); the lamp brightens over 12 f; the beam sweeps −35° → +35° over 3–6 s (sine), camera still. **Exit (T-SINK):** the beam swings toward the lens into a soft wash (4 f), switches off in 1 f, the tower sinks into the ground over 8 f, the ground flattens and fades over 4 f, and the lamp's light is left as the dot (v03 @ 0:06.12–0:06.72) | purpose, direction, guidance, being seen | events: rise, lamp on, sink |
| **P-SPIRAL-SPOTLIGHT** | Choosing | overlay | A spiral vortex (40–60 short 2 px arcs on log-spiral paths, `smoke`) around a bright dot (glow 60 px); a lit wedge (40°, alpha .25) from the dot reveals P-PICTOGRAM-TRIAD | The vortex turns 0.6°/f; the wedge sweeps 180° → 0° over 2–4 s, lighting one cluster at a time (v03 @ 0:12–0:20) | looking at your options, what you give your attention to | events per cluster lit |
| **P-FLARE-BOWTIE** | The light burst | overlay | Two opposed soft light wedges (a bow-tie) from the object's centre, covering ≤ 50% of the frame, peak alpha .55 | A **reveal**: a thin horizontal slit of light opens from the object (f1), widens into the bow-tie (f2), floods to a grey wash (f3, frame mean luma ≤ 40%), then decays over 8 f to show the object already transformed (v03 @ 0:00.67–0:01.0). **Max 1 per reel** | the moment of insight; the thesis landing on its key word; the hook's first transformation | event · tone `turn` |
| **P-STRIKE-X** | Rejected | annotation | 2 px `smoke` X marks (60 px) over rejected objects; those objects dim to 35% | Each X draws in 8 f (two strokes of 4 f), staggered by 4 f (v03 @ 0:19–0:20) | "it's not…", rejecting the default, ignoring the crowd | events per X |
| **P-ZOOM-OUT-ROLL** | The bigger picture | overlay (scene self-transform) | The current object sits inside a thin 2 px `mist` frame (a rotated square) that is first larger than the screen; a ring of large arcs (2 px, small white nodes on them) lies beyond it; a comet (the dot with a 60–120 px motion streak) crosses the frame | On the trigger word the whole scene scales ~3× → 1× and rolls ~50° (−5° → +45°) over ~20 f, ease-out, so the old object becomes a small part of a larger tiled pattern; the comet settles into the centre as the dot (v03 @ 0:09.97–0:10.67, on "zoom out"). Drawn as the scene's own scale + rotate at the measured values: the canvas camera's `roll` stops at 20° and 2° per frame, this roll is 50° at up to ≈ 4.6° per frame | literally "zoom out", "the bigger picture", "step back", perspective | event on the trigger · ≤ 1 per reel |

**D. Lit 3D objects (B-4, `VEOS.fx.three`).** Each is one `fx.three` scene (recipes below the table) in frosted greys: a soft key from the upper left, a white rim light from the right, no fill (the dark side falls to black like the void), a white `glow` halo as the bloom. One 3D scene on screen at a time; hand-offs to and from a lit object overlap only with 2D scenes.

| ID | Name | Type | On screen | Motion recipe (30 fps) | Use | Class / needs |
|---|---|---|---|---|---|---|
| **P-LIT-TOWER** | Tower | overlay | A lit 3D lighthouse: a tapered grey column (≈ 120 px wide at the top, 180 px at the base, 420 px tall on screen), a lamp cap with a white emissive core and halo, on a dark ground disc (≈ 640 × 90 px as seen) that takes its shadow; white rim light on the right edge | Grows out of the ground over 18 f (scale y 0 → 1, expoOut) after the disc widens over 3 f (v03 @ 0:02.47–0:03.1); the lamp's halo brightens over 12 f; the camera stays still. **Sink:** scale y 1 → 0 over 8 f, the disc flattens over 4 f | a lighthouse (direction), a monument, a goal to reach | `fx.three` · used by P-BEAM-SWEEP |
| **P-GLOBE-TURN** | The world | overlay | A lit 3D globe Ø 400 px: the procedural graticule (white lines on a dark grey sea, no land dots: there is no geo bundle), keyed from the upper left so the right side falls into a terminator, a `mist` atmosphere and a 30 px-scale white halo | Turns at 18°/s (0.6°/f, `spin: 18`) with a 20° tilt (v02 @ 0:42–0:49) | the world, everyone, scale, "out there" | `fx.three` |
| **P-LIT-SPHERE** | Ball | overlay | A lit 3D sphere Ø 120–200 px, light grey, rim-lit | Rises from below a horizon or a screen edge over 24 f (v02 @ 0:41), or rolls along a line (`keys` on `pos` + `rot`) | the dot made solid: the self with weight; a goal; momentum | `fx.three` · the motif may morph into it (hand off on the frame the sphere is born: the 2D dot fades over 4 f as the sphere scales in) |

```js
// B-4 lit objects (VEOS.fx.three). Colours are greyscale hex (tokens `three`); one 3D scene on screen at a time.
const LIT = { key: { color: "#FFFFFF", intensity: 1.6, pos: [-4, 5, 5] }, rim: { color: "#FFFFFF", intensity: 4.5, pos: [6, 2.5, -1.5] }, fill: false };
// P-LIT-TOWER: rises 18 f from its ground disc; sinks over the scene's last 8 f (T-SINK)
function litTower(id, t_in, t_out) { const d = t_out - t_in;
  VEOS.fx.three({ id, t_in, t_out, z: 3, box: { x: 240, y: 520, w: 600, h: 900 }, lights: LIT, ground: { y: 0, size: 4, shadow: 0.35 },
    camera: { fov: 30, pos: [0, 2.2, 15], target: [0, 2.1, 0] }, events: [0, 0.1, d - 0.27],
    objects: [
      { kind: "cylinder", radius: 2.9, height: 0.04, color: "#141414", metal: 0, rough: 0.9, shadow: false, receive: true,
        keys: [{ at: 0, scale: [0.2, 1, 0.2] }, { at: 0.1, scale: 1, ease: "out" }, { at: d - 0.13, scale: 1 }, { at: d, scale: [1, 0, 1] }] },
      { kind: "cylinder", radius: 0.82, radius_top: 0.55, height: 3.8, color: "#BDBDBD", metal: 0.1, rough: 0.55,
        keys: [{ at: 0.1, scale: [1, 0, 1] }, { at: 0.7, scale: 1, ease: "expoOut" }, { at: d - 0.27, scale: 1 }, { at: d, scale: [1, 0, 1], ease: "in" }] },
      { kind: "sphere", radius: 0.32, pos: [0, 4.05, 0], color: "#FFFFFF", emissive: "paper", emissive_k: 1.2,
        glow: { color: "paper", size: 2.2, strength: 0.45 },
        keys: [{ at: 0.6, opacity: 0 }, { at: 1.0, opacity: 1 }, { at: d - 0.3, opacity: 1 }, { at: d - 0.17, opacity: 0 }] }] }); }
// P-GLOBE-TURN: 18 deg/s, upper-left key, terminator on the right, no land dots
function litGlobe(id, t_in, t_out) {
  VEOS.fx.three({ id, t_in, t_out, z: 3, box: { x: 240, y: 660, w: 600, h: 600 }, lights: LIT, camera: { fov: 30, pos: [0, 0, 7.5] },
    objects: [{ kind: "globe", radius: 1.35, rot: [20, 0, -12], spin: 18, sea: "#2A2A2A", line: "#E9E9E9", land: false,
      atmosphere: "mist", glow: { color: "paper", size: 3.6, strength: 0.3 } }] }); }
// P-LIT-SPHERE: rises 24 f from below its rest
function litSphere(id, t_in, t_out, x, y, d /* px diameter */) { const b = d * 2.2;
  VEOS.fx.three({ id, t_in, t_out, z: 3, box: { x: x - b / 2, y: y - b / 2, w: b, h: b }, lights: LIT, camera: { fov: 30, pos: [0, 0, 6] },
    objects: [{ kind: "sphere", radius: 0.7, color: "#CFCFCF", rough: 0.5, glow: { color: "paper", size: 2.4, strength: 0.25 },
      keys: [{ at: 0, pos: [0, -2.4, 0] }, { at: 0.8, pos: [0, 0, 0], ease: "out" }] }] }); }
```
(The tower camera at z 15 renders the column ≈ 420 px tall on screen as measured (z 11 gave ≈ 630 px), base at y ≈ 1180; the rim light sits to the right and slightly behind (x 6, z −1.5, intensity 4.5) so the right edge of the column and the lamp cap read as the measured bright rim; the ground disc is the only "ground ellipse" now.)

**E. Fields (B-5)**

| ID | Name | Type | On screen | Motion recipe (30 fps) | Use | Class / needs |
|---|---|---|---|---|---|---|
| **P-DOT-FIELD** | Life as a grid | overlay | A 12 × 9 field of dots (pitch 52 px, Ø 6, `grid` grey) spanning 612 × 440 px around (540, 960) | The field fades in over 12 f; a cluster of 4–9 dots lights white (Ø 10, glow 12) on the trigger and drifts 2–3 cells over 60 f; an optional zoom-out of the field 1.0 → 0.8 (v02 @ 0:26–0:33). N lit dots = a spoken count when there is one | days, options, people, a life seen as units | events per cluster |
| **P-ICON-SWIRL** | The world's pulls | overlay (E4) | 12–20 line icons (`fx.icon`: phone, chat, play, globe, heart, mail, camera, bolt, coin, users) at 60–90 px, `smoke`, on a spiral around the dot | They spiral inward: radius 520 → 140 px over ≤ 3.0 s at 1.2°/f, opacity .6 → 0 at the end as they condense into the next object (v03 @ 0:00–0:00.5) | modern distraction, too many inputs, "everything wants your attention" | **E4**: z2, `ambient: true`, items marked `data-item`, no text, dimmed near the captions |

**F. Generic device and bar (B-6)**

| ID | Name | Type | On screen | Motion recipe (30 fps) | Use | Class / needs |
|---|---|---|---|---|---|---|
| **P-FEED-PHONE** | The feed | overlay | A generic phone outline 450 × 846 (radius 44, 3 px `mist`, notch), centred; inside, 6–8 grey cards (`slate`, radius 14, 360 × 92, gap 14) scrolling; the dot hops between cards; an optional lock-screen bar at the top (digits only if the script says a time) | Rises in from below as the falling dot lands on it (v02 @ 0:17.3–0:17.6). The cards scroll up 4 px/f with a slow ease every 30 f; the dot hops card to card (arc 10 f) on each trigger; at most one card carries an in-object word (P-OBJECT-WORD) (v02 @ 0:18–0:25). Exit: T-FLICKER off (v02 @ 0:25.8) | scrolling, distraction, comparison, social media, notifications | events per hop |
| **P-BAR-TO-SCREEN** | Progress → the bigger picture | overlay | A progress bar 864 × 80 (2 px `mist` outline, white fill) at y 960 | Flickers on (T-FLICKER). The fill rises over ~0.9 s, **snaps back to empty in 1 f**, and refills, once per spoken level (3 fills, v02 @ 0:33.0–0:36.1); then the bar grows into an 864 × 432 screen (T-MORPH **48 f**, ease-in-out, fastest mid-way, v02 @ 0:36.2–0:37.8) whose interior fills grey, then white; a P-LIT-SPHERE rises from its lower edge (v02 @ 0:41). Exit: T-CRT-OFF | progress, levels, "almost there", leaving one stage for the next | events per step |

**G. Quiet type objects and the seated take (B-7, B-10)**

| ID | Name | Type | On screen | Motion recipe (30 fps) | Use | Class / needs |
|---|---|---|---|---|---|---|
| **P-SPLIT-TITLE** | Split title | overlay (headline `title_card`) | §5.2 | §5.2 | HA-12 in F-B only | TC-display 50 px · `kind: "title_card"` |
| **P-OBJECT-WORD** | A word inside an object | overlay | One 1–2-word caps label inside an object (a feed card showing the spoken word) | Fades in over 6 f and holds ≥ 1.0 s; ≤ 1 per reel | when the VO quotes a short phrase the object "displays" | TC-label 40 px, `redundant: true` |
| **P-COLD-OPEN** | Text-only card (F-A) | stage | W-card black; CS-A0 captions at y 960 | The captions fade-swap over 3 f per phrase; the card lasts 3.0–6.0 s and ends on T-CARD-CUT | every F-A reel | captions only |
| **P-SEATED-HOLD** | The still take (F-A) | footage-treatment | L-seated full frame, no zoom, CS-A gold captions on the chest | None: the creator's hands and face are the motion | every F-A body beat | — |

**H. End cards (B-8)**, specified in §25

| ID | Name | Type | On screen | Motion recipe (30 fps) | Use | Class / needs |
|---|---|---|---|---|---|---|
| **P-PRODUCT-CARD** | Product | overlay | The line at y 230; the creator's cover image x 220–860, y 360–1320 on an `ash` panel with a soft white rim glow (16 px, alpha .35); two soft light streaks behind it (alpha .15) | Enters by T-COLLAPSE-DOT: the cover un-warps (shipped: scale 1.25 → 1, blur 14 → 0 px, opacity 0 → 1) over 10 f on the dot's centre; ~0.8 s later the line's letters flicker on in random order over 30–36 f; the streaks drift 2 px/f; camera still | `product_card` CTA | TC-label line · asset: creator |
| **P-KEYWORD-CARD** | Keyword | overlay | "comment" (44 px `mist`, y 780) + the KEYWORD (88 px `primary` white, y 900) + the dot under it at y 1080 | The words blur in over 10 f, the keyword 4 f later; the dot breathes | `comment_keyword` CTA | TC-label + TC-display · `kind: "cta-keyword"` |
| **P-HANDLE-CARD** | Handle | overlay | The "LINK IN BIO" line at y 230 + the handle at y 1430 + the dot at (540, 960) | The line reveals over 12 f; the handle fades in over 8 f | `link_bio` CTA | TC-label + TC-legal |

**I. Created substitutes (B-9)**, the §12.5 flow

| ID | Name | Type | On screen | Motion recipe (30 fps) | Use | Class / needs |
|---|---|---|---|---|---|---|
| **P-QUIET-QUOTE** | Quote, created | overlay | `fx.quoteCard({theme: "dark", …})` in greys: an `ash` card 880 wide, `mist` text 54 px, no avatar colours | Built-in rise + de-blur over 10 f; word reveal at 9 words per second | a post or a quote the VO reads out | insert record · TC-label |
| **P-QUIET-PLATE** | Name plate, created | overlay | `fx.logoPlate({…})` in greys: the product or company name in Montserrat 700 caps on `ash`, no logo | 10 f in | a named product, company or book that isn't the creator's | insert record |
| **P-QUIET-SCREEN** | Generic screen, created | overlay | `fx.appUI({kind: "list" \| "video", theme: "dark"})` in greys only | 10 f in | an app screen, or another creator's clip mentioned in the VO | insert record |

**Bespoke SVG recipes** (draw once as top-level helpers in `scenes.js`; coordinates relative to the object's centre; 4 px stroke (measured ≈ 4 px core + ~20 px bloom on the v02 megaphones), round caps and joins):
- *Hammer:* head = rounded rect (−60, −22, 120, 44, r 8); handle = rect (−9, 22, 18, 200, r 9); the pivot at the handle's bottom end.
- *Nail:* head = ellipse rx 17, ry 5; shaft = line (0, 0) → (0, 140) with a 10 px taper.
- *Megaphone:* a trapezoid (narrow end 18 px, wide end 54 px, length 56 px) + a 10 px handle; arcs = `A` paths of radius 30 + 14k, 30° spread.
- *Chomper:* a disc Ø 70 with a wedge cut of half-angle 30° × |sin(π·n/5)| (opens and closes every 5 f).
- *Ladder:* a polyline of steps. *Balance:* a triangle base 80, a beam line 560, pans = arcs r 70. *Door:* rect 280 × 520 + a leaf quad skewed by perspective. *Chain link:* ellipse rx 45, ry 26. *Maze:* a seeded recursive backtracker on 8 × 8. *Tree:* recursive branches at ±28°, length × 0.7 per level.

### 8.4 Line → pattern lookup `[NICHE]`
Classify every sentence at P5. The universal line types come first; the two example niches show how a topic maps.

| Line type | Primary | Alternates | Money & work `[NICHE: example]` | Health & fitness `[NICHE: example]` |
|---|---|---|---|---|
| L-01 "you" / the viewer / one person | P-DOT-SELF | P-DOT-AMONG | "you're one of millions with a 9-to-5" | "you, alone, at 6 am" |
| L-02 Days repeating / time consumed | P-DOT-ROW-EATEN | P-CLOCK-SWEEP, P-HOURGLASS-LOOP | "paycheck to paycheck" | "another Monday you'll start" |
| L-03 Many forces pulling | P-EMITTERS-CONVERGE | P-ICON-SWIRL | "everyone has advice about your money" | "every influencer has a new diet" |
| L-04 Distraction / the feed | P-FEED-PHONE | P-ICON-SWIRL | "scrolling other people's wins" | "scrolling instead of sleeping" |
| L-05 Trading time or attention for money | P-EYE-CLOCK | P-CLOCK-SWEEP | "renting out your hours" | "trading sleep for screen time" |
| L-06 One tool / one skill / focus | P-TOOL-STRIKE | P-WAVE-SETTLE | "one high-income skill" | "one lift, done well" |
| L-07 Loops / routines / comfort zone | P-DOT-ORBIT | P-HOURGLASS-LOOP | "the same job, a new year" | "the same routine that stopped working" |
| L-08 Life as units / options | P-DOT-FIELD | P-PICTOGRAM-TRIAD | "4,000 weeks" (lit dots stand for the count; the number stays in the caption) | "365 chances to move" |
| L-09 Progress / levels | P-BAR-TO-SCREEN | P-LADDER-CLIMB | "your savings growing" | "a little stronger each week" |
| L-10 Purpose / direction | P-BEAM-SWEEP | P-ROAD-VANISH | "knowing what you're building toward" | "training for something, not just training" |
| L-11 Choosing / attention on options | P-SPIRAL-SPOTLIGHT | P-PICTOGRAM-TRIAD | "what you spend your evenings on" | "what you choose to eat" |
| L-12 Rejecting the default | P-STRIKE-X | P-DOT-AMONG | "it's not another course" | "it's not another program" |
| L-13 Trade-off / cost vs benefit | P-SCALE-TIP | P-DOT-DIM | "comfort now, freedom later" | "pleasure now, pain later" |
| L-14 Opportunity / a beginning | P-DOOR-SPILL | P-DOT-SOURCE | "the side project you keep postponing" | "the first workout" |
| L-15 Breaking free / quitting | P-CHAIN-BREAK | P-DOT-ORBIT (escape) | "leaving the job" | "quitting sugar" |
| L-16 Confusion → clarity | P-MAZE-THREAD | P-WAVE-SETTLE | "a plan for your money" | "a simple plan" |
| L-17 Compounding / the long game | P-SEED-TREE | P-ROAD-VANISH | "compound interest" | "small habits compounding" |
| L-18 Identity / who you could be | P-MIRROR-HORIZON | P-DOT-SOURCE | "the person who owns their time" | "the person who trains by default" |
| L-19 Standing out / the crowd | P-DOT-AMONG | P-STRIKE-X | "everyone takes the safe job" | "everyone quits in February" |
| L-20 Pressure building | P-DOT-GROW | P-EMITTERS-CONVERGE | "the bills piling up" | "stress building up" |
| L-21 The cost / regret | P-DOT-DIM | P-HOURGLASS-LOOP | "waking up at 50 wondering" | "waking up tired every day" |
| L-22 The insight / the turn | P-DOT-SOURCE | P-FLARE-BOWTIE (≤ 1 per reel) | "but here's the thing" | "but if you stick with it" |
| L-23 The world / scale | P-GLOBE-TURN | P-DOT-AMONG | "the internet pays for leverage" | "everyone on earth ages" |
| L-24 A quoted post, person or headline | P-QUIET-QUOTE (created) or the creator's file | — | "a CEO once said…" | "a study said…" (quoted words only; no invented numbers) |
| L-25 A named product, app or company | P-QUIET-PLATE or P-QUIET-SCREEN | — | "your banking app" | "a fitness tracker" |
| L-26 A spoken number | the countable version of the line's object (N ticks, N dots, N steps) | — | "40 hours" → 40 ticks on P-CLOCK-SWEEP | "10,000 steps" → a road of dashes; the number stays in the caption |
| L-27 CTA | P-PRODUCT-CARD / P-KEYWORD-CARD / P-HANDLE-CARD | — | | |

### 8.5 Data and truth rules
- §18 is OFF; there are no charts, counters or figure cards.
- A quantity is a countable set of objects whose count equals the spoken number; when the number is too large to draw (> 120), draw "many" (≤ 120 objects) and never print the number on screen.
- Illustrative objects never carry invented numbers, percentages, dates or labels (NC-6). A clock shows no specific time unless the script names one.

### 8.6 Comedy layer
OFF (`tone.comedy: off`).

### 8.7 Asset rules
- Everything except the product cover and the seated take is built in the renderer.
- Device mocks are generic: an outline phone with grey cards; no app names, no logos, no recognisable UI.
- No stock, no AI imagery, no clip-art packs. Icons come from `fx.icon` or the bespoke recipes above.
- Logos are never drawn: a named brand is a P-QUIET-PLATE set in type, or the creator's own file (§12.5).

### 8.8 Density and variety
- F-B: one hero object per 2.3–4.5 s; 8–14 distinct patterns per 60 s; a pattern repeats only as the chain's return (the opening object, lit, at the end).
- The same pattern never twice in a row; P-DOT-SELF may link any two patterns.
- Internal events at least every 3.0 s (H2).

---

## §9 Transitions `[REQ] [DNA]`

### 9.1 Library
| ID | Transition | Frames | Recipe | Engine | SFX role |
|---|---|---|---|---|---|
| **T-MORPH** | Shape morph | 12–24 (default 18) | The outgoing object's outline resamples into the incoming object's outline (96 points, `fx.morph`); fill, stroke, glow and opacity interpolate; easing in-out `[0.37, 0, 0.63, 1]`. The object's centre may travel ≤ 300 px during the morph | `VEOS.fx.morphShape` keys, or `fx.shape` + `fx.morph` in a bespoke scene | silent, or a soft `transitions` cue |
| **T-PUSH-THROUGH** | Push into the object | 21 in two moves | (1) **Anticipation:** the object scales itself 1 → 0.65 over 12 f (ease-in-out) while its centre detail collapses to a dot (the pupil-clock becomes a point); (2) **push:** C-4 zoom-through ≥ 4× (default 5) into that darkest centre, ease-in, 9 f in the evidence; (3) a 2 f dissolve into dark, and the next object grows from the dark (v03 @ 0:01.70–0:02.57) | step 1 in the scene (`render` scale), step 2 `{"move": "zoom-through", "to": {"node": …}, "dur": 0.3, "p": {"scale": 5}}` (the measured 9 f push) | soft `whoosh` on the push (optional) |
| **T-HANDOFF** | The dot carries over | 15–24 | The dot (or a shared part) travels from its place in scene A to its place in scene B (`fx.handoff`, ease in-out); scene A fades out behind it over 10 f, scene B builds around it over 12 f. Variant: the dot falls under gravity (ease-in, 35 f) and the next object rises to catch it (v02 @ 0:16.2–0:17.5) | `fx.handoff` + the two scenes overlapping ≥ 10 f | silent |
| **T-SINK** | Back into the ground | 12–16 | The lit object reverses its own entrance: its light switches off in 1 f, it sinks into its ground ellipse over 8 f, the ground flattens and fades over 4 f, and its lamp or core stays behind as the dot (v03 @ 0:06.32–0:06.72) | scene keys | silent |
| **T-FLICKER** | Power flicker off / on | off 8–12, black 4–14, on 8–10 | **Off:** the object dims to ~40%, drops out for 1 f, blinks back dim for 2–3 f, goes out. **Black:** 0.13–0.45 s of pure black (the caption may stay). **On:** the next object blinks dim, out, dim, then full over 4 f. Object-level greys only, ≤ 3 blinks (v02 @ 0:00.07, 0:25.80–0:26.57, 0:32.3–0:33.1). **≤ 4 per reel with T-CRT-OFF**; for screens, devices, games and "switching off" lines, or wherever no shape links two scenes | per-frame opacity keys from a seeded pattern (`ctx.rng`) | optional calm `glitch` tick, unverified |
| **T-CRT-OFF** | Screen collapse | 5–6 + black 4 | A screen or bar flickers once, then squashes vertically to a 2–4 px bright line over 5 f (ease-in) and blinks out; 4 f of black; the next object flickers on (v02 @ 0:41.9–0:42.6) | scene `scaleY` keys | as T-FLICKER |
| **T-FLICKER-SWAP** | Shared shape, flickering | 6–8 | The two scenes alternate frame by frame for 6–8 f while the shared shape changes (the grown dot shrinks into the nail head), then the new scene holds (v02 @ 0:09.53–0:09.77) | two scenes with alternating opacity | silent |
| **T-COLLAPSE-DOT** | Into the dot | 6 + 2 dark | Every part of the scene retracts into the dot (the wedge narrows to a line, the vortex fades), the dot dims out, 2 f of dark; the next card arrives on the same centre (v03 @ 0:20.68–0:20.92). Real entry of the card: an un-warp from a heavy lens/whirl distortion to flat over 8–10 f while fading up (v03 @ 0:20.95–0:21.25); shipped as scale 1.25 → 1 + blur 14 → 0 + opacity over 10 f (engine gap) | scene keys | soft `shine` when the card settles (optional) |
| **T-BLOOM-DISSOLVE** | Fade through light | 10–14 | Scene A's bloom swells (glow +30 px) while its opacity falls to 0; scene B fades in from 0 under a decaying bloom. Used only when no shape, dot or flicker fits; **≤ 2 per reel** (the bloom swell that wipes the icon field in 2 f, v03 @ 0:00.47, is its fast form) | two scenes overlapping 10–14 f | silent |
| **T-BREATH** | One dark flicker frame | 1–2 | Superseded: the "breath" at v02 @ 0:00.20 is one off-frame inside T-FLICKER on. Kept as an id only | — | — |
| **T-FOCUS-PULL** | Blur in / out | 6–8 | Text or an object resolves from blur 10 px → 0 with opacity, or leaves the same way | `in: "blur"` / `out: "blur"` or `ctx.V` | — |
| **T-CARD-CUT** | The one cut (F-A) | 0 | Hard cut from W-card to L-seated on a sentence-end word boundary between 3.0 and 6.0 s (v01 @ 0:05.12) | `stage` `via: "cut"` | silent |
| **T-END** | Hard end | 0 | ≤ 6 f after the last word (or after the end card's hold); no black tail > 0.2 s | — | — |

### 9.2 Grammar
| Boundary | Use | Never |
|---|---|---|
| f0 | The opening object already moving (HA-15) or T-FLICKER on after 2 black frames (HA-12) / the first phrase already on the card (F-A) | a slam, a white flash |
| Hook's first transformation | T-MORPH in 4 f, or the one P-FLARE-BOWTIE reveal | a cut |
| Hook → first clause | T-PUSH-THROUGH (default) or T-HANDOFF | a cut |
| Clause → clause (same mechanism continues) | T-MORPH | a cut, a wipe |
| Clause → clause (a new world of meaning) | T-PUSH-THROUGH into the old object, T-SINK (a lit object leaves its light as the dot), T-HANDOFF of the dot, or T-FLICKER-SWAP when a shape survives | a cut |
| Out of a screen, phone, bar or game object; "switch off", "wake up" lines | T-FLICKER or T-CRT-OFF (≤ 4 per reel together) | an RGB glitch |
| "Zoom out", "the bigger picture" | P-ZOOM-OUT-ROLL (≤ 1 per reel) | a plain cut to a wide view |
| Into COST | T-MORPH while dimming (P-DOT-DIM) | a bright transition |
| Into TURN | T-HANDOFF to P-DOT-SOURCE, or T-PUSH-THROUGH into the light | — |
| Into the end card | T-COLLAPSE-DOT (default, v03), T-BLOOM-DISSOLVE, or T-MORPH (the dot becomes the cover's rim light) | a hard cut |
| F-A card phrase → phrase | hard swap (0 f) | a fade, any motion |
| F-A card → face | T-CARD-CUT | a fade, a zoom |
| F-A face → end card | `fade-through` 10 f (G-2) | a cut mid-word |
| Last word | T-END | a black tail |

### 9.3 Shot grammar
OFF (`spine` is `audio` / `talking_head`; no multi-camera, master or stunt source).

### 9.4 Budget (per 60 s, F-B)
- T-MORPH 8–16, T-PUSH-THROUGH 2–6, T-HANDOFF + T-SINK 2–6, T-FLICKER + T-CRT-OFF ≤ 4 per reel, T-FLICKER-SWAP ≤ 2 per reel, T-BLOOM-DISSOLVE ≤ 2 per reel, P-FLARE-BOWTIE and P-ZOOM-OUT-ROLL ≤ 1 each.
- A reel leans on one voice: lit-object chains (v03 model) use morphs, push-throughs and sinks and at most 1 flicker; screen-and-game chains (v02 model) may use the full flicker budget.
- **The same transition never 3× in a row**; T-PUSH-THROUGH never twice in a row.
- Every T-PUSH-THROUGH is a canvas-camera move: keep ≥ 0.4 s between the end of one camera move and the start of the next (§21).

Transition map format (part of the plan):
```yaml
transitions:
  - {t: 0.00, id: HA-15, from: null, to: S1-swirl, note: "icon swirl breathing at f0"}
  - {t: 0.45, id: T-MORPH, from: S1-swirl, to: S2-eye-clock, frames: 15}
  - {t: 1.95, id: T-PUSH-THROUGH, from: S2-eye-clock, to: S3-beam, node: pupil, frames: 14, sfx: "soft whoosh"}
  - {t: 9.80, id: T-HANDOFF, from: S5-feed, to: S6-ladder, carrier: M-dot}
```

---

## §10 Motion, camera, layers, finishing `[REQ] [DNA; motion tokens TUNE ±15%]`

### 10.1 Motion tokens (30 fps)
| Token | Value |
|---|---|
| Beat lead | 2 f before the trigger word's onset |
| Object entry | 12 f: opacity 0 → 1, blur 12 → 0 px, scale 0.96 → 1.00, ease `[0.33, 0, 0.2, 1]` |
| Object exit | 8 f: opacity → 0, blur 0 → 10 px, ease `[0.5, 0, 0.75, 0]` (when not morphing) |
| Morph | 12–24 f (default 18), ease `[0.37, 0, 0.63, 1]`; a hook snap 4 f; a shape-to-shape growth (bar → screen) up to 48 f |
| Push-through | contract 12 f (object 1 → 0.65) + push 9 f measured (15 f shipped, V-CANVAS floor), ease-in, + 2 f dissolve |
| Flicker | off 8–12 f (dim 40% → out 1 f → dim 2–3 f → out), black 4–14 f, on 8–10 f (dim → out → dim → full over 4 f); seeded |
| Flare reveal | 3 f ramp (slit → bow-tie → wash), 8 f decay, peak frame mean luma ≤ 40% |
| Letter flicker | end-card line: each letter blinks 1–3× (2 f on, 1–2 f off), seeded order, line done in 30–36 f |
| Chomper | 1 dot per 7–8 f |
| Breathing | scale 1.00 ↔ 1.04, period 90 f (sine) on every glowing core at rest |
| Idle drift | 6–12 px/s on the hero object or the canvas (C-3) |
| Rotation | ≤ 6°/f for clock hands and gears (v03: gear ≈ 6°/f), ≤ 1.2°/f for swirls |
| Beam sweep | 3–6 s per sweep (sine) |
| Hops | 10–14 f arcs, ease-in-out, **no bounce** |
| Overshoot | **0** (DNA: `pop_overshoot` 0) |
| Caption swap | CS-B chunk wipe L → R 5–7 f in, R → L 4–6 f out, 3–4 f gap (shipped: blur 6 f in, 5 f out); CS-A / CS-A0 hard (0 f) |
| Holds | text ≥ 0.3 s per word; any object ≥ 12 f after it settles; the one held-still dot ≤ 0.9 s |
| Camera creep | during long scenes a slow push of +0.6–1.6% per second (v03 @ 0:12.5–0:20); still camera on lit-tower scenes and on the end card |

### 10.2 Footage camera
`zoom_policy: none`. F-A is a locked-off take: no punch-ins, push-ins, crops per sentence, shake or rotation (v01: the framing is identical at every 1 fps sample). F-B has no footage.

### 10.3 Canvas camera
See §21 (F-B only).

### 10.4 Layer order (back to front)
1. z1 W-void ambient (`fx.ambient` void, continuous) — F-A: W-card or the footage.
2. z2 Fields and light: P-ICON-SWIRL (E4), beams, cones, the bloom halo of the hero object.
3. z3 The hero object (and its supporting parts at ≤ 50% opacity).
4. z4 The motif dot (always above the object it sits in or on).
5. z5 In-object words, the split title.
6. z7 Captions (CS-B / CS-A / CS-A0).
7. z8 End cards (captions hidden under them).
8. z11 P-FLARE-BOWTIE (momentary).

### 10.5 Finishing
- **Bloom** on the hero object and the dot only: `drop-shadow(0 0 Npx rgba(255,255,255,a))` with N 8–40 px and a .25–.6, plus one radial halo (r 20–60 px, alpha ≤ .4) behind it. Never on captions.
- **Noise** 0 on W-void (the void is flat #000, audit 2026-10-06; TUNE 0–0.04); grain on lit objects through the gradient stops only (v03 hourglass sand, lighthouse).
- **Vignette** 0 on W-void (TUNE 0–0.5). The haze around lit objects is their own bloom; v03's lit-tower and end-card scenes lift the surround to a soft grey glow (frame mean luma 15–35) from that bloom, not from a vignette.
- **Light cones** alpha ≤ .28; at most one cone or wedge per frame.
- **Performance:** ≤ 3 blurred layers per frame; particles ≤ 200 on one canvas; ≤ 30 ms per frame (G3).

---

## §11 Sound contract (minimal) `[REQ] [VAR]`
| Line | Decision |
|---|---|
| **Cue moments** | `hook` (one soft cue on f0, optional) · `transitions` (a soft `whoosh` on the T-PUSH-THROUGH push only; a quiet calm `glitch` tick may sit on a T-FLICKER / T-CRT-OFF off-frame; morphs and sinks are silent) · `reveals` (a soft `shine` on the flare reveal, or when the dot becomes a source or a beam opens) · `cta` (one soft tone when the end card settles). No list cue. At most 2 cues per 10 s (`budgets.sfx_per_10s` 2), pack defaults for `energy: calm` |
| **Meme cues** | off (comedy off) |
| **Music bed** | on, from f0: an ambient pad or a slow, sparse piano without drums or lyrics |
| **Ducking** | the bed sits ≥ 18 dB under the voice while the voice speaks; it may rise to −22 dB in pauses ≥ 0.6 s; F-A room tone is kept |
| **Loudness** | −14 LUFS integrated, true peak ≤ −1.5 dBTP; a hard end ≤ 6 f after the last word (NC-8) |

(Unverified: sound is not observable in the evidence; these values are the calm default of the SFX pack.)

---

## §12 Footage, shot list, fallbacks, inserts `[REQ]`

### 12.1 Setups `[DNA what the style assumes; VAR the buyer's actual setup]`
**F-B: the voice-over.** A quiet room, a close mic (15–25 cm), a calm, low, unhurried delivery at 130–155 words per minute; leave natural breaths between sentences (they become the chain's morphs). One take or comped takes with matched tone. WAV 48 kHz.

**F-A: Setup A, seated** (v01):
- Camera: tripod, eye level, front-on, 9:16 (4K or 1080p), 50–85 mm equivalent, shallow depth of field.
- Framing: medium close-up; head top y 220–300, eyes y 600–660, chin y 880–960, hands entering from the bottom and allowed to gesture; the chest band y 1320–1430 stays plain (the gold captions sit there).
- Background: a dark, low-detail wall (slate grey-green ≈ #3A4A4A) with two soft vertical light strips at the frame edges (x ≈ 8% and 92%), or any dark, plain wall.
- Light: soft frontal key, low contrast, no coloured practicals.
- Wardrobe: a plain black or charcoal tee (no text across the chest band: a small logo at chest left is fine).
- Frame rate: 24, 25 or 30 fps; conform to 30 fps CFR.
- Mic: off-frame (lav hidden or boom).

### 12.2 Shot list
OFF (`footage_dependency` is `none` / `low`).

### 12.3 Fallbacks
OFF for footage (no shot list). Graphic fallbacks are built in: every lit object is an engine 3D object (B-4), no files needed; a missing product cover means the end card becomes P-KEYWORD-CARD or P-HANDLE-CARD (or `none`); a missing seated take means the reel is made in F-B.

### 12.4 Props, reaction bank, matte, resolution
- Props: none. The product cover image (PNG/JPG, ≥ 1000 px tall, the creator's own) for `product_card`.
- Reaction bank: none. Matte: none.
- Resolution: F-A is never punched in; a 1080p take is enough (a one-off reframe ≤ 1.10× is allowed for framing, §3.6).

### 12.5 Third-party inserts: ask, then create `[REQ always]`
Claude **never fetches anyone else's media**.
1. **Analyse the transcript** (`veos inserts scan`) and list the moments that call for third-party material: a quoted post or person, a headline, a named product or app, another creator's clip, a book that isn't the creator's.
2. **Ask the creator once**: "For these N moments, do you have a clip or screenshot? Drop the files, or say no."
3. **Supplied:** show it inside the style: on an `ash` card (radius 24) desaturated to greyscale (`filter: grayscale(1) contrast(1.05)`), centred in the object zone, entering by T-FOCUS-PULL, never altered to say something it doesn't. A product cover the creator owns keeps its colours on the end card only.
4. **Not supplied: create** the quiet substitute from the script's words: P-QUIET-QUOTE (`fx.quoteCard`, dark, greys), P-QUIET-PLATE (`fx.logoPlate`, the name set in type), P-QUIET-SCREEN (`fx.appUI`, dark, generic), or a silhouette (`fx.silhouette`, greys) for a person. 
5. **Record** each moment in `plan/inserts.json` `{id, moment, origin: creator | created, file?, recipe?, substitute_of?, quote_text?}`.

In this style most essays have **no** third-party moment; when one appears, prefer re-casting it as a metaphor (L-24 → the quote becomes P-EMITTERS-CONVERGE with the quote in the captions) unless the exact words of a named person matter.

### 12.6 Frame rate and audio
30 fps CFR output, 1080 × 1920. Voice chain: high-pass 80 Hz, gentle de-ess, light compression (2:1), −14 LUFS.

---

## §13 Output contract `[REQ] [DNA]`

### 13.1 Core beat fields
`id`, `section` (THESIS / CLAUSE-n / COST / TURN / PAYOFF / CTA), `t0`/`t1`, `spoken`, `trigger {word, at}`, `tone` (state / cost / turn / resolve / cta), `line_type` (L-01…L-27), `layout` (L-void / L-card / L-seated), `visual` (one sentence), `layers` (scene ids), `pattern`, `sfx`.

### 13.2 Conditional fields
| Switch / module | Beat fields |
|---|---|
| captions | `caption {profile: CS-B \| CS-A \| CS-A0, overrides[]}` (no emphasis, no tiers) |
| canvas_camera (F-B) | `camera_canvas {move: C-1…C-4, to, frames}` |
| continuity (F-B) | `morph_in` (T-… + the parent scene id), `morph_out`, `motif_state` (idle / grown / eye / source / seed / dim / absent) |
| brand | `sponsor {id, disclosure}` when a sponsor exists; the end-card device |
| third-party moment | `insert {id, origin: creator \| created}` |
| declared exception | `exception: E3 \| E4` (E3 is inherited by captions; E4 on P-ICON-SWIRL / ambient P-DOT-FIELD) |

Example (F-B):
```yaml
- id: 4
  section: CLAUSE-2
  t0: 9.80
  t1: 13.40
  spoken: "and you numb your mind with endless scrolling"
  trigger: {word: "scrolling", at: 12.62}
  tone: cost
  line_type: L-04
  layout: L-void
  pattern: P-FEED-PHONE
  visual: "The dot drops into a grey outline phone; cards scroll; the dot hops card to card and the outlines dim to smoke on 'numb'"
  layers: [void, s4-phone, s4-dot]
  morph_in: {t: T-MORPH, from: s3-tower, note: "the tower's outline narrows into the phone frame"}
  morph_out: {t: T-HANDOFF, to: s5-hourglass, carrier: M-dot}
  motif_state: idle
  camera_canvas: {move: C-3, to: {by: {x: 0, y: -30}}, frames: 90}
  caption: {profile: CS-B, overrides: []}
  sfx: []
```

### 13.3 Reel header
```yaml
format: F-B                 # F-B | F-A
theme: null                 # single
hook_archetype: HA-15       # HA-15 | HA-12 | HA-14
structure: essay
thesis: "You weren't born to rent your hours to someone else's dream"
motif: M-dot
cta: {device: product_card, keyword: null, asset: cover}
sponsor: null
```

### 13.4 Hook proposals (3)
Each: name · archetype · the thesis line · the hook pair (§6.4) · the opening object and its first transformation · captions (first 3 chunks) · storyboard line (f0 | 0.5 | 1.5 | 2.5 s) · sound (the cues used) · stopper results (ST-1 object width %, ST-2 thesis captioned by s, ST-3 yes/no, ST-5 count, ST-6 s).

### 13.5 Checkpoint
1. The 3 hooks with their stopper tests and a recommendation.
2. The beat sheet with tones, patterns and the **chain table** (scene → morph_in → morph_out → motif state).
3. The transition map and the canvas-camera list.
4. The SFX ledger (≤ 2 cues per 10 s).
5. The inserts record (creator-supplied vs created) and the end-card asset.
6. Style stills: f0, 1.5 s, the first push-through landing, one body beat per tone (state, cost, turn), the end card. F-A: f0 card, the cut frame, one body frame, the end card.

**Wait for approval.**

---

## §14 Worked examples `[REQ] [NICHE: example]`
Times are estimates; replace them with `words.edit.json` onsets.

### 14.1 F-B, money & work: "You weren't born to rent your hours" (34 s, CTA keyword FREEDOM)
**Thesis:** "You weren't born to rent your hours to someone else's dream." **Hook:** HA-15. **Motif:** the dot = the viewer's time.

| t (s) | Spoken | Tone | Visual (pattern) | Caption (CS-B) | Camera | SFX |
|---|---|---|---|---|---|---|
| f0 | — | state | P-ICON-SWIRL: 16 line icons spiralling in around the dot (E4); W-void glow drifting | — | C-3 drift | soft pad swell (hook) |
| 0.10 | "You weren't born" | state | The swirl tightens | "You weren't born" (chunk wipe-in) | drift | — |
| 0.55 | "to rent your hours" | state | T-MORPH (15 f): the swirl condenses into a clock gauge, then the clock becomes the pupil of P-EYE-CLOCK | "to rent your hours" | — | soft tone (reveal) |
| 1.40 | "to someone else's" | state | The gear fades in behind at 35% and starts turning on "else's"; threads drift | "to someone else's" | — | — |
| 2.05 | "dream" | turn | T-PUSH-THROUGH into the pupil (C-4, ×5, 14 f) | "dream" | C-4 | soft whoosh |
| 2.55 | — | state | Out of the dark ring, P-LIT-TOWER rises; lamp lights | — | C-2 settle | — |

| Section | Spoken (gist) | Tone | Pattern | morph_in → morph_out | Dot |
|---|---|---|---|---|---|
| CLAUSE-1 (2.6–7.0) | "Most people spend their best hours building somebody else's lighthouse" | state | P-BEAM-SWEEP: the beam sweeps over the void, never toward the dot | T-PUSH-THROUGH → T-MORPH (the beam narrows into a clock hand) | absent → appears small at the tower's foot at 5.8 |
| CLAUSE-2 (7.0–11.5) | "Forty hours a week, for forty years" | cost | P-CLOCK-SWEEP with 40 ticks (spoken "forty"); the hands sweep fast then stop on "years" | T-MORPH → T-HANDOFF | idle, riding the minute hand |
| CLAUSE-3 (11.5–15.5) | "and the little time left goes to a screen" | cost | P-FEED-PHONE: the dot hops card to card; outlines dim to smoke | T-HANDOFF → T-MORPH (the phone outline collapses into a ring) | idle → dim at 15.0 |
| COST (15.5–20.0) | "until one day you wake up and wonder where it went" | cost | P-HOURGLASS-LOOP: the top bulb drains on "went"; P-DOT-DIM | T-MORPH → T-HANDOFF | dim |
| TURN (20.0–24.5) | "But your hours are the only thing you truly own" | turn | P-DOT-SOURCE: the dot relights, glow 24 → 90, rays turn | T-HANDOFF → T-MORPH (the rays become steps) | source |
| PAYOFF (24.5–30.0) | "Spend one of them every day building your own" | resolve | P-LADDER-CLIMB: one hop per "one"/"every"/"own"; each passed step lights white; the tower returns, lit, at the top (the chain's return) | T-MORPH → T-BLOOM-DISSOLVE | source |
| CTA (30.0–34.0) | "Comment FREEDOM and I'll send you my one-hour plan" | cta | P-KEYWORD-CARD: "comment" / FREEDOM in white / the dot below | T-BLOOM-DISSOLVE (1 of 2 allowed) | idle |

Cadence check: ~31 caption chunks ≈ 15.5 weighted + 9 scene entries + ~12 events over 34 s ≈ 10.8 per 10 s at the busiest window → **too busy**: merge CLAUSE-2's tick event into one (stop only), and set CS-B chunks to 2–4 words for this reel (`captions.overrides` breaks) → ≈ 8.5 per 10 s. Max gap ≤ 3.0 s held by the events listed.

### 14.2 F-B, health & fitness: "You don't lack motivation. You lack a default." (29 s, CTA product_card)
**Hook:** HA-12 alternate (split title). **Motif:** the dot = you, day by day.

| t (s) | Spoken | Tone | Visual | Caption | Camera |
|---|---|---|---|---|---|
| f0 | — | state | P-SPLIT-TITLE "YOU DON'T LACK / MOTIVATION" flickers on (T-FLICKER, 9 f) with a row of 9 dots (P-DOT-ROW-EATEN) | hidden | drift |
| 0.35 | "You don't lack motivation." | state | The title and row are fully on | hidden (title says it) | — |
| 0.67 | — | — | The chomper enters and eats the days at 7–8 f per dot | hidden | — |
| 1.60 | "You lack a default." | turn | The title and the uneaten days flicker off; the last dot (today) is alone, held still ≤ 0.9 s | "You lack a default" | — |
| 2.40 | — | state | Two outline steps fade in under the dot (T-HANDOFF begins) | — | — |

| Section | Spoken (gist) | Tone | Pattern | morph_in → morph_out | Dot |
|---|---|---|---|---|---|
| CLAUSE-1 (2.4–6.5) | "Motivation shows up when it wants to" | state | P-WAVE-SETTLE inverse: one calm line breaks into 5 noisy waves | T-HANDOFF → T-MORPH | idle, bobbing on the waves |
| CLAUSE-2 (6.5–11.0) | "A default shows up every day at 7 am, whether you feel like it or not" | state | P-CLOCK-SWEEP: hands sweep and stop at the 7 position (the script names the time) | T-MORPH → T-MORPH | idle at the centre |
| CLAUSE-3 (11.0–15.5) | "Shoes by the door. Same time. Same first move." | state | P-DOOR-SPILL: the door opens on "door"; the light spills over the dot | T-MORPH → T-HANDOFF | idle |
| COST (15.5–19.5) | "Wait for motivation and you'll wait forever" | cost | P-DOT-ORBIT: the dot circles a smoke ring, dimming | T-HANDOFF → T-MORPH | dim |
| TURN (19.5–23.0) | "Build the default once" | turn | P-DOT-SEED: the dot drops to a ground line; a shoot grows | T-MORPH → T-MORPH | seed |
| PAYOFF (23.0–26.0) | "and your body follows it for years" | resolve | P-SEED-TREE grows 3 levels on "body" / "follows" / "years" | T-MORPH → T-BLOOM-DISSOLVE | source at the tree's crown |
| CTA (26.0–29.0) | "My book on habits is out now" | cta | P-PRODUCT-CARD: the creator's cover, "NOW AVAILABLE" at y 230 | T-BLOOM-DISSOLVE | absent |

### 14.3 F-A, seated: "The fastest way to get fit is to change your room" (38 s, CTA none)
**Hook:** HA-12 (text-only cold open). Setup A (§12.1).

| t (s) | Spoken | Visual | Caption |
|---|---|---|---|
| f0 | "The fastest way" | W-card black; ambient at 0 glow | CS-A0 white 68 px, y 960: "the fastest way" |
| 0.9 | "to get in shape" | hard swap (0 f) | "to get in shape" |
| 1.8 | "is to change the room you live in" | holds 1.6 s | "is to change the room" → "you live in" |
| 4.30 | — (sentence ends) | **T-CARD-CUT** to L-seated on the boundary at 4.30 s | CS-A starts with the next word |

| Section | Spoken (gist) | Visual | Caption |
|---|---|---|---|
| CLAUSE-1…4 (4.3–24) | "You stop keeping sugar in the kitchen… you put your shoes by the bed… you follow people who train… you pick the gym on your way home" | P-SEATED-HOLD: the static take, hands gesturing; no zoom | CS-A gold lowercase, 3–5 words per chunk, y 1372 |
| COST (24–29) | "It's going to feel strange and a little lonely at first" | P-SEATED-HOLD | CS-A |
| TURN (29–33) | "but if you can stay in that room long enough" | P-SEATED-HOLD; the one allowed pause ≤ 0.8 s before the payoff | CS-A |
| PAYOFF (33–37.6) | "you become the person who lives there" | P-SEATED-HOLD | CS-A |
| END (37.6–37.8) | — | T-END ≤ 6 f after "there" | — |

Presence: 33.5 / 37.8 s = 89% (inside 80–92%). Longest absence 4.3 s (the card).

---

## §15 QA checklist `[REQ] [DNA]`

**1. Profile conformance**
- [ ] The reel header declares `format` F-B or F-A and the matching layouts; F-B stage is `L-void` throughout (V-LAYOUT).
- [ ] Duration 25–55 s (review). F-A presence 80–92%, absence ≤ 6 s (V-PRESENCE).

**2. Hook**
- [ ] F-B f0: a non-text object moving, ≥ 25% of the width; no presenter (V-F0). F-A f0: the black card with the first phrase; no face (V-F0).
- [ ] Thesis captioned by 3.0 s (F-B) / carded by 6.0 s (F-A) (V-F0 payoff); ≥ 3 / ≥ 1.0 weighted SCs in 0–3 s (V-CADENCE).
- [ ] P-SPLIT-TITLE (if used): ≤ 8 words, 2 lines at y 746 / 1160, gone by 2.0 s (V-TITLE).

**3. Body and cadence**
- [ ] F-B 3–9 SC per 10 s, no full-weight gap > 3.0 s, nothing static (V-CADENCE). F-A 1.5–4 per 10 s (V-CADENCE).
- [ ] **No orphan scene**: every F-B boundary is T-MORPH / T-PUSH-THROUGH / T-HANDOFF / T-BLOOM-DISSOLVE (≤ 2); 0 hard cuts; F-A has exactly 1 cut (review; V-CONTINUITY when it ships).
- [ ] The dot is in ≥ 60% of F-B scenes, never duplicated (review; V-CONTINUITY).
- [ ] One hero object per idea, centred in the object zone, 35–55% wide (review, G2).
- [ ] Every object action lands on its trigger word (V-ONWORD).
- [ ] The light curve: dimmest at COST, brightest at TURN; the final object is the lit return of the opening object or the dot as a source (review).

**4. Captions**
- [ ] CS-B: Poppins 500, 44 px, 1 line, 1–4 words, y 1470, chunk reveal (blur-in 6 f, out 5 f), no emphasis (V-CAPTION, V-TYPE under E3).
- [ ] CS-A: EB Garamond 400, 62 px, gold, lowercase, y 1372, 3–5 words, hard swaps; CS-A0: 68 px white at y 960 on the card, hard swaps (V-CAPTION, V-TYPE).
- [ ] Motion spot-check at full frame rate on the hook, every push-through and every flicker: contraction before the push, flicker ≤ 3 blinks and object-level only, one flare at most (review).
- [ ] No chunk straddles the F-A cold-open cut; captions hidden under end cards (review).
- [ ] Sync ≤ 0.15 s lead; spelling from the glossary (V-CAPTION).

**5. Modules**
- [ ] Canvas camera: moves ≥ 0.5 s, ≥ 0.4 s apart, eased; no text scene below its floor after zoom; captions never move (V-CANVAS).
- [ ] Continuity: every scene carries `morph_in`, `morph_out`, `motif_state` (review).
- [ ] Brand: one end card ≤ 4.0 s; the keyword readable ≥ 1.5 s; a sponsor disclosure ≥ 2 s if any (V-PROMISE, NC-12).

**6. Truth and inserts**
- [ ] No number printed on screen unless it is spoken; quantities are counted objects (review, NC-6).
- [ ] Every third-party moment is the creator's file (greyscale card) or a created quiet substitute, recorded in `plan/inserts.json` (V-INSERTS).
- [ ] Monochrome: no chroma in F-B graphics except the end-card accent (V-HUES + review at 3 sampled frames per scene).

**7. Sound**
- [ ] Cues only on hook / push-through / reveals / CTA; ≤ 2 per 10 s; no meme cues (S1–S6).
- [ ] Bed from f0, ≥ 18 dB under the voice; −14 LUFS; true peak ≤ −1.5 dBTP (NC-8).

**8. End and export**
- [ ] CTA hold within §6.7; hard end ≤ 6 f after the last word; no black tail > 0.2 s.
- [ ] 1080 × 1920, 30 fps CFR; ≤ 30 ms per frame in `veos measure`.

---

## §16 Frame template / persistent chrome
OFF (`profile.modules.chrome = false`): nothing persists on screen; the frame is empty black around one object.

## §17 Running state & anchored graphics
OFF (`modules.running_state = false`, `modules.anchors = false`): no counters, ledgers or tracked tags.

## §18 Data contract
OFF (`modules.data_figures = false`): quantities are counted objects (§8.5); there are no figures.

## §19 Evidence & citations
OFF (`modules.citations = false`): an essay style; third-party moments use the §12.5 flow.

## §20 Dialogue
OFF (`modules.dialogue = false`): one voice.

## §21 Canvas camera `[COND: modules.canvas_camera] [DNA]` (F-B only)
The camera moves over the void (z1–6), never over the captions (z7) or end cards (z8).

| Move | Scale | Frames | Ease | Use | Budget per 60 s |
|---|---|---|---|---|---|
| **C-1 push** | 1.0 → 1.2–1.6 to a node (`fill` 0.6) | 18–36 | inOut | leaning into the object on a `turn` beat; reading a small detail (the nail, the pupil) | ≤ 6 |
| **C-2 pull / settle** | 1.0 → 0.7–0.85, or back to home | 18–36 | inOut | `cost` (seeing how small it is), `resolve` (seeing the whole), the settle after a push-through | ≤ 4 |
| **C-3 drift** | 1.0 (pan 20–60 px) | 60–150 | sine | idle life on every long hold | ≤ 8 |
| **C-4 zoom-through** | 1 → 3–8× (default 5) into a node, then `then: home` | **9** (`dur: 0.3`; a zoom-through may take 0.25 s, at up to 35 % zoom per frame: ease `in` × 5 peaks at ≈ 30 %) | in | T-PUSH-THROUGH, always after the object's own 12 f contraction (the object fills the frame and becomes the next scene) | ≤ 6 |
| **C-5 orbit** | — | — | — | not used (the lit 3D objects keep a still camera) | 0 |
| **C-6 zoom-out with roll** | ~3× → 1× and ~50° roll | ~20 | out | P-ZOOM-OUT-ROLL only, on a literal "zoom out" line; built as the scene's own scale + rotate: the canvas camera's `roll` stops at 20° and 2° per frame | ≤ 1 per reel |

Measured: v01 camera locked (scale 1.000, p95 0.7 px/frame); v03 lit-tower and end-card scenes still; v03 spotlight scene creeps in +0.6–1.6%/s; v02 emitter scene rotates as a group at 13°/s with a slight pull-in.

Rules:
- Every C-4 target is a declared node (`canvas_nodes` or a scene's `nodes`) at the object's darkest centre (a pupil, a screen, a door gap, the dot's core), so the frame fills with black, not with glare.
- **≥ 0.4 s** between the end of one move and the start of the next; never two C-4 in a row.
- Text scenes that ride the camera (P-SPLIT-TITLE, P-OBJECT-WORD) stay ≥ their class floor after scale (`text_px` × zoom); end cards set `parallax: false`.
- Keep zoomed content out of the caption band (y 1420–1520) or hide captions for that span.
- Validator: V-CANVAS.

```json
"canvas_nodes": {"pupil": {"x": 510, "y": 930, "w": 60, "h": 60}},
"canvas_camera": [
  {"t": 0.0, "move": "drift", "dur": 2.0, "p": {"by": {"x": 0, "y": -20}}},
  {"t": 2.13, "move": "zoom-through", "to": {"node": "pupil"}, "dur": 0.3, "p": {"scale": 5, "then": {"x": 540, "y": 960, "s": 1}}},
  {"t": 7.2, "move": "push", "to": {"x": 540, "y": 1000, "s": 1.25}, "dur": 0.9},
  {"t": 16.0, "move": "pull", "to": {"x": 540, "y": 960, "s": 0.85}, "dur": 1.2}
]
```

## §22 Ink & annotation layer
OFF (`modules.ink = false`): the only marks are P-STRIKE-X, drawn as part of the object scene.

## §23 Continuity: morph chains, the motif, bookends `[COND: modules.continuity] [DNA]` (F-B only)

### 23.1 Morph chain
- Every scene declares `morph_in` (its parent: the previous scene's object, its centre, or the dot) and `morph_out` (its child).
- Boundaries are **T-MORPH, T-PUSH-THROUGH, T-HANDOFF, T-SINK, T-FLICKER-SWAP or T-COLLAPSE-DOT**; **T-FLICKER / T-CRT-OFF ≤ 4 per reel** (screens, devices, games, "switching off"); **T-BLOOM-DISSOLVE ≤ 2 per reel**.
- **No orphan scene:** zero hard cuts in F-B (v02 and v03: 0 cuts in 75 s). A flicker through black is the only boundary without a shared shape; it still never cuts mid-sentence: the caption carries across the black.
- **Shared-object rule:** the parent and child overlap on screen for ≥ 10 f; G1 is satisfied by declaring `overlaps: ["<parent id>"]` on the child for that span.
- **Chain table** (a checkpoint item): scene id · pattern · t_in–t_out · morph_in · morph_out · motif state.

### 23.2 The motif: M-dot
| State | Look | Used in |
|---|---|---|
| `idle` | Ø 40 (TUNE 30–48), white core, glow 24 px, breathing 1.00 ↔ 1.04 / 90 f | P-DOT-SELF, P-LADDER-CLIMB, P-FEED-PHONE, P-DOT-ORBIT, P-DOT-AMONG |
| `grown` | Ø 120–216, flat white, glow 40 px | P-DOT-GROW |
| `eye` | Ø 40 as a pupil highlight inside an object | P-EYE-CLOCK (optional) |
| `source` | Ø 40, glow 90 px, 6–8 rays | P-DOT-SOURCE, P-SPIRAL-SPOTLIGHT |
| `seed` | Ø 30, glow 16 px | P-DOT-SEED, P-SEED-TREE |
| `dim` | Ø 40, `bad` grey #6E6E6E, glow 0 | P-DOT-DIM, COST beats |
| `absent` | — | ≤ 40% of scenes (lit-object scenes, the end card) |

Rules: one motif per frame (P-DOT-AMONG shows many grey dots but only one lit); the motif always enters a scene by T-HANDOFF or is revealed inside the new object; it is the last thing on screen when the CTA is `none`.

### 23.3 Recurring diagram
Not used.

### 23.4 Bookend `[VAR]`
`continuity.bookend: false` by default. When on, the last 1.5 s reuses the opening object, now lit (the chain's return; §7.4).

Validator: V-CONTINUITY (pending in this engine; the frame reviewer checks every boundary still until it ships).

## §24 Series furniture
OFF (`modules.series = false`, VAR): the style carries no episode cards; a buyer who turns it on gets a TC-legal tag "part {n}" at x 64, y 140 in `smoke`, fading in over 12 f at 0.5 s and out at 3.0 s.

## §25 Sponsor, brand & end cards `[COND: modules.brand] [DNA look; VAR assets]`
- **P-PRODUCT-CARD** (default end card when the creator has a product): the line "NOW AVAILABLE" (+ "ON <STORE>" when the VO names it) in Montserrat 500 caps 60 px (cap height 48), `paper`, centre y 230 (two lines: 180 / 262), letters flickering on in place in a seeded random order over 30–36 f, starting ~0.8 s after the cover lands (v03 @ 0:21.83 → 0:23.0); the creator's cover image (`ctx.asset("cover")`) x 220–860, y 360–1320 on an `ash` panel, a white rim glow (16 px, alpha .35) and two soft light streaks behind it drifting 2 px/f; enters by **T-COLLAPSE-DOT** (the last scene retracts into the dot, 2 f dark, the cover un-warps and fades up over 8–10 f on the same centre), T-BLOOM-DISSOLVE or the dot becoming the rim light (T-MORPH). The camera is still for the whole card. Hold 2.5–4.0 s (v03 @ 0:21–0:25).
- **P-KEYWORD-CARD**: "comment" (Poppins 500, 44 px, `mist`, y 780) and {{BV-08.keyword|KEYWORD}} (Montserrat 700, 88 px, `primary` white with a 24 px bloom, tracking +0.06, y 900; `accent` only if the buyer brands it: the real void never carries gold), the dot breathing at y 1080. `kind: "cta-keyword"`. Hold 1.5–4.0 s.
- **P-HANDLE-CARD**: "LINK IN BIO" (60 px caps, `paper`, y 230), the dot at (540, 960), the handle {{BV-01.handle|@yourhandle}} (Poppins 400, 30 px, `smoke`, y 1430). Hold 2.0–3.0 s.
- **Sponsor:** a sponsored essay keeps the style: the sponsor's name appears as a P-QUIET-PLATE (greys, set in type) inside the chain, never a coloured logo pop; the disclosure line "Paid partnership" (BV-14 wording) (TC-legal 24 px, `smoke`, x 64, y 140) holds ≥ 2 s from the first sponsor mention, and the VO says it (NC-12).
- Rules: one end card per reel, ≤ 4.0 s; captions hidden during it; no black tail > 0.2 s; the accent appears on the keyword only.

---

## Part C. Exceptions and the non-overridable core

### C.1 Non-overridable core
NC-1…NC-14 apply unchanged. The ones this style leans on most:
- **NC-1:** F-A captions sit on the chest ≥ 40 px below the chin; nothing is drawn over or behind the face.
- **NC-4:** quiet type never goes under 40 px for F-B captions (the registry floor is 36; this style stops at 40) and contrast stays ≥ 7:1.
- **NC-5:** the evidence put F-B captions at y ≈ 1543 (v03), inside the IG bottom band; this template lifts them to y 1470 (band 1420–1520).
- **NC-6:** no printed numbers that aren't spoken; illustrative objects carry no statistics.

### C.2 Exceptions used
| E-id | Token limits (`tokens.exceptions`) | Scenes that set it |
|---|---|---|
| **E3** | `subtitle_min_px 40`, `label_min_px 32`, `contrast_min 7.0`, `pill_contrast_min 4.5`, `weight_min 500`, `max_lines 1`, `max_chars_line 24` | captions (CS-B inherits it); never F-A captions (60 px needs no exception) |
| **E4** | `max_items 24`, `max_item_area 0.04`, `max_speed_px_s 60`, `dim_under_text 0.4`, `max_s 3.0` | P-ICON-SWIRL; P-DOT-FIELD only when it is drawn as ambient background (z2, `ambient: true`) |

No new exception is needed. A buyer may switch E3 off (then CS-B must be ≥ 54 px) or E4 off (then P-ICON-SWIRL is not used) at VAR level.

### C.3 How the exceptions are declared in a reel
Captions inherit E3 from CS-B. A P-ICON-SWIRL scene sets `z: 2`, `exception: "E4"`, `ambient: true`, marks each icon `data-item`, and declares `dim_under_text: 0.4` when it dims under the caption rect.

---

## Part D. Personalisation

### D.1 Setup questions (one round, each with "keep the template default")
| ID | Question | Feeds | Default |
|---|---|---|---|
| BV-01 | Your name and handle | `creator.name/handle`; P-HANDLE-CARD | "the creator", "@yourhandle" |
| BV-02 | One brand colour (or keep gold) | `roles.accent` (F-A captions, the end-card keyword); nudged to ≥ 7:1 on #0B0B0B | #FCC31E |
| BV-05 | The language you speak and the caption language | `profile.language`, always asked: **English** → English captions (default) · **Hinglish** → romanised Hinglish captions · **Hindi** → Devanagari captions; numbers follow (BV-06) | English ({{BV-05.speech|en}} → {{BV-05.captions|en}}) |
| BV-08 | Your call to action: product card, comment keyword, link in bio, or none | `profile.cta.chosen`, §6.7, §25 | none |

Only one colour is brandable: the style is monochrome by DNA, so a second brand colour is not used.

### D.2 Lock summary
| Lock | Paths |
|---|---|
| **DNA** | source type, spine, graphics, caption role and mute policy, presence, comedy off, single theme, the CTA device set, the continuity and canvas-camera modules, every world, layout ids, font slots, caption mechanics, `primary`/`night`/`bad`/`good`, zero overshoot, `max_static_s` 0, hooks, structure, exceptions, tones |
| **TUNE** | grey role hexes (neutral only), caption sizes (CS-B 40–53, CS-A 54–66, CS-A0 60–76) and y (CS-B 1440–1480, CS-A 1340–1420), font families inside their class, motion ±15%, cadence ±15%, duration (micro/short, 20–60 s), energy (calm ↔ balanced), presence share ±10 pts, motif size 30–48 and shape (circle/ring/spark), void glow/vignette/noise |
| **VAR** | accent hex, creator name and handle, language, numbers, the chosen CTA and keyword, formats enabled, brand and series modules, bookend, disclosure wording, sound contract values (cue moments, bed), footage setups, BD/BN additions |
| **NICHE** | §6.4 hook pairs, §8.4 example columns, §14, App. A |

### D.3 Defaulted, changeable later
BV-03 fonts (inside each class) · BV-04 niche (inferred per reel) · BV-06 numbers (from BV-05) · BV-07 captions full ↔ keywords (TUNE) · BV-09 formats (both on; the editor picks F-B when there is no footage) · BV-13 series (off) · BV-14 sponsor wording ("Paid partnership") · BV-15 never-on-screen list (empty) · BV-16 wordmark image (none) · BV-17 duration within 25–55 s.

### D.4 NICHE slots, filled per reel
- §6.4: write the thesis → scene pair for each reel's topic at P7 and append it.
- §8.4: map each new line type to an existing pattern; up to 10 niche patterns may be added over time, built only from families B-1…B-5 and the same monochrome line-art rules.
- §14: after the first approved reel of each format, it becomes that format's worked example.
- App. A: approved thesis lines are added to the bank.
- Glossary: brand and tool names confirmed in captions.

---

## Part E. Template decisions that differ from the analysis or the coverage table
| # | Decision | Evidence and reason |
|---|---|---|
| TD-1 | F-B captions are `full` and `mute_safe` (coverage: `keywords → off`, `sound_on`) | v03 captions run 84% of the reel in 1–4-word groups; v02's caption-less body fails muted viewers (analysis gap D7). The orchestrator asked for captions via `lib:dankoe_b` |
| TD-2 | CS-B is Poppins **500 at 44 px** (lib: 300 at 38; analysis: "~36 px") | Measured from v03: "with endless scrolling" spans 454 px ≈ 43–44 px Poppins Regular. E3 requires weight ≥ 500, so the template uses Medium (Engine request 1) |
| TD-3 | CS-A is EB Garamond **60 px** (lib and analysis: 48) | Measured from v01: "and extremely uncomfortable" spans 691 px ≈ 62 px EB Garamond Regular; 60 px also clears the 54 px default floor, so F-A needs no exception |
| TD-4 | CS-A0 (the cold-open card) is a separate profile at 68 px, y 960 | v01 card phrases measure 518–630 px wide ≈ 68 px; centre y 959 |
| TD-5 | CS-B centre y 1470 (evidence 1543) | NC-5: the evidence sits in the IG bottom band |
| TD-6 | The lone dot stays centred at (540, 960) (analysis: "drops to 80%") | v02 hook sheet @ 0:01.5–0:02.83: the dot stays at the cell centre (y ≈ 960) |
| TD-7 | Object sizes 35–55% of the width, hard limits 15–80% | measured: hammer ≈ 17%, phone 42%, globe 37%, eye 39%, dot field 57%, progress bar 80% |
| TD-8 | Lit objects are engine 3D (`VEOS.fx.three`); the hourglass stays a line-art icon | the lighthouse, sphere and globe in v02/v03 are lit 3D renders; the globe has no landmasses (no geo bundle); one 3D scene at a time for render cost |
| TD-9 | `punct: strip_end` | v01 shows no full stops at chunk ends; trailing commas are also dropped (the engine cannot keep commas and drop full stops) |
| TD-11 | CS-B is `reveal: chunk` + the `wipe` swap, 6 f in / 5 f out, 40 px feather (measured 5–7 f L → R, 4–6 f R → L) | the chunk-level wipe is the measured device (the real chunk is fully visible long before its last word is spoken) |
| TD-12 | T-PUSH-THROUGH's push is 9 f (`dur: 0.3`) | V-CANVAS allows a zoom-through of 0.25 s; the 12 f contraction is drawn in the scene so the camera has one move only |
| TD-10 | `max_gap_s` none in F-A | v01 body is captions over a locked-off take for 33 s: the only weight-1 change in the body is none; requiring one would change the style |

---

## Part F. ID registry (this playbook)
| Prefix | IDs |
|---|---|
| D / BD | D1–D8; BD (buyer) |
| H / N / BN | H1–H16; N1–N14; BN (buyer) |
| E | E3, E4 |
| W | W-void, W-card, W-studio |
| L | L-void, L-card, L-seated |
| G | G-1 card → seated, G-2 seated → end card, G-3 none (F-B) |
| CS | CS-B, CS-A, CS-A0 |
| HA | HA-15 (F-B default), HA-12 (F-A default; F-B alternate), HA-14 (F-A alternate) |
| ST | ST-1, ST-2, ST-3, ST-4, ST-5, ST-6 |
| SM | none (`markers: none`) |
| B | B-1…B-10 |
| P (45) | P-DOT-SELF, P-DOT-ROW-EATEN, P-DOT-GROW, P-DOT-DIM, P-DOT-SOURCE, P-DOT-SEED, P-DOT-AMONG, P-DOT-ORBIT, P-TOOL-STRIKE, P-EMITTERS-CONVERGE, P-EYE-CLOCK, P-HOURGLASS-LOOP, P-CLOCK-SWEEP, P-LADDER-CLIMB, P-SCALE-TIP, P-DOOR-SPILL, P-CHAIN-BREAK, P-MAZE-THREAD, P-ROAD-VANISH, P-WAVE-SETTLE, P-SEED-TREE, P-MIRROR-HORIZON, P-PICTOGRAM-TRIAD, P-BEAM-SWEEP, P-SPIRAL-SPOTLIGHT, P-FLARE-BOWTIE, P-STRIKE-X, P-ZOOM-OUT-ROLL, P-LIT-TOWER, P-GLOBE-TURN, P-LIT-SPHERE, P-DOT-FIELD, P-ICON-SWIRL, P-FEED-PHONE, P-BAR-TO-SCREEN, P-SPLIT-TITLE, P-OBJECT-WORD, P-COLD-OPEN, P-SEATED-HOLD, P-PRODUCT-CARD, P-KEYWORD-CARD, P-HANDLE-CARD, P-QUIET-QUOTE, P-QUIET-PLATE, P-QUIET-SCREEN (+ the bespoke SVG recipes) |
| T | T-MORPH, T-PUSH-THROUGH, T-HANDOFF, T-SINK, T-FLICKER, T-CRT-OFF, T-FLICKER-SWAP, T-COLLAPSE-DOT, T-BLOOM-DISSOLVE, T-BREATH (superseded), T-FOCUS-PULL, T-CARD-CUT, T-END |
| C | C-1, C-2, C-3, C-4, C-6 (C-5 unused) |
| Z | none (`zoom_policy: none`) |
| L-… line types | L-01…L-27 (§8.4) |
| M | M-dot (motif) |
| F | F-B, F-A |
| BV | BV-01, BV-02, BV-05, BV-08 asked; BV-03…BV-17 defaulted |
| V | V-PROFILE, V-F0, V-CADENCE, V-ONWORD, V-SAFE, V-FACE, V-PRESENCE, V-CAPTION, V-TYPE, V-EXC, V-HUES, V-LAYOUT, V-CAMERA, V-CANVAS, V-TITLE, V-PROMISE, V-INSERTS, V-NUMFMT, V-CONTINUITY (pending) |

---

## App. A Headline & hook bank `[NICHE: example]`
Thesis lines (spoken first; F-B captioned, F-A carded). Swap the slot words for the buyer's topic.

**F-B (metaphor animation)**
| # | Thesis line | Archetype | Opening object |
|---|---|---|---|
| 1 | "You weren't born to rent your hours to someone else's dream." | HA-15 | P-ICON-SWIRL → P-EYE-CLOCK |
| 2 | "Every raise you get, your lifestyle quietly eats." | HA-15 | P-DOT-ROW-EATEN |
| 3 | "One skill, sharpened for a year, beats ten you dabble in." | HA-15 | P-TOOL-STRIKE |
| 4 | "YOUR SALARY / IS RENTED TIME" (split title) | HA-12 | P-SPLIT-TITLE + dot row |
| 5 | "Your attention is the only salary you'll never get back." | HA-15 | P-FEED-PHONE |
| 6 | "You don't lack motivation. You lack a default." | HA-15 | P-DOT-SELF → P-LADDER-CLIMB |
| 7 | "Your body is the sum of what you repeat." | HA-15 | P-DOT-FIELD |
| 8 | "YOU DON'T LACK / MOTIVATION" (split title) | HA-12 | P-SPLIT-TITLE + dot row |
| 9 | "The reason you're tired isn't work. It's never switching off." | HA-15 | P-FEED-PHONE → P-HOURGLASS-LOOP |
| 10 | "Life is a game, but you aren't even playing your own level." | HA-15 | P-DOT-ROW-EATEN → P-BAR-TO-SCREEN |

**F-A (seated essay)**
| # | Cold-open line (card, lowercase) | Archetype |
|---|---|---|
| 1 | "the fastest way to get rich is to stop renting your time" | HA-12 |
| 2 | "nobody builds wealth on a schedule someone else wrote" | HA-12 |
| 3 | "you don't need a better job. you need a better question" | HA-12 |
| 4 | "the fastest way to get fit is to change the room you live in" | HA-12 |
| 5 | "discipline is just a decision you stopped re-making" | HA-12 |
| 6 | "your habits are a vote for the person you're becoming" | HA-12 |
| 7 | "most people don't fail. they quietly stop" | HA-12 |
| 8 | "you will never feel ready. that's the point" | HA-12 |
| 9 | "nobody gets rich from a salary" (no card: face at f0) | HA-14 |
| 10 | "you don't need more motivation" (no card: face at f0) | HA-14 |

## App. B Evidence map
The full map (every DNA rule → `vNN @ m:ss`), the measured values and the `(unverified)` list are in `evidence.md`. Key sources: v01 (seated + cold open, 38.1 s), v02 (metaphor animation, 50.3 s, 0 cuts), v03 (metaphor animation + product card, 25.1 s, 0 cuts).
