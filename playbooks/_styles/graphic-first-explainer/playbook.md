# Graphic-First Explainer Style Playbook (template v2)

## The feel

This reel is a designed publication that talks. Frame 0 is already a number in motion: a day counter climbing beside a
draining hourglass, a bill ticking up row by row, a grid filling cell by cell, with the creator's face under it and a heavy
two-line headline sliding in from both sides at once. A stranger stops because something is already happening, and it can
be measured.

Then the pictures take over. Every idea is one full-screen figure, complete on the very frame its first word is spoken,
and nothing on it is decoration: a week is an hourglass dropping days, ninety-six machines are ninety-six cells, the record
is a red bar the blue ones have to beat. Inside the card something moves on every noun and every number: a ring draws, a
bar climbs, a counter lands on the exact syllable. When the idea changes, the card doesn't fade or fly away. It cuts. The
hard cut is the heartbeat of this reel, and because every new card is a new picture of a new idea, each cut feels like
turning a page in a beautifully set magazine.

The creator is a guest, and a welcome one. They come back for the opinions, the caveats, the turns ("But…", "Now, this
isn't…"), always landing a little too close and settling back, as if the camera stepped in to listen. The claim gets the
face; the explanation gets the figure; when they comment on a figure, it sits above them like the page they're pointing at.

Under it all the caption is quiet: a few words on a small solid pill, always at the same height, swapping with no
animation. The figure shouts; the caption only makes sure you never miss a word. One palette rules the whole reel (dark
editorial with coral numerals to explain, cream with hard black shadows to sell, pink and sage for the pain) and nothing
from outside it ever appears. It runs dense and steady, picture after picture on the word, and the last figure carries the
biggest idea.

**The test:** pause on any frame: it's a finished, designed figure of the exact thing just said, in this reel's one
palette, and nothing on it is decoration.

## What this playbook is

You're editing one talking-head take of a creator explaining something with numbers in it (a result, a study, a record, a
market move, how a thing works) or selling something (a course, a tool, a launch, an event), and you have the authority to
make it the clearest, most gripping reel in their niche. This playbook is the style, pulled from three 100xEngineers reels
(v01 a research explainer, v02 a cohort ad, v03 a tool ad), measured frame by frame at full frame rate, then sharpened.
Read it all, every time. Use it the way a great editor uses a reference: take what fits this reel, invent when a moment
needs more, and never ship a frame that breaks the feel above.

**Who it's for and what it needs.** Creators whose story can be drawn: numbers, mechanisms, comparisons, offers with parts.
Input: one vertical talking-head take (setup A, §12.1). Screen recordings, portraits, logos, a source clip and thumbnails
lift it; every one is optional, fetched from the web when the creator has none, and has a built fallback (§12). No cut-out is needed: the graphics own their own frames and
the presenter never shares a layer with them. Captions follow the creator's language (English, Hinglish or Hindi, set in
their copy); cards, FIG lines and labels are English. Machine values live in `tokens.json`; where this text gives a number
tokens also holds, they agree.

