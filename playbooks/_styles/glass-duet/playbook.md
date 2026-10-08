# Glass Duet Style Playbook (template v1)

**Purpose:** you (Claude) receive a seated talking-head take of {{BV-01.name|the creator}} teaching something (a method, a tool, N tips) or selling their own course or program, plus the script and whatever screen recordings, stills or result screenshots they drop in. Use this document to plan and build every caption, glass card, numbered marker, tutorial window, stage move and CTA so the reel reads at a glance as **Glass Duet**: an elegant two-voice caption at chest height, premium glass UI glowing in the reel's studio colour, and calm, eased motion.

**Input expected (SW-01 `talking_head`):** one continuous seated take, chest-up, 9:16, on a set lit in one saturated colour. Optional: exports or recordings of what is being taught, 4–8 portfolio stills, the link-card thumbnail, an earlier reel (for the recursion hook), real result screenshots (F-B).

**Style DNA.** A creator talks to camera in a coloured-light studio while every word they say is set in two type voices at chest height: an Edwardian-style script for the soft connective words and a clean bold sans for the content, with one heavy oversized word when it matters. Around them, premium "Apple-keynote" glass: numbered glass diamonds that pop out of the counting hand and glide, glowing chest windows with leader-line labels, full-screen tutorial cards with sparkle bullets, and the face itself shrinking into a floating card. One studio colour per reel tints every glow. Type and glass blur in, glide and blur out; the camera "breathes": every face shot lands slightly zoomed and settles out, leans in on each count/marker and leans back. Worlds change by hard cut, never by dissolve: the face leans in, cut, and the glass card grows out of the dark. F-B adds jump-cut reframes and two colour-burn glitch cuts.

**Copy these 5 things** (they make it this style):
1. **Duet captions at chest:** big script content words and openers + small geometric-sans function words + one bold punch word, 1–8 words, a 2–3 line block with tight leading, revealed word by word (§5.3, CS-1).
2. **Numbered glass markers:** a glass diamond (F-A) or glass tile (F-B) pops in on every ordinal word and the row returns as the recap (§7.2, P-DIAMOND-MARKER, P-DIAMOND-ROW, P-NUM-TILE-ROW).
3. **Glass cards with a rim glow:** the full-screen tutorial card, the chest window with leader labels, the link card (§8, P-TUTORIAL-CARD, P-PREVIEW-WINDOW, P-LINK-CARD).
4. **One studio colour per reel:** the set's hue tints every diamond, rim and glow (§4.3, TH-violet / TH-blue / TH-teal / TH-neon).
5. **The face moves into the graphics:** it shrinks into a floating card on a pale world, or sits in an orbit bubble, instead of being covered (§3.3 G-1, G-5).

### Creator directives (style laws)
| # | Directive | Where it lives |
|---|---|---|
| D1 | **Every spoken word is captioned in two voices.** Big script for openers and content words, small geometric sans for function words, one bold, biggest word for the point. Captions are the strongest element on screen | §5.3 CS-1, H9 |
| D2 | **Teach by showing.** Every step, tool, setting or result appears as the thing itself (a chest window, a glass card or a full-screen tutorial card) on the word that names it | §8.4, H5 |
| D3 | **Premium glass in one studio colour.** Every graphic is glass with a rim glow in the reel's studio hue. One hue family per reel; gold/green/red only for their fixed meanings | §4, H15, N4 |
| D4 | **Numbered glass markers carry the structure.** Every item gets the same diamond (F-A) or tile (F-B); the row returns as a recap | §7.2, H8 |
| D5 | **Calm, eased motion with a breathing camera.** Elements blur-in / glide / blur-out over 6–16 f; the camera lands (Z-0) on every face shot, pushes on markers (Z-1) and pulls back (Z-2), all expo-out, never a punch on F-A. World switches are hard cuts with a push before and a grow/settle after | §9, §10.2, N1 |
| D6 | **The face goes into the graphics, never under them.** Shrink-to-card, orbit bubble, recursion window; the face box is never covered | §3.3, H6 |
| D7 | **Face high, graphics at the chest.** The head owns the top 40% of the frame; captions, markers and windows live at y 960–1500; full-screen worlds take over briefly | §3.5 |
| D8 | **Proof is the creator's own.** Real results, posters, screenshots, their long video; otherwise a built example | §12, H13 |

Buyer directives BD1… (VAR) may only make the style stricter or more specific. Buyer never-list items are BN1….

### Quick index
| § | What | Status |
|---|---|---|
| §0 | Style profile | ON |
| §1 | Procedure | ON |
| §2 | Hard rules, exceptions | ON |
| §3 | Worlds, layouts, stage moves, safe zones | ON |
| §4 | Colour, theme packs | ON |
| §5 | Type and the duet caption system | ON |
| §6 | Hook system | ON |
| §7 | Structure and cadence | ON |
| §8 | Visual system: 43 patterns | ON |
| §9 | Transitions | ON |
| §10 | Motion, camera, layers, finishing | ON |
| §11 | Sound contract | ON |
| §12 | Footage, shot list, fallbacks, inserts | ON |
| §13 | Output contract | ON |
| §14 | Worked examples (F-A ×2, F-B ×1) | ON |
| §15 | QA checklist | ON |
| §16–§21 | Chrome, running state, data, citations, dialogue, canvas camera | OFF |
| §22 | Ink & annotation layer | ON |
| §23–§24 | Continuity, series | OFF |
| §25 | Brand, link cards, end cards | ON |
| Parts C–F, App. A–B | Exceptions, personalisation, changes, IDs, headline bank, evidence | ON |

Formats: **F-A Tutorial explainer** (default) · **F-B Course sales**.

---

## §0 Style profile `[REQ]`

```yaml
profile:                         # mirrored in tokens.json -> profile
  source_type: talking_head
  presenter: {presence: host, share: [45, 85], max_absence_s: 6.5}      # F-B: share [40, 80], max_absence_s 11
  spine: talking_head
  captions: {mode: full, role: primary, mute_policy: mute_safe}
  graphics: support
  duration: {class: short, target_s: [40, 60]}                          # F-B: {class: long, target_s: [90, 125]}
  language: {speech: en, captions: {lang: en, script: Latn, transform: verbatim}, on_screen: en, post_title: en,
             supported: [[en, en, Latn], [hinglish, hinglish, Latn], [hi, hi, Deva]]}
  numbers: {grouping: international, currency: "$", compact: k_m_b, units: metric, decimals: 0, compact_decimals: 1}
  tone: {energy: calm, comedy: off, comedy_max: off}
  themes: {policy: per_reel, packs: [TH-violet, TH-blue, TH-teal, TH-neon], default: TH-violet}   # F-B default TH-neon
  formats: {list: [F-A, F-B], default: F-A}
  footage_dependency: medium
  cta: {devices: [cross_promo, comment_keyword, dm, link_bio], placement: end, chosen: cross_promo}  # F-B chosen: comment_keyword
  modules: {chrome: false, running_state: false, anchors: false, data_figures: false, citations: false,
            dialogue: false, canvas_camera: false, ink: true, continuity: false, series: false, brand: true}
```

Why each switch has this value:
- **source_type talking_head:** all five references are one seated creator on a fixed camera (v01–v05).
- **presence host 45–85%:** face on screen 45–80% (v05 45%, v02 55%, v01 60%, v04 80%); tutorial and pale-world spans take the rest. Longest absence 6.5 s in F-A (v01 tutorial cards 0:11–0:17), 11 s in F-B (v05 chrome/void run 0:38.8–0:49.5).
- **spine talking_head:** the take is continuous (v03/v04 have 1 detected cut in ~50 s); graphics are inserted on it.
- **captions full / primary / mute_safe:** text is on screen 80–90% of runtime and the duet caption is the most designed element in every frame (v01 @0:00–0:03, v04 @0:00–0:17).
- **graphics support:** graphics fill 15–55% of runtime (v04 15%, v01 30%, v02 40%, v05 55%); they illustrate, the voice argues.
- **duration short 40–60 s (F-A), long 90–125 s (F-B):** v01–v04 run 46–53 s; the course pitch v05 runs 122 s.
- **language en (unverified):** no transcripts existed; captions are English. Hinglish is supported in Latin script only (the script font has no Devanagari).
- **numbers international, $:** the reference prices and income are in dollars (v05 @0:10, @0:34). BV-06 switches to Indian grouping + ₹ when the buyer picks a Hinglish combination.
- **tone calm, comedy off:** "calm-premium"; no gags, stickers or meme cues anywhere in the evidence.
- **themes per_reel:** the set colour changes per video (v01/v04 violet, v02 blue, v03 teal, v05 neon) and the graphics follow it (diamonds violet in v01/v04, cyan in v03).
- **formats F-A / F-B:** teaching reels (v01, v03, v04, v02) vs the course sales video (v05); they share the chest captions, the glass language and the numbered markers.
- **footage_dependency medium:** the style works on the talking head alone, but the tutorial cards, poster rows and proof are at their best with the creator's own exports and screenshots (fallbacks in §12.3).
- **cta:** a link card to the long video (v01 @0:00–0:04, @0:44–0:49; v03 @0:49–0:52) and "DM or comment" a keyword (v05 @1:54–2:00).
- **modules ink + brand:** leader lines and labels (v01 @0:39–0:42, v03 @0:07–0:17); link and video cards (§25). No chrome slots, data figures or canvas camera.

---

## §1 Procedure (follow in order) `[REQ] [DNA]`

