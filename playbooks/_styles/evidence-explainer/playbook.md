# Evidence Explainer Style Playbook (template v1)

**Purpose.** You (Claude) receive a talking-head take of {{BV-01.name|the creator}} making claims about a news story, a policy, a price, a myth or an incident. This playbook makes you edit it the way the most-watched Indian explainers are edited: no speech captions at all, a topic-coloured backdrop behind the cut-out presenter, and **every claim paid off on screen** by a source card with red highlight bars, a date or name plate, a map, a number on the data stage, or a stamped verdict. Input (SW-01 `talking_head`): one A-roll take shot against a clean background (for the matte), plus whatever screenshots, clips and photos the creator owns. Anything the creator does not have, you build yourself with the inserts toolkit and label it.

**Inspired by:** Dhruv Rathee (shorts, 4 reels analysed; `evidence.md`). The name of the style is generic; the creator appears only in `inspired_by`.

### Style DNA `[DNA]`
A serious, journalistic short. The presenter is cut out of his room and stands on a **mottled, topic-coloured plate** (crimson for rights and crime, ember for war and media, gold for money). He never gets subtitles: the screen carries only what proves him right. When he names a source, the frame **splits**: the evidence slides down from the top behind a thin rim-coloured hairline and he shrinks into the bottom half, or he drops into a **ringed circle** over a full-bleed article. Key phrases in the article are **struck through with red bars that wipe in word by word** exactly when he says them. Every date, name, place and number he speaks appears as a **plate** (dark slab, white caps, white underline). The reel opens **tight and blurred and pulls back to sharp**; new evidence lands blurred and snaps sharp; sections and evidence swaps are punched by a **half-second yellow-to-red light-leak burn** (3–6 per minute); a claim cluster ends with a **rubber-stamp verdict** (FAKE, SCAM, FALSE, TRUE). The camera on the presenter is mostly locked: one eased punch-in on a key word, not constant re-crops. Calm voice, dense proof, no decoration.

**Copy these 5 things** (if a reel lacks one, it is not this style):
1. **Matted presenter on a topic-coloured backdrop plate**, chosen per topic from the theme packs (§3.1 W-backdrop, P-BACKDROP, §4.3).
2. **No speech captions.** Plates carry every spoken date, name, place and number instead (H-TB, §5.4, P-DATE-PLATE / P-NAME-PLATE / P-NUMBER-CHIP).
3. **Citation cards with red highlight bars** wiping onto the spoken phrase: the creator's screenshot, or a created headline card (§19, P-CITE-SHOT / P-CITE-CARD).
4. **Split and PiP grammar:** a 50/50 slide-down split with a rim hairline at y 950, and a 480 px ringed circle over full-bleed evidence (§3.2 L-split-top, L-pip-ring).
5. **Punctuation:** blurred pull-back at f0, blur-hold-then-snap arrivals, light-leak burns between sections and evidence items, verdict stamps (§9 T-04, T-06, T-11; Z-0; P-STAMP).

### Directives `[DNA]`
| # | Directive | Where it lives |
|---|---|---|
| D1 | **Evidence on screen for every claim.** A claim that names a source, a number, a person, a date or a place gets its card, plate or figure within ±5 f of the word. An unsupported claim is flagged at the checkpoint, never decorated | §19, H5, H10 |
| D2 | **No speech captions, ever.** The text burden moves to plates: something readable starts or changes at least every 4 s, and every spoken date, name, place and number is on screen | H-TB, §5.4 |
| D3 | **The backdrop carries the topic.** One theme pack per reel, chosen by the topic table; the rim colour (hairline, ring, plate bar) comes from it | §3.1, §4.3 |
| D4 | **The face stays.** Evidence enters by the split or the ringed PiP; the presenter leaves the frame only for 1–6 s full-bleed proof | §3.2, §3.6 |
| D5 | **Highlight the exact words.** Red bars wipe word by word on the phrase being spoken, 4 f per word; never on a phrase the creator does not say | §19, P-CITE-CARD |
| D6 | **Close with a verdict.** A claim cluster that resolves (fake, scam, false, true) ends on a stamp; 1–3 stamps per reel | P-STAMP, §7.3 |
| D7 | **Punctuate with focus and light.** Blur at f0 and on every arrival; a light-leak burn (T-06, 16 f) at section changes and evidence swaps, 3–6 per 60 s, ≥ 2.5 s apart | §9 |
| D8 | **Truth before style.** Headlines and quotes verbatim, numbers recomputed, nothing fetched | §18, §19, §12.5, NC-6, NC-7, NC-13 |

Buyer directives go here as **BD1…** `[VAR]` and may only make the style stricter or more specific.

### Quick index
| § | What | Status |
|---|---|---|
| §0 | Style profile | ON |
| §1 | Procedure (claim → card pairing, plate pass) | ON |
| §2 | Hard rules, H-TB | ON |
| §3 | Worlds, layouts, stage moves, safe zones | ON |
| §4 | Colour, theme packs, clip treatments | ON |
| §5 | Type, plates (captions OFF) | ON |
| §6 | Hook system (HA-09 evidence slide) | ON |
| §7 | Structure (evidence) and cadence | ON |
| §8 | Visual system, 44 patterns | ON |
| §9 | Transitions | ON |
| §10 | Motion, camera, layers, finishing | ON |
| §11 | Sound contract | ON |
| §12 | Footage, shot list, fallbacks, inserts | ON |
| §13 | Output contract | ON |
| §14 | Worked examples (3) | ON |
| §15 | QA | ON |
| §16 | Frame template | OFF |
| §17 | Running state, anchors | OFF |
| §18 | Data contract | ON |
| §19 | Evidence and citations | **ON (core)** |
| §20–§23 | Dialogue, canvas camera, ink, continuity | OFF |
| §24 | Series | OFF (VAR) |
| §25 | Sponsor, brand, end cards | OFF |
| Parts C–F, App. A–B | Exceptions, personalisation, changes, IDs, headline bank, evidence map | ON |

Formats: **F-A Evidence explainer** (the only format). Themes: **TH-crimson** (default), **TH-ember**, **TH-gold**, **TH-slate** (inferred), **TH-room**.

---

## §0 Style profile `[REQ]`

```yaml
profile:                         # mirrored in tokens.json -> profile
  source_type: talking_head
  presenter: {presence: anchor, share: [80, 95], max_absence_s: 8}
  spine: talking_head
  captions: {mode: off, role: support, mute_policy: sound_on}
  graphics: support
  duration: {class: long, target_s: [100, 170]}
  language: {speech: en, captions: {lang: en, script: Latn, transform: verbatim}, on_screen: en, post_title: en,
             supported: [[en, en, Latn], [hinglish, hinglish, Latn], [hi, hi, Deva]]}
  numbers: {grouping: international, currency: "$", compact: k_m_b, units: metric, decimals: 2, style: full}
  tone: {energy: balanced, comedy: off, comedy_max: light}
  themes: {policy: per_topic, packs: [TH-crimson, TH-ember, TH-gold, TH-slate, TH-room], default: TH-crimson}
  formats: {list: [F-A], default: F-A}
  footage_dependency: high
  cta: {devices: [cross_promo, comment_keyword, link_bio], placement: end, chosen: none}
  modules: {chrome: false, running_state: false, anchors: false, data_figures: true, citations: true,
            dialogue: false, canvas_camera: false, ink: false, continuity: false, series: false, brand: false}
```

Why each value:
- **source_type: talking_head**, because every analysed reel is one presenter's A-roll with inserts (v01–v04).
- **presenter: anchor 80–95%, max absence 8 s**: the face is on screen ≈ 85–90% (full ≈ 40%, split ≈ 35%, PiP ≈ 10%); full-bleed bursts without him run 1–7 s (v02 @0:15–0:22), a static source card 6.2 s (v01 @1:33.4–1:39.5), and one TV clip 12.5 s (v01 @1:16.2–1:28.7, measured cut to cut). 8 s is the cap; the 12.5 s clip is not copied.
- **spine: talking_head**: the A-roll is the timeline; the evidence is inserted on the words.
- **captions: off / sound_on**: no subtitle on any spoken line in v01–v04 (the yellow subtitles at v02 @0:56 are burned into a third-party clip). PV-6 → H-TB in §2 and `on_screen: en`.
- **graphics: support**: evidence cards ≈ 25–35% of runtime, own graphics (plates, stamps, data) ≈ 8–12%, B-roll ≈ 50%. The graphics illustrate; the voice argues.
- **duration: long, 100–170 s**: the four reels run 130–179 s. TUNE allows `standard` (60–90 s) for a buyer who wants shorter reels.
- **language**: on-screen text is English in every reel while the speech is presumably Hindi `(unverified)`; Devanagari appears only inside third-party screenshots. Template default: English; setup always asks (English, Hinglish, Hindi; BV-05). Plates are written in the `on_screen` language.
- **numbers: decimals 2** (v04 shows ₹72, ₹111, ₹32.98 and ₹60–₹65 per litre; paise need 2 decimals). Numbers follow the language (BV-06): English → international `$` and K/M/B (unless the buyer picks ₹); Hinglish / Hindi → ₹ with Indian grouping and lakh / crore.
- **tone: balanced, comedy off (max light)**: serious delivery; stamps are verdicts, not jokes. The one die-cut gag (v02 @2:56) is the only "light" moment seen, so `light` is the ceiling.
- **themes: per_topic**: orange flame (v01, war/media), red mottled (v02, ICE/rights), gold marble (v04, petrol prices), real room (v03, incident). TH-slate is inferred for cool topics (tech, health) and marked so.
- **formats: F-A only**: one visual system across all four reels (STYLE-COVERAGE §1).
- **footage_dependency: high**: the look needs a matte-able background, and the real style leans on the creator's screenshots and clips. Every shot has a fallback (PV-11).
- **cta**: no CTA was observed; v04 ends on a cross-promo thumbnail of the creator's own long video. `comment_keyword` and `link_bio` are offered as end plates in the style's look (a product decision, not evidence); `chosen: none` is the default.
- **modules**: citations is the core; data_figures carries the then-vs-now data stage (v04). Everything else is off.

### 0.4 Formats
| Field | F-A "Evidence explainer" |
|---|---|
| `when` | Any reel that makes claims and proves them: news, politics, policy, prices, myth-busting, fact-checks, incident reconstructions |
| `profile` overrides | none |
| `layouts` | L-full, L-split-top, L-split-bottom, L-pip-ring, L-pip-card, L-band, L-hidden |
| `cadence` | §7.6 |
| `hooks.default` | HA-09 |
| `shared DNA` | matted presenter on a topic plate, no speech captions, source cards with red bars, plates for every date/name/number, verdict stamps |

### 0.5 Theme packs (summary; full table in §4.3)
TH-crimson (rights, law, crime; default) · TH-ember (war, conflict, media, disasters) · TH-gold (money, prices, tax, economy) · TH-slate (tech, science, health, climate; inferred) · TH-room (incident reconstructions shot in a real room; no backdrop swap). One pack per reel, picked by the topic → theme rule. The pack sets the backdrop gradient and the rim colour (`primary`).

---

## §1 Procedure (follow in order) `[REQ] [DNA]`

This style's craft is **claim → card pairing** (P8a) and the **plate pass** (P5b). Do them carefully; everything else follows.

1. **P1 Inventory.** `ffprobe` every input; conform to 30 fps CFR (60 fps masters are conformed, not slowed). Identify the setup (§12.1 A or B). Register every file with its origin: the creator's A-roll and their screenshots/clips/photos are `creator` (`veos asset add <file> --origin creator`); everything you build is `created`.
2. **P2 Matte (required).** Run `veos matte` over the whole A-roll. The backdrop plate (P-BACKDROP) needs the cut-out on every frame where the presenter is visible. Check hair edges at 200% on three frames (start, middle, a gesture frame). If the matte fails (busy background, green tee on green screen), switch the reel to **TH-room** (FB-1) and say so at the checkpoint.
3. **P3 Transcribe** with word timestamps (`veos transcribe`). There are no captions to build, but you need the words for timing, for the plate pass and for verbatim checks. Translate or transliterate only what becomes a plate (`language.captions.transform`: plates are written in `on_screen` language; names keep their real spelling; Hindi number words become digits).
4. **P4 Segment** into evidence beats `EB-1…EB-n` (§7.1): each beat = one claim + its proof + (optional) its counter-evidence; mark cluster ends where a verdict lands. Mark jump re-crop points on word boundaries (every 3–6 s of uninterrupted presenter).
5. **P5 Classify** every sentence with a line type (§8.4) and its trigger word (the outlet name, the number, the date, the person, the verdict word).
   - **P5b Plate pass (craft).** List every spoken date, proper name, place and number with its word time. Each becomes a plate, a chip, a card highlight or a figure (H-TB). Spoken numbers that are compared go to `plan/figures.json` (§18); one-off numbers become P-NUMBER-CHIP. A name that is also on a card's highlighted phrase is covered by the card.
6. **P6 Tone-tag** every sentence: `claim` · `evidence` · `context` · `warn` · `verdict` · `cta`. The tone picks the camera move and the role colour (tokens `tone_treatment`).
7. **P7 Hook plan.** Pick the archetype (§6: HA-09 variant H9-A / H9-B / H9-C, or HA-07 / HA-18). Write **3 hook variants** and run the stopper tests ST-3, ST-5, ST-6. Write 3 post titles (App. A formula).
8. **P8 Visual plan.**
   - **P8a Claim → card pairing (craft).** For every claim beat, capture the citation: masthead (outlet name), date, the exact headline (from the creator's screenshot, or verbatim from the script), and the highlight spans (the words the creator says while the card is up). One card per claim. A claim with no source in the script or the creator's files is **flagged** ("unsupported: needs a source or a rewrite") at the checkpoint; you never invent a headline.
   - **P8b Data check** (§18): every compared number gets inputs, a formula and a recompute; mismatches are flagged.
   - **P8c Ask, then create** (§12.5): `veos inserts scan`, refine the list, ask the creator **once** for screenshots/clips/photos of those moments, then plan the created substitutes for the rest.
   - **P8d Layout plan:** assign each beat a layout (§3.2 schedule rule) and the theme pack (§4.3).
9. **P9 Beat sheet** (§13): one beat per trigger; meet the cadence (§7.6): an SC at least every 4 s, 2.5–4.5 weighted SCs per 10 s.
10. **P10 SFX ledger and transition map** (§11, §9): cues only on the allowed moments.
11. **P11 Assets:** frame the creator's files (fx.shot / fx.citationStrip), build the created cards (fx.headlineCard, fx.quoteCard, fx.silhouette, fx.appUI, fx.logoPlate), the plates, the data stage and the maps. Record every insert in `plan/inserts.json`. List the fallbacks used (§12.3).
12. **P12 Checkpoint** (§13.5). **Wait for approval.**
13. **P13 Build** act by act (hook → each EB → end). `veos scenes-meta` → `veos measure` → `veos validate` (fix every failure) → preview frames and QA (§15, at most 3 passes) → render.

---

## §2 Hard rules `[REQ] [DNA]`

### 2.1 Editing rules (every style)
The ten editing rules in `playbooks/_global/GLOBAL-RULES.md` apply. They are directions, not limits: smooth, seamless motion; nothing overlaps by accident; keep the face clear (behind the speaker is fair game, text included); readable at a glance; one idea at a time; show the thing, not the word; say what was said; hook titles hook; pace like the style, not like a timer; the style decides the look.
- **Facts the engine checks:** accidental overlaps, jumps, the face covered, unreadable text, numbers and quotes that don't match what was said, the promised count. Every count, timing and budget this playbook gives is direction for the edit, not a limit.
- **Picture first, in this style's own look:** every key beat shows the thing being said (an object, a screen or app, a diagram, numbers in motion), not just its word; text supports the picture and never replaces it. When the speaker points with words ("this, this and this", "from this to this", "ye dekho"), show what they mean. Illustrations may use made-up but realistic numbers and names ("212 views", "1.2M views"), with no label; a number or quote the speaker says is shown as said. This overrides any rule below that bans made-up numbers or asks for an example tag: those rules now cover claims (the creator's results, prices, benchmarks, testimonials), not illustrations.
- **Hook titles hook:** the on-screen title promises the viewer something (an outcome, a curiosity gap, who it's for) and is true to what the reel delivers; it need not repeat the spoken words. This playbook sets its shape (§5.2, §6.5: lines, sizes, word limits, case), never its voice (§6).
- **Retired (8 Oct 2026), whatever this playbook says below:** no REPRESENTATIONAL or example labels on made-up cards, no credit lines, no flash limit (flash as often as this style calls for; any "NC-11" cap below no longer applies), and text may sit behind the speaker without an exception.

### 2.2 Declared exceptions
**None declared.** The style's small text is either `TC-legal` (SOURCE credits, 24 px) or `TC-decorative` (body copy inside the creator's own screenshots, where the highlighted phrase is the readable carrier). Plates, chips and card headlines all sit at ≥ 40 px, so E3 is not needed. Cards and plates are never placed behind the head (no E1). Buyers cannot add exceptions without a DNA deviation (Part C).

