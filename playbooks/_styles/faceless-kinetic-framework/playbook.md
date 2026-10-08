# Faceless Kinetic Framework Style Playbook (template v1)

**Purpose:** you (Claude) receive a **voice-over** (an audio file, or a script the creator records) from {{BV-01.name|the creator}} and nothing else: no face, no camera. Use this playbook to build **every frame from engine graphics**: kinetic type that stacks in alternating bold sans and italic serif, a framework diagram the canvas camera travels through, rounded 9:16 proof cards, section flips between paper, umber and ink worlds, and a lead-magnet card at the end. One idea per reel, 18-30 s.

**Input (SW-01 `voiceover_only`):** one VO file (`veos ingest --audio`), the script, and optionally the creator's own example clips or screenshots for the proof cards (asked once, §12.5). Nothing is ever fetched.

### Style DNA `[DNA]`
A Faceless Kinetic Framework reel is **a teacher's whiteboard that animates itself**. A warm-grey graph-paper canvas (`#E2E1DC` with a barely visible 64 px line grid; the hub hooks use a cool `#EBEBEB` ground with faint dots) carries short lines of type that fly up from low in the frame with a strong vertical motion blur, one spoken phrase per line, alternating a bold geometric sans with a light italic serif, until a stack of up to five lines reads like a sentence set by a magazine designer. The idea always has a **shape** (a hexagon hub with redacted bars, a ladder of giant initials, an equation, a stack beside a proof card), and a **camera that visits it** node by node. Proof lives in small rounded 9:16 cards with a view chip. Sections cut hard from paper to dark umber to charcoal ink and back. The palette is monochrome; colour is a whisper. It ends on a dark "database" card and a keyword to comment.

**Copy these 5 things and it reads as this style:**
1. **The alternating stack:** Montserrat ExtraBold / Instrument Serif italic lines, 1-3 words each, each new line added BELOW the last and flying up ≈ 450 px from the frame bottom (exponential out, settled by f20, motion blur on the first 3 f; earlier lines never move), up to 5 lines (§5.3 CS-1, P-01).
2. **A framework with a shape, visited by a camera:** hub, initial ladder or equation; a snap C-1 push 1.0 → 2.3× in 14 f (expo in-out, `p.snap`), node labels typed at 45 cps, the hub spinning to bring the next node up (§8 P-11…P-24, §21).
3. **Warm graph paper + two dark worlds:** `#E2E1DC` with a faint 64 px line grid (or cool `#EBEBEB` with faint dots for hub hooks), hard flips to umber `#3A2E2C` and ink `#141414` on section starts (§3.1, §4.3).
4. **Proof in rounded 9:16 cards:** 432-760 px wide, radius 28, soft drop shadow, eye + view-count chip, the creator's clip or a created card (§8 P-25…P-33).
5. **The lead-magnet close:** `Comment "{{BV-08.keyword|KEYWORD}}"` line + a dark resource card + a count line, held ≥ 3 s (§6.7, §25).

### Fidelity audit corrections (2026-10-06, full-resolution check of v01-v03)
These override any older figure further down. Evidence: `docs/audit/faceless-kinetic-framework/audit.md`.
- **Sans is Montserrat ExtraBold (800)**, tracking −0.035 em, not Poppins 600 (letterforms: slanted `t` top, straight `y`); stack sans 80 px, serif (Instrument Serif italic) 112 px, header line 76 px.
- **Stack motion:** each line is added *below* the previous one and flies up 180-300 px with a heavy vertical motion blur (14 px) over 8 f; earlier lines never move. Line pitch ≈ 140 px.
- **Header line (CS-3) is a hard swap**, 1-2 words per chunk, cy 312 (or ~70 px above a lower card), Montserrat 800.
- **Worlds:** W-paper is warm `#E2E1DC` with a barely visible 64 px *line* grid (not dots); hub / thumb-rain hooks sit on cool W-mist `#EBEBEB` with faint dots. Text ink `#392E2C` (the umber brown).
- **Hub centre** carries the framework's name in two tiers (small 500 / bold 800 Inter Tight), not a count numeral. **Title-mix tail** is a light sans italic, not a serif.
- **Frame 0** shows the shape / card alone; the first word lands by 0.3-0.4 s.

### Motion audit corrections (2026-10-07, every frame of v01-v03)
These override any older motion figure further down. Evidence: `docs/audit/faceless-kinetic-framework/completeness.md` (strips cited there).
- **Stack fly-in (G-1):** each new line appears near the frame bottom (y ≈ 1600-1860) and decelerates 420-500 px up into its slot: ½ of the travel by f5, 90 % by f12, settled by f20 (30 fps; exponential out). Motion blur only while fast (first 3 f). The first hook line builds **word by word in place with hard pops**; the P-07 arrow pops with its first word (no draw-on). (v01 @ 0:00.08-0:01.92)
- **Cuts carry the edit.** World flips, proof changes, letter changes and the CTA are **hard cuts with the new content already on the cut frame**; nothing fades. A card that arrives after a cut does so 4 f later (G-3 slide from the right, or G-8 rise from below).
- **C-1 push is a snap:** ≈ 15 f, 1.0 → 2.3×, almost all of the scale in the middle 2-3 f (zoom blur there); the title blurs out in place over the 6 f before. Node labels type at **45 cps** (1.5 chars/frame). (v02 @ 0:02.10-0:02.87)
- **Node → node is a hub spin, not a dolly:** the cut back from a proof lands mid-spin; the hub rotates −360/N about its centre (10 f, ease-out) with the camera held, so the next node arrives at the top; visited labels stay full ink. (v02 @ 0:06.37-0:06.50, 0:11.00-0:11.30)
- **Proof flurry:** a profile bar + proof card set is replaced by hard cuts every 0.25-0.5 s, each card tilted a random −5…+5° (v01 @ 0:06.21-0:08.13, 6 sets in 2 s).
- **Equation lines slide in from the right** with a horizontal motion blur (8 f, expo-out) and stack downward (v01 @ 0:19.06-0:21.35). **Ink punch** words pop hard in a staircase, the last word ≈ 2× (v01 @ 0:13.14-0:13.89).
- **Thumb field spins:** the HA-12 field is one plane that turns ≈ 40° and pulls back 1.2 → 1.0 with strong deceleration over 3.5 s (v03 @ 0:00-0:03.6), not tiles drifting upward.
- **Letters:** the line-up's letters slide in one every 4 f (Anton ≈ 290 px), the gap closes and the group pushes in ~1.1× while blurring into a hard cut (T-11); giant letters change by pure hard cuts (only the first de-blurs over 3 f). (v03 @ 0:04.28-0:06.48, 0:12.52-0:13.60)
- **CTA is still:** lines, card and count line are all present on the cut frame and do not move (v01 2.05 s dead still); no keyword underline. (v01 @ 0:21.69-0:23.8, v03 @ 0:13.60)

### Directives (the style's laws)
| # | Directive | Where it lives |
|---|---|---|
| D1 | **No face, ever.** Stage `hidden` for the whole reel; every pixel is a scene built from the VO | §0, §1, §3 |
| D2 | **Type is the picture.** Every spoken phrase is on screen as kinetic type (captions `full`, role `primary`); nothing is said that is not read | §5.3, §2 H3 |
| D3 | **One idea, one framework, one shape.** Each reel teaches exactly one framework and draws it with one marker shape (SM-1 hub, SM-2 initial ladder, SM-3 proof stack) | §7, §8 |
| D4 | **The camera visits the idea.** A diagram is never static for more than 2.0 s: push, hub spin, pull or drift on the canvas | §10, §21 |
| D5 | **Proof sits in rounded 9:16 cards** with a view chip: the creator's own clip if supplied, otherwise a card Claude builds. Never fetched | §8.2, §12.5 |
| D6 | **Quiet monochrome.** Ink on paper, white on umber and ink; one signal accent on one element at a time; at most 2 bright hues per frame | §4 |
| D7 | **Sections flip worlds** as rhythm: paper → umber → ink → paper, hard cuts on section starts, ≤ 3 flips, ≥ 3.0 s apart | §4.3, §9 |
| D8 | **Short and closed.** 18-30 s; the last 3-4 s are the lead-magnet card with the keyword readable ≥ 1.5 s | §6.7, §7, §25 |

Buyer directives BD1… `[VAR]` may only make the style stricter or more specific (e.g. "never use the umber world").

### Quick index
| § | What | Status |
|---|---|---|
| §0 | Style profile (switches) | ON |
| §1 | Procedure (VO branch; framework extraction is the craft step) | ON |
| §2 | Hard rules, exceptions (E4) | ON |
| §3 | Worlds, layout zones, scene moves, safe zones | ON (§3.6 presenter OFF) |
| §4 | Colour, theme packs (TH-paper / TH-umber / TH-ink) | ON |
| §5 | Type and captions (CS-1 stack low, CS-2 stack centre, CS-3 header line) | ON |
| §6 | Hook system (HA-06 default; HA-12, HA-02) and CTA | ON |
| §7 | Structure (framework) and cadence | ON |
| §8 | Visual system: 41 patterns P-01…P-41 | ON |
| §9 | Transitions T-01…T-10 | ON (§9.3 OFF) |
| §10 | Motion, camera, layers, finishing | ON |
| §11 | Sound contract | ON (minimal) |
| §12 | Inputs, inserts (ask, then create) | ON (§12.2-12.3 OFF) |
| §13 | Output contract | ON |
| §14 | Worked examples (3) | ON |
| §15 | QA checklist | ON |
| §16 | Frame template / chrome | OFF |
| §17 | Running state & anchors | OFF |
| §18 | Data contract | OFF |
| §19 | Evidence & citations (credit lines) | ON |
| §20 | Dialogue | OFF |
| §21 | Canvas camera C-1…C-5 | ON |
| §22 | Ink & annotation | OFF |
| §23 | Continuity (hub motif, morph hand-offs) | ON |
| §24 | Series furniture | OFF |
| §25 | Lead-magnet end card, sponsor chip | ON |
| Parts C-F | Exceptions, personalisation, changes, IDs | ON |
| App. A / B | Headline bank / evidence map | ON |

Formats: **F-A Kinetic framework** (the only format). Theme packs: TH-paper (default), TH-umber, TH-ink, switched **per section**.

---

## §0 Style profile `[REQ]`

```yaml
profile:                         # mirrored exactly in tokens.json → profile
  source_type: voiceover_only
  presenter: {presence: none, share: [0, 0], max_absence_s: null}
  spine: audio
  captions: {mode: full, role: primary, mute_policy: mute_safe}
  graphics: primary
  duration: {class: micro, target_s: [18, 30]}
  language: {speech: en, captions: {lang: en, script: Latn, transform: verbatim}, on_screen: en, post_title: en,
             supported: [[en, en, Latn], [hinglish, hinglish, Latn], [hi, hi, Deva]]}
  numbers: {grouping: international, currency: "$", compact: k_m_b, units: metric, decimals: 0, style: short, compact_decimals: 1}
  tone: {energy: calm, comedy: off, comedy_max: off}
  themes: {policy: per_section, packs: [TH-paper, TH-umber, TH-ink], default: TH-paper}
  formats: {list: [F-A], default: F-A}
  footage_dependency: none
  cta: {devices: [comment_keyword, link_bio, end_card], placement: end, chosen: comment_keyword}
  modules: {chrome: false, running_state: false, anchors: false, data_figures: false, citations: true,
            dialogue: false, canvas_camera: true, ink: false, continuity: true, series: false, brand: true}
```

Why each switch has this value:
- **source_type `voiceover_only`, presence `none`:** no face appears in any of the 3 reference reels (v01 0:00-0:24, v02, v03); the input is a voice and the picture is built. PV-1 holds: spine is `audio`, V-PRESENCE and V-FACE are off, E1 is unavailable.
- **spine `audio`:** the text appears at speech rate (v01 ≈ 2.3 words/s, one line per phrase); the VO's timeline decides every scene, one scene per sentence (§1 P8).
- **captions `full / primary / mute_safe`:** 95 %+ of v01 and v03 runtime has the spoken words on screen as the main visual (analysis §6 numbers card). Mode is DNA: keywords-only would remove trait 1.
- **graphics `primary`:** 100 % of the picture is graphics or proof cards (no presenter). This allows §21 (PV-5).
- **duration `micro` [18, 30]:** v01 23.9 s, v03 18.0 s; v02 33.3 s is the one long case (six nodes). A buyer may TUNE to `short` (adjacent class) for 6-8-node hubs.
- **language `en` default:** all three reels are English on screen (speech unverified: no transcripts). Hinglish and Hindi are supported for buyers (§5.5 says how the serif alternation survives in Devanagari).
- **numbers international / k_m_b / short:** the evidence's view chips read "6.7M", "2.1M", "155M"; counts read "1,500+". BV-06 switches to Indian grouping automatically for `hinglish` / `hi`.
- **tone `calm`, comedy `off`, comedy_max `off`:** no gag, sticker or meme in any reel; energy comes from motion density, not from jokes.
- **themes `per_section`:** the world flips light → brown → light → black → light in v01 (0:02.5, 0:05.8, 0:13, 0:14) and light → charcoal → light in v03 (0:03.7, 0:12.6).
- **one format:** the three reels are one style with three framework shapes (hub, acronym, proof stack); they share all 5 traits, so they are marker shapes SM-1…SM-3 inside F-A, not formats.
- **footage_dependency `none`:** the engine makes every picture from the VO; the creator's clips improve proof cards but are never required (§12.5).
- **cta:** v01 @ 0:22 and v03 @ 0:14 end on `Comment "Database"` + a database card; `end_card` is that card; `link_bio` is the buyer's alternative device.
- **modules:** canvas camera (v02 hub visits), continuity (the hub returns at every item, a card morphs into the hub), citations, brand (the lead-magnet end card).

### 0.4 Formats `[DNA set; VAR enable]`
| Field | F-A "Kinetic framework" |
|---|---|
| `when` | Any single idea that has a shape: "N ways to…", a named framework or acronym, a formula ("A = B = C"), "this is the X style/format", a do-this-not-that rule. 18-30 s, voice-over only |
| `profile` overrides | none |
| `layouts` | `L-canvas` (engine `hidden`) |
| `hooks.default` | HA-06 Framework build (alternates HA-12, HA-02) |
| `structure` | `framework` with one marker shape per reel: **SM-1 hub tour** (default), **SM-2 initial ladder**, **SM-3 proof stack** |
| `shared_dna` | no presenter; alternating sans/serif kinetic stack on warm graph paper; rounded 9:16 proof cards; a canvas camera that visits the framework; paper / umber / ink section flips; lead-magnet card CTA |

### 0.5 Theme packs `[DNA policy; VAR colours]`
| Pack | Ground | Type colour | Carries (`per_section` rule) |
|---|---|---|---|
| **TH-paper** (default) | W-paper `#E2E1DC` + 64 px line grid `#D8D7D1` (1.5 px); W-mist `#EBEBEB` + faint 64 px line grid `#DEDEDE` for SM-1 / SM-2 hooks | ink `#392E2C` | the hook, the framework (hub, stations, proof stack), the recap, the CTA |
| **TH-umber** | W-umber `#3A2E2C`, flat | paper `#FFFFFF` | the CONTEXT section right after the hook: "this is one of the easiest…", a reference card on brown |
| **TH-ink** | W-ink `#141414` + faint 64 px line grid `#1F1F1F` | paper; giant initials ghost `#6F6F6F` | the framework reveal: the initial ladder (SM-2), a dark proof card, the one-beat ink punch is NOT a theme flip (P-08) |

