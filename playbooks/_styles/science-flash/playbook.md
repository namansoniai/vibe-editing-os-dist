# Science Flash Style Playbook (template v1)

**Purpose.** You (Claude) receive a creator's handheld selfie narration of a curious "how does this work / how big is it / what did they find" script, plus the B-roll clips, stills and screenshots they own. Use this playbook to cut a 35–60 s reel in which the host flashes on screen for half a second, then **every sentence gets its own literal picture**, a lime arrow or bracket **points at the exact thing being named**, and one line of bold ALL CAPS captions carries the story to a cliffhanger.

**Input (SW-01 `narrated_footage`).** One or more selfie takes of the whole script (their audio is the voice-over; the picture is used only for host flashes), 12–25 short subject clips per minute that {{BV-01.name|the creator}} owns or holds, optional stills and source screenshots. Missing clips become Claude-built diagrams and scale scenes (§12.3).

### Style DNA `[DNA]`
A science-explainer conveyor belt. Frame 0 is the host mid-gesture, saying two words; by 0.7 s the subject fills the frame and never stops moving. The voice drives the picture: one sentence, one clip, cut on the caption beat; stills, pages and diagrams **land** with a fast pull-back (×1.15–3.7 → 1.0 in ≈ 10–16 f) and then hold. A single neon lime (`#C6F000`, dark-teal edge) is the only colour that isn't the footage's own, and it always means *look here*: a block arrow snapped onto a wing joint, a keyword chip typed over the object, a pin growing on a map, a measure bracket growing beside a person, a lime highlighter on a paper. A tiny credit line sits top-left on every borrowed clip. Captions are white, condensed, ALL CAPS, one line, low on the frame. The reel ends on the next question, with a subscribe sticker tapped by a cursor.

**Copy these 5 things**
1. **Host flash → subject.** 0.5–0.7 s of handheld selfie with the first 2–3 words, then a hard cut to the subject full-frame (§6.2, P-HOST-FLASH). The host returns only as 1.5–2.5 s drop-ins and the closing flash (§3.6).
2. **One-line ALL CAPS condensed captions**, white with a black stroke, 3–7 words, hard swaps, centre y 1470 (§5.3, CS-1).
3. **One lime that points.** Arrows, brackets, pins, chips and labels in `primary` with a dark-teal `edge` outline; nothing else is coloured (§4, §22).
4. **Literal footage.** Every sentence gets its own clip of the exact thing.
5. **Scale made visible + a cliffhanger CTA.** Sizes and amounts are shown against a known object, in two units; the end teases the next question under a scheduled subscribe tap (§5.5, §6.7, §7.1).

### Directives (the style's laws)
| # | Directive | Where it lives |
|---|---|---|
| D1 | **Subject-first stopper.** The host owns frame 0 for 0.5–0.7 s; the subject is full-frame by 0.7 s. No banner, no title card, ever | §6.2, H1, H3 |
| D2 | **One sentence, one picture.** Every caption-length sentence gets its own literal clip, still or diagram, cut on the caption beat. A visual that doesn't show the named thing is wrong | §8.4, H5, N9 |
| D3 | **Captions are the reading line.** ALL CAPS, white, condensed, one line, 3–7 words, cy 1470, hard swaps, never coloured | §5.3, H12 |
| D4 | **One lime, one meaning: look here.** Lime marks the thing to look at. A second hue appears only as the neon-blue glow world or a red hazard/recording HUD | §4, H13 |
| D5 | **Point at it, on the word.** When the voice names a part, place or number, an arrow, bracket, pin or chip lands on that exact spot within ±5 f of the word | §17.2, §22, H6 |
| D6 | **Nothing fetched, ever.** Borrowed clips are the creator's own files; everything else is built | §12.5, §19, H10 |
| D7 | **Scale is literal and dual.** "How big / how heavy / how far" is drawn beside a known object, and the number is shown in both unit systems | §5.5, P-MEASURE, H11 |
| D8 | **Curiosity, not comedy; end on a question.** No memes, no stickers other than the CTA sticker. The last 3–5 s ask the next question and tap subscribe | §6.7, §7.1, H9 |

Buyer directives BD1… `[VAR]` may only make the style stricter or more specific.

### Quick index
| § | What | Status |
|---|---|---|
| §0 | Style profile (switches) | ON |
| §1 | Procedure | ON |
| §2 | Hard rules H1–H16, NEVER N1–N12 | ON |
| §3 | Worlds W-…, layouts L-…, stage moves G-…, safe bands, presenter rules | ON |
| §4 | Colour roles | ON (single theme) |
| §5 | Fonts, chips, plates, hero numbers, caption profile CS-1, number and unit rules | ON |
| §6 | Hook system: HA-10 + 3 variants, alternates HA-13/HA-14, hook pairs, CTA sticker schedule | ON |
| §7 | Structure (explainer + cliffhanger), unit ritual, cadence | ON |
| §8 | Families B-1…B-10, patterns P-… (47), lookup, density | ON |
| §9 | Transitions T-01…T-08 | ON |
| §10 | Motion tokens, zoom policy, layers, finishing | ON |
| §11 | Sound contract | ON (minimal) |
| §12 | Setups, shot list SH-1…SH-7, fallbacks FB-1…FB-7, inserts | ON |
| §13 | Output contract | ON |
| §14 | Worked examples (3) | ON |
| §15 | QA | ON |
| §16 | Frame template / chrome | OFF |
| §17 | Running state & anchored graphics | ON (anchors only) |
| §18 | Data contract | OFF |
| §19 | Evidence & citations | ON |
| §20 | Dialogue | OFF |
| §21 | Canvas camera | OFF |
| §22 | Ink & annotation layer | ON |
| §23 | Continuity | OFF |
| §24 | Series furniture | OFF (VAR) |
| §25 | Sponsor, brand & end cards | OFF (VAR) |
| Parts C–F | Exceptions, personalisation, changes, IDs | ON |
| App. A / B | Headline bank / evidence map | ON |

Format list: **F-A "Science Flash"** (the only format).

---

## §0 Style profile `[REQ]`

```yaml
profile:                         # mirrored in tokens.json → profile
  source_type: narrated_footage
  presenter: {presence: flash, share: [4, 11], max_absence_s: 52}
  spine: audio
  captions: {mode: full, role: support, mute_policy: mute_safe}
  graphics: support
  duration: {class: short, target_s: [35, 60]}
  language: {speech: en, captions: {lang: en, script: Latn, transform: verbatim}, on_screen: en, post_title: en,
             supported: [[en, en, Latn], [hinglish, hinglish, Latn], [hi, hi, Deva]]}
  numbers: {grouping: international, currency: "$", compact: k_m_b, units: dual, decimals: 0}
  tone: {energy: balanced, comedy: off, comedy_max: off}
  themes: {policy: single, packs: [], default: null}
  formats: {list: [F-A], default: F-A}
  footage_dependency: high
  cta: {devices: [subscribe, comment_keyword, link_bio], placement: scheduled, schedule_every_s: 20, chosen: subscribe}
  modules: {chrome: false, running_state: false, anchors: true, data_figures: false, citations: true,
            dialogue: false, canvas_camera: false, ink: true, continuity: false, series: false, brand: false}
```

Why each value:
- **source_type `narrated_footage`**: ≈ 90–95% of runtime is B-roll under a voice; the host is on screen 4–11% (v01 ≈ 7%, v02 ≈ 11%, v03 ≈ 4%). The selfie take is recorded in full so its audio is the voice and its picture supplies the flashes.
- **presence `flash` [4, 11], max_absence_s 52**: v01 is absent from 0:06.6 to 0:57.5 (51 s); share measured 4–11%.
- **spine `audio`**: the voice is the timeline; the picture is chosen per sentence (D2).
- **captions full / support / mute_safe**: captions on ≈ 95% of runtime, every spoken word, one line; the picture still carries the meaning (support), and the story reads muted.
- **graphics `support`**: annotations, chips, diagrams and the sticker illustrate footage; diagram spans are 10–20% of runtime (v01 @ 0:07–0:14, 0:36–0:40).
- **duration short 35–60**: v01 59.1 s, v02 36.7 s, v03 53.7 s.
- **language en → en**: all three are English; Hinglish is supported because ALL CAPS works in Latin script. Devanagari captions are **not** supported (no caps, no condensed Devanagari font).
- **numbers dual units**: "130,000 – 150,000kg / 287,000 – 330,700lb" (v01 @ 0:57), "200m / 656ft" (v02 @ 0:05.8, rolled up live from 10 m).
- **tone balanced / comedy off**: curious, enthusiastic, never mocking; no meme sounds or comedy stickers in any video.
- **themes single**: one lime accent in all three videos.
- **footage_dependency `high`**: the look *is* the creator's footage; the engine can't invent CG creatures, microscopes or LiDAR.
- **cta scheduled subscribe**: 2 sticker taps per video at ~20 s spacing (v01 @ 0:25, 0:57; v02 @ 0:14, 0:35; v03 @ 0:12, 0:52), spoken "SUBSCRIBE!" only at the end.
- **modules**: anchors + ink (arrows at targets inside footage), citations. No chrome, no data figures (numbers are stated, not computed), no series.

---

## §1 Procedure (follow in order) `[REQ] [DNA]`

The craft step of this style is **P8b shot matching + annotation targeting**: one picture per sentence, and the lime mark on the exact pixel of the named thing.