### 2.3 Style MUST rules
| ID | Rule | Check |
|---|---|---|
| **H1** | **Frame 0 = the presenter alone on the backdrop, tight and blurred, pulling back.** Z-0 `pull-open` 1.30 → 1.00 over 36 f, ease `expoOut` (most of it in the first 0.4 s, a slow tail to 1.2 s), with P-FOCUS-PULL (the preset's own `blur`: held, sharp by f9–f11) (v01, v02 @0:00–0:00.5). No headline at f0. Exceptions: H9-B and H9-C open sharp and static (v03, v04); H9-B may land the date plate from 0.17 s | V-F0 |
| **H2** | **Cadence:** weighted SCs 2.5–4.5 per 10 s in the body, ≥ 4 in 0–3 s; max gap between SCs 4.0 s (1.5 s in the hook); nothing static > 3.0 s | V-CADENCE |
| **H3** | **Evidence by 1.5 s, a label by 2.0 s.** The first evidence panel (split, PiP or full-bleed card) is readable by 1.5 s; the first label (plate, highlight bar or stamp) lands by 2.0 s and carries `payoff: true` | V-F0 |
| **H4** | **Plate limits:** a plate or chip is ≤ 6 words, ≤ 2 lines, no emoji, held ≥ 1.0 s and ≥ 0.25 s per word, read time ≤ 1.5 s | V-TITLE |
| **H5** | **Dead air (talking_head spine):** at most 1 gap ≥ 150 ms per 15 s; jump cuts on word boundaries ±1 f. A pause of ≤ 0.4 s is allowed right before a verdict stamp | review |
| **H6** | **On the word:** every card, plate, chip, figure and stamp starts 2 f before its trigger word and is fully on within ±5 f; highlight bars start on the first word of their phrase | V-ONWORD |
| **H7** | **Face rule:** nothing in front of the face box in any layout; plates in L-full sit at chest height (cy 1380), ≥ 40 px below the chin; in L-split-top plates sit in the bottom band below the face or in the top band | V-FACE |
| **H8** | **Presence:** presenter visible 80–95% of runtime; the longest absence (L-hidden, L-band) is ≤ 8 s; after an absence the presenter returns in L-full or a split, never straight into another full-bleed card | V-PRESENCE |
| **H9** | **Promise integrity:** every "I will show you", "here is the proof", "let us check" is paid on screen within the same EB; a count ("3 cases") equals the cases shown; a CTA keyword is on screen ≥ 1.5 s | V-PROMISE |
| **H10** | **Citations exact:** every source beat shows masthead + date + headline; headlines and quotes are verbatim; highlight spans occur in the headline/excerpt text and are spoken while highlighted | V-CITE |
| **H11** | **Numbers traceable:** every displayed number is from the script, a cited source or the creator's inputs; compared numbers are figures in `plan/figures.json` and recompute | V-DATA |
| **H12** | **Number format:** Indian grouping (₹1,25,000), ₹ glyph (never Rs or INR in text you write; a verbatim headline keeps its own notation, see §5.5), lakh/crore compact (₹12.5 L, ₹3.2 Cr), up to 2 decimals for prices | V-NUMFMT |
| **H13** | **Inserts recorded:** every third-party moment is creator-supplied or a created substitute, recorded in `plan/inserts.json` | V-INSERTS |
| **H14** | **Hue cap:** ≤ 3 bright roles per frame (the rim + red + one of yellow/green/cyan) | V-HUES |
| **H15** | **Layouts:** only the F-A layouts (§3.2), within their shares | V-LAYOUT |
| **H16** | **Spelling:** names of people, outlets, places and laws are spelled exactly as in the creator's sources or script; add them to the glossary | review |
| **H17** | **Audio:** −14 LUFS integrated, true peak ≤ −1.5 dBTP, hard end ≤ 6 f after the last word (NC-8) | review |
| **H18** | **Determinism:** every frame a pure function of its index; particles and textures seeded (NC-9) | review |

**H-TB text-burden rule** (captions off, PV-6): with no captions, a plate, chip, card, figure or stamp **starts or changes at least every 4 s**, and **every proper noun, date, place and number that is spoken appears on screen** (as a plate, a chip, a card highlight or a figure) within ±5 f of the word. Exempt: a number or name that the same EB already shows on screen, and pronouns. `check: V-CADENCE (max_gap_s 4.0) + review` (the plate list from P5b is compared with the beat sheet at QA).

### 2.4 NEVER list
| ID | Never |
|---|---|
| N1 | Speech subtitles of any kind, karaoke words or kinetic captions. Text on screen is evidence, plates, figures or verdicts only |
| N2 | A fetched logo, masthead image, photo or clip. Outlet names are **set in type** unless the creator supplied the screenshot |
| N3 | A paraphrased headline or quote presented as the source's words; a highlight on words the creator does not say |
| N4 | a created card made to look like a real outlet's page (no outlet fonts, colours or layout copied) |
| N5 | Stock clichés: globes, newsroom stock loops, "breaking news" wipes, hooded hackers, gavels. Show the actual document, place, number or person |
| N6 | Meme sounds, emoji, stickers or comedy marks (comedy is off). A stamp is a verdict, not a joke |
| N7 | Red text on the red backdrop, yellow text on the gold backdrop, white plate text without its dark plate on a light photo |
| N8 | More than one backdrop swap per reel; a backdrop that clashes with the rim colour (always change both with the theme) |
| N9 | Transitions outside T-01…T-11; zooms outside Z-0…Z-4; light leaks other than the T-06 burn; RGB-split packs, film burns, glitch packs; a 1-frame jump re-crop every few seconds (not this style: the presenter's camera is locked between punches) |
| N10 | Two burns within 2.5 s; a burn longer than 18 f or with more than 2 bright peaks; more than 6 burns per 60 s |
| N11 | Personal identifiers visible in screenshots (phone numbers, emails, addresses, account IDs of private people): blur them for their whole time on screen (NC-14) |
| N12 | Graphics that only decorate. Every plate names something spoken; every card proves something said |

Buyers add **BN1…** `[VAR]`.

---

## §3 Worlds, layouts, stage moves, safe zones `[REQ] [DNA; coordinates TUNE ±5%]`

### 3.1 Worlds
| ID | Kind | Look (from the active theme) | Carries | Enter / exit |
|---|---|---|---|---|
| **W-backdrop** | backdrop | Radial three-stop gradient centred (540, 640–700): TH-crimson `#D45A44 → #B8352A → #7A1C14`; mottled texture (8 seeded soft blobs, ±12% lightness, 220–480 px), noise 0.06, vignette 0.35, 10–14 drifting embers (2–5 px, accent at 35%, 6–14 px/s upward) | The matted presenter in L-full, inside the split's footage band, inside the PiP | Always under the cut-out (P-BACKDROP). Swapped at most once per reel (P-BACKDROP-SWAP) |
| **W-evidence** | stage | `#09090B`, noise 0.05, vignette 0.4 | The top panel of L-split-top, the bottom panel of L-split-bottom, full-bleed created cards (L-hidden, L-pip-ring) | `world` cue at the stage change; cards blur in on it |
| **W-data** | stage | `#050506`, a 520 px accent glow at 8% drifting ±16/12 px, noise 0.06, vignette 0.45 | The data stage (P-DATA-STAGE, P-PRICE-TABLE, P-SHARE-PIE) with the presenter in L-pip-card | World flip at the stage change to L-pip-card |
| **W-map** | canvas | `#24262B` (water), noise 0.05, vignette 0.3 | Route maps and schematic maps (P-ROUTE-MAP) | World flip at the panel arrival |
| footage | footage | The creator's room, unchanged | TH-room reels only (no backdrop plate) | — |

### 3.2 Layout library
| ID | Engine | Presenter rect | Graphic rect | Treatment | Share (F-A) | Use |
|---|---|---|---|---|---|---|
| **L-full** | `full` | 0,0,1080,1920; head top y 140–260 | — | backdrop plate behind the cut-out | 30–65% | Claims, opinions, the verdict, the end |
| **L-split-top** | `stack` seam_y 950, top `graphic`, bottom footage (face 0.30, eye 0.40) | 0,950,1080,970 (face ≈ 290 px tall) | 0,0,1080,946 | 12 px `primary` hairline on the seam (measured 9–16 px: v03 @1:01, v02 @0:02.5) | 15–50% | The default evidence layout: articles, photos, clips, maps above the presenter |
| **L-split-bottom** | `stack` seam_y 960, top footage (face 0.30, eye 0.42), bottom `graphic` | 0,0,1080,960 | 0,964,1080,956 (text above y 1500) | 12 px `primary` hairline (v04 @0:23 bronze `#B47027`, 14 px) | 0–40% | Money and data reels (v04): the product/object or a card rises from below |
| **L-pip-ring** | `pip` circle d 480, ring 10 px `primary`, shadow 0.45, face 0.6 | circle centred (370, 1440) (v02 @0:29.5: outer ring x 116–616, y 1150–1710) | full frame behind | — | 0–25% | Long reads of one full-bleed article (> 4 s), full-bleed clips and reconstructions |
| **L-pip-card** | `card` 340×420 at (64, 1180), radius 8, border 6 px `primary`, glow `primary` 28 px, face 0.55 | 64,1180,340,420 | the rest of the frame | — | 0–20% | The data stage (P-DATA-STAGE) |
| **L-band** | `blurfill` band 608 at cy 960, blur 40, luma −0.55, `src: <clip asset>` | none (absence) | — | — | 0–12% | A creator-supplied 16:9 TV clip |
| **L-hidden** | `hidden` | none (absence) | full frame | — | 0–15% | Full-bleed proof: a vertical clip, a photo, a reconstruction, ≤ 8 s |

PiP positions (inline `corner` on the stage entry): **bottom-left-centre (380, 1470)** default (v02); **top-right (796, 370)** when the card's text block sits low (v03 @0:06); **bottom-right (796, 1400)** when the card's text is left-aligned and short (v03 @0:46); **bottom-left (290, 1490)** for a full-bleed clip whose subject is on the right (v03 @1:30). Never move the PiP while it is on screen; a new position needs a new evidence item.

**Layout schedule rule.**
- L-full runs 2–10 s per stint. The framing is locked (measured < 3% scale drift over 4 s, v01 @1:29.2–1:33.3); a stint gets at most one Z-2 punch-in (on its key word) or a Z-1 slow push, never both, and live gestures carry the rest.
- L-split-top / L-split-bottom run 2–8 s per evidence item; switch **on the source word** (the outlet name, "report", "according to", "this video", the person's name) within ±0.25 s.
- L-pip-ring is used only when a card must be read full-frame for > 4 s or a clip is vertical; ≤ 12 s per stint.
- L-hidden ≤ 8 s; L-band ≤ 8 s; both are followed by L-full or a split.
- L-split-top and L-split-bottom never alternate inside one EB; pick one orientation per reel (top for news and people, bottom for money and objects) and keep it.

### 3.3 Stage moves (G)
| ID | Move | Recipe (30 fps) | Use |
|---|---|---|---|
| **G-1** | Slide-down split | `via: slide-down`, **28 f**, ease `slide`: the graphic band and the seam ride in from y 0 → 950 while the presenter rescales into the bottom band. **Measured** (v02 @0:01.16–0:02.64, seam per frame): fast start, then a long settle: 50% of the travel by 0.20 s, 80% by 0.52 s, 95% by 0.92 s, at rest by 1.4 s; the presenter starts shrinking ≈ 4 f before the band appears (v01 @1.17, v02 @1.0). 28 f `slide` is the closest G3-safe curve (gap: expo-out). The card inside blurs in (T-04) from f4 | L-full → L-split-top, on the source word |
| **G-2** | Rise split | `via: morph`, **18 f** (v04 @0:00.50–0:01.10: presenter to ≈ 0.75 scale, panel at the seam by 0.9 s, settled 1.1 s): the presenter window shrinks into the top band while the hairline fades in on the seam (y 960); the graphic scene uses `in: "none"` and animates its own `translateY(956 → 0)` with the slide ease over the same 18 f. Engine request R-2 asks for a true bottom slide | L-full → L-split-bottom |
| **G-3** | Return | **T-11 blur-through cut** (`via: cut` under the blur): split → full or split → full-bleed (v02 @0:03.64–0:04.00). No slide-up return was measured; `slide-up` 12 f is the fallback when a cut would land mid-word | Back to the presenter for the next claim or the verdict |
| **G-4** | Into the ring | **T-11 blur-through cut** into L-pip-ring: the whole frame blurs out 5 f, cuts with the ring already in place, the new frame resolves 5–6 f (v02 @0:27.36, v03 @0:05.35–0:05.68). `pip-shrink` 10 f only when the same footage continues behind the ring | L-full or a split → L-pip-ring |
| **G-5** | Out of the ring | T-11 blur-through cut, or a T-06 burn at a section change; `pip-grow` 10 f as the fallback | L-pip-ring → L-full |
| **G-6** | Card shrink | `via: shrink-to-card` 12 f into L-pip-card, world flips to W-data on the same frame | Into the data stage |
| **G-7** | Cut out / in | `via: cut` (0 f) into L-hidden or L-band, under a T-06 burn or a T-11 blur-through | Full-bleed proof |
| **G-8** | Fade-through | `via: fade-through` 12 f | Between L-pip-ring and a split (the engine picks it when the window cannot travel smoothly) |

### 3.4 Layout diagrams
```
L-full (claim)                         L-split-top (evidence)
┌─────────────────────────┐ 0          ┌─────────────────────────┐ 0
│ (IG top UI, keep clear) │ ←110       │ credit line y 140 (TC-legal)
│                         │            │  ╭───────────────────╮  │ ← card column x 96–984
│      ╭──head──╮         │ ← 140–260  │  │ masthead · date   │  │   y 150–900
│      │  face  │         │            │  │ HEADLINE ▇▇▇▇▇▇   │  │   (red bars wipe in)
│      ╰────────╯         │            │  ╰───────────────────╯  │
│   backdrop plate        │            │   NAME PLATE (y ≤ 880)  │
│     (W-backdrop)        │            ├═════════════════════════┤ ← seam 950, 12 px rim
│  ▐ 30 SEPT 2026 ▌       │ ← plate    │      ╭──head──╮         │ ← head top ≈ 1040
│     cy 1380             │   cy 1380  │      │  face  │         │
│                         │            │  ▐ 8 JAN 2026 ▌ cy 1300  │ ← plate in band
│ (IG bottom UI, no text) │ ←1540      │ (IG bottom UI, no text) │ ←1540
└─────────────────────────┘ 1920       └─────────────────────────┘ 1920

L-pip-ring (long read)                  L-pip-card (data stage, W-data)
┌─────────────────────────┐            ┌─────────────────────────┐
│        MASTHEAD         │ ← y 230    │        ▐ 2014 ▌         │ ← year chip y 560
│ Headline in 2–3 lines   │            │  [barrel]   $105        │ ← y 700–860
│ excerpt ▇▇▇▇ highlighted│            │            (PER BARREL) │
│ excerpt lines ≤ y 1200  │            │  [nozzle]   ₹72         │ ← y 960–1120
│                         │            │            (PER LITRE)  │
│     ◯ ring Ø480         │ ← cy 1440  │ ┌──────┐                │ ← card 64,1180
│    (presenter)          │            │ │ face │                │   340×420, rim glow
└─────────────────────────┘            └─────────────────────────┘
```

### 3.5 Safe zones and bands
- Meaning text: x 64–1016, y 110–1500 (NC-5). Nothing readable in y > 1540 or in x > 970 between y 900 and 1540.
- **Plate band (L-full):** centre y 1380 (TUNE 1220–1450; v02 sat at ≈ 1240, v03 at ≈ 1380); plates never above y 1180 in L-full (they would touch the chin).
- **Plate band (L-split-top):** in the bottom band centre y 1300; in the top band the name plate's bottom edge sits 70 px above the seam (y ≤ 880).
- **Card column:** x 96–984; top band y 150–900 (L-split-top); full frame y 230–1200 (L-pip-ring, L-hidden), leaving the PiP rect + 40 px clear.
- **Credit line:** x 64, y 140 (TC-legal 24 px), only on creator-supplied clips and screenshots.
- **Stamp box:** x 140–940, y 560–1100 (over the evidence or the backdrop, never over the face).

### 3.6 Presenter rules
- Share 80–95%; longest absence 8 s (L-hidden, L-band). Return by a G-3 / G-5 blur-through cut or a T-06 burn into L-full.
- Crops: L-full head top y 140–260 and chin y 760–1000 (measured: v03 @0:00.3 134/768, v01 @0:00.5 180/1005, v02 @0:01 150/930; the face is ≈ ⅓ of the frame height, so a wide desk take needs a 1.35–1.6× base punch-in); L-split-top head top ≈ 1040 (face ≈ 290 px); L-split-bottom head top ≈ 120–180; PiP face fills ≈ 60% of the circle; L-pip-card face ≈ 55% of the card height.
- Nothing sits behind the head (no E1). The backdrop plate is the only thing behind the cut-out.
- Z-2 punch-in is 1.20× (measured 1.12–1.23); a 1080p source allows it up to 1.25× on top of the base reframe, 4K up to 1.35× (TUNE limit).

---

## §4 Colour, themes, grades `[REQ] [roles' meanings DNA; brandable hex VAR; theme hues TUNE]`

### 4.1 Role palette
| Role | Hex (default) | Its one job | Text on it | Contrast | Brandable |
|---|---|---|---|---|---|
| `primary` **rim** | `#EE0000` ({{BV-02.primary|#EE0000}}) | Split hairline, PiP ring, PiP-card border and glow, the date plate's wipe bar, the year-chip underline | `paper` | 5.5:1 | yes (the theme pack overrides it per topic) |
| `accent` **marker yellow** | `#F9E81F` ({{BV-02.accent|#F9E81F}}) | Keyword and number chips, map place labels and route lines, yellow highlighter on posts | `ink` | 13.9:1 | yes |
| `bad` **evidence red** | `#E30400` (sampled on v02's BBC bars) | Highlight bars (the toolkit darkens them until white reads ≥ 4.6:1), FAKE/SCAM/FALSE stamps, the higher or worse number | `paper` | 4.8:1 | no (fixed) |
| `good` **verified green** | `#2BD94A` | TRUE/CONFIRMED stamps, the lower or better number on the data stage | `ink` | 10.4:1 | no (fixed) |
| `data` **chart cyan** | `#3FE0D0` | Chart lines, bars and the map's secondary route | `ink` | 12.0:1 | no (TUNE) |
| `plate` | `#121214` | Fill of date, name and keyword plates (90% opacity) | `paper` | 18.7:1 | no |
| `ink` / `paper` | `#0B0B0B` / `#FFFFFF` | Text on yellow/green / plate and card text, underlines | — | — | no |
| `night` | `#09090B` | W-evidence and W-data | — | — | no |
| `slate` | `#24262B` | W-map water, map panels | — | — | no |
| `flash` | `#FCF88B` (ramp `#FFFDE0 → #FCF88B → #E6902A → #C04129`, sampled on the burns v01 @1:28.7–1:29.2, v04 @0:15.3–0:15.8) | The T-06 light-leak burn (light pass only) | — | — | no (TUNE list) |

### 4.2 Meanings
- **Red = evidence and alarm:** the highlighted phrase, the false claim, the higher price. Red is never decoration.
- **Green = verified or better:** a TRUE stamp, the lower/older price.
- **Yellow = look here:** a keyword chip, a number chip, a place on the map, the route.
- **The rim colour = the theme:** it frames the presenter (hairline, ring, card border) and nothing else.
- **B&W = archive:** photos of public figures and old clips may run in B&W (§4.4).
- Brand colours of outlets never appear on created cards (N4).

### 4.3 Theme packs `[DNA policy; VAR colours]`
| Pack | Backdrop (W-backdrop radial stops) | Rim (`primary`) | Topic → theme rule (`when`) | Evidence |
|---|---|---|---|---|
| **TH-crimson** (default) | `#D45A44 → #B8352A → #7A1C14`, mottled red | `#EE0000` (seam `#EE0000`, ring `#FA0405`, v02) | Rights, law, courts, crime, police, detentions, elections, protest, injustice | v02 (red mottled, red hairline and ring) |
| **TH-ember** | `#F2A12A → #D9730E → #8F3605`, flame orange with embers | `#C84A0C` | War, conflict, media and propaganda, disasters, breaking news | v01 (orange flame, orange PiP border) |
| **TH-gold** | `#E8C35A → #C49A2A → #7C5A10`, gold marble | `#B47027` (hairline sampled v04 @0:23) | Money, prices, taxes, inflation, budgets, business, money scams | v04 (gold marble, bronze hairline, gold PiP border) |
| **TH-slate** *(inferred)* | `#4C7099 → #2C4A6E → #121F33`, cool steel | `#2F6FD0` | Tech, AI, science, health, climate, space: topics without alarm | not observed; added so cool topics are not forced into red/orange/gold |
| **TH-room** | the creator's real room (no plate); W-backdrop values only colour the world fallback | `#EE0000` | Incident reconstructions and calm explainers shot in a tidy real room; or the matte failed (FB-1) | v03 (beige curtains, red hairline and ring) |

Rules:
- **One pack per reel** (`per_topic`), declared in the reel header. When a reel spans topics, pick the topic of the **verdict**.
- The buyer's brand colour (BV-02) is the base `primary`; each pack keeps its own rim because the colour carries the topic.
- Every pack passes NC-4 with `paper` on its rim (checked by `veos tokens`).
- **P-BACKDROP-SWAP** (≤ 1 per reel, at an EB boundary): the plate may change to a created **place pattern** in the same hue family (a flag's stripes rendered as soft bands, a map silhouette) for the EB about that place (v02 @0:13 US-flag plate). The rim does not change.

### 4.4 Grades (scene-level; no footage grade)
The presenter footage is **not regraded**. Clip treatments are applied inside the scene that shows the creator's clip or photo (CSS filters; the engine's grade module is not required):
| ID | Treatment | Filter | When | Max |
|---|---|---|---|---|
| **GR-bw** | Archive B&W | `grayscale(1) contrast(1.12) brightness(0.92)` | Photos of public figures and archive clips in the top panel (v02 @0:01 B&W podium photo) | no limit; never twice in a row on two different people |
| **GR-alarm** | Red tint | a `bad` overlay at 45% with `mix-blend-mode: multiply` + `brightness(0.85)` | The moment a clip is declared fake or dangerous (v01 @2:19, v04 @1.5 creeping red) | 2 per reel |
| **GR-dim** | Card bed | `brightness(0.42) blur(6px)` on the photo behind a full-bleed card | Full-bleed citation cards over the creator's photo (v02 ACLU, CNN) | — |

Rules: never two different treatments on consecutive clips; a treatment never touches the presenter.

### 4.5 Rules
- ≤ 3 bright roles per frame (`max_bright_per_frame` 3): rim + red + one of yellow/green/cyan.
- Yellow chips always carry `ink` text; red bars always carry white text; plates always carry white text on `plate`.
- On TH-gold, yellow chips get a 3 px `ink` outline (yellow on gold is N7).
- The flash (`flash` role) is a light pass, never a fill for text.

---

## §5 Type & caption system `[REQ]`

### 5.1 Font map `[slots DNA; families TUNE within class]`
| Slot | Family (bundled) | Weights | Font class (TUNE boundary) | Used for |
|---|---|---|---|---|
| `display` | **Montserrat** | 600–900 | geometric sans 600–900 | Date/name/place plates, keyword chips, quote overlays, CTA plate, sans card headlines |
| `numeric` | **Montserrat** | 700–900, tabular | geometric sans with tabular figures | Data values, year chips, number chips |
| `serif` | **Source Serif 4** | 400–700 | text serif | Created headline cards (broadsheet look), mastheads set in type |
| `stamp` | **Anton** | 400 | condensed heavy caps | Verdict stamps only |
| `mono` | **JetBrains Mono** | 500–700 | monospace | MAP NOT TO SCALE, other TC-legal tags |
| `deva` | **Noto Sans Devanagari** | 600–800 | Devanagari sans | Plates and chips when BV-05 picks Hindi on screen (Deva) |

Outlet logos are never drawn; outlet names are set in `serif` 700 (broadsheets) or `display` 800 (TV, agencies, wires).

### 5.2 Headline element: the plate `[DNA recipe; NICHE text]`
The style has **no banner**. Its headline element is the **plate** (kind `plate`), which does the hook's labelling (v02 "Donald J Trump", v03 "30 SEPT 2026") and the whole reel's text burden.

| Property | Date plate (P-DATE-PLATE) | Name plate (P-NAME-PLATE) |
|---|---|---|
| Fill | `plate` `#121214` at 90%, radius 4, padding 14/30 | none on dark photos; `plate` at 75%, radius 10, padding 10/26 on busy or light photos |
| Text | `display` 800, 64–88 px (default 80; v03 @0:00.3 cap 56 px), white, ALL CAPS, on `plate` at 70 % (sampled `#313A4B` over a blue tee), tracking 0.02 em (Latin only; Deva keeps case) | `display` 800, 60–76 px (default 68), white, ALL CAPS, shadow `0 3px 12px rgba(0,0,0,.75)` |
| Underline | 4 px `paper`, full plate width, 6 px under the text box | none |
| Size range | ≤ 4 words ("8 JAN 2026", "30 SEPT 2026") | ≤ 4 words (full name; a title line 40 px below it only if spoken) |
| Position | L-full: centre x 540, cy 1380; L-split-top bottom band: cy 1300 | Bottom-centre of the photo, bottom edge 70 px above the seam (y ≤ 880) or 70 px above the card bottom |
| Entry | L → R reveal behind a `primary` leading bar, **24 f, ease-out**: 50% of the width by f6, 90% by f15, at rest by f24; the bar is 60 px wide at the start and thins with the speed to 0 px at rest (it never fades separately) (measured v02 @2:03.08–2:04.12) | rises ≈ 60 px out from behind the seam (masked at the panel's bottom edge), **5 f**, ease-out, no fade (v02 @0:02.00–0:02.16) |
| Life | static; the underline grows with the reveal | static |
| Hold | ≥ 1.0 s and ≥ 0.25 s/word; typical 1.2–7.0 s (v02 held "8 Jan 2026" 7 s while he talked about it) | for as long as the photo is on screen, ≥ 1.0 s |
| Exit | fade + blur 0 → 8 px over 12 f while drifting down 24 px (v02 @2:10.1–2:10.5, v03 @1.0–1.17) | fade with the photo |
| Lifetime | `section` (one per spoken date) | `section` |

### 5.3 Caption system
**§5.3 Caption profile: OFF (`profile.captions.mode = off`).** No speech captions; H-TB (§2.3) and the plates of §5.2/§5.4 carry the text burden. `tokens.captions` is `null`; set `timeline.captions.subtitles: "off"` in every reel.

### 5.4 Other text systems
| ID | Element | Recipe | Class | Hold |
|---|---|---|---|---|
| **TX-1** | Place pin (P-PLACE-PIN) | On maps: `accent` fill, `ink` text, `display` 700 40–48 px, radius 4, padding 6/14, a 4 px leader to a 14 px dot. On footage: white `display` 800 56 px with shadow, top-right x ≤ 940, y 150–220 ("Pasadena, CA", v02 @1:20) | TC-label | while the place is on screen, ≥ 1.0 s |
| **TX-2** | Keyword chip (P-KEYWORD-CHIP) | opaque charcoal `chip` fill `#3F3F3F` (or `accent` fill with `ink` text for a defined term), `display` 800, **88–108 px** (v03 @0:36.5 "HIJACKING": cap 74 px, chip x 190–864, y 1266–1414), ALL CAPS, radius 8, padding 14/30; **at most 840 px wide (x 120–960, clear of the IG button column x > 970 at chest height): a longer keyword steps the size down to 72 px, then breaks to 2 lines**; on the chest (cy 1340) in L-full or inside the top panel ("HIJACKING" v03 @0:36; "ASTROLOGY" v01 @1:15; "FZ 1073" v03 @0:04) | TC-label | 1.0–2.0 s |
| **TX-3** | Number chip (P-NUMBER-CHIP) | `accent` fill (`#F9E81F` sampled), `ink` text, `numeric` 800, **80–96 px** (v04 @1:13.5: cap 66 px, chip x 130–952, y 1328–1458), radius 6, padding 14/24, **at most 840 px wide (x 120–960, clear of the IG button column): longer values step down to 72 px or drop the unit to a second line**, 24 px `accent` glow at 45% (v04 @1:13 "₹32.98 PER LITRE") | TC-label | 1.0–2.0 s |
| **TX-4** | Year chip (P-YEAR-CHIP) | `numeric` 800, 84–104 px white on a `plate` slab, 6 px `paper` underline; on the data stage top-centre (y 560–660), or straddling the seam of a split (centre y = seam) (v04 @0:06, @1:15) | TC-display | the whole data scene |
| **TX-5** | Data value + unit | `numeric` 800, 110–170 px, colour by meaning (`paper`, `good`, `bad`), glow 16–28 px; unit line `numeric` 600, 40–48 px, ALL CAPS in brackets "(PER LITRE)" 12 px under | TC-display / TC-label | per figure step |
| **TX-6** | Verdict stamp (P-STAMP) | `stamp` (Anton), 130–210 px, ALL CAPS, `bad` (or `good`) text inside a 10 px rounded border of the same colour, rotate −8°, a seeded grunge mask (24 holes, 3–9 px, 35% erase), a soft fog of the same colour behind (40% at the centre) | TC-display | 1.5–2.5 s |
| **TX-7** | Quote overlay (P-QUOTE-OVERLAY) | `display` 800, 72–88 px, white, ≤ 2 lines, shadow `0 4px 16px rgba(0,0,0,.8)`, curly quotes, over the speaker's clip or photo, y 300–520 ("Make America Great Again", v02 @2:42) | TC-display | ≥ 0.25 s/word + 0.5 s |
| **TX-8** | Card headline (created) | `serif` 600, 58–66 px, white on the dark card (`theme: dark`), line height 1.18, ≤ 4 lines | TC-label | the card |
| **TX-9** | Legal tags | `mono` 700, 24 px, tracking 0.16 em: MAP NOT TO SCALE, "example" | TC-legal | the whole span |
| **TX-10** | Credit line | `display` 600, 24 px caps, "• SOURCE: <OUTLET>", white at 85% with shadow, x 64, y 140 | TC-legal | the whole span of the creator's clip/screenshot |
| **TX-11** | Question glyph (P-QMARK) | `display` 900 "?" 300–420 px, white outline only (4 px stroke) with an electric glow (`paper` 18 px) and 3 seeded flicker frames, on the chest | TC-display | 1.0–1.5 s |
| **TX-12** | CTA plate (P-CTA-PLATE) | Date-plate recipe at 64–80 px: "COMMENT {{BV-08.keyword|KEYWORD}}" or "LINK IN BIO", cy 1380 | TC-display | ≥ 1.5 s |

### 5.5 Language and number rules
- **On-screen language** (BV-05): plates and chips are written in the `on_screen` language. English (Latn) is the default; Hindi (Deva) uses the `deva` slot, no ALL CAPS (Devanagari has no case), plate size +8 px.
- **Names:** the real spelling from the source ("SMIT MACHCHHAR"); never translated.
- **Dates:** `D MON YYYY` in caps with a 3–4 letter month ("8 JAN 2026", "30 SEPT 2026"); Deva: "8 जनवरी 2026".
- **Numbers** (Hinglish / Hindi; English uses `$`, international grouping and K/M/B the same way): Indian grouping, `₹` pre-painted, compact lakh/crore on plates longer than 7 characters (₹1,25,00,000 → ₹1.25 Cr), up to 2 decimals for prices (₹32.98), dollars stay `$` with international grouping when the source is in dollars ($105). Ranges use an en dash without spaces (₹60–₹65). Units in brackets on the data stage ("(PER LITRE)"), inline on chips ("₹32.98 PER LITRE").
- **Verbatim beats format:** a source headline or quote that writes "Rs", "INR" or international grouping is quoted as written (NC-13). Show it as the creator's screenshot (P-CITE-SHOT) whenever possible. If it must be a created card, keep the verbatim text, and report the V-NUMFMT failure it causes at the checkpoint as a known engine gap (engine request R-6 asks V-NUMFMT to exempt verbatim `quote_text` / `source.headline`). Plates and chips you write always use ₹.
- **Script untouched:** text inside the creator's screenshots stays as supplied (Devanagari headlines included); created cards quote the script verbatim in the language it was spoken or written in.

---

## §6 Hook system `[REQ]`

**Hook title (every style, 8 Oct 2026; above anything below):** the on-screen title promises the viewer something: an outcome they want, a curiosity gap, or who it's for ("How to go viral as a doctor creating content", not the label "Reels for Doctors"). It doesn't have to repeat the spoken words; it has to be true to what the reel delivers. A title shown as someone's words (in quotes) is still word for word. This section sets the title's shape (lines, sizes, word limits, case, the keyword device), never its voice. Write 8–10 candidates from the formulas below plus the proven patterns ("How to X as a Y", "Why your X isn't working", "The X nobody tells you", "Stop doing X", "Your X vs mine", a number or a contrast), score them on outcome, curiosity, who it's for and brevity, check the best against the stopper tests, and pick; any "write 3" below means this, and the next two go to the storyboard as alternates. A style with no on-screen title applies this to its post title.

### 6.1 Stopper tests
| Test | This style's number | Why |
|---|---|---|
| ST-1 Thumbnail | **off** | f0 is a blurring face on a coloured plate, not a thumbnail (v01, v02 @0.0). The post's cover is chosen separately (App. A) |
| ST-2 Mute | **off** | `mute_policy: sound_on`; the plates make the first 3 s partly legible anyway |
| **ST-3** Motion at f0 | live footage + Z-0 pull-open (1.30 → 1.00) under the focus pull | v01, v02 measured: scale 1.23–1.33 → 1.00 by 0.45–0.52 s, sharp by 0.38 s; v03, v04 live gesture |
| **ST-5** Change count | **≥ 4 weighted SCs in 0–3 s** | v01: blur-in, slide-down, TV arrives, TV sharpens; v04: slide-up, red tint, stamp, flare |
| **ST-6** Payoff-by | **evidence panel by 1.5 s; first label by 2.0 s** | v01 1.33 / 1.83, v02 1.33 / 2.0, v03 0.17 (plate) / 1.5 (route label), v04 0.67 / 1.83 |

### 6.2 Default archetype: HA-09 Evidence slide `[DNA]`
Three variants of the same archetype. Pick by the first sentence: **H9-A** when it names a source, a person or an event; **H9-B** when it opens on a date or an incident; **H9-C** when it opens on an accusation (scam, fake, lie).

**H9-A "Panel slam" (default; v01, v02)**
| t (s) | Beat | Tone | Visual | Layout / camera | Cue (from the pack) |
|---|---|---|---|---|---|
| **f0** | First word | claim | Presenter alone on the backdrop plate, **tight and blurred**: Z-0 `pull-open` 1.30 → 1.00 over 36 f (ease `expoOut`) under **P-FOCUS-PULL** (the camera preset's built-in defocus: 30 px held f0–f7, sharp by f11). Measured v02: 1.33 → 1.00, 75% of it by 0.52 s; v01: 1.23 → 1.00 by 0.45 s | L-full, Z-0 | `hook`: soft sub hit on f0 |
| 0.33–1.0 | The claim ("X has done Y…") | claim | Face sharp; gestures carry the line. No text yet unless a date/name is spoken (then its plate, H-TB) | L-full | — |
| **1.0–1.3** | The source word (outlet, person, event) | evidence | **G-1 slide-down** (28 f, long settle) into L-split-top on the source word ±0.25 s; the 12 px rim hairline rides in with the seam | L-split-top | `transitions`: whoosh on the slide |
| **1.2–1.5** | — | evidence | The evidence **blurs in** in the top panel (T-04: blur held, snaps sharp by f9–f12 as the band settles, v01 @1.45–1.85): a citation card (P-CITE-SHOT / P-CITE-CARD), a person photo in GR-bw (P-PERSON-PHOTO) or a TV frame (P-TV-SCREEN). Evidence readable by 1.5 s; scene `kind: "evidence"` | L-split-top | `reveals`: card pop |
| **1.5–2.0** | The key words | evidence | **First label lands, `payoff: true`:** the name plate rises (P-NAME-PLATE), or the first red bar wipes on the spoken phrase (P-CITE-*), or a place pin drops | L-split-top | `reveals`: tick |
| 2.0–3.0 | Continuation | evidence | Something moves inside the panel: the photo's arrival push 1.00 → 1.15 (15 f, ease-out, v02 @1.52–2.0), a second highlight span, or a hard cut to a second photo of the same event with the name plate staying (v02 @2.36) | L-split-top | — |
| 3.0–5.0 | The turn ("but…", "the truth is…") | claim | **G-3 blur-through** to L-full or straight to a full-bleed clip (v02 @3.64–4.0), a Z-2 punch-in on the turn word, or a **T-06 burn** into EB-1 | L-full | `transitions` |

**H9-B "Dated incident" (v03)**
| t (s) | Visual | Layout / camera |
|---|---|---|
| f0 | Presenter sharp (TH-room or a plate), live gesture, camera locked | L-full |
| **0.17** | **Date plate** wipes in at cy 1380 ("30 SEPT 2026"), grey → solid by 0.33 | L-full |
| 0.33–1.0 | Plate holds while the incident is named | L-full |
| 1.0–1.17 | Plate exits (drift down + blur) | L-full |
| **1.33** | **G-1 slide-down** into L-split-top: a map panel on W-map (`kind: "evidence"`) | L-split-top |
| **1.5–1.83** | **Route line draws** from the origin (accent, 6 px, 18 f) and the origin's **place pin** drops (`payoff: true`) | L-split-top |
| 2.0–3.0 | The map pans along the route (translate 0 → −180 px over 1.0 s, ease in-out); a second place pin at the far end | L-split-top |

**H9-C "Verdict first" (v04)**
| t (s) | Visual | Layout / camera |
|---|---|---|
| f0 | Presenter sharp on the plate (TH-gold for money), hands low, camera locked (v04 @0–0.5 measured static) | L-full |
| **0.5–1.1** | **G-2 rise split**: the presenter shrinks and the bottom panel rises (18 f) with the subject object in GR-bw on W-evidence (a creator photo, or a created icon card drawn with `fx.icon`), `kind: "evidence"` | L-split-bottom |
| 1.70 | **GR-alarm** red tint floods the panel in 3 f, just before the stamp (v04 @1.70) | L-split-bottom |
| **1.83** | **P-STAMP** "SCAM" / "FAKE" / "FALSE" slams in the panel (scale 1.35 → 1.00 in 5 f, rotate −8°) + **Z-4 shake** + red fog; `payoff: true` | L-split-bottom |
| 2.0–2.5 | Stamp holds; 2 seeded jitter frames | L-split-bottom |
| 2.5–2.7 | Stamp flares white and blurs (2–3 f), then a cut into the next evidence, which arrives with T-04 blur-in (v04 @2.67: blur held 9 f, sharp by +0.37 s) | L-split-bottom |

The stamp in H9-C states **the reel's verdict**, so the body must prove it. If the script only asks a question ("is it a scam?"), stamp "SCAM?" with the question mark and keep the loop open until the verdict at the end.

### 6.3 Allowed alternates `[DNA list; VAR choice per reel]`
**HA-07 "Then vs now" (live number; v04 @0:05–0:14)** for price, salary, budget or statistic reels.
| t (s) | Visual |
|---|---|
| f0 | W-data with the presenter in **L-pip-card** (bottom-left, rim glow); the **year chip** "2014" (kind `chip`) blurs in top-centre; the first value rolls ($87 → $105, 18 f) next to its icon (barrel, nozzle, house, pill: `fx.icon` or a drawn icon) |
| 0.6–1.0 | The second value lands (₹72, `good`), unit lines under both; the payoff is the number scene |
| 1.0–2.5 | The year chip swaps to "2026" (blur-out 6 f, blur-in 8 f); the same layout rebuilds with the new values on the same scale; the unknown value shows "???" in `good` until revealed |
| ≤ 3.0 | T-06 flash into L-full for the claim |
| Example (money) | "2014: oil $105, petrol ₹72. 2026: oil $96, petrol ???" |
| Example (health) | "2015: 6.9 crore diabetics. 2025: ???" (only with a sourced number) |

**HA-18 "Borrowed clip" (v01 TV montage @0:03–0:12; v02 clip @0:15)** for viral-claim debunks.
| t (s) | Visual |
|---|---|
| f0 | The creator-supplied viral clip full-bleed (L-hidden), or, when not supplied, a **created quote card** (P-POST-CARD) of the claim being debunked with its post header |
| 0.5–2.5 | The claim plays/reads; red bar on the claim's key words |
| ≤ 3.0 | Payoff = the clip/card itself (`payoff: true`) |
| ≤ 6.0 | The presenter is back (L-full via cut, or L-pip-ring over the clip from 2.0 s) |
| Example (money) | A viral post "Banks will charge ₹50 per UPI payment from 1 April" → presenter: "This is fake." |
| Example (health) | A viral clip "Drinking hot water cures dengue" → presenter in the ring, red bar on "cures dengue" |

### 6.4 Hook pairs: claim → evidence `[NICHE: example]`
The most important table for literal visuals. Add one row per reel at P7; the evidence column must exist (creator file) or be creatable verbatim from the script.

| Niche | Topic | Claim (spoken) | Source / number | Card type | Variant |
|---|---|---|---|---|---|
| Money & prices | Fuel prices | "Petrol is the biggest scam in the country" | crude $/barrel vs ₹/litre, 2014 vs today | P-DATA-STAGE + P-STAMP "SCAM" | H9-C / HA-07 |
| Money & prices | Bank charges | "Your bank is quietly charging you this fee" | the bank's notice / the regulator's circular (creator screenshot) | P-CITE-SHOT, highlight on the fee line | H9-A |
| Money & prices | Loan rules | "On 12 March the rules changed" | the date + the circular headline | P-DATE-PLATE → P-CITE-CARD | H9-B |
| Money & prices | Viral tax rumour | "₹50 tax on every UPI payment? Fake." | the viral post + the official denial | P-POST-CARD → P-CITE-CARD + P-STAMP "FAKE" | HA-18 |
| Health & science | Sugar myth | "This 'sugar-free' biscuit has more sugar than…" | the label numbers (creator photo) | P-CITE-SHOT with outline boxes + P-NUMBER-CHIP | H9-A |
| Health & science | Miracle-cure claim | "A celebrity says this cures diabetes" | the quote + a study / health-ministry statement | P-QUOTE-OVERLAY or P-POST-CARD → P-CITE-CARD + P-STAMP "FALSE" | HA-18 |
| Health & science | Outbreak | "On 3 August, the first case was found in Kerala" | date + place + the report headline | P-DATE-PLATE → P-ROUTE-MAP (spread) → P-CITE-CARD | H9-B |
| Health & science | Air quality | "Delhi's air was 14 times the safe limit" | AQI value + the WHO limit (figures) | P-DATA-STAGE (bars on one scale) | HA-07 |

### 6.5 Plate and title writing `[DNA formula; NICHE examples]`
The hook has no banner. You write (a) the **plates** (exact words from the speech: names, dates, places, numbers) and (b) the **post title** for the caption field and the cover.
- **Plate formula:** the spoken item, nothing added: "8 JAN 2026", "SMIT MACHCHHAR", "₹32.98 PER LITRE", "HIJACKING". ≤ 4 words (chips ≤ 3). No verbs, no emoji, no adjectives.
- **Post title formula:** `[claim or accusation] + [the object] + [! or ?]`, ≤ 8 words, sentence case with one CAPS word: "Petrol prices SCAM in 2026!", "Don't travel to X! You can be arrested", "X has been destroyed… by Indian media". Write 3; pick the one that (1) names the specific object, (2) promises a verdict the reel delivers, (3) fits 8 words.
- **Banned:** "shocking truth", "you won't believe", "exposed!!!", more than one "!" or "?", a verdict the body does not prove.

### 6.6 Hook sound
Cues allowed in the hook: one soft hit on f0, one whoosh on the slide, one pop on the card, one tick on the first label, one impact on a stamp (H9-C). The bed enters after the hook (§11).

### 6.7 CTA `[DNA device set; VAR values]`
The default is **no CTA** (`chosen: none`): the reel ends on the presenter's last line, hard end ≤ 6 f (v01, v02, v03).

| Device | Spoken pattern | On screen | Hold | Placement |
|---|---|---|---|---|
| `cross_promo` | "The full story is in my long video" | **P-CROSS-PROMO:** the long video's thumbnail (SH-6, creator file) on a dark card in the graphic band of the split, title line under it in `display` 700 40 px; fallback FB-6 | 2.0–3.5 s | last 4 s |
| `comment_keyword` | "Comment {{BV-08.keyword|KEYWORD}} and I'll send you the sources" | **P-CTA-PLATE** "COMMENT {{BV-08.keyword|KEYWORD}}" (kind `cta-keyword`) at cy 1380 in L-full; date-plate look, the keyword in `accent` | ≥ 1.5 s | last 3 s |
| `link_bio` | "Sources are linked in my bio" | **P-CTA-PLATE** "SOURCES · LINK IN BIO" | ≥ 1.5 s | last 3 s |

No silence is needed before the CTA (the voice runs on). No end card, no follow/save stack.

---

## §7 Structure & cadence `[REQ] [DNA]`

### 7.1 Structure type: `evidence`
**Arc:** hook (claim + first proof) → **EB-1…EB-n** (claim → evidence → counter-evidence) → **verdict** → (CTA). 100–170 s holds 4–7 evidence beats of 12–30 s each.

| Unit | Content | Length |
|---|---|---|
| Hook | HA-09 variant or an alternate | 3–8 s (≤ 15% of runtime) |
| EB (evidence beat) | One claim, its proof (1–3 evidence items), optional counter-evidence, optional mini-verdict | 12–30 s |
| Verdict | The answer to the hook's question; stamp | 4–10 s |
| End | Last line on the presenter; optional CTA | 2–6 s |

### 7.2 Markers
**`markers: none (spoken only)`.** No numbering, no chapter badge, no progress rail (v01–v04). Section changes are marked by a **T-06 light-leak burn** or a **backdrop swap** (≤ 1), never by a numeral. A spoken count ("three cases") is honoured by the cases themselves (H9).

### 7.3 Unit ritual: the evidence beat (identical every time; frames at 30 fps)
1. **Claim on the presenter** (L-full, 2–6 s): camera locked, then either Z-1 slow push (1.00 → 1.05 over 3–4 s) through the claim or one Z-2 punch-in (1.00 → 1.20, 12 f) on its key word, held to the next cut. Every spoken date/name/number gets its plate (P5b list) at cy 1380.
2. **Source word → split** (G-1 slide-down, 28 f) or, for a long read, **into the ring** (G-4 blur-through cut), within ±0.25 s of the source word.
3. **Evidence arrives** with T-04 blur-in (blur held, sharp by f6–f11), starting on f4 of the stage move. A photo then pushes 1.00 → 1.15 over 15 f (ease-out); a text card stays still.
4. **Highlight the spoken words:** each span's bar starts on its first word and wipes L → R **linearly over the time the phrase is spoken** (≈ 0.3 s per word, 12–30 f per span; measured 0.8 s for "11 September 2001" and for "undocumented immigration", v02 @0:27.52–0:28.32 and @0:28.80–0:29.60); bars accumulate in speaking order, never fade (`hlAt` = the word time − `t_in`).
5. **Label** the person/place/date on the evidence (P-NAME-PLATE, P-PLACE-PIN) if spoken.
6. **Hold** ≥ 1.0 s after the last bar; something moves every ≤ 4 s (a new bar, a second card, the live PiP; photos and renders drift, text cards hold still: v02 BBC card 0 % scale change over 4 s).
7. **Counter-evidence** (optional): a second card with **outline-box** highlights (white 4 px boxes) instead of bars, or the data stage.
8. **Return** (G-3 blur-through cut) to L-full for the presenter's conclusion, **or** a T-06 burn straight into the next item or EB.
9. **Verdict** (cluster end only): P-STAMP over the evidence or over the backdrop in the stamp box (x 140–940, y 560–1100) + Z-4 shake; hold 1.5–2.5 s.

### 7.4 Open loops and re-hooks
- **Loop types:** the hook's question ("is it a scam?"), the "???" value on the data stage (v04 @0:12–0:14), "but there is one more thing", a stamped "?" verdict (H9-C).
- **Payoff rule:** every loop is paid on screen: "???" becomes the number in the same layout; the "?" stamp becomes the verdict stamp; a promised clip is shown.
- **Re-hooks (long class): one every 20–30 s** (default 25 s): a T-06 burn **plus** a new evidence item of a new card type (screenshot card, clip, data stage, map, person photo). Two consecutive EBs never open with the same card type.
- **Intro cap:** hook ≤ 15% of runtime; there is no series card.

### 7.5 Rhythm and energy curve
- **Energy:** level and serious; it rises at each verdict stamp and at the data reveal. No comedy beats.
- **Escalation:** the strongest evidence comes last before the verdict (the official document, the number that settles it, the clip that contradicts the claim).
- **Ending:** abrupt. The last sentence on the presenter in L-full with a Z-1 push or a Z-2 punch on the last clause, hard end ≤ 6 f after the last word (v01 @2:36, v02 @2:57). With `cross_promo`, the thumbnail card fills the last 2–4 s.

### 7.6 Cadence (state changes)
| Token | Value | Why |
|---|---|---|
| `sc_per_10s` | **[2.5, 4.5]** | Captions off: changes come from cuts, burns, plates, cards, highlights and stage moves. Measured cuts alone: 3.0–3.4 per 10 s (scene detection, all four reels) |
| `hook_sc_3s` | **4** | ST-5 |
| `max_gap_s` | **4.0** (hook 1.5) | H-TB: a readable change at least every 4 s |
| `max_static_s` | **3.0** | live footage counts as motion; a full-bleed photo drifts; a text card may hold still only while the PiP is live, a bar is wiping or an embedded clip plays (v01 @1:33.4–1:39.5) |
| `caption_weight` | 0.5 (unused: captions off) | — |
| `cuts_per_min` / `median_shot_s` | null (measured 18–20 / min; median shot 2.0–2.9 s, p90 6.1–8.0 s, longest 8.4–13.1 s) | after merging blur and burn frames (0.2 s window); left null so V-CADENCE judges weighted SCs, not raw cuts |
| Budgets | burns 3–6 / 60 s (measured 3.4–6.0), ≥ 2.5 s apart; blur-in arrivals 4–7 / 60 s; Z-2 punches 1–3 / 60 s; stamps 1–3 per reel; evidence cards 3–6 / 60 s; plates 3–8 / 60 s | v01–v04 |

---

## §8 Visual system: graphics, B-roll and patterns `[REQ]`

### 8.1 Graphics role and budget
`graphics: support`. Evidence (cards, clips, photos, maps, data) fills **45–60%** of runtime, own graphics (plates, chips, stamps, figures) a further **8–15%**; the presenter's face is visible 80–95% because most evidence shares the frame with him (split, PiP). Per 60 s: **3–6 evidence items, 3–8 plates/chips, 3–6 light-leak burns, 0–2 stamps, ≥ 4 different patterns from ≥ 3 families.** Numbers that are **compared** become pictures (the data stage, one scale); a single number becomes a chip.

### 8.2 Families
| ID | Family | Source class | The creator supplies | Created substitute (§12.5) |
|---|---|---|---|---|
| **B-1** | Backdrop and stage | engine | a clean-background take (SH-1) | — (TH-room when no matte) |
| **B-2** | Plates and chips | engine | — | — |
| **B-3** | Citation cards (articles, reports, documents) | creator-supplied third-party | screenshots with masthead, date, headline (SH-2) | `fx.headlineCard` / `fx.citationStrip` (created) |
| **B-4** | Posts and quotes | creator-supplied third-party | screenshots of posts (SH-2) | `fx.quoteCard` (verbatim, no platform logo) |
| **B-5** | Clips (TV, phone video, speeches) | creator-supplied third-party | the clips (SH-3) | `fx.appUI({kind: "video"})` frame with the spoken line, or `fx.quoteCard` |
| **B-6** | People | creator-supplied third-party | photos (SH-4) | `fx.silhouette` + name plate |
| **B-7** | Data stage | engine (figures) | — (numbers from the script / sources) | — |
| **B-8** | Maps and routes | engine over a creator basemap, or created | a map screenshot (SH-5) | schematic map on W-map + MAP NOT TO SCALE |
| **B-9** | Reconstructions and illustrations | created | — | `fx.card` / `fx.diagram` / `fx.icon` scenes |
| **B-10** | Verdict and punctuation | engine | — | — |
| **B-11** | End devices | creator (own thumbnail) or created | the long video's thumbnail (SH-6) | a title card in the `fx.logoPlate` look |

### 8.3 Pattern specs
Motion at 30 fps. "Lead 2 f" = the element starts 2 f before its trigger word. Every text scene sets `text_class`; evidence scenes set `kind: "evidence"`, stamps `kind: "stamp"`, plates `kind: "plate"`, chips `kind: "chip"` (V-F0, V-TITLE).

**B-1 Backdrop and stage**
| ID | Name | Type | What is on screen | Motion recipe | When | Class / engine block |
|---|---|---|---|---|---|---|
| **P-BACKDROP** | Backdrop plate | stage | The W-backdrop gradient of the active theme, 8 seeded soft blobs (radial gradients, ±12% lightness, Ø 220–480 px), noise, vignette, 10–14 embers | Blobs drift ±10 px on 6–9 s sine cycles; embers rise 6–14 px/s, seeded (`ctx.rngStable`); no entry, no exit | The whole reel wherever the presenter is visible (except TH-room) | no text. One scene `behind: true`, z 1, box 0,0,1080,1920, painted in footage space so it follows the split, PiP and card windows and the camera |
| **P-BACKDROP-SWAP** | Place plate | stage | The plate changes to a created place pattern in the same hue family (flag stripes as soft 160 px bands at 25% over the gradient, or a country silhouette at 18%) | Cross-fade 12 f at an EB boundary; out the same way | ≤ 1 per reel, for the EB about that place (v02 @0:13) | a second `behind` scene; never with a rim change |
| **P-FOCUS-PULL** | Focus pull | footage-treatment | The whole frame blurred, resolving to sharp | Footage blur, drawn by core on the stage (footage, cut-out, z1 plates; graphics and captions stay sharp): 30 px defocus over 11 f, **held then snapped** (keys: full for f0–f7, 0 by f11; measured sharp at +0.38 s v01, +0.32 s v02). At f0 it is the `blur` of Z-0 (`camera_presets.pull-open.blur`, rides the pull-open); on a later presenter return it is a `timeline.blur` entry on the cut | f0 of H9-A (H1); a presenter return after a cut (v02 @2:02.9) | built-in: `camera_presets.pull-open.blur` = `{"kind": "defocus", "px": 30, "keys": [[0, 1], [7, 1], [11, 0]]}`; a return: `"blur": [{"t": <cut>, "kind": "defocus", "px": 30, "keys": [[0, 1], [7, 1], [11, 0]]}]`. No scene |
| **P-PUSH-EMPHASIS** | Emphasis push | footage-treatment | The presenter slowly closes in | Camera `push-drift` (Z-1) 1.00 → 1.05 over 3–4 s (linear), then hold (measured v02 @2:03–2:06.5) | A claim stint ≥ 3 s that gets no punch; the last sentence | camera preset |
| **P-PUNCH-IN** | Punch-in | footage-treatment | An eased push toward the face that then holds | Camera `punch-in` (Z-2) 1.00 → 1.20 over 12 f, ease-out (90% by f10), centred on the face; hold until the next cut, where `jump-wide` (Z-3, 1 f) restores 1.00 (measured v02 @0:13.28 1.22×, @2:09.36 1.19×; v04 @1:09.9 1.12×, @1:12.6 1.16×) | 1–3 per 60 s, on a "but", a number (just before its chip lands) or a name; at most one per stint | camera presets; 4K allows 1.35 |
| **P-SPLIT-SLIDE** | Slide-down split | stage | The evidence band slides down from the top with the rim hairline; the presenter drops into the bottom half | G-1: `slide-down` 28 f, ease `slide` (measured: long settle, 95% by 0.92 s) | On the source word (±0.25 s) | stage `L-split-top` |
| **P-SPLIT-RISE** | Rise split | stage | The presenter moves into the top half; the evidence rises from below | G-2: `morph` 18 f + the scene's own `translateY(956 → 0)` | Money/data reels, objects and products (v04) | stage `L-split-bottom` |
| **P-PIP-RING** | Ringed PiP | stage | The presenter in a Ø 480 circle with a 10 px rim ring and a soft shadow over a full-bleed card or clip | G-4: T-11 blur-through cut with the ring already in place (measured v02 @0:27.36, v03 @0:05.5); out G-5 the same or a T-06 burn | Long reads > 4 s, vertical clips, reconstructions | stage `L-pip-ring` (corner per §3.2) |
| **P-PIP-CARD** | Rim card | stage | The presenter in a 340×420 card with a 6 px rim border and a 28 px rim glow, bottom-left | G-6: `shrink-to-card` 12 f; the world flips to W-data | The data stage | stage `L-pip-card` |

**B-2 Plates and chips** (all `TC-label` unless noted)
| ID | Name | Type | What | Motion recipe | When | Engine block |
|---|---|---|---|---|---|---|
| **P-DATE-PLATE** | Date plate | overlay | §5.2 date plate, cy 1380 (L-full) or 1300 (split bottom band) | Lead 2 f; L → R clip-path reveal 24 f ease-out (50% by f6, 90% by f15) led by a `primary` bar 60 px wide that thins with the speed to 0; underline grows with it; hold ≥ 1.0 s; exit 12 f: fade + drift down 24 px + blur 0 → 8 px | Every spoken date (v02 @2:03, v03 @0.17) | bespoke scene z5, `kind: "plate"` |
| **P-NAME-PLATE** | Name plate | overlay | §5.2 name plate on the person's photo/clip, bottom edge 70 px above the panel bottom | Lead 2 f; rises ≈ 60 px out from behind the seam (clipped at the panel's bottom edge), 5 f ease-out, no fade; stays across a cut to a second photo of the same person (v02 @0:02.36); hold while the photo shows | Every spoken person's name shown with their photo (v02 @2.0, v03 @1:01) | bespoke scene z5, `kind: "plate"`; with no photo, P-PERSON-SIL carries the name |
| **P-PLACE-PIN** | Place pin | overlay | TX-1: a yellow label with leader and dot on a map, or a white place line top-right on footage | Dot pops 6 f (scale 0 → 1.15 → 1), leader draws 4 f, label wipes 6 f | Every spoken place on a map or a location clip (v03 @1.5, v02 @1:20) | inside the map scene, or a z5 scene on footage |
| **P-KEYWORD-CHIP** | Keyword chip | overlay | TX-2 on the chest (cy 1340) or in the top panel | Lead 2 f; rise ≈ 120 px + fade 0 → 1 over 14 f, ease-out, no blur, no scale (measured v03 @0:35.70–0:36.17); hold 1.0–2.0 s; exit blur-out 5 f (v03 @0:05) | A defined term, flight number, law or scheme name (v03 "HIJACKING", "FZ 1073"; v01 "ASTROLOGY") | bespoke z5, `kind: "chip"` |
| **P-NUMBER-CHIP** | Number chip | overlay | TX-3 yellow chip "₹32.98 PER LITRE" on the chest | Lead 2 f; fade 0 → 1 over 6 f (no overshoot), then the glow blooms 0 → 24 px over the next 6 f; usually right after a Z-2 punch on the number word (v04 @1:12.6–1:13.3); exit with a burn or a 5 f blur-out | A single spoken number not compared with another (v04 @1:13) | bespoke z5, `kind: "chip"`, `figure` when it comes from figures.json |
| **P-YEAR-CHIP** | Year chip | overlay | TX-4 slab "2014" on the data stage top-centre, or straddling a split seam | Blur-in 8 f; a swap to the next year = blur-out 6 f then blur-in 8 f (never a hard swap) | Then-vs-now comparisons, timelines (v04 @0:06, @1:15) | bespoke z6, `kind: "chip"`, `TC-display` |
| **P-QUOTE-OVERLAY** | Quote overlay | overlay | TX-7: the quoted words over the speaker's clip or photo, y 300–520 | Words appear in 2 groups on their spoken onsets, each a 5 f rise + fade; hold ≥ 0.25 s/word + 0.5 s | A famous line quoted aloud (v02 @2:42) | z5 scene, `TC-display`, `quote_text` verbatim (NC-13) |

**B-3 / B-4 Evidence cards** (z3 under a PiP, z4 in a split's band; `kind: "evidence"`; bars `hlRole: "bad"`)
| ID | Name | Type | What | Motion recipe | When | Engine block |
|---|---|---|---|---|---|---|
| **P-CITE-SHOT** | Screenshot card | overlay | The creator's screenshot framed full-width (x 70, w 940) in the top panel, or full-bleed under GR-dim with the PiP; red highlight **boxes** on the spoken lines; the credit line | T-04 blur-in (held, sharp by f6–f11); **no push** on text (measured static 4 s, v02 @0:27.5–0:31.4); each highlight wipes L → R linearly over its spoken phrase (≈ 0.3 s/word) | Any article, report, document or post the creator supplied | `fx.shot({asset, aspect, chrome: false, highlights: [{x, y, w, h, at, role: "bad"}], credit: "SOURCE: <OUTLET>"})` or `fx.citationStrip({asset, highlights, credit})` |
| **P-CITE-CARD** | Created headline card | overlay | A dark card (`theme: "dark"`), the masthead set in type, the date, the **exact** headline in `serif`, red bars wiping word by word on the spoken span | T-04 blur-in; static; bars: each span wipes linearly from `hlAt` over its spoken duration (≈ 0.3 s/word, 12–30 f), bars accumulate; spans ≥ 0.5 s apart | Every cited article the creator did not supply (FB-2) | `fx.headlineCard({masthead, date, headline, highlight: [...], hlAt, hlRole: "bad", theme: "dark", font: "serif", body: 3, x: 70, y: 150 (split) / 260 (PiP), w: 940, kind: "evidence"})` |
| **P-CITE-STRIP** | Source strip | overlay | A black "SOURCE · masthead · date" strip over the card body, a rim-coloured underline growing | The strip underline grows 10 f; the body as P-CITE-SHOT / P-CITE-CARD | When the masthead is not visible in the creator's screenshot (cropped) | `fx.citationStrip` |
| **P-DOC-EXCERPT** | Document excerpt | overlay | An official rule/law/manual excerpt: a dark card with a bold title line (`display` 800 52 px), a section line (40 px) and the verbatim excerpt (`serif` 44 px), red bars on the spoken clause (v03 @0:24 "Chapter 4. Air Traffic Control") | As P-CITE-CARD | Rules, laws, manuals, terms and conditions | `fx.headlineCard` with `kicker` = section, or a bespoke card in the same look|
| **P-OUTLINE-BOX** | Outline highlight | annotation | White 4 px rounded boxes (`paper`) around a number or date inside a card instead of red bars (v04 @0:37 "Rs 9.48/ltr", @1:01 "May 06, 2020") | The box draws (scaleX 0 → 1) 7 f at the word | Counter-evidence and figures inside a card, so red stays for the claim | `fx.shot` highlights with `role: "paper"`, or inside a bespoke card |
| **P-POST-CARD** | Post card | overlay | A generic post card (avatar initials, name, no platform logo), the verbatim post text, a **yellow marker** highlight (`hlRole: "accent"`) on the spoken words | Reveal word by word at 9 words/s from 0.28 s, then the highlight | A post or statement read aloud (v01 @0:25, @0:30) | `fx.quoteCard({quote, name, handle?, highlight, hlRole: "accent", theme: "dark", kind: "evidence"})`; with the creator's screenshot, P-CITE-SHOT with `role: "accent"` boxes |
| **P-THUMB-WALL** | Headline wall | overlay | 4–5 created headline cards (or the creator's screenshots) stacked in a column, scrolling up 60 px/s on W-evidence with a red glow edge (v01 @2:23) | The column enters from y 1920 over 12 f, then scrolls; each card's key word turns red as it passes y 700 | "Every channel said X", "dozens of reports" | a bespoke z4 scene composing headline-card blocks; one insert record per card |
| **P-TV-SCREEN** | TV frame | overlay | A drawn retro TV set (grey bezel, two knobs) on W-evidence with the creator's clip or a created headline card inside the screen | The set blurs in 8 f; the screen content cuts in 2 f later | Television claims, channel coverage (v01 @1.5) | a bespoke scene drawing the set; screen = `ctx.videoFrame(asset, lt)` or the created card; never a channel logo |

**B-5 / B-6 Clips and people**
| ID | Name | Type | What | Motion recipe | When | Engine block |
|---|---|---|---|---|---|---|
| **P-CLIP-PANEL** | Clip in the panel | overlay | The creator's clip cover-cropped into the top panel (0, 0, 1080, 946), the credit line | Cut in on the word; Ken Burns 1.00 → 1.04 if the clip is static | News footage or phone video that supports the claim | `fx.shot({asset, x: 0, y: 0, w: 1080, h: 946, chrome: false, radius: 0, credit})` in L-split-top |
| **P-CLIP-FULL** | Full-bleed clip | cut | The creator's vertical clip full-frame, the presenter in the ring or absent ≤ 6 s | Hard cut or T-06 in; G-4 adds the ring from 1.0 s if the clip runs > 3 s | Viral clips, eyewitness video (v02 @0:15, v03 @0:09) | `fx.clip({asset})` + stage L-hidden or L-pip-ring; `kind: "evidence"` |
| **P-CLIP-BAND** | 16:9 clip band | stage | A 16:9 clip in a 608 px band over a blurred copy of itself | `morph` 10 f into L-band | TV segments and landscape footage (v01 @1:05) | stage `L-band` with `src: <asset>` |
| **P-PERSON-PHOTO** | Person photo | overlay | The creator's photo of a named person in GR-bw, cover-cropped in the top panel, P-NAME-PLATE on it | T-04 blur-in; arrival push 1.00 → 1.15 over 15 f ease-out (v02 @0:01.52–0:02.0), then drift; the plate rises on the name | Politicians, officials, the people involved (v02 @1.5) | `fx.shot({asset, ...})` with GR-bw applied in a wrapper scene; name plate z5 |
| **P-PERSON-SIL** | Person card | overlay | A silhouette disc with a rim-coloured ring drawing, the name (76 px) and role (44 px) | Ring draws 16 f, silhouette rises 12 f, name 10 f | A named person with no photo (FB-4) | `fx.silhouette({name, role, accent: "primary", theme: "dark"})` |
| **P-ALARM-TINT** | Alarm tint | footage-treatment | GR-alarm red tint over a clip or photo | Tint floods 0 → 45% over 3 f, ≈ 3 f before the stamp or the verdict word (v04 @1.70) | The moment a clip is called fake or dangerous (v01 @2:19) | inside the clip's scene (filter + overlay) |

**B-7 Data stage** (§18; `figure` / `figures` on every scene)
| ID | Name | Type | What | Motion recipe | When | Engine block |
|---|---|---|---|---|---|---|
| **P-DATA-STAGE** | Then vs now | figure | W-data; the year chip top-centre (y 560); two rows, each: an icon (120–150 px, drawn), the value (TX-5, 130 px) and its unit line; the presenter in L-pip-card | Icon blurs in 8 f; the value rolls 18 f and lands on the spoken number (±5 f); the second year rebuilds the same layout on the same scale; "???" for the unknown | Prices, salaries, budgets, counts at two times (v04 @0:05–0:14, @0:26–0:30) | `VEOS.data.counter` per value + a bespoke icon scene; `scale_id` shared |
| **P-PRICE-TABLE** | Ranked table | figure | A two-column table (city/item · value) on W-evidence, rows 72 px, `display` 600 40 px; the spoken rows highlighted with an `accent` bar (ink text) | Rows stagger in 3 f; the highlight bar wipes 7 f on the spoken row | Lists of numbers by place or item (v04 @0:19) | a bespoke figure scene with `figures` bound |
| **P-BAR-COMPARE** | Bars on one scale | figure | 2–4 horizontal bars on one axis, values at the bar ends, a leader chip on the extreme | Bars grow 18 f in spoken order; the leader chip pops 6 f | "X times the limit", "A vs B" | `VEOS.data.bars({figures, scale, leader: {text, role: "bad"}})` |
| **P-CHART-CIRCLE** | Chart + circle | figure / annotation | A line chart card (white card, cyan line) or the creator's chart screenshot; a red hand-drawn ellipse (6 px `bad`) draws around the spoken point; a value tag on it | The card blurs in 8 f; the line draws 24 f; the ellipse draws 10 f with a 15° overshoot | A trend with one moment that matters (v04 @0:43, @1:26) | a bespoke figure scene (line from `figures`), or `fx.shot` + a bespoke ellipse scene |
| **P-SHARE-PIE** | Share donut | figure | A donut in `accent` with the share % (TX-5) and its label | Sweep 0 → value over 20 f; the % rolls with it | "61% of the price is tax" (v04 @0:52) | a bespoke figure scene, `kind: "figure"`, formula `ratio` |
| **P-MAP-CHART** | Chart on a map | figure | A boxed chart (white 3 px frame) over the dark map, cyan line, callout values "34,000 ft → 31,585 ft" | The box draws 8 f; the line draws 24 f; the callout box steps to the spoken point | Altitude, speed or level along a route (v03 @0:13–0:17) | a bespoke figure scene over P-ROUTE-MAP |

**B-8 Maps**
| ID | Name | Type | What | Motion recipe | When | Engine block |
|---|---|---|---|---|---|---|
| **P-ROUTE-MAP** | Route map | overlay | The creator's satellite/map screenshot in GR-bw (or the created schematic on W-map: land `#3A3D44`, water `slate`, simplified outlines), a 6 px `accent` route line drawing with a 14 px end dot, P-PLACE-PIN labels, MAP NOT TO SCALE when created | The route draws 18–30 f from origin to destination; the map pans along the route (≤ 180 px/s, ease in-out); labels drop on their spoken names | Journeys, flights, borders, spreads (v03 @1.33–2.83, @2:08) | `fx.shot` (creator basemap) or `fx.diagram` (created) + a bespoke route scene; engine request R-4 (geo maps) |

**B-9 Reconstructions**
| ID | Name | Type | What | Motion recipe | When | Engine block |
|---|---|---|---|---|---|---|
| **P-RECON** | Reconstruction | overlay | A created illustration of the event (a control panel, a code being typed, a room, an object) built from `fx.card` / `fx.diagram` / `fx.icon` top-left | Blur-in 8 f; one internal action every 1.5–3 s (a code typing, a light switching, an arrow moving) | Events no camera recorded (v03 @0:20–0:31, @0:46–0:57) | bespoke scenes`synthetic: true` |

**B-10 Verdict and punctuation**
| ID | Name | Type | What | Motion recipe | When | Engine block |
|---|---|---|---|---|---|---|
| **P-STAMP** | Verdict stamp | overlay | TX-6 stamp "FAKE" / "SCAM" / "FALSE" / "MISLEADING" (`bad`) or "TRUE" / "CONFIRMED" (`good`) in the stamp box, a red fog behind | Scale 1.35 → 1.00 in 5 f with rotate −8°; Z-4 shake (8 px, 6 f); the fog fades in 8 f; 2 jitter frames at +6 and +9 f; hold 1.5–2.5 s; exit: a 2 f white flare, then a cut | Cluster ends and the reel's verdict, 1–3 per reel (v01 @0:46, v04 @1.83) | a bespoke z6 scene, `kind: "stamp"`, `roles: ["bad"]` or `["good"]` |
| **P-QMARK** | Question glyph | overlay | TX-11 electric "?" on the chest | Strokes draw 10 f, 3 flicker frames, hold 1.0–1.5 s | The open question before the reveal (v04 @0:16) | a bespoke z5 scene |
| **P-FLASH-CUT** | Light-leak burn | overlay (light pass) | A full-frame warm light leak (screen blend) hiding the cut, over the whole frame including a split | **16 f** (measured 0.50–0.53 s, v01 @1:28.67, v03 @0:19.25, v04 @0:15.27): f0–f3 an orange leak with a soft diagonal edge sweeps in and the frame warms; f4–f9 it blooms to near-white yellow (`#FFFDE0`/`#FCF88B`), the outgoing shot fading under it; **the cut lands under the peak at f9**; f10–f15 the incoming shot shows through while orange → red (`#E6902A` → `#C04129`) leak bands sweep diagonally across and recede, with **one** bright flicker frame near f14; clean at f16. Max 2 bright peaks | Section changes, re-hooks, swaps between evidence items, into/out of full-bleed clips: **3–6 per 60 s** (v01 3.4, v02 5.4, v03 4.0, v04 6.0), ≥ 2.5 s apart (v04 min 2.6 s, median ≈ 7 s) | built-in `leak` transition: `{"t": <cut>, "type": "leak", "frames": 16, "pre": 9, "colours": ["#E6902A", "#FCF88B", "#FFFDE0", "#C04129"], "angle": 35, "peak": 0.9}` in `timeline.transitions` (the cut lands on `t`; `layers` stays `picture`, captions are off in this style). No scene.|

**B-11 End devices**
| ID | Name | Type | What | Motion recipe | When | Engine block |
|---|---|---|---|---|---|---|
| **P-CROSS-PROMO** | Long-video card | overlay | The creator's own thumbnail (SH-6) on a dark rounded card with its title line and view line in the graphic band | Blur-in 10 f; push 1.00 → 1.04 | `cross_promo` CTA, the last 2–4 s (v04 @2:04) | `fx.shot({asset, chrome: false})` + title text; fallback FB-6 in the `fx.logoPlate` look |
| **P-CTA-PLATE** | CTA plate | overlay | TX-12 plate at cy 1380 | Date-plate wipe 8 f; the keyword in `accent` | `comment_keyword` / `link_bio` | a bespoke z6 scene, `kind: "cta-keyword"` |
| **P-SPONSOR-PLATE** | Sponsor plate | overlay | Only when §25 is switched on (VAR): the sponsor's name set in type on a plate + "Paid partnership" (TC-legal) ≥ 2 s | Plate wipe 8 f | Paid integrations | bespoke; NC-12 |

**44 patterns.** A buyer's new patterns (≤ 10, Part D.6) must come from these families and keep their motion grammar.

### 8.4 Line → pattern lookup `[NICHE]`
Classify every sentence with a line type, then use the primary pattern; use an alternate when the primary was used in the previous beat.

| Line type | Example (money & prices) | Example (health & science) | Primary | Alternates |
|---|---|---|---|---|
| LT-1 Claim (the presenter's assertion) | "This is the biggest tax trap" | "This supplement does nothing" | presenter L-full + P-PUSH-EMPHASIS | P-PUNCH-IN |
| LT-2 Source named ("according to…", outlet, report) | "The Economic Times reported…" | "A study in The Lancet found…" | P-SPLIT-SLIDE + P-CITE-SHOT | P-CITE-CARD (created), P-CITE-STRIP |
| LT-3 Long reading of a source (> 4 s) | reading a circular aloud | reading a study's conclusion | P-PIP-RING + full-bleed P-CITE-SHOT / P-CITE-CARD | P-DOC-EXCERPT |
| LT-4 Rule, law, policy text | "Section 194 says…" | "The food-safety rule says…" | P-DOC-EXCERPT | P-CITE-SHOT |
| LT-5 A post or statement read aloud | the viral WhatsApp forward | the influencer's caption | P-POST-CARD | P-QUOTE-OVERLAY on the person's clip |
| LT-6 Person named | "the finance minister said" | "Dr. X claims" | P-PERSON-PHOTO + P-NAME-PLATE | P-PERSON-SIL (created) |
| LT-7 Date | "on 1 April" | "in March 2020" | P-DATE-PLATE | P-YEAR-CHIP (on the data stage) |
| LT-8 Place, route, spread | "in Mumbai and Pune" | "it spread from Kerala to…" | P-ROUTE-MAP + P-PLACE-PIN | P-PLACE-PIN on a clip |
| LT-9 One number | "₹32.98 per litre" | "only 12% of it is real fruit" | P-NUMBER-CHIP | P-OUTLINE-BOX on the card |
| LT-10 Comparison (then vs now, A vs B) | "₹72 then, ₹111 now" | "14 times the safe limit" | P-DATA-STAGE | P-BAR-COMPARE |
| LT-11 Share or breakdown | "61% of the price is tax" | "half of all cases" | P-SHARE-PIE | P-BAR-COMPARE |
| LT-12 Trend with a moment | "prices fell in 2020, but…" | "cases peaked in May" | P-CHART-CIRCLE | P-MAP-CHART |
| LT-13 List of rows (cities, products) | "in Delhi ₹102, in Mumbai ₹111" | "these 5 brands" | P-PRICE-TABLE | P-BAR-COMPARE |
| LT-14 "Everyone is saying it" | "every channel ran it" | "thousands of posts claim" | P-THUMB-WALL | P-TV-SCREEN |
| LT-15 Footage proves it ("watch this") | the bank queue video | the hospital video | P-CLIP-PANEL | P-CLIP-FULL, P-CLIP-BAND |
| LT-16 An event no camera saw | "inside the meeting, they decided…" | "inside your body, the drug…" | P-RECON | P-KEYWORD-CHIP over the presenter |
| LT-17 Defined term | "GST", "repo rate" | "glycaemic index" | P-KEYWORD-CHIP | — |
| LT-18 Fake / false / scam / true | "this is fake" | "this is false" | P-STAMP | P-ALARM-TINT on the clip first |
| LT-19 Open question | "so where does the money go?" | "so does it work?" | P-QMARK | P-DATA-STAGE "???" |
| LT-20 Quote by a known person | "he said 'not a single rupee'" | "she said 'it's 100% safe'" | P-QUOTE-OVERLAY | P-POST-CARD |
| LT-21 Topic shift / new chapter | "now the real story" | "now the science" | P-FLASH-CUT | P-BACKDROP-SWAP (once) |
| LT-22 CTA | "comment SOURCES" | "link in bio" | P-CTA-PLATE | P-CROSS-PROMO |

### 8.5 Data and truth rules
- Every compared number is a figure (§18) and recomputes; one-off numbers come from the script or a cited source (NC-6).
- Comparisons share one scale and one layout (the 2014 and 2026 rows of P-DATA-STAGE are identical in position and size).
- Units are always shown ("(PER LITRE)", "per month", "%", "crore").
- Unknown values are "???" in the value's colour until revealed; never a placeholder number.
- Illustrative curves (no data) carry the `example` tag and no axis numbers.
- Reconstructions never show numbers or names that the script does not state.

### 8.6 Comedy layer
**§8.6 Comedy layer: OFF (`tone.comedy = off`).** If the buyer switches to `light` (BV-11, the template's maximum), one device only: a die-cut photo of a public figure the creator supplied, sliding up from the bottom edge beside the presenter for ≤ 2 s on a sarcastic line (v02 @2:56), at most once per reel. No meme sounds, ever.

### 8.7 Asset rules
- **Creator files first** (screenshots, clips, photos, own thumbnail), framed by the template; never altered to say something they don't; crops keep the masthead or date visible.
- **Created substitutes** use the inserts toolkit only (§12.5); every reconstruction is labelled; a created card never imitates a real outlet's design (no logo, no outlet colours, no outlet fonts).
- **No stock clichés** (N5). No fetched logos (N2). Personal identifiers blurred (N11).
- **People:** photos only from the creator; otherwise P-PERSON-SIL.
- **Maps:** the creator's map screenshot, or the created schematic with MAP NOT TO SCALE.

### 8.8 Density and variety
- An SC every ≤ 4 s; 2.5–4.5 weighted SCs per 10 s.
- ≥ 4 different patterns and ≥ 3 families per 60 s.
- The same evidence pattern at most 2 items in a row (the EB ritual repeats; its cards vary: screenshot, post, clip, data, map, person).
- Plates do not count toward variety; they are the text burden.

---

## §9 Transitions & shot grammar `[REQ] [DNA]`

### 9.1 Library
Measured at full frame rate (all four reels; `evidence.md` §5). Of the change points: ≈ 30% are T-06 burns, ≈ 35% land with a T-04 blur-in, the rest are hard cuts and stage moves.

| ID | Transition | Frames | Recipe | Cue role |
|---|---|---|---|---|
| **T-01** | Hard cut | 0 | A straight cut on a word boundary ±1 f; inside a panel (photo → photo of the same event, plates staying) and on the presenter's own jump cuts | none |
| **T-02** | Slide-down split | 28 | G-1 (`slide-down`, ease `slide`; real curve: 50% by 0.20 s, 95% by 0.92 s) | whoosh |
| **T-03** | Slide-up return | 12 | G-3 fallback only (no slide-up was measured; use T-11) | soft whoosh |
| **T-04** | Blur-in arrival | 9 (6–11) | The incoming shot, card or whole new layout arrives **heavily blurred (30 px), holds the blur ≈ 70% of the time, then snaps sharp in the last 2–3 f** (ease-in). No scale. Measured sharp at +0.16–0.24 s (v02, 14 cuts) and +0.30–0.37 s (v04, 4 cuts). Footage / whole-layout arrivals: built-in `timeline.blur` `{"t": <cut>, "kind": "defocus", "px": 30, "keys": [[0, 1], [6, 1], [9, 0]]}` (v02-fast: `[[0, 1], [4, 1], [6, 0]]`). A card inside the panel draws its own held blur (the scene presets ease the blur out, they do not hold it) | pop (cards), none (photos) |
| **T-05** | Blur-out exit | 5 | Outgoing card or chip: blur 0 → 12 px, opacity 1 → 0 | none |
| **T-06** | Light-leak burn | 16 | P-FLASH-CUT: built-in `leak` (16 f, `pre` 9: leak in, near-white peak with the cut at f9, orange → red bands sweep off); 3–6 per 60 s, ≥ 2.5 s apart | whoosh + light riser end (`transitions`) |
| **T-07** | PiP shrink / grow | 10 | `pip-shrink` / `pip-grow`, only when the same footage continues behind the ring | swish |
| **T-08** | Jump cut | 0 | A cut inside the presenter's take on a word boundary; if a Z-2 punch is active, Z-3 `jump-wide` (1 f) on the same frame restores 1.00 | none |
| **T-09** | Fade-through | 12 | G-8, only when the engine needs it between PiP and split | none |
| **T-10** | Hard end | 0 | The last frame ≤ 6 f after the last word, no black tail | none |
| **T-11** | Blur-through cut | 10 | The **whole frame** (presenter, panel, plates) blurs 0 → 30 px over 5 f, hard cut (`via: cut`) to the new layout, T-04 blur-in 5–6 f (measured v02 @0:03.64–0:04.00 split → full-bleed clip; v02 @0:27.36 and v03 @0:05.35–0:05.68 into L-pip-ring). Build: the built-in `blur-through` transition `{"t": <cut>, "type": "blur-through", "px": 30, "frames": 10, "pre": 5}` with the stage entry `via: cut` at the same `t` (`layers: picture` blurs world, footage and z1–6 cards and plates together) | soft whoosh |

### 9.2 Grammar
| Boundary | Use | Never |
|---|---|---|
| Frame 0 | H9-A: Z-0 + P-FOCUS-PULL; H9-B/C: sharp, static | a fade from black, a title card |
| Claim → source | T-02 on the source word | a hard cut to a full-bleed card while the presenter is mid-sentence |
| Card → card (same EB) | T-01 inside the panel, T-04 for the second card, or T-06 when the item changes kind | a slide (the split is already open) |
| Evidence → presenter | T-11 (or T-06 at an EB boundary) | a slide-up when a cut fits |
| EB → EB, re-hook, chapter | T-06 | two burns within 2.5 s |
| Presenter → long read / ring | T-11 (G-4) | T-02 for reads > 4 s |
| Presenter → full-bleed clip | T-11 or T-06 | T-07 when the clip runs < 3 s |
| Number lands | Z-2 punch on the word, then the chip / counter | a burn |
| Verdict | GR-alarm 3 f → P-STAMP + Z-4; out with a white flare + cut into a T-04 arrival | a slide |
| Last word | T-10 | a black tail, an outro animation |

### 9.3 Shot grammar
**§9.3 Shot grammar: OFF** (spine `talking_head`, one presenter). Camera rules live in §10.2.

### 9.4 Budget (per 60 s)
- T-06: 3–6 (≥ 2.5 s apart). T-04 arrivals: 4–7. T-02: 1–4. T-11: 2–5. T-07: 0–1. T-01 / T-08: the rest (cuts total ≈ 18–20 / min).
- The same transition never 3× in a row, except T-01, T-04 and T-08.
- Cuts on word boundaries ±1 f; audio never offset.

---

## §10 Motion, camera, layers, finishing `[REQ] [DNA; motion tokens TUNE ±15%]`

### 10.1 Motion tokens
| Token | Value |
|---|---|
| Lead | 2 f before the trigger word |
| Entries | `cubic-bezier(0.22, 1, 0.36, 1)`; stage slides `slide` 28 f (a long settle is the look); blur-ins ease-**in** (hold, then snap) |
| Exits | `cubic-bezier(0.64, 0, 0.78, 0)`, 5–6 f; plates 12 f |
| Blur-in (T-04) | 9 f (6–11), 30 px held ≈ 70%, sharp in the last 2–3 f, no scale |
| Focus pull (f0) | 11 f, 30 px held f0–f7 → 0 by f11 (Z-0's built-in `blur` keys), with Z-0 pull-open 1.30 → 1.00 over 36 f, ease `expoOut` |
| Plate wipe | 24 f L → R ease-out (50% f6, 90% f15), lead bar 60 → 0 px; exit 12 f (drift 24 px, blur 8 px) |
| Chips | keyword: rise 120 px + fade 14 f ease-out; number: fade 6 f + glow bloom 6 f; name plate: rise from behind the seam 5 f |
| Highlight bars | one linear wipe per span over its spoken duration (≈ 0.3 s/word, 12–30 f); ≥ 0.5 s between spans; bars accumulate |
| Photo arrival | push 1.00 → 1.15 over 15 f ease-out, then drift; text cards static |
| Stamp | 5 f, scale 1.35 → 1.00, rotate −8°, then Z-4; tint 3 f before |
| Burn (T-06) | 16 f, cut at f9, ≤ 2 bright peaks |
| Route line | 18–30 f |
| Counter roll | 18 f, lands on the word ±5 f |
| Holds | plates and chips ≥ 1.0 s and ≥ 0.25 s/word; cards ≥ 1.0 s after the last bar; titles ≥ 10 f after building |

### 10.2 Footage camera (Z)
| ID | Preset | Recipe | Tone / use |
|---|---|---|---|
| **Z-0** | `pull-open` | 1.30 → 1.00 over 36 f, ease `expoOut` (≈ 90% by 0.4 s, the rest a slow tail to 1.2 s), with P-FOCUS-PULL as the preset's own `blur` (measured v02 1.33 → 1.00 by 0.52 s; v01 1.23 → 1.00 by 0.45 s, a slow tail to ≈ 1.2 s) | f0 of H9-A only; once per reel |
| **Z-1** | `push-drift` | 1.00 → 1.05, linear over 3–4 s, then hold (v02 @2:03–2:06.5: +5% in 3.5 s) | `claim`, `context`: a stint ≥ 3 s with no punch; the last sentence |
| **Z-2** | `punch-in` | 1.00 → 1.20 over 12 f, ease-out (90% by f10), toward the face; held to the next cut (measured 1.12–1.23×, settled in 0.3–0.6 s: v02 @0:13.28, @2:09.36; v04 @1:09.9, @1:12.6, @1:58.0) | `claim`, `warn`, `verdict`, `context`: a "but", a number, a name, the turn |
| **Z-3** | `jump-wide` | → 1.00 in 1 f | on the next T-08 jump cut after a Z-2 |
| **Z-4** | `shake` | ±8 px, 6 f, 1.02 bump | `verdict`, `warn`: on stamps only |

Rules (`zoom_policy: presets`): **the presenter's framing is locked by default** (v01 @1:29.2–1:33.3: < 3% scale change in 4 s); per 60 s 1–3 Z-2 punches and 0–2 Z-1 pushes, at most one move per stint; never the same preset twice in a row; never two moves within 0.4 s; the face stays inside the frame and the plate band stays clear (in L-full, Z-2 at 1.20 must keep the chin above y 1180, else use 1.12). No rotation on the presenter (measured ±0.5°, body sway only).

**Plates ride the punch (built-in, R-9).** A plate or chip on the presenter (P-DATE-PLATE, P-NAME-PLATE on L-full, P-KEYWORD-CHIP, P-NUMBER-CHIP) that is on screen while a Z-2 punch plays sets `follow_footage: true`: it scales and moves with the punch, as the creator's date plate does with the 1.19 punch (v02 @2:09.4). Only when the punched plate stays inside the safe band: its bottom after the punch, `face_cy + (plate_bottom − face_cy) × punch`, must stay ≤ 1500 and clear of the face; otherwise leave the plate in screen space (or use the 1.12 punch). Never on cards in a split's graphic band (the band does not move with the presenter) and never with `anchor`.

### 10.3 Canvas camera
**§10.3 Canvas camera: OFF (`modules.canvas_camera = false`).**

### 10.4 Layer order (back to front)
1. World (W-evidence, W-data, W-map; the W-backdrop values feed P-BACKDROP)
2. z3 scenes that sit **under** the presenter window (full-bleed cards and clips under a PiP or the pip-card)
3. Footage window: the presenter footage → **P-BACKDROP** (`behind`, z1, in footage space) → the matte cut-out
4. Stage lines: the split hairline (12 px rim)
5. z4 evidence cards in a split's graphic band
6. z5 plates, chips, pins, quote overlays
7. z6 stamps, year chips, the CTA plate
8. Core-drawn, not scenes: P-FOCUS-PULL (footage blur on the stage), T-06 `leak` and T-11 `blur-through` (`timeline.transitions`, over the picture)

### 10.5 Finishing
- Grain only on the backdrop (noise 0.06) and the stages (0.05–0.06); the presenter is untouched.
- Vignette only in the worlds (0.3–0.45).
- Glow only on number chips (24 px), data values (16–28 px), the PiP-card rim (28 px), the stamp fog and the question glyph.
- Soft shadow on cards (0 30 90 rgba(0,0,0,.55)) and the PiP (0.45).
- A soft matte shadow (20 px, 35%) behind the cut-out is part of the look (v01, v04), but the engine has no matte shadow (engine request R-3). Until it ships, render **no** matte shadow; do not fake one with a dark blob behind the head.

---

## §11 Sound contract (minimal) `[REQ] [VAR]`
| Line | Decision |
|---|---|
| **Cue moments** | `hook` (the f0 hit, the first slide, the first card, the first label), `transitions` (T-02, T-06 whoosh + light riser end, T-11 soft whoosh), `reveals` (cards landing, stamps, counters landing, a route arriving), `cta`. Plates and highlight bars are silent, except the hook's first label |
| **Meme cues** | off (comedy off) |
| **Music bed** | on `(unverified)`: a low, tense documentary bed entering after the hook (on the first T-03 or T-06); never in the last 2 s |
| **Ducking** | the bed sits ≥ 18 dB under the voice while he speaks; the creator's clips keep their own audio, ducked under the voice when he talks over them, at full level when he pauses for them |
| **Loudness** | −14 LUFS integrated, true peak ≤ −1.5 dBTP; hard end ≤ 6 f after the last word (NC-8) |

---

## §12 Footage requirements, shot list, fallbacks, inserts `[REQ]`

### 12.1 Setups `[DNA what the style assumes; VAR the buyer's actual setups]`
| Setup | Spec |
|---|---|
| **A (default)** | Front-on, eye-level camera, mid-close (head top y 140–260 on the 9:16 frame, chest and hands in frame); a **plain flat background ≥ 1 m behind** (grey, white or green), no shelves, no lamps in frame; soft key from 30–45° + fill, no hard shadow on the wall; **a solid dark tee (navy or black)**, never green on green and never the backdrop's hue (no red tee for TH-crimson); lapel or shotgun mic out of frame; 4K 30/60 fps preferred (allows 1.35× re-crops), 1080p minimum (1.25×). The OK-pinch and open-palm gestures read well; keep hands below the chin |
| **B (TH-room)** | The creator's own tidy room: one curtain or plain wall, warm practicals off-frame, same framing. No matte needed; the backdrop plate is not drawn |

### 12.2 Shot list `[DNA]`
| ID | Shot | Spec | Count per 60 s | Must / optional | Fallback |
|---|---|---|---|---|---|
| **SH-1** | The A-roll take | Setup A (or B), one continuous take or several, the whole script | the whole reel | **must** | FB-1 |
| **SH-2** | Screenshots of the cited articles, reports, posts, documents | Full page or the top of the article: masthead, date and headline visible; PNG/JPG ≥ 1080 px wide; one per cited source | 2–5 | optional | FB-2 |
| **SH-3** | Clips the creator owns or holds | News segments, phone video, speeches; MP4/MOV; the exact seconds needed + 1 s handles | 1–4 | optional | FB-3 |
| **SH-4** | Photos of the named people | Head-and-shoulders, ≥ 800 px tall | 0–3 | optional | FB-4 |
| **SH-5** | A map screenshot or satellite still | The region with the places named; ≥ 1600 px on the long side | 0–1 | optional | FB-5 |
| **SH-6** | The thumbnail of the creator's own long video | 1280×720 | 0–1 (only with `cross_promo`) | optional | FB-6 |

### 12.3 Fallbacks
| ID | For | What the engine does instead | Fidelity cost | Result |
|---|---|---|---|---|
| **FB-1** | SH-1 without a clean background (no matte) | Switch the reel to **TH-room**: the real room stays, no P-BACKDROP; the rim colour still carries the theme | The topic colour behind the head is lost | degraded |
| **FB-2** | SH-2 | **P-CITE-CARD**: a created headline card (masthead set in type, the date, the exact headline from the script, red bars) | No real screenshot texture | holds |
| **FB-3** | SH-3 | A created substitute: P-POST-CARD of the quoted line, or `fx.appUI({kind: "video"})` (a generic video frame with the spoken caption); or move the beat to P-RECON | No live third-party footage; more weight on cards and the presenter | degraded |
| **FB-4** | SH-4 | **P-PERSON-SIL**: silhouette + name + role | No face | holds |
| **FB-5** | SH-5 | A schematic route map on W-map (simplified outlines, place pins, route line), MAP NOT TO SCALE | No satellite texture | holds |
| **FB-6** | SH-6 | A dark title card with the long video's title set in type (`fx.logoPlate` look) | No thumbnail image | holds |

Say at the checkpoint which fallbacks the reel uses ("FB-2 ×3, FB-4 ×1").

### 12.4 Props, reaction bank, matte, resolution
- **Props:** none. The hands are the props (counting, pinching, pointing at the panel above).
- **Reaction bank:** none.
- **Matte:** required (`veos matte`), except TH-room. QA the hair edge at 200%; a fringe of the old background > 2 px wide means TH-room.
- **Resolution:** a 1080p source allows the Z-2 punch ≤ 1.25× (1.20 default); 4K allows ≤ 1.35×. Creator screenshots below 1080 px wide are shown at most 940 px wide.

### 12.5 Third-party inserts: ask, then create `[REQ always]`
This style is built on third-party material, so this flow runs on every reel:
1. **Scan:** `veos inserts scan` lists the moments (headline, post, clip, person, chart, event). Refine it: one moment per cited source, per person shown, per clip, per map.
2. **Ask once**, as one short list: "For these N moments, do you have a screenshot, clip or photo? (drop the files, or say no): 1) the Economic Times article on the fee, 2) the viral post, 3) a photo of the minister, 4) a map of the route."
3. **Supplied:** `veos asset add <file> --origin creator`; frame it with P-CITE-SHOT / P-CLIP-PANEL / P-PERSON-PHOTO; keep the masthead or date visible; never alter what it says.
4. **Not supplied:** build the substitute from the script's words: P-CITE-CARD (headline card), P-POST-CARD (quote card), P-PERSON-SIL (silhouette), the schematic map, P-RECON, a logo plate for a product or company (name set in type).
5. **Record** each in `plan/inserts.json` (`{id, moment, origin: "creator" | "created", file?, recipe?, substitute_of?, quote_text?, source? {masthead, date, headline, highlight_spans}}`).

Rules: a created card quotes only what the script states; no headline is invented to make a point; if the script cites a source without its exact headline, ask for it at step 2 or show a P-KEYWORD-CHIP with the outlet name instead of a headline card.

### 12.6 Frame rate and audio
30 fps CFR output (60 fps masters conformed). One voice track: high-pass 80 Hz, de-ess, light compression, −14 LUFS. The creator's clips keep their own sound under the rules of §11.

---

## §13 Output contract `[REQ] [DNA]`

### 13.1 Core beat fields
`id`, `section` (HOOK | EB-n | VERDICT | END), `t0`/`t1`, `spoken`, `trigger {word, at}`, `tone`, `line_type` (LT-1…LT-22), `layout` (L-…), `visual` (one sentence), `layers` (scene ids), `pattern` (P-…), `sfx`.

### 13.2 Conditional fields used by this style
| Module / switch | Beat fields |
|---|---|
| captions off | `captions: {subtitles: "off"}` on the timeline (no per-beat caption fields) |
| citations | `source {masthead, date, url?, headline}`, `highlight_spans[]`, `credit` |
| data_figures | `figure_id` |
| themes (per_topic) | `theme` in the reel header only |
| footage ≥ medium | `shot_id`, `fallback_used` |
| third-party moment | `insert {id, origin: creator | created}` |

Example beat:
```yaml
- id: 7
  section: EB-2
  t0: 31.40
  t1: 36.90
  spoken: "The Hindu ki headline thi: Govt hikes excise duty on petrol by ₹10 per litre, diesel by ₹13 per litre"
  trigger: {word: "Hindu", at: 31.52}
  tone: evidence
  line_type: LT-2
  layout: L-split-bottom
  pattern: P-CITE-CARD
  visual: "The panel rises from below: a dark headline card, 'The Hindu' set in type, red bars wipe over '₹10 per litre' as he says it"
  layers: [cite-hindu, plate-date-2020]
  source: {masthead: "The Hindu", date: "May 06 2020", headline: "Govt hikes excise duty on petrol by ₹10 per litre, diesel by ₹13 per litre"}
  highlight_spans: ["₹10 per litre"]
  credit: null
  insert: {id: I3, origin: created}
  shot_id: SH-2
  fallback_used: FB-2
  sfx: [{id: "ui-pop-02", on: "cite-hindu@0", why: "card lands"}]
```

### 13.3 Reel header
```yaml
format: F-A
theme: TH-gold                  # by the topic rule (§4.3)
hook_archetype: HA-09           # variant H9-C
structure: evidence
count: null                     # or the spoken count of cases
keyword: null                   # only with comment_keyword
figures: [crude_2014, petrol_2014, crude_2026, petrol_2026, tax_share]
cast: [presenter]
series: null
sponsor: null
captions: off
inserts: {creator: 2, created: 5}
```

### 13.4 Hook proposals (3)
Each: `name`, `archetype` (+ variant), `first label` (the plate/highlight/stamp text), `hook pair` (§6.4 row), `storyboard` (f0 | 0.67 | 1.33 | 1.83 | 3.0), `sound` (cue list), `stopper tests` {ST-3: pass, ST-5: n SCs, ST-6: evidence t / label t}.

### 13.5 Checkpoint (before building)
1. The 3 hook proposals with stopper-test results; the 3 post titles.
2. The **plate list** (P5b): every spoken date/name/place/number → its plate, chip, card highlight or figure, with times.
3. The **citation list** (P8a): per claim → masthead, date, exact headline, highlight spans, origin (creator / created); **unsupported claims flagged**.
4. The figure plan (§18) with recomputed values; mismatches flagged.
5. The inserts record (creator vs created) and the fallbacks used.
6. The beat sheet with tones and layouts, the transition map, the SFX ledger.
7. The theme pack chosen and why (topic rule).
8. Style stills: f0 (blur-in), the first split with its label, one citation card mid-highlight, one PiP read, the data stage (if any), the verdict stamp, the last frame.

**Wait for approval.**

---

## §14 Worked examples `[REQ] [NICHE]`
Times are estimates; replace them with the `words.json` onsets. Each example uses only patterns from §8.

### 14.1 Money & prices: "Petrol prices SCAM in 2026!" (TH-gold, H9-C, ~125 s)
**Header:** F-A · TH-gold (money) · HA-09 / H9-C · figures: crude and petrol prices 2014 and 2026, the tax share · inserts: 1 creator photo (pump), 4 created cards · CTA `cross_promo`.

**Hook (0–3 s)**
| t (s) | Spoken (gist) | Visual | Layout / camera | Label |
|---|---|---|---|---|
| f0 | "Petrol ke daam…" | Presenter sharp on the gold plate, camera locked (H9-C) | L-full | — |
| 0.67 | "…ek bahut bada scam hai" | G-2 rise split: B&W photo of a fuel nozzle (creator photo, GR-bw) rises from below | L-split-bottom | — |
| 1.5 | — | GR-alarm red tint creeps over the photo | L-split-bottom | — |
| 1.83 | "scam" | **P-STAMP "SCAM"** + Z-4, red fog (`payoff: true`) | L-split-bottom | SCAM |
| 2.7 | — | White flare, hard cut to the data stage | → L-pip-card | — |

**Section plan**
| Section | Spoken (gist) | Patterns | Layout |
|---|---|---|---|
| EB-1 Then vs now (3–15 s) | "2014 mein crude $105 tha, petrol ₹72… 2026 mein crude $96, aur petrol?" | P-DATA-STAGE: year chip 2014, barrel $87 → $105, nozzle ₹72 (`good`); swap to 2026, $96 (yellow down-arrow), "???"; P-QMARK on the presenter at the question | L-pip-card on W-data → L-full |
| EB-2 The real price (15–30 s) | "Aaj Delhi mein ₹102, Mumbai mein ₹111" | T-06 burn → P-PRICE-TABLE (6 cities, the two spoken rows highlighted yellow); P-NUMBER-CHIP "₹111 PER LITRE" | L-split-bottom → L-full |
| EB-3 Where the money goes (30–55 s) | "The Hindu ne likha: Govt hikes excise duty on petrol by ₹10 per litre…" | P-CITE-CARD (created, "The Hindu" set in type, the headline verbatim from the script), red bars on "₹10 per litre"; P-OUTLINE-BOX on the date "May 06 2020"; P-PERSON-SIL for the minister quoted | L-split-bottom |
| EB-4 The tax share (55–75 s) | "Har ₹100 mein se ₹61 tax hai" | T-06 → P-SHARE-PIE 61% (formula `ratio`), P-YEAR-CHIP 2020 on the seam; P-CHART-CIRCLE on the 2020 crude dip | L-pip-card → L-split-bottom |
| EB-5 Counter-claim (75–100 s) | "Sarkar kehti hai ki ye paisa…" | P-QUOTE-OVERLAY of the quoted line (verbatim) over a created silhouette card; P-DOC-EXCERPT of the budget note; P-DATE-PLATE "1 FEB 2026" | L-split-top → L-full |
| Verdict (100–115 s) | "Toh haan, ye scam hai" | P-STAMP "SCAM" on the backdrop stamp box + Z-4 | L-full |
| End (115–125 s) | "Poori kahani meri lambi video mein" | P-CROSS-PROMO (FB-6 title card if no thumbnail) | L-split-bottom |

**Figures:** `crude_2014` 105 ($, script), `petrol_2014` 72 (₹, script), `crude_2026` 96, `petrol_2026` 111 (₹), `tax_share` = ratio(61, 100) → 61% (script); `petrol_2014` and `petrol_2026` share `scale_id: S-petrol`.

### 14.2 Health & science: "Does hot water cure dengue? (Viral forward)" (TH-slate, HA-18, ~110 s)
**Header:** F-A · TH-slate (health) · HA-18 · figures: cases 2024 vs 2025 · inserts: the viral forward (created post card, the creator has no screenshot), 2 created headline cards, 1 creator clip of a hospital ward · CTA `comment_keyword` "SOURCES".

**Hook (0–6 s)**
| t (s) | Spoken (gist) | Visual | Layout / camera | Label |
|---|---|---|---|---|
| f0 | (reads the forward) "Garam paani peeyo, dengue theek ho jayega" | **P-POST-CARD** (created, verbatim forward text, generic sender "Family group"), word-by-word reveal; presenter absent | L-hidden on W-evidence | — |
| 1.2 | "…theek ho jayega" | Yellow marker on "cures dengue" (`payoff: true`) | L-hidden | marker |
| 2.0 | "Ye message 2 crore logon tak pahuncha" | G-4 blur-through cut: the presenter appears in the ring over the card (bottom-left-centre) | L-pip-ring | — |
| 2.6 | "2 crore" | P-NUMBER-CHIP "2 CRORE SHARES" in the card's top area | L-pip-ring | — |
| 4.5 | "Sach kya hai?" | G-5 pip-grow to the presenter; Z-2 on "sach" | L-full | — |

**Section plan**
| Section | Spoken (gist) | Patterns | Layout |
|---|---|---|---|
| EB-1 What dengue is (6–25 s) | "Dengue ek virus hai, Aedes machhar se failta hai" | P-KEYWORD-CHIP "AEDES"; P-RECON (created mosquito-to-blood diagram) | L-full → L-split-top |
| EB-2 What the ministry says (25–45 s) | "Health ministry ki advisory saaf kehti hai…" | P-CITE-CARD (created, the advisory headline verbatim from the script), red bars on "no specific treatment"; P-DATE-PLATE "12 AUG 2025" | L-split-top |
| EB-3 The numbers (45–65 s) | "2024 mein 2.3 lakh case, 2025 mein 2.9 lakh" | T-06 → P-BAR-COMPARE on one scale (`S-cases`), leader chip "+26%" (`percent_change`) | L-pip-card on W-data |
| EB-4 What does help (65–90 s) | "Fluids, rest, platelet watch, doctor" | P-CLIP-PANEL (the creator's own hospital-ward clip, credit line); P-KEYWORD-CHIP "PLATELETS" | L-split-top |
| Verdict (90–100 s) | "Garam paani cure nahi hai" | P-STAMP "FALSE" + Z-4 over the post card recalled in the panel | L-split-top → L-full |
| CTA (100–110 s) | "Comment SOURCES, saare links bhej dunga" | P-CTA-PLATE "COMMENT SOURCES" (kind `cta-keyword`) ≥ 1.5 s | L-full |

**Figures:** `cases_2024` 230000, `cases_2025` 290000 (script), `growth` = percent_change → 26.1% shown as "+26%" (`round_to` 1); both bars `scale_id: S-cases`; number format ₹-free, Indian grouping "2.3 lakh" (`style: long`).

### 14.3 Travel & incidents: "Why the Mumbai flight landed in Jaipur" (TH-room, H9-B, ~140 s)
**Header:** F-A · TH-room (incident, shot in a real room; no matte) · HA-09 / H9-B · inserts: the airline's statement (creator screenshot), a passenger video (creator clip), 1 created schematic map, 2 created reconstructions · CTA none.

**Hook (0–3 s)**
| t (s) | Spoken (gist) | Visual | Layout / camera | Label |
|---|---|---|---|---|
| f0 | "14 August ko…" | Presenter sharp in the room, camera locked | L-full | — |
| 0.17 | "14 August" | **P-DATE-PLATE "14 AUG 2026"** at cy 1380 | L-full | date |
| 1.1 | — | Plate exits (drift + blur) | L-full | — |
| 1.33 | "Mumbai se Delhi ki flight…" | G-1 slide-down: created schematic map on W-map (MAP NOT TO SCALE) | L-split-top | — |
| 1.5 | "Mumbai" | Route draws from Mumbai; **P-PLACE-PIN "Mumbai"** (`payoff: true`) | L-split-top | pin |
| 2.2–3.0 | "…achanak Jaipur mud gayi" | The map pans north; the route bends to "Jaipur" (second pin) | L-split-top | pin |

**Section plan**
| Section | Spoken (gist) | Patterns | Layout |
|---|---|---|---|
| EB-1 The flight (3–20 s) | "Flight number AI 865, 180 passengers" | P-KEYWORD-CHIP "AI 865"; P-NUMBER-CHIP "180 PASSENGERS" | L-full |
| EB-2 What the crew saw (20–45 s) | "Cockpit mein ek warning light jali" | P-RECON (created cockpit panel, a warning light switching on) with the presenter in the ring top-right | L-pip-ring (tr) |
| EB-3 The statement (45–70 s) | "Airline ne kaha…" | P-CITE-SHOT (the creator's screenshot of the statement, credit line), red boxes on "precautionary landing" | L-split-top |
| EB-4 The passengers (70–95 s) | "Passengers ne video banaya" | T-06 → P-CLIP-FULL (the creator's passenger clip, 5 s) → G-4 ring from 1.0 s | L-hidden → L-pip-ring |
| EB-5 The altitude (95–120 s) | "35,000 feet se 18,000 tak 6 minute mein" | P-MAP-CHART over the map (`unit_convert` not needed; values from the airline statement), callout steps 35,000 → 18,000 | L-split-top |
| Verdict (120–140 s) | "Ye hijack nahi tha, safety landing thi" | P-STAMP "CONFIRMED" (`good`) over the statement card; last line on the presenter, Z-1, hard end | L-split-top → L-full |

---

## §15 QA checklist `[REQ] [DNA]`
**1. Profile conformance**
- [ ] Format F-A; the theme matches the topic rule; the reel header is complete (V-PROFILE).
- [ ] Presenter 80–95%; longest absence ≤ 6 s (V-PRESENCE). Duration 100–170 s (or the buyer's TUNE).
- [ ] `captions.subtitles: "off"`; no subtitle, karaoke or kinetic caption anywhere (N1).

**2. Hook**
- [ ] f0: the presenter alone; H9-A: Z-0 pull-open under the focus pull; H9-B/C: sharp and static (V-F0, H1).
- [ ] Evidence by 1.5 s; first label (`payoff: true`) by 2.0 s; ≥ 4 SCs in 0–3 s (V-F0, ST-5, ST-6).

**3. Body and cadence**
- [ ] SC every ≤ 4 s; 2.5–4.5 per 10 s (V-CADENCE). The presenter's framing is locked except 1–3 Z-2 punches / 60 s (eased 12 f, held) and Z-1 pushes; no 1-frame re-crop rhythm.
- [ ] Every EB follows the ritual (§7.3); re-hooks every 20–30 s with a new card type; burns 3–6 / 60 s, 16 f, ≥ 2.5 s apart; arrivals blur-hold-snap; highlight bars wipe at speaking pace.
- [ ] Layouts only from §3.2, inside their shares (V-LAYOUT); split orientation consistent in the reel.

**4. Text burden (captions off)**
- [ ] The P5b plate list is fully covered: every spoken date, name, place and number is on screen within ±5 f (H-TB, review).
- [ ] Plates ≤ 6 words, ≥ 1.0 s, no emoji (V-TITLE); floors and contrast pass (V-TYPE); nothing on the face (V-FACE); nothing in the IG bands (V-SAFE).

**5. Modules**
- [ ] §18: every compared number is a figure, recomputes, lands on its word ±5 f, shares its scale (V-DATA); formatting ₹/lakh/crore correct (V-NUMFMT).
- [ ] §19: masthead + date + headline on every source beat; headlines verbatim; highlight spans in the text and spoken while highlighted (V-CITE).

**6. Truth and inserts**
- [ ] Every third-party moment is creator-supplied or created and recorded (V-INSERTS).
- [ ] Quotes verbatim and attributed (NC-13); private identifiers blurred (NC-14); unsupported claims were flagged and resolved at the checkpoint.

**7. Sound**
- [ ] Cues only on hook, transitions, reveals, CTA; no meme cues; bed after the hook, ≥ 18 dB under the voice (S1–S6, NC-8).

**8. End and export**
- [ ] The CTA (if any) holds ≥ 1.5 s; hard end ≤ 6 f after the last word; no black tail; 1080×1920, 30 fps CFR; −14 LUFS, ≤ −1.5 dBTP.

---

## Conditional modules

**§16 Frame template / chrome: OFF (`profile.modules.chrome = false`).** The frame changes per beat; nothing persists.

**§17 Running state & anchored graphics: OFF (`profile.modules.running_state = false`, `anchors = false`).** No running counter; map pins are drawn inside the map scene, not anchored.

### §18 Data contract `[COND: modules.data_figures] [DNA rules]`
- **What becomes a figure:** every number that is compared with another (then vs now, A vs B, share of a whole, ranked rows, a trend), and any number derived by arithmetic in the script ("that's 61%", "it went up 26%"). A lone number that is only stated becomes a P-NUMBER-CHIP (still traceable to the script).
- **`plan/figures.json`:** `inputs` with `from: script` (+ the `said` words), `source:<citation id>` (a cited article) or `creator` (asked for); formulas from this style's set: `sum`, `diff`, `ratio`, `percent_change`, `per_period`, `unit_convert`, `cagr`; `scale_id` shared by compared figures (`S-petrol`, `S-cases`).
- **Format:** `profile.numbers` (Indian grouping, ₹, lakh/crore, 2 decimals for prices). Dollar values from dollar sources keep `$` with international grouping (`format: {currency: "$", grouping: "international"}` on that figure).
- **Display rules:** values roll 18 f and land on the spoken number word (±5 f); the unknown is "???" until its step; units always visible; one scale per comparison.
- **Illustrative figures:** only for concept curves (no numbers), with the `example` tag.
- **Validator V-DATA** (recompute, provenance, landing, scale) and **V-NUMFMT** (format) run on every reel with a figure.

### §19 Evidence & citations `[COND: modules.citations] [DNA]` **(the core of this style)**
- **Credit line:** "• SOURCE: <OUTLET>", `display` 600 24 px caps, white at 85% with shadow, x 64, y 140, fade in 6 f after the card lands. Optional: use it when the creator wants a source shown; nothing requires it.
- **Source card, creator screenshot (P-CITE-SHOT):** framed full-width in the top panel (x 70, w 940, radius 30) or full-bleed under GR-dim with the PiP; highlight **boxes** (6 px `bad` border, wiping L → R in 7 f) or bars placed on the spoken line; Ken Burns 1.00 → 1.06. Body text inside a screenshot is `TC-decorative`; the highlighted phrase and the headline must be readable at ≥ 40 px equivalent after framing, else crop tighter (v03 @1:03 body at 22 px failed this; QA rule).
- **Source card, created (P-CITE-CARD):** `fx.headlineCard` on `theme: "dark"`: the masthead set in `serif` 700 50 px (broadsheets) or `display` 800 (TV, agencies), the date (`display` 600 40 px), the **exact headline** in `serif` 600 60–66 px, 3 decorative body lines. **Highlight recipe:** red bars (`bad`, darkened until white reads ≥ 4.6:1) wipe in word by word: first word at `hlAt` (= the spoken word time − `t_in` − 2 f), +4 f per word, 6 f wipe each, the next span 0.5 s later. Text on a bar turns white at 55% of its wipe.
- **Highlight variants:** red bars = the claim (default); white outline boxes (P-OUTLINE-BOX) = a number or date being checked; yellow marker (`accent`, ink text) = a post or statement read aloud (P-POST-CARD). One variant per card.
- **Figure numbering:** off.
- **Plates:** date, name and place plates per §5.2 / §5.4.
- **Verdict stamps:** `bad` (FAKE, SCAM, FALSE, MISLEADING, UNPROVEN) and `good` (TRUE, CONFIRMED); tones `verdict` and `warn` only; 1–3 per reel.
- **Rules:** headlines and quotes verbatim (case and edge punctuation aside), never paraphrased; one card per claim; the highlighted words are spoken while highlighted; an outlet's logo or design is never imitated; unsupported claims are flagged at the checkpoint.
- **Validator V-CITE:** every `source` beat has masthead + date + headline; highlight spans occur in the headline; created headlines are verbatim in the script/transcript/creator texts; the credit line where required; synthetic scenes carry the label.

**§20 Dialogue: OFF (`profile.modules.dialogue = false`).** One presenter.

**§21 Canvas camera: OFF (`profile.modules.canvas_camera = false`).** Maps pan inside their own scene.

**§22 Ink & annotation layer: OFF (`profile.modules.ink = false`).** The only hand-drawn mark is the red ellipse inside P-CHART-CIRCLE, drawn by that scene.

**§23 Continuity: OFF (`profile.modules.continuity = false`).** Cuts and slides, no morph chains.

**§24 Series furniture: OFF (`profile.modules.series = false`, VAR).** If the buyer turns it on (BV-13), the only device is a part tag "PART {n}" in the date-plate look, top-left (x 64, y 150), for the first 2.0 s after the hook, counted in the intro cap.

**§25 Sponsor, brand & end cards: OFF (`profile.modules.brand = false`; no `end_card` or `product_card` device).** The cross-promo card is specified in §6.7 / P-CROSS-PROMO. If the buyer turns `brand` on (VAR): P-SPONSOR-PLATE with "Paid partnership" ≥ 2 s (NC-12), never over evidence.

---

## Part C. Declared exceptions and the non-overridable core
- **Declared exceptions: none** (§2.2). The style needs no bend of G1–G4: no behind-head text (E1), no chaos bursts (E2), no quiet type (E3: plates ≥ 56 px, cards ≥ 40 px, legal tags are TC-legal), no ambient fields (E4), no edge bleed (E5), no hard swaps (E6: the year chip blurs between values).
- **NC rules that this style leans on hardest:**
  - **NC-6 Truth:** every number traceable; created cards quote the script only.
  - **NC-7 Creator-owned media:** nothing fetched; outlet names set in type; reconstructions labelled.
  - **NC-13 Quote integrity:** quotes and headlines verbatim, attributed, never re-ordered.
  - **NC-14 Redaction:** private identifiers inside screenshots blurred for their whole time on screen.
- A buyer may not add an exception without a DNA deviation; no exception may bend an NC rule.

---

## Part D. Personalisation

### D.1 Setup questions (one round, ≤ 4, each with "keep the template default")
| ID | Question | Lands on | Default |
|---|---|---|---|
| BV-01 | Your name and handle | `creator.name`, `creator.handle` (CTA plate, credit lines) | {{BV-01.name|the creator}} / {{BV-01.handle|@yourhandle}} |
| BV-02 | One or two brand colours | `roles.primary` (the rim: the base under the theme packs) and `roles.accent` (marker yellow) | `#EE0000` / `#F9E81F` |
| BV-05 | The language you speak, and the on-screen language | `profile.language`, always asked: **English** → English captions (default) · **Hinglish** → romanised Hinglish captions · **Hindi** → Devanagari captions; numbers follow (BV-06) | English ({{BV-05.speech|en}} → {{BV-05.captions|en}}) | hi}} → English plates |
| BV-08 | Your CTA (none, cross-promo, comment keyword, link in bio) and its value | `profile.cta.chosen`, `creator.cta` | none |

### D.2 Lock summary
- **DNA:** captions off, the backdrop + matte, the split/PiP grammar, the citation recipe, H-rules, the HA list, structure `evidence`, citations and data modules on, the bad/good meanings.
- **TUNE (ranges in `tokens.locks`):** fonts within class, plate and stamp sizes, seam y 900–1000, PiP Ø 400–480, cadence ±15%, max gap 3–4 s, re-hook 20–30 s, duration standard/long, energy calm/balanced, presenter share ±10 pts.
- **VAR:** brand colours, theme pack colours and the default pack, language, numbers, CTA device and value, series/brand modules, sound contract lines, comedy off/light.
- **NICHE:** §6.4 hook pairs, §8.4 examples, §14, App. A, the glossary.

### D.2b Topic → theme for a new niche
When the buyer's niche is not in §4.3, map it once and append it here: alarm/injustice → TH-crimson; conflict/media → TH-ember; money → TH-gold; calm/technical → TH-slate; incidents filmed at home → TH-room.

### D.3 NICHE slots per reel (D.6)
At P7 append the reel's claim → evidence row to §6.4; at P5/P8 append new line types to §8.4; after the first approved reel, replace §14's matching example; add approved post titles to App. A; add confirmed names and outlets to the glossary.

---

## Part E. Changes
| Version | Date | Change |
|---|---|---|
| v1 | 2026-10-06 | First template from the Dhruv Rathee short-form analysis (4 reels, all 40 sheets read). |
| v1.1 | 2026-10-07 | Completeness pass at full frame rate (`docs/audit/evidence-explainer/completeness.md`): T-06 is a 16 f light-leak burn at 3–6 / 60 s (was a 5 f flash at 1–3); f0 pulls back (Z-0) instead of pushing in; the presenter's camera is locked with eased Z-2 punches (was 1-frame re-crops every 3–6 s); new T-11 blur-through cut for layout changes and the ring; blur-ins hold then snap; highlight bars wipe at speaking pace; plate, chip and slide timings measured; absence cap 8 s. |
| v1.2 | 2026-10-07 | Engine built-ins (cc324ec): P-FOCUS-PULL is Z-0's own footage `blur` (no z11 scene); Z-0 runs 36 f `expoOut` (the measured slow tail); T-06 is the built-in `leak` transition and T-11 the built-in `blur-through` (bespoke z11 scenes deleted); T-04 footage arrivals use `timeline.blur`; plates ride a Z-2 punch with `follow_footage` inside the safe band. |

---

## Part F. ID index
| Prefix | IDs used |
|---|---|
| D | D1–D8 |
| H, H-TB | H1–H18, H-TB |
| N | N1–N12 |
| W | W-backdrop, W-evidence, W-data, W-map |
| L | L-full, L-split-top, L-split-bottom, L-pip-ring, L-pip-card, L-band, L-hidden |
| G | G-1–G-8 |
| TH | TH-crimson, TH-ember, TH-gold, TH-slate, TH-room |
| GR | GR-bw, GR-alarm, GR-dim |
| TX | TX-1–TX-12 |
| HA | HA-09 (H9-A, H9-B, H9-C), HA-07, HA-18 |
| ST | ST-3, ST-5, ST-6 |
| B | B-1–B-11 |
| P | 44 patterns (§8.3) |
| LT | LT-1–LT-22 |
| T | T-01–T-11 |
| Z | Z-0–Z-4 |
| SH, FB | SH-1–SH-6, FB-1–FB-6 |
| F | F-A |
| BV | BV-01, BV-02, BV-05, BV-08 (asked); BV-03, -06, -10, -11, -13, -15, -17 (defaulted) |
| Engine requests | R-1 focus-pull camera preset, R-2 bottom slide for `stack`, R-3 matte drop shadow, R-4 geo maps, R-5 text-burden check, R-6 V-NUMFMT exemption for verbatim quotes, R-8 expo-settle stage ease, R-9 front scenes following the footage, R-10 burn and blur-through transition presets (`evidence.md`) |

---

## App. A Headline & hook bank `[NICHE]`
Post titles (cover and caption field) with their hook. Slots in `[brackets]`.
| # | Title | Hook | Archetype |
|---|---|---|---|
| 1 | "[Product/price] SCAM in [year]!" | H9-C stamp "SCAM" on the object | HA-09 |
| 2 | "Don't [do X]! You can be [consequence]" | H9-A, the evidence panel on the consequence | HA-09 |
| 3 | "[Viral claim]? FAKE." | the forward as a post card, then the presenter in the ring | HA-18 |
| 4 | "What really happened on [date] in [place]" | H9-B date plate → route map | HA-09 |
| 5 | "[Year] vs [year]: why is [price] still so high?" | data stage, "???" | HA-07 |
| 6 | "[Outlet/channel] lied about [topic]" | H9-A TV frame + red bars | HA-09 |
| 7 | "Who is [person] and why is everyone talking about him?" | H9-A person photo + name plate | HA-09 |
| 8 | "Your [bank/app] is charging you this hidden fee" | H9-A screenshot card, box on the fee | HA-09 |
| 9 | "Does [remedy] really cure [illness]?" | HA-18 post card → stamp "FALSE" at the end | HA-18 |
| 10 | "[Number] [people/cases] in [time]: the real reason" | HA-07 bars on one scale | HA-07 |

## App. B Evidence map
The full map (every DNA rule → `vNN @ m:ss`) and the list of `(unverified)` values are in `evidence.md`. Key anchors: backdrop plates v01 (ember), v02 (crimson), v04 (gold), v03 (real room); split slide-down v01 @1.33, v02 @1.17–1.33, v03 @1.33; rise split v04 @0.67; ringed PiP v02 @0:27–1:11, v03 @0:06–0:12, @0:46, @1:30; red highlight bars v02 @0:29, @0:44, @0:54, @1:01–1:06, @2:16–2:20, v03 @0:25, @0:59, @1:03, @1:14, v04 @1:01; date plates v02 @2:03–2:10, v03 @0.17–1.33; name plates v02 @2.0, @0:32, v03 @1:01, @1:10; stamps v01 @0:46, v04 @1.83; light-leak burns (measured 3.4–6.0 / 60 s) v01 @0:13.1, @0:17, @0:55, @1:50, v02 @0:09, @1:25, @2:35, v03 @0:19, @0:26, @1:24, @2:35, v04 @0:15, @0:33, @0:54, @1:14, @1:23, @1:37, @1:51; data stage v04 @0:05–0:30; route map v03 @1.33–2.83, @2:08.
