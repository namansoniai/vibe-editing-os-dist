# Graphic-First Explainer Style Playbook (template v1)

**Purpose.** This playbook makes you (Claude, the editor) turn {{BV-01.name|the creator}}'s talking-head take into a reel where **designed graphics carry the argument** and the presenter is a guest. Every sentence gets one full-frame, literal graphic from a closed design system (one theme per reel), replaced by a hard cut every 1.5–3 s, with 1–4-word pill captions hard-swapping on every spoken second and numbers that visibly move. Input (SW-01 `talking_head`): one vertical A-roll take plus the script; optional screen recordings, photos and clips the creator owns (§12).

**How to read it.** §0 sets the switches. §1 is the procedure: follow it in order. §2 holds the hard rules. §3–§10 are the look and the motion, §11 the sound contract, §12 the footage, §13 what you hand back, §14 worked plans, §15 QA. Modules §16–§25 follow; the ones this style switches off are one line each.

### Style DNA `[DNA]`
A reel in this style looks like a **designed publication that talks**. The frame is almost always a full-bleed graphic card built from one of three locked theme packs (a near-black editorial stage with cream and coral, a cream neo-brutalist grid with outlined window cards, or pink and sage blocks). Each idea is one card: an hourglass that drains while the day counter climbs, concentric rings that add one per loop, bars that climb on one axis, a billing card whose dollars tick up. Cards change by **hard cut** on the first word of the next idea (the cream and pink packs add one designed transition each: an iris wipe, a push). Every cut *to the presenter* lands zoomed in and **settles out** to rest in ≈ 0.7 s. The presenter appears in short doses (a 50/50 stack under the graphic, a full-frame claim, a ringed bubble beside a header) and is never the hero. A 1–4-word caption on a solid pill sits at the same height on every graphic frame, swapping chunk by chunk with no animation, for the whole reel.

**Copy these 5 things** (each points to the section that implements it):
1. **One full-screen designed graphic per idea, hard-cut every 1.5–3 s**, presenter on screen only 20–40% of runtime (§3.2, §7.3, §8.3).
2. **1–4-word chunk captions on a solid pill at y 1390–1450, hard-swapped** (seam on a stack, chest on full frame), on every spoken second (§5.3).
3. **One locked theme pack per reel**: TH-editorial, TH-brutal or TH-pinksage, never mixed (§4.3).
4. **The presenter as a guest**: a 50/50 stack under the graphic, a short full-frame claim, or a ringed bubble beside a header; never over a graphic (§3.2, §3.6).
5. **Numbers that move and come from figures**: counters, climbing bars, filling grids and tickers, all bound to `plan/figures.json` (§8.5, §18).