1. **P1 Inventory.** `ffprobe` every input; conform to 30 fps CFR (`veos conform`); register every supplied file with `veos asset add --origin creator`. Note which shots of §12.2 exist (SH-1…SH-6).
2. **P1b Studio colour pick (this style's first craft step).** Read frame 15 of the take. Sample the backdrop (the region above the shoulders and beside the head, excluding the face box). Pick the theme pack whose `primary` hue is nearest in OKLCH hue: violet/magenta/purple → TH-violet; blue → TH-blue; teal/cyan/green-grey → TH-teal; dark room with neon bars or RGB practicals → TH-neon. A neutral or white set → the buyer's BV-02 colour if set, else TH-violet (F-A) / TH-neon (F-B). Write it to the reel header `theme`.
3. **P2 Prepare.** Run `veos matte` only when the plan uses P-POSTER-ROW behind the head (the matte puts the row behind the hair, v01 @0:01). Everything else needs no matte.
4. **P3 Transcribe** with word timestamps. Apply `language.captions.transform` (verbatim for en; romanised verbatim for hinglish; translate for hinglish → en). Fix brand and tool spellings against the glossary.
5. **P4 Segment** into `HOOK`, `PROMISE` (the "here are N…" line), `ITEM-n`, `RECAP`, `CTA` (F-A) or `HOOK`, `WHAT`, `PROOF`, `INSIDE-n`, `GUARANTEE`, `CTA` (F-B). Mark jump-cut points on word boundaries.
6. **P5 Classify** every sentence with a line type (§8.4) and its trigger word.
7. **P5b Type-voice pass (this style's second craft step).** Read every caption chunk the engine will build (`veos captions build`, then `work/captions.json`). Check per chunk: exactly one tier-2 word at most; tier-2 sits on a number, the topic noun or a name; no chunk is all script; no number or brand is in script. Fix with `captions.overrides` (`{i, emph: true|false}`, `{i, break: before|after}`), never by hand-written cards.
8. **P6 Tone-tag** every sentence: `hype` (hook claims), `awe` (reveals, results), `explain` (steps), `win` (payoff, results achieved), `warn` (the mistake), `cta`.
9. **P7 Hook plan.** Pick the archetype (§6.2 default HA-05; alternates §6.3). Write **3 hook variants**, each with its promise line, proof element and the stopper tests (§6.1). Pick the hook pair from §6.4 (append a new row for this topic).
10. **P8 Show-pairing (this style's third craft step).** For every item: choose the ritual R-A / R-B / R-C (§7.3), the pattern per line (§8.4), and the exact content inside each window or card (which recording, which still, which bullets, which leader labels). List every third-party moment (§12.5).
11. **P9 Beat sheet** (§13): one beat per trigger word; meet the cadence (§7.6).
12. **P10 SFX ledger** (from the bundled pack, §11) and the transition map (§9).
13. **P11 Assets.** Build or collect them; resolve fallbacks (§12.3) and record which ones were used. **P11b Link card:** collect the long video's thumbnail and title (SH-4) or build FB-4.
14. **P12 Checkpoint** (§13.5), then **wait for approval.**
15. **P13 Build** act by act; `veos scenes-meta` → `veos measure` → `veos validate`; preview; QA (§15, at most 3 passes); render.

---

## §2 Hard rules `[REQ] [DNA]`

### 2.1 Editing rules (every style)
The nine editing rules in `playbooks/_global/GLOBAL-RULES.md` apply. They are directions, not limits: smooth, seamless motion; nothing overlaps by accident; keep the face clear (behind the speaker is fair game, text included); readable at a glance; one idea at a time; show what's being said; never fake facts; pace like the style, not like a timer; the style decides the look.
- **Facts the engine checks:** accidental overlaps, jumps, the face covered, unreadable text, numbers and quotes that don't match what was said, the promised count. Every count, timing and budget this playbook gives is direction for the edit, not a limit.
- **Retired (8 Oct 2026), whatever this playbook says below:** no REPRESENTATIONAL or example labels on made-up cards, no credit lines, no flash limit (flash as often as this style calls for; any "NC-11" cap below no longer applies), and text may sit behind the speaker without an exception.

### 2.2 Declared exceptions
| E-id | Style limit (≤ registry) | DNA reason | Evidence |
|---|---|---|---|
| **E3 Quiet type** | Labels 28–39 px only with `redundant: true` (leader labels, link-card meta); card-layout subtitles (CS-2) 44 px, weight ≥ 500, 1 line, ≤ 32 chars, contrast ≥ 7:1 (ink on the pale world: 17.2:1). Display stays ≥ 40 px. | The leader-line labels and the under-card caption are deliberately small and quiet; that small/large contrast is what makes the glass feel premium | v01 @0:12–0:17 bullet text, v01 @0:39–0:42 "Edges of the screen", v03 @0:07–0:17 "Sans Font Coolvetica", v03 @0:01–0:03 "more than two years to build", v02 @0:01–0:03 "Can't create a viral edit" |
| **E4 Ambient field** | P-FALLING-ICONS only: ≤ 24 items, each ≤ 6% of the frame, no text, ≤ 60 px/s, dimmed ≥ 40% under text, ≤ 5 s per occurrence, F-B only | The chrome-title void is alive with falling icon tiles and bills behind the title | v05 @0:39–0:49 |

### 2.3 Style MUST rules
- **H1 Frame 0** (HA-05): the presenter is full frame (L-full) and **lands**: Z-0 land-settle 1.22 → 1.0 over 45 f from t 0 (`land`, measured 1.20–1.25 settling in 40–50 f), with a 3 f defocus on f0–f2 (camera `blur`, as v01; v04's f0 is one black frame); the promise lockup's first word blurs in at chest by 0.3 s. The promise's first line is readable by 0.7 s. check: V-F0
- **H2 Cadence:** 4–10 weighted state changes per 10 s in the body (F-B 3.5–9), ≥ 6 in 0–3 s, no gap > 2.0 s (hook 1.0 s) between SCs of weight ≥ 1, nothing static > 2.5 s. Caption chunk swaps weigh 1.0 (captions are primary). check: V-CADENCE
- **H3 Proof by 2.5 s:** a proof element lands by 2.5 s: the poster row, the link card, stat cards, the rating widget, the recursion window, a chrome title (F-B) or the shrink-to-card collage. check: review (V-F0 for HA-02)
- **H4 Headline limits:** the F-B chrome title is ≤ 4 words on ≤ 2 lines, reads in ≤ 1.2 s, holds ≥ 30 f after landing, exits with T-10. The F-A promise lockup is ≤ 12 words on ≤ 3 lines per chunk. check: V-TITLE
- **H5 On the word:** every marker, window, card, label and bullet starts 2 f before its trigger word and is fully settled within +5 f. Diamonds land on the ordinal word ("first", "two", "number three"). check: V-ONWORD
- **H6 Face:** nothing is drawn over the face box (eyebrows to chin, ear to ear). Duet captions start ≥ 40 px below the chin (anchor `chest`). Top-band graphics either sit behind the head (`behind: true`, matte) or end ≥ 40 px above the head top. check: V-FACE
- **H7 Presence:** face visible 45–85% of runtime (F-B 40–80%); longest absence 6.5 s (F-B 11 s). Every absence ends with the face back in L-full or in a card. check: V-PRESENCE
- **H8 Promise integrity:** the number of diamonds/tiles equals the number of items spoken; the recap row shows all of them; "the full tutorial is on YouTube" is followed by the link or video card; the CTA keyword is on screen ≥ 1.5 s. check: V-PROMISE
- **H9 Captions:** every spoken word is captioned (CS-1 on L-full, CS-2 under a card, CS-3 in F-B), except inside the tutorial world, under z8 title scenes and under the CTA card. Sync: shown ≤ 0.15 s before the word. ≤ 1 tier-2 word per chunk, ≤ 0.35 per second. Brands spelled exactly. check: V-CAPTION
- **H10 Layouts:** layout shares and run lengths per §3.2 (L-tutorial runs ≤ 6.5 s, L-card-pale ≤ 6.0 s, L-pip-orbit ≤ 3.0 s, L-graphic ≤ 11 s; L-full runs ≥ 1.5 s). check: V-LAYOUT
- **H11 Camera:** only Z-0 land-settle (and its cut-back form Z-0b), Z-1 marker-push, Z-2 pull-out and Z-3 push-drift (§10.2), all ≥ 15 f; Z-1…Z-3 ≤ 0.12 scale, Z-0 / Z-0b are landings (`land`: start on f0 or a cut, settle to 1.0, ≤ 1.5×, exempt under slow_push); Z-0 on every face entry (f0 and each cut back from a graphic world); Z-1 on the count word and each marker; never two moves within 0.4 s; never the same move twice in a row. F-B jump cuts may also reframe (T-14). check: V-CAMERA
- **H12 Dead air:** at most 1 gap ≥ 150 ms per 15 s; jump cuts on word boundaries ±1 f, hidden under a caption blur swap or a world switch; never a visible jump in the face mid-sentence. check: review
- **H13 Truth:** every count, view number, income figure, rating claim and testimonial is the creator's own real figure or verbatim text; any F-B earnings figure carries a `TC-legal` "Results vary" line (24 px) while it shows. check: V-DATA, V-NUMFMT, V-INSERTS
- **H14 Glass budget:** ≤ 2 glass elements plus the captions at once; ≤ 1 element with `backdrop-filter` per frame; ≤ 30 ms per frame. check: review (`veos measure` ms/frame)
- **H15 Hues:** ≤ 3 bright hues per frame: the studio `primary`, its `accent` glow, and at most one of gold / good / bad. check: V-HUES
- **H16 Audio:** −14 LUFS integrated, true peak ≤ −1.5 dBTP, bed ≥ 18 dB under the voice (we use 20), hard end ≤ 6 f after the last word (NC-8). check: review (qa)
- **H17 Determinism:** every frame is a pure function of its index; drifts, floats and falling icons use `ctx.rng(seed)` / `rngStable`. check: review

### 2.4 NEVER
- **N1** Crash zooms, shakes, rotation snaps, whip pans, speed ramps on the face; in F-A any punch-in (camera moves are eased, ≥ 15 f). Dissolves or blur-throughs between worlds (the source always cuts).
- **N2** Comedy: meme cues, stickers, stamps, marker roasts, freeze-frame gags.
- **N3** Coloured caption words. Emphasis is size, weight and family only (tier 2). No caption boxes or pills on L-full.
- **N4** A second studio hue family in one reel, or a glow that fights the set (a teal glow on a violet set).
- **N5** Flat boxes without a rim or glow; hard offset shadows; sticker outlines; thick ink strokes.
- **N6** The script font on numbers, brand names or the tier-2 word; script under 70 px.
- **N7** Captions above the chin or across the face; graphics over the face box.
- **N8** Invented view counts, ratings, income, testimonials or screenshots; look-alikes of YouTube, Instagram or app chrome presented as real (the link card is a generic glass card with the creator's own thumbnail and title).
- **N9** A raw full-bleed screen recording; recordings always sit in a glass frame (tutorial card, chest window, screen panel).
- **N10** White text on the pale world (1.1:1); a caption over a busy poster row or screen wall without its scrim.
- **N11** Stock B-roll, AI stock scenes, emoji in captions, platform or product logos (use `fx.icon` glyphs and type).
- **N12** Transitions outside T-01…T-14 (§9); glitch or burn effects except T-12 in F-B (≤ 2 per reel); RGB split, lens-flare PNGs.

---

## §3 Worlds, layouts, stage moves, safe zones `[REQ] [DNA; coordinates TUNE ±5%]`

### 3.1 Worlds
| ID | Kind | Look (default TH-violet; packs recolour) | Carries | Enter / exit |
|---|---|---|---|---|
| **W-studio** | footage | The creator's coloured-light set, untouched | The talk, duet captions, markers, chest windows, checklist cards, link card | Default; back from other worlds by T-05 hard cut + Z-0 or T-03 grow |
| **W-tutorial** | stage | Linear 180° `#030F22` (navy) → `#33005A` (pack bottom; sampled v01 @0:14: top `#020F20`, bottom `#310056`); a `primary` glow 640 px at 14–18% at y 1700 drifting ±16/10 px; noise 0.03 | P-TUTORIAL-CARD: the step's title row, the glass card with the result, sparkle bullets, the footer line | T-04 push-cut in (card grows); T-05 hard cut out on a sentence start |
| **W-pale** | canvas (light) | Radial `#F8FBFE` → `#EAF3FA` → `#DCE9F5` centred (540, 900); the pack `accent` glow 520 px at 22% | The face card (P-SHRINK-TO-CARD), P-CARD-CAROUSEL, P-STATCARDS, P-SEARCH-BAR, P-PROFILE-TILE, P-COURSE-STACK, P-ORBIT-FACE | With T-02 shrink-to-card (8 f fade under the morph); out with T-03 grow or T-05 cut |
| **W-void** | void | `#05070F` with the `accent` glow 700 px at 16% drifting; noise 0.04 | F-B chrome titles, glass slabs, falling icons, neon outline figures, the screen wall, style cards | T-05 cut (or T-12 in F-B); out with T-05 |
| **W-grid** | canvas (light) | `#E8E9ED` with a 96 px grid of `#C9CBD3` lines at 70% | F-B P-TRACKED-FIGURE (the money/result figure) | T-05 cut in and out |
| **W-flat** | card-world | Flat pack colour (`#33005A` violet, `#0F55C8` blue, `#0F4A63` teal, `#1B1660` neon) | P-COLOUR-FLASH-WORD only (0.6–1.2 s) | T-08 hard cut in and out |

Switching worlds is itself a state change; land every switch on a sentence start or an ordinal word.

### 3.2 Layout library
| ID | Engine | Presenter rect | Graphic area | Caption | Share F-A | Share F-B |
|---|---|---|---|---|---|---|
| **L-full** | `full` | full frame | chest and lower band y 960–1500, top band y 140–(head top − 40) | CS-1 / CS-3, anchor `chest` (face bottom + 220, fallback cy 1120) | 45–85% | 40–80% |
| **L-card-pale** | `card` | x 312, y 520, w 456, h 811, radius 26, crop 9:16, 2 px white border, glow `accent` 44 px, shadow 0.22 | everything outside the card on W-pale | CS-2 `below_card` +34 px (≈ y 1365–1410), ink | 0–15% | 0–15% |
| **L-tutorial** | `hidden` | none | x 64–1016, y 300–1500 (W-tutorial) | none (hidden: bullets carry the words) | 0–40% | — |
| **L-pip-orbit** | `pip` | circle Ø 300 at (540, 880), 6 px `accent` ring, shadow 0.35 | the orbit ellipse around it, W-pale | CS-2 at cy 1380 | 0–6% | — |
| **L-graphic** | `hidden` | none | x 64–1016, y 160–1500 (W-void / W-grid) | CS-3 at cy 1420 when the voice runs over it | — | 0–45% |
| **L-dim** | `full` + `dim {blur 8, luma −0.25}` | full frame, softened | the CTA band y 1200–1480 | CS-3 chest | — | 0–10% (CTA only) |

**Layout schedule:** L-full runs ≥ 1.5 s. L-tutorial ≤ 6.5 s per run, L-card-pale ≤ 6.0 s, L-pip-orbit ≤ 3.0 s, L-graphic ≤ 11 s. Switch layouts on a sentence start, an ordinal word or "look at" / "this is" (the word that introduces the thing shown).

### 3.3 Stage moves
| ID | Move | Recipe (30 fps) | Use |
|---|---|---|---|
| **G-1** | **Shrink-to-card** (T-02) | L-full → L-card-pale via `shrink-to-card`, 16 f, ease `card`; the world cross-fades W-studio → W-pale over the first 8 f; the card's `accent` glow rises 0 → 44 px over f6–f16; captions switch CS-1 → CS-2 after the morph | The hook's "proof collage" (v02 @0:00.6), the carousel, stat cards, "look at these" moments |
| **G-2** | **Grow-from-card** (T-03) | L-card-pale → L-full via `grow-from-card`, 12 f; W-pale fades out over the last 6 f | Back to the face after a card span when the sentence continues |
| **G-3** | **Push-cut to tutorial** (T-04) | Z-3 push-drift on the face for the 15–25 f before the cut (measured 1.0 → 1.09, v01 @0:10.3–0:11.0); L-full → L-tutorial via `cut`; W-tutorial is on from frame 1; the glass card grows from 15% at frame centre to full in 20 f (3% overshoot) while the title row (diamond + title) fades in 10 f (v01 @0:11.03, @0:24.13). Variant: the card lands oversized (≈ 2×, filling the frame) and settles into place in 15–18 f (v01 @0:32.57, @0:38.53) | Into a tutorial card on the step's title words |
| **G-4** | **Hard cut back + land** (T-05) | In the last ~30 f the tutorial world eases out to 0.94 (accelerating, v01 @0:17.1–0:18.07); L-tutorial / L-graphic → L-full via `cut` on the first word of the next sentence; Z-0 land-settle on the face from that frame | Out of tutorial and void worlds (v01 @0:18.07, @0:30.3, @0:36.47) |
| **G-5** | **Orbit bubble** (T-09) | L-full → L-pip-orbit via `pip-shrink` 12 f (the frame rounds into a squircle, then a circle, v02 @0:33.77–0:34.2); the orbit tiles burst outward from behind the bubble to the frame edges in 6–8 f; back via `pip-grow` 10 f | "All the tools / options / courses out there" (v02 @0:34–0:36) |
| **G-6** | **Recursion open** | Inside L-full: a dashed 2 px `paper` rect draws on the chest (8 f), the creator's earlier clip fades in inside it (6 f), then G-1 shrinks the whole frame into a card at 0.5 s | HA-18 hook (v03 @0:00–0:01) |
| **G-7** | **Dim for the CTA** (T-11) | L-full → L-dim via `dim`, 10 f | the keyword CTA in both formats (F-B v05 @1:54; F-A `comment_keyword`, P-KEYWORD-GLASS); L-dim is in both formats' layout lists |

### 3.4 Layout diagrams
**L-full with a chest window (F-A body, v03 @0:07–0:17)**
```
┌─────────────────────────┐ 0
│   (IG top UI, clear)    │ ← y 0–110
│                         │
│        ( head )         │ ← head top y 180–360, chin y 700–860
│   label ╲               │ ← leader label y 820–880, x 700–950 (E3 30 px)
│ ╭───────────────────╮   │ ← chest window x 216–864, y 980–1300, radius 14, accent rim glow
│ │  the thing shown  │   │
│ ╰───────────────────╯   │
│  ✦ bullet one           │ ← sparkle bullets x 240, y 1340 / 1392 / 1444, 40 px
│  ✦ bullet two           │
└─────────────────────────┘ 1500 (meaning text ends) … 1920
```
While a chest window is up, the duet caption is hidden (the window is z8) or the window waits for the chunk to end; never both at the chest.

**L-full with duet caption + marker (F-A, v01 @0:10, v04 @0:06)**
```
│        ( head )         │ ← chin ≈ y 760
│                         │
│    This editing style   │ ← CS-1 block top = chin + 220 (≈ y 980), 1–3 lines, ≤ 900 px wide
│      is taking over     │
│  ◆1   First is the …    │ ← P-DIAMOND-MARKER: diamond centre (250, 1120), title x 360 (z8 hides captions)
│      ◆1  ◆2  ◆3         │ ← P-DIAMOND-ROW centre y 1380, pitch 134 px
│ ╭ link card ──────────╮ │ ← P-LINK-CARD x 150–930, y 1250–1480 (hook and CTA only)
└─────────────────────────┘
```

**L-tutorial (F-A step, v01 @0:11–0:17)**
```
┌─────────────────────────┐
│ ◆1 Creating the backgr… │ ← title row: diamond Ø-diag 170 at (150, 436), title x 250, 56 px
│ ╭─────────╮ ✦ bullet    │ ← glass card x 136–576, y 540–1340, radius 22; bullets x 616, from y 600, pitch 64
│ │ result  │ ✦ bullet    │
│ │ (still/ │ ✦ bullet    │
│ │  clip)  │ ✦ bullet    │
│ ╰─────────╯             │
│  The full tutorial is … │ ← footer TC-legal 30 px, centred y 1470
└─────────────────────────┘
```

**L-card-pale (hook proof collage, v02 @0:01–0:03)**
```
┌─────────────────────────┐ W-pale
│ ▢635K        ▢331K      │ ← stat cards 300×400, dark glass, drifting (real counts only)
│      ╭─────────╮        │
│      │  face   │        │ ← card x 312–768, y 520–1331, accent glow 44 px
│      │  card   │        │
│      ╰─────────╯        │
│  Can't create a viral…  │ ← CS-2, ink, 44 px, y ≈ 1365–1410
│ ▢325K        ▢400K      │ ← lower stat cards end ≤ y 1500
└─────────────────────────┘
```

**F-B chrome title on the void (v05 @0:39–0:41)**
```
┌─────────────────────────┐ W-void, falling icon tiles (E4) behind
│                         │
│      ULTIMATE           │ ← chrome title, caps 900 italic 150 px, 2 lines, centre y 760–1060
│      PROGRAM            │   (flare sweeps x 200 → 880)
│ ╭ MASTER THE SKILL ───╮ │ ← glass slab 1: x 240–840, y 1120–1270
│ ╭ RESULT IN 30 DAYS ──╮ │ ← glass slab 2: x 240–840, y 1300–1450
└─────────────────────────┘
```

### 3.5 Safe zones and bands
- **Meaning text** stays in x 64–1016, y 110–1500 (NC-5: never in y > 1540, never at x > 970 for y 900–1540).
- **Caption band:** CS-1/CS-3 block top = chin + 220 px (typically y 980–1230); clamped inside y 110–1500. CS-2 sits 34 px under the card.
- **Top band** (y 140 → head top − 40): P-POSTER-ROW (without matte) only. With the matte, the row may run y 200–720 behind the head.
- **Chest band** (y 960–1300): chest windows, checklist card, markers, duo icons, video card.
- **Lower band** (y 1300–1500): sparkle bullets under a window, the diamond row (cy 1380), the rating widget, the link card, glass slabs.
- **Bottom** (y > 1500): only footage and decorative glow; never text.

### 3.6 Presenter rules
- Share 45–85% (F-B 40–80%); longest absence 6.5 s (F-B 11 s).
- Returns: from the tutorial/void worlds by a hard cut on a sentence start + Z-0 land (G-4); from a card by G-2 grow.
- Framing the style assumes: head top y 180–360, chin y 700–860, face centre x 420–660 (a seated chest-up shot). F-A never reframes the face beyond the Z-0…Z-3 moves; F-B jump cuts alternate wide ↔ tight (T-14).
- The creator counts on his fingers on ordinal words (v04 @0:06.1, @0:20.8; v01 @0:18.2): the diamond emerges from that hand (P-DIAMOND-MARKER). Ask for it in the shot brief.
- Behind the head: only P-POSTER-ROW (no text in it, so no E1). Nothing with text ever goes behind the head.

---

## §4 Colour, theme packs `[REQ] [meanings DNA; brandable hex VAR; theme hues TUNE]`

### 4.1 Role palette
| Role | Default (TH-violet) | One job | Text on it | Contrast | Brandable |
|---|---|---|---|---|---|
| `primary` | `#8018D0` Studio violet (sampled: v01 @0:09 diamonds `#7D1ACF`, @0:14 tutorial diamond `#8314D2`) | Glass fill of diamonds and tiles, window rim, active marker, chip fill | `paper` (numerals ≥ 56 px only) | 7.1:1 | yes (BV-02, first colour) |
| `accent` | `#B46CFF` Glow lavender | Outer glow of cards and windows, sparkle bullets, leader-line dots, orbit ring, filled rating stars (as `primary`-light `#9F3DD5` core) | `ink` | 6.1:1 | yes (BV-02, second colour) |
| `good` | `#39FF7A` Money green | Money, guarantee, "yes", the F-B keyword glow | `ink` | 14.5:1 | no (fixed) |
| `bad` | `#FF5C7A` Rose | The viewer's current wrong state (a low rating, a crossed-out habit), one element at a time | `ink` | 6.5:1 | no (fixed) |
| `gold` | `#F7D15B` Star gold | "5/5", a won state (not the rating stars: those are violet in the source, v04 @0:03) | `ink` | 13.1:1 | no (fixed) |
| `ink` | `#0B0D1A` | Text on the pale world and light cards | — | 17.2:1 on canvas | TUNE |
| `paper` | `#FFFFFF` | Caption text, glass text, rims | — | — | TUNE |
| `canvas` | `#EAF3FA` | W-pale | — | — | TUNE |
| `navy` / `night` / `grid` | `#030F22` (sampled v01 @0:14 top) / `#05070F` / `#C9CBD3` | W-tutorial top / W-void / W-grid lines | — | — | TUNE |

Brand colours for this copy: `primary` = {{BV-02.primary|#8018D0}}, `accent` = {{BV-02.accent|#B46CFF}}.

Gradients: `chrome` `#FFFFFF → #DCEBFF → #8FB7FF → #3C5FB8 → #E8F2FF` (the chrome title ramp, light-dark-light); `glass_rim` white 85% → 10% → 45% (the 2 px rim, top-left to bottom-right); `money` `#B9FFD3 → #39FF7A → #12B24E` (F-B money figure glow only).

### 4.2 Meanings
- **The studio colour (`primary` + `accent`) = this reel's brand surface.** Every glass element carries it; it says "this is part of the lesson".
- **White** = what is said (captions) and what is shown (glass text).
- **Gold** = earned (result achieved). Rating stars stay in the studio colour (violet fill + glow, outline-only when empty), as in v04 @0:00–0:03. **Green** = money and guarantee (F-B). **Rose** = the wrong state, rarely.
- The axis is **dim → lit**, not red → green: a wrong state is drawn dim/grey (an empty star, an inactive tile), the right state lit (gold stars, the active tile glowing, the stars filling violet). Rose is a last resort.
- Brand colours appear only on the creator's own brand elements (their logo, their course art).

### 4.3 Theme packs (per reel)
| Pack | `primary` | `accent` | W-tutorial bottom | W-flat | When (P1b rule) |
|---|---|---|---|---|---|
| **TH-violet** | `#8018D0` | `#B46CFF` | `#33005A` | `#33005A` | Violet / purple / magenta set; neutral set (F-A default) (v01, v04) |
| **TH-blue** | `#1E6BFF` | `#5FB4FF` | `#0E3E9E` | `#0F55C8` | Blue set (v02) |
| **TH-teal** | `#2391CC` | `#46D3FF` | `#0F4A63` | `#0F4A63` | Teal / cyan / cool grey set, plants under cool light (v03) |
| **TH-neon** | `#3B2BB0` | `#4D8BFF` | `#1B1660` | `#1B1660` | Dark room with neon bars / RGB practicals; F-B default (v05) |

- One pack per reel. Never switch packs mid-reel.
- All packs pass contrast: `primary` vs paper ≥ 3.0:1 for numerals ≥ 56 px (teal is the lowest at 3.5:1; numerals on teal tiles are 800–900 weight); `accent` vs ink ≥ 5.9:1.
- If the buyer sets BV-02, their two colours replace every pack's `primary` / `accent` (policy per_reel), so the set should then be lit in their colour.

### 4.4 Grades
OFF: the footage is never graded or tinted; the set colour is the grade (no LUTs, no grade events, no clip treatments).

### 4.5 Rules
- ≤ 3 bright hues per frame (`max_bright_per_frame` 3): `primary`, `accent`, plus one of gold / good / bad.
- On W-pale, all text is `ink` (or `primary` at ≥ 96 px); never white.
- On footage, glass text is `paper` with the card's own dark tint behind it (glass fill ≥ 55% opacity under text).
- Glows are always the pack `accent` (or `good` for the F-B keyword and money figure); never a second hue family.

---

## §5 Type and the duet caption system `[REQ]`

### 5.1 Font map
| Slot | Family | Weights | Font class (the TUNE boundary) | Used for |
|---|---|---|---|---|
| `geo` | **Jost** | 500, 700 | geometric sans with a single-storey a/g (Futura-like) | **CS-1 duet sans**: tier 0 (500) and tier 2 (700). Audit: v01/v04 captions use a Futura-class face ("taking", "at", "what" have single-storey a/g), not a grotesk |
| `display` | **Inter Tight** | 700–900 | neo-grotesk sans 600–900 | Diamond numerals, marker titles, stat counts, outline word |
| `body` | **Inter Tight** | 400–600 | neo-grotesk sans 400–700 | Bullets, labels, card text |
| `script` | **Pinyon Script** | 400 | formal copperplate script (Edwardian-like) | Tier-1 caption words and sentence openers, script tags under caps words ("Style", "Month", "Basics") |
| `caps` | **Montserrat** (true italic) | 400–900 | geometric sans with a true italic | F-B italic caps captions (CS-3), chrome title, glass slabs, number tiles, CTA keyword |
| `numeric` | **Inter Tight** | 700–900 | neo-grotesk sans 700–900 | Counts, tracked money figures (F-B uses `caps` for the hero figure) |

All are bundled OFL fonts. Logos and wordmarks are image assets, never fonts.

### 5.2 Headline element
**F-A: the promise lockup (P-PROMISE-DUET), lifetime `hook`.** It is the hook's first sentence set in the CS-1 duet skin, built word by word at chest (§8.3). ≤ 12 words, ≤ 3 lines per chunk, readable from f0, holds until its last word + 0.25 s, then hands over to the auto-captions with a 5 f blur swap.

**F-B: the chrome title (P-CHROME-TITLE), kind `lockup`, lifetime `hook` (and once more as the product reveal mid-reel).**
| Property | Spec |
|---|---|
| Text | The product name, ≤ 4 words, ≤ 2 lines (≤ 2 words per line), caps |
| Type | Montserrat 900 italic, 150 px (120–170 by length), tracking −1%, line height 0.92 |
| Fill | `chrome` gradient top → bottom (`background-clip: text`), a 2 px inner highlight line at 46% height |
| Extrusion | 6 stacked text shadows `0 1px … 0 6px #1B2A5A` + `0 10px 24px rgba(0,0,0,.55)` |
| Glow | `0 0 30px` pack `accent` at 60% |
| Flare | A 4-point star (radial gradient 260 px, white core) + two 900×4 px streaks, sweeping x 200 → 880 across the title from f6 of the land, 18 f, peak opacity 0.9 at the centre |
| Land (f0 of the title) | Scale 0.85 → 1.0 and blur 12 → 0 px over 14 f (expo-out); letter-spacing −0.06 → −0.01 em |
| Placement | Hook: over the footage at chest, centre y 1160–1300 (z8, captions hidden). Mid-reel: on W-void, centre y 760–1060 |
| Hold | ≥ 30 f after landing, ≤ 2.5 s |
| Exit (T-10) | Fly-through: scale 1.0 → 2.6 (expo-in) while travelling down 700 px, vertical smear blur 0 → 24 px, opacity → 0 over the last 3 f; 8 f total (v05 @0:01.63–0:01.92). Mid-reel on the void the camera instead dollies through the title into the next one (v05 @0:45–0:46) |
| **3D build (default when WebGL is available)** | `VEOS.fx.three` text, traced from the `caps` slot (Montserrat 900 italic): a chrome face (`material: "chrome"`: the measured bright white → ice-blue polished face), a deep blue extrusion, a lavender halo; the land and the T-10 fly-through as `keys`; the flare stays a 2D z11 light pass over it. Mid-reel on W-void, one 3D scene holds the current title and the next one deeper in z, and the 3D camera dollies through the first into the second (v05 @0:45–0:46, the "camera orbit / dolly through titles"). Recipe below. One 3D scene on screen at a time (≈ 50–85 ms per frame) |
| **Flat fallback** | When the title must run inside a perf budget (another heavy scene on screen) or the buyer turns it off: `#FFFFFF → #BFD6FF` gradient fill, the glow only, no extrusion, no flare; same land and exit |

```js
// P-CHROME-TITLE, 3D: land 0.85 -> 1.0 in 14 f, hold, T-10 fly-through (x2.6 toward the lens and down) in the last 8 f
function chromeTitle3D(id, t_in, t_out, text, cy /* 1160-1300 hook, 760-1060 void */) { const d = t_out - t_in;
  VEOS.fx.three({ id, t_in, t_out, z: 8, kind: "lockup", box: { x: 0, y: cy - 330, w: 1080, h: 660 },
    camera: { fov: 30, pos: [0, 0, 9] }, lights: { rim: { color: "accent", intensity: 2.5 } },
    objects: [{ kind: "text", text, slot: "caps", weight: 900, italic: true, size: 1.05, depth: 0.35, bevel: 0.03,
      material: "chrome", side: "#1B2A5A", glow: { color: "accent", size: 5, strength: 0.35 },
      keys: [{ at: 0, scale: 0.85, opacity: 0 }, { at: 0.13, opacity: 1 }, { at: 0.47, scale: 1, ease: "expoOut" },
             { at: d - 0.27, scale: 1, pos: [0, 0, 0] }, { at: d - 0.1, opacity: 1 },
             { at: d, scale: 2.6, pos: [0, -2.6, 2], opacity: 0, ease: "in" }] }] }); }
// Mid-reel on W-void: two titles in one 3D scene; the camera dollies through the first into the second
function chromeDolly3D(id, t_in, t_out, a, b, at /* local s of the dolly */) {
  VEOS.fx.three({ id, t_in, t_out, z: 8, kind: "lockup", box: { x: 0, y: 560, w: 1080, h: 700 },
    camera: { fov: 30, pos: [0, 0, 9], keys: [{ at, pos: [0, 0, 9] }, { at: at + 0.6, pos: [0, 0, -3], ease: "inOut" }] },
    lights: { rim: { color: "accent", intensity: 2.5 } },
    objects: [a, b].map((text, i) => ({ kind: "text", text, slot: "caps", weight: 900, italic: true, size: 1.0, depth: 0.35,
      material: "chrome", side: "#1B2A5A", pos: [0, 0, -12 * i], glow: { color: "accent", size: 5, strength: 0.3 } })) }); }
```
(Captions are hidden under z8 for the title's life. No `ground`: the title floats, no shadow.)

### 5.3 Caption system profiles
Three profiles. `captions.default` is CS-1 (F-A) / CS-3 (F-B); `by_layout` sends L-card-pale and L-pip-orbit to CS-2. All extend `lib:joseph`.

| Group | **CS-1 Duet (F-A, L-full)** | **CS-2 Under-card (W-pale layouts)** | **CS-3 Italic caps (F-B)** |
|---|---|---|---|
| Mode | full / primary / mute_safe | same | same |
| Chunking | `phrase`, 1–8 words (a whole short sentence builds into a 2–3 line block: v01 @0:00–0:02.3 "This editing style / is taking over / In 2026"), ≤ 18 chars/line, ≤ 3 lines; never split names, numbers, units; break on punctuation and pauses ≥ 0.9 s | `phrase`, 2–6 words, ≤ 30 chars, 1 line | `phrase`, 1–4 words, ≤ 18 chars/line, ≤ 2 lines |
| Timing | reveal `word` (each word blurs in on its onset, in place), lead 1 f, ≥ 0.25 s/word, pause hold ≤ 0.6 s, tail 0.12 s | same | same |
| Swap | `blur` 5 f, 10 px, out 5 f | `blur` 4 f, 8 px | `blur` 5 f, 10 px |
| Skin | Jost 500, 56 px base, as spoken, white `#FFFFFF`, shadow `0 2 14 rgba(0,0,0,.45)`, line height 0.9 (lines nearly touch; script swashes interlock with the line below), no container | Inter Tight 500, 44 px (E3), ink, no shadow | Montserrat italic 400, 58 px, UPPER, white, soft white glow + dark shadow |
| Position | anchor `chest`: block top = face bottom + 220 px; fallback cy 1120 (measured block centres 1060–1130 across v01/v02/v04; 3-line block spans y ≈ 1000–1240); max width 800 (measured 650–780); centred (the source staggers lines left → right, see engine limits); avoids the face | `below_card` + 34 px (≈ y 1365) | anchor `chest` + 220; fallback cy 1220 |
| Emphasis | `size_tier`: select number > topic noun > name; ≤ 1 per chunk; ≤ 0.35/s; min score 1.5 | none | `size_tier` ×1.25 in weight 800 |
| Duet | **tier 0** (function words: is, at, you, and, like, what, to…) → `geo` Jost 500 at 1.0× = **56 px**; **tier 1** (content words) → `script` Pinyon 400 at 1.55× = **87 px**; **tier 2** (the punch word or number) → `geo` Jost 700 at 1.8× = **101 px** (measured v04 @0:01.5: "think" ascender band 72 px ≈ 98 px font; "and you" ≈ 55 px; script "That" cap 60 px ≈ 88 px font) | off | tier 0/1 → caps 400/500 italic 58 px; tier 2 → caps 800 italic 72 px |
| Hide | under z8 scenes, during declared transitions and stage morphs | same | same |
| Language | Latin; keep English terms; spelling not normalised; profanity masked (`inner`) | same | same |

**Duet assignment rules (the editor checks them in P5b):**
1. A chunk is never all one voice. Runs of 2–3 script words are fine (v01 @0:03.5 "*And every single*"); a whole 3-line block in script is not. Sentence openers (This, If, That, The, In, And) are script in the source (v01, v02, v04): the engine puts function words in sans, so the editor promotes the opener to tier 1 by hand in P5b when the chunk starts a sentence.
2. Numbers, brands, tool names and the tier-2 word are never in script (N6). Content words go to script by default, so mark numbers, tool names and names `emph` (tier 2) or demote them to tier 0 in P5b; check that names are in the glossary.
3. The tier-2 word is the punch of the line, set bold and largest ("taking over", "2026", "your", "think", "reason"), at most one per chunk (one per line in long blocks), at most one every ~3 s.
4. A chunk alternates voices: script → small sans → script → **bold**. Verified targets at full res: "*This* editing *style* / is **taking over** / *In* **2026**" (v01 @0:02.3) and "*If* you *look* / at **your** *edits* / and you **think**" (v04 @0:01.5).
5. Single-word chunks are allowed and common in the body (v01 @0:20 "two", @0:44 "create"): use them for short emphatic sentences.

### 5.4 Other text systems
| System | Class | Recipe | Hold |
|---|---|---|---|
| Diamond numeral | TC-display | Inter Tight 800, 64 px in a 128 px diamond (96 px in a 180 px diamond), `paper` | with its diamond |
| Marker title | TC-display | Inter Tight 700, 62 px, `paper`, shadow `0 2 12 rgba(0,0,0,.45)`, right of the diamond | ≥ 1.0 s after built |
| Tutorial title | TC-display | Inter Tight 600, 56 px, `paper` 92% | the tutorial span |
| Sparkle bullet | TC-label | Inter Tight 500, 40 px, `paper` 90%, ≤ 4 words, ≤ 2 lines (≤ 18 chars/line); a 28 px four-point sparkle in `paper` with an `accent` glow | to the end of its card |
| Leader label | TC-label, E3 `redundant` | Inter Tight 500, 30 px, `paper` 88%, ≤ 4 words on ≤ 2 lines; the words must be spoken or shown larger nearby | ≥ 1.2 s |
| Footer line | TC-legal | Inter Tight 400, 30 px, `paper` 78% ("The full tutorial is on my YouTube") | the tutorial span |
| Card caption | TC-subtitle, E3 | = CS-2 | per chunk |
| Link-card title / meta | TC-label 40 px 700 / TC-legal 26 px 500 | `paper` on dark glass | the card's life |
| Stat count | TC-label | Inter Tight 800, 44 px, with a 34 px eye glyph | the collage |
| Rating label | TC-label | Inter Tight 500, 40 px, `paper` 85% ("Your edits" → "Pro edits") | the widget |
| Outline word | TC-display | Inter Tight 900, 240 px, transparent fill, 3 px `paper` stroke at 70% | 1.0–1.6 s |
| Script tag | TC-display | Pinyon Script 400, 100–130 px, `paper`, overlapping the lower right of a caps word by 30% of its height | with its word |
| Tracked line (F-B) | TC-label | Montserrat 400, 44 px, UPPER, letter-spacing 0.5 em, ink 70% | with the figure |
| Hero figure (F-B) | TC-display | Montserrat 900 italic, 230 px, ink with a soft 3D drop (`0 18px 30px rgba(0,0,0,.35)`) | ≥ 1.5 s |
| Glass slab text (F-B) | TC-display | Montserrat 800 italic 64 px caps + 400 italic 48 px second line | ≥ 1.5 s |
| Number tile (F-B) | TC-display | Montserrat 900 italic 72 px in a 96 px tile | the module span |
| Style name (F-B) | TC-display | Montserrat 900 italic 88 px caps + script tag "Style" | ≥ 1.2 s |
| CTA lead / keyword (F-B) | TC-display | "DM OR COMMENT" Montserrat 800 italic 64 px ("OR" 400 at 60%); keyword Montserrat 900 italic 128 px in quotes | to the end |
| Flash word | TC-display | Inter Tight 700, 96 px | 0.6–1.2 s |
| "Results vary" tags | TC-legal | Inter Tight 500, 24 px, `paper` 70% (ink 60% on light worlds), bottom-right inside the element | while the element shows |

### 5.5 Language and number rules
- English words and brand names are spelled exactly; Hinglish is romanised as spoken (`transform: verbatim`); no Devanagari (Pinyon Script has none).
- Numbers: international grouping with `$` (1,000 · $2,000 · 635K); BV-06 switches to Indian grouping and ₹ when the buyer speaks Hinglish (₹1,20,000 · 12.5 L).
- Counts on stat cards use the compact form the creator's platform shows (635K, 1.2M).
- Caps (CS-3, titles) are Latin only.

---

## §6 Hook system `[REQ]`

### 6.1 Stopper tests
| ID | Test | This style's number |
|---|---|---|
| ST-1 | Thumbnail: frame 0 at 25% scale shows a person teaching + the first caption word | the script word at 87 px reads as a word at 25% (22 px) |
| ST-2 | Mute: the first 3 s tell the promise without sound | the promise lockup + the proof element |
| ST-3 | Motion at f0 | Z-0 land-settle from t 0 + the first word's blur-in |
| ST-4 | Read time | the promise's first chunk reads in ≤ 1.5 s; the F-B chrome title in ≤ 1.2 s |
| ST-5 | Change count | ≥ 6 weighted SCs in 0–3 s (each promise word is a declared event) |
| ST-6 | Payoff-by | first promise line by 0.7 s; a proof element by 2.5 s (H3) |

### 6.2 Default archetype: HA-05 "Promise + proof"
The creator states the promise ("This editing style is taking over in 2026", "If you look at your edits and you think…", "What is <product>?") while a proof element animates in within the first 0.5–2.5 s. Not result-first: the hook promises, the proof makes the promise credible.

**F-A (v01 @0:00–0:04, v04 @0:00–0:03):**
| t | Visual | Caption | Layout / camera | SFX moment |
|---|---|---|---|---|
| **f0** | Face full frame in the studio colour, **zoomed in and settling out** (v01 1.25 → 1.0 in 50 f with f0–f2 blurred; v04 1.20 → 1.0 in 40 f after one black frame; half the travel by f12). P-PROMISE-DUET's first word (the script opener: "This", "If", "The") blurs in by 0.13–0.3 s (v04 @0:00.13, v01 @0:00.07) | the promise lockup (word build) | L-full; Z-0 land-settle 1.22 → 1.0 over 45 f from t 0, `blur: {"kind": "defocus", "px": 10, "frames": 3, "shape": "decay"}` on the f0 event | hook cue on f0 (soft whoosh-in or tick) |
| 0.0–0.5 | Words 2–3 build in place (alternating script / small sans), each a 5–6 f blur+fade-in | "This editing style" | — | — |
| 0.5 | **Proof lands:** P-POSTER-ROW's first card slides in from the left edge (v01 @0:00.47), **or** P-STAR-RATING's label + first star fade in under the caption (v04 @0:00.17–0:00.5) | — | — | reveal cue |
| 0.5–0.8 | P-LINK-CARD blurs in and rises at y 1250–1480, 8–10 f (v01 @0:00.53–0:00.8) | — | — | — |
| 1.0–2.0 | The poster row fills (4 cards, 3 f stagger) and starts drifting left 40 px/s; line 2 builds | "is taking over" | — | — |
| 2.0–2.5 | The tier-2 word lands (101 px Jost 700): the claim's hero word ("2026", "Instagram", "faceless") | "In **2026**" | — | text-pop cue |
| 2.5–3.5 | The rating widget (if used) fills 1 → 5 stars with the label swap; the promise completes | — | — | success cue (rating) |
| 3.5–4.5 | Proof elements blur out (6–8 f, v04 @0:04.2–0:04.47); the body captions (CS-1) take over | "And every single editor…" | Z-0 has settled | — |
| ≤ 9 | The "here are N…" line: P-DIAMOND-ROW pops in (N diamonds, 5 f stagger) on the count word | "*Three Steps*" as a script hero line (≈ 160 px Pinyon, v01 @0:09) over "to making this / **editing**" | L-full; **Z-1 marker-push** +8% in 20 f on the count word, held ~1.5 s, Z-2 pull-out as item 1 starts (v04 @0:04.3–0:07.0) | list cue on the row |

**F-B (v05 @0:00–0:04):**
| t | Visual | Caption | Layout / camera | SFX moment |
|---|---|---|---|---|
| **f0** | Face full frame (neon set). P-PROMISE-DUET in the CS-3 skin: "WHAT IS?" blurs in at chest | "WHAT IS?" | L-full; Z-0 from t 0 | hook cue |
| 0.7 | **P-CHROME-TITLE lands** under "WHAT IS?" (scale 0.85 → 1, blur 12 → 0, 6–8 f, v05 @0:00.71–0:00.96) with the flare sweep | captions hidden (z8) | — | impact / shine on the land |
| 0.9–1.6 | The title holds; the flare passes | — | — | — |
| 1.6 | T-10 fly-through exit: the title scales up toward the lens and drops off the bottom with motion blur in 6–8 f (v05 @0:01.63–0:01.92) | — | — | whoosh on the exit |
| 1.9–3.8 | Script tag opener + italic caps line: "*Well,* SOMETHING THAT'S NEVER **been seen** BEFORE" | CS-3 (P-SCRIPT-TAG "Well," on the first word) | — | — |
| 3.8 | T-12 colour-burn cut (≈ 0.3 s, built-in `burn`) into the product-name line (v05 @0:03.71–0:04.0) | CS-3 | Z-0b after the cut | glitch / burn whoosh |
| 3.8–9.5 | The promise: "<PRODUCT> IS A PROGRAM THAT CAN TAKE ANY BEGINNER … IN ONLY **30 DAYS**" | CS-3 | Z-2 pull-out after the claim | — |
| 9.5–12.5 | **Result claim:** cut to W-void, P-NEON-OUTLINE-FIGURE with the creator's real result figure ("$1K–$2K / MONTH" only if the script says it) + "Results vary" | captions hidden | L-graphic, T-05 cut | reveal cue |
| 12.5–17 | "DON'T BELIEVE ME? EXPLAIN THIS" → P-TILTED-GLASS-SHOTS (2–3 real screenshots) | CS-3 then hidden | L-full | card-in cues (different files) |

### 6.3 Allowed alternates
| ID | Name | Short recipe (0–3 s) | Example (Niche 1: fitness coaching) | Example (Niche 2: design & software tutorials) |
|---|---|---|---|---|
| **HA-02** | **Face-shrink proof** (v02 @0:00–0:03) | f0 promise lockup (`satisfies: [headline]`); 0.6 s G-1 shrink-to-card into W-pale; 0.9–1.5 s P-STATCARDS drift in around the card with the creator's **real** counts (`kind: card`); CS-2 under the card | "The reason your squat isn't growing" → card + 4 stat cards of the creator's own posts' saves | "The reason your slides still look amateur" → card + 4 of the creator's real view counts |
| **HA-07** | **Live number: the star rating** (v04 @0:00–0:03; the engine's HA-07 "Live number / ledger open": a number moving at f0 + a claim, payoff ≤ 1.0 s) | f0 promise lockup (`satisfies: ["headline", "claim"]`: it is the claim V-F0 asks for) + P-STAR-RATING from t 0 (`kind: "stat"` + `satisfies: ["number"]`, with `events` (the first star's pulse) so it is moving at f0; the star count is the live number HA-07 needs): label "Your <thing>" 1 star; on the comparison word the label swaps to the target ("Instagram", "Pro") and the stars fill 1 → 5 (4 f stagger) | "If you look at your form and think…" → "Your squat ★" → "Coach-level ★★★★★" | "If you look at your dashboards…" → "Your dashboard ★" → "Pro ★★★★★" |
| **HA-18** | **Recursion** (v03 @0:00–0:01; needs SH-2) | f0 the creator's earlier reel plays in a dashed window on the chest (`kind: clip`) with a TC-legal header chip "My first reel · <year>" (`satisfies: [post]`); 0.5 s G-1 shrinks the whole frame into a card; 1.0 s P-CARD-CAROUSEL with the old-reel side cards; CS-2 above/under; **fallback FB-2**: HA-02 without stat cards (carousel only) | "It took me 3 years to build this physique" + the first transformation reel in the window | "It took me 2 years to build this template system" + the first tutorial reel in the window |

F-B uses HA-05 (chrome title) by default and HA-07 when the product has a rating story.

### 6.4 Hook pairs (promise → proof) `[NICHE: example]`
| Topic | Promise line (spoken) | Proof visual | How it is shown |
|---|---|---|---|
| **N1** Squat / glute training | "This squat cue is everywhere in 2026" | 4 client stills (creator's own, consented) | P-POSTER-ROW behind the head |
| **N1** Fat-loss mistakes | "If you look at your progress and you think…" | rating "Your progress ★" → "On track ★★★★★" | P-STAR-RATING (HA-07) |
| **N1** Coaching program (F-B) | "What is <PROGRAM NAME>?" | chrome title of the program | P-CHROME-TITLE |
| **N1** "I built this in 3 years" | "It took me 3 years to build this" | the first transformation reel | P-RECURSION (HA-18) |
| **N2** A design style | "This slide style is taking over in 2026" | 4 of the creator's own slide exports | P-POSTER-ROW + P-LINK-CARD to the full tutorial |
| **N2** Why work looks amateur | "The reason your dashboards still look basic" | face card + 4 real view counts | P-SHRINK-TO-CARD + P-STATCARDS (HA-02) |
| **N2** A template course (F-B) | "What is <COURSE NAME>?" | chrome title + glass slabs ("MASTER <SKILL>", "<RESULT> IN 30 DAYS") | P-CHROME-TITLE + P-GLASS-SLAB |
| **N2** Tool comparison | "Everyone is using the wrong tool for this" | orbit of tool tiles (type-set names) | P-ORBIT-FACE |

Append a row per reel (D.6).

### 6.5 Headline (promise) writing `[DNA formula; NICHE examples]`
**Formula (F-A):** `[soft opener in script] + [what] + [claim or tension] + [hero word]`, 6–12 words, written so the chunker produces 2–3 chunks with one tier-2 word in the last chunk.

| Template | Example |
|---|---|
| Trend | "This **<style/method>** is taking over in **2026**" |
| Mirror | "If you look at your **<work>** and think it looks nothing like **<target>**" |
| Reason | "The reason you still can't **<result>**" |
| Effort | "It took me more than **<N> years** to build this" |
| Steps | "Here are **3 steps** to **<result>**" |

**Formula (F-B chrome title):** the product name in ≤ 4 words, preceded by "What is…?" as the spoken opener. Glass slabs carry `MASTER <SKILL>` / `<RESULT> IN <N> DAYS` (only real, script-stated promises).

Rules: sentence case as spoken (F-A), caps (F-B). No emoji. No hype words without a claim ("insane", "game-changer"). **Write 3 and pick by the stopper tests**; the other two go to trial reels.

### 6.6 Hook sound
The hook carries cues on f0 (soft whoosh-in or UI tick), on the proof landing and on the tier-2 word (§11). The music bed enters after the hook (on the "here are N" line or the first marker).

### 6.7 CTA
| Device | Spoken pattern | On screen | Hold | Placement |
|---|---|---|---|---|
| `cross_promo` (F-A default) | "The full tutorial is on my YouTube… just go watch it" | P-VIDEO-CARD (thumbnail + title + "Watch the full tutorial" meta) at chest, z8; earlier P-LINK-CARD in the hook | ≥ 2.5 s, ≤ 4 s | end (+ a hook tease) |
| `comment_keyword` (F-B default) | "DM me or comment <keyword>" | P-KEYWORD-GLASS on L-dim: "DM OR COMMENT" + the glass chip with the keyword in quotes | ≥ 3 s to the last frame | end |
| `dm` | "DM me <keyword>" | P-KEYWORD-GLASS with "DM ME" | ≥ 3 s | end |
| `link_bio` | "Link in my bio" | P-LINK-CARD with a "link in bio" chip under the title | ≥ 2 s | end |

- The keyword for this copy: **{{BV-08.keyword|KEYWORD}}** (device: {{BV-08.device|cross_promo}}).
- Silence before the CTA: no SFX in the 1.0 s before the first CTA word.
- The CTA never runs on W-pale; it is on the face (L-full / L-dim).
- Hard end ≤ 6 f after the last word.

---

## §7 Structure and cadence `[REQ] [DNA]`

### 7.1 Structure types
| Format | Type | Arc | Evidence |
|---|---|---|---|
| F-A | `tutorial` (numbered) | promise + proof → "here are N steps/tips/reasons" (row) → item 1…N (ritual) → recap row → CTA (link/video card) | v01 (3 steps), v03 (6 techniques), v04 (3 reasons) |
| F-B | `list` (sales) | "What is <product>?" (chrome title) → result claim → proof (screenshots) → re-hook question → what's inside: modules 1…N (tiles) → guarantee → last re-hook → CTA keyword | v05 |

### 7.2 Markers
| ID | Marker | Recipe | Format |
|---|---|---|---|
| **SM-GLASS-DIAMOND** | Glass diamond + title | P-DIAMOND-MARKER on every ordinal word; numbering ascending 1…N | F-A |
| **SM-DIAMOND-ROW** | Progress row | P-DIAMOND-ROW: N diamonds on the count word in the promise; returns as P-RECAP-ROW before the CTA | F-A (with SM-GLASS-DIAMOND) |
| **SM-NUM-TILE** | Glass tile row | P-NUM-TILE-ROW: N rounded tiles, the active one lit, with the module title + script tag | F-B |

One marker style per reel, at every item. No teaser chips.

### 7.3 Unit ritual (F-A, identical for every item; `o` = onset of the ordinal word)
| Frame | Step |
|---|---|
| o − 2 f | **Diamond emerges from the counting hand** and glides to (250, 1120): opacity 0 → 1, scale 0.4 → 1.08 → 1.0, ~80 px diagonal travel, 10 f with overshoot (v04 @0:20.8–0:21.1, @0:06.07–0:06.3; v03 @0:13.57–0:13.7). Z-1 marker-push starts on the same word. List cue SFX (the one allowed repeat) |
| o + 6 f | **Title reveals** right of the diamond (x 360, 62 px), a left → right wipe with a soft edge over 10 f (v03 @0:14.1–0:14.5, @0:05.87); in v01/v04 the title is the duet caption itself ("*First* is the **background**") |
| o + 1.0–1.5 s | Z-2 pull-out (20 f) unless R-A follows (then Z-3 push into the cut) |
| o + 1.2 s (≥ 10 f after the title is built) | Branch by ritual: |
| **R-A Tutorial** (a visual process with ≥ 2 sub-steps; creator media or FB-1) | T-04 push-cut to L-tutorial: hard cut, the glass card grows from the centre (20 f), the title row (diamond + title) fades in at (150, 436); each sub-step's sparkle bullet on its phrase (stagger 0.6–1.2 s; the card content changes per bullet with a 4 f crossfade, v01 @0:12.6); the world holds still otherwise (v01 @0:12.4–0:17.1); 3.5–7 s total; eases out, T-05 hard cut back + Z-0 |
| **R-B Chest window** (one idea shown by one image/clip) | The marker blurs out (6–8 f, v03 @0:15.13–0:15.4); P-PREVIEW-WINDOW opens at chest (a thin line growing to full height, 8–10 f, v03 @0:15.53–0:15.8) with the thing; 1–2 P-LEADER-LABELs; ≤ 3 sparkle bullets under it; 2.5–5 s |
| **R-C Concept** (a reason or mindset with nothing to show) | The marker holds 1.2–2.0 s, blurs out; the body runs on duet captions with one support pattern (P-OUTLINE-WORD, P-LIGHT-BAR-LIST, P-PLAY-BULLETS, P-CHECKLIST-CARD or P-DUO-ICONS) |
| end of item | Back to L-full captions for the creator's comment line (≥ 1.5 s of face before the next diamond) |

Pick R-A for at least one item per reel when SH-1 or FB-1 material exists (the tutorial world is part of the DNA, v01). Never two R-A items back to back without ≥ 2 s of face between them.

**F-B module ritual:** on the module word, P-NUM-TILE-ROW rises (row of N tiles at y 1380–1476, the active tile lit) with the module title (caps 800 italic 96 px at y 1290) and its script tag; holds 2–3 s; then the creator explains on CS-3 captions, optionally with one P-STYLE-CARD / P-SCREEN-PANEL of the module's content.

### 7.4 Open loops and re-hooks
- **Count loop:** the diamond row in the promise shows N; each item lights its number; the recap row shows all N (H8).
- **Deliverable loop:** "the full tutorial is on YouTube" (hook link card) → paid by the video card at the end.
- **F-B re-hooks every 25 s** (`structure.rehook_every_s`): a question line set big ("HOW IS THIS DIFFERENT…?", "DON'T BELIEVE ME?", "AND LASTLY, THE SECRET") with P-SCREEN-WALL, P-TILTED-GLASS-SHOTS or a P-COLOUR-FLASH-WORD.
- Intro cap: hook + promise ≤ 15% of runtime (≤ 9 s in a 60 s reel).

### 7.5 Rhythm and energy curve
- **Calm, steady, premium.** Energy is carried by the caption rhythm and the reveals, not by camera moves.
- Alternate the worlds: face → (tutorial or window) → face. Never two non-face spans back to back except the F-B void runs.
- The last item gets the richest visual (an R-A tutorial card or the checklist card).
- The end is quiet: recap row, one sentence, the CTA card, hard end.

### 7.6 Cadence (state changes)
| Token | F-A | F-B |
|---|---|---|
| `sc_per_10s` | 4–10 | 3.5–9 |
| `hook_sc_3s` | 6 | 6 |
| `max_gap_s` (weight ≥ 1) | 2.0 (hook 1.0) | 2.2 |
| `max_static_s` | 2.5 | 2.5 |
| `caption_weight` | 1.0 (primary captions) | 1.0 |
| `cuts_per_min` | not DNA (1–2 detected) | not DNA |

**Measured pacing (full-rate scene detection):** F-A hard cuts are only world switches: v01 8 in 50 s (shots 2.1–11 s, median 6.1 s), v02 9 in 47 s (median 6.2 s), v03 1, v04 0 (one 46 s take). Within a take the visual changes are caption words (every 0.25–0.5 s), markers and camera breaths: marker-pushes ≈ 1 per 10 s (v04 5 in 46 s, v03 6 in 53 s). F-B v05: 35 cuts in 122 s, median shot ≈ 3.4 s, p90 ≈ 7.4 s, two burn cuts. Longest stretch with no new element: ≈ 1.5 s (captions carry it); the tutorial world holds its card still for up to 4.7 s while bullets land every ~0.9 s (v01 @0:12.4–0:17.1).

Live footage counts as continuous motion; a Z-0 settle or Z-1 hold also does. Declare `events` for every word built inside z8 type scenes, every bullet, label, star and tile.

---

## §8 Visual system `[REQ]`

### 8.1 Graphics role and budget
- `support`: graphics on screen 15–50% of runtime (F-A 25–40%, F-B 40–55%).
- 43 patterns; each reel uses 8–16 of them.
- ≥ 4 families per 60 s.
- "Show the thing": every step, tool, result or number is shown, on the word (D2). Numbers on screen are the creator's real figures (§8.5).

### 8.2 Families
| ID | Family | Source class | Buyer supplies |
|---|---|---|---|
| **B-1** | Duet type and titles (promise, script tags, outline word, chrome title, slabs, figures) | engine | — |
| **B-2** | Glass markers (diamonds, rows, tiles) | engine | — |
| **B-3** | Teaching windows (tutorial card, chest window, bullets, labels, checklist, lists) | engine frame + buyer-owned content | SH-1 exports / recordings (else FB-1) |
| **B-4** | Proof and UI cards (poster row, stat cards, rating, search bar, notices, product stacks) | engine + buyer-owned images | SH-3 stills, real counts |
| **B-5** | Stage moves (shrink-to-card, carousel, recursion, orbit) | engine | SH-2 earlier reel (optional) |
| **B-6** | Ambient fields (falling icons) | engine | — |
| **B-7** | CTA and link cards | engine + buyer-owned thumbnail | SH-4 |
| **B-8** | Creator media frames and third-party stand-ins (screen panel, style card, tilted shots, screen wall, profile tile) | buyer-owned, or creator-supplied third-party with a created substitute (§12.5) | SH-5, SH-6 |

### 8.3 Pattern specs
All recipes at 30 fps. "Glass" means the **glass-lite recipe**: fill `rgba(18,20,38,.58)` on footage/void (`rgba(255,255,255,.62)` on W-pale); 2 px rim with the `glass_rim` gradient; a 1 px inner top highlight `rgba(255,255,255,.35)`; outer glow `0 0 28px` pack `accent` at 55%; corner radius 14–26; no `backdrop-filter` except where marked (≤ 1 per frame, blur 14 px).

**B-1 Duet type and titles**
| ID | Type | What's on screen | Motion recipe | When | Text class / flags |
|---|---|---|---|---|---|
| **P-PROMISE-DUET** | overlay (z8, `kind: promise`) | The hook's first sentence in the CS-1 (F-A) or CS-3 (F-B) skin at chest, each word in its tier | Each word blurs in on its onset (opacity 0 → 1, blur 14 → 0 px, y +16 → 0, 6 f expo-out), in its final place; lines stack upward-centred; the whole block blur-swaps out 5 f after the last word + 0.25 s. Declare `events` at every word onset. Hide auto-captions for its span | Every hook (H1) | TC-subtitle; `satisfies: [headline]` for HA-02 |
| **P-SCRIPT-TAG** | overlay | A script word tucked under the lower right of a caps word ("EDITING *Basics*", "$2,000 *Month*", "Well," before a caps line) | Script blurs in 4 f after its caps word lands, slides x −24 → 0 over 8 f | F-B titles, style cards, number tiles | TC-display |
| **P-OUTLINE-WORD** | overlay (z5) | One hollow word 240 px (3 px `paper` stroke at 70%) behind a marker, with its filled sub-title under it (v04 @0:32 "Poor / Post Production") | Fades in 8 f with letter-spacing 0.12 → 0 em; holds 1.0–1.6 s; fades 6 f. The diamond sits on it (`overlaps`) | R-C items whose name has one strong word | TC-display |
| **P-COLOUR-FLASH-WORD** | world cut | W-flat (pack colour) or W-pale fills the frame with one word, 96 px, centred y 960 (v02 @0:25–0:26) | Hard cut in (T-08), word fades in 3–4 f (v02 @0:26.43), holds 0.6–1.2 s, hard cut out; in a declared pair each word hard-swaps on its onset (v02 @0:25.0 "they're" → "just" → @0:26.43 "Hard enough"); ≤ 2 per reel; never two back to back except as a declared pair ("just" → "hard enough") | A punch word in a calm stretch, an F-B re-hook | TC-display; captions hidden for the span |
| **P-CHROME-TITLE** | overlay (z8, `kind: lockup`) | §5.2: chrome caps title with extrusion, glow and flare; a lit 3D chrome word (`VEOS.fx.three`, recipe in §5.2) or the 2D chrome recipe | Land 14 f + flare 18 f; hold ≥ 30 f; T-10 exit 8 f. Flat fallback per §5.2 | F-B hook, F-B product reveal | TC-display |
| **P-GLASS-SLAB** | overlay (z5) | 1–2 glass plates 600×150 (radius 22) with caps text: "MASTER <SKILL>" / "<RESULT> IN <N> DAYS" | Each rises from y +80 with rotateX 12° → 0 (perspective 1200) over 12 f, 6 f stagger; floats ±6 px (3 s sine) | Under the chrome title (F-B) | TC-display; one `backdrop-filter` allowed |
| **P-NEON-OUTLINE-FIGURE** | overlay on W-void | The result figure in outlined type (Montserrat 900 italic 180 px, 3 px `accent` stroke, 24 px glow) over a light-beam cone from the top (linear gradient 30% → 0) with seeded dust motes | Stroke draws (dash offset) over 18 f, then the glow blooms 8 f; motes drift 10 px/s | F-B result claim (only a real, script-stated figure) + "Results vary" | TC-display; figure from `plan/figures.json` (stated) |
| **P-TRACKED-FIGURE** | overlay on W-grid (`kind: counter`) | Tracked caps line ("MAKE $1,000 TO") y 760; hero figure 230 px y 820–1050; script tag ("Month"); tracked line ("IN 30 DAYS") y 1110 | Tracked lines fade + letter-spacing 0.8 → 0.5 em over 12 f; the figure rolls from its first value to the stated one over 18 f and lands on the spoken number (±5 f) | F-B money/result statement (v05 @0:34–0:36) | TC-display / TC-label; bound to `plan/figures.json` |

**B-2 Glass markers**
| ID | Type | What's on screen | Motion recipe | When | Text class / flags |
|---|---|---|---|---|---|
| **P-DIAMOND-MARKER** | overlay (z8) | A glass diamond (a 128 px rounded square rotated 45°, diagonal 181 px; fill linear 135° `primary`-light → `primary` → `primary`-dark; 2 px rim; inner top-left highlight; glow 28 px `primary` 70%) with the numeral; title right of it | Emerge: from the creator's counting hand, opacity 0 → 1, scale 0.4 → 1.08 → 1.0, ~80 px diagonal glide, 10 f (measured v04 @0:20.8–0:21.1, v03 @0:13.57–0:13.7; no 3D flip in any reference); numeral visible from f0; title wipes in L → R 10 f from o + 6 f; exit: blur-out 6 f or glide to the next world's title row (14 f) | Every ordinal word (F-A) | TC-display |
| **P-DIAMOND-ROW** | overlay (z6) | N diamonds (190 px diagonal, pitch 228 px; measured v01 @0:09 centres x 309/540/765, y 1419) centred x 540, y 1400 (3 items; for 4–6 items shrink to 140 px diagonal, pitch 160, as v03 @0:25); on the count word all are lit; later the inactive ones drop to 45% and the active one glows | Diamonds pop in left → right (scale 0 → 1.1 → 1, 8 f, 5 f stagger; v04 @0:04.87–0:05.27) on the count word under a Z-1 push; the whole row leaves in 1–2 f as the first marker arrives (v04 @0:06.0); the active one lights (opacity + glow 6 f) on its ordinal word | The "here are N" line; progress inside long items | TC-display (numerals) |
| **P-RECAP-ROW** | overlay (z6) | The same row returning, all lit, under the closing caption (v04 @0:43–0:45) | Rise from y +40 with 4 f stagger; holds to the CTA turn | Last sentence before the CTA | TC-display |
| **P-NUM-TILE-ROW** | overlay (z8) | N glass tiles 96×96 (radius 18) at y 1380–1476, pitch 120; active tile white glass 90% with the numeral in ink, others dark glass 40%; module title (caps 800 italic 96 px, y 1290) + script tag | Row slides in from x +60 (10 f); the active tile scales 1 → 1.12 → 1 (8 f) and the previous dims; title + tag blur in 8 f | Every F-B module | TC-display |

**B-3 Teaching windows**
| ID | Type | What's on screen | Motion recipe | When | Text class / flags |
|---|---|---|---|---|---|
| **P-TUTORIAL-CARD** | world (L-tutorial) | §3.4: title row (diamond + 56 px title) at y 436; glass card x 136–576, y 540–1340 holding the step's result (creator still / recording via `ctx.videoFrame`, or FB-1 mock); sparkle bullets right; footer line y 1470 | Enters with the hard cut (G-3): grows from 15% at frame centre to full in 20 f (expo-out, 3% overshoot, dim → full brightness) and glides to its rect; title row fades in 10 f during the grow (v01 @0:11.03–0:11.7, @0:24.13–0:24.7); variant: lands ≈ 2× oversized and settles in 15–18 f (v01 @0:32.57, @0:38.53). Then holds still; before the exit the whole world eases to 0.94 over ~30 f (v01 @0:17.1–0:18.07); inside, the result evolves per bullet (layer added, texture applied: crossfade 8 f or a wipe 10 f); bullets per P-SPARKLE-BULLETS; footer fades in at 1.0 s | R-A items | bullets TC-label 40; footer TC-legal 30|
| **P-SPARKLE-BULLETS** | overlay | Up to 5 bullets (tutorial card) or 3 (under a chest window): a four-point sparkle 28 px + 40 px text | Sparkle spins 90° and scales 0 → 1 (6 f); text blurs in 8 f; each on its spoken phrase, stagger ≥ 0.6 s | Sub-steps, settings, features | TC-label |
| **P-PREVIEW-WINDOW** | overlay (z8) | A glowing chest window x 216–864, y 980–1300 (radius 14, 2 px `accent` rim at 90%, glow 28 px) showing the thing: a still, a recording, a before/after, a text sample set in the font being taught | Opens from a thin horizontal line to full height (scaleY 0.05 → 1, 8–10 f, v03 @0:15.53–0:15.8) with a rim flash 0.9 → 0.55; content crossfades per spoken example (8 f); closes scaleY → 0.2 + fade (8 f) | R-B items, "this looks like…" | content TC-decorative unless it is the point |
| **P-WINDOW-WIPE** | state | Inside a chest window or tutorial card: before → after with a vertical light wipe (a 6 px white line with a 20 px glow travelling L → R, 14 f) | 14 f wipe, hold ≥ 1.0 s on the after | "Before / after", "add this and…" | — |
| **P-COMPARE-CARDS** | overlay (z8) | Two portrait glass cards side by side at chest (each ≈ 300×440, x 200–500 and 580–880, y 1000–1440), each labelled in the duet skin above it ("*Text* centric" / "*Object* centric") | Cards rise + blur in 10 f, 6 f stagger, labels with them; exit by the push-cut into the next world (v01 @0:23.9–0:24.13) | "Option A vs option B", two kinds of something | labels TC-display (duet), content TC-decorative |
| **P-LEADER-LABEL** | annotation (ink, z6) | A 2–3 px `paper` line from a 5 px `accent` dot on the target to a 30 px label (≤ 4 words, 2 lines) | Dot pops 4 f; line draws 8 f; label blurs in 6 f; ≤ 3 on screen; exits with its window | Naming parts of what is shown ("Edges of the screen", "Sans font") | TC-label E3 `redundant` |
| **P-ROW-HIGHLIGHT** | annotation (ink) | A highlight bar (`accent` 35%, radius 8) moving from row to row inside a list window (v03 @0:44) | Glides to the next row in 8 f (ease glide) on each spoken item | Listing options inside a UI | — |
| **P-CHECKLIST-CARD** | overlay (z8) | A translucent `primary` card x 300–780, y 980–1500 (radius 20): header 40 px centred, a 3 px `accent` underline, sparkle bullets 40 px (≤ 3 words each) | Card blurs in + rises 12 f; underline draws 10 f; bullets per P-SPARKLE-BULLETS | A checklist, "make sure you…", the last item | TC-label |
| **P-LIGHT-BAR-LIST** | overlay (z8) | A vertical glowing bar (6×260 px, `primary` → transparent) at x 300, y 1060–1320 and one italic sub-point label (Inter Tight 500 italic 44 px) beside it that swaps per spoken sub-point (v04 @0:25–0:28) | Bar grows top-down 10 f; label blur-swaps (in 6 f, out 6 f, previous label slides down 40 px as it fades) | Sub-points of a concept | TC-label |
| **P-PLAY-BULLETS** | overlay (z8) | Up to 2 consequences with ▶ glyphs (28 px `primary`-light) and 40 px text at x 230, y 1080 / 1140 (v04 @0:18–0:20) | Glyph slides x −20 → 0 + text blur-in 8 f; stagger on speech | "If you don't, you'll…" consequences | TC-label |

**B-4 Proof and UI cards**
| ID | Type | What's on screen | Motion recipe | When | Text class / flags |
|---|---|---|---|---|---|
| **P-POSTER-ROW** | overlay (z3, `behind: true` with matte) | 4–6 portrait cards 270×486 (radius 10), 2 px white rim, 18 px `accent` glow, creator's stills (SH-3); y 200–686 behind the head; without matte y 140 → head top − 40 with cards scaled to fit (min 260 tall, else skip) | Cards slide in from x −420 (16 f, 3 f stagger), then the row drifts left 40 px/s; exit blur 6 f | Hook proof (v01 @0:00.5–0:03); "styles like these" | no text; FB-3 cards are type-set |
| **P-STATCARDS** | overlay on W-pale (z3, `kind: card`) | 4 dark glass cards 300×400 around the face card, each with an eye glyph + a real count (44 px) | Drift in from the edges (14 f, 4 f stagger) with depth scale 0.9–1.05 and ±8 px float (3 s sine) | HA-02 proof; "these got <N> views" | TC-label; counts from the creator only |
| **P-STAR-RATING** | overlay (z6, `kind: stat`) | No container. Label (44 px, `paper` 85%) left-aligned at x 230, y ≈ 1340; 5 stars (68 px, gap 10) on one row under it at y ≈ 1430, left edge x 230 (measured v04 @0:00.5–0:03); empty stars = 2 px `primary` outline, filled = `primary`-light `#9F3DD5` with a 16 px `accent` glow (not gold) | Stars fill 5 f each (scale 1 → 1.2 → 1) with 4 f stagger; the label roll-swaps on the comparison word (old label rises 40 px and fades 6 f, new label rises in from +40 px) | HA-07; "rated", "quality" comparisons | TC-label |
| **P-SEARCH-BAR** | overlay on W-pale | A dark glass pill 560×84 at x 260–820, y 900 with a magnifier glyph; the query types in 40 px | Pill grows from 40% width (10 f); 1 character / 2 f typing with a blinking caret (on 15 f / off 15 f) | "You search for…", "Why can't I…" (v02 @0:07) | TC-label |
| **P-APP-NOTICE** | overlay (z8) | A notification pill x 140–940, y 1240–1370: 84 px icon tile (`fx.icon`), title 40 px 700, sub 26 px, an "Open" pill | Slides down from y −40 + blur-in 10 f; holds ≥ 1.5 s; slides up 8 f | A freebie, a file, a resource ("my inspiration vault", v04 @0:12) | TC-label + TC-legal sub |
| **P-PROFILE-TILE** | overlay on W-pale (third-party) | A dark profile tile 560×280 tilted −8°: avatar circle with initials, name, two decorative lines, a "Following" pill | Peels out of the carousel: the card rotates −30° and flips from portrait to the landscape tile, settling at −8° → −3° over 12–14 f (v02 @0:14.13–0:14.6); holds | Naming another creator / mentor (v02 @0:14); creator's own screenshot or the created tile | TC-label; insert record |
| **P-COURSE-STACK** | overlay on W-pale | 3 product cards 420×200 stacked at y 560/800/1040, each with its own soft glow; script heading ("So many *Courses*") y 430 and script footer ("*For you*") y 1320 | Cards drop in 10 f with 5 f stagger; glows breathe 0.4 → 0.6 (2 s) | "There are so many options/courses…" (v02 @0:37) | TC-display script + type-set cards (FB-6) |
| **P-DUO-ICONS** | overlay (z6) | Two glass diamonds 220 px at (330, 1160) and (750, 1160), each holding an `fx.icon`, labels 40 px under them | Pop in with 6 f stagger; on "and" / "together" they glide to the centre and merge into one diamond (14 f, ease glide) | "A + B = result" (v02 @0:29–0:33) | TC-label |
| **P-COURSE-BANNER** | overlay (z5) | A 760×420 product card (radius 24) in `primary` with a deep `accent` arc glow and the product name in the chrome-lite type (flat fallback) | Rises 12 f; glow sweep 18 f | Naming the creator's own product in F-A (v02 @0:05) | TC-display |

**B-5 Stage moves**
| ID | Type | What's on screen | Motion recipe | When | Flags |
|---|---|---|---|---|---|
| **P-SHRINK-TO-CARD** | stage (G-1) | The face shrinks into the 9:16 card on W-pale with an `accent` glow | §3.3 G-1 | Hook proof; "look at…"; before a collage | layout L-card-pale |
| **P-CARD-CAROUSEL** | stage + overlay (z3) | The face card centred; 2 side cards (300×620 at x 40 and 740, y 625, 0.85 scale, 55% opacity, 3 px blur) + 2 cut-off cards beyond; side cards hold the creator's stills (SH-3); without stills, the take itself registered as a video asset (`veos asset add <take> --name take`) at other moments via `ctx.videoFrame("take", t)`, dimmed 45% | Side cards slide in from the edges 14 f; ripple x ±30 px (2 s sine); to show the next card the whole row scrolls sideways one card pitch in 16 f (ease in-out, peak ≈ 100 px/f, v02 @0:11.93–0:12.47; cards curve slightly in perspective); CS-2 caption above or under | "More than N years…", body of work (v03 @0:01–0:04) | FB-3 for stills |
| **P-RECURSION** | stage (G-6) | The creator's earlier reel in a dashed window on the chest x 350–730, y 900–1576 (9:16) with a TC-legal header chip ("My first reel · <year>") | Dashed rect draws 8 f; the clip fades in 6 f and plays (`ctx.videoFrame`); at 0.5 s G-1 shrinks the frame into a card | HA-18 hook only; **needs SH-2**, else FB-2 | `kind: clip`; header `satisfies: [post]`; insert record origin creator |
| **P-ORBIT-FACE** | stage (G-5) + overlay | The face in the Ø 300 bubble (L-pip-orbit); 6–8 small tiles (150×100: type-set tool or product names, or creator stills) orbit an ellipse rx 380, ry 260; one hollow word (300 px, `primary` 12%) behind ("tools", "options") | Orbit 1 rev / 8 s, tiles scale 0.8–1.05 by depth; bubble enters by pip-shrink 12 f | "All the tools / options out there" (v02 @0:34) | ≤ 3.0 s |

**B-6 Ambient fields**
| ID | Type | What's on screen | Motion recipe | When | Flags |
|---|---|---|---|---|---|
| **P-FALLING-ICONS** | ambient (z2, E4) | ≤ 24 rounded icon tiles (90 px, `fx.icon` glyphs in the studio colour) and bill shapes (120×60, `good` 30%) falling in depth behind a title on W-void, blurred by depth (0–6 px) | Fall 30–60 px/s with slow spin ±20°/s, seeded positions; ≤ 5 s | Behind P-CHROME-TITLE / P-GLASS-SLAB on the void (F-B) | `ambient: true`, `exception: E4`, no text, no brand logos |

**B-7 CTA and link cards**
| ID | Type | What's on screen | Motion recipe | When | Flags |
|---|---|---|---|---|---|
| **P-LINK-CARD** | overlay (z6) | Dark glass card x 150–930, y 1250–1480 (radius 18): 16:9 thumbnail 300×169 left (SH-4 or FB-4), title 40 px 700 (2 lines), channel/meta 26 px | Blurs in + rises 24 px (10 f); holds; blurs out 6 f. If the caption block would end below y 1210, skip it in the hook (keep it for the CTA) | Hook tease (v01 @0:00–0:04), CTA (v01 @0:44–0:49) | TC-label + TC-legal |
| **P-VIDEO-CARD** | overlay (z8, `kind: end-card`) | A tall glass card x 230–850, y 1040–1500: thumbnail 620×349, title 40 px, meta 26 px ("Watch the full tutorial") | Grows from 30% at the chest centre to full in 12–15 f with a rim glow flash (v03 @0:48.73–0:49.13) while Z-3 pushes +8% and holds to the end; gentle float ±4 px; holds 2.5–4 s | F-A CTA `cross_promo` (v03 @0:49–0:52) | captions hidden while it shows |
| **P-KEYWORD-GLASS** | overlay (z8, `kind: cta-keyword`) | On L-dim: "DM OR COMMENT" (64 px, "OR" at 400 / 60%) at y 1240; the glass chip 520×150 (radius 26, 2 px rim, `good` glow 24 px at 40%) at y 1290–1440 with the keyword in quotes, 128 px | Lead line blurs in 8 f; chip rises 10 f, scale 0.9 → 1.0; breathes 1.0 → 1.03 → 1.0 every 1.2 s; holds to the last frame | F-B CTA, F-A `comment_keyword` | TC-display; one `backdrop-filter` allowed (the chip) |

**B-8 Creator media frames and third-party stand-ins**
| ID | Type | What's on screen | Motion recipe | When | Flags |
|---|---|---|---|---|---|
| **P-SCREEN-PANEL** | overlay (z8) | A tall white glass panel x 300–780 (480×640), y 860–1500, holding a screen recording or UI capture (`fx.shot` with `chrome: false`) | Rises 12 f with a white rim glow; the recording plays; exits with a fade + scale 0.96 (8 f) | Showing an app, a panel, a workflow (v03 @0:38–0:41) | content TC-decorative; creator asset |
| **P-STYLE-CARD** | overlay on W-void | A portrait card 340×600 at x 370–710, y 360–960 with a still or clip; the name in caps 900 italic 88 px at y 1040 + script tag "Style" | Card rises from smoke (blur 18 → 0, 12 f); name blurs in 8 f; tag 4 f later | Naming examples / modules / "styles you'll learn" (v05 @1:09–1:24) | creator asset or FB-3|
| **P-TILTED-GLASS-SHOTS** | overlay (z8) | 2–3 screenshots of real results in glass frames 620×300, rotateY −18°, rotateX 8°, offset stack over the chest y 1050–1450 | Each slides in from the right with rotateY −35° → −18° (12 f), 8 f stagger; float ±6 px | F-B proof ("explain this", "and this", "and even this", v05 @0:15–0:17) | creator screenshots (SH-5) or FB-5 quote cards; names/handles blurred (NC-14) |
| **P-SCREEN-WALL** | overlay on W-void | A perspective wall of 12 tiles (rotateY −28°, rotateX 14°) filling the frame, slow drift; a question in caps 900 italic 110 px (2 lines) on a 50% dark scrim | Wall drifts 20 px/s diagonally; the question blurs in per word (6 f) | F-B re-hook question (v05 @0:21–0:24) | tiles = creator stills or FB-3; text TC-display |

### 8.4 Line → pattern lookup `[NICHE]`
| Line type | Primary | Alternates |
|---|---|---|
| The hook promise ("This X is taking over…") | P-PROMISE-DUET + P-POSTER-ROW | P-LINK-CARD, P-STAR-RATING |
| "The reason you still can't…" | P-SHRINK-TO-CARD + P-STATCARDS | P-SEARCH-BAR |
| "It took me N years…" | P-RECURSION (SH-2) | P-CARD-CAROUSEL (FB-2) |
| "Here are N steps / tips / reasons" | P-DIAMOND-ROW | P-NUM-TILE-ROW (F-B) |
| An ordinal word ("first", "number two") | P-DIAMOND-MARKER (+ ritual §7.3) | P-NUM-TILE-ROW (F-B) |
| A visual process step | P-TUTORIAL-CARD + P-SPARKLE-BULLETS | P-PREVIEW-WINDOW + P-WINDOW-WIPE |
| "This looks like…", "use this font/setting" | P-PREVIEW-WINDOW + P-LEADER-LABEL | P-SCREEN-PANEL |
| Before → after | P-WINDOW-WIPE | P-TUTORIAL-CARD evolving |
| A list of settings / options in a tool | P-ROW-HIGHLIGHT in a P-SCREEN-PANEL | P-SPARKLE-BULLETS |
| A checklist / "make sure you…" | P-CHECKLIST-CARD | P-SPARKLE-BULLETS |
| Sub-points of a concept | P-LIGHT-BAR-LIST | P-PLAY-BULLETS |
| Consequences ("you'll get lost…") | P-PLAY-BULLETS | P-LIGHT-BAR-LIST |
| A one-word verdict ("Poor", "Bad") | P-OUTLINE-WORD under the marker | P-COLOUR-FLASH-WORD |
| A quality comparison | P-STAR-RATING | P-WINDOW-WIPE |
| "A plus B" | P-DUO-ICONS | — |
| "A vs B", two kinds of a thing | P-COMPARE-CARDS | P-WINDOW-WIPE |
| "All the tools / courses out there" | P-ORBIT-FACE | P-COURSE-STACK |
| "You search for…" | P-SEARCH-BAR | — |
| A free resource / file | P-APP-NOTICE | P-LINK-CARD |
| Another creator / mentor named | P-PROFILE-TILE (creator screenshot or created) | — |
| A punch word in a calm stretch | P-COLOUR-FLASH-WORD (≤ 2 per reel) | tier-2 caption only |
| What is <product>? (F-B) | P-CHROME-TITLE + P-FALLING-ICONS | P-COURSE-BANNER |
| What the product promises (F-B) | P-GLASS-SLAB | — |
| A money / result figure (F-B) | P-TRACKED-FIGURE | P-NEON-OUTLINE-FIGURE |
| Proof of results (F-B) | P-TILTED-GLASS-SHOTS | P-STATCARDS |
| A module / what's inside (F-B) | P-NUM-TILE-ROW + P-STYLE-CARD | P-SCREEN-PANEL |
| A re-hook question (F-B) | P-SCREEN-WALL | P-COLOUR-FLASH-WORD |
| CTA: watch the full video | P-VIDEO-CARD | P-LINK-CARD |
| CTA: DM / comment keyword | P-KEYWORD-GLASS | — |
| `[NICHE: example]` N1 fitness: "keep your knees out" | P-PREVIEW-WINDOW with the creator's clip + P-LEADER-LABEL "knees over toes" | P-WINDOW-WIPE (wrong → right rep) |
| `[NICHE: example]` N1 fitness: "your program needs these 3 things" | P-CHECKLIST-CARD | P-DIAMOND-ROW |
| `[NICHE: example]` N2 software: "go to Format → Theme" | P-SCREEN-PANEL + P-ROW-HIGHLIGHT | P-TUTORIAL-CARD |
| `[NICHE: example]` N2 software: "pick a font like this" | P-PREVIEW-WINDOW with the sample set in that font + P-LEADER-LABEL | — |

### 8.5 Data and truth rules
- Every number on screen is the creator's real figure (counts, views, results) or a value the script states; F-B figures go through `plan/figures.json` with `formula: none` and the spoken word (V-DATA).
- Income or result promises (F-B) carry "Results vary" while shown.
- Quantities stay honest: 4 stat cards show 4 real posts, a 5-star widget is a comparison device, never a real rating claim about a third party.

### 8.6 Comedy layer
OFF (profile.tone.comedy = off): no stickers, stamps, meme cues or roast marks.

### 8.7 Asset rules
- The creator's own exports, recordings, stills and screenshots first (SH-1…SH-6).
- Built mocks are generic and unbranded (`fx.appUI`, `fx.device`, glass cards with `fx.icon`).
- No stock footage, no AI stock scenes, no platform or product logos; app icons are `fx.icon` glyphs in the studio colour.
- Third-party material follows ask-then-create (§12.5); private data in screenshots is blurred (NC-14).

### 8.8 Density and variety
- An event every 0.8–2.0 s (captions included).
- ≥ 8 distinct patterns per 60 s (F-A), ≥ 10 per 120 s (F-B); ≥ 4 families per 60 s.
- The same pattern at most 2 beats in a row, except the marker ritual.
- ≤ 2 glass elements plus captions at once (H14).

---

## §9 Transitions `[REQ] [DNA]`

### 9.1 Library (30 fps)
| ID | Transition | Frames | Recipe | SFX role |
|---|---|---|---|---|
| **T-01** | Caption blur swap | 5 | The chunk blurs 0 → 10 px and fades while the next one blurs in (CS profiles) | none |
| **T-02** | Shrink-to-card | 16 | G-1: `shrink-to-card`, ease card; W-studio → W-pale crossfade 8 f; glow rises f6–f16 | soft whoosh |
| **T-03** | Grow-from-card | 12 | G-2: `grow-from-card`; W-pale fades over the last 6 f | soft whoosh (different file) |
| **T-04** | Push-cut into a world | 15–25 + 0 + 20 | G-3: Z-3 push on the face, hard `cut`, the world's card grows from the centre (or lands oversized and settles). Measured v01 @0:11.03, @0:24.13, @0:32.57, @0:38.53 | air whoosh on the cut |
| **T-05** | World hard cut back + land | 0 + 22–30 | G-4: the world eases out (~30 f), `cut` on the first frame of a sentence's first word, Z-0 land-settle on the face (v01 @0:18.07, @0:30.3, @0:36.47, @0:43.27; v03 @0:05.0); also into W-grid / W-void in F-B | none or a tick |
| **T-06** | Diamond emerge | 10 | P-DIAMOND-MARKER entry from the counting hand (not a scene change) | list cue |
| **T-07** | Directional blur exit | 6 | An element leaves with a 24 px directional blur toward its exit side and a 60 px travel (v05 @0:10, v01 @0:09): `filter:${ctx.blur(0 → 24, 0)}` (horizontal; 90 for a vertical exit) in a bespoke exit, or `out: "slide-l" / "slide-r", out_frames: 6, smear: true` | swish (optional) |
| **T-08** | Colour flash cut | 0 + hold | Hard cut into W-flat / W-pale with one word (P-COLOUR-FLASH-WORD), hard cut out | tick |
| **T-09** | Orbit bubble | 12 / 10 | G-5 `pip-shrink` / `pip-grow` | pop |
| **T-10** | Chrome fly-through exit | 8 | Scale 1.0 → 2.6 expo-in + 700 px downward travel + vertical smear 24 px (`ctx.blur(24, 90)`; the 3D title flies with `keys` instead); fade in the last 3 f (v05 @0:01.63–0:01.92) | whoosh |
| **T-11** | CTA dim | 10 | G-7 `dim` (blur 8, luma −0.25) | none |
| **T-12** | Colour-burn cut (F-B only) | 9 | Posterised, hue-shifted frames of the outgoing shot (magenta / cyan / green), a burnt-edged hole that opens from the centre and reveals the next shot, 1–2 near-white frames at the peak (v05 @0:03.71–0:04.0, @0:28.82–0:29.2): the built-in `{"t": <cut>, "type": "burn", "frames": 9, "pre": 2, "at": "centre", "colour": "#FF4FD8", "ring": 140, "peak": 1}`. ≤ 2 per reel, on a section turn or the guarantee; the engine's V-FLASH counts it as a luminous transition () | burn / glitch whoosh |
| **T-13** | Page scroll (F-B) | 12–16 | The whole pale/void layout scrolls up (ease-in, peak ≈ 130 px/f) and the next layout scrolls in from below (v05 @0:33.3–0:33.8, @0:41.3–0:41.5) | swish |
| **T-14** | Jump-cut reframe (F-B) | 0 | On a jump cut inside the take, alternate wide (1.0) and tight (≈ 1.25×) framing (v05 @0:06→0:07, @1:24→1:25, sheet estimate); a quote beat may open dim and snap up to full brightness with a 3 f +20% punch (v05 @0:20.4–0:20.6) | none |

### 9.2 Grammar
| Boundary | Use | Never |
|---|---|---|
| Frame 0 | Z-0 land + the first promise word's blur-in (no transition) | A fade from black, a flash |
| Hook → proof collage | T-02 | Hard cut to the pale world |
| Card → face | T-03 (sentence continues) or T-05 (new sentence) | Crossfade |
| Face → tutorial world | T-04 on the step's title words | Dissolve / blur-through, a cut without the push |
| Tutorial / void → face | T-05 on a sentence start (with Z-0) | Blur-through out; a cut that lands at 1.0 with no settle |
| New item | T-06 marker on the ordinal word + Z-1 | Any world change before the marker |
| F-B section turn / guarantee | T-12 (≤ 2) or T-13 | T-12 in F-A |
| F-B jump cut | T-14 (alternate wide / tight) | Two tight shots in a row |
| Element exits | blur-out 6 f or T-07 | Pops, scale-to-zero |
| Punch word | T-08 (≤ 2 per reel) | Zoom punch, shake |
| F-B title exit | T-10 | Hard pop-off |
| CTA | T-11 (F-B) or none (F-A video card) | Any whoosh in the 1.0 s before the CTA |
| Last word | Hard end ≤ 6 f after the last word | Black tail > 0.2 s, fade to black |

### 9.3 Shot grammar
OFF (spine talking_head; single camera, single speaker).

### 9.4 Budget (per 60 s; F-B per 120 s ×1.5)
- T-02/T-03 ≤ 2 pairs; T-04 ≤ 4 (v01 has 4 in 50 s); T-08 ≤ 2; T-09 ≤ 1; T-10 one per chrome title; T-12 ≤ 2 per reel (F-B); T-13 ≤ 2 (F-B).
- T-05 as needed (one per graphic-world exit).
- The same transition never 3× in a row, except T-06 in the marker ritual and T-01 (captions).

---

## §10 Motion, camera, layers, finishing `[REQ] [DNA; motion tokens TUNE ±15%]`

### 10.1 Motion tokens
| Token | Value |
|---|---|
| Lead | 2 f before the trigger onset (captions 1 f) |
| Entry ease | `cubic-bezier(0.22, 1, 0.36, 1)` (expo-out) |
| Exit ease | `cubic-bezier(0.64, 0, 0.78, 0)` |
| Glide ease | `cubic-bezier(0.65, 0, 0.35, 1)` (in-out) for travel between positions |
| Blur-in (every text and card) | opacity 0 → 1, blur 14 → 0 px, y +16 → 0, 8 f (caption words 6 f) |
| Blur-out | blur 0 → 12 px, opacity → 0, 6 f |
| Diamond emerge | opacity 0 → 1, scale 0.4 → 1.08 → 1.0, ~80 px glide from the counting hand, 10 f; row stagger 5 f; title wipe L → R 10 f |
| Card rise | y +60 → 0, blur 10 → 0, scale 0.96 → 1, 12 f (chest cards, link card) |
| Tutorial card grow | from 15% at frame centre, 20 f expo-out, 3% overshoot; world exit pull 1.0 → 0.94 over 30 f (ease-in) |
| Window open | thin line → full height (scaleY 0.05 → 1) from centre, 8–10 f; rim flash 0.9 → 0.55 |
| Bullet | sparkle spin 90° + scale 0 → 1 in 6 f; text blur-in 8 f; stagger ≥ 0.6 s |
| Leader line | dot 4 f → line 8 f → label 6 f |
| Chrome land / flare | 14 f / 18 f |
| Counter roll | 18 f ease-out, lands on the spoken number ±5 f |
| Float (ambient life on held glass) | ±8 px, 3 s sine, phase seeded per element |
| Typing | 1 character / 2 f |
| Hold | text ≥ 0.25 s per word; titles ≥ 10 f after built; markers ≥ 1.0 s |

### 10.2 Footage camera (zoom policy `slow_push`)
| ID | Preset | Recipe | Tone / use |
|---|---|---|---|
| **Z-0** | `land-settle` | lands at 1.22 and settles to 1.00 over 45 f (`land: 1.22`, `ease: "expoOut"`; half the travel by f12); on f0 add `blur: {"kind": "defocus", "px": 10, "frames": 3, "shape": "decay"}` | Frame 0. Measured: hook 1.20–1.25 → 1.0 in 40–50 f, f0–f2 blurred (v01, v04). A landing on f0 / a cut is exempt from the slow_push 0.12 cap |
| **Z-0b** | `land-back` | lands at 1.15 and settles to 1.00 over 24 f (`land: 1.15`, `ease: "expoOut"`) | The first frame of every cut back to the face. Measured 1.15 → 1.0 in 22–25 f (v01 @0:18.07, @0:30.3; v03 @0:05.0) |
| **Z-1** | `marker-push` | 1.00 → 1.08 in 20 f, expo-out, then held | `hype`, `awe`, `explain`: the count word and each marker word, a key claim. Measured +6–10% in 18–25 f, held 1.0–1.5 s (v04 @0:04.3, @0:21.1, @0:31.1, @0:41.8; v03 @0:13.7, @0:29.4, @0:42.1; v01 @0:05.6) |
| **Z-2** | `pull-out` | 1.08 → 1.00 over 20 f, expo-out; only after a Z-1 in the same stage segment | `win`, `cta`, the item's explanation starting (v04 @0:06.3–0:07.0) |
| **Z-3** | `push-drift` | 1.00 → 1.08 linear over the beat (15–25 f) | The lean-in before a T-04 cut (v01 @0:10.3–0:11.0); under the CTA video card, held to the last frame (v03 @0:48.9–0:49.9) |

Rules:
- Frequency: ≈ 1 Z-1 (+ its Z-2) per 10 s on L-full, plus Z-0 at f0 and Z-0b on every later face entry; nothing on other layouts (the tutorial card animates itself).
- Order on a face span: Z-0 / Z-0b → (Z-1 → Z-2)… → Z-3 before the next cut. Never the same preset twice in a row; never two moves within 0.4 s (NC-3).
- Measured rotation is 0 (≤ 0.1° per 0.5 s apart from body motion) and there is no shake: no rotation presets.
- No punches in F-A (N1); the only fast camera change is the F-B jump-cut reframe (T-14). A 1080p source holds ≤ 1.12× sharp: the Z-0 / Z-0b landings start above that and read slightly soft for their first ≈ 10 f while moving (as in the source); a buyer whose source is soft may lower `land` to 1.12. Z-1…Z-3 stay ≤ 1.12×.
- Whips (the built-in `whip`) are not used: the source never whips (N1).

### 10.3 Canvas camera
OFF (§21).

### 10.4 Layer order (back to front)
1. World background (W-studio footage, W-tutorial, W-pale, W-void, W-grid, W-flat)
2. Glow (world glows, P-FALLING-ICONS at z2)
3. Cards and collages (P-POSTER-ROW, P-STATCARDS, P-CARD-CAROUSEL side cards) — P-POSTER-ROW may be `behind` the cut-out
4. The presenter (footage, card, bubble)
5. Labels, outline words, glass slabs, link card (z5–z6)
6. Markers and rows (z6)
7. Auto-captions (z7)
8. Big type and chest windows (z8: P-PROMISE-DUET, P-DIAMOND-MARKER, P-PREVIEW-WINDOW, P-CHECKLIST-CARD, P-CHROME-TITLE, P-VIDEO-CARD, P-KEYWORD-GLASS); captions hide under them
9. (comedy: none)
10. (banner: none)
11. Light passes: the chrome flare, the P-WINDOW-WIPE light line

### 10.5 Finishing
- No grain, no vignette added (the engine's rule); the set's own look is kept.
- Glow only on glass rims, markers, the chrome title and the money figure; captions get a soft dark shadow only.
- Card radius 14 (windows), 18 (link card), 22–26 (tutorial and face cards); rims 2 px; no hard offset shadows.

---

## §11 Sound contract (minimal) `[REQ] [VAR]`
| Line | Decision |
|---|---|
| **Cue moments** | hook (f0 and the proof landing), reveals (cards, windows, chrome title, tutorial card), list cue (the diamond/tile entry on every item: the one allowed repeat), transitions (T-02/T-03/T-04/T-09/T-10/T-12/T-13 only), CTA (the keyword chip or video card landing) |
| **Meme cues** | off (comedy off) |
| **Music bed** | on; enters after the hook (on the "here are N" line or the first marker) |
| **Ducking** | the bed sits 20 dB under the voice while the voice speaks |
| **Loudness** | −14 LUFS integrated, true peak ≤ −1.5 dBTP; hard end ≤ 6 f after the last word (NC-8) |

The pack's calm/premium vibes apply (`tone.energy: calm`): soft whooshes, UI ticks, glassy shines; no hits louder than the pack's role defaults.

---

## §12 Footage, shot list, fallbacks, inserts `[REQ]`

### 12.1 Setups
| Setup | What the style assumes | Buyer's actual setup |
|---|---|---|
| **A Seated studio** | Seated chest-up, fixed camera, 9:16, 1080×1920 30 fps; head top y 180–360, chin y 700–860; one saturated backdrop light (violet / blue / teal / neon bars) and a rim light on the shoulders; a boom-arm mic in frame is fine (captions may cross the arm, never the face); plain dark tee or hoodie | VAR: recorded at setup or read at P1 |

### 12.2 Shot list
| ID | Shot | Spec | Count per 60 s | Must / optional | Formats |
|---|---|---|---|---|---|
| SH-1 | What is being taught | exports, stills or screen recordings of the result and its stages, 3–8 s each, any aspect | 2–6 | optional | F-A |
| SH-2 | An earlier reel | any 3–6 s span of an older reel of the creator, 9:16 | 0–1 | optional (HA-18 only) | F-A |
| SH-3 | Portfolio stills | 4–8 posters, thumbnails or stills of the creator's own work, 9:16 or 4:5 | 4–8 | optional | F-A, F-B |
| SH-4 | Link-card art | the long video's thumbnail + exact title (or the lead magnet's cover) | 0–1 | optional | F-A |
| SH-5 | Proof screenshots | 3–6 screenshots of real student/client results or messages | 2–4 | optional | F-B |
| SH-6 | Product art | the course/product cover and module thumbnails | 1–4 | optional | F-B |

### 12.3 Fallbacks
| ID | For | What the engine does instead | Fidelity cost | Result |
|---|---|---|---|---|
| FB-1 | SH-1 | Build the result live: a generic glass mock of the outcome (a poster card, an `fx.appUI` screen, a before/after tile) | The viewer sees an illustration, not the creator's real result | degraded |
| FB-2 | SH-2 | HA-18 becomes HA-02: P-SHRINK-TO-CARD + P-CARD-CAROUSEL with the creator's stills, or the take registered as a video asset (`veos asset add <take> --name take`) shown at other moments, dimmed 45% | The "old video inside the new video" wink is lost | holds |
| FB-3 | SH-3 | Gradient glass cards in the studio colour, each with one `fx.icon` of the niche and a 1–2 word title | No real work on show; reads as mood, not proof | degraded |
| FB-4 | SH-4 | A type-set 16:9 thumbnail: a still of the creator from this take, the video title in Inter Tight 800, a play glyph | none worth noting | holds |
| FB-5 | SH-5 | `fx.quoteCard` cards with the verbatim text the creator pastes; without text, skip proof cards and lean on the guarantee line | Screenshots read as more authentic | degraded |
| FB-6 | SH-6 | Glass product cards set in type (`fx.logoPlate` look): product name, module names | No cover art | holds |

Say at the checkpoint which fallbacks were used.

### 12.4 Props, reaction bank, matte, resolution
- Props: none.
- Reaction bank: none (no comedy).
- Matte: optional; run it only for P-POSTER-ROW behind the head.
- Resolution: 1080×1920 is enough (camera ≤ 1.12× when held; the landings start at 1.15–1.22 and settle); 720p sources are upscaled once at conform and get no push.

### 12.5 Third-party inserts: ask, then create `[REQ always]`
Claude never fetches anyone else's media.
1. **Analyse the transcript** (`veos inserts scan`) and list the moments that call for third-party material: another creator's profile or reel (P-PROFILE-TILE, P-STYLE-CARD), competitor courses (P-COURSE-STACK), a tool's UI (P-SCREEN-PANEL), a third-party post (P-TILTED-GLASS-SHOTS).
2. **Ask once:** "For these N moments, do you have a screenshot or clip? (drop the files, or say no)".
3. **Supplied:** use it as given, framed in glass, cropped and blurred for private data, never altered to say something it doesn't.
4. **Not supplied → create:**
   | Pattern | Created substitute |
   |---|---|
   | P-PROFILE-TILE | the generic profile tile (initials, the name as spoken, two decorative lines) |
   | P-STYLE-CARD (someone else's style) | a type-set card in the studio colour with the style's name; no imitation of their footage |
   | P-COURSE-STACK (other courses) | type-set glass cards with generic names ("Course A / B / C") or the names as spoken |
   | P-SCREEN-PANEL (a tool UI) | `fx.appUI` (list / settings / browser) recreated generically |
   | P-TILTED-GLASS-SHOTS (posts) | `fx.quoteCard` with the verbatim words the creator gives |
   | Brand / tool logos anywhere | `fx.logoPlate` (the name set in type) |
5. **Record** every insert in `plan/inserts.json` (`{id, moment, origin: creator | created, file?, substitute_of?}`); scenes carry `insert`.

### 12.6 Frame rate and audio
30 fps CFR output, 1080×1920, BT.709. Voice chain: high-pass 80 Hz, de-ess, light compression, −14 LUFS.

---

## §13 Output contract `[REQ] [DNA]`

### 13.1 Core beat fields
`id`, `section`, `t0`, `t1`, `spoken`, `trigger {word, at}`, `tone`, `line_type`, `layout`, `visual` (one sentence), `layers` (scene ids), `pattern`, `sfx`.

### 13.2 Conditional fields used by this style
| Field | When |
|---|---|
| `caption {profile, overrides[], emphasis[], tier[]}` | every beat (captions on); `tier` lists forced tier changes from the P5b pass |
| `ritual` (R-A, R-B or R-C) | every ITEM beat that opens an item |
| `ink [{mark, target, frames}]` (mark = leader_line, highlight_box or underline) | beats with P-LEADER-LABEL / P-ROW-HIGHLIGHT |
| `theme` | reel header only (per_reel) |
| `shot_id`, `fallback_used` | beats showing SH-1…SH-6 material or its FB |
| `insert {id, origin}` | third-party moments (§12.5) |
| `exception` (E3 or E4) | beats with leader labels, CS-2 captions or falling icons |
| `figure_id` | F-B beats with P-TRACKED-FIGURE / P-NEON-OUTLINE-FIGURE |

```yaml
- id: 7
  section: ITEM-1
  t0: 9.80
  t1: 11.40
  spoken: "First is the background"
  trigger: {word: "First", at: 9.86}
  tone: explain
  line_type: ordinal
  layout: L-full
  ritual: R-A
  pattern: P-DIAMOND-MARKER
  visual: "Glass diamond 1 emerges from the counting hand at chest left, title 'Creating the background' wipes in beside it; Z-1 push"
  layers: [dmk-1]
  caption: {profile: CS-1, overrides: [], emphasis: [], tier: []}
  sfx: [{t: 9.80, id: "<list-cue id>", on: "dmk-1@0", why: "item 1 marker flip"}]
```

### 13.3 Reel header
```yaml
format: F-A                 # F-A | F-B
theme: TH-violet            # from the P1b studio colour pick
hook_archetype: HA-05       # HA-05 | HA-02 | HA-07 | HA-18
structure: tutorial         # tutorial (F-A) | list (F-B)
count: 3                    # items / modules
keyword: "{{BV-08.keyword|KEYWORD}}"
cta: cross_promo            # cross_promo | comment_keyword | dm | link_bio
link_card: {title: "<exact title>", art: SH-4 | FB-4}
fallbacks: [FB-1]
```

### 13.4 Hook proposals (3)
```yaml
- name: "Trend promise + poster row"
  archetype: HA-05
  headline: "This slide style is taking over in 2026"
  hook_pair: {promise: "slide style taking over", proof: "4 of the creator's slide exports in a poster row + link card"}
  stoppers: [ST-1, ST-2, ST-3, ST-4, ST-5, ST-6]
  captions: {profile: CS-1, chunks: ["This slide style", "is taking over", "in 2026"], tier2: ["2026"]}
  storyboard: "f0 'This' blurs in + Z-0 land | 0.5 poster card 1 | 0.6 link card | 1.0 row fills | 2.2 '2026' lands | 4.0 proof exits"
  sound: [hook tick f0, reveal on row, text-pop on '2026']
  stopper_test: {thumbnail: pass, mute: pass, read_s: 1.1, changes_3s: 11, payoff_s: 0.5}
```

### 13.5 Checkpoint
Send:
1. 3 hooks with stopper tests and the chosen archetype.
2. The studio colour pick (theme) with the sampled hex.
3. The beat sheet with tones, rituals and the transition map.
4. The SFX ledger (bundled pack).
5. The type-voice pass: chunks whose tiers were forced, and why.
6. The inserts record (creator-supplied vs created) and the fallbacks used.
7. Style stills: f0, the proof landing (≈ 1.0 s), one marker, one tutorial card or chest window, the recap row, the CTA card.

**Wait for approval.**

---

## §14 Worked examples `[REQ] [NICHE: example]`
Times are estimates; replace them with `words.edit.json` onsets.

### 14.1 F-A, Niche 1 (fitness coaching): "3 reasons your squat isn't growing your glutes" (52 s, TH-violet, cross_promo)
**Hook (HA-07 live number, the star rating):**
| t (s) | Spoken | Visual | Caption | Layout / camera |
|---|---|---|---|---|
| f0 | "If you look at your squat…" | P-PROMISE-DUET "*If* you look *at your* squat" builds at chest; P-STAR-RATING "Your squat" 1 gold star, 4 empty, at y 1370–1484 | promise (CS-1 skin) | L-full; Z-0 from 0 |
| 1.2 | "…and you think" | the rating holds; one star pulses | "*and you* **think**" | — |
| 2.1 | "it looks nothing like a coach's" | label blur-swaps to "Coach-level"; stars fill 1 → 5 (4 f stagger) | "*it* looks nothing *like a* **coach's**" | — |
| 3.4 | "it's one of these three things" | rating blurs out; P-DIAMOND-ROW: 3 diamonds pop at y 1380 | "*one of these* **three** things" | Z-2 pull-out |

**Body:**
| Section | Spoken (gist) | Ritual | Patterns |
|---|---|---|---|
| Item 1 (5–17 s) | "First: your depth. Most people stop here…" | R-B | P-DIAMOND-MARKER "1 Depth" → P-PREVIEW-WINDOW with the creator's side-view clip (SH-1) + P-LEADER-LABEL "hip below knee" + P-WINDOW-WIPE half rep → full rep |
| Item 2 (17–30 s) | "Second: your stance… toes out, knees track…" | R-A | P-DIAMOND-MARKER "2 Stance" → T-04 → P-TUTORIAL-CARD: the stance still in the glass card, bullets "Feet shoulder-width", "Toes out 15°", "Knees over toes"; footer "Full breakdown on my YouTube"; T-05 back |
| Item 3 (30–41 s) | "Third, and the one nobody tracks: progression" | R-C | P-DIAMOND-MARKER "3 Progression" + P-OUTLINE-WORD "Poor" under it → P-CHECKLIST-CARD "Progression checklist": "Add 2.5 kg", "Log every set", "Deload week 5" |
| Recap (41–45 s) | "So next time your squat feels flat, check these three" | — | P-RECAP-ROW (1 2 3 lit) under the caption |
| CTA (45–52 s) | "The full program walkthrough is on my YouTube, go watch it" | — | P-VIDEO-CARD (SH-4 thumbnail, exact title, "Watch the full breakdown"), z8, 3.5 s; hard end |

### 14.2 F-A, Niche 2 (design & software tutorials): "This slide style is taking over in 2026" (48 s, TH-blue, cross_promo)
**Hook (HA-05 default):**
| t (s) | Spoken | Visual | Caption | Layout / camera |
|---|---|---|---|---|
| f0 | "This slide style…" | P-PROMISE-DUET "*This* slide style" at chest | promise | L-full; Z-0 from 0 |
| 0.5 | — | P-POSTER-ROW: 4 of the creator's slide exports (SH-3) slide in from the left behind the head (matte) | — | — |
| 0.6 | — | P-LINK-CARD rises (SH-4 thumbnail, "How to design minimal slides in 2026") | — | — |
| 1.1 | "…is taking over" | the row fills and drifts | "*is* taking over" | — |
| 2.2 | "in 2026" | tier-2 "2026" lands at 101 px (Jost 700) | "*In* **2026**" | — |
| 3.0 | "and every designer wants to learn it" | row and link card blur out (6 f) | CS-1 | — |
| 6.5 | "So here are three steps…" | P-DIAMOND-ROW (3) | "*So here are* **three** steps" | Z-2 |

**Body:**
| Section | Spoken (gist) | Ritual | Patterns |
|---|---|---|---|
| Step 1 (9–18 s) | "First, the background: pure white, a grid, a soft shadow" | R-A | P-DIAMOND-MARKER "1 The background" → T-04 → P-TUTORIAL-CARD: the blank slide evolving per bullet (white → grid → shadow, crossfade 8 f each), bullets "White background", "Subtle grid", "Soft shadow" |
| Step 2 (18–30 s) | "Two: one main object in the middle, desaturated" | R-A | marker "2 Main object" → tutorial card: object placed, then desaturated (P-WINDOW-WIPE); bullets "Centre it", "Desaturate", "Add texture" |
| Step 3 (30–40 s) | "Three: the type around it, a script and a sans" | R-B | marker "3 Typography" → P-PREVIEW-WINDOW with the finished slide + P-LEADER-LABEL "Sans: Inter Tight" and "Script: Pinyon" (both spoken) |
| Recap + CTA (40–48 s) | "Want the full walkthrough? It's on my YouTube" | — | P-RECAP-ROW → P-VIDEO-CARD (SH-4) |

### 14.3 F-B, Niche 2 (design course): "What is <COURSE NAME>?" (115 s, TH-neon, comment_keyword {{BV-08.keyword|KEYWORD}})
**Hook (HA-05 F-B):**
| t (s) | Spoken | Visual | Caption | Layout / camera |
|---|---|---|---|---|
| f0 | "What is…" | P-PROMISE-DUET "WHAT IS?" (CS-3 skin) | promise | L-full; Z-0 from 0 |
| 0.8 | "<COURSE NAME>?" | P-CHROME-TITLE lands at chest with flare | hidden | — |
| 1.6 | — | T-10 exit | — | — |
| 1.9 | "Well, something that's never been done before" | P-SCRIPT-TAG "Well," + CS-3 line | CS-3 | — |
| 3.8 | "a program that takes any beginner to their first paid client in 30 days" | — | "IN ONLY **30 DAYS**" | Z-2 |
| 9.5 | "making their first $1,000" (script-stated) | T-05 → W-grid P-TRACKED-FIGURE "MAKE $1,000 IN 30 DAYS" + "Results vary" | hidden | L-graphic |
| 12.5 | "Don't believe me? Explain this" | P-TILTED-GLASS-SHOTS (SH-5, names blurred) | CS-3 then hidden | L-full |

**Body:**
| Section | Spoken (gist) | Patterns |
|---|---|---|
| Re-hook 1 (~20 s) | "How is this different from the other courses?" | P-SCREEN-WALL with the question (FB-3 tiles) |
| What it is (24–38 s) | "Coaching, a community, a guarantee" | P-COURSE-BANNER; T-08 P-COLOUR-FLASH-WORD "Coaching" |
| Product reveal (38–49 s) | "Inside <COURSE NAME>…" | T-05 → W-void: P-CHROME-TITLE + P-GLASS-SLAB "MASTER SLIDE DESIGN" / "FIRST CLIENT IN 30 DAYS" + P-FALLING-ICONS (E4, 5 s) |
| Modules 1–4 (50–85 s) | "Module one, the basics…" | P-NUM-TILE-ROW per module (title + script tag) → P-STYLE-CARD of the module's best slide (SH-6/FB-6) |
| Re-hook 2 (~75 s) | "And the best part?" | P-COLOUR-FLASH-WORD "Guarantee" |
| Guarantee (85–100 s) | "If you don't land a client, I work with you until you do" | CS-3 tier-2 "GUARANTEE"; P-APP-NOTICE "Client guarantee" |
| Last re-hook + CTA (100–115 s) | "So what are you going to do? DM me or comment <KEYWORD>" | T-11 → L-dim, P-KEYWORD-GLASS holds to the last frame |

---

## §15 QA checklist `[REQ] [DNA]`

**1. Profile conformance**
- [ ] Format and theme declared; the theme matches the set colour (P1b). review
- [ ] Presence 45–85% (F-B 40–80%); longest absence ≤ 6.5 s (F-B 11 s). V-PRESENCE
- [ ] Duration in class (F-A 40–60 s, F-B 90–125 s). review

**2. Hook**
- [ ] f0: face full frame, Z-0 land-settle running, the first promise word blurring in by 0.3 s. V-F0
- [ ] First promise line readable by 0.7 s; a proof element by 2.5 s. V-F0 / review
- [ ] ≥ 6 SCs in 0–3 s; the mute test passes. V-CADENCE / review

**3. Body and cadence**
- [ ] 4–10 SCs per 10 s (F-B 3.5–9); no gap > 2.0 s; nothing static > 2.5 s. V-CADENCE
- [ ] A diamond/tile on every ordinal word; the count matches; the recap row shows all. V-PROMISE
- [ ] At least one R-A tutorial card when SH-1 or FB-1 material exists; ≥ 2 s of face between R-A items. review
- [ ] F-B re-hook every ~25 s. review

**4. Captions**
- [ ] Every word captioned outside z8 overlays and the tutorial world; sync ≤ 0.15 s lead. V-CAPTION
- [ ] Duet tiers: no all-script chunk; no number, brand or tier-2 word in script; ≤ 1 tier-2 per chunk. review (P5b)
- [ ] Captions below the chin; never across the face. V-FACE
- [ ] CS-2 under cards is ink on the pale world, 44 px. V-TYPE

**5. Modules**
- [ ] Ink: ≤ 3 marks on screen; leader labels 28–39 px only when redundant; marks exit with their window. V-TYPE / V-EXC
- [ ] Brand: link/video card title exact; keyword chip ≥ 1.5 s (F-B to the end). V-PROMISE

**6. Truth and inserts**
- [ ] Counts, ratings, results and testimonials are the creator's real ones; F-B earnings carry "Results vary". V-DATA / V-NUMFMT / review
- [ ] Every third-party moment is creator-supplied or a created substitute; private data blurred. V-INSERTS
- [ ] No platform or product logos. review

**7. Look**
- [ ] One studio hue family; ≤ 3 bright hues per frame. V-HUES
- [ ] Every graphic is glass (rim + glow); ≤ 2 glass elements + captions; ≤ 1 backdrop-filter. review
- [ ] Motion: blur-in/out, glides; no punches or shakes (F-A); Z-0 on every face entry, Z-1 + Z-2 on markers, Z-3 before T-04 cuts; world switches are cuts, never dissolves. V-CAMERA / G3

**8. Sound, end and export**
- [ ] Cues only on the allowed moments; list cue on markers; no cue in the 1.0 s before the CTA; bed after the hook. S1–S6
- [ ] −14 LUFS, TP ≤ −1.5 dBTP; hard end ≤ 6 f after the last word; 1080×1920 30 fps. qa

---

## Conditional modules (§16–§25)

§16 Frame template / chrome: OFF (profile.modules.chrome = false; the frame changes with every world and the markers move).

§17 Running state & anchored graphics: OFF (profile.modules.running_state = false, anchors = false; the diamond row is a marker, not a state variable, and ink targets are the style's own drawn elements).

§18 Data contract: OFF (profile.modules.data_figures = false). The few F-B figures (P-TRACKED-FIGURE, P-NEON-OUTLINE-FIGURE) still go through `plan/figures.json` with `formula: none` so V-DATA and V-NUMFMT check them (§8.5).

§19 Evidence & citations: OFF (profile.modules.citations = false). The §12.5 inserts flow stays on.

§20 Dialogue: OFF (single speaker).

§21 Canvas camera: OFF (graphics: support; PV-5).

### §22 Ink & annotation layer `[COND: modules.ink] [DNA look; TUNE colour]`
**Purpose:** thin, precise annotation lines that name the parts of what is shown, like a design spec (v01 @0:39–0:42, v03 @0:07–0:17, @0:24–0:28).

| Token | Value |
|---|---|
| Stroke | `paper` at 85% (TUNE: `accent`), 2 px (3 px on footage), no wobble, square caps |
| Anchor dot | 5 px radius, `accent`, 8 px glow |
| Draw-on | 8 f (dot 4 f first), no overshoot |
| Label | P-LEADER-LABEL type: Inter Tight 500, 30 px (E3 redundant), ≤ 4 words on ≤ 2 lines |
| Max on screen | 3 marks |

**Marks:**
| Mark | Recipe | Use |
|---|---|---|
| `leader_line` | dot on the target → straight line at 30–70° → label; line length 80–220 px | Naming a part ("Edges of the screen", "Sans font", "hip below knee") |
| `bracket` | a thin 2 px bracket along one edge of a window (height of the part) with the label at its centre | Naming a span (a margin, a range) |
| `highlight_box` | P-ROW-HIGHLIGHT: an `accent` 35% bar that glides between rows | Walking through a list in a UI |
| `underline` | a 3 px `accent` line under a title, drawn L → R in 10 f | P-CHECKLIST-CARD header |

**Rules:**
- Targets are points inside the style's own windows and cards (written as coordinates in the scene); no footage tracking.
- Marks never touch the face box; labels stay inside x 64–970, y 110–1500.
- Every mark exits with its window (no orphan lines).
- Labels repeat words that are spoken or shown larger (`data-redundant`), otherwise they are 40 px.

§23 Continuity: OFF (no morph chains; worlds change by cut or the card morph).

§24 Series furniture: OFF (profile.modules.series = false; VAR). When a buyer turns it on: a "Part {n}" glass chip, TC-label 40 px, top-left at (96, 150), lifetime `hook`, blur-in 8 f.

### §25 Brand, link cards and end cards `[COND: modules.brand] [DNA look; VAR assets]`
| Element | Spec |
|---|---|
| **Link card** (P-LINK-CARD) | Dark glass 780×230 at x 150, y 1250; thumbnail 300×169 (SH-4 or FB-4); title 40 px 700, exact; meta 26 px TC-legal (the creator's handle, or "Full tutorial"); hook tease ≤ 3.5 s and/or the CTA ≤ 4 s |
| **Video card** (P-VIDEO-CARD, `kind: end-card`) | Tall glass 620×460 at x 230, y 1040; holds 2.5–4 s (`brand.endcard.max_s` 4.0); the keyword or title readable ≥ 1.5 s |
| **Keyword chip** (P-KEYWORD-GLASS) | F-B and `comment_keyword` / `dm`; holds ≥ 3 s to the last frame |
| **Product card** (P-COURSE-BANNER) | The creator's own product in the studio colour; never a competitor's art |
| **Sponsor / app notice** | P-APP-NOTICE as the sponsor card: the product name set in type (or the sponsor's supplied logo), never over the face or a window; a TC-legal "Paid partnership" (BV-14 wording) visible ≥ 2 s and said in speech (NC-12) |
| **Rules** | End cards ≤ 4 s; black tail ≤ 0.2 s; the CTA runs on the face (L-full / L-dim), never on W-pale |

Link-card meta for this copy: {{BV-01.handle|@yourhandle}}.

---

## Part C. Exceptions and the non-overridable core

### C.1 Non-overridable core
NC-1…NC-14 of the structure apply unchanged. The ones this style touches most:
- **NC-1:** captions anchor to the chest because the face is high; a caption that would touch the face moves below it (engine `avoid_face`).
- **NC-4:** the script tier is 87 px and never under 70 px; the small sans tier is 56 px and never under 54 px; leader labels never under 28 px; CS-2 never under 40 px.
- **NC-5:** the link card, rating widget and tile rows stay above y 1500; nothing meaningful sits in the right-hand button column (x > 970, y 900–1540).
- **NC-6 / NC-7:** counts, results and screenshots are the creator's own; others' material is creator-supplied or created (§12.5).
- **NC-14:** names, handles and emails in proof screenshots are blurred.

### C.2 Declared exceptions (this style)
| ID | Token | Limits (≤ registry) | Where used | Off (VAR) means |
|---|---|---|---|---|
| **E3** quiet type | `exceptions.E3` | labels 28–39 px only with `redundant: true`; CS-2 at 44 px (≥ 40), weight ≥ 500, 1 line, ≤ 32 chars, contrast ≥ 7:1 | P-LEADER-LABEL, link-card meta (TC-legal anyway), CS-2 | Labels and CS-2 go to 40 px / 54 px |
| **E4** ambient field | `exceptions.E4` | ≤ 24 items, ≤ 6% of frame each, no text, ≤ 60 px/s, dim ≥ 40% under text, ≤ 5 s | P-FALLING-ICONS (F-B) | P-FALLING-ICONS is dropped; the void keeps its glow drift |

Scenes that rely on them set `exception: "E3"` / `"E4"`. No other bend: text over the mic arm is not an exception (props are not elements, structure C.2).

---

## Part D. Personalisation (path A)

### D.1 Branding questions (one round, ≤ 4, each with "keep the template default")
| ID | Question | Default | Feeds |
|---|---|---|---|
| BV-01 | Your name and handle | none | `creator.name/handle`, link-card meta |
| BV-02 | One or two brand colours for the glass (studio colour + glow), or "match my set per reel" | match the set (TH-violet / TH-blue / TH-teal / TH-neon) | `roles.primary`, `roles.accent` (all packs follow them) |
| BV-05 | The language you speak and the caption language | English ({{BV-05.speech|en}} → {{BV-05.captions|en}}) | `profile.language`, always asked: **English** → English captions (default) · **Hinglish** → romanised Hinglish captions · **Hindi** → Devanagari captions; numbers follow (BV-06) |
| BV-08 | Your call to action: a link to your long video, a comment/DM keyword, or link in bio | F-A: link to your YouTube tutorial; F-B: comment keyword | `profile.cta.chosen`, `creator.cta`, §6.7 |

Never asked (defaulted, changeable later): fonts (within each slot's class), formats enabled (both), theme packs, humour (off), number format (from BV-05), series (off), sponsor wording ("Paid partnership").

### D.2 Lock summary
| What | Lock |
|---|---|
| Duet captions (three tiers: small sans / big script / bold punch; chest anchor; blur reveal) | DNA (base size 54–62 px TUNE; offset 160–300 px TUNE) |
| Glass recipe, diamonds/tiles, tutorial card, chest window | DNA (glow strength TUNE) |
| Studio colour per reel | policy DNA; the colours VAR |
| Fonts | slots DNA; families TUNE inside their class |
| Hook archetype set | DNA; choice per reel VAR |
| Hook pairs, lookup rows, worked examples, headline bank | NICHE |
| Cadence, motion timings, layout rects | TUNE ±15% / ±5% |
| CTA device and keyword | VAR |
| E3 / E4 | DNA (switching off is VAR) |

### D.3 How copies change
Every tweak is classified by `locks` (`tokens.json`): VAR and in-range TUNE apply; DNA changes need confirmation and are logged as `DV-n`; NC changes are refused. Three or more DNA deviations (or one on captions.role, graphics, spine or source type) make the copy "derived".

### D.4 NICHE slots per reel
At P7 append the reel's hook pair to §6.4; at P8 append new line types to §8.4; after the first approved reel per format, it replaces that format's §14 example; approved promise lines go to App. A.

---

## Part E. Changes
| Version | Date | Change |
|---|---|---|
| v1 | 2026-10-06 | First template, from the Joseph's Work evidence (v01–v05). Status draft. |
| v1.1 | 2026-10-07 | Completeness audit (full-frame-rate motion): camera Z-0 land-settle / Z-1 marker-push / Z-2 / Z-3 replace the linear push from t 0; T-04 is a push-cut with a growing tutorial card (no blur-through); diamonds emerge from the counting hand; F-B transitions T-12 colour-burn, T-13 page scroll, T-14 jump-cut reframe; P-COMPARE-CARDS added. |
| v1.2 | 2026-10-07 | Engine built-ins: Z-0 lands from the measured 1.22 over 45 f with a 3 f f0 defocus (camera `land` + `blur`), new Z-0b land-back 1.15 / 24 f for cut-backs; T-12 = the built-in `burn` transition; T-07 / T-10 smears = `ctx.blur(px, angle)`; P-CHROME-TITLE as a lit 3D word (`fx.three`) with a 3D dolly through titles on the void. T-14 jump-cut reframe stays the preset + reset recipe (slow_push is reel-wide) |

## Part F. IDs used in this playbook
| Prefix | IDs |
|---|---|
| D | D1–D8 |
| H / N | H1–H17 / N1–N12 |
| E | E3, E4 |
| W | W-studio, W-tutorial, W-pale, W-void, W-grid, W-flat |
| L | L-full, L-card-pale, L-tutorial, L-pip-orbit, L-graphic, L-dim |
| G | G-1…G-7 |
| TH | TH-violet, TH-blue, TH-teal, TH-neon |
| CS | CS-1, CS-2, CS-3 |
| HA / ST | HA-05 (default), HA-02, HA-07, HA-18 / ST-1…ST-6 |
| SM | SM-GLASS-DIAMOND, SM-DIAMOND-ROW, SM-NUM-TILE |
| R (rituals) | R-A tutorial, R-B chest window, R-C concept |
| B | B-1…B-8 |
| P | 43 patterns (§8.3) |
| T | T-01…T-14 |
| Z | Z-0 land-settle, Z-1 marker-push, Z-2 pull-out, Z-3 push-drift |
| SH / FB | SH-1…SH-6 / FB-1…FB-6 |
| F | F-A Tutorial explainer, F-B Course sales |

---

## App. A Headline and hook bank `[NICHE]`
Slots in `<angle brackets>` are filled per reel. Tier-2 words in bold.

**F-A (promise lockups)**
| # | Promise line | Archetype | Niche example |
|---|---|---|---|
| 1 | "This **<style/method>** is taking over in **2026**" | HA-05 | "This slide style is taking over in 2026" |
| 2 | "If you look at your **<work>** and think it looks nothing like **<target>**" | HA-07 | "…your squat… nothing like a coach's" |
| 3 | "The reason you still can't **<result>**" | HA-02 | "The reason you still can't grow your glutes" |
| 4 | "It took me more than **<N> years** to build this" | HA-18 | "It took me 3 years to build this template system" |
| 5 | "Here are **<N>** things every **<role>** gets wrong" | HA-05 | "Here are 3 things every beginner lifter gets wrong" |
| 6 | "Stop doing **<habit>**. Do this instead" | HA-05 | "Stop doing cardio first. Do this instead" |
| 7 | "This is how pros **<do X>** in **<N> steps**" | HA-05 | "This is how pros build dashboards in 3 steps" |
| 8 | "Your **<thing>** looks **<adjective>** because of one setting" | HA-07 | "Your slides look amateur because of one setting" |
| 9 | "I tested **<N>** **<options>** so you don't have to" | HA-02 | "I tested 5 protein routines so you don't have to" |
| 10 | "Everyone is using the wrong **<tool>** for **<job>**" | HA-05 | "Everyone is using the wrong app for budgeting" |

**F-B (chrome titles and slabs)**
| # | Spoken opener | Chrome title | Glass slabs |
|---|---|---|---|
| 1 | "What is <product>?" | **<PRODUCT NAME>** | "MASTER <SKILL>" / "<RESULT> IN <N> DAYS" |
| 2 | "This is <product>" | **<PRODUCT NAME>** | "FROM ZERO TO <RESULT>" |
| 3 | "I built <product> for people who…" | **<PRODUCT NAME>** | "FOR <AUDIENCE>" / "<N> MODULES" |
| 4 | "Introducing <product>" | **<NAME> 2.0** | "NEW: <FEATURE>" |
| 5 | "What if you could <result> in <N> days?" | **<N>-DAY <OUTCOME>** | "STEP-BY-STEP" / "WITH COACHING" |
| 6 | "Don't buy another course until…" | **<PRODUCT NAME>** | "<GUARANTEE>" |
| 7 | "Here's everything inside <product>" | **INSIDE <NAME>** | "<N> MODULES" / "LIVE CALLS" |
| 8 | "My students did this…" | **<RESULT>** (only a real, script-stated result) | "RESULTS VARY" (TC-legal) |
| 9 | "How is this different?" | **NOT ANOTHER COURSE** | "COACHING" / "COMMUNITY" |
| 10 | "Last chance to join <product>" | **DOORS CLOSE <DAY>** | "DM <KEYWORD>" |

---

## App. B Evidence map
The full DNA → evidence trace is in `evidence.md` (templates only). Summary:
| Element | Evidence |
|---|---|
| Duet captions (script openers/content + small sans + bold punch word), chest height | v01 @0:00–0:03 (full-res audit @0:02.3, @0:03.0–0:03.6), v02 @0:00.3, v04 @0:00–0:17 (audit @0:01.5, @0:03.0) |
| Glass diamonds, rows, recap | v01 @0:07–0:10, v03 @0:03–0:43, v04 @0:05–0:06, @0:43–0:45 |
| Tutorial world with sparkle bullets and footer | v01 @0:11–0:17, @0:24–0:35 |
| Chest windows with leader labels | v03 @0:07–0:20, @0:24–0:28, @0:44–0:46 |
| Face shrinks into a card / carousel / recursion | v02 @0:00.6–0:03, v03 @0:00–0:04 |
| Studio colour per reel | v01/v04 violet, v02 blue, v03 teal, v05 neon |
| Chrome title, glass slabs, falling icons, number tiles, keyword chip | v05 @0:01, @0:39–0:49, @0:52–1:19, @1:54–2:00 |
| Link and video cards | v01 @0:00–0:04, @0:47–0:48; v03 @0:49–0:52 |
| (unverified) | speech language, exact hook wording, CTA wording, the duet tier sizes beyond the measured range |
