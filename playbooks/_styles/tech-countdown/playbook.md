# Tech Countdown Style Playbook (template v2)

## The feel

This reel is a premium tech-news desk that turned up in your feed. The first frame already makes a claim and backs it: a
black-and-red plate saying the most exciting part of the event isn't the thing everyone covered, a white proof card under
it, the creator holding the product while its colour flips in their hand. You stop because someone clearly knows
something you don't, and they're about to show you.

Then it shows you. Every tool, feature and number gets its evidence on screen. A giant numeral lands on the cut, white
hash, lime digits, a small italic chip naming it; the tool's logo appears behind the creator's head; then a smear of light
wipes the number away, the room goes soft and dark, and the tool itself fills the middle of the frame, its real screen
changing exactly on the words that describe it. Nobody has to take the creator's word for anything. That is the
authority of this style: proof, not volume.

Inside a beat everything is still and expensive. No shakes, no stickers, no memes. The energy lives in the doors between
beats: a warm light leak flaring white, the camera rushing in from wide as the colour drains away, lime bars swiping a
number into place. Calm room, fast doors. Never the other way round.

The words stay small and quiet, a neat line under the chin or resting just above the split, until one phrase in each
thought blows up into a big white italic serif: the part you'd quote to a friend. That phrase is the reel's voice. Lime
only ever means where you are: the number, the pill, the thing to tap.

It's a countdown, so it keeps a promise. The count said at the start is the count you get, the face comes back for a
verdict on every tool, and the best item comes last and gets the most. Then Save, Follow, the community, and out,
fast and confident.

**The test:** pause on any frame and you can tell which item we're on and what's proving it.

## What this playbook is

You're editing one talking-head take of a creator who covers tools, launches and tech news, and you have the authority to
make it the most trusted, most watchable roundup in their niche. This playbook is the style: how it looks, moves, sounds
and thinks, pulled from three reference reels (v01 a keynote recap counting up #01→#10, v02 a one-story "Day 60" brief,
v03 a "Week 09" tools countdown #10→#01), measured at full resolution and full frame rate, then sharpened. Read it all,
every time. Use it the way a great editor uses a reference: take what fits this reel, invent when a moment needs more, and
never ship a frame that breaks the feel above.

**Who it's for and what it needs.** Creators who review tools, features, apps and launches, or brief one tech story a day.
Input: one talking-head take (seated at a desk, or standing), plus, for a countdown, a screen recording of each tool
(SH-1); logos, product B-roll and the creator's own post and clip lift it. Anything missing is fetched from the web (the
real logo, the real product page, the real post), and only what can't be found gets built (§12). Two
formats: **F-A Countdown** (the default: 5–10 numbered items, 90–170 s) and **F-B Daily brief** (one story, no numerals,
70–100 s). The person cut-out is needed only when something stands behind the head (a logo, the Save badge, the link tile,
the tool wheel). Captions follow the creator's language (English, Hinglish or Hindi, set in their copy); chips, cards and
the series card stay in English. Machine values live in `tokens.json`; where this text gives a number tokens also holds,
they agree.

### Style directives (non-negotiable)
| # | Directive | Where it lives |
|---|---|---|
| D1 | **Evidence on screen.** Every tool, feature, number or claim gets its visual: the real recording, a card, a note card or a stat line. Never just a talking head saying a product name | §8, §2 |
| D2 | **Premium calm, fast doors.** No meme layer, no shakes, no stickers, no rotation. Inside a beat everything holds still; the energy lives in the doors between beats: the warm light-leak flash, the rush-in zoom that starts on its cut, the smear wipes | §9, §10 |
| D3 | **Countdown identity.** Every item opens with the same `#NN` ritual; the numbering direction and the count are promised in the intro and paid off | §7.2, §7.3 |
| D4 | **Every sentence is subtitled,** small; exactly one phrase per thought becomes the big italic serif | §5.3 |
| D5 | **Series identity.** A "Day / Week N" card closes the intro; the end stack asks for Save, Follow and the community | §7.6, §6.7 |
| D6 | **One skin per reel.** TH-studio (black pill, white `#` + lime digits) or TH-lime (lime pill, lime hash + white digits); never mixed | §4.3 |
| D7 | **The presenter is the anchor.** Full, split or dimmed under a card, the face is there or one beat away; only the borrowed-post hook leaves it for long | §3.6 |
| D8 | **The number is the re-hook.** Every numeral, teaser chip and italic question is a fresh reason to stay; the viewer is never far from the next one | §7.4 |

### Quick index
| § | What |
|---|---|
| §1 | Procedure: how to approach a reel in this style |
| §2 | Hard rules: the craft and the style's never-list |
| §3 | Worlds W-, layouts L-full / L-split / L-card / L-board, stage moves G-, safe zones, the person |
| §4 | Colour, the two skins TH-studio / TH-lime, grades |
| §5 | Type and captions: the two-line plate, caption profiles CS-1 / CS-1S / CS-2, numerals, chips, cards |
| §6 | Hook system: stopper test, HA-02 default, HA-18 / HA-12 / HA-05 alternates, hook pairs, title writing, CTA and the end stack |
| §7 | Structure and rhythm: F-A / F-B, markers SM-…, the item ritual, open loops, rhythm, series furniture |
| §8 | Visual system (B-roll and patterns): families B-1…B-8, 36 patterns, line → pattern lookup, data and truth, assets |
| §9 | Transition system T-1…T-12 |
| §10 | Motion tokens, camera Z-1…Z-3, layers, finishing |
| §11 | Sound |
| §12 | Footage handling: setups, shots and fallbacks, the cut-out, inserts |
| §13 | What your plan should settle |
| §14 | Worked examples (3) |
| §15 | Your look at the storyboard: the checklist |
| §16 | Build notes |
| App. A / B | Evidence map / hook-title bank |

---

## §1 Procedure: how to approach a reel in this style

You watch, listen, plan, build and look at the storyboard yourself; the edit skill has the mechanics. This style's
craft is two decisions made well: **pairing every item with its proof** (a numeral, a chip, a logo moment and a card whose
screens change on the spoken features), and **picking the one phrase per thought** that the viewer would quote. Make them
in this order.

1. **Pick the format and the skin.** A numbered roundup of tools, features or launches is F-A; one story explained is F-B.
   TH-studio for keynote recaps, feature lists and daily briefs; TH-lime for "tools of the week" roundups. A series keeps
   its skin from reel to reel (§4.3). Numbering runs `desc` (10 → 01, the best last) unless the items are equal features
   of one launch (`asc`, §7.2).
2. **Build the tool inventory** (F-A). Every item in spoken order: its number; the tool's name exactly as the product spells
   it, case included ("MiniMax", "n8n", "Midjourney"), added to the glossary; its recording (SH-1); its logo (SH-3, else
   fetched) or a monogram; a 2–3-word chip label from the script; the 2–4 features said about it, each one a screen swap.
3. **Fetch what's missing** (§12.4): every tool UI, logo, post, clip and headline the reel names that the creator didn't
   give you, from the web, source noted; rebuild from the exact text only when nothing usable turns up.
4. **Feel the tone of every line:** `explain` · `awe` · `warn` · `win` · `cta`. There's no `mock`: comedy is off. The
   tone decides the emphasis treatment (`awe` blur-ins and the slow drift, `warn` the paid chip, `win` the FREE chip).