### Directives `[DNA]`
| # | Directive | Where it lives |
|---|---|---|
| D1 | **Every sentence gets a literal graphic.** The card shows the exact thing said: a week becomes an hourglass counting days, "96 machines" becomes 96 filled cells | §8.3, §8.4 |
| D2 | **The presenter is a guest in the layout.** Graphics own the frame; the face returns every ≤ 10 s (F-A) / ≤ 8 s (F-B) for a claim, a turn or the CTA | §3.6, H8 |
| D3 | **One theme per reel.** The pack is chosen at P7 and never changes inside the reel | §4.3, H12 |
| D4 | **Real numbers only, and they move.** Every number on screen is a figure with provenance and is animated (roll, tick, grow, fill) | §8.5, §18, H10 |
| D5 | **Hard cuts between ideas, motion inside an idea.** New idea = hard cut (or the theme's one transition, §9.1); same idea = the card evolves; every cut to the presenter settles out (Z-1/Z-2) | §9.2, §10.2 |
| D6 | **Captions never stop.** 1–4 words on a solid pill, the whole chunk at once, hard swap, same position on every graphic frame | §5.3, H11 |
| D7 | **Hook = a number already moving at frame 0** (HA-07) with the claim spoken over it | §6.2 |
| D8 | **Ads say the keyword twice.** F-B reels place the comment-keyword CTA mid-reel and again at the end | §6.7 |

**Buyer directives** `[VAR]`: BD1… (add yours here; they may only make the style stricter or more specific).

### Quick index
| § | What | Status |
|---|---|---|
| §0 | Style profile (switches, formats, themes) | ON |
| §1 | Procedure | ON |
| §2 | Hard rules, exceptions E3 + E6 | ON |
| §3 | Worlds, layouts L-graphic / L-stack / L-full / L-pip / L-cardtop, stage moves, safe zones | ON |
| §4 | Colour roles, theme packs TH-editorial / TH-brutal / TH-pinksage | ON |
| §5 | Type and the pill caption profile CS-1 | ON |
| §6 | Hooks: HA-07 default, HA-18, HA-02; headline formulas; CTA | ON |
| §7 | Structure (F-A explainer, F-B list), rituals, cadence | ON |
| §8 | Visual system: 52 patterns P-01…P-52 | ON |
| §9 | Transitions and shot grammar | ON |
| §10 | Motion tokens, camera (crop-on-cut), layers, finishing | ON |
| §11 | Sound contract | ON |
| §12 | Footage, shot list, fallbacks, inserts | ON |
| §13 | Output contract | ON |
| §14 | Worked examples (3) | ON |
| §15 | QA checklist | ON |
| §16 | Frame template / chrome | OFF |
| §17 | Running state & anchors | OFF |
| §18 | Data contract | **ON** |
| §19 | Evidence & citations | **ON** (F-A cards; F-B quotes only) |
| §20 | Dialogue | OFF |
| §21 | Canvas camera | OFF |
| §22 | Ink & annotation | OFF |
| §23 | Continuity | OFF |
| §24 | Series furniture | OFF (VAR) |
| §25 | Sponsor, brand & end cards | **ON** |
| App. A | Headline & hook bank (20) | ON |
| App. B | Evidence map | ON (`evidence.md`) |

**Formats:** `F-A` Editorial figure explainer (default) · `F-B` Ad card. **Themes:** `TH-editorial` (F-A default) · `TH-brutal` (F-B default) · `TH-pinksage`.

---

## §0 Style profile `[REQ]`

```yaml
profile:                         # mirrored in tokens.json -> profile
  source_type: talking_head
  presenter: {presence: guest, share: [20, 40], max_absence_s: 10}      # F-A [20,35]/10 s, F-B [25,40]/8 s
  spine: hybrid
  captions: {mode: full, role: support, mute_policy: mute_safe}
  graphics: primary
  duration: {class: short, target_s: [35, 60]}                          # F-A standard [50,80], F-B short [35,55]
  language: {speech: en, captions: {lang: en, script: Latn, transform: verbatim}, on_screen: en, post_title: en,
             supported: [[en, en, Latn], [hinglish, hinglish, Latn], [hi, hi, Deva]]}
  numbers: {grouping: international, currency: "$", compact: k_m_b, units: metric, decimals: 0, compact_decimals: 1}
  tone: {energy: balanced, comedy: off, comedy_max: off}
  themes: {policy: per_reel, packs: [TH-editorial, TH-brutal, TH-pinksage], default: TH-editorial}  # F-B default TH-brutal
  formats: {list: [F-A, F-B], default: F-A}
  footage_dependency: low
  cta: {devices: [comment_keyword, dm, link_bio, none], placement: mid+end}   # F-A: end
  modules: {chrome: false, running_state: false, anchors: false, data_figures: true, citations: true,
            dialogue: false, canvas_camera: false, ink: false, continuity: false, series: false, brand: true}
```

Why each switch has its value:
- **source_type: talking_head**: the voice comes from one seated vertical take in all three reels (v01–v03); the interview clips in v01 are creator-held inserts (§12.5), not the spine.
- **presenter: guest [20, 40]**: face on screen about 22% (v01), 20% + 17% bubble (v02), 38% (v03). The measured absences run to 18–24 s (v01 0:27–0:45, v02 0:16–0:41); the template caps them at **10 s (F-A) / 8 s (F-B)** because a buyer's face is less known than the source brand. This is a deliberate tightening; TUNE 6–14 s.
- **spine: hybrid**: the A-roll carries the voice, but the picture is chosen per sentence and the graphics are equals of the footage (cuts land on sentence starts, not on the presenter's gestures).
- **captions: full / support / mute_safe**: a pill caption on every spoken second in all three reels (v01 0:02–1:14, v02 0:00–0:46, v03 0:00–0:42); the graphics, not the captions, are the strongest element.
- **graphics: primary**: 55–75% of runtime is full-bleed designed graphics (v01 ≈ 75%, v02 ≈ 65%, v03 ≈ 55%).
- **duration**: v01 75 s (an explainer: F-A `standard`), v02 47 s and v03 44 s (ads: F-B `short`).
- **language: en**: the only style with transcripts; all three are English. Hinglish speech is supported for buyers (captions English or romanised Hinglish).
- **numbers: international $ k_m_b**: "$2,000", "$449", "96 CPUs", "193.6x" (v01, v03). BV-06 switches to Indian grouping + ₹ when the buyer speaks an Indian language.
- **tone: balanced / comedy off**: informational, fast, no roast layer. v03's one film clip is third-party and is never fetched (§12.5); no comedy layer replaces it.
- **themes: per_reel**: three distinct packs across three reels (v01 dark editorial, v02 cream neo-brutalist, v03 pink and sage).
- **formats**: v01 is a figure explainer, v02/v03 are ad cards; they share the five traits above, so they are one style with two formats.
- **footage_dependency: low**: the style is built in the engine; recordings, photos and clips are optional and have fallbacks.
- **cta: comment_keyword ×2**: "comment CONTENT" at 0:12 and 0:44 (v02), "comment JEV" at 0:21 and 0:41 (v03). v01 has no CTA, so F-A places it at the end only.
- **modules**: data figures (every number animates), citations (FIG + SRC lines on every F-A card), brand (promo carousel + comment sheet). **running_state is off** although the coverage table lists counters: in all three reels every counter lives inside one figure and nothing persists across a cut, so counters are §18 figures. Chrome is off: the FIG line belongs to each card, not to a persistent slot.

### 0.4 Formats `[DNA set; VAR enable]`

| Field | F-A "Editorial figure explainer" | F-B "Ad card" |
|---|---|---|
| `when` | Explaining a result, a study, a launch, a record, a market move, a "how it works" story | Offers, courses, launches, tools, events, "N ways / N use cases" pitches |
| Profile overrides | presenter [20, 35], max absence 10 s; duration `standard` [50, 80]; theme default TH-editorial; CTA placement `end` | presenter [25, 40], max absence 8 s; duration `short` [35, 55]; theme default TH-brutal; CTA placement `mid+end` |
| Layouts | L-graphic, L-stack, L-full | L-graphic, L-stack, L-full, L-pip, L-cardtop |
| Default hook | HA-07 live number (editorial counter + title slab) | HA-07 live number (ticker card); HA-02 when the opening line has no number |
| Allowed hooks | HA-07, HA-18, HA-02 | HA-07, HA-02 |
| Structure | `explainer`: claim → mechanism figures → turn → verification → caveat → payoff | `list`: pain/claim → product → items (numeral cards) → proof → CTA ×2 |
| Markers | SM-FIG (`FIG. 01` … on every card) | SM-NUMERAL (full-screen numeral cards) |
| Headline | Title slab (plate), hook only | Slug pill + 2-line section header (lockup), per section |
| Captions | CS-1: Plus Jakarta Sans 600 54 px, sentence case, pill `#0B0A0A` (editorial), cy 1390 | CS-1 override: Poppins 700 48 px, as spoken, pill `#DF2E2B` (brutal) / `#DF2C14` (pinksage), cy 1450 on graphics |
| Numerals | Instrument Serif (`numeric` slot) | Poppins 800 with ink stroke + hard shadow |
| Citations | SRC line required on every card | Off (quotes keep their attribution) |

**Shared DNA (one line):** the same closed design system: one theme per reel, a full-frame designed graphic per idea replaced by a hard cut every 1.5–3 s, chunked pill captions, numbers that move, the presenter as a guest.

**Format pick (P7, decided):** if the script explains *what happened or how something works* and is not selling, use **F-A**. If the script sells, invites, announces or lists use cases, use **F-B**. A reel never mixes them.

### 0.5 Theme packs `[DNA policy; VAR colours]`
Policy `per_reel`. Packs, hexes and the pick rule are in §4.3. With the buyer's brand colours (BV-02), `primary` and `accent` are replaced in every pack; `pill`, `card`, `line`, `mute`, `highlight` and the worlds keep each pack's values.

---

## §1 Procedure (follow in order) `[REQ] [DNA]`

This style's craft is the **claim → figure pairing** (P5/P8): every sentence is paired with one figure pattern before anything is built, and every number in that sentence becomes a figure in `plan/figures.json`.

1. **P1 Inventory.** `ffprobe` every input (resolution, fps, duration, audio). Conform VFR to 30 fps CFR. Identify the A-roll setup (§12.1). Register every extra file with its origin: `veos asset add <file> --origin creator` (screen recordings, photos, logos, clips). Nothing is fetched (NC-7).
2. **P2 Prepare.** No matte (no behind-subject type in this style). Check the A-roll framing: eyes at 38–42% of frame height, head top at y 260–420. If the head top is above y 260, plan L-cardtop out of this reel (its card would touch the face).
3. **P3 Transcribe** with word timestamps. Apply `language.captions.transform` (verbatim for English; translate or transliterate for Hinglish, §5.5). Apply the glossary (brand and tool names exact).
4. **P4 Segment.**
   - F-A: into **figures**: one unit per sentence or clause that carries one idea (a number, a mechanism, a person, a turn). A 75 s explainer has 14–20 figures.
   - F-B: into **sections**: HOOK, PRODUCT, ITEM-1…n (each opened by a numeral card), PROOF, CTA-MID, BENEFIT, CTA-END.
5. **P5 Classify** every sentence with a line type (§8.4) and mark its **trigger word** (the noun or number its figure lands on).
6. **P6 Tone-tag** every sentence: `claim` · `explain` · `proof` · `warn` · `win` · `cta`. The tone picks the role colour and whether the presenter shows (§10, tone treatment).
7. **P7 Hook plan.**
   - Pick the format (§0.4) and the theme (§4.3).
   - Pick the archetype: HA-07 by default; HA-02 for an F-B opening line with no number; HA-18 only if the creator supplied a source clip (SH-3).
   - Write **3 hook variants** (§13.4), each with its headline (F-A title slab or F-B section header) and the live number it opens on. Run the stopper tests (§6.1).
8. **P8 Visual plan.**
   - A pattern per sentence from §8.4 (the pairing).
   - **Data check (module step, §18):** for each figure, write its inputs with provenance (`script` + the words, `creator`, `source:`), its formula, its steps aligned to spoken words, and its `scale_id`. Recompute with `veos figures --project P`. Flag every mismatch with the script at the checkpoint.
   - **Citation capture (F-A):** the SRC line for every card (outlet + month), FIG numbers in order, and the exact quote for every P-09 quote note.
   - **Inserts (§12.5):** run `veos inserts scan`, list the third-party moments (people's photos, other people's posts, product UIs, source clips), ask the creator once, record the answers in `plan/inserts.json`.
9. **P9 Beat sheet** (§13): one beat per figure or card state, meeting the cadence (§7.6): a weight-1 change every ≤ 2.0 s, a hard cut every 1.5–3.0 s, the presenter back every ≤ 10 s (F-A) / 8 s (F-B).
10. **P10 SFX ledger** (§11) and the transition map (§9.3).
11. **P11 Assets.** Build every card as a scene (§8.3 engine mapping). Resolve fallbacks (§12.3) and list the ones used.
12. **P12 Checkpoint** (§13.5), then **wait for approval.**
13. **P13 Build:** act by act; `veos scenes-meta` → `veos measure` → `veos validate` (global checks + the registry in tokens); preview and QA (§15, at most 3 passes); render.

---

## §2 Hard rules `[REQ] [DNA]`

### 2.1 Editing rules (every style)
The ten editing rules in `playbooks/_global/GLOBAL-RULES.md` apply. They are directions, not limits: smooth, seamless motion; nothing overlaps by accident; keep the face clear (behind the speaker is fair game, text included); readable at a glance; one idea at a time; show the thing, not the word; say what was said; hook titles hook; pace like the style, not like a timer; the style decides the look.
- **Facts the engine checks:** accidental overlaps, jumps, the face covered, unreadable text, numbers and quotes that don't match what was said, the promised count. Every count, timing and budget this playbook gives is direction for the edit, not a limit.
- **Picture first, in this style's own look:** every key beat shows the thing being said (an object, a screen or app, a diagram, numbers in motion), not just its word; text supports the picture and never replaces it. When the speaker points with words ("this, this and this", "from this to this", "ye dekho"), show what they mean. Illustrations may use made-up but realistic numbers and names ("212 views", "1.2M views"), with no label; a number or quote the speaker says is shown as said. This overrides any rule below that bans made-up numbers or asks for an example tag: those rules now cover claims (the creator's results, prices, benchmarks, testimonials), not illustrations.
- **Hook titles hook:** the on-screen title promises the viewer something (an outcome, a curiosity gap, who it's for) and is true to what the reel delivers; it need not repeat the spoken words. This playbook sets its shape (§5.2, §6.5: lines, sizes, word limits, case), never its voice (§6).
- **Retired (8 Oct 2026), whatever this playbook says below:** no REPRESENTATIONAL or example labels on made-up cards, no credit lines, no flash limit (flash as often as this style calls for; any "NC-11" cap below no longer applies), and text may sit behind the speaker without an exception.

### 2.2 Declared exceptions
| E-id | Style limits (≤ registry) | DNA reason | Evidence |
|---|---|---|---|
| **E3 Quiet type** | F-B subtitles **46–53 px** (F-A captions are 54 px since the 2026-10 audit and no longer need E3), weight ≥ 600, 1 line, ≤ 26 characters, always on a solid pill (contrast ≥ 4.5:1 on the pill). Labels **30–39 px** only for mono micro labels marked `redundant` (the same word or number is spoken or shown larger). Display stays ≥ 40 px. | The small, quiet pill caption under a dominant graphic is the look; 54 px captions would compete with the figure | Captions first estimated 42–46 px from sheets; full-res re-measure (2026-10): F-A 52–54 px (v01 @0:40 "and fixed" 244 px wide, 42 px ascender height), F-B ≈ 46–48 px (v02 @0:00–0:03) (v01 0:06 "This was", v02 0:00 "This", v03 0:08 "you pay"); mono micro labels ("DAYS", "LOOPS · THE RECORD", "CPUs RUNNING") v01 0:02–0:44 |
| **E6 Hard swap** | Only counter digits and ticker values inside a fixed-width value box (`data-slot`, ±4 px). The box's own entry and exit stay eased. | Billing tickers and day counters tick in discrete steps, not smooth rolls | v03 0:00–0:02 ($37 → $449 in steps of ≈ $22 every 0.17 s); v01 0:02–0:05 (3 → 7 DAYS) |

No other exception. In particular the v02 header that runs **under** the face bubble (0:00–0:08, "LEARN AI B|") is **not allowed** (structure Part C): the header stops 40 px left of the bubble (§3.4).

### 2.3 Style MUST rules
- **H1 Frame 0 is a live number.** f0 shows a figure scene (`kind: counter | number | figure | data_row | stat`) already moving (entrance or events at t 0) plus the claim: the caption of the first word or the headline. check: V-F0
- **H2 Cadence.** Body: 7–16 weighted state changes per 10 s (captions weigh 0.5); a weight-1 change every ≤ 2.0 s (hook ≤ 1.2 s); nothing static > 2.5 s; ≥ 6 weighted changes in 0–3 s. check: V-CADENCE
- **H3 Payoff by 1.0 s.** The opening figure lands its first value by 1.0 s (HA-07); the reel's result number (money, time, count, % ) lands by 6.0 s. check: V-F0 (first value) + review (result)
- **H4 Headline limits.** F-A title slab: ≤ 5 words, 2 lines, ≤ 16 characters per line, caps, readable at 25% in ≤ 1.2 s, hook only. F-B section header: ≤ 6 words, 2 lines, ≤ 12 characters per line, slug ≤ 16 characters. check: V-TITLE
- **H5 Hard cut per idea.** A new idea starts with a hard cut (stage or scene swap on a declared `cuts` time) on its first content word ±2 f; the same idea never hard-cuts mid-sentence. Graphic holds are 1.5–3.0 s (F-A ≤ 7.5 s when the card keeps an event every ≤ 2.0 s: v01 holds 2–7.6 s between hard cuts, median 3.0 s). check: review + V-CADENCE
- **H6 On-the-word visuals.** Every figure, number, name and object lands 2 f before its trigger word and is fully on within ±5 f; counters land on the spoken number within ±5 f. check: V-ONWORD + V-DATA
- **H7 Face rule.** No graphic or text over the presenter's face box in any layout; captions on L-full sit at the chest (cy 1290) and move below the chin when the face is lower (`avoid_face`). Cards in L-cardtop end ≥ 40 px above the face top. check: V-FACE
- **H8 Presence.** Presenter visible 20–35% (F-A) / 25–40% (F-B) of runtime; never absent longer than 10 s (F-A) / 8 s (F-B). check: V-PRESENCE
- **H9 Promise integrity.** Numeral cards count the items said ("two use cases" = two numeral cards); the CTA keyword is on screen ≥ 1.5 s each time it is said; the deliverable title on the promo card is the one spoken. check: V-PROMISE
- **H10 Truth.** Every number on screen is a figure in `plan/figures.json` with provenance (script words, creator, or a cited source) and is written with `ctx.fmtNum`; illustrative curves carry the "example" tag and no axis numbers. check: V-DATA
- **H11 Captions.** CS-1 on every spoken word, 1–4 words, ≤ 26 characters, the whole chunk on at once and hard-swapped (0 f), ≤ 0.15 s lead; hidden only under a z8 type scene (P-38 word stack, P-48 keyword card) and during stage morphs. check: V-CAPTION
- **H12 One theme.** One theme pack per reel, declared in the reel header; no world from another pack. check: V-THEME (review until registered)
- **H13 Layouts.** Only the format's layouts (F-A: L-graphic, L-stack, L-full; F-B adds L-pip, L-cardtop), within their runtime shares (§3.2). check: V-LAYOUT
- **H14 Sources (F-A).** Every F-A card carries the FIG line with a monotonic FIG number and an SRC line; every quote is verbatim and attributed. check: V-CITE + V-INSERTS
- **H15 Number format.** Grouping, currency and compact system follow `profile.numbers` (international `$2,000`, `$1.2M`; Indian `₹1,20,000`, `₹1.2 L` when BV-06 is Indian). check: V-NUMFMT
- **H16 Spelling.** Brand, tool and people's names exact, in captions and on cards (glossary). check: V-CAPTION
- **H17 Audio.** −14 LUFS integrated, true peak ≤ −1.5 dBTP, bed ≥ 18 dB under the voice, hard end ≤ 6 f after the last word. check: NC-8 (mix)
- **H18 Determinism.** Particles, tickets, scatter and grids use `ctx.rng(seed)` / `ctx.rngStable(seed)`; nothing reads time. check: NC-9 (review)

### 2.4 NEVER
- **N1** A presenter frame with a graphic floating over the face, or text running under the PiP bubble (v02's clipped header).
- **N2** Two theme packs in one reel; a world colour that is not the active pack's.
- **N3** Crossfades, dissolves, glitch packs, light leaks, zoom-throughs between ideas. Ideas change by hard cut or the active theme's own transition (§9.1); never another theme's.
- **N4** Punch-ins, crash zooms, shakes or slow drifts on the presenter. The only camera move is the cut-in settle (Z-1 / Z-2), which starts on a hard cut and only ever zooms **out**.
- **N5** A static number on a card: numbers roll, tick, grow, fill or draw (D4).
- **N6** Invented numbers, "decorative" metrics, fake dashboards, fake comment threads, fake likes, fake testimonials (NC-6). The comment sheet (P-50) shows only the keyword being typed.
- **N7** Stock footage, film or TV clips, memes, AI-generated people, other creators' thumbnails, fetched logos (NC-7). Brand names without a supplied logo are set in type (P-46).
- **N8** Readable real code or logs as the point of a card. Code-shaped lines are `TC-decorative` texture; the meaning sits on a pill (P-11).
- **N9** Contrast failures: primary-orange text on the cream world below 3:1 (use the deepened `#DB5320` at ≥ 96 px, or put it on a chip); white numerals on pink without the ink stroke; red text on the dark stage without a chip.
- **N10** More than 3 bright hues in one frame (primary + accent + one of bad/good/highlight).
- **N11** Coloured or emphasised words inside captions (emphasis is off: the graphic does the emphasis).
- **N12** Decoration that is not the world: stars, squiggles and dot matrices live only in the z1 decor band of TH-brutal (P-51), never as z3–10 elements.
- **N13** A black tail > 0.2 s, or an end card longer than 3.5 s.

---

## §3 Worlds, layouts, stage moves, safe zones `[REQ] [DNA; coordinates TUNE ±5%]`

### 3.1 Worlds (colours come from the active theme, §4.3)
| ID | Kind | Look (per theme) | Carries | Enter / exit |
|---|---|---|---|---|
| **W-main** | stage (editorial) / canvas (brutal, pinksage) | Editorial: `#141210`, film grain 0.06, vignette 0.30. Brutal: cream `#FBF3E4` with a 48 px grid (`#EADCC4`, 2 px, 80%). Pinksage: pink `#F4849C`, grain 0.05 | Every figure card, numeral card, window card | Hard cut |
| **W-alt** | canvas | Editorial: cream graph paper `#EDE6D6`, 72 px grid `#CFC5B0`. Brutal: blush `#F6D9D5`. Pinksage: sage `#A9B9B4` | The "different kind of figure" card: concept maps, slider matrices (editorial); a second card family to alternate (pinksage alternates pink ↔ sage on every hard cut inside a section) | Hard cut |
| **W-dark** | stage | `#161515`, grain 0.02 (all themes) | Screen recordings and recreated app UIs (P-45, P-10 in brutal/pinksage reels) | Hard cut |
| **W-promo** | card-world | Gradient `#120A0A → #C9341F → #F7C2B5` top to bottom (all themes) | The promo carousel (P-49) only | Hard cut, ≤ 2.5 s |

World rules:
- **W-main carries ≥ 60% of graphic time.** W-alt is a contrast beat, ≤ 1 in 3 cards (pinksage excepted: it alternates).
- Pinksage alternation: card k on W-main, card k+1 on W-alt, by hard cut (v03 0:03–0:20).
- The world switch is the hard cut itself: never fade worlds (`fade` unset).

### 3.2 Layout library
| ID | Engine | Presenter rect | Graphic rect | Caption | Share F-A | Share F-B | Evidence |
|---|---|---|---|---|---|---|---|
| **L-graphic** | `hidden` | none | full frame; content zone x 64–1016, y 300–1320 (FIG line at y 232) | fixed y, cy **1390** (F-B 1450) | 55–75% | 40–65% | v01 0:02–0:13, v02 0:18–0:40, v03 0:03–0:20 |
| **L-stack** | `stack`, seam_y **960**, top `graphic`, bottom `footage` (face 0.34 of the band, eyes at 0.40) | x 0–1080, y 960–1920 | x 0–1080, y 0–960; content band x 64–1016, **y 140–880** | on the seam (cy 960) | 8–25% | 5–20% | v01 0:00–0:01, 0:14–0:17, 0:45–0:50, 1:03, 1:12–1:14; v03 0:00–0:02, 0:32–0:34 |
| **L-full** | `full` | full frame | none (z8 type only: P-38, P-48) | fixed y, cy **1290** (chest) | 8–20% | 15–30% | v01 0:09–0:10, 0:26, 1:06; v02 0:09–0:15, 0:41; v03 0:02, 0:21–0:23, 0:38–0:39 |
| **L-pip** | `pip`, circle **d 420** at (816, 330), ring **10 px `primary`**, face 0.55 | circle x 606–1026, y 120–540 | full frame; header x 64–566 (stops 40 px left of the ring) | fixed y, cy **1440** | — | 0–20% | v02 0:00–0:08 (orange-ringed bubble top-right) |
| **L-cardtop** | `low`, offset **380** | footage lowered 380 px | card x 64–1016, y 130 → (face top − 40), max 600 | fixed y, cy **1430** | — | 0–12% | v02 0:09–0:11 (stopwatch card above the presenter) |

**Layout schedule (decided):**
- F-A: L-graphic is the home. L-stack for (a) the hook, (b) a figure the presenter comments on (opinion, caveat, "it used methods that…"), 1.5–5 s. L-full for a turn or caveat ("Now, this isn't…", "Then…"), 1.0–2.5 s, on the turn word.
- F-B: L-stack or L-pip open the reel; L-full for claims, pains and both CTAs (≤ 4.0 s per run); L-cardtop for one proof card about the presenter's own experience ("it took me only…"); L-graphic for everything else.
- Every layout change is a hard cut on a word boundary (`via: "cut"`), never a morph (D5).
- A run of L-full longer than 4.0 s is split by a hard cut to a graphic (budgets.full_frame_presenter_max_s).

### 3.3 Stage moves
| ID | Move | Recipe | Use |
|---|---|---|---|
| **G-1** | Hard cut to graphic | Stage → `hidden` (L-graphic) with `via: "cut"` on the first content word (lead 2 f); the new card's object starts its entrance on the same frame | Presenter → figure (the default move) |
| **G-2** | Hard cut to stack | Stage → L-stack, `via: "cut"` + **Z-2** settle on the footage; the top band shows the current or next figure re-laid for the band (y 140–880) and settles with it (band scene scale 1.40 → 1 over 22 f, expo-out, about the band centre, `in: "none"`). This one stays scene-side on purpose: `target: "all"` / `follow_footage` scale graphics about the face pivot in the bottom band, which would slide the top band ≈ 360 px instead of settling it in place | Presenter returns under a figure |
| **G-3** | Cut to full + settle | Stage → L-full, `via: "cut"` + **Z-1** settle (1.26 → 1.0, roll 4° → 0) on the same frame | Claims, turns, CTA |
| **G-4** | Bubble open | Stage → L-pip, `via: "cut"` (not `pip-shrink`): the bubble is there on the cut, ring included | F-B intros with a section header |
| **G-5** | Card over head | Stage → L-cardtop, `via: "cut"`; the card enters with the skew-in (P-20 recipe) on the same frame | F-B personal proof ("it took me…") |

No morphs (`stage_morphs: {cut: 0}`). The engine's default moves (`slide-down`, `pip-shrink`…) are never used: always write `"via": "cut"`.

### 3.4 Layout diagrams
**L-graphic (F-A figure card)**
```
┌─────────────────────────┐ 0
│   (IG top UI, clear)    │ ← y 0–110
│ FIG. 04 ONE WEEK  SRC:… │ ← FIG line, mono 26, y 232 (TC-legal)
│                         │
│   ┌───────────────┐     │ ← figure zone x 64–1016, y 300–1320
│ 4 │   hourglass   │     │   (counter numerals at x 64, y 760–900)
│DAYS   / bars /    │     │
│   │   rings /...  │     │
│   └───────────────┘     │ ← zone bottom 1320
│      ▌working on it▐    │ ← caption pill, cy 1390 (rect ≈ 1350–1430; F-B 1450)
│                         │ ← y 1500: end of meaning text
│   (IG bottom UI)        │ ← y 1540–1920: world only (decor band in brutal)
└─────────────────────────┘ 1920
```
**L-stack (hook and returns)**
```
┌─────────────────────────┐ 0
│  figure band            │ ← content y 140–880 (ticker card, bars, title slab)
│  CLAUDE SOLVED          │ ← F-A title slab y 800–925 (hook only)
│ ─────▌caption▐───────── │ ← seam y 960, caption on the seam
│  presenter (footage)    │ ← eyes at y ≈ 1345 (0.40 of the band)
│                         │
└─────────────────────────┘ 1920
```
**L-pip (F-B intro)**
```
┌─────────────────────────┐ 0
│ ▌// who_we_are▐   ╭───╮ │ ← slug pill x 64, y 150 · bubble d 420 at (816,330), ring 10 px primary
│ LEARN AI BY       │ ☺ │ │ ← header line 1 (ink), x 64–566, y 220
│ BUILDING.         ╰───╯ │ ← header line 2 (primary), y 330
│ ┌─● ● ●──file.exe──□□□┐ │ ← window card x 80–1000, y 640–1300
│ │ APPLIED AI          │ │
│ │ COHORT.  [chip]     │ │
│ └─────────────────────┘ │
│   [6 weeks] [live]      │ ← chips nested on the card edge (y 1240–1310)
│        ▌caption▐        │ ← cy 1440
│  ☆   ～～   ⠿⠿⠿          │ ← decor band y 1580–1860 (z1, brutal only)
└─────────────────────────┘
```
**L-cardtop (F-B proof)**
```
┌─────────────────────────┐ 0
│ ┌─────────────────────┐ │ ← card x 64–1016, y 130–600 (bottom ≥ 40 px above face top)
│ │ IT TOOK ME [ONLY]   │ │
│ │ ⏱  20 MINUTES       │ │
│ └─────────────────────┘ │
│        presenter        │ ← footage lowered 380 px; blurred copy fills the top
│      ▌caption▐          │ ← cy 1430
└─────────────────────────┘
```

### 3.5 Safe zones and bands
- Meaning text: x 64–1016, y 110–1500 (NC-5: nothing in the top 110 px, below y 1540, or in x > 970 between y 900–1540).
- Caption band: L-graphic cy 1390 F-A / 1450 F-B (TUNE 1280–1460); L-stack the seam (960); L-full 1290; L-pip 1440; L-cardtop 1430. Graphics stay ≥ 40 px clear of the caption rect (figure zone ends at 1320).
- FIG line: y 232 ± 8 (F-A only). Header band (F-B): y 150–440.
- Decor band (TH-brutal, z1, no text): y 1580–1860.

### 3.6 Presenter rules
- Share 20–35% (F-A) / 25–40% (F-B); the longest absence is 10 s (F-A) / 8 s (F-B). Plan a return (L-stack or L-full, ≥ 1.5 s) before each limit, on the next opinion, caveat, turn or "you" sentence.
- Returns are hard cuts (G-2, G-3). Never fade the presenter in.
- Crops: L-full as shot, entered with the Z-1 settle; L-stack bottom band face 0.34 of 960 px, eyes at 0.40; L-pip face 0.55 of the circle; L-cardtop as shot, lowered 380 px.
- Nothing sits behind or in front of the head; no matte work in this style.

---

## §4 Colour, themes, grades `[REQ] [roles' meanings DNA; primary/accent VAR; theme hues TUNE]`

### 4.1 Role palette (defaults = TH-editorial)
| Role | Hex (editorial) | One job | Text on it | Contrast | Brandable |
|---|---|---|---|---|---|
| `primary` | `#F08060` coral | Hero numerals, the FIG number, header line 2, the active bar, the PiP ring | ink | 7.2:1 | **yes** (BV-02 colour 1) |
| `accent` | `#4F8CFF` blue | The new / winning series, slug pills, chips, the CTA keyword | ink | 5.9:1 | **yes** (BV-02 colour 2) |
| `pill` | `#0B0A0A` (sampled v01 @0:20, @0:40) | Caption pill fill | paper | 17:1 | theme only |
| `card` | `#EDE6D6` | Card and window bodies | ink | 15:1 | theme only |
| `line` | `#2A2622` | Card outlines and hard shadows | — | — | theme only |
| `mute` | `#9A9384` | Mono micro labels, FIG title, SRC line, axis labels | (text colour) | 6.1:1 on W-main | theme only |
| `highlight` | `#C27BD9` | Highlighter bar behind a stat (P-40) | ink | 5.4:1 | theme only |
| `bad` | `#D4372D` | The old value, the cost, the problem, the record to beat | paper | 4.8:1 | **fixed** |
| `good` | `#2FBF71` | The fix, the pass, the saving | ink | 7.9:1 | **fixed** |
| `ink` | `#111111` | Dark text, outlines | — | — | theme only |
| `paper` | `#FFFFFF` | Caption text, light text on dark | — | — | fixed |
| `cream` | `#EDE6D6` | Editorial body text on the dark stage | — | 15:1 on `#141210` | theme only |

Gradients: `G-old` `#F06A5E → #8A2320` (old/bad bars, top to bottom), `G-new` `#E4ECFF → #3B74FF` (new/accent bars), `G-fill` `#F08060 → #B07CE8 → #4F8CFF` (grid fills, rings, left to right), `G-promo` `#120A0A → #C9341F → #F7C2B5` (W-promo).

### 4.2 Meanings
- **Old → new axis: `bad` (warm red) → `accent` (blue / the theme's second accent).** The record, the old way, the cost are red; the new result is the accent (v01 0:57–1:02: red 2023 record bar vs blue new bars).
- `good` appears only on a pass, a fix or a saving (✓ PASS, the cheaper route).
- `primary` marks *the number this card is about*. One primary element per card.
- Brand colours appear only on brand elements (a supplied logo, a logo plate's monogram).

### 4.3 Theme packs (`per_reel`)
| Pack | `primary` | `accent` | `pill` | `card` | `line` | `mute` | `ink` | W-main | W-alt | Pick it when |
|---|---|---|---|---|---|---|---|---|---|---|
| **TH-editorial** | `#F08060` | `#4F8CFF` | `#0B0A0A` | `#EDE6D6` | `#2A2622` | `#9A9384` | `#111111` | `#141210` stage, grain | `#EDE6D6` graph paper | **F-A default.** Results, research, records, how-it-works, market moves |
| **TH-brutal** | `#F26B3A` | `#8CFF3C` | `#DF2E2B` | `#FFFFFF` | `#111111` | `#6E6559` | `#111111` | `#FBF3E4` + 48 px grid | `#F6D9D5` blush | **F-B default.** Offers, courses, launches, tools, events, workflows |
| **TH-pinksage** | `#F4849C` | `#A9B9B4` | `#DF2C14` | `#FFFFFF` | `#2B1F2A` | `#2B1F2A` | `#2B1F2A` | `#F4849C` pink, grain | `#A9B9B4` sage | F-B reels whose hook is a cost, a waste or a pain number (bills, hours lost, money leaking) |

Pick rule at P7 (decided): the buyer's `profile.themes.default` wins if they set one; otherwise F-A → TH-editorial; F-B → TH-pinksage when the hook figure is a cost or loss, else TH-brutal. The pack is written in the reel header and never changes.

Per-pack text rules:
- **Editorial:** body text `cream` on W-main; `ink` on cards and on W-alt. Primary numerals on W-main.
- **Brutal:** text `ink`; header line 2 in primary **deepened to `#DB5320`** (3.6:1 on cream, display ≥ 96 px only; use `fx.textColour`). Lime `accent` is a fill only (chips, pills, panels), never text on cream.
- **Pinksage:** text `#2B1F2A`; white numerals and ticker values always carry a 5–8 px ink stroke + hard ink shadow (white on pink alone is 2.4:1).

### 4.4 Grades
Footage is not graded. One clip treatment exists: **halftone** on creator-supplied portrait photos in P-07 / P-14 (grayscale 1, contrast 1.25, a 6 px dot screen overlay at 35%). Until the grades module ships, apply it as a CSS filter + an SVG dot pattern inside the scene.

### 4.5 Rules
- `max_bright_per_frame` **3**: primary + accent + one of bad / good / highlight.
- Coloured text on a light world needs ≥ 3:1 at ≥ 96 px or a chip behind it; below 96 px use ink.
- No gradients on text. Gradients only on bars, rings, grid fills and W-promo.

---

## §5 Type & caption system `[REQ]`

### 5.1 Font map
| Slot | Family (weight) | Font class (TUNE boundary) | Used for |
|---|---|---|---|
| `display` | **Unbounded** 900, upright caps | extended heavy sans caps (Unbounded 900, Archivo Black) | F-A title slab (P-37) |
| `header` | **Barlow Semi Condensed** 700, caps | semi-condensed bold grotesque (Barlow Semi Condensed 700, Barlow Condensed) | F-B section headers |
| `chunky` | **Barlow Condensed** 700, caps | condensed bold grotesque (Barlow Condensed 700, Anton) | window titles, slab labels |
| `body` | **Inter Tight** 600–800 | neo-grotesque sans (Inter Tight, Plus Jakarta Sans, Space Grotesk) | F-A captions, figure labels |
| `ui` | **Poppins** 600–800 | geometric sans (Poppins, Jost) | F-B captions, card copy, word stacks, CTA keyword, list numerals |
| `numeric` | **Instrument Serif** 400 (F-A) / **Poppins** 800 (F-B) | display serif (F-A) / geometric heavy (F-B) | Hero numerals, counters, ticker values |
| `serif` | **Instrument Serif** 400 italic | high-contrast display serif | Quote notes, chart annotations ("off the chart ↑") |
| `mono` | **JetBrains Mono** 500–600 | monospace | FIG / SRC lines, `// slug` pills, micro labels, terminal logs, window filenames |

Closest-match note: v01's slab is an **upright** extended black (Druk-Wide-like), not italic (full-res check, v01 @0:01.2); Unbounded 900 is the closest bundled face. v02's header is a semi-condensed grotesque; Barlow Semi Condensed 700 (the `header` slot) is the closest bundled face.

### 5.2 Headline element `[DNA recipe; NICHE text]`
**F-A: title slab (`plate`, lifetime `hook`)** (P-37)
| Property | Spec |
|---|---|
| Text | Unbounded 900 upright, caps, **80 px** (TUNE 70–92; real cap 59 px, line 1 x 76–1010), line height 0.9, a soft dark shadow, white `#FFFFFF`, 2 lines, ≤ 16 characters per line, ≤ 5 words |
| Box | No fill, no stroke; a soft shadow `0 4px 18px rgba(0,0,0,.55)` for legibility over footage or figures |
| Position | Centred on x 540, near full width, lines at y 800–925 (measured v01 @0:00.6: 801–860 / 875–924) inside the L-stack top band, ≈ 35 px above the seam (the bottom of the band, above the seam caption) |
| f0 | Line 1 slides in from the **right** (x +540) and line 2 from the **left** (x −540) on the same frame, each with a 14 px horizontal blur, expo-out over **12 f**; settled by f12 (v01 0:00.04–0:00.48) |
| Life | Static once settled (the figure above it moves) |
| Exit | Leaves with the stack on the first hard cut (1.5–2.0 s); never animated out |

**F-B: section lockup (`lockup`, lifetime `section`)** (P-21)
| Property | Spec |
|---|---|
| Slug pill | `// snake_case_label` (≤ 16 characters), JetBrains Mono 600 **32 px** lowercase ink on `accent`, radius 24, padding 8/20, 3 px `line` outline. x 64, y 150, height 52. TC-label `redundant` (E3) |
| Header | Barlow Semi Condensed 700 caps (`header` slot) **104 px** (TUNE 96–112), line height 0.98. Line 1 `ink`, line 2 `primary` (deepened, §4.3) and ends with a period. ≤ 12 characters per line. x 64, y 220–440; width ≤ 502 px with L-pip (stops 40 px before the ring), ≤ 952 px without |
| f0 | The slug pops (scale 0.6 → 1, 4 f); line 1 **rises out of a clip line** (y +60 → 0 under a mask, 4 f, expo-out) from f3; line 2 rises the same way ≈ 10 f later (v02 0:00.12–0:00.52). No typing |
| Life | Changes per section: after the section transition (T-07 iris wipe) the slug pops and the new lines rise again |
| Exit | Hard cut when the section ends or the layout becomes L-full |

### 5.3 Caption profile CS-1 `[DNA mechanics; fonts TUNE; language VAR]`
`extends: "lib:100x"` and tunes it.

| Group | Value |
|---|---|
| Mode | `full`, role `support`, `mute_safe` |
| Chunking | unit `group`, **1–4 words**, 1 line, ≤ **26 characters**, never split a name, number or unit; break on punctuation and on pauses ≥ 0.6 s |
| Timing | lead 2 f; **reveal `chunk`**: the whole 1–4-word group appears at once, pill included; **swap `hard` 0 f** (no fade, no pop, no rise: v01 0:01.90 "by" → "working on it", v02 0:00.36 "This" → "video", v03 0:03.70 "Here are" → "two real", all one-frame swaps); min hold 0.25 s per word; tail 0.12 s; no pause hold |
| Skin F-A | Plus Jakarta Sans **600**, **54 px** (TUNE 44–58; Inter Tight was 12 % too narrow against v01 @0:08, @0:40), sentence case as spoken, white `paper`, no stroke, no shadow; **pill** fill `pill` (`#0B0A0A` editorial, near-black on the `#191814` stage), opacity 1.0, radius 10, padding 10/18 (pill ≈ y 1350–1422) |
| Skin F-B | Poppins **700**, **48 px**, case as spoken (mostly lowercase), white; pill `#DF2E2B` (brutal; sampled #EA3B35 at v02 @0:00–0:03, nudged darker so white 48 px text reaches 4.5:1) / `#DF2C14` (pinksage; sampled #F5452D at v03 @0:10, same nudge), opacity 1.0, radius 10, padding 8/16 (pill 62–70 px tall) |
| Position | L-graphic fixed cy **1390** (F-A, measured 1386) / **1450** (F-B brutal, measured 1452); **TH-pinksage per card**: each card scene declares `caption_cy` so the pill sits under that card's content (measured v03 1075 / 1277 / 1408 on different cards; 1290 when the card sets none; or timeline `captions.overrides` `{t: [a, b], cy}`; V-CAPTION keeps it inside `layout.safe.y`); L-stack **seam** (cy 960); L-full cy **1290**; L-pip cy **1440**; L-cardtop cy **1430**; centred, max width 952; `avoid_face` on |
| Emphasis | **none** (N11): no colour, no size jump, no chip inside captions |
| Hide | Under z8 type scenes (P-38, P-48), during stage morphs (there are none), and over the numeral card's label box if they would collide (they don't at 1390–1450 vs 900–1060) |
| Language | Latin script; keep English terms verbatim; don't normalise spelling; glossary from the buyer's brand and tool names |

Measured basis: 1–3 words per chunk, median 2 (v01 "working on it", "for a whole", "set by"; v02 "is fully", "by Claude Opus 5.5."; v03 "you pay", "LLM call,"); pill y 1385–1455 on graphic frames, the seam on stacks (v01 0:14 "in layers"), the chest on full frames (v02 0:12 "If you want" ≈ y 1215, v01 0:09 "the formula" ≈ y 1280).

### 5.4 Other text systems
| System | Recipe | Class | Hold |
|---|---|---|---|
| **FIG line** (F-A) | JetBrains Mono 500 **26 px** caps, tracking 0.12. Left: "FIG. 04" in `primary` + two spaces + the card title in `mute` ("ONE WEEK, NONSTOP"). Right-aligned at x 1016: "SRC: OUTLET · MON YYYY" in `mute`. y 232 | TC-legal | The card's life |
| **Micro labels** | JetBrains Mono 500 **30–34 px** caps, tracking 0.12, `mute` ("DAYS", "LOOPS · THE RECORD", "CPUs RUNNING", axis ticks) | TC-label `redundant` (E3) | ≥ 10 f after built |
| **Figure labels** | Inter Tight 600 **40–48 px** caps, tracking 0.06 (bar names, node names when not redundant) | TC-label | ≥ 0.25 s / word |
| **Hero numerals** F-A | Instrument Serif 400, **520–720 px**, `primary`; counters 140–200 px | TC-display | ≥ 0.6 s after landing |
| **List numerals** F-B | Poppins 800, **620–760 px**, white, 8 px ink stroke (`paint-order: stroke fill`), hard ink shadow +16/+18 | TC-display | 1.2–1.6 s |
| **Ticker values** F-B | Poppins 800 **150 px**, white, 5 px ink stroke, hard shadow +8/+10, in a fixed-width value box (`data-slot`, E6) | TC-display | the card's life |
| **Label box** F-B | Poppins 700 **88 px** ink in a white box, 5 px `line` outline, hard shadow +10/+12, typed **1 char / 2 f** with a caret blinking 8 f on / 8 f off (v03 0:06.7) | TC-display | ≥ 1.0 s after typed |
| **Chips** | JetBrains Mono 600 **40 px**, radius 30, padding 10/24, 3 px `line` outline, fill `accent` / white / `card`, rotated −3…+3° | TC-label | the card's life |
| **Quote** | Instrument Serif italic **58 px**, line height 1.12, ink on `card`; key phrase underlined by a 6 px `primary` hand stroke | TC-label | ≥ 0.25 s / word |
| **Annotation** | Instrument Serif italic **64 px**, `bad` or `primary` ("off the chart ↑") | TC-label | ≥ 10 f |
| **Terminal lines** | JetBrains Mono 500 **38 px**; meaning lines in `cream`/ink, timestamps in `mute`; filler lines `TC-decorative` | TC-label / TC-decorative | ≥ 0.6 s per line |
| **Word stack** | Poppins 700 lowercase **110 / 140 / 110 px**, white, shadow `0 3px 16px rgba(0,0,0,.45)` | TC-display | the clause |
| **CTA keyword** | "comment" Poppins 800 **130 px** white; the keyword Poppins 800 **200 px** in curly quotes, fill `accent` (brutal, editorial) or `primary` (pinksage); both with a hard ink drop shadow offset 6/6 px and no outline (v03 @0:22 "comment / “Jev”", keyword cap ≈ 190 px) | TC-display | ≥ 1.5 s |
| **Stat line** | Poppins 600 **110 px** ink, highlighter bar `highlight` behind | TC-display | ≥ 0.25 s / word |
| **Window filename** | JetBrains Mono 500 24 px `mute` in the title bar ("who_we_are.exe") | TC-decorative (chrome) | — |
| **Legal** | JetBrains Mono 500 24 px `mute`, bottom-left of the card at y ≤ 1490 | TC-legal | the card's life |

### 5.5 Language and number rules
- **Speech `en` (default):** captions verbatim English, sentence case (F-A) / as spoken (F-B). Brand names exact.
- **Speech `hinglish` → captions `en`:** translate per chunk, keep the timing of the spoken words; on-screen cards in English.
- **Speech `hinglish` → captions `hinglish` Latn:** romanised as spoken, English terms verbatim; cards stay English (the design system is English-first).
- Numbers: `ctx.fmtNum` only. International: `$2,000`, `$1.2M`, `96`, `193.6x`. Indian (BV-06): `₹2,000`, `₹1,20,000`, `₹1.2 L`, `₹3 Cr`. Units as spoken ("20 MINUTES", "7 DAYS").
- Mono caps and tracked caps are Latin-only; Devanagari is not supported by this template's on-screen system.

---

## §6 Hook system `[REQ]`

**Hook title (every style, 8 Oct 2026; above anything below):** the on-screen title promises the viewer something: an outcome they want, a curiosity gap, or who it's for ("How to go viral as a doctor creating content", not the label "Reels for Doctors"). It doesn't have to repeat the spoken words; it has to be true to what the reel delivers. A title shown as someone's words (in quotes) is still word for word. This section sets the title's shape (lines, sizes, word limits, case, the keyword device), never its voice. Write 8–10 candidates from the formulas below plus the proven patterns ("How to X as a Y", "Why your X isn't working", "The X nobody tells you", "Stop doing X", "Your X vs mine", a number or a contrast), score them on outcome, curiosity, who it's for and brevity, check the best against the stopper tests, and pick; any "write 3" below means this, and the next two go to the storyboard as alternates. A style with no on-screen title applies this to its post title.

### 6.1 Stopper tests
| Test | This style's number |
|---|---|
| ST-1 Thumbnail | f0 at 25% shows a moving figure and a readable claim: the title slab (F-A, 84 px → 21 px at 25%) or the ticker values (F-B, 150 px → 38 px) |
| ST-2 Mute | With sound off, 0–3 s tells the claim: the number climbing + the caption words + the slab/header |
| ST-3 Motion at f0 | The figure is already moving on f0 (counter rolling, ticker ticking, particles falling) |
| ST-5 Change count | ≥ **6** weighted state changes in 0–3 s |
| ST-6 Payoff-by | The opening figure's first value by **1.0 s**; the reel's result number by **6.0 s** |
| ST-4 Read time | Headline readable in ≤ 1.2 s (≤ 5 words F-A, ≤ 6 words F-B) |

### 6.2 Default archetype: HA-07 Live number `[DNA]`
The spoken claim plays over a number that is already moving at frame 0; the claim's own result number lands within 6 s.

**F-A version (editorial, L-stack → figure cards)** — from v01's structure with v03's frame-0 number.
| t | Layout / camera | Visual | Caption | Cue moment |
|---|---|---|---|---|
| **f0** | L-stack + **Z-2 settle** (both bands start at 1.45 and settle out over 22 f, 2 f of motion blur: v01 0:00) | Top band (y 140–660): the claim's figure already moving: a counter rolling from its start value (P-02 day counter, P-12 grid count, P-35 count) or a ticker (P-27). Title slab lines sliding in from opposite sides at y 800 | Word 1 on the seam pill | hook hit |
| 0.0–0.4 | — | Slab settles by f12; counter keeps rolling | Chunk swaps | — |
| ≤ 1.0 | — | **First value lands** (a step of the figure on a spoken word, or the start state the sentence describes) | — | reveal |
| 1.0–2.0 | **Hard cut** to L-graphic (G-1) on the second clause | FIG. 01 card: the same figure, full size (hourglass/grid/bars), its mechanism running (particles fall, cells fill) | cy 1390 pill | transition |
| 2.0–3.0 | L-graphic | 1–2 in-figure events on the spoken nouns (the counter steps 4 → 5 DAYS; "NONSTOP" label + red dot) | — | — |
| 3.0–6.0 | Hard cut or evolve | **The result number** lands: a hero numeral (P-06) or a counter in the same card ("≈ $2,000 · TOTAL COMPUTE") | — | reveal |
| 6.0+ | Hard cut | FIG. 02: the first mechanism figure of the body | — | transition |

**F-B version (brutal / pinksage, ticker stack → word stack → product card)** — from v03.
| t | Layout / camera | Visual | Caption | Cue moment |
|---|---|---|---|---|
| **f0** | L-stack | Top band: P-27 ticker card (header strip + 2 rows), values already ticking (+1 step every 4 f, E6) | Word 1 on the seam | hook hit |
| 0.0–2.0 | — | Rows tick in sync toward their spoken / script values; the card is still | Words on the seam (2-word chunks) | — |
| ≤ 1.0 | — | First value step lands on a spoken word (the noun of the pain: "bill") | — | reveal (tick run starts) |
| 2.0 | **Hard cut** to L-full + **Z-1** settle (G-3) | **P-38 word stack**: the payoff clause, 2–3 words blurring in on their onsets ("you / probably / need") | Hidden (z8) | transition |
| ~3.0–3.3 | **Hard cut** to L-graphic | The answer card on the product/brand word: P-28 router, P-20 window card or P-46 logo plate | cy 1390 | reveal |
| 3.3–6.5 | L-graphic, W-main ↔ W-alt | The promise ("two real use cases"): P-29 tickets or P-23 tiles preview the items | — | — |
| 6.5 | Hard cut | **P-39 numeral card "1"** with the item label typing | — | list cue |

### 6.3 Allowed alternates `[DNA list; VAR choice per reel]`
**HA-02 Headline + proof (F-B, when the opening line has no number)** — v02.
| t | Visual | Notes |
|---|---|---|
| f0 | L-pip; slug pill pops, header line 1 typing; P-20 window card skewing in (rotateY −10° → 0, 8 f) with the product/offer title | Proof = the window card (kind `card`) |
| 1.0–1.6 | P-22 chips pop on the card's bottom edge on the attribute words (3 chips, 5 f stagger) | — |
| 2.4–2.7 | The window swaps (hard wipe-left 6 f) to the next window; the header retypes with a new slug | The reel's second idea |
| ≤ 2.5 | Proof readable | payoff |
Example [NICHE: fitness]: "This program was built by two physios." → `// who_we_are` / "TRAIN WITH / PHYSIOS." + window "12-WEEK / STRENGTH." + chips "3x a week", "live", "home or gym".
Example [NICHE: finance]: "This is the simplest budget you'll ever set up." → `// the_method` / "ONE SHEET. / ZERO APPS." + window "50·30·20 / BUDGET." + chips "10 minutes", "free template", "monthly".

**HA-18 Borrowed clip (F-A, only with a creator-supplied source clip, SH-3)** — v01 opening.
| t | Visual | Notes |
|---|---|---|
| f0 | L-stack with the **source clip in the top band** (`top: "source:<id>"` or `ctx.videoFrame`), credit line `SRC: …` TC-legal at the band's top-left; title slab sliding in at y 800–925; presenter in the bottom band | The clip shows the person or event the claim is about |
| 1.5–1.8 | Hard cut to FIG. 01 | The first figure with a live number |
| ≤ 3.0 | Clip payoff (the claim is clear); presenter on screen from f0 | — |
Fallback when no clip: open on HA-07 (FB-3). Never a recreated "interview".
Example [NICHE: finance]: a creator-held clip of a fund manager's interview + slab "FUNDS LOST / TO INDEX".
Example [NICHE: fitness]: a creator-held conference clip of a sports scientist + slab "WALKING BEAT / RUNNING".

### 6.4 Hook pairs by topic `[NICHE]` (pair type: claim → evidence)
| Topic [NICHE: example] | Claim (spoken) | Number (provenance) | Figure at f0 → payoff | Format / theme |
|---|---|---|---|---|
| Finance: fund fees | "Most fund managers lose to a simple index fund" | share of funds beating the index over N years (script / source) | P-12 grid fill counting losers → P-15 bars active vs index | F-A editorial |
| Finance: subscriptions | "Your subscriptions cost more than your rent" | monthly totals per app (creator's own numbers) | P-27 ticker climbing per app → P-06 yearly total | F-B pinksage |
| Finance: compounding | "Starting at 25 instead of 35 doubles your money" | contribution, rate, years (script) → `compound` | P-05 bars climbing by decade → P-06 the gap | F-A editorial |
| Finance: budgeting app | "This sheet replaced three budgeting apps" | minutes to set up (creator) | P-25 stopwatch counting → P-26 receipt "$0" | F-B brutal |
| Fitness: steps | "8,000 steps does more than an hour at the gym" | steps, minutes (study, cited) | P-12 grid of days filling → P-15 bars | F-A editorial |
| Fitness: program launch | "Twelve weeks, three sessions, no gym" | weeks, sessions (offer facts) | P-35 count 0 → 36 sessions with calendar → P-20 program window | F-B brutal |
| Fitness: protein | "You're eating half the protein you need" | grams eaten vs target (script) | P-27 ticker of grams per meal → P-15 bars vs target | F-B pinksage |
| Fitness: recovery | "Sleep under 6 hours erases a week of training" | hours, % strength (study, cited) | P-02 hourglass of nights → P-16 off-chart loss bar | F-A editorial |

The pair is written per reel at P7 and appended here in the buyer's copy (D.6).

### 6.5 Headline writing `[DNA formula; NICHE examples]`
**F-A title slab formula:** `[SUBJECT] [PAST/PRESENT VERB] / [OBJECT or RESULT]`, caps, ≤ 5 words, 2 lines, ≤ 16 characters per line, no punctuation, no emoji. It names the *event*, the live number shows the *scale*.
- "INDEX FUNDS / BEAT 9 IN 10" · "WALKING BEAT / RUNNING" · "RENT ATE / YOUR RAISE"

**F-B section header formula:** slug `// what_this_is` + line 1 (verb or frame) + line 2 (the payoff noun + period), caps, ≤ 6 words, ≤ 12 characters per line.
- `// who_we_are` "LEARN BY / BUILDING." · `// what_you_get` "SHIP REAL / PROJECTS." · `// the_cost` "YOUR BILL / EXPLODED."

Rules:
- **Write 3 and pick by the stopper tests.** The other two go to the checkpoint as alternates.
- English on screen even when the speech is Hinglish.
- Banned: vague hype ("GAME CHANGER"), question marks in the slab, numbers that the figure doesn't show, any word not supported by the script.

### 6.6 Hook sound
The hook carries cues on f0 (a hit), on the first value landing (a tick run or pop), and on the first hard cut. The bed runs from f0 under the voice (§11).

### 6.7 CTA `[DNA device set; VAR values]`
Device set: `comment_keyword` (default), `dm`, `link_bio`, `none`. Placement: **F-B mid + end; F-A end**.

**comment_keyword** ({{BV-08.keyword|KEYWORD}}, deliverable {{BV-08.deliverable|the free resource}}):
| Moment | Spoken pattern | On screen | Hold |
|---|---|---|---|
| **Mid CTA (F-B)** at 25–50% of runtime, right after the first proof | "If you comment {{BV-08.keyword|KEYWORD}}, I'll send you {{BV-08.deliverable|the free resource}}…" | Hard cut to L-full + Z-1; **P-48 keyword card** ("comment" + "“{{BV-08.keyword|KEYWORD}}”") y 1080–1420, captions hidden; then **P-49 promo carousel** (1.5–2.5 s) and **P-41 title window** with the deliverable's exact title typed (1.5–2.5 s) | keyword ≥ 1.5 s |
| **End CTA** (both formats) in the last 2.5–3.5 s | "Comment {{BV-08.keyword|KEYWORD}} and I'll see you there." | Hard cut to L-full + Z-1; P-48 keyword card 1.5 s; **P-50 comment sheet** slides up over the blurred presenter with the keyword typed into the input (1.0–1.5 s) | keyword ≥ 1.5 s |
| Silence | None required before the CTA (the voice is continuous in the evidence) | — | — |

**dm:** same placement; the keyword card reads "DM “{{BV-08.keyword|KEYWORD}}”"; no comment sheet (end on the keyword card).
**link_bio:** the keyword card becomes "link in bio" + the deliverable title on a P-41 title window; held 2.0 s at the end only.
**none:** F-A ends on its last figure (P-18 slider matrix or the result number); F-B ends on the benefit card. Hard end ≤ 6 f after the last word.


---

## §7 Structure & cadence `[REQ] [DNA]`

### 7.1 Structure type (one per format)
**F-A `explainer` (figure sequence).** One figure per idea, numbered in order. The arc, from v01's 14 figures in 75 s:
| Act | Share | Content | Typical patterns |
|---|---|---|---|
| 1 Claim + scale | 0–10% | What happened and how big (the hook, the result number) | HA-07 stack, P-02, P-06, P-12 |
| 2 What it is | 10–25% | The object or problem explained (what X is, why it's hard) | P-03, P-04, P-05 |
| 3 The record / the stakes | 25–40% | Who held it, since when, who challenged it | P-06, P-07, P-08, P-09 |
| 4 How it was done | 40–65% | The process, step by step (the run, the resources, the method) | P-10, P-11, P-12, P-13 |
| 5 Verification / proof | 65–80% | Who checked it; the comparison with others | P-14, P-15 |
| 6 Caveat + meaning | 80–100% | What it isn't; what it changes (the payoff); the CTA if chosen | P-19, P-16, P-17, P-18 |

**F-B `list` (pitch → items → CTA ×2).** From v02 and v03:
| Section | Share | Content | Typical patterns |
|---|---|---|---|
| HOOK | 0–8% | The pain number or the offer headline | HA-07 ticker stack / HA-02 pip + window |
| PRODUCT | 8–15% | The product or offer named, the promise ("two use cases") | P-28, P-20, P-46, P-29 |
| ITEM-1…n | 15–45% | Each item: numeral card → 1–3 cards | P-39 → P-30, P-28, P-29, P-23 |
| CTA-MID | 45–60% | Keyword + deliverable | P-48, P-49, P-41 |
| BENEFIT / PROOF | 60–90% | Who it's for, the stat, what you'll learn | P-31, P-40, P-33, P-34, P-35 |
| CTA-END | last 2.5–3.5 s | Keyword again + comment sheet | P-48, P-50 |

### 7.2 Markers
- **F-A: SM-FIG.** Every L-graphic card carries the FIG line "FIG. nn  TITLE … SRC: …" at y 232. Numbers are two digits, start at **01**, rise by one per **new card concept** (a card that evolves keeps its number), and never repeat or go backwards. v01 runs 04 → 05 → 06 → 08 … and restarts at 01 near the end; the template fixes that to strictly monotonic. L-stack top bands and L-full frames carry no FIG line.
- **F-B: SM-NUMERAL.** One full-screen numeral card per list item (P-39), on the ordinal word ("1.", "One:", "First"), ascending. The label box types the item name. Sections without a list use the slug lockup only (v02 has no numerals; v03 uses "1", "2").
- No recap, no teaser chips.

### 7.3 Unit rituals
**F-A figure ritual (every card):**
1. **f −2 (lead):** hard cut (G-1, or a scene swap with `cuts`) on the first content word of the sentence.
2. **f 0:** W-main (or W-alt) + the FIG line present; the main object starts its entrance (8 f expo-out, or a 10–14 f draw-on).
3. **f 8 → end:** the mechanism runs (particles fall, rings add, bars grow, cells fill), with **1–3 events** on the sentence's nouns and numbers, ≥ 0.4 s apart and never > 2.0 s apart.
4. **Hold:** 1.5–3.0 s per card; up to 5.0 s only while events keep landing every ≤ 2.0 s.
5. **Exit:** none: the next hard cut replaces the card. When the next sentence continues the same idea, the card **evolves** instead (T-04): the hero numeral dims to 15% and becomes the backdrop of the portrait card (v01 0:19 → 0:21).
6. **Presenter return** every ≤ 10 s: an L-stack with this figure re-laid in the top band, or an L-full on a turn word.

**F-B item ritual (every list item):**
1. Hard cut to the **P-39 numeral card** on the ordinal word (lead 2 f). The numeral pops (1.25 → 1, 6 f); the label box rises 8 f; the label types 1 char / f with the caret.
2. Hold 1.2–1.6 s (the spoken item name).
3. Hard cut to the item's first card (alternating W-main / W-alt) on the item's first content word.
4. 1–3 cards per item, each 1.5–3.0 s, each with ≥ 1 event (cursor click, fork draw, ticket scatter → sort).
5. Presenter return (L-full or L-stack) every ≤ 8 s.

### 7.4 Open loops, re-hooks and the intro cap
- **Loops used:** the count promise ("two use cases", "three things") paid by numeral cards; the result-number loop of F-A (shown by 6 s, explained by the end); the deliverable loop of F-B (mid CTA, paid by the end CTA and the comment sheet).
- **Re-hook every 25 s** (`structure.rehook_every_s`):
  - F-A puts a **turn beat** at 22–28 s and 47–53 s: a hard cut to L-full + Z-1 on the turn word ("Then", "But", "Until", "Now"), or a figure with an open slot (the dotted "?" bar of P-05, the "UNCLAIMED" line of P-08).
  - F-B's mid CTA *is* its re-hook (it lands at 25–50% of runtime).
- **Intro cap:** hook + product/promise ≤ 15% of runtime (≤ 9 s in a 60 s reel).
- Every promise is paid on screen (H9).

### 7.5 Rhythm and energy curve
- **F-A:** steady and dense. A new figure every 2–4 s, an in-figure event every ≤ 2 s, the presenter as a breather every 8–10 s. Act 5 (verification) slows to 3–5 s cards with bars filling. The last figure carries the biggest idea (the price, the shift, the summary matrix).
- **F-B:** fast and punchy. Hook ticker (dense), product card, numerals as resets. The mid CTA drops the energy to one big word; the benefit section re-accelerates with cards every 1.5–2.5 s; the end CTA is clean.
- No comedy beats (comedy off).

### 7.6 Cadence (state changes)
| Token | Value | Basis |
|---|---|---|
| `sc_per_10s` | **[7, 16]** (captions weigh 0.5) | ≈ 8 picture changes per 10 s (v01: ≈ 60 picture changes in 75 s on the 1 fps sheets) + ≈ 5 caption weight (≈ 1.2 chunks/s × 0.5); v02/v03 ≈ 28–30 picture changes per minute plus captions |
| `hook_sc_3s` | **6** | v01 0–3 s: slab + cut at 1.64 + numeral 3 → 4 → 5 + ≈ 6 caption chunks; v03: ticker + cut at 2.0 + word stack |
| `max_gap_s` | **2.0** (hook **1.2**) | Graphic holds of 1.5–3 s with in-card events (v01 0:31–0:38: a terminal line every ≈ 1 s) |
| `max_static_s` | **2.5** | Particles, live footage and typing count as continuous motion |
| `caption_weight` | 0.5 | support captions |
| `cuts_per_min` | not DNA (measured 12.8 / 15.2 / 20.6) | Scene detection misses graphic swaps |

The coverage table's "4–5 per 10 s" counted picture changes without in-card events and captions; this template counts what the validator counts (events + caption weight) and states the range accordingly.

---

## §8 Visual system: graphics, B-roll and patterns `[REQ]`

### 8.1 Graphics role and budget
- `graphics: primary`: designed graphics own **55–75%** (F-A) / **45–70%** (F-B) of runtime (L-graphic plus the top band of L-stack).
- **52 patterns** (P-01…P-52) in 8 families; ≥ **8 different patterns per 60 s** and ≥ 4 families.
- **Numbers become pictures** (D4): every spoken quantity is a figure that animates; comparisons share one axis (`scale_id`).
- **Every card is one element** (G2): labels, chips, the FIG line and value boxes are drawn inside the card's own scene. With the caption, a frame holds ≤ 3 text blocks: the card, the F-B header lockup (when present) and the caption.

### 8.2 Families
| ID | Family | Source class | Buyer must supply |
|---|---|---|---|
| **B-1** | Figure cards (editorial data art: hourglass, rings, bars, grids, timelines) | engine | — |
| **B-2** | Window & ad cards (neo-brutalist windows, chips, tiles, tickets, routers) | engine | — |
| **B-3** | Type cards (title slab, word stack, numeral card, stat highlight, title window) | engine | — |
| **B-4** | Diagrams & flows (node map, router fork, cycle, slider matrix) | engine | — |
| **B-5** | Presenter stage patterns (split proof, guest bubble, card over head) | buyer-owned (A-roll) | the A-roll |
| **B-6** | Evidence & inserts (portraits, quote notes, app screens, logo plates, source clips) | creator-supplied third-party, else a **created substitute** (named per pattern) | optional: photos, screenshots, recordings, clips, logos |
| **B-7** | Data figures (counters, tickers, bars, grid fills) bound to `figures.json` | engine | the numbers (script or creator) |
| **B-8** | CTA & brand (keyword card, promo carousel, comment sheet, decor band, sponsor chip) | engine (+ optional buyer thumbnails) | optional: 3–6 of their own thumbnails (SH-5) |

### 8.3 Pattern specs
Motion is in frames at 30 fps. "Engine" names the building block to use in `plan/scenes.js`. Every card scene declares `text_class`, `events` (every in-card change), `figure` / `figures` when it shows numbers, and `cuts` when it swaps hard. Class shorthand: D display, L label, g legal, x decorative.

**B-1 Figure cards (the F-A home family; usable in F-B)**
| ID | Pattern | Type | What's on screen | Motion (30 fps) | Use for | Engine | Class / needs |
|---|---|---|---|---|---|---|---|
| **P-01** | **FIG card frame** | figure | W-main full-bleed; FIG line at y 232 (left "FIG. nn  TITLE", right "SRC: …"); the figure inside the zone x 64–1016, y 300–1320 | Hard cut in (0 f); the FIG line **and the whole figure** are present on the cut frame (v01 0:01.66, 0:38.70); the mechanism (particles, typing, counters) runs from f0; no exit animation | Every F-A L-graphic card | bespoke `VEOS.scene` z3; FIG line as `data-tc="TC-legal"`; SRC via `fx.creditLine` | g + the figure's class; citations |
| **P-02** | **Hourglass counter** | figure | A `card` hourglass (x 230–850, y 300–1350, 40 px waist) with 24 seeded ink dots in the top bulb and one `primary` "start" dot with a leader label ("DAY 1 · one instruction", mono 30); a counter numeral at x 64, y 760–900 (Instrument Serif 160 px `primary`) + a "DAYS" micro label; a "NONSTOP" micro label with a `bad` dot appears on its word | A dot drops through the neck every 6 f (10 f ease-in fall, seeded x jitter ±6 px) and piles at the bottom; the counter steps on the spoken time words (each step an event; E6 inside a fixed box) | Time passing, duration, "for a whole week", waiting | `ctx.canvas()` + `VEOS.data.counter` (kind counter, steps at words) | D counter, L micro (E3 redundant), E6 |
| **P-03** | **Loop rings** | figure | Concentric rings at (540, 800), ring k radius 70 + 28k, 4 px, coloured along `G-fill` by k; a dot orbits the outer ring; the count numeral at the centre (Instrument Serif 160 px); a formula or label under it (serif italic 64 px + a micro label) | Each new ring draws on in 6 f (stroke-dashoffset) on its count word; the numeral steps (E6); the orbit dot does 1 rev / 2 s | Layers, levels, iterations, rounds, "N times" | `ctx.canvas()` + counter figure | D, E6 |
| **P-04** | **Crossing paths** | figure | A perspective grid floor (`mute` 18%); two spheres (r 60, `bad` and `accent`, 30 px soft glow) on dashed diagonals from opposite corners; small mono labels (p1…p4) at the path ends; a header micro label ("PREDICTED OUTCOMES") | The spheres travel 20 f ease-in-out to cross at the centre; on contact 12 seeded particles scatter (12 f) | Two forces meeting, a collision, a match, a competition, a prediction | `ctx.canvas()`, `ctx.rngStable` | illustrative (no numbers); L micro |
| **P-05** | **Bar climb** | figure | An axis on the left with an up arrow and a label (`accent` mono 30: "HARDER", "COST", "TIME"); N bars (L1…Ln micro labels) in `G-old`; the next slot as a dotted outline with "?" | Bars grow one after another, 3 f stagger, 14 f each, heights from the figure's steps (one `scale_id`); the "?" slot pulses 1.0 → 1.06 → 1 on the open-question word; an optional curve draws over the tops (12 f) | Exponential or steady growth, "every step makes it harder", the record to beat | `VEOS.data.bars` or bespoke canvas with `ctx.figScale` | L, figure, scale |
| **P-06** | **Hero numeral** | figure | One numeral in Instrument Serif **640 px** `primary`, centred (y 560–1100); a micro label under it ("LOOPS · THE RECORD") | Blur-in 10 f (blur 16 → 0, scale 1.04 → 1); a 12–18 f counter roll when the value is computed; afterwards it may **dim to 15%** and stay as the backdrop of the next card (evolve) | The single number the sentence is about (a record, a total, a price) | `VEOS.data.counter` (size 640, font numeric) | D, figure |
| **P-07** | **Portrait pair** | figure / insert | 1–3 circular portraits d 280 at y 420–700 with 4 px rings (`primary` for the first, `accent` for the second), halftone; the name in mono 32 caps (`cream` on W-main), the role in mono 26 `mute` | Each scales in 0.2 → 1 with a fade in 4 f, no overshoot, 6 f stagger, on the name word; name and role fade in 4 f after (v01 0:21.05–0:21.45) | People named in the script | `fx.shot` (creator photo + halftone) else **`fx.silhouette`** | L; insert (person) |
| **P-08** | **Timeline dot** | figure | An x axis of years (mono 30), y ticks for two levels; a glowing `primary` dot at the start; a dashed `accent` target line with a micro label ("UNCLAIMED") | The dot pops 6 f; a solid line draws from the dot towards the current year over the spoken span; the target line draws 12 f | "Nobody had done it for N years", a record standing, waiting time | `VEOS.data.slider` (years) + a bespoke line | figure (years), L |
| **P-09** | **Quote note** | insert | A `card` note (x 108–990, y 420–1260) tilted −3°; an avatar circle (creator photo or initials), name 36 px bold, role 26 px `mute`, date in `primary` mono 26; the quote in Instrument Serif italic 58 px; a footer micro label | The note settles from −8° and y +60 in 10 f; quote words appear on their spoken onsets (verbatim, NC-13); the key phrase gets a 6 px `primary` hand underline drawn L → R in 10 f | Someone's public statement, a challenge, a review, a promise | **`fx.quoteCard`** (`reveal`, `highlight`, theme paper) | L; insert (post) |
| **P-10** | **Run log** | figure / insert | A dark window (`#1E1C1A`, radius 18, traffic lights, a title, a model chip outlined in `primary`), x 64–1016, y 400–1340; log lines in mono 38 with timestamps in `mute`, "update:" lines in `accent`; a status line at the bottom ("☾ OPERATORS: ASLEEP") | Typing at 22 chars / s (`fx.typewriter`); a new line every 0.6–1.0 s on the spoken words; the status line fades in 6 f on its word | A process running unattended, an agent working, a sequence of steps | **`fx.appUI({kind: "terminal"})`** or bespoke | L / x filler; insert (app_ui) when it stands for a real product |
| **P-11** | **Code fix** | figure | 5–7 code-shaped lines (mono 30, `mute` 45%, decorative); one line gets a `bad` wavy underline + an "✕ ERROR" pill (mono 34, paper on `bad`), which flips to "✓ FIXED" (`accent` or `good`) | The underline draws 8 f; the pill pops 6 f on "bug / error"; it flips on the X axis in 4 f on "fixed"; the code blurs to 6 px 8 f later | Bugs, mistakes, self-correction | bespoke | x + L pill |
| **P-12** | **Grid fill** | figure | A 12 × 8 grid of rounded squares (56 px, gap 14, radius 10) at x 126–954, y 780–1340; empty cells `mute` 12%; filled cells coloured along `G-fill` by column; the counter top-right (Instrument Serif 120 px `primary`) + a micro label ("{UNIT} RUNNING") top-left | Cells fill in reading order, 1 cell / f, up to each step's value; the counter rolls to the same step (12 f) and lands on the spoken number | Capacity, scale, "N machines / people / days", a share of a whole (out of 96 or 100) | `VEOS.data.counter` + a bespoke grid bound to the same figure (`grid_fill`) | figure, D counter, E6 |
| **P-13** | **Node map** | figure | W-alt graph paper; 6–9 nodes (circles 60–90 px in `primary`, `accent`, `highlight`, `good`) with mono chip labels (white chip, 2 px ink outline, mono 30 caps, redundant); a centre node (ink circle 120 px with the result glyph) appears last; a footer micro label ("EVERY METHOD: …") | Nodes pop 6 f, 4 f stagger, on the nouns; lines draw from each node to the centre (10 f, 2 f stagger); optional value chips (mono 30) slide up at the bottom on their numbers | Many ingredients combining, existing methods, "pulled it all together" | **`fx.diagram`** (nodes + edges) | one element, L |
| **P-14** | **Check bars** | figure | A portrait (P-07 style) top-left; a day counter numeral right (Instrument Serif 200 px `primary` + "DAYS CHECKING"); two progress bars (track `mute` 25%, fill `accent`), each with a mono label and a % value; a result chip under them, with a `primary` oval drawn around it | The counter steps on the time words; bar 1 fills to 100% in 18 f, then "✓ PASS" (`good` mono) replaces the %; bar 2 follows; the oval draws 12 f on "held up / passed" | Verification, review, testing, approval | bespoke + `VEOS.data.counter` | figure, L |
| **P-15** | **Compare bars** | figure | Vertical bars on one axis (y ticks mono 30 `mute`); old = `G-old`, new = `G-new`; under each bar a name (Inter Tight 600 40 px, `primary` / `accent`) + a micro sub-label; a dashed threshold line with a label at the right ("FRONTIER"); a marker (diamond or ✓) drops onto the winner | Bars rise 14 f, 6 f stagger, in the spoken order; the threshold draws 12 f; the marker drops 8 f with a 2-frame bounce | Old vs new, A vs B vs C, "reached the same level" | **`VEOS.data.bars`** (shared `scale_id`) + a bespoke threshold | figure, scale, L |
| **P-16** | **Off the chart** | figure | One `G-old` bar on a baseline (x 160–340) with the micro label "EXPECTED" + "off the chart ↑" (serif italic 64 px `bad`) | The bar shoots past the top edge in 10 f (ease-in), holds 0.6 s, then collapses to its true value in 12 f (ease-out) while the annotation fades; the "ACTUAL" micro label appears | Expected vs actual, "thought it was too expensive", overestimates | bespoke + figure | figure (the top is illustrative) |
| **P-17** | **Price tag** | figure | A line-drawn object outline (4 px `cream` or ink: laptop, phone, car, house, bag; `fx.icon` or paths) with the subject's glyph inside; a `primary` price tag (mono value via `ctx.fmtNum`) on a string | The outline draws 14 f; the glyph fades in 6 f; the tag swings in from the top-right and settles with a 10 f pendulum (±12° → 0) | "For the price of X", real-world cost comparisons | bespoke + figure | figure, L |
| **P-18** | **Slider matrix** | figure | W-alt; 3–5 rows: a left pole label (mono 30 caps), a track with 3 dots, a right pole label; a soft `accent` ribbon (90 px wide, 22%) | The ribbon sweeps through the active dot of each row from the left column to the right column over 24 f (ease-in-out); the final dot glows `primary`; the active poles get a chip | The summary: what changed, before → after on several axes | bespoke canvas | L; the last card of F-A |
| **P-19** | **Horizon** | figure | A half disc (`primary`, grain) above a thin horizon line, its blurred mirror below; a serif label top-left (Instrument Serif 72 px `primary`) + a micro sub-label | The disc rises 16 f from the horizon; the label types 1 char / f | Model vs reality, a simplified version, "this isn't the real world" | bespoke | illustrative; L |

**B-2 Window & ad cards (the F-B home family)**
| ID | Pattern | Type | What's on screen | Motion (30 fps) | Use for | Engine | Class / needs |
|---|---|---|---|---|---|---|---|
| **P-20** | **Window card** | overlay | A `card` window x 80–1000, y 640–1300, radius 14, **5 px `line` outline, hard shadow +12/+14** (`line`, or `primary` on cream); a 60 px title bar with three outlined dots, a mono filename (decorative) and window buttons; inside, the title in Barlow Condensed 700 **120 px** caps (line 1 ink, line 2 `primary` deepened) + a tag chip (`accent`) | Hook: settles from a perspective skew (rotateY −10°, rotate −4°, scale 0.94) in **6 f** expo-out (v02 0:00 → 0:00.24). Body: **T-08 grow-in** from a `primary` chip (scale 0.25 → 1, fill `primary` → `card`, 6 f), then the title slab slams (5 f) and the lines rise (4 f each); a second window sits offset behind (+18/+22, `primary` fill) as a stacked deck (v02 0:18.2–0:19.1); chips pop last | The offer, the product, a module, a statement | bespoke `VEOS.scene` (one element, chips inside) | D title, L chips, x chrome |
| **P-21** | **Slug header** | headline | The F-B lockup (§5.2): `// slug` pill + a 2-line Barlow Semi Condensed header | Slug pop 7 f; the lines type 1 char / f; a section change = slug swap + retype | Every F-B section in L-pip / L-graphic | bespoke, `kind: "lockup"` | D + L (E3 redundant) |
| **P-22** | **Chip row** | annotation | 2–4 chips (§5.4) on the bottom edge of the card, slightly rotated | Each pops 0.6 → 1.15 → 1 in 4 f (one overshoot frame), 5 f stagger, on its attribute word | Attributes: duration, format, level, price | inside the P-20 scene (events) | L |
| **P-23** | **Tile grid** | overlay | Inside a window, 2 × 2 tiles (fills `primary`, `accent`, `#F6D9D5`, white; 3 px outline), each with an `fx.icon` 64 px, a 2-line label (Barlow Condensed 56 px) and a mono micro chip (step / week); a cursor arrow | Tiles pop 6 f, 5 f stagger, on their nouns; the cursor glides 10 f to the tile being named and taps (scale 0.94, 3 f) | Modules, features, a curriculum, what's included | bespoke | L |
| **P-24** | **Profile fan** | insert | 2–3 profile cards (520 × 700) with a colour panel (`primary` / `accent`) holding the photo, the name (Barlow Condensed 56), a role chip and a micro credential line | They fan in from the right (rotation −6° / +4°, 8 f, 6 f stagger); a star sticker (`fx.icon('star')`, `accent`) pops on the last name | Instructors, team, founders, coaches | `fx.shot` (creator photos) else **`fx.silhouette`** | L; insert (person) |
| **P-25** | **Stopwatch** | figure | A stopwatch (`primary` ring, 5 px ink outline) with an `accent` sector; the minutes counter (Poppins 800 160 px, ink stroke, hard shadow); a unit chip ("MINUTES", `accent`, skewed −4°); a header "IT TOOK ME [ONLY]" (Barlow Condensed 56 + chip) | The sector sweeps clockwise in step with the counter (an 18 f roll to each step); the unit chip pops 6 f | Time to do it, setup time, speed claims | `VEOS.data.counter` + a bespoke dial | figure, D |
| **P-26** | **Receipt** | figure | A receipt (white, zig-zag bottom, 5 px `line`) with "LESS THAN" mono + the value (Poppins 800 120 px) + a coin icon (`good`) | It prints downward in 16 f (clip reveal) beside the shrunk stopwatch; the value rolls 10 f | The cost of doing it, "for less than $1" | bespoke + figure | figure |
| **P-27** | **Ticker card** | figure | A `primary` card (x 64–1016; in L-stack y 140–860) with an ink header strip (mono 34 "Billing Information" in paper) and 2–3 rows: a logo plate (creator logo, else the name set in type on a white chip) + "–" + the value (Poppins 800 **150 px** white, 5 px ink stroke, hard shadow +8/+10) in a fixed-width value box | Values step every **4 f** towards the next figure step (E6 hard swap in `data-slot` boxes), rows in sync; the card itself is still | Bills, costs, prices rising, counts climbing in real time | `VEOS.data.counter` per row (steps, `roll` 0) or bespoke with `ctx.figAt` | figure, E6, D; insert (product) for logos |
| **P-28** | **Router fork** | figure | A name box (`primary` fill, 5 px outline, hard shadow, Barlow Condensed 96 px) at the top; dashed connectors to 2 option boxes (white, ink outline, Poppins 600 48 px); a cursor | The box pops 6 f; the connectors draw 10 f; the options pop 6 f, 4 f stagger; the cursor clicks the box (3 f); the chosen branch thickens to 6 px and turns `accent` / `good` on the decision word | Routing, choosing, "decides whether…", either/or | **`fx.diagram`** (nodes + dashed edges) | one element |
| **P-29** | **Ticket sort** | figure | 8–12 tilted white tickets (Poppins 600 40 / 30 px, two lines: type + name; 3 px outline) scattered over W-alt; 2–3 labelled bins (`primary` / `highlight` boxes with Barlow Condensed labels) | Tickets pop in (scale 0.2 → 1 in 3 f) at seeded positions with ±12° rotations, 1–2 new tickets per frame until 10–12 are on (≈ 0.6 s, v03 0:15.78–0:16.38); on the routing verb they fly into their bins in 14 f and align into grids | Classification, triage, sorting leads / tickets / tasks | bespoke, `ctx.rngStable` | L (≤ 12 snippets inside one element) |
| **P-30** | **Button press** | overlay | A window: a heading (Poppins 600 64 px, e.g. "0 Credits Remaining") + a `primary` button with a hard shadow ("Buy More", Poppins 700 72 px); a cursor | The cursor glides in 10 f and presses: the button's shadow collapses in 3 f and it scales to 0.96 | A pain moment, a paywall, an action the viewer knows | bespoke | D |
| **P-31** | **Icon slab** | overlay | One big flat icon (`fx.icon`, 380 px, `accent` fill + ink outline) and a tilted slab label (Barlow Condensed 110 px caps, ink, on a `primary` slab, −4°): "IF YOU'RE A / {AUDIENCE}" | The line "IF YOU'RE A" rises (4 f); the slab **slams** (scale 1.8 → 1, roll −8° → −3°, 5 f) on the audience word (v02 0:27.50): the slab is its own scene with `in: "stamp", in_frames: 5`; the icon pops 6 f later. The card leaves by T-08 shrink-out. **Optional 3D slam (VAR, off by default; the creator's slabs are flat):** a brand word or the creator's own logo as `VEOS.fx.three` `text` / `svg` dropping in with a `back`-eased key over ≈ 0.35 s and a ground shadow, box sized to the word, at most once per reel and the only 3D scene on screen (45–150 ms/frame) | Audience call-outs, "this is for you if…" | bespoke + `fx.icon` | D |
| **P-32** | **Alert window** | overlay | A window with a `good` circle "!" icon and 3 lines in Barlow Condensed 100 px ("DON'T / MISS / THIS."; the last line `primary`) | T-08 grow-in (0.25 → 1, roll −5° → −2°, 6 f; v02 0:29.26); the lines are already set | Urgency, "don't miss this" | bespoke | D |
| **P-33** | **Prompt window** | overlay | A chat window: an input bar with "+" and a send button (`good`), a `primary` message block (3 blurred text lines, decorative), tag chips down its left edge (ROLE / TASK / STYLE / FORMAT, mono 30, redundant), an attachment card | The message block slides up 8 f; the chips pop 4 f stagger on the spoken technique; the attachment card rises 8 f | How to instruct a tool, a method with named parts | bespoke (generic UI, never a real product's look) | L (E3 redundant chips) |
| **P-34** | **Media fan** | overlay | A phone (ink, play button `accent`) centred, an image card left and a post card right (tilted ±8°); chips "ADS", "CONTENT" (or the buyer's formats) | The cards fan out 8 f; the chips pop on their words; the phone's progress bar fills over 30 f | Outputs, formats, deliverables | bespoke | L |
| **P-35** | **Play grid** | figure | A headline count (Poppins 800 200 px `primary`, ink stroke, hard shadow), e.g. "1 → 100s", + a calendar icon "1 DAY"; a 6 × 4 grid of play tiles in mixed fills | The count rolls on the number word (12 f); tiles pop in a seeded order, 2 f stagger, until the grid is full | Volume, scale of output ("hundreds a day") | `VEOS.data.counter` + a bespoke grid | figure, D |
| **P-36** | **Cycle diagram** | figure | A dashed ellipse loop with 6 nodes (small `fx.icon` circles + mono labels) around a centre avatar icon; a header chip (`primary`, mono) with the system's name | Nodes pop 4 f stagger; a dot travels the loop (1 rev / 3 s); the active node scales to 1.15 when named | An automated loop, a workflow that repeats | **`fx.diagram`** | one element |

**B-3 Type cards**
| ID | Pattern | Type | What's on screen | Motion (30 fps) | Use for | Engine | Class / needs |
|---|---|---|---|---|---|---|---|
| **P-37** | **Title slab** | headline | The F-A plate (§5.2) in the L-stack top band | Slide-in + blur 10 f; line 2 +3 f | The F-A hook | bespoke, `kind: "plate"` | D |
| **P-38** | **Word stack** | overlay (z8) | On L-full: 2–3 words of the clause stacked (Poppins 700 lowercase 110 / 140 / 110 px, white, soft shadow), left edges aligned at x 300, y 1050–1350 | Each word blurs in on its onset (blur 10 → 0, scale 1.06 → 1, **4 f**; v03 0:02.03, 0:02.27, 0:02.63); the stack clears on the hard cut | The punch clause of a hook or a claim ("you / probably / need") | **`fx.typeStack`** (`maxLines` 3, `fx.linesFromWords`) + `captions.hide` | D; captions hidden |
| **P-39** | **Numeral card** | marker | W-main (or W-alt); the numeral (Poppins 800 **720 px** white, 8 px ink stroke, hard shadow +16/+18) at y 230–800; a label box (white, 5 px outline, hard shadow +10/+12) at y 900–1060 with the item name (Poppins 700 88 px) | The numeral fades in with a 1.06 → 1 settle in 6 f (no pop; v03 0:06.53–0:06.73); the label box appears 6 f later; the name types 1 char / 2 f with a caret blinking 8 f on / 8 f off | Every F-B list item (SM-NUMERAL) | bespoke, `kind: "number"` | D |
| **P-40** | **Highlight stat** | figure | The stat line(s) in Poppins 600 110 px ink on W-main; a `highlight` bar behind each phrase; 3 columns of tiny body texture above (decorative) | The bar wipes L → R behind each phrase on its spoken word (8 f) | A headline result ("200× faster, 400× cheaper") | bespoke + figure (`ratio`) | D, figure |
| **P-41** | **Title window** | overlay | A window with an ink header strip (mono 30 "{KIND} TITLE" in paper) and the exact title typed (Poppins 800 110 px; white with an ink stroke on pink, ink on white); the last word in `primary` | The window skews in 8 f; the title types 1 char / f | The deliverable / event / course title | bespoke | D |

**B-4 Diagrams & flows:** P-13, P-18, P-28 and P-36 (above) form the diagram family; each is one element with internal labels.

**B-5 Presenter stage patterns**
| ID | Pattern | Type | What's on screen | Motion | Use for | Engine | Class / needs |
|---|---|---|---|---|---|---|---|
| **P-42** | **Split proof** | stage | L-stack: the current figure re-laid in the top band (y 140–880), the presenter below, the caption on the seam | Hard cut in (G-2); the band's figure keeps its mechanism running | The hook; the presenter commenting on a figure (opinion, caveat, "it used…") | stage `L-stack`, `via: "cut"` | — |
| **P-43** | **Guest bubble** | stage | L-pip with the slug header (P-21) left and a window card (P-20) below | Hard cut in (G-4); the ring is on from the first frame | F-B intros and section openers (≤ 8 s per run) | stage `L-pip` | — |
| **P-44** | **Card over head** | stage | L-cardtop: a P-25 / P-20 card in y 130–600 over the lowered presenter | Hard cut in (G-5); card skew-in 8 f | The presenter's own proof ("it took me…", "I did this in…") | stage `L-cardtop` | face clearance 40 px |

**B-6 Evidence & inserts** (ask, then create: §12.5)
| ID | Pattern | Stands in for | Creator-supplied | Created substitute |
|---|---|---|---|---|
| **P-45** | **App screen** | A product's UI or a screen recording | `fx.shot` / `fx.clip` in a dark window (W-dark), radius 18, a title bar, a `primary` highlight box on the field being named | **`fx.appUI`** (`chat` / `terminal` / `list` / `browser`), generic and unbranded |
| **P-46** | **Logo row** | A product or brand named | The creator's logo files in white chips | **`fx.logoPlate`**: the name set in type on a chip (never a fetched logo) |
| **P-47** | **Source clip** | Another person's interview / keynote / press clip (HA-18) | L-stack with `top: "source:<id>"`, credit line "SRC: …" | No substitute clip: open on HA-07 and use P-09 for their words |
| P-07, P-09, P-24 | Portraits, quotes, profiles | (above) | (above) | `fx.silhouette`, `fx.quoteCard` |

**B-7 Data figures:** P-02, P-03, P-05, P-06, P-08, P-12, P-14, P-15, P-16, P-17, P-25, P-26, P-27, P-35 and P-40 (above) are bound to `plan/figures.json` (§18).

**B-8 CTA & brand**
| ID | Pattern | Type | What's on screen | Motion (30 fps) | Use for | Engine | Class / needs |
|---|---|---|---|---|---|---|---|
| **P-48** | **Keyword card** | overlay (z8) | On L-full: "comment" (Poppins 800 130 px white, 6 px ink stroke) over “{{BV-08.keyword|KEYWORD}}” (Poppins 800 200 px in curly quotes, fill `accent` in brutal and editorial, `primary` in pinksage, 6 px ink stroke), centred at y 1080–1420 (below the chin) | "comment" blurs in 4 f on its word; the keyword blurs in 4 f on its word (no pop; v03 0:21.40, 0:21.64): two scenes, each `in: "blur", in_frames: 4`; it holds ≥ 1.5 s | Every CTA moment | bespoke, **`kind: "cta-keyword"`** | D; captions hidden |
| **P-49** | **Promo carousel** | overlay | W-promo; a pill "FREE · LIVE" (mono, `primary` outline) + the deliverable kind in Barlow Condensed 180 px white ("MASTERCLASS", "GUIDE", "WORKSHOP"); 3 cards in a carousel (centre card 600 × 760): the buyer's thumbnails (SH-5) or typographic tiles (FB-5); carousel dots | The header drops 8 f; the cards slide left one position every 0.8 s (12 f ease-in-out); the active dot moves | The deliverable mention in the mid CTA | bespoke + `fx.clip` for thumbnails | D; insert when thumbnails show other people |
| **P-50** | **Comment sheet** | overlay | A generic bottom sheet (`#1E1E1E`, radius 36 at the top, x 0–1080, y 820–1920) over the dimmed presenter; a title bar "Comments"; one input field in which the keyword is being typed, with a caret; no other users, no likes, no platform logo | The sheet rises from the bottom edge in **7 f** (`in: "rise", in_frames: 7`; v02 0:44.60–0:44.84); the keyword types 1 char / 2 f; it holds to the hard end | The end CTA | bespoke + the layout's `dim` treatment | L; never fake comments (NC-6) |
| **P-51** | **Decor band** | world (z1) | TH-brutal only: an outlined star, a `primary` squiggle, a 6 × 6 dot matrix and a lime sparkle in the bottom band (y 1580–1860), plus one sparkle beside the card | Static; the sparkle twinkles (scale 0.9 ↔ 1.1 over 30 f) | Every TH-brutal L-graphic and L-pip frame | bespoke z1 scene (no text) | z1: not counted as an element |
| **P-52** | **Sponsor chip** | brand | A chip "Paid partnership" (TC-legal mono 24) top-left at y 150 + the sponsor's name set in type | Fades in 6 f, holds ≥ 2 s | Sponsored reels (NC-12) | bespoke | g |

### 8.4 Line → pattern lookup `[NICHE]`
Classify every sentence with this table (P5). Two example niches fill the right-hand columns; the editor appends the buyer's own line types per reel.

| Line type | Primary | Alternates | [NICHE: finance] example | [NICHE: fitness] example |
|---|---|---|---|---|
| A duration / time passing | P-02 | P-08 | "it took ten years of saving" | "eight weeks of training" |
| A count of layers / rounds / iterations | P-03 | P-05 | "three rounds of funding" | "five sets, each one harder" |
| Something growing step by step | P-05 | P-15 | "fees compound every year" | "every week adds 2 kg" |
| The single number the sentence is about | P-06 | P-17 | "the record return was 8%" | "the record is 42 minutes" |
| People named | P-07 | P-24 | "two economists at a university" | "the coach who trained…" |
| "Nobody has done it since…" | P-08 | P-05 "?" slot | "unbeaten since 2009" | "the record has stood for 4 years" |
| Someone's public words | P-09 | P-41 | "the CEO wrote…" | "the athlete posted…" |
| A process running by itself | P-10 | P-36 | "the bot rebalances every night" | "the app adjusts your plan nightly" |
| A mistake and its fix | P-11 | P-28 | "it caught its own error" | "fix your form, not the weight" |
| Capacity / a share of a whole | P-12 | P-35 | "96 of 100 funds" | "30 of 31 days" |
| Many ingredients combine | P-13 | P-23 | "four income streams" | "sleep, protein, steps, strength" |
| Verification / testing | P-14 | P-15 | "audited for two weeks" | "tested on 500 people" |
| A vs B (vs C) | P-15 | P-28 | "index vs active vs savings" | "walking vs running" |
| Expected vs actual | P-16 | P-15 | "everyone thought it would cost millions" | "you think you need 2 hours" |
| "For the price of…" | P-17 | P-26 | "the cost of one coffee a day" | "less than a gym day-pass" |
| What changed (summary) | P-18 | P-15 | "from guessing to a system" | "from random workouts to a plan" |
| Model vs reality / caveat | P-19 | L-full turn | "this is a backtest, not the future" | "this was a lab study" |
| The offer / product / module | P-20 | P-41, P-46 | "the 30-day money course" | "the 12-week strength program" |
| Attributes of the offer | P-22 (inside P-20) | P-23 | "6 weeks, live, beginner-friendly" | "3x a week, home or gym" |
| What's included | P-23 | P-13 | "budget, invest, tax, insurance" | "strength, mobility, nutrition, sleep" |
| Instructors / team | P-24 | P-07 | "taught by two accountants" | "built by two physios" |
| "It took me only…" | P-25 (+ P-44) | P-26 | "set up in 20 minutes" | "a 25-minute session" |
| The cost of doing it | P-26 | P-17 | "for less than $5 a month" | "for $1 a day" |
| A bill / cost / count rising | P-27 | P-05 | "your subscriptions add up" | "calories creep up every meal" |
| A decision / routing | P-28 | P-15 | "decide: pay off debt or invest" | "decide: cardio or weights first" |
| Classification / sorting | P-29 | P-28 | "sort every expense into three buckets" | "sort foods into fuel and treats" |
| A pain moment the viewer knows | P-30 | P-27 | "insufficient balance" | "the scale didn't move" |
| An audience call-out | P-31 | P-32 | "if you're a freelancer" | "if you're over 40" |
| Urgency | P-32 | P-48 | "enrolment closes Sunday" | "only 20 spots" |
| How to instruct / a method with parts | P-33 | P-13 | "give the app these four rules" | "tell your coach these four things" |
| Outputs / formats | P-34 | P-35 | "reports, alerts, a monthly summary" | "plans, videos, check-ins" |
| Volume / scale of output | P-35 | P-12 | "hundreds of transactions a day" | "hundreds of reps a week" |
| An automated loop | P-36 | P-10 | "auto-invest every payday" | "plan → train → log → adjust" |
| A headline stat | P-40 | P-06 | "3× cheaper, 10× faster" | "2× the strength gains" |
| The punch clause of a claim | P-38 | P-48 | "you probably need this" | "you're doing it wrong" |
| A product UI / screen recording | P-45 | P-33 | the app's dashboard | the tracking app |
| A brand or tool named | P-46 | P-20 | "a broker like X" | "an app like Y" |
| A turn / caveat / opinion | L-full + Z-1 | P-42 | "But here's the catch" | "Now, this isn't for everyone" |
| CTA | P-48 → P-49 / P-50 | P-41 | "comment BUDGET" | "comment PLAN" |

### 8.5 Data and truth rules
1. **Every number is a figure** (§18) with provenance; `ctx.fmtNum` writes it; counters land within ±5 f of the spoken number.
2. **Small quantities are countable** (≤ 100): 96 machines are 96 cells (P-12), 9 loops are 9 rings (P-03).
3. **Same axes:** compared bars share one `scale_id` (P-15, P-05).
4. **Old = red, new = accent** (§4.2); `good` only for a pass, a fix or a saving.
5. **Illustrative concept graphics** (P-04, P-16 before it lands, P-19) carry no unsourced numbers; when a number appears on them, add the TC-legal "example" tag.
6. **Script-stated hypotheticals** ("if you invested $100 a month…") are figures with `from: script` and the words.
7. **One idea per card:** ≤ 3 animated groups; everything else is static or dimmed to 40%.

### 8.6 Comedy layer
OFF (`profile.tone.comedy = off`; `comedy_max: off`).

### 8.7 Asset rules
- **Real captures first** for the buyer's own product: screen recordings (SH-2) in P-45.
- **Mocks** are generic and unbranded (`fx.appUI`, `fx.device`), never a look-alike of a real product.
- **No stock, no film clips, no memes, no AI people** (N7). v03's film clip and illustrated clerk are not copied.
- **Logos** come only from the creator's files; otherwise P-46 type plates.
- **Ask, then create** for every third-party moment (§12.5): photos of named people, other people's posts, product UIs, source clips, thumbnails showing other people.

### 8.8 Density and variety
- An event (weight 1) every ≤ 2.0 s; a hard cut every 1.5–3.0 s on average.
- ≥ 8 different patterns and ≥ 4 families per 60 s.
- The same pattern at most 2 cards in a row (the numeral-card ritual is the exception); the same world at most 4 cards in a row in TH-editorial and TH-brutal.

---

## §9 Transitions & shot grammar `[REQ] [DNA]`

### 9.1 Library
| ID | Transition | Frames | Recipe | SFX role |
|---|---|---|---|---|
| **T-01** | **Hard cut** | 0 | A stage or scene swap on a word boundary ±1 f (`via: "cut"`, scene `cuts`). Graphic → graphic: the new card is complete on the cut frame (no camera move; v01 0:38.70). Graphic → presenter: always with the Z-1/Z-2 settle (§10.2) | light whoosh or tap from the pool, at most 1 per 2 s |
| **T-02** | **Card skew-in** | 6 | The hook window card settles from a perspective tilt (rotateY −10°, rotate −4°, scale 0.94 → 1), expo-out (v02 0:00–0:00.24). Hook only | pop |
| **T-03** | **Push** (pinksage) | 9 | The current card exits left (x 0 → −1080, ease-in) while the next element enters from the right (x +1080 → 0, expo-out), same frames, no fade (v03 0:09.80–0:10.12). Scene presets `out: "slide-l", out_frames: 9` on the old card / `in: "slide-r", in_frames: 9` on the new one (not the built-in `push` transition: that moves the world too, and here the pink world stays put) | swish |
| **T-04** | **Evolve** | 5–6 | Same card, next state: the hero numeral dims to ≈ 20% with a 4 px blur in 5 f while the portrait scales 0.2 → 1 with a fade in 4 f, no overshoot; its name fades in 4 f later (v01 0:21.00–0:21.45) | none, or a pop |
| **T-05** | **Slab slide** | 12 | The F-A title slab: line 1 from the right, line 2 from the left, horizontal blur (§5.2) | the hook hit |
| **T-07** | **Iris wipe** (brutal) | 8 | Section change: a `primary` disc grows from the frame centre to cover the frame, then a `card`/world-coloured disc grows inside it; the PiP bubble stays on top; the new section's content starts after (v02 0:06.13–0:06.41, 7 f @25). Built in: `{"t": <cut>, "type": "iris", "reveal": "open", "at": "centre", "frames": 8, "ring": 200, "colour": "primary"}` (the new frame opens in a circle led by a thick 200 px `primary` band: the measured orange disc lagging ahead of the cream one). The old frame is shown frozen under it, so start the next section's scenes on the cut | whoosh |
| **T-08** | **Grow-in / shrink-out** (brutal) | 5–7 | Card → card inside a section: the old card shrinks and fades out in 2 f; the new window grows 0.25 → 1 with its fill flashing `primary` → `card` and a −5° → −2° roll, expo-out, 6 f (v02 0:18.16–0:18.40, 0:29.26–0:29.42). Old card `out: "pop", out_frames: 2`; the grow-in stays bespoke (its fill flash and roll are not a preset) | pop |
| **T-09** | **Flash-in** (pinksage) | 6 | A new card appears as a flat white panel, then its fill and content fade up to their colours in 5–6 f; a follow-up card lands overlapping it lower (deck stack) (v03 0:03.34–0:03.90) | tap |
| **T-10** | **Blank beat** (brutal) | 6 | After a hard cut from footage or a screen recording, the empty world holds ≈ 6 f before the next card's slam (v02 0:27.04–0:27.30); at most 2 per reel | none |
| **T-06** | **Hard end** | 0 | Cut to nothing ≤ 6 f after the last word | — |

No dissolves, light leaks, zoom-throughs or glitches (N3; the engine's `glitch` transition exists but none of the three reels uses one, so it stays out). T-07/T-10 are brutal-only, T-03/T-09 pinksage-only; the editorial pack uses T-01 and T-04 only.

### 9.2 Grammar
| Boundary | Use | Never |
|---|---|---|
| Frame 0 | The figure already moving + T-05 (F-A) / the ticker already ticking (F-B) | A fade-in, a black frame |
| Hook → body | T-01 to the first L-graphic card on the second clause | A morph |
| A new idea / card | T-01 (editorial); T-08 or T-01 (brutal); T-09, T-03 or T-01 (pinksage) | A crossfade |
| A new section (F-B brutal) | T-07 iris wipe, then the slug lockup | T-07 more than once per section |
| The same idea continues | T-04 evolve | A hard cut mid-sentence |
| To the presenter | T-01 to L-stack (+ Z-2) / L-full (+ Z-1), every time | The `pop-back` / `grow-from-card` morphs; a cut to footage without the settle |
| A new list item (F-B) | T-01 to the P-39 numeral card on the ordinal word | Anything with a lead over 2 f |
| A number lands | An internal event (counter landing, bar top) | A camera shake |
| CTA | T-01 to L-full + Z-1, then P-48 | — |
| The last word | T-06 | A black tail > 0.2 s |

### 9.3 Shot grammar (spine `hybrid`)
- **R-1** Cut on the first content word of a sentence (±2 f), never inside a word or a name.
- **R-2** Presenter runs: L-full ≤ 4.0 s; L-stack ≤ 5.0 s; L-pip ≤ 8.0 s; L-cardtop ≤ 3.0 s.
- **R-3** Jump cuts inside the A-roll (dead-air removal) happen *under a graphic* whenever possible. On an L-full run each jump cut gets the next settle (Z-1 ↔ Z-2 alternate), so the jump reads as intentional.
- **R-4** A claim, pain or CTA sentence starts on L-full (+ Z-1) when the previous 6 s had no presenter.
- **R-5** Never cut back to the same layout with the same crop twice in a row.

Transition map (part of the plan; example timings from a 75 s F-A reel):
```yaml
transitions:
  - {t: 0.00, id: T-05, to: L-stack, note: "title slab slides in; figure already rolling"}
  - {t: 1.64, id: T-01, to: L-graphic, note: "FIG. 01 on 'by'"}
  - {t: 6.26, id: T-01, note: "FIG. 02 on 'This'"}
  - {t: 9.00, id: T-01, to: L-full, camera: Z-1, note: "presenter on 'which is the formula'"}
```

### 9.4 Budget (per 60 s)
- T-01: 20–35 (it is the rhythm itself). T-02: once (F-B hook). T-03: 1–3 (pinksage). T-04: ≤ 6. T-05: once (F-A hook). T-07: one per F-B section (2–4). T-08: 3–8 (brutal). T-09: 3–8 (pinksage). T-10: ≤ 2.
- Measured cadence of hard cuts: v01 2.1 / 10 s (median 3.0 s, p90 9.2 s, including evolves), v02 3.4 / 10 s (median 2.0 s), v03 5.7 / 10 s (median 1.3 s). Cuts to the presenter: v01 8 in 75 s, v03 5 in 44 s.
- Three T-01 in a row is normal (it is the style); any other transition never 3× in a row.
- Cuts sit within ±1 f of word boundaries; the audio is never offset.

---

## §10 Motion, camera, layers, finishing `[REQ] [DNA; motion tokens TUNE ±15%]`

### 10.1 Motion tokens (30 fps)
| Token | Value |
|---|---|
| Beat lead | 2 f before the onset |
| Card entry (B-1) | **0 f**: the F-A card is complete on the cut frame (`in: "none"`); later elements pop or fade in 4–5 f on their words; draws 10–14 f |
| Window skew-in (B-2, hook) | 6 f, expo-out, rotateY −10°, rotate −4°, scale 0.94. Body windows use T-08 grow-in (6 f) |
| Slab slam (P-31, window title slabs) | 5 f: scale 1.8 → 1, roll −8° → the slab's resting −3°, ease-in, no overshoot: `in: "stamp", in_frames: 5` (v02 0:18.53, 0:27.50: 4–5 f @25) |
| Header line rise | 4 f per line behind a clip line, expo-out; line 2 ≈ 10 f after line 1 |
| Blur-in (word stack, CTA words) | 4 f: `in: "blur", in_frames: 4` (measured 3 f @25) |
| Cut-in settle (Z-1 / Z-2) | 20 / 22 f, `ease: "expoOut"`, half the zoom gone by f4; Z-1 also rolls 4° → 0 (§10.2) |
| Pop (chips, nodes, portraits) | `in: "pop", in_frames: 4`: 0.6 → 1.08 → 1.0 in 4 f (chips overshoot one frame; portraits none). F-B numerals fade + settle 1.06 → 1 in 6 f (v03 0:06.53–0:06.73), no pop |
| Slab slide | 10 f, x +260 → 0, horizontal blur 12 → 0 px |
| Typing | 1 char / 2 f (label boxes, title windows); 22 chars / s (terminal, code lines) |
| Counter roll | 18 f ease-out to each step (F-A); tickers step +1 every **4 f** without easing (F-B, E6) |
| Bar grow | 14 f expo-out, 3–6 f stagger |
| Ring draw | 6 f per ring |
| Particle drop | 1 dot / 6 f, a 10 f ease-in fall, seeded |
| Comment sheet rise (P-50) | `in: "rise", in_frames: 7` (measured 6 f @25) |
| Exit | none on a hard cut; T-08 shrink-out `out: "pop", out_frames: 2`; T-03 push `out: "slide-l", out_frames: 9`; fades only at the end of the comment sheet (4 f) |
| Hold | titles ≥ 10 f after complete; text ≥ 0.25 s / word; cards 1.5–3.0 s |

Counters roll eased in F-A (premium) and tick linearly in F-B tickers (v03 looks mechanical on purpose). The linear tick is an E6 hard swap inside a fixed box, so G3 holds.

### 10.2 Footage camera: `zoom_policy: crop_on_cut` (the cut-in settle)
Measured at 25 fps with ORB between consecutive frames: **every** hard cut to presenter footage lands zoomed in and eases out to rest; graphic → graphic cuts carry no camera move (scale 1.000).

| ID | Preset | Recipe (30 fps) | Use | Evidence |
|---|---|---|---|---|
| **Z-1** | `pull-out` | On the cut frame the footage is at **1.26** and eases out to 1.0 over **20 f** (expo-out: 1.26 → 1.16 by f2 → 1.10 by f5 → 1.04 by f12); 1–2 f of motion blur come with the speed. The source also rolls **3–6°** back to 0 over the same frames. Preset: `scale [1.26, 1.0]`, `frames 20`, `ease: "expoOut"`, `rotate: [4, 0]` (the measured median; per event `p.rotate: [3..6, 0]`, sign as shot), `blur: {kind: "radial", amount: 0.1, at: "face", frames: 2, shape: "decay"}` | Every cut to L-full | v01 0:09.00 (1.24, roll 5.9°), 0:26.40 (1.26, 4.2°), 1:05.96 (1.27, 3.5°); v03 0:02.00 (1.32), 0:21.20 (1.24), 0:29.20 (1.18) |
| **Z-2** | `pull-out-wide` | **1.40** → 1.0 over **22 f**, same curve (`ease: "expoOut"`, the same 2 f radial blur), no roll; the L-stack graphic band settles with it inside its own scene (G-2) | Every cut to L-stack and the hook; an L-full cut that follows another L-full cut (presets never repeat) | v01 0:00 (1.53), 0:13.72 (1.49), 0:45.12 (1.35), 1:02.84 (1.52), 1:11.92 (1.38) |

Rules: only on a hard cut (±2 f of the stage change); only ever **out** (never a punch-in, N4); Z-1 and Z-2 never twice in a row; nothing else moves the camera; no settle on graphic → graphic cuts. A 1080p source starts at ≤ 1.40× (the face is soft for ≈ 6 f, as in the evidence). Frequency: one per presenter return, ≈ 1 per 10 s.

### 10.3 Canvas camera
OFF (§21).

### 10.4 Layer order (back to front)
1. The world (W-main / W-alt / W-dark / W-promo) + the P-51 decor band (z1)
2. —
3. The card / figure (z3), one per frame
4. Presenter footage (stack bottom, PiP, full): the stage layer
5. Labels drawn outside a card (rare; prefer inside)
6. Marker overlays (z6)
7. CS-1 captions (z7)
8. Word stack, keyword card (z8; captions hidden)
9. —
10. The F-B header lockup, the F-A title slab (z10)
11. —

### 10.5 Finishing
- **Editorial:** film grain 0.06 and vignette 0.30 on W-main (world tokens); soft glows only on the spheres of P-04, the ring dot of P-03 and the timeline dot of P-08.
- **Brutal / pinksage:** no grain on cards (pink world grain 0.05); **hard offset shadows only** (no blur) on cards, windows, chips, numerals and ticker values; no glows.
- Footage is untouched (no grade), except the halftone treatment on supplied portrait photos (§4.4).
- Card radius: windows 14, F-A cards 18–24, chips 30, pills 10.

---

## §11 Sound contract (minimal) `[REQ] [VAR]`

Sound comes from the bundled SFX pack and its global rules (S1–S6: every cue marks a visible event, ≤ 2 uses per file, one list-cue exception, no consecutive repeats, catalogue ids only).

| Line | Decision |
|---|---|
| **Cue moments** | `hook` (the f0 hit, the first value landing), `transitions` (hard cuts between ideas: light whooshes or taps, at most one per 2 s; a whoosh on every T-07 iris wipe and T-03 push; a pop on a slab slam), `reveals` (counter landings, bars topping out, ✓ PASS, the numeral card), `list_cue` (one file for every numeral card), `cta` (the keyword pop, the sheet rising). A ticker run gets **one** tick-run cue, never one per step |
| **Meme cues** | Off (comedy off) |
| **Music bed** | On, from **f0**, under the whole reel (unverified: the audio was not observable) |
| **Ducking** | The bed sits ≥ 18 dB under the voice while the voice speaks; creator-supplied clips (P-47) keep their own audio, ducked under the voice |
| **Loudness** | −14 LUFS integrated, true peak ≤ −1.5 dBTP; hard end ≤ 6 f after the last word (NC-8) |

---

## §12 Footage, shot list, fallbacks, inserts `[REQ]`

### 12.1 Setups `[DNA what the style assumes; VAR the buyer's setups]`
| Setup | Spec |
|---|---|
| **A: seated / standing vertical take** | 9:16 at ≥ 1080 × 1920, ≥ 30 fps (conform to 30 CFR), chest-up framing, eyes at 38–42% of frame height, head top at y 260–420; a plain or bright backdrop (a printed sky, a colour wall, plants), soft key; a lav or a handheld mic may be in shot (v02 holds one); a plain dark or mid-grey tee |

The evidence presenters sit in front of a printed sky with a rainbow arch (v01, v03) or on a sofa against a blue wall (v02). Neither is required; any clean backdrop works because the presenter is framed small or in a band.

### 12.2 Shot list
| ID | Shot | Spec | Count per 60 s | Must / optional | Formats |
|---|---|---|---|---|---|
| **SH-1** | The talking-head take | Setup A, one continuous take or a few takes of the script | 1 | **must** | F-A, F-B |
| SH-2 | Screen recordings of the buyer's own product, tool or workflow | 1080 px wide or more, 4–10 s each, cursor visible, no private data | 0–3 | optional | F-B |
| SH-3 | A source clip the creator owns or holds (interview, keynote, press clip) | 2–4 s, the person or event the claim is about | 0–2 | optional | F-A (HA-18) |
| SH-4 | Portrait photos of the people named in the script | ≥ 600 px, face centred | 0–3 | optional | F-A, F-B |
| SH-5 | 3–6 thumbnails or stills of the buyer's own content or event | 9:16 or 4:5 | 0–1 set | optional | F-B (P-49) |

### 12.3 Fallbacks
| ID | For | What the engine does instead | Fidelity cost | Result |
|---|---|---|---|---|
| FB-2 | SH-2 | `fx.appUI` recreated generic window (chat, terminal, list, browser) built from the script's words | no real UI texture | holds |
| FB-3 | SH-3 | Open on HA-07 instead of HA-18; the person's words go on a P-09 quote note (exact spoken quote) | loses the "someone else said it" authority beat | holds |
| FB-4 | SH-4 | `fx.silhouette` portraits with the name and role in mono labels | no faces | holds |
| FB-5 | SH-5 | Typographic tiles (the deliverable title split over 3 cards) on W-promo | no product imagery | holds |

SH-1 has no fallback: without a presenter take, use a voice-over style template instead.

### 12.4 Props, reaction bank, matte, resolution
- Props: none. Reaction bank: none (no comedy layer).
- Matte: **none** (no behind-subject type, no depth sandwich).
- Minimum source resolution: 1080 × 1920 (the Z-2 settle starts at 1.40×; its first frames are soft and motion-blurred, as in the evidence).

### 12.5 Third-party inserts: ask, then create `[REQ always]`
Claude never fetches anyone else's media. Per reel:
1. **Scan** the transcript (`veos inserts scan`) and list the moments that call for third-party material. In this style they are typically: a named person (P-07 / P-24), someone's public words (P-09), a product or tool's UI (P-45), a brand or tool name (P-46), a source clip (P-47), and thumbnails of other people (P-49).
2. **Ask the creator once**, as a short list: "For these N moments, do you have a photo, screenshot, logo or clip you own or hold? Drop the files, or say no."
3. **Supplied:** use the file as given (crop, frame, halftone portraits, highlight a field); never alter it to say something it doesn't.
4. **Not supplied:** build the created substitute named in §8.3 (B-6): `fx.silhouette`, `fx.quoteCard`, `fx.appUI`, `fx.logoPlate`, typographic tiles. Created quote cards quote the script verbatim (NC-13).
5. **Record** every insert in `plan/inserts.json` `{id, moment, origin: "creator" | "created", file?, recipe?, substitute_of?, quote_text?}`.

### 12.6 Frame rate and audio
30 fps CFR output, 1080 × 1920, BT.709. One voice track: high-pass 80 Hz, de-ess, light compression, −14 LUFS.

---

## §13 Output contract `[REQ] [DNA]`

### 13.1 Beat sheet (the first yaml block of the edit brief)
```yaml
- id: 4
  section: FIG-02                      # F-A: HOOK | FIG-nn | TURN | CTA ; F-B: HOOK | PRODUCT | ITEM-n | CTA-MID | BENEFIT | CTA-END
  t0: 6.26
  t1: 8.90
  spoken: "This was a nine-loop scattering amplitude problem,"
  trigger: {word: "nine-loop", at: 7.10}
  tone: explain                        # claim | explain | proof | warn | win | cta
  line_type: "count of layers"
  layout: L-graphic
  world: W-main
  visual: "FIG. 02 SCATTERING AMPLITUDE: rings add one by one around a centre numeral that counts 1 → 9; the formula label appears on 'amplitude'"
  layers: [fig02-rings]
  pattern: P-03
  figure_id: loops                     # data_figures
  caption: {profile: CS-1, overrides: []}
  source: {masthead: "ANTHROPIC", date: "SEP 2026", headline: null}   # citations (F-A SRC line)
  insert: null                         # {id, origin} when a third-party moment is shown
  exception: E6                        # the numeral steps inside a fixed box
  sfx: [{id: "<catalogue id>", on: "fig02-rings@0.84", why: "ring 9 lands on 'nine'"}]
```

### 13.2 Conditional fields used by this style
| Switch / module | Beat fields |
|---|---|
| captions (full) | `caption {profile: CS-1, overrides[]}` (emphasis is always off) |
| data_figures | `figure_id` (or `figures`) for every beat that shows a number |
| citations (F-A) | `source {masthead, date, headline?}`, `credit` |
| themes (`per_reel`) | the theme lives in the reel header, not per beat |
| any third-party moment | `insert {id, origin: creator \| created}` |
| declared exception | `exception: E3 \| E6` (also on the scene) |
| brand | `sponsor {id, disclosure}` when sponsored |

### 13.3 Reel header (top of the edit brief)
```yaml
reel:
  format: F-A                      # F-A | F-B
  theme: TH-editorial              # TH-editorial | TH-brutal | TH-pinksage (one per reel)
  hook_archetype: HA-07            # HA-07 | HA-18 | HA-02
  structure: explainer             # explainer (F-A) | list (F-B)
  count: null                      # F-B: the number of list items (= numeral cards)
  keyword: "{{BV-08.keyword|KEYWORD}}"
  deliverable: "{{BV-08.deliverable|the free resource}}"
  figures: plan/figures.json
  fig_numbers: [01, 02, 03, …]     # F-A: the FIG numbers in order
  inserts: plan/inserts.json
  sponsor: null
```

### 13.4 Hook proposals (3 required)
```yaml
- name: "Live grid: 9 in 10 lost"
  archetype: HA-07
  headline: {kind: plate, lines: ["INDEX FUNDS", "BEAT 9 IN 10"]}
  hook_pair: {claim: "Nine out of ten fund managers lost to an index fund", number: "90 of 100 (script)", figure: P-12}
  stoppers: [ST-1, ST-2, ST-3, ST-5, ST-6]
  captions: {profile: CS-1, first_chunks: ["Nine out", "of ten", "fund managers"]}
  storyboard: "f0 stack: 10x10 grid filling red, counter rolling | 0.5 counter lands 90 on 'ten' | 1.7 cut FIG. 01 full grid + FIFTEEN YEARS micro | 4.3 FIG. 02 fee bars"
  sound: [hook hit f0, reveal on 0.5 landing, transition 1.7]
  stopper_test: {thumbnail: pass, mute: pass, read_s: 1.0, changes_3s: 7, payoff_s: 0.5}
```

### 13.5 Checkpoint (before building)
Send:
1. The format, the theme and why (§0.4, §4.3).
2. 3 hooks with headlines and stopper tests.
3. The beat sheet (with tones, layouts, patterns, FIG numbers) and the transition map.
4. **`plan/figures.json`** with `veos figures` output (shown vs recomputed values) and every number's provenance; flag mismatches with the script.
5. The citation list (F-A SRC lines, quotes) and `plan/inserts.json` (creator-supplied vs created).
6. The fallbacks used (§12.3).
7. The SFX ledger.
8. Style stills: f0 (thumbnail), the first value landing (≤ 1.0 s), one card per layout used, one numeral card (F-B), the CTA keyword card.

**Wait for approval.**

---

## §14 Worked examples `[REQ] [NICHE]`
Timings are estimates; replace them with `words.edit.json` onsets. Numbers are example script values: in a real reel each comes from the script, the creator or a cited source.

### 14.1 F-A editorial · [NICHE: finance] · "Index funds beat 9 in 10 fund managers" (≈ 62 s, TH-editorial, HA-07)
**Spoken hook:** "Nine out of ten professional fund managers lost to a simple index fund over fifteen years… and the index fund charged almost nothing."
**Headline (plate):** "INDEX FUNDS / BEAT 9 IN 10".

| t (s) | Spoken | Layout | Visual | Caption | Cue |
|---|---|---|---|---|---|
| f0 | — | L-stack | Top band: P-12 grid (10 × 10, y 160–640) filling `bad` cells, counter rolling from 0; title slab line 1 sliding in at y 800 | "Nine out" on the seam | hook hit |
| 0.5 | "…of ten" | — | Counter **lands 90** (figure `share_lost`), 90 cells red, 10 cells `accent` | "of ten" | reveal |
| 0.9 | "professional fund managers" | — | Micro label "FUNDS THAT LOST" pops over the grid | words | — |
| 1.7 | "lost to a simple index fund" | **cut** L-graphic | FIG. 01 "THE SCORECARD" · SRC: the report named in the script; the full grid (12 × 8 → 10 × 10 version), the 10 winners pulse `accent` | pill 1390 | transition |
| 3.0 | "over fifteen years" | — | P-08 timeline under the grid draws 15 years | — | — |
| 4.3 | "and the index fund charged almost nothing" | cut | FIG. 02 "WHAT THEY CHARGE": P-15 bars 1.00% (`G-old`) vs 0.05% (`G-new`), one scale | — | transition + reveal |

| Section | t | Spoken gist | Layout | Pattern | Figure / FIG |
|---|---|---|---|---|---|
| Act 2 What it is | 6.8–12 | "An index fund just buys every company in the market…" | L-graphic | P-13 node map: 9 company nodes joining one basket node | FIG. 03 |
| | 12–15 | "…so it never has to guess." | L-full + Z-1 | presenter (turn) | — |
| Act 3 Stakes | 15–20 | "A 1% fee sounds tiny." | L-graphic | P-06 hero numeral "1%" → dims (evolve) | FIG. 04, figure `fee_active` |
| | 20–26 | "On $10,000 over 30 years it costs you about $17,600." | L-graphic | P-05 bar climb by decade (two series, one scale) → P-06 "$17,628" | FIG. 05, figures `end_active`, `end_index`, `gap` |
| Re-hook | 24–27 | "But here's what nobody tells you." | L-full + Z-1 | turn beat | — |
| Act 4 How | 27–40 | "Managers trade more, pay more tax, and charge for it…" | L-graphic | P-10 run log of trades (generic) → P-11 "✕ GUESS" → "✓ MARKET" | FIG. 06, 07 |
| | 40–44 | "It's not that they're bad…" | L-stack (FIG. 07 in band) | P-42 | — |
| Act 5 Proof | 44–52 | "Over 15 years, 90 lost, 10 won." | L-graphic | P-15 compare bars (lost vs won, one scale) + ✓ marker | FIG. 08 |
| Re-hook | 49–51 | "Now, this isn't a guarantee." | L-full + Z-1 | turn | — |
| Act 6 Meaning | 51–58 | "It's history, not a promise…" | L-graphic (W-alt) | P-19 horizon "PAST ≠ FUTURE" | FIG. 09 |
| | 58–62 | "…what changes is who you pay." | L-stack | P-18 slider matrix (guessing → market, high fee → low fee, active → passive) top band | — |
| CTA (optional) | last 2.5 s | "Comment {{BV-08.keyword|KEYWORD}} for the fee checklist." | L-full + Z-1 | P-48 → P-50 | — |

`plan/figures.json` (excerpt):
```json
{"inputs": {"share_lost": {"value": 90, "from": "script", "said": "nine out of ten"},
            "principal": {"value": 10000, "from": "script", "said": "$10,000"},
            "years": {"value": 30, "from": "script", "said": "30 years"},
            "rate_active": {"value": 6.0, "from": "script", "said": "7% minus a 1% fee"},
            "rate_index": {"value": 6.95, "from": "script", "said": "7% minus 0.05%"}},
 "figures": [
  {"id": "lost", "kind": "grid_fill", "formula": "none", "args": {"value": "share_lost"}, "steps": [{"value": 90, "at": 0.5}]},
  {"id": "end_active", "kind": "bar", "formula": "compound", "args": {"principal": "principal", "rate_pct": "rate_active", "years": "years"}, "scale_id": "S-end", "round_to": 1},
  {"id": "end_index", "kind": "bar", "formula": "compound", "args": {"principal": "principal", "rate_pct": "rate_index", "years": "years"}, "scale_id": "S-end", "round_to": 1},
  {"id": "gap", "kind": "hero_number", "formula": "diff", "args": {"a": "fig:end_index", "b": "fig:end_active"}, "steps": [{"value": 17628, "at": 24.6}]}]}
```
(`end_active` ≈ $57,435, `end_index` ≈ $75,063, `gap` ≈ $17,628; the script must say "about $17,600" for the rounded caption; the card shows `$17,628` from the figure.)

### 14.2 F-B brutal · [NICHE: fitness] · "A 12-week strength program built by two physios" (≈ 46 s, TH-brutal, HA-02, keyword {{BV-08.keyword|KEYWORD}})
**Spoken hook:** "This program was built by two physiotherapists. Everything, from the warm-ups to the progressions."
**Header (lockup):** `// who_we_are` "TRAIN WITH / PHYSIOS."

| t (s) | Spoken | Layout | Visual | Caption | Cue |
|---|---|---|---|---|---|
| f0 | "This" | L-pip | Bubble top-right (ring `primary`); slug pops; header line 1 typing; P-20 window "12-WEEK / STRENGTH." skewing in (8 f) with the chip "home or gym"; P-51 decor band | "This" pill (red) | hook hit |
| 1.0 | "program was built" | — | Chips pop on the card edge: "12 weeks", "3x a week" | words | pop |
| 1.8 | "by two physiotherapists" | — | Header line 2 completes; the window title is readable (**proof by 2.5 s**) | — | — |
| 2.6 | "Everything, from the warm-ups" | cut | Window wipe (T-03) to "program.exe" with P-23 tiles (warm-up, strength, mobility, deload); slug `// what_you_get`, header "EVERY SET / PLANNED." | — | swish |
| 5.6 | "to the progressions" | — | Cursor taps the "progression" tile | — | tap |

| Section | t | Spoken gist | Layout | Pattern | Figure |
|---|---|---|---|---|---|
| PRODUCT | 6–9 | "It took us 18 months to test it on 200 clients." | L-cardtop | P-25 stopwatch → calendar variant "18 MONTHS" + chip "200 clients" | `months`, `clients` (creator) |
| ITEM-1 | 9–10.4 | "One: strength that lasts." | L-graphic | P-39 numeral "1" + label "Strength that lasts" | — |
| | 10.4–14 | "Three sessions a week, 40 minutes each" | L-graphic (W-alt) | P-35 play grid counting sessions → "36 SESSIONS" | `sessions = 3 × 12` (`sum` / creator) |
| ITEM-2 | 14–15.4 | "Two: no more guessing" | L-graphic | P-39 numeral "2" + "No more guessing" | — |
| | 15.4–19 | "The app tells you when to add weight" | L-graphic (W-dark) | P-45 creator screen recording (else `fx.appUI` list) | — |
| CTA-MID | 19–24 | "Comment {{BV-08.keyword|KEYWORD}} and I'll send you the free week-one plan" | L-full + Z-1 | P-48 keyword card → P-49 promo "FREE · PLAN" → P-41 title window "Week One: Strength Basics" | — |
| BENEFIT | 24–38 | "If you're over 35… you don't need a gym… 3 sessions, 40 minutes…" | L-graphic | P-31 icon slab "IF YOU'RE / OVER 35" → P-34 media fan (videos, plans, check-ins) → P-40 highlight stat "40 MIN · 3× A WEEK" | `minutes` |
| | 38–42 | "These are not random workouts." | L-full | presenter | — |
| CTA-END | 42–46 | "Comment {{BV-08.keyword|KEYWORD}} and I'll see you inside." | L-full + Z-1 | P-48 → P-50 comment sheet | — |

### 14.3 F-B pinksage · [NICHE: finance] · "Your subscriptions are eating your salary" (≈ 42 s, TH-pinksage, HA-07, keyword {{BV-08.keyword|KEYWORD}})
**Spoken hook:** "If your subscriptions keep climbing every month, you probably need a money audit."

| t (s) | Spoken | Layout | Visual | Caption | Cue |
|---|---|---|---|---|---|
| f0 | "If" | L-stack | Top band: P-27 ticker card ("Monthly Subscriptions" header strip), rows "Streaming – $", "Apps – $", "Cloud – $" (names set in type), values ticking every 4 f | "If your" on the seam | hook hit |
| 0.8 | "subscriptions" | — | First step lands: streaming reaches $18 (figure step at the word) | — | tick-run cue |
| 0–2.1 | "keep climbing every month" | — | Rows climb in sync to $45 / $62 / $38 (script / creator values) | — | — |
| 2.1 | "you probably need" | **cut** L-full + Z-1 | P-38 word stack "you / probably / need" | hidden | transition |
| 3.0 | "a money audit" | cut | L-graphic W-main: P-28 router box "AUDIT" with forks "KEEP" / "CANCEL" | pill | reveal |
| 3.4–6.4 | "Here are two things it fixes in a week." | cut (W-alt sage) | P-29 tickets (each a subscription) scattering | — | — |

| Section | t | Spoken gist | Layout | Pattern | Figure |
|---|---|---|---|---|---|
| ITEM-1 | 6.5–8 | "1. The forgotten subscriptions" | L-graphic (pink) | P-39 "1" + "Forgotten subscriptions" | — |
| | 8–13 | "Every charge gets sorted: keep or cancel" | L-graphic (sage) | P-29 tickets fly into "KEEP" / "CANCEL" bins | `count_cancel` |
| | 13–15 | "Most people cancel three." | L-full | presenter | — |
| ITEM-2 | 15–16.5 | "2. The auto-save rule" | L-graphic (pink) | P-39 "2" + "Auto-save rule" | — |
| | 16.5–20 | "What you cancel goes straight to savings" | L-graphic (sage) | P-36 cycle (charge → cancel → save → invest) | — |
| CTA-MID | 20.5–25 | "Comment {{BV-08.keyword|KEYWORD}} and I'll send you the audit sheet" | L-full + Z-1 | P-48 → P-41 title window "The 7-Day Money Audit" | — |
| BENEFIT | 25–36 | "That's $145 a month… $1,740 a year back." | L-graphic | P-40 highlight stat "$145 / MONTH · $1,740 / YEAR" (figure `yearly = 145 × 12`) → P-17 price tag on a laptop outline | `monthly`, `yearly` (`per_period` / `sum`) |
| | 36–39 | "Takes one evening." | L-cardtop | P-25 stopwatch "1 EVENING" | — |
| CTA-END | 39–42 | "Comment {{BV-08.keyword|KEYWORD}}, see you there." | L-full + Z-1 | P-48 → P-50 | — |

---

## §15 QA checklist `[REQ] [DNA]`

**1. Profile conformance**
- [ ] The reel header declares the format, the theme, the archetype; layouts are only the format's (V-LAYOUT).
- [ ] Presenter share within 20–35% (F-A) / 25–40% (F-B); longest absence ≤ 10 s / 8 s (V-PRESENCE).
- [ ] Duration within the format's range; one theme for the whole reel (H12).

**2. Hook**
- [ ] f0: a figure scene already moving + the claim (caption word 1 or the headline) (V-F0).
- [ ] First value lands by 1.0 s; the result number by 6.0 s (H3).
- [ ] ≥ 6 weighted state changes in 0–3 s; no weight-1 gap > 1.2 s in the hook (V-CADENCE).
- [ ] Title slab ≤ 5 words / 2 lines / 16 characters per line; or the F-B header ≤ 6 words / 12 characters per line (V-TITLE).
- [ ] The mute test passes (number + captions + headline tell the claim).

**3. Body and cadence**
- [ ] 7–16 weighted SCs per 10 s; a weight-1 change every ≤ 2.0 s; nothing static > 2.5 s (V-CADENCE).
- [ ] A hard cut per idea on its first content word ±2 f; card holds 1.5–3.0 s (F-A ≤ 7.5 s with events) (H5).
- [ ] F-A: FIG numbers start at 01 and rise monotonically; every card has its SRC line. F-B: one numeral card per promised item.
- [ ] Re-hooks at ~25 s and ~50 s (F-A turn beats); the F-B mid CTA lands at 25–50% of runtime.
- [ ] ≥ 8 patterns and ≥ 4 families per 60 s; the same pattern ≤ 2 cards in a row.

**4. Captions**
- [ ] CS-1 on every spoken word, 1–4 words, ≤ 26 characters, whole-chunk reveal, hard swap, lead ≤ 0.15 s (V-CAPTION).
- [ ] F-A 54 px / F-B 48 px on a solid pill (F-B under E3: 46–53 px, weight ≥ 600, pill contrast ≥ 4.5:1) (V-TYPE / V-EXC).
- [ ] Position: 1390 (F-A) / 1450 (F-B brutal) on L-graphic, each pinksage card's own `caption_cy`, the seam on L-stack, 1290 on L-full, 1440 on L-pip, 1430 on L-cardtop; never over the face (V-FACE).
- [ ] Hidden only under P-38 / P-48; no emphasis colours (N11). Spelling of names exact (glossary).

**5. Modules**
- [ ] **§18 Data:** every number is a figure with provenance; `veos figures` recomputes; counters land ±5 f on the spoken number; compared bars share a `scale_id`; formats match `profile.numbers` (V-DATA, V-NUMFMT).
- [ ] **§19 Citations (F-A):** FIG line + SRC on every card; quotes verbatim with attribution.
- [ ] **§25 Brand:** the keyword on screen ≥ 1.5 s each time; the promo / title window shows the exact deliverable title; the comment sheet shows no fake users or likes; a sponsor chip ≥ 2 s when sponsored (V-PROMISE).

**6. Truth and inserts**
- [ ] Every third-party moment is creator-supplied or a created substitute, recorded in `plan/inserts.json` (V-INSERTS).
- [ ] No stock, film, meme or AI-people footage; no fetched logos (N7).
- [ ] Illustrative graphics carry no unsourced numbers (or the "example" tag).

**7. Visual system**
- [ ] ≤ 4 elements z3–10 and ≤ 3 text blocks at once (cards are single elements) (G2).
- [ ] ≤ 3 bright hues per frame; old = `bad`, new = `accent` (V-HUES).
- [ ] Brutal text in primary is the deepened `#DB5320` at ≥ 96 px; pinksage white numerals carry the ink stroke (V-TYPE).
- [ ] Every cut to the presenter carries the Z-1 (L-full) / Z-2 (L-stack) settle-out; no other camera move; never the same preset twice in a row (V-CAMERA).
- [ ] Transitions are the active theme's own (§9.1): editorial T-01/T-04 only.
- [ ] The header never runs under the PiP bubble (N1).

**8. Sound contract**
- [ ] Cues only on hook, transitions (≤ 1 per 2 s), reveals, the list cue and the CTA; one tick-run cue per ticker (S1–S6).
- [ ] Bed from f0, ≥ 18 dB under the voice; −14 LUFS; true peak ≤ −1.5 dBTP.

**9. End and export**
- [ ] The end CTA keyword ≥ 1.5 s; the comment sheet ≤ 1.5 s; hard end ≤ 6 f after the last word; no black tail.
- [ ] 1080 × 1920, 30 fps CFR.

---

## Conditional modules (§16–§25)

### §16 Frame template / chrome
OFF (`profile.modules.chrome = false`): the FIG line belongs to each card (P-01), not to a persistent slot.

### §17 Running state & anchored graphics
OFF (`profile.modules.running_state = false`, `anchors = false`): every counter in the evidence lives inside one figure and nothing persists across a cut, so counters are §18 figures.

### §18 Data contract `[COND: modules.data_figures] [DNA rules]`
Every counter, ticker, bar, grid fill, timeline and hero number is a figure in `plan/figures.json`.

| Field | This style's rule |
|---|---|
| `kind` | `counter` (P-02, P-03, P-25, P-35), `hero_number` (P-06), `bar` (P-05, P-15, P-16), `grid_fill` (P-12), `slider` / `line` (P-08), `ledger` is unused; ticker rows (P-27) are `counter` figures with steps |
| `inputs` | `script` + the exact words (`said`), `creator` (asked for at the checkpoint: their own prices, minutes, client counts), `source:<id>` (the F-A SRC), or `spoken@t` |
| `formula` | From `data.formulas`: `sum`, `diff`, `ratio`, `percent_change`, `per_period`, `unit_convert`, `compound`, `cagr`; `none` for a stated value |
| `steps` | Each step aligned to its spoken word (`at`); counters land on it ±5 f |
| `scale_id` | Bars compared in one card share one scale id (P-05, P-15); the P-12 grid uses the total as its scale |
| `format` | From `profile.numbers` (international $ k_m_b by default; Indian ₹ lakh_crore with BV-06) |
| `illustrative` | `true` for P-04, P-16's "off the chart" phase, P-19: a concept label, no axis numbers, the "example" tag if any number appears |

Display bindings: use `VEOS.data.counter` / `bars` / `slider` where the shape fits; for bespoke cards (hourglass, rings, grid, ticker) bind with `figure` / `figures`, write values with `ctx.fmtNum`, roll with `ctx.figAt`, and declare `lands`. Tickers (E6) step through `ctx.figAt(id, t)` values on a 4 f grid inside a `data-slot` box. **Validator V-DATA** recomputes every formula, checks provenance, axis maxima, landing times and spoken numbers; **V-NUMFMT** checks the formatting.

### §19 Evidence & citations `[COND: modules.citations] [DNA]`
- **Credit line (F-A, optional):** the right half of the FIG line: "SRC: OUTLET · MON YYYY", JetBrains Mono 500 **26 px** caps, `mute`, right-aligned at x 1016, y 232; present from the card's first frame (no fade). When the script cites no outside source, the SRC names the creator: "SRC: {{BV-01.handle|@yourhandle}} · MON YYYY" (their own figure). Optional: nothing requires a credit line.
- **Figure numbering:** "FIG. nn" left of the line, `primary`, two digits, monotonic from 01 (`citations.figure_numbering: true`; V-CITE checks the order).
- **Source cards:** P-09 quote notes (the creator's screenshot of the post when supplied, framed by `fx.shot`; else `fx.quoteCard` with the exact words). Headlines of articles are quoted exactly (`fx.headlineCard` in the editorial theme: cream card, ink serif headline, `primary` marker highlight on the spoken phrase).
- **Plates:** names and roles on portraits (P-07) in mono.
- **Verdict stamps:** only "✓ PASS" / "✓ FIXED" (`good` / `accent`) and "✕ ERROR" (`bad`) pills.
- **F-B:** credit lines off (`required_on: none`); quotes still carry name + attribution.
- **Validator V-CITE / V-INSERTS:** masthead + date present on sourced beats, highlight spans inside the headline, synthetic assets, FIG numbers increasing.

### §20 Dialogue
OFF (`profile.modules.dialogue = false`): one presenter.

### §21 Canvas camera
OFF (`profile.modules.canvas_camera = false`): ideas change by hard cut, not by camera travel (D5).

### §22 Ink & annotation layer
OFF (`profile.modules.ink = false`): the few hand strokes (the P-09 underline, the P-14 oval) are drawn inside their cards.

### §23 Continuity
OFF (`profile.modules.continuity = false`): the only hand-off is T-04 evolve inside one idea.

### §24 Series furniture
OFF (`profile.modules.series = false`, VAR): a buyer may turn it on; the tag then reads "FIG. {n}"-style in mono at y 150 (F-B) and counts toward the intro cap.

### §25 Sponsor, brand & end cards `[COND: modules.brand] [DNA look; VAR assets]`
- **Sponsor (P-52):** "Paid partnership" chip (TC-legal mono 24, `mute` text on a 2 px outline) at x 64, y 150 in both formats (the F-A FIG line stays at y 232 below it), held ≥ 2 s from the sponsor's first mention, plus the spoken disclosure (NC-12). The sponsor's name is set in type (or their supplied logo) on a P-46 plate; never over the face or a figure.
- **Promo carousel (P-49):** the deliverable card of the mid CTA, ≤ 2.5 s, on W-promo; thumbnails only from SH-5.
- **Title window (P-41):** the exact deliverable title, ≤ 2.5 s.
- **End card = the comment sheet (P-50):** ≤ 1.5 s, the keyword typed in the input, nothing else; `brand.endcard.max_s` 3.5 s for keyword card + sheet together.
- **Rules:** brand colours only on brand elements; the keyword readable ≥ 1.5 s; black tail ≤ 0.2 s.

---

## Part C. Declared exceptions and the non-overridable core

**Declared (§2.2):** E3 quiet type (captions 42–53 px on a solid pill; mono micro labels 30–39 px when redundant) and E6 hard swap (counter digits and ticker values inside fixed boxes). Tokens: `exceptions.E3 {subtitle_min_px 42, label_min_px 30, contrast_min 7.0, pill_contrast_min 4.5, weight_min 600}`, `exceptions.E6 {slot_tolerance_px 4}`. Captions inherit E3 from CS-1; scenes using them set `exception: "E3"` or `"E6"`. A buyer may switch either off (stricter): captions then go to 54 px (CS-1 size TUNE stops at 52, so switching E3 off is recorded as a deviation), tickers then roll eased.

**The non-overridable core** (NC-1…NC-14) applies in full. Where this style meets it:
- NC-1: no card over the face in L-cardtop (card bottom ≥ 40 px above the face top); captions avoid the face on L-full.
- NC-2: chips, labels and the FIG line live inside their card (one element); the header never runs under the bubble.
- NC-5: the decor band (y 1580–1860) is non-text world; the caption at 1390–1450 stays above 1500.
- NC-6: figures with provenance; the comment sheet has no fake users; app mocks are generic and labelled.
- NC-7: no fetched media; logos only from the creator.
- NC-10: ≤ 3 bright hues per frame (style value).
- NC-13: P-09 quotes are verbatim and attributed.

---

## Part D. Personalisation

### D.1 Branding questions (one round, each with "keep the template default")
| ID | Question | Lands on | Default |
|---|---|---|---|
| BV-01 | Your name and handle | `creator.name`, `creator.handle`; the SRC fallback ("SRC: {{BV-01.handle|@yourhandle}}"); the P-41/P-49 cards | — |
| BV-02 | One or two brand colours | `roles.primary`, `roles.accent` in **all three** packs (policy per_reel); contrast-nudged to ≥ 4.5:1 against ink | coral / blue (editorial), orange / lime (brutal), pink / sage (pinksage) |
| BV-05 | Language you speak, and the caption language | `profile.language`, always asked: **English** → English captions (default) · **Hinglish** → romanised Hinglish captions · **Hindi** → Devanagari captions; numbers follow (BV-06) | English ({{BV-05.speech|en}} → {{BV-05.captions|en}}) |
| BV-08 | Your call to action and its value | `profile.cta.chosen` + keyword / deliverable | comment keyword "{{BV-08.keyword|KEYWORD}}" |

Defaulted and changeable later: fonts inside each slot's class (BV-03), the default theme and which packs to use (BV-10), formats enabled (BV-09), number format (BV-06 follows BV-05), sponsor wording (BV-14), never-on-screen list (BV-15), logo files (BV-16), duration target (BV-17).

### D.2 What a buyer can change
| Level | In this template |
|---|---|
| **DNA** | Graphic-first (primary graphics, guest presenter), one theme per reel, hard cuts between ideas, the pill caption mechanics (1–4 words, word reveal, no emphasis), the FIG / numeral marker systems, HA-07 as default, the figure data contract, the layout set, crop-on-cut camera |
| **TUNE** | Caption size 42–52 px and y 1360–1460; pill colour (a red-orange or the world's ink); presenter share ±10 points and max absence 6–14 s; cadence ±15%; motion ±15%; type sizes (ranges in `locks`); font families inside their class; PiP diameter 360–460; stack seam 900–1020; theme world colours keeping polarity |
| **VAR** | Primary / accent colours, the default theme, formats enabled, language, numbers, CTA device and keyword, sponsor wording, series on/off, sound cue moments, the creator block |
| **NICHE** | §6.4 hook pairs, §8.4 lookup rows, §14 examples, App. A headlines |

### D.3 NICHE slots per reel
- **§6.4:** at P7, write this reel's claim → number → figure pair and append it.
- **§8.4:** at P5, map any new line type to an existing pattern (≤ 10 new niche patterns over time, from the existing families) and append it.
- **§14:** after the first approved reel of each format, it replaces that format's worked example.
- **App. A:** approved headlines are added to the bank.
- **Glossary:** brand, product and people's names confirmed in captions are added.

---

## Part E. What this template changes vs the evidence and the coverage table

| Item | Evidence / coverage | Template decision | Why |
|---|---|---|---|
| Presenter absence | 18–24 s runs (v01 0:27–0:45, v02 0:16–0:41) | ≤ 10 s F-A, ≤ 8 s F-B | Buyers are less known than the source brand; the guest must return |
| Header under the bubble | v02 0:00–0:08 clips "LEARN AI B|" | Forbidden; the header stops 40 px before the ring | Structure Part C: not allowed |
| FIG numbers | v01 04 → 05 → 06 → 08 … → 01 → 02 | Strictly monotonic from 01 | V-CITE; a visible order the viewer can trust |
| Comment-sheet ending | v02/v03 show comments from brand accounts with likes | The sheet shows only the keyword being typed | NC-6: no fake comments |
| Film clip / illustrated clerk | v03 0:27–0:31 | Not used; P-31 icon slab or P-36 instead | NC-7 |
| `running_state` | Coverage: ON (counters) | OFF; counters are §18 figures | No value persists across a cut in any reel |
| Cadence | Coverage: 4–5 SC / 10 s | [7, 16] including in-card events and caption weight | Counted the validator's way from the 1 fps sheets |
| F-B default hook | Coverage: HA-02 for ads | HA-07 (ticker) by default; HA-02 when the first line has no number | v03 (an ad) opens on a live number; the brief makes HA-07 the style's hook |
| Captions on the seam (v03 hook) | 2-line white text without a pill | The same CS-1 pill everywhere | One caption system; the v01 seam captions use a dark box |
| Card margins | v03 ticker card x 18–1062 | x 64–1016 | G2 breathing room |
| Orange text on cream | v02 "BUILDING." 2.7:1 | Deepened to `#DB5320` (3.6:1 at ≥ 96 px) | NC-4 |

---

## Part F. IDs used in this playbook
| Prefix | IDs |
|---|---|
| D / BD | D1–D8 / BD1… |
| H / N / BN | H1–H18 / N1–N13 / BN1… |
| E / NC | E3, E6 / NC-1…NC-14 |
| W / L / G | W-main, W-alt, W-dark, W-promo / L-graphic, L-stack, L-full, L-pip, L-cardtop / G-1…G-5 |
| TH | TH-editorial, TH-brutal, TH-pinksage |
| CS | CS-1 |
| HA / ST | HA-07 (default), HA-18, HA-02 / ST-1, ST-2, ST-3, ST-4, ST-5, ST-6 |
| SM | SM-FIG (F-A), SM-NUMERAL (F-B) |
| P / B | P-01…P-52 / B-1…B-8 |
| T / R | T-01…T-10 / R-1…R-5 |
| Z | Z-1 (`pull-out` settle 1.26 + roll 4° → 0), Z-2 (`pull-out-wide` settle 1.40) |
| SH / FB | SH-1…SH-5 / FB-2…FB-5 |
| F | F-A, F-B |
| V | V-F0, V-CADENCE, V-TITLE, V-ONWORD, V-SAFE, V-FACE, V-PRESENCE, V-CAPTION, V-LAYOUT, V-TYPE, V-EXC, V-HUES, V-NUMFMT, V-DATA, V-CITE, V-INSERTS, V-THEME, V-PROMISE, V-CAMERA, V-COMEDY |

---

## App. A Headline & hook bank `[NICHE]`
Slots in `{braces}` are filled per reel from the script. Numbers must be figures.

**F-A title slabs (plate, ≤ 5 words, 2 lines, ≤ 16 characters per line)**
| # | Headline | Archetype | Opening figure |
|---|---|---|---|
| 1 | "{SUBJECT} SOLVED / {HARD THING}" | HA-07 | P-02 hourglass of the time it took |
| 2 | "{SUBJECT} BEAT / {N} IN {M}" | HA-07 | P-12 grid of the share |
| 3 | "{RECORD} FELL / AFTER {N} YEARS" | HA-07 | P-08 timeline dot |
| 4 | "{COST} FOR / {RESULT}" | HA-07 | P-27 ticker or P-17 price tag |
| 5 | "{THING} GOT / {N}× CHEAPER" | HA-07 | P-15 compare bars |
| 6 | "{PERSON} SAID / {IT} WAS IMPOSSIBLE" | HA-18 | P-47 source clip (creator-supplied) |
| 7 | "{N} DAYS / NONSTOP" | HA-07 | P-02 hourglass |
| 8 | "THE {N}% / NOBODY SEES" | HA-07 | P-12 grid fill |
| 9 | "{OLD WAY} VS / {NEW WAY}" | HA-02 | P-15 bars as proof |
| 10 | "WHY {THING} / COSTS {X}" | HA-07 | P-16 off the chart |

**F-B section headers (lockup: `// slug` + 2 lines, ≤ 12 characters per line)**
| # | Slug + header | Archetype | Opening figure / proof |
|---|---|---|---|
| 1 | `// the_cost` "YOUR BILL / EXPLODED." | HA-07 | P-27 ticker |
| 2 | `// who_we_are` "LEARN BY / BUILDING." | HA-02 | P-20 window card |
| 3 | `// what_you_get` "{N} REAL / {OUTCOMES}." | HA-02 | P-23 tiles |
| 4 | `// time_spent` "IT TOOK / {N} MINUTES." | HA-07 | P-25 stopwatch |
| 5 | `// use_cases` "{N} WAYS TO / USE {TOOL}." | HA-07 | P-35 count |
| 6 | `// for_you` "IF YOU'RE A / {AUDIENCE}." | HA-02 | P-31 icon slab |
| 7 | `// the_problem` "{PAIN} IS / COSTING YOU." | HA-07 | P-27 ticker |
| 8 | `// the_method` "ONE {THING}. / ZERO {OTHER}." | HA-02 | P-20 window card |
| 9 | `// your_coaches` "LEARN FROM / {EXPERTS}." | HA-02 | P-24 profile fan |
| 10 | `// free_class` "{TITLE} / THIS WEEKEND." | HA-02 | P-41 title window |

---

## App. B Evidence map `[DNA; templates only]`
The full source map (each DNA rule → `vNN @ m:ss`), the measured values and the `(unverified)` list are in `evidence.md` beside this playbook. Sources: `analysis/short/100xengineers.md`; frames `evidence/short/100xengineers/v01–v03/sheets`; transcripts `v01–v03/transcript.txt`.
