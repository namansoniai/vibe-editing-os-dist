# Whiteboard Split Style Playbook (template v1)

**Purpose.** You (Claude) receive one talking-head take of {{BV-01.name|the creator}} ({{BV-01.handle|@yourhandle}}) teaching a framework, a before/after model or a step-by-step workflow. This playbook makes you cut it into a **three-band whiteboard split** (an animated card on top, a one-word caption band, the creator in a rounded window below) that **punches to the full face** on every claim, builds **one recurring diagram** the viewer learns to read, and ends on a keyword CTA with a preview of the thing they get. Input expected: `source_type: talking_head` (SW-01), ideally a 4K landscape take (§12).

**Style DNA** `[DNA]`. A teacher at a whiteboard, cut like a thriller. The top two-thirds of the frame is a clean card band (warm grid paper or a black neon stage) where a headline in bold sans with one *italic-serif* word and a crimson key phrase sits above a diagram that draws itself one spoken term at a time. Between the card and the face window, the caption shows **one word at a time**. Every 2–7 seconds the picture **hard-cuts to a full-frame close-up** of the face for the claim, then cuts back to a card that has moved on. The same diagram returns at every step with the active part lit, so the reel feels like one idea unfolding.

**Copy these 5 things** (each one is load-bearing):

| # | Trait | Implemented in |
|---|---|---|
| 1 | **Three-band split:** card band y 150–1160, caption band at cy 1245, rounded face window x 64–1016, y 1400 → bleeds off the bottom, radius 30 | §3.2 L-split, §16 slots |
| 2 | **Mode schedule:** hard cut to the full face (L-full) on a claim word, 3–8 times per 60 s; full runs 0.8–4.5 s (median 2.2), split runs 1.5–18 s (median 5.5); 15–35% of runtime full-face; about half the longer full runs step tighter on a jump cut | §3.2 schedule, H3, §9 |
| 3 | **One-word captions:** Inter Tight 700, as spoken, hard swap (no pop); 56 px at cy 1245 in the split (black on paper, white on stage), 66 px at cy 1160 on the face; a rare italic-serif keyword swap | §5.3 CS-1 / CS-2 |
| 4 | **Mixed-type lockup:** bold sans + one *Instrument Serif italic* span + a crimson key phrase or crimson underline, Title Case, ≤ 8 words | §5.2 LK-1…LK-5 |
| 5 | **Diagrams that draw on the words + one recurring diagram:** neon curves and nodes on black or ink lines on grid paper; the framework diagram returns at every step with the active node lit | §8 P-CURVE-DRAW, P-MOTIF-*, §23 |

### Directives `[DNA]`
| # | Directive | Where it lives |
|---|---|---|
| D1 | **Show the framework, don't just say it.** Every named idea, step, number and tool appears in the card band on its word | §8.4, H7 |
| D2 | **The claim gets the face.** Opinions, warnings and turns ("but", "instead", "the reason is") are said full-face, with nothing else on screen but the one-word caption | §3.2, H3 |
| D3 | **One idea per card.** A card evolves (node by node) while its idea lasts and is replaced when the idea changes; never two cards side by side | §8.2, N4 |
| D4 | **One recurring diagram per reel.** It is built once, visited at every step with the active part lit, and recapped at the end | §23, H12 |
| D5 | **The caption is the pulse.** One word at a time, always on, in its own band; it never sits on a card or on the face | §5.3, H4 |
| D6 | **The lockup is the title of the moment.** Bold sans + one italic-serif span + crimson; it changes when the card's idea changes | §5.2, H6 |
| D7 | **Quiet colour, loud ideas.** Neutral worlds; colour only marks meaning (crimson = the key phrase, neon = the active part, red/green = old/new, yellow = the threshold) | §4 |
| D8 | **Truthful diagrams.** Concept curves carry concept labels, never invented numbers; every number on screen is spoken, scripted or the creator's own | H11, §18 |

Buyer directives are added as **BD1…** `[VAR]` and may only make the style stricter or more specific.

### Quick index
| § | What | Status |
|---|---|---|
| §0 | Style profile (switches) | ON |
| §1 | Procedure | ON |
| §2 | Hard rules, exceptions, NEVER list | ON |
| §3 | Worlds, layouts, mode schedule, stage moves, safe zones | ON |
| §4 | Colour | ON |
| §5 | Type, lockups, captions | ON |
| §6 | Hook system | ON |
| §7 | Structure and cadence | ON |
| §8 | Visual system: 50 patterns | ON |
| §9 | Transitions | ON |
| §10 | Motion, camera, layers, finishing | ON |
| §11 | Sound contract | ON |
| §12 | Footage, fallbacks, inserts | ON |
| §13 | Output contract | ON |
| §14 | Worked examples (3) | ON |
| §15 | QA | ON |
| §16 | Frame template / chrome | **ON** |
| §17 | Running state & anchors | OFF |
| §18 | Data contract | **ON** |
| §19 | Evidence & citations | OFF |
| §20 | Dialogue | OFF |
| §21 | Canvas camera | OFF |
| §22 | Ink | OFF |
| §23 | Continuity (recurring diagram) | **ON** |
| §24 | Series | OFF |
| §25 | Sponsor, brand & end cards | OFF |
| Parts C–F | Exceptions, personalisation, changes, IDs | — |
| App. A / B | Headline bank / evidence map | — |

Format list: **F-A "Whiteboard split"** (the only format).

---

## §0 Style profile `[REQ]`

```yaml
profile:                         # mirrored in tokens.json -> profile
  source_type: talking_head
  presenter: {presence: anchor, share: [90, 100], max_absence_s: 4}
  spine: talking_head
  captions: {mode: full, role: primary, mute_policy: mute_safe}
  graphics: primary
  duration: {class: standard, target_s: [60, 90]}
  language: {speech: en, captions: {lang: en, script: Latn, transform: verbatim}, on_screen: en, post_title: en,
             supported: [[en, en, Latn], [hinglish, hinglish, Latn], [hi, hi, Deva]]}
  numbers: {grouping: international, currency: "$", compact: k_m_b, units: metric, decimals: 0}
  tone: {energy: balanced, comedy: off, comedy_max: off}
  themes: {policy: single, packs: [], default: null}
  formats: {list: [F-A], default: F-A}
  footage_dependency: low
  cta: {devices: [comment_keyword, link_bio, post_only], placement: end, chosen: comment_keyword}
  modules: {chrome: true, running_state: false, anchors: false, data_figures: true, citations: false,
            dialogue: false, canvas_camera: false, ink: false, continuity: true, series: false, brand: false}
```

Why each value:
- **source_type talking_head:** all three reference reels are one presenter to camera; the full-face shots are a tighter crop of the same session (v01 @ 0:01.8, v03 @ 0:03).
- **presence anchor 90–100, max absence 4 s:** a face is on screen ≈ 95% of runtime (window or full); the only absences are full-bleed example clips of 2–4 s (v02 @ 1:12–1:15, 1:18–1:22).
- **spine talking_head:** the take is the timeline; cards are inserted on its words.
- **captions full / primary / mute_safe:** a one-word caption is on screen ≈ 98% of runtime and is the pulse of the edit; the reel reads on mute through captions + lockup + diagram.
- **graphics primary:** a card occupies 55–65% of runtime and carries the argument (curves, loops, UI flows).
- **duration standard 60–90 s:** evidence 62.7, 74.0, 107.6 s; 107 s is a `long` outlier the buyer may tune to (adjacent class).
- **language en:** read from the burnt-in captions (no transcript, `unverified` for speech); the other three combinations are supported because the style's devices survive them (§5.5).
- **numbers international, K/M compact:** "10K followers", "408K subscribers", "70%" (v02 @ 0:38, 1:43; v01 @ 0:27). Indian buyers get Indian grouping automatically (BV-06).
- **energy balanced, comedy off:** fast delivery (≈ 3.2 words/s) but no gags, stickers or meme cues anywhere in the evidence.
- **themes single:** the accent system never changes; what changes per section is the **world** (paper ↔ stage), handled in §3.1 (a deliberate deviation from the coverage table, Part E).
- **footage_dependency low:** one take is enough; everything else can be built. A 4K landscape take is what makes the full-face punch sharp (§12.4).
- **cta comment_keyword (+ link_bio, post_only):** every reference reel ends "Comment '<word>' to get the doc/video" with an asset preview (v01 @ 1:12, v02 @ 1:40, v03 @ 1:01).
- **modules:** chrome (the three bands never move), continuity (the recurring diagram), data_figures (counters and stated numbers; illustrative curves labelled). Canvas camera is OFF because the diagram camera lives inside the card band (§21, ER-2).

### 0.4 Formats `[DNA set; VAR enable]`
| ID | Name | When | Profile overrides | Layouts | Hook default | Shared DNA |
|---|---|---|---|---|---|---|
| F-A | Whiteboard split | Every reel: a numbered framework (FW-1), an old-vs-new model (FW-2) or a tool workflow (FW-3) | none | L-split, L-full, L-clip | HA-06 | the whole style |

The three structure variants (§7.1) are not formats: they share every visual system and differ only in the shape of the recurring diagram.

### 0.5 Theme packs
OFF (`themes.policy: single`): the role palette is fixed per reel; the paper/stage flip is a world change (§3.1), not a theme.

---

## §1 Procedure (follow in order) `[REQ] [DNA]`

This style's craft is **framework extraction → mode schedule**: turning a talk into named parts the diagram can show, then deciding, word by word, when the viewer sees the card and when they see the face.

1. **P1 Inventory.** ffprobe the take: resolution, orientation, fps, duration, audio. Classify it as setup A (landscape ≥ 3840 px wide), FB-2 (landscape 1920) or FB-1 (vertical) (§12.4) and note which fallback applies. Conform to 30 fps CFR. Register every supplied file with its origin (`veos asset add --origin creator`).
2. **P2 Prepare.** No matte needed (ER-1 pop-out is not available yet). Run face boxes (`veos matte` writes them) so the window and full-face crops frame the face.
3. **P3 Transcribe** with word timestamps; apply `language.captions.transform` (§5.5) and the glossary. Check every tool, brand and proper name in the caption text.
4. **P4 Segment** into `HOOK`, then the units of the structure variant (§7.1): `STEP-n` (FW-1), `OLD` / `TURN` / `NEW` (FW-2) or `STATION-n` (FW-3), then `RECAP`, `CTA`. Mark jump-cut points on word boundaries (dead air, §2.3 H5).
5. **P4b Framework extraction (the craft, part 1).** Write the reel's framework in one line: its name (becomes a lockup), its N parts (each a 1–3-word name), and the **motif shape** that carries it (loop, ring, ladder, road, axes or chain; §23.2). If the talk has no named parts, name them yourself from the speaker's own words and show them at the checkpoint.
6. **P5 Classify** every sentence with a line type LT-… (§8.4) and mark its trigger word.
7. **P6 Tone-tag** every sentence: `explain` · `hype` (a claim, an opinion) · `warn` (a mistake, the old way) · `awe` (a reveal) · `win` (the payoff) · `cta`.
8. **P7 Hook plan.** Pick the archetype (§6.2–6.3; default HA-06), write **3 lockups** (§6.5) and 3 hook variants, and run the stopper tests ST-1…ST-6 with this style's numbers.
9. **P8 Visual plan.** A pattern per line (§8.4); the recurring diagram's states (§23); the figure plan for every number (§18); the third-party moments (§12.5).
10. **P8b Mode schedule (the craft, part 2).** Walk the transcript and mark every **punch** (to L-full) and **return** (to L-split) on a word, with the rules of §3.2: punch on the claim word, return on the first word the card illustrates, full runs 0.8–4 s, split runs 1.5–12 s, 6–9 punches per 60 s. Every return lands with a card event on the same frame.
11. **P8c World plan.** Choose W-stage or W-paper per section (§3.1); at most 3 flips per reel, only on a split return at a section start.
12. **P9 Beat sheet** (§13): one beat per trigger word; check the cadence numbers (§7.6) and the layout shares (§3.2).
13. **P10 SFX ledger** (§11) and the transition map (§9.3).
14. **P11 Assets.** Build the cards; collect the creator's files; resolve fallbacks FB-1…FB-4 and say which were used.
15. **P12 Checkpoint** (§13.5), then **wait for approval.**
16. **P13 Build.** Act by act (hook, each unit, recap, CTA). `veos figures` → `veos scenes-meta` → `veos measure` → `veos validate`; preview and QA (§15, at most 3 passes); render.

**Module steps** (already placed above): data check for every figure (P8, §18); chain design for the recurring diagram (P4b + P8, §23). Branch insertions: `talking_head` only (P4 marks jump-cut points).

---

## §2 Hard rules `[REQ] [DNA]`

### 2.1 Editing rules (every style)
The nine editing rules in `playbooks/_global/GLOBAL-RULES.md` apply. They are directions, not limits: smooth, seamless motion; nothing overlaps by accident; keep the face clear (behind the speaker is fair game, text included); readable at a glance; one idea at a time; show what's being said; never fake facts; pace like the style, not like a timer; the style decides the look.
- **Facts the engine checks:** accidental overlaps, jumps, the face covered, unreadable text, numbers and quotes that don't match what was said, the promised count. Every count, timing and budget this playbook gives is direction for the edit, not a limit.
- **Retired (8 Oct 2026), whatever this playbook says below:** no REPRESENTATIONAL or example labels on made-up cards, no credit lines, no flash limit (flash as often as this style calls for; any "NC-11" cap below no longer applies), and text may sit behind the speaker without an exception.

### 2.2 Declared exceptions
| ID | Style limits (≤ registry) | DNA reason | Evidence |
|---|---|---|---|
| **E3** Quiet type | **Labels only:** diagram callout tags, axis titles and tiny node tags may be 28–39 px when `data-redundant` (the same word is spoken or shown larger), weight ≥ 600, contrast ≥ 7:1 (≥ 4.5:1 on their own white tag). **Subtitles are not quiet:** CS-1/CS-2 stay ≥ 54 px (`subtitle_min_px: 54`) | Diagrams carry many small labels that annotate a node the caption is saying; enlarging them to 40 px crowds the curve | v01 @ 0:07–0:10 ("Initial Conflict", "Rising Action", "Climax" tags ≈ 22 px measured, raised to 28); v01 @ 0:21 axis titles "Plot Development / Over Time" |
| **E6** Hard swap | Counter digits stepping inside a fixed chip (P-COUNTER-TICK) and the step numeral changing inside the motif's numeral slot; container rect constant ±4 px; the chip's first entry and last exit stay eased | The follower count ticks every 0.17 s; easing each digit would blur it | v03 @ 0:01.7–0:02.9 (2K → 19K) |

No other exception. E1 (behind-head text), E2 (chaos), E4 (ambient fields) and E5 (edge bleed) are never used.

