# Archive Explainer Style Playbook (template v1)

**Purpose.** You (Claude) edit {{BV-01.name|the creator}}'s reels in one of two formats that share one visual voice. **F-A Archive explainer:** a voice-over (no presenter on screen) becomes a fast documentary short: archive images and created plates cut on the words, a royal-blue canvas carrying "receipt" cards (the exact headline of the cited source with its key span in lime), maps and figure cards, under a monospaced caption in a dark box that *is* the headline. **F-B Podcast clip:** a 30–60 s moment from the creator's own two-camera conversation, cut on speaker handovers with calm holds, captioned in brand-blue boxes. Both end on the creator's branded end card.

**Input you expect.** F-A: a voice-over file (+ the script), and optionally the creator's own photos, clips, article screenshots and map images (every one is optional: §12.3 builds a created substitute). F-B: two (or three) synced camera files of a conversation and one audio track per person, or one wide shot (single-camera fallback).

**Who reads this.** You, section by section while planning and building a reel for a creator in any niche. Every number is on the final 1080×1920 frame at 30 fps.

### Style DNA `[DNA]`
A short that reads like a well-researched documentary cut down to one minute. Nothing is decoration: every picture is either *the thing being named* (a face, a place, a document, a number) or *the receipt for it* (the cited headline with its key words in lime). The canvas is one saturated brand blue; cards sit on it with 40 px corners; archive images cut hard every ~1.1 s with a slow Ken Burns; and over everything a white monospaced caption in a black box carries the sentence, two to five words at a time, so the reel works on mute. The voice is calm and certain; the pace is fast because the *pictures* change, not because anything shouts.