### Style directives (non-negotiable)
| # | Directive | Where it lives |
|---|---|---|
| D1 | **Every idea gets a literal figure.** The card shows the exact thing said: a week becomes an hourglass counting days, "96 machines" becomes 96 filled cells | §8.3, §8.4 |
| D2 | **The presenter is a guest in the layout.** Graphics own the frame; the face comes back for a claim, a turn, a caveat or the CTA, and before the viewer forgets who's talking | §3.6, §7.5 |
| D3 | **One theme per reel.** The pack is chosen with the format and never changes inside the reel | §4.3 |
| D4 | **Numbers move, and the claims are true.** Every number on screen rolls, ticks, grows, fills or draws; every number the creator states comes from their words, their data or a cited source; illustrations may use made-up but realistic numbers, no label | §8.5 |
| D5 | **Hard cuts between ideas, motion inside an idea.** A new idea is a hard cut (or the theme's own transition, §9.1); the same idea evolves in place; every cut to the presenter settles out (Z-1 / Z-2) | §9.2, §10.2 |
| D6 | **Captions never stop.** 1–4 words on a solid pill, the whole chunk at once, hard swap, the same position on every graphic frame | §5.3 |
| D7 | **The hook is a number already moving at frame 0** (HA-07) with the claim spoken over it | §6.2 |
| D8 | **Ads say the keyword twice.** F-B reels place the comment-keyword CTA mid-reel and again at the end | §6.7 |

### Quick index
| § | What |
|---|---|
| §1 | Procedure: the two formats, and how to approach a reel in this style |
| §2 | Hard rules: the craft and the style's never-list |
| §3 | Worlds W-, layouts L-graphic / L-stack / L-full / L-pip / L-cardtop, stage moves G-, safe zones, the person |
| §4 | Colour roles, the three theme packs TH-editorial / TH-brutal / TH-pinksage, the halftone treatment |
| §5 | Type and captions: the title slab and the section lockup, caption profile CS-1, other text |
| §6 | Hook system: stopper test, HA-07 default, HA-02 / HA-18 alternates, hook pairs, headline writing, CTA and end cards |
| §7 | Structure and rhythm: explainer and list, markers SM-FIG / SM-NUMERAL, the rituals, open loops, rhythm by feel |
| §8 | Visual system (B-roll and patterns): families B-1…B-8, patterns P-01…P-52, line → pattern lookup, data and sources, assets |
| §9 | Transition system T-01…T-10, grammar, shot grammar, how the moves breathe |
| §10 | Motion tokens, the cut-in settle Z-1 / Z-2, layers, finishing |
| §11 | Sound |
| §12 | Footage handling: setups, shots and fallbacks, inserts |
| §13 | What your plan should settle |
| §14 | Worked examples (3) |
| §15 | Your look at the storyboard: the checklist |
| §16 | Build notes |
| App. A / B | Evidence map / hook-title bank |

---

## §1 Procedure: how to approach a reel in this style

You watch, listen, plan, build and look at the storyboard yourself; the edit skill has the mechanics. This style's
craft is the **claim → figure pairing**: every idea is paired with one figure before anything is built, and every number in
it becomes a figure in `plan/figures.json`.

**Two formats, one style.** Both share the same closed design system: one theme per reel, a full-frame designed graphic
per idea replaced by a hard cut, chunked pill captions, numbers that move, the presenter as a guest. A reel never mixes
them.

| Field | F-A "Editorial figure explainer" (default) | F-B "Ad card" |
|---|---|---|
| When | Explaining a result, a study, a launch, a record, a market move, a "how it works" story | Offers, courses, launches, tools, events, "N ways / N use cases" pitches |
| Length and presence | Standard, 50–80 s; the face a guest for about a fifth to a third of the reel | Short, 35–55 s; the face a little more present (a quarter to two fifths) |
| Layouts | L-graphic, L-stack, L-full | L-graphic, L-stack, L-full, L-pip, L-cardtop |
| Default hook | HA-07 live number (editorial counter + title slab) | HA-07 live number (ticker card); HA-02 when the opening line has no number |
| Allowed hooks | HA-07, HA-18, HA-02 | HA-07, HA-02 |
| Structure | `explainer`: claim → mechanism figures → turn → verification → caveat → payoff | `list`: pain/claim → product → items (numeral cards) → proof → CTA ×2 |
| Markers | SM-FIG (`FIG. 01` … on every card) | SM-NUMERAL (full-screen numeral cards) |
| Headline | Title slab (plate), hook only | Slug pill + 2-line section header (lockup), per section |
| Captions | CS-1: Plus Jakarta Sans 600 54 px, sentence case, pill `#0B0A0A` (editorial), cy 1390 | CS-1 for F-B: Poppins 700 48 px, as spoken, pill `#DF2E2B` (brutal) / `#DF2C14` (pinksage), cy 1450 on graphics |
| Numerals | Instrument Serif (`numeric` slot) | Poppins 800 with ink stroke + hard shadow |
| Sources | The FIG line names the real source on every card that has one | No SRC lines (quotes keep their attribution) |
| CTA | At the end, if any | Mid-reel and at the end |

1. **Pick the format and the theme.** If the script explains *what happened or how something works* and isn't selling, it's
   F-A. If it sells, invites, announces or lists use cases, it's F-B. Then the pack (§4.3): the creator's default theme if
   their copy sets one; otherwise F-A → TH-editorial; F-B → TH-pinksage when the hook figure is a cost or a loss, else
   TH-brutal. It holds for the whole reel.
2. **Check the framing.** Eyes at 38–42% of frame height, head top at y 260–420. If the head top sits higher than y 260,
   leave L-cardtop out of this reel: its card would reach the hair (§3.6).
3. **Find the units.** F-A: one **figure** per sentence or clause that carries one idea (a number, a mechanism, a person, a
   turn); a 75 s explainer holds around fourteen to twenty. F-B: **sections**: HOOK, PRODUCT, ITEM-1…n (each opened by a
   numeral card), PROOF, CTA-MID, BENEFIT, CTA-END.
4. **Pair every idea with its figure** and mark its **trigger word** (the noun or number the figure lands on). The lookup
   (§8.4) is vocabulary, not a decision table: ask what this idea looks like, then reach for the pattern that shows it.
5. **Feel the tone of each line:** `claim` · `explain` · `proof` · `warn` · `win` · `cta`. The tone picks the role colour and
   whether the face shows (§10.3). Claims, turns and CTAs want the face; explanations want the figure.
6. **Write the hook** (§6): the archetype, the live number it opens on, 8–10 headline candidates (title slab or section
   header), the best by the stopper test, two alternates.
7. **Do the numbers** (§8.5): every figure's inputs with provenance, its formula, its steps on the spoken words, its
   `scale_id`; recompute and flag anything that disagrees with the script. F-A: the SRC line for every card with a real
   source, FIG numbers in order, the exact words of every quote.
8. **Plan the returns and the turns** (§7.5): where the face comes back, which settle it lands with, where the F-A turn
   beats fall, where the F-B mid CTA lands.
9. **Third-party moments:** fetch the real thing (the creator's files first, then the web, source noted); rebuild from
   its exact text only when nothing usable turns up (§12.4).
10. **Plan the sound** (§11) and the transition map (§9.4).

---

## §2 Hard rules: the craft and the style's never-list

**Craft, by eye** (judge it on the storyboard, in context, the way an editor does):
- **Keep the person clear.** The guest arrives for the claim, the turn and the opinion, so their face and hair read clear of
  the front layers whenever they're on. The framing that does it, with 40 px to spare: in L-stack the caption block's
  bottom edge sits 24 px above the seam (y 936) and the head stays inside its band below y 960; in L-cardtop the card ends
  ≥ 40 px above the top of the hair; in L-pip nothing runs under or over the bubble (the header stops 40 px before the
  ring); in L-full the caption, the word stack and the keyword card sit below the chin. The exact geometry is in §3.6.
  When a moment wants otherwise (a caption crossing the chin for a beat on a low-framed take), that's editing; what's never
  fine is a head chopped or a face buried by accident.
- **No text over text.** The card (one element: its labels, chips, FIG line and value boxes drawn inside it), the F-B header
  lockup when present, and the caption: that's the most the screen ever holds. Band graphics in L-stack end ≥ 40 px above
  the caption pill; the F-A title slab sits above the pill, never on it (§5.2).
- **On the word.** Every figure, number, name and object starts 2 f before its trigger word and is fully on within ±5 f;
  counters land on the spoken number within ±5 f. Cuts sit on word boundaries ±1 f, never inside a word or a name; the audio
  is never offset.
- **Say what was said.** Every number the creator states is a figure in `plan/figures.json` with provenance (their words,
  their own data, or a cited source), written with `ctx.fmtNum`. Quotes are word for word and attributed. Illustrations
  (concept curves, collisions, a mock app) may use made-up but realistic numbers and names, with no label.
- **Promise integrity.** A promised count ("two use cases") equals the numeral cards shown; the CTA keyword is on screen
  ≥ 1.5 s each time it's said; the deliverable title on the promo and title cards is the one spoken.
- **Spelling.** Brand, tool and people's names exact, in captions and on cards.
- **Readable.** Captions on a solid pill with ≥ 4.5:1 contrast, weight ≥ 600 (E3 lets this style's quiet captions sit below
  the usual 54 px floor, down to 42 px; F-A uses 54, F-B 48). Mono micro labels run 30–39 px only when the same word or
  number is spoken or shown larger (E3, `redundant`). Display text ≥ 40 px. Coloured text on a light world reaches ≥ 3:1 at
  ≥ 96 px or sits on a chip; below 96 px it's ink.
- **Numbers formatted for the audience** (`profile.numbers`): international `$2,000`, `$1.2M`; Indian `₹1,20,000`, `₹1.2 L`,
  `₹3 Cr` when the creator's audience counts in rupees.
- **Determinism.** Particles, tickets, scatter and grids use `ctx.rng(seed)` / `ctx.rngStable(seed)`; nothing reads the
  clock.
- **Audio.** −14 LUFS integrated, true peak ≤ −1.5 dBTP, the bed ≥ 18 dB under the voice, a hard end ≤ 6 f after the last
  word, no black tail.

**Never in this style:**
- A graphic parked over the presenter's head, or a header running under the PiP bubble (v02 clipped its header there,
  "LEARN AI B|"; this style doesn't).
- Two theme packs in one reel, or a world colour that isn't the active pack's.
- Crossfades, dissolves, glitch packs, light leaks, zoom-throughs between ideas. Ideas change by hard cut or the active
  theme's own transition (§9.1), never another theme's.
- Punch-ins, crash zooms, shakes or slow drifts on the presenter. The only camera move is the cut-in settle (Z-1 / Z-2),
  which starts on a hard cut and only ever zooms **out**.
- A static number on a card: numbers roll, tick, grow, fill or draw (D4).
- Fake social proof presented as real: comment threads, likes, testimonials, follower counts. The comment sheet (P-50) shows
  only the keyword being typed.
- Stock footage, film or TV clips, memes, AI-generated people, other creators' thumbnails. A brand named gets its real logo
  (the creator's file, else fetched from the web, source noted); its name set in type (P-46) only when none can be found.
- Readable real code or logs as the point of a card. Code-shaped lines are decorative texture; the meaning sits on a pill
  (P-11).
- Contrast failures: primary-orange text on the cream world (use the deepened `#DB5320` at ≥ 96 px, or a chip); white
  numerals on pink without the ink stroke; red text on the dark stage without a chip.
- More than three bright hues in one frame: primary + accent + one of bad / good / highlight.
- Coloured or emphasised words inside captions: the graphic does the emphasis.
- Decoration that isn't the world: stars, squiggles and dot matrices live only in the decor band of TH-brutal (P-51), never
  as elements over the card.
- A black tail longer than 0.2 s, or an end card longer than 3.5 s.

---

## §3 Worlds, layouts, stage moves, safe zones

### 3.1 Worlds (colours come from the active theme, §4.3)
| ID | Kind | Look (per theme) | Carries | Enter / exit |
|---|---|---|---|---|
| **W-main** | stage (editorial) / canvas (brutal, pinksage) | Editorial: `#141210`, film grain 0.06, vignette 0.30. Brutal: cream `#FBF3E4` with a 48 px grid (`#EADCC4`, 2 px, alpha 0.8). Pinksage: pink `#F4849C`, grain 0.05 | Every figure card, numeral card, window card | Hard cut |
| **W-alt** | canvas | Editorial: cream graph paper `#EDE6D6`, 72 px grid `#CFC5B0` (2 px, alpha 0.7). Brutal: blush `#F6D9D5`. Pinksage: sage `#A9B9B4` | The "different kind of figure" card: concept maps, slider matrices (editorial); a second card family to alternate (pinksage alternates pink ↔ sage on every hard cut inside a section) | Hard cut |
| **W-dark** | stage | `#161515`, grain 0.02 (all themes) | Screen recordings and recreated app UIs (P-45, P-10 in brutal and pinksage reels) | Hard cut |
| **W-promo** | card-world | Gradient `#120A0A → #C9341F → #F7C2B5` top to bottom (all themes) | The promo carousel (P-49) only | Hard cut, ≤ 2.5 s |

**How the worlds behave.** W-main is home: it carries most of the graphic time, and W-alt is a contrast beat, a different
kind of figure that makes the next return to W-main feel fresh. Pinksage is the exception: card k on pink, card k+1 on
sage, by hard cut (v03 0:03–0:20), so the alternation itself is the rhythm. The world switch is the hard cut itself; worlds
never fade.

### 3.2 Layouts
| ID | Engine | Presenter rect | Graphic rect | Caption | Evidence |
|---|---|---|---|---|---|
| **L-graphic** | `hidden` | none | full frame; content zone x 64–1016, y 300–1320 (FIG line at y 232) | fixed y, cy **1390** (F-A); F-B cy **1450** (the brutal theme pins the measured 1452); pinksage per card (§5.3) | v01 0:02–0:13, v02 0:18–0:40, v03 0:03–0:20 |
| **L-stack** | `stack`, seam_y **960**, top `graphic`, bottom `footage` (face 0.34 of the band, eyes at 0.40) | x 0–1080, y 960–1920 | x 0–1080, y 0–960; content band x 64–1016, **y 140–900**, its content inside y 140–730 (§3.6) | `seam_above`: the block's bottom edge **24 px above the seam** (y 936) | v01 0:00–0:01, 0:14–0:17, 0:45–0:50, 1:03, 1:12–1:14; v03 0:00–0:02, 0:32–0:34 |
| **L-full** | `full` | full frame | none (z8 type only: P-38, P-48) | fixed y, cy **1290** (chest), moves below the chin if the face sits low | v01 0:09–0:10, 0:26, 1:06; v02 0:09–0:15, 0:41; v03 0:02, 0:21–0:23, 0:38–0:39 |
| **L-pip** | `pip`, circle **d 420** at (816, 330), ring **10 px `primary`**, face 0.55, eye 0.45 | circle x 606–1026, y 120–540 | full frame; header x 64–566 (stops 40 px left of the ring) | fixed y, cy **1440** | v02 0:00–0:08 (orange-ringed bubble top-right) |
| **L-cardtop** | `low`, offset **380** | footage lowered 380 px | card rect x 64–1016, y 130–690, ending ≥ 40 px above the top of the hair | fixed y, cy **1430** | v02 0:09–0:11 (stopwatch card above the presenter) |

**When each layout comes.**
- F-A: L-graphic is home. L-stack for the hook and for a figure the presenter comments on (an opinion, a caveat, "it used
  methods that…"). L-full for a turn or a caveat ("Now, this isn't…", "Then…"), on the turn word.
- F-B: L-stack or L-pip open the reel; L-full for claims, pains and both CTAs; L-cardtop for the one proof card about the
  presenter's own experience ("it took me only…"); L-graphic for everything else.
- A face run is a claim, not a monologue: when an L-full run goes past about four seconds, cut to a figure on the next noun
  and come back if the opinion continues.
- Every layout change is a hard cut on a word boundary (`via: "cut"`), never a morph (D5).

### 3.3 Stage moves
| ID | Move | Recipe | Use |
|---|---|---|---|
| **G-1** | Hard cut to graphic | Stage → `hidden` (L-graphic) with `via: "cut"` on the first content word (lead 2 f); the new card's object starts its entrance on the same frame | Presenter → figure (the default move) |
| **G-2** | Hard cut to stack | Stage → L-stack, `via: "cut"` + **Z-2** settle on the footage; the top band shows the current or next figure re-laid for the band (y 140–900) and settles with it (band scene scale 1.40 → 1 over 22 f, expo-out, about the band centre y 520, `in: "none"`). This stays scene-side on purpose: `target: "all"` / `follow_footage` scale graphics about the face pivot in the bottom band, which would slide the top band ≈ 360 px instead of settling it in place. Keep the band's content inside y 140–730 so even at 1.40 it never reaches the caption pill | Presenter returns under a figure |
| **G-3** | Cut to full + settle | Stage → L-full, `via: "cut"` + **Z-1** settle (1.26 → 1.0, roll 4° → 0) on the same frame | Claims, turns, CTA |
| **G-4** | Bubble open | Stage → L-pip, `via: "cut"` (not `pip-shrink`): the bubble is there on the cut, ring included | F-B intros with a section header |
| **G-5** | Card over head | Stage → L-cardtop, `via: "cut"`; the card enters with the skew-in (P-20 recipe) on the same frame | F-B personal proof ("it took me…") |

No morphs (`stage_morphs: {cut: 0}`). The engine's default moves (`slide-down`, `pip-shrink`…) are never used: always write
`"via": "cut"`.

### 3.4 Layout diagrams
**L-graphic (F-A figure card)**
```
┌─────────────────────────┐ 0
│   (IG top UI, clear)    │ ← y 0–110
│ FIG. 04 ONE WEEK  SRC:… │ ← FIG line, mono 26, y 232
│                         │
│   ┌───────────────┐     │ ← figure zone x 64–1016, y 300–1320
│ 4 │   hourglass   │     │   (counter numerals at x 64, y 760–900)
│DAYS   / bars /    │     │
│   │   rings /...  │     │
│   └───────────────┘     │ ← zone bottom 1320
│      ▌working on it▐    │ ← caption pill, cy 1390 (≈ y 1349–1431; F-B cy 1450)
│                         │ ← y 1500: end of meaning text
│   (IG bottom UI)        │ ← y 1540–1920: world only (decor band in brutal)
└─────────────────────────┘ 1920
```
**L-stack (hook and returns)**
```
┌─────────────────────────┐ 0
│  figure band            │ ← band y 140–900, content inside y 140–730; in the F-A hook the figure ends by y 620
│  CLAUDE SOLVED          │ ← F-A title slab, hook only: lines y 690–813, ≥ 40 px above the pill
│      ▌caption▐          │ ← caption pill ≈ y 854–936, bottom edge 24 px above the seam
│ ─────────────────────── │ ← seam y 960
│  presenter (footage)    │ ← head top ≈ y 1050, eyes at y ≈ 1345 (0.40 of the band)
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
│  ☆   ～～   ⠿⠿⠿          │ ← decor band y 1580–1860 (brutal only)
└─────────────────────────┘
```
**L-cardtop (F-B proof)**
```
┌─────────────────────────┐ 0
│ ┌─────────────────────┐ │ ← card x 64–1016 from y 130; bottom ≥ 40 px above the hair (≈ y 600 for a head top at 640)
│ │ IT TOOK ME [ONLY]   │ │
│ │ ⏱  20 MINUTES       │ │
│ └─────────────────────┘ │
│        presenter        │ ← footage lowered 380 px (head top y 640–800); blurred copy fills the top
│      ▌caption▐          │ ← cy 1430
└─────────────────────────┘
```

### 3.5 Safe zones and bands
- Meaning text: x 64–1016, y 110–1500. Nothing in the top 110 px, below y 1540, or at x > 970 between y 900 and 1540
  (Instagram's buttons).
- Caption band: L-graphic cy 1390 (F-A) / 1450 (F-B), pinksage per card; L-stack 24 px above the seam; L-full 1290; L-pip
  1440; L-cardtop 1430. Graphics stay ≥ 40 px clear of the caption pill (the L-graphic figure zone ends at 1320).
- FIG line: y 232 ± 8 (F-A only). Header band (F-B): y 150–440.
- Decor band (TH-brutal, no text): y 1580–1860.

### 3.6 The person
The guest and the graphics take turns; they don't fight over the frame. This style uses no cut-out and layers nothing
behind the person (it doesn't need to: the graphics own their own frames). Keep the head region (face, hair and the room
above the head top) clear of the front layers, captions included, with 40 px to spare (`layout.face_clearance` 40), unless
the moment wants otherwise; judge it by eye on the storyboard.

- **L-stack:** the presenter window is x 0, y 960, w 1080, h 960, no breakout, so the head never draws above y 960; face
  0.34 of the band, eyes at 0.40 (y ≈ 1345), head top ≈ y 1050. The caption block's bottom edge sits 24 px above the seam,
  y 936 (F-A pill ≈ y 854–936, F-B ≈ y 865–936): ≥ 24 px above the window and ≈ 110 px above the head top. Even on the
  first frame of the Z-2 settle (1.40×) the footage stays clipped inside its band. The band's content lives inside
  y 140–730: the band settles from 1.40 about its centre (y 520), and anything lower would ride through the pill on the
  first frames; once settled, its lowest text sits well over 40 px above the pill.
- **L-full:** setup A puts the head top at y 260–420 and the eyes at 38–42% of the frame (y ≈ 730–806). The caption sits at
  cy 1290 on the chest (F-A pill ≈ y 1249–1331) and `avoid_face` moves it below the chin when the face sits low. The P-38
  word stack (y 1050–1350) and the P-48 keyword card (y 1080–1420) sit below the chin with ≥ 40 px clear; on a low-framed
  take, drop them lower, never higher than the chin + 40.
- **L-pip:** the bubble is x 606–1026, y 120–540 (d 420, ring 10 px `primary`, face 0.55 of the circle, eye 0.45). The header
  stops at x 566, 40 px before the ring; the window card starts at y 640, 100 px below the bubble. Nothing crosses the ring.
- **L-cardtop:** the footage is lowered 380 px, so the head top lands at y 640–800. The card's rect allows x 64–1016,
  y 130–690, but its bottom stops 40 px above the top of the hair: by y 600 when the head top is at 640. The caption
  (cy 1430) rides the chest and drops below the chin if needed.
- **The face comes back** before the viewer starts to wonder who's talking: on the next opinion, caveat, turn or "you"
  sentence, as an L-stack under the current figure or an L-full on the turn word. The source reels ran gaps of 18–24 s
  (v01 0:27–0:45, v02 0:16–0:41); that works for a known brand, not for a creator the viewer is just meeting, so this style
  returns much sooner (tokens keep 10 s for an explainer and 8 s for an ad as the outer edge).
- Returns are hard cuts (G-2, G-3), never a fade. Crops: L-full as shot, entered with the Z-1 settle; L-stack face 0.34 of
  the band; L-pip face 0.55 of the circle; L-cardtop as shot, lowered 380 px.

---

## §4 Colour system

### 4.1 Role palette (defaults = TH-editorial)
| Role | Hex (editorial) | One job | Text on it | Contrast |
|---|---|---|---|---|
| `primary` | `#F08060` coral | Hero numerals, the FIG number, header line 2, the active bar, the PiP ring | ink | 7.2:1 |
| `accent` | `#4F8CFF` blue | The new / winning series, slug pills, chips, the CTA keyword | ink | 5.9:1 |
| `pill` | `#0B0A0A` (sampled v01 @0:20, @0:40) | Caption pill fill | paper | 17:1 |
| `card` | `#EDE6D6` | Card and window bodies | ink | 15:1 |
| `line` | `#2A2622` | Card outlines and hard shadows | — | — |
| `mute` | `#9A9384` | Mono micro labels, FIG title, SRC line, axis labels | (text colour) | 6.1:1 on W-main |
| `highlight` | `#C27BD9` | Highlighter bar behind a stat (P-40) | ink | 5.4:1 |
| `bad` | `#D4372D` | The old value, the cost, the problem, the record to beat (fixed meaning) | paper | 4.8:1 |
| `good` | `#2FBF71` | The fix, the pass, the saving (fixed meaning) | ink | 7.9:1 |
| `ink` | `#111111` | Dark text, outlines | — | — |
| `paper` | `#FFFFFF` | Caption text, light text on dark | — | — |
| `cream` | `#EDE6D6` | Editorial body text on the dark stage | — | 15:1 on `#141210` |

Gradients: `G-old` `#F06A5E → #8A2320` (old / bad bars, top to bottom), `G-new` `#E4ECFF → #3B74FF` (new / accent bars),
`G-fill` `#F08060 → #B07CE8 → #4F8CFF` (grid fills, rings, left to right), `G-promo` `#120A0A → #C9341F → #F7C2B5` (W-promo).

With the creator's brand colours, `primary` and `accent` take them in every pack; `pill`, `card`, `line`, `mute`,
`highlight`, `bad`, `good` and the worlds keep each pack's values.

### 4.2 Meanings
- **Old → new runs `bad` (warm red) → `accent`.** The record, the old way and the cost are red; the new result is the accent
  (v01 0:57–1:02: the red 2023 record bar against the blue new bars).
- `good` appears only on a pass, a fix or a saving (✓ PASS, the cheaper route).
- `primary` marks *the number this card is about*. One primary element per card.
- Brand colours appear only on brand elements (a real logo, a logo plate's monogram).

### 4.3 Theme packs (one per reel)
| Pack | `primary` | `accent` | `pill` | `card` | `line` | `mute` | `ink` | W-main | W-alt | Pick it when |
|---|---|---|---|---|---|---|---|---|---|---|
| **TH-editorial** | `#F08060` | `#4F8CFF` | `#0B0A0A` | `#EDE6D6` | `#2A2622` | `#9A9384` | `#111111` | `#141210` stage, grain | `#EDE6D6` graph paper | **F-A default.** Results, research, records, how-it-works, market moves |
| **TH-brutal** | `#F26B3A` | `#8CFF3C` | `#DF2E2B` | `#FFFFFF` | `#111111` | `#6E6559` | `#111111` | `#FBF3E4` + 48 px grid | `#F6D9D5` blush | **F-B default.** Offers, courses, launches, tools, events, workflows |
| **TH-pinksage** | `#F4849C` | `#A9B9B4` | `#DF2C14` | `#FFFFFF` | `#2B1F2A` | `#2B1F2A` | `#2B1F2A` | `#F4849C` pink, grain | `#A9B9B4` sage | F-B reels whose hook is a cost, a waste or a pain number (bills, hours lost, money leaking) |

`highlight` is `#C27BD9` in all three. The pack is written in the plan's reel header and never changes.

Per-pack text rules:
- **Editorial:** body text `cream` on W-main; `ink` on cards and on W-alt. Primary numerals on W-main.
- **Brutal:** text `ink`; header line 2 in primary **deepened to `#DB5320`** (3.6:1 on cream, display ≥ 96 px only; use
  `fx.textColour`). The source's orange "BUILDING." measured 2.7:1, so it's deepened here. Lime `accent` is a fill only
  (chips, pills, panels), never text on cream.
- **Pinksage:** text `#2B1F2A`; white numerals and ticker values always carry a 5–8 px ink stroke + a hard ink shadow (white
  on pink alone is 2.4:1).

### 4.4 Grades and clip treatments
Footage is never graded. One clip treatment exists: **halftone** on portrait photos (the creator's or fetched) in P-07 / P-24
(grayscale 1, contrast 1.25, a 6 px dot screen overlay at 35%), built as a CSS filter + an SVG dot pattern inside the scene.

### 4.5 Rules
- Three bright hues per frame at most (`max_bright_per_frame` 3): primary + accent + one of bad / good / highlight.
- Coloured text on a light world needs ≥ 3:1 at ≥ 96 px or a chip behind it; below 96 px use ink.
- No gradients on text. Gradients live only on bars, rings, grid fills and W-promo.

---

## §5 Type and captions

### 5.1 Font map
| Slot | Family (weight) | Font class | Used for |
|---|---|---|---|
| `display` | **Unbounded** 900, upright caps | extended heavy sans caps (Unbounded 900, Archivo Black) | F-A title slab (P-37) |
| `header` | **Barlow Semi Condensed** 700, caps | semi-condensed bold grotesque | F-B section headers |
| `chunky` | **Barlow Condensed** 700, caps | condensed bold grotesque (Barlow Condensed 700, Anton) | Window titles, slab labels |
| `body` | **Plus Jakarta Sans** 600–800 | neo-grotesque sans (Plus Jakarta Sans, Inter Tight) | F-A captions, figure labels |
| `ui` | **Poppins** 600–800 | geometric sans (Poppins, Jost) | F-B captions, card copy, word stacks, CTA keyword, list numerals |
| `numeric` | **Instrument Serif** 400 (F-A) / **Poppins** 800 (F-B) | display serif (F-A) / geometric heavy (F-B) | Hero numerals, counters, ticker values |
| `serif` | **Instrument Serif** 400 italic | high-contrast display serif | Quote notes, chart annotations ("off the chart ↑") |
| `mono` | **JetBrains Mono** 500–600 | monospace | FIG / SRC lines, `// slug` pills, micro labels, terminal logs, window filenames |

Closest matches, measured: v01's slab is an **upright** extended black (Druk-Wide-like), not italic (v01 @0:01.2), and
Unbounded 900 is the closest bundled face. v02's header is a semi-condensed grotesque; Barlow Semi Condensed 700 is the
closest. The F-A caption measured wider than Inter Tight (12% too narrow at v01 @0:08, @0:40); Plus Jakarta Sans 600 at
54 px matches.

### 5.2 The headline element
**F-A: the title slab (`plate`, lifetime `hook`)** (P-37). It names the *event*; the live number above it shows the *scale*.
| Property | Spec |
|---|---|
| Text | Unbounded 900 upright, caps, **80 px** (76–88; real cap 59 px, line 1 x 76–1010), line height 0.9, white `#FFFFFF`, 2 lines, ≤ 16 characters per line, ≤ 5 words, readable in 1.2 s |
| Box | No fill, no stroke; a soft shadow `0 4px 18px rgba(0,0,0,.55)` for legibility over footage or figures |
| Position | Centred on x 540, near full width, in the L-stack top band, **lines at y 690–749 / 764–813**, its bottom ≈ 41 px above the caption pill (≈ y 854–936). The source measured the slab at y 801–860 / 875–924 (v01 @0:00.6), where no caption ran under it; the caption now sits above the seam, so the slab rides 111 px higher and the hook's figure ends by y 620. The slab is its own z10 scene: it doesn't ride the band's Z-2 settle |
| f0 | Line 1 slides in from the **right** (x +540) and line 2 from the **left** (x −540) on the same frame, each with a 14 px horizontal blur, expo-out over **12 f**; settled by f12 (v01 0:00.04–0:00.48) |
| Life | Static once settled (the figure above it moves) |
| Exit | Leaves with the stack on the first hard cut (1.5–2.0 s); never animated out |

**F-B: the section lockup (`lockup`, lifetime `section`)** (P-21)
| Property | Spec |
|---|---|
| Slug pill | `// snake_case_label` (≤ 16 characters), JetBrains Mono 600 **32 px** lowercase ink on `accent`, radius 24, padding 8/20, 3 px `line` outline. x 64, y 150, height 52. `redundant` (E3) |
| Header | Barlow Semi Condensed 700 caps (`header` slot) **104 px** (96–112), line height 0.98. Line 1 `ink`, line 2 `primary` (deepened, §4.3) and ends with a period. ≤ 6 words, ≤ 12 characters per line. x 64, y 220–440; width ≤ 502 px with L-pip (it stops 40 px before the ring), ≤ 952 px without |
| f0 | The slug pops (scale 0.6 → 1, 4 f); line 1 **rises out of a clip line** (y +60 → 0 under a mask, 4 f, expo-out) from f3; line 2 rises the same way ≈ 10 f later (v02 0:00.12–0:00.52). No typing |
| Life | Changes per section: after the section transition (T-07 iris wipe) the slug pops and the new lines rise again |
| Exit | Hard cut when the section ends or the layout becomes L-full |

### 5.3 Caption profile CS-1
`extends: "lib:100x"` and tunes it. The caption is quiet on purpose: the figure is the loudest thing on screen, and the
pill only makes sure nobody misses a word, with the sound on or off.

| Group | Value |
|---|---|
| Mode | `full`, role `support`, `mute_safe` |
| Chunking | unit `group`, **1–4 words**, 1 line, ≤ **26 characters**, never split a name, number or unit; break on punctuation and on pauses ≥ 0.6 s |
| Timing | lead 2 f; **reveal `chunk`**: the whole 1–4-word group appears at once, pill included; **swap `hard` 0 f** (no fade, no pop, no rise: v01 0:01.90 "by" → "working on it", v02 0:00.36 "This" → "video", v03 0:03.70 "Here are" → "two real", all one-frame swaps); min hold 0.25 s per word; tail 0.12 s; no pause hold |
| Skin F-A | Plus Jakarta Sans **600**, **54 px**, sentence case as spoken, white `paper`, no stroke, no shadow; **pill** fill `pill` (`#0B0A0A` editorial, near-black on the `#191814` stage), opacity 1.0, radius 10, padding 10/18 (pill ≈ 82 px tall) |
| Skin F-B | Poppins **700**, **48 px**, case as spoken (mostly lowercase), white; pill `#DF2E2B` (brutal; sampled `#EA3B35` at v02 @0:00–0:03, nudged darker so white 48 px text reaches 4.5:1) / `#DF2C14` (pinksage; sampled `#F5452D` at v03 @0:10, the same nudge), opacity 1.0, radius 10, padding 8/16 (pill ≈ 71 px tall) |
| Position | L-graphic fixed cy **1390** (F-A, measured 1386) / **1450** (F-B; the brutal theme pins the measured 1452). **TH-pinksage per card:** each card scene declares `caption_cy` so the pill sits under that card's content (measured v03 1075 / 1277 / 1408 on different cards; **1290** when the card sets none), or a timeline `captions.overrides` `{t: [a, b], cy}`; it stays inside the safe y 110–1500. **L-stack `seam_above`**: the block's bottom edge 24 px above the seam (y 936). L-full cy **1290**; L-pip cy **1440**; L-cardtop cy **1430**. Centred, max width 952, `avoid_face` on |
| Emphasis | **none**: no colour, no size jump, no chip inside captions |
| Hide | Under z8 type scenes (P-38 word stack, P-48 keyword card) and during stage morphs (there are none) |
| Language | Latin script for English and Hinglish; keep English terms verbatim; don't normalise spelling; the glossary holds the creator's brand and tool names |

Measured basis: 1–3 words per chunk, median 2 (v01 "working on it", "for a whole", "set by"; v02 "is fully", "by Claude Opus
5.5."; v03 "you pay", "LLM call,"); pill y 1385–1455 on graphic frames, the chest on full frames (v02 0:12 "If you want"
≈ y 1215, v01 0:09 "the formula" ≈ y 1280).

### 5.4 Other text
| System | Recipe | Class | Hold |
|---|---|---|---|
| **FIG line** (F-A) | JetBrains Mono 500 **26 px** caps, tracking 0.12. Left: "FIG. 04" in `primary` + two spaces + the card title in `mute` ("ONE WEEK, NONSTOP"). Right-aligned at x 1016: "SRC: OUTLET · MON YYYY" in `mute` (24 px, the citation line), only when the card has a real source. y 232 | small print (`type.fig_line`) | The card's life |
| **Micro labels** | JetBrains Mono 500 **30–34 px** caps, tracking 0.12, `mute` ("DAYS", "LOOPS · THE RECORD", "CPUs RUNNING", axis ticks) | TC-label `redundant` (E3) | ≥ 10 f after built |
| **Figure labels** | Plus Jakarta Sans 600 **40–48 px** caps, tracking 0.06 (bar names, node names when not redundant) | TC-label | ≥ 0.25 s / word |
| **Hero numerals** F-A | Instrument Serif 400, **520–720 px**, `primary`; counters 140–200 px | TC-display | ≥ 0.6 s after landing |
| **List numerals** F-B | Poppins 800, **620–760 px**, white, 8 px ink stroke (`paint-order: stroke fill`), hard ink shadow +16/+18 | TC-display | 1.2–1.6 s |
| **Ticker values** F-B | Poppins 800 **150 px**, white, 5 px ink stroke, hard shadow +8/+10, in a fixed-width value box (`data-slot`, E6) | TC-display | The card's life |
| **Label box** F-B | Poppins 700 **88 px** ink in a white box, 5 px `line` outline, hard shadow +10/+12, typed **1 char / 2 f** with a caret blinking 8 f on / 8 f off (v03 0:06.7) | TC-display | ≥ 1.0 s after typed |
| **Chips** | JetBrains Mono 600 **40 px**, radius 30, padding 10/24, 3 px `line` outline, fill `accent` / white / `card`, rotated −3…+3° | TC-label | The card's life |
| **Quote** | Instrument Serif italic **58 px**, line height 1.12, ink on `card`; the key phrase underlined by a 6 px `primary` hand stroke | TC-label | ≥ 0.25 s / word |
| **Annotation** | Instrument Serif italic **64 px**, `bad` or `primary` ("off the chart ↑") | TC-label | ≥ 10 f |
| **Terminal lines** | JetBrains Mono 500 **38 px**; meaning lines in `cream` / ink, timestamps in `mute`; filler lines decorative | TC-label / TC-decorative | ≥ 0.6 s per line |
| **Word stack** | Poppins 700 lowercase **110 / 140 / 110 px**, white, shadow `0 3px 16px rgba(0,0,0,.45)` | TC-display | The clause |
| **CTA keyword** | "comment" Poppins 800 **130 px** white; the keyword Poppins 800 **200 px** in curly quotes, fill `accent` (brutal, editorial) or `primary` (pinksage); both with a hard ink drop shadow offset 6/6 px and no outline (v03 @0:22 "comment / “Jev”", keyword cap ≈ 190 px) | TC-display | ≥ 1.5 s |
| **Stat line** | Poppins 600 **110 px** ink, a `highlight` bar behind | TC-display | ≥ 0.25 s / word |
| **Window filename** | JetBrains Mono 500 24 px `mute` in the title bar ("who_we_are.exe") | TC-decorative (chrome) | — |

### 5.5 Language and numbers
- **English speech (default):** captions verbatim, sentence case (F-A) / as spoken (F-B). Brand names exact.
- **Hinglish speech → English captions:** translate per chunk, keep the timing of the spoken words.
- **Hinglish speech → Hinglish captions:** romanised as spoken, English terms verbatim.
- **Hindi speech → Devanagari captions,** on the same pill.
- Cards, FIG lines, headers and labels stay English in every case: the mono caps and tracked caps of this design system are
  Latin-only.
- Numbers through `ctx.fmtNum` only. International: `$2,000`, `$1.2M`, `96`, `193.6x`. Indian, when the creator's audience
  counts in rupees: `₹2,000`, `₹1,20,000`, `₹1.2 L`, `₹3 Cr`. Units as spoken ("20 MINUTES", "7 DAYS").

---

## §6 Hook system

The on-screen headline promises the viewer something: an outcome they want, a curiosity gap, or who it's for. In this
style that promise is an *event big enough to be surprising*, stated flat ("CLAUDE SOLVED / PHYSICS PROBLEM", "INDEX FUNDS /
BEAT 9 IN 10"), with a live number proving its scale before the viewer has time to doubt it. It doesn't have to repeat the
spoken words; it has to be true to what the reel delivers. A headline shown as someone's words (in quotes) is word for word.
Write 8–10 candidates from the formulas (§6.5) and the proven patterns ("How to X as a Y", "Why your X isn't working", "The X
nobody tells you", "Stop doing X", a number or a contrast), score them on outcome, curiosity, who it's for and brevity, run
the best through the stopper test and pick; the next two go to the storyboard as alternates.

### 6.1 The stopper test
| Test | In this style |
|---|---|
| Thumbnail | f0 at 25% shows a moving figure and a readable claim: the title slab (F-A, 80 px → 20 px at 25%) or the ticker values (F-B, 150 px → 38 px) |
| Mute | With the sound off, the first three seconds tell the claim: the number climbing + the caption words + the slab or header |
| Motion at f0 | The figure is already moving on f0 (a counter rolling, a ticker ticking, particles falling) |
| Payoff | The opening figure's first value lands by **1.0 s**; the reel's result number (money, time, count, %) by **6.0 s** |
| Read time | The headline reads in ≤ 1.2 s (≤ 5 words F-A, ≤ 6 words F-B) |

The first three seconds feel dense: the slab slides in, the counter steps, the caption chunks swap, the cut lands on the
full figure. Dense in time, never in space: each thing arrives while the last one settles.

### 6.2 HA-07 Live number (default)
The spoken claim plays over a number that is already moving at frame 0; the claim's own result number lands within 6 s.
Frame 0 is a figure scene (`kind: counter | number | figure | data_row | stat`) already moving (an entrance or events at
t 0), plus the claim: the first caption chunk or the headline.

**F-A version (editorial, L-stack → figure cards)**, from v01's structure with v03's frame-0 number.
| t | Layout / camera | Visual | Caption | Cue moment |
|---|---|---|---|---|
| **f0** | L-stack + **Z-2 settle** (both bands start at 1.40 and settle out over 22 f, 2 f of motion blur: v01 0:00) | Top band (y 140–620): the claim's figure already moving: a counter rolling from its start value (P-02 day counter, P-12 grid count, P-35 count) or a ticker (P-27). Title slab lines sliding in from opposite sides at y 690–813 | Chunk 1 on the pill above the seam | hook hit |
| 0.0–0.4 | — | Slab settles by f12; the counter keeps rolling | Chunks swap | — |
| ≤ 1.0 | — | **First value lands** (a step of the figure on a spoken word, or the start state the sentence describes) | — | reveal |
| 1.0–2.0 | **Hard cut** to L-graphic (G-1) on the second clause | FIG. 01 card: the same figure, full size (hourglass, grid, bars), its mechanism running (particles fall, cells fill) | cy 1390 pill | transition |
| 2.0–3.0 | L-graphic | 1–2 in-figure events on the spoken nouns (the counter steps 4 → 5 DAYS; the "NONSTOP" label + red dot) | — | — |
| 3.0–6.0 | Hard cut or evolve | **The result number** lands: a hero numeral (P-06) or a counter in the same card ("≈ $2,000 · TOTAL COMPUTE") | — | reveal |
| 6.0+ | Hard cut | FIG. 02: the first mechanism figure of the body | — | transition |

**F-B version (brutal / pinksage, ticker stack → word stack → product card)**, from v03.
| t | Layout / camera | Visual | Caption | Cue moment |
|---|---|---|---|---|
| **f0** | L-stack | Top band: P-27 ticker card (header strip + 2 rows), values already ticking (+1 step every 4 f, E6) | Chunk 1 above the seam | hook hit |
| 0.0–2.0 | — | Rows tick in sync toward their spoken / script values; the card itself is still | 2-word chunks above the seam | — |
| ≤ 1.0 | — | The first value step lands on a spoken word (the noun of the pain: "bill") | — | reveal (the tick run starts) |
| 2.0 | **Hard cut** to L-full + **Z-1** settle (G-3) | **P-38 word stack**: the payoff clause, 2–3 words blurring in on their onsets ("you / probably / need") | Hidden (z8) | transition |
| ~3.0–3.3 | **Hard cut** to L-graphic | The answer card on the product or brand word: P-28 router, P-20 window card or P-46 logo plate | cy 1450 (brutal) / the card's `caption_cy` (pinksage) | reveal |
| 3.3–6.5 | L-graphic, W-main ↔ W-alt | The promise ("two real use cases"): P-29 tickets or P-23 tiles preview the items | — | — |
| 6.5 | Hard cut | **P-39 numeral card "1"** with the item label typing | — | list cue |

### 6.3 Alternate hooks
**HA-02 Headline + proof (F-B, when the opening line has no number)**, from v02.
| t | Visual | Notes |
|---|---|---|
| f0 | L-pip; the slug pill pops, header line 1 rising; a P-20 window card skewing in (rotateY −10° → 0, 6 f) with the product or offer title | The proof is the window card (kind `card`) |
| 1.0–1.6 | P-22 chips pop on the card's bottom edge on the attribute words (3 chips, 5 f stagger) | — |
| 2.4–2.7 | The window swaps (hard wipe-left 6 f) to the next window; the header rises again with a new slug | The reel's second idea |
| ≤ 2.5 | The proof is readable | payoff |

For example: "This program was built by two physios." → `// who_we_are` / "TRAIN WITH / PHYSIOS." + window "12-WEEK /
STRENGTH." + chips "3x a week", "live", "home or gym".

**HA-18 Borrowed clip (F-A, only with a real source clip, SH-3: the creator's, else fetched)**, v01's opening.
| t | Visual | Notes |
|---|---|---|
| f0 | L-stack with the **source clip in the top band** (`top: "source:<id>"` or `ctx.videoFrame`) and its real source named "SRC: …" at the band's top-left; the title slab sliding in at y 690–813; the presenter in the bottom band | The clip shows the person or event the claim is about |
| 1.5–1.8 | Hard cut to FIG. 01 | The first figure, with a live number |
| ≤ 3.0 | The clip pays off (the claim is clear); the presenter on screen from f0 | — |

Without a clip, open on HA-07 (FB-3). Never a recreated "interview". For example: a real clip of a fund manager's
interview + slab "FUNDS LOST / TO INDEX".

### 6.4 Hook pairs by topic (claim → evidence)
| Topic | Claim (spoken) | Number (provenance) | Figure at f0 → payoff | Format / theme |
|---|---|---|---|---|
| Finance: fund fees | "Most fund managers lose to a simple index fund" | share of funds beating the index over N years (script / source) | P-12 grid fill counting losers → P-15 bars active vs index | F-A editorial |
| Finance: subscriptions | "Your subscriptions cost more than your rent" | monthly totals per app (the creator's own numbers) | P-27 ticker climbing per app → P-06 yearly total | F-B pinksage |
| Finance: compounding | "Starting at 25 instead of 35 doubles your money" | contribution, rate, years (script) → `compound` | P-05 bars climbing by decade → P-06 the gap | F-A editorial |
| Finance: budgeting sheet | "This sheet replaced three apps" | minutes to set up (creator) | P-25 stopwatch counting → P-26 receipt "$0" | F-B brutal |
| Fitness: steps | "8,000 steps does more than an hour at the gym" | steps, minutes (study, cited) | P-12 grid of days filling → P-15 bars | F-A editorial |
| Fitness: program launch | "Twelve weeks, three sessions, no gym" | weeks, sessions (offer facts) | P-35 count 0 → 36 sessions with calendar → P-20 program window | F-B brutal |
| Fitness: protein | "You're eating half the protein you need" | grams eaten vs target (script) | P-27 ticker of grams per meal → P-15 bars vs target | F-B pinksage |
| Fitness: recovery | "Sleep under 6 hours erases a week of training" | hours, % strength (study, cited) | P-02 hourglass of nights → P-16 off-chart loss bar | F-A editorial |

Write this reel's claim → number → figure pair before anything else in the hook.

### 6.5 Headline writing
**F-A title slab formula:** `[SUBJECT] [PAST/PRESENT VERB] / [OBJECT or RESULT]`, caps, ≤ 5 words, 2 lines, ≤ 16 characters
per line, no punctuation, no emoji. It names the *event*; the live number shows the *scale*.
- "INDEX FUNDS / BEAT 9 IN 10" · "WALKING BEAT / RUNNING" · "RENT ATE / YOUR RAISE"

**F-B section header formula:** slug `// what_this_is` + line 1 (a verb or a frame) + line 2 (the payoff noun + a period),
caps, ≤ 6 words, ≤ 12 characters per line.
- `// who_we_are` "LEARN BY / BUILDING." · `// what_you_get` "SHIP REAL / PROJECTS." · `// the_cost` "YOUR BILL / EXPLODED."

Rules:
- Write 8–10 and pick by the stopper test; the next two are the alternates.
- English on screen even when the speech is Hinglish or Hindi.
- Never: vague hype ("GAME CHANGER"), a question mark in the slab, a number the figure doesn't show, a claim the script
  doesn't support.

### 6.6 Hook sound
The hook carries cues on f0 (a hit), on the first value landing (a tick run or a pop) and on the first hard cut. The bed runs
from f0 under the voice (§11).

### 6.7 CTA, brand and end cards
Devices: `comment_keyword` (default), `dm`, `link_bio`, `none`. Placement: **F-B mid + end; F-A at the end, if at all.**

**comment_keyword** (the reel's keyword, KEYWORD, and the creator's deliverable):
| Moment | Spoken pattern | On screen | Hold |
|---|---|---|---|
| **Mid CTA (F-B)**, a quarter to half-way through, right after the first proof (v02 26%, v03 49%) | "If you comment KEYWORD, I'll send you the free guide…" | Hard cut to L-full + Z-1; **P-48 keyword card** ("comment" + "“KEYWORD”") y 1080–1420, captions hidden; then **P-49 promo carousel** (1.5–2.5 s) and **P-41 title window** with the deliverable's exact title typed (1.5–2.5 s) | keyword ≥ 1.5 s |
| **End CTA** (both formats), the last 2.5–3.5 s | "Comment KEYWORD and I'll see you there." | Hard cut to L-full + Z-1; P-48 keyword card 1.5 s; **P-50 comment sheet** slides up over the blurred presenter with the keyword typed into the input (1.0–1.5 s) | keyword ≥ 1.5 s |
| Silence | None before the CTA (the voice is continuous in every source reel) | — | — |

**dm:** the same placement; the keyword card reads "DM “KEYWORD”"; no comment sheet (end on the keyword card).
**link_bio:** the keyword card becomes "link in bio" + the deliverable title on a P-41 title window, held 2.0 s, at the end
only.
**none:** F-A ends on its last figure (the P-18 slider matrix or the result number); F-B ends on the benefit card. Hard end
≤ 6 f after the last word.

**Brand and end cards:**
- **Sponsor (P-52):** a "Paid partnership" chip (mono 24, `mute` text on a 2 px outline) at x 64, y 150 in both formats (the
  F-A FIG line stays at y 232 below it), held ≥ 2.0 s from the sponsor's first mention, plus the spoken disclosure. The
  sponsor's logo (theirs, else fetched from their site) or their name set in type on a P-46 plate; clear of the face and
  the figures.
- **Promo carousel (P-49):** the deliverable card of the mid CTA, ≤ 2.5 s, on W-promo; thumbnails only from SH-5.
- **Title window (P-41):** the exact deliverable title, ≤ 2.5 s.
- **The end card is the comment sheet (P-50):** ≤ 1.5 s, the keyword typed in the input, nothing else; keyword card and
  sheet together ≤ 3.5 s (`brand.endcard.max_s`).
- Brand colours only on brand elements; the keyword readable ≥ 1.5 s; a black tail ≤ 0.2 s.

---

## §7 Structure and rhythm

### 7.1 Structure: one per format
**F-A `explainer` (a figure sequence).** One figure per idea, numbered in order. The arc, from v01's fourteen figures in
75 s:
| Act | Where | Content | Typical patterns |
|---|---|---|---|
| 1 Claim + scale | the opening | What happened and how big (the hook, the result number) | HA-07 stack, P-02, P-06, P-12 |
| 2 What it is | the first quarter | The object or problem explained (what X is, why it's hard) | P-03, P-04, P-05 |
| 3 The record / the stakes | before the middle | Who held it, since when, who challenged it | P-06, P-07, P-08, P-09 |
| 4 How it was done | the middle | The process, step by step (the run, the resources, the method) | P-10, P-11, P-12, P-13 |
| 5 Verification / proof | the last third | Who checked it; the comparison with others | P-14, P-15 |
| 6 Caveat + meaning | the end | What it isn't; what it changes (the payoff); the CTA if chosen | P-19, P-16, P-17, P-18 |

**F-B `list` (pitch → items → CTA twice).** From v02 and v03:
| Section | Where | Content | Typical patterns |
|---|---|---|---|
| HOOK | the opening seconds | The pain number or the offer headline | HA-07 ticker stack / HA-02 pip + window |
| PRODUCT | right after | The product or offer named, the promise ("two use cases") | P-28, P-20, P-46, P-29 |
| ITEM-1…n | the first half | Each item: numeral card → 1–3 cards | P-39 → P-30, P-28, P-29, P-23 |
| CTA-MID | a quarter to half-way | Keyword + deliverable | P-48, P-49, P-41 |
| BENEFIT / PROOF | the second half | Who it's for, the stat, what you'll learn | P-31, P-40, P-33, P-34, P-35 |
| CTA-END | the last 2.5–3.5 s | The keyword again + the comment sheet | P-48, P-50 |

### 7.2 Markers
- **SM-FIG (F-A).** Every L-graphic card carries the FIG line "FIG. nn  TITLE … SRC: …" at y 232. Numbers are two digits,
  start at **01**, rise by one per **new card concept** (a card that evolves keeps its number), and never repeat or go
  backwards: a visible order the viewer can trust (v01 ran 04 → 05 → 06 → 08 … and restarted at 01 near the end; this style
  doesn't). L-stack top bands and L-full frames carry no FIG line.
- **SM-NUMERAL (F-B).** One full-screen numeral card per list item (P-39), on the ordinal word ("1.", "One:", "First"),
  ascending. The label box types the item name. Sections without a list use the slug lockup only (v02 has no numerals; v03
  uses "1", "2").
- No recap, no teaser chips.

### 7.3 The rituals
**F-A figure ritual (every card):**
1. **f −2 (lead):** hard cut (G-1, or a scene swap with `cuts`) on the first content word of the sentence.
2. **f 0:** W-main (or W-alt) and the FIG line are present; the whole figure is on the cut frame; its main object starts its
   mechanism, or a later element draws on (10–14 f) or pops (4 f) on its word.
3. **f 8 → end:** the mechanism runs (particles fall, rings add, bars grow, cells fill), with events on the sentence's nouns
   and numbers: one to three, each on its word, never so far apart that the card goes still.
4. **The hold:** a card lives as long as its idea. It stays longer only while it keeps changing (v01 holds a terminal card
   7.6 s with a new line every second).
5. **Exit:** none: the next hard cut replaces the card. When the next sentence continues the same idea, the card **evolves**
   instead (T-04): the hero numeral dims and becomes the backdrop of the portrait card (v01 0:19 → 0:21).
6. **The face returns** in time (§3.6): an L-stack with this figure re-laid in the top band, or an L-full on a turn word.

**F-B item ritual (every list item):**
1. Hard cut to the **P-39 numeral card** on the ordinal word (lead 2 f). The numeral fades in with its 1.06 → 1 settle (6 f);
   the label box appears 6 f later; the label types 1 char / 2 f with the caret.
2. Hold 1.2–1.6 s (the spoken item name).
3. Hard cut to the item's first card (alternating W-main / W-alt) on the item's first content word.
4. One to three cards per item, each with at least one event (a cursor click, a fork drawing, tickets scattering then
   sorting).
5. The face returns (L-full or L-stack) between items or on the item's opinion.

The ritual is the one place repetition is the point: the viewer learns it and feels the count go up.

### 7.4 Open loops and the re-hook
- **Loops used:** the count promise ("two use cases", "three things") paid by numeral cards; F-A's result-number loop (shown
  by 6 s, explained by the end); F-B's deliverable loop (the mid CTA, paid by the end CTA and the comment sheet).
- **The re-hook.** F-A puts a **turn beat** where attention sags, around every twenty-five seconds (v01's "Then…", "But…"):
  a hard cut to L-full + Z-1 on the turn word ("Then", "But", "Until", "Now"), or a figure with an open slot (the dotted "?"
  bar of P-05, the "UNCLAIMED" line of P-08). F-B's mid CTA *is* its re-hook.
- **The hook is over fast:** the hook and the product or promise are done while the promise is fresh, so the first figure
  of the body (or the first numeral) arrives early.
- Every promise is paid on screen.

### 7.5 Rhythm by feel
- **The speech is the rhythm.** A new idea is a new picture, on its first word; the cut lands there and nowhere else. The
  card never waits for the voice and the voice never waits for the card.
- **It never sits still, but it's never random.** Inside every card something lands on the words: a ring, a bar, a counter
  step, a typed log line. When the words give nothing new, the mechanism keeps the card alive (particles fall, a dot orbits),
  and when the idea changes, the cut comes.
- **The face is the breather.** F-A runs steady and dense, figure after figure, and the face returns as the breath between
  ideas: on the opinion, the caveat, the turn. The claim gets the face; the explanation gets the figure.
- **F-A's energy curve:** dense from frame 0 → steady through the mechanism → the verification act slows down, its bars
  filling with weight → the last figure carries the biggest idea (the price, the shift, the summary matrix).
- **F-B's energy curve:** fast and punchy. The ticker hook is dense, the product card lands, the numerals are resets; the mid
  CTA drops the energy to one big word; the benefit section re-accelerates; the end CTA is clean.
- There are no comedy beats (comedy off): the energy comes from the cut, the figure and the moving numbers.
- For reference, measured on the three reels (a description, not a target): hard cuts 2.1 / 3.4 / 5.7 per 10 s (v01 / v02 /
  v03), median gap 3.0 / 2.0 / 1.3 s; v01's graphic holds run 2–7.6 s between hard cuts; the longest near-static stretch is
  2.3 s (v01 0:22.4–0:24.8); cuts to the presenter: 8 in v01's 75 s, 5 in v03's 44 s.

---

## §8 Visual system: B-roll and patterns

`graphics: primary`: designed graphics own most of the runtime (v01 ≈ 75%, v02 ≈ 65%, v03 ≈ 55%, counting the L-stack top
band). Every spoken quantity becomes a figure that animates; comparisons share one axis (`scale_id`). Variety comes from
the moment, never from a quota: a different idea looks different because it *is* different. The F-B numeral ritual is the
one deliberate repeat.

### 8.1 Families (B-…)
| ID | Family | Source | The creator may supply |
|---|---|---|---|
| **B-1** | Figure cards (editorial data art: hourglass, rings, bars, grids, timelines) | engine | — |
| **B-2** | Window and ad cards (neo-brutalist windows, chips, tiles, tickets, routers) | engine | — |
| **B-3** | Type cards (title slab, word stack, numeral card, stat highlight, title window) | engine | — |
| **B-4** | Diagrams and flows (node map, router fork, cycle, slider matrix) | engine | — |
| **B-5** | Presenter stage patterns (split proof, guest bubble, card over head) | the A-roll | the A-roll |
| **B-6** | Evidence and inserts (portraits, quote notes, app screens, logo plates, source clips) | the creator's own files, else the real thing fetched from the web (source noted), else rebuilt from its exact text (named per pattern) | photos, screenshots, recordings, clips, logos |
| **B-7** | Data figures (counters, tickers, bars, grid fills) bound to `figures.json` | engine | the numbers (script or creator) |
| **B-8** | CTA and brand (keyword card, promo carousel, comment sheet, decor band, sponsor chip) | engine (+ the creator's thumbnails) | 3–6 of their own thumbnails (SH-5) |

### 8.2 How the graphics behave
- **Every card is one element:** labels, chips, the FIG line and value boxes are drawn inside the card's own scene. With the
  caption, a frame holds at most three text blocks: the card, the F-B header lockup (when present) and the caption.
- **One idea per card:** at most three animated groups; everything else static or dimmed to 40%.
- **Small quantities are countable:** up to about a hundred, show every unit: 96 machines are 96 cells (P-12), 9 loops are 9
  rings (P-03).
- **Every number moves** (D4) and lands on its word.

### 8.3 Pattern specs (P-…)
Motion is in frames at 30 fps. "Engine" names the building block in `plan/scenes.js`. Every card scene declares
`text_class`, `events` (every in-card change), `figure` / `figures` when it shows numbers, and `cuts` when it swaps hard.
Class shorthand: D display, L label, x decorative.

**B-1 Figure cards (the F-A home family; usable in F-B)**
| ID | Pattern | Type | What's on screen | Motion (30 fps) | Use for | Engine | Class / needs |
|---|---|---|---|---|---|---|---|
| **P-01** | **FIG card frame** | figure | W-main full-bleed; the FIG line at y 232 (left "FIG. nn  TITLE", right "SRC: …" when the card has a real source); the figure inside the zone x 64–1016, y 300–1320 | Hard cut in (0 f); the FIG line **and the whole figure** are present on the cut frame (v01 0:01.66, 0:38.70); the mechanism (particles, typing, counters) runs from f0; no exit animation | Every F-A L-graphic card | bespoke `VEOS.scene` z3; the FIG line in the small-print class (`type.fig_line`); SRC via `fx.creditLine` | the figure's class; sources |
| **P-02** | **Hourglass counter** | figure | A `card` hourglass (x 230–850, y 300–1350, 40 px waist) with 24 seeded ink dots in the top bulb and one `primary` "start" dot with a leader label ("DAY 1 · one instruction", mono 30); a counter numeral at x 64, y 760–900 (Instrument Serif 160 px `primary`) + a "DAYS" micro label; a "NONSTOP" micro label with a `bad` dot appears on its word | A dot drops through the neck every 6 f (10 f ease-in fall, seeded x jitter ±6 px) and piles at the bottom; the counter steps on the spoken time words (each step an event; `exception: E6` inside a fixed box) | Time passing, duration, "for a whole week", waiting | `ctx.canvas()` + `VEOS.data.counter` (kind counter, steps at words) | D counter, L micro (E3 redundant), E6 |
| **P-03** | **Loop rings** | figure | Concentric rings at (540, 800), ring k radius 70 + 28k, 4 px, coloured along `G-fill` by k; a dot orbits the outer ring; the count numeral at the centre (Instrument Serif 160 px); a formula or label under it (serif italic 64 px + a micro label) | Each new ring draws on in 6 f (stroke-dashoffset) on its count word; the numeral steps (E6); the orbit dot does 1 rev / 2 s | Layers, levels, iterations, rounds, "N times" | `ctx.canvas()` + counter figure | D, E6 |
| **P-04** | **Crossing paths** | figure | A perspective grid floor (`mute` 18%); two spheres (r 60, `bad` and `accent`, 30 px soft glow) on dashed diagonals from opposite corners; small mono labels (p1…p4) at the path ends; a header micro label ("PREDICTED OUTCOMES") | The spheres travel 20 f ease-in-out to cross at the centre; on contact 12 seeded particles scatter (12 f) | Two forces meeting, a collision, a match, a competition, a prediction | `ctx.canvas()`, `ctx.rngStable` | illustrative (`illustrative: true`); L micro |
| **P-05** | **Bar climb** | figure | An axis on the left with an up arrow and a label (`accent` mono 30: "HARDER", "COST", "TIME"); N bars (L1…Ln micro labels) in `G-old`; the next slot as a dotted outline with "?" | Bars grow one after another, 3 f stagger, 14 f each, heights from the figure's steps (one `scale_id`); the "?" slot pulses 1.0 → 1.06 → 1 on the open-question word; an optional curve draws over the tops (12 f) | Exponential or steady growth, "every step makes it harder", the record to beat | `VEOS.data.bars` or a bespoke canvas with `ctx.figScale` | L, figure, scale |
| **P-06** | **Hero numeral** | figure | One numeral in Instrument Serif **640 px** `primary`, centred (y 560–1100); a micro label under it ("LOOPS · THE RECORD") | Blur-in 10 f (blur 16 → 0, scale 1.04 → 1); an 18 f counter roll when the value is computed; afterwards it may **dim to ≈ 20%** and stay as the backdrop of the next card (evolve, T-04) | The single number the sentence is about (a record, a total, a price) | `VEOS.data.counter` (size 640, font numeric) | D, figure |
| **P-07** | **Portrait pair** | figure / insert | 1–3 circular portraits d 280 at y 420–700 with 4 px rings (`primary` for the first, `accent` for the second), halftone; the name in mono 32 caps (`cream` on W-main), the role in mono 26 `mute` | Each scales in 0.2 → 1 with a fade in 4 f, no overshoot, 6 f stagger, on the name word; name and role fade in 4 f after (v01 0:21.05–0:21.45) | People named in the script | `fx.shot` (the creator's photo, else the real one fetched; + halftone) else **`fx.silhouette`** | L; insert (person) |
| **P-08** | **Timeline dot** | figure | An x axis of years (mono 30), y ticks for two levels; a glowing `primary` dot at the start; a dashed `accent` target line with a micro label ("UNCLAIMED") | The dot pops 4 f; a solid line draws from the dot towards the current year over the spoken span; the target line draws 12 f | "Nobody had done it for N years", a record standing, waiting time | `VEOS.data.slider` (years) + a bespoke line | figure (years), L |
| **P-09** | **Quote note** | insert | A `card` note (x 108–990, y 420–1260) tilted −3°; an avatar circle (creator photo or initials), the name 36 px bold, the role 26 px `mute`, the date in `primary` mono 26; the quote in Instrument Serif italic 58 px; a footer micro label | The note settles from −8° and y +60 in 10 f; quote words appear on their spoken onsets (word for word); the key phrase gets a 6 px `primary` hand underline drawn L → R in 10 f | Someone's public statement, a challenge, a review, a promise | **`fx.quoteCard`** (`reveal`, `highlight`, theme paper) | L; insert (post) |
| **P-10** | **Run log** | figure / insert | A dark window (`#1E1C1A`, radius 18, traffic lights, a title, a model chip outlined in `primary`), x 64–1016, y 400–1340; log lines in mono 38 with timestamps in `mute`, "update:" lines in `accent`; a status line at the bottom ("☾ OPERATORS: ASLEEP") | Typing at 22 chars / s (`fx.typewriter`); a new line every 0.6–1.0 s on the spoken words; the status line fades in 6 f on its word | A process running unattended, an agent working, a sequence of steps | **`fx.appUI({kind: "terminal"})`** or bespoke | L / x filler; insert (app_ui) when it stands for a real product |
| **P-11** | **Code fix** | figure | 5–7 code-shaped lines (mono 30, `mute` 45%, decorative); one line gets a `bad` wavy underline + an "✕ ERROR" pill (mono 34, paper on `bad`), which flips to "✓ FIXED" (`accent` or `good`) | The underline draws 8 f; the pill pops 4 f on "bug / error"; it flips on the X axis in 4 f on "fixed"; the code blurs to 6 px 8 f later | Bugs, mistakes, self-correction | bespoke | x + L pill |
| **P-12** | **Grid fill** | figure | A 12 × 8 grid of rounded squares (56 px, gap 14, radius 10) at x 126–954, y 780–1320; empty cells `mute` 12%; filled cells coloured along `G-fill` by column; the counter top-right (Instrument Serif 120 px `primary`) + a micro label ("CPUs RUNNING") top-left | Cells fill in reading order, 1 cell / f, up to each step's value; the counter rolls to the same step (18 f) and lands on the spoken number | Capacity, scale, "N machines / people / days", a share of a whole (out of 96 or 100) | `VEOS.data.counter` + a bespoke grid bound to the same figure (`grid_fill`) | figure, D counter, E6 |
| **P-13** | **Node map** | figure | W-alt graph paper; 6–9 nodes (circles 60–90 px in `primary`, `accent`, `highlight`, `good`) with mono chip labels (a white chip, 2 px ink outline, mono 30 caps, redundant); a centre node (an ink circle 120 px with the result glyph) appears last; a footer micro label ("EVERY METHOD: …") | Nodes pop 4 f, 4 f stagger, on the nouns; lines draw from each node to the centre (10 f, 2 f stagger); optional value chips (mono 30) slide up at the bottom on their numbers | Many ingredients combining, existing methods, "pulled it all together" | **`fx.diagram`** (nodes + edges) | one element, L |
| **P-14** | **Check bars** | figure | A portrait (P-07 style) top-left; a day counter numeral right (Instrument Serif 200 px `primary` + "DAYS CHECKING"); two progress bars (track `mute` 25%, fill `accent`), each with a mono label and a % value; a result chip under them, with a `primary` oval drawn around it | The counter steps on the time words; bar 1 fills to 100% in 18 f, then "✓ PASS" (`good` mono) replaces the %; bar 2 follows; the oval draws 12 f on "held up / passed" | Verification, review, testing, approval | bespoke + `VEOS.data.counter` | figure, L |
| **P-15** | **Compare bars** | figure | Vertical bars on one axis (y ticks mono 30 `mute`); old = `G-old`, new = `G-new`; under each bar a name (Plus Jakarta Sans 600 40 px, `primary` / `accent`) + a micro sub-label; a dashed threshold line with a label at the right ("FRONTIER"); a marker (a diamond or ✓) drops onto the winner | Bars rise 14 f, 6 f stagger, in the spoken order; the threshold draws 12 f; the marker drops 8 f with a 2-frame bounce | Old vs new, A vs B vs C, "reached the same level" | **`VEOS.data.bars`** (shared `scale_id`) + a bespoke threshold | figure, scale, L |
| **P-16** | **Off the chart** | figure | One `G-old` bar on a baseline (x 160–340) with the micro label "EXPECTED" + "off the chart ↑" (serif italic 64 px `bad`) | The bar shoots past the top edge in 10 f (ease-in), holds 0.6 s, then collapses to its true value in 12 f (ease-out) while the annotation fades; the "ACTUAL" micro label appears | Expected vs actual, "thought it was too expensive", overestimates | bespoke + figure | figure (the off-chart phase is `illustrative`) |
| **P-17** | **Price tag** | figure | A line-drawn object outline (4 px `cream` or ink: laptop, phone, car, house, bag; `fx.icon` or paths) with the subject's glyph inside; a `primary` price tag (mono value via `ctx.fmtNum`) on a string | The outline draws 14 f; the glyph fades in 6 f; the tag swings in from the top-right and settles with a 10 f pendulum (±12° → 0) | "For the price of X", real-world cost comparisons | bespoke + figure | figure, L |
| **P-18** | **Slider matrix** | figure | W-alt; 3–5 rows: a left pole label (mono 30 caps), a track with 3 dots, a right pole label; a soft `accent` ribbon (90 px wide, 22%) | The ribbon sweeps through the active dot of each row from the left column to the right over 24 f (ease-in-out); the final dot glows `primary`; the active poles get a chip | The summary: what changed, before → after on several axes | bespoke canvas | L; the last card of F-A |
| **P-19** | **Horizon** | figure | A half disc (`primary`, grain) above a thin horizon line, its blurred mirror below; a serif label top-left (Instrument Serif 72 px `primary`) + a micro sub-label | The disc rises 16 f from the horizon; the label types 1 char / f | Model vs reality, a simplified version, "this isn't the real world" | bespoke | illustrative; L |

**B-2 Window and ad cards (the F-B home family)**
| ID | Pattern | Type | What's on screen | Motion (30 fps) | Use for | Engine | Class / needs |
|---|---|---|---|---|---|---|---|
| **P-20** | **Window card** | overlay | A `card` window x 80–1000, y 640–1300, radius 14, **5 px `line` outline, hard shadow +12/+14** (`line`, or `primary` on cream); a 60 px title bar with three outlined dots, a mono filename (decorative) and window buttons; inside, the title in Barlow Condensed 700 **120 px** caps (line 1 ink, line 2 `primary` deepened) + a tag chip (`accent`) | Hook: settles from a perspective skew (rotateY −10°, rotate −4°, scale 0.94) in **6 f** expo-out (v02 0:00 → 0:00.24). Body: **T-08 grow-in** from a `primary` chip (scale 0.25 → 1, fill `primary` → `card`, 6 f), then the title slab slams (5 f) and the lines rise (4 f each); a second window sits offset behind (+18/+22, `primary` fill) as a stacked deck (v02 0:18.2–0:19.1); chips pop last | The offer, the product, a module, a statement | bespoke `VEOS.scene` (one element, chips inside) | D title, L chips, x chrome |
| **P-21** | **Slug header** | headline | The F-B lockup (§5.2): `// slug` pill + a 2-line Barlow Semi Condensed header | The slug pops 4 f; the lines rise out of their clip line (4 f each, line 2 ≈ 10 f later); a section change = a slug swap + the lines rising again | Every F-B section in L-pip / L-graphic | bespoke, `kind: "lockup"` | D + L (E3 redundant) |
| **P-22** | **Chip row** | annotation | 2–4 chips (§5.4) on the bottom edge of the card, slightly rotated | Each pops 0.6 → 1.06 → 1 in 4 f (`in: "pop", in_frames: 4`), 5 f stagger, on its attribute word | Attributes: duration, format, level, price | inside the P-20 scene (events) | L |
| **P-23** | **Tile grid** | overlay | Inside a window, 2 × 2 tiles (fills `primary`, `accent`, `#F6D9D5`, white; 3 px outline), each with an `fx.icon` 64 px, a 2-line label (Barlow Condensed 56 px) and a mono micro chip (step / week); a cursor arrow | Tiles pop 4 f, 5 f stagger, on their nouns; the cursor glides 10 f to the tile being named and taps (scale 0.94, 3 f) | Modules, features, a curriculum, what's included | bespoke | L |
| **P-24** | **Profile fan** | insert | 2–3 profile cards (520 × 700) with a colour panel (`primary` / `accent`) holding the photo, the name (Barlow Condensed 56), a role chip and a micro credential line | They fan in from the right (rotation −6° / +4°, 8 f, 6 f stagger); a star sticker (`fx.icon('star')`, `accent`) pops on the last name | Instructors, team, founders, coaches | `fx.shot` (the creator's photos, else the real ones fetched; halftone) else **`fx.silhouette`** | L; insert (person) |
| **P-25** | **Stopwatch** | figure | A stopwatch (`primary` ring, 5 px ink outline) with an `accent` sector; the minutes counter (Poppins 800 160 px, ink stroke, hard shadow); a unit chip ("MINUTES", `accent`, skewed −4°); a header "IT TOOK ME [ONLY]" (Barlow Condensed 56 + chip) | The sector sweeps clockwise in step with the counter (an 18 f roll to each step); the unit chip pops 4 f | Time to do it, setup time, speed claims | `VEOS.data.counter` + a bespoke dial | figure, D |
| **P-26** | **Receipt** | figure | A receipt (white, zig-zag bottom, 5 px `line`) with "LESS THAN" mono + the value (Poppins 800 120 px) + a coin icon (`good`) | It prints downward in 16 f (clip reveal) beside the shrunk stopwatch; the value rolls 10 f | The cost of doing it, "for less than $1" | bespoke + figure | figure |
| **P-27** | **Ticker card** | figure | A `primary` card (x 64–1016; in L-stack y 140–730) with an ink header strip (mono 34 "Billing Information" in paper) and 2–3 rows: a logo plate (the real logo, the creator's or fetched, else the name set in type on a white chip) + "–" + the value (Poppins 800 **150 px** white, 5 px ink stroke, hard shadow +8/+10) in a fixed-width value box | Values step every **4 f** towards the next figure step (`exception: E6`, a hard swap in `data-slot` boxes), rows in sync; the card itself is still | Bills, costs, prices rising, counts climbing in real time | `VEOS.data.counter` per row (steps, `roll` 0) or bespoke with `ctx.figAt` | figure, E6, D; insert (product) for logos |
| **P-28** | **Router fork** | figure | A name box (`primary` fill, 5 px outline, hard shadow, Barlow Condensed 96 px) at the top; dashed connectors to 2 option boxes (white, ink outline, Poppins 600 48 px); a cursor | The box pops 4 f; the connectors draw 10 f; the options pop 4 f, 4 f stagger; the cursor clicks the box (3 f); the chosen branch thickens to 6 px and turns `accent` / `good` on the decision word | Routing, choosing, "decides whether…", either/or | **`fx.diagram`** (nodes + dashed edges) | one element |
| **P-29** | **Ticket sort** | figure | 8–12 tilted white tickets (Poppins 600 40 / 30 px, two lines: type + name; 3 px outline) scattered over W-alt; 2–3 labelled bins (`primary` / `highlight` boxes with Barlow Condensed labels) | Tickets pop in (scale 0.2 → 1 in 3 f) at seeded positions with ±12° rotations, 1–2 new tickets per frame until 10–12 are on (≈ 0.6 s, v03 0:15.78–0:16.38); on the routing verb they fly into their bins in 14 f and align into grids | Classification, triage, sorting leads / tickets / tasks | bespoke, `ctx.rngStable` | L (≤ 12 snippets inside one element) |
| **P-30** | **Button press** | overlay | A window: a heading (Poppins 600 64 px, e.g. "0 Credits Remaining") + a `primary` button with a hard shadow ("Buy More", Poppins 700 72 px); a cursor | The cursor glides in 10 f and presses: the button's shadow collapses in 3 f and it scales to 0.96 | A pain moment, a paywall, an action the viewer knows | bespoke | D |
| **P-31** | **Icon slab** | overlay | One big flat icon (`fx.icon`, 380 px, `accent` fill + ink outline) and a tilted slab label (Barlow Condensed 110 px caps, ink, on a `primary` slab, −4°): "IF YOU'RE A / {AUDIENCE}" | The line "IF YOU'RE A" rises (4 f); the slab **slams** (scale 1.8 → 1, roll −8° → −3°, 5 f) on the audience word (v02 0:27.50): the slab is its own scene with `in: "stamp", in_frames: 5`; the icon pops 6 f later. The card leaves by the T-08 shrink-out. **Optional 3D slam (off by default; the source's slabs are flat):** a brand word or the creator's own logo as `VEOS.fx.three` `text` / `svg` dropping in with a `back`-eased key over ≈ 0.35 s and a ground shadow, its box sized to the word; it's a signature moment, the only 3D scene on screen, so it happens once if at all (45–150 ms/frame) | Audience call-outs, "this is for you if…" | bespoke + `fx.icon` | D |
| **P-32** | **Alert window** | overlay | A window with a `good` circle "!" icon and 3 lines in Barlow Condensed 100 px ("DON'T / MISS / THIS."; the last line `primary`) | T-08 grow-in (0.25 → 1, roll −5° → −2°, 6 f; v02 0:29.26); the lines are already set | Urgency, "don't miss this" | bespoke | D |
| **P-33** | **Prompt window** | overlay | A chat window: an input bar with "+" and a send button (`good`), a `primary` message block (3 blurred text lines, decorative), tag chips down its left edge (ROLE / TASK / STYLE / FORMAT, mono 30, redundant), an attachment card | The message block slides up 8 f; the chips pop 4 f stagger on the spoken technique; the attachment card rises 8 f | How to instruct a tool, a method with named parts | bespoke (a generic UI, never a real product's look) | L (E3 redundant chips) |
| **P-34** | **Media fan** | overlay | A phone (ink, play button `accent`) centred, an image card left and a post card right (tilted ±8°); chips "ADS", "CONTENT" (or the creator's formats) | The cards fan out 8 f; the chips pop on their words; the phone's progress bar fills over 30 f | Outputs, formats, deliverables | bespoke | L |
| **P-35** | **Play grid** | figure | A headline count (Poppins 800 200 px `primary`, ink stroke, hard shadow), e.g. "1 → 100s", + a calendar icon "1 DAY"; a 6 × 4 grid of play tiles in mixed fills | The count rolls on the number word (18 f); tiles pop in a seeded order, 2 f stagger, until the grid is full | Volume, scale of output ("hundreds a day") | `VEOS.data.counter` + a bespoke grid | figure, D |
| **P-36** | **Cycle diagram** | figure | A dashed ellipse loop with 6 nodes (small `fx.icon` circles + mono labels) around a centre avatar icon; a header chip (`primary`, mono) with the system's name | Nodes pop 4 f stagger; a dot travels the loop (1 rev / 3 s); the active node scales to 1.15 when named | An automated loop, a workflow that repeats | **`fx.diagram`** | one element |

**B-3 Type cards**
| ID | Pattern | Type | What's on screen | Motion (30 fps) | Use for | Engine | Class / needs |
|---|---|---|---|---|---|---|---|
| **P-37** | **Title slab** | headline | The F-A plate (§5.2) in the L-stack top band, lines y 690–813 | Line 1 from the right, line 2 from the left, the same frame, horizontal blur 14 → 0, 12 f expo-out (T-05) | The F-A hook | bespoke, `kind: "plate"` | D |
| **P-38** | **Word stack** | overlay (z8) | On L-full: 2–3 words of the clause stacked (Poppins 700 lowercase 110 / 140 / 110 px, white, soft shadow), left edges aligned at x 300, y 1050–1350, below the chin | Each word blurs in on its onset (blur 10 → 0, scale 1.06 → 1, **4 f**, `in: "blur", in_frames: 4`; v03 0:02.03, 0:02.27, 0:02.63); the stack clears on the hard cut | The punch clause of a hook or a claim ("you / probably / need") | **`fx.typeStack`** (`maxLines` 3, `fx.linesFromWords`) + `captions.hide` | D; captions hidden |
| **P-39** | **Numeral card** | marker | W-main (or W-alt); the numeral (Poppins 800 **720 px** white, 8 px ink stroke, hard shadow +16/+18) at y 230–800; a label box (white, 5 px outline, hard shadow +10/+12) at y 900–1060 with the item name (Poppins 700 88 px) | The numeral fades in with a 1.06 → 1 settle in 6 f (no pop; v03 0:06.53–0:06.73); the label box appears 6 f later; the name types 1 char / 2 f with a caret blinking 8 f on / 8 f off | Every F-B list item (SM-NUMERAL) | bespoke, `kind: "number"` | D |
| **P-40** | **Highlight stat** | figure | The stat line(s) in Poppins 600 110 px ink on W-main; a `highlight` bar behind each phrase; 3 columns of tiny body texture above (decorative) | The bar wipes L → R behind each phrase on its spoken word (8 f) | A headline result ("200× faster, 400× cheaper") | bespoke + figure (`ratio`) | D, figure |
| **P-41** | **Title window** | overlay | A window with an ink header strip (mono 30 "{KIND} TITLE" in paper) and the exact title typed (Poppins 800 110 px; white with an ink stroke on pink, ink on white); the last word in `primary` | The window skews in 6 f; the title types 1 char / f | The deliverable / event / course title | bespoke | D |

**B-4 Diagrams and flows:** P-13, P-18, P-28 and P-36 (above) form the diagram family; each is one element with its labels
inside.

**B-5 Presenter stage patterns**
| ID | Pattern | Type | What's on screen | Motion | Use for | Engine | Class / needs |
|---|---|---|---|---|---|---|---|
| **P-42** | **Split proof** | stage | L-stack: the current figure re-laid in the top band (content inside y 140–730), the presenter below, the caption 24 px above the seam | Hard cut in (G-2); the band's figure keeps its mechanism running | The hook; the presenter commenting on a figure (an opinion, a caveat, "it used…") | stage `L-stack`, `via: "cut"` | — |
| **P-43** | **Guest bubble** | stage | L-pip with the slug header (P-21) left and a window card (P-20) below | Hard cut in (G-4); the ring is on from the first frame | F-B intros and section openers, while the header and the window carry the section | stage `L-pip` | — |
| **P-44** | **Card over head** | stage | L-cardtop: a P-25 / P-20 card from y 130, ending ≥ 40 px above the hair, over the lowered presenter | Hard cut in (G-5); the card skews in 6 f | The presenter's own proof ("it took me…", "I did this in…") | stage `L-cardtop` | 40 px clear of the head |

**B-6 Evidence and inserts** (the real thing, fetched when the creator has none: §12.4)
| ID | Pattern | Stands in for | The real thing (the creator's file, else fetched) | Rebuilt when nothing usable turns up |
|---|---|---|---|---|
| **P-45** | **App screen** | A product's UI or a screen recording | `fx.shot` / `fx.clip` in a dark window (W-dark), radius 18, a title bar, a `primary` highlight box on the field being named | **`fx.appUI`** (`chat` / `terminal` / `list` / `browser`), generic and unbranded |
| **P-46** | **Logo row** | A product or brand named | The real logos (the creator's files, else fetched from the brand's site) in white chips | **`fx.logoPlate`**: the name set in type on a chip, only when no logo can be found |
| **P-47** | **Source clip** | Another person's interview / keynote / press clip (HA-18) | L-stack with `top: "source:<id>"` (the creator's clip, else the real one fetched), the real source named "SRC: …" | No recreated clip: open on HA-07 and use P-09 for their words |
| P-07, P-09, P-24 | Portraits, quotes, profiles | (above) | (above) | `fx.silhouette`, `fx.quoteCard` |

**B-7 Data figures:** P-02, P-03, P-05, P-06, P-08, P-12, P-14, P-15, P-16, P-17, P-25, P-26, P-27, P-35 and P-40 (above)
are bound to `plan/figures.json` (§8.5).

**B-8 CTA and brand**
| ID | Pattern | Type | What's on screen | Motion (30 fps) | Use for | Engine | Class / needs |
|---|---|---|---|---|---|---|---|
| **P-48** | **Keyword card** | overlay (z8) | On L-full: "comment" (Poppins 800 130 px white) over “KEYWORD” (Poppins 800 200 px in curly quotes, fill `accent` in brutal and editorial, `primary` in pinksage), both with a hard ink drop shadow 6/6, centred at y 1080–1420, below the chin | "comment" blurs in 4 f on its word; the keyword blurs in 4 f on its word (no pop; v03 0:21.40, 0:21.64): two scenes, each `in: "blur", in_frames: 4`; it holds ≥ 1.5 s | Every CTA moment | bespoke, **`kind: "cta-keyword"`** | D; captions hidden |
| **P-49** | **Promo carousel** | overlay | W-promo; a pill "FREE · LIVE" (mono, `primary` outline) + the deliverable kind in Barlow Condensed 180 px white ("MASTERCLASS", "GUIDE", "WORKSHOP"); 3 cards in a carousel (centre card 600 × 760): the creator's thumbnails (SH-5) or typographic tiles (FB-5); carousel dots | The header drops 8 f; the cards slide left one position every 0.8 s (12 f ease-in-out); the active dot moves | The deliverable mention in the mid CTA | bespoke + `fx.clip` for thumbnails | D; insert when thumbnails show other people |
| **P-50** | **Comment sheet** | overlay | A generic bottom sheet (`#1E1E1E`, radius 36 at the top, x 0–1080, y 820–1920) over the dimmed presenter; a title bar "Comments"; one input field in which the keyword is being typed, with a caret; no other users, no likes, no platform logo | The sheet rises from the bottom edge in **7 f** (`in: "rise", in_frames: 7`; v02 0:44.60–0:44.84); the keyword types 1 char / 2 f; it holds to the hard end | The end CTA | bespoke + the layout's `dim` treatment | L; never fake comments (v02 and v03 showed brand accounts' comments with likes; this style doesn't) |
| **P-51** | **Decor band** | world (z1) | TH-brutal only: an outlined star, a `primary` squiggle, a 6 × 6 dot matrix and a lime sparkle in the bottom band (y 1580–1860), plus one sparkle beside the card | Static; the sparkle twinkles (scale 0.9 ↔ 1.1 over 30 f) | Every TH-brutal L-graphic and L-pip frame | bespoke z1 scene (no text) | z1: part of the world, not an element |
| **P-52** | **Sponsor chip** | brand | A chip "Paid partnership" (mono 24, small print) top-left at y 150 + the sponsor's name set in type | Fades in 6 f, holds ≥ 2.0 s | Sponsored reels | bespoke | small print |

### 8.4 Line → pattern lookup
Vocabulary, not a decision table: it tells you what this style reaches for when a line sounds like this. Ask what the
viewer should see at this moment, then use it, combine it, or invent a figure in the same design language when the moment
needs one the table never imagined.

| Line type | Primary | Alternates | For example |
|---|---|---|---|
| A duration / time passing | P-02 | P-08 | "eight weeks of training" |
| A count of layers / rounds / iterations | P-03 | P-05 | "five sets, each one harder" |
| Something growing step by step | P-05 | P-15 | "fees compound every year" |
| The single number the sentence is about | P-06 | P-17 | "the record is 42 minutes" |
| People named | P-07 | P-24 | "two economists at a university" |
| "Nobody has done it since…" | P-08 | P-05 "?" slot | "unbeaten since 2009" |
| Someone's public words | P-09 | P-41 | "the CEO wrote…" |
| A process running by itself | P-10 | P-36 | "the bot rebalances every night" |
| A mistake and its fix | P-11 | P-28 | "it caught its own error" |
| Capacity / a share of a whole | P-12 | P-35 | "96 of 100 funds" |
| Many ingredients combine | P-13 | P-23 | "sleep, protein, steps, strength" |
| Verification / testing | P-14 | P-15 | "audited for two weeks" |
| A vs B (vs C) | P-15 | P-28 | "index vs active vs savings" |
| Expected vs actual | P-16 | P-15 | "everyone thought it would cost millions" |
| "For the price of…" | P-17 | P-26 | "the cost of one coffee a day" |
| What changed (summary) | P-18 | P-15 | "from random workouts to a plan" |
| Model vs reality / caveat | P-19 | L-full turn | "this is a backtest, not the future" |
| The offer / product / module | P-20 | P-41, P-46 | "the 12-week strength program" |
| Attributes of the offer | P-22 (inside P-20) | P-23 | "6 weeks, live, beginner-friendly" |
| What's included | P-23 | P-13 | "strength, mobility, nutrition, sleep" |
| Instructors / team | P-24 | P-07 | "built by two physios" |
| "It took me only…" | P-25 (+ P-44) | P-26 | "set up in 20 minutes" |
| The cost of doing it | P-26 | P-17 | "for less than $5 a month" |
| A bill / cost / count rising | P-27 | P-05 | "your subscriptions add up" |
| A decision / routing | P-28 | P-15 | "decide: pay off debt or invest" |
| Classification / sorting | P-29 | P-28 | "sort every expense into three buckets" |
| A pain moment the viewer knows | P-30 | P-27 | "insufficient balance" |
| An audience call-out | P-31 | P-32 | "if you're over 40" |
| Urgency | P-32 | P-48 | "only 20 spots" |
| How to instruct / a method with parts | P-33 | P-13 | "give the app these four rules" |
| Outputs / formats | P-34 | P-35 | "plans, videos, check-ins" |
| Volume / scale of output | P-35 | P-12 | "hundreds of transactions a day" |
| An automated loop | P-36 | P-10 | "plan → train → log → adjust" |
| A headline stat | P-40 | P-06 | "3× cheaper, 10× faster" |
| The punch clause of a claim | P-38 | P-48 | "you probably need this" |
| A product UI / screen recording | P-45 | P-33 | the tracking app's dashboard |
| A brand or tool named | P-46 | P-20 | "an app like Y" |
| A turn / caveat / opinion | L-full + Z-1 | P-42 | "But here's the catch" |
| CTA | P-48 → P-49 / P-50 | P-41 | "comment PLAN" |

### 8.5 Data and truth
Every counter, ticker, bar, grid fill, timeline and hero number is a figure in `plan/figures.json`.

| Field | This style's rule |
|---|---|
| `kind` | `counter` (P-02, P-03, P-25, P-35), `hero_number` (P-06), `bar` (P-05, P-15, P-16), `grid_fill` (P-12), `slider` / `line` (P-08); ticker rows (P-27) are `counter` figures with steps; `ledger` is unused |
| `inputs` | `script` + the exact words (`said`), `creator` (their own prices, minutes, client counts, from their words, brief or files), `source:<id>` (the F-A SRC), or `spoken@t` |
| `formula` | From `data.formulas`: `sum`, `diff`, `ratio`, `percent_change`, `per_period`, `unit_convert`, `compound`, `cagr`; `none` for a stated value |
| `steps` | Each step aligned to its spoken word (`at`); counters land on it ±5 f |
| `scale_id` | Bars compared in one card share one scale id (P-05, P-15); the P-12 grid uses the total as its scale |
| `format` | From `profile.numbers` (international $ k_m_b by default; Indian ₹ lakh / crore when the audience counts in rupees) |
| `illustrative` | `true` for P-04, the off-chart phase of P-16, P-19 and any made-up example: made-up but realistic numbers are fine, with no label |

Display bindings: `VEOS.data.counter` / `bars` / `slider` where the shape fits; for bespoke cards (hourglass, rings, grid,
ticker) bind with `figure` / `figures`, write values with `ctx.fmtNum`, roll with `ctx.figAt`, and declare `lands`. Tickers
(`exception: E6`) step through `ctx.figAt(id, t)` values on a 4 f grid inside a `data-slot` box (±4 px).

The truth rules:
1. **Every number the creator states is a figure** with provenance; `ctx.fmtNum` writes it; counters land within ±5 f of the
   spoken number.
2. **Same axes:** compared bars share one `scale_id` (P-15, P-05).
3. **Old = red, new = accent** (§4.2); `good` only for a pass, a fix or a saving.
4. **Script-stated hypotheticals** ("if you invested $100 a month…") are figures with `from: script` and the words.
5. **Illustrations** (a concept curve, a collision, a mock app, an example dashboard) may use made-up but realistic numbers
   and names, unlabelled (`illustrative: true`). What may never be invented: the creator's results, prices, benchmarks,
   testimonials, and anyone's comments or likes presented as real.

### 8.6 Sources and citations (F-A)
- **The SRC line:** the right half of the FIG line, "SRC: OUTLET · MON YYYY", JetBrains Mono 500 caps, `mute`, right-aligned
  at x 1016, y 232, present from the card's first frame (no fade). It names the real source the script cites, or the
  creator's handle when the figure is their own. A card with nothing true to name carries no SRC; never invent one.
- **Figure numbering:** "FIG. nn" left of the line, `primary`, two digits, from 01 upward in order (`citations.figure_numbering`).
- **Source cards:** P-09 quote notes (the real post, the creator's screenshot or captured from the web, framed by
  `fx.shot`; else `fx.quoteCard` with the exact words). An article's headline is quoted exactly (`fx.headlineCard` in the editorial theme:
  a cream card, an ink serif headline, a `primary` marker highlight on the spoken phrase).
- **Plates:** names and roles on portraits (P-07) in mono.
- **Verdict stamps:** only "✓ PASS" / "✓ FIXED" (`good` / `accent`) and "✕ ERROR" (`bad`) pills.
- **F-B:** no SRC lines; quotes still carry the name and the attribution.

### 8.7 Assets
- **Real captures first** for the creator's own product: screen recordings (SH-2) in P-45.
- **A real product shown by name** is the real one: the creator's capture, else the real page captured from the web.
- **Mocks** are generic and unbranded (`fx.appUI`, `fx.device`), never a look-alike of a real product.
- **No stock, no film clips, no memes, no AI people.** v03's film clip and its illustrated clerk aren't copied; the P-31 icon
  slab or the P-36 cycle does that job.
- **Logos:** the creator's files first, else the real logo fetched from the web; P-46 type plates only when none can be
  found.
- **Third-party moments:** fetch the real thing, source noted (§12.4).
- Comedy layer: off (`tone.comedy` off). No reaction bank, no meme cues.

---

## §9 Transition system

### 9.1 Library
| ID | Transition | Frames | Recipe | SFX role |
|---|---|---|---|---|
| **T-01** | **Hard cut** | 0 | A stage or scene swap on a word boundary ±1 f (`via: "cut"`, scene `cuts`). Graphic → graphic: the new card is complete on the cut frame (no camera move; v01 0:38.70). Graphic → presenter: always with the Z-1 / Z-2 settle (§10.2) | a light whoosh or tap from the pool, sparingly |
| **T-02** | **Card skew-in** | 6 | The hook window card settles from a perspective tilt (rotateY −10°, rotate −4°, scale 0.94 → 1), expo-out (v02 0:00–0:00.24). Hook only (brutal) | pop |
| **T-03** | **Push** (pinksage) | 9 | The current card exits left (x 0 → −1080, ease-in) while the next element enters from the right (x +1080 → 0, expo-out), the same frames, no fade (v03 0:09.80–0:10.12). Scene presets `out: "slide-l", out_frames: 9` on the old card / `in: "slide-r", in_frames: 9` on the new one (not the built-in `push` transition: that moves the world too, and here the pink world stays put) | swish |
| **T-04** | **Evolve** | 5 | Same card, next state: the hero numeral dims to ≈ 20% with a 4 px blur in 5 f while the portrait scales 0.2 → 1 with a fade in 4 f, no overshoot; its name fades in 4 f later (v01 0:21.00–0:21.45) | none, or a pop |
| **T-05** | **Slab slide** | 12 | The F-A title slab: line 1 from the right, line 2 from the left, horizontal blur (§5.2). Editorial hook only | the hook hit |
| **T-07** | **Iris wipe** (brutal) | 8 | A section change: a `primary` disc grows from the frame centre to cover the frame, then a `card` / world-coloured disc grows inside it; the PiP bubble stays on top; the new section's content starts after (v02 0:06.13–0:06.41, 7 f @25). Built in: `{"t": <cut>, "type": "iris", "reveal": "open", "at": "centre", "frames": 8, "ring": 200, "colour": "primary"}` (the new frame opens in a circle led by a thick 200 px `primary` band: the measured orange disc lagging ahead of the cream one). The old frame is shown frozen under it, so start the next section's scenes on the cut | whoosh |
| **T-08** | **Grow-in / shrink-out** (brutal) | 6 (out 2) | Card → card inside a section: the old card shrinks and fades out in 2 f; the new window grows 0.25 → 1 with its fill flashing `primary` → `card` and a −5° → −2° roll, expo-out, 6 f (v02 0:18.16–0:18.40, 0:29.26–0:29.42). Old card `out: "pop", out_frames: 2`; the grow-in stays bespoke (its fill flash and roll aren't a preset) | pop |
| **T-09** | **Flash-in** (pinksage) | 6 | A new card appears as a flat white panel, then its fill and content fade up to their colours in 5–6 f; a follow-up card lands overlapping it lower (a deck stack) (v03 0:03.34–0:03.90) | tap |
| **T-10** | **Blank beat** (brutal) | 6 | After a hard cut from footage or a screen recording, the empty world holds ≈ 6 f before the next card's slam (v02 0:27.04–0:27.30) | none |
| **T-06** | **Hard end** | 0 | Cut to nothing ≤ 6 f after the last word | — |

No dissolves, light leaks, zoom-throughs or glitches (the engine's `glitch` transition exists, but none of the three reels
uses one, so it stays out). T-02, T-07, T-08 and T-10 are brutal-only; T-03 and T-09 pinksage-only; the editorial pack uses
T-01, T-04 and the T-05 hook slide only. A new move is welcome when it's built in the active pack's own language.

### 9.2 Grammar
| Boundary | Use | Never |
|---|---|---|
| Frame 0 | The figure already moving + T-05 (F-A) / the ticker already ticking (F-B) | A fade-in, a black frame |
| Hook → body | T-01 to the first L-graphic card on the second clause | A morph |
| A new idea / card | T-01 (editorial); T-08 or T-01 (brutal); T-09, T-03 or T-01 (pinksage) | A crossfade |
| A new section (F-B brutal) | T-07 iris wipe, then the slug lockup | A second iris inside the same section |
| The same idea continues | T-04 evolve | A hard cut mid-sentence |
| To the presenter | T-01 to L-stack (+ Z-2) / L-full (+ Z-1), every time | The `pop-back` / `grow-from-card` morphs; a cut to footage without the settle |
| A new list item (F-B) | T-01 to the P-39 numeral card on the ordinal word | Anything with a lead over 2 f |
| A number lands | An internal event (a counter landing, a bar topping out) | A camera shake |
| CTA | T-01 to L-full + Z-1, then P-48 | — |
| The last word | T-06 | A black tail > 0.2 s |

### 9.3 Shot grammar (spine `hybrid`)
The A-roll carries the voice, but the picture is chosen per idea: cuts land on sentence starts, not on the presenter's
gestures.
- R-1 Cut on the first content word of a sentence (±2 f), never inside a word or a name.
- R-2 A presenter run lasts as long as its claim. The full face holds an opinion, never a paragraph; the stack holds a
  comment on its figure; the bubble holds while its section header and window carry the story; the card-over-head holds one
  proof.
- R-3 Jump cuts inside the A-roll (dead air removed) happen *under a graphic* whenever possible. On an L-full run each jump
  cut gets the next settle, alternating Z-1 and Z-2, so the jump reads as intentional.
- R-4 A claim, pain or CTA sentence starts on L-full (+ Z-1) when the face hasn't been seen for a while.
- R-5 A return to the face looks different from the last one: a different layout, or the other settle.

### 9.4 How the moves breathe
- **The hard cut is the rhythm itself:** runs of hard cuts are the style, and they never feel repetitive because every one
  lands on a new picture. The designed transitions are accents of their pack: the iris marks a new chapter, the grow-in a
  new card inside a section, the push and the flash-in the pink-sage alternation.
- **The blank beat is a held breath:** it only works because it's rare, so save it for the moment after a screen recording
  when the next slam deserves a gasp.
- **Evolves keep an idea alive** without a cut: the same card, the next state, when the next sentence continues the idea.
- Cuts sit within ±1 f of word boundaries; the audio is never offset.

The transition map, part of the plan (example timings from a 75 s F-A reel):
```yaml
transitions:
  - {t: 0.00, id: T-05, to: L-stack, note: "title slab slides in; figure already rolling"}
  - {t: 1.64, id: T-01, to: L-graphic, note: "FIG. 01 on 'by'"}
  - {t: 6.26, id: T-01, note: "FIG. 02 on 'This'"}
  - {t: 9.00, id: T-01, to: L-full, camera: Z-1, note: "presenter on 'which is the formula'"}
```

---

## §10 Motion tokens, camera and zoom, layers, finishing

### 10.1 Motion tokens (30 fps)
| Token | Value |
|---|---|
| Beat lead | 2 f before the onset |
| Card entry (B-1) | **0 f**: the F-A card is complete on the cut frame (`in: "none"`); later elements pop or fade in 4–5 f on their words; draws 10–14 f |
| Window skew-in (B-2, hook) | 6 f, expo-out, rotateY −10°, rotate −4°, scale 0.94. Body windows use the T-08 grow-in (6 f) |
| Slab slam (P-31, window title slabs) | 5 f: scale 1.8 → 1, roll −8° → the slab's resting −3°, ease-in, no overshoot: `in: "stamp", in_frames: 5` (v02 0:18.53, 0:27.50: 4–5 f @25) |
| Header line rise | 4 f per line behind a clip line, expo-out; line 2 ≈ 10 f after line 1 |
| Blur-in (word stack, CTA words) | 4 f: `in: "blur", in_frames: 4` (measured 3 f @25) |
| Cut-in settle (Z-1 / Z-2) | 20 / 22 f, `ease: "expoOut"`, half the zoom gone by f4; Z-1 also rolls 4° → 0 (§10.2) |
| Pop (chips, nodes, portraits) | `in: "pop", in_frames: 4`: 0.6 → 1.06 → 1.0 in 4 f (chips overshoot one frame; portraits none). F-B numerals fade + settle 1.06 → 1 in 6 f (v03 0:06.53–0:06.73), no pop |
| Slab slide | 12 f, x ±540 → 0, horizontal blur 14 → 0 px |
| Typing | 1 char / 2 f (label boxes, the comment sheet); 1 char / f (title windows, the horizon label); 22 chars / s (terminal, code lines) |
| Counter roll | 18 f ease-out to each step (F-A); tickers step +1 every **4 f** without easing (F-B, E6) |
| Bar grow | 14 f expo-out, 3–6 f stagger |
| Ring draw | 6 f per ring |
| Particle drop | 1 dot / 6 f, a 10 f ease-in fall, seeded |
| Evolve | 5 f |
| Comment sheet rise (P-50) | `in: "rise", in_frames: 7` (measured 6 f @25) |
| Exit | None on a hard cut; T-08 shrink-out `out: "pop", out_frames: 2`; T-03 push `out: "slide-l", out_frames: 9`; fades only at the end of the comment sheet (4 f) |
| Hold | Titles ≥ 10 f after complete; text ≥ 0.25 s / word; a card as long as its idea (§7.3) |

Counters roll eased in F-A (premium) and tick linearly in F-B tickers (v03 looks mechanical on purpose). The linear tick is
an E6 hard swap inside a fixed box, so nothing jumps.

### 10.2 Footage camera (`zoom_policy: crop_on_cut`): the cut-in settle
Measured at 25 fps with ORB between consecutive frames: **every** hard cut to presenter footage lands zoomed in and eases out
to rest; graphic → graphic cuts carry no camera move (scale 1.000).

| ID | Preset | Recipe (30 fps) | Use | Evidence |
|---|---|---|---|---|
| **Z-1** | `pull-out` | On the cut frame the footage is at **1.26** and eases out to 1.0 over **20 f** (expo-out: 1.26 → 1.16 by f2 → 1.10 by f5 → 1.04 by f12); 1–2 f of motion blur come with the speed. The source also rolls **3–6°** back to 0 over the same frames. Preset: `scale [1.26, 1.0]`, `frames 20`, `ease: "expoOut"`, `rotate: [4, 0]` (the measured median; per event `p.rotate: [3..6, 0]`, sign as shot), `blur: {kind: "radial", amount: 0.1, at: "face", frames: 2, shape: "decay"}` | Every cut to L-full | v01 0:09.00 (1.24, roll 5.9°), 0:26.40 (1.26, 4.2°), 1:05.96 (1.27, 3.5°); v03 0:02.00 (1.32), 0:21.20 (1.24), 0:29.20 (1.18) |
| **Z-2** | `pull-out-wide` | **1.40** → 1.0 over **22 f**, the same curve (`ease: "expoOut"`, the same 2 f radial blur), no roll; the L-stack graphic band settles with it inside its own scene (G-2) | Every cut to L-stack and the hook; an L-full cut that follows another L-full cut | v01 0:00 (1.53), 0:13.72 (1.49), 0:45.12 (1.35), 1:02.84 (1.52), 1:11.92 (1.38) |

The settle starts only on a hard cut (±2 f of the stage change) and only ever zooms **out**: the camera steps in to listen,
then gives the creator room. Nothing else moves the camera, and graphic → graphic cuts never settle. On back-to-back face
cuts, alternate the two settles so the camera feels alive. A 1080p source starts at ≤ 1.40× (its first frames are soft and
motion-blurred, as in the evidence).

### 10.3 Tone decides the treatment
| Tone | Role colour | Camera | Layout |
|---|---|---|---|
| `claim` | `primary` | `pull-out` (Z-1) | L-full or L-stack |
| `explain` | `accent` | — | L-graphic |
| `proof` | `primary` | — | L-graphic or L-stack |
| `warn` | `bad` | — | L-graphic |
| `win` | `good` | — | L-graphic |
| `cta` | `accent` | `pull-out` (Z-1) | L-full |

The canvas camera is off: ideas change by hard cut, not by camera travel (D5).

### 10.4 Layer order (back to front)
1. The world (W-main / W-alt / W-dark / W-promo) + the P-51 decor band (z1)
2. —
3. The card / figure (z3), one per frame
4. Presenter footage (the stack's bottom band, the bubble, full frame): the stage layer
5. Labels drawn outside a card (rare; prefer inside)
6. Marker overlays (z6)
7. CS-1 captions (z7)
8. Word stack, keyword card (z8; captions hidden)
9. —
10. The F-B header lockup, the F-A title slab (z10)

### 10.5 Finishing
- **Editorial:** film grain 0.06 and vignette 0.30 on W-main (world tokens); soft glows only on the spheres of P-04, the ring
  dot of P-03 and the timeline dot of P-08.
- **Brutal / pinksage:** no grain on cards (the pink world carries grain 0.05); **hard offset shadows only** (no blur) on
  cards, windows, chips, numerals and ticker values; no glows.
- Footage is untouched (no grade), except the halftone treatment on portrait photos (§4.4).
- Card radius: windows 14, F-A cards 18–24, chips 30, pills 10.

---

## §11 Sound

Sound comes from the bundled SFX pack (catalogue ids only) and its global rules: every cue marks a visible event, no file
more than twice, one list cue, no cue repeated back to back. Sound is sparse here: the cut is the beat, and a cue only marks
a landing.

| Line | Decision |
|---|---|
| **Cue moments** | `hook` (the f0 hit, the first value landing); `transitions` (light whooshes or taps on hard cuts between ideas, never one on every cut; a whoosh on every T-07 iris and T-03 push; a pop on a slab slam); `reveals` (counter landings, bars topping out, ✓ PASS, the numeral card); `list_cue` (one file for every numeral card); `cta` (the keyword pop, the sheet rising). A ticker run gets **one** tick-run cue, never one per step |
| **Meme cues** | Off (comedy off) |
| **Music bed** | On, from **f0**, under the whole reel (unverified: the source audio wasn't observable) |
| **Ducking** | The bed sits ≥ 18 dB under the voice while the voice speaks; source clips (P-47) keep their own audio, ducked under the voice |
| **Loudness** | −14 LUFS integrated, true peak ≤ −1.5 dBTP; a hard end ≤ 6 f after the last word |

---

## §12 Footage handling

### 12.1 Setups
| Setup | Spec |
|---|---|
| **A: seated or standing vertical take** | 9:16 at ≥ 1080 × 1920, ≥ 30 fps (conformed to 30 CFR), chest-up framing, eyes at 38–42% of frame height, head top at y 260–420; a plain or bright backdrop (a printed sky, a colour wall, plants), a soft key; a lav or a handheld mic may be in shot (v02 holds one); a plain dark or mid-grey tee |

The source presenters sit in front of a printed sky with a rainbow arch (v01, v03) or on a sofa against a blue wall (v02).
Neither is required: any clean backdrop works, because the presenter is framed small or in a band. The arch is their set,
not a graphic; don't reproduce it.

### 12.2 Shots and fallbacks
| ID | Shot | Spec | Must / optional | Formats |
|---|---|---|---|---|
| **SH-1** | The talking-head take | Setup A, one continuous take or a few takes of the script | **must** | F-A, F-B |
| SH-2 | Screen recordings of the creator's own product, tool or workflow | 1080 px wide or more, 4–10 s each, cursor visible, no private data | optional | F-B |
| SH-3 | A source clip (interview, keynote, press clip): the creator's, else the real one fetched, source noted | 2–4 s, the person or event the claim is about | optional | F-A (HA-18) |
| SH-4 | Portrait photos of the people named in the script | ≥ 600 px, face centred | optional | F-A, F-B |
| SH-5 | 3–6 thumbnails or stills of the creator's own content or event | 9:16 or 4:5 | optional | F-B (P-49) |

| ID | For | What the engine does instead | Cost | Result |
|---|---|---|---|---|
| FB-2 | SH-2 | The real page captured from the web in a P-45 window; else `fx.appUI`: a recreated generic window (chat, terminal, list, browser) built from the script's words | no real UI texture | holds |
| FB-3 | SH-3 | No real clip to be found: open on HA-07 instead of HA-18; the person's words go on a P-09 quote note (the exact spoken quote) | loses the "someone else said it" authority beat | holds |
| FB-4 | SH-4 | The real portraits fetched from the web; else `fx.silhouette` portraits with the name and role in mono labels | no faces | holds |
| FB-5 | SH-5 | Typographic tiles (the deliverable title split over 3 cards) on W-promo | no product imagery | holds |

SH-1 has no fallback: without a presenter take, use a voice-over style instead.

### 12.3 Props, the cut-out, resolution
- Props: none. Reaction bank: none (no comedy layer).
- Cut-out: **none** (no behind-the-person layer, no depth sandwich).
- Minimum source resolution: 1080 × 1920 (the Z-2 settle starts at 1.40×; its first frames are soft and motion-blurred, as
  in the evidence).

### 12.4 Third-party moments: fetch the real thing
When the script names a real person, post, article, product, brand or clip, the viewer should see the real one. In this
style they're usually: a named person (P-07 / P-24), someone's public words (P-09), a product or tool's UI (P-45), a brand
or tool name (P-46), a source clip (P-47), and thumbnails showing other people (P-49).
1. **The creator's own files** in their folder come first.
2. **Otherwise search the web and fetch it:** the real portrait, the real post, the real page (captured and framed on the
   part that matters), the real logo, the real clip. Note where it came from; the F-A SRC line names it.
3. **Use it as it is** (crop, frame, halftone portraits, highlight a field); never alter it to say something it doesn't. A
   post or headline is shown word for word.
4. **Nothing usable to be found:** rebuild it from its exact words with the pattern named in §8.3 (B-6): `fx.silhouette`,
   `fx.quoteCard`, `fx.appUI`, `fx.logoPlate`, typographic tiles. Rebuilt quote cards quote the script word for word. No
   credit lines on anything made up or recreated.

### 12.5 Frame rate and audio
30 fps CFR output, 1080 × 1920, BT.709. One voice track: high-pass 80 Hz, de-ess, light compression, −14 LUFS.

---

## §13 What your plan should settle

Your `ideas.md` is a page or two, for you. In this style it has decided, before any code:
1. **The format and the theme**, and why (§1, §4.3), written in the reel header with the hook archetype, the structure, the
   list count (F-B), the keyword and deliverable, the FIG numbers in order (F-A), and the sponsor if any.
2. **The hook:** the archetype, the live number and its first landing (by 1.0 s), the result number (by 6.0 s), the slab or
   header with its two alternates, every hook beat to the frame.
3. **Every idea's figure:** the pattern, the world, what's on it in px, its events on their words, its FIG number and SRC
   (F-A), its `caption_cy` (pinksage), and whether it's a new card or an evolve.
4. **The numbers:** a figure for every number, with provenance, formula, steps and `scale_id`; anything that disagrees with
   the script flagged.
5. **The cut map:** every hard cut on its word, every layout change and its settle (Z-1 / Z-2), every pack transition, the
   F-A turn beats, the F-B mid CTA.
6. **The inserts** (the creator's / fetched, with the source / rebuilt) and the fallbacks used.
7. **The sound:** the cue moments, the list cue, the bed's entry.
8. **The CTA:** the device, the keyword card, the promo and title windows, the comment sheet.
9. **The moments you'll look at hardest on the storyboard:** f0 (the thumbnail: the figure moving, the slab or ticker readable at 25%); the
   first value landing (≤ 1.0 s); every L-stack frame (the pill clear of the band's text and of the head; the slab above the
   pill); one card per layout used; one numeral card (F-B); the L-cardtop card against the hair; the CTA keyword card
   against the chin.

How decided one beat is (in `timeline.json` it becomes a beat, its scenes and its cues):
```yaml
- id: 4
  section: FIG-02                      # F-A: HOOK | FIG-nn | TURN | CTA ; F-B: HOOK | PRODUCT | ITEM-n | CTA-MID | BENEFIT | CTA-END
  t0: 6.26
  t1: 8.90
  spoken: "This was a nine-loop scattering amplitude problem,"
  trigger: {word: "nine-loop", at: 7.10}
  tone: explain
  layout: L-graphic
  world: W-main
  visual: "FIG. 02 SCATTERING AMPLITUDE: rings add one by one around a centre numeral that counts 1 → 9; the formula label appears on 'amplitude'"
  layers: [fig02-rings]
  pattern: P-03
  figure_id: loops
  caption: {profile: CS-1, overrides: []}
  source: {masthead: "ANTHROPIC", date: "SEP 2026", headline: null}   # the real source behind the SRC line
  insert: null                         # {id, origin: creator | fetched | rebuilt, source} when a third-party moment is shown
  exception: E6                        # the numeral steps inside a fixed box
  sfx: [{id: "<catalogue id>", on: "fig02-rings@0.84", why: "ring 9 lands on 'nine'"}]
```

One hook, fully decided:
```yaml
- name: "Live grid: 9 in 10 lost"
  archetype: HA-07
  headline: {kind: plate, lines: ["INDEX FUNDS", "BEAT 9 IN 10"]}
  hook_pair: {claim: "Nine out of ten fund managers lost to an index fund", number: "90 of 100 (script)", figure: P-12}
  captions: {profile: CS-1, first_chunks: ["Nine out", "of ten", "fund managers"]}
  storyboard: "f0 stack: 10x10 grid filling red, counter rolling | 0.5 counter lands 90 on 'ten' | 1.7 cut FIG. 01 full grid + FIFTEEN YEARS micro | 4.3 FIG. 02 fee bars"
  sound: [hook hit f0, reveal on 0.5 landing, transition 1.7]
  stopper_test: {thumbnail: pass, mute: pass, read_s: 1.0, payoff_s: 0.5}
```

---

## §14 Worked examples

Times are planning estimates: take the real ones from the words. The numbers are the script's: in a real reel each comes
from the script, the creator or a cited source. They show the standard; match it, then beat it.

### 14.1 F-A editorial, finance: "Index funds beat 9 in 10 fund managers" (≈ 62 s, TH-editorial, HA-07)
**Spoken hook:** "Nine out of ten professional fund managers lost to a simple index fund over fifteen years… and the index
fund charged almost nothing."
**Headline (plate):** "INDEX FUNDS / BEAT 9 IN 10".

| t (s) | Spoken | Layout | Visual | Caption | Cue |
|---|---|---|---|---|---|
| f0 | — | L-stack + Z-2 | Top band: P-12 grid (10 × 10, y 160–620) filling `bad` cells, counter rolling from 0; title slab line 1 sliding in at y 690 | "Nine out" above the seam | hook hit |
| 0.5 | "…of ten" | — | Counter **lands 90** (figure `share_lost`), 90 cells red, 10 cells `accent` | "of ten" | reveal |
| 0.9 | "professional fund managers" | — | Micro label "FUNDS THAT LOST" pops over the grid | words | — |
| 1.7 | "lost to a simple index fund" | **cut** L-graphic | FIG. 01 "THE SCORECARD" · SRC: the report named in the script; the full 10 × 10 grid, the 10 winners pulse `accent` | pill 1390 | transition |
| 3.0 | "over fifteen years" | — | A P-08 timeline under the grid draws 15 years | — | — |
| 4.3 | "and the index fund charged almost nothing" | cut | FIG. 02 "WHAT THEY CHARGE": P-15 bars 1.00% (`G-old`) vs 0.05% (`G-new`), one scale | — | transition + reveal |

| Section | t | Spoken gist | Layout | Pattern | Figure / FIG |
|---|---|---|---|---|---|
| Act 2 What it is | 6.8–12 | "An index fund just buys every company in the market…" | L-graphic | P-13 node map: 9 company nodes joining one basket node | FIG. 03 |
| | 12–15 | "…so it never has to guess." | L-full + Z-1 | presenter (turn) | — |
| Act 3 Stakes | 15–20 | "A 1% fee sounds tiny." | L-graphic | P-06 hero numeral "1%" → dims (evolve) | FIG. 04, figure `fee_active` |
| | 20–26 | "On $10,000 over 30 years it costs you about $17,600." | L-graphic | P-05 bar climb by decade (two series, one scale) → P-06 "$17,628" | FIG. 05, figures `end_active`, `end_index`, `gap` |
| Re-hook | 24–27 | "But here's what nobody tells you." | L-full + Z-1 | turn beat | — |
| Act 4 How | 27–40 | "Managers trade more, pay more tax, and charge for it…" | L-graphic | P-10 run log of trades (generic) → P-11 "✕ GUESS" → "✓ MARKET" | FIG. 06, 07 |
| | 40–44 | "It's not that they're bad…" | L-stack + Z-2 (FIG. 07 in the band) | P-42 | — |
| Act 5 Proof | 44–52 | "Over 15 years, 90 lost, 10 won." | L-graphic | P-15 compare bars (lost vs won, one scale) + ✓ marker | FIG. 08 |
| Re-hook | 49–51 | "Now, this isn't a guarantee." | L-full + Z-1 | turn | — |
| Act 6 Meaning | 51–58 | "It's history, not a promise…" | L-graphic (W-alt) | P-19 horizon "PAST ≠ FUTURE" | FIG. 09 |
| | 58–62 | "…what changes is who you pay." | L-stack + Z-2 | P-18 slider matrix (guessing → market, high fee → low fee, active → passive) in the top band | — |
| CTA (optional) | last 2.5 s | "Comment KEYWORD for the fee checklist." | L-full + Z-1 | P-48 → P-50 | — |

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
(`end_active` ≈ $57,435, `end_index` ≈ $75,063, `gap` ≈ $17,628; the script says "about $17,600" for the rounded caption; the
card shows `$17,628` from the figure.)

### 14.2 F-B brutal, fitness: "A 12-week strength program built by two physios" (≈ 46 s, TH-brutal, HA-02, keyword KEYWORD)
**Spoken hook:** "This program was built by two physiotherapists. Everything, from the warm-ups to the progressions."
**Header (lockup):** `// who_we_are` "TRAIN WITH / PHYSIOS."

| t (s) | Spoken | Layout | Visual | Caption | Cue |
|---|---|---|---|---|---|
| f0 | "This" | L-pip | The bubble top-right (ring `primary`); the slug pops; header line 1 rising; the P-20 window "12-WEEK / STRENGTH." skewing in (6 f) with the chip "home or gym"; the P-51 decor band | "This" pill (red) | hook hit |
| 1.0 | "program was built" | — | Chips pop on the card edge: "12 weeks", "3x a week" | words | pop |
| 1.8 | "by two physiotherapists" | — | Header line 2 has risen; the window title is readable (**the proof by 2.5 s**) | — | — |
| 2.6 | "Everything, from the warm-ups" | T-07 iris | The window swaps to "program.exe" with P-23 tiles (warm-up, strength, mobility, deload); slug `// what_you_get`, header "EVERY SET / PLANNED." | — | whoosh |
| 5.6 | "to the progressions" | — | The cursor taps the "progression" tile | — | tap |

| Section | t | Spoken gist | Layout | Pattern | Figure |
|---|---|---|---|---|---|
| PRODUCT | 6–9 | "It took us 18 months to test it on 200 clients." | L-cardtop | P-25 stopwatch → a calendar variant "18 MONTHS" + the chip "200 clients" | `months`, `clients` (creator) |
| ITEM-1 | 9–10.4 | "One: strength that lasts." | L-graphic | P-39 numeral "1" + the label "Strength that lasts" | — |
| | 10.4–14 | "Three sessions a week, 40 minutes each" | L-graphic (W-alt) | P-35 play grid counting sessions → "36 SESSIONS" | `sessions = 3 × 12` (`sum` / creator) |
| ITEM-2 | 14–15.4 | "Two: no more guessing" | L-graphic | P-39 numeral "2" + "No more guessing" | — |
| | 15.4–19 | "The app tells you when to add weight" | L-graphic (W-dark) | P-45 the creator's screen recording (else an `fx.appUI` list) | — |
| CTA-MID | 19–24 | "Comment KEYWORD and I'll send you the free week-one plan" | L-full + Z-1 | P-48 keyword card → P-49 promo "FREE · PLAN" → P-41 title window "Week One: Strength Basics" | — |
| BENEFIT | 24–38 | "If you're over 35… you don't need a gym… 3 sessions, 40 minutes…" | L-graphic | P-31 icon slab "IF YOU'RE / OVER 35" → P-34 media fan (videos, plans, check-ins) → P-40 highlight stat "40 MIN · 3× A WEEK" | `minutes` |
| | 38–42 | "These are not random workouts." | L-full + Z-2 | presenter | — |
| CTA-END | 42–46 | "Comment KEYWORD and I'll see you inside." | L-full + Z-1 | P-48 → P-50 comment sheet | — |

### 14.3 F-B pinksage, finance: "Your subscriptions are eating your salary" (≈ 42 s, TH-pinksage, HA-07, keyword KEYWORD)
**Spoken hook:** "If your subscriptions keep climbing every month, you probably need a money audit."

| t (s) | Spoken | Layout | Visual | Caption | Cue |
|---|---|---|---|---|---|
| f0 | "If" | L-stack + Z-2 | Top band: the P-27 ticker card ("Monthly Subscriptions" header strip, y 140–730), rows "Streaming – $", "Apps – $", "Cloud – $" (names set in type), values ticking every 4 f | "If your" above the seam | hook hit |
| 0.8 | "subscriptions" | — | The first step lands: streaming reaches $18 (a figure step at the word) | — | tick-run cue |
| 0–2.1 | "keep climbing every month" | — | Rows climb in sync to $45 / $62 / $38 (script / creator values) | — | — |
| 2.1 | "you probably need" | **cut** L-full + Z-1 | P-38 word stack "you / probably / need" | hidden | transition |
| 3.0 | "a money audit" | cut | L-graphic W-main: the P-28 router box "AUDIT" with forks "KEEP" / "CANCEL" | the card's `caption_cy` | reveal |
| 3.4–6.4 | "Here are two things it fixes in a week." | T-09 flash-in (sage) | P-29 tickets (each a subscription) scattering | — | tap |

| Section | t | Spoken gist | Layout | Pattern | Figure |
|---|---|---|---|---|---|
| ITEM-1 | 6.5–8 | "1. The forgotten subscriptions" | L-graphic (pink) | P-39 "1" + "Forgotten subscriptions" | — |
| | 8–13 | "Every charge gets sorted: keep or cancel" | L-graphic (sage) | P-29 tickets fly into the "KEEP" / "CANCEL" bins | `count_cancel` |
| | 13–15 | "Most people cancel three." | L-full + Z-1 | presenter | — |
| ITEM-2 | 15–16.5 | "2. The auto-save rule" | L-graphic (pink) | P-39 "2" + "Auto-save rule" | — |
| | 16.5–20 | "What you cancel goes straight to savings" | L-graphic (sage, T-03 push) | P-36 cycle (charge → cancel → save → invest) | — |
| CTA-MID | 20.5–25 | "Comment KEYWORD and I'll send you the audit sheet" | L-full + Z-1 | P-48 → P-41 title window "The 7-Day Money Audit" | — |
| BENEFIT | 25–36 | "That's $145 a month… $1,740 a year back." | L-graphic | P-40 highlight stat "$145 / MONTH · $1,740 / YEAR" (figure `yearly = 145 × 12`) → P-17 price tag on a laptop outline | `monthly`, `yearly` (`per_period` / `sum`) |
| | 36–39 | "Takes one evening." | L-cardtop | P-25 stopwatch "1 EVENING", ending 40 px above the hair | — |
| CTA-END | 39–42 | "Comment KEYWORD, see you there." | L-full + Z-2 | P-48 → P-50 | — |

---

## §15 Your look at the storyboard: the checklist

Watch it once as a stranger with a thumb over the next reel, then once as the editor whose name is on it. Fix what
bothers you, in one pass.

**The style (does it feel like §The feel?)**
- Frame 0 is a number already moving with the claim readable; the first value lands by 1.0 s, the result number by
  6.0 s; at 25% the slab or ticker still reads.
- Every idea is one complete, literal figure, there on its first word; nothing on any card is decoration.
- Something moves inside every card on the words; numbers roll, tick, grow, fill or draw, never sit.
- Ideas change by hard cut (or the pack's own move); every cut to the face settles out; nothing else moves the camera.
- One pack, start to end; at most three bright hues a frame; old is red, new is accent.
- The caption is quiet: the same height on every graphic frame, a hard swap, no emphasis.
- F-A: the FIG numbers count up from 01, real sources named; the turn beats get the face. F-B: one numeral card per item,
  the keyword said twice.
- Start to end: it feels like a beautifully designed magazine turning its pages on the beat of the voice, the face
  arriving exactly when there's an opinion, and the last figure the biggest.

**Craft (by eye, in context)**
- The guest's face reads whenever they're on: on L-stack the caption ends above the seam and the head stays in its band;
  on L-cardtop the card clears the hair; on L-pip nothing crosses the ring; on L-full the caption, word stack and keyword
  card sit below the chin. Nothing chops the head or buries the face by accident.
- No text over text by accident: the card, the lockup, the caption; L-stack band text clear of the pill, even on the
  settle's first frames; the title slab above the pill.
- Every figure, number, name and object lands on its word; counters land on the spoken number; cuts sit on word
  boundaries; nothing teleports, nothing lingers after its point.
- Every number the creator states is a figure with provenance, recomputed, on one scale where compared, formatted for the
  audience; quotes and fetched posts word for word; illustrations unlabelled; no fake comments, likes or testimonials.
- Names and brands spelt exactly; the promised count = the numeral cards; the keyword readable each time it's said; the
  deliverable title exact.
- Captions on a solid pill you can read on a phone; micro labels small only when redundant; brutal primary text deepened
  to `#DB5320`; pinksage white numerals stroked.
- Meaning text inside x 64–1016, y 110–1500 and out of Instagram's button bands.
- The file itself (1080 × 1920, 30 fps, −14 LUFS, the bed under the voice, a hard end ≤ 6 f after the last word, no black
  tail, the end card ≤ 3.5 s) is the render's job; it checks it.

---

## §16 Build notes

- **Fonts:** Unbounded 900, Barlow Semi Condensed 700, Barlow Condensed 700, Plus Jakarta Sans 600–800, Poppins 600–800,
  Instrument Serif 400 (roman and italic), JetBrains Mono 500–600. Pre-paint $ ₹ ✓ ✕ ↑ ☾ ≈ ×.
- **Scene building blocks** (write them as helpers at the top of `plan/scenes.js`, then reuse them across the reel):

| Block | Role |
|---|---|
| `FigCard` | The F-A card frame: W-main, the FIG line (FIG number + title + SRC) at y 232, the figure zone x 64–1016, y 300–1320, `in: "none"` (P-01) |
| `Counter` | `VEOS.data.counter` in the `numeric` slot: eased 18 f rolls (F-A) or 4 f ticks in a `data-slot` box with `exception: E6` (F-B) (P-02, P-03, P-06, P-12, P-25, P-27, P-35) |
| `Window` | The neo-brutalist window: 5 px `line` outline, hard shadow, title bar, chips inside, skew-in or T-08 grow-in (P-20, P-23, P-30, P-32, P-33, P-41) |
| `Lockup` / `Slab` | The F-B slug + header lines rising from their clip line (P-21); the F-A title slab sliding from both sides (P-37), z10, outside the band's settle |
| `Diagram` | `fx.diagram` nodes and edges in one element (P-13, P-28, P-36) |
| `BandSettle` | The L-stack top band re-laid at y 140–730, scaling 1.40 → 1 over 22 f expo-out about y 520 with `in: "none"` (G-2, P-42) |
| `CTA` | `kind: "cta-keyword"` blur-ins (P-48), the W-promo carousel (P-49), the comment sheet `in: "rise", in_frames: 7` (P-50) |
| Camera and cuts | Z-1 / Z-2 = `timeline.camera` presets `pull-out` / `pull-out-wide`; T-07 = the built-in iris; T-03 / T-08 = scene presets |

---

## Appendix A. Evidence map
The full map (every element → `vNN @ m:ss`), the measured values and the unverified list are in `evidence.md`. In short:
| Element | Source |
|---|---|
| One full-screen figure per idea, hard cuts | v01 0:02 hourglass → 0:06 rings → 0:11 collision → 0:19 numeral → 0:21 portraits → 0:27 quote → 0:31 terminal → 0:39 code → 0:41 grid → 0:45 node map → 0:51 checks → 0:57 bars → 1:03 horizon → 1:07 cost bar → 1:12 sliders |
| Live number at f0 | v03 0:00 billing ticker $37 → $449 by 0:02 (a step every ≈ 0.17 s); v01 the day counter 3 → 7 |
| Cut-in settle (measured per frame) | Z-1 v01 0:09.00, 0:26.40, 1:05.96, v03 0:02.00; Z-2 v01 0:00, 0:13.72, 0:45.12, 1:02.84, 1:11.92 |
| Pill captions, chunk reveal, hard swap | v01 0:01.90, v02 0:00.36, v03 0:03.70; pill cy 1386 (F-A), 1452 (F-B brutal), per card in pinksage |
| Three theme packs, one per reel | v01 dark editorial, v02 cream neo-brutalist, v03 pink and sage |
| Keyword said twice | v02 0:14–0:15 and 0:44; v03 0:21–0:23 and 0:41 |

Not verifiable from the reels: all sound (the bed is inferred), exact font families (closest bundled matches), the ticker
step timing (±1 frame at 6 fps).

## Appendix B. Hook-title bank
`{…}` slots are filled per reel from the script; every number on screen is a figure. Write 8–10 per reel and pick by the
stopper test.

**F-A title slabs (plate, ≤ 5 words, 2 lines, ≤ 16 characters per line)**
| # | Template | Hook | Opening figure | For example |
|---|---|---|---|---|
| 1 | "{SUBJECT} SOLVED / {HARD THING}" | HA-07 | P-02 hourglass of the time it took | "CLAUDE SOLVED / PHYSICS PROBLEM" |
| 2 | "{SUBJECT} BEAT / {N} IN {M}" | HA-07 | P-12 grid of the share | "INDEX FUNDS / BEAT 9 IN 10" |
| 3 | "{RECORD} FELL / AFTER {N} YEARS" | HA-07 | P-08 timeline dot | "THE RECORD / FELL AFTER 14" |
| 4 | "{COST} FOR / {RESULT}" | HA-07 | P-27 ticker or P-17 price tag | "$2,000 FOR / A PROOF" |
| 5 | "{THING} GOT / {N}× CHEAPER" | HA-07 | P-15 compare bars | "AI CALLS GOT / 400× CHEAPER" |
| 6 | "{PERSON} SAID / {IT} WAS IMPOSSIBLE" | HA-18 | P-47 source clip (the creator's, else fetched) | "HE SAID IT / WAS IMPOSSIBLE" |
| 7 | "{N} DAYS / NONSTOP" | HA-07 | P-02 hourglass | "7 DAYS / NONSTOP" |
| 8 | "THE {N}% / NOBODY SEES" | HA-07 | P-12 grid fill | "THE 1% FEE / NOBODY SEES" |
| 9 | "{OLD WAY} VS / {NEW WAY}" | HA-02 | P-15 bars as proof | "WALKING VS / RUNNING" |
| 10 | "WHY {THING} / COSTS {X}" | HA-07 | P-16 off the chart | "WHY RENT / COSTS MORE" |

**F-B section headers (lockup: `// slug` + 2 lines, ≤ 12 characters per line)**
| # | Slug + header | Hook | Opening figure / proof | For example |
|---|---|---|---|---|
| 1 | `// the_cost` "YOUR BILL / EXPLODED." | HA-07 | P-27 ticker | an AI bill ticking to $449 |
| 2 | `// who_we_are` "LEARN BY / BUILDING." | HA-02 | P-20 window card | a cohort window with 3 chips |
| 3 | `// what_you_get` "{N} REAL / {OUTCOMES}." | HA-02 | P-23 tiles | "4 REAL / PROJECTS." |
| 4 | `// time_spent` "IT TOOK / {N} MINUTES." | HA-07 | P-25 stopwatch | "IT TOOK / 20 MINUTES." |
| 5 | `// use_cases` "{N} WAYS TO / USE {TOOL}." | HA-07 | P-35 count | "2 WAYS TO / USE IT." |
| 6 | `// for_you` "IF YOU'RE A / {AUDIENCE}." | HA-02 | P-31 icon slab | "IF YOU'RE A / MARKETER." |
| 7 | `// the_problem` "{PAIN} IS / COSTING YOU." | HA-07 | P-27 ticker | "SNOOZING IS / COSTING YOU." |
| 8 | `// the_method` "ONE {THING}. / ZERO {OTHER}." | HA-02 | P-20 window card | "ONE SHEET. / ZERO APPS." |
| 9 | `// your_coaches` "LEARN FROM / {EXPERTS}." | HA-02 | P-24 profile fan | "LEARN FROM / BUILDERS." |
| 10 | `// free_class` "{TITLE} / THIS WEEKEND." | HA-02 | P-41 title window | "FREE CLASS / THIS SUNDAY." |