Rules: flips are hard cuts at section starts; at most 3 per reel and ≥ 3.0 s apart (V-THEME `min_gap_s: 3.0`, measured from v01's 2.5 → 5.8 s flips); a reel opens and closes on TH-paper.

---

## §1 Procedure (follow in order) `[REQ] [DNA]`

The craft step of this style is **P6b framework extraction**: turning a spoken idea into a shape with N labelled parts before any scene is written.

1. **P1 Inventory.**
   - `veos project init --project P --voiceover vo.wav --script script.md --playbook <this playbook>` then `veos ingest --audio vo.wav --script script.md --project P`.
   - Check: one voice, 44.1/48 kHz, no music baked in (if music is baked in, ask for the dry VO once; otherwise keep it and set the bed `off`).
   - Register every file the creator hands over with `veos asset add <file> --origin creator --project P`. No other media enters the project.
2. **P2 Prepare:** skipped (no presenter, no matte).
3. **P3 Transcribe** with word timestamps (`veos transcribe`); the words are aligned to the script. Apply `language.captions.transform` (captions language: {{BV-05.captions|en}}, script {{BV-05.script|Latn}}). Add every brand and tool name to the glossary.
4. **P4 Segment** into sections: `HOOK` (≤ 15 % of runtime, normally 2.3-3.7 s) → `CONTEXT` (optional, 2.5-4 s, TH-umber) → `ITEM-1…ITEM-N` (the framework parts) → `RECAP` (optional, 1-2.5 s) → `CTA` (3-4 s).
5. **P5 Classify** every sentence with a line type (§8.4) and mark its trigger word (the noun or number the visual lands on).
6. **P6 Tone-tag** every sentence: `explain` · `awe` · `warn` · `win` · `cta`. No `mock` (comedy off).
7. **P6b Framework extraction (the craft step).** Write, before anything else:
   - `framework`: its name in ≤ 4 words ("6 ways to hook viewers", "the HRST formula").
   - `shape`: SM-1 hub (3-8 parallel parts), SM-2 initial ladder (an acronym of 3-6 letters, or a word whose letters are the parts), SM-3 proof stack ("this is the X" + proof card + equation). Rule: an acronym in the script ⇒ SM-2; 3-8 parallel items ⇒ SM-1; one thing shown with proof ⇒ SM-3.
   - `parts`: each part's label, ≤ 18 characters, ≤ 4 words, written as the VO says it.
   - `proof`: per part, what proves it (a creator clip, a created card, or nothing: then the label + a CS-2 stack carries it).
8. **P7 Hook plan:** pick the archetype (§6: HA-06 for SM-1, HA-12 for SM-2, HA-02 for SM-3), write **3 hook variants** with their titles, run the stopper tests (§6.1).
9. **P7b Inserts:** `veos inserts scan --project P`; refine the moment list; **ask the creator once** (§12.5); record `plan/inserts.json`.
10. **P8 Visual plan, one scene per sentence, no gaps:**
    - the world per section (TH-paper / umber / ink, §0.5) and the `theme_flips`;
    - the pattern per line (§8.4);
    - the canvas plan: `canvas_nodes`, the camera moves per item (§21);
    - the caption profile per span (CS-1 / CS-2 / CS-3 / hidden under a built text scene, §5.3).
11. **P9 Beat sheet** (§13): one beat per trigger, cadence targets met (§7.6).
12. **P10 SFX cues** (§11, from the bundled pack) and the transition map (§9).
13. **P11 Assets:** build the created cards; frame the creator's files; say which substitutes were used.
14. **P12 Checkpoint** (§13.5), then **wait for approval.**
15. **P13 Build:** write `plan/timeline.json` + `plan/scenes.js` → `veos captions build` → `veos scenes-meta` → `veos measure --every 10` → `veos validate` → fix → `veos render --test` + `veos sheet` → QA (§15, max 3 passes) → render.

---

## §2 Hard rules `[REQ] [DNA]`

### 2.1 Editing rules (every style)
The ten editing rules in `playbooks/_global/GLOBAL-RULES.md` apply. They are directions, not limits: smooth, seamless motion; nothing overlaps by accident; keep the face clear (behind the speaker is fair game, text included); readable at a glance; one idea at a time; show the thing, not the word; say what was said; hook titles hook; pace like the style, not like a timer; the style decides the look.
- **Facts the engine checks:** accidental overlaps, jumps, the face covered, unreadable text, numbers and quotes that don't match what was said, the promised count. Every count, timing and budget this playbook gives is direction for the edit, not a limit.
- **Picture first, in this style's own look:** every key beat shows the thing being said (an object, a screen or app, a diagram, numbers in motion), not just its word; text supports the picture and never replaces it. When the speaker points with words ("this, this and this", "from this to this", "ye dekho"), show what they mean. Illustrations may use made-up but realistic numbers and names ("212 views", "1.2M views"), with no label; a number or quote the speaker says is shown as said. This overrides any rule below that bans made-up numbers or asks for an example tag: those rules now cover claims (the creator's results, prices, benchmarks, testimonials), not illustrations.
- **Hook titles hook:** the on-screen title promises the viewer something (an outcome, a curiosity gap, who it's for) and is true to what the reel delivers; it need not repeat the spoken words. This playbook sets its shape (§5.2, §6.5: lines, sizes, word limits, case), never its voice (§6).
- **Retired (8 Oct 2026), whatever this playbook says below:** no REPRESENTATIONAL or example labels on made-up cards, no credit lines, no flash limit (flash as often as this style calls for; any "NC-11" cap below no longer applies), and text may sit behind the speaker without an exception.

### 2.2 Declared exceptions
| E-id | Limits in this style (≤ the registry) | DNA reason | Evidence |
|---|---|---|---|
| **E4 Ambient field** | P-33 thumb rain only: ≤ 30 tiles (default 24), each ≤ 12 % of frame (tiles 150-230 px wide, 9:16), no text, speeds 24 / 40 / 56 px/s (≤ 60), ≤ 5.0 s, once per reel, z2 with `ambient: true`, tiles within 40 px of the active text rect drop to opacity ≤ 0.55 and blur 6 px (`dim_under_text: 0.4`) | The "sea of examples" opening of HA-12: the thesis is read over a field of drifting reels | v03 @ 0:00-0:03.7 (≈ 25 cards, 3 depths) |

Not declared (and why): **E5 edge bleed** would let the giant initials touch the frame edge as in v03 @ 0:05 (the H starts at x 0), but PV-9 ties E5 to presenter footage, so this faceless template keeps every glyph inside the 64 px margin (Engine request R-3). **E3 quiet type** is not needed: the smallest meaning text is 40 px (view chips, node labels), the credit line is TC-legal 24 px.

### 2.3 Style MUST rules
- **H1 Frame 0 builds.** f0 shows the warm paper world with the hook's skeleton already moving: for HA-06 the hub dot growing + the title's first word rising; for HA-12 the thumb rain drifting + the first word rising; for HA-02 the hero proof card on screen + the first stack line rising. No empty or faded-in frame 0. check: V-F0
- **H2 Cadence.** ≥ 8 weighted state changes in 0-3 s; 8-22 per 10 s in the body; no gap between weight-1 changes > 1.5 s; nothing fully static > 2.0 s (a diagram hold gets a C-3 drift). check: V-CADENCE
- **H3 Every word is read.** Every spoken phrase is on screen within ±1 f of its onset (captions lead 1 f), either as an auto-caption (CS-1/2/3) or inside a built text scene that carries the same words (title, node label, ladder, CTA line); never both at once. check: V-CAPTION + review
- **H4 Payoff by 2.5 s.** The framework's shape (hub skeleton, the condensed claim, or the proof card + full stack) is readable by 2.5 s (HA-06, HA-02) or 3.0 s (HA-12). check: V-F0
- **H5 Title limits.** The hook title (kind `title_card`) has ≤ 10 words, ≤ 5 stack lines, ≤ 2 lines when set as a TITLE-MIX (P-04), and holds ≥ 10 f after its last word lands. check: V-TITLE
- **H6 Dead air (spine `audio`).** The VO is not re-cut except to remove breaths > 0.35 s and false starts; a pause ≤ 0.8 s holds the current stack (the stack clears only after a pause ≥ 0.8 s or 5 lines, CS-1 `clear_gap_s`); a pause > 1.5 s is trimmed to 0.5 s. check: review
- **H7 On-the-word visuals.** Every node label, card, letter and count starts 2 f before its trigger word and is fully landed within ±5 f; camera pushes start 6 f before the item word so the node is framed on the word. check: V-ONWORD
- **H8 Face rule:** n/a (no presenter). V-FACE off.
- **H9 Presence:** n/a (`presence: none`); instead, **no frame without a built element** besides the world (a world alone > 0.5 s fails review). check: review
- **H10 Promise integrity.** The title's count equals the nodes, letters or items shown; every node of the hub is typed and visited; the acronym's letters all appear; the CTA keyword in the VO equals the keyword on the card. check: V-PROMISE
- **H11 Truth.** Every number on screen is spoken, stated in the script, or supplied by the creator (view counts, follower counts, the lead magnet's size). Created cards never show invented numbers; their rows are skeleton bars. check: V-NUMFMT + V-INSERTS + review
- **H12 Spelling.** English words and brand names exact; the glossary is enforced in captions. check: V-CAPTION
- **H13 Audio.** −14 LUFS integrated, true peak ≤ −1.5 dBTP, bed ≥ 18 dB under the VO, hard end ≤ 6 f after the last word (NC-8). check: qa
- **H14 Determinism.** Every frame a pure function of its index; thumb rain and drift seeded (`ctx.rngStable`). check: NC-9
- **H15 One shape per reel.** One marker shape (SM-1, SM-2 or SM-3), one hub or ladder; a second diagram type never appears. check: review
- **H16 Camera texts stay legible.** Text that the canvas camera moves is ≥ 40 px at zoom 1 (node labels, hub count) and is never pushed into the caption band while captions show. check: V-CANVAS
- **H17 World flips on section starts.** ≤ 3 flips, ≥ 3.0 s apart, each a hard cut on the first frame of a section. check: V-THEME

### 2.4 NEVER
- N1. A face, a hand, a webcam frame, an AI avatar or a stock person as the main visual. A creator-supplied clip may contain people (it is proof), never as a presenter substitute.
- N2. Fetched media of any kind: other creators' reels, tweets, profile photos, logos (NC-7). Created substitutes only (§12.5).
- N3. Bright palettes: more than 2 bright hues per frame; gradients; neon glows; colour on whole stack lines (the accent touches one word or one element).
- N4. Contrast failures: ink text on umber or ink worlds; white text on paper; ghost grey `#6F6F6F` below 96 px; the signal `#AE3F18` as text on umber.
- N5. Emoji, stickers, meme sounds, stamps, shakes, crash zooms (comedy is off).
- N6. Footage-style zooms on cards (no Ken Burns on created cards; creator clips may push 1.00 → 1.04 only).
- N7. Transitions outside T-01…T-10: no whips, light leaks, glitches, flashes, spins, page curls.
- N8. Two kinetic stacks at once, or a stack under a card; a stack line longer than 3 words or 16 characters.
- N9. A static diagram > 2.0 s, or a camera move shorter than 0.5 s.
- N10. Fake dashboards or invented "155M views" rows on a created card; a created card styled to look like a real platform (no platform logos, no platform blue ticks).
- N11. A lead-magnet promise the creator hasn't confirmed (resource name, count, delivery).
- N12. Decoration: every card, node and letter shows the thing being said.

Buyer additions BN1… `[VAR]`.

---

## §3 Worlds, layout zones, scene moves, safe zones `[REQ] [DNA; coordinates TUNE ±5%]`

### 3.1 Worlds
| ID | Kind | Look | Carries | Enter / exit |
|---|---|---|---|---|
| **W-paper** | canvas | `#E2E1DC` flat + graph-paper LINES: 64 px pitch, 1.5 px `#D8D7D1` (barely visible, as in v01); drawn by `fx.ambient({kind: "grid", bg: "canvas", ink: "grid", spacing: 64, follow: 0.7})` so the grid slides and scales with the canvas camera. **W-mist** (SM-1 hub and SM-2 thumb-rain hooks, v02 / v03 @ 0:00): `#EBEBEB` + faint dots, `fx.ambient({kind: "paper", bg: "mist", ink: "mist_dot", spacing: 36, dot: 1.6})` | Hook, framework, proof stack, recap, CTA | Open on it; return by T-01 hard cut |
| **W-umber** | card-world | `#3A2E2C` flat, no grid; `fx.ambient({kind: "void", bg: "umber", glow: "paper"})` is NOT used: draw a flat z1 fill (the void bloom adds a glow the evidence doesn't have) | CONTEXT section: white header line + one reference card | T-01 hard cut in and out |
| **W-ink** | void | `#151515` + faint dots 36 px `#1E1E1E` r 2.0 | Initial ladder (SM-2), dark proof card, the formula | T-01 hard cut in and out |
| *(P-08 punch)* | — | `#000000` full-frame z2 scene, 0.6-1.2 s | one two-line serif beat ("It's / that") | hard cut in, hard cut out; not a theme flip |

The timeline's `world` entries name the same ids (`W-paper`, `W-umber`, `W-ink`) at every flip, so the caption engine flips caption colour (ink on light, white on dark) with the world.

### 3.2 Layout library
| ID | Engine | Presenter | Graphic rect | Caption band | Share F-A |
|---|---|---|---|---|---|
| **L-canvas** | `hidden` | none | x 64-1016, y 110-1500 | per profile: CS-3 cy 330, CS-2 stack top 660, CS-1 stack top 910 | 100 % |

Timeline: `"stage": [{"t": 0, "layout": "L-canvas"}]` (engine `hidden`; the VO bundle forces it anyway). There is no layout schedule; the **zone plan** below replaces it.

### 3.3 Scene moves (G-…) (how elements change places; there is no presenter to move)
| ID | Move | Recipe (30 fps) | Use |
|---|---|---|---|
| **G-1** | **Stack fly-in** | A new line appears below the last one, near the frame bottom (≈ 450 px under its slot), and decelerates up into the slot: exponential out, ½ by f5, 90 % by f12, settled by f20; vertical motion blur 16 px → 0 over the first 3 f only; older lines stay exactly where they are (`anchor: "top"`, no glide). Measured v01 @ 0:01.29-0:01.92 ("style": 507 → 0 px from its slot, × 0.8 per frame) | Every new phrase in a stack |
| **G-2** | **Stack clear** | The whole stack vanishes on a hard cut (the next section's first frame); only inside one section, when a 6th line is due, do the lines blur 0 → 8 px and lift 44 px over 6 f | Section change (cut), or 5 lines full |
| **G-3** | **Card slide-in** | 4 f after a flip, a card enters from the right frame edge: a horizontal smear (`ctx.blur(12 → 0, 0)`) on its first 4 f, 80 % of the travel in 6 f, then the last ≈ 140 px continue as a slow drift (≈ 50 px/s) through the whole hold | A reference card arriving after a world flip (v01 @ 0:02.63-0:05.9) |
| **G-4** | **Proof flurry** | Hard cut to the next card set (profile bar + card) on its word; every card sits at a random tilt −5…+5° (`ctx.rngStable`, never 0 twice in a row); 0.25-0.5 s per set, 3-6 sets | A run of examples ("…just like these creators", v01 @ 0:06.21-0:08.13) |
| **G-5** | **Push-and-type** | Canvas camera C-1 snap to the node (15 f, see §21); 5 f after it lands the node's redaction bar is consumed from the left by its label typed at 45 cps, caret blinking every 15 f after | The first hub node visit (SM-1) |
| **G-6** | **Letter cut** | The giant initial and its tucked word are on screen whole on the cut frame (rest x 64); the first letter only de-blurs 8 → 0 px over 3 f; later letters have no entry motion at all | Every SM-2 letter (v03 @ 0:05.20, 0:06.48) |
| **G-8** | **Card rise-in** | 0-1 f after a cut to paper, a card rises from ≈ 450 px below its rest with scale 1.12 → 1.0, vertical motion blur on the first 3 f (`ctx.blur(px, 90)`), settled in 12 f (expo-out) | The first proof after an ink punch or a header change on paper (v01 @ 0:08.22, 0:13.89) |
| **G-9** | **Hub spin** | Camera held at the push framing; the hub (hex, bars, leaders, labels) rotates −360/N about its centre in 10 f, ease-out, so node k+1 comes to the top; the cut back from a proof lands on the spin's 3rd-4th frame; the next label starts typing on the spin's last 3 f | SM-1 node → node (v02 @ 0:06.37, 0:11.00) |
| **G-7** | **Morph hand-off** | `fx.morphShape`: the outgoing object becomes the incoming one (card rect → hub hexagon, letter → recap word) over 0.5 s | Section changes inside one world |

### 3.4 Zone diagrams (1080 × 1920)

**Zone A: hero card + low stack** (HA-02 hook, SM-3 proof stack; v01 @ 0:00-0:02.3)
```
┌──────────────────────────┐ 0
│   (IG top UI, keep clear)│ ← y 0-110
│      ╭──────────╮        │ ← HERO CARD x 324-756, y 180-856 (432×676, r 28)
│      │ 9:16 proof│       │   view chip bottom-left inside: x 346, y 790
│      │   card    │       │
│      ╰──────────╯        │ ← credit line (creator clips) y 864-888, x 324
│ ↶ This is the            │ ← stack top y 910 (CS-1), lines centred at x 540
│      Image to            │   sans 80 / serif 112, gap 36 (pitch ≈ 140), ≤ 5 lines
│        video             │   bottom of a 5-line stack ≈ y 1422
│        style             │
│       content            │ ← keep ≤ y 1500
│  (IG bottom UI)          │ ← y 1540-1920: nothing that means anything
└──────────────────────────┘ 1920
```

**Zone B: header line + large card** (CONTEXT on umber; proof beats; v01 @ 0:03-0:12)
```
┌──────────────────────────┐
│        types             │ ← CS-3 header line, cy 330, 64 px, 1-3 words
│    ╭───────────────╮     │ ← LARGE CARD x 270-810, y 450-1410 (540×960, r 28)
│    │               │     │   or PROFILE CARD x 80-1000, y 450-644 (920×194)
│    │   9:16 proof  │     │      + CLIP CARD x 335-745, y 700-1330 (410×630)
│    │               │     │
│    ╰───────────────╯     │ ← credit line y 1418-1442 when the card is a creator clip
└──────────────────────────┘
```

**Zone C: hub** (SM-1, HA-06; v02 @ 0:00-0:02.3), world px = screen px at home
```
┌──────────────────────────┐
│ 6 ways to Hook Viewers   │ ← TITLE-MIX line 1, cy 330, 62-72 px
│ in the first 3 seconds   │ ← line 2, cy 425 (serif tail)
│          ▬▬▬▬            │ ← top bar centre (540, 630), 230×40
│   ▬▬▬▬ ╲   │   ╱ ▬▬▬▬     │ ← bars at r 330 from the hub centre, -90° + k·360/N
│         ⬢ 6              │ ← HUB hexagon centre (540, 960), r 160; name in two tiers: Inter Tight 500 44 "6 ways to" over 800 72 "Hook Viewers" (paper)
│   ▬▬▬▬ ╱   │   ╲ ▬▬▬▬     │   leader lines 2 px ink, 8 px end dots; a right-hand node in y 1100-1700 keeps its right edge ≤ 960 (§21 hub geometry)
│          ▬▬▬▬            │ ← bottom bar centre (540, 1290)
└──────────────────────────┘
```

**Zone D: initial ladder** (SM-2 on W-ink; v03 @ 0:04-0:12)
```
┌──────────────────────────┐
│ ██       OOK             │ ← tucked word: Anton ≤ 200 px, scaleX 0.8, ghost; cap top y 500
│ ██  ██                   │   left = letter right edge + 16
│ ██████     Make them stop│ ← EXPLANATION LADDER x 520-1004, centre y 1000
│ ██  ██      scrolling    │   small 44 px / key word ≤ 104 px, white
│ ██  ██                   │
│ ↑ GIANT INITIAL x 64, cap y 500-1445 (Anton 1100 px, scaleX 0.8, ghost #6F6F6F)
└──────────────────────────┘
```

**Zone E: centre stack** (type-only beats, equation; v01 @ 0:18-0:21): CS-2 stack top y 660, up to 5 lines; the equation's "=" lines are serif 112 px; nothing else on screen.

**Zone F: lead-magnet card** (CTA; v01 @ 0:22, v03 @ 0:14)
```
┌──────────────────────────┐
│ Comment "KEYWORD"        │ ← CTA line y 300-410: 2 lines, Montserrat 800 48 px, ink
│ and I'll send you the link│
│ ╭──────────────────────╮ │ ← LEAD CARD x 110-970, y 470-1330 (860×860, r 28, vault #111111)
│ │ ▣ The [resource name]│ │   header row 44 px white; 5 skeleton rows (decorative)
│ │ ───── ▬▬ ▬▬          │ │
│ ╰──────────────────────╯ │
│  1,500+ [things] inside. │ ← COUNT LINE cy 1400, Montserrat 800 48 px, ink
└──────────────────────────┘
```

### 3.5 Safe zones and bands
- Meaning text stays inside x 64-1016, y 110-1500 (NC-5: nothing meaningful in the top 110 px, below y 1540, or in the right 110 px between y 900 and 1540).
- **Header band** y 270-400 (CS-3 and the TITLE-MIX first line). **Stack zones:** low y 910-1470, centre y 660-1260.
- The canvas camera may carry world content anywhere, but text it moves stays inside the safe box at rest positions (V-SAFE samples the settled frames).

### 3.6 Presenter rules
OFF (`presence: none`).

---

## §4 Colour, themes, grades `[REQ] [roles' meanings DNA; brandable hex VAR; theme hues TUNE]`

### 4.1 Role palette
| Role | Hex | Its one job | Text on it | Contrast | Brandable |
|---|---|---|---|---|---|
| `primary` **Signal** | {{BV-02.primary|#AE3F18}} | The one accent on paper: the active node ring, the typing caret, a quoted keyword in a stack | paper (5.96:1) | as text on canvas 4.86:1 | **yes** (BV-02 colour 1) |
| `accent` **Signal (dark)** | {{BV-02.accent|#F2A65A}} | The same job on umber and ink: active node on a dark card, caret on dark, the keyword on the lead card | ink (7.22:1) | on night 9.1:1, on umber 6.46:1 | **yes** (BV-02 colour 2) |
| `bad` | `#B83A3A` | The wrong way: strike-through, ✕ on a contrast pair | paper (5.67:1) | on canvas 4.62:1 | no (fixed) |
| `good` | `#1B6E49` | The right way: ✓ on a contrast pair | paper (6.23:1) | on canvas 5.08:1 | no (fixed) |
| `ink` | `#392E2C` | All type on paper, hub fill outline, card text | — | on canvas 11.92:1 | TUNE |
| `paper` | `#FFFFFF` | Type on umber / ink, light cards | — | on umber 13.07:1, on night 18.42:1 | DNA |
| `canvas` | `#E2E1DC` | W-paper ground | — | — | TUNE |
| `grid` | `#D8D7D1` | W-paper grid lines (1.5 px, 64 px pitch) | — | — | TUNE |
| `umber` | `#3A2E2C` | W-umber ground | — | — | TUNE |
| `night` | `#141414` | W-ink ground | — | — | TUNE |
| `hub` | `#262626` | Hub hexagon, redaction bars | paper (15.13:1) | — | TUNE |
| `ghost` | `#6F6F6F` | Giant initials and tucked words on W-ink (≥ 96 px only) | — | on night 3.67:1 | TUNE |
| `mute` | `#5E5853` | Secondary small type on paper ("It's a", "Top creators use", sublabels) | — | on canvas 5.72:1 | TUNE |
| `vault` | `#111111` | The lead-magnet card body | paper (18.88:1) | — | TUNE |
| `comedy` | — | unused (comedy off) | — | — | no |

Brand colours appear only on the buyer's own wordmark or the lead card's icon; a third-party brand colour never appears (created cards are neutral).

### 4.2 Meanings
- **Ink on paper** = the explanation. **White on dark** = a new section (context or reveal).
- **Signal (primary / accent)** = "this one": the node being visited, the word being typed, the keyword to comment. One element per frame.
- **Red → green** only for a wrong-way / right-way pair (P-16); never decorative.
- **Ghost grey** = the structure behind the explanation (giant letters, tucked words): big, quiet, never the words you read first.

### 4.3 Theme packs (per section)
| Section type | Pack | Ground | Notes |
|---|---|---|---|
| HOOK | TH-paper | W-paper | always |
| CONTEXT | TH-umber (SM-1, SM-3) / TH-ink (SM-2) | W-umber / W-ink | optional; umber when the VO gives context with a reference card ("one of the easiest… millions of views"); in SM-2 the letter line-up (P-24) opens the ink run |
| ITEM-n (SM-1 hub, SM-3 stack) | TH-paper | W-paper | the hub lives on paper |
| ITEM-n (SM-2 ladder) | TH-ink | W-ink | the whole ladder is one ink section |
| RECAP | TH-paper | W-paper | the acronym recap or the equation |
| CTA | TH-paper | W-paper | the lead card is dark on paper |

Write every flip twice: `timeline.theme_flips: [{t, theme}]` (V-THEME) and `timeline.world: [{t, world}]` (renderer + caption colour), at the same frame, which is a section's first frame. Budget: ≤ 3 flips; ≥ 3.0 s apart.

### 4.4 Grades
OFF: no footage grade. Creator-supplied clips are shown as delivered (no LUT, no B&W).

### 4.5 Rules
- `max_bright_per_frame: 2` (signal + one of bad/good). Most frames have 0 or 1.
- Coloured text on paper: only `primary`, `bad`, `good`, `mute` at ≥ 40 px (all ≥ 4.5:1 on canvas). Never `accent` on paper (1.9:1).
- On umber / ink: text is paper; the only coloured text is `accent`.
- No gradients, glows, bloom or vignette on any world.

---

## §5 Type & caption system `[REQ]`

### 5.1 Font map `[slots DNA; families TUNE within the class]`
| Slot | Family | Weights | Font class (TUNE boundary) | Used for |
|---|---|---|---|---|
| `display` | **Montserrat** | 500 / 600 / 700 | geometric sans 600-700 (Montserrat, Plus Jakarta Sans, Jost, Space Grotesk) | sans stack lines (600), header line (700), CTA lines, ladder text |
| `serif` | **Instrument Serif** | 400 italic | light italic display serif (Instrument Serif, EB Garamond, Source Serif 4) | serif stack lines, serif tails in titles, "=" lines |
| `numeric` | **Anton** | 400 | tall condensed caps (Anton, Barlow Condensed) | giant initials, tucked words, the condensed claim, the acronym recap |
| `ui` | **Inter Tight** | 500-800 | neo-grotesk (Inter Tight, Plus Jakarta Sans, Space Grotesk) | TITLE-MIX hub titles, node labels, view chips, card text, credit lines |
| `body` | **Montserrat** | 600-700 | as `display` | CS-3 header line |
| `mono` | **JetBrains Mono** | 400-600 | monospace | commands or prompts inside a created UI card only |

All fonts are bundled (`assets/fonts`). No other family enters a reel.

### 5.2 Headline element: the hook title `[DNA recipe; NICHE text]`
Kind **`title_card`** (scene `kind: "title_card"`), lifetime `hook`. It is either the hook's kinetic stack (HA-02, HA-12) or a TITLE-MIX (HA-06).

| Property | Spec |
|---|---|
| Fill / stroke / shadow | none: type sits directly on the world. No box, no stroke, no shadow |
| Size | stack: Montserrat 800 80 (tracking −0.035) / Instrument Serif italic 112 (−0.02); TITLE-MIX: Inter Tight 62-72 px (500 for connectors, 800 for keywords) + a light sans-italic tail (Inter Tight 300 italic) |
| Words / lines | ≤ 10 words; stack ≤ 5 lines of 1-3 words; TITLE-MIX ≤ 2 lines of ≤ 22 characters |
| Emphasis | TITLE-MIX: the count and the topic noun 800; connectors 500; the final 1-3 words serif italic (`_3 seconds_`). Stack: alternation is the emphasis; at most one word in `primary` (a quoted keyword) |
| f0 | the first word or line is rising on frame 0 (rise 6-9 f, blur 6 → 0) |
| Life | words append on their onsets (TITLE-MIX) or lines push up (stack); a serif tail may enter at 40 % opacity and reach 100 % over 10 f (P-09, v02 @ 0:01.17) |
| Exit | HA-06: blurs up and out (rise −60 px, blur 0 → 10 px, 8 f) inside the first C-1 push; HA-02 / HA-12: hard world flip (T-01) or stack clear (G-2) |
| Hold | ≥ 10 f after the last word lands; total hook 2.3-3.7 s |

### 5.3 Caption system profiles `[DNA mechanics; fonts TUNE; language VAR]`
Three profiles; all `extends: "lib:peter_visuals"` (the engine's caption library). The timeline switches them with `captions.overrides: [{t: [a, b], profile: "CS-3"}]` and hides them under built text with `captions.hide: [[a, b]]`.

| Group | **CS-1 Stack low** (default) | **CS-2 Stack centre** | **CS-3 Header line** |
|---|---|---|---|
| When | Under a hero card (Zone A), the hook stack of HA-02 | Type-only beats (Zone E): no card, no diagram | Above a card, a clip or a diagram (Zones B and C during visits) |
| Mode | full / primary / mute_safe | same | same |
| Chunking | `phrase`, 1-3 words, ≤ 16 chars, 1 line per chunk; never split a name, number or unit; new chunk on punctuation | same | `phrase`, 1-3 words, ≤ 18 chars |
| Timing | lead 1 f; ≥ 0.25 s per word; G-1 fly-in (≈ 450 px, 20 f exponential out, blur first 3 f) | same | lead 1 f; **hard swap** (0 f), 1-2 words per chunk, 2-3 swaps per second at speech pace; `pause_hold_s` 0.6 |
| Stack | `max_lines` 5; clear on the section cut; `top` 910; `gap_px` 36 (pitch ≈ 140); alternate: line 1 `display` 800 80 px (−0.035 em), line 2 `serif` italic 400 112 px, repeat | same, `top` 660 | none (replace mode: one phrase at a time) |
| Skin | case as spoken; ink on light worlds, paper on dark (`colour_by_bg`); no stroke, no shadow, no container | same | Montserrat 800, 76 px, same colours |
| Position | `fixed_y`, centred x 540, `max_w` 920 | `fixed_y` cy 960 | `fixed_y` cy 312 (≈ 70 px above a lower card), `max_w` 900 |
| Emphasis | none (the alternation is the emphasis) | none | none |
| Hide rules | under z8 scenes; under any built text scene carrying the same words (title, node label, ladder, CTA line) via `captions.hide` | same | same |
| Language | Latn; keep English terms; no spelling normalisation; profanity masked `inner` (S**T), on by default; glossary enforced | same | same |

Measured basis: v01 @ 0:00.17-0:02.33 (lines rise from ≈ y 1595 to their slot with a visible vertical blur; the 5-line stack "This is the / Image to / video / style / content" occupies y 905-1470); v01 @ 0:03-0:12 (one bold phrase at a time at cy 313-486 above the card).

**The stack's alternation never breaks:** the engine alternates by line position (`alternate`). Do not override fonts per line in captions; when one word must be serif inside a sans line (a title), build that text as a scene (P-04) and hide the captions there.

### 5.4 Other text systems
| Token (`type.*`) | Element | Class | Recipe | Hold |
|---|---|---|---|---|
| `title_mix` | **Title-mix** (P-04) | TC-display | Inter Tight 62-72 px; keywords 800, connectors 500, tail in light sans italic (Inter Tight 300 italic, e.g. "3 seconds"), NOT a serif (v02 @ 0:01.5); words appear on their onsets in final position, each rising 18 px with blur 6 → 0 over 6 f; line 1 cy 330, line 2 cy 425 | ≥ 10 f after the last word |
| `node_label` | **Node label** (P-12) | TC-label | Inter Tight 500, 40 px world (≈ 92 px on screen at 2.3×); typed at 45 cps with a caret (`fx.typewriter`); the redaction bar is consumed from the left as the letters arrive | until the hub leaves |
| `hub_center` | **Hub name** (P-11) | TC-display | the framework's name in two tiers, centred in the hexagon: Inter Tight 500 44 px ("6 ways to") over Inter Tight 800 72 px ("Hook Viewers"), paper; the hex has a thin inner light ring (v02 @ 0:02.6). No giant count numeral | the hub's life |
| `giant_initial` | **Giant initial** (P-20) | TC-display | Anton 1100 px, `scaleX(0.8)`, ghost `#6F6F6F` on W-ink, cap y 500-1445, x 64 | 1.0-2.0 s per letter |
| `tucked_word` | **Tucked word** (P-21) | TC-display | Anton, size = min(200, fit to x 1004), `scaleX(0.8)`, ghost; uppercase; cap top y 500; when the fitted size is < 110 px the colour switches to paper (contrast) | with its letter |
| `ladder_small` / `ladder_big` | **Explanation ladder** (P-22) | TC-label + TC-display | 2-4 words, Montserrat white: helper words 500 44 px, the key word 700 at min(104 px, fit to 484 px width); x 520-1004, block centre y 1000; words appear on onsets with 6 f rise | until the next letter |
| `stack_cond` / `stack_small` | **Condensed claim** (P-06) | TC-display | Anton 140-200 px uppercase, `mute` on paper; small helper above ("It's a") and below ("Top creators use") in Montserrat 500 48 px `mute`, serif italic for one helper word | ≥ 0.8 s |
| `view_chip` | **View chip** (P-34) | TC-label | inside the card bottom-left (22 px inset): eye icon 34 px + Inter Tight 700 40 px paper on `rgba(0,0,0,.6)` pill, radius 30, padding 8/20 | the card's life |
| `credit` | **Credit line** (§19) | TC-legal | Inter Tight 500, 24 px, ink (paper on dark) at 72 % opacity, `via @handle`, left-aligned under the card | the card's life |
| `cta_line` | **CTA line** (P-38) | TC-label | Montserrat 800 48 px ink, 2 lines centred, cy 354 / 415; the keyword in straight quotes, same weight, no underline, no colour | the CTA |
| `cta_count` | **Count line** (P-39) | TC-label | Montserrat 800 48 px ink, cy 1400, one sentence ending in a full stop ("1,500+ viral hooks with links.") | the CTA |
| `acronym_recap` | **Acronym recap** (P-23) | TC-display | "That's" Montserrat 500 56 px ink above; the letters Anton 300 px ink, centred cy 960 | ≥ 0.8 s |
| — | **Arrow pointer** (P-07) | TC-display | a hand-drawn curved arrow SVG (4 px ink, 120 × 90 px) that pops in whole with the first stack word (v01 @ 0:00.08), pointing up-right at the hero card, left of that word | the stack's life |

### 5.5 Language and number rules
- **English (default):** sentence case as spoken; brand names exact; straight double quotes around a keyword (`"Database"`).
- **Hinglish (`hinglish/hinglish/Latn`):** romanised as the creator writes it; English terms kept verbatim; the alternation is unchanged.
- **Hinglish → English captions:** translate per sentence (`transform: translate`) from the script; on-screen titles and labels in English.
- **Hindi (`hi/hi/Deva`):** Devanagari has no italic: the serif lines become **Noto Sans Devanagari 400 at 88 px** and the sans lines **Noto Sans Devanagari 700 at 72 px** (the weight contrast replaces the style contrast); ALL-CAPS tucked words become the full word in Devanagari at the same size rule; giant initials stay Latin only when the acronym is Latin, else use the Devanagari first akshara.
- **Numbers:** International grouping by default; compact view chips with one decimal (`6.7M`, `2.1M`, `155M`); counts with grouping and a plus (`1,500+`); currency glyph pre-painted; Indian grouping (`1,50,000`, `₹2.5 L`) when the language is Hinglish or Hindi (BV-06).
- Every number is spoken, in the script, or creator-supplied (H11).

---

## §6 Hook system `[REQ]`

**Hook title (every style, 8 Oct 2026; above anything below):** the on-screen title promises the viewer something: an outcome they want, a curiosity gap, or who it's for ("How to go viral as a doctor creating content", not the label "Reels for Doctors"). It doesn't have to repeat the spoken words; it has to be true to what the reel delivers. A title shown as someone's words (in quotes) is still word for word. This section sets the title's shape (lines, sizes, word limits, case, the keyword device), never its voice. Write 8–10 candidates from the formulas below plus the proven patterns ("How to X as a Y", "Why your X isn't working", "The X nobody tells you", "Stop doing X", "Your X vs mine", a number or a contrast), score them on outcome, curiosity, who it's for and brevity, check the best against the stopper tests, and pick; any "write 3" below means this, and the next two go to the storyboard as alternates. A style with no on-screen title applies this to its post title.

### 6.1 Stopper tests (run on frame 0 and on 0-3 s)
| Test | This style's number |
|---|---|
| **ST-1 Thumbnail** | f0 at 25 % scale shows paper + the shape starting; at 1.0 s (the cover frame) the title is readable at 25 % (72 px → 18 px) |
| **ST-2 Mute** | with sound off, 0-3 s tells the promise: the title or stack carries every word |
| **ST-3 Motion at f0** | ≥ 1 element moving on f0 (hub dot growing, rain drifting, title word rising) |
| **ST-5 Change count** | ≥ **8** weighted state changes in 0-3 s (`hooks.stopper.hook_sc_3s`; measured 8-10 in v01 / v02, 7-8 in v03) |
| **ST-6 Payoff-by** | the shape is readable by **2.5 s** (HA-06, HA-02) or **3.0 s** (HA-12) |

ST-4 (read time) is replaced by H5: the title builds at speech pace and holds ≥ 10 f.

### 6.2 Default archetype: HA-06 Framework build (SM-1 hub tour; from v02 @ 0:00-0:03)
Spoken pattern: "**[N] ways to [result] [in / for / without X]**", then straight into item 1.

| t (s) | f | On screen | Captions | Canvas camera | Cue moment |
|---|---|---|---|---|---|
| **0.00** | 0 | W-paper. Hub dot (hex r 12, `hub` fill) at (540, 960) already scaling. Title word 1 (the count, Inter Tight 800 72 px) rising at cy 330 | hidden (the title carries the words) | home (540, 960, 1) | — (bed from f0) |
| 0.10-0.53 | 3-16 | Hex at ≈ 70 % size by f4; N redaction bars (230 × 40, `hub`) pop one every 2 f clockwise from the top, each with a 2 px leader line and an 8 px end dot; the whole hub keeps growing to 100 % until 1.2 s (scale it from 0.8, ease-out; v02 @ 0:00.13-0:01.20) | — | home | reveal (the hub lands) |
| 0.17-1.10 | 5-33 | Title line 1 appends word by word on the onsets: "**[N]** ways to **[Topic]**" (count and topic 800, connectors 500) | — | home | — |
| 1.00 | 30 | Hub name inside the hex: Inter Tight 500 44 px "[N] ways to" over Inter Tight 800 72 px "[Noun]" (paper) | — | home | — |
| 1.10-1.50 | 33-45 | Title line 2 at cy 425: "in the **[keyword]** _[serif tail]_"; the serif tail enters at 40 % and reaches 100 % over 10 f (P-09) | — | home | — |
| 1.20-2.10 | 36-63 | Hold, almost still (the hub's last ≤ 1 % of growth) | — | home | — |
| **2.10-2.60** | 63-78 | The title blurs out in place (blur 0 → 10, fade, 6 f); **C-1 snap push** 1.0 → 2.3× (15 f, nearly all of it on f5-f8, zoom blur there), framed so node 1's bar sits at y ≈ 820 and the hub below it | — | C-1 | transition (the push) |
| 2.47-2.87 | 74-86 | Node 1's label types at 45 cps over its bar, caret blinking after | CS-3 header line from the item sentence | held | — |

Payoff: the hub skeleton is complete by 1.0 s (≤ 2.5 s). State changes 0-3 s: hub enter + N bar events + 6-9 title words + line 2 + count + drift + push + label ≈ 14.

### 6.3 Allowed alternates `[DNA list; VAR choice per reel]`

**HA-12 Thesis typography (SM-2 initial ladder; from v03 @ 0:00-0:04).** Spoken: "**[Topic] isn't [myth]. It's a [N]-letter formula [who] use.**"

| t (s) | f | On screen | Captions | Camera | Cue |
|---|---|---|---|---|---|
| **0.00** | 0 | W-paper + **P-34 thumb rain** drifting (24 tiles, 3 depths); thesis word 1 "[Topic]" rising at cy 950 (Montserrat 800 80) | hidden | home | — |
| 0.17-1.17 | 5-35 | Words append on one line (P-10): "[Topic] isn't _[Myth]._" (the last word Instrument Serif italic 112) | — | — | — |
| 1.17-1.50 | 35-45 | Line clears (G-2, 6 f); "It's a" (Montserrat 500 48 `mute`) rises at y 880 | — | — | — |
| 1.67 | 50 | **P-06 condensed claim** "[N]-LETTER FORMULA" Anton 160 px `mute` rises 9 f at cy 960 | — | — | reveal |
| 2.00-2.40 | 60-72 | Helper "[Top] _[Creators]_ [use]" (48 px `mute`, one serif word) appends at cy 1070 | — | — | — |
| 2.40-3.70 | 72-111 | Hold; the rain keeps drifting (continuous motion) and dims under the text | — | — | — |
| **3.70** | 111 | **T-01** hard flip → W-ink: P-24 letter line-up "It's called [L1] [L2] [L3] [L4]" | CS-3 (white) | — | transition |

Payoff: thesis + claim readable by 2.0 s (≤ 3.0). The HOOK section ends at 2.7 s (payoff + 10 f); 2.7-3.7 s is the start of CONTEXT on paper (the intro cap, §7.4). Example (fitness): "Fat loss isn't _willpower._ It's a 4-LETTER FORMULA coaches use" → "It's called S L E D". Example (marketing): "Going viral isn't _luck._ It's a 4-LETTER FORMULA top creators use" → "It's called H R S T".

**HA-02 Headline + proof (SM-3 proof stack; from v01 @ 0:00-0:03).** Spoken: "**This is the [name] [style / format / method].**"

| t (s) | f | On screen | Captions | Camera | Cue |
|---|---|---|---|---|---|
| **0.00** | 0 | W-paper; **P-25 hero card** (432 × 676 at x 324, y 180) settling over f0-8 (scale 1.04 → 1, blur 8 → 0) showing the proof (the creator's clip playing, or a created card); view chip inside | hidden (the title stack carries the words) | — | — |
| 0.08 | 2 | **P-07 arrow** pops in whole with the first word; line 1 "_This is the_" (serif italic 112, y 910) builds word by word in place, each word a hard pop on its onset | — | — | — |
| 0.75-2.33 | 23-70 | Lines fly in on their phrase onsets (G-1): "**[Name]**" / "_[part 2]_" / "**[style]**" / "_[content]_" (≤ 5 lines, 1-3 words each); a line still settling when the next arrives keeps settling | — | — | — |
| 2.33-2.50 | 70-75 | Hold (the stack is complete) | — | — | — |
| **2.50** | 75 | **T-01** hard flip → W-umber: CS-3 header "[next phrase]" (white, cy 312) on the cut frame; 4 f later **P-29** a second card slides in from the right edge (G-3) | CS-3 | — | transition |

Payoff: the proof is on screen at f0; the stack completes by 2.33 s. Example (marketing): "This is the / image to / _video_ / style / _content_". Example (fitness): "This is the / 3-2-1 / _method_ / for / _fat loss_".

The hook stack of HA-02 **starts on a serif line** (the arrow + "This…", as v01); every other stack starts on sans.

### 6.4 Hook pairs by topic `[NICHE]`
Pair types: HA-06 = **promise → proof** (the count → N nodes, each proved); HA-12 = **thesis → scene promise** (the myth → the acronym); HA-02 = **subject → reveal** (the named thing → its proof card at f0).

| Niche `[NICHE: example]` | Archetype | Hook line (title) | Shape / proof by 2.5 s | Proof per part |
|---|---|---|---|---|
| Content & marketing | HA-06 | "6 ways to hook viewers _in the first 3 seconds_" | 6-bar hub | a creator example clip per node (or a created clip-UI card with the hook line typed) |
| Content & marketing | HA-12 | "Storytelling isn't _talent._ It's a 4-LETTER FORMULA" | condensed claim over the thumb rain | giant initials H-R-S-T with one ladder phrase each |
| Content & marketing | HA-02 | "This is the / image to / _video_ / style / _content_" | the creator's reel in the hero card | profile card + clip card (P-28), a quote card (P-27) |
| Content & marketing | HA-06 | "4 posts that _turn followers into buyers_" | 4-bar hub | a created quote card per post type |
| Fitness & nutrition | HA-06 | "5 habits that _keep fat off_" | 5-bar hub | number card (P-36) or icon card (P-37) per habit |
| Fitness & nutrition | HA-12 | "Fat loss isn't _willpower._ It's a 4-LETTER FORMULA" | condensed claim over the thumb rain | giant initials S-L-E-D (sleep, lift, eat protein, daily steps) |
| Fitness & nutrition | HA-02 | "This is the / 3-2-1 / _method_ / for / _fat loss_" | the creator's training clip in the hero card | clip card + equation recap "3 lifts = 2 cardio = 1 rest day" |
| Fitness & nutrition | HA-06 | "3 meals _that do the work for you_" | 3-bar hub | icon cards (P-37: bowl, plate, cup) |

Per reel (P7) the editor writes the new pair in the archetype's pair type and appends it here in the buyer's copy.

### 6.5 Headline writing `[DNA formula; NICHE examples]`
| Template | Formula | Example |
|---|---|---|
| **Hub promise** (HA-06) | "**[N]** [ways / habits / posts / mistakes] to **[result]** _[when / for whom]_" | "6 ways to **Hook Viewers** _in the first 3 seconds_" |
| **Myth → formula** (HA-12) | "[Topic] isn't _[myth]._" + "It's a **[N]-LETTER FORMULA** [who] use" | "Fat loss isn't _willpower._ It's a **4-LETTER FORMULA** coaches use" |
| **This-is** (HA-02) | "_This is the_ / **[name]** / _[kind]_ / **[noun]**" (one phrase per line) | "_This is the_ / **image to** / _video_ / **style** / _content_" |
| **Equation** (recap, P-05) | "_More [X]_ / = / _More [Y]_ / = / _[Result]._" | "_More loops_ = _More views_ = _Better reach._" |

Rules:
- ≤ 10 words; sentence case; the count is a numeral and equals the parts shown (H10).
- One serif tail per title (the last 1-3 words); the count and the topic noun are the bold words.
- No emoji, no exclamation marks, no ALL CAPS except the condensed claim and acronyms.
- Banned: "game changer", "secret", "nobody tells you", "hack" (unless the VO says it), any claim the reel doesn't show.
- **Write 3 and pick by the stopper tests** (§6.1); the other two go to the checkpoint as A/B options.

### 6.6 Hook sound
The music bed runs from f0 (calm, ducked ≥ 18 dB under the VO). The hook may carry one cue on its reveal moment (the hub landing, the claim, or the first flip). See §11.

### 6.7 CTA `[DNA device set; VAR values]`
The CTA is the last 3.0-4.0 s, always on W-paper, always the **P-39 lead card** (§25). Device: {{BV-08.device|comment_keyword}}.

| Device | Spoken pattern | On screen | Hold | Placement |
|---|---|---|---|---|
| `comment_keyword` (default) | "Comment **'{{BV-08.keyword|KEYWORD}}'** and I'll send you [the resource]." | **P-38** CTA line `Comment "{{BV-08.keyword|KEYWORD}}"` / `and I'll send you the link.` (scene `kind: "cta-keyword"`); **P-39** lead card; count line, all on screen on the cut frame and still | card ≥ 2.0 s; keyword readable ≥ 1.5 s | end |
| `link_bio` | "It's free, the link is in my bio." | CTA line `Free [resource]` / `link in bio`; P-39 card; count line | same | end |
| `end_card` | (always on) | the lead card itself, ≤ 4.0 s | — | end |

- The CTA beat's captions are hidden (the CTA line carries the words); a VO phrase after the keyword runs as a CS-3 header **only if** the CTA line has already shown for 1.5 s, replacing it. **Alternate (v03 @ 0:13.60-0:17.9):** no CTA line; the whole CTA sentence runs as CS-3 header words ("comment" / "Database" / "and I'll" / "send" / "you"…) over the still card.
- **Nothing moves in the CTA** except header swaps: no drift, no row build, no underline (v01 is dead still for its last 2.05 s). If no header swap falls in the last 2.0 s, end the reel ≤ 2.0 s after the card lands (`max_static_s`).
- No silence before the CTA; no cue after the last word; hard end ≤ 6 f after the last word.

---

## §7 Structure & cadence `[REQ] [DNA]`

### 7.1 Structure type: `framework`
`HOOK` (title + shape, ≤ 15 % of runtime) → `CONTEXT` (optional, 2.5-4.0 s; TH-umber when it carries a reference card) → `ITEM-1…N` (the marker ritual) → `RECAP` (optional, 1.0-2.5 s: the hub pulled out, the acronym, or the equation) → `CTA` (3.0-4.0 s).

Typical timings (24 s reel): HOOK 0-2.5 · CONTEXT 2.5-6.0 · ITEMS 6.0-18.5 · RECAP 18.5-20.5 · CTA 20.5-24.0.

### 7.2 Markers (one shape per reel)
| ID | Marker shape | Numbering | Recap | Evidence |
|---|---|---|---|---|
| **SM-1** | **Hub tour**: hexagon hub + N bars; each item = a camera visit to its node; the label types | clockwise from the top (asc) | the pull-out shows all labels (P-14) | v02 @ 0:00-0:33 |
| **SM-2** | **Initial ladder**: one giant initial per item on W-ink, tucked word, explanation ladder | the acronym's letter order | "That's [ACRONYM]" on paper (P-23) | v03 @ 0:04-0:13 |
| **SM-3** | **Proof stack**: hero card + stack below; items are proofs; no numbering | none (spoken only) | the equation (P-05) | v01 @ 0:00-0:21 |

No numbered badges, no "Step 1" chips: the shape is the marker.

### 7.3 Unit rituals (identical for every item of a reel)
**SM-1 node visit** (3.0-5.0 s per item):
1. f −8 (before the item word): item 1 = **C-1 snap push** home → node (15 f, 2.3×); item k > 1 = **G-9 hub spin** (−360/N, 10 f, ease-out, camera held), entered by the T-02 cut back from the previous proof on the spin's 3rd-4th frame.
2. f 0 (item word): node k's bar is typed over at 45 cps (≤ 18 chars ≈ ≤ 12 f), caret blinking after. Visited labels stay full ink (no dimming, v02 @ 0:06.50); unvisited nodes stay black bars.
3. Label done + 10-25 f: either
   - **with proof:** T-02 hard cut to the proof, 2.5-4.5 s (v02: full-bleed example reels 3.0-4.6 s each, ≈ 60 % of runtime): P-33 full-bleed clip or P-32 clip card, P-26 large card or P-27 quote card + CS-3 header line; then T-02 hard cut back into the next spin; or
   - **without proof:** CS-3 header line runs over the zoomed hub (the header band y 270-400 is clear because the node is framed at y ≥ 560), 1.0-2.5 s, with a C-3 drift of 30 px.
4. After the last item: the reel goes straight to the CTA (v02 ends on its last proof). Optional, not in evidence: **C-2 pull** to home (18 f) under a recap line.

**SM-2 letter** (1.0-2.0 s per letter):
1. f −2 (before the part's word): T-09 hard cut: the previous letter, tucked word and ladder vanish together (declared `cuts`).
2. f 0: **G-6** the giant initial and its tucked word are on screen whole (the first letter only de-blurs 8 → 0 over 3 f).
3. f 6 →: the ladder words pop on their onsets: helpers hard, the key word at 110 % settling to 100 % over 4 f (v03 @ 0:06.08).
4. Hold ≥ 10 f after the last ladder word; the next letter cuts in on its word.
5. After the last letter: T-01 flip → W-paper, P-23 acronym recap (letters slide in like P-24, then T-11 into the CTA).

**SM-3 proof** (one section per idea, 2.5-5 s):
1. A section opens on a hard cut (world flip, or a header change on paper) with its card entering by G-3 (slide from the right) or G-8 (rise from below); the card then holds while CS-3 header words swap above it 2-3× per second.
2. A run of examples is a **G-4 proof flurry** (hard cuts every 0.25-0.5 s, tilted cards).
3. One emphatic line gets the **P-08 ink punch**; the recap is the equation (P-05) on W-paper, entered after a hard cut that empties the frame.

### 7.4 Open loops and re-hooks
- **Count loop:** the title's N is paid by N visited nodes / N letters (V-PROMISE count = shown items).
- **Deliverable loop:** the CTA resource named in the hook (optional) is shown on the lead card.
- **Re-hooks:** none required (micro). When TUNEd to `short` (> 30 s), add one numeral teaser at mid-reel: the hub pulls out to show "[k] of [N]" by dimming visited nodes (scene `kind: "teaser"`).
- **Intro cap:** HOOK ≤ 15 % of the runtime (V-REHOOK): 2.7 s in an 18 s reel, 3.75 s in a 25 s reel. The HOOK section ends when the payoff lands + 10 f; any longer hold belongs to CONTEXT.

### 7.5 Rhythm and energy curve
- Information only (no comedy beats). Energy is flat-calm with **one peak**: the first C-1 push (SM-1), the first giant letter (SM-2) or the umber flip (SM-3).
- Items run at an even pace (± 20 % duration); the last item never escalates in size. Completion is shown by **pulling back** to the whole framework (recap), not by a bigger effect.
- The end feels filed and finished: the lead card holds still while the CTA line reads.

### 7.6 Cadence (weighted state changes)
| Token | Value | Basis |
|---|---|---|
| `sc_per_10s` | **[8, 22]** | full-frame-rate: motion onsets 11.8 (v01), 9.0 (v02), 9.5 (v03) per 10 s, plus CS-3 header swaps 2-3/s on top |
| `hook_sc_3s` | **8** | v01 ≈ 9, v02 ≈ 9, v03 ≈ 7-8 |
| `max_gap_s` | **1.5** | the longest phrase hold at speech pace |
| `max_static_s` | **2.0** | longest fully still stretch in the body: 0.67 s (v01), 1.13 s (v02, inside a clip), 0.76 s (v03); aim ≤ 1.2 s in the body; only the CTA reaches 2.0 s (v01 2.05 s) |
| hard-cut shot length | median 2.5 s (v01), 1.3 s (v02), 3.6 s (v03 detector; letter cuts add 1.0-1.3 s shots) | scene detection at 0.2 |
| `caption_weight` | **1.0** | captions are `primary` |
| `cuts_per_min` | not DNA | the detector reads 13-27, but changes are type-driven |

Deviation from STYLE-COVERAGE (which lists 6-10 SC/10 s): the band is [8, 22] because primary captions weigh 1.0 and header words swap 2-3× per second.

---

## §8 Visual system: graphics, proof cards and patterns `[REQ]`

### 8.1 Graphics role and budget
- `graphics: primary`: 100 % of runtime is built graphics or proof cards. Per reel (micro): **8-14 distinct patterns**, ≥ 4 families, exactly 1 marker shape.
- **Numbers become pictures** the style's way: a spoken count becomes N nodes / N letters; a view or follower count becomes a view chip on its card; a spoken stat ("6 months", "4 clients") becomes a P-36 number card. Never a bare number floating on paper.

### 8.2 Families
| ID | Family | Source class | Buyer must supply |
|---|---|---|---|
| B-1 | Kinetic type | engine (caption profiles CS-1…3, `fx.typeStack`, bespoke title scenes) | — |
| B-2 | Diagram canvas | engine (`fx.diagram`, `fx.morphShape`, canvas camera) | — |
| B-3 | Giant type | engine (bespoke scenes) | — |
| B-4 | Proof cards | **creator-supplied third-party** (their screenshots of posts, profiles, reels) → created substitute: `fx.quoteCard`, a created profile card (`recreated_ui`), `fx.appUI({kind: "video"})` | optional: screenshots / clips they own or hold |
| B-5 | Creator clips | **buyer-owned** (their own reels, B-roll, screen recordings) or creator-supplied third-party (example reels they hold) → created substitute: `fx.appUI({kind: "video", caption})` | optional: 9:16 clips ≥ 720 × 1280 |
| B-6 | Ambient & world | engine (`fx.ambient`, bespoke z1-2 grounds, P-34 tiles) | optional: thumbnails of their own reels for P-34 |
| B-7 | Engine cards | engine (`fx.card` number and icon cards) | — |
| B-8 | Lead magnet & brand | engine (created lead card) or buyer-owned (a screenshot of their own resource via `fx.shot`) | optional: a screenshot of the resource; its real name and size (required to state a count) |

### 8.3 Pattern specs (30 fps)

**B-1 Kinetic type**

| ID | Pattern | Type | What's on screen | Motion recipe | Use | Engine block · class |
|---|---|---|---|---|---|---|
| **P-01** | Stack low | overlay | 1-5 phrase lines under the hero card, alternating Montserrat 800 80 / Instrument Serif italic 112, centred, top y 910 | G-1 fly-in ≈ 450 px, 20 f exponential out, blur first 3 f; older lines fixed; cleared by the section cut | Any phrase while a hero card holds (Zone A) | captions CS-1 · TC-subtitle |
| **P-02** | Stack centre | overlay | the same stack centred, top y 660 | as P-01 | Type-only beats (no card) | captions CS-2 · TC-subtitle |
| **P-03** | Header line | overlay | one bold phrase (Montserrat 800 76) at cy 330, replaced phrase by phrase | hard swap, 1-2 words per chunk, same position (v01 @ 0:04.45 → 0:04.55); holds through pauses ≤ 0.6 s | Above a card, clip, profile card or zoomed hub | captions CS-3 · TC-subtitle |
| **P-04** | Title-mix | overlay | the HA-06 title: 2 lines at cy 330 / 425, Inter Tight 500/800 + serif italic tail | each word rises 18 px with blur 6 → 0 over 6 f on its onset (final position, no reflow) | HA-06 hook only | bespoke scene `kind: "title_card"` · TC-display |
| **P-05** | Equation stack | overlay | "_More [X]_ / = / _More [Y]_ / = / _[Result]._": serif italic 112 lines, "=" serif 112 lines, centred, first line cy ≈ 670, pitch ≈ 150, growing downward | after a hard cut that empties the frame, each element (line or "=") slides in from the right edge with a horizontal motion blur, 8 f expo-out (½ by f2), on its onset; nothing above it moves (v01 @ 0:19.06-0:21.35) | RECAP of SM-3; any "A means B means C" | bespoke scene (captions hidden; `in: "none"`, per element: x +600 → 0 and a horizontal smear `filter:${ctx.blur(12 → 0, 0)}` on f0-3) · TC-display |
| **P-06** | Condensed claim | overlay | "[N]-LETTER FORMULA" Anton 140-200 px uppercase `mute`, helper lines Montserrat 500 48 `mute` above and below (one helper word serif) | the claim rises 30 px over 9 f; helpers append per word (6 f) | HA-12 hook; any "it's a [N]-part [thing]" | bespoke or `fx.typeStack` with `style: "cond"` · TC-display |
| **P-07** | Arrow pointer | annotation | a curved hand-drawn arrow (4 px ink SVG, 120 × 90) beside the first stack word, pointing at the hero card | `stroke-dashoffset` draw over 8 f, head last 2 f | HA-02 "This is…" | bespoke SVG next to the hook stack · — |
| **P-08** | Ink punch | overlay | full-frame `#000000` (z2) + a 2-3 line serif italic staircase in white: "It's" 96 px right of centre, "that" 96 px left of centre, "simple." ≈ 200 px under them (the payoff word ≈ 2×) | hard cut in (`cuts: [0]`) with word 1 on the cut frame; each next word pops hard on its onset (no rise); hard cut out after 0.6-1.0 s straight into a G-8 card rise (v01 @ 0:13.14-0:13.89) | One short emphatic phrase between two paper sections, ≤ 1 per reel | bespoke z2 scene · TC-display |
| **P-09** | Ghost tail | overlay | the last 1-3 words of a title in serif italic at 40 % opacity, then 100 % | opacity 0.4 → 1 over 10 f, 6 f after the words land | HA-06 title line 2 | inside P-04 (`~ghost~` mark) · TC-display |
| **P-10** | Word-append thesis | overlay | one centred line at cy 950; words append in place on their onsets; the last word serif italic 112 | each word rises 18 px + blur 6 over 6 f; the line clears with G-2 | HA-12 hook | bespoke scene `kind: "title_card"` · TC-display |

**B-2 Diagram canvas**

| ID | Pattern | Type | What's on screen | Motion recipe | Use | Engine block · class |
|---|---|---|---|---|---|---|
| **P-11** | Hub skeleton | stage | hexagon r 160 (`hub`) at (540, 960) + N bars 230 × 40 at r 330, leader lines 2 px ink, end dots 8 px; the framework name in two tiers inside the hex (thin outer ring + thin inner light ring, v02) | f0 hex dot; hex ≈ 70 % by f4; bars pop every 2 f clockwise from −90°; the whole hub grows 0.8 → 1.0 until 1.2 s (ease-out) | SM-1 hook | `fx.diagram` (nodes `reveal: "redact"`, scene `kind: "diagram"`) + a C-1-style camera `push` 0.8 → 1.0 over 1.2 s, `ease: out` · TC-label |
| **P-12** | Push-and-type | stage | the camera framed on node 1 at 2.3× (bar at y ≈ 820, hub below); its bar becomes the typed label (Inter Tight 500 40 px world ≈ 92 px on screen) | C-1 snap push 15 f; the label types at 45 cps from 5 f after landing; the caret blinks every 15 f after | SM-1 item 1 | canvas camera + node `label_at`, `cps: 45` · TC-label |
| **P-13** | Hub spin | stage | the hub rotates −360/N about its centre so node k comes to the top; camera held | G-9: 10 f ease-out, entered mid-spin by the T-02 cut back from a proof; node k's label types (45 cps) from the spin's last 3 f | SM-1 items 2…N | bespoke hub scene with `transform: rotate()` about (540, 960) (still bespoke: a −360/N spin is 45-120° in 10 f, past the canvas camera's roll limits of 20° and 2°/frame, and `fx.diagram` has no rotation); fallback C-3 `dolly` 15 f started 4 f before the cut back · — |
| **P-14** | Hub recap *(optional; not in evidence)* | stage | pull-out to home: every label readable, none active | C-2 18 f | End of SM-1 when the VO recaps | canvas camera · TC-label |
| **P-15** | Redact list | stage | a vertical list of N bars (x 160-920, 120 px pitch from y 520) that type their labels one by one | C-3 pan down 24 f per item (the active row at y 760 on screen) | SM-1 when the parts are sequential steps, not parallel | `fx.diagram` (bars `reveal: "redact"`) · TC-label |
| **P-16** | Contrast pair | figure | two columns on paper: "wrong" (ink 48 px label, `bad` 6 px strike over it) and "right" (ink 48 px + `good` ✓ 48 px), 420 px each, x 80 / 580, y 700-1180 | left column rises 9 f; the strike wipes L → R 7 f on the wrong word; right column 9 f; ✓ pops 6 f | "do this, not that" lines | `fx.diagram` (rect nodes) or `fx.card` × 2 · TC-label |
| **P-17** | Flow stations | stage | 2-4 stations on one canvas (one screen apart), each a pill title + 1-2 rect nodes with an arrow | C-3 dolly 1.0-1.5 s between stations; C-1 push into the key node | A process (input → step → output) inside an item | `fx.diagram` × stations (offsets as in `renderer/demo/faceless`) · TC-label |
| **P-18** | Zoom-through | stage | the camera dives into a node; its fill becomes the next scene's ground | C-4 scale 4, 0.6 s, `then` home | HOOK → ITEM-1 when the first item is a station; the ink-world reveal | canvas camera · — |
| **P-19** | Card-to-hub morph | stage | the outgoing card's rect morphs into the hub hexagon (or a node) | `fx.morphShape` rect → hex over 0.5 s, ease inOut | CONTEXT → SM-1 items; a proof card becoming the next node | `fx.morphShape` · — |

**B-3 Giant type** (all on W-ink)

| ID | Pattern | Type | What's on screen | Motion recipe | Use | Engine block · class |
|---|---|---|---|---|---|---|
| **P-20** | Giant initial | overlay | one letter, Anton 1100 px `scaleX(0.8)`, ghost `#6F6F6F`, x 64, cap y 500-1445 | G-6: whole on the cut frame; the first letter de-blurs 8 → 0 over 3 f, later letters none | Every SM-2 part | bespoke scene (recipe below) · TC-display |
| **P-21** | Tucked word | overlay | the rest of the word, Anton ≤ 200 px uppercase `scaleX(0.8)`, ghost, at the letter's top-right | with its letter, no own motion | Every SM-2 part | same scene · TC-display |
| **P-22** | Explanation ladder | overlay | 2-4 words, Montserrat white: helpers 500 44 px, key word 700 ≤ 104 px, x 520-1004, centre y 1000 | helpers pop hard on their onsets; the key word pops at 110 % and settles in 4 f | Every SM-2 part | same scene · TC-label / TC-display |
| **P-23** | Acronym recap | overlay | "That's" Inter Tight 500 48 ink + the acronym Anton ≈ 290 px ink, centred cy 945 on W-paper | after 2 empty paper frames: "That's" fades in 4 f; letters enter as in P-24; then T-11 into the CTA | End of SM-2 | bespoke scene · TC-display |
| **P-24** | Letter line-up | overlay | "It's called" (Inter Tight 500 48 white, cy 810; each word fades in 4 f, no rise) + the initials in a row, Anton ≈ 290 px (cap ≈ 215) white, centred cy 945, gaps ≈ 0.25 em | one initial every 4 f, each a 4-5 f motion-blurred slide (alternate from the left and from below with a 6° tilt that straightens); when all are in, the gaps close over 6 f and the group scales 1.0 → 1.1 while blurring 0 → 6 px, then T-11 (v03 @ 0:04.28-0:05.16) | Bridge HOOK → SM-2 | bespoke scene · TC-display |

**B-4 Proof cards** (third-party moments: ask, then create, §12.5)

| ID | Pattern | Type | What's on screen | Motion recipe | Use | Engine block · class |
|---|---|---|---|---|---|---|
| **P-25** | Hero card | overlay | a 9:16 card 432 × 676 at x 324, y 180, radius 28, shadow `0 18px 48px rgba(0,0,0,.18)`, view chip inside bottom-left | on screen whole from f0 / the cut frame, still (v01 @ 0:00-0:02.4, 0:09.6-0:12.6); leaves on the next hard cut | HA-02 hook; SM-3 proofs | creator: `fx.clip({w: 432, h: 676, radius: 28, chip})` · created: `fx.appUI({kind: "video", caption, w: 432})` or `fx.quoteCard` (`in: "none"`) · TC-label |
| **P-26** | Large card | overlay | a 9:16 card 540 × 882 at x 282, y 468 under a CS-3 header | G-3 slide-in from the right (after a flip) or G-8 rise from below (on paper) | CONTEXT (umber), SM-1 proofs | as P-25 · TC-label |
| **P-27** | Quote card | overlay | a post read aloud: avatar initials, name, quote text 44-54 px; light card on paper / dark card on umber or ink| rise + de-blur 10 f; the quote reveals word by word (9 wps); the spoken phrase highlights | "[Name] posted / said…" | `fx.quoteCard({quote, name, theme})` · TC-label |
| **P-28** | Profile card + clip | overlay | a dark bar 920 × 194 at (80, 450): avatar Ø 140 (initials), handle 44 px, a stats row **only with creator numbers**; below it a 410 × 630 clip card at (335, 700) | the bar drops 20 px + fades in 8 f; the clip card settles 8 f, 4 f later | "[Creator] gets millions of views with this" | bespoke (`insert`, recipe `recreated_ui`) + P-32 · TC-label |
| **P-29** | Card slide-in | stage | any card entering from the right frame edge | G-3: starts 4 f after the flip; blur 12 → 0 on f0-4; 80 % of the travel in 6 f, the last ≈ 140 px as a ≈ 50 px/s drift through the hold | The first card after a world flip | bespoke `in: "none"` render: x = rest + 900·2^(−t/0.08 s) + max(0, 140 − 50·t), `filter:${ctx.blur(12 → 0, 0)}` on f0-4 · — |
| **P-30** | Proof flurry | stage | a profile bar (920 × 194) + a tilted proof card, replaced as a set | G-4: hard cut per set on its word, 0.25-0.5 s each, 3-6 sets; card tilt random −5…+5° (seeded) | A run of examples / "creators like these" | one scene per set, `in: "none"`, `cuts: [0]`, card `transform: rotate()` · — |
| **P-31** | View chip pulse | state | the eye + count chip on a card pulses once when the VO says the number | scale 1 → 1.08 → 1 over 8 f | "…6.7 million views" | inside P-25 / P-32 (`events`) · TC-label |

**B-5 Creator clips**

| ID | Pattern | Type | What's on screen | Motion recipe | Use | Engine block · class |
|---|---|---|---|---|---|---|
| **P-32** | Clip card | overlay | the creator's 9:16 clip in a card (540 × 960 at x 270, y 450 under a header, or 760 × 1350 at x 160, y 140 with no header), muted, playing at 1×, view chip | settle 8 f; push 1.00 → 1.04 over its life; exit blur 6 f | Proof for a node, a "for example" | `fx.clip({asset, radius: 28, kenburns: [1, 1.04], chip})` · TC-label |
| **P-33** | Example clip, full-bleed | overlay | the creator's clip full frame, original framing (letterbox kept), its own burned-in captions; our captions hidden | hard cut in and out (T-02) | 2.5-4.5 s, one per hub node, only for a clip the creator supplied (v02: six clips, 3.0-4.6 s) | `fx.clip({asset})` full frame · — |

**B-6 Ambient & world**

| ID | Pattern | Type | What's on screen | Motion recipe | Use | Engine block · class |
|---|---|---|---|---|---|---|
| **P-34** | Thumb field | stage | 24 rounded 9:16 tiles (150 / 190 / 230 px wide, radius 18) laid on one plane larger than the frame; the creator's own reel thumbnails, or `grid`-tone blank tiles | the plane turns ≈ 40° and pulls back 1.2 → 1.0 with strong deceleration over 3.5 s (½ of the turn in the first 0.5 s; v03 @ 0:00-0:03.6); tiles near the text dim to ≤ 0.55 and blur 6 px. Within E4 (≤ 60 px/s) use the closest recipe below | HA-12 hook only, ≤ 5 s, once per reel (E4) | bespoke z2 scene `ambient: true, exception: "E4"` (recipe below) · no text |
| **P-35** | World flip | stage | the whole ground changes paper ↔ umber ↔ ink | T-01 hard cut on a section's first frame | Section starts (§4.3) | z1 world scenes + `timeline.world` + `theme_flips` · — |

**B-7 Engine cards**

| ID | Pattern | Type | What's on screen | Motion recipe | Use | Engine block · class |
|---|---|---|---|---|---|---|
| **P-36** | Number card | figure | a card 400 × 460: a numeral (Anton 220) + a 2-word unit (Montserrat 600 56); two cards side by side at x 110 / 570, y 700; `glass` on umber / ink, `light` on paper | rise 10 f; the numeral lands on its spoken word (counter roll 12 f when > 12) | A spoken stat inside an item ("6 months", "4 apps") | `fx.card({theme, number, title, layout: "stack"})` · TC-display |
| **P-37** | Icon card | overlay | a light card 888 × 250: line icon 72 px + label 64 px + sublabel 48 px | rise 10 f; the icon draws 8 f | A concept noun with no proof ("a memory file", "a protein shake") | `fx.card({icon, title, sub, layout: "row"})` · TC-label |

**B-8 Lead magnet & brand**

| ID | Pattern | Type | What's on screen | Motion recipe | Use | Engine block · class |
|---|---|---|---|---|---|---|
| **P-38** | CTA line | overlay | `Comment "{{BV-08.keyword|KEYWORD}}"` / `and I'll send you the link.` (Montserrat 800 48, ink, cy 354 / 415); no underline | on screen whole on the cut frame, still (v01 @ 0:21.69) | CTA | bespoke scene `kind: "cta-keyword"`, `in: "none"` · TC-label |
| **P-39** | Lead card (created) | overlay | `vault` card 860 × 860 at (110, 470), radius 28: header row (icon 40 + the resource name, Inter Tight 700 44 white), 5 skeleton rows (decorative bars, two muted tag chips each), footer counts only if the creator stated them; the count line at cy 1400 | on screen whole on the CTA cut frame (with P-38 and the count line), still; no drift, no row build (v01 @ 0:21.69-0:23.8) | CTA (comment or link) | bespoke scene (recipe below) · TC-label (+ TC-decorative rows) |
| **P-40** | Lead card (creator screenshot) | overlay | the creator's screenshot of their resource in the same 860 × 860 rect (cover crop), no label | as P-39 (still) | CTA when the creator supplies it | `fx.shot({asset, x: 110, y: 470, w: 860, chrome: false})` · — |
| **P-41** | Sponsor chip | overlay | a paper pill top-left (x 64, y 140, h 64): "Paid partnership · [brand]" Inter Tight 600 28 px (`TC-legal` disclosure) | fade 8 f; holds ≥ 2 s while the sponsor is spoken | Paid integrations only (NC-12) | bespoke · TC-legal |

**Bespoke recipes (use them as written; they are sized and checked for this style):**
```js
// Shared styles for any hand-built stack (they match CS-1 / CS-2)
const PV = { sans: { slot: "display", weight: 800, size: 80, track: -0.035 },
             serif: { slot: "serif", weight: 400, size: 112, italic: true, track: -0.02 },
             cond: { slot: "numeric", weight: 400, size: 160, track: 0.01, upper: true },
             small: { slot: "display", weight: 500, size: 48, track: -0.01 } };

// HA-02 hook stack (kind title_card; captions hidden over it); the first line is serif
VEOS.fx.typeStack({ id: "hook-stack", kind: "title_card", t_in: 0, t_out: 2.5, z: 5, y: 910, anchor: "top", styles: PV,
  rise: 450, blurPx: 16, inFrames: 20, gap: 36, maxLines: 5, out: "none", keepTween: true,   // G-1: vertical smear (blurAngle default); each line finishes its own rise when the next arrives
  lines: VEOS.fx.linesFromWords(0, 2.5, { maxWords: 3 }).map((l, i) => ({ ...l, style: i % 2 ? "sans" : "serif" })) });

// P-34 thumb field (E4), closest recipe inside the 60 px/s cap: the plane turns 3° (quad-out over 3.7 s, <= 31 px/s at the corners)
// while the tiles drift slowly (<= 28 px/s); the real field turns ~40° from 1.2x, which needs a wider E4 cap (Engine gaps, completeness.md)
VEOS.scene({ id: "rain", t_in: 0, t_out: 3.7, z: 2, in: "none", out: "none", ambient: true, exception: "E4",
  items: 24, item_area: 0.022, speed_px_s: 59, dim_under_text: 0.4, box: { x: 0, y: 0, w: 1080, h: 1920 },
  render(ctx) { const rnd = ctx.rngStable("rain"), T = { y0: 860, y1: 1120 }; let h = "";
    for (let i = 0; i < 24; i++) { const d = i % 3, w = [150, 190, 230][d], hh = Math.round(w * 16 / 9), sp = [12, 20, 28][d];
      const span = 1920 + 2 * hh, x = rnd() * 1180 - 50, y0 = rnd() * span, y = ((y0 - sp * ctx.t) % span + span) % span - hh;
      const near = y + hh > T.y0 - 40 && y < T.y1 + 40, op = near ? 0.5 : [0.45, 0.7, 0.95][d];
      h += `<div data-item style="position:absolute;left:${x.toFixed(1)}px;top:${y.toFixed(1)}px;width:${w}px;height:${hh}px;`
         + `border-radius:18px;background:${ctx.col("grid")};opacity:${op};${near ? "filter:blur(6px);" : ""}`
         + `box-shadow:0 10px 30px rgba(0,0,0,.12)"></div>`; }
    const q = 1 - Math.pow(1 - ctx.clamp(ctx.t / 3.7), 2), rot = -3 * (1 - q);
    return ctx.html(`<div style="position:absolute;inset:0;transform-origin:540px 960px;transform:rotate(${rot.toFixed(2)}deg)">${h}</div>`); } });

// P-20/21/22 giant initial + tucked word + ladder (one scene per letter, W-ink)
function initialScene(id, t_in, t_out, L, rest, ladder /* [{text, at, key}] */, first /* true only for the first letter */) {
  VEOS.scene({ id, t_in, t_out, z: 5, in: "none", out: "none", cuts: [0], text: true, text_class: "TC-display",
    text_content: [L + rest, ...ladder.map(w => w.text)].join(" "), box: { x: 64, y: 500, w: 940, h: 945 },
    events: ladder.map(w => w.at - t_in),
    render(ctx, lt) {
      const sx = 0.8, op = 1, bl = first ? 8 * (1 - ctx.clamp(lt * 30 / 3)) : 0;   // G-6: whole on the cut frame
      const g = ctx.col("ghost"), Lw = ctx.measure(L, `400 1100px ${ctx.fam("numeric")}`) * 0.8, tx = 64 + Lw + 16;
      const tSize = Math.min(200, Math.floor(200 * (1004 - tx) / (ctx.measure(rest.toUpperCase(), `400 200px ${ctx.fam("numeric")}`) * 0.8)));
      const tCol = tSize >= 110 ? g : ctx.col("paper"), tp = 1;
      let lad = "", y = 0;
      for (const w of ladder) { if (ctx.t < w.at - 2 / 30) continue; const k = w.key ? 1 + 0.1 * (1 - ctx.ease.out(ctx.clamp((ctx.t - w.at + 2 / 30) * 7.5))) : 1;
        const sz = w.key ? Math.min(104, Math.floor(104 * 484 / ctx.measure(w.text, `700 104px ${ctx.fam("display")}`))) : 44;
        lad += `<div style="font:${w.key ? 700 : 500} ${sz}px/1.05 ${ctx.fam("display")};color:${ctx.col("paper")};transform:scale(${k.toFixed(3)})">${ctx.esc(w.text)}</div>`; }
      return ctx.html(`<div style="position:absolute;left:64px;top:${(500 - 0.064 * 1100).toFixed(0)}px;opacity:${op.toFixed(2)};font:400 1100px/1 ${ctx.fam("numeric")};color:${g};transform:scaleX(${sx.toFixed(3)});transform-origin:left top;${bl > 0.4 ? `filter:blur(${bl.toFixed(1)}px);` : ""}">${ctx.esc(L)}</div>`
        + `<div style="position:absolute;left:${tx.toFixed(0)}px;top:${(500 - 0.064 * tSize + 30 * (1 - tp)).toFixed(0)}px;opacity:${tp};font:400 ${tSize}px/1 ${ctx.fam("numeric")};color:${tCol};transform:scaleX(.8);transform-origin:left top;white-space:nowrap">${ctx.esc(rest.toUpperCase())}</div>`
        + `<div style="position:absolute;left:520px;width:484px;top:1000px;transform:translateY(-50%);text-align:center">${lad}</div>`);
    } });
}
```
(With the creator's own thumbnails in P-34, set each tile's `background: url(${ctx.asset(name)}) center/cover`; give the beat an `insert` record only if the thumbnails show third-party reels. Verify the giant letter's top offset (0.064 em = the gap above the cap height in an Anton line box at line-height 1, typo metrics) on the first test frame; nudge `top` so the cap top sits at y 500.)

### 8.4 Line → pattern lookup `[NICHE]`
| Line type | Primary | Alternates | `[NICHE: example]` lines |
|---|---|---|---|
| Count promise ("[N] ways / habits / posts…") | P-11 hub + P-04 title | P-15 redact list | "6 ways to hook viewers…"; "5 habits that keep fat off" |
| Myth → formula ("X isn't Y, it's a formula") | P-10 + P-06 over P-34 | P-02 | "Storytelling isn't talent…"; "Fat loss isn't willpower…" |
| "This is the [name]…" | P-25 hero card + hook stack (HA-02) | P-26 | "This is the image-to-video style"; "This is the 3-2-1 method" |
| An item of a parallel list | P-12 push-and-type (then P-13) | P-15 | "Make them curious"; "Sleep 7 hours" |
| An acronym letter | P-20 + P-21 + P-22 | — | "H, hook: make them stop scrolling"; "S, sleep" |
| A named creator / account as proof | P-28 profile card + clip | P-25 | "[Creator] gets millions of views"; "[Coach] lost 20 kg with this" |
| A post / tweet / quote read aloud | P-27 quote card | P-25 with a created quote | "[Name] wrote: '…'"; "a client messaged me…" |
| "For example" / showing an example video | P-32 clip card | P-33 (≤ 2.5 s), created clip-UI card | "look at this reel"; "watch this squat" |
| A spoken statistic | P-36 number card | P-31 view chip pulse | "6.7 million views"; "lost 8 kg in 12 weeks" |
| A concept noun with no proof | P-37 icon card | P-02 stack | "a content calendar"; "a protein target" |
| Do this, not that | P-16 contrast pair | P-02 with a `bad` strike word | "don't post daily, post better"; "don't cut carbs, cut liquid calories" |
| A process (input → step → output) | P-17 flow stations | P-15 | "idea → hook → script"; "plan → prep → portion" |
| One emphatic phrase between sections | P-08 ink punch | P-02 | "It's that simple"; "That's it" |
| A rule or chain of effects | P-05 equation | P-02 | "More loops = more views = better reach"; "More protein = more fullness = fewer snacks" |
| The whole framework again | P-14 hub recap / P-23 acronym recap | P-05 | "That's HRST"; "That's SLED" |
| CTA (comment keyword / link) | P-38 + P-39 (or P-40) | — | "Comment DATABASE…"; "Comment PLAN…" |
| Paid mention | P-41 sponsor chip + the content pattern | — | (only when sponsored) |

### 8.5 Data and truth rules
- The data-figures module is off; every number is still traced (H11): spoken, in the script, or creator-supplied. When a reel shows a number that is not spoken (a view chip, a follower count, the lead magnet's size), write `plan/figures.json` with that input `from: "creator"` so V-DATA checks it.
- Quantities are countable in the shape (N bars, N letters); comparisons use the same card size side by side (P-36 pairs, P-16).
- Illustrative created cards carry no numbers (NC-6).

### 8.6 Comedy layer
OFF (`tone.comedy = off`, `comedy_max = off`). No stickers, stamps, meme cues or freeze-frames.

### 8.7 Asset rules
- **Real captures first:** the creator's own clips, screenshots and resource screenshots, as delivered, framed by P-25 / P-26 / P-32 / P-40.
- **Created substitutes** (when the creator has none): `fx.quoteCard` (posts), a created profile card (generic, no platform UI), `fx.appUI({kind: "video", caption})` (a reel stand-in: a dark 9:16 frame with the reel's spoken hook line as its caption), `fx.logoPlate` (a product named in type), `fx.silhouette` (a person). Each is recorded in `plan/inserts.json` with `origin: "created"`.
- **Never:** platform logos, verified ticks, fetched avatars, stock footage, AI images of real people, a created card that imitates a real platform's layout pixel for pixel.
- P-34 tiles are the creator's own reel thumbnails, or blank `grid` tiles.

### 8.8 Density and variety
- An event every 0.6-1.5 s (type lines, labels, cards, moves).
- 8-14 distinct patterns and ≥ 4 families per reel; the same pattern at most 2 beats in a row, except the marker ritual (P-12/P-13 for every node, P-20/21/22 for every letter).
- ≤ 1 P-08 punch, ≤ 1 P-34 rain, ≤ 1 P-33 full-bleed clip per hub node, ≤ 6 proof cards per reel outside one P-30 flurry (≤ 6 sets).

---

## §9 Transitions `[REQ] [DNA]`

### 9.1 Library (30 fps)
| ID | Transition | Frames | Recipe | Cue role |
|---|---|---|---|---|
| **T-01** | World flip | 0 | Hard cut of the whole ground (paper ↔ umber ↔ ink) on a section's first frame; the new header / text is already on the cut frame; a card follows 4 f later (G-3 or G-8) | transition (soft hit or swish) |
| **T-02** | Proof cut | 0 | Hard cut between the hub (camera held) and a screen-pinned proof, and back | none (the card's settle carries it) |
| **T-03** | Clearing cut | 0 | hard cut that empties the frame (the stack and card vanish; 0-2 empty frames) before a new build: equation, recap (v01 @ 0:19.06, v03 @ 0:12.52) | none |
| **T-04** | Snap push | 14 | the title blurs out in place (6 f), then the C-1 snap push (`ease: "expoInOut"`, `p.snap: true`; the canvas camera's own motion blur on its middle 2-3 f) | transition (whoosh) |
| **T-05** | Zoom-through | 18 | C-4 into a node, scale 4, then cut to `then` (P-18) | transition (whoosh) |
| **T-06** | Morph hand-off | 15 | `fx.morphShape` rect → hex (P-19) | reveal (soft) |
| **T-07** | Flurry cut | 0 | G-4: hard cut to the next tilted proof set | none (the list cue may tick the first 3) |
| **T-08** | Ink punch | 0 + 0 | hard cut to black, hard cut back (P-08) | none |
| **T-09** | Letter cut | 0 | hard cut of the whole letter group; the next is whole on the cut frame (G-6) | list cue (one sound for every letter) |
| **T-10** | Hard end | 0 | the last frame ≤ 6 f after the last word; no black tail | none |
| **T-11** | Blur-push cut | 6 + 0 | the outgoing picture punches 1.0 → 1.1 and blurs over 6 f, then a hard cut: built-in `{"t": <cut>, "type": "zoom-blur", "frames": 6, "pre": 6, "punch": 0.1, "amount": 0.06, "at": "centre"}` (v03 @ 0:04.96-0:05.20 line-up → giant H; 0:13.12-0:13.60 recap → CTA) | none |
| **T-12** | Hub spin | 10 | G-9, entered by the T-02 cut back from a proof | none |

### 9.2 Grammar
| Boundary | Use | Never |
|---|---|---|
| Frame 0 | the hook's first element already moving | a fade-in from black |
| HOOK → CONTEXT | T-01 to umber | a dissolve |
| HOOK → ITEM-1 (SM-1) | T-04 snap push | a cut that loses the hub |
| HOOK → ITEM-1 (SM-2) | T-01 to ink, P-24 line-up, T-11 into the first letter | — |
| CONTEXT → ITEMS | T-01 back to paper, or T-06 card → hub morph | — |
| Node → node | T-02 cut back into the T-12 hub spin | a second push; a camera dolly |
| Node → its proof → node | T-02, T-02 | a camera move while the proof shows |
| Letter → letter | T-09 | a crossfade |
| Proof → proof | T-07 flurry cut (SM-3), or T-01 / T-03 + G-8 rise for a new section | a crossfade; a slide in the opposite direction |
| Any → RECAP | T-01 (SM-2), T-03 + P-05 (SM-3); SM-1 has none (optional C-2 pull) | — |
| RECAP → CTA | hard cut (SM-3) or T-11 (SM-2); the whole CTA is on the cut frame | an entry animation on the CTA |
| Last word | T-10 | a black tail, an outro sting |

### 9.3 Shot grammar
OFF (spine `audio`; no footage).

### 9.4 Budget (per reel, micro)
- T-01 ≤ 3; T-08 ≤ 1; T-05 ≤ 1; T-06 ≤ 1.
- T-04 once (SM-1 hook); T-09 once per letter; T-02 twice per proved node; T-12 once per node after the first; T-11 ≤ 2.
- The same transition never 3× in a row (rituals excepted: T-12 hub spins and T-09 letters).

---

## §10 Motion, camera, layers, finishing `[REQ] [DNA; motion tokens TUNE ±15%]`

### 10.1 Motion tokens (30 fps)
| Token | Value |
|---|---|
| Lead | 2 f before the onset (captions 1 f) |
| Stack line fly-in (G-1) | ≈ 450 px (420-500) from near the frame bottom, exponential out: ½ by f5, 90 % by f12, settled by f20 (≈ × 0.83 of the remaining travel per frame); motion blur 16 → 0 on f0-3; earlier lines fixed |
| Hook first line | words pop hard in place on their onsets (0 f) |
| Header line (CS-3) | hard swap, 0 f; 2-3 swaps per second |
| Word pop (titles, ladder, punch) | hard (0 f); a ladder key word 110 % → 100 % in 4 f; TITLE-MIX words fade in 4 f in final position |
| Equation element | from the right edge, 8 f expo-out (½ by f2), blur 12 → 0 on f0-3 |
| Card slide-in (G-3) | starts 4 f after the flip; blur 12 → 0 on f0-4; 80 % in 6 f; the last ≈ 140 px as a ≈ 50 px/s drift through the hold |
| Card rise-in (G-8) | from ≈ 450 px below, scale 1.12 → 1.0, 12 f expo-out, vertical blur on f0-3 |
| Card exit | none: cards leave on hard cuts |
| Card tilt (flurry) | random −5…+5°, seeded |
| Letter (G-6) | whole on the cut frame; the first letter de-blurs 8 → 0 over 3 f |
| Letter line-up | one initial every 4 f, each a 4-5 f directional smear slide (`ctx.blur(px, 0)` from the left, `ctx.blur(px, 90)` from below); gap close 6 f; T-11 built-in `zoom-blur` (punch 0.1, 6 f before the cut) |
| Typewriter | 45 cps (1.5 chars/f), caret 0.08 em wide, blinks every 15 f after typing |
| Hub build | f0 dot; hex ≈ 70 % by f4; bars every 2 f; whole hub 0.8 → 1.0 by 1.2 s, ease-out |
| C-1 snap push | 14 f (`dur: 0.47`), 1.0 → 2.3×, `ease: "expoInOut"`, `p.snap: true`: ≈ 80 % of the scale on f5-f8, the camera's motion blur there |
| Hub spin (G-9) | −360/N in 10 f, ease-out, camera held |
| Counter roll | 12 f (only numbers > 12) |
| Drift | 30-60 px over 3 s, sine (only on a held zoomed hub ≥ 2 s; never on the CTA) |
| Hold | titles ≥ 10 f after complete; text ≥ 0.25 s per word |
| Card shadow | `0 18px 48px rgba(0,0,0,.18)`; radius 28 (tiles 18) |

### 10.2 Footage camera
`zoom_policy: none` (no footage). Z-presets are not used. Creator clips may push 1.00 → 1.04 inside their card (P-32) and nothing else.

### 10.3 Canvas camera
See §21 (C-1 snap push, C-2 pull, C-3 pan / drift, C-4 zoom-through) and G-9 (hub spin, a scene rotation, not a camera move).

### 10.4 Layer order (back to front)
1. z1 world ground (`fx.ambient` paper / flat umber / ink dots)
2. z2 P-34 thumb rain; the P-08 ink-punch ground
3. z3 diagrams (hub, stations, lists), morphs
4. z4 proof cards, clip cards, engine cards, the lead card
5. z5 built text: titles, ladder, giant initials, condensed claim, CTA line
6. z6 view chips and marks that sit on cards (declared `overlaps` with their card)
7. z7 auto-captions (CS-1/2/3)
8. z8 none (avoid it: z8 hides the captions)
9. z9-11 unused (no comedy, no banner, no light passes)

Parallax: the z1 paper follows the camera at 0.7; z3-6 scenes that belong to the canvas follow at 1; **screen-pinned scenes during a held camera (proof cards, their chips) set `parallax: false`**.

### 10.5 Finishing
- No grain, no vignette, no glow, no bloom, no colour grade.
- Soft drop shadows only under cards (token above); type never has a shadow or stroke.
- Corners: cards 28, tiles 18, chips 30 (pill), hub bars 4.

---

## §11 Sound contract (minimal) `[REQ] [VAR]`
Sound comes from the bundled SFX pack and its global rules S1-S6 (every cue marks a visible event, ≤ 2 uses per file, one list-cue exception, no consecutive repeats, catalogue ids only). This style adds only:

| Line | Decision |
|---|---|
| **Cue moments** | `transitions` (world flips T-01, the first push T-04, a zoom-through T-05), `reveals` (the hub landing, the condensed claim, a proof card landing), `list_cue` (one file for every node visit or letter), `cta` (the hard cut to the CTA). The hook may carry one cue, on its reveal. Stack lines, typing and drifts are silent |
| **Meme cues** | off (comedy off) |
| **Music bed** | on, from f0: calm, minimal, ≤ 100 BPM; no drop, no riser |
| **Ducking** | the bed sits ≥ 18 dB under the VO while it speaks; creator clips play **muted** (their sound is not used; see Engine request R-1) |
| **Loudness** | −14 LUFS integrated, true peak ≤ −1.5 dBTP; hard end ≤ 6 f after the last word (NC-8) |

Mirrored in `tokens.json → sound`.

---

## §12 Inputs, inserts and fallbacks `[REQ]`

### 12.1 Setup the style assumes `[DNA]` / the buyer's setup `[VAR]`
| Item | Spec |
|---|---|
| Voice-over | one voice, a cardioid or lav mic 15-20 cm away, a quiet soft room; 48 kHz WAV (mp3 / m4a accepted); peaks around −6 dBFS; no music or effects baked in |
| Pace | 150-170 words per minute (2.5-2.8 words/s); sentences ≤ 12 words; one breath per part |
| Script shape | 45-80 words for 18-30 s: a hook line (≤ 10 words) → optional context (1 sentence) → N parts, each "[label]. [one explaining phrase]" → an optional recap ("That's [name]") → the CTA ("Comment [KEYWORD] and I'll send you [resource]") |
| No camera | nothing is filmed; no presenter footage is accepted into this format |

### 12.2 Shot list
OFF (`footage_dependency: none`). No shot is required; the optional creator files below improve proof cards.

### 12.3 Fallbacks (optional creator files → what Claude builds without them)
| Optional file | Used by | Without it, Claude builds | Fidelity cost |
|---|---|---|---|
| The creator's own reels / B-roll (9:16, ≥ 720 × 1280) | P-25, P-26, P-32, P-33 | `fx.appUI({kind: "video", caption})`: a dark 9:16 frame with the reel's spoken line as its caption | proof looks illustrative, not lived-in; holds |
| Screenshots of posts / profiles / reels the creator holds | P-27, P-28 | `fx.quoteCard` with the verbatim quote; a created profile card with initials (no stats) | no real avatar or counts; holds |
| Thumbnails of the creator's own reels | P-34 | blank `grid` tiles | the field reads as abstract; holds |
| A screenshot of the lead magnet | P-40 | P-39 created lead card (name + skeleton rows) | no real rows; holds |
| The lead magnet's real size ("1,500+ hooks") | P-39 count line | a count-free line ("The free [resource].") | weaker promise; holds |

### 12.4 Props, reaction bank, matte, resolution
- Props, reaction bank, matte: none.
- Minimum source sizes: clip cards (P-32 at 540 wide) ≥ 720 × 1280; full-bleed clips (P-33) ≥ 1080 × 1920; screenshots for P-26 / P-40 ≥ 1080 px on the long side. Smaller files are shown at a smaller card (P-25, 432 wide) or replaced by the created substitute.

### 12.5 Third-party inserts: ask, then create `[REQ]`
Claude **never fetches anyone else's media** (no web tools for media, no URLs in scenes). Per reel:
1. **Scan:** `veos inserts scan --project P` lists the moments (a post read aloud, another creator's reel, a profile, a product, a headline).
2. **Ask once**, as one short list: "For these N moments, do you have a clip or screenshot you own or hold? Drop the files, or say no." Also ask: "Your lead magnet: its exact name, its size if you want a number on screen, and a screenshot if you have one."
3. **Supplied:** `veos asset add <file> --origin creator`; shown as given (crop, frame, card), never altered to say something else; credit line `via @handle` (§19).
4. **Not supplied:** create the visual from the script's words:

| Moment | Created substitute | Pattern | Label |
|---|---|---|---|
| A post / tweet read aloud | `fx.quoteCard({quote: verbatim script words, name})` | P-27 | — |
| Another creator's reel as an example | `fx.appUI({kind: "video", caption: "[the reel's hook line, as the VO says it]"})` in the card rect | P-25 / P-26 / P-32 | — |
| A creator / account as proof | created profile card (initials avatar, name / handle only if spoken, no stats) | P-28 | — |
| A product, app or tool | `fx.logoPlate({name, kicker})` (name set in type) | P-37 alternative | none (type, not a reconstruction) |
| A person | `fx.silhouette({name, role})` | P-27 alternative | — |
| A news headline | `fx.headlineCard({masthead, date, headline: exact})` on a light card | P-27 alternative | — |

5. **Record** every moment in `plan/inserts.json`:
```json
{"version": 1, "asked": {"question": "For these 3 moments, do you have a clip or screenshot you own or hold?", "moments": ["M1", "M2", "M3"], "answer": "M2 yes (my reel), others no"},
 "creator_texts": [],
 "inserts": [
  {"id": "I1", "moment": "M1", "t0": 3.1, "t1": 5.8, "kind": "clip", "origin": "created", "recipe": "recreated_ui", "substitute_of": "example reel", "scene": "ctx-card"},
  {"id": "I2", "moment": "M2", "t0": 6.0, "t1": 8.4, "kind": "clip", "origin": "creator", "file": "my-reel-01", "credit": "via {{BV-01.handle|@yourhandle}}", "scene": "proof-2"},
  {"id": "I3", "moment": "M3", "t0": 9.0, "t1": 11.2, "kind": "post", "origin": "created", "recipe": "quote_card", "substitute_of": "post", "quote_text": "…verbatim…", "scene": "quote-3"}],
 "dismissed": []}
```

### 12.6 Frame rate and audio
1080 × 1920, 30 fps CFR. VO chain: high-pass 80 Hz, de-ess, light compression, −14 LUFS integrated, true peak ≤ −1.5 dBTP.

---

## §13 Output contract `[REQ] [DNA]`

### 13.1 Core beat fields
`id`, `section` (HOOK · CONTEXT · ITEM-n · RECAP · CTA), `t0`, `t1`, `spoken`, `trigger {word, at}`, `tone` (explain · awe · warn · win · cta), `line_type` (§8.4), `layout` (`L-canvas`), `visual` (one sentence), `layers` (scene ids), `pattern` (P-…), `sfx`.

### 13.2 Conditional fields used by this style
| Field | When |
|---|---|
| `caption {profile: CS-1 \| CS-2 \| CS-3 \| hidden, overrides[]}` | every beat |
| `camera_canvas {move: C-1…C-5, to, frames}` | every beat with a canvas move |
| `theme` | the first beat of a section that flips (also written in `timeline.theme_flips`) |
| `morph_in`, `morph_out` | P-19 hand-offs |
| `insert {id, origin: creator \| created}` | every third-party moment (P-25…P-28, P-32, P-33) |
| `source {masthead, date, headline}`, `credit` | a created headline card; credit on creator-supplied clips |
| `exception: "E4"` | the P-34 beat |
| `sponsor {id, disclosure}` | a paid mention |

Example beat:
```yaml
- id: 4
  section: ITEM-1
  t0: 2.60
  t1: 5.60
  spoken: "One: give them a checklist they can tick off"
  trigger: {word: "checklist", at: 3.32}
  tone: explain
  line_type: list_item
  layout: L-canvas
  pattern: P-12
  visual: "Camera pushes into the top bar of the 5-node hub (C-1, 2.3x); the bar types 'Give a checklist'; hard cut to a light icon card 'a checklist they tick' with the header line above"
  layers: [paper, hub-a, card-check]
  caption: {profile: CS-3}
  camera_canvas: {move: C-1, to: {node: n1, fill: 0.7}, frames: 24}
  sfx: [{id: "<list-cue id>", t: 2.62, on: "camera@2.62", why: "item 1 visit"}]
```

### 13.3 Reel header (top of the edit brief)
```yaml
format: F-A
theme: TH-paper                    # the opening pack; flips listed below
theme_flips: [{t: 3.10, theme: TH-ink}, {t: 14.00, theme: TH-paper}]
hook_archetype: HA-06              # HA-06 | HA-12 | HA-02
structure: framework
marker: SM-1                       # SM-1 hub | SM-2 ladder | SM-3 proof stack
framework: {name: "5 ways to get more saves", parts: ["Give a checklist", "Number your slides", "End on a summary", "Teach one thing", "Make a cheat sheet"]}
count: 5
keyword: "{{BV-08.keyword|KEYWORD}}"
lead_magnet: {name: "[resource]", size: "[creator-stated or null]", screenshot: false}
inserts: {asked: true, creator: 1, created: 2}
```
The timeline skeleton every reel of this style starts from:
```json
{"meta": {"playbook": "<this playbook>", "format": "F-A", "theme": "TH-paper", "hook_archetype": "HA-06", "keyword": "KEYWORD", "count": 5},
 "stage": [{"t": 0, "layout": "L-canvas"}],
 "world": [{"t": 0, "world": "W-paper"}],
 "theme_flips": [],
 "canvas_nodes": {"hub": {"x": 380, "y": 800, "w": 320, "h": 320}},
 "canvas_camera": [],
 "captions": {"subtitles": "auto", "hide": [[0, 2.6]], "overrides": [{"t": [2.6, 17.8], "profile": "CS-3"}]},
 "transitions": [], "sfx": [], "audio": {"bed": "<pack id>", "bed_db": -22, "dropouts": []}}
```

### 13.4 Hook proposals (3)
```yaml
- name: "Hub of 5"
  archetype: HA-06
  headline: "5 ways to get more saves _on every post_"
  hook_pair: {type: promise_to_proof, promise: "5 ways", proof: "5-node hub, one proof per node"}
  stoppers: [hub dot growing at f0, title word-append, 5 bar pops, push at 2.2 s]
  captions: hidden in the hook (title carries the words), CS-3 from the push
  storyboard: "f0 dot + '5' rising | 0.1-0.4 hex + 5 bars | 0.2-1.1 title line 1 | 1.1-1.5 serif tail | 2.2 C-1 push to n1, 'Give a checklist' types"
  sound: [reveal cue on the hub landing, list cue at the push]
  stopper_test: {thumbnail: pass, mute: pass, sc_0_3s: 13, payoff_s: 1.0}
```

### 13.5 Checkpoint (before building)
Send:
1. The framework extraction (name, shape SM-…, parts ≤ 18 chars) and the 3 hooks with stopper results.
2. The beat sheet with tones, patterns, caption profiles, theme flips, and the canvas plan (nodes + moves).
3. The transition map and the cue list (SFX pack ids, ≤ 2 uses per file, one list cue).
4. The inserts record (asked / creator / created) and the substitutes used.
5. The lead magnet: name, stated size, screenshot or created card.
6. Style stills: f0, 1.0 s (the cover), the first node visit or letter, one proof card, the recap, the CTA.

**Wait for approval.**

---

## §14 Worked examples `[REQ] [NICHE]`
Times are planning estimates; replace them with `words.edit.json` onsets.

### 14.1 SM-1 hub tour, HA-06 (content & marketing; keyword SAVES; 23.8 s)
**VO:** "Five ways to get more saves on every post. One: give them a checklist. Two: number your slides. Three: end on a summary slide. Four: teach one thing, not five. Five: make it look like a cheat sheet. That's how saves pile up. Comment SAVES and I'll send you my twenty post templates."
**Inserts asked:** the creator supplies 2 of their own carousel screenshots (items 3 and 5); nothing else.

Hook table:
| t (s) | On screen | Captions | Camera |
|---|---|---|---|
| 0.00 | W-paper; hub dot growing at (540, 960); "**5**" rising at cy 330 | hidden | home |
| 0.10-0.30 | hex r 160; 5 bars pop (angles −90°, −18°, 54°, 126°, 198°; centres (540, 630), (854, 858), (734, 1227), (346, 1227), (226, 858)) | — | home |
| 0.20-1.30 | "**5** ways to get more **saves**" word by word | — | home |
| 1.00 | hub count "5" + "ways" | — | — |
| 1.30-1.70 | line 2 "_on every post_" (ghost tail 40 % → 100 %) | — | — |
| 1.70-2.40 | hold (the hub's last growth) | — | home |
| 2.40-2.90 | title blurs out (6 f); C-1 snap push to n1 (2.3×, 15 f); n1 types "Give a checklist" at 45 cps from 2.75 | CS-3 from 2.6 | C-1 |

Section plan:
| Section | t (s) | Spoken (gist) | Patterns | World | Camera | Captions |
|---|---|---|---|---|---|---|
| HOOK | 0.0-2.6 | "Five ways… every post" | P-04, P-11, P-09 | paper | home → drift | hidden |
| ITEM-1 | 2.6-5.6 | "give them a checklist" | P-12 → T-02 → P-37 icon card "a checklist they tick" (list icon) → T-02 back | paper | C-1 n1 | CS-3 |
| ITEM-2 | 5.6-8.4 | "number your slides" | T-02 back into the P-13 hub spin → label "Number your slides"; no proof: header line over the zoomed hub + drift | paper | held (spin) | CS-3 |
| ITEM-3 | 8.4-11.4 | "end on a summary slide" | P-13 → label → T-02 → **P-26** the creator's summary-slide screenshot (credit `via {{BV-01.handle|@yourhandle}}`) → T-02 | paper | held (spin) | CS-3 |
| ITEM-4 | 11.4-14.4 | "teach one thing, not five" | P-13 → label → T-02 → **P-16** contrast pair: "5 tips" (`bad` strike) / "1 tip" (`good` ✓) → T-02 | paper | held (spin) | CS-3 |
| ITEM-5 | 14.4-17.8 | "make it look like a cheat sheet" | P-13 → label → T-02 → **P-26** the creator's cheat-sheet screenshot → T-02 | paper | held (spin) | CS-3 |
| RECAP | 17.8-19.8 | "That's how saves pile up" | **P-14** (optional) pull to home, all 5 labels | paper | C-2 | CS-3 |
| CTA | 19.8-23.8 | "Comment SAVES… twenty post templates" | hard cut to **P-38** `Comment "SAVES"` + **P-39** lead card "20 post templates" (creator-stated) + count line "20 post templates you can copy.", all still | paper | home | hidden |

Canvas plan: `canvas_nodes` = the hub + n1…n5 (bar rects 230 × 40 centred on the points above); pushes `fill: 0.7`, `keep: []`; every move ≥ 0.6 s; ≥ 0.4 s between moves. Cues: reveal (hub, 0.3 s), list cue × 5 (each visit), CTA (the cut). Flips: none (SM-1 reels may stay on paper).

### 14.2 SM-2 initial ladder, HA-12 (fitness & nutrition; keyword PLAN; 19.6 s)
**VO:** "Fat loss isn't willpower. It's a four-letter formula coaches use. It's called SLED. S: sleep seven hours. L: lift three times a week. E: eat protein first. D: daily steps, eight thousand. That's SLED. Comment PLAN and I'll send you the free four-week SLED plan."
**Inserts:** none (no third-party moment). Thumb rain with blank tiles.

Hook table:
| t (s) | On screen | Captions |
|---|---|---|
| 0.00 | W-paper + P-34 rain (blank tiles); "Fat" rising at cy 950 | hidden |
| 0.10-1.20 | "Fat loss isn't _willpower._" appends (P-10) | — |
| 1.20-1.40 | clear; "It's a" (48 `mute`) at y 880 | — |
| 1.60 | "**4-LETTER FORMULA**" Anton 160 `mute` rises (P-06) | — |
| 2.30-2.90 | "coaches _use_" appends at cy 1070 | — |
| 2.90-3.10 | hold | — |

Section plan:
| Section | t (s) | Spoken | Patterns | World / theme | Captions |
|---|---|---|---|---|---|
| HOOK | 0.0-3.1 | "Fat loss… coaches use" | P-34, P-10, P-06 | paper | hidden |
| CONTEXT | 3.1-4.4 | "It's called SLED" | **T-01 flip** → P-24 line-up "It's called S L E D" (initials slide every 4 f) | **ink** (`theme_flips` 3.10 TH-ink) | hidden (the line-up carries it) |
| ITEM-1 | 4.4-6.6 | "S: sleep seven hours" | T-09 → P-20 "S" + P-21 "LEEP" + P-22 "sleep / **7 hours**" | ink | hidden |
| ITEM-2 | 6.6-9.0 | "L: lift three times a week" | T-09 → "L" + "IFT" + "three times / **a week**" | ink | hidden |
| ITEM-3 | 9.0-11.2 | "E: eat protein first" | T-09 → "E" + "AT" + "eat / **protein** / first" | ink | hidden |
| ITEM-4 | 11.2-14.0 | "D: daily steps, eight thousand" | T-09 → "D" + "AILY" + "steps / **8,000**" | ink | hidden |
| RECAP | 14.0-15.6 | "That's SLED" | **T-01 flip** → P-23 "That's" + "SLED" Anton 300 ink | **paper** (`theme_flips` 14.00 TH-paper) | hidden |
| CTA | 15.6-19.6 | "Comment PLAN… four-week SLED plan" | P-38 `Comment "PLAN"`; P-39 lead card "The 4-week SLED plan"; count line "The free 4-week SLED plan." | paper | hidden |

Flips: 2 (3.10, 14.00; 10.9 s apart). Rain 0-3.1 s (E4 ≤ 5 s). Intro cap: 3.1 / 19.6 = 15.8 % → **trim**: end HOOK at 2.9 s (payoff 1.6 s + 10 f + "coaches use" moved into CONTEXT's first 0.2 s), giving 14.8 %. Cues: reveal (claim, 1.6 s), transition (3.1 flip), list cue × 4 (letters), CTA.

### 14.3 SM-3 proof stack, HA-02 (content & marketing; keyword CAROUSEL; 21.0 s)
**VO:** "This is the carousel-to-reel style of content. It's one of the easiest formats to make, and it still gets views. You take a carousel you already posted, turn every slide into a two-second scene, and add your voice. It's that simple. More slides, more watch time, more reach. Comment CAROUSEL and I'll send you the template."
**Inserts asked:** the creator supplies 2 of their own carousel-to-reel videos and states one has "1.2M views".

| Section | t (s) | Spoken | Patterns | World | Captions |
|---|---|---|---|---|---|
| HOOK | 0.0-2.5 | "This is the carousel-to-reel style of content" | **P-25** hero card = the creator's reel 1 (`fx.clip`, chip "1.2M" from the creator → figures.json `from: creator`); **P-07** arrow; hook stack "_This is the_ / **carousel** / _to reel_ / **style** / _of content_" (title_card, first line serif) | paper | hidden |
| CONTEXT | 2.5-6.2 | "one of the easiest formats… still gets views" | **T-01 flip** → CS-3 header (white) + **P-29** reel 2 slides in as a **P-26** large card; **P-31** chip pulse on "views" | **umber** (`theme_flips` 2.50 TH-umber) | CS-3 |
| ITEM-1 | 6.2-9.4 | "take a carousel you already posted" | **T-01 flip** → P-25 hero card: a created carousel card (`fx.card` light, 3 stacked slide tiles, icon "grid") ; CS-1 stack below | **paper** (`theme_flips` 6.20 TH-paper) | CS-1 |
| ITEM-2 | 9.4-12.4 | "turn every slide into a two-second scene" | **G-8** rise-in → created clip-UI card (`fx.appUI({kind: "video", caption: "slide 1 · 2 s"})`); stack rebuilds | paper | CS-1 |
| ITEM-3 | 12.4-14.6 | "and add your voice" | hard cut + G-8 → **P-37** icon card "mic" "your voice-over" in the hero rect | paper | CS-1 |
| (punch) | 14.6-15.4 | "It's that simple" | **P-08** ink punch "_It's that_ / _simple._" (z2, not a theme flip) | paper (black card) | hidden |
| RECAP | 15.4-17.6 | "more slides, more watch time, more reach" | **P-05** equation "_More slides_ / = / _More watch time_ / = / _More reach._" (overrides: "," → "=") | paper | CS-2 |
| CTA | 17.6-21.0 | "Comment CAROUSEL… the template" | P-38 `Comment "CAROUSEL"`; **P-40** the creator's template screenshot (supplied) or P-39; count line "The carousel-to-reel template." | paper | hidden |

Flips: 2.50 (umber), 6.20 (paper): 3.7 s apart (≥ 3.0). The punch is a z2 scene, so V-THEME sees no flip. Inserts: I1 reel 1 (creator), I2 reel 2 (creator, credit), I3 the created clip-UI card (`recreated_ui`, substitute_of "a reel made from a carousel").

---

## §15 QA checklist `[REQ] [DNA]`

**1. Profile conformance**
- [ ] Format F-A; `stage` `L-canvas` (hidden) for the whole reel; no presenter anywhere (V-PROFILE, review).
- [ ] Duration 18-30 s (or the TUNEd `short` range); themes only TH-paper / TH-umber / TH-ink; the reel opens and closes on paper (V-THEME).

**2. Hook**
- [ ] f0: the archetype's elements present and moving (HA-06: `title_card` + `diagram`; HA-12: live motion + a text beat by 0.7 s; HA-02: `title_card` + proof) (V-F0).
- [ ] ≥ 8 weighted SCs in 0-3 s; the shape readable by 2.5 s (3.0 s HA-12) (V-CADENCE, V-F0).
- [ ] Title ≤ 10 words, ≤ 5 lines, count = parts shown, holds ≥ 10 f (V-TITLE, V-PROMISE).
- [ ] HOOK ≤ 15 % of runtime (V-REHOOK).

**3. Body and cadence**
- [ ] 6-16 SC per 10 s; no weight-1 gap > 1.5 s; nothing static > 2.0 s (V-CADENCE).
- [ ] One marker shape; the same ritual for every node or letter; every node typed and visited (review, V-PROMISE).
- [ ] Camera moves ≥ 0.5 s, eased, ≥ 0.4 s apart; moved text ≥ 40 px at its zoom; nothing zoomed into the caption band while captions show (V-CANVAS).
- [ ] World flips ≤ 3, ≥ 3.0 s apart, on section starts, written in `theme_flips` and `world` (V-THEME).

**4. Captions**
- [ ] Every spoken phrase on screen, once: auto-caption (CS-1/2/3) or a built text scene, never both (V-CAPTION, review).
- [ ] The stack alternates sans / serif, ≤ 5 lines, ≤ 3 words and ≤ 16 chars per line; header lines ≤ 3 words (V-CAPTION).
- [ ] Ink on paper, white on umber / ink; sizes ≥ floors (sans 80, serif 112, header 76) (V-TYPE).
- [ ] Glossary spellings exact (V-CAPTION).

**5. Modules**
- [ ] §21: canvas nodes declared; pushes framed with `fill` 0.6-0.8; recap pull-out shows every label (V-CANVAS).
- [ ] §23: the hub returns at the same framing after each proof; morphs only at P-19 points (V-CONTINUITY when available, else review).
- [ ] §25: lead card ≤ 4.0 s; keyword readable ≥ 1.5 s; no black tail > 0.2 s (V-PROMISE).
- [ ] E4: the rain ≤ 5 s, no text in it, ≤ 60 px/s, dimmed under the text (V-EXC).

**6. Truth and inserts**
- [ ] Every number spoken, scripted or creator-stated (and in `figures.json` when not spoken) (V-NUMFMT, V-DATA, review).
- [ ] `plan/inserts.json` complete: asked once, every moment creator or created, quotes verbatim (V-INSERTS, NC-13).
- [ ] No platform logos, ticks or look-alike UIs; no fetched media (NC-7, review).

**7. Sound contract**
- [ ] Cues only on transitions, reveals, the list cue and the CTA; one file for the list cue; ≤ 2 uses per other file (S1-S6).
- [ ] Bed from f0, ≥ 18 dB under the VO; creator clips muted; −14 LUFS, true peak ≤ −1.5 dBTP (qa).

**8. End and export**
- [ ] Hard end ≤ 6 f after the last word; 1080 × 1920, 30 fps CFR (qa).

---

## Conditional modules (§16-§25)

### §16 Frame template / persistent chrome
OFF (`profile.modules.chrome = false`): nothing persists across the reel; every section rebuilds its own frame.

### §17 Running state & anchored graphics
OFF (`modules.running_state = false`, `modules.anchors = false`): no counters carried across cuts, nothing tracks footage.

### §18 Data contract
OFF (`modules.data_figures = false`): the style shows few numbers. Any number not spoken (a view chip, a follower count, the lead magnet's size) still goes into `plan/figures.json` with `from: "creator"` (§8.5), which switches V-DATA on for that reel.

### §19 Evidence & citations `[COND: modules.citations] [DNA]`
- **Credit line** (`citations.credit_line`): `via @handle` in Inter Tight 500, 24 px (`TC-legal`), ink at 72 % on paper / paper at 72 % on umber and ink, left-aligned with the card's left edge, 8 px under the card (hero card: x 324, y 864; large card: x 270, y 1418), fading in with the card. Optional: use it when the creator wants a source shown; nothing requires it.
- **Source card:** none by default. If the VO quotes a news headline, use `fx.headlineCard({masthead, date, headline})` on a light card at x 90, y 450, exact headline; the beat carries `source {masthead, date, headline}`.
- **Figure numbering, verdict stamps, plates:** none.
- **Rules:** quotes verbatim (NC-13); one card per claim; claims the creator can't support are flagged at the checkpoint.
- **Validator:** V-CITE (credit lines on creator records, labels on synthetic scenes), V-INSERTS.

### §20 Dialogue
OFF (`modules.dialogue = false`): one voice.

### §21 Canvas camera `[COND: modules.canvas_camera] [DNA]`
The camera moves over the graphics world (z1-6), never over captions (z7) or screen-pinned proof scenes (`parallax: false`). It looks at world point (x, y) at zoom s; home = (540, 960, 1).

| ID | Move (timeline `move`) | Scale | Frames | Ease | Use in this style |
|---|---|---|---|---|---|
| **C-1** | `push` to a node (snap) | 1.0 → 2.3 (`fill: 0.7`) | **14** (`dur: 0.47`, `p.snap: true`: the evidence settles in 13-14 f with ≈ 80 % of the scale in 3 f; expoInOut over 14 f peaks at ≈ 33 % per frame, inside V-CANVAS's 35 % snap allowance) | **expoInOut** (snap); inOut for the others | the first node visit (P-12, the one snap of the reel: never two snaps in a row); a station's key node (P-17, `dur` 0.5, `inOut`, no snap); the hub growth at f0-1.2 s as `push` 0.8 → 1.0, `ease: out` |
| **C-2** | `pull` / `settle` | → 1.0 | 18 (12-21) | inOut | the hub recap (P-14); leaving a station |
| **C-3** | `dolly` node → node; `pan`; `drift` | keeps the zoom; dolly `arc: 0.10` | dolly 30, pan 24, drift 90 | inOut (drift sine) | list rows (P-15); a held zoomed hub ≥ 2 s (drift 30-60 px); node → node only as the fallback for the G-9 spin |
| **C-4** | `zoom-through` | × 4 into the node, then `then` | 18 | in | the HOOK → stations hand-off (P-18), ≤ 1 per reel |
| **C-5** | `orbit` | radius 40 px, 2° roll, returns | 60 | sine | not in evidence; avoid |

Hub geometry (world px = screen px at home), for N parts (3 ≤ N ≤ 8):
- hub `{x: 380, y: 800, w: 320, h: 320}` (hex r 160, centre 540, 960);
- node k (k = 0…N−1) centre = (540 + 330·cos θk, 960 + 330·sin θk), θk = −90° + k·360°/N; bar rect `{x: cx − 115, y: cy − 20, w: 230, h: 40}`;
- **Button band clear (n3):** a node on the right whose rect (the 230 px bar, or its typed label if wider: ≈ 22 px per character at 40 px) has any part in y 1100–1700 slides left until its right edge is ≤ 960 at full hub size (left of the IG button column at x 970). For N = 6 that is n3 (k = 2, θ 30°): centre (826, 1125) → (≤ 760, 1125) with an 18-character label; its leader line ends at the moved bar. The hex, the other nodes and the 330 px ring stay as measured (also N = 3 k = 1, N = 8 k = 3);
- labels ≤ 18 characters at 40 px world (Inter Tight 600), centred on the bar.

Rules:
- Text the camera moves is ≥ its floor at zoom 1 (node labels 40 px, hub count 120 / 40 px); at 2.4× labels read at 96 px.
- Never two moves within 0.4 s; every move ≥ 0.5 s; zoom 1.0-4.0 only (5.0 inside C-4).
- During a held zoom, the caption band (header y 270-400) stays clear: push targets are framed with `fill` 0.6-0.8 so the node sits at y ≥ 560 on screen.
- The paper world follows the camera at 0.7 (`fx.ambient follow: 0.7`) for depth; umber and ink grounds don't move.
- **Validator V-CANVAS:** known moves, ≥ 0.5 s (0.25 s for the single `p.snap` push), eased, ≥ 0.4 s gaps, travel ≤ 110 px and zoom ≤ 12 % per frame (snap: 220 px and 35 %), text floors after zoom.

### §22 Ink & annotation layer
OFF (`modules.ink = false`). The only drawn mark is the P-07 arrow (part of the hook stack) and the P-16 strike, both specified in §8.

### §23 Continuity `[COND: modules.continuity] [DNA]`
- **Motif `M-hub`:** the hexagon hub (r 160, `hub` fill). States: `dot` (f0, r 12) → `skeleton` (bars redacted) → `labelled` (bars typed) → `visited` (the active node's end dot in `primary`, the rest at 40 %) → `recap` (all labels, none active). In SM-2 and SM-3 reels the motif is absent (H15: one shape per reel).
- **Recurring diagram:** after every proof the hub returns at exactly the framing it left (the camera never moves while a proof shows), so the viewer re-enters the same map.
- **Morph hand-offs** (P-19, `fx.morphShape`, 0.5 s): a CONTEXT card → the hub hexagon; a proof card → the next station's first node. At most 1 per reel. Other section boundaries are hard cuts (T-01, T-02): `morph_required: false`.
- **Bookend:** none.
- **Validator V-CONTINUITY** (pending in the engine; checked by review until it ships): every declared `morph_in` / `morph_out` has its morph scene; the hub motif is present in every SM-1 item beat.

### §24 Series furniture
OFF (`modules.series = false`; a buyer may turn it on as a VAR, then the series tag is a TC-legal line top-left at y 140, 24 px).

### §25 Lead-magnet end card and sponsor chip `[COND: modules.brand, cta ∋ end_card] [DNA look; VAR assets]`
**Lead-magnet card (P-39)**, the last 3.0-4.0 s, W-paper:

| Element | Spec |
|---|---|
| CTA line (P-38) | cy 354 / 415, two lines centred, Montserrat 800 48 px ink: `Comment "{{BV-08.keyword|KEYWORD}}"` / `and I'll send you the link.` (link_bio: `Free [resource]` / `link in bio`). No underline. Scene `kind: "cta-keyword"`, `text_content` includes the keyword |
| Card | x 110-970, y 470-1330 (860 × 860), radius 28, `vault` `#111111`, shadow `0 18px 48px rgba(0,0,0,.18)`; on screen whole on the CTA cut frame with the CTA line and count line (v01 @ 0:21.69) |
| Header row | y +40 inside: a 40 px line icon (`fx.icon("list")` or "grid") in `accent` + the resource name, Inter Tight 700 44 px paper ("The [resource]") |
| Rows | 5 rows, 120 px pitch from y +140: a skeleton title bar (rgba(255,255,255,.14), 60 % width, 16 px tall), a second bar (35 %), two muted tag chips (`#2A2A2A`, 28 px tall, rgba(255,255,255,.55) 24 px text only if the creator gave category names, else empty); rows all present; `data-tc="TC-decorative"` |
| Footer | inside, y +760: counts only if creator-stated ("1,500+ hooks · 15 niches"), Inter Tight 600 40 px paper; otherwise omitted |
| Count line | cy 1400 under the card: Montserrat 800 48 px ink, one sentence ending in a full stop ("1,500+ viral hooks with links." / "The free 4-week SLED plan.") |
| Motion during the hold | none (v01 dead still 2.05 s); only CS-3 header swaps may run over it (v03) |
| With the creator's screenshot | P-40: `fx.shot({asset, x: 110, y: 470, w: 860, chrome: false})`, no label, still |

Rules: card on screen ≤ 4.0 s (`brand.endcard.max_s`); the keyword readable ≥ 1.5 s; no outro sting; the last frame ≤ 6 f after the last word; no black tail.

**Sponsor chip (P-41):** a paper pill top-left (x 64, y 140, h 64, radius 32): the disclosure wording (BV-14, default "Paid partnership") + " · [brand]" in Inter Tight 600 28 px ink (`TC-legal`), held ≥ 2.0 s while the sponsor is spoken; the sponsor's own logo only if the buyer supplies it, never fetched (NC-12, NC-7).

---

## Part C. Declared exceptions and the non-overridable core

### C.1 Non-overridable core
NC-1…NC-14 apply unchanged (STYLE-PLAYBOOK-STRUCTURE Part C.1). The ones this style touches most: **NC-4** legibility (ghost grey only ≥ 96 px; labels ≥ 40 px even after camera zoom-out), **NC-5** IG bands (the CTA count line at cy 1400, never below 1500), **NC-6** truth (created cards carry no numbers), **NC-7** creator-owned media only, **NC-13** quote integrity (quote cards verbatim).

### C.2 Exceptions used
| E-id | Token | Limits | Scenes that use it |
|---|---|---|---|
| **E4** ambient field | `exceptions.E4 = {max_items: 30, max_item_area: 0.12, max_speed_px_s: 60, dim_under_text: 0.4, max_s: 5}` | the P-34 recipe: 24 tiles, ≤ 2.2 % area each, ≤ 56 px/s, ≤ 5 s, dimmed near text | the P-34 scene only (`exception: "E4"`, `ambient: true`, z2) |

Not used: E1 (no presenter), E2 (no chaos), E3 (no small type), E5 (blocked by PV-9 in faceless profiles; see Part E), E6 (captions rise, they don't hard-swap).

### C.3 Buyer changes to exceptions
A buyer may switch E4 off (VAR): HA-12 then opens on plain paper with the thesis only. Adding an exception is a DNA change (DV-n).

---

## Part D. Personalisation

### D.1 Asked at setup (one round, each with "keep the template default")
| BV | Question | Lands on |
|---|---|---|
| BV-01 | Your name and handle | `creator.name`, `creator.handle`; credit lines on your own clips (`via @handle`) |
| BV-02 | One or two brand colours | `roles.primary` (the signal on paper) and `roles.accent` (the signal on dark), contrast-nudged (primary must read ≥ 4.5:1 on `#E2E1DC`; accent ≥ 4.5:1 on `#141414`). The worlds stay paper / umber / ink (per-section packs keep their grounds) |
| BV-05 | Language you speak and caption language | `profile.language`, always asked: **English** → English captions (default) · **Hinglish** → romanised Hinglish captions · **Hindi** → Devanagari captions; numbers follow (BV-06). |
| BV-08 | Call to action | `comment_keyword` + your keyword (default) or `link_bio` + your resource name; the lead card is always on |

### D.2 Defaulted, changeable later
| BV | Variable | Default |
|---|---|---|
| BV-03 | Fonts | Montserrat / Instrument Serif / Anton / Inter Tight, swappable inside each slot's class (§5.1) |
| BV-04 | Niche and topics | inferred per reel |
| BV-06 | Numbers | international + `$` + k_m_b; Indian grouping + ₹ + lakh/crore for Hinglish / Hindi |
| BV-07 | Captions full / keywords / off | not offered: captions `full` are DNA |
| BV-09 | Formats | F-A (the only one); marker shapes SM-1 / SM-2 / SM-3 are picked per reel |
| BV-10 | Ground colours | TUNE within the ranges in `locks` (paper L 0.88-0.95; umber L 0.25-0.35; ink L 0.15-0.22) |
| BV-11 | Humour | off (the template's maximum) |
| BV-13 | Series | off |
| BV-14 | Sponsor disclosure wording | "Paid partnership" |
| BV-15 | Never-on-screen list | empty |
| BV-16 | Logo / wordmark | none (the lead card's header uses the resource name in type) |
| BV-17 | Duration | 18-30 s (TUNE to `short`, up to 45 s, for 6-8-node hubs) |

### D.3 Lock summary
| Area | Lock |
|---|---|
| Header DNA, D1-D8, §1, §2, §9, §13, §15 | DNA |
| Source, presence, spine, captions mode/role, graphics, footage dependency, theme policy and packs, format set, CTA device set | DNA |
| Duration class / target | TUNE (micro ↔ short; 15-45 s) |
| Language, numbers, chosen CTA, keyword, primary / accent hex | VAR |
| Ground hexes, ink, ghost, mute | TUNE (ranges in `locks`) |
| Font families | TUNE inside the slot class |
| Caption mechanics (unit, chunking, swap, stack, alternation) / sizes and y | DNA / TUNE (ranges in `locks`) |
| Motion tokens, cadence, budgets, camera frames and scales | TUNE ±15 % |
| §6.4 hook pairs, §8.4 lookup, §14, App. A, glossary | NICHE |
| Bad / good roles, IG bands, loudness, inserts.fetch | NC |

### D.4 NICHE slots, filled per reel
- §6.4: the reel's hook pair is appended at P7.
- §8.4: new line types are mapped to existing patterns at P5 (≤ 10 niche patterns over time, from families B-1…B-8).
- §14: after the first approved reel of each marker shape, it becomes that shape's worked example.
- App. A: approved titles are appended.
- Glossary: confirmed names and terms are added.

---

## Part E. Changes and deviations (template v1, 2026-10-06, draft)
Decisions that differ from `STYLE-COVERAGE.md` or from the raw evidence, and why:

| # | What | Evidence / coverage said | This template does | Why |
|---|---|---|---|---|
| E-1 | Body cadence | 6-10 SC/10 s | 6-16 | primary captions weigh 1.0; v01 3-12 s measures ≈ 14 |
| E-2 | Hook alternates | HA-06 (HA-12) | HA-06 (HA-12, **HA-02**) | v01's hook is a proof card at f0 + a stack: that is HA-02's f0 (headline + proof) |
| E-3 | World-flip spacing | §0.5: ≤ 1 per 5 s | ≥ 3.0 s apart (V-THEME `min_gap_s: 3.0`) | v01 flips at 2.5 s and 5.8 s (3.3 s apart) |
| E-4 | The 1 s black beat | v01 @ 0:13 (a flip to black and back in 1 s) | P-08 ink punch: a z2 scene, not a theme flip | keeps V-THEME's spacing honest while keeping the beat |
| E-5 | Giant initials | v03: the letter touches the left frame edge | x 64 margin, `scaleX(0.8)` Anton | E5 edge bleed is blocked by PV-9 for faceless profiles (Engine request R-3) |
| E-6 | Hub labels | v02: ≈ 20 px labels read only at 2.4× | 40 px world labels (88-96 px at 2.2-2.4×) | NC-4 / V-CANVAS: text visible at zoom 1 must meet its floor |
| E-7 | Hub centre text | v02: the whole title tiny inside the hex | count numeral + one noun | the same floor rule |
| E-8 | Example clips | v02: full-bleed third-party reels with their sound, 3.5-6 s | creator clips in cards, muted; full-bleed ≤ 2.5 s | creator-owned media only; no clip-audio support (R-1) |
| E-9 | Reference cards | real tweets / profiles / reels | the creator's files or created cards | NC-7 ask-then-create |
| E-10 | Accent | no owned accent | one brandable signal (primary / accent) on one element | buyers need a brand colour; kept to one job so the monochrome DNA survives |

Version log: v1 (2026-10-06) first draft. v1.1 (2026-10-07) engine built-ins: C-1 snap push (`expoInOut` + `p.snap`, 14 f), directional smears (`ctx.blur(px, angle)`), `typeStack({keepTween: true})`, T-11 as the built-in `zoom-blur` transition; G-9 hub spin and the P-34 thumb-field turn stay bespoke (see `evidence.md`).

---

## Part F. IDs used in this playbook
| Prefix | IDs |
|---|---|
| D | D1-D8 |
| H / N | H1-H17 / N1-N12 |
| E | E4 |
| W / L / G | W-paper, W-umber, W-ink / L-canvas / G-1…G-7 |
| TH | TH-paper, TH-umber, TH-ink |
| CS | CS-1 stack low, CS-2 stack centre, CS-3 header line |
| HA / ST | HA-06 (default), HA-12, HA-02 / ST-1, ST-2, ST-3, ST-5, ST-6 |
| SM | SM-1 hub tour, SM-2 initial ladder, SM-3 proof stack |
| P / B | P-01…P-41 / B-1…B-8 |
| T | T-01…T-10 |
| C | C-1…C-5 |
| F | F-A |
| BV | BV-01…BV-17 (Part D) |
| V | V-PROFILE, V-F0, V-CADENCE, V-ONWORD, V-SAFE, V-CAPTION, V-TYPE, V-EXC, V-HUES, V-TITLE, V-PROMISE, V-LAYOUT, V-THEME, V-REHOOK, V-CANVAS, V-INSERTS, V-CITE, V-CONTINUITY, V-NUMFMT |

---

## App. A Headline & hook bank `[NICHE]`
Ten titles in the style's voice; `[slots]` are filled per reel. The count always equals the parts shown.

| # | Title (serif tail in _italics_) | Archetype · shape |
|---|---|---|
| 1 | "[N] ways to [get result] _in [time / place]_" | HA-06 · SM-1 |
| 2 | "[N] [habits / posts / rules] that _[outcome]_" | HA-06 · SM-1 |
| 3 | "[N] mistakes that _kill your [metric]_" | HA-06 · SM-1 |
| 4 | "[Topic] isn't _[myth]._ It's a [N]-LETTER FORMULA" | HA-12 · SM-2 |
| 5 | "Every [good result] follows _one formula_" → "It's called [ACRONYM]" | HA-12 · SM-2 |
| 6 | "_This is the_ / [name] / _[kind]_ / of / _[content / training / selling]_" | HA-02 · SM-3 |
| 7 | "_This is how_ / [who] / [verb] / _[result]_" | HA-02 · SM-3 |
| 8 | "_More [X]_ = _More [Y]_ = _[Result]._" (as the recap of a proof stack) | HA-02 · SM-3 |
| 9 | "The [N]-step [system] _behind [result]_" | HA-06 · SM-1 (stations P-17) |
| 10 | "Stop [doing X]. _Do [Y] instead._" (a contrast pair inside a 2-node hub) | HA-06 · SM-1 |

[NICHE: example] filled: (1) "6 ways to hook viewers _in the first 3 seconds_"; (2) "5 habits that _keep fat off_"; (3) "3 mistakes that _kill your saves_"; (4) "Fat loss isn't _willpower._ It's a 4-LETTER FORMULA"; (5) "Every viral post follows _one formula_" → "It's called HRST"; (6) "_This is the_ / carousel / _to reel_ / style / _of content_"; (7) "_This is how_ / coaches / plan / _a cut_"; (8) "_More protein_ = _More fullness_ = _Fewer snacks._"; (9) "The 3-step system _behind every launch_"; (10) "Stop posting daily. _Post better instead._"

---

## App. B Evidence map (summary; full map with timestamps in `evidence.md`)
| DNA element | Source |
|---|---|
| No presenter, VO-driven type, one idea in 18-33 s | v01, v02, v03 (all frames); analysis §0, §1 |
| Alternating sans / serif stack, rise + vertical blur, ≤ 5 lines, y 905-1470 | v01 @ 0:00.17-0:02.33 |
| Header line above a card, cy 313-486 | v01 @ 0:03-0:12 |
| Warm paper `#E2E1DC` + 64 px line grid; umber `#3A2E2C`; black / charcoal `#141414` | v01 @ 0:00, 0:02.5, 0:13; v03 @ 0:04 |
| Hub with redacted bars, push 1.0 → 2.4×, typed labels | v02 @ 0:00-0:03, 0:06, 0:11, 0:16, 0:22 |
| Thumb rain (≈ 25 drifting cards) + condensed claim | v03 @ 0:00-0:03.7 |
| Giant initials + tucked words + explanation ladder; "That's HRST" | v03 @ 0:04-0:13 |
| Hero 9:16 card 432 × 674 with a view chip; profile card; dark quote cards | v01 @ 0:00, 0:06, 0:14-0:18 |
| Equation recap | v01 @ 0:18-0:21 |
| Lead-magnet card + `Comment "Database"` | v01 @ 0:22-0:23.9; v03 @ 0:14-0:18 |

`(unverified)`: the speech language (no transcripts), sound and music (not observable), the exact font families (closest bundled matches), the hook state-change counts (counted from 6 fps sheets).