### 2.3 MUST rules H1…
| ID | Rule | Check |
|---|---|---|
| **H1** | **Frame 0** shows the lockup readable (every word opacity 1, blur ≤ 4 px), a card skeleton already moving in the card band (scale-in or a line drawing), the live face window, and the first caption word if speech starts within 3 f. | V-F0 |
| **H2** | **Cadence:** weighted state changes per 10 s of body 11–24 (captions weigh 0.34 each); ≥ 9 in 0–3 s; no full-weight change gap > 4.0 s (body) or 1.5 s (hook); nothing static > 2.0 s. In L-split, the card changes (event, node, title swap, new card) at least every 2.5 s. | V-CADENCE (+ review for the 2.5 s card rule) |
| **H3** | **Mode schedule:** L-full runs 0.8–4.5 s, L-split runs 1.5–18.0 s, L-clip runs 1.5–4.0 s; every switch lands within ±0.25 s of a claim / "but" / number / sentence-start / post-pause word; shares L-split 60–80%, L-full 15–35%, L-clip ≤ 8%; 3–8 punches per 60 s (default 6–7); two L-full runs are separated by ≥ 1.5 s of L-split. | V-LAYOUT (+ review for the punch count and the 1.5 s separation) |
| **H4** | **Captions:** CS-1 in L-split, CS-2 in L-full and L-clip; one word per chunk (two only when the engine glues a name or number, or two very short words); shown ≤ 1 f before the word; never on a card, never over the face; italic-serif keyword swaps ≤ 1 per 5 s. | V-CAPTION, V-TYPE |
| **H5** | **Dead air:** ≤ 1 gap ≥ 150 ms per 15 s; jump cuts on word boundaries ±1 f; a deliberate ≤ 0.4 s beat before a punch line is allowed once per 20 s. | review (cut map) |
| **H6** | **Lockup:** ≤ 8 words, ≤ 2 lines, Title Case (Latin), exactly one crimson device (coloured key phrase on paper, underline, or slab) and at most one italic-serif span, 0 emoji, readable in ≤ 2.0 s; one lockup on screen at a time. | V-TITLE |
| **H7** | **On the word:** every card event, node, label, numeral and tool lands 2 f before its word and is fully on within ±5 f. | V-ONWORD |
| **H8** | **Face:** nothing is drawn over the face window or the full-face face box; the window is never covered by a card; captions sit ≥ 40 px clear of the face box (CS-2 at cy 1160 sits on the chest). | V-FACE |
| **H9** | **Presence:** a face is visible ≥ 90% of runtime (window face box ≥ 134 px = 7% of the frame height); the longest absence (L-clip) ≤ 4 s. | V-PRESENCE |
| **H10** | **Promise integrity:** a promised count ("4 steps") equals the steps shown (numerals 1…N, motif nodes N); the CTA keyword is on screen ≥ 2.0 s in the CTA lockup; the asset previewed is the asset promised. | V-PROMISE |
| **H11** | **Truth:** concept curves have no axis numbers; every number shown is in `plan/figures.json` (spoken, scripted or the creator's own data); an illustrative chart that shows any number carries the TC-legal `example` tag. | V-DATA, V-NUMFMT |
| **H12** | **Recurring diagram:** one motif per reel, built in the first 25% of runtime, visited at every unit with the active part lit and the rest at 35%, recapped before the CTA; ≥ 3 appearances. | V-CONTINUITY (pending: review) |
| **H13** | **Spelling:** tool, brand and person names exact in captions and cards (glossary). | V-CAPTION |
| **H14** | **Camera:** the L-full entry is a **static crop** (no land, no settle: scale 1.00 over the first 6 frames, v01 @ 0:01.76, v02 @ 0:30.36). The only footage moves: `punch-in` (a 1.12–1.2× framing step on a jump cut inside an L-full run ≥ 2 s, about every second such run, ≤ 6 per reel) and an occasional `push-drift` (1.00 → 1.05 over a whole run, never two runs in a row). Never a move in L-split or L-clip. | V-CAMERA |
| **H15** | **Audio:** −14 LUFS integrated, true peak ≤ −1.5 dBTP, bed ≥ 18 dB under the voice, hard end ≤ 6 f after the last word. | NC-8 (mix gate) |
| **H16** | **Determinism:** every frame is a pure function of its index; any scatter uses `ctx.rng(seed)`. | NC-9 |

### 2.4 NEVER list
- **N1** Captions in any other place: on a card, inside the window, at the top, or more than one word-pair at a time.
- **N2** A card in L-full. The full-face run carries only the face and the caption (no lockup, no chip, no sticker).
- **N3** Crimson **text** on the stage world (2.8:1 on #050505). On W-stage crimson is only an underline or a slab with white text.
- **N4** Two cards side by side, a card next to a lockup from a different idea, or a third text block (lockup + one label group + caption is the maximum).
- **N5** Stock footage, stock icons packs with brand colours, emoji, stickers, meme cues, light leaks, film burns, glitches, whip pans **of the footage** (the in-band card smear P-SMEAR-PUSH is not a whip pan), spinning 3D logos.
- **N6** Fake dashboards, fake view counts or follower numbers presented as real (NC-6).
- **N7** A full-face run that starts mid-word, or a return to an unchanged card.
- **N8** Bright hues beyond 3 per frame; more than one neon colour on one diagram state (white + one accent).
- **N9** Gradients on cards, drop shadows on text in the card band, rounded "bubble" captions, caption boxes.
- **N10** Regrading the footage; slow-motion; speed ramps.
- **N11** A black tail > 0.2 s or an end card after the CTA asset.

Buyers may add **BN1…** `[VAR]`.

---

## §3 Worlds, layouts, stage moves, safe zones `[REQ] [DNA; coordinates TUNE ±5%]`

### 3.1 Worlds
| ID | Kind | Look (tokens) | Carries | Entered / exited |
|---|---|---|---|---|
| **W-stage** | stage | `night` #050505; faint white dot grid (pitch 36, alpha 0.05, r 1.2); a 900 px soft white glow at (540, 700), alpha 0.035; no noise, no vignette | Concepts, psychology, models, curves, loops, roads, numbered frameworks; the recurring motif's neon | Default world. Flip in/out only on a split return at a section start (G-5) |
| **W-paper** | canvas | `canvas` #E4E4E0 (measured #E1E2DD–#E4E4E4, a cooler, darker grey than first analysed); grid lines `grid` #DADAD6 (faint: ≈ 6 levels under the paper), pitch 40, 1.5 px, alpha 0.9, visible mostly in the centre and fading out toward the frame edges (radial; v01 @ 1:03.6): world `grid.fade {x: 540, y: 770, inner: 0.1, outer: 0.3, min: 0}` (built-in) | Tools, apps, documents, profiles, workflows, anything that is a screen or a page; the CTA asset | Same |

**World choice rule (P8c).** A section about *a thing on a screen* (an app, a site, a document, a profile, a prompt) is W-paper. A section about *an idea* (a model, a curve, a habit, a mechanism) is W-stage. The hook takes the world of its first card. Flips: ≤ 3 per reel, ≥ 5 s apart, never inside a unit. The CTA asset card takes W-paper when the deliverable is a document or tool, W-stage when it is a video.

Text colour flips with the world: ink #0B0B0B on paper, paper #FFFFFF on stage (lockups, labels and the CS-1 caption).

### 3.2 Layout library
| ID | Engine | Presenter rect | Graphic band | Caption | Share (F-A) |
|---|---|---|---|---|---|
| **L-split** | `card` | x 64, y 1400, w 952, h 560 (bleeds 40 px off the bottom, so only the top corners show), radius 30, crop 16:9, face 0.33 (measured face box ≈ 225 px, centre y 1450–1520), eye 0.16 (the face centre sits high, so the head rises over the top edge into the 120 px breakout), shadow 0.25, no border | x 64–1016, y 150–1160 (headline slot y 150–360, card slot y 380–1160) | CS-1, cy 1245 | 0.60–0.80 |
| **L-full** | `card` | x 0, y 0, w 1080, h 1920, radius 0, crop 9:16, face 0.26, eye 0.36 | none (N2) | CS-2, cy 1160 | 0.15–0.35 |
| **L-clip** | `hidden` | none: a full-bleed clip scene (z4) fills the frame | the whole frame | CS-2, cy 1160 | 0–0.08 |

**Layout schedule rule (the mode schedule, DNA).**
- **Punch** (L-split → L-full) on the first strong word of a claim: *is, because, but, instead, never, don't, the reason, actually, now, then*, or a number. In the hook, the first punch lands at 1.5–3.0 s.
- **Return** (L-full → L-split) on the first word the card illustrates (a noun, a step name, "here's", "look"). The card shows a new state on that same frame (new card, title swap, next node): never return to an unchanged card (N7).
- **Run lengths (measured):** L-full 1.5–3.5 s typical (median 2.2), 0.8 s minimum ("But.", v01 @ 0:11.4; v03 @ 0:03), 4.5 s maximum (v02 @ 0:30.4–0:34.7). L-split 4–8 s typical (median 5.5), 1.5 s minimum (the hook's first run), 18 s maximum (v02 holds 12–18 s: 0:00–0:16.4, 0:34.7–0:52.5; allowed only while the card changes every ≤ 2.5 s). L-clip 1.5–4.0 s.
- **Rate:** 3–8 punches per 60 s (v01 7.3, v03 7.7, v02 3.3); default 6–7, toward 3–4 when the reel lives on a long motif build (HA-06b). Two L-full runs are separated by ≥ 1.5 s of L-split (a clip may sit between L-full runs).
- **Ends:** the reel opens on L-split (f0) and ends on L-split (the CTA asset).
- Tokens: `layouts.schedule = {switch_on: [claim, but, number, sentence, pause], max_s: {L-split: 12, L-full: 4, L-clip: 4}, min_s: {L-split: 1.5, L-full: 0.8, L-clip: 1.5}}`.

### 3.3 Stage moves
| ID | Move | Recipe (30 fps) | Use |
|---|---|---|---|
| **G-1** | **Punch cut** | `stage {layout: L-full, via: cut}` (0 f). No camera move on the cut (static crop, face 0.26). In a run ≥ 2 s, a jump cut on a mid-run word may step to the tight framing (`punch-in` 1.15×, 1 f), about every second run; or the run carries a slow `push-drift` (1.00 → 1.05) (H14). Captions switch CS-1 → CS-2 on the cut frame | Every claim |
| **G-2** | **Return cut** | `stage {layout: L-split, via: cut}` (0 f); a card event on the same frame (title swap starts, next node pops, new card scales in) | Back to the explanation |
| **G-3** | **Clip in** | `stage {layout: L-clip, via: cut}` + the full-bleed clip scene z4 `t_in` on the same frame; the clip starts already playing (no fade) | The example moment (P-CLIP-INTERCUT) |
| **G-4** | **Clip out** | `via: cut` to L-full (preferred: the reaction) or to L-split with a new card | After the example |
| **G-5** | **World flip** | On a G-2 return frame, `world {world: W-paper or W-stage}` with `fade: 0`; the card band is new anyway | Section start whose subject changes kind (§3.1) |

There are no animated window moves (no shrink, no slide): the mode change is always a hard cut. `stage_morphs: {cut: 0}`.

### 3.4 Layout diagrams
```
L-split (y px on 1080x1920)                L-full                             L-clip
┌──────────────────────────────┐ 0         ┌──────────────────────────┐ 0      ┌──────────────────────────┐
│ IG UI (keep clear)           │ ← 0–110   │                          │        │  creator clip, full      │
│  This Is Why Your            │ ← S-HEAD  │      head top ≈ 300      │        │  bleed (or a created     │
│  Plan *Never* Works          │   150–360 │                          │        │  substitute scene)       │
│  ───────────── (crimson)     │           │   eyes ≈ 690 (eye 0.36)  │        │                          │
│ ╭──────────────────────────╮ │ ← S-CARD  │   face box ≈ 440–940     │        │                          │
│ │  diagram / UI / doc /    │ │   380     │                          │        │                          │
│ │  motif (one idea)        │ │   …1160   │                          │        │                          │
│ ╰──────────────────────────╯ │           │        "because"         │ ← CS-2 │         "almost"         │ ← CS-2
│           word               │ ← CS-1    │        cy 1160, 66 px    │  1160  │         cy 1160          │  1160
│                              │   cy 1245 │                          │        │                          │
│ ╭──────────────────────────╮ │ ← window  │  (chest / hands)         │        │                          │
│ │   face window (16:9 look)│ │   1400    │                          │        │                          │
│ │   x 64–1016, r 30        │ │           │                          │        │                          │
└─┴──────────────────────────┴─┘ 1920      └──────────────────────────┘ 1920   └──────────────────────────┘
```

### 3.5 Safe zones and bands
- Meaning text stays inside x 64–1016, y 110–1500 (NC-5); nothing in the right 110 px between y 900 and 1540 except the face window (no text there).
- **S-HEAD** y 150–360 (lockup top at y 160); **S-CARD** y 380–1160; **caption band** y 1205–1285 (CS-1 cy 1245); **window** from y 1400. Card content keeps ≥ 45 px above the caption rect (card bottom ≤ 1160).
- In L-full the caption band is cy 1160 (CS-2); nothing else is placed.
- A pushed diagram (P-DIAGRAM-PUSH) is clipped to the band x 0–1080, y 110–1170; its remaining text stays inside x 64–1016.

### 3.6 Presenter rules
- **Share** 90–100%; longest absence 4.0 s (L-clip only).
- **Window crop (L-split):** face box ≈ 168 px tall (face 0.30 of 560), face centre at window top + 90 px (eye 0.16): the head top rises ≈ 50 px above the window's top edge and the breakout (`breakout: 120`, the matted cut-out) draws it over the edge, as in every reference split.
- **Full crop (L-full):** face box ≈ 500 px tall (face 0.26), eyes at y ≈ 690; the chin sits ≈ 940, the caption at 1160 lands on the chest.
- **Returns** are cuts (G-1/G-2/G-4); the presenter never slides or shrinks.
- Nothing ever sits behind the head (no E1).

---

## §4 Colour `[REQ] [meanings DNA; brandable hex VAR]`

### 4.1 Role palette
| Role | Hex | One job | Text on it | Contrast | Brandable |
|---|---|---|---|---|---|
| `primary` crimson | {{BV-02.primary|#B0122A}} | The key phrase: coloured lockup words (paper only), the 4 px underline, the key slab, the CTA deliverable line, count chips on paper | `paper` | 7.1:1 (white on it); 5.5:1 as text on #E4E4E0 | ✔ (BV-02 first colour) |
| `accent` neon signal | {{BV-02.accent|#FF2D55}} | The recurring motif and the lit node/segment on W-stage; its glow | `ink` | 5.4:1 vs #050505 | ✔ (BV-02 second colour) |
| `data` magenta | #D61FD0 | The reading: the viewer's / measured curve, the overlay series, the area fill | `ink` | 4.7:1 vs #050505 | ✔ (third) |
| `highlight` yellow | #FFE000 | The threshold: segment bars under an axis, the highlighted page/row/line | `ink` | 15:1 | TUNE |
| `bad` red | #E0102A | The old way, the failing curve, the drop | `paper` | 4.9:1 | fixed |
| `good` green | #2BD96B | The new way, the working result, the success outline | `ink` | 11:1 | fixed |
| `mute` grey | #8A8A8A | Inactive nodes, the ghost serif line, axis titles, grey bevel chips | `ink` | — | TUNE |
| `ink` | #0B0B0B | Text and strokes on paper; CS-1 on paper | — | — | TUNE |
| `paper` | #FFFFFF | Text and lines on stage; node dots; CS-1 on stage; CS-2 | — | — | DNA |
| `canvas` / `grid` | #E4E4E0 / #DADAD6 | W-paper | — | — | TUNE |
| `night` | #050505 | W-stage | — | — | TUNE |

### 4.2 Meanings
- **Crimson = the words that matter** (the key phrase of the lockup, the deliverable). Never a diagram colour.
- **Neon accent = the part of the diagram we are on.** Exactly one lit thing at a time.
- **Magenta = the reading** (what the data actually does, the viewer's own curve), against a white or red model curve.
- **Red → green = old → new.** The before/after axis of every comparison.
- **Yellow = the threshold** (the window that decides: the first 3 seconds, the line that matters).
- Brand colours (a tool's own colours) appear only on that brand's created logo plate, never elsewhere.

### 4.3 Theme packs
OFF (`policy: single`).

### 4.4 Grades
OFF: footage is not graded; only exposure and white balance are matched if the take has two segments.

### 4.5 Rules
- `max_bright_per_frame` 3 (bright roles: primary, accent, data, highlight, bad, good). Typical frame: crimson underline + one accent + one of data/bad/good.
- Crimson text only on W-paper (N3). On W-stage the key phrase is paper-white with a crimson underline or a crimson slab.
- Coloured diagram lines on paper are darkened to ≥ 3:1 against #E4E4E0 (accent → #D81B45, data → #B514AE, good → #12A150); text labels stay ink.
- Glow (canvas `shadowBlur` 20–28 px) only on W-stage, only on the lit element and the neon lines.

**Must match `tokens.json`.**

---

## §5 Type & caption system `[REQ]`

### 5.1 Font map `[slots DNA; families TUNE within class]`
| Slot | Family | Weight | Font class (buyer TUNE range) | Used for |
|---|---|---|---|---|
| `display` | Inter Tight | 800 (labels 700) | neo-grotesk sans 700–900: Inter Tight, Plus Jakarta Sans, Space Grotesk, Poppins | Lockup sans lines, step names, labels, chips |
| `body` | Inter Tight | 700 | same class, 600–800 | One-word captions |
| `serif` | Instrument Serif | 400 italic | condensed high-contrast italic serif: Instrument Serif, EB Garamond Italic, Source Serif 4 Italic | The italic span in lockups, the caption keyword swap, annotation tags ("HOOK") |
| `numeric` | Inter Tight | 900 numerals, 800 counters (tabular) | same as display | Hero numerals, counters, stat chips |
| `ui` | Inter Tight | 500–600 | same | Text inside recreated UI |
| `mono` | JetBrains Mono | 500 | monospace | Commands, URLs, prompts typed into a chat mock |
| `dev` | Noto Sans Devanagari | 600–800 | Devanagari sans | `hi` captions and lockups |

Brand wordmarks are never fonts: a product name is set in `display` inside a neutral logo plate.

### 5.2 Headline element: the **lockup** `[DNA recipe; NICHE text]`
Kind `lockup`, lifetime `section` (it lives as long as its card's idea), slot S-HEAD (x 64–1016, top y 160, centred).

| Recipe | Lines | Look | Use | Evidence |
|---|---|---|---|---|
| **LK-1 Two-line title** | L1 sans 800 52–60 px; L2 sans 800 60–72 px | Key phrase (1–3 words, usually L2's end) in crimson on W-paper; on W-stage paper-white with a 4 px crimson underline under the key phrase | The hook, section titles on paper | v01 @ 0:00 "This Is The Reason / Why Your **Video Fails**"; v03 @ 0:19 "Paste URL And Get / **Every Secret** In That Video" |
| **LK-2 Serif lead** | L1 sans 800 44–48 px; L2 serif italic 76–88 px | L2 underlined 3–4 px crimson across its width | Hooks and big promises on stage | v02 @ 0:01 "How to make your / *Storytelling addictive*" |
| **LK-3 Key slab** | L1 sans 800 52–60; L2 sans 800 56–64 on a crimson slab (radius 6, padding 2/16, white text) | The slab sweeps in L → R 6 f behind L2 | The turn: "this no longer works", "stop doing this" | v01 @ 0:14 "This Traditional Story Arc / **No Longer Works**" |
| **LK-4 Concept title** | One line, 60–68 px: sans word(s) + serif-italic word(s) at 1.18× | Optional 3 px crimson underline; on stage white, on paper ink | Titles of a diagram card or a step | v01 @ 0:04 "Traditional *Story Arc*"; v02 @ 1:05 "Art of *Contrast*" |
| **LK-5 CTA lockup** | L1 sans 800 56–64 + serif-italic keyword in curly quotes; L2 sans 800 52–60 crimson (paper) or white + underline (stage) | — | The CTA only | v01 @ 1:12 "Comment *"Story"* / To Get The Doc"; v03 @ 1:01 |

Rules (H6): ≤ 8 words; ≤ 2 lines; Title Case (every word capitalised except a/an/the/of/to/in/on/for/and/or inside a line); exactly one crimson device; at most one serif span (1–2 words, never the crimson words too); no emoji, no punctuation except the CTA quotes and a question mark.

| Property | Value |
|---|---|
| Size | L1 44–60 px, L2 56–88 px (serif 1.18× of the sans size it sits with), line height 1.04, tracking −1% |
| Colour | ink on W-paper, paper on W-stage; mute #8A8A8A only for a "ghost" serif second line that is about to be named (v02 @ 0:05 "The Dopamine / *Addiction*" grey) |
| f0 behaviour | **Not on f0** (v01, v02, v03 @ 0.0 s: no lockup). The hook lockup fades in (blur 4 → 0 px, 8 f) and is readable by 0.4–1.0 s (v01 @ 0.5 s, v02 @ 1.0 s), while the whole band (lockup + card) zooms in about 0.65 → 1.00 over 0–1.5 s, ease-out (v01: the phone card grows 313 → 504 px wide between 0 and 1.5 s); the underline draws L → R over 8 f once its line is in. Later section lockups: readable on their first frame |
| Body entrance | **Blur build:** LK-1/LK-3/LK-4 build **line by line** (each line 6 f, opacity 0 → 1 from light grey, blur 8 → 0 px; line 2 starts 5 f after line 1; v01 @ 0:00.13–0:00.33, 1:03.7–1:04.0); LK-2 builds **word by word**, 4 f per word with blur (v02 @ 0:00.04–0:00.5); the underline draws 8 f after the last word lands; LK-3 slab sweeps 6 f after L1 |
| Life | Static once built (the card below carries the motion); a 1.04 bump (4 f) on the crimson words when they are spoken |
| Swap (P-TITLE-SWAP) | Old lockup blur-out 4 f (blur 0 → 10, opacity → 0), new lockup blur-in 6 f starting on the same frame; one lockup at a time |
| Exit | Blur-out 5 f, or carried off the band by P-DIAGRAM-PUSH (it fades in the push's first 4 f) |
| Lifetime | Section (one card idea), 2–12 s; it disappears with the cut to L-full and returns with the split if the idea continues |

### 5.3 Caption system profiles `[DNA mechanics; fonts TUNE; language VAR]`
Two profiles, chosen by layout (`captions.by_layout: {L-full: CS-2, L-clip: CS-2}`; default CS-1). Both extend `lib:kallaway`.

| Group | CS-1 "split word" | CS-2 "face word" |
|---|---|---|
| Mode | full · primary · mute_safe | same |
| Chunking | unit `word`, words [1, 2] (two only for glued names/numbers or two very short words), max 18 chars, 1 line; never split a name, number or unit; punctuation kept and breaks the chunk; hard pause 0.9 s | same, max 16 chars |
| Timing | lead 1 f; min hold 0.25 s per word; tail 0.12 s; swap **hard** (0 f: the next word replaces the last on its frame, no pop, no fade; every burst v01–v03); chunks are often 2 short words ("The reason", "of a", "we were", "story arc."); no pause hold (the caption clears in a pause ≥ 0.9 s) | same |
| Skin | Inter Tight 700, **56 px**, TC-subtitle, case **as spoken** (keeps "But", "Claude", "YouTube"), tracking −1%, no stroke, shadow `0 2 6 rgba(0,0,0,.35)`, no container | Inter Tight 700, **66 px**, shadow `0 2 10 rgba(0,0,0,.6)`, no container |
| Position | `fixed_y` cy **1245**, centred, max width 952; colour by background: **ink #0B0B0B on W-paper, paper #FFFFFF on W-stage** | `fixed_y` cy **1160**, centred; always paper #FFFFFF |
| Emphasis | `font_swap`: the word becomes Instrument Serif italic 400 at 1.12×, same colour; selection topic noun / name / glossary term, score ≥ 1.45, ≤ 1 per chunk, ≤ 1 per 5 s; never stop-words | same |
| Variants | karaoke, tiers, duet, stack: none | none |
| Hide rules | hidden only during stage morphs (there are none: all mode changes are cuts); never hidden for lockups, numerals or the hook | same |
| Language | Latn, keep English terms, spelling not normalised (as spoken), profanity masked `inner` (S**T), on by default; glossary from the creator's tools and names | same |

Evidence: one word per 0.3–0.6 s throughout (v01 @ 0:04–0:11 "what / school, / story arc. / Initial conflict, / rising action, / climax,"); split captions at y ≈ 1240–1287 measured, full-face at y ≈ 1158–1255; black on paper (v01 @ 0:00, v03), white on stage; italic serif swap "story" (v01 @ 0:03) and "dopamine" (v01 @ 0:43). Measured sizes ≈ 52 px (split) and ≈ 62–66 px (face), raised to 56 / 66 to stay above the 54 px floor.

### 5.4 Other text systems
| System | Class | Recipe | Hold |
|---|---|---|---|
| **Hero numeral + step name (SM-NUM)** | TC-display | Numeral Inter Tight 900, 200 px (160–240), paper on stage / ink on paper; step name 2 lines Inter Tight 800, 72 px, line height 0.98, left-aligned, 24 px right of the numeral, baseline-aligned to its bottom. Placed beside the lit motif node (inside S-CARD) | 1.2–2.0 s, then exits with the motif pan |
| **Node label** | TC-label 40 px (28–39 with E3 + redundant) | Inter Tight 700 next to its node, paper on stage / ink on paper; pops 5 f (scale 0.8 → 1) on its word | Until the card changes |
| **Callout tag** | TC-label 28–40 px | White tag (radius 4, padding 4/10) with ink text, a 2 px tail toward its node | Same |
| **Grey bevel chip** | TC-label 40 px | Fill #3A3A3C, paper text, radius 6, padding 8/18, top inner highlight; stacked 12 px apart | Until the card changes |
| **Annotation tag** | TC-label 52–64 px | Instrument Serif italic paper/ink + a hand-drawn 4 px curl arrow (SVG path, draw 8 f) pointing at the threshold | 1.0–3.0 s |
| **Hand label** | TC-label 56–68 px | Inter Tight 800 + a hand-drawn squiggle arrow (4 px) to its card | Same |
| **Counter / stat chip** | TC-label 40–56 px | Inter Tight 800 tabular in a chip: crimson fill + white text on paper, white fill + ink text on stage; digits step (E6) | While the reading is discussed |
| **Mono line** | TC-label 40–44 px | JetBrains Mono 500 inside a chat input, typed 1 char/f | Until sent |
| **Example / representational tag** | TC-legal 24 px | Inter Tight 500, 70% opacity, bottom-left of its card | Whole card life |

### 5.5 Language and number rules
- **Spelling:** captions as spoken; English words and brand names exact (glossary).
- **Hinglish speech:** captions romanised Hinglish (`hinglish/Latn`, verbatim) one word at a time; or English captions (`en/Latn`, `transform: translate` from the script; the chunker still shows one word at a time). Lockups stay English Title Case unless the buyer writes them in Hinglish (then Title Case romanised).
- **Hindi (Devanagari):** captions `dev` slot 700; Title Case does not apply; the italic serif does not exist in Devanagari, so: lockup serif span → the same words in `primary` crimson on paper / underlined on stage; caption emphasis → `bold` (800 vs 700). The copy sets `emphasis.mechanism: bold` on CS-1/CS-2 (a language adaptation, VAR).
- **Numbers:** `international` + `$` + K/M ("10K", "$4.2M") by default; Indian buyers get `indian` + `₹` + lakh/crore (BV-06 follows BV-05). Every number through `ctx.fmtNum` (§18).
- **Units:** metric.

---

## §6 Hook system `[REQ]`

### 6.1 Stopper tests (this style's numbers)
| Test | Number |
|---|---|
| ST-1 Thumbnail | f0 at 25% scale: the card skeleton and the face window are recognisable; the lockup (L2 ≥ 60 px, ≥ 15 px at 25 %) is readable from 0.5 s, so the cover frame is picked from 1.5 s |
| ST-2 Mute | 0–3 s tell the topic: lockup + card reading + one-word captions |
| ST-3 Motion at f0 | the card skeleton is scaling in or a line is drawing on f0; the window is live |
| ST-4 Read time | lockup reads in ≤ 2.0 s (≤ 8 words × 0.25 s) |
| ST-5 Change count | ≥ 9 weighted state changes in 0–3 s (captions 0.34 each) |
| ST-6 Payoff-by | the diagram or proof is readable by 2.5 s |

### 6.2 Default archetype: **HA-06 Framework build** `[DNA]`
| t (s) | Beat | Layout / world | Visual | Caption | Camera | Cue |
|---|---|---|---|---|---|---|
| **f0** | Stopper | L-split, world of the first card | No lockup yet; the card skeleton (blank phone, doc, axes or motif outline) is up and the whole band starts a slow zoom-in (≈ 0.65 → 1.0 over 1.5 s, P-CARD-SCALE-IN stretched); window live. **0.2–0.5 s:** LK-1 or LK-2 fades in (blur 4 → 0, 8 f), crimson underline draws 8 f; readable by ≤ 1.0 s | first word (CS-1) | — | hook cue on f0 |
| 0.17–0.8 | Proof fills | same | The skeleton populates on the nouns: UI rows (P-UI-POPULATE, 2 f stagger), the axes draw (P-AXES-BUILD), or the motif outline draws (P-MOTIF-BUILD) | one word per word | — | — |
| 0.8–1.8 | The reading | same | One decisive event: the curve drops (P-CURVE-DRAW in `data`), a counter steps (P-COUNTER-TICK), the first node lights | words | — | reveal cue on the event |
| 1.5–3.0 (the claim word) | **Punch** | **L-full** (G-1) | Face only | CS-2 at 1160 | — (static crop) | — |
| punch → +1.5–3.0 | The claim | L-full | Nothing else (N2) | one word per word | — | — |
| claim end (sentence start) | **Return** | L-split (G-2), same or flipped world | Title swap to LK-4 (the model's name) + the diagram skeleton scales in | CS-1 | — | — |
| return → ≈ 11 s | Build | L-split | The diagram builds one node / label per spoken term every 0.8–1.5 s; the second punch lands on the next claim | — | `push-drift` on the second punch | — |

Payoff: the f0 card is itself the diagram or the proof, readable by 2.5 s (V-F0 payoff `diagram`). The hook (title + first card + first punch + build) ends by 15% of runtime (≤ 11 s on a 75 s reel). **Variant HA-06b "word build"** (v02): the LK-2 lockup builds word by word at 5 f per word from f0 (first word readable at f0) while a mini player (P-MINI-PLAYER) cycles 3–4 creator clips with a hard swap every 5 f (measured 4 f at 24 fps, v02 @ 0:00–0:00.67) in the card slot, and the first punch may wait until the build ends (v02 holds the split 16 s); the object pulse (P-OBJECT-PULSE) lands at 1.0 s.

### 6.3 Allowed alternates `[DNA list; VAR per reel]`
**HA-02 Headline + proof** (v03): use when the reel is about a tool or a result the creator can show.
| t | Visual | Caption | Note |
|---|---|---|---|
| f0 | LK-1 lockup + a created logo plate or the creator's screenshot card moving (pulse or scale-in) | first word | proof element = kind `proof` |
| 1.0–1.7 | The proof card swaps to the result card (profile, dashboard, page) sliding up 10 f | words | — |
| 1.7–2.5 | The result reads: counter steps (E6) / tiles fill | words | proof by 2.5 s |
| 2.5–3.5 | Punch to L-full on the claim | CS-2 | — (static crop) |
- Example (fitness `[NICHE: example]`): "This App Just Fixed My *Meal* Prep" — plate "MealPlanner" (created logo plate) → a created week-plan card filling day by day.
- Example (marketing `[NICHE: example]`): "One Prompt Rewrote My Whole **Ad Account**" — a chat mock with the prompt → a created results card whose numbers come from the creator.

**HA-07 Live number** (v03 counter): use when the reel opens on the creator's own metric.
| t | Visual | Caption |
|---|---|---|
| f0 | LK-1 lockup + counter card already stepping (P-COUNTER-TICK) from a stated start value | first word |
| ≤ 1.0 | First stated value lands (figures.json `at` on its spoken number) | words |
| 1.0–2.5 | Counter climbs to the stated end value, tile grid fills behind it | words |
| 2.5–3.5 | Punch on the claim | CS-2 |
- Example (fitness): "**0 → 40** Clients In 90 Days" with the creator's client count. Example (marketing): "How I Got **10K** Followers With 3 Posts" with the creator's follower count.

**HA-05 Claim lockup**: use when the opening line is a pure opinion with nothing to show yet.
| t | Visual | Caption |
|---|---|---|
| f0 | LK-3 lockup (key slab) alone in S-HEAD over an empty band; window live | first word |
| ≤ 0.7 | The slab sweeps; the first card arrives under it (P-CARD-SCALE-IN) | words |
| 1.2–2.5 | Punch | CS-2 |
- Example (fitness): "Cardio **Is Not** The Problem". Example (marketing): "Your Funnel **Is Not** Broken".

### 6.4 Hook pairs by topic `[NICHE]`
Pair type for HA-06: **promise → framework** (topic · lockup · the f0 card · the first punched claim).

| Niche | Topic | Lockup (≤ 8 words) | f0 card (the diagram/proof) | First punch (claim word) |
|---|---|---|---|---|
| Fitness `[NICHE: example]` | Quitting workout plans | "Why You Quit Every *Workout* Plan" (LK-1, "Workout Plan" crimson on paper) | A weekly streak calendar whose ticks stop on day 9 (created UI) | "**because** you're relying on motivation" |
| Fitness | Fat-loss plateau | "The Real Reason You *Stopped* Losing Fat" | Weight curve on axes that flattens (illustrative, no numbers) | "**it's** not your metabolism" |
| Fitness | Habit loop | "The 3-Part Loop Behind *Every* Habit" (LK-2) | The loop motif outline drawing with 3 empty nodes | "**most** coaches teach this backwards" |
| Fitness | Protein | "You're Eating Protein At The **Wrong** Time" | A day timeline with 3 meal markers | "**timing** beats total" |
| Marketing `[NICHE: example]` | Ads stopped working | "Why Your Ads **Stopped Working**" (LK-1) | A results-panel mock whose curve drops fast (magenta) | "**because** the old funnel is dead" |
| Marketing | Posting consistency | "Posting Daily Is *Killing* Your Reach" | A tile grid of 9 posts greying out one by one | "**reach** isn't about volume" |
| Marketing | Offer framework | "The 4-Step *Offer* That Sells Itself" (LK-2) | The ladder motif with 4 empty rungs | "**nobody** buys features" |
| Marketing | Email list | "Your Email List Is Worth **More** Than Followers" | A counter card (the creator's list size) | "**here's** the math" |

### 6.5 Headline writing `[DNA formula; NICHE examples]`
**Formula:** `[viewer-pointed setup] + [key phrase in crimson] (+ one italic-serif word)`, ≤ 8 words, Title Case, saying exactly what the f0 card shows.

| Template | Example |
|---|---|
| The reason | "This Is The Reason Your *Videos* **Fail**" |
| How to make X Y | "How To Make Your *Offer* **Irresistible**" |
| X just changed Y | "This Tool Just *Changed* **Meal Prep Forever**" |
| N-part model | "The **4-Step** Loop Behind *Every* Sale" |
| Old vs new | "The *Old* Funnel **No Longer Works**" (LK-3) |
| Paste / do X and get Y | "Paste One Link And Get **Every Secret**" |
| All you need | "All You Need Is This **One** *Habit*" |

Write 3 and pick by ST-1 and ST-4. Banned: questions longer than 6 words, clickbait without a card that proves it, more than one crimson device, emoji, ALL CAPS.

### 6.6 Hook sound
The hook may carry one cue on f0 and one on the reading event (§11); the mode cuts are silent; the bed enters after the hook (at the first unit).

### 6.7 CTA `[DNA device set; VAR values]`
| Device | Spoken | On screen | Hold | Where |
|---|---|---|---|---|
| `comment_keyword` (default) | "Comment '{{BV-08.keyword|KEYWORD}}' and I'll send you the <deliverable>" | **P-CTA-ASSET:** LK-5 "Comment *“{{BV-08.keyword|KEYWORD}}”*" / "To Get The <Deliverable>" + an asset preview card in S-CARD (doc grid page by page; video card with a channel row "{{BV-01.name|the creator}} · <subscribers>"; or the tool's screenshot) | Keyword ≥ 2.0 s; the CTA run ≥ 4 s | Last 6–10 s, L-split (W-paper for docs/tools, W-stage for videos) |
| `link_bio` | "The <deliverable> is in my bio" | LK-1 "Grab The <Deliverable>" / "**Link In Bio**" + the same asset preview | ≥ 2.0 s | Same |
| `post_only` | none | The reel ends on the motif recap (P-MOTIF-RECAP) in L-split | — | — |

A mid-reel verbal mention of the keyword is allowed (placement TUNE `mid+end`); it shows the LK-5 lockup for ≥ 1.5 s in the split, no asset. Silence (no SFX) in the 1.0 s before the CTA's first word. No end card after the asset (N11).

---

---


## §7 Structure & cadence `[REQ] [DNA]`

### 7.1 Structure type: `framework` (three variants)
| Variant | Arc | Recurring diagram (§23) | Units | Evidence |
|---|---|---|---|---|
| **FW-1 Numbered framework** | promise → the model built → step 1…N (each a visit) → recap → CTA | The motif (loop, ring, ladder) with N nodes | `STEP-1…N`, N = 3–5 | v02 (4-step addiction loop) |
| **FW-2 Old vs new** | the problem → the old model (named) → "but" → the new model on the **same axes** → the part that matters (threshold) → CTA | The shared axes chart: the old curve, then the new curve, then the threshold bars | `OLD`, `TURN`, `NEW`, `DETAIL` | v01 (traditional vs modern story arc) |
| **FW-3 Workflow** | the result → station 1 (do this) → station 2 (get this) → station 3 (connect this) → result again → CTA | The station chain (3–4 stations on a line; the active station lit) | `STATION-1…N`, N = 3–4 | v03 (paste URL → analysis → install) |

Pick the variant at P4b from the talk's shape: named parts → FW-1; a "used to / now" contrast → FW-2; a sequence of actions in a tool → FW-3.

### 7.2 Markers
- **SM-NUM** (FW-1): hero numeral + 2-line step name beside the lit motif node (§5.4), on the step word ±2 f, numbering ascending, at **every** step.
- **SM-STATION** (FW-3): the station's number in a 64 px circle on the chain + its LK-4 title.
- FW-2 uses no numerals: the lockup names the model ("Traditional *Story Arc*" → "Modern *Story Arc*").
- **Recap** (FW-1, FW-3): P-MOTIF-RECAP, all N labels around the motif, before the CTA. No teaser chips.

### 7.3 Unit ritual (identical for every step; frames at 30 fps from the step word's onset, f0)
| Frames | What happens |
|---|---|
| f−2…f24 | **P-MOTIF-VISIT** in L-split: the whole band pans to node k (400–700 px, expo ease-out: most of the travel in 8 f, then a 16 f settle drift; the caption hides during a silent pan; v02 @ 0:10.8–0:11.5); node k−1 dims to 35% (6 f); node k lights in `accent` with a 28 px glow at f12 |
| f0…f10 | **P-HERO-NUMERAL:** numeral k fades in grey → white (6 f) already placed beside the node and travels with the pan (v02 @ 0:10.85–0:11.05), landing on the step name word; the 2 name lines stagger 3 f. List cue on the landing frame |
| +1.2…2.0 s | **P-TITLE-SWAP** to the step's LK-4 lockup; the step's explainer card scales in (P-CARD-SCALE-IN, 8 f) in place of the motif |
| next 2–8 s | The explainer evolves on its nouns, one event every 0.8–2.5 s (patterns from §8.4) |
| on the claim word | **P-FULL-PUNCH** (1.5–3.0 s) |
| on the example word | **P-SPLIT-RETURN** with a new card state, or **P-CLIP-INTERCUT** (≤ 2 per reel) |
| next step word | back to row 1 |

FW-2 ritual per model: P-AXES-BUILD (once) → the curve draws → callouts per term → punch on "but" → P-ARC-SWAP on the return. FW-3 ritual per station: the chain slides to station k (12 f), station k lights, then the tool card (P-CHAT-TYPE / P-RESULT-SECTIONS / P-SETTINGS-LIST) takes the card slot.

### 7.4 Open loops and re-hooks
- **Count loop:** FW-1 shows N empty nodes at the build; the viewer watches them fill. The numerals match (H10).
- **Model loop:** FW-2 names the old model first and holds the new one until after the "but" punch.
- **Payoff rule:** every promised part, model and deliverable appears on screen before the CTA.
- **Re-hooks** (`standard`, `rehook_every_s: 30`): every motif visit with a hero numeral is a re-hook (beat `rehook: true`); FW-2 and FW-3 add one at 40–65% of runtime: an LK-3 key-slab lockup ("This Is The Part Nobody Shows") or a P-CLIP-INTERCUT, flagged `rehook: true`. No gap between re-hooks > 30 s.
- **Intro cap:** the hook ≤ 15% of runtime.

### 7.5 Rhythm and energy curve
- Information rhythm: a new card idea every 6–12 s (≈ 4 per minute), a punch every 7–15 s (3–8 per minute), the caption every 0.25–0.6 s.
- Energy: hook (fast: punch by 3 s) → model build (steady, explain) → each step (punch on its claim) → the last step escalates (the longest motif push, the example clip) → recap (calm, all lit) → CTA (clean; no punch after the CTA starts).
- No comedy beats (comedy off).

### 7.6 Cadence (state changes)
| Token | Value | Why |
|---|---|---|
| `sc_per_10s` | [11, 24] | Graphic + stage events 4–8 per 10 s plus one-word captions (≈ 28 per 10 s × 0.34) |
| `hook_sc_3s` | 9 | v01 0–3 s: 6 graphic/stage events + 11 caption words |
| `max_gap_s` | 4.0 (hook 1.5) | A full-face run (≤ 4 s) is the longest stretch without a full-weight change |
| `max_static_s` | 2.0 | Live footage is always on screen, so this only bites on a frozen card with no footage motion |
| `caption_weight` | 0.34 | One-word captions swap ~3× as often as a 3-word card; each counts a third (Part E) |
| `cuts_per_min`, `median_shot_s` | null | Mode switches are stage events, not cuts; the layout schedule enforces them (H3) |

---

## §8 Visual system `[REQ]`

### 8.1 Graphics role and budget
- `graphics: primary`: a card is on screen whenever L-split is (60–80% of runtime); 50 patterns.
- Families per 60 s: ≥ 4 (B-1 and B-4 always, plus at least two of B-2, B-3, B-5, B-6, B-7, B-9).
- **Numbers become pictures:** a spoken number is a counter, a stat chip on its curve point, or a count of things (N tiles, N nodes); never a lone number on an empty card.

### 8.2 Families
| ID | Family | Source class | What the buyer supplies |
|---|---|---|---|
| B-1 | Concept diagrams: axes, curves, nodes, loops, roads, ladders | engine | nothing |
| B-2 | Recreated UI & devices: phone, chat, settings, insights panel, profile | engine (created) | optional: their own screenshots (SH-2) |
| B-3 | Document & page cards: doc pages, script page, output sections | engine | optional: their own doc pages for the CTA asset |
| B-4 | Lockups, numerals, step names | engine | nothing |
| B-5 | Chips, tags, annotations, hand labels | engine | nothing |
| B-6 | Line-art objects & icons with glow (`fx.icon`, bespoke SVG) | engine | nothing |
| B-7 | Creator media: own screenshots, screen recordings, reels, thumbnails | buyer-owned | SH-2, SH-3 |
| B-8 | Creator-supplied third-party: a film moment, another creator's reel, a news screenshot | creator-supplied only (never fetched); substitute named per pattern | asked once per reel (§12.5) |
| B-9 | Counters & stat chips | engine + figures.json | the numbers (spoken or stated) |
| B-10 | Stage patterns (mode cuts, world flips) | engine | nothing |

### 8.3 Pattern specs
Frames at 30 fps. "Engine" names the building block: `VEOS.scene` (bespoke; diagrams drawn on `ctx.canvas()` with `box` = the card slot, so a push stays measured as the slot), `fx.diagram`, `fx.card`, `fx.device`, `fx.appUI`, `fx.logoPlate`, `fx.shot`, `fx.clip`, `fx.icon`, `VEOS.data.counter`, and the inserts toolkit (`fx.quoteCard`, `fx.silhouette`).

**Stage (B-10)**
| ID | Name | Type | On screen | Motion | Use when | Engine |
|---|---|---|---|---|---|---|
| **P-FULL-PUNCH** | Full punch | stage | L-full: face + the CS-2 caption only | Cut (0 f) to a static crop; in runs ≥ 2 s about every second one steps tighter on a mid-run jump cut (`punch-in` 1.15×, 1 f) or drifts (`push-drift` 1.0 → 1.05) | Every claim, turn, warning, opinion | `stage` + `camera` |
| **P-SPLIT-RETURN** | Return with change | stage | L-split with a new card state on the cut frame | Cut (0 f); the card event starts on the same frame | Back to the explanation | `stage` + any card pattern |
| **P-WORLD-FLIP** | World flip | stage | The band flips W-stage ↔ W-paper with a new card | Cut on a G-2 return, `fade: 0` | A section start whose subject changes kind (§3.1) | `world` |
| **P-CLIP-INTERCUT** | Example intercut | footage-treatment | A creator-supplied clip full-bleed (L-clip), CS-2 captions on it | Cut in, plays from its own first frame; may be 2–3 shots cut every 0.25–1.5 s (v02 @ 1:18.4–1:22.3); exit by a hard cut to L-full or by **P-CLIP-PULLOUT** (v01 @ 0:43.5) | A story, film moment, scene or example the creator owns or holds | `fx.clip` z4 (insert) |

**Cards & lockups (B-4)**
| ID | Name | Type | On screen | Motion | Use when | Engine |
|---|---|---|---|---|---|---|
| **P-CARD-SCALE-IN** | Card arrives | overlay | A blank rounded card (phone 520×980 r 48, doc 640×820 r 18, panel 952×700 r 28) in S-CARD; white on paper (shadow 0 10 30 rgba(0,0,0,.15)); #121214 with a 1.5 px rgba(255,255,255,.35) hairline on stage | Scale 0.92 → 1.0, blur 10 → 0, opacity 0 → 1 over 8 f (ease-out); content populates from f6 | Every new card | `fx.card` / bespoke |
| **P-TITLE-SWAP** | Title swap | overlay | Lockup A replaced by lockup B in S-HEAD | A blur-out 4 f; B blur-in 6 f (words staggered 3 f); underline redraws 8 f | The idea changes but the band stays | bespoke `kind: lockup` |
| **P-SLAB-KEY** | Key slab | overlay | LK-3: a crimson slab behind the key line, white text | Slab width 0 → 100% L → R 6 f (ease-out), text fades in over it 4 f | The turn ("no longer works") | bespoke `kind: lockup` |
| **P-SMEAR-PUSH** | Smear push | overlay | Card A leaves, card B arrives, same slot; the lockup stays | A exits sideways 700 px in 3 f with a horizontal motion blur ≈ 40 px; B enters from the other side in 4 f, blurred → sharp, ease-out, often slightly oversized (1.1 → 1.0) | A quick swap between two things of one idea (logo → profile, grid → logo); ≤ 3 per reel; never on a mode cut | scene fields `in: "slide-r", in_frames: 4` on B and `out: "slide-l", out_frames: 3` on A, both with `smear: true` (the presets' own 700 px travel, smeared along it by core; no scene-side blur). B draws its own 1.1 → 1.0 scale |
| **P-DETAIL-CUTZOOM** | Detail cut-zoom | overlay | The same card cut to 2–2.6× on one detail (the channel row, a stat), lockup gone | Hard cut on the detail word, the zoomed card blurs 10 → 0 over 4 f; then holds or drifts | The CTA asset's channel row (v02 @ 1:42.5), a key number on a card; ≤ 1 per reel | bespoke (the card scene re-drawn at scale) |
| **P-CLIP-PULLOUT** | Clip pull-out | footage-treatment | An L-clip shrinks into a phone frame in the card band (world revealed around it); a kinetic word builds on it ("brain") | Phone bezel appears at the edges, scale 1.0 → 0.62 over 8 f ease-out; the window returns on the same frame | Leaving an example clip back into the explanation (v01 @ 0:43.55) | `fx.clip` + `fx.device`, bespoke scale |

**Concept diagrams (B-1)**: lines 4 px (paper on stage, ink on paper); node dots 14 px white (with a 2 px ink ring on paper).
| ID | Name | Type | On screen | Motion | Use when | Engine |
|---|---|---|---|---|---|---|
| **P-AXES-BUILD** | Axes | overlay | L-shaped axes (x 120–960, y 520–1080 inside the slot), optional axis titles 28 px `mute` (E3, redundant) | Y-axis draws up 8 f, x-axis right 10 f | Before any curve | `VEOS.scene` canvas |
| **P-CURVE-DRAW** | Curve draws | overlay | A smooth curve on the axes with node dots at its turning points; neon glow on stage | Path draws L → R over 24–40 f (ease in-out); dots pop 5 f as the head passes | A process over time, an arc, a retention or growth shape | canvas |
| **P-NODE-CALLOUT** | Node tags | annotation | White callout tags (28–40 px) next to nodes ("Initial Conflict", "Climax") | Each tag pops 6 f (scale 0.8 → 1, opacity) on its spoken term | Naming the parts of a curve or diagram | canvas + DOM tags |
| **P-ARC-SWAP** | Old → new | overlay | The old curve fades to 25% in `bad`; the new curve draws in paper/`good` on the same axes; the lockup swaps "Old" → "New" | Old fade 8 f; new draw 24–36 f; title swap 4+6 f | FW-2 at the turn | canvas |
| **P-CURVE-OVERLAY** | The reading | overlay | A second series in `data` magenta over the model curve (same axes), with one stat chip | Draws 20–30 f; the chip pops on its number | "Your numbers actually do this" | canvas + figure |
| **P-AREA-FILL** | Area fill | overlay | `data` fill (alpha 0.55) under one section of the curve | The fill sweeps L → R 18 f | "This part is where they stay" | canvas |
| **P-THRESHOLD-BAR** | Threshold | annotation | `highlight` yellow segment bars (h 12 px) under the x-axis on the deciding window + an italic-serif annotation tag with a curl arrow ("Hook") | Bars grow L → R 6 f each; the tag fades 6 f, the arrow draws 8 f | "The first 3 seconds", "the part that decides" | canvas + DOM |
| **P-DIAGRAM-PUSH** | Push into the diagram | overlay (in-band camera) | The diagram scaled 1.6–2.4× about a target node, clipped to the band (x 0–1080, y 110–1170); off-target labels and the lockup fade first | Labels/lockup fade 4 f, then scale + translate over 18–24 f ease in-out; hold; pull back 18 f or cut away | Reading a detail (a point, a segment); the motif travel | canvas, `box` = band |
| **P-CHIP-STACK** | Ingredient chips | overlay | Grey bevel chips stacked in a column, joined to a diagram point by a 2 px bracket line | The bracket draws 8 f; each chip rises 12 px + fades 6 f on its word, 12 px apart | Listing what goes into one part ("contrast moment, contrarian take, shocking stat") | DOM |
| **P-MINI-FRAMES** | Two small frames | overlay | Two framed mini charts stacked (each 640×300, hairline frame, small title "Good …" / "Great …"), each with its own curve | Frame 1 draws, curve 20 f; frame 2 the same 1.0–2.0 s later | Good vs great, before vs after on small multiples | canvas |
| **P-ROAD-FORK** | Expectation vs turn | overlay | A dashed road (expected path, `mute`) and a glowing road (`good`) diverging; a white dot with a soft cone travels; "A" / "B" labels 64 px | Roads draw 20 f; the dot travels 1.5–2.5 s along A, then swings to B on the turn word | Headfakes, twists, "you think it goes here, then…" | canvas |
| **P-TOKEN-LIST** | Numbered tokens | overlay | Round numbered tokens (Ø 96, rim in `highlight`, numeral 48 px) each with a 2-line label (40 px) | Tokens drop in from y −60 with one spin (12 f) and settle into a column, one per spoken item | 2–4 sub-parts of a step | DOM / canvas |
| **P-CONCEPT-LINK** | Linked objects | overlay | Object A (line-art icon 200 px with glow) linked by a 2 px line to object B, then C | The line draws 10 f between objects; each object fades/scales in 8 f | "X drives Y, the same as Z" | `fx.icon` + canvas |
| **P-OBJECT-PULSE** | Object pulse | overlay | One line-art object centred (Ø 300) with a filled `accent` disc expanding behind it (0.55 → 1.1 scale, alpha 0.55 → 0) | The object fades in 8 f; the disc expands 15 f and fades | Naming the mechanism ("your brain", "the algorithm") | `fx.icon` + DOM |

**The recurring motif (B-1, §23)**
| ID | Name | Type | On screen | Motion | Use when | Engine |
|---|---|---|---|---|---|---|
| **P-MOTIF-BUILD** | Motif built | state | The motif (loop, ring, ladder, road or chain) in `accent` neon on stage (ink with a `primary` lit node on paper) with N numbered empty nodes; LK-4 title above | The path draws 30–45 f; nodes pop 5 f each in order; numbers fade 6 f | The first mention of the framework (≤ 25% of runtime) | canvas, `kind: diagram` |
| **P-MOTIF-VISIT** | Motif visit | state | The same motif pushed (1.6–2.2×) so node k sits at the slot's left-centre; node k lit, the others at 35% | In-band pan, expo ease-out: main travel 8 f + 16 f settle; light 6 f; the previous node dims 6 f | Every step / station entry | canvas |
| **P-HERO-NUMERAL** | Step numeral | overlay | Numeral k 200 px + a 2-line step name 72 px beside node k | Fades grey → white 6 f in place, travels with the pan; name lines stagger 3 f | With every P-MOTIF-VISIT (FW-1) | DOM, `kind: rehook` |
| **P-MOTIF-RECAP** | Motif recap | state | The whole motif, every node lit in sequence, all N labels around it; an LK-4 title | Pull-out 18 f; nodes light one by one 8 f apart; labels fade 6 f | Before the CTA | canvas |

**Recreated UI, devices and documents (B-2, B-3)**
| ID | Name | Type | On screen | Motion | Use when | Engine |
|---|---|---|---|---|---|---|
| **P-UI-POPULATE** | UI fills | overlay | A generic panel inside a phone/card: header, a thumbnail block, a chart area, rows | Rows fade + rise 8 px, 2 f stagger, top → bottom; a chart line draws last | "Your dashboard / insights / results show…" | `fx.device` / `fx.appUI` |
| **P-PHONE-MOCK** | Phone | overlay | A generic phone frame (520×1000, r 56) with content inside (a feed, a post, a page) | Scale-in 8 f; the content scrolls 1 px/f or swaps hard inside the screen | "On your phone", "the post", "the page" | `fx.device({kind: "phone"})` |
| **P-CHAT-TYPE** | Typed command | overlay | A chat input card (952×300, r 24) with a mono line and a send button | Types 1 char/f (blur 6 → 0 per char), the caret blinks every 15 f; send pulses 1.0 → 1.12 → 1.0 (6 f) on "enter/send" | "Type /analyze", "paste the link", a prompt | `fx.appUI({kind: "chat"})` |
| **P-RESULT-SECTIONS** | Output sections | overlay | A white output card whose sections (bold header + 2–3 decorative lines) appear one per spoken section name | Each section rises 10 px + fades 8 f on its word; the card scrolls up 40 px per section after the third | "It gives you X, Y and Z" | `fx.card({device: doc})` |
| **P-SETTINGS-LIST** | Settings list | overlay | A two-column settings panel; a list of items appears row by row; one row highlighted in `highlight` at 35% | Rows 2 f stagger; the highlight box slides to its row 8 f | "Go to settings → skills → install" | `fx.appUI({kind: "settings"})` |
| **P-DOC-HIGHLIGHT** | Script line | overlay | A dark doc card (title "SCRIPT"/"PLAN") with grey placeholder lines and one real sentence lit white (40 px) | The card scales 0.92 → 1 (8 f), then pushes 1.0 → 1.25 (18 f) toward the lit line; the line types at 2 chars/f | Quoting one line of a plan, script or rule | bespoke |
| **P-DOC-GRID** | Page grid | overlay | A grid of N doc pages (3 per row, 220×280, 16 px gaps), illegible body lines (TC-decorative), the last page's key line in `highlight` | Pages pop in reading order 4 f apart; the highlight sweeps 8 f | The deliverable, "my 8-page guide" | bespoke |

**Counters and stats (B-9)**
| ID | Name | Type | On screen | Motion | Use when | Engine |
|---|---|---|---|---|---|---|
| **P-COUNTER-TICK** | Counter ticks | figure | A profile/result card with a counter chip ("2K followers" → "19K followers") | Digits step every 5 f (E6, `data-slot` chip) through a figures.json series; the tile grid behind fills one tile per step | The creator's own growth or result | `VEOS.data.counter` + `exception: E6` |
| **P-STAT-CHIP** | Stat on the curve | figure | A small chip (icon + number, 40 px) pinned to a curve point ("832 views") | Pops 6 f on the number word; a 2 px leader draws 6 f | A spoken number that belongs to a point on the diagram | bespoke `figure` |

**Creator media & tiles (B-7, B-8)**
| ID | Name | Type | On screen | Motion | Use when | Engine |
|---|---|---|---|---|---|---|
| **P-SHOT-CARD** | Creator screenshot | overlay | The creator's screenshot in a card (r 24), optional highlight box | Scale-in 8 f, push 1.0 → 1.06 over its life | Showing their real tool, page or data | `fx.shot` (insert, origin creator) |
| **P-CLIP-CARD** | Clip in a card | footage-treatment | A creator clip in a 9:16 card (430×760, r 24) in S-CARD | Scale-in 8 f; plays by `ctx.videoFrame` | An example reel or B-roll while the face stays in the window | `fx.clip` (insert) |
| **P-CLIP-TAG** | Tagged clip | annotation | P-CLIP-CARD + a neon outline box (`good` or `data`, 3 px) on a region + a label with a dotted leader ("10K followers") | The box draws 8 f; the label fades 6 f; the leader draws 6 f | Pointing at the moment inside the example | `fx.clip` + DOM (static coordinates) |
| **P-MINI-PLAYER** | Mini player montage | footage-treatment | A 16:9 card (760×428, r 18, white glow) cycling 3–4 creator clips | Hard swap every 5 f (E6 slot); the card grows slowly (1.0 → 1.05) | HA-06b hook: "creators who…" | `fx.clip` ×N (inserts) |
| **P-TILE-WALL** | Tile column | overlay | A 3-column wall of 9:16 tiles (180×320, 8 px gaps) | The column slides up 10 f per row; on the negative word every tile tints `bad` (2 f) | "Everyone posts this", "the feed is full of…" | `fx.clip` / `fx.card` tiles (inserts when not the creator's own) |
| **P-TILE-GRID** | Tile grid | overlay | A 2×3 grid of the creator's tiles (280×500) | Tiles pop 4 f apart; a number tile may carry a stat | "My last 6 videos", examples | `fx.shot` tiles |
| **P-COLLAGE-FLIP** | Collage flip | overlay | 4–5 playing clip tiles in a 3D cluster that orbits and re-stacks | Cut in on a return; continuous rotateY/translate orbit ≈ 30 f (v01 @ 0:12.27–0:13.5), then cut to the next card | Card → card at a section change (≤ 1 per reel) | bespoke |

**Labels, plates, objects (B-5, B-6)**
| ID | Name | Type | On screen | Motion | Use when | Engine |
|---|---|---|---|---|---|---|
| **P-HAND-LABELS** | Hand labels | annotation | 3 stacked cards, each with a big bold label (56–68 px) and a hand-drawn squiggle arrow pointing at it | The card rises 8 f; the label fades 6 f; the arrow draws 8 f; 0.6–1.0 s apart | "You get trends, insights and patterns" | DOM + SVG |
| **P-LOGO-LINK** | Linked plates | overlay | Two created logo plates (180×180, r 24) joined by a chain-link icon; a third may join | Plate A pops 6 f, the link draws 8 f, plate B pops 6 f | "Connect X to Y" | `fx.logoPlate` + `fx.icon` |
| **P-CONVERGE** | Converge | overlay | 3–5 small plates scattered, flying into one large plate | Scatter in 8 f, hold, converge 14 f (ease-in) into the big plate (scale 0.4 → 1) | "All of it in one place" | `fx.logoPlate` |
| **P-TILE-FLIP** | Card flip | overlay | A card back (pattern) flips to its face (the reveal: a word, a number, a line-art image) | rotateY 0 → 180° over 10 f; face content from frame 5 | A reveal, a draw, "the twist" | bespoke |

**CTA and brand**
| ID | Name | Type | On screen | Motion | Use when | Engine |
|---|---|---|---|---|---|---|
| **P-CTA-ASSET** | CTA asset | overlay | The LK-5 lockup + the deliverable preview: P-DOC-GRID, a video card (thumbnail 952×536 r 18 + a channel row: avatar, name, subscribers, a "Join" pill), or a P-SHOT-CARD of the tool | Lockup blur-build; the preview builds (pages pop 4 f apart / the card scales in 8 f); the keyword's serif span bumps 1.04 on its word | The CTA (§6.7) | bespoke, `kind: cta-keyword` |
| **P-SPONSOR-CARD** | Sponsor | overlay | A created logo plate + one line + TC-legal "Paid partnership" 24 px under it | Scale-in 8 f; disclosure held ≥ 2 s | Only when `modules.brand` is on (§25) | `fx.logoPlate` |

### 8.4 Line → pattern lookup `[NICHE]`
| Line type | Primary | Alternates | Fitness `[NICHE: example]` | Marketing `[NICHE: example]` |
|---|---|---|---|---|
| LT-1 The problem / "the reason X fails" | P-CARD-SCALE-IN + P-UI-POPULATE | P-CURVE-DRAW (`data` drop) | A streak calendar that stops on day 9 | An ad results panel, the curve drops |
| LT-2 The old way / what everyone teaches | P-AXES-BUILD + P-CURVE-DRAW + P-NODE-CALLOUT | P-MINI-FRAMES | "Eat less, move more": a flat line | "Awareness → interest → buy": the funnel arc |
| LT-3 The turn ("but", "instead", "here's the thing") | P-FULL-PUNCH | LK-3 P-SLAB-KEY on the return | — | — |
| LT-4 The new way / the model | P-ARC-SWAP | P-CURVE-OVERLAY | A small-wins curve rising in steps | A trust curve with repeated spikes |
| LT-5 The part that decides | P-THRESHOLD-BAR + P-DIAGRAM-PUSH | P-AREA-FILL | "The first 14 days" bars | "The first 3 seconds" bars |
| LT-6 A list of ingredients | P-CHIP-STACK | P-TOKEN-LIST | Sleep / protein / steps chips | Hook / proof / offer chips |
| LT-7 A named step ("step one: …") | P-MOTIF-VISIT + P-HERO-NUMERAL | — | "1 Cue" on the habit loop | "1 Stakes" on the offer ladder |
| LT-8 A mechanism ("your brain…", "the algorithm…") | P-OBJECT-PULSE + P-CONCEPT-LINK | — | Line-art heart → flame → trophy | Line-art eye → speech bubble → cart |
| LT-9 Expectation vs reality / a twist | P-ROAD-FORK | P-TILE-FLIP | "You expect the scale to drop…" | "They expect a pitch; you give a story" |
| LT-10 An example scene / story / clip | P-CLIP-INTERCUT (creator-supplied) | P-CLIP-CARD; created: P-TILE-FLIP or a `fx.silhouette` scene | A client's before/after clip (the creator's own) | A competitor ad (only if the creator supplies it) |
| LT-11 Good vs great | P-MINI-FRAMES | P-ARC-SWAP | "Good plan / great plan" | "Good post / great post" |
| LT-12 A tool action (type, paste, click) | P-CHAT-TYPE | P-SETTINGS-LIST | "Type your goal into the app" | "Paste your ad copy" |
| LT-13 What the tool gives you | P-RESULT-SECTIONS | P-HAND-LABELS | "Meals, macros, shopping list" | "Hook, angle, CTA" |
| LT-14 Where to click / install | P-SETTINGS-LIST | P-PHONE-MOCK | Settings → reminders | Settings → integrations |
| LT-15 The creator's own result | P-COUNTER-TICK | P-SHOT-CARD | Client count climbing | Follower count climbing |
| LT-16 "Everyone does this" / examples | P-TILE-WALL | P-TILE-GRID | 9 workout-post tiles | 9 ad tiles |
| LT-17 Connect two tools | P-LOGO-LINK | — | Watch ↔ app | CRM ↔ email tool |
| LT-18 All in one place | P-CONVERGE | — | 4 apps → one plan | 5 channels → one inbox |
| LT-19 Labelled takeaways | P-HAND-LABELS | P-CHIP-STACK | "Strength, Cardio, Recovery" | "Trends, Insights, Patterns" |
| LT-20 Quoting a line of a plan/script | P-DOC-HIGHLIGHT | — | One line of a meal plan | One line of a sales script |
| LT-21 A spoken number on the model | P-STAT-CHIP | P-COUNTER-TICK | "70% quit by week 3" (only if stated with its source) | "832 views → 101" (the creator's own) |
| LT-22 The summary ("that's the loop") | P-MOTIF-RECAP | — | The habit loop, all lit | The offer ladder, all lit |
| LT-23 Opinion / warning / claim | P-FULL-PUNCH | — | — | — |
| LT-24 CTA | P-CTA-ASSET | — | "Comment PLAN" + plan pages | "Comment ADS" + guide pages |

### 8.5 Data and truth rules
- Pointer: §18. Concept curves (arcs, retention shapes, habit curves) are **illustrative**: no axis numbers, a concept label (the lockup or the axis titles), and the TC-legal `example` tag if any number appears on them.
- Same axes for every comparison (P-ARC-SWAP, P-CURVE-OVERLAY, P-MINI-FRAMES share one scale).
- Counters and stat chips show only spoken, scripted or creator-supplied numbers (figures.json provenance).
- A recreated UI that stands for a real product shows only the words of the script.

### 8.6 Comedy layer
OFF (`tone.comedy: off`, comedy_max off): no stickers, stamps, freeze-frames or meme cues.

### 8.7 Asset rules
- Real captures first: the creator's own screenshots, reels and data (SH-2, SH-3).
- Mocks are generic and unbranded (never a look-alike of a real app); product names appear as created logo plates (the name set in `display` in a neutral rounded tile).
- No stock footage, no stock 3D, no AI-generated scenes. Line-art objects come from `fx.icon` or are drawn in SVG.
- Every third-party moment goes through ask-then-create (§12.5).

### 8.8 Density and variety
- Card events every 0.8–2.5 s in L-split; ≥ 8 distinct patterns per 60 s; ≥ 4 families per 60 s.
- The same pattern at most 2 cards in a row, except the unit ritual (P-MOTIF-VISIT + P-HERO-NUMERAL repeat by design).
- One idea per card; ≤ 3 animated groups inside a card at once.

---

## §9 Transitions `[REQ] [DNA]`

### 9.1 Library
| ID | Transition | Frames | Recipe | SFX role |
|---|---|---|---|---|
| **T-01** | Mode cut | 0 | A hard cut between L-split, L-full and L-clip on a word start | silent |
| **T-02** | Jump-cut step | 0 | Inside an L-full run: a jump cut on a word boundary that also steps the framing 1.12–1.2× tighter (`punch-in`) | silent |
| **T-03** | Card scale-in | 8 | P-CARD-SCALE-IN | reveal (optional) |
| **T-04** | Title swap | 4 + 6 | P-TITLE-SWAP | silent |
| **T-05** | Evolve | — | A state change inside the same card (a node, a label, a series): no transition | — |
| **T-06** | Diagram push | 18–24 | P-DIAGRAM-PUSH (in-band) | silent |
| **T-07** | Motif pan | 14–20 | The P-MOTIF-VISIT travel | list cue on the numeral landing |
| **T-08** | Collage orbit | ≈ 30 | P-COLLAGE-FLIP | reveal (optional) |
| **T-09** | Tint flip | 2 | Tiles tint `bad` on the negative word (P-TILE-WALL) | silent |
| **T-10** | Slide-up | 10 | A new card or tile column rises 60 px + fades in; the old one fades out 6 f | reveal (optional) |
| **T-11** | World flip | 0 | P-WORLD-FLIP on a T-01 return frame | silent |
| **T-12** | Hard end | 0 | The last frame ≤ 6 f after the last word | — |
| **T-13** | Smear push | 3 + 4 | P-SMEAR-PUSH: the old card leaves sideways with a horizontal motion blur, the new one arrives from the other side, blurred, ease-out (v03 @ 0:01.6, 0:32.4–0:32.9) | whoosh (soft, optional) |
| **T-14** | Detail cut-zoom | 0 + 4 | P-DETAIL-CUTZOOM: cut to the same card at 2–2.6× on one detail, blur 10 → 0 over 4 f (v02 @ 1:42.47) | silent |
| **T-15** | Clip pull-out | 8 | P-CLIP-PULLOUT: the full-bleed clip shrinks into a phone frame in the card band, ease-out (v01 @ 0:43.55–0:43.9) | silent |

### 9.2 Grammar
| Boundary | Use | Never |
|---|---|---|
| Frame 0 | T-03 card scale-in + the lockup readable | A fade-in from black |
| Claim word | T-01 to L-full (static crop) | A morph, a shrink, a slide, a land/settle zoom |
| Mid-run in L-full (≥ 2 s) | T-02 jump-cut step, about every second run | Two steps in one run |
| Back to the card | T-01 + a T-03 / T-04 / T-05 event on the same frame | Returning to an unchanged card |
| New step | T-07 motif pan + numeral | A hard cut to an unrelated card |
| Card → card (same section) | T-04 + T-03, T-10, or T-13 (≤ 3 per reel) | Two cards on screen together |
| Section change | T-11 (with T-01) or T-08 | More than one T-08 per reel |
| Number lands | E6 digit steps, P-STAT-CHIP pop | Shake, flash |
| Example | T-01 into L-clip; T-01 or T-15 out | A fade into the clip |
| CTA asset detail | T-14 onto the channel row / key page | More than one T-14 per reel |
| Last word | T-12 | A black tail, an outro card |

### 9.3 Shot grammar
OFF (`spine: talking_head`, one presenter): jump cuts only remove dead air on word boundaries (H5).

### 9.4 Budget (per 60 s)
- T-01 mode cuts: 6–16 (3–8 punches and their returns).
- T-07: one per step; T-08 ≤ 1 per reel; T-11 ≤ 3 per reel.
- The same transition (other than T-01 and T-05) never 3× in a row.

---

## §10 Motion, camera, layers, finishing `[REQ] [DNA; motion TUNE ±15%]`

### 10.1 Motion tokens
| Token | Value |
|---|---|
| Lead | 2 f before the onset |
| Entries / exits | `cubic-bezier(0.22, 1, 0.36, 1)` / `cubic-bezier(0.64, 0, 0.78, 0)`, exits 4–6 f |
| In-out (pushes, pans) | `cubic-bezier(0.65, 0, 0.35, 1)` |
| Blur build | 6 f per word, blur 12 → 0 px, y +8 → 0, stagger 3 f |
| Underline draw / slab sweep | 8 f / 6 f, L → R |
| Card scale-in | 0.92 → 1.0, blur 10 → 0, 8 f |
| Curve draw | 24–40 f; node pop 5 f; callout pop 6 f |
| Push / pan | 12–24 f at 1.6–2.4× (the hold then drifts 1–3%) / motif pan expo-out 8 f + 16 f settle |
| Smear push | out 3 f + in 4 f, 700 px, horizontal motion blur ≈ 40 px |
| Detail cut-zoom | cut to 2.0–2.6×, blur-in 4 f |
| Clip pull-out | clip → phone frame at 0.62, 8 f ease-out |
| Hook band zoom | 0.65 → 1.0 over 45 f, ease-out |
| Lockup build | line 6 f, line stagger 5 f; LK-2 word 4 f |
| Title swap | 4 f out + 6 f in |
| Counter step | every 5 f (E6) |
| Typewriter | 1 char/f |
| Row stagger | 2 f |
| Hold | text ≥ 0.25 s per word; titles ≥ 10 f after they finish building |

### 10.2 Footage camera (`zoom_policy: crop_on_cut`)
| ID | Preset | Recipe | Use |
|---|---|---|---|
| — | (entry) | No move: the L-full entry is a static crop (face 0.26) | Every punch |
| **Z-2** | `push-drift` | 1.00 → 1.05 linear over the whole L-full run | Occasionally (v02 @ 1:08–1:11); never two runs in a row |
| **Z-3** | `punch-in` | 1.00 → 1.15 (measured 1.08–1.22) in 1 f on a jump cut, held to the end of the run | About every second L-full run ≥ 2 s, on a mid-run word (v01 @ 0:02.75, 0:23.75, 0:55.25; v03 @ 0:15.76, 0:17.25, 0:50.0); ≤ 6 per reel |

Rules: camera events only on a mode cut or a jump cut (V-CAMERA); never the same preset twice in a row; no camera moves in L-split (the window stays still) or in L-clip.

### 10.3 Canvas camera
OFF (§21). The diagram camera is in-band (P-DIAGRAM-PUSH, P-MOTIF-VISIT).

### 10.4 Layer order (back to front)
1. World (W-stage / W-paper), z1
2. World glow, z2
3. Card-slot content: diagrams, motif, UI, docs, tiles, clip cards, z3 (drawn under the footage group, which never overlaps the band)
4. Face window / full-face footage (the stage); the full-bleed clip scene in L-clip, z4
5. Lockup, labels, tags, chips, hand labels, z5
6. Hero numeral, stat chips, counter chips, z6
7. Captions (CS-1 / CS-2), z7
8.–11. Unused (no z8 big captions, no comedy layer, no banner slab, no light passes)

### 10.5 Finishing
No grain, no vignette, no light leaks. Glow only on W-stage neon lines and the lit node (`shadowBlur` 20–28 px, the role colour at 70%). Paper cards: radius 18–28, shadow `0 10px 30px rgba(0,0,0,.15)`. Stage cards: #121214 fill, a 1.5 px rgba(255,255,255,.35) hairline, glow `0 0 40px rgba(255,255,255,.08)`. The face window: radius 30, shadow 0.25, no border.

---

## §11 Sound contract (minimal) `[REQ] [VAR]`
| Line | Decision |
|---|---|
| **Cue moments** | `hook` (f0 and the first reading event), `reveals` (a card or diagram landing, a counter's last value), `list_cue` (each P-HERO-NUMERAL / station landing: the one allowed repeat), `cta` (the CTA lockup landing); optionally a soft `whoosh` on a P-SMEAR-PUSH. **Mode cuts, jump-cut steps, title swaps and pushes are silent.** At most 4 cues per 10 s (sound unobservable in the evidence: a decision, not a measurement) |
| **Meme cues** | Off (comedy off) |
| **Music bed** | On; enters at the first unit after the hook; drops out 0.5 s before the recap |
| **Ducking** | The bed sits ≥ 18 dB under the voice while the voice speaks; a creator clip's own audio (P-CLIP-INTERCUT) is kept 20 dB under the voice, or muted if it has speech |
| **Loudness** | −14 LUFS integrated, true peak ≤ −1.5 dBTP; hard end ≤ 6 f after the last word |

Mirrored in `tokens.json → sound`.

---

## §12 Footage, shot list, fallbacks, inserts `[REQ]`

### 12.1 Setups `[DNA what the style assumes; VAR the buyer's setups]`
| Setup | Spec |
|---|---|
| **A (assumed)** | Landscape 16:9, **3840×2160**, 30 fps (or 24/25, conformed), locked-off at eye level, medium-wide (waist up), presenter centred (face centre at 42–58% of the width), head top at 12–22% of the frame height, face 20–26% of the frame height; one coloured practical light in the background (an LED strip or lamp) on a dark set; plain dark top; hands free (the style lives on gestures); lav or shotgun mic out of frame |
| **B (fallback)** | Vertical 9:16, 1080×1920, chest-up, head top at 10–14% of the frame height (FB-1) |

From setup A the window (L-split) shows the whole wide frame (a 0.27× scale of the 4K frame) and the full face (L-full) is a 9:16 slice of the same frame at ≈ 1.0× (no upscaling): one camera gives both modes.

### 12.2 Shot list
OFF as a requirement (`footage_dependency: low`): the style needs only the take (SH-1). Optional SH-2 (own screen recordings/screenshots) and SH-3 (own reels/clips) raise fidelity; their fallbacks are FB-3 / FB-4 in 12.4.

### 12.3 Fallbacks
OFF as a section (`footage_dependency: low`); the resolution and media fallbacks are in 12.4.

### 12.4 Props, reaction bank, matte, resolution
- Props: none. Reaction bank: none. Matte: optional (only for ER-1 when it ships).
- **Minimum source:** a full-face punch at face 0.26 needs a face box ≥ 450 px in the source, i.e. a 4K landscape take (setup A). 1080p sources allow ≤ 1.35× upscale.

| ID | When | What the engine does | Fidelity cost | Result |
|---|---|---|---|---|
| **FB-1** | Vertical 1080×1920 take | L-split window face 0.30 (head and shoulders); L-full on the native frame at face 0.24 (≤ 1.15×) | The window loses the room; the two modes look closer | degraded |
| **FB-2** | Landscape 1920×1080 take | L-full face 0.20 (a 1.35× crop of the 9:16 slice); window as setup A | Looser, slightly soft punches | degraded |
| **FB-3** | No screen recording of a tool | Recreated generic UI (P-CHAT-TYPE, P-SETTINGS-LIST, P-UI-POPULATE) from the script's words| No real product pixels | holds |
| **FB-4** | No own reels/clips | Created typographic tiles (topic word + tint) in P-TILE-WALL / P-TILE-GRID; the intercut becomes a P-TILE-FLIP or P-ROAD-FORK beat | No footage texture in the example beat | holds |

### 12.5 Third-party inserts: ask, then create `[REQ]`
1. At P5, run `veos inserts scan` and list the moments that call for third-party material: a film or TV moment, another creator's reel, a tweet or post, a news headline, a product's screen, a person's photo, a brand logo.
2. **Ask the creator once:** "For these N moments, do you have a clip or screenshot you own or hold? (drop the files, or say no)".
3. **Supplied:** use it as given (`veos asset add --origin creator`) in P-CLIP-INTERCUT, P-CLIP-CARD, P-CLIP-TAG, P-SHOT-CARD or P-MINI-PLAYER; never altered to say something else.
4. **Not supplied: Claude creates:**

| Moment | Created substitute |
|---|---|
| A film/TV/other creator's clip (P-CLIP-INTERCUT, P-CLIP-CARD) | A `fx.silhouette` or line-art scene of the action in the card slot, or a P-TILE-FLIP / P-ROAD-FORK beat carrying the same point; never a full-bleed fake clip |
| Another creator's reel or thumbnail (P-TILE-WALL, P-MINI-PLAYER) | Created typographic tiles (topic word, tint; no faces, no handles) |
| A post or quote | `fx.quoteCard` with the verbatim script words |
| A product screen | `fx.appUI` / `fx.device` recreated generic UI |
| A brand or tool (P-LOGO-LINK, P-CONVERGE) | `fx.logoPlate` (the name set in type) |
| A person | `fx.silhouette` with the name and role from the script |

5. **Record** every insert in `plan/inserts.json` `{id, moment, origin: creator | created, file?, recipe?, substitute_of?}`.

### 12.6 Frame rate and audio
30 fps CFR output, 1080×1920, BT.709. One voice track: high-pass 80 Hz, de-ess, light compression, −14 LUFS.

---

## §13 Output contract `[REQ] [DNA]`

### 13.1 Core beat fields
`id`, `section` (HOOK · STEP-n / OLD · TURN · NEW · DETAIL / STATION-n · RECAP · CTA), `t0`, `t1`, `spoken`, `trigger {word, at}`, `tone`, `line_type` (LT-…), `layout` (L-split · L-full · L-clip), `visual` (one sentence), `layers` (scene ids), `pattern` (P-…), `sfx`.

### 13.2 Conditional fields
| Switch / module | Beat fields |
|---|---|
| captions | `caption {profile: CS-1 or CS-2, emphasis: [word] or [], overrides: []}` |
| chrome | `slot_content {S-HEAD: "LK-n: text", S-CARD: "pattern + ref"}` |
| data_figures | `figure_id` (every number on screen) |
| continuity | `motif_state` (`build` · `idle` · `visit:k` · `recap`), `rehook: true` on visits |
| worlds | `world` (W-stage · W-paper) on beats where it flips |
| camera | `camera` (`punch-in` at a mid-run jump cut · `push-drift` · null) |
| a third-party moment | `insert {id, origin: creator or created}` |
| an exception | `exception: E3 or E6` (also on the scene) |

### 13.3 Reel header
```yaml
reel:
  format: F-A
  theme: null
  hook_archetype: HA-06          # or HA-02 / HA-07 / HA-05
  structure: {type: framework, variant: FW-1, count: 4}
  motif: {shape: loop, nodes: ["Stakes", "Big Question", "Headfake", "Rehook"]}
  worlds: [W-stage]              # in order of appearance
  keyword: "{{BV-08.keyword|KEYWORD}}"
  cta: {device: "{{BV-08.device|comment_keyword}}", deliverable: "<the doc / video / template>"}
  figures: plan/figures.json
  inserts: plan/inserts.json
  fallbacks_used: []             # FB-1...FB-4
```

### 13.4 Hook proposals (3)
```yaml
- name: "Framework build: the loop behind every habit"
  archetype: HA-06
  lockup: {recipe: LK-2, l1: "The 3-Part Loop Behind", l2: "Every Habit", serif: "Every Habit", crimson: underline}
  f0_card: "habit loop outline drawing, 3 empty nodes (P-MOTIF-BUILD)"
  first_punch: {word: "most", at: 2.1}
  captions: "CS-1, CS-2 from the punch"
  storyboard: "f0 lockup + loop outline | 0.5 nodes pop 1-2-3 | 1.2 node 1 lights | 2.1 punch 'most coaches...' | 3.9 return: Cue card"
  sound: [hook cue f0, reveal on node 1]
  stopper_test: {thumbnail: pass, mute: pass, read_s: 1.75, sc_3s: 11, payoff_s: 1.2}
```

### 13.5 Checkpoint
1. 3 hook proposals with lockups and stopper results.
2. The framework line (name, N parts, motif shape) and the structure variant.
3. The beat sheet with tones, layouts and the **mode schedule** (every punch and return with its word).
4. The world plan and the transition map.
5. The SFX ledger.
6. The figure plan (every number with its provenance) and the inserts record (asked / creator / created).
7. The fallbacks used (FB-n).
8. Style stills: f0, the first punch, one motif visit with its numeral, one diagram push, the CTA asset.

**Wait for approval.**

---
## §14 Worked examples `[REQ] [NICHE]`
Times are planning estimates; replace them with `words.edit.json` onsets. Every switch sits on a word start. Camera "—" on a punch means the static crop; in about every second full run ≥ 2 s also add a `punch-in` on a mid-run jump cut (H14). Two example niches: **fitness coaching** and **small-business marketing**, plus a workflow example for an educator.

### 14.1 Fitness coaching, FW-1 numbered framework, HA-06 `[NICHE: example]`
```yaml
reel: {format: F-A, hook_archetype: HA-06, structure: {type: framework, variant: FW-1, count: 3},
       motif: {shape: ring, nodes: ["The Cue", "The Effort", "The Reward"]}, worlds: [W-stage, W-paper],
       keyword: LOOP, cta: {device: comment_keyword, deliverable: "30-day habit tracker"}, duration_s: 62.5}
```
**Hook (f0 → payoff):**
| t (s) | Spoken | Layout · world | Visual | Caption | Camera | Cue |
|---|---|---|---|---|---|---|
| 0.00 | "Here's why you quit…" | L-split · stage | LK-2 "Why You Quit Every / *Workout Plan*" (underline drawing); P-CARD-SCALE-IN phone with a streak calendar (P-UI-POPULATE), days 1→9 ticking white (illustrative, `example` tag) | "Here's" (CS-1, white) | — | hook |
| 0.4–1.3 | "…every workout plan" | same | Ticks stop at day 9; days 10–14 stay grey; the empty row pulses `bad` once on "plan" (1.3) | one word each | — | reveal |
| 1.9 | "**because** you're relying on motivation" | L-full | Face only | "because" (CS-2) | — | — |
| 3.5 | "Habits run on a loop, three parts" | L-split · stage | P-TITLE-SWAP LK-4 "The Habit *Loop*"; P-MOTIF-BUILD ring draws (3.5–4.8), 3 nodes pop on "three" (4.4) | — | — | — |
| 5.6 | "**and most** coaches teach it backwards" | L-full | Face | — | `push-drift` | — |
| 7.4 | "Part one: the cue." | L-split | P-MOTIF-VISIT node 1 + P-HERO-NUMERAL "1 / The Cue" (hook ends: 11.8%) | — | — | list cue |

**Section plan:**
| t (s) | Section | Spoken (gist) | Layout | Patterns | Lockup (S-HEAD) | Camera |
|---|---|---|---|---|---|---|
| 7.4 | STEP-1 | "Part one: the cue" | split | P-MOTIF-VISIT, P-HERO-NUMERAL (rehook) | — | — |
| 9.0 | STEP-1 | "Same time, same place, shoes by the door" | split | P-CHIP-STACK: "Same Time" 9.6 · "Same Place" 10.4 · "Shoes By The Door" 11.3 | "The *Cue*" | — |
| 12.3 | STEP-1 | "Motivation is **not** the trigger" | full 2.4 s | P-FULL-PUNCH | — | — |
| 14.7 | STEP-1 | "Your environment is" | split | Chips fold into one node label "Environment" on node 1 (T-05) | "The *Cue*" | — |
| 17.0 | STEP-2 | "Part two: the effort" | split | P-MOTIF-VISIT node 2 + "2 / The Effort" (rehook) | — | — |
| 18.6 | STEP-2 | "Most plans start at an hour a day" | split | P-AXES-BUILD + P-CURVE-DRAW in `bad`: high start, drop-off (no numbers) | "Start *Smaller* Than Easy" | — |
| 21.2 | STEP-2 | "**That's** why week two kills you" | full 2.0 s | P-FULL-PUNCH | — | `push-drift` |
| 23.2 | STEP-2 | "Instead, ten minutes, then build" | split | P-ARC-SWAP to a `good` staircase; P-STAT-CHIP "10 min" on step 1 (figure: spoken) | "Start *Smaller* Than Easy" | — |
| 26.4 | STEP-2 | "The first fourteen days decide it" | split | P-THRESHOLD-BAR under days 1–14 + annotation "*First 14 Days*" (curl arrow); P-DIAGRAM-PUSH into the bars at 27.4 | — | — |
| 29.6 | STEP-2 | "Miss once, fine. **Miss** twice, you're out." | full 2.6 s | P-FULL-PUNCH | — | — |
| 32.2 | STEP-3 | "Part three, the one everyone skips: the reward" | split | P-MOTIF-VISIT node 3 + "3 / The Reward" (rehook) | — | — |
| 34.0 | STEP-3 | "Your brain needs the win today" | split | P-CONCEPT-LINK: line-art dumbbell → tick → trophy (34.4, 35.2, 36.0) | "Win *Today*" | — |
| 37.4 | STEP-3 | "Abs in ninety days is **not** a reward" | full 2.2 s | P-FULL-PUNCH | — | `push-drift` |
| 39.6 | STEP-3 | "A ticked box is" | split | P-PHONE-MOCK tracker; today's box ticks `good` on "ticked" (40.2) | "Win *Today*" | — |
| 42.5 | STEP-3 | "My client did exactly this" | clip 3.0 s | P-CLIP-INTERCUT of the creator's own client clip (consent given); if none: stay split, P-TILE-FLIP "Week 1 → Week 12" (created) (rehook) | — | — |
| 45.5 | STEP-3 | "and **never** missed a Monday since" | full 2.5 s | P-FULL-PUNCH | — | — |
| 48.0 | RECAP | "Cue, effort, reward. That's the loop." | split | P-MOTIF-RECAP: nodes light on each word (48.4, 48.9, 49.5), labels around the ring | "The Habit *Loop*" | — |
| 53.0 | RECAP | "**Run** it thirty days and it runs itself" | full 2.6 s | P-FULL-PUNCH | — | `push-drift` |
| 55.6 | CTA | "Comment LOOP and I'll send you my 30-day tracker" | split · **paper** (P-WORLD-FLIP) | P-CTA-ASSET: LK-5 "Comment *“LOOP”*" / "To Get The Tracker" + P-DOC-GRID (6 pages, last row highlighted) | LK-5 | — |
| 62.5 | end | — | — | T-12 | — | — |

Shares: L-full 17.9 s (29%), L-clip 3.0 s (5%), L-split 66%. Punches: 8 in 62.5 s. Figures: `ten_min` (spoken@23.6), `days_14` (spoken@26.9, illustrative bar label). Inserts: I1 client clip (creator) or created P-TILE-FLIP; I2 tracker app (created recreated UI).

### 14.2 Small-business marketing, FW-2 old vs new, HA-06 `[NICHE: example]`
```yaml
reel: {format: F-A, hook_archetype: HA-06, structure: {type: framework, variant: FW-2},
       motif: {shape: axes, states: ["old funnel arc", "new trust curve", "hook bars"]}, worlds: [W-paper, W-stage, W-paper],
       keyword: ADS, cta: {device: comment_keyword, deliverable: "3-second hook guide"}, duration_s: 63.5}
```
**Hook:**
| t (s) | Spoken | Layout · world | Visual | Caption | Camera | Cue |
|---|---|---|---|---|---|---|
| 0.00 | "This is why your ads…" | L-split · paper | LK-1 "Why Your Ads / **Stopped Working**" (crimson key phrase); P-CARD-SCALE-IN results panel (created, `example` tag) | "This" (CS-1, ink) | — | hook |
| 0.2–0.7 | "…your ads…" | same | P-UI-POPULATE rows, 2 f stagger | words | — | — |
| 1.1 | "…stopped working" | same | P-CURVE-DRAW in `data` inside the panel: a steep drop | words | — | reveal |
| 2.0 | "**because** you're still selling with the old funnel" | L-full 2.1 s | Face | CS-2 | — | — |
| 4.1 | "Awareness, interest, decision" | L-split · **stage** (P-WORLD-FLIP) | LK-4 "The Old *Funnel*"; P-AXES-BUILD + P-CURVE-DRAW smooth arc; P-NODE-CALLOUT "Awareness" 5.4 · "Interest" 6.2 · "Decision" 7.0 | CS-1 white | — | — |
| 8.2 | "**But** nobody waits for step three anymore" | L-full 1.6 s | Face | — | `push-drift` | — |
| 9.8 | "This funnel…" | L-split | P-SLAB-KEY LK-3 "The Old Funnel / **No Longer Works**" (hook ends: 15%) | — | — | — |

**Section plan:**
| t (s) | Section | Spoken (gist) | Layout | Patterns | Lockup | Camera |
|---|---|---|---|---|---|---|
| 9.8 | TURN | "My own click rate fell from 4% to under 1%" | split | Old arc fades to 25% `bad`; P-CURVE-OVERLAY `data` drop with P-STAT-CHIP "4%" 11.2 and "0.8%" 12.6 (figures: creator data, asked) | LK-3 (held) | — |
| 13.8 | TURN | "**Here's** what changed" | full 1.8 s | P-FULL-PUNCH | — | — |
| 15.6 | NEW | "Now it's a trust curve" | split | P-TITLE-SWAP "The New *Trust Curve*"; P-ARC-SWAP: a curve of repeated small spikes; P-NODE-CALLOUT "Proof" 17.6 · "Story" 18.4 · "Offer" 19.2 | "The New *Trust Curve*" | — |
| 20.6 | NEW | "People buy after the **fifth** touch, not the first" | full 2.3 s | P-FULL-PUNCH | — | `push-drift` |
| 22.9 | NEW | "One, two, three, four, five" | split | P-DIAGRAM-PUSH along the spikes; spikes 1–5 light `accent` on each count word | — | — |
| 27.0 | DETAIL | "And what decides each one is the first three seconds" | split | P-THRESHOLD-BAR under each spike start + annotation "*Hook*" (27.8) (rehook) | "The *First* Three Seconds" | — |
| 30.5 | DETAIL | "If those **don't** stop them, nothing else gets seen" | full 3.0 s | P-FULL-PUNCH | — | — |
| 33.5 | DETAIL | "Contrast, a number, or a question" | split | P-CHIP-STACK on spike 1: "Contrast" 34.1 · "A Number" 34.9 · "A Question" 35.7 | — | — |
| 37.2 | DETAIL | "Look at the ad I ran last month" | split | P-CLIP-CARD of the creator's own ad recording + P-CLIP-TAG outline on its first 3 s caption (37.8); if none: P-PHONE-MOCK with a created generic ad (rehook) | "Same Product, *New* Hook" | — |
| 41.0 | DETAIL | "**Same** product. Same budget." | full 1.8 s | P-FULL-PUNCH | — | `push-drift` |
| 42.8 | DETAIL | "Old hook, new hook" | split | P-MINI-FRAMES: "Old Hook" flat retention, "New Hook" held retention (illustrative, same scale) 43.0 / 44.6 | "Same Product, *New* Hook" | — |
| 46.8 | DETAIL | "**Triple** the sales" | full 2.6 s | P-FULL-PUNCH | — | — |
| 49.4 | RECAP | "So stop building funnels" | split | The shared axes, final state: old arc 25% `bad`, trust curve white, every hook bar lit yellow (P-MOTIF-RECAP on the axes) | "Earn *Trust* Five Times" | — |
| 53.6 | RECAP | "**Build** the curve" | full 2.0 s | P-FULL-PUNCH | — | `push-drift` |
| 55.6 | CTA | "Comment ADS and I'll send you my hook guide" | split · **paper** | P-CTA-ASSET: LK-5 "Comment *“ADS”*" / "To Get The Hook Guide" + P-DOC-GRID (9 pages) | LK-5 | — |
| 63.5 | end | — | — | T-12 | — | — |

Shares: L-full 17.2 s (27%). Figures: `ctr_before` 4% and `ctr_after` 0.8% (from: creator); "triple" stays spoken (not shown). Inserts: I1 the creator's own ad (creator) or a created phone ad (recreated_ui).

### 14.3 Educator workflow, FW-3, HA-02 (alternate archetype) `[NICHE: example]`
```yaml
reel: {format: F-A, hook_archetype: HA-02, structure: {type: framework, variant: FW-3, count: 3},
       motif: {shape: chain, nodes: ["Dump", "Sort", "Block"]}, worlds: [W-paper],
       keyword: WEEK, cta: {device: comment_keyword, deliverable: "the planning prompt"}, duration_s: 60.8}
```
| t (s) | Section | Spoken (gist) | Layout | Patterns | Lockup | Camera |
|---|---|---|---|---|---|---|
| 0.00 | HOOK | "Plan your whole week in ten minutes" | split · paper | LK-1 "Plan Your Whole Week / In **10 Minutes**"; proof: a created week grid already filling Mon→Fri, one block every 4 f (kind `proof`) | LK-1 | — |
| 2.2 | HOOK | "**and** I haven't missed a deadline since" | full 1.6 s | P-FULL-PUNCH | — | — |
| 3.8 | HOOK | "Three stations" | split | P-TITLE-SWAP "Three *Stations*"; P-MOTIF-BUILD chain of 3 stations (4.0–5.2) | "Three *Stations*" | — |
| 5.6 | HOOK | "You **just** need one chat and one calendar" | full 1.8 s | P-FULL-PUNCH | — | `push-drift` |
| 7.4 | STATION-1 | "First, dump everything" | split | Chain slides to station 1 (SM-STATION "1") (rehook); P-CHAT-TYPE types a brain-dump line (8.2–11.0); send pulses on "enter" (11.2) | "*Dump* Everything" | — |
| 12.0 | STATION-1 | "**Don't** organise it. Just dump it." | full 2.0 s | P-FULL-PUNCH | — | — |
| 14.0 | STATION-2 | "Second, ask it to sort by energy" | split | Station 2 lit (rehook); P-RESULT-SECTIONS "Deep Work" 14.4 · "Admin" 15.2 · "Calls" 16.0 | "Sort By *Energy*" | — |
| 18.2 | STATION-2 | "Your **energy** decides the order" | full 2.6 s | P-FULL-PUNCH | — | `push-drift` |
| 20.8 | STATION-2 | "Mornings, afternoons, evenings" | split | P-HAND-LABELS "Morning" 21.2 · "Afternoon" 22.0 · "Evening" 22.8 pointing at the three sections | "Sort By *Energy*" | — |
| 24.6 | STATION-3 | "Third, send it to your calendar" | split | Station 3 lit (rehook); P-LOGO-LINK plates "Chat" ↔ "Calendar" (25.4, 26.2), or the creator's named tools as created plates | "*Block* It" | — |
| 27.6 | STATION-3 | "**This** is the part nobody does" | full 2.2 s | P-FULL-PUNCH | — | — |
| 29.8 | STATION-3 | "Settings, integrations, calendar" | split | P-SETTINGS-LIST, the highlight lands on "Calendar" (30.6) | "*Block* It" | — |
| 33.0 | STATION-3 | "Here's my actual week" | split | P-SHOT-CARD of the creator's own calendar screenshot (SH-2), or FB-3 week grid (rehook) | "My *Actual* Week" | — |
| 38.4 | STATION-3 | "**Ten** minutes on Sunday. That's it." | full 2.6 s | P-FULL-PUNCH | — | `push-drift` |
| 41.0 | RECAP | "Dump, sort, block" | split | P-MOTIF-RECAP: stations light on each word | "The *Sunday* Ten" | — |
| 45.0 | RECAP | "**Try** it this Sunday" | full 1.8 s | P-FULL-PUNCH | — | — |
| 46.8 | RECAP | "Tasks, calls, notes, all in one place" | split | P-CONVERGE three plates into one calendar plate (47.2–49.4) | "All In *One* Place" | — |
| 50.6 | RECAP | "**Your** week plans itself" | full 2.2 s | P-FULL-PUNCH | — | `push-drift` |
| 52.8 | CTA | "Comment WEEK and I'll send you the prompt" | split | P-CTA-ASSET: LK-5 "Comment *“WEEK”*" / "To Get The Prompt" + a prompt doc card (P-DOC-HIGHLIGHT on paper) | LK-5 | — |
| 60.8 | end | — | — | T-12 | — | — |

Shares: L-full 16.8 s (28%). Inserts: the tool names as created logo plates; the calendar screenshot (creator) or FB-3.

---

## §15 QA checklist `[REQ] [DNA]`
**1. Profile conformance**
- [ ] Format F-A; theme null; duration 60–90 s (or the tuned class) — V-PROFILE
- [ ] Face visible ≥ 90%, longest absence ≤ 4 s — V-PRESENCE
- [ ] Layout shares L-split 60–80%, L-full 15–35%, L-clip ≤ 8%; runs within min/max; switches on claim/but/number/sentence/pause words — V-LAYOUT

**2. Hook**
- [ ] f0: lockup readable, card skeleton moving, window live — V-F0
- [ ] ≥ 9 weighted SCs in 0–3 s; the first punch at 1.5–3.0 s; the diagram/proof readable by 2.5 s — V-CADENCE, V-F0
- [ ] Lockup ≤ 8 words, 2 lines, Title Case, one crimson device, ≤ 1 serif span, reads in ≤ 2.0 s — V-TITLE
- [ ] Mute test passes (lockup + card + captions tell the topic) — review

**3. Body and cadence**
- [ ] 11–24 weighted SCs per 10 s; no full-weight gap > 4.0 s; card events every ≤ 2.5 s in L-split — V-CADENCE + review
- [ ] 3–8 punches per 60 s; L-full entries are static crops; about every second run ≥ 2 s has one punch-in step; captions swap hard; every return changes the card — V-CAMERA + review
- [ ] Unit ritual identical at every step; numerals 1…N match the promise — review, V-PROMISE
- [ ] Re-hooks: no gap > 30 s; one in 25–75% of runtime; hook ≤ 15% — V-REHOOK

**4. Captions**
- [ ] CS-1 in L-split (56 px, cy 1245, ink on paper / white on stage), CS-2 in L-full and L-clip (66 px, cy 1160, white) — V-CAPTION, V-TYPE
- [ ] One word per chunk; lead ≤ 1 f; serif swaps ≤ 1 per 5 s; glossary spelling — V-CAPTION
- [ ] Never on a card, never on the face — V-FACE, G1

**5. Modules**
- [ ] Chrome: S-HEAD, S-CARD, S-CAP and S-WIN rects constant ±4 px; nothing outside its slot (except the in-band push, clipped to the band) — V-CHROME (pending: review)
- [ ] Continuity: one motif, ≥ 3 appearances, lit node = the current step, recap before the CTA — V-CONTINUITY (pending: review)
- [ ] Data: every number in figures.json; illustrative charts labelled; counters land ±5 f — V-DATA, V-NUMFMT

**6. Truth and inserts**
- [ ] Every third-party moment asked once; creator-supplied or created (recorded in inserts.json); reconstructions labelled — V-INSERTS
- [ ] No fake metrics, no look-alike UIs — review (NC-6)

**7. Sound contract**
- [ ] Cues only on hook, reveals, list cue, CTA; mode cuts silent; ≤ 4 per 10 s; silence 1 s before the CTA — S1–S6
- [ ] Bed after the hook, ≥ 18 dB under the voice; −14 LUFS, TP ≤ −1.5 dBTP — mix gate

**8. End and export**
- [ ] CTA keyword ≥ 2.0 s; the asset shown is the asset promised; ends on L-split — V-PROMISE
- [ ] Hard end ≤ 6 f after the last word; no black tail; 1080×1920, 30 fps — review / `veos qa`

---

## §16 Frame template / persistent chrome `[COND: modules.chrome] [DNA rects; TUNE ±5%]`
The frame never changes in L-split; only slot content changes. In L-full and L-clip the whole template steps aside (the face or the clip fills the frame) and returns unchanged.

| Slot | Rect (x, y, w, h) | z | Lifetime | Content types | Entry | Content swap |
|---|---|---|---|---|---|---|
| **S-HEAD** | 64, 150, 952, 210 | 5 | `section:split` (each card idea) | lockup LK-1…LK-5, step name | blur build 6 f per word | P-TITLE-SWAP (4 + 6 f) |
| **S-CARD** | 64, 380, 952, 780 | 3 | `section:split` | diagram, motif, recreated UI, doc card, clip card, tile grid, counter card, logo plate | P-CARD-SCALE-IN 8 f | evolve (T-05) or a new card (T-03 / T-10) |
| **S-CAP** | 64, 1205, 952, 80 (cy 1245) | 7 | video (CS-1; CS-2 moves to cy 1160 in L-full) | the one-word caption | hard | hard |
| **S-WIN** | 64, 1400, 952, 520 (bleeds off the bottom) | 4 | `section:split` | the face (footage) | cut | cut |

Rules:
- Slot rects stay constant ±4 px for their lifetime (V-CHROME; pending, so the frame reviewer checks it).
- Slots never overlap; S-CARD content stays ≥ 45 px above the caption rect.
- The only content allowed outside S-CARD is an in-band push (P-DIAGRAM-PUSH / P-MOTIF-VISIT), clipped to x 0–1080, y 110–1170, during which the lockup is hidden.
- A hero numeral and step name live inside S-CARD (beside the node), never in S-HEAD.
- The beat sheet writes `slot_content` only (§13.2).

## §17 Running state & anchored graphics
OFF (`modules.running_state = false`, `modules.anchors = false`): counters are single figures inside one card (§18), not a reel-long state; annotations use static coordinates set at P8.

## §18 Data contract `[COND: modules.data_figures] [DNA rules]`
Every number on screen is a figure in `plan/figures.json`:

| Figure kind | Used by | Provenance | Rule |
|---|---|---|---|
| `counter` (series) | P-COUNTER-TICK | `creator` (asked: "what were the start and end numbers?") or `script` | Steps every 5 f between the stated values; the first stated value lands ±5 f of its spoken number; E6 slot |
| `hero_number` / stat chip | P-STAT-CHIP, P-CURVE-OVERLAY chips | `spoken@t` or `creator` | Written by `ctx.fmtNum` in the profile's format ("10K", "4%", "$1.2M") |
| `line` (illustrative) | P-CURVE-DRAW, P-ARC-SWAP, P-MINI-FRAMES, P-AREA-FILL | none | `illustrative: true`: no axis numbers; a concept label (lockup or axis titles); the TC-legal `example` tag if any number appears on the chart |
| `bar` (illustrative threshold) | P-THRESHOLD-BAR | the spoken window ("first 3 seconds", "14 days") | Integers ≤ 12 may be shown as words; larger ones need a figure |

Formulas allowed: `sum`, `diff`, `ratio`, `percent_change`, `per_period`. Compared curves share one `scale_id`.

Example (P-COUNTER-TICK with the creator's own numbers):
```json
{"inputs": {"start": {"value": 2000, "from": "creator"}, "end": {"value": 19000, "from": "creator"}},
 "figures": [{"id": "followers", "kind": "counter", "formula": "none", "format": {"compact": "k_m_b", "suffix": " followers"},
   "steps": [{"value": 2000, "at": 1.70}, {"value": 5000, "at": 1.87}, {"value": 8000, "at": 2.03}, {"value": 12000, "at": 2.20},
             {"value": 15000, "at": 2.37}, {"value": 18000, "at": 2.53}, {"value": 19000, "at": 2.70}]}]}
```
Validator: V-DATA, V-NUMFMT.

## §19 Evidence & citations
OFF (`modules.citations = false`): the style shows no source lines or article cards. Third-party moments still follow §12.5.

## §20 Dialogue
OFF (`modules.dialogue = false`): one presenter.

## §21 Canvas camera
OFF (`modules.canvas_camera = false`). The reference reels do move a camera over their diagrams (v01 @ 0:26–0:41, v02 @ 0:35, 1:15), but the move stays inside the card band while the caption band and the window hold still. The engine's canvas camera frames targets on the frame centre (y 960) and has no viewport, so a push would run into the caption band. The style therefore uses an **in-band camera** inside the diagram scene (P-DIAGRAM-PUSH, P-MOTIF-VISIT: canvas-drawn, `box` = the band, clipped). Engine request ER-2 (Part E) would let this module turn on.

## §22 Ink & annotation layer
OFF (`modules.ink = false`): the style's hand-drawn arrows and outline boxes (v01 @ 0:27 "HOOK", v03 @ 0:35 "Trends", v02 @ 0:38 "10K followers") are drawn **inside** their card scene (P-THRESHOLD-BAR, P-HAND-LABELS, P-CLIP-TAG), never as a free ink layer over footage.

## §23 Continuity `[COND: modules.continuity] [DNA]`
**23.1 The recurring diagram.** One per reel, chosen at P4b:

| Shape | Variant | Nodes | Look on W-stage | Look on W-paper |
|---|---|---|---|---|
| **Loop** (infinity) | FW-1, 4 parts | 4 numbered nodes on the crossings and lobes | `accent` neon tube (14 px, glow 24), white numerals | ink tube 10 px, `primary` lit node |
| **Ring** | FW-1, 3–5 parts | N nodes evenly on a circle (r 280) | same | same |
| **Ladder** | FW-1, steps that build on each other | N rungs bottom → top | same | same |
| **Road** | FW-1/FW-2 with a twist | 2 paths, A/B points | `mute` dashed + `good` glow | ink dashed + `good` |
| **Chain** | FW-3 | 3–4 stations (Ø 64 circles, numbered) on a line | white line, `accent` lit station | ink line, `primary` lit station |
| **Axes** | FW-2 | old curve, new curve, threshold bars | white axes, curves per §4 | ink axes, darkened curves |

**23.2 States:** `build` (P-MOTIF-BUILD, within the first 25% of runtime) → `idle` (shown smaller under a lockup) → `visit:k` (P-MOTIF-VISIT; node k lit in the accent role with a 28 px glow, others at 35%) → `recap` (P-MOTIF-RECAP, all lit).

**23.3 Rules:**
- The motif is drawn at the same world position and size every time it returns (`same_position`), so a visit is a pan to a known place.
- ≥ 3 appearances (build, ≥ 1 visit, recap); in FW-1 one visit per step.
- Exactly one node lit at a time except in the recap.
- Hand-offs are hard (T-01 returns, T-04 title swaps); no morph chain is required (`morph_required: false`), no bookend.
- Beats carry `motif_state`; visits carry `rehook: true`.

Validator: V-CONTINUITY (pending: the frame reviewer checks the appearances and the lit node).

## §24 Series furniture
OFF (`modules.series = false`): the evidence shows no series cards or episode tags; adding them is a deviation (DNA).

## §25 Sponsor, brand & end cards
OFF (`modules.brand = false`, no `end_card` device): the reel ends on the CTA asset (N11). If the buyer turns brand on (VAR), a sponsor appears as **P-SPONSOR-CARD** in S-CARD (created logo plate + one line), with the spoken disclosure and the TC-legal "Paid partnership" line held ≥ 2 s (NC-12), never over the window.

---

## Part C. Declared exceptions and the non-overridable core
**C.1 Core.** NC-1…NC-14 hold without exception. The ones this style leans on hardest: **NC-1** (the face window and the full face are never covered; captions sit on the chest in L-full), **NC-3** (mode changes are cuts, every element inside a card is eased), **NC-4** (captions ≥ 54 px; labels ≥ 28 px only under E3), **NC-5** (the window lives in the bottom band but carries no text), **NC-6** (illustrative curves labelled, no invented metrics), **NC-7** (creator-owned media only; created substitutes otherwise), **NC-10** (≤ 3 bright hues).

**C.2 Exceptions used:** E3 (labels only, 28–39 px with `data-redundant`; subtitles keep 54 px) and E6 (counter digits, numeral slot, mini-player swaps). Declared in §2.2 and `tokens.exceptions`; each scene that relies on one sets `exception`. Buyers may switch either off (stricter, VAR).

**C.3 Not exceptions here:** no chaos bursts (E2), no ambient fields (E4), no edge bleed (E5).

---

## Part D. Personalisation

### D.1 Branding questions (one round, each with "keep the template default")
| ID | Question | Lands on | Default |
|---|---|---|---|
| BV-01 | Your name and handle | `creator.name/handle`; the CTA video card's channel row | {{BV-01.name|the creator}} · {{BV-01.handle|@yourhandle}} |
| BV-02 | One or two brand colours | `roles.primary` (the crimson key phrase, underline, slab), `roles.accent` (the neon motif); contrast-nudged (primary must carry white text at ≥ 4.5:1 and read on #E4E4E0; accent must glow on #050505) | {{BV-02.primary|#B0122A}}, {{BV-02.accent|#FF2D55}} |
| BV-05 | Language you speak / caption language | `profile.language`, always asked: **English** → English captions (default) · **Hinglish** → romanised Hinglish captions · **Hindi** → Devanagari captions; numbers follow (BV-06) | English ({{BV-05.speech|en}} → {{BV-05.captions|en}}) | en}} speech, {{BV-05.captions | en}} captions |
| BV-08 | Your call to action | `profile.cta.chosen` + keyword/value: comment keyword · link in bio · none (post_only) | {{BV-08.device|comment_keyword}} "{{BV-08.keyword|KEYWORD}}" |

Defaulted, changeable later: fonts inside their classes (BV-03), number format (BV-06, follows BV-05), formats (only F-A), humour (off, DNA), never-on-screen list (BV-15), duration within the tuned class (BV-17).

### D.2 What a buyer may change
| Lock | Examples |
|---|---|
| **DNA** (a warned deviation) | The three bands and their rects, one-word captions, the mode schedule and cut-only changes, the lockup recipe, the recurring diagram, `captions.mode`, comedy off, the world pair, the pattern grammar |
| **TUNE** (inside a range) | Caption size CS-1 54–64 / CS-2 60–76 and cy (1225–1300 / 1140–1260); window y 1340–1460, radius 20–40, face 0.24–0.38; L-split max 8–20 s, punches 3–9 per 60 s, L-full max 3–6 s; cadence and motion ±15%; lockup size 48–80, max words 6–9; energy balanced ↔ hype; duration short ↔ long; fonts inside their classes; highlight yellow/lime |
| **VAR** | Brand colours (primary, accent, data), language, numbers, CTA device and keyword, sound contract, sponsor module, exceptions off, setups |
| **NICHE** | Hook pairs (§6.4), the line lookup (§8.4), worked examples (§14), the headline bank (App. A), the motif shape per reel |

### D.3 NICHE slots, filled per reel
At P7 write the reel's hook pair into §6.4; at P5/P8 map new line types onto the existing patterns (§8.4, ≤ 10 new niche patterns over time, built from the existing families); after the first approved reel, it replaces the closest §14 example; approved lockups join App. A; confirmed tool and brand names join the glossary.

---

## Part E. Changes from the coverage table and the analysis (with evidence)
| # | Coverage / analysis said | This template does | Why |
|---|---|---|---|
| 1 | `themes: per_section` (paper / stage) | `themes: single`; paper/stage are **worlds** flipped per section (≤ 3 per reel) | The palette never changes between paper and stage; only the background does (v01 @ 0:00 → 0:04 → 1:04). A world flip is the right engine device; theme packs would have nothing to change |
| 2 | sc_per_10s 4–6, hook 12 | sc_per_10s 11–24, hook 9, with `caption_weight` 0.34 | The coverage numbers counted graphic changes only (4–6) and the hook with captions at full weight; with one-word captions at weight 1.0 the window maximum would always fail. 0.34 makes one-word captions count like a primary 3-word card |
| 3 | SPLIT ≤ 8 s | L-split max 12 s (TUNE 8–18), typical 4–9 s | v02 holds split for 12–18 s while its card changes every 2–3 s (v02 @ 0:18–0:30, 0:35–0:52) |
| 4 | Caption ≈ 52 px, lowercase | CS-1 56 px / CS-2 66 px, case as spoken | Raised to the 54 px floor; the face-mode caption measures larger than the split one (v01 @ 0:02 vs 0:05); the evidence shows "But", "Then", "Claude", "YouTube" capitalised |
| 5 | Diagram labels ≈ 22 px | 28–39 px under E3 (redundant), else 40 | NC-4 absolute floor for labels is 28 |
| 6 | Face window x 30–1050 | x 64–1016 (measured 65–1011 on v01 sheets) | The measured rect sits exactly on the 64 px margin |
| 7 | Face window: the head breaks the top edge | Done: eye 0.16 + `breakout: 120` | The head breaks the top edge (engine head breakout) |
| 8 | (none) canvas camera | Off; in-band camera inside the scene | ER-2 |
| 9 | Ink not listed | Off; annotations drawn inside cards | One element per card (§22) |
| 10 | Clip world ≈ 0–10% | L-clip (stage hidden) ≤ 8%, ≤ 4 s, creator-supplied only | Film clips in v02 are third-party; never fetched (NC-7) |
| 11 | Full face 30–38%, 6–9 punches/min; 2-frame 1.05 → 1.0 punch on entry | L-full 15–35%, 3–8 punches/60 s, static entry + mid-run punch-in step | Full-rate completeness pass (Oct 2026): v01 29% / 7.3, v02 16% / 3.3, v03 31% / 7.7; entries measure 1.00 scale for 6 f; face-box steps 1.08–1.22× inside runs (`docs/audit/whiteboard-split/completeness.md`) |
| 12 | Captions pop 3 f | Hard swap | Every burst shows the word replaced on its frame, no scale (lib:kallaway is hard too) |

**Engine requests from the completeness pass**
- ~~ER-5~~ **Done (built-in):** slide presets take `smear: true` (P-SMEAR-PUSH).
- ~~ER-6~~ **Done (built-in):** world `grid.fade` (W-paper).
- **ER-7 Clip-to-device pull-out** (P-CLIP-PULLOUT): a stage morph from `hidden`/full-bleed clip into a `fx.device` rect; today a bespoke scene scales the clip.

**Engine requests**
- **ER-1 Window pop-out.** A `card` layout option `popout: {top_px: 60–90}` that draws the matte cut-out above the window's top edge, so the head breaks the frame as in every reference split (v01 @ 0:00, v02 @ 0:00, v03 @ 0:00). Today: head inside the window (eye 0.30).
- **ER-2 Canvas-camera viewport.** `canvas_camera.viewport {x, y, w, h}` so pushes frame nodes inside the graphic band and clip to it while captions and the window hold. Today: in-band camera inside one canvas scene.
- **ER-3 V-CHROME and V-CONTINUITY** are pending in the registry; until they ship, §15 module checks are frame-reviewer checks.
- **ER-4 Punch-rate check.** `layouts.schedule.punches_per_60s [3, 8]` (in tokens, not yet enforced) and a minimum separation between runs of one layout; today the max split length (12 s) forces switches and the rest is reviewed.

---

## Part F. ID index
| Prefix | IDs in this playbook |
|---|---|
| D | D1–D8 |
| H / N | H1–H16 / N1–N11 |
| W / L / G | W-stage, W-paper / L-split, L-full, L-clip / G-1–G-5 |
| CS | CS-1 (split word), CS-2 (face word) |
| LK | LK-1–LK-5 (lockup recipes) |
| HA / ST | HA-06 (default), HA-02, HA-07, HA-05 / ST-1–ST-6 |
| FW / SM | FW-1, FW-2, FW-3 / SM-NUM, SM-STATION |
| B / P | B-1–B-10 / 50 patterns (§8.3) |
| LT | LT-1–LT-24 (line types) |
| T / Z | T-01–T-15 / Z-2 push-drift, Z-3 punch-in (no Z-1: entries are static) |
| S | S-HEAD, S-CARD, S-CAP, S-WIN |
| SH / FB | SH-1–SH-3 / FB-1–FB-4 |
| E | E3, E6 |
| ER | ER-1–ER-7 (engine requests) |

---

## Appendix A. Headline & hook bank `[NICHE]`
Slots in angle brackets are filled per reel; the `[NICHE: example]` lines show both example niches.

| # | Lockup (≤ 8 words) | Recipe | Archetype | Fitness `[NICHE: example]` | Marketing `[NICHE: example]` |
|---|---|---|---|---|---|
| 1 | "This Is Why Your <Thing> **<Fails>**" | LK-1 | HA-06 | "This Is Why Your Diet **Never Sticks**" | "This Is Why Your Ads **Stopped Working**" |
| 2 | "How To Make Your / *<Thing> <Outcome>*" | LK-2 | HA-06 | "How To Make Your / *Workouts Addictive*" | "How To Make Your / *Offer Irresistible*" |
| 3 | "The <N>-Part *<Model>* Behind **Every <Win>**" | LK-2 | HA-06 | "The 3-Part *Loop* Behind **Every Habit**" | "The 4-Step *Ladder* Behind **Every Sale**" |
| 4 | "The <Old Way> / **No Longer Works**" | LK-3 | HA-05 | "The 12-Week Plan / **No Longer Works**" | "The Sales Funnel / **No Longer Works**" |
| 5 | "<Tool> Just *Changed* **<Domain> Forever**" | LK-1 | HA-02 | "This App Just *Changed* **Meal Prep Forever**" | "AI Just *Changed* **Cold Email Forever**" |
| 6 | "Paste <Input> And Get **<Every Result>**" | LK-1 | HA-02 | "Log One Meal And Get **Every Macro**" | "Paste One Link And Get **Every Secret**" |
| 7 | "**<0 → N>** <Result> In <Time>" | LK-1 | HA-07 | "**0 → 40** Clients In 90 Days" | "**2K → 19K** Followers In 6 Weeks" |
| 8 | "All You Need Is This **One** *<Thing>*" | LK-1 | HA-06 | "All You Need Is This **One** *Habit*" | "All You Need Is This **One** *Hook*" |
| 9 | "<Common Advice> Is **Killing** Your *<Goal>*" | LK-1 | HA-05 | "Cardio Is **Killing** Your *Progress*" | "Posting Daily Is **Killing** Your *Reach*" |
| 10 | "The *<Part>* Nobody **Shows You**" | LK-4 + slab | HA-06 | "The *Recovery* Nobody **Shows You**" | "The *Follow-Up* Nobody **Shows You**" |

Markup: **bold** = the crimson key phrase (or slab/underline on stage); *italic* = the Instrument Serif span. Never both on the same word.

## Appendix B. Evidence map
The full map (every DNA rule → `vNN @ m:ss`) and the `(unverified)` list are in `evidence.md`. Sources: `vibe-editing-os-research/analysis/short/kallaway.md` and the frame sheets `evidence/short/kallaway/v01–v03`. Unverified: the speech language (read from burnt-in captions, no transcript), all sound, the camera setup (single 4K camera vs two angles), and the head pop-out mechanism.