**Copy these 5 things** (each one points at the section that implements it):
1. **The boxed caption is the headline.** White JetBrains Mono Bold 58 px in one black 60 % box per chunk (F-A), white Inter Tight ExtraBold 60 px in brand-blue 85 % boxes, one per line (F-B); 2–5 words, ≤ 2 lines, hard swaps, centred on y 1415 / 1405. No other headline element exists. → §5.3 CS-A / CS-B, H7.
2. **One brand blue.** `primary` {{BV-02.primary|#1A2FAA}} is the F-A canvas, the F-B caption box and the QR end card. Cards on it are rounded 40 px; the lime `accent` {{BV-02.accent|#CCF852}} marks only the key span of a receipt, the leader dot and the end-card action box. → §3.1, §4.
3. **Show the receipt.** Every claimed fact that comes from somewhere appears as a source card: outlet + date in small mono, the exact headline typed on in white, its key span turning lime on the spoken word, a thin leader line to decorative body copy and photo thumbs; plus a credit line on every creator-supplied image. → P-SOURCE-CARD §8.3, §19, H9.
4. **Thesis montage, then hard cuts on the words.** The first 3 s state the whole thesis over 3–5 archive pictures and one topical stinger; after that, a picture change every 0.9–1.8 s, always on a caption-chunk boundary or a named noun. (F-B: cut on the handover, hold calmly in between.) → §6.2, §7.6, §9.
5. **Branded end card.** The tagline end card (F-A: four-line heavy tagline with two accent words + wordmark + Follow → Following) or the QR end card (F-B: brand-blue field, three mono lines, URL chip, white QR). → §25, P-END-TAGLINE, P-END-QR.

F-A and F-B share traits 1, 2 and 5 (and the no-decoration restraint of 3): that is what makes them one style (§0.4).

### Directives `[DNA]`
| # | Directive | Where it lives |
|---|---|---|
| D1 | **The caption is the banner.** Never add a title slab, pill or kinetic headline; the first boxed chunk at f0 is the headline | §5.2 (OFF), §5.3, H3 |
| D2 | **Literal pictures only.** A person → that person (their photo, or a silhouette plate with their name); a place → that place (photo, locator card); a number → a figure card or the receipt that states it. Never mood stock | §8.4, H5, N1 |
| D3 | **Receipts, not paraphrase.** A cited claim shows its source exactly as written (outlet, date, headline verbatim); the key span in lime lands on the spoken word | §19, P-SOURCE-CARD, H9 |
| D4 | **Pictures move on the words.** F-A: a hard cut or a card event at least every 2.0 s, every cut on a chunk boundary or a noun onset (±2 f); F-B: a cut within ±3 f of every handover | §7.6, §9, H2, H13 |
| D5 | **Blue world, black-box captions, lime receipts:** three colour jobs, never a fourth bright hue except the comparison chips and the two end-card words | §4, H8 |
| D6 | **Ask, then create.** Every third-party picture is the creator's own file or a created substitute; never fetched | §12.5, H10 |
| D7 | **Calm authority.** No memes, stickers, emoji, shakes or crash zooms; energy comes from cut rhythm, in-card builds and at most 3 stingers per reel | §8.6 (OFF), §10.2, N4 |
| D8 | **End on the brand.** Every reel ends on the branded end card, ≤ 3.5 s, with the creator's action readable ≥ 1.5 s | §25, H15 |

Buyer directives BD1… may be added below this line (they may only make the style stricter or more specific).

### Quick index
| § | What | State |
|---|---|---|
| §0 | Style profile (F-A default, F-B override) | ON |
| §1–§15 | Procedure, rules, worlds, colour, type, hook, structure, patterns, transitions, motion, sound, footage, output, examples, QA | ON |
| §16 | Frame template / chrome | OFF |
| §17 | Running state & anchors | OFF |
| §18 | Data contract | ON (F-A) |
| §19 | Evidence & citations | ON (F-A) |
| §20 | Dialogue | ON (F-B) |
| §21 | Canvas camera | OFF |
| §22 | Ink | OFF |
| §23 | Continuity | OFF |
| §24 | Series furniture | OFF (VAR: buyer may switch on) |
| §25 | Brand & end cards | ON (both) |
| Parts C–F, App. A–B | Exceptions & core, personalisation, changes, ID index, headline bank, evidence | ON |

Formats: **F-A Archive explainer** (default) · **F-B Podcast clip**. One format per reel, declared in the reel header (§13.3).

---

## §0 Style profile `[REQ]`

```yaml
profile:                         # mirrored in tokens.json -> profile (F-A values; F-B overrides below)
  source_type: voiceover_only
  presenter: {presence: none, share: [0, 0], max_absence_s: null}
  spine: audio
  captions: {mode: full, role: primary, mute_policy: mute_safe}
  graphics: primary
  duration: {class: standard, target_s: [45, 80]}
  language: {speech: en, captions: {lang: en, script: Latn, transform: verbatim}, on_screen: en, post_title: en,
             supported: [[en, en, Latn], [hinglish, hinglish, Latn], [hi, hi, Deva]]}
  numbers: {grouping: international, currency: "$", compact: k_m_b, units: metric, decimals: 0, style: long}
  tone: {energy: balanced, comedy: off, comedy_max: off}
  themes: {policy: single, packs: [], default: null}
  formats: {list: [F-A, F-B], default: F-A}
  footage_dependency: medium
  cta: {devices: [end_card, subscribe, qr, link_bio, cross_promo, comment_keyword], placement: end}
  modules: {chrome: false, running_state: false, anchors: false, data_figures: true, citations: true,
            dialogue: false, canvas_camera: false, ink: false, continuity: false, series: false, brand: true}

formats.F-B.profile:             # only what differs
  source_type: multi_speaker
  presenter: {presence: anchor, share: [85, 100], max_absence_s: 4}
  spine: talking_head
  graphics: minimal
  duration: {class: short, target_s: [30, 60]}
  footage_dependency: high
  modules: {data_figures: false, citations: false, dialogue: true}
```

Why each switch has its value:
- **source_type: voiceover_only (F-A)** because the archive shorts have no presenter at all (v01, v02: 0 % on screen); the engine's VO-only pipeline (E-12) is the path that builds every frame from scenes. The archive pictures enter as the creator's assets. **multi_speaker (F-B)** because the podcast clip is a two-camera conversation (v03).
- **presenter: none (F-A)** (v01 0:00–1:19, v02 0:00–0:58: no host); **anchor 85–100 % (F-B)** (v03: a speaker on screen 0:00–0:41, the QR card is the only absence).
- **spine: audio (F-A)**: every picture is chosen per sentence of the VO; **talking_head (F-B)**: the conversation take is the timeline.
- **captions: full / primary / mute_safe**: every word is captioned, the boxed caption is the strongest element on every frame (all three videos), and the story reads on mute.
- **graphics: primary (F-A)**: receipts, maps, figure cards and plates carry the argument for ~45 % of runtime and the archive pictures for the rest (v01: archive ≈ 50 %, blue cards ≈ 40 %, green figures ≈ 7 %). **minimal (F-B)**: captions + end card only (v03).
- **duration: standard 45–80 s (F-A)** (v01 80 s, v02 59 s) with one re-hook at 20–30 s; **short 30–60 s (F-B)** (v03 43 s).
- **language: en** (all captions English; speech unverified, no transcript). Hinglish options are offered because mono captions work for any Latin-script text. Devanagari is **not** supported: no bundled monospaced Devanagari face exists, and a sans substitute breaks DNA 1.
- **numbers: international, $, long** ("$20 billion", "$2 million each" in v01). Indian buyers switch to ₹ + lakh/crore through BV-06.
- **tone: balanced, comedy off** (no gags in any video; calm news read).
- **themes: single** (one blue world per format; the brand colour replaces it).
- **footage_dependency: medium (F-A)**: the reel is complete from a VO alone; the creator's photos raise fidelity (§12.3 FB-1). **high (F-B)**: it needs the creator's two-camera footage.
- **cta**: the evidence uses an end card with a subscribe pill (v01, v02), a cross-promo video card (v01) and a QR card (v03); link-in-bio and comment keyword are the Instagram equivalents the buyer may pick.
- **modules**: citations + data_figures + brand (F-A); dialogue + brand (F-B).

### 0.4 Formats `[DNA set; VAR enable]`
| Field | F-A Archive explainer | F-B Podcast clip |
|---|---|---|
| `when` | A VO explainer about a person, company, place, event or rule: why it happened, who is behind it, how it works | A 30–60 s moment from the creator's own conversation (podcast, interview, panel) |
| profile overrides | — | source multi_speaker, presence anchor, spine talking_head, graphics minimal, duration short, footage high, dialogue on, citations/data off |
| layouts | L-A-canvas (stage hidden throughout), L-end | L-B-full (shots composed by the engine), L-end |
| default hook | HA-11 Thesis montage | HA-14 Cold authority |
| allowed hooks | HA-11, HA-12, HA-07, HA-19 | HA-14, HA-03 |
| structure | explainer | conversation |
| cadence | SC/10 s 8–16 · hook 7 · cuts/min 15–30 · median shot 0.9–2.2 s | SC/10 s 5–12 · hook 2 · cuts/min 7–16 · median shot 2.0–5.0 s |
| captions | CS-A (mono, black box) | CS-B (Inter Tight, brand-blue box) |
| end card | P-END-TAGLINE (or P-END-QR when the device is qr) | P-END-QR (or P-END-TAGLINE when the device is subscribe) |
| shared DNA | the boxed caption is the headline; one brand blue; a branded end card with the creator's wordmark | same |

Pick the format from the input: a VO file → F-A; two or more camera files of a conversation → F-B. Never mix (a podcast clip never gets archive cutaways; an archive explainer never shows the creator talking).

---

## §1 Procedure (follow in order) `[DNA]`

### 1.1 Core steps with the F-A branch (voice-over archive explainer)
1. **P1 Inventory.** `veos ingest --audio <vo> --script <script>` (the VO is source `V`); ffprobe every creator file; conform to 30 fps. Register every creator image or clip with `veos asset add <file> --origin creator --name <slug>` and note its subject, date and credit (P1b below).
2. **P1b Archive bank tagging** (this style's first craft step). For each creator asset write one line: `{name, subject (person/place/object/document), date or era, look (colour | b&w | sepia | halftone | vhs), aspect, credit}`. Images < 1080 px on the short side may only be used inside cards (P-PHOTO-CARD), never full-bleed.
3. **P2 Prepare.** Nothing to matte. Pick a grade per archive asset from §4.4 (never the same treatment on two consecutive shots).
4. **P3 Transcribe** with word timestamps (`veos transcribe`), `captions.transform` verbatim; apply the glossary (every proper noun in the script goes in the glossary before captions are built).
5. **P4 Segment** into `HOOK` (0–3 s thesis) · `TURN` ("Here's why" / the question) · `CONTEXT` · `RECEIPTS` (escalation) · `COMPARE` (when the script compares two sides) · `PAYOFF` · `CTA`.
6. **P5 Classify** every sentence with a line type (§8.4) and mark its trigger word (the noun or figure the picture lands on).
7. **P5b Picture-per-chunk pass** (this style's core craft): run `veos captions build` first, then give **every caption chunk a picture decision**: *cut* (new archive picture or card), *event* (an event inside the current card: highlight, pin, bar, thumb) or *hold* (only allowed when the previous chunk cut). No two consecutive chunks may both hold. This is how the 0.9–1.8 s rhythm is made.
8. **P6 Tone-tag** every sentence: `explain` · `evidence` · `turn` · `warn` · `awe` · `cta` (§10, §11).
9. **P7 Hook plan.** HA-11 by default (§6.2): pick 3–5 archive pictures (or plates) that carry the thesis, one topical stinger object, and write **3 hook variants** (the first 1–3 chunks are the headline: §6.5). Run the stopper tests (§6.1).
10. **P8 Visual plan.** One pattern per line (§8.4); the figure plan (§18: every number shown is in `plan/figures.json`); the citation capture (§19: masthead, date, exact headline, highlight spans per receipt); the map plan (P-LOCATOR-CARD until E-18).
11. **P8b Inserts.** `veos inserts scan`, refine the list, **ask the creator once** (§12.5), record `plan/inserts.json`.
12. **P9 Beat sheet** (§13): one beat per trigger; check the cadence targets (§7.6) against the chunk list.
13. **P10 Sound contract** (§11) and the transition map (§9).
14. **P11 Assets.** Build the created plates; resolve fallbacks (§12.3) and list which were used.
15. **P12 Checkpoint** (§13.5), then **wait for approval.**
16. **P13 Build** act by act: `veos scenes-meta` → `veos measure --every 10` → `veos validate` → fix → preview stills → QA (§15, ≤ 3 passes) → render.

### 1.2 F-B branch (two-camera podcast clip)
1. **P1 Inventory.** `veos ingest` all camera files and mic tracks → `veos conform` → `veos sync` (2+ files; abort and ask if `SYNC_UNRELIABLE`).
2. **P3 Transcribe** the session master (`veos transcribe --id MIX`).
3. **P3b Diarise:** `veos speakers` (mode `mics` when one mic per person exists, else `diarize`), then `veos speakers name S1=<Host>:host S2=<Guest>:guest`.
4. **P3c Angle map:** `veos angles` (which camera shows whom; faux crops `<src>:<speaker>` from a wide).
5. **P4 Moment selection** (this format's craft): `veos shots mine --min 30 --max 60`, then pick the candidate whose **first sentence is the strongest standalone line** (HA-14 needs the payoff in the first second) and whose last sentence is a **button** (a quotable conclusion). Trim the in-point to the first word of that sentence (±2 f); trim the out-point to include 1.5–2.5 s of non-essential tail (a laugh, "yeah", "exactly", a breath) for the end card (§25.3). Write the EDL; `veos cut`.
6. **P5/P6** classify and tone-tag as in F-A (most lines are `explain`/`turn`; the button is `awe`).
7. **P7 Hook plan:** HA-14 (§6.2b). Write 3 in-point options (3 different first sentences) and pick by the stopper tests.
8. **P9b Cut grammar pass:** `veos shots plan --apply` (the turn generator with this style's `dialogue.cut_rules`: no stack opener, holds ≤ 6 s, reactions 1.2–2.2 s, re-crop ×1.2), then hand-edit only for R-4 (wide establish) and R-5 (stack exchange) (§9.3). `veos shots check` must pass (V-SPEAKER).
9. **P10–P13** as in F-A, with `veos shots render` before `prep-frames`.

### 1.3 Module steps
| Module | Step |
|---|---|
| `citations` (F-A) | **Citation capture** inside P8: for every receipt write `{masthead, date, headline (verbatim), highlight_spans, body_line (verbatim sentence from the article if the creator gave it, else none), credit}`. A headline the script does not state verbatim (and the creator did not paste) is **not** shown; flag it at the checkpoint. |
| `data_figures` (F-A) | **Data check:** every figure's inputs with provenance (`script` + the said words), the formula from the safe set, recomputed; mismatches flagged at the checkpoint. |
| `brand` (both) | **End-card check:** tagline written (BV-01 + niche; asked once at the first checkpoint, then stored in `brand.endcard.tagline`), wordmark asset or monogram (SH-8 / FB-8), the chosen device and its value (BV-08). Sponsor: disclosure line + hold (§25.4). |
| `dialogue` (F-B) | Covered by the F-B branch (P3b, P3c, P9b). |

---

## §2 Hard rules `[DNA]`

### 2.1 Editing rules (every style)
The ten editing rules in `playbooks/_global/GLOBAL-RULES.md` apply. They are directions, not limits: smooth, seamless motion; nothing overlaps by accident; keep the face clear (behind the speaker is fair game, text included); readable at a glance; one idea at a time; show the thing, not the word; say what was said; hook titles hook; pace like the style, not like a timer; the style decides the look.
- **Facts the engine checks:** accidental overlaps, jumps, the face covered, unreadable text, numbers and quotes that don't match what was said, the promised count. Every count, timing and budget this playbook gives is direction for the edit, not a limit.
- **Picture first, in this style's own look:** every key beat shows the thing being said (an object, a screen or app, a diagram, numbers in motion), not just its word; text supports the picture and never replaces it. When the speaker points with words ("this, this and this", "from this to this", "ye dekho"), show what they mean. Illustrations may use made-up but realistic numbers and names ("212 views", "1.2M views"), with no label; a number or quote the speaker says is shown as said. This overrides any rule below that bans made-up numbers or asks for an example tag: those rules now cover claims (the creator's results, prices, benchmarks, testimonials), not illustrations.
- **Hook titles hook:** the on-screen title promises the viewer something (an outcome, a curiosity gap, who it's for) and is true to what the reel delivers; it need not repeat the spoken words. This playbook sets its shape (§5.2, §6.5: lines, sizes, word limits, case), never its voice (§6).
- **Retired (8 Oct 2026), whatever this playbook says below:** no REPRESENTATIONAL or example labels on made-up cards, no credit lines, no flash limit (flash as often as this style calls for; any "NC-11" cap below no longer applies), and text may sit behind the speaker without an exception.

### 2.2 Declared exceptions
**None declared.** The evidence's captions measure 58 px (F-A) and 60 px (F-B) on the 1080 frame, above the 54 px floor, so E3 quiet type is not needed (the coverage table's "38–42 px" was measured on the 720 px source without scaling; see App. B). Labels on maps, chips and plates are set at 40 px. Caption swaps are hard, which needs no E6 (subtitles are exempt from G3).

### 2.3 MUST rules
| ID | Rule | Check |
|---|---|---|
| **H1** | **Frame 0 (F-A, HA-11):** an archive picture (kind `archive`, or a created plate with `satisfies: ["archive"]`) fills the frame with a Ken Burns move already running, **and** the first caption chunk is on screen in its box (first word ≤ 3 f in). No other text at f0. F-B (HA-14): the speaker single is live and the first chunk is on screen at f0. | V-F0 |
| **H2** | **Cadence (F-A):** 8–16 weighted SC per 10 s of body; ≥ 7 in 0–3 s; no gap > 2.0 s between weight-1 SCs; nothing static > 2.5 s; 15–30 picture cuts per minute; median shot 0.9–2.2 s. **F-B:** 5–12 SC/10 s; ≥ 2 in 0–3 s; max gap 3.0 s; 7–16 cuts/min; median shot 2.0–5.0 s. | V-CADENCE |
| **H3** | **Thesis by 3.0 s (F-A):** the full thesis sentence (subject + what happened + the twist) is spoken and captioned by 3.0 s, and the scene on screen at that moment is tagged `payoff: true`. **F-B:** the clip's in-point is the first word of its strongest sentence (P4), so that sentence starts at f0 (± 2 f) on the speaker single, and it completes by 4.0 s. | V-F0 (F-A), review (F-B) |
| **H4** | **Caption chunks:** 2–5 words, ≤ 18 characters per line (F-A) / ≤ 20 (F-B), ≤ 2 lines, never splitting a name, number or unit; hard swaps; lead 1 f; never on screen > 0.15 s before the first word. | V-CAPTION |
| **H5** | **On-the-word pictures:** a cut or card event lands 2 f before its trigger word and is fully settled within +5 f. Receipt highlights land on the first word of the highlighted span ±3 f. | V-ONWORD |
| **H6** | **Dead air (spine audio):** pauses in the VO ≤ 0.6 s inside a paragraph, ≤ 1.0 s between paragraphs (tighten with `cut --identity --tighten --max-pause 0.6`); the caption holds over pauses ≤ 0.4 s (`pause_hold_s`) and the picture keeps moving (Ken Burns, card drift). F-B: at most 1 gap ≥ 0.4 s per 15 s, except a deliberate listener beat before the button. | review (F-A cut stats), V-CADENCE |
| **H7** | **The caption band is sacred:** CS-A / CS-B only, centred on y 1415 / 1405, nothing else in y 1290–1540 while a chunk shows (stingers pass *under* the caption), captions hidden only on the end card. | V-SAFE, G1 |
| **H8** | **Hues:** ≤ 3 bright hues per frame (brand blue, lime, plus one of side_a / bad / good / end_a / end_b). Lime appears only on receipt spans, the leader dot, active pins and the end-card action box. | V-HUES |
| **H9** | **Receipts are exact:** masthead + date + headline on every source card; the headline is verbatim from the script, the transcript or a creator-pasted text; highlight spans occur in the headline. | V-CITE |
| **H10** | **Inserts:** every third-party moment is recorded in `plan/inserts.json` as `creator` (file) or `created` (recipe + substitute_of). | V-INSERTS |
| **H11** | **Numbers:** every number drawn on a card, chart, map or plate comes from `plan/figures.json` (or is verbatim inside a quoted headline) and is written by `ctx.fmtNum`; counters land within ±5 f of the spoken number. | V-DATA, V-NUMFMT |
| **H12** | **Face rule:** (F-B) nothing covers a speaker's face; captions move to the chest automatically (`avoid_face`). (F-A) a face inside an archive picture is never covered by a card, chip or plate: plates sit under the chin or beside the head with 40 px clearance. | V-FACE (F-B), review (F-A) |
| **H13** | **Speakers (F-B):** a cut within ±3 f of every handover on full shots; no shot holds > 7.0 s; reaction cutaways 1.2–2.2 s, never across a handover; the caption style matches the diarised speaker (host upright, guest italic). | V-SPEAKER |
| **H14** | **Presence (F-B):** a speaker on screen ≥ 85 % of runtime; the only absence is the end card (≤ 4 s). | V-PRESENCE |
| **H15** | **Promise and end:** every open loop ("here's why", "now why…") is paid on screen; the end card holds ≤ 3.5 s with the action (keyword, URL, QR, Follow) readable ≥ 1.5 s; hard end ≤ 6 f after the last spoken word; black tail ≤ 0.2 s. | V-PROMISE, review |
| **H16** | **Safe zones:** meaning text inside x 64–1016, y 110–1500; nothing but the right-edge-free picture in x > 970 between y 900–1540; credit and label tags at y ≥ 128. | V-SAFE |
| **H17** | **Spelling:** proper nouns exactly as in the glossary; captions normalised (the source reel's "lenghts" typo would fail). | V-CAPTION |
| **H18** | **Re-hook (F-A standard):** one re-hook between 25 % and 75 % of runtime (P-QUESTION-TURN: "Now why…" over a hard cut back to an archive face, beat `rehook: true`), and no stretch > 25 s without one before the CTA. | V-REHOOK |
| **H19** | **Audio:** −14 LUFS integrated, true peak ≤ −1.5 dBTP, bed ≥ 18 dB under the voice. | NC-8, `veos mix` |
| **H20** | **Determinism:** particles and stinger rows use `ctx.rng(seed)`, letter resolves use `fx.resolve` with a `seed`; nothing reads the clock. | NC-9 |

### 2.4 NEVER list
- **N1** Stock-cliché pictures: globes spinning, typing hands, "business people" handshakes, generic city timelapses. If there is no literal picture, build the plate (§12.3).
- **N2** A headline, quote or statistic that is paraphrased, shortened mid-sentence or re-ordered and still presented as the source's words (NC-13).
- **N3** Fetched media of any kind: no image search, no logo download, no screenshot of someone else's site taken by Claude (NC-7).
- **N4** Memes, emoji, stickers, meme SFX, shakes, crash zooms, RGB splits, light leaks, film burns.
- **N5** Coloured words inside captions; a caption without its box; two caption styles in one reel (except F-B speaker italics).
- **N6** Lime as decoration (frames, backgrounds, underlines of non-key words); a second highlight colour on receipts.
- **N7** Full-bleed images softer than 1080 px on the short side, or upscaled > 1.35× (§12.4).
- **N8** A map, flag or border drawn from memory as if accurate: until E-18 ships, maps are schematic and say so (`SCHEMATIC` tag).
- **N9** Fake UIs or dashboards presented as real; the cross-promo card shows only the creator's own video.
- **N10** Captions on the end card (the card carries the words); an end card longer than 3.5 s.
- **N11** In F-B: archive cutaways, B-roll, zoom presets, or graphics over the speakers beyond the optional name plate and the end card.

A buyer may add BN1… here.

---

## §3 Worlds, layouts, stage moves, safe zones `[DNA; coordinates TUNE ±5%]`

### 3.1 Worlds
| ID | Kind | Look | Carries | Enter / exit | Share of runtime (F-A) |
|---|---|---|---|---|---|
| **W-blue** | card-world | `primary` {{BV-02.primary|#1A2FAA}}, film noise 0.03, no grid, no vignette | Receipts (P-SOURCE-CARD), maps, photo cards, comparison cards, plates set in type | Hard cut on a chunk boundary (T-01); stinger (T-02) out of the hook | 35–55 % |
| **W-archive** | archive | Black behind full-bleed archive pictures and created plates (the picture *is* the world) | Faces, places, events, objects, dates: the montage | Hard cut (T-01), stinger (T-02), roll-by (T-03) | 35–55 % |
| **W-green** | stage | `data` #1B473A, noise 0.03 | Figures: seat arcs, bars, flows, counters (on a `data_card` #19613B card) | Hard cut | 0–15 % |
| **W-white** | canvas (light) | #FFFFFF flat | P-WATCH-FULL cross-promo video card only | Hard cut in, hard cut out to the end card | 0–5 % |
| **W-end** | void | `end_bg` #0A1314, noise 0.05 | P-END-TAGLINE | Hard cut, then the card builds (T-06) | 3–8 % |
| **W-qr** | card-world | `primary`, flat | P-END-QR (F-B, and F-A when the device is `qr`) | Hard cut | F-B 3–8 % |
| **W-room** | footage | The creator's own podcast set (F-B) | Speakers | Shot cuts (timeline.shots) | F-B 92–97 % |

F-A uses W-blue, W-archive, W-green (when a figure appears), W-white (when cross-promo is chosen) and W-end / W-qr. Set the world with `timeline.world` entries on the same frame as the cut that changes it. Full-bleed archive scenes are z2 and opaque, so W-archive only shows around letterboxed pictures.

### 3.2 Layout library
| ID | Engine | Rects (1080×1920) | Caption | Use | Share |
|---|---|---|---|---|---|
| **L-A-canvas** | `hidden` (VO reel: no footage) | Scene rects inside it: **card** x 64 y 500 w 952 h 620 r 40 (centre y 810) · **tall** x 64 y 320 w 952 h 952 r 40 · **text** x 64–1016, y 240–1250 (receipts) · **bleed** 0, 0, 1080 × 1920 (archive) | CS-A, cy 1415 | Every F-A frame but the end card | F-A 0.90–1.00 |
| **L-B-full** | `full` (the engine composes shots into the footage) | Speaker footage full frame; head top y 140–300; stack shots inside it via `timeline.shots` (seam y 960) | CS-B, cy 1405; on the seam during stack shots | Every F-B frame but the end card | F-B 0.90–1.00 |
| **L-end** | `hidden` | End-card graphic x 64 y 160 w 952 h 1300 | captions hidden | The last 2.0–3.5 s of both formats | 0.02–0.10 |

F-A writes `"stage": [{"t": 0, "layout": "L-A-canvas"}, {"t": <end card t>, "layout": "L-end", "via": "cut"}]`. F-B writes `"stage": [{"t": 0, "layout": "L-B-full"}, {"t": <end card t>, "layout": "L-end", "via": "cut"}]` and puts every camera decision in `timeline.shots` (never in `stage`).

**Rect use rules (F-A):** one card rect per screen; the card rect and the text rect never appear together; a **bleed** picture never shares the frame with a card (cards sit on W-blue / W-green only). Choose **card** for landscape media and maps, **tall** for portrait media, square maps and the comparison cards, **text** for receipts and quotes.

### 3.3 Stage moves
| ID | Move | Recipe | Use |
|---|---|---|---|
| **G-1** | Hard cut | 0 f; incoming scene `in: "none"`, `cuts: [0]`; the outgoing scene ends on the same frame | Every archive-to-archive, archive-to-canvas and card-to-card change (≈ 60 % of changes) |
| **G-2** | Card cut-in | The card hard-cuts in fully framed (no rise, no fade: v01 @25.37 green card, @47.84 map card); what moves is *inside* it: the avatar, pins or media build over the next 6–16 f | Every card after an archive run |
| **G-3** | Deck advance | The next comparison card hard-cuts in on top; the previous card stays visible as a 48 px strip at the left edge; the new media window fades up from blue-tinted (G-7). **Side change** (A → B): the old chips and card push up off the top edge in 4 f: the built-in transition `{"t": <side change>, "type": "push", "dir": "up", "frames": 4}` (v02 @34.24) | P-COMPARE-SWIPE sequences |
| **G-4** | Follow-push | When body copy / thumbs arrive, the whole receipt block scales 1.00 → 1.14 (TUNE 1.10–1.16) and translates up-left so the newest element sits in the upper 60 %, over 24–27 f, sine in-out, then keeps creeping ≈ 1 %/s until the next event (measured v01 @14.52–15.40: ×1.145, −110 / −300 px) | P-SOURCE-CARD |
| **G-5** | Shot cut (F-B) | `timeline.shots` boundary; 0 f | Handover, reaction, re-crop, wide |
| **G-6** | End cut + build | Hard cut to W-end; the end card builds in place (§25.2) (v01 @76.80, v02 @56.00: no dissolve) | P-END-TAGLINE |
| **G-7** | Inner punch + drift | Inside a map or figure card: a hard ×1.5–1.8 punch toward the focus on the spoken place / person word (0 f), then a slow drift for the rest of the hold: pull-out ≈ 0.15 %/f or a pan of ≈ 9 px/f toward the next focus (v01 @29.97 seat arc ×1.8, @49.14 map ×1.52 then pan south). Media windows fade up from 35 % over `primary` to 100 % in 14–16 f | P-MAP-CARD, P-LOCATOR-CARD, P-SEAT-ARC, P-COMPARE-SWIPE |

### 3.4 Layout diagrams

**F-A card on blue (L-A-canvas / card)**
```
┌─────────────────────────┐ 0
│  (IG top UI, keep clear)│ ← y 0–110
│ ●                       │ ← credit / label slot x 64, y 128 (TC-legal 22–24 px)
│                         │
│  W-blue #1A2FAA         │
│ ╭─────────────────────╮ │ ← card x 64–1016, y 500, radius 40
│ │  map / photo / chart │ │
│ │                      │ │
│ ╰─────────────────────╯ │ ← card bottom y 1120 (graphic floor 1290)
│   ▇▇▇ mono caption ▇▇▇  │ ← CS-A box, centre y 1415 (band 1330–1505)
│   ▇▇▇ line two ▇▇▇▇▇▇▇  │
│  (IG caption / buttons) │ ← y > 1540 clear
└─────────────────────────┘ 1920
```

**F-A receipt (L-A-canvas / text)**
```
y 360   Outlet Name · 12 Mar 2025          ← mono 500 30 px, label_dim
y 404   Headline line one $20bn            ← display 700 64 px; key span lime, the rest muted after the highlight
        headline line two goes here
        headline line three ●              ← lime dot Ø 18 after the last line
y ~640  ──────────────────────╮            ← leader 3 px muted, from the dot left to x 300,
                              ╰─────────── ← corner r 36, down 120 px, then left off-frame
        decorative body copy (mono 20, muted 50 %, one span lime)
y ~860  ▇▇▇▇ ▇▇▇▇ ▇▇▇▇                     ← photo thumbs h 290, square corners, gap 0, centred
        (the block settles up so it ends ≤ y 1250)
y 1415  ▇▇ caption ▇▇
```

**F-A full-bleed archive (L-A-canvas / bleed)**
```
┌─────────────────────────┐
│ ● PHOTO: credit         │ ← y 128
│                         │
│   archive picture       │ ← z2, cover, settle 1.04 → 1.00, drift ≤ 1 %/s
│   (face in the top 60%) │ ← face centre y 520–900
│                         │
│   ▇▇ caption ▇▇         │ ← y 1415
└─────────────────────────┘
```

**F-B speaker single (L-B-full)** and **stack exchange (shots)**
```
┌─────────────────────────┐        ┌─────────────────────────┐
│                         │        │   speaker (top cell)    │
│     speaker single      │ ←head  │                         │
│     head top y 140–300  │  top   ├───── seam y 960 ────────┤ ← caption box on the seam
│     face ~17 % of h     │        │   listener (bottom)     │
│   ▇▇ blue box caption ▇▇│ ←1405  │                         │
└─────────────────────────┘        └─────────────────────────┘
```

**End cards (L-end)**
```
P-END-TAGLINE (W-end)              P-END-QR (W-qr, primary)
y 200  For more                     y 470  Watch the full conversation
y 330  <topic A> and   ← end_a      y 522  with <Name>
y 460  <topic B>,      ← end_b      y 574  at [ url.chip ]  ← paper box, ink text
y 590  decoded                      y 760  ┌──────────┐
y 880  (●logo) [Follow] [handle]           │   QR     │ 620 × 620, white
                                    y 1380 └──────────┘
```

### 3.5 Safe zones and bands
- Meaning text: x 64–1016, y 110–1500 (`layout.safe`). The right column x > 970 between y 900–1540 carries no text.
- **Caption band:** y 1330–1505 (CS-A 2-line box 1333–1497 as measured by the caption engine; CS-B 1316–1494). Graphics stay above **y 1290** while a chunk shows.
- **Credit / label slot:** x 64, top y 128, one line, mono 22–24 px. Holds the photo credit, SCHEMATIC or `example`; one tag at a time.
- **Card zone:** y 320–1272 (tall) / 500–1120 (card). **Receipt zone:** y 240–1250.
- **End-card zone:** y 160–1460.

### 3.6 Presenter rules `[COND: presence ≠ none]` (F-B only)
- Share ≥ 85 %; the longest absence is the end card (≤ 4 s).
- Crops: single = face ≈ 17 % of the frame height, face centre at 36 % of the crop height (engine default); head top y 140–300; never crop through the chin or the top of the head.
- Re-crop step ×1.2 (a 4K source gives clean results; 1080p sources cap at ×1.35 total).
- Nothing in front of the face (NC-1); the caption moves to the chest when a face reaches the band (`avoid_face`).
- F-A has no presenter: §3.6 does not apply (PV-1).

---

## §4 Colour `[roles' meanings DNA; brandable hex VAR/TUNE]`

### 4.1 Role palette
| Role | Hex | One job | Text on it | Contrast | Brandable |
|---|---|---|---|---|---|
| `primary` | {{BV-02.primary|#1A2FAA}} | Brand blue: F-A canvas, F-B caption box, QR end card | paper | 10.3 : 1 | **yes** (TUNE: one deep saturated hue, white text ≥ 7 : 1) |
| `accent` | {{BV-02.accent|#CCF852}} | Receipt lime: key span, leader dot, active pin, end-card action box | ink | 16.0 : 1 (8.4 : 1 as text on `primary`) | **yes** (TUNE: one bright highlighter hue ≥ 7 : 1 on primary) |
| `end_a` | #35CFD2 | End-card tagline word 1 | ink | 10.3 : 1 | yes (VAR) |
| `end_b` | #C64D3C | End-card tagline word 2 (display ≥ 112 px only) | paper | 4.6 : 1 | yes (VAR) |
| `side_a` | #BA3221 | Comparison side A chip | paper | 5.9 : 1 | no (fixed meaning) |
| `side_b` | #DDE3DB | Comparison side B chip | ink | 15.1 : 1 | no (fixed meaning) |
| `bad` | #E5483B | Blocked route ×, a loss, a closed door | ink | 5.0 : 1 | no |
| `good` | #3FBF6B | Open route, a gain, allowed | ink | 8.3 : 1 | no |
| `data` / `data_card` | #1B473A / #19613B | Green figure world / its card | paper | 10.5 / 7.5 : 1 | no |
| `navy` | #121B3A | Map sea, plate backs, inner fills | paper | 16.9 : 1 | no |
| `land` / `focus` | #7D8381 / #E9EDE6 | Map land / focus region and label chips | ink | 5.1 / 16.6 : 1 | no |
| `muted` | #8C9AD8 (source #6478BC is 2.4 : 1; raised to the 3 : 1 large-text floor) | Non-key headline words after the highlight, the leader line, body copy | — | 3.8 : 1 on primary | no |
| `label_dim` | #C2D184 | Outlet + date line | — | 6.3 : 1 on primary | no |
| `end_bg` | #0A1314 | End-card ground | paper | 18.8 : 1 | no |
| `ink` / `paper` | #0B0B0B / #FFFFFF | Text | — | — | no |
| CS-A box | #000000 @ 60 % (sampled 50–68 % over blue: #060D37 on #132595, #0D1A51 on #1C33A5) | The F-A caption container | paper | ≥ 8.4 : 1 on any ground | DNA |

### 4.2 Meanings
- **Blue = this creator's world.** It is the only ground graphics sit on in F-A, and the only box colour in F-B.
- **Lime = "this is the receipt".** It marks the exact words or number the voice is citing, nothing else.
- **side_a red vs side_b off-white = the two sides of a comparison** (v02: Japan red, US white). The first-named side is always `side_a`. Never use them as good / bad.
- **bad / good** only on routes, doors and outcomes (the × at the end of a blocked route).
- Other companies' brand colours never appear (logos are set in type: §12.5).

### 4.3 Theme packs: OFF (`themes.policy: single`). The buyer's BV-02 colours replace `primary` and `accent` directly.

### 4.4 Grades (archive treatments)
| ID | Filter | Use |
|---|---|---|
| GR-bw | `grayscale(1) contrast(1.12) brightness(0.98)` | Default for pre-1990 photos and portraits |
| GR-sepia | `grayscale(1) sepia(0.55) contrast(1.08)` | Newspaper-era photos, documents |
| GR-halftone | `grayscale(1) contrast(1.25)` + a 6 px dot-screen overlay at 22 % (multiply) | Created plates (always), print photos |
| GR-vhs | `saturate(0.85) contrast(1.05) blur(0.4px)` | Colour video clips from the 1980s–2000s |
| (none) | as supplied | Recent colour photos and clips |

Rules: never the same treatment on two consecutive archive shots, except "(none)"; the hook uses at least two different treatments when it has ≥ 3 archive shots (v02 0:00–0:01: colour card → B&W → sepia halftone); a treatment never changes what a picture shows (no recolouring flags, no removing people). Treatments are CSS filters on the scene (V-GRADE is pending in the engine; the frame reviewer checks them).

### 4.5 Rules
- ≤ 3 bright hues per frame (`max_bright_per_frame: 3`).
- Coloured text only on blue (lime, muted, label_dim) or on its own chip; never coloured words on a photo without a box.
- Footage (F-B) is never regraded; archive pictures change only through §4.4.

---

## §5 Type & captions

### 5.1 Font map `[slots DNA; families TUNE within class]`
| Slot | Family | Weights | Class (TUNE boundary) | Used for |
|---|---|---|---|---|
| `mono` | **JetBrains Mono** | 400 / 500 / 700 | monospace | CS-A captions, outlet lines, chips, name plates, credit lines, QR-card text |
| `display` | **Space Grotesk** | 600 / 700 | geometric grotesk 500–700 | Map labels, date plates, figures (receipt headlines moved to `endcard`, audit 2026-10) |
| `body` | **Inter Tight** | 700 / 800 | tight grotesk 700–900 | CS-B captions, end-card pills, video-card titles |
| `endcard` | **Montserrat** | 700 / 800 | wide geometric heavy 700–900 | The end-card tagline (800) and the receipt headline T-HEAD (700) |
| `numeric` | Space Grotesk | 700 | geometric grotesk | Counters and figure values |
| `serif` | Space Grotesk | 700 | (alias) | Keeps the inserts toolkit's masthead slot in style |

Brand wordmarks are image assets (SH-8) or the FB-8 monogram, never a font.

### 5.2 Headline element: OFF (`type.headline.kind: none`). The first CS-A / CS-B chunk is the headline (D1). No slab, pill, lockup or title card in either format.

### 5.3 Caption system profiles
**CS-A** (F-A; `extends: lib:johnny_a`, tuned to the measured evidence)
| Group | Value |
|---|---|
| Mode | full · primary · mute_safe |
| Chunking | `unit: phrase`, 2–5 words, ≤ 18 characters per line, ≤ 2 lines; never split names, numbers, units; a new chunk on `. , ? !` (punct_break) and on pauses ≥ 0.3 s (`pause_split_s`), always on ≥ 0.9 s |
| Timing | lead 1 f; ≥ 0.25 s per word; tail 0.12 s; **hard swap** (0 f); `pause_hold_s` 0.4 (the last chunk holds through short pauses, so the band is never empty mid-paragraph) |
| Skin | JetBrains Mono **700, 58 px** (TC-subtitle), case as spoken (sentence case, punctuation kept: "Donald Trump."), tracking 0, white, no stroke, no shadow, line height 1.24 |
| Container | **one `box` per chunk** (as wide as the longest line; a short second line sits centred inside it), fill #000000 at **60 %** (navy on blue, charcoal on light photos), radius 0, padding 10 × 16 |
| Position | `fixed_y`, **cy 1415** (block centre: a 1-line box spans 1369–1461, a 2-line box 1333–1497), centred, max width 952 |
| Speakers | — |
| Emphasis | **none** (no coloured, bold or bigger words; the receipt carries the emphasis) |
| Hide | on the end card only. The caption stays **on top of** stingers and roll-bys (measured: "just launched / a new scheme" stays readable over the full banknote cover, v01 @1.30–2.13; "and it involves / Donald Trump." over the ball, @4.43–4.84) and over the cross-promo card (v01 @76.4) |
| Language | Latin script; keep English terms verbatim; normalise spelling; profanity masked `inner` by default (S**T); glossary = every proper noun in the script |

**CS-B** (F-B; `extends: lib:johnny_b`)
| Group | Value |
|---|---|
| Mode | full · primary · mute_safe |
| Chunking | phrase, 2–5 words, ≤ 20 characters per line, ≤ 2 lines, same no-split and break rules (`pause_split_s` 0.35) |
| Timing | lead 1 f; hard swap; `pause_hold_s` 0.6 (conversation pauses) |
| Skin | Inter Tight **800, 60 px** (TC-subtitle), as spoken, white, soft shadow `0 2 4 rgba(0,0,0,.35)`, line height 1.45 |
| Container | **one box per line** (`box_per_line`, each shrink-wrapped to its line, stacked with no gap; measured v03 @11.40–11.83 "that's one dimension" / "of a place." are two boxes of different widths), fill `primary` at **85 %**, radius 0, padding 6 × 12 |
| Position | `fixed_y`, **cy 1405**; on `stack` shots the box sits on the seam (y 960); `avoid_face` on (it moves to the chest if a face drops into the band) |
| Speakers | host: white upright · guest: white *italic* (`captions.speakers`). The box colour never changes per speaker |
| Emphasis | none |
| Hide | on the end card |
| Language | as CS-A; profanity mask `inner` (S**T), on by default |

Both profiles: chunks never mix speakers; never hand-write cards (`captions.overrides` only: `{from, to}` spelling fixes, `{i, break: before}` to move a break so a name stays whole).

### 5.4 Other text systems
| ID | Element | Recipe | Class | Hold |
|---|---|---|---|---|
| T-OUTLET | Outlet + date line on a receipt | mono 500 40 px (measured ≈ 40–44 px, v01 @0:15), `label_dim`, "Outlet Name · 12 Mar 2025" (date as the source prints it); letters resolve in seeded random order over 16 f (14–18 f): `VEOS.fx.resolve(text, lt, {at, dur: 0.53, every: 2, order: "random", seed, ctx, font})` | TC-label | the receipt's life |
| T-HEAD | Receipt headline | `endcard` (Montserrat) 700 **70 px** — the receipt headline and the end tagline share one wide heavy grotesk in the source (v01 @0:15 vs @1:20), Space Grotesk is too narrow; (64–76 by length: ≤ 3 lines at 952 px; measured ≈ 72 px, v01 @0:15), line height 1.04, tracking −0.03, white → non-key words `muted`, key spans `accent` | TC-display | ≥ 2.0 s after the highlight lands |
| T-BODY | Receipt body copy | mono 400 20 px, `muted` 50 %, 3–5 lines, one span in lime (the spoken figure) | TC-decorative (the headline beside it carries the meaning) | with its receipt |
| T-CHIP | Side / trait chip | mono 700 40 px caps, tracking 0.04, pill radius 18, padding 12 × 24, `side_a` or `side_b` fill, a 44 px monogram disc or icon at left (never a flag drawn from memory) | TC-label | its card's life |
| T-MAPLABEL | Map / locator label | display 700 40 px caps on a `focus` chip radius 10, ink text | TC-label | its map's life |
| T-PLATE | Name plate | mono 700 40 px caps, white on a #000 70 % box, padding 8 × 16 (the caption's family) | TC-label | ≥ 1.2 s |
| T-DATE | Date plate | display 700 140–220 px, white, tracking −0.03, on a halftone plate | TC-display | ≥ 1.0 s |
| T-FIG | Figure value | numeric 700 72–160 px, white on green | TC-display | lands on the spoken number, holds ≥ 0.8 s |
| T-CREDIT | Credit line | mono 500 24 px, white 85 %, prefix "● " (dot in `accent`), x 64 y 128, fades in 6 f | TC-legal | the picture's life |
| T-TAG | SCHEMATIC / example | mono 500 22 px caps, tracking 0.08, white 80 %, same slot as T-CREDIT | TC-legal | the created picture's life |
| T-END | End tagline | Montserrat 800, 138 px (128–148), line height 1.0, tracking −0.04, left x 90, off-white `#E4ECE6` | TC-display | the end card |
| T-QR | QR-card text | mono 700 40 px, white, line height 1.3, centred; the URL in a paper box with ink text | TC-label | the end card |

### 5.5 Language and number rules
- English captions verbatim; brand and person names exactly as in the glossary; outlet names exactly as the outlet writes itself ("Financial Times", not "FT", unless the source's own masthead uses the short form).
- Numbers in captions are as spoken (the transcript's digits: "$20 billion", "211"); numbers on cards are `ctx.fmtNum` (long style: "$20 billion", "$2 million") unless they sit inside a verbatim headline ("$20bn" stays "$20bn").
- Hinglish (BV-05): captions romanised as spoken (`transform: verbatim`) or translated to English (`translate`); the mono boxes are unchanged. Indian buyers get ₹ + lakh / crore (BV-06): "₹1,20,000", "₹12.5 lakh".
- Units: metric; dual units only when the script says both.

---

## §6 Hook system

**Hook title (every style, 8 Oct 2026; above anything below):** the on-screen title promises the viewer something: an outcome they want, a curiosity gap, or who it's for ("How to go viral as a doctor creating content", not the label "Reels for Doctors"). It doesn't have to repeat the spoken words; it has to be true to what the reel delivers. A title shown as someone's words (in quotes) is still word for word. This section sets the title's shape (lines, sizes, word limits, case, the keyword device), never its voice. Write 8–10 candidates from the formulas below plus the proven patterns ("How to X as a Y", "Why your X isn't working", "The X nobody tells you", "Stop doing X", "Your X vs mine", a number or a contrast), score them on outcome, curiosity, who it's for and brevity, check the best against the stopper tests, and pick; any "write 3" below means this, and the next two go to the storyboard as alternates. A style with no on-screen title applies this to its post title.

### 6.1 Stopper tests
| Test | F-A value | F-B value |
|---|---|---|
| ST-1 Thumbnail | f0 at 25 % scale shows a literal subject (a face, a place, an object) and the boxed first chunk (58 px → 14.5 px, still a readable dark bar of 1–3 words) | off |
| ST-2 Mute | the first 3 s of captions state the whole thesis (subject + event + twist) | the first sentence makes sense alone, on mute |
| ST-3 Motion at f0 | Ken Burns already moving on the f0 picture | live speaker footage |
| ST-4 Read time | each hook chunk ≤ 5 words, readable in ≤ 1.0 s | — |
| ST-5 Change count | ≥ 7 weighted SCs in 0–3 s | ≥ 2 |
| ST-6 Payoff-by | thesis complete by 3.0 s | the strongest line starts at f0 |

### 6.2 Default archetypes `[DNA]`

#### 6.2a F-A: **HA-11 Thesis montage**
Spoken pattern: one sentence that names the subject, what it just did, and the twist; then a turn line. ("*<Subject> just <did a surprising thing>, and it involves <unexpected party>. Here's why.*")

| t | Beat | Tone | Visual (pattern) | Caption (CS-A) | Layer / camera | Cue moment |
|---|---|---|---|---|---|---|
| **f0** | Stopper | turn | **The subject, tight**: archive photo of the person / place / object, cropped 1.18 so the face fills the top 60 % (P-ARCHIVE-BLEED), slow drift 1.18 → 1.17 (measured ≈ 0.4 %/s, v01 @0.45–1.05); or the created **P-SILHOUETTE-PLATE**. Optional credit line at y 128 | chunk 1 = the subject's name or title, 2–4 words ("The King of FIFA") | W-archive, z2, `in: none` | — (the bed is already under) |
| 0.40–0.50 | Re-crop | turn | **P-RECROP-CUT**: the same picture hard-cuts to 1.00 (wider) (v01 @0.417), slow drift continues | — | `cuts: [0.45]` | — |
| 0.8–1.2 | Verb | turn | (holds) | chunk 2 = what happened ("just launched / a new scheme") | — | — |
| 1.10–2.45 | **Topical stinger** | turn | **P-STINGER-STACK**: a stacked block of the created topical object (banknote shapes for money, tickets for events, folded newspapers for media, balls for sport, crates for trade) rises from the bottom, accelerating, covers the frame at 1.63 (16 f), holds 6 f, then lifts off upward, decelerating, over 16–18 f, revealing picture 2 already in place underneath (measured v01 @1.09–2.43) | chunk 2 stays on top, readable throughout | z6, `events: [0.53, 0.75]` | **hook cue** on the cover peak (1.63) |
| 1.85–2.45 | Picture 2 | awe | The subject in action (event photo), revealed bottom-up by the lifting stinger; **P-PARTICLE-OVERLAY** (24–30 seeded flakes in `accent` / gold #E8C547 at 70 %) only when the line is about winning, money or celebration | chunk 3 = the purpose ("to make money") at 2.18, once the stinger has lifted | z2 + z5 overlay | — |
| 2.6–3.0 | **Thesis lands** | awe | Picture 3: the unexpected party (their photo or silhouette plate), Ken Burns pull-out; this scene has `payoff: true` | chunk 4 = the twist ("and it involves / Donald Trump.") | z2 | — |
| 3.0–4.0 | Turn | turn | Hard cut to a new archive picture or straight to W-blue | "Here's why." (alone, 1 line) | — | — |
| 4–8 | Context | explain | 3–4 archive pictures, 0.9–1.3 s each, or the first receipt (P-SOURCE-CARD) on W-blue | chunks as spoken | — | — |

Weighted SCs in 0–3 s: re-crop, chunk 2, stinger enter, stinger cover event, picture 2 cut, chunk 3, chunk 4 = **7** (target ≥ 7). The v02 variant swaps the stinger for **P-ARCHIVE-FLURRY** (three stills in 0.9 s: 0.30 / 0.20 / 0.40 s, three different treatments) followed by a live clip with a punch re-crop at 1.9 s; use it when the subject is a *place, sport or era* rather than a person.

**Never** open on W-blue text alone in HA-11 (that is HA-12), never put a title over the f0 picture, and never let the hook run past 4.0 s before the turn line.

#### 6.2b F-B: **HA-14 Cold authority**
| t | Beat | Visual | Caption (CS-B) | Shots |
|---|---|---|---|---|
| **f0** | Mid-thought | The speaker who says the strongest line, single (cam A or B), live; no graphic | chunk 1 at f0 (≤ 2 f) | shot 1, `cut_reason: open` |
| 0–1.0 | Strongest line | Same single | chunks 1–2 | no cut |
| 1.0–6.0 | Development | Same single; a ×1.2 re-crop at 4–6 s if the turn continues (R-3) | as spoken | ≤ 1 cut |
| first handover | Second voice | Cut to the other person on their first word (R-1) | guest chunks in italic | handover |
| ≥ 8 s | Rhythm | Handover cuts, 1.2–2.2 s reactions, re-crops ≤ every 6 s | | |

No music, no title, no zoom preset; the authority is the person and the sentence.

### 6.3 Allowed alternates `[DNA list; VAR per reel]`
**HA-12 Receipt open (F-A)**: when the story *is* a document or announcement and no strong subject picture exists.
| t | Visual | Caption |
|---|---|---|
| f0 | W-blue; P-SOURCE-CARD outlet line scrambling in, headline line 1 typing (7 f per line) | chunk 1 at f0 |
| 0.7 | headline complete | chunk 2 |
| 1.2–2.0 | key span turns lime on its spoken word; leader dot + line draw | chunk 3 |
| 2.0–3.0 | first thumb pops (the subject), thesis complete (`payoff: true` on the card) | chunk 4 |
| 3.0 | hard cut to archive (the HA-11 rhythm from here) | "Here's why." |
Example (business): "<Company> / told investors / it will stop / selling <X>." Example (places): "<City> council / just voted / to ban <X>."

**HA-07 Number open (F-A)**: when the thesis is a number ("$20 billion", "211 votes", "3 out of 4").
| t | Visual | Caption |
|---|---|---|
| f0 | W-green; P-COUNTER-CARD rolling from 0 (`kind: counter`) | the claim, chunk 1 |
| ≤ 1.0 | counter lands on the spoken number (±5 f), lime rule wipes 6 f | chunk 2 |
| 1.0–3.0 | hard cut to the subject (archive) + the twist chunk | chunks 3–4 |
Example (business): "$40 billion / is what <Company> / just paid / for a company / with no revenue." Example (places): "211 countries / vote on this, / and one man / decides."

**HA-19 Place open (F-A)**: when the subject is a place or an era.
| t | Visual | Caption |
|---|---|---|
| f0 | full-bleed archive clip or still of the place (Ken Burns), a one-word place chip (T-PLATE, e.g. "JAPAN, 1870s") at y 1180 | chunk 1 |
| 0.6–2.5 | P-ARCHIVE-FLURRY (3 stills) | chunks 2–3 |
| ≤ 3.0 | the premise complete; P-LOCATOR-CARD may follow at the turn | chunk 4 |
Example (places): "Japanese baseball / looks a lot / different / than American baseball." Example (business): "<Town> / makes half / the world's <X>."

**HA-03 Question over the stack (F-B)**: when the clip starts with one person asking the other a sharp question.
| t | Visual | Caption |
|---|---|---|
| f0 | Stack shot (asker top, answerer bottom, seam y 960) for 2.7–4.0 s (hand-edit `timeline.shots[0]` into a stack: §9.3 R-5); **P-B-QUESTION-PLATE** above the seam | the question, on the seam |
| 2.7–4.0 | Cut to the answerer single on their first word | answer chunks |

### 6.4 Hook pairs by topic `[NICHE: example]` (pair type **thesis → scene promise**)
| Niche | Topic | Thesis (≤ 3 s) | The scene / object that carries it | Stinger object |
|---|---|---|---|---|
| Business & brands | A company's surprise move | "<Company> just <bought / banned / launched> <X>, and it involves <rival or regulator>." | Founder / CEO photo → the announcement receipt | banknote rows |
| Business & brands | A price that changed | "<Product> costs <2×> what it did in <year>. Here's who's behind it." | Product plate → P-BAR-TRACKS of the two prices | price tags |
| Business & brands | A founder's comeback | "<Founder> was fired from <Company>. <N> years later, they bought it back." | Two dated photos, same face | folded newspapers |
| Places & history | Why a border is where it is | "<Country A> and <Country B> share a border nobody can cross. Here's why." | Locator card with the line drawn in `bad` | none: T-03 roll-by of a pin |
| Places & history | Why a city looks the way it does | "<City> has no <skyscrapers / cars / …>, and it's on purpose." | Archive street photo → date plate of the rule | building blocks |
| Places & history | An old event still shaping today | "In <year>, <event>. It still decides <present thing>." | Date plate → archive photo → today's photo | ticket stubs |
F-B pairs are in-point choices: "the line that works alone" → "the person who says it, single, at f0". Write the pair for every new topic at P7 and append it here (Part D.6).

### 6.5 Headline writing (the first 1–3 chunks)
**Formula:** `<Subject named concretely> + <what it did, plain past-tense verb> + <the twist>`, said in the first 3 s, chunked 2–5 words. The post title (outside the video) repeats the thesis in ≤ 9 words.
| Template | Example |
|---|---|
| **Name + move + twist** (default) | "The King of FIFA / just launched / a new scheme / to make money, / and it involves / Donald Trump." |
| **Place + difference + why** | "Japanese baseball / looks a lot / different / than American / baseball. / Here's why." |
| **Number + owner** | "$20 billion / is about to / change hands. / Here's who / gets it." |
| **Then / now** | "In 1998, / this was illegal. / Today it's / everywhere." |
Rules: the subject is always named (never "this guy", "this company"); the twist is a concrete noun; no question as the first chunk in F-A (questions are the re-hook's job); no hype words ("insane", "crazy", "you won't believe"). Write 3 and pick by ST-1, ST-2 and ST-4.

### 6.6 Hook sound
F-A: the bed runs from f0 (a documentary pulse under the voice); the only hook cue is on the stinger's cover peak. F-B: dry (room tone only). See §11.

### 6.7 CTA `[DNA device set; VAR values]`
| Device | Spoken pattern (last line) | On screen | Hold | Placement |
|---|---|---|---|---|
| `subscribe` (Follow) | "For more <topic A> and <topic B>, decoded, follow {{BV-01.handle|@yourhandle}}." | P-END-TAGLINE with the Follow → Following pill | 2.0–3.5 s | end |
| `end_card` (wordmark only) | the tagline line | P-END-TAGLINE without the pill | 2.0–3.0 s | end |
| `link_bio` | "The full story is linked in my bio." | P-END-TAGLINE with a lime "link in bio" box (or P-END-QR without the QR) | readable ≥ 1.5 s | end |
| `comment_keyword` | "Comment {{BV-08.keyword|KEYWORD}} and I'll send you <the deliverable>." | P-END-TAGLINE with "Comment" + the keyword in a lime box, mono 700 56 px | ≥ 1.5 s | end |
| `qr` | "Watch the full conversation at <url>." (or text only, §25.3) | P-END-QR | 2.0–3.0 s | end |
| `cross_promo` | "Watch the full deep dive over on my channel." | P-WATCH-FULL (1.5–2.5 s) **before** the end card | 1.5–2.5 s | end |
Silence before the CTA: the last body sentence ends, then ≥ 0.25 s, then the CTA line. One device per reel (cross-promo may precede it). The chosen device is `{{BV-08.device|subscribe}}`.

---

## §7 Structure & cadence `[DNA]`

### 7.1 Structure types
**F-A `explainer`:** thesis (0–3 s) → turn ("Here's why", 3–4 s) → context (who / where / when, 4–12 s) → receipts (escalation: 2–4 receipts or named people, 12–35 s) → **re-hook** ("Now why…", 20–30 s) → comparison or mechanism (side A vs side B, the money flow, the map) → payoff (the answer to "why", one card or one picture) → wrap line → CTA.
**F-B `conversation`:** strongest line (f0) → development by the same speaker → second voice (agreement, push-back or a question) → back to the first voice → the button (the quotable conclusion) → tail → end card.

### 7.2 Markers
- F-A: **SM-SIDE-CHIPS** is the only marker: in a comparison every card carries its side chip (`side_a` red / `side_b` off-white + the trait word), and the two sides always alternate A, B, A, B. Lists inside an explainer are spoken only (no numerals on screen).
- F-B: `markers: none` (spoken only).

### 7.3 Unit ritual (F-A receipt beat; identical every time)
1. Hard cut to an **empty** W-blue on the chunk that names the source ("reports say", "according to", "a new filing shows") (0 f); nothing for 4 f (v01 @7.93–8.05).
2. Headline types on **word by word**: a new word every 2–3 f, each entering at 40 % (`muted`) and brightening to white over 4 f (≈ 10 words in 0.75 s, faster than the voice); the outlet line's letters appear in seeded random order over 14–18 f alongside it (v01 @8.09–8.80).
3. On the first word of the key span: non-key words → `muted`, key span → `accent` (6 f); lime dot pops (4 f); leader line draws (12 f).
4. On the next named person or figure: body copy fades in (8 f) with its spoken figure in lime; thumbs **fade** in (0 → 100 % over 6 f, no scale; 4 f stagger) for each named person; the block follow-pushes (G-4, 24–27 f).
5. Hold until the voice leaves the source; hard cut out. A receipt never shows more than 16 s (v01 held one 15.3 s, @7.9–23.3); events inside it every ≤ 2.0 s.

**Comparison ritual (P-COMPARE-SWIPE):** card A1 (side_a chip) → deck advance (G-3) → card A2 → … → side change (push-up, G-3) → card B1 (side_b chip) → …; 2.0–4.0 s per card, a whole comparison up to 20 s (v02 @25.36–44.52). Each card: media fades up 14–16 f (G-7), then the chip grows from a 4 px sliver to full width over 6 f, its disc appears, and the trait word's letters resolve in seeded order over 10–12 f (v02 @29.64–30.12); the media may hard-cut to a second clip inside the frame while the chip stays. The trait word is the word the voice uses ("CONSISTENCY", "POWER").

### 7.4 Open loops and re-hooks
- Loops used: the **why loop** ("Here's why." at 3 s, paid by the payoff card); the **who loop** ("and it involves …", paid by the receipts); the **question re-hook** (P-QUESTION-TURN: "Now why is <subject> …?" over a hard cut back to the subject's face, 20–30 s in, beat `rehook: true`).
- F-A is `standard`: exactly one mid-reel re-hook (25–75 % of runtime) and no stretch > 25 s without one before the CTA (V-REHOOK). F-B is `short`: no re-hook obligation.
- Intro cap: the hook (thesis + turn) ≤ 15 % of runtime (≤ 4.0 s on a 45 s reel).

### 7.5 Rhythm and energy curve
- Information only (no comedy beats). Energy rises through *picture density*, not volume: context at ~1 change / 1.3 s → receipts at ~1 event / 1.8 s → the comparison at ~1 card / 2.5 s with chip events → the payoff slows to one picture held 2–3 s (the only slow moment) → the end card.
- F-B: calm holds; the energy is in the handovers; the button line is never cut away from.

### 7.6 Cadence (state changes)
| Token | F-A | F-B | Why |
|---|---|---|---|
| `sc_per_10s` | **8–16** | **5–12** | Captions are primary (weight 1.0): F-A ~8 chunks / 10 s + 3–4 picture cuts (v01 0:08–0:24: a chunk every ~1.0 s); F-B ~7 chunks + 1–2 cuts (v03) |
| `hook_sc_3s` | **7** | **2** | v01 ≈ 9, v02 ≈ 5 changes in 0–3 s; v03 ≈ 2 |
| `max_gap_s` | 2.0 | 3.0 | No picture or caption change longer than this |
| `max_static_s` | 2.5 | 4.0 | Ken Burns / live footage keep frames alive |
| `caption_weight` | 1.0 | 1.0 | primary captions |
| `cuts_per_min` | **15–30** (DNA) | **7–16** | v01 24.7, v02 19.2 · v03 11.2 |
| `median_shot_s` | **0.9–2.2** | **2.0–5.0** | v01 1.08, v02 1.64 · v03 3.1 |

In F-A every hard picture change is declared as a cut (`cuts: [0]` on the incoming full-bleed or card scene) so V-CADENCE counts it; receipts and cards count their internal changes as `events`.

---

## §8 Visual system: archive, receipts, cards, patterns

### 8.1 Graphics role and budget
- **F-A `primary`:** every frame is a picture or a card; numbers become pictures (a counter, bars, a seat arc or the receipt that states them). Per 60 s: archive pictures (B-1) 35–55 % of runtime, receipts (B-2) 15–35 %, maps / cards / figures (B-3…B-5) 10–30 %, stingers ≤ 4, end card 3–8 %. ≥ 4 families and ≥ 8 distinct patterns per 60 s.
- **F-B `minimal`:** three recurring devices only: CS-B captions, the optional name plate (first appearance), the end card. Graphics beyond captions ≤ 10 % of runtime.

### 8.2 Families
| ID | Family | Source class | The creator supplies | Created substitute when not supplied |
|---|---|---|---|---|
| **B-1** | Archive pictures (full-bleed stills and clips) | creator-supplied (own or held), else engine-created plates | Photos and clips of the people, places, objects and events named (SH-1, SH-2), with a credit | P-SILHOUETTE-PLATE, P-OBJECT-PLATE, P-DATE-PLATE (FB-1) |
| **B-2** | Receipts (source headlines, quotes) | engine-created from the script's exact words; or the creator's own screenshot | Article screenshots (SH-3) or the pasted headline text | P-SOURCE-CARD is itself the created recipe (`headline_card`) |
| **B-3** | Maps | engine (schematic today; E-18 later); or the creator's own map image | Map exports (SH-4) | P-LOCATOR-CARD (FB-4) |
| **B-4** | Cards on blue (photo cards, comparisons, strips, plates) | engine frames around creator media or created plates | Photos (SH-1) | created plates inside the same frames |
| **B-5** | Figures on green | engine (`VEOS.data`, bespoke scenes from `plan/figures.json`) | Numbers in the script (always) | — |
| **B-6** | Stingers & overlays | engine-created objects (vector shapes, never photos of real money or brands) | — | — |
| **B-7** | Brand furniture (end cards, cross-promo, credit lines, sponsor) | engine + the creator's logo / thumbnail / QR | SH-8, SH-9, SH-10 | FB-8, FB-9, FB-10 |
| **B-8** | Conversation cuts (F-B) | buyer-owned footage | SH-5, SH-6, SH-7 | FB-5, FB-6, FB-7 |

### 8.3 Pattern specs (30 fps; "f" = frames)
Every scene names its pattern in the beat (`pattern`), its family and its text class. Third-party patterns (marked †) carry `insert` and follow §12.5.

**B-1 Archive**
| ID | Type | On screen | Motion recipe | Use | Text class / needs |
|---|---|---|---|---|---|
| **P-ARCHIVE-BLEED** † | footage-treatment | One archive photo full-bleed (z2, `kind: "archive"`, cover-fit, focus on the face or subject), grade from §4.4, T-CREDIT at y 128 | Hard cut in (`in: "none"`, `cuts: [0]`); a quick **settle** 1.04 → 1.00 over the first 5 f (expo-out; v02 @45.15–45.35 measured −3.8 % in ≤ 5 f, then static), then a barely visible drift ≤ 1 %/s, alternating in / out on consecutive shots; hard cut out. No big Ken Burns: the pace comes from the cuts | Every named person, place, object or event when the creator has the picture | credit TC-legal; face centre y 520–900 |
| **P-ARCHIVE-CLIP** † | footage-treatment | A creator clip full-bleed (`fx.clip`, z2, `kind: "archive"`), grade GR-vhs for old colour video | Hard cut in; plays at 1.0×; no added camera move; one **punch** on the action word: a hard cut to a tighter shot of the same action (v02 @1.88 cuts from the wide wind-up to a waist close-up), or, with one clip only, a ×1.25 re-crop (`cuts: [t]`) | Action: a pitch, a speech, a crowd, a launch | credit |
| **P-ARCHIVE-FLURRY** † | cut | 3 stills in 0.9 s (holds 0.30 / 0.20 / 0.40 s), three different treatments, same subject class | Hard cuts; each still settles 1.04 → 1.00 in 5 f | Hook (HA-11 v02 variant, HA-19), era montages | credit per still |
| **P-RECROP-CUT** | cut | The same picture re-framed | Hard cut from crop 1.18 to 1.00 (or 1.00 to 1.18) mid-hold, on a word onset; Ken Burns continues | Hook f0 + 0.45 s; any hold > 2.0 s on one picture | — |
| **P-SILHOUETTE-PLATE** † | overlay (created) | Full-bleed `navy` field, a 6 px dot halftone (GR-halftone) silhouette bust (head + shoulders, 760 px tall, centred x 540, top y 360) in `land` with a `focus` rim light, T-PLATE name under the chin at y 1180 | Hard cut in; Ken Burns 1.00 → 1.05; the name plate wipes in L → R 8 f at +6 f | A named person with no creator photo (FB-1) | name plate TC-label; `satisfies: ["archive"]`, recipe `silhouette` |
| **P-OBJECT-PLATE** † | overlay (created) | Full-bleed halftone paper (#D9D4C7 × GR-sepia) or navy, one large line icon from `fx.icon` (420 px, stroke 10, ink or paper) of the object / place type, T-PLATE caps label (the noun) at y 1180, T-TAG at y 128 | Hard cut in; icon scale 0.96 → 1.00 over the hold, Ken Burns on the paper 1.00 → 1.04 | A named object, building, product category or place with no photo | label TC-label; recipe `logo_plate` for products, `diagram` for objects |
| **P-DATE-PLATE** | overlay (created) | Full-bleed halftone navy plate, the year or date in T-DATE (display 700, 180 px, white), centred at y 760; a thin `accent` rule 120 × 6 px under it | Hard cut in; digits roll from the previous year mentioned (or count up 8 f) and land on the spoken year (±3 f); hold ≥ 1.0 s | "In 1870 …", "By 2005 …", era jumps | TC-display; number from the script (`figures.json` input) |

**B-2 Receipts**
| ID | Type | On screen | Motion recipe | Use | Text class / needs |
|---|---|---|---|---|---|
| **P-SOURCE-CARD** † | overlay (signature) | On W-blue, no card: T-OUTLET (outlet · date) at y ≈ 360; T-HEAD 70 px, ≤ 3 lines, x 64; lime dot Ø 18 after the last line; leader line 3 px `muted` from the dot left to x 300, corner r 36, down 120 px, then left off the frame edge; T-BODY 3–5 lines right of the corner; 0–3 photo thumbs (h 290, square corners, no border, gap 0, centred, max total width 760); | f0–4 f empty blue; outlet letters appear in seeded order over 14–18 f; headline types **word by word** (a word every 2–3 f, each 40 % → white over 4 f); **highlight** on the key span's first word: non-key words → `muted` and key span → `accent` over 6 f; dot pops 4 f (scale 0 → 1.15 → 1); leader draws 12 f (stroke-dashoffset); body fades in 8 f; thumbs fade in 6 f each (opacity only), 4 f stagger, on each named person; **follow-push** (G-4) ×1.14 over 24–27 f, then a ≈ 1 %/s creep; all receipt motion stepped on twos (§10.1) | Every "according to / reports / announced / a filing shows" line; the evidence beat of the unit ritual §7.3 | headline TC-display, outlet TC-legal, body TC-decorative; `source {masthead, date, headline, highlight_spans}`, `insert`, recipe `headline_card` (created) or `creator_media` (the creator's screenshot shown with `fx.shot` inside the text rect instead of the typed headline) |
| **P-SOURCE-SWAP** † | overlay | A second headline replaces the first in place (same or another outlet) | Old headline + body fade up 8 px and out over 6 f; new outlet scrambles, headline types (as P-SOURCE-CARD); the leader re-draws | A second source within 10 s of the first (v01 0:39: FT → Guardian) | same |
| **P-RECEIPT-RETURN** † | overlay | The same receipt shown again later with a different body span lit | Hard cut in fully built; the new body span turns lime 6 f on its spoken figure | Returning to a source with a new detail (v01 0:34) | same |
| **P-QUOTE-RECEIPT** † | overlay | On W-blue: T-OUTLET slot carries the speaker's name + where they said it; the quote in T-HEAD white between curly quotes, the key span lime; a silhouette or creator photo thumb (240 × 240) at the left under it | As P-SOURCE-CARD; the quote types on word by word at the voice's pace (9 words/s cap) | A person's exact words read aloud | NC-13 verbatim; recipe `quote_card`, `quote_text` |

**B-3 Maps**
| ID | Type | On screen | Motion recipe | Use | Text class / needs |
|---|---|---|---|---|---|
| **P-MAP-CARD** (E-18) | overlay | Card rect r 40: `navy` sea, `land` countries, the focus region `focus`, label chips T-MAPLABEL, logo / pin markers | Card cut-in (G-2); inner punch ×1.5 to the focus on the place word, then a slow pan toward the next focus (G-7; v01 @49.14); a different region is a hard cut to a new map card (v01 @51.6 Eurasia → North America); face cut-outs (no disc) and labels sit on the map from the cut | Any "where" line | **Unavailable until the geo-map bundle ships: use P-LOCATOR-CARD** |
| **P-LOCATOR-CARD** † | overlay (created, today's map) | Card rect (or tall) r 40, `navy` fill, a dotted graticule (dots r 2, pitch 80 px, white 12 %), a north tick "N" (mono 500 24 px, TC-legal) top-right; 1–4 pins (white disc Ø 28 with a 6 px `primary` ring) placed in rough relative position (west → left, north → up), each with a T-MAPLABEL chip; T-TAG "SCHEMATIC" at y 128 | Card cut-in (G-2); graticule fades in 8 f; pins pop 6 f, 4 f stagger, each on its spoken name; the active pin gets a lime ring (6 f); on the second named place an inner punch ×1.5 toward it, then a slow pan (G-7) | Every "where" line until E-18 | labels TC-label; recipe `diagram`; no coastlines, no borders, no distances |
| **P-ROUTE-LINE** | annotation | A dashed line (dash 18 / gap 12, 6 px) between two pins on a locator / map | Draws 14 f from origin to destination; ends in a `good` arrowhead (allowed / went there) or a `bad` × (24 px, blocked); the × pops 4 f | Movement, trade, migration, blocked paths (v02 0:17) | — |
| **P-FACE-PINS** † | annotation | Round avatars (Ø 150, creator photo circle-crop or silhouette disc, 6 px `paper` ring) on pins, a T-MAPLABEL under each | Pop 6 f, 6 f stagger, on each spoken name | Who is where (v01 0:46–0:52) | labels TC-label |
| **P-TOKEN-MIGRATION** | state | 3–6 small portrait tokens (90 × 120, 4 px `side_a` frame) travel along a corridor band (a 40 px `side_a` 35 % stripe) from region A to B | Tokens leave 6 f apart, travel 18 f each (ease_card), settle in a cluster at B | People or products moving from one place to another (v02 0:49–0:55) | — |

**B-4 Cards on blue**
| ID | Type | On screen | Motion recipe | Use | Text class / needs |
|---|---|---|---|---|---|
| **P-PHOTO-CARD** † | overlay | One creator photo (or plate) inside the card or tall rect, r 40, Ken Burns inside the mask | Card cut-in (G-2), hard cuts between consecutive photo cards; media fades up 14–16 f (G-7), then drift ≤ 1 %/s | Two people meeting, an event photo that must not go full-bleed (low resolution) | credit |
| **P-PHOTO-STRIP** † | overlay | 2–3 square-cornered photos side by side (h 300–420, gap 0), centred in the card zone | Each pops 6 f, 4 f stagger, on its name | "<A>, <B> and <C>" lists of people | name plates optional |
| **P-COMPARE-SWIPE** † | overlay (ritual) | Tall rect card filled `primary` darkened 25 % (mix with `navy` 0.35), a soft diagonal light band (140 px, 20°, `primary` lightened 12 %, 40 %) behind; inner media frame x 235 y 450 w 610 h 640, 3 px `side_b` border, r 8; T-CHIP centred on the frame's bottom edge (cy 1090) in `side_a` (side A) or `side_b` (side B) with a 44 px monogram disc and the trait word; the previous card peeks 48 px at the left (60 %) | Deck advance / side-change push-up (G-3); media window fades up 14–16 f with its 3 px border drawn; chip grows 6 f, trait word resolves 10–12 f (§7.3); media plays live | Side A vs side B comparisons (v02 0:25–0:44) | chip TC-label (spoken word, 40 px) |
| **P-NAME-PLATE** | overlay | T-PLATE under a face (bleed picture or photo card), x centred on the face, top = chin + 40 px, max y 1250 | Wipes in L → R 8 f (box first, text 2 f later); exits with its picture | The first time a person appears on screen | TC-label |
| **P-AVATAR-RING** † | overlay | Circular avatar Ø 200 (photo or silhouette disc) with a 6 px ring (paper 60 %), entering a figure or map | Rises 10 f from behind the figure's lower edge (masked, `ease_card`; v01 @25.66–26.03), ring visible from the start | The person who controls a figure (v01 0:26) | name plate under it |

**B-5 Figures on green** (all values from `plan/figures.json`, written with `ctx.fmtNum`)
| ID | Type | On screen | Motion recipe | Use | Text class / needs |
|---|---|---|---|---|---|
| **P-SEAT-ARC** | figure | Card rect on W-green (`data_card`, r 40): a half-circle seat chart (centre 540, 1010; r 170–400), wedges per group with T-MAPLABEL-style labels (≤ 6 groups at 40 px; more groups → a legend row), one dot (r 6) per seat; P-AVATAR-RING in the middle | Card hard-cuts in with the arc built (v01 @25.37); the avatar rises on its name; on the member count an inner punch ×1.8 onto the avatar + nearest wedges, then pull-out ≈ 0.15 %/f (G-7, v01 @29.97); optional token flow (P-FLOW-TOKENS) | Votes, members, seats, shares of a body (v01 0:25–0:33) | figure `seat` kind `grid_fill`; labels TC-label |
| **P-FLOW-TOKENS** | figure | Small chips (amount via `fmtNum`, mono 700 40 px on `data_card` lighter pill) flying from a source to N targets | Each token 12 f arc, 3 f stagger; the amount lands on the spoken figure | Money or votes moving | figure `flow` |
| **P-BAR-TRACKS** | figure | `VEOS.data.bars` restyled: 2–4 tracks (row h 96, track `data`, bar = `data_card` mixed 45 % with paper, radius 48), icon or avatar at the left, value at the bar end (T-FIG 72 px) | Bars grow 18 f on one shared scale; values roll and land on the spoken number | Two to four quantities compared (v01 1:12) | V-DATA same scale |
| **P-COUNTER-CARD** | figure | `VEOS.data.counter` on a card: T-FIG 140–160 px white, a mono 700 40 px unit line under it, a lime rule 6 px that wipes under the number when it lands | Roll 18 f, lands within ±5 f of the spoken number | One hero number; HA-07 | `kind: counter` |
| **P-TIMELINE-RAIL** | figure | A horizontal rail (6 px `muted`) across the card with year ticks; the active year in a lime pill (mono 700 40, ink) | The pill slides to each spoken year 10 f; ticks pop 4 f | Sequences of dated events (inferred: the evidence uses date captions instead) | years from the script |

**B-6 Stingers & overlays**
| ID | Type | On screen | Motion recipe | Use | Text class / needs |
|---|---|---|---|---|---|
| **P-STINGER-STACK** | transition (created) | 4 overlapping rows of one created topical object filling the frame (generic banknote shapes with no real currency art, ticket stubs, folded newspapers with illegible texture, balls, crates), each row offset 40 px | The stacked block rises from y 1920 as one mass, accelerating (ease-in), covers the frame by f 16, holds 6 f, then lifts off the top decelerating (ease-out) over 16–18 f, no blur; the next picture is cut underneath at cover and is revealed bottom-up; the caption stays on top (measured v01 @1.09–2.43) | The hook (once) and at most 2 more topic turns per 60 s | no text; `events` at cover and exit |
| **P-ROLL-BY** | transition (created) | One created object (a ball, a coin, a wheel) **bigger than the frame width** (Ø ≈ 1150 px) | Enters from the bottom edge, flies up and slightly right, exits the top in 9 f with ≈ 120° rotation; the cut happens under it at its mid-pass (f 4–5) (v01 @4.43–4.72) | A lighter topic turn inside the body (v01 0:04.5) | no text |
| **P-PARTICLE-OVERLAY** | overlay (created) | 24–30 seeded flakes (confetti strips 14 × 34 px or coins Ø 26) in `accent` / gold #E8C547 at 70 %, drifting down 60–120 px/s with spin | Continuous over a celebration picture, 1.5–3.0 s, fades out 8 f | Wins, money, ceremony (v01 0:02–0:04) | z5, `ambient`-free (≤ 30 items, small); never over a face box |
| **P-QUESTION-TURN** | cut (re-hook) | Hard cut back to the subject's face (bleed) with the question as the caption | Hard cut; settle 1.04 → 1.00 in 5 f, then near-static (v01 @23.27) | The mid-reel re-hook "Now why is …?" (v01 0:24) | beat `rehook: true`, scene `kind: "rehook"` |

**B-7 Brand furniture**
| ID | Type | On screen | Motion recipe | Use | Text class / needs |
|---|---|---|---|---|---|
| **P-WATCH-FULL** † | overlay | W-white; a video card x 120 y 520 w 840: thumbnail 840 × 472 r 18 (the creator's own thumbnail SH-9, or FB-9 title field), title body 700 44 px ink below (y 1020), channel line mono 500 26 px #5A5A5A (TC-legal, the creator's name, no view counts); a cursor (64 px arrow, ink with paper outline) | Card rises 9 f; cursor glides from (900, 1300) to the thumbnail centre over 18 f (ease_card), clicks at +0.6 s: card scales 0.97 → 1.00 over 6 f | Cross-promo of the creator's long video before the end card (v01 1:14–1:16) | title TC-label; captions show as a grey box on white (CS-A 70 % black) |
| **P-END-TAGLINE** | overlay | §25.2 | §25.2 | F-A end (and F-B with `subscribe`) | §25 |
| **P-END-QR** | overlay | §25.3 | §25.3 | F-B end (and F-A with `qr`) | §25 |
| **P-SPONSOR-SOURCE** | overlay | A sponsor segment built like a receipt: the sponsor's name set in type in the outlet slot, their line as the headline (key span lime), a "Paid partnership" T-TAG at y 128 held through the segment | As P-SOURCE-CARD | Paid integrations (inferred) | NC-12 disclosure |

**B-8 Conversation cuts (F-B)**
| ID | Type | On screen | Motion recipe | Use | Text class / needs |
|---|---|---|---|---|---|
| **P-B-SINGLE-HOLD** | cut | The speaker single, face ≈ 17 % of frame height, head top y 140–300 | Holds 4.0–6.0 s; live footage | The default picture | — |
| **P-B-HANDOVER-CUT** | cut | Cut to the new speaker's single | 0 f, 1 f before their first word (±3 f) | Every handover (R-1) | V-SPEAKER |
| **P-B-REACTION** | cut | The listener's single while the speaker continues | 1.2–2.2 s, not in the first 1.0 s of a turn, not in the last 1.0 s before a handover | A back-channel ("right", "yeah"), or once per ≥ 8 s turn (R-2) | caption stays the speaker's |
| **P-B-RECROP** | cut | The same angle re-framed ×1.2 (or back to ×1.0) | Hard cut on a word onset | A turn longer than 6 s (R-3) | — |
| **P-B-WIDE** | cut | The wide two-shot (cam W) | 1.5–4.0 s, once, in the last third, on a sentence start | Room establish before the button (R-4, v03 0:32) | — |
| **P-B-STACK** | cut | 50/50 stack: speaker top, listener bottom, seam y 960, hairline 0; caption on the seam | Generator-placed or hand-edited; 3.0–6.0 s | Rapid exchanges (≥ 3 handovers in 6 s) and HA-03; ≤ 12 % of runtime (R-5) | captions on seam |
| **P-B-QUESTION-PLATE** | overlay | The question in mono 700 40 px white on a `primary` box (padding 12 × 20), max 2 lines, centred at y 860 (above the seam) | Wipes in L → R 8 f; out with the stack | HA-03 only | TC-label |
| **P-B-NAME-PLATE** | overlay | Two lines at x 64, y 1180: name (mono 700 40 caps, white on `primary` box) + role (mono 500 24 px, TC-legal) | Box wipes L → R 8 f, text 2 f later; holds 2.0 s; out 6 f | Each speaker's first appearance, only when the clip has a guest the audience may not know (inferred; 0–2 per reel) | TC-label |

**Pattern count:** 43 (F-A 33 + shared end cards 2 + F-B 8).

### 8.4 Line → pattern lookup `[NICHE: example niches "Business & brands" and "Places & history"]`
| Line type (what the sentence does) | Primary | Alternates |
|---|---|---|
| Names a person ("<Name>, the founder of…") | P-ARCHIVE-BLEED + P-NAME-PLATE (first appearance) | P-SILHOUETTE-PLATE, P-PHOTO-CARD |
| Names a company, product or brand | P-OBJECT-PLATE (logo_plate: the name set in type) | P-ARCHIVE-BLEED of the creator's own product photo |
| Names a place ("in <City>", "across the border") | P-LOCATOR-CARD (pins) | P-ARCHIVE-BLEED of the place, P-MAP-CARD (E-18) |
| A date or era ("In 1998…") | P-DATE-PLATE | P-ARCHIVE-FLURRY with GR-sepia |
| Cites a source ("reports say", "according to", "announced") | **P-SOURCE-CARD** | P-SOURCE-SWAP, P-RECEIPT-RETURN |
| Quotes someone | P-QUOTE-RECEIPT | P-ARCHIVE-BLEED of the speaker + caption only |
| States one number | P-COUNTER-CARD | the receipt that states it (key span = the number) |
| Compares two quantities | P-BAR-TRACKS | P-COUNTER-CARD × 2 on one card |
| Shares / votes / members | P-SEAT-ARC | P-BAR-TRACKS |
| Money moves from A to B | P-FLOW-TOKENS | P-ROUTE-LINE with amount chips |
| People or goods move between places | P-TOKEN-MIGRATION | P-ROUTE-LINE |
| Something is blocked / forbidden | P-ROUTE-LINE ending in `bad` × | P-OBJECT-PLATE + `bad` rule |
| "A vs B" traits (styles, cultures, strategies) | **P-COMPARE-SWIPE** (SM-SIDE-CHIPS) | P-PHOTO-STRIP with chips |
| Who is connected to whom | P-PHOTO-STRIP (thumbs inside a receipt) | P-FACE-PINS |
| An action happening (a launch, a match, a protest) | P-ARCHIVE-CLIP | P-ARCHIVE-BLEED + P-RECROP-CUT |
| Celebration, win, payout | P-ARCHIVE-BLEED + P-PARTICLE-OVERLAY | — |
| Topic turn ("But…", "Meanwhile…") | P-STINGER-STACK (≤ 1 outside the hook) | P-ROLL-BY, hard cut |
| The mid-reel question | P-QUESTION-TURN | — |
| Sequence of dated events | P-DATE-PLATE per date | P-TIMELINE-RAIL |
| "Watch the full…" | P-WATCH-FULL | — |
| The CTA | P-END-TAGLINE / P-END-QR (§25) | — |
| Business example lines | "They raised $40 million" → P-COUNTER-CARD; "a filing shows…" → P-SOURCE-CARD; "its two rivals" → P-COMPARE-SWIPE | |
| Places example lines | "the river that splits the city" → P-LOCATOR-CARD + P-ROUTE-LINE; "the 1923 earthquake" → P-DATE-PLATE → P-ARCHIVE-BLEED | |
| **F-B** any line | P-B-SINGLE-HOLD; a handover → P-B-HANDOVER-CUT; a back-channel → P-B-REACTION; a > 6 s turn → P-B-RECROP | P-B-STACK for rapid exchanges |

### 8.5 Data and truth rules
Pointer: §18. Quantities are drawn countable (one dot per seat up to 600, then one dot per N with a "1 dot = N" legend TC-legal); compared figures share one scale; every number comes from the script (or a verbatim headline); illustrative charts carry the `example` tag; no invented view counts, dates or percentages anywhere (including the cross-promo card).

### 8.6 Comedy layer: OFF (`tone.comedy: off`). No stickers, stamps, emoji, meme cues or freeze-frames.

### 8.7 Asset rules
- Real pictures first: the creator's own or held photos and clips. Ask once (§12.5).
- Created plates are clearly designed objects (halftone silhouettes, icons, type), never fake photos, never AI images of real people, and always.
- Logos of other companies: never drawn; the name is set in type (P-OBJECT-PLATE `logo_plate`).
- Flags: never drawn from memory; side chips use monogram discs (two-letter country or team codes set in type).
- Banknotes, tickets and newspapers in stingers are generic shapes with illegible texture: no real currency, mastheads or serial numbers.

### 8.8 Density and variety
- F-A: an SC every 0.6–1.25 s on average (captions + pictures); ≥ 8 distinct patterns and ≥ 4 families per 60 s; the same pattern ≤ 3 times in a row except the comparison ritual and archive runs (an archive run may be up to 6 consecutive P-ARCHIVE-BLEED shots if their treatments alternate).
- F-B: one picture device (cuts); the cut types rotate (never 3 re-crops in a row).

---

## §9 Transitions & shot grammar `[DNA]`

### 9.1 Library
| ID | Transition | Frames | Recipe | Cue role |
|---|---|---|---|---|
| **T-01** | Hard cut | 0 | Incoming scene `in: "none"`, `cuts: [0]`; on a chunk boundary or a noun onset ±2 f | silent |
| **T-02** | Stinger stack | 38–40 | P-STINGER-STACK: rise 16 f (ease-in), hold 6 f, lift-off 16–18 f (ease-out); the cut happens under full cover | whoosh (transition) on the rise, cue on the cover peak |
| **T-03** | Roll-by | 9 | P-ROLL-BY: an oversized object flies bottom → top; the cut happens under it at f 4–5 | swish |
| **T-04** | Deck advance / side push-up | 0 / 4 | G-3: the next comparison card hard-cuts on top (the previous one peeks left); a side change is the built-in `push` (`dir: "up"`, `frames: 4`) | silent (the chip may carry a reveal cue) |
| **T-05** | Evolve in place | 6–27 | Inside a receipt or card: word type-on, highlight, follow-push, thumbs, pins, inner punch + drift (G-4, G-7; declared `events`) | reveal cue on the lime highlight (≤ 1 per receipt) |
| **T-06** | End cut + build | 0 | Hard cut to W-end; the logo row rises and the tagline resolves (§25.2) | the CTA cue on the pill change |
| **T-07** | Punch | 0 | A hard cut to a tighter shot of the same action (P-ARCHIVE-CLIP), a ×1.18–1.25 re-crop (P-RECROP-CUT), or an inner card punch ×1.5–1.8 (G-7) | silent |
| **T-08** | Handover / shot cut (F-B) | 0 | `timeline.shots` boundary | silent |
| **T-09** | Hard end | 0 | The last frame ≤ 6 f after the last word; black tail ≤ 0.2 s | — |
Share in F-A (measured, v01 + v02: 58 picture changes at scene threshold 0.2): ≈ 75 % T-01, ≈ 10 % T-07, ≈ 5 % T-02 / T-03 (1 stack + 1 roll-by in v01, none in v02), ≈ 5 % T-04, 2 × T-06 (both hard cuts). Between cuts, T-05 evolves carry the long card stretches (15–19 s on one receipt or deck). No dissolves, fades, whips or flashes anywhere in the evidence.

### 9.2 Grammar
| Boundary | Use | Never |
|---|---|---|
| f0 | Already-moving archive picture + first chunk (no transition) | A fade-in, a stinger, a title |
| Hook → body | T-02 once (at the verb of the thesis), then T-01 | A cross-dissolve |
| Archive → archive | T-01 on the next chunk boundary; alternate Ken Burns direction | Two pictures with the same treatment and the same Ken Burns direction back to back |
| Archive → receipt (W-blue) | T-01 on the source word ("reports", "according") | A stinger into a receipt |
| Inside a receipt | T-05 evolves only | A cut while the headline is still typing |
| Card → card (same topic) | T-01, or T-04 inside a comparison | Sliding, rising or fading a card in (cards cut; only their contents move) |
| Topic turn ("But", "Meanwhile", "Now") | T-02 (≤ 1 outside the hook) or T-03, or P-QUESTION-TURN for the re-hook | Two stingers within 8 s |
| Number lands | T-05 (counter landing + lime rule) | A cut before the number has held 0.8 s |
| Last body line → end card | T-06 (F-A tagline) or T-01 (F-B / QR) | A dissolve or a black frame between |
| Last word | T-09 | A black tail > 0.2 s |

### 9.3 Shot grammar R-… (F-B; the turn generator with this style's `dialogue.cut_rules`)
| ID | Rule | Numbers |
|---|---|---|
| **R-1** | Cut on the first word of a new speaker | 1 f lead, ±3 f; never inside a word |
| **R-2** | Listener reaction cutaway | 1.2–2.2 s; on a back-channel, or once in a turn ≥ 8 s; never in the first 1.0 s of a turn or the last 1.0 s before a handover |
| **R-3** | Jump re-crop on the same angle | ×1.2 (step 1.0 ↔ 1.2) when a hold reaches 4.0–6.0 s |
| **R-4** | Wide establish | 1.5–4.0 s once, in the last third, starting on a sentence start, if cam W (or a faux wide) exists; hand-edit one `timeline.shots` entry to the wide angle with `cut_reason: "recrop"` |
| **R-5** | Stack exchange | 3.0–6.0 s per stack shot, ≤ 12 % of runtime; the stack opener is off (`open_s: [0, 0]`): the clip opens on the speaker single. Hand-edit a stack only for HA-03 or ≥ 3 handovers within 6 s |
| **R-6** | Max hold | 6.0 s single (7.0 s hard limit with the SPK-6 tolerance); the generator rotates re-crop → reaction → stack |
| **R-7** | Button protection | No cut in the final sentence (the button) unless it is a handover |
| **R-8** | Min shot | 1.0 s (except a handover) |
F-A has no shot grammar (the spine is audio); its cut rules are §9.2.

### 9.4 Budget (per 60 s)
- F-A: T-02 + T-03 ≤ 3 together (evidence: 2 in 80 s, both in the first 5 s; 0 in v02), T-02 at most once outside the hook, T-04 per comparison card, T-07 ≤ 4, T-06 once. The same transition ≤ 3 times in a row except T-01 (hard cuts are the grammar).
- F-B: cuts 7–16 per minute; ≤ 2 stack shots; 1 wide.

---

## §10 Motion, camera, layers, finishing `[DNA; motion tokens TUNE ±15%]`

### 10.1 Motion tokens
| Token | Value |
|---|---|
| Beat lead | 2 f before the trigger onset (captions 1 f) |
| Entry ease | `cubic-bezier(0.22, 1, 0.36, 1)` (expo-out) |
| Card ease (`ease_card`) | `cubic-bezier(0.33, 0, 0.15, 1)` |
| Exit ease | `cubic-bezier(0.64, 0, 0.78, 0)`, 4–6 f (most exits are hard cuts) |
| Archive settle | 1.04 → 1.00 over 5 f (expo-out) at the cut, then drift ≤ 1 %/s, alternating in / out; focus = the face or subject point (measured: v02 @45.15 −3.8 % in ≤ 5 f; v01 hook face 0.4 %/s). There is **no** 6 %-per-hold Ken Burns in the evidence |
| Graphics on twos | every graphic scene (receipts, type-on, follow-push, inner pans, chips, avatar, end card) sets `step_fps: 12` (poses held 3 and 2 frames at 30 fps; G3 judges each pose) (v01 receipt and push frames repeat in pairs at 23.98 fps, @8.43–8.76, @14.52–15.40). Archive clips (P-ARCHIVE-CLIP, P-ARCHIVE-STILL) and the built-in transitions run at full rate: no `step_fps` on them |
| Type-on | word by word: a word every 2–3 f, each 40 % → 100 % over 4 f; outlet letters in seeded order over 14–18 f |
| Highlight | 6 f colour cross-fade (white → muted, white → accent) |
| Leader draw | 12 f; dot pop 4 f (0 → 1.15 → 1) |
| Thumb in | 6 f opacity 0 → 1, no scale, 4 f stagger |
| Follow-push (G-4) | ×1.14 (1.10–1.16) + translate to frame the newest element, 24–27 f sine in-out, then creep ≈ 1 %/s |
| Inner punch (G-7) | ×1.5 (maps) / ×1.8 (figures), 0 f, then pull-out 0.15 %/f or pan ≈ 9 px/f |
| Media fade-up | 14–16 f from 35 % over `primary` to 100 % |
| Chip grow | 6 f width 4 px → full; trait word letters resolve over 12 f (`fx.resolve`, `dur: 0.4`, seeded) |
| Side push-up | 4–6 f, `ease_exit` |
| Counter roll | 18 f, lands ±5 f on the number word |
| Stinger | rise 16 f ease-in, hold 6 f, lift-off 16–18 f ease-out (38–40 f) |
| Roll-by | 9 f bottom → top, Ø ≈ 1150 px |
| Idle drift | cards and receipts keep moving through G-4's creep or G-7's drift (continuous motion, keeps `max_static_s`) |
| Hold | titles / labels ≥ 10 f after they finish; text ≥ 0.25 s per word |

### 10.2 Footage camera
- **F-A `zoom_policy: none`:** there is no footage camera; all movement is scene-internal: the archive settle, re-crop cuts (P-RECROP-CUT), the receipt follow-push (G-4) and the inner card punch + drift (G-7). No camera presets, no shake, no rotation (ORB rotation < 0.3° on every measured move).
- **F-B `zoom_policy: crop_on_cut`:** the only "zoom" is the ×1.2 re-crop at a cut (R-3). No push-ins, no shakes, no crash zooms.

### 10.3 Canvas camera: OFF (§21). The receipt's settle-up and the map card's inner pull are scene-internal motions.

### 10.4 Layer order (back to front)
1. World (W-blue / W-green / W-white / W-end / W-qr; F-B footage)
2. Full-bleed archive pictures and plates (z2, opaque)
3. Cards: photo, map / locator, comparison, figure (z3)
4. Receipt text blocks, figure values, inner media (z4)
5. Overlays: particles, name plates, chips, avatars (z5)
6. Stingers and roll-bys (z6, momentary)
7. Captions (`__subtitles`, z7)
8. Credit line, when used (z6 in the top slot; never overlaps the band)
9. End card (z10 on L-end)

### 10.5 Finishing
- W-blue and W-green carry 3 % film noise (static texture); W-end 5 %. No vignette, no light leaks, no bloom, no grain on footage.
- Card radius 40 (photo cards, maps, figures); inner media radius 8; thumbs and caption boxes square (radius 0).
- Shadows: cards `0 26px 70px rgba(0,0,0,.28)` on W-blue only; nothing else has a shadow except the CS-B text shadow.

---

## §11 Sound contract (minimal) `[VAR]`
| Line | F-A | F-B |
|---|---|---|
| **Cue moments** | hook (the stinger's cover peak), transitions (stingers and roll-bys only), reveals (the lime highlight of a receipt: ≤ 1 per receipt; a counter landing; a pin on the payoff map), cta (the Follow → Following change) | cta only (the QR card's entrance) |
| **Meme cues** | off (`comedy: off`) | off |
| **Music bed** | on, from f0 (a low documentary pulse under the hook), ducked; drops out 0.5 s before the payoff picture and returns on it | off: the room tone of the conversation is the bed |
| **Ducking** | bed ≥ 18 dB under the voice while it speaks | the creator's dialogue mix is kept; nothing is added under it |
| **Loudness** | −14 LUFS integrated, true peak ≤ −1.5 dBTP, hard end ≤ 6 f after the last word | same |
Which sounds, their vibe and density come from the bundled SFX pack and its global rules S1–S6 (`tone.energy: balanced`). F-B sets `timeline.audio.bed: null`.

---

## §12 Footage, shot list, fallbacks, inserts

### 12.1 Setups `[DNA what the style assumes; VAR the buyer's setups]`
| Setup | F-A voice-over (VO) | F-B two-camera conversation (POD) |
|---|---|---|
| Capture | Close dynamic or small-diaphragm condenser mic, 15–20 cm, pop filter; a dry room (no echo) | Cam A host single and cam B guest single at eye height, 3/4 angles, eyelines off-camera toward each other; optional cam W wide two-shot; one mic per person (dynamic on arms, visible is fine) |
| Delivery | A steady news read, 2.6–3.0 words per second, sentences of 8–16 words; record paragraph by paragraph | Natural conversation; the creator marks the moments worth clipping |
| Framing | — | Head-and-shoulders singles with room above the head; 16:9 4K (or vertical 1080 × 1920) so 9:16 crops keep a head top at y 140–300 |
| Light / set | — | Warm practicals, depth behind each person (shelves, lamps, maps); the set is the "archive" mood |
| Rate | 48 kHz WAV | 30 fps (or 25/60 conformed), all cameras the same rate |

### 12.2 Shot list
| ID | Shot | Spec | Count per 60 s | Must / optional | Formats |
|---|---|---|---|---|---|
| SH-1 | Archive / reference photos the creator owns or holds | ≥ 1080 px short side for full-bleed; faces, places, objects, documents | 8–15 | optional (fidelity) | F-A |
| SH-2 | Archive / B-roll clips the creator owns or holds | 2–8 s each, ≥ 720p (cards) / 1080p (full-bleed) | 2–6 | optional | F-A |
| SH-3 | Screenshots of the cited articles, taken by the creator | full headline visible, outlet and date visible | 0–3 | optional | F-A |
| SH-4 | Map images the creator exported or owns | locator, route or region; ≥ 1080 px wide | 0–3 | optional | F-A |
| SH-5 | Cam A: host single | 4K 16:9 or vertical 1080p; the whole clip | the whole clip | **must** | F-B |
| SH-6 | Cam B: guest single | same height and lens as cam A | the whole clip | **must** | F-B |
| SH-7 | Cam W: wide two-shot | locked off, both people, the room | the whole clip | optional | F-B |
| SH-8 | Brand logo (PNG / SVG, transparent) | square-safe, ≥ 512 px | once | optional | both |
| SH-9 | Thumbnail + title of the creator's own long video | 1280 × 720 | once | optional | F-A |
| SH-10 | QR image of the creator's URL, or the URL | PNG / SVG | once | optional | both |

### 12.3 Fallbacks
| ID | For | What the engine does instead | Fidelity cost | Format holds? |
|---|---|---|---|---|
| FB-1 | SH-1 | Created archive plates: P-SILHOUETTE-PLATE (people), P-OBJECT-PLATE (things, places, products), P-DATE-PLATE (years), all GR-halftone | No real faces or places; the montage reads designed rather than documentary | degraded |
| FB-2 | SH-2 | A still (SH-1) or a plate with the settle + a 1.00 → 1.03 drift | No live motion inside the shot | degraded |
| FB-3 | SH-3 | The created P-SOURCE-CARD (outlet set in type, the exact headline from the script or the creator) | None visible: this is the style's own card | holds |
| FB-4 | SH-4 | P-LOCATOR-CARD (schematic) until the geo-map bundle (E-18) ships | No coastlines or borders | degraded |
| FB-5 | SH-5 | A faux single cropped from cam W or the one camera there is (E-13b two crops) | Softer image, no angle change on handovers | degraded |
| FB-6 | SH-6 | A faux guest single from cam W (E-13b) | Softer image, reactions share one angle | degraded |
| FB-7 | SH-7 | Skip R-4 (no wide); end on the speaker single | No room establish | holds |
| FB-8 | SH-8 | A typeset monogram disc: the creator's initials in Montserrat 800 on a `primary` disc | No logo artwork | holds |
| FB-9 | SH-9 | A created video card: the long video's title set in type on a `primary` thumbnail field (no image, no view count) | No thumbnail art | holds |
| FB-10 | SH-10 | The URL chip end card (P-END-QR without the QR, or P-END-TAGLINE `link_bio`) | Viewers type the URL | holds |
At the checkpoint, list every fallback used. A reel where **all** archive pictures are created plates still ships, but say so in one line ("this reel uses created plates for every person and place; your own photos would make it look like a documentary").

### 12.4 Props, matte, resolution
- No props, no reaction bank, no matte (F-A has no presenter; F-B never puts text behind people).
- Minimum source resolution: full-bleed archive pictures ≥ 1080 px on the short side, upscale ≤ 1.35×; F-B re-crops ×1.2 need a 4K 16:9 source (a 1080p 16:9 source is cropped ×3.2 for 9:16 already: use a vertical 1080 × 1920 camera or accept softness and set `recrop_step` to 1.0).

### 12.5 Third-party inserts: ask, then create `[REQ]`
1. **Scan:** `veos inserts scan` on the transcript (+ script). Typical moments in this style: an article headline (→ P-SOURCE-CARD), a person (→ P-ARCHIVE-BLEED or P-SILHOUETTE-PLATE), a place (→ P-ARCHIVE-BLEED or P-LOCATOR-CARD), an event (→ P-ARCHIVE-CLIP or P-DATE-PLATE + plate), a company or product (→ P-OBJECT-PLATE with the name set in type), a quote (→ P-QUOTE-RECEIPT), a chart (→ a B-5 figure built from the script's numbers).
2. **Ask once**, as one short list: "For these N moments, do you have your own photo, clip or screenshot? Drop the files, or say no and I'll build them." Ask for article screenshots only when the script quotes a headline.
3. **Supplied:** `veos asset add <file> --origin creator`; show it framed by the pattern; never altered to say something else (treatments §4.4 only).
4. **Not supplied:** create it (FB-1…FB-4, P-SOURCE-CARD, P-QUOTE-RECEIPT) from the script's words; the created card quotes only what the script states.
5. **Record** every moment in `plan/inserts.json`: `{id, moment, t0, t1, kind, origin: creator | created, file?, recipe?, substitute_of?, quote_text?, source?, scene}`; dismiss the rest with a reason.
F-B: the conversation itself is the creator's footage; third-party moments inside it (a speaker mentions an article) are **not** illustrated (N11) unless the creator asks; then use P-SOURCE-CARD in a 3.0 s stack-free cutaway with the speaker's audio continuing (counts against presence).

### 12.6 Frame rate and audio
30 fps CFR output, 1080 × 1920, BT.709. F-A: the VO chain (high-pass 80 Hz, de-ess, light compression) → −14 LUFS. F-B: the session MIX (`veos sync` automix) → the same chain.

---

## §13 Output contract `[DNA]`

### 13.1 Beat fields (core + this style's conditionals)
```yaml
- id: 7
  section: RECEIPTS               # HOOK | TURN | CONTEXT | RECEIPTS | REHOOK | COMPARE | PAYOFF | CTA
  t0: 9.20
  t1: 13.85
  spoken: "the Financial Times reports the board plans a $20 billion vehicle"
  trigger: {word: "reports", at: 9.31}
  tone: evidence                  # explain | evidence | turn | warn | awe | cta
  line_type: cites_source          # §8.4
  layout: L-A-canvas
  pattern: P-SOURCE-CARD
  family: B-2
  visual: "Receipt on blue: 'Financial Times · 12 Mar 2025', headline types on, '$20bn' turns lime on 'twenty', leader draws to the body, two thumbs pop"
  layers: [src-ft]
  caption: {profile: CS-A, overrides: []}
  source: {masthead: "Financial Times", date: "12 Mar 2025", headline: "<exact headline>", highlight_spans: ["$20bn"]}
  credit: null # created card: no credit, no label
  insert: {id: I3, origin: created}
  figure_id: null
  shot_id: SH-3
  fallback_used: FB-3
  sfx: [{t: 9.98, on: "src-ft@0.78", why: "lime lands on the figure"}]
```
F-B beats add `speaker`, `angle`, `crop` (step), `cut_reason` (open / handover / reaction / recrop / stack / establish). F-A figure beats add `figure_id`; comparison beats add `side: A | B`.

### 13.2 Reel header
```yaml
format: F-A                       # F-A | F-B
theme: null                       # single
hook_archetype: HA-11
structure: explainer              # explainer | conversation
keyword: null                     # BV-08 when comment_keyword
cta_device: subscribe             # one of profile.cta.devices
figures: [fig-deal, fig-seats]
citations: [I3, I5]
cast: null                        # F-B: {S1: {name, role: host}, S2: {name, role: guest}}
endcard: {tagline: "For more business and power, decoded", device: subscribe}
```

### 13.3 Hook proposals (3)
```yaml
- name: "Name + move + twist"
  archetype: HA-11
  headline_chunks: ["<Subject>", "just <did X>", "and it involves", "<twist>."]
  pair: {thesis: "...", scene: "subject photo → stinger (banknotes) → twist photo"}
  stoppers: [ST-1 pass, ST-2 pass, ST-3 pass, ST-5 7 SC, ST-6 thesis at 2.8 s]
  storyboard: "f0 subject tight + chunk 1 | 0.45 re-crop | 1.2 stinger | 2.1 event photo + particles | 2.8 twist photo (payoff)"
  sound: "bed from f0; one cue on the stinger cover"
```

### 13.4 Checkpoint (send before building, then wait)
1. 3 hook proposals with stopper tests.
2. The beat sheet with tones, patterns and the picture-per-chunk pass (every chunk: cut / event / hold).
3. The transition map and the cue moments.
4. The figure plan (`plan/figures.json` resolved: shown vs computed) and the citation list (masthead, date, exact headline, spans) with any unsupported claim flagged.
5. The inserts record: creator-supplied (with credits) vs created, and the fallbacks used.
6. The end card: tagline, device, value, wordmark (asset or monogram).
7. Style stills: f0, the thesis payoff (≈ 2.8 s), one receipt fully built, one comparison card or map, the end card. F-B: f0, a handover, the stack (if used), the end card.

---

## §14 Worked examples `[NICHE: example]`
The examples use **slots** (`<Company>`, `<$X>`) where a real reel puts the script's facts. Times are planning estimates; replace them with `words.edit.json` onsets. Never fill a slot with a fact the script does not state.

### 14.1 F-A, niche "Business & brands": "Why <Company> just bought its own rival" (62 s, keyword none, device `subscribe`)
**Script gist:** "<Company> just bought <Rival> for <$X>, and the person who signed the deal used to run <Rival>. Here's why. … According to <Outlet>, … Now why would <Founder> sell? … For more business and power, decoded, follow <handle>."
**Assets the creator gave:** 4 photos (founder, CEO, both storefronts), 1 article screenshot. Not given: the regulator, the rival's old CEO → created plates.

| t (s) | Spoken (gist) | Tone | Pattern | Visual | Caption chunks | Cue |
|---|---|---|---|---|---|---|
| 0.00 | "<Company>'s CEO" | turn | P-ARCHIVE-BLEED (creator photo, GR-none, crop 1.18) | CEO face tight, KB 1.18 → 1.12; "● PHOTO: <credit>" | "<Company>'s CEO" | — |
| 0.45 | — | turn | P-RECROP-CUT | same photo at 1.00 | — | — |
| 0.90 | "just bought / <Rival>" | turn | (hold) | — | "just bought / <Rival>" | — |
| 1.20 | "for <$X>," | turn | P-STINGER-STACK (banknote shapes) | rows cover by 1.60, exit 2.33 | "for <$X>," (hidden under the cover) | hook cue at 1.60 |
| 2.10 | "and the man who signed it" | awe | P-ARCHIVE-BLEED (storefront, GR-bw) + P-PARTICLE-OVERLAY off (not a celebration) | storefront, KB pull | "and the man / who signed it" | — |
| 2.70 | "used to run <Rival>." | awe | P-SILHOUETTE-PLATE (old CEO, created), `payoff: true` | silhouette + name plate "<NAME>" | "used to run / <Rival>." | — |
| 3.40 | "Here's why." | turn | T-01 to W-blue | — | "Here's why." | — |
| 4.0–8.0 | context: founded in <year>, <city> | explain | P-DATE-PLATE → P-LOCATOR-CARD (1 pin) | "<year>" rolls and lands; pin pops on "<city>" | as spoken | — |
| 8.0–17.0 | "According to <Outlet>, the deal values…" | evidence | **P-SOURCE-CARD** (creator screenshot via fx.shot in the text rect, credit "● SOURCE: <Outlet>") | headline, "<$X>" lime on its word, leader, 2 thumbs (CEO, old CEO) | as spoken | reveal cue on the lime |
| 17.0–22.0 | "it's the third deal this year" | explain | P-COUNTER-CARD on W-green | counter lands on "third" (figure input from the script) | as spoken | — |
| 22.0–24.5 | "Now why would <Founder> sell?" | turn | **P-QUESTION-TURN** (founder photo, beat `rehook: true`) | hard cut, KB pull | "Now why would / <Founder> sell?" | — |
| 24.5–38.0 | the two strategies | explain | **P-COMPARE-SWIPE** ×4 (A: <Company> "SCALE", B: <Rival> "LOYALTY", A, B) | side chips red / off-white | as spoken | reveal cue on the first chip only |
| 38.0–46.0 | "the regulator approved it in <month>" | evidence | P-SOURCE-SWAP (created headline card) | new outlet, "approved" lime | as spoken | — |
| 46.0–55.0 | the payoff: who gains | awe | P-BAR-TRACKS (two shares on one scale) → P-ARCHIVE-BLEED of the founder (held 2.6 s: the slow moment) | bars land on the spoken numbers | as spoken | bed drop-out 0.5 s before the founder photo |
| 55.0–58.5 | "Watch the full breakdown on my channel." | cta | P-WATCH-FULL (SH-9 thumbnail) | cursor click at +0.6 s | "Watch the full / breakdown" (hidden on the click) | — |
| 58.5–61.8 | "For more business and power, decoded, follow <handle>." | cta | **P-END-TAGLINE** (T-06) | tagline: "business" in end_a, "power," in end_b; logo disc; Follow → Following at +0.8 s | hidden | cta cue on the pill change |
**Figures:** `fig-deals` (counter, input "third" from the script = 3), `fig-shares` (two bars, one `scale_id`). **Inserts:** I1 CEO photo (creator), I2 storefront (creator), I3 old CEO (created silhouette), I4 screenshot (creator), I5 regulator headline (created headline_card). **Cadence check:** 0–3 s = 7 SC; body ≈ 11 SC / 10 s; cuts ≈ 22 / min.

### 14.2 F-A, niche "Places & history": "Why <City> has no skyscrapers" (48 s, device `comment_keyword` "SKYLINE")
| t (s) | Spoken (gist) | Tone | Pattern | Visual |
|---|---|---|---|---|
| 0.00–0.90 | "<City> / has no skyscrapers," | turn | **P-ARCHIVE-FLURRY** (3 creator street photos: colour, GR-bw, GR-sepia) | 0.30 / 0.20 / 0.40 s |
| 0.90–1.90 | "and it's / on purpose." | turn | P-ARCHIVE-CLIP (creator drone clip) with a punch re-crop at 1.6 | street-level motion |
| 1.90–2.80 | "A rule from <year> / still decides" | awe | P-DATE-PLATE "<year>" (`payoff: true` at 2.6: thesis complete) | digits land on the year |
| 2.80–3.60 | "Here's why." | turn | T-02 stinger (building-block shapes) into W-blue | — |
| 3.6–10.0 | where and what | explain | P-LOCATOR-CARD: river + old town + new district pins; P-ROUTE-LINE for the height line | SCHEMATIC tag |
| 10.0–18.0 | the law | evidence | P-SOURCE-CARD (created; headline verbatim from the script's quote of the law's title), body span lime on "<N> metres" | — |
| 18.0–21.0 | "Now why would a city say no to money?" | turn | P-QUESTION-TURN on a creator photo of the old town | re-hook |
| 21.0–36.0 | old town vs new district | explain | P-COMPARE-SWIPE (A "HERITAGE", B "HEIGHT") ×4 | photo cards (creator) / plates |
| 36.0–43.0 | the cost (rents) | warn | P-BAR-TRACKS (two rents on one scale) | values from the script |
| 43.0–48.0 | "Comment SKYLINE and I'll send you the map of every height rule." | cta | P-END-TAGLINE with "Comment" + lime box "SKYLINE" | keyword readable ≥ 1.5 s |

### 14.3 F-B, niche "Business podcast": a 44 s clip (host + guest, cam A / B / W, device `qr`)
**Moment selection:** `shots mine` → candidate 3 (opening line: "Most founders think the product is the hard part. It isn't."; button: "Distribution is the product."; 2.0 s laugh tail).
| t (s) | Speaker | Shot (timeline.shots) | Pattern | Caption (CS-B) |
|---|---|---|---|---|
| 0.00–5.40 | guest | B single, step 1.0, `open` | P-B-SINGLE-HOLD (HA-14: chunk 1 at f0) | italic: "Most founders think / the product / is the hard part." |
| 5.40–9.80 | guest | B single ×1.2, `recrop` | P-B-RECROP | italic |
| 9.80–11.40 | guest speaking, host "right" | A single, `reaction` (1.6 s) | P-B-REACTION | italic (the guest's words) |
| 11.40–14.10 | guest | B single 1.0 | — | italic |
| 14.10–19.80 | host | A single, `handover` | P-B-HANDOVER-CUT | upright |
| 19.80–24.30 | guest ↔ host rapid | stack (guest top, host bottom), `stack` (4.5 s) | P-B-STACK, caption on the seam | per speaker |
| 24.30–31.00 | guest | B single, `handover` | — | italic |
| 31.00–34.20 | guest | W wide, `recrop` (R-4) | P-B-WIDE | italic |
| 34.20–41.60 | guest (the button) | B single ×1.2 | R-7: no cut in the button | italic: "Distribution / is the product." |
| 41.60–44.00 | laugh tail | L-end | **P-END-QR**: "Watch the full conversation / with <Guest> / at [url]" + QR | hidden |
**Checks:** handover cuts within ±3 f; longest hold 5.7 s; stack share 10 %; presence 95 %; cuts 9 / 44 s ≈ 12 / min; median shot 4.4 s.

---

## §15 QA checklist `[DNA]`
**1. Profile conformance**
- [ ] The reel header names one format; F-A has no presenter; F-B presence ≥ 85 % (V-PROFILE, V-PRESENCE).
- [ ] Duration in range (F-A 45–80 s, F-B 30–60 s); F-A has one re-hook between 25 % and 75 % (V-REHOOK).
**2. Hook**
- [ ] f0: archive picture moving + boxed chunk 1 (F-A) / speaker live + chunk 1 (F-B); nothing else (V-F0).
- [ ] F-A: ≥ 7 SC in 0–3 s; the thesis complete by 3.0 s on a `payoff: true` scene; one stinger max in the hook.
- [ ] ST-1 (25 % thumbnail) and ST-2 (mute) pass.
**3. Body and cadence**
- [ ] V-CADENCE numbers (§7.6); every F-A picture cut declared (`cuts: [0]`) and on a chunk boundary or noun onset ±2 f (V-ONWORD).
- [ ] No two consecutive chunks both "hold" (P5b); no picture on screen > 2.5 s without a Ken Burns or an event.
- [ ] Receipts follow the ritual (§7.3); comparison sides alternate A / B with the right chip colours.
- [ ] Treatments never repeat on consecutive shots (§4.4).
**4. Captions**
- [ ] CS-A / CS-B only; 58 / 60 px; one box per chunk; hard swaps; ≤ 2 lines; ≤ 18 / 20 characters per line; lead ≤ 0.15 s (V-CAPTION).
- [ ] No caption on the end card; hidden under the stinger cover and the P-WATCH-FULL click only.
- [ ] Glossary spelling exact; F-B host upright / guest italic (V-SPEAKER SPK-2).
**5. Modules**
- [ ] §18: every number on a card is in `plan/figures.json`, recomputes, lands ±5 f (V-DATA, V-NUMFMT).
- [ ] §19: every receipt has masthead + date + verbatim headline + spans; created ones (V-CITE, V-INSERTS).
- [ ] §20: handover cuts ±3 f, holds ≤ 7.0 s, reactions 1.2–2.2 s, the button not cut (V-SPEAKER, `veos shots check`).
- [ ] §25: end card ≤ 3.5 s, the action readable ≥ 1.5 s, the wordmark present (asset or monogram) (V-PROMISE).
**6. Truth and inserts**
- [ ] Every third-party moment is creator-supplied or created; nothing fetched (V-INSERTS, NC-7).
- [ ] Quotes and headlines verbatim (NC-13); locator cards tagged SCHEMATIC; no flags or logos drawn.
**7. Sound contract**
- [ ] Cues only on hook / transitions / reveals / CTA (F-A) or CTA (F-B), S1–S6 clean; F-A bed ducked ≥ 18 dB, drop-out before the payoff; F-B no bed.
- [ ] −14 LUFS, true peak ≤ −1.5 dBTP (NC-8).
**8. End and export**
- [ ] Hard end ≤ 6 f after the last word; black tail ≤ 0.2 s; 1080 × 1920, 30 fps CFR.

---

## Conditional modules

### §16 Frame template / chrome: OFF (`profile.modules.chrome = false`: the frame changes with every picture; only the caption band is persistent, and it is the caption profile's job).

### §17 Running state & anchored graphics: OFF (`running_state = false`, `anchors = false`: figures are one-shot cards, not persistent counters; pins are placed statically inside their card).

**Object tracking (optional, F-A archive clips).** When a line names one moving thing inside a full-bleed archive clip ("this man", "that ship") and a label or ring should stay on it, request a track at plan time: `veos track --project P --clip <asset> --at <s> --look`, then `--id <name> --box x,y,w,h --from/--to` over the scene's span only (≤ 4 s here, clip-space track), check `plan/tracks/<id>.preview.jpg`, and give the label scene `anchor: {track, offset, lost: "fade", place}` (needs a `box`). The receipt itself never needs a track (it is created on W-blue). **Fallback:** when the track loses the object for more than 20 % of the span, or no single object is clear, drop the label and let the caption carry the name (or put a static T-MAPLABEL-style chip in the lower third, clear of the subject).

### §18 Data contract `[COND: modules.data_figures — F-A]` `[DNA rules]`
- Every counter, bar, seat arc, flow amount, date plate year and timeline year is a figure (or an input) in `plan/figures.json`. Kinds used: `counter` (P-COUNTER-CARD), `bar` (P-BAR-TRACKS, one `scale_id` per card), `grid_fill` (P-SEAT-ARC: `value` = seats, `steps` per group), `hero_number` (P-DATE-PLATE uses an input with `from: script`), `table` (never).
- Formulas: `sum`, `diff`, `ratio`, `percent_change`, `per_period`, `unit_convert`, `cagr` (`data.formulas`). A stated value is `formula: none` with `from: script` and `said` = the exact words.
- Format: `profile.numbers` (international $, long style: "$20 billion"); a figure inside a verbatim headline keeps the headline's own spelling and is not bound.
- Illustrative shapes (a "1 dot = 10 seats" legend, a schematic trend) carry the `example` tag at y 128 and no unsourced number.
- V-DATA / V-NUMFMT: recompute, provenance, same scale, landing ±5 f, formatting.

### §19 Evidence & citations `[COND: modules.citations — F-A]` `[DNA]`
- **Credit line** (T-CREDIT): x 64, y 128, mono 500 24 px, white 85 %, prefix "● " with the dot in `accent`, fades in 6 f with its picture. Optional: use it when the creator wants a source shown; nothing requires it.
- **Source card:** P-SOURCE-CARD (§8.3). Two builds:
  - *Created* (default): the outlet set in type (T-OUTLET, no masthead logo), the date as published, the **exact** headline from the script, the transcript or a creator-pasted text, `highlight_spans` (1–2 spans, each the words the voice stresses or the figure), body copy as decorative texture (`TC-decorative`; if the creator pasted the article's first sentence, use it verbatim, otherwise neutral illegible mono lines).
  - *Creator screenshot*: `fx.shot({asset, chrome: false, highlights})` placed in the text rect (x 64–1016, y 360–1000), the lime highlight box drawn on the spoken span, the credit "● SOURCE: <Outlet>". The leader and thumbs still follow.
- **Highlight recipe:** lime (`accent`) text colour on the key span + all other headline words dimmed to `muted` (the "lime figure" highlight); never bars, boxes or underlines on created cards.
- **Figure numbering:** off.
- **Plates:** P-NAME-PLATE (names), P-DATE-PLATE (dates), T-MAPLABEL (places).
- **Verdict stamps:** none (the style never stamps a verdict; the voice concludes).
- **Rules:** one receipt per claim; headlines quoted exactly; a claim without a verbatim source line is flagged at the checkpoint and shown only as a caption (no receipt).
- **Beat fields:** `source {masthead, date, headline, highlight_spans}`, `credit`, `insert` (V-CITE, V-INSERTS).

### §20 Dialogue `[COND: modules.dialogue — F-B]` `[DNA]`
- **Cast:**
  | id | role | caption style | angles |
  |---|---|---|---|
  | host | host (the creator) | white upright on the blue box | A (single), W (wide) |
  | guest | guest | white italic on the blue box | B (single), W (wide) |
  More than two people: add `guest2` (white italic, same box) and keep the cut grammar; captions never colour-code beyond upright / italic.
- **Angle map:** `veos angles`; preferred singles A → host, B → guest; faux crops `<W>:<speaker>` when a camera is missing (FB-5 / FB-6).
- **Layouts:** full singles (≥ 85 % of runtime), stack (≤ 12 %, seam y 960, hairline 0, top = the speaker), wide (one shot, 1.5–4.0 s).
- **Cut grammar:** §9.3 R-1…R-8, written in `dialogue.cut_rules`: `handover_tol_f 3, lead_f 1, open_s [0, 0] (no stack opener), max_hold_s 6.0, stack_max_s 6.0, reaction_s [1.2, 2.2], recrop_step 1.2, min_shot_s 1.0, backchannel_max_s 1.6`, `stack.share 0.12`.
- **Captions:** CS-B; the dominant speaker only during overlaps; cards never mix speakers; on the seam during stack shots.
- **Single-camera fallback:** two crops of one wide shot (E-13b); with one person only, F-B does not apply (use another template).
- **Validator:** V-SPEAKER (`veos shots check`): labels ≥ 95 %, one caption style per speaker, cut ±3 f on handovers, the speaker on screen, no cut inside a word, holds ≤ max + 1 s.

### §21 Canvas camera: OFF (`canvas_camera = false`: the camera never travels over the canvas; pictures cut).
### §22 Ink & annotation: OFF (`ink = false`: the only marks are the lime highlight and the leader line, both part of the receipt).
### §23 Continuity: OFF (`continuity = false`: hard cuts are the grammar; no morph chains).
### §24 Series furniture: OFF by default (`series = false`, VAR). If the buyer turns it on: a T-PLATE "PART <n>" in the credit slot (x 64, y 128) for the first 2.0 s after the turn line, never inside the hook; `series.tag_format: "part {n}"`.

### §25 Sponsor, brand & end cards `[COND: modules.brand — both]` `[DNA look; VAR assets and values]`
**25.1 Rules:** one end card per reel, ≤ 3.5 s, the action readable ≥ 1.5 s, captions hidden, hard end ≤ 6 f after the last word (the end card's line is the last spoken line, or it covers a non-speech tail), black tail ≤ 0.2 s.

**25.2 P-END-TAGLINE** (F-A default; F-B when the device is `subscribe`)
| Element | Spec |
|---|---|
| Ground | W-end `end_bg` #0A1314 + noise 0.05 (a faint 8 % halftone of the reel's last archive picture may sit behind at 6 % opacity) |
| Tagline | Montserrat 800, 138 px (128–148, fit the longest line to 900 px), line height 1.0, tracking −0.04 (letters nearly touch), left x 90, top y 150 (measured v01 @1:20: cap top 151, x 93–966), 4 lines in off-white `#E4ECE6`: "For more" / "<topic A> and" (topic A in `end_a`) / "<topic B>," (topic B in `end_b`) / "decoded" (paper). Pattern `brand.endcard.tagline_pattern`; the buyer's own tagline replaces it (`brand.endcard.tagline`, written once at the first checkpoint) |
| Wordmark row | top y 920: the logo (SH-8) or the FB-8 monogram in a Ø 280 disc at x 72 (measured Ø ≈ 295, y 925–1220); then the action element 40 px right of it, vertically centred on the disc |
| Action: `subscribe` | white pill "Follow" (Inter Tight 700 40 px, ink, h 84, padding 0 × 40, radius 42) → at +0.8 s it becomes "Following" (fill #2A2F30, paper text, a bell glyph) over 6 f with a 6-particle lime sparkle; a ghost pill "{{BV-01.handle|@yourhandle}}" (paper 2 px outline) next to it |
| Action: `comment_keyword` | "Comment" (Inter Tight 700 44 px, paper) + the keyword in a lime box (`accent` fill, ink, mono 700 56 px, padding 10 × 22): {{BV-08.keyword|KEYWORD}} |
| Action: `link_bio` | "Full story: link in bio" with "link in bio" in the lime box |
| Action: `end_card` | the wordmark row only |
| Motion | T-06 hard cut (no dissolve: v01 @76.80, v02 @56.00); from f0 the tagline is on screen at ≈ 10 % with letters resolving in seeded order (`fx.resolve`, `order: "random"`, `ghost` on), and each line brightens from dim grey (`#4C5252` → `#707474` → `#E4ECE6`) over ≈ 1.5 s, top line first; topic A turns `end_a` first, topic B turns `end_b` last (v01 @1:16.6–1:20, v02 @0:57–0:59); the whole wordmark row (disc + pills) rises from y +180 to its place over 8–10 f (`ease_entry`) from f0, then creeps up ≈ 20 px over the hold; the Follow → Following change at +0.8 s |
| Hold | 2.0–3.5 s |

**25.3 P-END-QR** (F-B default; F-A when the device is `qr`)
| Element | Spec |
|---|---|
| Ground | W-qr (`primary`, flat) |
| Text | mono 700 40 px, paper, line height 1.3, centred at y 470–620, three lines: "Watch the full conversation" / "with <Guest or Show>" / "at [url]" with the URL in a paper box (ink text, padding 4 × 12) |
| QR | SH-10 image (or a QR Claude generates locally from the creator's URL, origin `created`), white panel 620 × 620 at x 230, y 760, 40 px quiet zone; the FB-8 monogram disc Ø 120 in the centre only if the QR's error correction is H |
| Fallback | FB-10: no QR panel; the URL box grows to mono 700 56 px at y 900 |
| Motion | hard cut in (T-01); text types on 8 f per line; the QR panel pops 8 f (0.94 → 1.00) |
| Timing | covers the clip's non-speech tail (laugh, "yeah", a breath) of 1.5–2.5 s; if the clip has no tail, record a 2 s sign-off line ("Full conversation: link on screen") and put the card under it |

**25.4 Sponsor (P-SPONSOR-SOURCE):** a paid segment is built like a receipt with the sponsor's name in the outlet slot and "Paid partnership" ({{BV-14.disclosure|Paid partnership}}) T-TAG held through the whole segment (≥ 2.0 s) and said aloud (NC-12). No sponsor logo unless the sponsor supplied it.

---

## Part C. Exceptions and the non-overridable core

### C.1 Non-overridable core (applies unchanged)
NC-1 face never covered · NC-2 meaning text never overlaps · NC-3 smooth motion · NC-4 legibility floors and contrast · NC-5 IG UI bands · NC-6 truth (no invented facts, numbers or UIs) · NC-7 creator-owned media only, never fetched · NC-8 audio −14 LUFS / −1.5 dBTP / bed ≥ 18 dB under the voice · NC-9 determinism · NC-10 ≤ 4 bright hues (this style: 3) · NC-12 disclosure · NC-13 quote integrity · NC-14 redaction of personal identifiers.

How this style meets the ones it leans on hardest:
| NC | Where this style is exposed | The rule here |
|---|---|---|
| NC-6 | Receipts, figures, maps | Every headline verbatim, every number in `figures.json`, maps tagged SCHEMATIC until E-18 |
| NC-7 | The archive montage | Creator files only; else created plates |
| NC-13 | P-QUOTE-RECEIPT, F-B clips | Quotes verbatim and attributed; an F-B clip is never re-ordered to change a speaker's meaning |
| NC-14 | Creator screenshots of articles, documents | Blur emails, phone numbers and IDs visible in any screenshot for their whole time on screen |

### C.2 Declared exceptions
**None.** E1–E6 are not used (captions 58 / 60 px, labels 40 px, no behind-subject type, no bursts, no ambient fields, no edge bleed; caption hard swaps are exempt from G3). A buyer may not add one without a deviation (DV-n).

---

## Part D. Personalisation

### D.1 Branding questions (one round, each with "keep the default")
| BV | Question | Writes | Default |
|---|---|---|---|
| BV-01 | Your name and handle | `creator.name`, `creator.handle`; end-card wordmark, ghost pill, default credit | {{BV-01.name|the creator}} · {{BV-01.handle|@yourhandle}} |
| BV-02 | One or two brand colours | `roles.primary` (the blue: canvas, caption box, QR card), `roles.accent` (the lime) | {{BV-02.primary|#1A2FAA}} · {{BV-02.accent|#D4F56A}} |
| BV-05 | Language you speak / caption language | `profile.language`, always asked: **English** → English captions (default) · **Hinglish** → romanised Hinglish captions · **Hindi** → Devanagari captions; numbers follow (BV-06) | English ({{BV-05.speech|en}} → {{BV-05.captions|en}}) | en}} → {{BV-05.captions | en}} |
| BV-08 | Your call to action and its value | `profile.cta.chosen`, `creator.cta` | {{BV-08.device|subscribe}} (keyword {{BV-08.keyword|KEYWORD}}) |
The end-card tagline is **not** asked at setup: it is proposed at the first checkpoint from the creator's niche ("For more <A> and <B>, decoded") and stored in `brand.endcard.tagline`.

Colour rules for BV-02: `primary` must stay a deep saturated colour that carries white text at ≥ 7 : 1 (a pastel or a light brand colour is nudged darker in OKLCH lightness, same hue); `accent` must stay a light highlighter colour at ≥ 7 : 1 on `primary`. A buyer whose brand colours fail both (e.g. two mid greys) keeps the defaults and is told why in one line.

### D.2 Lock map (summary; `tokens.json → locks` is authoritative)
| Area | Lock |
|---|---|
| Source type, presence, spine, caption mode / role, graphics, footage dependency, the format set, hook archetypes, structure, captions mechanics (box, hard swap, chunking), receipt recipe, side-chip meaning, zoom policy | **DNA** |
| Brand blue and lime (within their ranges), caption size (CS-A 54–64, CS-B 56–66) and cy (±25 px), box opacity, fonts within class, cadence ±15 %, motion ±15 %, duration short ↔ standard, stack share 0–20 %, max hold 5–8 s, end-card length 2–4 s | **TUNE** |
| Language, numbers, CTA device and value, end-card tagline and accent words, enabled formats, series on/off, sound cue moments and bed, credit wording | **VAR** |
| §6.4 hook pairs, §8.4 lookup rows, §14 examples, App. A | **NICHE** |

### D.3 Defaults never asked
BV-03 fonts (the template's), BV-04 niche (from each transcript), BV-06 numbers (from BV-05: Indian languages → ₹ lakh/crore), BV-09 both formats on, BV-11 humour off (max off), BV-13 series off, BV-14 "Paid partnership", BV-15 never-list empty, BV-16 logo none (FB-8 monogram), BV-17 duration in range.

### D.4 NICHE slots, filled per reel
| Slot | When |
|---|---|
| §6.4 hook pairs | At P7 of every reel: the thesis → scene pair for this topic, appended |
| §8.4 lookup | At P5: new line types mapped to existing patterns (≤ 10 niche patterns from B-1…B-8 over time) |
| §14 | The first approved reel of each format replaces its worked example |
| App. A | Approved hook chunks are added |
| Glossary | Every proper noun confirmed in captions |
| Stinger objects | The topical object chosen per reel is added to the §6.4 table |

---

## Part E. Changes and decisions (template v1)
| Decision | Versus | Why |
|---|---|---|
| Captions 58 px (F-A) / 60 px (F-B), no E3 | STYLE-COVERAGE "~40 px, E3"; `lib:johnny_a` 40 px / `lib:johnny_b` 44 px | Measured on the 1080 frame: "The King of FIFA" spans 590 px in JetBrains Mono (0.6 em advance) = 61 px; the 2-line block is 8 % of frame height. The 38–42 px figure was the 720 px source unscaled |
| CS-A: one `box` per chunk; CS-B: `box_per_line` (completeness audit 2026-10) | `lib:johnny_a` `box_per_line`; earlier v1 had one box for CS-B too | v01 0:14 "One is reported / to be", v02 0:54 "would change / baseball forever.": one rectangle; v03 @11.40–11.83 "that's one dimension" / "of a place.": two boxes of different widths |
| Motion measured at full frame rate (completeness audit 2026-10) | v1 motion estimated from 1 fps sheets | Cards cut in (no rise), deck not swipe, word-by-word type-on, follow-push ×1.14, inner punch + drift, stinger 38–40 f under a visible caption, oversized vertical roll-by, hard cut to the end card, graphics on twos, archive settle instead of Ken Burns: `docs/audit/archive-explainer/completeness.md` |
| F-A box = black 60 % (audit 2026-10; was 70 %) | analysis "#0B1038 at 85 %" | The box reads navy on blue (#090E36 sampled) and charcoal on light photos (#4D5353): a translucent black, not a navy fill |
| F-A `voiceover_only`, footage medium | coverage "NF, footage high" | The engine's VO path (E-12, which lists this style's F-A) builds every frame; every archive picture has a created fallback, so the reel is complete from a VO |
| F-B kept inside this template | coverage "split; fold F-B into a generic Podcast Clip" | Naman's brief for this template asks for both formats; they share traits 1, 2 and 5 of "Copy these 5", which satisfies §0.4 |
| F-B box = `primary` (one brand blue) | v03 box #1940D9, brighter than the F-A canvas | Branding: one buyer colour must recolour both formats |
| F-B guest captions italic | v03 uses one style for both speakers | V-SPEAKER SPK-2 requires a distinct style per speaker; italic is the least visible change |
| Stack allowed (≤ 12 %), opener off | v03 never stacks | The multi-speaker engine's stack is kept for rapid exchanges and HA-03; the default HA-14 opens on a single |
| Maps schematic | evidence uses real geo maps | No geo data in the engine (E-18 pending); never draw borders from memory (NC-6) |
| Engine built-ins (2026-10-07) | hand-rounded scene time, a bespoke letter scramble, a scene-drawn push-up | `step_fps: 12` on graphic scenes, `fx.resolve` for outlet / chip / tagline letters, the built-in `push` (up, 4 f) for the side change; tracking optional on archive clips (§17) |

---

## Part F. ID index (this playbook)
| Prefix | IDs |
|---|---|
| D | D1–D8 |
| H / N | H1–H20 / N1–N11 |
| F | F-A Archive explainer, F-B Podcast clip |
| W | W-blue, W-archive, W-green, W-white, W-end, W-qr, W-room |
| L | L-A-canvas (rects card, tall, text, bleed), L-B-full, L-end |
| G | G-1 hard cut … G-6 end cut + build, G-7 inner punch + drift |
| GR | GR-bw, GR-sepia, GR-halftone, GR-vhs |
| CS | CS-A, CS-B |
| T (text) | T-OUTLET, T-HEAD, T-BODY, T-CHIP, T-MAPLABEL, T-PLATE, T-DATE, T-FIG, T-CREDIT, T-TAG, T-END, T-QR |
| T (transitions) | T-01 … T-09 |
| HA | F-A: HA-11 (default), HA-12, HA-07, HA-19 · F-B: HA-14 (default), HA-03 |
| SM | SM-SIDE-CHIPS |
| B | B-1 … B-8 |
| P | 43 patterns (§8.3) |
| R | R-1 … R-8 |
| SH / FB | SH-1 … SH-10 / FB-1 … FB-10 |
| V | V-F0, V-CADENCE, V-ONWORD, V-CAPTION, V-SAFE, V-FACE, V-PRESENCE, V-HUES, V-LAYOUT, V-DATA, V-NUMFMT, V-CITE, V-INSERTS, V-SPEAKER, V-PROMISE, V-REHOOK, V-TYPE, V-EXC, V-PROFILE |

---

## App. A Headline & hook bank `[NICHE: example]`
Each line is the first 3 s of captions (chunks separated by " / "), with its archetype.

**F-A Archive explainer**
| # | Hook chunks | Archetype | Niche |
|---|---|---|---|
| 1 | "<CEO> / just bought / <Rival> / and it involves / <Regulator>." | HA-11 | business |
| 2 | "<Brand> / quietly killed / its best-seller. / Here's why." | HA-11 | business |
| 3 | "$<X> billion / is what <Company> / paid for / a company / with no revenue." | HA-07 | business |
| 4 | "<Company> / told investors / it will stop / selling <X>." | HA-12 | business |
| 5 | "<Founder> / was fired / from <Company>. / Then he / bought it back." | HA-11 | business |
| 6 | "<City> / has no skyscrapers, / and it's / on purpose." | HA-19 | places |
| 7 | "<Country A> / and <Country B> / share a border / nobody can cross." | HA-11 | places |
| 8 | "In <year>, / one decision / still decides / how <City> looks." | HA-19 | places |
| 9 | "<N> countries / vote on this, / and one man / decides." | HA-07 | places / power |
| 10 | "<Sport> in <Country> / looks a lot / different. / Here's why." | HA-19 | places / culture |

**F-B Podcast clip** (the in-point line, said by the speaker at f0)
| # | First sentence | Archetype |
|---|---|---|
| 1 | "Most founders think the product is the hard part. It isn't." | HA-14 |
| 2 | "Nobody tells you the first year is the easy year." | HA-14 |
| 3 | "I stopped reading the news, and I understand the world better." | HA-14 |
| 4 | "The best decision we made was saying no to <X>." | HA-14 |
| 5 | "Every place is more than the headline it's famous for." | HA-14 |
| 6 | "Q: Would you do it again? / A: Not the way we did it." | HA-03 |
| 7 | "Here's what nobody says about <niche>: …" | HA-14 |
| 8 | "We lost <X> and it was the best thing that happened." | HA-14 |
| 9 | "Q: What would you tell yourself at 20? / A: Stop waiting." | HA-03 |
| 10 | "The people who live there tell a different story." | HA-14 |

## App. B Evidence map
The full source map, measurements and the `(unverified)` list are in `evidence.md` (templates only). Sources: `analysis/short/johnny-harris.md`; frames `evidence/short/johnny-harris/v01–v03/sheets`. Summary: captions (v01 0:00–1:12, v02 0:00–0:54, v03 0:00–0:40), blue canvas and cards (v01 0:08–0:22, 0:34–0:41, 1:02–1:13; v02 0:07–0:20, 0:25–0:44, 0:49–0:55), green figures (v01 0:25–0:33, 1:12), hook (v01 0:00–0:03 stinger, v02 0:00–0:03 flurry, v03 0:00 cold open), end cards (v01 1:14–1:19, v02 0:56–0:58, v03 0:41–0:42).