5. **Pick the hook** (§6) by what the reel has: a product to hold or a proof image → HA-02; a viral post and its clip
   (the creator's own, else the real one fetched) → HA-18; cinematic B-roll of one story → HA-12 (F-B); a roundup whose
   payoff is "free replaces paid" → HA-05. Write 8–10 titles, pick by the stopper test (§6.1), keep two alternates.
6. **Pick the emphasis phrase of every thought.** One phrase of 2–4 words (≤ 22 characters) per thought becomes the big
   italic serif. Prefer the benefit ("completely free"), the twist ("nobody is talking"), the stake ("sell your data"), the
   number with its noun ("in just 60 seconds"). Never a stop-word phrase, never two in one chunk. Write them as
   `captions.overrides` `{i, emph: true}` / `{i, emph: false}` (§5.3).
7. **Pair every item with its card** (F-A): the numeral variant (SM-NUM-A for TH-studio, SM-NUM-B for TH-lime), the chip
   (label, teaser or recap) and its text, the logo moment (the real logo or a monogram), one screen per spoken feature swapped
   on the feature word, the one UI element the cursor box taps, and the pop-back line with its emphasis phrase.
8. **Plan the doors and the breath.** Where the warm washes fall (section breaks in both skins; every item door in
   TH-lime), where the face comes back for the verdict, where the last item escalates, where a long hold earns the slow
   drift.
9. **Settle the series card** (§7.6) from the reel brief (`Day 60`, `Week 09`), or the count-card fallback, and the end
   stack (§6.7). A paid integration gets its disclosure.
10. **Get the cut-out** if anything stands behind the head: P-LOGO-BEHIND, P-SAVE-BADGE, P-DELIVERABLE-TILE,
    P-WHEEL-STAGE (`veos matte --if-needed` after the scenes are written; make sure it's there before the storyboard).
    Otherwise no matte.
11. **Cut the dead air.** Every pause of 150 ms or more comes out, on word boundaries ±1 f; a pause up to 0.6 s may hold
    the last caption chunk instead.

---

## §2 Hard rules: the craft and the style's never-list

**Craft, by eye** (judge it on the storyboard, in context, the way an editor does):
- **Keep the person clear.** The presenter is the anchor, so the head region (face, hair and the room above the head, from
  the cut-out when it exists) reads clear of the front layers when the moment is about them. The framing that does it: on
  L-full the captions ride the chest and the chip's top sits 40 px below the chin; on L-split the caption ends 24 px above
  the seam (y 928), above the presenter's band (§3.6). When a moment wants otherwise (a three-tier caption brushing the
  chin for a beat), that's editing; what's never fine is a head chopped or a face buried by accident. Behind the person is
  fair game, text included (`behind: true`): that's where the logos, the Save badge and the link tile live. L-card is the
  deliberate exception: the presenter is dimmed to a backdrop and the card owns the frame.
- **Letters behind the head stay readable.** A monogram behind the head (P-LOGO-BEHIND, P-DELIVERABLE-TILE) is display type
  ≥ 120 px; for its whole hold ≥ 65 % of its glyph area is visible and its first and last letters are ≥ 50 % visible; one
  at a time; it holds ≥ 0.6 s; the letters' centre sits ≥ 40 px above the head top on the scene's first frame. Such scenes
  set `exception: "behind_text"`. A creator's logo image isn't text and needs only `behind: true`.
- **No text over text.** Captions hide under every z8 scene (numeral, chip, series card, end-card lines) and under the
  plate; a chip never sits over the brand row; never two numerals on screen at once.
- **On the word.** Every numeral lands 2 f before its ordinal or number word and is settled within ±5 f; every tool card's
  brand row lands within ±2 f of the tool's name; every screen swap lands on its feature word ±5 f. Cuts sit on word
  boundaries ±1 f; audio is never offset.
- **Say what was said.** Prices, dates, model sizes and claims come from the script or the creator; a stat line or price
  chip shows the spoken figure exactly; no invented benchmarks, star counts or prices presented as real. Illustrations may
  use made-up but realistic numbers, names and screens, with no label (`illustrative: true`). A real product is shown by
  its real UI (the creator's recording, else captured from the web); created UIs are generic and unbranded, never a
  look-alike of the real product.
- **Promise integrity.** The count said or shown in the intro equals the numerals shown; numbering runs without gaps in one
  direction; a teaser chip's "next NN" equals the items left; every "I'll share the links" is paid by the deliverable line
  and the community card; a comment keyword is on screen ≥ 1.5 s.
- **Spelling.** Every tool and brand exactly as the product spells it, case included. The reference reel shipped
  "elevanlabs": that's a fail here.
- **Numbers formatted for the audience.** International `$1.2M`, `22,000` for English; Indian `₹1,20,000`, `₹2.5 L` for
  Hinglish and Hindi; the currency glyph, never "Rs" or "INR" (§5.5).
- **Readable.** Full-frame captions are 60 px. The seam and card captions are this style's quiet type (E3): 40–53 px
  (default 42), weight ≥ 500, ≤ 3 lines per chunk, ≤ 30 characters a line, contrast ≥ 7:1 on bare footage or ≥ 4.5:1
  inside the pill; labels 32–39 px only when the same word is spoken or shown larger (`redundant: true`); display type
  ≥ 40 px. Text holds ≥ 0.25 s per word, titles ≥ 10 f after they finish building, numerals ≥ 36 f. Meaning text stays
  inside x 64–1016, y 110–1500, and never above y 110, below y 1540, or at x > 970 between y 900 and 1540 (Instagram's
  buttons).
- **Private data.** Emails, keys and personal details in a recording are blurred.
- **Audio.** −14 LUFS integrated, true peak ≤ −1.5 dBTP, the bed ≥ 18 dB under the voice, a hard end ≤ 6 f after the last
  word, no black tail (≤ 0.2 s).
- **Deterministic frames.** Every frame is a pure function of its index; randomness is seeded.

**Never in this style:**
- Meme sounds, stickers, stamps, freeze-frame roasts, emoji in captions or chips.
- Shakes, rotation snaps, whip pans, punch-ins mid-sentence, any zoom that doesn't start on a cut. The only camera moves are
  the Z-1 / Z-2 rush-ins under a wash and Z-3's slow drift (§10.2).
- Raw full-bleed screen recordings over the presenter beyond a glance. Recordings live in the card window, the split top or
  the phone mock.
- Two emphasis phrases in one chunk; emphasis on a stop-word phrase ("and then", "of the").
- Coloured words inside the caption pill. The pill is one colour; emphasis is size and serif, never colour.
- Lime on lime: no lime chip on a CS-2 pill line, no lime text on the lime Link in Bio pill.
- Glowing robot brains, Matrix rain, random stock "AI" footage, hooded hackers. Show the product, the UI or a created
  diagram.
- A redrawn logo or a fake product UI presented as the real one; a fetched post, headline or screen altered to say more
  than it does.
- A brand's colours on anything but that brand's logo (created logo plates stay on the neutral `tile`).
- More than three bright hues in one frame: lime + red + one brand logo at most.
- The plate outside the hook; the series card anywhere but the end of the intro.
- A numeral or tool card the speech hasn't reached yet (no early reveals, except the HA-05 teaser tiles).
- Effect packs: RGB-split, film burns, lens-flare PNGs (the warm leak is this style's own light). A new move is welcome
  when it's built in this style's language.

---

## §3 Worlds, layouts, stage moves, safe zones

### 3.1 Worlds
| ID | Kind | Look | Carries | Enter / exit |
|---|---|---|---|---|
| **W-studio** | footage | The presenter's own room: warm key + practicals (lamp, shelves, plaques), mid-chest framing, never regraded | Claims, opinions, numerals, series card, end-stack lines | Hard cut; dim on/off (8–12 f) |
| **W-void** | void | `#000000` | The HA-18 borrowed-post hook; P-FRAMED-CLIP (a rounded clip on black with italic lines) | Hard cut in; warm wash (T-2) out |
| **W-board** | canvas | Vertical two-stop gradient: TH-studio warm `#E9773C → #F6C9A5`, TH-lime cool `#2F7FD8 → #7FD8E6`, noise 0.03, one soft darker glow blob drifting ±40 px over the hold (v01 @1:14.2–1:14.6) | A full-screen phone or browser mock showing a flow (P-PHONE-BOARD) | **Hard cut in** (v01 @1:14.20); out by **T-12 zoom-through** into the phone's screen (v01 @1:17.68–1:17.93) |
| **W-wheel** | behind-matte stage | The presenter cut out over a radial "tool wheel": a 4–6-segment colour wheel (category names from the script) behind the head, ringed by rows of small app tiles radiating to the edges, on deep purple | The promise beat after the series card (v03 @0:17.4–0:22.6, ≈ 5 s; F-A, TH-lime) | **T-5** in (zoom-through into the wheel); out with radial white speed lines + T-2 |
| **W-endcard** | stage | `#050B06` with a lime dot grid (pitch 26, r 1.6, 10 %), one 620 px lime glow at (540, 520) drifting ±14 px, noise 0.02, vignette 0.35 | The community card (P-COMMUNITY-CARD) only | Warm wash (T-2) in; hard end |

### 3.2 Layouts
| ID | Engine | Presenter | Graphic | Caption |
|---|---|---|---|---|
| **L-full** | `full` | Full frame; head top y 300–460 (setup A) / 220–380 (B); chin ≈ 760–880 (A) / 700–820 (B) | Chest band x 64–1016, y 760–1500 for numerals, chips, note cards, logo pops | `fixed_y` cy **1000** (the layout's caption block, both skins); avoids the head |
| **L-split** | `stack`, seam_y **952**, top `graphic`, bottom `footage` | Bottom band y 952–1920, face centred (eye line ≈ y 1220–1300), no breakout | Top band 0, 0, 1080 × 960: B-roll, recording, created UI, stat line; a 140 px black fade above the seam (y 812–952), no hairline | **`seam_above`, offset 24:** the block's bottom edge 24 px above the seam, at y 928 (CS-1S) |
| **L-card** | `full` + dim | Full frame dimmed: blur 12 px, luma −0.5 (the face still recognisable) | Brand row y 660–720; window x 54–1026, y 740–1280 (972 × 540, 16:9); behind-head logo y 150–560 | `fixed_y` cy **1343** (CS-2 lime pill, or CS-1S in TH-studio, under the card; measured v03 @0:27, @0:50) |
| **L-board** | `hidden` | none | x 64–1016, y 120–1340: phone mock (centred, 600 × 1210) or clip | `fixed_y` cy **960** (the pill sits over the phone's screen, v01 @1:14.3, @1:17.6) |

**When to use which.** L-full is home: the claim, the opinion, the numeral, the verdict. L-split is for the sentence that
names a thing you can show while the face keeps talking under it: a product, an event, a feature list. L-card is the tool
itself: it takes the whole frame for as long as the features are being said, and its screens keep changing. L-board is a
glance: a flow on a phone, a framed clip, then straight back. Switch layouts on a trigger: an ordinal ("number seven",
"next"), a tool name, "look", "here's", a number, or a sentence start.

### 3.3 Stage moves
| ID | Move | Recipe (30 fps) | Use |
|---|---|---|---|
| **G-1** | Cut to split | `via: cut` into L-split on the word; band, seam and the seam caption are complete on the cut frame; the bottom band re-frames the presenter (v01 @0:01.85, @0:25.30) | The default way into a split (nearly every split in the reference) |
| **G-2** | Slide-down split | `via: slide-down`, 9 f | A split entered mid-sentence, where a cut would chop the phrase |
| **G-3** | Dim under card | **T-11 smear wipe** (3 f) carries the numeral out and leaves the brand row + window complete; then `via: dim` ramps blur 0 → 12, luma 0 → −0.5 over **12 f** (v03 @0:24.55–0:24.95) | Into every tool card |
| **G-4** | Undim | Hard cut (default) or `via: dim` 8 f back; the card leaves with the cut | Back to the presenter for the opinion line |
| **G-5** | Cut to board | `via: cut` (v01 @1:14.20); out by T-12 zoom-through | Into a full-screen phone flow |
| **G-6** | Slide-up split | `via: slide-up`, 9 f; a hard cut is the default | Leaving a split when the next beat is L-full |

### 3.4 Layout diagrams
```
L-full                             L-split                            L-card (tool card)
┌──────────────────────┐ 0         ┌──────────────────────┐ 0         ┌──────────────────────┐ 0
│ IG top UI  y 0-110   │           │ B-ROLL / RECORDING   │           │  [LOGO behind head]  │ y 150-560
│                      │           │ top band y 0-952     │           │      (head)          │
│      (head)          │ y 300-460 │                      │           │ ◼ Tool name          │ y 660-720
│      (face)          │           │ ░░ fade 812-952 ░░░░ │           │╭────────────────────╮│ y 740
│   ╭─chip─╮           │ cy 866**  │ ▬ caption ▬          │ ≤ y 928   ││  WINDOW 972 × 540  ││
│ ▬ caption ▬          │ cy 1000*  ├──── seam y 952 ──────┤           ││  recording         ││
│    #07               │ cy 1056** │  (presenter, head    │           │╰────────────────────╯│ y 1280
│  (chest)             │           │   below the seam)    │ eye 1220  │   ▬ lime pill ▬      │ cy 1343
│                      │           │                      │           │  (dimmed presenter)  │
│ IG bottom UI >1540   │           │ IG bottom UI >1540   │           │ IG bottom UI >1540   │
└──────────────────────┘ 1920      └──────────────────────┘ 1920      └──────────────────────┘ 1920
*  a block that would touch the head drops below the chin.
** numeral beats: the chip and SM-NUM-A replace the caption (captions hide under z8); SM-NUM-B sits at cy 1200.
```

### 3.5 Safe zones and bands
- Meaning text stays inside x 64–1016, y 110–1500; nothing meaningful above 110, below 1540, or at x > 970 between y 900
  and 1540.
- **Caption bands:** as §3.2 (measured on L-full: TH-studio's plain pill ≈ cy 960, emphasis blocks centred 1047–1121).
- **Headline band (plate):** line 1 cy 1000, line 2 cy 1078 (both centred on x 540); the proof card y 1100–1500.
- **Numeral band:** chip cy = max(866, chin + 76) (h ≈ 72); SM-NUM-A cy 1056, SM-NUM-B cy 1200, both moving down with the
  chip when the chin pushes it. Nothing else in that band while they show.
- **Series card band:** kicker cy 1000, number cy 1130, sub cy 1250 (all moved down by the same chin shift when the chin
  is below 790).
- **Brand row band:** y 660–720; window y 740–1280.

### 3.6 The person
- **People come for the presenter.** Full, split or dimmed under a card, the face is on screen for most of the reel
  (measured ≈ 80–85 % of the runtime). The one long absence is the borrowed-post hook (HA-18, up to 8 s); anywhere else a
  faceless moment (a board, a framed clip) is a glance, and the face is back within a few seconds. Come back by hard cut,
  undim (G-4) or slide-up (G-6), never by a wash in the body (washes are section breaks and item doors, §9).
- **The head region** is the face, the hair and the room above the head top, from the cut-out when it exists. In front of
  it: nothing, captions included, unless the moment wants otherwise (judged by eye). Behind it: the item's logo, the Save
  badge, the link tile, the tool wheel.
- **L-full** (setup A): head top y 300–460, chin y 760–880 (setup B: 220–380 / 700–820). The caption centres at cy 1000; a
  three-line emphasis block is ≈ 264 px tall (60 + 116 + 60 px lines), so on a low chin the engine drops it below the chin.
  The numeral chip's top edge sits 40 px below the chin (chip cy = max(866, chin + 76)), the numeral under it.
- **L-split:** the presenter's window is the bottom band from the seam (y 952) down, with no breakout, so the head never
  draws above y 952; the eye line sits at y 1220–1300, the head top well below the seam. The caption (CS-1S) is anchored
  `seam_above`: its bottom edge at y 928, 24 px above the window, inside the black fade over the B-roll, never on the
  presenter's band.
- **L-card:** the presenter is a deliberate backdrop, blurred 12 px and darkened 50 %; the engine doesn't treat a dimmed
  face as a reading surface, so the brand row and the window may cross the dimmed chest and chin. The logo behind the head
  stays behind the matte, its top edge ≥ y 140.
- **L-board:** no presenter.
- **Crops:** L-full as shot; jump cuts keep the same crop (measured: 5 of 5 sampled full → full jump cuts change scale < 2 %,
  v01 @0:39.8, 0:44.5, 0:57.1, 1:01.2; v02 @1:08.3). The only crop changes are the Z-1 / Z-2 rush-ins under a wash, which
  land back on the base framing (§10.2).
- **Behind the head** (with the matte): P-LOGO-BEHIND (the tool's real logo, or a monogram), P-SAVE-BADGE, P-DELIVERABLE-TILE and
  the W-wheel; their top edge ≥ y 140, never wider than 560 px (the wheel is a full-frame world).

---

## §4 Colour system

### 4.1 Role palette
| Role | Hex | Its one job | Text on it | Contrast |
|---|---|---|---|---|
| `primary` **Signal Lime** | `#C6FF0C` | Navigation: numeral digits (SM-NUM-A) or hash (SM-NUM-B), the CS-2 pill, the Link in Bio pill, the community headline, the cursor box, teaser arrows | `ink` | 15.1:1 |
| `accent` **Plate Red** | `#E60005` | The plate's second line, the Save badge, the "Comment below" title | `paper` | 4.75:1 |
| `bad` **Paid Red** | `#FF453A` | Paid / risky / the old way: price chips, strike lines | `ink` | 5.8:1 |
| `good` **Free Green** | `#30D158` | Free / works / the new way: FREE chip, ticks | `ink` | 9.8:1 |
| `ink` | `#0A0A0A` | Text on light cards and chips; plate line 1 fill; the CS-1S seam pill (65 %) | — | — |
| `paper` | `#FFFFFF` | White text, chips, note cards, the SM-NUM-A hash, italic emphasis | — | — |
| `tile` | `#1C1C1E` | The neutral glass tile of created logo plates and monograms | `paper` | 17.0:1 |
| `night` | `#050B06` | End-card ground | — | — |
| `canvas` | `#E9773C` | W-board top stop (TH-studio) | — | — |
| `grid` | `#C6FF0C` | End-card dot grid (10 %) | — | — |

Lime and red carry the creator's brand when their copy sets one: a first brand colour replaces lime in both skins (the
CS-2 pill follows `primary`), nudged at copy time to ≥ 4.5:1 against `ink`; a second replaces the plate red. `bad` and
`good` never change.

### 4.2 Meanings
- **Lime = where you are in the reel:** the item number, the call to action, the thing to click. It never decorates.
- **White = the voice:** captions, italic emphasis, chips. Emphasis is never coloured.
- **Red (accent) = the stake:** the plate's second line ("of WWDC-26"), Save, "Comment below".
- **The money axis is `bad` → `good`:** "$22 a month" in a `bad` chip with a strike, "free forever" in a `good` chip. Use
  it only when the script contrasts paid and free.
- **Brand colours appear only inside real brand logos** (the creator's files or fetched). Created logo plates use `tile` +
  `paper`.

### 4.3 Theme packs: one skin per reel
| Pack | Caption profiles | Numeral | Tool window | W-board | When |
|---|---|---|---|---|---|
| **TH-studio** (default) | **CS-1** on full frames: plain-only chunks in a 44 px `ink` pill (hard swap), emphasis chunks bare; **CS-1S** on the split *and* under tool cards: `ink` pill at 65 %, white 42 px | **SM-NUM-A**: white `#` + lime digits, Montserrat 900, inline | Dark window `#111214` with a 2 px `rgba(255,255,255,.14)` border, radius 28 | Warm `#E9773C → #F6C9A5` | Keynote and launch recaps, feature lists, F-B daily briefs (v01, v02). Items enter by hard cut; the warm flash only at section breaks |
| **TH-lime** | **CS-1** bare white 60 px on full frames, typed on character by character (`reveal: "char"`, 50 cps); **CS-1S** on the split; **CS-2** lime pill (`primary`, 100 %), black 42 px, weight 600, under tool cards | **SM-NUM-B**: giant lime `#` behind white condensed digits (Barlow Condensed 700) | White 8 px frame around the window, radius 28 | Cool `#2F7FD8 → #7FD8E6` | "Tools of the week" roundups (v03). Every item enters through a warm leak + rush-in + lime swipe |

- The reel header declares the theme. Captions pick their profile by layout: CS-1 on L-full and L-board, CS-1S on L-split,
  CS-2 on L-card; a TH-studio reel puts CS-1S under its cards. Never mix profiles, numeral variants or window frames inside
  one reel.
- A series keeps its pack: "Week NN of the AI tools" is always TH-lime; "Day NN of future tech" always TH-studio. The
  first reel of a series picks; later reels inherit it (series memory, §7.6).

### 4.4 Grades
Footage is **not regraded** (the reference rooms are already warm); only exposure and white balance are matched between
setups. No grade events, no clip treatments. The only treatments are the L-card **dim** (blur 12 px, luma −0.5) and the
warm leak (T-2, §9).

### 4.5 Rules
- Lime + red + one real brand logo is the brightest a frame gets. The `bad`/`good` pair counts as two: never show it in
  a frame that also has the red plate.
- Coloured text on light worlds (W-board, white note cards) needs a chip: lime text never sits on white; red text on white
  is ≥ 48 px bold (the "Comment below" title).
- On footage, white text carries the soft shadow `0 2 8 rgba(0,0,0,.55)` or sits in a pill.

---

## §5 Type and captions

### 5.1 Font map
| Slot | Family | Weights | Class | Used for |
|---|---|---|---|---|
| `body` | **Inter Tight** | 400 / 500 / 600 / 700 | neo-grotesk sans 400–700 | Caption plain words, brand rows, plate lines, card text, series kicker / sub |
| `serif` | **Instrument Serif** | 400 italic | high-contrast italic display serif | Emphasis phrases, series number, chips, end-card kicker, stat values |
| `display` | **Montserrat** | 900 | heavy grotesk 800–900 (the real `#01` has Montserrat's round `0` and flagged `1`; measured v01 @0:11) | SM-NUM-A numerals, the SM-NUM-B hash, the community headline |
| `numeric` | **Barlow Condensed** | 700 | condensed sans 600–700 | SM-NUM-B white digits |
| `mono` | **JetBrains Mono** | 400 | monospace | Created terminal / code texture inside a card (decorative unless it carries the point) |

All bundled (OFL). Brand logos are image assets (the creator's or fetched), never fonts. Devanagari: `Noto Sans Devanagari`
replaces `body`; Devanagari has no true italic, so the emphasis becomes `Noto Sans Devanagari 700` at the same size
(§5.5).

### 5.2 The headline: the two-line plate (`kind: plate`)
The plate is the reel's hook title in this style: a confident two-line news headline, the setup on black and the stake on
red, with its proof directly under it.

| Property | Spec |
|---|---|
| Line 1 plate | `ink` fill, radius 6, padding 6/18; text `paper`, Inter Tight 600, **62 px**, line height 1.0, tracking −1 %; centred on x 540, **cy 1000** |
| Line 2 plate | `accent` fill (red), radius 6, padding 6/18; text `paper`, Inter Tight 700, **62 px**; centred on x 540, **cy 1078**; usually narrower than line 1 (measured v01 @0:00.6: black plate y 955–1038, red y 1042–1114) |
| Words | ≤ 9 in total, on exactly 2 lines: line 1 ≤ 5 (the setup), line 2 ≤ 4 (the stake: the event, the number, the twist); reads in ≤ 1.5 s |
| Proof card | Directly under the plate, its top edge tucked under line 2 as in the reference: white card x 120–960, y 1100–1500, radius 18, soft shadow `0 18 40 rgba(0,0,0,.35)`; the subject image on the left 45 %, a 2-line counter-claim on the right (Inter Tight 600, 52 px; line 1 `ink`, line 2 `accent`), its text starting below y 1130 |
| f0 | Plate + proof card arrive as **one group zooming in from the viewer**: scale 1.25 → 1.00 over f0–f6 (expo-out) with 8 → 0 px motion blur, cross-dissolving over the presenter; both lines readable from frame 0, settled and sharp by **0.2 s** (measured: a 2-frame pre-roll, then ≈ 2× → 1.0 over f2–f7, settled f8, v01 @0:00.07–0:00.27) |
| Life | The held prop strobes: the product in the presenter's hand flips colour (red ↔ black) every 2–3 f from 0.33 s for ≈ 1 s (v01 @0:00.33–0:01.3; two takes or photos alternated). Without a prop the card's image flips the same way. The plate itself doesn't move |
| Lifetime | The hook only: 2.5–8 s; gone before the first L-split or at the first warm wash |
| Exit | Blur 0 → 12 px + fade over 6 f, or it leaves with the hook beat on a hard cut |
| Text class | `TC-display` (62 px) |

### 5.3 Caption profiles (CS-…)
Three profiles share one mechanic: small plain words, one phrase blown up into italic serif, stacked around it.

| Field | CS-1 **Full frame** (L-full, L-board) | CS-1S **Seam** (L-split; TH-studio cards) | CS-2 **Lime pill** (TH-lime cards) |
|---|---|---|---|
| Mode | every word captioned, support role, mute-safe | same | same |
| Chunking | `unit: phrase`, 2–5 words, ≤ 30 characters a line, ≤ 3 lines (the italic line + plain lines); never split names, numbers or units; a new chunk on punctuation and on pauses ≥ 0.9 s | same | same |
| Timing | lead 2 f; ≥ 0.25 s per word; pause hold ≤ 0.6 s; tail 0.12 s | same | same |
| Swap | **TH-studio:** `hard` (measured v01 @0:01.85, @1:17.95). **TH-lime:** plain lines type on, `reveal: "char"`, `cps` 50 (measured 1.5–2 characters a frame, v03 @0:17.67); the italic phrase blur-pops in 2 f (`blur`, 10 px; v03 @0:17.92). Both skins override the base swap, the measured word-group smear (`smear`, 3 f in / 2 f out, `smear_px` 24, `angle` 0, `stretch` 1.6, `travel_px` 40, `dir: right`; v02 @0:34.77) | `blur` 3 f, 12 px | `blur` 3 f, 12 px |
| Plain words | Inter Tight **500**, **60 px** (measured 62–66 px, v01 @0:05), sentence case, `paper`, shadow `0 2 8 rgba(0,0,0,.55)`, line height 1.12. TH-studio plain-only chunks **44 px** (cap height 32 px, v01 @1:13.95) | Inter Tight 500, **42 px** (measured 40–44 px, v01 @0:02.5), `paper`, soft shadow (E3) | Inter Tight **600**, **42 px**, `ink`, no shadow (E3) |
| Container | TH-lime: **none** (bare). TH-studio: plain-only chunks in an `ink` pill, opacity 0.75, radius 8, padding 4/14 (measured pill y 928–992, v01 @1:13.95); emphasis chunks bare, their plain lines too (`tiers.connector_container_when: "plain_only"`) | `ink` pill, opacity 0.65 (sampled `#5A5A5A` over white B-roll), radius 8, padding 4/14, one pill per plain line | `primary` (lime) pill, opacity 1.0, radius 10, padding 6/16 |
| Emphasis | The chosen phrase in Instrument Serif **Italic 400, 116 px** (measured ≈ 125 px v01 @0:05; ≈ 84 px v03 @2:31), `paper`, no pill, soft shadow; `split` stacking: the plain words before it above, after it below. One per chunk | Italic **80 px** (measured ≈ 76 px, v02 @0:02), bare white on the dark fade | Italic **80 px**; the italic line stays white on footage, never lime |
| Position | L-full `fixed_y` cy **1000** (the layout's caption block; the profile's own cy 1080 applies only on a layout without one, and all four here have one); L-board cy **960**; avoids the head | L-split **`seam_above`, offset 24**: the block's bottom edge 24 px above the seam, at **y 928** (one plain pill ≈ y 873–928; with an italic line the block grows upward into the fade); under TH-studio cards cy 1343 | L-card cy **1343** (measured pill x 321–755, y 1312–1374, v03 @0:27, @0:50) |
| Colour flips | none: CS-1 relies on the soft shadow (keep the chest mid-to-dark; the reference reels shoot dark tops) | none: the pill | none |
| Hide | under z8 scenes (numeral, chips, series card, end-card lines), under the plate, during the T-2 / T-5 / T-6 transitions and stage morphs | same | same |
| Language | Latin script; English product terms verbatim; the speaker's grammar not normalised; profanity masked inside the word; glossary = every tool and brand of the reel with exact casing | same | same |

**The emphasis phrase** is this style's signature craft. Make it the line a viewer would screenshot.
1. 2–4 words, ≤ 22 characters, so the 116 px italic line fits inside 952 px (the engine sets the whole phrase on one
   line). Shorten a longer span with `captions.overrides {i, emph: false}` on the extra words.
2. One phrase per thought. On full frames that's the heartbeat of the caption; in splits and inside cards it comes less
   often, because the picture is already speaking. Inside L-card chunks emphasis stays off unless the phrase is the tool's
   key benefit.
3. Pick the quotable part: the benefit ("completely free"), the twist ("nobody is talking"), the stake ("sell your data"),
   the number + noun ("in just 60 seconds").
4. A question carries its emphasis on its last ≤ 22 characters ("So why does an AI / *company want it?*") and is a re-hook
   (§7.4).
5. Never on stop-words, never on the tool name inside its own tool card (the brand row shows it), never on the CTA keyword
   (it has its own card).

### 5.4 Other text
| Element | Class | Recipe | Hold |
|---|---|---|---|
| **Numeral SM-NUM-A** | TC-display | `#` `paper` + digits `primary`, Montserrat 900, **330–360 px** (digit cap measured 252 px, `#` x 202–488, digits x 494–820, the whole numeral ≈ 618 px wide, v01 @0:11), tracking −4 %, soft shadow `0 10 30 rgba(0,0,0,.35)`; centred on x 540, **cy 1056**; keeps 64 px margins | 1.2–2.0 s |
| **Numeral SM-NUM-B** | TC-display | Lime `#` Montserrat 900, **540 px** (hash measured 394 px tall, x 342–738, y 1002–1396, v03 @0:24), with a darker bevel edge (`#8FB51F`, offset +6/+6) behind; white digits Barlow Condensed 700, **330 px** (digit height 234 px), centred on the hash; **cy 1200** | 1.2–2.0 s |
| **Chip (label / teaser / recap)** | TC-label | `paper` box, radius 4, padding 2/16; Instrument Serif Italic 54 px `ink` (50–56); centred on x 540, cy = max(866, chin + 76) (measured centre ≈ 866) | with the numeral |
| **Series card** | TC-display | "Welcome to" Inter Tight 400 52 px `paper` (cy 1000) / "Day 60" Instrument Serif Italic 170 px `paper` (160–180; cy 1130) / "of future tech updates" Inter Tight 400 50 px `paper` (cy 1250); soft shadow. Built while the T-2 tint is still fading: the kicker **types on** ≈ 1 character a frame from 6 f after the flash (v02 @0:07.45–0:07.58), the number blur-pops in, the sub types on; it leaves under the next wash (v03 @0:17.12) | 1.8–2.2 s |
| **Brand row** | TC-label | Logo or monogram square 80 px (radius 18) + 18 px gap + the tool name in Inter Tight 500 50 px `paper`; left-aligned at x 64, y 660–720 (measured y ≈ 673–690) | the whole card |
| **Note card** | TC-label | `paper` card w 700, radius 26, padding 36/40; optional title Inter Tight 700 48 px `accent`; body Inter Tight 500 44 px `ink`, ≤ 3 lines; a 120 px generic gradient orb (`orb` gradient `#5B8CFF → #B26BFF → #FF6FB1`, never a product's assistant logo) overlapping the top edge by 50 % | 2–4 s |
| **Stat line** | TC-display | Value Instrument Serif Italic 104 px `paper` (96–120) + label Inter Tight 500 44 px `paper` under it; on the split top's lower third (y 640–860) or at chest | 1.5–3 s |
| **Price chips** | TC-label | `bad` chip, Inter Tight 800 48 px `ink`, with a 6 px `ink` strike line drawn L → R over 6 f; `good` chip "FREE", Inter Tight 800 48 px `ink` | 1.5–3 s |
| **Plate** | TC-display | §5.2 | the hook |
| **Disclosure** | small print (`type.legal`) | Inter Tight 500 26 px `paper` at 80 %, at x 64, y 140: "Paid partnership" on a sponsored item | the whole sponsored item (≥ 2 s) |

### 5.5 Language and numbers
- **Spelling:** English captions verbatim; brand and tool names exactly as the product writes them (case included). The
  glossary is the source of truth.
- **Hinglish speech → English captions:** transform `translate`; product terms verbatim; the emphasis phrase is picked in
  the translated text.
- **Hinglish captions:** romanised; phonetic spelling allowed for Hindi words, English words exact.
- **Hindi (Devanagari):** `Noto Sans Devanagari`; the emphasis becomes weight 700 at 116 px (no italic); chips and the
  series card stay in English (Latin) unless the creator asks otherwise.
- **Numbers:** international `$1.2M`, `200`, `22,000` for English; Indian `₹1,20,000`, `₹2.5 L` for Hinglish and Hindi.
  Currency glyphs are written, never "Rs" or "INR". Marker numerals are always two digits: `#01`…`#10`.
- **Units:** metric; a spoken imperial unit is shown as spoken.

---

## §6 Hook system

**The hook title.** In this style the title is a news headline that promises the viewer an edge: the part of the event
nobody covered, the free tool that replaces a paid one, the setting to change today ("The feature nobody / is talking
about", not "WWDC recap"). It doesn't have to repeat the spoken words; it has to be true to what the reel delivers, and it
always arrives with its proof. A title shown as someone's words (in quotes) is word for word. Write 8–10 candidates from
the formulas in §6.5 plus the proven shapes ("How to X as a Y", "Why your X isn't working", "The X nobody tells you",
"Stop doing X", a number or a contrast), score them on outcome, curiosity, who it's for and brevity, run the best through
the stopper test, pick one, and keep the next two as alternates.

### 6.1 The stopper test
| Test | This style |
|---|---|
| **Thumbnail** | f0 at 25 % shows the plate (62 px → 15.5 px, readable) and the proof card; for HA-18, the post line and the clip's subject |
| **Mute** | The first 3 s say what the reel is about with the sound off: the plate or the post line + the proof + the first caption |
| **Motion at f0** | The presenter's live footage, the clip playing, or the B-roll moving on frame 0 |
| **Read time** | The plate or lockup reads in ≤ 1.5 s (≤ 9 words) |
| **Payoff by** | The proof (card, product, clip, B-roll subject) on screen by 2.5 s (HA-02, HA-18); the thesis readable by 3.0 s (HA-12); the lockup by 0.7 s (HA-05) |
| **Frame 0 built** | The archetype's f0 is complete on frame 0: HA-02 = plate (both lines readable) + proof card + presenter; HA-18 = post header + the clip playing; HA-12 = moving B-roll in the split + the first caption by 0.33 s; HA-05 = presenter + the italic lockup readable by 0.7 s |

The first three seconds feel dense: the plate group lands, the prop strobes, the cut to the split, the caption swaps. Dense
in time, never in space: each thing lands while the last one settles.

### 6.2 HA-02 Headline + proof ("Plate + proof"), the default
Spoken pattern: "*The most exciting part of [EVENT] isn't [THE OBVIOUS THING]… it's [THE THING NOBODY IS TALKING ABOUT].*"

| t | Beat | Tone | Visual | Caption | Layout / camera | Sound |
|---|---|---|---|---|---|---|
| **f0** | Stopper frame | awe | **Plate** "The most exciting part / **of [EVENT]**" settled (cy 1000 / 1078) + **proof card** (subject image + "This is not the / **exciting part**") under it + the presenter holding the product or gesturing | hidden (the plate is up) | L-full, as shot | hook hit on f0 |
| 0.0–0.2 | Group lands | awe | Plate + card zoom in 1.25 → 1.00 with motion blur (f0–f6), one group | — | — | whoosh into the hit |
| 0.33–1.3 | Prop strobe | awe | The held product flips colour every 2–3 f (or the card image does) | — | — | soft ticks (one file) |
| 1.8–1.9 | First proof cut | explain | **Hard cut to L-split** (v01 @0:01.85): the product / feature B-roll or recording, moving, in the top band | seam caption: the first phrase ("[Company] just launched one"), complete on the cut | G-1 cut | light whoosh on the cut |
| 1.9–3.0 | Proof runs | explain | The top band animates; the plate is gone | the seam caption swaps per phrase | L-split | — |
| 3.0–6.0 | The twist | awe | L-full; the **italic emphasis** on the twist ("*exciting part*") | split tiers: "This is / *exciting part* / not the most" | L-full | — |
| 6.0–8.0 | Proof montage | explain | L-split: 3 B-roll / recording swaps, one per phrase (feature grid, a screen, the product) | seam caption | L-split | — |
| 8.0–8.5 | Section break | — | **T-2 warm wash** (≈ 15 f, white peak) | hidden | cut under the wash; the softer **Z-1 rush-in** (×1.12 over 8 f) starts on the cut | wash + impact on the white frame |
| 8.5–10.4 | **Series card** | awe | "Welcome to / *Day 60* / of [SERIES]" over the presenter (L-full), kicker typing on | hidden (the card is z8) | L-full | reveal on the number; the bed enters |
| 10.4–12 | Promise | win | italic "*nobody is talking about*" + the count ("here are the 10 that matter") | split tiers | L-full | — |
| ≈ 12 | Item 1 | explain | `#10` (or `#01`) numeral on the ordinal word (§7.3) | hidden | L-full | **list cue** |

Never skip the proof: with no product image, the proof card shows a created image from the script's words (§12.4), and the
1.8 s cut goes to a created UI in the split (P-SPLIT-UI).

### 6.3 Alternate hooks

**HA-18 Borrowed post ("Post + clip")**: when there's a real viral post and its clip: the creator's own files, else the
real ones fetched from the web, source noted (v03).
| t | Visual | Caption | Layout |
|---|---|---|---|
| f0 | W-void: the post header (avatar initials circle 72 px + name Inter Tight 600 34 px + handle 28 px small print + the post line Inter Tight 500 40 px) at y 300–440 (measured y ≈ 324–432); the clip in a band x 0–1080, y 470–1400 (cover crop; measured y ≈ 461–1397); a 6 px white progress bar on the band's bottom edge with a 64 px avatar dot riding it | the clip's own words at the L-board caption position (cy 960); when the clip carries its own subtitles, hide ours for its span (`captions.overrides {t: [a, b], hide: true}`) | L-board |
| 0.0–3.0 | The clip plays its payoff line (the viral moment) | caption per phrase | L-board |
| 3.0–7.5 | The clip continues (or a second clip); the avatar dot travels the bar (0 → 100 % over the hook) | caption | L-board |
| 7.5–8.0 | **T-2 warm wash** out | — | — |
| 8.0–10 | Presenter; italic reaction lockup ("*[Name]* / is literally…") | split tiers | L-full |
| 10–13 | Teaser: "*#02, #03 and #08* / do the whole job for free" + 3 tool tiles (P-TEASER-TILES) | split tiers | L-full |
| 13–17 | Series card "Welcome to / *Week 09* / of the AI tools" | hidden | L-full |
| 17–22.6 | **T-5** into **W-wheel**: the presenter over the tool wheel; "I went through / *100 launches this week*" … "*Let's dive into it*" | typed plain + italic | W-wheel |
| 22.6–23.1 | Radial speed lines + **T-2** → Z-1 rush-in → lime swipe → `#10` | hidden | L-full |

The presenter is away for up to 8 s; the clip's payoff line plays by 3 s. Without the creator's clip: FB-4 (HA-02, or a
created quote card + a created video UI).

**HA-12 Thesis typography ("Split thesis")**: the F-B default (v02).
| t | Visual | Caption | Layout |
|---|---|---|---|
| f0 | L-split: moving B-roll of the story's subject in the top band (or P-DOT-REVEAL), black fade above the seam; the presenter below | — | L-split |
| 0.17–0.33 | **T-9 dot dissolve** (6 f): the B-roll subject dissolves into the dot-matrix figure (v02 @0:00.17–0:00.33) | — | L-split |
| 0.37 | The first plain phrase above the seam ("One [kind of company] just"), 1 f blur-in | seam | L-split |
| 1.67 | The thesis phrase in italic with it ("*announced a full-body scanner*", shortened to ≤ 22 characters: "*a full-body scanner*"), blur-in 6 f | split tiers | L-split |
| 2.2–2.8 | HUD corner brackets (P-HUD-MARKS) draw on the B-roll | — | L-split |
| 3.0–6.0 | A second B-roll + "*in just 60 seconds*" | seam | L-split |
| 6.0–7.0 | L-full, italic reaction ("Even experts / *are shocked*") | tiers | L-full |
| 7.0–7.4 | T-2 warm wash | — | — |
| 7.4–9.5 | Series card "Welcome to / *Day 60* / of future tech updates" | hidden | L-full |

The thesis is readable by 3.0 s.

**HA-05 Claim lockup ("Teaser lockup")**: roundups whose payoff is "N tools that replace a paid one" (v03 @0:11–0:13).
| t | Visual | Caption | Layout |
|---|---|---|---|
| f0 | L-full; the italic lockup built by 0.7 s on the chest: "*#02, #03 and #08*" (the CS-1 italic line, 116 px) / "do the whole job for free" (the plain line under it) | the lockup is the caption (tiers) | L-full |
| 0.4–1.2 | P-TEASER-TILES: 3 tool tiles (240 px, gap 24) pop below it (cy 1340), 4 f stagger | — | — |
| 1.5–3.0 | Presenter line "Let me show you"; the tiles exit | caption | L-full |
| 3.0–5.0 | Series card | hidden | L-full |

### 6.4 Hook pairs by topic
| Topic | Hook | Pair | Column 1 | Column 2 | How each is shown |
|---|---|---|---|---|---|
| A keynote / launch event | HA-02 | promise → proof | "The most exciting part of [EVENT]" | the one feature nobody covered | plate + proof card (a product photo the creator holds) → its recording in the split at 1.8 s |
| A weekly AI-tools roundup | HA-05 | promise → proof | "[#a, #b and #c] do the whole job for free" | the three tool tiles, then item #10 | italic lockup + 3 tiles (logo plates if no logos) |
| A rival's viral moment | HA-18 | claim → evidence | the creator's own post line about it | the clip (theirs, else the real one fetched) | post header + clip band |
| A single AI product launch (F-B) | HA-12 | thesis → scene promise | "[Company] just announced [product]" | the product B-roll / render | split B-roll + italic thesis |

The machinery travels: a money-apps creator runs the same pairs ("The best update / of [APP] this month" + their own app
screenshot; "[#a and #b] replace a ₹[X]/month app" + paid-vs-free chips at item 1), as §14.2 shows in full.

### 6.5 Title writing
**Plate formula:** line 1 `[the setup, ≤ 5 words]` (white on black) / line 2 `[the stake: the event, a number or the
twist, ≤ 4 words]` (white on red). Sentence case, no emoji, no exclamation marks. An italic lockup (HA-05) is ≤ 8 words on
≤ 2 lines.

| Template | For example |
|---|---|
| **Most-X part** (default) | "The most exciting part / of [EVENT]" |
| **Nobody is talking** | "The feature nobody / is talking about" |
| **Free replaces paid** | "Free tools that / replace [PAID TOOL]" |
| **Count + window** | "10 AI tools / from this week" |
| **Warning** | "Turn this setting off / before [DATE]" |
| **Switch** | "Why I'm switching / back to [PRODUCT]" |

- The plate says what the proof card and the first split show (the mute test).
- Write 8–10, pick by the stopper test, keep two alternates for the post caption or trial reels.
- **Banned:** "game changer", "insane", "you won't believe"; a count that doesn't match the numerals; a claim the reel
  doesn't show.

### 6.6 Hook sound
The hook carries its own cues (the f0 hit, the first cut, the wash); the music bed enters after the hook, at the series
card (§11).

### 6.7 CTA and the end stack
The CTA is the end stack, in this order, in the last 10–14 s (F-A; 6–9 s in F-B, where steps 2 and 3 may merge). It's fast
and confident, with no recap of the items.

| Step | Spoken pattern | On screen | Geometry | Hold |
|---|---|---|---|---|
| 0 | — | T-2 warm wash from the last item | full frame | 12–15 f |
| 1 **Save** | "Save this now, because 90 % of you will forget" | **P-SAVE-BADGE** (a red bookmark badge behind the head) + "Save this now because" / "*90% of you*" / "will forget" | badge x 260–820, y 140–700 | 2.0–3.0 s |
| 2 **Follow** | "And follow, because I do this every single week" | "And follow because I do this" / "*every single week*" (L-full) + the creator's handle as a small chip (28 px, `paper` on 60 % `ink`) at cy 1220 | L-full | 1.5–2.5 s |
| 3 **Deliverable** | "And if you want all [N] with the links…" | **P-DELIVERABLE-TILE** (a link tile behind the head) + "And if you want" / "*all 10 with the links*" | tile x 390–690, y 180–480 | 1.5–2.5 s |
| 4 **Community** | "…join the free community, link in bio" | **P-COMMUNITY-CARD** (W-endcard): "Join the free / [COMMUNITY]", phone mock, the **Link in Bio** pill tapped by the cursor at 1.2 s | §8.3 | 3.0–4.0 s (never past 4 s) |
| 5 | — | Hard end (T-10) ≤ 6 f after the last word | — | — |

- No silence is needed before the CTA: the warm wash before step 1 is the break. TH-lime also puts a T-2 + Z-1 door between
  Save and Follow (v03 @2:33.20–2:33.77), and the Follow line types on.
- **Device variants** (the creator's copy chooses): `follow_save_stack` / `link_bio` (default) as above;
  `comment_keyword`: step 4 becomes **P-COMMENT-CARD**, a white note card "**Comment below**" (accent) + "Comment
  **KEYWORD** and I'll send you the list", the keyword in a lime chip, held ≥ 1.5 s after the keyword is spoken;
  `end_card`: steps 1 and 2, then a 3 s community card without the phone (headline + pill).
- "Link in Bio" or the keyword is readable ≥ 1.5 s; the black tail ≤ 0.2 s.
- **Sponsor** (paid integrations only): **P-SPONSOR-ROW** on the sponsor's tool card: their logo (theirs, else fetched from
  their site) in the brand row, and **"Paid partnership"** (or the creator's disclosure wording) at x 64, y 140 for the whole sponsored item
  (≥ 2 s), also said in speech. The sponsor's colours stay inside their logo; the card frame keeps the skin's style. Clear
  of the face, never in the end stack.

---

## §7 Structure and rhythm

### 7.1 Structure
| Format | Type | Arc | Typical timing (150 s F-A / 90 s F-B) |
|---|---|---|---|
| **F-A Countdown** | `news` | hook (2.5–8 s) → promise + teaser (2–5 s) → **series card** (8–15 s) → items `#NN` (5–10 items, one direction, 10–20 s each) → final verdict (0–6 s, optional) → end stack (10–14 s) | hook 0–8 · promise 8–12 · series 12–14 · items 14–136 · end 136–150 |
| **F-B Daily brief** | `explainer` | hook (thesis, 3–7 s) → **series card** → what it is (mechanism, B-roll) → the twist question (italic re-hook) → why it matters / the catch → the honest caveat ("To be fair…") → end card | hook 0–7 · series 7–9.5 · what 9.5–35 · twist 35–55 · why 55–75 · caveat 75–82 · end 82–90 |

The two formats share the caption profiles, the split, the series card and the end card; F-B swaps the numerals for
italic questions.

### 7.2 Markers (SM-…)
| ID | Marker | Recipe | Use |
|---|---|---|---|
| **SM-NUM** | `#NN` numeral + chip | TH-studio → **SM-NUM-A** (white `#`, lime digits, inline); TH-lime → **SM-NUM-B** (lime hash, white condensed digits); chip above, numeral below (§5.4) | Every F-A item, without exception |
| **SM-CHIP-LABEL** | label chip | the item's 2–3-word name or feature ("Personal context", "Dictation", "Notify me") | The default chip |
| **SM-CHIP-TEASER** | teaser chip | "Wait for the next 02 >>>" (the count of items left, two digits) | Once, on the item where 2 or 3 items remain |
| **SM-CHIP-RECAP** | recap chip | "Recap feature" | An item that returns to an earlier feature or sums up |
| **SM-SERIES** | series card | §7.6 | Once, closing the intro |
| **SM-QUESTION** | italic question chunk | the question as a full italic emphasis chunk on L-full | F-B re-hooks; F-A mid-item re-hooks |

**Numbering:** `desc` (10 → 01, the countdown) is the default and the stronger loop: the best is last. `asc` (01 → 10)
when the items are equal features of one launch (v01). Declared in the reel header; never both in one reel. A countdown
has 5–10 items: fewer is an F-B brief, more splits into two reels.

### 7.3 The item ritual (F-A; the same for every item; t = 0 at the ordinal or number word's onset)
| Frame | Step | Recipe |
|---|---|---|
| −14…0 f | **Entry door** | **TH-lime (every item, v03 ×10):** T-2 warm leak over the previous card (≈ 6–8 f build), cut under it to L-full, **Z-1 / Z-2 rush-in** from the cut (×1.7, 12 f, `expoOut`, alternating) while the red tint fades (v03 @0:22.67–0:23.10, @1:28.03–1:28.47). **TH-studio:** hard cut to L-full (v01 @0:29.37); the first item alone enters through the white-peak T-2 (v01 @0:10.13–0:10.37) |
| −2 f | **Numeral** | TH-lime: **T-6 lime swipe** (3 bars, 2 f) across the numeral band, then SM-NUM-B **snaps in at full size** and its white digits **flicker** (on 1 f, dim 2 f, off 1 f, on; ≈ 8 f) (v03 @0:23.10–0:23.37, @1:28.43–1:28.67). TH-studio: SM-NUM-A lands **on the cut frame** as the 1–2 f smear-stretch of P-NUMERAL-A, no overshoot (v01 @0:29.37–0:29.40). No growth during the hold. Captions hide; **list cue** |
| +4 f | **Chip** | P-LABEL-CHIP (or teaser / recap) drops 24 px + fades in over 6 f above the numeral |
| +14 f | **Logo behind the head** | P-LOGO-BEHIND **cuts on at full size** ≈ 0.45 s after the numeral, no grow (v03 @0:23.55); holds, dimmed, through the card |
| +36…+45 f | Numeral out | Leaves inside the T-11 smear wipe that brings the card (v03 @0:24.55); the chip leaves with it |
| tool name ±2 f | **Card in** | **T-11 smear wipe** (3 f of horizontal streaks across the chest band) → brand row + window complete on the next frame, no rise; dim ramps over 12 f (G-3); the CS-2 lime pill may land 2–3 f before the card (v03 @0:24.55–0:24.65) |
| card body | **Features** | One screen per spoken feature, swapped on the feature word (crossfade 4 f, `events`); P-CURSOR-BOX on the element that is clicked or named; P-PRICE-STRIKE when a price is said |
| after the features | **Pop-back** (optional) | Hard cut or G-4 undim to L-full for the opinion line, one italic phrase (≥ 1.5 s). TH-lime cards often run straight into the next wash (v03 @1:28.0, @2:33.1) |
| next ordinal | Next item | The same door again: TH-lime through T-2 every item; TH-studio by hard cut |

The ritual is the one place repetition is the point: the viewer learns it by the second item and feels the count move.

**F-B beat unit** (t = 0 at the beat's first sentence): L-split B-roll + seam captions (3–8 s) → L-full with the italic key
phrase (2–4 s) → P-FRAMED-CLIP or P-STAT-LINE for the number (2–4 s) → back to L-full. Every second beat opens with an
SM-QUESTION.

### 7.4 Open loops and re-hooks
- **The loops:** the count loop ("10 tools; #02 is free forever"); the teaser loop (P-TEASER-TILES, or "#02, #03 and #08 do
  the whole job for free"); the "wait for the next 02" chip; the deliverable loop ("I'll share all 10 with the links");
  F-B's question loop ("So why does an AI company want it?").
- **Every loop is paid on screen:** the teased items appear with their numerals; the deliverable is the community card; a
  question's answer is the next italic phrase.
- **The number is the re-hook.** Every numeral is a fresh promise (scene `rehook: true`), and so are the teaser chip and
  every SM-QUESTION. When one item runs long, give it its own mid-item re-hook, an italic question or a P-PRICE-STRIKE beat
  flagged `rehook: true`, so the viewer never drifts between numbers.
- **F-B** has no numerals, so its questions carry it: the twist question lands in the middle stretch of the reel, and no
  long stretch passes without an italic question or a stat.
- **The intro is over fast:** hook, promise and series card are behind you while the promise is still fresh (in the
  reference, under 15 % of the runtime), so the first numeral arrives hungry.

### 7.5 Rhythm
- **Calm room, fast doors.** Inside a beat things hold: a card sits still while its screens change, a numeral holds without
  growing, the face talks. The doors are fast and decisive: 1–3 f smears, swipes and snaps, a one-frame white peak. That
  contrast is the whole energy of the style.
- **It follows the speech.** Captions swap with the phrases, cards swap screens on the feature words, the layout switches
  on an ordinal, a tool name or a sentence start. Nothing changes without a word to change on, and nothing waits once the
  word arrives.
- **The face comes back for the verdict.** Every item gets one opinion beat (the pop-back), so the creator's personality
  returns with every tool. A card never sits on one screen; when the features run out, the face takes over.
- **Escalation:** the last two items get the longest cards and the strongest claims ("this one is my favourite", "free
  forever"); in `desc` order `#01` is the biggest item and gets a P-PRICE-STRIKE or a P-STAT-LINE.
- **Washes are chapters.** In TH-studio they mark the section breaks (hook → series, the first item, a mid-reel break,
  body → end stack), rare enough that each one feels like a new chapter. In TH-lime the wash *is* the item door, so it
  arrives with every numeral, and never two doors on top of each other.
- **The end** is fast and confident: the wash, then Save → Follow → Deliverable → Community, no recap.
- There are no entertainment-only beats: the entertainment is the reveal rhythm, numeral → logo → card → screens.
- For reference, measured on the three reels (a description, not a target): median shot 1.33 s (v01), 1.67 s (v02),
  3.03 s (v03, whose long cards carry their screen swaps as crossfades); 17–36 cuts a minute; the longest static picture
  outside a card ≈ 5 s, carried by a Z-3 drift (v01 @2:48.9–2:53.9); items every 10–20 s.

### 7.6 Series furniture
- **The series card (P-SERIES-CARD, SM-SERIES):** "Welcome to" / *{unit} {number}* / "of {series name}". It closes the
  intro (8–15 s in the reference, after the hook's wash and before the first item), holds ≈ 2.0 s (1.8–2.2), captions
  hidden, a Z-3 drift on the presenter.
- **Unit and number:** `Day`, `Week`, `Episode` or `Part` + the number from the reel brief, two digits for 1–9 in `Week`
  series ("Week 09") and as said for `Day` ("Day 60") (`tag_format` "{unit} {n}", pad 2).
- **No series yet (the count card):** the same three-line recipe with the count: "Here are / *10 tools* / you can't miss
  this week" (F-A) or "Today's / *one story* / in 90 seconds" (F-B). Never invent a series number.
- **Series memory:** a series keeps its skin (§4.3) and its unit; after each approved reel, record `{name, unit,
  last_number, theme}` in the copy's niche notes.
- **No persistent series tag** (the reference reels show none).

---

## §8 Visual system: B-roll and patterns

`graphics: support`. The face and the words carry the argument; the graphics prove it. Every spoken product, feature,
price or number gets its visual (D1), and numbers become pictures only as stat lines or price chips with the spoken value
(no charts in this style). In the reference, cards, splits, boards and chest graphics cover roughly half the runtime
(v01 ≈ 45 %, v03 ≈ 60 %). Variety comes from the moment, never from a quota; the item ritual is the one deliberate repeat.

### 8.1 Families (B-…)
| ID | Family | Source class | The real thing (the creator's, else fetched) | Rebuilt when nothing usable turns up (§12.4) |
|---|---|---|---|---|
| **B-1** | Numerals & chips | engine | — | — |
| **B-2** | Tool card (brand row + window) | third-party (a tool's UI: the creator's recording, else captured from the web) | screen recordings (SH-1), logos (SH-3) | `recreated_ui` (fx.appUI) + `logo_plate` (fx.logoPlate / monogram) |
| **B-3** | Split B-roll | the creator's own, else fetched | B-roll, product shots, screenshots (SH-2, SH-5) | `diagram` / a created icon grid / a note card |
| **B-4** | Chest graphics (note card, logo pop, logo cluster, stat line, price chips) | engine (+ real logos) | logos | monogram tiles |
| **B-5** | Borrowed post & clip | third-party (the post and its clip: the creator's, else fetched) | SH-4 | `quote_card` + `recreated_ui` (video) |
| **B-6** | Boards (phone flow, framed clip on black) | engine + creator media | screenshots / B-roll | fx.device phone with created rows |
| **B-7** | Series & end furniture (series card, save badge, deliverable tile, community card, comment card) | engine | the community name; optionally a screenshot of their own community page | a created community screen (generic rows) |
| **B-8** | Hook furniture (plate, proof card, teaser tiles, dot reveal, HUD marks, tool wheel) | engine (+ a creator image) | a product photo (optional) | a created icon / silhouette |

### 8.2 How the graphics behave
- **One idea per screen.** The numeral leaves before the card enters; a chest graphic leaves before the next one arrives;
  the plate and the proof card are one group.
- **The card owns the frame while it's up.** The window never moves; its screens change in place on the feature words.
- **Behind or below, never in front.** Logos, badges and tiles stand behind the head; chest graphics sit under the chin;
  cards take the whole frame only over the dimmed presenter.
- **No comedy layer.** Tone is calm; authority comes from evidence, not jokes.

### 8.3 Pattern specs (P-…)
All motion at 30 fps; z per the scenes API. Behind-the-head scenes set `behind: true` (+ the matte); a monogram behind the
head also sets `exception: "behind_text"`.

| ID | Name | Type | On screen | Motion recipe | Use when | Family · class | Engine · needs |
|---|---|---|---|---|---|---|---|
| **P-PLATE-HOOK** | Two-line plate | overlay | §5.2 plate | zooms in with the proof card as one group 1.25 → 1.0 + blur 8 → 0, f0–f6; exit blur 6 f or with the cut | HA-02 f0 | B-8 · TC-display | bespoke scene `kind: "plate"`, z10 |
| **P-THUMB-CARD** | Proof card | overlay | A white card under the plate: image left, a 2-line counter-claim right | part of the plate group's zoom-in (f0–f6); the image (or the held prop) strobes 2 colours every 2–3 f from 0.33 s for ≈ 1 s | HA-02 f0 | B-8 · TC-label | `kind: "proof"`; the creator's image via `fx.shot`, else `fx.card({theme: "light", icon})`; insert record |
| **P-POST-CLIP** | Post header + clip band | overlay | Avatar initials + name + handle + the post line (y 300–440) over a clip band (y 470–1400) | already in at f0; the clip plays; the bar progresses linearly | HA-18 | B-5 · TC-label | header `kind: "post"`; clip `fx.clip` (creator) or `fx.appUI({kind: "video"})`; insert record |
| **P-PROGRESS-AVATAR** | Clip progress | overlay | A 6 px white bar on the clip's bottom edge, a 64 px avatar dot riding it | x = clip progress, linear | with P-POST-CLIP | B-5 · none | part of the P-POST-CLIP scene |
| **P-DOT-REVEAL** | Dot-matrix reveal | overlay | A subject outline (fx.icon or silhouette) built from a 12 px cyan-white dot grid on white, with 3–5 scan markers | the B-roll subject dissolves into the dots over 6 f (f5–f10, v02 @0:00.17); markers pop 3 f stagger | HA-12 f0 when there is no B-roll | B-8 · none | canvas scene in the split top; `fx.silhouette` / `fx.icon` as the mask |
| **P-HUD-MARKS** | HUD brackets | annotation | 4 corner brackets (40 px arms, 3 px `paper`) around the subject + an optional readout of a **spoken** number | brackets draw 6 f; the readout types 1 character a frame (`fx.typeOn(text, lt, {at, cps: 30, frames: 2})`) | a B-roll subject is introduced | B-8 · TC-label | bespoke scene z5 in the split top |
| **P-CLAIM-SPLIT** | Split thesis | stage | L-split with the italic thesis resting just above the seam | captions only (CS-1S tiers) | HA-12, F-B beats | B-3 · TC-subtitle | stage + `captions.overrides` |
| **P-TEASER-TILES** | Teaser tiles | overlay | 3 rounded tiles (240 px, radius 44, gap 24) of the teased tools at cy 1340 | pop 0.6 → 1.05 → 1 over 7 f, 4 f stagger; exit fade 5 f | HA-05, the promise beat | B-8 · TC-decorative (monograms) | creator logos in tiles, else `fx.logoPlate` monograms |
| **P-SERIES-CARD** | Series card | overlay | §5.4 series card over L-full | built under the fading T-2 tint: kicker types on 1 character a frame from +6 f (`fx.typeOn(text, lt, {at, cps: 30, frames: 2, drop: 0, stretch: 0})`); number blur-pops 3 f; sub types on (the same `fx.typeOn`); exits under the next wash or a hard cut | closes the intro | B-7 · TC-display | bespoke scene z8, `kind: "title_card"` |
| **P-NUMERAL-A** | Inline numeral | marker | White `#` + lime digits, 330–360 px, cy 1056 | lands on the cut frame: 1–2 f horizontal smear-stretch (scaleX 1.3 → 1, scaleY 0.5 → 1, h-blur 16 → 0 as `filter:${ctx.blur(16, 0)}`: a directional smear, not a uniform blur), no overshoot, no growth; exits with the next cut or wipe | every item (TH-studio) | B-1 · TC-display | scene z8, `kind: "numeral"`, `rehook: true` |
| **P-NUMERAL-B** | Hash numeral | marker | A lime 540 px `#` behind white 330 px condensed digits, cy 1200 | T-6 lime swipe (2 f) reveals it at full size; the white digits flicker on / dim / off / on over ≈ 8 f; holds still ≥ 1.1 s; exits inside T-11 | every item (TH-lime) | B-1 · TC-display | scene z8, `kind: "numeral"`, `rehook: true` |
| **P-LABEL-CHIP** | Label chip | marker | A white chip, italic 54 px `ink`, above the numeral | drop 24 px + fade 6 f | every item | B-1 · TC-label | scene z8 (its own rect, clear of the numeral's) |
| **P-TEASER-CHIP** | Teaser chip | marker | "Wait for the next 02 >>>" in the chip | as the label chip; the ">>>" steps in 2 f per arrow | once, with 2–3 items left | B-1 · TC-label | scene z8, `kind: "teaser"` |
| **P-RECAP-CHIP** | Recap chip | marker | "Recap feature" | as the label chip | summary items | B-1 · TC-label | scene z8 |
| **P-LOGO-BEHIND** | Logo behind the head | overlay | The tool's logo (or a `tile` monogram: 420 px square, radius 80, initials 220 px `paper`) centred on x 540, y 150–560, behind the presenter (measured logo ≈ 400 px at y ≈ 144–560, v03) | cuts on at full size ≈ 14 f after the numeral (v03 @0:23.55), no grow; holds (dimmed) through the card; exits with the item's wash | every item start | B-2 · TC-display (monogram) | `behind: true` + matte; a monogram sets `exception: "behind_text"`; insert record (logo) |
| **P-BRAND-ROW** | Brand row | overlay | Logo / monogram 80 px + the tool name 50 px at x 64, y 660–720 | complete on the frame after the T-11 smear (no slide) | with every tool card | B-2 · TC-label | part of P-TOOL-CARD |
| **P-TOOL-CARD** | Tool card | stage + overlay | L-card: brand row + window (972 × 540, radius 28) with the recording; TH-lime adds the 8 px white frame | T-11 smear wipe 3 f → window + brand row complete, no rise; dim ramps 12 f; exits under the next T-2 wash (TH-lime) or a hard cut | every F-A item; F-B product mentions | B-2 · TC-label | `fx.shot` / `fx.clip` (creator) or `fx.appUI` (created); `kind: "card"`; insert record |
| **P-SCREEN-SWAP** | Screen swap | state | The next screenshot / recording segment in the same window | crossfade 4 f; the window rect never moves | each spoken feature inside a card | B-2 · none | scene `events` (a crossfade) |
| **P-CURSOR-BOX** | Cursor box | annotation | A 4 px `primary` rounded box (radius 10) around the named UI element + a 56 px arrow cursor that taps it | the box draws clockwise in 8 f; the cursor glides 10 f and taps (scale 0.9, 3 f) | "click", "upload", "add", "you get…" on a visible element | B-2 · none | bespoke scene z5, `overlaps: [<card id>]` |
| **P-PRICE-STRIKE** | Paid vs free | overlay | A `bad` chip with the spoken price ("$22/month") and a strike line, then a `good` chip "FREE" beside it, at the card's top-right corner (or chest in L-full) | the chip pops 6 f; the strike draws L → R 6 f on "charges"; FREE pops on "free" | paid → free comparisons | B-4 · TC-label | bespoke scene z6; the price exactly as spoken; may carry `rehook: true` |
| **P-SPLIT-BROLL** | Split B-roll | stage | L-split with the creator's B-roll / screenshot / recording in the top band, caption just above the seam | the top content swaps per phrase (crossfade 4 f or cut) | any sentence about a product or an event | B-3 · none | stage `L-split` + `fx.clip` / `fx.shot` in `rects.graphic`; insert record |
| **P-SPLIT-UI** | Split created UI | stage | L-split with a recreated generic UI flow (list, chat, settings) in the top band | rows type / appear per spoken step (`at` times) | no recording; a flow is described | B-3 · TC-label | `fx.appUI` in `rects.graphic` |
| **P-FEATURE-GRID** | Feature grid | overlay | 2–3 rows of 72 px icons in coloured circles (fx.icon) in the split top | pop 4 f stagger, one row per spoken feature | a list of features ("health, sleep, fitness") | B-3 · none | `fx.icon` scene in the split top |
| **P-NOTE-CARD** | Note card | overlay | §5.4 note card (orb on top) at chest (L-full, cy 1160) or in the split top | rise 30 px + de-blur 8 f; the text types word by word at 9 words/s | a spoken request, notification, prompt or quote | B-4 · TC-label | `fx.quoteCard`-style or bespoke; quotes word for word |
| **P-LOGO-POP** | Logo pop | overlay | One 320 px logo tile at chest (cy 1250) under the caption | pop 0.6 → 1.05 → 1 (7 f); exit fade 5 f | a single app named in L-full | B-4 · none | creator logo, else `fx.logoPlate` |
| **P-LOGO-CLUSTER** | Logo cluster | overlay | 2–4 round 240 px badges at chest (cy 1200–1380) in a triangle / arc | each pops on its name (7 f) | "tools like A, B and C" | B-4 · none | as P-LOGO-POP |
| **P-STAT-LINE** | Stat line | overlay | §5.4 stat line (the spoken value + a label) on the split top's lower third or at chest | the value blurs in 6 f; the label fades 6 f (+4 f) | a spoken number that matters | B-4 · TC-display | bespoke scene; the value exactly as spoken |
| **P-PHONE-BOARD** | Phone board | stage | L-board on W-board: a 600 × 1210 phone mock centred; rows build inside per spoken step | hard cut in; rows rise 20 px + fade 6 f; out by T-12 (the phone pushes 1.03–1.06×/f for 4 f, then rushes into its white screen with motion blur for 4 f, hard cut) | a step-by-step flow ("you just explain… it sets it up"); a glance (the reference holds ≈ 3.5 s) | B-6 · TC-label | `fx.device("phone")` + created rows, or the creator's screenshot inside |
| **P-FRAMED-CLIP** | Framed clip on black | stage | W-void: a 640 × 640 rounded (radius 44) clip at cy 860 with italic serif lines above (cy 470) and below (cy 1290) | the clip scales 0.94 → 1 (12 f); the lines blur in | F-B "what it is" beats; a glance (≈ 3 s in the reference) | B-6 · TC-display | `fx.clip` (creator) or `fx.card`; L-board |
| **P-RENDER-WORDS** | Words on B-roll | overlay | Full-bleed creator B-roll (L-board) with one italic serif word group per beat at cy 1370 ("No radiation" → "No magnet" → "No tube") | each group smears out 2 f and the next smears in 3 f (horizontal blur: `filter:${ctx.blur(px, 0)}`, px 24 → 0), the B-roll cutting on the same word (v02 @0:34.77–0:34.93) | a spoken list of 2–4 short properties | B-3 · TC-display | L-board + `fx.clip`; captions hidden for the span |
| **P-SAVE-BADGE** | Save badge | overlay | A 560 px `accent` circle with a white bookmark glyph (soft 3-D: inner shadow + highlight) behind the head, x 260–820, y 140–700 | cuts on at full size behind the head (as P-LOGO-BEHIND); holds through the Save line; leaves under a T-2 (v03 @2:33.2) | end stack step 1 | B-7 · none | `behind: true` + matte |
| **P-DELIVERABLE-TILE** | Deliverable tile | overlay | A 300 px `tile` square with a link or code glyph (fx.icon) behind the head, x 390–690, y 180–480 | as P-SAVE-BADGE | end stack step 3 | B-7 · none | `behind: true` + matte |
| **P-COMMUNITY-CARD** | Community end card | stage | W-endcard: "Join the free" italic 76 px `paper` (cy 300) / the community name in Montserrat 900, 120 px `primary` (112–128) with a 28 px glow (cy 400–520) / a 600 × 900 phone mock at y 600–1500 showing a created group screen (the creator's avatar, the group name, 3 generic rows) / the **Link in Bio** pill (`primary`, 64 px `ink`, Inter Tight 600) at cy 1440 / a 3-D-style cursor arrow tapping it / 3 floating chat-bubble glyphs (generic, `primary` at 60 %) | headline lines fade + rise 6 f each; the phone rises 80 px (12 f); the pill shows its outline first and fills lime on the tap (6 f); bubbles drift ±10 px | end stack step 4 (3–4 s) | B-7 · TC-display | L-board on W-endcard; `kind: "end-card"`; the creator's own community screenshot may replace the created screen |
| **P-COMMENT-CARD** | Comment card | overlay | A note card at chest: "Comment below" (accent, 48 px) + the question, or "Comment KEYWORD…" with the keyword in a `primary` chip | as P-NOTE-CARD | the `comment_keyword` device, or a closing question | B-7 · TC-label | `kind: "cta-keyword"` when a keyword is used |
| **P-WHEEL-STAGE** | Tool-wheel world | stage | W-wheel behind the cut-out presenter: a colour wheel of 4–6 category names (from the script) behind the head + radiating rows of 40 px monogram / app tiles | in by T-5 (the wheel zooms through 1.19 → 1.0×/f, expo-out, ≈ 10 f); the tiles drift outward slowly; out with 24 white radial speed lines (4 f) + T-2 | the promise beat after the series card (F-A, TH-lime); the reel's one map of the field | B-8 · TC-decorative | `behind: true` full-frame scene + matte; creator logos in the tiles, else monograms |
| **P-SPONSOR-ROW** | Sponsor row | overlay | The sponsor's brand row over its card + "Paid partnership" (26 px, x 64, y 140) held ≥ 2 s | as P-BRAND-ROW | paid integrations only (§6.7) | B-2 · TC-label | `kind: "sponsor"` |

### 8.4 Line → pattern lookup
Vocabulary, not a decision table: it tells you what this style reaches for. Ask what the moment needs, then use it.

| Line type | For example | Primary | Alternates |
|---|---|---|---|
| Ordinal / item start | "Number seven…", "Next up…", "And number one…" | P-NUMERAL-A/B + P-LABEL-CHIP + P-LOGO-BEHIND | P-TEASER-CHIP (2–3 left), P-RECAP-CHIP |
| Tool / app named with what it does | "[TOOL] turns any video link into notes" | P-TOOL-CARD (+ P-BRAND-ROW) | P-SPLIT-BROLL, P-LOGO-POP |
| A feature of the tool | "It records, transcribes and summarises" | P-SCREEN-SWAP | P-CURSOR-BOX on the feature |
| A click / an action | "Just paste the link and hit analyse" | P-CURSOR-BOX | P-PHONE-BOARD |
| Price / paid vs free | "[OTHER] charges $22 a month for this" | P-PRICE-STRIKE | P-STAT-LINE |
| A spoken number that matters | "200 open-source models" | P-STAT-LINE | caption emphasis on the number |
| A request / prompt / notification | "Hey, find me the cheapest flight" | P-NOTE-CARD | P-SPLIT-UI |
| A step-by-step flow | "You explain it, it builds the shortcut" | P-PHONE-BOARD | P-SPLIT-UI |
| Several apps named together | "Tools like Make, Zapier, n8n" | P-LOGO-CLUSTER | P-TEASER-TILES |
| A single app mentioned in passing | "…like on [TRAVEL APP]" | P-LOGO-POP | P-BRAND-ROW alone |
| A product / launch / event | "[Company] just launched one" | P-SPLIT-BROLL | P-NOTE-CARD (a created headline card) |
| A list of features or properties | "health, sleep, fitness, hearing" | P-FEATURE-GRID | P-RENDER-WORDS (F-B) |
| The twist / an opinion | "But here's what nobody is talking about" | L-full + italic emphasis | SM-QUESTION (F-B) |
| A rhetorical question | "So why does an AI company want it?" | SM-QUESTION (L-full, an italic chunk) | — |
| A post / another creator's moment | "This tweet blew up", "[Name] said…" | P-POST-CLIP (the real post and clip, the creator's or fetched) | P-NOTE-CARD as a created quote |
| A story subject with B-roll (F-B) | "a ring of a million sensors" | P-SPLIT-BROLL + P-HUD-MARKS | P-FRAMED-CLIP, P-DOT-REVEAL |
| The promise of the items | "#02, #03 and #08 do the whole job for free" | P-TEASER-TILES + italic lockup | P-WHEEL-STAGE (TH-lime) |
| Series / welcome | "Welcome to Day 60 of…" | P-SERIES-CARD | the count card (§7.6) |
| Save / Follow / links / community | "Save this now…", "join the free community" | P-SAVE-BADGE → follow line → P-DELIVERABLE-TILE → P-COMMUNITY-CARD | P-COMMENT-CARD |
| A paid integration | "This video is sponsored by…" | P-SPONSOR-ROW + P-TOOL-CARD | — |

### 8.5 Data and truth
Every number on screen is the **spoken** value or part of the creator's own recording; stat lines and price chips show the
exact spoken figure in the audience's format (§5.5); comparisons are paid-vs-free chips, never charts; no invented
benchmarks, star counts or prices presented as real. Created UIs carry only words from the script, or made-up but
realistic placeholder content with no label when they're plainly an illustration. A screen the recording shows (a
"DEEPFAKE DETECTED" banner, a price) stays as recorded; nothing is added to a real recording to make it say more.

### 8.6 Assets
- **Real captures first:** the creator's own screen recording of each tool (SH-1); else the tool's real pages captured
  from the web. A real screen beats any created UI.
- **Logos:** the creator's files first, else the real logo fetched from the web (the tool's site, its press kit). The
  monogram / logo plate on `tile` only when none can be found, never a redrawn brand mark. P-LOGO-POP and P-LOGO-CLUSTER
  follow the same rule.
- **Created UIs** are generic and unbranded (fx.appUI, fx.device), never a look-alike of a real product.
- **No stock clichés.** Cinematic renders are the real ones: the creator's (SH-5), else the company's own, fetched.
- **Third-party moments:** fetch the real thing, source noted (§12.4).

---

## §9 Transition system

### 9.1 Library (measured at full frame rate)
| ID | Transition | Frames | Recipe | Sound |
|---|---|---|---|---|
| **T-1** | Hard cut | 0 | On a word boundary ±1 f; most boundaries (v01: 106 cuts in 179 s, almost all hard) | none |
| **T-2** | Warm leak wash | 15 | A light leak (magenta `#FF5E7A` → orange `#FF8A3D` → pale yellow `#FFC2A8`) sweeps in from one edge or corner over **6 f**, covering the frame. **Peak:** section breaks flash to **full white for 1 f** (v01 @0:10.30, v02 @0:07.25, v03 @0:08.50); TH-lime item doors hold a saturated red-yellow field for 3–6 f instead (v03 @0:22.70–0:22.87). The cut sits under the peak; the white falls off in 1–2 f and a **warm tint residue** pulses over the new shot for 6–10 f (v01 @0:10.40–0:10.57, v02 @0:07.38–0:07.58). **Build (core draws it):** `timeline.transitions` `{"t": <cut>, "type": "leak", "frames": 15, "pre": 6, "colours": ["#FF5E7A", "#FF8A3D", "#FFC2A8", "#FFFFFF"], "angle": 35, "peak": 1.0}` (6 f build, cut, 9 f residue). Section breaks add the 1 f white on the cut: `fx.flash({id, at: <cut>, up: 1, hold: 0, decay: 2, peak: 1.0})`. TH-lime item doors: the same leak with `"colours": ["#FF3B2F", "#FF8A3D", "#FFC83D"], "peak": 0.95` and no white flash. One leak per door | whoosh + impact on the peak |
| **T-3** | Dim | 12 | `via: dim`: blur 0 → 12, luma 0 → −0.5, ramped over 12 f after T-11 (v03 @0:24.62–0:25.0) | — |
| **T-4** | Slide-down / slide-up split | 9 | engine `slide-down` / `slide-up` | light whoosh |
| **T-5** | Vortex into the wheel | 18 | T-2's leak (built-in `leak`, 8 f: `"frames": 8, "pre": 8`) covers the series card; under it the frame **zooms through** into W-wheel: the wheel world scales in ×1.19, 1.13, 1.08, 1.05 … per frame (expo-out, ≈ 10 f), the presenter ghosted, then matted in front (v03 @0:17.12–0:17.60). The wheel scene does its own scale; its radial blur is a `timeline.grades` `{"t": <cut>, "blur": 14, "dur": 0.33, "frame": true}` frame blur pulse (no bespoke CSS blur). Without W-wheel: 36 seeded radial streaks + scale 1.0 → 1.25 | riser end |
| **T-6** | Lime swipe | 2 | 3 horizontal `primary` bars (h 60, gap 30, over the numeral band, cy ≈ 1200) sweep L → R with heavy motion blur in 2 f; the numeral is complete on the next frame (v03 @0:23.03–0:23.10, @1:28.43–1:28.47). **Build:** `fx.streak({id, at, frames: 2, y: 1200, angle: 0, color: "primary", width: 60, count: 3, spread: 90, length: 1.0, glow: 12})` | swish |
| **T-7** | Screen crossfade | 4 | inside a card window only | none (or a soft click on a click) |
| **T-8** | Fade-through | 14 | engine `fade-through`; a fallback only (boards enter by cut and leave by T-12) | light whoosh |
| **T-9** | Dot dissolve | 6 | the opening image dissolves into P-DOT-REVEAL dots, sweeping, f5–f10 (v02 @0:00.17–0:00.33) | none |
| **T-10** | Hard end | 0 | cut to black ≤ 6 f after the last word | none |
| **T-11** | Smear wipe | 3 | Horizontal streaks (white + the outgoing colours, 6–20 px tall, h-blur 40 px) race across the chest band and carry the numeral out; the card is complete on the next frame (v03 @0:24.55–0:24.65). **Build:** `fx.streak({id, at, frames: 3, y: <chest band cy>, angle: 0, color: "paper", width: 14, count: 6, spread: 200})` (a second one in the outgoing colour if wanted); the numeral leaves with `out: "slide-r", out_frames: 3, smear: true` (a directional smear, not a uniform blur) | swish |
| **T-12** | Zoom-through | 8 | The board's phone pushes ×1.03–1.06 per frame for 4 f, then rushes into its own white screen with motion blur for 4 f; hard cut on the white (v01 @1:17.68–1:17.93). The phone scene scales itself; the motion blur of the last 4 f is a built-in `{"t": <cut>, "type": "zoom-blur", "frames": 4, "pre": 4, "amount": 0.25, "punch": 0, "at": "centre"}` | whoosh |

### 9.2 Grammar
| Boundary | Use | Never |
|---|---|---|
| Frame 0 | the archetype's f0, already built | a fade from black |
| Hook → series card | **T-2 warm wash** | a hard cut |
| Series card → promise / first item | **T-5** into W-wheel (TH-lime); **T-2** white peak into `#01` (TH-studio, v01 @0:10.3) | — |
| New item | **TH-lime: T-2 → Z-1 rush-in → T-6 → numeral, every item.** TH-studio: T-1 with the numeral smearing in on the cut frame | mixing the two doors in one reel |
| Numeral → tool card | **T-11 smear** + T-3 dim | a slow fade into a card |
| Card → presenter | T-1 (or T-3 reversed) | — |
| Sentence → its B-roll | T-1 into L-split (default); T-4 for a split entered mid-sentence | — |
| Into / out of a full-screen flow | T-1 in, **T-12** out | a fade |
| Screen → screen inside a card | T-7 | moving the window |
| Body → end stack | **T-2 warm wash** | — |
| Last word | T-10 | a black tail > 0.2 s |

### 9.3 How the moves breathe
The hard cut is the heartbeat: most boundaries, silent, on the word. The doors are the accents, and they're fast: the
smear wipe into every card, the lime swipe under every TH-lime numeral, the warm leak with its one white frame at each
section break. Flash as often as the style calls for: in TH-lime that's every item door (the reference has thirteen
washes in under three minutes), in TH-studio only the chapters. Never stack two doors on top of each other; each one should
land on a reel that's had a moment to settle. The vortex into the wheel and the zoom-through out of a phone board are
events: they happen once, where the reel opens up, so they keep their surprise.

---

## §10 Motion tokens, camera and zoom, layers, finishing

### 10.1 Motion tokens (30 fps)
| Token | Value |
|---|---|
| Beat lead | 2 f before the onset |
| Entry ease | `cubic-bezier(0.22, 1, 0.36, 1)` (expo-out); doors are 1–3 f (smears, swipes, snaps), soft entries (chips, notes, series number) 3–8 f |
| Exit ease | `cubic-bezier(0.64, 0, 0.78, 0)`, 4–6 f |
| In-out ease | `cubic-bezier(0.65, 0, 0.35, 1)` |
| Numeral | A: 1–2 f horizontal smear-stretch on the cut frame, no overshoot. B: 2 f lime swipe, snap, digit flicker ≈ 8 f. No growth during the hold |
| Chip drop | 24 px + fade, 6 f |
| Card in | T-11 smear 3 f, then complete (no rise); dim ramp 12 f |
| Blur-in (series number, stat value) | blur 14 → 0 px + fade, 3–6 f; word groups and italic lines smear in horizontally over 2–3 f |
| Type-on | ≈ 50 characters/s (1.5–2 a frame): TH-lime plain caption lines; the series kicker 1 character a frame. Captions: `reveal: "char"`, `cps: 50`; scenes: `fx.typeOn` |
| Warm leak (T-2) | build 6 f, peak 1 f white or 3–6 f red-yellow, fall 1–2 f, residue 6–10 f (8 f default): built-in `leak` `frames` 15, `pre` 6 (+ `fx.flash` 1 f white at section breaks) |
| Logo behind the head | cut on at full size, +14 f after the numeral |
| Screen swap | crossfade 4 f |
| Cursor glide / tap | 10 f glide, 3 f tap at scale 0.9 |
| Rush-in | 12 f, `expoOut` (§10.2) |
| Holds | text ≥ 0.25 s per word; titles ≥ 10 f after built; numerals ≥ 36 f |

### 10.2 Footage camera (`zoom_policy: crop_on_cut`)
| ID | Preset | Recipe | Use |
|---|---|---|---|
| **Z-1** | `snap-punch` (**rush-in**) | The cut lands **wide** and rushes ×1.7 to the base framing over **12 f**, `ease: "expoOut"` (per-frame ×1.20, 1.15, 1.07, 1.05, 1.035, 1.025 …), starting **on the cut under a T-2 wash**: `from_wide: 0.59` (= 1 / 1.7), `scale` [1.0, 1.0] (measured v03 @0:22.97–0:23.37, @1:28.27–1:28.67, @2:33.47–2:33.77). After the hook wash, the softer one: `{"t": <cut>, "preset": "snap-punch", "p": {"from_wide": 0.89, "frames": 8}}` (×1.12 over 8 f, v03 @0:08.73–0:08.93). It ends on the base framing, so nothing resets it | Every T-2 door: TH-lime every item; both skins at section breaks |
| **Z-2** | `crash-zoom` (**rush-in B**) | Identical to Z-1 (`from_wide: 0.59`, 12 f, `expoOut`) under a second preset id | Consecutive doors alternate Z-1 / Z-2 |
| **Z-3** | `push-drift` | 1.00 → 1.08, linear, over a ≥ 3 s beat, starting on a cut (measured +9.6 % over 5 s, v01 @2:48.9–2:53.9) | L-full holds of 3 s or more (the only long static stretches); `awe` beats; the series card |

- Camera moves start only on cuts. Plain jump cuts keep the crop (measured, §3.6). No camera change while a card or the
  split is up; no shake, no rotation.
- `from_wide` never goes wider than the raw footage: the rush-in starts at 1 / (base reframe), capped at 1 / 1.7. The full
  ×1.7 needs a base reframe ≥ 1.7 (shoot 4K, or frame the take wide with the head small in the frame); a take already
  framed tight rushes in only as far as the raw frame allows, and a take at the target framing has no rush at all.
- Tone decides the treatment: `awe` takes the blur-in emphasis and the Z-3 drift; `warn` the `bad` price chip when money
  is involved; `win` the `good` FREE chip; `explain` and `cta` stay plain.
- No canvas camera: boards and worlds move inside their own scenes.

### 10.3 Layer order (back to front)
1. The world (W-void / W-board / W-endcard), the presenter's footage, or W-wheel (behind the cut-out)
2. Behind-the-head elements (`behind: true`: P-LOGO-BEHIND, P-SAVE-BADGE, P-DELIVERABLE-TILE)
3. The presenter cut-out (only while a behind scene is up), then the L-card **dim** treatment
4. Split-top content (B-roll, created UI) and its black seam fade
5. Cards: tool-card window, note card, proof card, phone mock (z3 / z4)
6. Brand row, stat lines, HUD marks, cursor box (z5)
7. Price chips, logo pops (z6)
8. Captions CS-1 / CS-1S / CS-2 (z7)
9. Numeral, chips, series card, end-card lines (z8; captions hide)
10. The plate (z10)
11. Light passes: T-2 leaks and blur pulses are drawn by core (`timeline.transitions` / `timeline.grades`, under the
    captions); the white peak (`fx.flash`) and the T-6 / T-11 streaks (`fx.streak`) are z11

### 10.4 Finishing
- No grain, no vignette on footage, no bloom except the community headline's 28 px lime glow and the end-card world's glow.
- Cards: radius 28 (windows), 26 (note cards), 18 (proof card); soft shadows only (`0 18 40 rgba(0,0,0,.35)`); no hard
  offset shadows anywhere.
- Footage is not regraded; exposure and white balance are matched between setups.

---

## §11 Sound

The reference reels' sound wasn't measured, so this is a decision: sound marks the picture's doors and reveals and never
plays on its own. Sparse inside the beats, decisive on the doors.

| Line | Direction |
|---|---|
| **Where sound goes** | The hook (an f0 whoosh-hit as the plate group lands, the first cut); transitions (T-2: a whoosh into an impact on the white peak; T-5: a riser end; T-6 / T-11: a swish; T-12: a whoosh); reveals (the series card number, the price strike, the community card); the **list cue** (every numeral shares one cue, on its swipe or cut frame); the CTA (the Link in Bio tap). The rush-in rides the T-2 cue; no separate sound. Hard cuts are silent |
| **Meme sounds** | None (comedy is off) |
| **The bed** | On; calm tech / lo-fi from the pack; enters at the series card, after the hook |
| **Ducking** | The bed sits ≥ 18 dB under the voice while the voice speaks; the borrowed clip (HA-18) keeps its own audio, and the bed is muted under it |
| **Loudness** | −14 LUFS integrated, true peak ≤ −1.5 dBTP; a hard end ≤ 6 f after the last word |

Sounds come from the bundled SFX catalogue: no file more than twice in a reel except the list cue, never the same file back
to back, every cue on a picture event.

---

## §12 Footage handling

### 12.1 Setups
| Setup | Camera | Framing | Set & light | Wardrobe |
|---|---|---|---|---|
| **A Seated desk** (default) | Tripod at eye level, 35–50 mm equiv., 4K 30 fps preferred | Mid-chest, centred; head top y 300–460, chin y 760–880; hands on the desk in frame | A tidy, warm room: one lamp or practical, shelves or a plaque in soft focus; warm key from 45° | A plain mid-tone or dark top (no logos), so the dimmed card still separates and the bare captions read |
| **B Standing** | Tripod at chest height | Mid-thigh, centred; head top y 220–380, chin y 700–820; a handheld or lapel mic is fine | Bright, clean studio, practicals behind | Same |

30 fps CFR (VFR conformed). The presenter looks into the lens; no B-cam needed. Frame the take wider than the target
framing (or shoot 4K) so the rush-in has room (§10.2).

### 12.2 Shots and fallbacks
| ID | Shot | Spec | Must / optional | Without it |
|---|---|---|---|---|
| **SH-1** | Screen recording of each tool / feature | 1080 px wide or more, 30 fps, cursor visible, 5–15 s per item covering the 2–4 features said; personal data blurred | **must** (F-A) | **FB-1:** the tool's real pages captured from the web, swapped on the feature words in the card window; else a recreated generic UI (`fx.appUI` list / browser / terminal / chat) built from the script's words inside the same tool card; the cursor box still taps the named element. No real product footage; it reads as an illustration (degraded) |
| **SH-2** | Product / feature B-roll or screenshots | the creator's own captures, else the company's press material fetched from the web | optional (F-A, F-B) | **FB-2:** P-SPLIT-UI, P-FEATURE-GRID, P-NOTE-CARD or P-STAT-LINE in the split top. Less proof, more explainer (holds) |
| **SH-3** | Logo files of each tool | SVG / PNG with transparency; the creator's, else fetched from the tool's site | optional (F-A) | **FB-3** (none to be found): a logo plate (the tool's name in type on the `tile` chip) and a monogram tile behind the head (`exception: "behind_text"`). No brand mark or colour (holds) |
| **SH-4** | A post screenshot + its clip: the creator's, else the real ones fetched | post PNG; clip ≥ 720 p, 3–8 s | optional (F-A, F-B; HA-18) | **FB-4:** the HA-02 plate + proof hook instead; or a created quote card (the script's words, verbatim) + a created video UI. Loses the "someone else's viral moment" pull (holds) |
| **SH-5** | Story B-roll (renders, product films) | the creator's, else the company's own fetched from the web | optional (F-B) | **FB-5:** P-FRAMED-CLIP and P-SPLIT-BROLL with created diagrams, P-DOT-REVEAL and stat lines. Less cinematic (degraded) |

Your plan names every fallback the reel uses, and you mention them when you show the storyboard.

### 12.3 Props, the cut-out, resolution
- **Props:** optional: the product the reel is about, held at chest height for the hook (v01's foldable phone). Never in
  front of the face.
- **Reaction bank:** none.
- **The cut-out:** only when the reel stands something behind the head (P-LOGO-BEHIND, P-SAVE-BADGE, P-DELIVERABLE-TILE,
  P-WHEEL-STAGE); check the hair edges at 200 %.
- **Resolution:** the Z-1 / Z-2 rush-in starts on the raw (wide) take and lands on the base framing, so the base reframe
  sets its size: ×1.7 needs a take framed wide enough that the base reframe is ≥ 1.7 (4K, or the head small in a 1080p
  frame). Recordings narrower than 1080 px go into the split top (the 960 px band) rather than the card window.

### 12.4 Third-party moments: fetch the real thing
This style is built on other companies' products, so it has more third-party moments than most, and the viewer should
see the real ones.
1. **Find the moments** in the transcript: each tool's UI and logo, product photos, posts, clips, news headlines.
2. **The creator's own files** in their folder come first. Recordings the creator made of a tool's public UI count as
   theirs.
3. **Otherwise search the web and fetch it:** the tool's real logo, its real pages (captured and framed on the part that
   matters), its own product shots and demo clips, the real post, the real headline, the real photo. Note where each came
   from.
4. **Use it as it is** (cropped, framed in the card, highlighted with the cursor box), never altered to say something it
   doesn't; a post or headline is shown word for word.
5. **Nothing usable to be found: rebuild it** from its exact words (no labels, no credit lines):

   | Moment | Rebuilt as | Recipe |
   |---|---|---|
   | A tool's UI / recording | `recreated_ui` | `fx.appUI` (list / browser / terminal / chat) in the card window |
   | A logo | `logo_plate` | `fx.logoPlate` on `tile` (brand row); a monogram tile behind the head |
   | A post / tweet | `quote_card` | `fx.quoteCard` with the verbatim words from the script; generic avatar initials |
   | Another creator's clip | `recreated_ui` (video) | `fx.appUI({kind: "video", caption})` with the spoken line as its caption |
   | A news headline | `headline_card` | `fx.headlineCard` with the outlet name in type and the exact headline from the script |
   | A person's photo | `silhouette` | `fx.silhouette` with the name and role from the script |
   | A product photo | `diagram` | `fx.card` with an `fx.icon` of the product type |
The patterns that show third-party material: P-POST-CLIP, P-THUMB-CARD, P-TOOL-CARD, P-LOGO-BEHIND, P-LOGO-POP,
P-LOGO-CLUSTER, P-SPLIT-BROLL, P-NOTE-CARD, P-FRAMED-CLIP, P-RENDER-WORDS.

### 12.5 Frame rate and audio
30 fps CFR, 1080 × 1920, BT.709. One voice track: high-pass 80 Hz, de-ess, light compression, −14 LUFS.

---

## §13 What your plan should settle

Your `ideas.md` is a page or two, for you. In this style it has decided, before any code:
1. **The format, skin and count:** F-A or F-B, TH-studio or TH-lime, numbering `desc` / `asc`, the number of items, the
   series (unit, number, name) or the count card, the CTA device and community name, any sponsor.
2. **The hook:** the archetype, the title with its two alternates, the proof (the creator's image, a fetched one or the
   created card),
   every hook beat to the frame.
3. **The item → card table** (F-A): number, tool (exact casing), chip kind and text, logo origin (creator / fetched / monogram), the
   screens and the feature word each swaps on, the cursor element, the price strike or stat line, the pop-back line and its
   emphasis phrase. In F-B: the beats, their B-roll, their questions.
4. **The emphasis phrase of every thought,** and every caption override (forced, blocked, shortened, hidden spans).
5. **The tone of every line,** and so its emphasis treatment.
6. **The doors:** every wash (white peak or red-yellow), every rush-in and its Z-1 / Z-2 alternation, every T-6 and T-11,
   the T-5 and T-12 events, every layout switch on its trigger word.
7. **The re-hooks:** every numeral, teaser chip and question flagged `rehook: true`; the escalated last item.
8. **The inserts** (the creator's / fetched, with the source / rebuilt) and the fallbacks used.
9. **The sound:** the cue moments, the list cue, the bed's entry at the series card.
10. **The moments you'll look at hardest on the storyboard:** f0 (the thumbnail: plate, proof, presenter); the proof by 2.5 s; the series
    card; one numeral with its chip (the chip clear of the chin); one tool card (brand row, window, pill, the logo behind
    the head); one split (the caption's bottom at y 928, clear of the presenter's band); the community card.

How decided the reel header and one item are (in `timeline.json` they become `meta`, beats, scenes and cues):
```yaml
reel:
  format: F-A                 # F-A Countdown | F-B Daily brief
  theme: TH-lime              # TH-studio (CS-1 + CS-1S, SM-NUM-A) | TH-lime (CS-1 + CS-2, SM-NUM-B)
  hook_archetype: HA-05
  structure: news             # F-A news | F-B explainer
  count: 10
  numbering: desc
  series: {unit: Week, number: 9, name: "the AI tools"}
  cta: {device: follow_save_stack, community: "the free community", keyword: null}
  sponsor: null
```
```yaml
- section: ITEM-2
  t0: 108.0
  t1: 122.0
  spoken: "Number two. [TOOL-2] clones your voice from 3 seconds of audio. [OTHER] charges $22 a month for this. This one is free forever."
  trigger: {word: "two", at: 108.2}
  tone: win
  layout: L-full → L-card (G-3) → L-full (G-4)
  item: {n: 2, of: 10, numeral: SM-NUM-B, chip: label, chip_text: "Voice cloning", tool: "[TOOL-2]", logo: creator}
  door: {wash: T-2 red-yellow, camera: Z-2, swipe: T-6}
  screens: [{on: "clones", shot: "rec-2a"}, {on: "seconds", shot: "rec-2b"}, {on: "audio", shot: "rec-2c"}]
  pattern: [P-NUMERAL-B, P-LABEL-CHIP, P-LOGO-BEHIND, P-TOOL-CARD, P-PRICE-STRIKE]
  price_strike: {paid: "$22/month", on: "charges", free_on: "free", rehook: true}
  caption: {profile: CS-2, emphasis: ["free forever"]}
  insert: {id: tool-2-rec, origin: creator}
  rehook: true
```

---

## §14 Worked examples

Times are planning estimates: take the real ones from the words. Bracketed names are slots the reel's script fills (no
real product claims are implied). They show the standard; match it, then beat it.

### 14.1 F-A Countdown, AI tools: "Week 09 of the AI tools" (TH-lime, HA-05, desc 10 → 01, 150 s)
**Hook**
| t (s) | Spoken | Tone | Visual | Caption | Layout / camera | Sound |
|---|---|---|---|---|---|---|
| f0 | — | awe | Presenter at the desk; italic lockup building | "*#02, #03 and #08*" (116 px italic) / "do the whole job for free" | L-full | hook hit |
| 0.4 | "#02, #03 and #08 do the whole job for free" | win | P-TEASER-TILES: three tiles pop (monograms if no logos) at cy 1340 | tiers | L-full | pop ×3 (pack variants) |
| 1.6 | "Let me show you" | explain | Tiles exit; hard jump cut (same crop) | "Let me show you" typed on, bare (no emphasis: stop-words only) | L-full | — |
| 2.6 | "I went through 100 launches this week" | explain | — | "I went through" / "*100 launches*" / "this week" | L-full | — |
| 4.4 | "and picked these 10, completely free" | win | — | "and picked these 10" / "*completely free*" | L-full | — |
| 6.2 | — | — | **T-2 warm wash** | hidden | cut under the wash; Z-1 soft (×1.12, 8 f) | wash |
| 6.6 | "Welcome to Week 09 of the AI tools" | awe | **P-SERIES-CARD** "Welcome to / *Week 09* / of the AI tools" | hidden | L-full, Z-3 drift | bed enters; reveal on "09" |
| 8.8 | "Let's dive into it" | win | **T-5 vortex** into item 10 | italic "*Let's dive into it*" | — | riser end |
| 9.6 | "Number ten…" | explain | Item 10 ritual | hidden under the numeral | L-full | list cue |

The intro is over at 9.6 s; the lockup pays off at 0.4 s.

**Items**
| Section | Spoken gist | Layout | Patterns |
|---|---|---|---|
| #10 (9.6–22) | "[TOOL-10] turns any video link into notes, a transcript and key takeaways" | L-full → L-card | P-NUMERAL-B "10" + chip "Video to notes" + P-LOGO-BEHIND; P-TOOL-CARD (recording, 3 screens: link pasted / transcript / takeaways) with P-CURSOR-BOX on "Analyse"; pop-back "you never sit through / *a lecture again*" |
| #09 (22–34) | "[TOOL-9] records your screen and turns repetitive tasks into automations" | L-card | ritual; 4 screens; P-PRICE-STRIKE: "[OTHER] charges $[X] a month" → FREE |
| #08 (34–46) | "[TOOL-8] makes original music for your reels" | L-card | ritual; screens: plans page → generator → download; cursor box on "Add to downloads" |
| #07 (46–58) | "[TOOL-7] gives you 200 open models for image, video and audio in one place" | L-card → L-full | ritual; P-STAT-LINE "*200* open models" on the pop-back |
| #06 (58–70) | "[TOOL-6] checks if the person on your call is real or a deepfake" | L-card | ritual; a "DEEPFAKE DETECTED" screen only if it's in the recording (never added) |
| #05 (70–82) | "[TOOL-5] records, transcribes and summarises meetings on your own laptop" | L-card | ritual; P-LOGO-CLUSTER of two paid alternatives on "unlike [A] and [B]" |
| #04 (82–96) | "[TOOL-4] finally gets text right in images" | L-card | **T-6 lime swipe** into the numeral; screens ×4 |
| #03 (96–108) | "[TOOL-3] makes a full video from one prompt" | L-card | ritual; the **teaser chip** "Wait for the next 02 >>>" replaces the label chip |
| #02 (108–122) | "[TOOL-2] clones your voice from 3 seconds of audio, free forever" | L-card | ritual; P-PRICE-STRIKE "$22 a month" → FREE; pop-back "*free forever*" |
| #01 (122–136) | "[TOOL-1] is a free coding agent you run on your own machine" | L-card → L-full | ritual; the longest card (5 screens); pop-back "*my favourite this week*" |
| End (136–150) | Save / Follow / all 10 with the links / community | L-full → L-board | T-2 wash → P-SAVE-BADGE + "*90% of you*" → follow line + handle chip → P-DELIVERABLE-TILE + "*all 10 with the links*" → P-COMMUNITY-CARD 3.5 s → T-10 |

Every numeral is a re-hook, at most 14 s apart, plus the teaser at #03. Third-party: 10 recordings (creator), 10 logos
(creator, else fetched from each tool's site; FB-3 monograms only for one that can't be found).

### 14.2 F-A Countdown, money apps: "5 app updates that save you money" (TH-studio, HA-02, asc 01 → 05, 100 s, Hinglish speech → English captions)
**Hook**
| t (s) | Spoken (translated caption) | Tone | Visual | Caption | Layout | Sound |
|---|---|---|---|---|---|---|
| f0 | — | awe | Plate "The best update / **of [APP] this month**" + proof card (the creator's own app screenshot left, "This isn't the / **best part**" right) + presenter holding the phone | hidden | L-full | hook hit |
| 1.0 | — | awe | Card event: the screenshot's toggle flips on | — | — | soft pop |
| 1.7 | "[APP] just shipped five updates" | explain | Cut to L-split: the creator's screen recording of the app (top) | seam pill | L-split | light whoosh |
| 3.2 | "but nobody is talking about the one that saves you money" | awe | L-full (jump cut, same crop) | "but" / "*nobody is talking*" / "about the one…" | L-full | — |
| 5.8 | — | — | T-2 wash | — | — | wash |
| 6.2 | "Welcome to Day 12 of money made simple" | awe | P-SERIES-CARD "Welcome to / *Day 12* / of money made simple" | hidden | L-full | reveal |
| 8.2 | "Number one…" | explain | `#01` SM-NUM-A + chip "Split bills" | hidden | L-full | list cue |

**Items**
| Section | Spoken gist | Patterns |
|---|---|---|
| #01 (8–24) | "Split a bill with friends inside the app" | P-TOOL-CARD (creator recording), P-CURSOR-BOX on "Split", P-NOTE-CARD "Your friend owes you ₹450" (the spoken amount) at chest on the pop-back |
| #02 (24–40) | "Auto-pay limit you set yourself" | P-PHONE-BOARD (TH-studio warm board) 3.5 s with created rows "Set limit → Pick account → Done" → back to L-card |
| #03 (40–56) | "Free credit score, no third-party app" | P-PRICE-STRIKE "₹99 per report" → FREE; teaser chip "Wait for the next 02 >>>" |
| #04 (56–72) | "UPI Lite for small payments without a PIN" | P-SPLIT-BROLL (the creator paying at a shop) + P-STAT-LINE "*₹500* without a PIN" (spoken value) |
| #05 (72–86) | "International payments at the real rate" | P-TOOL-CARD; pop-back "*this one is my favourite*" |
| End (86–100) | Save / Follow / Comment MONEY | wash → P-SAVE-BADGE → follow line → P-COMMENT-CARD "Comment **MONEY** and I'll send you all 5 steps" (keyword ≥ 1.5 s) → T-10 |

Numbers in Indian format for the creator's Hinglish audience: ₹450, ₹99, ₹500.

### 14.3 F-B Daily brief, tech: "Day 60: [COMPANY] built a full-body scanner" (TH-studio, HA-12, 90 s)
| Section | t (s) | Spoken gist | Layout | Patterns |
|---|---|---|---|---|
| Hook | 0–3 | "One image-gen AI company just announced a full-body ultrasound scanner" | L-split | creator B-roll (or P-DOT-REVEAL), seam caption at 0.33 s, italic "*a full-body scanner*" at 1.67 s, P-HUD-MARKS at 2.2 s |
| Hook | 3–6.5 | "that scans your body in just 60 seconds. Even radiologists are shocked" | L-split → L-full | second B-roll + "*in just 60 seconds*"; L-full "Even radiologists / *are shocked*" |
| Series | 6.5–9.5 | "Welcome to Day 60 of future tech updates" | L-full | T-2 wash → P-SERIES-CARD |
| What | 9.5–22 | "Why would a company that makes AI art build this?" | L-split → L-full | P-SPLIT-BROLL of the product page they recorded; SM-QUESTION "So why does an AI / *company want it?*" (re-hook) |
| Mechanism | 22–36 | "a shallow pool, a million sensors, sound through you, a computer maps everything" | L-split | P-SPLIT-BROLL ×4 swaps (creator renders, else the company's own, fetched) or FB-5 diagrams; P-RENDER-WORDS "No radiation" / "No magnet" / "No tube" (L-board, 3 s) |
| Twist | 36–55 | "But here's where you slow down… 50,000 scanners doing a billion scans a month by 2031" | L-full → L-split | italic "*where you slow down*" (re-hook); P-STAT-LINE "*50,000* scanners" and "*1 billion* scans a month" (spoken values) |
| Stakes | 55–72 | "You can change a password. You cannot change your organs. Who owns that file?" | L-split → L-full | P-SPLIT-UI password field (created) → SM-QUESTION "*Who owns that file?*" (re-hook) |
| Caveat | 72–82 | "To be fair, it's still a prototype; it can't diagnose anything yet" | L-full | italic "*still a prototype*"; P-FRAMED-CLIP 3 s with "That 60-second scan / *takes twenty minutes today*" |
| End | 82–90 | "You ask the questions before you step into the water… join the community" | L-full → L-board | "You ask the questions before you step" / "*into the water*" → P-COMMUNITY-CARD 3.5 s |

The questions carry it: 9.5 (the why), 36 (the twist), the stakes question, 72 (the caveat). Pull the stakes question up
to about 60 s so the stretch after the twist never sags.

---

## §15 Your look at the storyboard: the checklist

Watch it once as a stranger with a thumb over the next reel, then once as the editor whose name is on it. Fix what
bothers you, in one pass.

**The style (does it feel like §The feel?)**
- Frame 0 makes a claim and shows its proof: the plate and card (or the post and clip, the split thesis, the lockup)
  complete and readable at thumbnail size; the proof on screen by 2.5 s.
- One skin throughout: caption profiles, numeral variant and window frame all match the theme.
- Every F-A item runs the full ritual: its door (TH-lime T-2 + rush-in + T-6; TH-studio hard cut), numeral, chip, logo
  moment, T-11 into the card, screens changing on the features, the face back for the verdict.
- Look closely at one door, one numeral and one card entry in the move strips: doors are 1–3 f, no eased pops or rises,
  the rush-in starts on the cut, the white peak is one frame, no zoom anywhere but the rush-ins and Z-3 drifts.
- Every thought has one quotable italic phrase, 2–4 words, never a stop-word; the plain words stay small and quiet.
- Lime only marks where you are; red only the stake; paid/free only when the script contrasts them.
- The last item is the biggest; the end stack is fast, in order, with no recap; the series card closes the intro.
- Start to end: calm inside, fast at the doors, and on any frame you know which item you're on and what proves it.

**Craft (by eye, in context)**
- The presenter's face reads whenever the moment is about them: on L-full the caption under the chin and the chip below
  it; on L-split the caption above the seam; behind-the-head elements behind the matte, the hair edge clean. Nothing
  chops the head or buries the face by accident.
- A monogram behind the head reads: most of it visible, first and last letters clear, one at a time.
- No text over text by accident: captions out of the way under the numeral, chip, series card, plate and end-card lines;
  one numeral at a time; the chip clear of the brand row.
- Numerals on their ordinal; brand rows on the tool name; screens on their feature word; cuts on word boundaries;
  nothing teleports, nothing lingers after its point.
- Numbering continuous in one direction; the count matches the promise; the teaser's number is right; every loop paid.
- Every tool and brand spelt exactly, case included; every number spoken or in the creator's recording, in the
  audience's format; no invented benchmarks or prices; illustrations unlabelled.
- Every tool UI, logo, post and clip is the real one (the creator's or fetched, source noted) or, when none could be
  found, rebuilt from its exact words; fetched posts and headlines word for word; private data in recordings blurred; a
  sponsored item shows "Paid partnership" long enough to read.
- Captions readable on a phone: full size on full frames, the quiet pill text on the seam and cards; meaning text inside
  the safe box and out of Instagram's button bands.
- The file itself (1080 × 1920, 30 fps CFR, −14 LUFS, the bed under the voice, a hard end ≤ 6 f after the last word, no
  black tail) is the render's job; it checks it.

---

## §16 Build notes

- **Fonts:** Inter Tight 400–800, Instrument Serif Italic, Montserrat 900, Barlow Condensed 700, JetBrains Mono 400, Noto
  Sans Devanagari 700. Pre-paint ₹ $ # > ✓.
- **Scene building blocks** (write them as helpers at the top of `plan/scenes.js`, then reuse them for every item):

| Block | Role |
|---|---|
| `Numeral` | SM-NUM-A smear-stretch on the cut frame / SM-NUM-B swipe-snap-flicker, `kind: "numeral"`, z8, `rehook: true` (P-NUMERAL-A, P-NUMERAL-B) |
| `Chip` | label / teaser / recap chip at max(866, chin + 76), drop 24 px over 6 f (P-LABEL-CHIP, P-TEASER-CHIP, P-RECAP-CHIP) |
| `BehindHead` | `behind: true` + matte, cut on at full size; monograms add `exception: "behind_text"` (P-LOGO-BEHIND, P-SAVE-BADGE, P-DELIVERABLE-TILE) |
| `ToolCard` | brand row + window + `events` screen swaps + the skin's frame, `kind: "card"`; with the G-3 dim and the T-11 `fx.streak` (P-TOOL-CARD, P-BRAND-ROW, P-SCREEN-SWAP) |
| `CursorBox` | the 8 f clockwise box + 10 f glide + 3 f tap, `overlaps: [<card id>]` (P-CURSOR-BOX) |
| `EndStack` | P-COMMUNITY-CARD on W-endcard (`kind: "end-card"`), P-COMMENT-CARD (`kind: "cta-keyword"`) |
| Doors and camera | T-2 = `timeline.transitions` `leak` (+ `fx.flash` 1 f white at section breaks); T-6 / T-11 = `fx.streak`; T-12 blur = built-in `zoom-blur`; T-5 blur = `timeline.grades` frame blur pulse; Z-1 / Z-2 / Z-3 = `timeline.camera` presets with `from_wide` |

- **What stays scene-driven:** the leak alone can't hold a pure-white full frame, so the 1 f white is a z11 `fx.flash` on
  the cut; the T-5 wheel zoom-through and the T-12 phone push scale inside their own scenes (only their blur is built in).

---

## Appendix A. Evidence map
The full map (every element → `vNN @ m:ss`), the fidelity and motion audits and the unverified list are in `evidence.md`.
In short:
| Element | Source |
|---|---|
| Small captions + one big italic-serif phrase | v01 @0:05 "This is / *exciting part* / not the most"; v02 @0:02, @0:48; v03 @0:18, @2:31; TH-studio pill v01 @1:13.95; TH-lime type-on v03 @0:17.67 |
| `#NN` numerals, chips, logo behind the head | SM-NUM-A v01 @0:11, @0:29.37; SM-NUM-B v03 @0:23.10, @1:28.43; chips v01 @0:11, @2:00, @2:16; logo v03 @0:23.55 |
| Tool card over the dimmed presenter | v03 @0:24.55–0:31 and every item to @2:29; brand row y ≈ 673–690, window y ≈ 738–1303, pill cy ≈ 1343 |
| Split, seam caption, warm leak, rush-in | split v01 @0:01.85, v02 @0:00–0:05; leak v01 @0:10.30, v02 @0:07.25, v03 @0:08.50; rush-in v03 @0:22.97, @1:28.27, @2:33.47 |
| Hook plate, series card, end stack | plate v01 @0:00.07–0:00.6; series v02 @0:07.45, v03 @0:15; end stack v03 @2:30–2:42, community card in all three |

Not verifiable from the reels: the speech language and caption transform (no transcripts), and all sound.

## Appendix B. Hook-title bank
`[…]` slots are filled per reel. Plates are line 1 / line 2; lockups and F-B theses are plain / *italic*. Write 8–10 per
reel and pick by the stopper test.

| # | Template | Hook | For example |
|---|---|---|---|
| 1 | "The most exciting part / of [EVENT]" | HA-02 | "The most exciting part / of WWDC-26" |
| 2 | "*[#a, #b and #c]* / do the whole job for free" | HA-05 | "*#02, #03 and #08* / do the whole job for free" |
| 3 | "[N] [THINGS] / from this week" | HA-02 | "10 AI tools / from this week" |
| 4 | "Free tools that / replace [PAID TOOL]" | HA-02 | "Free tools that / replace your editor" |
| 5 | "The feature nobody / is talking about" | HA-02 | "The feature nobody / is talking about" |
| 6 | "This free tool / ruined [X]'s plan" (the creator's own post) | HA-18 | "This free tool / ruined a startup's plan" |
| 7 | "The best update / of [APP] this month" | HA-02 | "The best update / of your UPI app this month" |
| 8 | "*[#a and #b]* / save you [AMOUNT] a year" | HA-05 | "*#01 and #04* / save you ₹6,000 a year" |
| 9 | "[N] [THING] settings / to change today" | HA-02 | "5 app settings / to change today" |
| 10 | "Turn this off / before [DATE]" | HA-02 | "Turn this off / before Friday" |
| 11 | "One [kind of] company just / *announced [PRODUCT]*" | HA-12 | "One image-gen AI company just / *announced a body scanner*" |
| 12 | "[COMPANY] just / *changed [THING] forever*" | HA-12 | "This startup just / *changed search forever*" |
| 13 | "Why would [COMPANY] / *build [PRODUCT]?*" | HA-12 | "Why would an AI art company / *build a scanner?*" |
| 14 | "This is the / *end of [OLD WAY]*" | HA-12 | "This is the / *end of passwords*" |
| 15 | "Nobody read / *the fine print*" | HA-12 | "Nobody read / *the fine print*" |
| 16 | "*Who owns* / your data?" | HA-12 | "*Who owns* / your body scan?" |