1. **P1 Inventory.** `ffprobe` every input. Identify the selfie narration take(s) (SH-1, setup A) and conform to 30 fps CFR. Register every other file with `veos asset add <file> --origin creator` (videos become frame folders; stills copy). Note each clip's resolution: a 16:9 clip under 1440 px tall may only be cover-cropped full-bleed for ≤ 3 s of motion (§12.4); otherwise it becomes P-BAND-CLIP.
2. **P1b B-roll bank tagging.** Write `plan/broll.md`: one row per clip `{asset, shot SH-4/5/6/7, subject, what's visible, best 2–6 s span, motion, credit text (if third-party), orientation}`. This is the menu for P8b.
3. **P2 Prepare.** No matte (nothing goes behind the host). Skip.
4. **P3 Transcribe** the narration take with word timestamps. Apply `language.captions.transform` (verbatim for en; for hinglish → en, translate per line, keep English terms). Build the glossary (scientific names, places, instruments, units) and add it to `plan/glossary.json`.
5. **P4 Segment** into the explainer units: `HOOK` (0–≈5 s), `LOOP` (the host drop-in line), `COMPARE`, `MECHANISM-1…n`, `PAYOFF`, `CLIFFHANGER` (§7.1). Cut dead air: pauses > 0.35 s become ≈ 0.12 s (`veos cut --tighten` logic on the EDL), except a ≤ 0.4 s held breath before the cliffhanger question.
6. **P5 Classify** every caption-length sentence with a line type (§8.4) and mark its **trigger word** (the noun, number or place the picture must show).
7. **P6 Tone-tag** every sentence: `awe` (scale, reveal), `explain` (mechanism), `warn` (hazard, limit), `win` (payoff, "it works"), `hype` (host drop-in exclamation), `cta`.
8. **P7 Hook plan.** Pick the HA-10 variant (S scale / P place / D difference, §6.2–6.3) from the opening claim. Write **3 hook variants** (first-flash words + the subject shot + the annotation) and run ST-1, ST-2, ST-3, ST-5, ST-6 (§6.1).
9. **P8 Visual plan.** For each sentence: the pattern from §8.4; numbers and units (§5.5); the sticker schedule (§6.7).
10. **P8b Shot matching.** Give each sentence a clip from `plan/broll.md` (the trigger word's subject, the best span). No clip fits → a created visual from FB-4 (§12.3); write which. Third-party clips without creator files → the ask-then-create list (§12.5).
11. **P8c Anchor pass** (§17.2). For every annotated shot: render or sheet the clip's span at 6 fps (`veos sheet plan/assets/<clip> …`), read the target's position frame by frame, and write keyframes `{t, x, y}` in the beat (`anchor`). The arrow tip sits 24 px off the target edge, the arrow body outside the target, never on a face.
12. **P9 Beat sheet** (§13): one beat per sentence or trigger, meeting the cadence (§7.6): a hard cut or annotation event at least every 2.5 s, caption swaps every 0.9–1.6 s.
13. **P10 Sound + transitions.** Cue moments only from §11; the transition map (§9.3); the SFX ledger (S5).
14. **P11 Assets + inserts.** Build created visuals; record every third-party moment in `plan/inserts.json` (origin creator | created).
15. **P12 Checkpoint** (§13.5), then **wait for approval.**
16. **P13 Build** act by act → `veos scenes-meta` → `veos measure` → `veos validate` (global checks + `validator.rules`) → preview and QA (§15, ≤ 3 passes) → render.

---

## §2 Hard rules `[REQ] [DNA]`

### 2.1 Editing rules (every style)
The ten editing rules in `playbooks/_global/GLOBAL-RULES.md` apply. They are directions, not limits: smooth, seamless motion; nothing overlaps by accident; keep the face clear (behind the speaker is fair game, text included); readable at a glance; one idea at a time; show the thing, not the word; say what was said; hook titles hook; pace like the style, not like a timer; the style decides the look.
- **Facts the engine checks:** accidental overlaps, jumps, the face covered, unreadable text, numbers and quotes that don't match what was said, the promised count. Every count, timing and budget this playbook gives is direction for the edit, not a limit.
- **Picture first, in this style's own look:** every key beat shows the thing being said (an object, a screen or app, a diagram, numbers in motion), not just its word; text supports the picture and never replaces it. When the speaker points with words ("this, this and this", "from this to this", "ye dekho"), show what they mean. Illustrations may use made-up but realistic numbers and names ("212 views", "1.2M views"), with no label; a number or quote the speaker says is shown as said. This overrides any rule below that bans made-up numbers or asks for an example tag: those rules now cover claims (the creator's results, prices, benchmarks, testimonials), not illustrations.
- **Hook titles hook:** the on-screen title promises the viewer something (an outcome, a curiosity gap, who it's for) and is true to what the reel delivers; it need not repeat the spoken words. This playbook sets its shape (§5.2, §6.5: lines, sizes, word limits, case), never its voice (§6).
- **Retired (8 Oct 2026), whatever this playbook says below:** no REPRESENTATIONAL or example labels on made-up cards, no credit lines, no flash limit (flash as often as this style calls for; any "NC-11" cap below no longer applies), and text may sit behind the speaker without an exception.

### 2.2 Declared exceptions
**E3 Quiet type (audit 2026-10):** CS-1 captions are **48 px** (floor 46 px), Barlow Semi Condensed 700, one line, ≤ 30 characters, white with a 2 px black stroke (contrast ≥ 7 : 1 on any footage). The source caption is ≈ 45–47 px (cap height 31 px, 23.6 px per character, v01 @0:19, v03 @0:01); 60 px read clearly heavier than Cleo's. Credit lines are `TC-legal` (24 px, not counted in G2), hard caption swaps are exempt from G3 as subtitles, and nothing sits behind the host.

### 2.3 MUST rules
- **H1 Frame-0 stopper.** f0 shows the host mid-gesture (hand moving toward the lens or waving) on L-host with caption chunk 1 (the first 2–3 words) on screen; no headline, chip or sticker at f0. *check: V-F0*
- **H2 Cadence.** Body: 4–8 weighted state changes per 10 s (captions weigh 0.5); a weight-1 change (cut, annotation entry, scene event) at least every 2.5 s (1.5 s in the hook); nothing static > 1.5 s (moving B-roll runs its own motion; a held still or page needs an event: wipe, punch, mark, highlight, inside every 1.5 s). *check: V-CADENCE*
- **H3 Subject by 0.7 s.** A `kind: "subject"` scene (full-bleed clip, still or created subject visual) fills the frame by 0.70 s. *check: V-F0 (HA-10 payoff)*
- **H4 Headline limits.** There is no banner. Chips ≤ 3 words; title plates ≤ 6 words on ≤ 2 lines; each holds ≥ words × 0.25 s and ≥ 10 f after it finishes typing. *check: V-TITLE*
- **H5 One sentence, one picture.** Each caption-length sentence (or its trigger) starts a new clip, still, diagram state or annotation; no B-roll shot stays > 4.0 s without a new annotation event or cut. *check: V-CADENCE + review*
- **H6 On the word.** The picture of the trigger word cuts in 2 f before it; its annotation lands within ±5 f of it. *check: V-ONWORD*
- **H7 Face.** On L-host, nothing but the caption may sit within 40 px of the face box; the sticker sits below the chin (§6.7); arrows never point at a face. *check: V-FACE*
- **H8 Presence.** The host is on screen 4–11% of runtime: the f0 flash (0.5–0.7 s), 1–2 drop-ins (1.5–2.5 s each), the closing flash (0.6–0.8 s, measured 0.61–0.73 s); the longest absence ≤ 52 s. *check: V-PRESENCE*
- **H9 Promise integrity.** Every "look at this / watch this" is followed by the thing within 1 s; the cliffhanger asks a question the reel doesn't answer and the sticker is on screen when "SUBSCRIBE / FOLLOW" is said; a comment keyword (when chosen) is on screen ≥ 1.5 s. *check: V-PROMISE*
- **H10 Inserts.** Every third-party picture is a creator-supplied file or a created substitute; recorded in `plan/inserts.json`. *check: V-INSERTS + V-CITE*
- **H11 Numbers.** Every number on screen is said in the script; measures appear in both unit systems (metric first for `international`, the spoken system first otherwise), written by `ctx.fmtNum`. *check: V-NUMFMT*
- **H12 Captions.** CS-1 only: ALL CAPS, 1 line, ≤ 28 characters, ≤ 7 words, hard swaps, sync ≤ 0.15 s lead, glossary spellings exact. *check: V-CAPTION*
- **H13 Hues.** ≤ 2 bright hues per frame: lime + at most one of {accent blue (glow world, hand arrow), bad red (hazard chip, REC HUD)}. *check: V-HUES*
- **H14 Safe bands.** Meaning text inside x 64–1016, y 110–1500; nothing in the right column x > 970 between y 900–1540; captions in the band y 1420–1492. *check: V-SAFE*
- **H15 Dead air.** Spine `audio`: ≤ 1 pause ≥ 150 ms per 15 s, except one ≤ 0.4 s held breath before the cliffhanger question; picture keeps moving during any pause. *check: review*
- **H16 Audio and determinism.** −14 LUFS, true peak ≤ −1.5 dBTP, hard end ≤ 6 f after the last word (NC-8); every scene a pure function of the frame (NC-9). *check: review + engine*

### 2.4 NEVER
- **N1** A banner, slab, title card or lower-third over the hook. The first words are the caption.
- **N2** Generic stock that isn't the subject: glowing brains, spinning globes for "science", abstract particles, lab-coat stock, "Matrix" code. If the clip doesn't show the named thing, build a diagram instead.
- **N3** Coloured caption words, caption pills, caption boxes or karaoke. Emphasis lives in chips and labels, never in the caption.
- **N4** Lime on lime-ish footage without the edge: lime text or arrows always carry the 5–6 px `edge` outline; on green/yellow footage (lime contrast < 3:1) the chip turns `bad` red (P-ALERT-CHIP).
- **N5** More than 3 ink marks on screen, or two arrows pointing at the same thing.
- **N6** Comedy: meme sounds, reaction stickers, emoji stickers, crash zooms, freeze-frame roasts.
- **N7** Zoom presets on the host footage (snap punches, crash zooms, rotation snaps). The handheld selfie already moves.
- **N8** Transitions outside T-01…T-09: no whip pans, glitch packs, film burns, light leaks, spins.
- **N9** A clip that only decorates, or a clip shown while the voice talks about something else for > 0.5 s.
- **N10** A fetched picture: no downloaded stills, screenshots or clips; no masthead logos. Created cards set the outlet name in type.
- **N12** Numbers the script doesn't say, fake precision ("37.2%" when the voice says "about a third"), or a measurement in one unit only.

Buyers may add BN1… `[VAR]`.

---

## §3 Worlds, layouts, stage moves, safe zones `[REQ] [DNA; coordinates TUNE ±5%]`

### 3.1 Worlds
| ID | Kind | Look | Carries | Enter / exit |
|---|---|---|---|---|
| **W-host** | footage | The creator's own room on a handheld selfie (shelf, plant, window light), not regraded | f0 flash, drop-ins, closing flash | T-01 hard cut in and out |
| **W-void** | void | `#000000` | Footage that sits on black (microscopy, space, night shots, P-BAND-CLIP sides), P-SPLIT-REVEAL | T-01 |
| **W-grid** | stage | Charcoal `#2A2B34`, 2 px grid lines `#4A4D5E` at 85% every 120 px, vignette 0.22 | Real-looking specimens side by side (P-VS-STACK), scale lineups, silhouettes | T-01 in; T-07 to W-glow |
| **W-glow** | stage | Navy radial gradient `#16207A` (centre x 540, y 860) → `#060A2C`, vignette 0.35 | The "x-ray" version of the same diagram: neon-blue `accent` outlines with an 18 px glow, white bones/lines, lime or white labels | T-07 from W-grid; T-01 out |
| **W-paper** | paper | `#FFFFFF` | Paper pages, quotes, figure cards, map figures (black serif type, lime highlighter) | T-01 |

The B-roll itself is not a world: it is a full-bleed scene at z1 (P-BROLL-FULL) on top of W-void.

### 3.2 Layout library
| ID | Engine | Presenter rect | Graphic rect | Caption | Share (F-A) |
|---|---|---|---|---|---|
| **L-host** | `full` | 0, 0, 1080 × 1920 (handheld selfie as shot) | none (only the caption and, at the end, the sticker) | fixed_y cy 1470 | 4–11% |
| **L-evidence** | `hidden` | none | 0, 0, 1080 × 1920: the full-bleed clip or still at z1, ink at z5–6 | fixed_y cy 1470 | 55–92% |
| **L-diagram** | `hidden` | none | x 64–1016, y 160–1240 on W-grid / W-glow / W-paper / W-void | fixed_y cy 1470 | 4–35% |

**Layout schedule rule:** L-host runs are 0.45–2.6 s (min 0.45 s so the flash reads; max 2.6 s, the longest evidence drop-in, v02 @ 0:22–0:24.5). Every switch lands on a sentence boundary or a pause (`layouts.schedule.switch_on: sentence, pause, but`).

### 3.3 Stage moves
| ID | Move | Recipe (30 fps) | Use |
|---|---|---|---|
| **G-1** | Flash-out | `stage: {layout: L-evidence, via: cut}` on the word boundary after the 2nd–3rd word, 0.50–0.70 s; the subject scene's `t_in` is the same frame | f0 flash → subject |
| **G-2** | Drop-in | `via: cut` into L-host on the first word of the drop-in line; out with `via: cut` on its last word + 2 f | The loop line, a reaction ("so many more!") |
| **G-3** | Closing flash | `via: cut` into L-host on the CTA verb's sentence; hard end ≤ 6 f after the last word | "…SUBSCRIBE!" |

There are no splits, PiPs, cards or morphs between the host and the footage (evidence: full-frame only). The host never shares the frame with B-roll.

### 3.4 Layout diagrams
```
L-evidence (and L-diagram)              L-host
┌─────────────────────────┐ 0          ┌─────────────────────────┐ 0
│ (IG top UI)             │ ← 0–110    │ (IG top UI)             │
│• SOURCE: …  (credit)    │ ← y 140–170│      ╭───────╮          │ ← head top y 180–420
│                         │            │      │ face  │  ✋       │   (handheld, arm's length)
│   ANNOTATION BAND       │ ← y 160–   │      ╰───────╯          │
│   arrows, brackets,     │   1240     │                         │
│   pins, chips, labels   │            │      torso              │
│   (on the target)       │            │                         │
│                         │            │ ┌──────────────┐        │ ← sticker only at the end:
│ ┌─────────────┐         │ ← sticker  │ │  SUBSCRIBE ☝ │        │   cx 540, cy 1320, 440×120
│ │ SUBSCRIBE ☝ │         │   y 1260–  │ └──────────────┘        │
│ └─────────────┘         │   1380     │                         │
│ WAS AS BIG AS A BUS,    │ ← caption  │ THIS ANIMAL             │ ← caption cy 1470
│                         │   cy 1470  │                         │
│ (IG bottom UI, no text) │ ← y > 1540 │ (IG bottom UI)          │
└─────────────────────────┘ 1920       └─────────────────────────┘ 1920
```

### 3.5 Safe zones and bands
| Band | y range | What may live there |
|---|---|---|
| IG top | 0–110 | nothing |
| Credit line | 130–176 (text top 140), x from 64 | `TC-legal` credit only |
| Annotation | 160–1240, x 64–1016 (x ≤ 970 below y 900) | arrows, brackets, pins, chips, labels, plates, hero numbers, diagrams |
| Sticker | 1260–1380 | the CTA sticker (cx 540, cy 1320) only |
| Caption | 1420–1492 | CS-1 captions only |
| IG bottom | > 1540 | nothing readable |

Diagram and footage pictures may run full-bleed behind these bands; text may not leave them.

### 3.6 Presenter rules `[COND: presence ≠ none]`
- **Share 4–11%**, longest absence ≤ 52 s. A 35–45 s reel: f0 flash + 1 drop-in + close. A 45–60 s reel: f0 flash + 1–2 drop-ins + close.
- **Returns** are hard cuts only (G-2, G-3), always on a sentence start, always with a big gesture or facial reaction (the reason to cut back).
- **Crop:** as shot. Head top y 180–420; face height 22–34% of frame (arm's length). If the take is wider (face < 18%), crop centred on the face up to 1.25× (a 1080p source allows ≤ 1.35×).
- **What sits over the host:** the caption (cy 1470, chest) and, on the closing flash only, the sticker (cy 1320, below the chin; if the face box bottom is lower than y 1220, put the last sticker on the preceding B-roll beat instead). Nothing behind the head (E1 not used).

---

## §4 Colour `[REQ] [meanings DNA; brandable hex VAR]`

### 4.1 Role palette
| Role | Hex | Its one job | Text on it | Contrast | Lock |
|---|---|---|---|---|---|
| `primary` **Lime** | `{{BV-02.primary|#C6F000}}` | *Look here*: block arrows, keyword chips, typed keywords, diagram labels, map pins, ? marks, measure tags, hero numbers, the sticker, the highlighter on paper, the credit dot | `edge` | 8.6:1 | VAR (brandable) |
| `accent` **Neon blue** | `{{BV-02.accent|#2F6BFF}}` | Second voice, rare: neon outlines + glow in W-glow, the hand-drawn marker arrow (P-HAND-ARROW) | `paper` (large only) | 4.5:1 | VAR (brandable) |
| `edge` **Dark teal** | `#17454A` | The 5–6 px outline and hard shadow of every lime element; the text colour on lime | `paper` | 10.2:1 | TUNE (dark) |
| `bad` **Alarm red** | `#FF3B30` | A named hazard or limit, the REC HUD and trace markers, and the chip fill when lime would vanish on green/yellow footage | `paper` with a 4 px `edge` stroke | 3.6:1 (+ halo) | fixed |
| `good` **Check green** | `#3DDC84` | A ✓ on the payoff only (≤ 1 per reel) | `ink` | 11:1 | fixed |
| `paper` | `#FFFFFF` | Caption fill, measure brackets, dimension arrows, unit sub-lines, the paper world | — | — | DNA |
| `ink` | `#0A0A0A` | Caption stroke, serif text on paper | — | — | DNA |
| `night` | `#060A2C` | W-glow floor | — | — | TUNE |
| `grid` / `gridline` | `#2A2B34` / `#4A4D5E` | W-grid | — | — | TUNE |

Measured in the evidence: lime `#C6F000`, teal outline `#17454A`, diagram grid ≈ `#2A2B34`, neon blue `#2F6BFF` / `#1E5BFF`, red `#FF3B30` (App. B).

### 4.2 Meanings
- **Lime = look here.** The single accent. Its shape says what kind of "here": an arrow is a part, a bracket is a size, a pin is a place, a chip is the word to remember, a ? is the unknown.
- **Blue = the inside view.** Only in the glow world (the x-ray of the same diagram) and as the hand-drawn second arrow when a lime arrow is already on screen.
- **Red = hazard or recording.** A warning term, a REC HUD, trace markers. Never "wrong answer" theatre.
- **The footage keeps its own colours.** No grade, no LUT, no tint.
- **Brand colours** of products appear only inside the creator's own footage.

### 4.3 Theme packs
OFF: `themes.policy = single` (one lime in all three videos). A buyer's BV-02 colour replaces lime everywhere.

### 4.4 Grades
OFF: footage is never regraded. Created worlds are flat colour (W-grid and W-glow carry their own vignette).

### 4.5 Rules
- **≤ 2 bright hues per frame** (`max_bright_per_frame: 2`): lime + one of {blue, red}. Never blue and red together.
- Every lime element has the `edge` outline (5–6 px) and a hard `edge` shadow 0/+6 px, no blur. This keeps lime readable on bright skies and white paper.
- On W-paper, lime is only a highlighter behind black serif text (the text stays `ink`), never lime text.
- A chip on green or yellow footage (lime vs the footage around the chip < 3:1) switches to `bad` red with white text and a 4 px `edge` stroke (P-ALERT-CHIP; evidence v02 @ 0:11 "LiDAR").
- **Must match `tokens.json`.**

---

## §5 Type & captions `[REQ]`

### 5.1 Font map
| Slot | Family | Weight | Font class (TUNE boundary) | Used for |
|---|---|---|---|---|
| `caption` | **Barlow Semi Condensed** | 600 | condensed sans 600–700, caps | CS-1 captions |
| `display` | **Archivo Black** | one black weight | heavy wide grotesque | chips, typed keywords, diagram labels, title plates, the sticker |
| `numeric` | **Montserrat** | 900 | heavy wide grotesque | hero numbers, dimension tags |
| `body` | **Inter Tight** | 600–700 | neutral grotesque | credit lines, unit sub-lines, leader labels, plate sub-lines |
| `serif` | **Source Serif 4** | 400 / 700 | text serif | created paper and quote cards |

Measured faces: captions ≈ a semi-condensed DIN-like caps face (bundled: Barlow Semi Condensed, which replaces the earlier Barlow Condensed stand-in); chips and labels ≈ Archivo Black (bundled: the `display` slot); credit ≈ a small neutral sans. Brand wordmarks appear only inside the creator's own footage.

### 5.2 Headline element: the lime chip `[DNA recipe; NICHE text]`
There is **no banner**. The style's title device is the **keyword chip** (`type.headline.kind: chip`), with the **title plate** as its two-line variant.

| Property | Chip (P-KW-CHIP) | Title plate (P-TITLE-PLATE) |
|---|---|---|
| Fill | `primary` lime, radius 14, padding 8/24 | none (lime text on the footage) |
| Text | Archivo Black, **76 px** (64–84), ALL CAPS, `edge` colour | Archivo Black, **84 px** (72–96), ALL CAPS, lime, line height 1.0, 5 px `edge` stroke |
| Stroke / shadow | 5 px `edge` border; hard shadow 0/+6 px `edge` | stroke + 0/+6 px `edge` shadow |
| Sub-line | — | Inter Tight 600, 44 px, white (a date range or place: "~600 BCE – 850 CE") |
| Words / lines | ≤ 3 words, 1 line | ≤ 4 title words on ≤ 2 lines + the sub-line; ≤ 6 words in total |
| Position | Over the object, on its anchor; centre x 200–880, y 260–1180 | Upper third: centre y 520–760 |
| f0 | Never at f0 | Never at f0 |
| Entry | Typed: one letter per frame from the left (9–14 f), the box grows with the text; a 7 f pop (0.6 → 1.08 → 1.0) for ≥ 15 letters | Line 1 types; line 2 types 4 f after; the sub-line rises 12 px + fades in over 8 f, 6 f after line 2 |
| Life | Holds still; 1 pulse (1.0 → 1.06 → 1.0, 6 f) if the word is said again | Holds |
| Lifetime | `section`: until the shot cuts (≥ 1.0 s and ≥ words × 0.25 s + 10 f) | Until the shot cuts (≥ 1.5 s) |
| Exit | Fades out over 4 f on the next cut | Fades out over 4 f |

Evidence: "250 NANOMETERS" (v03 @ 0:09), "GEOGLYPHS" typed (v02 @ 0:04), "AQUIRY CIVILIZATION / ~600 BCE – 850 CE" (v02 @ 0:26–0:28).

### 5.3 Caption profile CS-1 (extends `lib:cleo`) `[DNA mechanics; size & y TUNE; language VAR]`
| Group | Value |
|---|---|
| Mode | `full` / `support` / `mute_safe` |
| Chunking | `unit: line`; **1–7 words** (target 3–6); **1 line**; ≤ **28 characters**; never split a name, number or unit; break on `, . ! ? …` and on pauses ≥ 0.6 s; a one-word chunk only for an exclamation ("SUBSCRIBE!") |
| Timing | Lead 2 f; min hold 0.25 s per word; **hard swap** (0 f); `pause_hold_s` 0.4 (a chunk may hold 0.4 s into a pause, then clears); tail 0.12 s |
| Skin | **Barlow Semi Condensed 700, 48 px** (TC-subtitle under E3; TUNE 46–56), **UPPER**, tracking 0 (letters nearly touch), `paper` white, **2 px black stroke**, shadow 0/+3 px rgba(0,0,0,.55); no container |
| Position | `fixed_y`, **centre y 1470** on every layout (TUNE 1440–1474; the source sits at 1518, inside the y > 1500 band), centred, max width 952; `avoid_face` on |
| Punctuation | Kept as spoken: commas, "…", "!" ("WAS AS BIG AS A SCHOOL BUS,", "HIDDEN IN THE AMAZON…", "AND THIS!") |
| Emphasis | `none`. The caption is never coloured; the keyword goes into a chip (§5.2) |
| Hide | Never hidden (the black stroke keeps it readable even on the whiteout) |
| Speakers | n/a (one voice) |
| Language | Latin script only; English terms verbatim; the glossary from P3; profanity masked `inner` (S**T) |

**Measured vs template (audit 2026-10, full-res):** the caption cap height is 31 px (≈ 45–47 px font), centre y 1518, bold, tight, thin 2 px stroke (v01 @0:02, @0:19; v02 @0:02; v03 @0:01). The template keeps its size under E3 at **48 px** and lifts it only to **cy 1470**, so its bottom (≈ 1496) clears the y 1500 band. One line: 28 caps at 48 px ≈ 640 px wide (the source's 27-character line is 637 px).

### 5.4 Other text systems
| ID | Element | Class | Recipe | Hold |
|---|---|---|---|---|
| **TX-1** | Typed keyword on footage (P-KW-WORD) | TC-display | Archivo Black, 96 px (84–120), lime, 6 px `edge` stroke, 0/+6 shadow, no box; types 1 letter per 2 f with a white flare on the newest letter (v02 @ 0:04.3–4.8) | ≥ 1.0 s |
| **TX-2** | Diagram label | TC-display (inside a diagram = one element) | Archivo Black, 80 px (64–100), lime; the active label turns white and scales 1.25 | the diagram's span |
| **TX-3** | Leader label (P-LEADER-LABEL) | TC-label | Inter Tight 700, 44 px caps, white with a 3 px black stroke, + a 3 px white leader line to the target; sub-line 40 px | ≥ 1.0 s |
| **TX-4** | Dimension tag (P-DIM-LABEL) | TC-label | A lime pill, Montserrat 800 48 px `edge` text ("176 M") + the other unit beneath in Inter Tight 600 44 px white with a black stroke ("578 FT"); rotated to the dimension's angle (±35° max) | ≥ 1.2 s |
| **TX-5** | Hero number (P-HERO-NUMBER) | TC-display | Montserrat 900, 96 px (84–140), lime, 5 px `edge` stroke; the unit line in Inter Tight 600 44 px white (the other system); a white 8 px bracket beneath | ≥ 1.5 s |
| **TX-6** | Credit line (P-CREDIT-LINE) | **TC-legal** | Inter Tight 600, **24 px**, caps, tracking +0.04 em, white at 75%, a lime asterisk "*" (the source uses an asterisk, not a dot) + "SOURCE: ", x 64–96, text top y 100–150 (measured v01 @0:02 x 96 / y 156, v02 @0:02 x 75 / y 98: keep y ≥ 140 for the IG top band); **on from the cut frame** (no fade, v01 @ 0:01.97, v03 @ 0:00.63) and kept without re-entry across consecutive clips of the same source (v01 @ 0:03.87) | the whole shot |
| **TX-8** | Sticker word (P-SUBSCRIBE-TAP) | TC-display | Archivo Black, 56 px, `edge` text on a 440 × 120 lime button | ≈ 2.4 s incl. the 1 s fade (S3 to the end) |
| **TX-9** | REC HUD (P-REC-HUD) | TC-label | "REC" Montserrat 900 56 px white + a 44 px `bad` dot with a 4 px white ring, top-centre y 210 | the shot |
| **TX-10** | Paper body text | TC-decorative | Source Serif 4 400, 44 px, black; always next to a highlighted, readable span | the card |

### 5.5 Language and number rules
- **Spelling:** English and scientific names exact (glossary). Species, instruments and places are written in captions as spoken, and in chips and labels in their canonical spelling (a case-sensitive term such as "LiDAR" keeps its case in a chip).
- **Grouping:** international (`130,000`) by default; Indian (`1,30,000`) when BV-05/BV-06 sets an Indian language.
- **Dual units (DNA).** Every length, mass, volume, temperature and speed shown on screen carries both systems: the spoken unit first, the other beneath (graphics) or in brackets (chips). Written by `ctx.fmtNum(v, {unit, units: "metric"})` and `ctx.fmtNum(v, {unit, units: "imperial"})`; one decimal for converted values under 100. Units below a millimetre (µm, nm) have no everyday imperial pair: they stay metric only, with a familiar comparison instead ("1/1000 OF A HAIR").
- **Ranges** use a spaced en dash: "130,000 – 150,000 KG".
- **Approximations** keep the speaker's hedge: "~600 BCE", "ABOUT 250 NM".
- **Currency:** `$` by default; `₹` with Indian grouping for Indian-language copies. Money is never converted.
- **Captions** show a number as spoken (digits for 10 and up, words for one to nine); graphics always show digits.

---

## §6 Hook system `[REQ]`

**Hook title (every style, 8 Oct 2026; above anything below):** the on-screen title promises the viewer something: an outcome they want, a curiosity gap, or who it's for ("How to go viral as a doctor creating content", not the label "Reels for Doctors"). It doesn't have to repeat the spoken words; it has to be true to what the reel delivers. A title shown as someone's words (in quotes) is still word for word. This section sets the title's shape (lines, sizes, word limits, case, the keyword device), never its voice. Write 8–10 candidates from the formulas below plus the proven patterns ("How to X as a Y", "Why your X isn't working", "The X nobody tells you", "Stop doing X", "Your X vs mine", a number or a contrast), score them on outcome, curiosity, who it's for and brevity, check the best against the stopper tests, and pick; any "write 3" below means this, and the next two go to the storyboard as alternates. A style with no on-screen title applies this to its post title.

### 6.1 Stopper tests
| Test | This style's number |
|---|---|
| **ST-1 Thumbnail** | f0 at 25%: the host's face (≥ 22% of frame height) mid-gesture + the caption (48 px → 12 px) is legible as a line |
| **ST-2 Mute** | The captions alone tell the claim by 3 s ("THIS ANIMAL / WAS AS BIG AS A SCHOOL BUS,") |
| **ST-3 Motion at f0** | The handheld hand is moving on f0 (a wave or a reach toward the lens) |
| **ST-5 Change count** | ≥ **6** weighted state changes in 0–3 s |
| **ST-6 Payoff-by** | The subject is full-frame by **0.70 s** |
| ST-4 Read time | n/a: no headline in the hook |

### 6.2 Default archetype: HA-10 Host flash → subject (variant S, scale reveal)
Spoken pattern: "[THIS SUBJECT] / [was as big as / could …] [a familiar comparison], / [a second fact], / and [did it in a really surprising way]!"

| t (s) | Frames | Beat | Visual | Caption (CS-1) | Layout / motion | Cue? |
|---|---|---|---|---|---|---|
| **0.00–0.60** | f0–f17 | Host flash | L-host. The host on a handheld selfie, mid-gesture (an open hand moving toward the lens), saying the first 2–3 words | "THIS ANIMAL" (chunk 1 at f0) | No zoom; the handheld sway is the motion | — (dry first frame) |
| **0.60** | f18 (±3 f, on the word boundary after word 2–3) | Cut to subject | **G-1 hard cut** to the subject full-bleed (P-BROLL-FULL, `kind: subject`); **P-LAND** ×1.13 → 1.0 over 16 f (expo-out) | Hard swap to the claim: "WAS AS BIG AS A SCHOOL BUS," | L-evidence | **Hook cue** on the cut |
| 0.60–1.03 | f18–f31 | Scale proof | **P-MEASURE:** starting on the cut frame, a white 8 px arrow-line grows from the ground line to the top of the subject (13 f, ease-out) while the shot lands, beside a person or known object in the shot (anchor pass) | holds | — | Reveal cue when the line tops out |
| 0.60 | f18 | Credit | P-CREDIT-LINE on with the cut (only on a third-party clip) | — | — | — |
| 1.47–1.93 | f44–f57 | Hold | The bracket holds; the push continues | holds | — | — |
| **1.93** | f58 (±9 f, on the next clause) | Second fact | Hard cut to the second clip (same subject, new angle) | "MAY HAVE WEIGHED" → "AS MUCH AS A GRIZZLY BEAR," | — | — |
| 2.10–3.00 | f63–f90 | Point | **P-LIME-ARROW** lands on the feature the line names (pops on in 1 f, nudges 20 px in over 6 f), then holds | swaps on the comma | — | Reveal cue on landing |
| 3.0–4.8 | — | Proof run | 1–2 more one-line clips, each with its annotation (P-ARROW-HOP, P-KW-CHIP) | one chunk per clip | — | ≤ 1 cue |
| **4.8–6.6** | — | Loop drop-in | **G-2 drop-in** to the host (1.5–2.0 s), a big reaction on the open-loop line | "AND DID IT IN A REALLY FREAKY WAY!" | L-host | — |
| 6.6 | — | Into COMPARE | Hard cut to the diagram world (P-VS-STACK) | next chunk | L-diagram | Transition cue |

**SC count 0–3 s (weighted):** cut 0.60 (1) + caption 0.60 (0.5) + bracket enters (1) + credit enters (1) + cut 1.93 (1) + caption (0.5) + arrow enters (1) + caption swap ≈ 2.5 (0.5) = **6.5 ≥ 6**.

**Never** hold the flash beyond 0.9 s, never put a chip, plate or sticker on the flash, never open on B-roll with the host coming later (that is HA-14, an alternate with its own rule).

### 6.3 Variants and alternates `[DNA list; VAR choice per reel]`
**HA-10 variants** (the same 0.0–0.7 s; the reveal differs):

| Variant | Use when the opening claim is about… | 0.6–2.6 s reveal | Evidence |
|---|---|---|---|
| **HA-10.S Scale** (default) | how big / heavy / far / fast | P-MEASURE or P-DIM-LABEL on the subject beside a known thing | v01 @ 0:00.67–0:01.8 |
| **HA-10.P Place** | where something was found / happens | P-PLACE-DOLLY on a map or aerial (1.0 → 1.5 with a −15° roll over 21 f) + P-MAP-PIN grow at 0.75 s with a ripple; cut at ≈ 1.75 s to the close-up with a P-LIME-ARROW | v02 @ 0:00.58–0:02.6 |
| **HA-10.D Difference** | before/after, old vs new, blurry vs sharp | Image A in the top half on black ("BETWEEN THIS…"); at 1.3 s image B wipes in below from the seam (T-02, 9 f) ("AND THIS!"); at 2.46 s P-SNAP-PUSH, a 0 f punch-in cut ×2.46, on "BOTH" | v03 @ 0:00.62–0:02.5 |

**HA-10.P**
| t | Visual | Caption |
|---|---|---|
| 0.00–0.55 | Host flash, hand toward the lens | "THEY FOUND SOMETHING" |
| 0.58 | Cut to the aerial or map of the region; the place name set in type, tilted to the ground plane; P-PLACE-DOLLY starts | "HIDDEN IN [PLACE]…" |
| 0.75 | P-MAP-PIN grows from its tip (0 → 1, 8 f) + a ripple ring (18 f) on the exact site; the map keeps dollying | holds |
| 1.75 | Cut to the close-up of the find; credit line | "[HUNDREDS OF …]" |
| 1.95 | P-LIME-ARROW pops onto the structure, nudges 20 px in, holds | holds |
| 2.6 | T-04 state swap: the same frame in another render (colour map, night/day, x-ray) + a second arrow | next chunk |

**HA-10.D**
| t | Visual | Caption |
|---|---|---|
| 0.00–0.60 | Host flash, a frown and a reach toward the lens | "LOOK AT THE DIFFERENCE" |
| 0.62 | Cut to W-void: image A in the top half (y 260–760), credit line | "BETWEEN THIS…" |
| 1.30–1.60 | T-02 seam wipe: image B draws in below the seam (y 760–1240) | "AND THIS!" |
| 2.46 | P-SNAP-PUSH: punch-in cut ×2.46 on the seam (0 f) | "BOTH IMAGES" |
| 3.5–5.0 | P-HAND-ARROW (accent blue) draws from A down into B | "BUT THIS ONE WAS TAKEN WITH A" |

**Alternates (other archetypes)**
| ID | When | Recipe | Rule |
|---|---|---|---|
| **HA-13 Cold action** | The single best clip is an action (a launch, a collapse, an animal taking off) and the opening words describe it | f0 = the action clip moving + caption chunk 1; first cut ≤ 2.1 s; the host drop-in at 3–6 s carries the loop line | ≤ 1 reel in 4 |
| **HA-14 Cold authority** | The script opens mid-thought on one striking image ("This is the sharpest picture of a cell ever taken.") | f0 = the strongest still or clip + the caption; the strongest image by 1.0 s; the host drop-in by 6 s | Only when SH-2 is unusable and FB-2 has no gesture |

### 6.4 Hook pairs by topic `[NICHE]` (pair type: subject → reveal)
| Niche | Topic | Flash words (0.0–0.6 s) | Reveal by 0.7–2.0 s | Variant |
|---|---|---|---|---|
| Tech & AI `[NICHE: example]` | Data-centre scale | "THIS BUILDING" | Aerial of the data centre; P-DIM-LABEL along its length in m / ft; a person silhouette for scale | S |
| Tech & AI | Chip transistors | "THIS CHIP" | Macro of the chip; P-SNAP-PUSH into the die; P-KW-CHIP "[N] BILLION SWITCHES" | S |
| Tech & AI | Phone night mode | "LOOK AT THE DIFFERENCE" | The dark, noisy photo (top) → the night-mode photo (bottom), seam wipe | D |
| Tech & AI | Undersea cables | "THEY RUN UNDER THE OCEAN" | Map dolly + pins at both landing stations; P-DIM-LABEL along the route in km / mi | P |
| Tech & AI | GPU heat | "THIS GETS HOTTER THAN" | The thermal clip; P-HERO-NUMBER °C / °F beside a familiar object | S |
| Tech & AI | Satellite internet | "THERE ARE THOUSANDS" | Night-sky clip; P-QMARK-SWARM → the dots resolve into satellites; P-LIME-ARROW on one | S |
| Food & health science `[NICHE: example]` | Sugar in a soda | "THIS CAN" | The can beside a stack of sugar cubes; P-MEASURE up the stack; P-HERO-NUMBER g / oz | S |
| Food & health | Gut bacteria | "INSIDE YOUR GUT" | Microscope clip; P-KW-CHIP "TRILLIONS"; P-LIME-ARROW on one cell | S |
| Food & health | Muscle growth | "LOOK AT THE DIFFERENCE" | Muscle-fibre still before (top) → after (bottom), seam wipe | D |
| Food & health | Where coffee grows | "EVERY CUP STARTS HERE" | Map dolly to the growing belt + pin; P-DIM-LABEL altitude in m / ft | P |
| Food & health | Sleep and the brain | "WHILE YOU SLEEP" | Brain-scan still; P-OUTLINE-TRACE around the region named; P-KW-CHIP with the region's name | S |
| Food & health | Chilli heat | "THIS PEPPER" | Macro of the pepper; P-HERO-NUMBER in heat units beside a bell pepper at 0 | S |

The editor appends a row per reel at P7 (Part D.3).

### 6.5 Headline writing (the first words) `[DNA formula; NICHE examples]`
There is no banner, so the "headline" is the **flash line + the claim chunk**:
- **Flash line (chunk 1, f0):** 2–3 words, a demonstrative ("this") or "they / look" + the subject: "THIS ANIMAL", "THEY FOUND SOMETHING", "LOOK AT THE DIFFERENCE", "THIS CHIP", "INSIDE YOUR GUT".
- **Claim chunk (chunk 2, 0.6 s):** the size or novelty claim against something familiar, ≤ 7 words: "WAS AS BIG AS A SCHOOL BUS,", "HIDDEN IN THE AMAZON…", "BETWEEN THIS…".
- **Loop line (drop-in, 4.8–6.6 s):** an exclamation that promises a mechanism: "AND DID IT IN A REALLY FREAKY WAY!", "THAN WE EVER KNEW ABOUT!".
- **Post title (App. A):** "How This [Thing] Could [Verb]", "They Found Something Hidden In [Place]", "This [Instrument] Is Insane". Title case.
- **Banned:** "You won't believe", "scientists are baffled", a claim the reel doesn't show, a comparison object the clip doesn't show, emoji in captions.
- Write 3 hook variants and pick by ST-2 (the mute read) and ST-6 (subject by 0.7 s).

### 6.6 Hook sound
The hook carries cues only on the G-1 cut and on the first annotation landing (§11). The music bed runs from f0, ≥ 18 dB under the voice.

### 6.7 CTA: scheduled sticker + cliffhanger `[DNA device set; VAR values]`
**Device chosen:** `{{BV-08.device|subscribe}}`. The sticker word is **FOLLOW** on Instagram-first reels and **SUBSCRIBE** when the reel is also posted as a YouTube Short (the evidence word). With `comment_keyword` the final sticker reads **"COMMENT {{BV-08.keyword|KEYWORD}}"** (`kind: "cta-keyword"`); with `link_bio` it reads **"LINK IN BIO"**.

**Schedule (H9):**
| Sticker | When | Over | Spoken? |
|---|---|---|---|
| **S1** | The first sentence end in the window 10–26 s, on a B-roll or diagram beat with the sticker band (y 1260–1380) free | B-roll / diagram | No |
| **S2** | Only in reels ≥ 45 s: the sentence end nearest 65% of the runtime | B-roll / diagram | No |
| **S3** | The CTA word at the end ("…SUBSCRIBE!" / "…FOLLOW!" / "…COMMENT [KEYWORD]!") | The closing host flash (G-3), or the cliffhanger visual when the host's chin is below y 1220 | **Yes** |

Rules: ≥ 15 s between stickers; never in the first 8 s; never within 1.0 s of a chip, plate or hero number landing; ≤ 3 per reel. The evidence spacing is ≈ 20–30 s (v01 @ 0:25 / 0:57, v02 @ 0:14 / 0:35, v03 @ 0:12 / 0:52).

**Sticker recipe (P-SUBSCRIBE-TAP):** a 440 × 120 lime button at cx 540, cy 1320, radius 16, 5 px `edge` border, hard shadow 0/+8 px `edge`, the word in Archivo Black 56 px `edge`. **Measured motion (v01 @ 0:24.52–26.9, v02 @ 0:34.9–36.7):** it **rises in** from 28 px lower with a 6 f fade, ease-out, no scale pop (width constant). A white hand cursor (64 px, 3 px `edge` outline) slides in from the lower right (+150, +90) over 8 f, **≈ 0.9 s after** the button lands, to its lower-right corner; **tap ≈ 8 f later**: the button goes to 0.94 for 3 f and three 4 px lime spark lines burst from its upper-left corner over 6 f. The sticker is a z8 overlay that **rides across cuts** (2–3 clips under it). Exit: a slow fade to 0 over ≈ 30 f (1.0 s). S1 and S2 last ≈ 2.2–2.6 s in total; S3 enters 1.1–1.7 s before the end over the last B-roll beats and holds through the closing flash.

**Cliffhanger (P-CLIFFHANGER, the last 3–5 s):** "BUT [the bigger / smaller / next question]…" over a teaser visual (the next subject as a dark silhouette, or a hero number under P-QMARK-SWARM), then "[TO SEE / LEARN] THAT," with S3 popping in, then the closing flash on "SUBSCRIBE!" (G-3). A ≤ 0.4 s held breath is allowed before "BUT". Hard end ≤ 6 f after the last word; no end card.

---

## §7 Structure & cadence `[REQ] [DNA]`

### 7.1 Structure type: `explainer` + cliffhanger outro
| Section | Span in a 55 s reel | What happens | Layout |
|---|---|---|---|
| **HOOK** | 0–5 s | HA-10: flash → subject → 2–3 proof clips with annotations | L-host → L-evidence |
| **LOOP** | 5–7 s | Host drop-in (G-2) with the open-loop exclamation | L-host |
| **COMPARE** | 7–16 s | The subject against 1–2 familiar things on the same axes: P-VS-STACK → P-VS-FOCUS → P-XRAY-SWAP, or two clips in sequence with matching framing | L-diagram, L-evidence |
| **MECHANISM** | 16–46 s | 3–4 steps, each a unit ritual (§7.3); at most one sustained analogy block (P-ANALOGY-SCENE, ≤ 20 s) | L-evidence, L-diagram |
| **PAYOFF** | 46–51 s | The answer made visible: P-HERO-NUMBER, the crisp result (P-SPLIT-REVEAL), or the subject doing the thing; an optional ✓ | L-evidence |
| **CLIFFHANGER** | last 3–5 s | P-CLIFFHANGER + S3 + the closing flash | L-evidence → L-host |

Short reels (35–45 s) shrink COMPARE to 4–6 s and MECHANISM to 2 steps.

### 7.2 Markers
`markers: none (spoken only)`. There are no numbered badges. In COMPARE, the parallel labels of P-VS-STACK ("BIRD / PTEROSAUR / BAT", v01 @ 0:07–0:14) are the list, and the active row lights up (P-VS-FOCUS).

### 7.3 Unit ritual (every MECHANISM step)
1. **Cut** (T-01) on the step's first caption chunk to the literal subject of the sentence (P-BROLL-FULL / P-STILL-PUSH / P-BAND-CLIP).
2. **Credit** is on from the cut frame (third-party clips); stills and pages P-LAND.
3. **Point** on the trigger word: the annotation that matches the line (arrow at a part, bracket at a size, pin at a place, chip at a term) lands within ±5 f (anchor pass).
4. **Evolve** inside the shot when the line names a second part: P-ARROW-HOP (the arrow travels to the next part in 8 f) or a second mark; ≤ 3 marks on screen.
5. **Swap** to the next clip on the next sentence; marks and chips stay to the last frame and leave **with the cut** (v01 @ 0:01.93).

Each step lasts 3–9 s, with 2–6 caption chunks and 1–3 clips.

### 7.4 Open loops and re-hooks
- **The loop line** (the LOOP drop-in) promises a mechanism ("…in a really freaky way!"); the MECHANISM pays it on screen.
- **"Look at / watch this"** lines are paid within 1 s by the thing itself (v01 @ 0:29 "BUT JUST WATCH THIS" → the bat walks).
- **The cliffhanger** is the only promise left open: it points to the next reel.
- Duration `short`: no mid-reel re-hook is required; in 50–60 s reels a second drop-in (G-2) at a section break does that job. The intro (hook + loop) is ≤ 15% of the runtime: ≤ 7.5 s in a 50 s reel.

### 7.5 Rhythm and energy
- Energy: hook (fastest: a cut every ≈ 1.3 s) → compare (calmer: a diagram evolving for 5–9 s) → mechanism (steady: a cut every 1.5–3 s; one analogy block may breathe, with an event every ≤ 2.5 s) → payoff (a beat of stillness on the answer, ≥ 1.5 s) → cliffhanger (quick, 3–5 s).
- No comedy beats (`comedy: off`). The entertainment is wonder: scale shots, reveals and the host's reactions.

### 7.6 Cadence (state changes)
| Token | Value | Why |
|---|---|---|
| `sc_per_10s` | **[4, 8]** | v01 ≈ 5, v02 ≈ 8, v03 ≈ 5 (captions × 0.5 + cuts + annotation entries) |
| `hook_sc_3s` | **6** | weighted counts: v01 ≈ 5.5, v02 ≈ 9, v03 ≈ 5.5; the floor keeps the busier half |
| `max_gap_s` | **2.5** (hook 1.5) | the longest weight-1 gaps in the body are 2–3 s with only captions swapping |
| `max_static_s` | **1.5** | every shot pushes or moves |
| `caption_weight` | 0.5 | support captions |
| `max_shot_s_without_event` | 4.0 | H5 |
| `cuts_per_min` | not DNA (evidence 16–36 per min) | — |
| `median_shot_s` | **1.8** (p90 4.7, max 9.8 s) | measured (scene-detect 0.2): v01 2.3 / v02 0.9 / v03 2.8 s median; the 7–10 s shots are CG analogy or diagram scenes carried by marks every ≤ 2.5 s (v01 @ 0:28.9–36.2, v03 @ 0:29.6–39.5) |

---

## §8 Visual system `[REQ]`

### 8.1 Graphics role and budget
- `graphics: support`: the creator's footage carries ≈ 60–90% of the runtime; graphics point at it, label it, measure it, and replace it only where no clip exists (diagram spans 4–35%).
- **47 patterns** (§8.3). Per 60 s: ≥ 8 distinct patterns and ≥ 4 families.
- **Numbers become pictures** whenever they are about size, amount or distance: a bracket against a known object, a dimension tag on the object, a lineup on one ground line, a hero number with both units. Never a bare number card.
- **Credit lines** are `TC-legal`: they don't count toward G2's text limit.

### 8.2 Families
| ID | Family | Source class | The buyer supplies | Created substitute when missing |
|---|---|---|---|---|
| **B-1** | Subject B-roll clip, full-bleed | buyer-owned, or creator-supplied third-party | 12–25 clips of 2–6 s per minute (SH-4) | B-3 / B-4 diagram (FB-4) |
| **B-2** | Still (photo, render, figure image) with a push | buyer-owned / creator-supplied | stills ≥ 1500 px tall (SH-7) | B-3 diagram |
| **B-3** | Created diagram on W-grid / W-glow / W-void | engine | — | — |
| **B-4** | Created scale scene (silhouettes, rulers, lineups) | engine | — | — |
| **B-5** | Paper / quote / figure card on W-paper | creator-supplied screenshot (SH-6), else created | the page screenshot with outlet, date, headline | `fx.headlineCard`, `fx.quoteCard` |
| **B-6** | Ink annotation (arrows, brackets, pins, ? marks, traces) | engine | — | — |
| **B-7** | Type (chips, typed keywords, plates, hero numbers, leader labels, credits) | engine | credit strings for third-party clips | — |
| **B-8** | Host footage (flash, drop-in, close) | buyer-owned (SH-1–SH-3) | the selfie narration | none (FB-1 no_fallback) |
| **B-9** | CTA sticker | engine | — | — |
| **B-10** | Map (aerial, globe, figure map) | creator-supplied map clip/still, else created schematic | map footage or a map figure they hold | P-MAP-SCHEMATIC |

### 8.3 Pattern specs (47)
Motion in frames at 30 fps. "Anchor" = target keyframes from the anchor pass (§17.2). Engine names: `VEOS.fx.*` (renderer/fx.js, inserts.js) or a bespoke `VEOS.scene`.

**Host (B-8)**
| ID | Type | On screen | Motion | When | Family · class | Engine / needs |
|---|---|---|---|---|---|---|
| **P-HOST-FLASH** | stage | The host's selfie, mid-gesture, first 2–3 words | Hard cut in at f0, hard cut out at 0.50–0.70 s (G-1); no zoom | f0 of every HA-10 reel | B-8 | `stage: [{t:0, layout:"L-host"}, {t:0.6, layout:"L-evidence", via:"cut"}]` |
| **P-HOST-DROPIN** | stage | The host reacting big on one line | 1.5–2.5 s, hard cuts both ends (G-2) | The loop line; a section break in 50–60 s reels | B-8 | stage entries |
| **P-HOST-CLOSE** | stage | The host on the CTA sentence, pointing down at the sticker or reaching into the lens | 0.6–0.8 s to the hard end (G-3), hand reaching into the lens (v01 @ 0:58.46, v02 @ 0:36.0) | Every reel's last words | B-8 | stage entry + S3 sticker |

**Footage (B-1, B-2)**
| ID | Type | On screen | Motion | When | Family · class | Engine / needs |
|---|---|---|---|---|---|---|
| **P-BROLL-FULL** | footage-treatment | The creator's clip, full-bleed 9:16 cover crop on the subject | Hard cut in; the clip's own camera move is the motion (measured ≈ 1%/s push or pull, v01 @ 0:02.0, 0:14.4); add a scene push 1.00 → 1.03 only when the clip itself is locked off. The hook subject and any clip that must read as "huge" use P-LAND first | Every sentence with a matching clip | B-1 | `fx.clip({z:1, in:"none", out:"none", kind:"subject", kenburns:[1,1.06], focus})`; insert record if third-party |
| **P-STILL-PUSH** | footage-treatment | A still, full-bleed | P-LAND in (×1.8 → 1.0), then **hold still** (v03 @ 0:00.84–2.42 static); events (wipe, punch, mark) carry the cadence. A still with no event inside 1.5 s gets a 1.00 → 1.04 drift | A photo, render or figure image | B-2 | `fx.clip({z:1, asset: still, focus, land: {from: 1.8, frames: 10}})` (holds after landing; add `kenburns: [1, 1.04]` only when no event comes inside 1.5 s) |
| **P-BAND-CLIP** | footage-treatment | A 16:9 clip as a 1080 × 608 band at cy 800 over a blurred (24 px), 45%-dimmed copy of itself | Push 1.00 → 1.04 inside the band | 16:9 clips too small to crop (§12.4) or whose crop loses the subject | B-1 | two `fx.clip` scenes (z1 blurred copy with `dim: 0.55`, z2 band) |
| **P-SNAP-PUSH** | footage-treatment | The current shot punched in ×2.0–2.5 on the detail (a punch-in **cut**) | 0 f: the very next frame is ×2.46 on the detail (v03 @ 0:02.46), on the caption swap; then holds still; ≤ 2 per reel | "BOTH", "LOOK", "RIGHT HERE" on a detail | B-1/B-2 | the clip scene's own scale keyed to an `event` |
| **P-SPLIT-REVEAL** | footage-treatment | Image A in the top half (y 260–760), image B drawn in below a seam at y 760 | A lands with P-LAND (×1.8 → 1.0, 8 f) and holds; B wipes downward from the seam in 9 f (T-02) starting on the "AND THIS!" swap; then P-SNAP-PUSH on the seam | "the difference between this… and this" | B-1/B-2 on W-void | image A `fx.clip({x: 0, y: 260, w: 1080, h: 500, land: {from: 1.8, frames: 8}})`; image B a clip scene with `clip-path` driven by `lt`; events at the wipe |
| **P-STATE-SWAP** | cut | The same framing in another render (colour map, x-ray, night/day, before/after) | Hard cut (T-04); annotations keep their anchors | "revealing…", "and in infrared…" | B-1/B-2 | two clip scenes, the same `focus` |
| **P-WHITEOUT** | footage-treatment | The frame flooding to white as content ("all you'd see is a blinding glow") | Ease-in ramp to ≈ 95% white over 18 f (luma 70 → 240, v03 @ 0:22.85–23.6), hold 3–6 f, recede over 15 f to ≈ 60% white (the scene stays glowing); captions stay on (black stroke); ≤ 1 flash per reel incl. T-07 () | A literal glare, blinding or overexposure line | B-1 | built-in transition on the peak frame: `{"t": <peak>, "type": "flash", "colour": "#FFFFFF", "peak": 0.95, "pre": 18, "frames": 30, "decay": 1.2}` (18 f up, peak, 12 f down onto the veil: ≤ 1 s, inside; the picture layers only, so the captions stay on top); the ≈ 60% rest glow is a static z2 white veil (opacity 0.6) from the peak to the cut |
| **P-LENS-IRIS** | footage-treatment | A circular viewer (a lens or porthole) with a tick-marked ring; the subject inside | The circle opens from r 0 → 430 px in 12–14 f (T-05); ring ticks rotate 6°/s | "through the microscope / telescope / lens" | B-1/B-3 | bespoke scene: `clip-path: circle()` + an SVG ring |
| **P-LAND** | footage-treatment | The new picture arrives scaled up on its subject and pulls back to its resting frame | Scale ×1.12–1.2 (footage) or ×1.8–3.7 (stills, pages, split image A) → 1.0 over 10–16 f, expo-out, starting on the cut frame; then the shot holds or runs its own motion (v01 @ 0:00.70 ×1.13/16 f; v03 @ 0:00.63 ×1.8/10 f; v02 @ 0:06.63 ×3.7/10 f) | Every still, page and split; the hook subject; the cliffhanger lineup. ≤ 1 per shot, never on host footage | B-1/B-2/B-5 | `fx.clip({asset, focus, land: {from, frames}})` (expo-out by default; `in` becomes `none`, so the shot never fades up): footage `{from: 1.13, frames: 16}`, stills `{from: 1.8, frames: 10}`, pages up to `{from: 3.0, frames: 10}` (`fx.clip` caps `from` at 3; v02's page lands from 3.7) |
| **P-RECAP-RUN** | cut | 3–4 shots already seen in this reel, re-cut at 0.4–0.6 s each, no marks, no new credits | Hard cuts on a steady beat under one summary line | "…revealing what was hidden before!" (v02 @ 0:20.1–22.4); under the cliffhanger/CTA line (v02 @ 0:34.8–35.7). ≤ 2 per reel | B-1 | `fx.clip` scenes reusing assets |
| **P-PLACE-DOLLY** | footage-treatment | A map or aerial pushing toward the site; the place name set in type and tilted onto the ground plane (white 60%, Montserrat 800, 72 px) | Scale 1.00 → 1.50 over 21 f (ease in-out: ≈ 1%/f for the first 5 f, peak ≈ 5%/f mid) **with a −12 to −16° roll** around the site (v02 @ 0:00.62–1.29); the name rides with the map | "in [place]", "hidden in…" | B-10 | `fx.clip({asset, focus: <site>, kenburns: [1.5, 1.5], land: {from: 0.667, frames: 21, ease: "inOut"}, rotate: [0, -15]})` (1.0 → 1.5 with the roll eased with the land, then held; the image is scaled to keep covering) + a z5 label (TC-display) that rides the same scale and roll |

**Ink annotation (B-6)**
| ID | Type | On screen | Motion | When | Family · class | Engine / needs |
|---|---|---|---|---|---|---|
| **P-LIME-ARROW** | annotation | A chunky lime block arrow (≈ 210 × 150 px), 6 px `edge` outline, hard shadow 0/+6, tip 24 px off the target | **Pops on at full size in 1 f** ≈ 6 f after the cut, nudges 20 px toward the target over 6 f (ease-out), then **holds** (drift ≤ 3 px, no bob; v02 @ 0:01.95–2.53); exits hard on the cut | "this part", any named feature | B-6 | bespoke SVG scene; **anchor** |
| **P-ARROW-HOP** | annotation | The same arrow gliding along the structure to the next named part | Glides along the part over 1.5–2.5 s (sine in-out), re-aiming as it goes (← to ↓, v01 @ 0:15.4–17.9); a jump to an unrelated part is 8 f in-out | The line names a second / third part, or the length of one part (v01 @ 0:15–0:18) | B-6 | the arrow scene with `events` at each hop; **anchor** |
| **P-PINCER-ARROWS** | annotation | Two curved lime marker arrows from both sides converging on two points | Each shaft draws in 8 f (stroke-dashoffset), the head pops in 2 f; the second starts 4 f after the first | "both its legs and its thumbs", two matching parts (v01 @ 0:33) | B-6 | SVG paths; **anchor ×2** |
| **P-HAND-ARROW** | annotation | A hand-drawn curved marker arrow in `accent` blue, 20 px stroke | Shaft draws in 10 f, head in 2 f; no bob | A second mark when a lime one is on screen, or "this one" between two images (v03 @ 0:04, 0:29) | B-6 | SVG path; **anchor** |
| **P-MEASURE** | annotation | A white 8 px measure line with a 56 px flat foot cap and an arrowhead at the top, beside the subject; a person or known object in frame for scale | Starts on the cut frame and grows from the ground line to the top in 13 f (ease-out, v01 @ 0:00.70–1.12) while the shot lands (P-LAND); holds to the cut | "as big / tall / long as" (v01 @ 0:00.8–0:01.8) | B-6 | SVG scene; **anchor** (ground y, top y) |
| **P-DIM-LABEL** | annotation | A white two-headed arrow along a dimension of the object + a TX-4 dual-unit tag rotated to it | The arrow grows outward over ≈ 22 f and the tag **rolls its number with the arrow's length** (10 m / 3 ft → 170 → 196 → **200 m / 656 ft**, v02 @ 0:05.05–5.8), landing on the spoken value ±5 f | "[N] metres across", an exact size (v02 @ 0:05–0:06) | B-6 + B-7 · TC-label | SVG + HTML tag; **anchor** (two endpoints); `fmtNum` dual |
| **P-MAP-PIN** | annotation | A lime map pin (64 × 88 px, `edge` outline) + a lime ripple ring | Grows from its tip 0 → 1.0 in 8 f (ease-out, no drop) while the map dollies, ring r 0 → 90 px over 18 f fading out; one repeat ring at +24 f | The exact place (v02 @ 0:00.75–1.0) | B-6 | SVG scene; **anchor** |
| **P-QMARK-SWARM** | annotation | 3–5 lime "?" glyphs (Montserrat 900, 72–110 px, `edge` stroke) scattered around an unclear area | Pop in with 3 f stagger (0 → 1.15 → 1), wobble ±6° every 20 f | "no one knows", "we don't know", "what is the smallest…?" (v02 @ 0:31, v03 @ 0:26, v01 @ 0:57) | B-6 · TC-display | bespoke scene; seeded positions (`ctx.rngStable`) |
| **P-REC-HUD** | annotation | TX-9 REC tag + red triangle markers (28 px) on the points being recorded | REC fades in 6 f; markers pop with 2 f stagger as they're named | "recording / tracking / mapping each…" (v03 @ 0:32–0:37) | B-6 · `bad` | bespoke scene; **anchor** per marker |
| **P-OUTLINE-TRACE** | annotation | A neon outline (6 px, `bad` red or `accent` blue + 14 px glow) tracing the shape of a region | Draws along its path in 18–24 f | "the whole region / every one of these" (v03 @ 0:37) | B-6 | SVG path from the anchor polygon |
| **P-LEADER-LABEL** | annotation | TX-3 label + a 3 px white leader line to the part | The line draws from the part in 6 f, the label fades in over 6 f | Naming 1–2 parts in a still or a slow shot (v03 @ 0:51 "HEMOGLOBIN 6.5NM") | B-6 + B-7 · TC-label | HTML + SVG; **anchor** |

**Type (B-7)**
| ID | Type | On screen | Motion | When | Family · class | Engine / needs |
|---|---|---|---|---|---|---|
| **P-KW-CHIP** | overlay | §5.2 lime chip with the term (≤ 3 words) | Types 1 letter per 2 f, the box growing with it; or pops in 7 f | A term or number the viewer must keep ("250 NANOMETERS", v03 @ 0:09) | B-7 · TC-display | `kind: "chip"`; near the anchor |
| **P-KW-WORD** | overlay | TX-1 typed lime word on the footage, no box | Types 1 letter per 2 f with a white glow flare (24 px blur, fading over 4 f) on the newest letter (v02 @ 0:04.3–4.8); holds to the cut | A new named thing the shot shows ("GEOGLYPHS", v02 @ 0:04) | B-7 · TC-display | `kind: "chip"`; text from `VEOS.fx.typewriter(word, lt, {at, cps: 15, flare: {color: "#FFFFFF", px: 24, frames: 4}})` |
| **P-ALERT-CHIP** | overlay | The chip in `bad` red with white text and a 4 px `edge` stroke | As P-KW-CHIP | A hazard term, or any chip over green/yellow footage (v02 @ 0:11 "LiDAR") | B-7 · TC-display | `kind: "chip"`, roles [bad] |
| **P-TITLE-PLATE** | overlay | §5.2 two-line lime title + white sub-line | Types line by line; the sub-line rises | Naming a people, place, era or mission with a date range (v02 @ 0:26–0:28) | B-7 · TC-display | `kind: "plate"` |
| **P-HERO-NUMBER** | overlay | TX-5 lime number, the other unit beneath, a white bracket | Static text revealed by the scene's P-LAND pull-back (no count, v01 @ 0:56.6–58.3); on screen when the number is said | The payoff number, or the biggest number in the reel (v01 @ 0:57) | B-7 · TC-display | `kind: "hero"`; `ctx.fmtNum` metric + imperial; `events` at the landing |

**Diagrams and scale (B-3, B-4)**
| ID | Type | On screen | Motion | When | Family · class | Engine / needs |
|---|---|---|---|---|---|---|
| **P-VS-STACK** | stage | 2–3 specimens stacked on W-grid at y ≈ 420, 820, 1180, each with a TX-2 lime label locked above it; same scale | **Conveyor scroll:** the grid scrolls up and each specimen + label rides in from below the frame (≈ 490 px in the first 5 f, ease-out, then ≈ 35 px/f), the next ≈ 10 f later, until the stack settles (v01 @ 0:06.63–0:09) | "X vs Y vs Z", the COMPARE section (v01 @ 0:07–0:09) | B-3 | `fx.diagram` or a bespoke scene; one element (labels internal) |
| **P-VS-FOCUS** | state | The active specimen scales 1.25 and gets a 6 px `accent` outline panel (radius 24); the others shrink to 0.85 and dim 30% | 10 f in-out per focus change, on the specimen's name | Walking through the stack one by one (v01 @ 0:13–0:14, 0:37–0:40) | B-3 | the P-VS-STACK scene with `events` |
| **P-XRAY-SWAP** | state | The same stack turns into neon-blue outlines with white bones on W-glow | T-07 bloom flip: brighten to ≈ 80% white over 6 f, cut to W-glow at the peak, the glow blooms down over 5 f; the labels turn white (v01 @ 0:09.93–10.27) | "inside / underneath / the skeleton / how it's built" (v01 @ 0:10) | B-3 | world flip + diagram redraw + the built-in `flash` transition (T-07) on the cut |
| **P-SCALE-LINEUP** | figure | 3–5 objects in size order on one ground line (W-grid), a human silhouette (1.75 m) as reference, a dual-unit tag under each | Objects join in size order from the right, each first a pale 40% ghost silhouette that turns solid over 8 f, ≈ 10 f apart; the lineup pulls back slowly (×1.3 → 1.0 over ≈ 1.7 s, v01 @ 0:56.6–58.3) | "smaller than / bigger than", sizes across orders of magnitude (v03 @ 0:50–0:52) | B-4 · TC-label | bespoke scene; `fmtNum` dual |
| **P-SCALE-PERSON** | figure | A flat white human silhouette (1.75 m) beside the created subject + P-MEASURE | The silhouette fades in over 6 f, then the bracket grows | Scale with no SH-5 footage (FB-5) | B-4 | bespoke SVG |
| **P-BLUR-VS-SHARP** | figure | The same created dot field: blurred (24 px) on top, crisp dots below | Built for P-SPLIT-REVEAL with created imagery: the crisp half wipes in from the seam | "blurry vs crisp", resolution, focus (created stand-in for v03 @ 0:01–0:03) | B-3 on W-void | bespoke canvas (`ctx.rngStable` dots) |
| **P-MECHANISM-LOOP** | figure | A 2–4 s looping flow diagram: 2–4 nodes (icons from `fx.icon`) linked by lime arrows; a dot travels the path | Nodes pop 6 f apart; the dot travels 24 f per edge; loops | How a process works when no clip shows it (FB-4) | B-3 | `fx.diagram` (edges `style: arrow`, `dot: true`) |
| **P-ANALOGY-SCENE** | stage | One familiar scene used for 10–20 s to explain a mechanism (a stadium of lights, a crowd, a kitchen), creator footage or created | Its own cuts and marks every ≤ 2.5 s (REC HUD, arrows, ? swarm, whiteout) | "Imagine you're…" (v03 @ 0:17–0:38) | B-1/B-3 | ≤ 1 per reel; every 2.5 s an `event` |
| **P-MAP-SCHEMATIC** | figure | A created flat map: land `#2A2B34`, water `#060A2C`, coast line white 3 px, the place name set in type; P-MAP-PIN on it | P-PLACE-DOLLY on it | A place with no map footage (FB-4) | B-10 · TC-display | bespoke canvas; generic shapes only (no traced real coastlines unless the creator supplies the map) |

**Paper and source (B-5)**
| ID | Type | On screen | Motion | When | Family · class | Engine / needs |
|---|---|---|---|---|---|---|
| **P-PAPER-HILITE** | overlay | The paper or article page on W-paper (creator screenshot, else a created headline card); a lime highlighter sweeps over the exact spoken phrase | **P-LAND from ×3.5 on the headline to the full page in 10 f** (expo-out, v02 @ 0:06.63–7.0), then holds dead still; the highlight wipes left → right at 0.5 s per span, starting on the phrase's first word | "a study / paper / report found…" (v02 @ 0:07–0:09) | B-5 · TC-label + TC-decorative | `fx.shot({asset, highlights})` or `fx.headlineCard({masthead, date, headline, highlight, hlRole:"primary"})`; insert + source fields |
| **P-QUOTE-HILITE** | overlay | A pull-quote paragraph on W-paper (Source Serif 4), the spoken sentence highlighted lime | The paragraph fades in, then the highlight wipes as it's read | A researcher's quote read aloud (v02 @ 0:32–0:34) | B-5 | `fx.quoteCard` / `fx.shot`; verbatim (NC-13) |
| **P-FIGURE-CARD** | overlay | A paper figure (map, chart, micrograph) on W-paper, pushed in on the region named | Push 1.00 → 1.15 toward the region over the shot; a P-LIME-ARROW or ring on the region | "over this area", a figure from the paper (v02 @ 0:13) | B-5 | `fx.shot({asset})`; creator file only (else P-MAP-SCHEMATIC / P-MECHANISM-LOOP) |

**Credits (B-7, TC-legal)**
| ID | Type | On screen | Motion | When | Family · class | Engine / needs |
|---|---|---|---|---|---|---|

**CTA (B-9)**
| ID | Type | On screen | Motion | When | Family · class | Engine / needs |
|---|---|---|---|---|---|---|
| **P-SUBSCRIBE-TAP** | overlay | §6.7 sticker + hand cursor | Rise-in 28 px + fade 6 f, cursor 8 f at +0.9 s, tap 8 f later with sparks, rides across cuts, fade-out 30 f | S1, S2, S3 | B-9 · TC-display | bespoke scene `kind: "cta-sticker"`, z8, `events` at the tap |
| **P-KEYWORD-TAP** | overlay | The same button reading "COMMENT [KEYWORD]" (width grows to fit, max 760) | As P-SUBSCRIBE-TAP; holds ≥ 1.5 s | S3 when the device is `comment_keyword` | B-9 · TC-display | `kind: "cta-keyword"` (V-PROMISE) |
| **P-CLIFFHANGER** | stage | The next question's teaser: a dark silhouette of the next subject or a ? swarm over a hero number; then S3 and the closing flash | §6.7 | The last 3–5 s of every reel | B-3/B-6/B-9 | scenes + G-3 |

### 8.4 Line → pattern lookup `[NICHE]`
| Line type (what the voice says) | Primary | Alternates | Created substitute (no clip) |
|---|---|---|---|
| Opening subject ("this animal / chip / can") | P-HOST-FLASH → P-BROLL-FULL | — | P-SCALE-PERSON on W-grid |
| How big / tall / long / heavy | P-MEASURE | P-DIM-LABEL, P-HERO-NUMBER | P-SCALE-PERSON, P-SCALE-LINEUP |
| An exact size of a part | P-DIM-LABEL | P-LEADER-LABEL | — |
| "This part / here / its wing" | P-LIME-ARROW | P-ARROW-HOP, P-HAND-ARROW | arrow on a created diagram |
| Two matching parts | P-PINCER-ARROWS | two P-LIME-ARROWs | — |
| A new term | P-KW-WORD | P-KW-CHIP | chip on W-grid |
| A number to keep | P-KW-CHIP | P-HERO-NUMBER | — |
| A hazard / limit | P-ALERT-CHIP | P-OUTLINE-TRACE (red) | — |
| "X vs Y vs Z" | P-VS-STACK → P-VS-FOCUS | two clips in sequence, same framing | P-VS-STACK with created specimens |
| "Inside / underneath / built like" | P-XRAY-SWAP | P-STATE-SWAP | P-XRAY-SWAP |
| "The difference between this and this" | P-SPLIT-REVEAL | P-STATE-SWAP | P-BLUR-VS-SHARP |
| "Where" / a place | P-PLACE-DOLLY + P-MAP-PIN | P-FIGURE-CARD | P-MAP-SCHEMATIC + P-MAP-PIN |
| "A study / paper found" | P-PAPER-HILITE | P-FIGURE-CARD | `fx.headlineCard` (P-SYNTH-TAG) |
| A quote from a researcher | P-QUOTE-HILITE | — | `fx.quoteCard` (P-SYNTH-TAG) |
| "Imagine…" (an analogy) | P-ANALOGY-SCENE | P-MECHANISM-LOOP | P-MECHANISM-LOOP |
| How a process works | P-BROLL-FULL sequence + P-ARROW-HOP | P-MECHANISM-LOOP | P-MECHANISM-LOOP |
| "Through the lens / microscope" | P-LENS-IRIS | P-SNAP-PUSH | P-LENS-IRIS on a created image |
| "Recording / tracking each one" | P-REC-HUD | P-OUTLINE-TRACE | — |
| "Blinding / glare / all you'd see" | P-WHITEOUT | — | — |
| "Nobody knows / what is…?" | P-QMARK-SWARM | — | — |
| A people / era / mission name | P-TITLE-PLATE | P-KW-CHIP | — |
| "Look at / watch this" | P-SNAP-PUSH (≤ 1 s later the thing) | P-LIME-ARROW | — |
| A summary of what was just shown | P-RECAP-RUN | — | — |
| A reaction ("so many more!") | P-HOST-DROPIN | — | — |
| The next question | P-CLIFFHANGER | — | — |
| "Subscribe / follow" | P-SUBSCRIBE-TAP + P-HOST-CLOSE | P-KEYWORD-TAP | — |

Niche examples `[NICHE: example]`:
- *Tech & AI:* "each transistor is 5 nanometres wide" → P-KW-CHIP "5 NANOMETRES" + P-SCALE-LINEUP (hair → cell → virus → transistor); "the cable runs 6,600 km across the Atlantic" → P-PLACE-DOLLY + P-DIM-LABEL "6,600 KM / 4,101 MI"; "the model predicts the next word" → P-MECHANISM-LOOP.
- *Food & health:* "a can has 35 grams of sugar" → P-MEASURE up a stack of sugar cubes + P-HERO-NUMBER "35 G / 1.2 OZ"; "your gut holds trillions of bacteria" → P-SNAP-PUSH into the micrograph + P-KW-CHIP "TRILLIONS"; "a 2023 study found…" → P-PAPER-HILITE.

### 8.5 Data and truth rules
- Every number on screen is said in the script (or shown in the creator's own source screenshot); `data_figures` is off, so no computed figures. A conversion to the other unit system is a format, not a new claim.
- **Same axes.** P-VS-STACK and P-SCALE-LINEUP draw everything at one scale; when the sizes span > 100×, they say so with a break mark (two slanted white lines) and a tag per object.
- **Illustrative scenes** (a created silhouette, a schematic map, a dot field) carry no numbers except script-stated ones.
- **CG and artist's impressions** supplied by the creator are shown as given.

### 8.6 Comedy layer
OFF: `tone.comedy = off` (no stickers, stamps, meme sounds or freeze-frame roasts in any evidence video).

### 8.7 Asset rules
- **The creator's own or held footage first.** One clip per sentence; the clip must show the named thing.
- **Mocks:** created diagrams, schematic maps, silhouettes and scale lineups are generic shapes; no traced brand logos or real UIs.
- **No stock clichés** (N2).
- **Logos** appear only inside creator footage; a brand or institution named on screen is set in type (`fx.logoPlate`).
- **Third-party moments** follow §12.5 (ask once, then create).

### 8.8 Density and variety
- An event (cut, mark, chip, state change) every 1.0–2.5 s; caption swaps every 0.9–1.6 s.
- Per 60 s: ≥ 8 distinct patterns, ≥ 4 families, 12–25 clips.
- The same pattern ≤ 3 times in a row; P-BROLL-FULL is the base layer and doesn't count. P-LIME-ARROW ≤ 2 shots in a row: then switch the mark (bracket, chip, pinch, label).
- ≤ 3 ink marks on screen; ≤ 1 chip or plate at a time.

---

## §9 Transitions & shot grammar `[REQ] [DNA]`

### 9.1 Library
| ID | Transition | Frames | Recipe | SFX role |
|---|---|---|---|---|
| **T-01** | Caption-beat cut | 0 | A hard cut on the caption swap frame (±1 f of the word boundary). ≈ 85% of all boundaries | none, except the hook cut |
| **T-02** | Seam wipe | 8–10 | Image B draws downward from a horizontal seam (y 760) with a 2 px white edge line that fades after | soft swish |
| **T-03** | Whiteout | 18 + 3–6 + 15 | Ease-in to ≈ 95% white in 18 f, hold, recede to ≈ 60% in 15 f (P-WHITEOUT: the built-in `flash`, `pre: 18`, `peak: 0.95`, over a 0.6 white veil); ≤ 1 flash per reel (T-03 or T-07) | rising shimmer |
| **T-04** | State swap | 0 | The same framing, another render (P-STATE-SWAP); annotations persist | tick / click |
| **T-05** | Lens iris | 12–14 | A circle opens from r 0 to 430 px with a tick ring (P-LENS-IRIS) | soft whoosh |
| **T-06** | Place dolly | 21 | Push 1.0 → 1.5 with a −15° roll into a map/aerial, then T-01 to the close-up (P-PLACE-DOLLY) | air whoosh |
| **T-07** | Bloom flip | 6 + 5 | Brighten W-grid to ≈ 80% white in 6 f, cut to W-glow at the peak, bloom decays 5 f (P-XRAY-SWAP): built-in `{"t": <cut>, "type": "flash", "colour": "#FFFFFF", "peak": 0.8, "pre": 6, "frames": 11}`; counts as the reel's one flash | digital sweep |
| **T-08** | Punch-in cut | 0 | The same image ×2.0–2.5 on the detail on the next frame (P-SNAP-PUSH); ≤ 2 per reel | zoom tick |
| **T-09** | Recap run | 0 × 3–4 | Hard cuts every 0.4–0.6 s through shots already seen (P-RECAP-RUN); ≤ 2 per reel | none |

### 9.2 Grammar
| Boundary | Use | Never |
|---|---|---|
| f0 | The host flash already moving | a fade-in, a title |
| Host → subject (hook) | T-01 on the word boundary (G-1) | a dissolve, a zoom |
| Clip → clip | T-01 on the caption beat | a dissolve, a whip |
| Same subject, new render | T-04 | T-01 to a different angle |
| A → B comparison image | T-02 | side-by-side split |
| Into a place | T-06 | T-01 straight to the close-up (lose the "where") |
| Diagram → inside view | T-07 | — |
| Through a lens | T-05 | — |
| Back to the host | T-01 (G-2 / G-3) | a morph, a PiP |
| A summary line ("revealing…", the CTA line) | T-09 recap run of 3–4 earlier shots | new, uncredited footage |
| Last word | hard end ≤ 6 f | an end card, a black tail |

### 9.3 Shot grammar `[COND: spine footage/hybrid]`
OFF as a rule set (the spine is `audio`; footage follows the voice). Two cut rules still hold: **R-1** cut on the caption beat (±1 f), never mid-word; **R-2** cut on the motion beat when a clip has one inside the sentence (a wingbeat, a pour, a flash).

### 9.4 Budget (per 60 s)
- Non-cut transitions (T-02, T-03, T-05, T-06, T-07) ≤ 4 (≈ 1 per 15 s).
- T-03 ≤ 1 per reel; T-08 ≤ 2 per reel.
- The same non-cut transition never twice in a row.

---

## §10 Motion, camera, layers, finishing `[REQ] [DNA; motion tokens TUNE ±15%]`

### 10.1 Motion tokens (30 fps)
| Token | Value |
|---|---|
| Beat lead | the picture 2 f before the trigger word; marks land within ±5 f |
| Entries | `cubic-bezier(0.22, 1, 0.36, 1)` (expo-out), 6–10 f |
| Arrows, pins, stickers | back-out `cubic-bezier(0.34, 1.56, 0.64, 1)`, 7–8 f |
| Exits | marks, chips, labels and the credit leave **with the cut** (0 f); the sticker fades over 30 f; a chip leaving mid-shot fades 4 f |
| Arrow land | pop on in 1 f ≈ 6 f after the cut; nudge 20 px toward the target over 6 f, ease-out; then hold (no bob) |
| Land (P-LAND) | footage ×1.12–1.2, stills/pages ×1.8–3.7 (≤ 3.0 in `fx.clip`) → 1.0 over 10–16 f, expo-out, from the cut frame: `fx.clip({land: {from, frames}})` |
| Arrow hop | 8 f in-out to the new anchor |
| Bracket grow | 13 f ease-out, from the cut frame |
| Pin drop | 60 px in 6 f with squash 1.2 × 0.8 → 1; ripple r 0 → 90 px over 18 f |
| Chip type-on | 1 letter per 2 f + a white flare on the newest letter (`fx.typewriter` `cps: 15`, `flare: {color: "#FFFFFF", px: 24, frames: 4}`); pop 7 f (0.6 → 1.08 → 1.0) |
| Hand arrow | shaft 10 f (dashoffset), head 2 f |
| Slow push | none on moving clips (their own ≈ 1%/s move is enough); locked-off clips 1.00 → 1.03; stills hold after P-LAND |
| Snap push | 1.00 → 1.80 in 6 f, ease-out |
| Counter | 18 f ease-out, landing on the spoken number ±5 f |
| Hold | text ≥ 0.25 s/word; chips ≥ 10 f after typing ends |
| Sticker | pop 7 f, cursor 8 f, tap +14 f, ghost 6 f, out 4 f |

### 10.2 Footage camera: `zoom_policy: none`
No camera presets on the host footage (the handheld selfie moves on its own; the flashes are too short). All land/punch/dolly motion is scene-level on the B-roll (P-LAND, P-SNAP-PUSH, P-PLACE-DOLLY). Never two scene-level moves starting within 0.4 s. **Measured: no shake, no rotation, no whip anywhere** (ORB affine on 16 bursts: host flashes ≤ 0.3% scale/frame; B-roll moves are the clips' own); the only roll is the place dolly's.

### 10.3 Canvas camera
OFF (`modules.canvas_camera = false`).

### 10.4 Layer order (back to front)
| z | Layer |
|---|---|
| 1 | B-roll full-bleed clip / still (P-BROLL-FULL, P-STILL-PUSH, the P-BAND-CLIP blur copy), or the world (W-grid, W-glow, W-paper, W-void) |
| 2 | Band clip (P-BAND-CLIP), whiteout layer, glow |
| 3 | Diagrams, paper cards, scale scenes |
| 4 | (host stage on L-host) |
| 5 | Chips, typed keywords, plates, hero numbers, leader labels, dimension tags |
| 6 | Ink: arrows, brackets, pins, ? marks, traces; the credit line |
| 7 | CS-1 captions |
| 8 | CTA sticker + cursor |

### 10.5 Finishing
- No grain. No vignette on footage; W-grid 0.22 and W-glow 0.35 carry their own.
- Glow only on W-glow outlines (`accent`, 14–18 px) and P-OUTLINE-TRACE.
- Footage is never regraded; match only exposure between the host takes.
- Hard shadows (0/+6–8 px, no blur) only on lime elements and the sticker. Captions use their 3 px stroke + 0/+3 shadow.

---

## §11 Sound contract (minimal) `[REQ] [VAR]`
| Line | Decision |
|---|---|
| **Cue moments** | `hook` (the G-1 cut, and the first mark landing), `reveals` (a chip, plate, hero number, pin or bracket landing; ≤ 1 per 3 s), `transitions` (T-02, T-03, T-05, T-06, T-07, T-08 only; plain T-01 cuts are silent), `cta` (the sticker tap click). No list cue |
| **Meme cues** | OFF (`comedy: off`) |
| **Music bed** | ON from f0 (curious, light, mid-tempo), ≥ 18 dB under the voice; it may drop out for ≤ 0.6 s before the payoff number |
| **Ducking** | Bed ≥ 18 dB under the voice while it speaks; creator clips' own audio is muted unless it is the point (an animal call, a machine noise), then ducked ≥ 12 dB under the voice |
| **Loudness** | −14 LUFS integrated, true peak ≤ −1.5 dBTP, hard end ≤ 6 f after the last word (NC-8) |

Sounds come from the bundled SFX pack and its global rules S1–S6 (every cue on a visible event, ≤ 2 uses per file, no consecutive repeats). Mirrored in `tokens.json → sound`.

---

## §12 Footage, shot list, fallbacks, inserts `[REQ]`

### 12.1 Setups `[DNA assumption; VAR the buyer's actual setup]`
| Setup | Spec |
|---|---|
| **A: Handheld selfie** | Phone front camera at arm's length, 9:16, 1080 × 1920 or better, 30 fps; eye level or slightly above; head top at y 180–420, face 22–34% of frame height; a home office behind (shelf, plant, a lamp), soft window key from the side; one saturated wardrobe colour (blue, red, green); hands in frame: every line gets an open-hand gesture toward the lens. Mic: a clip-on or the phone, the room quiet (this audio is the voice-over) |

### 12.2 Shot list `[DNA]`
| ID | Shot | Spec | Per 60 s | Must / optional |
|---|---|---|---|---|
| **SH-1** | Narration take | The whole script on setup A, 1–3 takes, read with energy; its audio is the voice-over | 1–3 takes | **must** |
| **SH-2** | Opening flash | The first 2–3 words with a big open-hand gesture (wave or reach), 3 takes | 1 | **must** |
| **SH-3** | Reaction drop-ins | The loop line and one payoff line, performed big (eyes wide, a hand to the head) | 1–2 | optional |
| **SH-4** | Subject B-roll | One clip per sentence of the exact thing named, 2–6 s each, vertical or 16:9 ≥ 1080 px tall; owned or held by the creator (their own shots, licensed stock in their account, CG they commissioned, screen captures of their own simulations), each with its credit text when it isn't theirs | 12–25 | **must** |
| **SH-5** | Scale reference | The subject next to a person or a known object | 0–2 | optional |
| **SH-6** | Source screenshots | The paper / article / figure page with outlet, date and the exact headline visible | 0–3 | optional |
| **SH-7** | Stills | Photos, renders, figure images ≥ 1500 px tall | 0–6 | optional |

### 12.3 Fallbacks
| ID | For | What the engine does instead | Fidelity cost | Result |
|---|---|---|---|---|
| **FB-1** | SH-1 | Nothing: the selfie narration is the spine and the host flash. Ask the creator to record it (one phone take, ≈ 3 minutes) | The reel can't be made in this style | **no_fallback** |
| **FB-2** | SH-2 | The first 2–3 words of the SH-1 take become the flash | A weaker gesture at f0 | holds |
| **FB-3** | SH-3 | Reuse the SH-1 line with the most energy as the drop-in | A less performed reaction | holds |
| **FB-4** | SH-4 | Per missing sentence, a created visual: P-VS-STACK, P-SCALE-LINEUP, P-SCALE-PERSON, P-MECHANISM-LOOP, P-BLUR-VS-SHARP, P-MAP-SCHEMATIC, or a headline/quote card | No real-world footage on those beats; the reel reads as a diagram explainer. **Holds** while ≥ 50% of the runtime is still creator clips; **degraded** below that; below 20%, tell the creator at the checkpoint that the style is not working for this reel | degraded |
| **FB-5** | SH-5 | P-SCALE-PERSON + P-MEASURE beside the created subject on W-grid | No photographic scale | holds |
| **FB-6** | SH-6 | `fx.headlineCard` / `fx.quoteCard` with the exact words from the script, P-SYNTH-TAG | No real page | holds |
| **FB-7** | SH-7 | A created diagram, or the nearest SH-4 clip with its slow push (P-BROLL-FULL) | Less literal | degraded |

### 12.4 Props, reaction bank, resolution
- **Props:** none required. A physical prop for a scale shot (a ruler, a coin, a can) makes SH-5 easy.
- **Reaction bank** (ask at the shoot, 2 s each): an open hand to the lens, a wave, eyes-wide "so many more!", a frown + reach ("look at the difference"), a point down (for the S3 sticker).
- **Matte:** none.
- **Resolution:** vertical clips ≥ 1080 px tall go full-bleed. A 16:9 clip goes full-bleed by a centre-on-subject crop only when it is ≥ 1440 px tall (≤ 1.33× upscale), or ≥ 1080 px tall **and** ≤ 3 s **and** moving (the softness hides in motion); otherwise P-BAND-CLIP. P-SNAP-PUSH ×2.4 needs a 4K source or a still ≥ 3000 px tall; below that, cap the punch at ×1.6 (soft micrographs and maps may go to ×2.4, as v03 @ 0:02.46 does).

### 12.5 Third-party inserts: ask, then create `[REQ always]`
Claude **never fetches anyone else's media.** In this style almost every borrowed picture is a clip or a paper, so the flow runs on every reel:
1. **Analyse the transcript** (`veos inserts scan`) and the B-roll bank: list the sentences whose picture would be third-party (a documentary clip, a research figure, an article, a product, a person).
2. **Ask the creator once**: "For these N moments, do you have a clip, still or screenshot you own or hold? Drop the files with their source names, or say no."
3. **Supplied:** `veos asset add <file> --origin creator`; show it as given (crop, push, annotate).
4. **Not supplied:** a created visual from the words of the script: the FB-4 diagram set, `fx.headlineCard` (outlet set in type, the exact headline), `fx.quoteCard` (verbatim), `fx.silhouette` (a person), `fx.logoPlate` (a product or institution), each with P-SYNTH-TAG.
5. **Record** every moment in `plan/inserts.json` `{id, moment, origin: creator | created, file?, recipe?, substitute_of?}`.

### 12.6 Frame rate and audio
30 fps CFR, 1080 × 1920, BT.709. The voice chain on the SH-1 audio: high-pass 80 Hz, de-ess, light compression, −14 LUFS.

---

## §13 Output contract `[REQ] [DNA]`

### 13.1 Beat schema (the first ```yaml``` block of the edit brief)
```yaml
- id: 4
  section: HOOK                    # HOOK | LOOP | COMPARE | MECHANISM-n | PAYOFF | CLIFFHANGER
  t0: 1.93
  t1: 3.05
  spoken: "may have weighed as much as a grizzly bear"
  trigger: {word: "bear", at: 2.71}
  tone: awe                        # awe | explain | warn | win | hype | cta
  line_type: "how heavy"
  layout: L-evidence
  shot_id: SH-4
  fallback_used: null              # or FB-4 …
  visual: "Low-angle forest clip of the subject; lime arrow pops onto its body on 'bear', nudges in and holds"
  layers: [clip-forest, arrow-body, credit-forest]
  pattern: P-LIME-ARROW
  caption: {profile: CS-1, overrides: []}
  anchor: {target: "object:body", keyframes: [[0.00, 610, 905], [0.50, 622, 896], [1.10, 640, 884]]}
  ink: [{mark: block_arrow, target: "object:body", frames: [63, 71]}]
  insert: {id: I3, origin: creator}
  source: null
  credit: "• SOURCE: [OUTLET]"
  sfx: [{t: 2.70, id: "<pop from the pack>", on: "arrow-body@0.77", why: "arrow lands on the named body"}]
```

### 13.2 Conditional fields (this style)
| Field | When |
|---|---|
| `shot_id`, `fallback_used` | every beat (footage_dependency high) |
| `anchor`, `ink` | every annotated beat (§17, §22) |
| `insert`, `credit` / label | every third-party or reconstructed picture (§12.5, §19) |
| `source {masthead, date, headline, highlight_spans}` | P-PAPER-HILITE / P-QUOTE-HILITE beats |
| `caption` | always (CS-1) |

### 13.3 Reel header
```yaml
format: F-A
theme: null
hook_archetype: HA-10          # HA-10 (variant S | P | D), HA-13, HA-14
hook_variant: S
structure: explainer
count: null
keyword: null                  # set only with comment_keyword
cta: {device: subscribe, word: FOLLOW, stickers: [14.2, 38.6, 54.1]}
host_share_planned: 7.4        # %
clips: {creator: 17, created: 3}
```

### 13.4 Hook proposals (3)
```yaml
- name: "Scale flash: as big as a bus"
  archetype: HA-10
  variant: S
  flash_words: "THIS ANIMAL"
  claim_chunk: "WAS AS BIG AS A SCHOOL BUS,"
  hook_pair: {subject: "the subject beside a person", reveal: "P-MEASURE bracket to the top by 1.47 s"}
  stoppers: [ST-1, ST-2, ST-3, ST-5, ST-6]
  storyboard: "f0 host wave | 0.60 cut to subject + claim | 0.67 bracket grows | 1.93 second clip | 2.10 lime arrow"
  sound: [hook cut, bracket top-out]
  stopper_test: {thumbnail: pass, mute: pass, sc_3s: 6.5, subject_by_s: 0.60}
```

### 13.5 Checkpoint
Send, then **wait for approval**:
1. 3 hook proposals with the stopper results.
2. The beat sheet with tones, patterns and `shot_id` per beat.
3. The B-roll match table: sentence → clip (or the FB-4 visual used), with the share of runtime that is creator footage.
4. The anchor plan: each annotated shot with its keyframes and a contact frame.
5. The inserts record (creator vs created) and every credit line's text.
6. The sticker schedule (S1, S2, S3 times) and the cliffhanger line.
7. The transition map and the SFX ledger.
8. Style stills: f0 (host flash), 0.7 s (subject + bracket), one arrow beat, one diagram beat, the payoff, S3 on the closing flash.

---

## §14 Worked examples `[REQ] [NICHE]`
Times are estimates; replace them with `words.edit.json` onsets. Numbers are the example script's own (script-stated); a real reel shows only what its script says. Each example is the one format F-A; together they cover the three HA-10 variants and both example niches.

### 14.1 Food & health science: "This is how much sugar is in one can" (HA-10.S, 46 s)
**Clips the creator has:** host selfie take; a can on a kitchen counter (vertical); sugar cubes being stacked (vertical); a spoon of sugar pouring (16:9, 4K); a 2-s macro of a soda pour; a screenshot of a health-agency guideline page; no liver/insulin footage.

| t (s) | Spoken | Tone | Visual | Caption | Layout | Cue |
|---|---|---|---|---|---|---|
| 0.00 | "This can…" | awe | P-HOST-FLASH: host waving the can at the lens | "THIS CAN" | L-host | — |
| 0.57 | "…has more sugar than you'd ever put in your coffee," | awe | G-1 cut to the can beside a stack of 9 sugar cubes (P-BROLL-FULL); P-MEASURE grows up the stack 0.63–1.43 | "HAS MORE SUGAR THAN YOU'D" → (1.30) "EVER PUT IN YOUR COFFEE," | L-evidence | hook cut; bracket top-out |
| 1.95 | "thirty-five grams," | awe | P-SNAP-PUSH ×1.35 on the stack (event 1.95); P-HERO-NUMBER "35 G" / "1.2 OZ" enters 2.05, counts 18 f, lands on "grams" at 2.40 | "THIRTY-FIVE GRAMS," | | hero landing |
| 2.95 | "about nine sugar cubes," | explain | Cut to the cubes falling into a glass (P-BROLL-FULL); P-LIME-ARROW lands on the cubes at 3.10 | "ABOUT NINE SUGAR CUBES," | | — |
| 4.30 | "and your body handles it in a really sneaky way!" | hype | P-HOST-DROPIN (1.8 s), eyes wide | "AND YOUR BODY HANDLES IT" → "IN A REALLY SNEAKY WAY!" | L-host | — |

**SC 0–3 s:** cut 0.57 (1) + caption (0.5) + bracket enters (1) + caption 1.30 (0.5) + snap event 1.95 (1) + caption (0.5) + hero enters (1) + hero lands 2.40 (1) + cut 2.95 (1) + caption (0.5) = **8.0** ✓. No credit: every clip is the creator's own.

| Section | Span | Spoken gist | Patterns |
|---|---|---|---|
| COMPARE | 6.1–13.5 | "A can, a doughnut and a bowl of fruit can have similar sugar…" | P-VS-STACK on W-grid: CAN / DOUGHNUT / FRUIT BOWL (created specimens: flat illustrations) → P-VS-FOCUS on CAN as it's named → P-XRAY-SWAP to W-glow: each turns into a neon outline with its sugar as stacked cubes inside (same scale) |
| MECHANISM-1 | 13.5–21.0 | "Liquid sugar hits your blood fast…" | Pour macro (P-BROLL-FULL) + P-KW-WORD "GLUCOSE"; S1 sticker at 17.2 over the pour; P-MECHANISM-LOOP (gut → blood → liver, a dot travelling) because there is no organ footage (FB-4) |
| MECHANISM-2 | 21.0–30.5 | "Your liver turns the extra into fat…" | P-MECHANISM-LOOP continues with the liver node lit; P-ALERT-CHIP "FAT STORAGE" over the liver node |
| MECHANISM-3 | 30.5–37.5 | "Guidelines say about 25 grams a day for most adults…" | The creator's screenshot of the guideline page: P-PAPER-HILITE on the exact sentence, credit "• SOURCE: [AGENCY]"; S2 sticker at 33.8 |
| PAYOFF | 37.5–41.5 | "One can is already over the line." | P-SCALE-LINEUP: the 25 g line vs the 35 g stack, one ground line, "25 G / 0.9 OZ" and "35 G / 1.2 OZ" tags; ✓-less (it's a warning): the 35 g stack's top glows `bad` |
| CLIFFHANGER | 41.5–46.0 | "But the drink with the most hidden sugar isn't soda… to find out which, follow!" | Dark silhouettes of 3 bottles + P-QMARK-SWARM; S3 "FOLLOW" pops at 44.3 over the silhouettes; P-HOST-CLOSE 44.9–46.0 pointing down at it |

Host share: 0.57 + 1.8 + 1.1 = 3.5 s / 46 s = **7.6%** ✓. Inserts: guideline page (creator screenshot, credited); the organ path is created (P-MECHANISM-LOOP, no label: a diagram, not a reconstruction).

### 14.2 Tech & AI: "Why your phone can see in the dark" (HA-10.D, 50 s)
**Clips:** host take; the creator's own night photo taken twice (normal mode, night mode); a screen recording of the camera app; a 4K tripod time-lapse of a dark street; a macro of the phone's camera lens; no sensor footage.

| t (s) | Spoken | Tone | Visual | Caption | Layout | Cue |
|---|---|---|---|---|---|---|
| 0.00 | "Look at the difference…" | awe | P-HOST-FLASH: frown, reaching toward the lens | "LOOK AT THE DIFFERENCE" | L-host | — |
| 0.60 | "between this…" | awe | G-1 cut to W-void: the normal-mode photo in the top half (y 260–760); a P-LIME-ARROW lands on its noisy shadows at 0.90 | "BETWEEN THIS…" | L-evidence | hook cut |
| 1.30 | "…and this!" | awe | T-02 seam wipe: the night-mode photo draws in below (9 f) | "AND THIS!" | | seam swish |
| 2.20 | "Same phone, same street, same second." | explain | P-SNAP-PUSH ×1.35 on the seam (the 1080p photos cap the snap) | "SAME PHONE, SAME STREET," → (2.90) "SAME SECOND." | | — |
| 3.60 | "The trick is that it never takes just one photo," | explain | P-HAND-ARROW (accent) draws from the top photo into the bottom one | "THE TRICK IS THAT IT NEVER" → "TAKES JUST ONE PHOTO," | | arrow draw |
| 5.40 | "and that changes everything!" | hype | P-HOST-DROPIN 1.6 s | "AND THAT CHANGES EVERYTHING!" | L-host | — |

**SC 0–3 s:** cut 0.60 (1) + caption (0.5) + arrow enters 0.90 (1) + wipe event 1.30 (1) + caption (0.5) + snap event 2.20 (1) + caption (0.5) + caption 2.90 (0.5) = **6.0** ✓. No credit: the creator's own photos.

| Section | Span | Spoken gist | Patterns |
|---|---|---|---|
| COMPARE | 7.0–15.0 | "A normal photo grabs light for a fraction of a second; night mode grabs many" | P-SCALE-LINEUP turned into time: one frame tile vs a row of 12 frame tiles on W-grid (created), dual-free (time); P-KW-CHIP "12 FRAMES" (script-stated) |
| MECHANISM-1 | 15.0–23.5 | "Each frame is noisy, but the noise is random…" | Created dot-field P-BLUR-VS-SHARP: 12 noisy layers stacking into a clean one (each layer a seeded dot field); S1 sticker at 18.4 |
| MECHANISM-2 | 23.5–32.0 | "So the phone lines them up and averages them…" | The creator's camera-app screen recording (P-BAND-CLIP: 16:9 at 1080p, 5 s) + P-LEADER-LABEL on the shutter progress ring "HOLD STILL" |
| MECHANISM-3 | 32.0–40.0 | "…and a model guesses the colours the sensor missed." | Lens macro (P-BROLL-FULL) + P-LENS-IRIS into the created sensor grid (W-void), P-OUTLINE-TRACE (accent) around one pixel group; S2 sticker at 34.9 |
| PAYOFF | 40.0–45.0 | "That's how a tiny lens sees what your eyes can't." | Back to the split: P-SPLIT-REVEAL replay + good ✓ chip "NIGHT MODE" |
| CLIFFHANGER | 45.0–50.0 | "But some phones can see through fog… to see how, subscribe!" | The street time-lapse darkened to a silhouette + P-QMARK-SWARM; S3 "SUBSCRIBE" at 48.2; P-HOST-CLOSE 48.8–50.0 |

Host share 0.6 + 1.6 + 1.2 = 3.4 s / 50 s = **6.8%** ✓.

### 14.3 Tech & AI: "Where your photos actually live" (HA-10.P, 40 s)
**Clips:** host take; an aerial drone clip of a data-centre campus (licensed in the creator's stock account, credit "• SOURCE: [STOCK LIBRARY]"); a server-rack walk-through (creator's own visit); a still of a cooling tower; no map footage.

| t (s) | Spoken | Tone | Visual | Caption | Layout | Cue |
|---|---|---|---|---|---|---|
| 0.00 | "Your photos live here…" | awe | P-HOST-FLASH: host pointing down at the phone | "YOUR PHOTOS LIVE HERE…" | L-host | — |
| 0.58 | "…in a building you've never heard of," | awe | G-1 cut to P-MAP-SCHEMATIC (created: no map footage), the region name in type, P-PLACE-DOLLY 1.0 → 1.5 + roll; P-MAP-PIN grows at 0.75 + ripple | "IN A BUILDING YOU'VE" → "NEVER HEARD OF," | L-diagram | hook cut; pin |
| 1.75 | "as long as ten football fields." | awe | Cut to the aerial clip (credit fades in 1.95); P-DIM-LABEL along the roof: "1,000 M" / "3,281 FT" (script-stated) | "AS LONG AS TEN FOOTBALL FIELDS." | L-evidence | tag pop |
| 3.40 | "Inside, it's loud, hot and full of blinking lights" | explain | Cut to the rack walk-through; P-LIME-ARROW on a blinking rack | "INSIDE, IT'S LOUD, HOT" → "AND FULL OF BLINKING LIGHTS" | | — |
| 5.20 | "and it never, ever turns off!" | hype | P-HOST-DROPIN 1.7 s | "AND IT NEVER, EVER TURNS OFF!" | L-host | — |

**SC 0–3 s:** cut (1) + cap (0.5) + dolly start (1) + pin (1) + cap 1.2 (0.5) + cut 1.75 (1) + cap (0.5) + credit (1) + tag (1) = **7.5** ✓.

| Section | Span | Spoken gist | Patterns |
|---|---|---|---|
| COMPARE | 6.9–12.5 | "Your phone holds about a thousand photos; this building holds billions" | P-SCALE-LINEUP: a phone silhouette → a shelf → the building, each with its photo count chip (script-stated) |
| MECHANISM-1 | 12.5–20.0 | "Every photo is copied to at least three places" | P-MAP-SCHEMATIC again with 3 pins dropping in sequence + P-MECHANISM-LOOP arrows between them; S1 sticker at 15.6 |
| MECHANISM-2 | 20.0–28.5 | "and all those machines make heat" | The cooling-tower still (P-STILL-PUSH) + P-HERO-NUMBER "40 °C" / "104 °F" (script-stated) + P-ALERT-CHIP "HEAT" |
| PAYOFF | 28.5–34.0 | "So the 'cloud' is really a very big, very hot room." | The aerial again, P-SNAP-PUSH ×1.35 on the roof; P-KW-WORD "THE CLOUD" |
| CLIFFHANGER | 34.0–40.0 | "But one company put theirs under the sea… to see it, subscribe!" | A dark created silhouette of a capsule on W-void + P-QMARK-SWARM; S3 at 38.4; P-HOST-CLOSE 38.9–40.0 |

Host share 0.58 + 1.7 + 1.1 = 3.4 s / 40 s = **8.5%** ✓. A 40 s reel gets S1 + S3 only (S2 needs ≥ 45 s).

---

## §15 QA checklist `[REQ] [DNA]`

**1. Profile conformance**
- [ ] Format F-A; host share 4–11%, the longest absence ≤ 52 s (V-PRESENCE); 35–60 s (review).
- [ ] Layout runs: L-host 0.45–2.6 s each; shares inside L-host 4–11%, L-evidence 55–92%, L-diagram 4–35% (V-LAYOUT).

**2. Hook**
- [ ] f0: the host mid-gesture + caption chunk 1; nothing else on screen (V-F0).
- [ ] A `kind: subject` scene full-frame by 0.70 s (V-F0 payoff); ≥ 6 weighted SCs in 0–3 s (V-CADENCE).
- [ ] The first annotation lands on its target by 1.5 s (review); the loop drop-in by 7 s (review).

**3. Body and cadence**
- [ ] 4–8 weighted SCs per 10 s; a weight-1 change every ≤ 2.5 s; nothing static > 1.5 s (V-CADENCE).
- [ ] One sentence, one picture; no shot > 4.0 s without a new mark or cut; no clip shows something other than what's said for > 0.5 s (review).
- [ ] Marks land within ±5 f of their trigger words (V-ONWORD); ≤ 3 marks on screen (review).
- [ ] ≤ 4 non-cut transitions per 60 s; ≤ 1 whiteout; ≤ 2 snap pushes (review).

**4. Captions**
- [ ] CS-1: ALL CAPS, one line, ≤ 28 characters, ≤ 7 words, hard swaps, cy 1470, 48 px (E3), never coloured (V-CAPTION, V-TYPE).
- [ ] Sync lead ≤ 0.15 s; glossary spellings exact (V-CAPTION).

**5. Modules**
- [ ] §17/§22 anchors: every arrow tip within 40 px of its target on every sampled frame; none on a face (review + V-FACE).

**6. Truth and inserts**
- [ ] Every number on screen is in the script; every measure shows both unit systems (V-NUMFMT).
- [ ] `plan/inserts.json` covers every scanned moment; quotes and headlines verbatim (V-INSERTS).

**7. Sound contract**
- [ ] Cues only on the hook cut, reveals, non-cut transitions and sticker taps; no meme cues; bed ≥ 18 dB under the voice (S1–S6, NC-8).

**8. End and export**
- [ ] Stickers: S1 in 10–26 s, S2 only if ≥ 45 s, S3 on the CTA word; ≥ 15 s apart; none in the first 8 s (V-PROMISE + review).
- [ ] The cliffhanger asks the next question; a comment keyword (if chosen) on screen ≥ 1.5 s (V-PROMISE).
- [ ] Hard end ≤ 6 f after the last word, no black tail; 1080 × 1920, 30 fps; −14 LUFS, TP ≤ −1.5 dBTP.

---

## Conditional modules

## §16 Frame template / chrome
OFF (`modules.chrome = false`): the frame changes with every clip; only the caption band and the credit slot are fixed, and they are tokens, not slots.

## §17 Running state & anchored graphics `[COND: modules.anchors] [DNA mechanics]`
**17.1 Running state:** OFF (`modules.running_state = false`): no counters persist across cuts.

**17.2 Anchors (ON).** Every arrow, bracket, pin, trace, leader line and chip that refers to something inside a clip is anchored to it.
- **Targets:** `object:<label>` (a part in the clip: "wing joint", "the stack top"), `region:{x,y,w,h}` (an area), or `point` pairs for brackets and dimension arrows. Never `face` (marks don't point at people's faces).
- **The anchor pass (P8c).** For each annotated shot, generate a contact sheet of the clip span at 6 fps (`veos sheet` on the asset's frames, or `veos render --test` frames of the beat), read the target's pixel position on the 1080 × 1920 frame (after the full-bleed crop and the push), and write keyframes `[[t, x, y], …]` every 0.17–0.5 s (denser while the target moves faster than 60 px/s).
- **Follow modes:** `static` when the target moves < 40 px over the mark's life (one position, held); `keyframes` otherwise (the mark position = `ctx.lerp` between keyframes with ease in-out). `track` (automatic tracking) is not used.
- **Today's engine:** `ctx.anchor()` and `plan/anchors.json` (E-15) aren't built yet. Write the keyframes as a constant array at the top of `scenes.js` (`const A_WING = [[0, 610, 820], [0.5, 640, 800]];`) and interpolate inside the scene's `render`; copy the same keyframes into the beat's `anchor` field so the reviewer can check them. When E-15 ships, move them to `plan/anchors.json` unchanged.
- **Placement rules:** the arrow tip sits 24 px outside the target edge, pointing in; the arrow body lies outside the target and outside the caption, sticker and credit bands; the arrow never crosses the face box + 40 px; when two marks point at nearby targets, they come from opposite sides (P-PINCER-ARROWS).
- **Check:** every sampled frame, the mark is within 40 px of the interpolated target (review now; V-STATE when E-15 lands).

## §18 Data contract
OFF (`modules.data_figures = false`): the style states numbers, it doesn't compute them. Numbers follow §5.5 (dual units via `ctx.fmtNum`) and NC-6. A reel whose script needs a calculation uses P-HERO-NUMBER on the stated result only.

## §19 Evidence & citations `[COND: modules.citations] [DNA]`
- **Credit line (P-CREDIT-LINE):** Inter Tight 600, 24 px, caps, white 75%, a 10 px lime dot, x 64, text top y 140; on from the cut frame and stays for the whole shot (carried across consecutive clips of the same source). Text: "• SOURCE: [NAME]" with the name the creator gives (outlet, author, institution, stock library, "[AUTHOR] ET AL. / [JOURNAL] [YEAR]"). Optional: nothing requires a credit line.
- **Required on:** every creator-supplied third-party clip, still, figure and page (≈ 85% of B-roll shots in the evidence). **Not on:** the creator's own footage, created diagrams, the host.
- **Source card (P-PAPER-HILITE):** the creator's screenshot via `fx.shot` / `fx.citationStrip`, or a created `fx.headlineCard` with the outlet set in type, the date and the exact headline; `highlight_spans` swept in lime (`source_card.highlight: marker`, colour `primary`); the body is `TC-decorative`.
- **Rules:** headlines and quotes verbatim (NC-13); one card per claim; claims without a source are flagged at the checkpoint, and the line is shown with footage only (no card).
- **Figure numbering:** off.
- **Validator:** V-CITE (source fields, verbatim headline, highlight spans, credit present) and V-INSERTS.

## §20 Dialogue
OFF (one voice).

## §21 Canvas camera
OFF (`graphics: support`; pushes are scene-level, §10.2).

## §22 Ink & annotation layer `[COND: modules.ink] [DNA look; TUNE colour]`
| Mark | Stroke / shape | Colour | Draw-on | Life |
|---|---|---|---|---|
| **Block arrow** (P-LIME-ARROW, P-ARROW-HOP) | A filled chunky arrow ≈ 210 × 150 px, shaft 40% of head width; 6 px `edge` outline; hard shadow 0/+6 | `primary` | pops on in 1 f, nudges 20 px in over 6 f | holds; glides along the part 1.5–2.5 s when the line follows it |
| **Marker arrow** (P-PINCER-ARROWS) | A curved stroke, 16–24 px wide, round caps, a filled head 56 px; 4 px `edge` outline | `primary` | shaft 8 f, head 2 f | holds |
| **Hand arrow** (P-HAND-ARROW) | A curved stroke 20 px, round caps, open head | `accent` | shaft 10 f, head 2 f | holds |
| **Measure bracket** (P-MEASURE) | An 8 px line, 56 px flat foot cap, top arrowhead | `paper` | grows 13 f from the ground, from the cut frame | holds |
| **Dimension arrow** (P-DIM-LABEL) | A 6 px two-headed line + the TX-4 tag | `paper` + `primary` tag | grows ≈ 22 f; the tag's number rolls with the length | holds |
| **Pin + ripple** (P-MAP-PIN) | A 64 × 88 px pin, `edge` outline; ripple ring 4 px | `primary` | grows from its tip 8 f; ripple 18 f, repeat once | holds |
| **? marks** (P-QMARK-SWARM) | Montserrat 900 glyphs 72–110 px, 5 px `edge` stroke | `primary` | pop 3 f stagger | wobble ±6° / 20 f |
| **Trace** (P-OUTLINE-TRACE) | A 6 px line + 14 px glow along the region outline | `bad` or `accent` | 18–24 f along the path | holds |
| **Leader line** (P-LEADER-LABEL) | 3 px | `paper` | 6 f from the part | holds |
| **Highlighter** (P-PAPER-HILITE) | A lime bar behind the words, 0.9 × line height | `primary` | 0.5 s per span, left → right | holds |

**Rules:** ≤ 3 marks on screen; marks finish drawing before the next cut and leave with it (0 f); never on a face; never inside the caption, sticker or credit bands; the mark always sits on the thing being named (§17.2). `ink.stroke.width` TUNE 12–28 px.

## §23 Continuity
OFF: no morph chains or motifs; shots are hard-cut by design.

## §24 Series furniture
OFF (`modules.series = false`, VAR). A buyer who runs a numbered series turns it on: a "#[N]" lime chip in the credit band's right end (x 900–1016), 1 s at the first subject cut. The look is DNA.

## §25 Sponsor, brand & end cards
OFF (`modules.brand = false`, VAR; no end card: the reel ends on the host). A sponsored reel still follows NC-12: the sponsor is said aloud and a `TC-legal` "{{BV-01.handle|@yourhandle}} · Paid partnership" line sits in the credit slot for ≥ 2 s.

---

## Part C. Exceptions and the non-overridable core
- **Declared exceptions: E3 only** (audit 2026-10: CS-1 captions 48 px, floor 46, one line, 700, 2 px black stroke, ≥ 7 : 1). Everything else stays inside G1–G4 as written: labels ≥ 40 px, the credit line is `TC-legal` (22 px floor, 24 used), nothing behind the host, no chaos bursts, no hard-swap slots (subtitle swaps are exempt from G3).
- **Why E3:** the measured captions are 45–47 px bold (cap height 31 px, v01 @0:19); at 60 px they read as a different, heavier style, so E3 keeps them at 48 px; the label-size dual-unit sub-lines (≈ 36 px measured, v01 @ 0:57) were raised to 44 px.
- **NC-1…NC-14 hold as written.** Most relevant here: NC-6 (numbers only from the script), NC-7 (creator-owned media; never fetched), NC-13 (quotes verbatim), NC-14 (blur personal data in any screenshot).
- A buyer may not add exceptions without a logged DNA deviation; switching none off is n/a.

## Part D. Personalisation
**D.1 Setup questions (one round, each with "keep the template default"):**
| BV | Question | Lands on | Default |
|---|---|---|---|
| BV-01 | Your name and handle | `creator.name`, `creator.handle`; the disclosure line | the creator / @yourhandle |
| BV-02 | One or two brand colours | `roles.primary` (the lime: arrows, chips, sticker) then `roles.accent` (the blue glow); contrast-nudged against `edge` / `paper` | `#C6F000`, `#2F6BFF` |
| BV-05 | Language you speak / caption language | `profile.language`, always asked: **English** → English captions (default) · **Hinglish** → romanised Hinglish captions · **Hindi** → Devanagari captions; numbers follow (BV-06) | English ({{BV-05.speech|en}} → {{BV-05.captions|en}}) |
| BV-08 | Your CTA: subscribe / follow, comment keyword, or link in bio (+ the keyword) | `profile.cta.chosen`, the S3 sticker text | subscribe (sticker word FOLLOW on Instagram) |

**D.2 What a buyer can tweak later:** caption size 56–68 px and cy 1400–1460 (TUNE); fonts inside each slot's class; the credit prefix (VAR); the sticker word and count (2–3); cadence ±15%; host share ±10 points; the series chip and sponsor line on/off (VAR). DNA (deviation, warned): the host flash at f0, one-line ALL CAPS captions, the single lime meaning "look here", credits on borrowed footage, dual units, the cliffhanger close, no comedy.

**D.3 NICHE slots, filled per reel:** §6.4 hook pairs (one row per reel at P7), §8.4 lookup (new line types → existing patterns, ≤ 10 new patterns from existing families over time), §14 (the first approved reel of the buyer's niche becomes its example), App. A (approved flash lines and post titles), the glossary.

## Part E. Changes (template log and deviations from the architects' table)
| Version | Date | Change |
|---|---|---|
| v1 | 2026-10-06 | First draft from v01–v03 frame sheets and `analysis/short/cleo-abram.md` |
| v1.1 | 2026-10-07 | Motion completeness pass (full-frame-rate bursts + ORB affine, `docs/audit/science-flash/completeness.md`): P-LAND and P-RECAP-RUN added; arrow pop-and-hold (no bob); punch-in cut ×2.46; bloom flip; conveyor-scroll stack; rolling dimension tag; sticker rise/ride/1 s fade; credit and marks cut with the shot; closing flash 0.6–0.8 s |
| v1.2 | 2026-10-07 | Engine built-ins: P-LAND = `fx.clip({land})`, P-PLACE-DOLLY = `fx.clip({land, rotate})`, P-KW-WORD / chip flare = `fx.typewriter({flare})`, T-03 whiteout and T-07 bloom flip = the built-in `flash` transition; the rolling dimension tag stays bespoke (`data_figures` off) |

**Deviations from `STYLE-COVERAGE.md` (row 6), with evidence:**
| Coverage says | Template does | Why |
|---|---|---|
| Subscribe sticker ×3 (scheduled) | **2–3**: S1 (10–26 s), S2 only in reels ≥ 45 s, S3 at the end | Every evidence video shows exactly 2 (v01 @ 0:25, 0:57; v02 @ 0:14, 0:35; v03 @ 0:12, 0:52); a third fits only the longer reels at the observed ≈ 20 s spacing |
| Hook SC 8 | `hook_sc_3s` **6** | Weighted counts (captions × 0.5) are v01 ≈ 5.5, v02 ≈ 9, v03 ≈ 5.5; 8 was an unweighted count. The §6.2 recipe reaches 6.5 |
| Caption y ≈ 1520 → lift to ≤ 1500 | **cy 1470** at **48 px** (E3) | the line's bottom (≈ 1496) stays inside y 1500 |
| Sticker word SUBSCRIBE | **FOLLOW** on Instagram, SUBSCRIBE when cross-posted to YouTube Shorts (VAR) | Instagram reels have no subscribe button; the device stays `subscribe` |
| Readiness R4 | R4, plus FB-1 `no_fallback` for the selfie narration | The selfie take is both the voice and the host flash; a VO-only reel can't make D1 |

## Part F. ID index (this playbook)
| Prefix | IDs |
|---|---|
| D | D1–D8 |
| H / N | H1–H16 / N1–N12 |
| W | W-host, W-void, W-grid, W-glow, W-paper |
| L | L-host, L-evidence, L-diagram |
| G | G-1 flash-out, G-2 drop-in, G-3 closing flash |
| CS | CS-1 |
| TX | TX-1…TX-10 |
| HA | HA-10 (default; variants HA-10.S / .P / .D), HA-13, HA-14 |
| ST | ST-1, ST-2, ST-3, ST-5, ST-6 |
| S (stickers) | S1, S2, S3 |
| B | B-1…B-10 |
| P | 47 patterns: P-HOST-FLASH, P-HOST-DROPIN, P-HOST-CLOSE, P-BROLL-FULL, P-STILL-PUSH, P-BAND-CLIP, P-SNAP-PUSH, P-SPLIT-REVEAL, P-STATE-SWAP, P-WHITEOUT, P-LENS-IRIS, P-LAND, P-RECAP-RUN, P-PLACE-DOLLY, P-LIME-ARROW, P-ARROW-HOP, P-PINCER-ARROWS, P-HAND-ARROW, P-MEASURE, P-DIM-LABEL, P-MAP-PIN, P-QMARK-SWARM, P-REC-HUD, P-OUTLINE-TRACE, P-LEADER-LABEL, P-KW-CHIP, P-KW-WORD, P-ALERT-CHIP, P-TITLE-PLATE, P-HERO-NUMBER, P-VS-STACK, P-VS-FOCUS, P-XRAY-SWAP, P-SCALE-LINEUP, P-SCALE-PERSON, P-BLUR-VS-SHARP, P-MECHANISM-LOOP, P-ANALOGY-SCENE, P-MAP-SCHEMATIC, P-PAPER-HILITE, P-QUOTE-HILITE, P-FIGURE-CARD, P-CREDIT-LINE, P-SYNTH-TAG, P-SUBSCRIBE-TAP, P-KEYWORD-TAP, P-CLIFFHANGER |
| T / R | T-01…T-09 / R-1, R-2 |
| SH / FB | SH-1…SH-7 / FB-1…FB-7 |
| F | F-A |
| Validator cites | H1→V-F0, H2→V-CADENCE, H3→V-F0, H4→V-TITLE, H5→V-CADENCE, H6→V-ONWORD, H7→V-FACE, H8→V-PRESENCE, H9→V-PROMISE, H10→V-INSERTS, H11→V-NUMFMT, H12→V-CAPTION, H13→V-HUES, H14→V-SAFE |

---

## App. A Headline & hook bank `[NICHE]`
Flash words (f0) + claim chunk + the post title. Replace [SLOTS] from the reel's script; numbers only as the script states them.

| # | Variant | Flash words → claim chunk | Post title |
|---|---|---|---|
| 1 | HA-10.S | "THIS [THING]" → "IS AS BIG AS A [FAMILIAR OBJECT]," | How This [Thing] Got So Big |
| 2 | HA-10.S | "THIS [ANIMAL / MACHINE]" → "CAN [VERB] FASTER THAN A [FAMILIAR THING]," | How This [Thing] Could [Verb] |
| 3 | HA-10.P | "THEY FOUND SOMETHING" → "HIDDEN UNDER [PLACE]…" | They Found Something Hidden Under [Place] |
| 4 | HA-10.P | "EVERY [EVERYDAY THING]" → "STARTS IN [PLACE]," | Where Your [Everyday Thing] Actually Comes From |
| 5 | HA-10.D | "LOOK AT THE DIFFERENCE" → "BETWEEN THIS…" / "AND THIS!" | This [Instrument / Technique] Is Insane |
| 6 | HA-10.D | "SAME [THING]," → "SAME [SETTING], WATCH THIS!" | Why Your [Device] Can [Surprising Ability] |
| 7 | HA-10.S | "INSIDE YOUR [BODY PART]" → "ARE [NUMBER] [THINGS]," | What's Really Inside Your [Body Part] |
| 8 | HA-13 | (action clip) "[THING] JUST [DID SOMETHING]," → host: "AND NOBODY EXPECTED IT!" | The Day [Thing] [Did Something] |
| 9 | HA-14 | (strongest image) "THIS IS THE [SHARPEST / BIGGEST] [THING] EVER [VERBED]." | The [Sharpest / Biggest] [Thing] Ever [Verbed] |
| 10 | HA-10.S | "THIS TINY [THING]" → "HOLDS MORE [X] THAN [BIG FAMILIAR THING]," | How Something This Small Holds So Much [X] |

Niche fills `[NICHE: example]`: Tech & AI: #1 "THIS BUILDING / IS AS LONG AS TEN FOOTBALL FIELDS,"; #6 "SAME PHONE, / SAME STREET, WATCH THIS!"; #10 "THIS TINY CHIP / HOLDS MORE SWITCHES THAN…". Food & health: #1 "THIS CAN / HAS MORE SUGAR THAN…"; #4 "EVERY CUP / STARTS IN THE MOUNTAINS,"; #7 "INSIDE YOUR GUT / ARE TRILLIONS OF BACTERIA,".

## App. B Evidence map `[DNA; templates only]`
The full source map (every DNA rule → `vNN @ m:ss`) and the `(unverified)` list live in `evidence.md` next to this playbook. Sources: `vibe-editing-os-research/analysis/short/cleo-abram.md`; frame sheets `evidence/short/cleo-abram/v01–v03/sheets/` (hook at 6 fps, the whole video at 1 fps). Unverified: the speech language beyond the burnt-in captions (no transcripts), all sound (not observable; the bed decision is the template's), the subscribe device's spoken wording on Instagram.
