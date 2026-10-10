# Proof Dashboard Style Playbook (template v2)

## The feel

This reel is a receipt. Other creators tell you a setting works; this one opens the app, taps it, and rolls the number up
in front of you. The first frame is a verdict waiting to happen: the creator at a desk in a dark night-city room, a huge
two-line banner glowing at their chest, and under it two ghosted phone cards rising into place. A breath later the loser
floods red. Then the winner hits gold on a single frame, its view counter spins and lands on the real number, and a flare
sweeps across it. You haven't heard the tip yet and you already believe it.

That's the engine: claim, then proof, before doubt has time to start. Every sentence that promises something gets paid on
screen. The real app fills the frame, a cyan orb glides to the exact row and presses on the exact word "tap", everything
else dims so your eye has nowhere else to go, and the toggle snaps on. Then a glitch cut throws you back to the face,
because people trust a person who just showed their work. The creator is the anchor of this control room: lit by the set,
framed by it, their face kept clear of what's in front of them.

Colour is a verdict, never decoration. Red is wrong, green is right, gold is the winner, cyan is the hand that taps.
Nothing glows unless it's telling you something, and the colour lands on its word, never before it. When the creator
explains, the captions stay white and the room stays still. When they turn from the mistake to the fix, the room itself
relights, red to blue, on one frame.

It breathes like a confident walkthrough: hype at the top, calm and exact through the steps, a peak at the proof, then a
keyword typing itself into a DM. The proof gets bigger as the reel goes on, and the biggest number is the last one. If a
frame only says something, it's unfinished. This style shows it.

**The test:** pause on any frame and you can point at the proof of what's being said.

## What this playbook is

You're editing one seated talking-head take of a creator who teaches a feature, a setting, a tactic or a result, and you
have the authority to make it the most convincing reel in their niche. This playbook is the style, pulled from five reels
of the original creator (v01–v05), audited at full resolution and measured frame by frame, then sharpened. Read it all,
every time. Use it the way a great editor uses a reference: take what fits this reel, invent when a moment needs more, and
never ship a frame that breaks the feel above.

**Who it's for and what it needs.** Creators whose proof lives on a screen: social growth, apps and tools, personal
finance, coaching results. Input: one talking-head take, plus their screen recordings and results screens where they have
them; a third-party screen they don't have (an article, a post, a product page) is fetched from the web, and anything
else missing gets built as a generic, unbranded screen (§12). The person cut-out (matte) is required: the virtual
set replaces the real room in every reel. Captions follow the creator's language (English by default; Hinglish or Hindi
set in their copy); the banner stays English unless the copy says otherwise. Machine values live in `tokens.json`; where
this text gives a number tokens also holds, they agree.

### Style directives (non-negotiable)
| # | Directive | Where it lives |
|---|---|---|
| D1 | **The banner is built on frame 0.** Two lines at the chest, one white and one glowing, ≤ 5 words, gone by 3.6 s | §5.2, §6.2 |
| D2 | **Every claim gets its proof on screen within a breath** (about 1.5 s of its trigger word): a real screen, a counter, a card pair, an article, a result. A claim with no proof is proven or cut | §1, §8.4 |
| D3 | **Colour is meaning, never decoration.** Red wrong, green right, gold winner, cyan the tool and the tap. One verdict colour per beat | §4.2 |
| D4 | **Show the exact screen.** Real recordings first; the orb taps on the spoken verb (±2 f); the tapped row is the only bright thing | §8.3 P-SCREENREC-ORB, §8.6 |
| D5 | **The presenter lives on a virtual set** that swaps or relights with the section; the real room never shows | §3.1, §12.3 |
| D6 | **Captions are 1–4 caps words with one glowing keyword**; swearing is masked (S**T) everywhere: captions, banner, labels | §5.3 |
| D7 | **Illustration is never presented as proof.** The creator's results, views and money come from their own screen or their own mouth; an illustration (a sample settings page, a made-up coffee price) may use realistic made-up numbers, with no label | §2, §8.5 |
| D8 | **One CTA: a keyword typed into a DM or comment pill**, readable ≥ 1.5 s, at the end | §6.7 |

### Quick index
| § | What |
|---|---|
| §1 | Procedure: how to approach a reel in this style (the claim → proof pairing) |
| §2 | Hard rules: the craft and the style's never-list |
| §3 | Worlds (the sets W-set-*, UI, stage, verdict), layouts L-set / L-set-dim / L-ui / L-bubble / L-in-app, stage moves, safe zones, the person |
| §4 | Colour: the neon meaning axis |
| §5 | Type and captions: the glow banner, CS-1 + CS-BAD / GOOD / DATA / WIN / SOFT / BOX / HYPE, other text |
| §6 | Hook system: HA-02 Headline + proof (alternates HA-01, HA-07, HA-05, HA-18), banner writing, CTA |
| §7 | Structure and rhythm: walkthrough, teardown, funnel, cash-in; the step ritual; the re-hook |
| §8 | Visual system (B-roll and patterns): 51 patterns in 7 families, line → pattern lookup, data, state and anchors |
| §9 | Transition system T-1…T-14 |
| §10 | Motion tokens, camera and zoom Z-1…Z-5, tone treatments, layers, finishing |
| §11 | Sound |
| §12 | Footage handling: setups, shots SH-1…SH-7 and fallbacks FB-0…FB-7, inserts |
| §13 | What your plan should settle |
| §14 | Worked examples (3) |
| §15 | Your look at the storyboard: the checklist |
| §16 | Build notes |
| App. A / B | Evidence map / hook-title bank |

---

## §1 Procedure: how to approach a reel in this style

You watch, listen, plan, build and look at the storyboard yourself; the edit skill has the mechanics. This style's
craft is one question asked of every sentence: *what on screen proves this?* Get that right and the edit writes itself.

1. **Feel the tone of every line:** `hype` · `explain` · `proof` · `wrong` · `right` · `win` · `story` · `cta`. The tone
   picks the caption profile, the set's light and the camera move (§10.3). Mark each line's trigger word: the noun, number
   or verb the visual lands on.
2. **Pair every claim with its proof.** This is the style's own craft step. For every claim, name the screen, card pair,
   counter, article or result that shows it, and the exact word it lands on. Rank the sources: the creator's own recording
   > their own screenshot > the real thing fetched from the web (the article, the announcement, the product page; never
   the creator's own results) > a created generic UI > a stated number on a card. A claim you can't prove gets proven or
   cut, and you tell the creator which when you show the storyboard.
3. **Pick the hook and write the banner** (§6): the archetype (HA-02 unless an alternate fits better, §6.3), 8–10 banner
   candidates, the best by the stopper test (§6.1), two alternates, and the hook pair (§6.4).
4. **Plan the sets.** Which world each section lives in (§3.1), and the wrong → right turn as a hard relight on the
   caption-swap frame. Sets change at section boundaries, never mid-sentence.
5. **Plan the numbers and the state** (§8.5, §8.6). Every number shown goes into `plan/figures.json` with its provenance;
   counters, the countdown and the progress bar get their state ops.
6. **Run the anchor pass** (§8.6). Read every screen recording's frames and write the orb keyframes and highlight boxes:
   one per tap target.
7. **Plan the steps and the moves** (§7.3, §9): the pill, the cut into the screen, the orb's path, the proof that holds,
   the return to the face. Decide where the reel holds still on purpose and where the last proof escalates.
8. **Get the third-party moments** (§12.4): the creator's files first, then the web, source noted; rebuild from the exact
   text only when nothing usable turns up. Note the fallbacks used.
9. **Count on the cut-out.** Every set, the bubble and the object cut-outs need it (`matte: required`, so it starts right
   after the cut); make sure it's there before the storyboard.
10. **Mark the cue moments** (§11). Jump cuts sit on word boundaries (±1 f).

---

## §2 Hard rules: the craft and the style's never-list

**Craft, by eye** (judge it on the storyboard, in context, the way an editor does):
- **Keep the person clear.** People trust the face that just showed its work, so keep the face and hair clear of the front
  layers when the moment is about them. The framing that does it (the geometry is in §3.6): the banner's top ≥ 80 px below
  the chin, graphics 40 px clear of the head region, side cards in the half of the frame away from the face. When the
  moment wants otherwise (a caption crossing the chin for a beat), that's editing; what's never fine is a head chopped or
  a face buried by accident. Behind the person is fair game, text included (`behind: true`): the set always is.
- **No text over text.** The chest band holds one occupant at a time: the banner, a caption, a verdict word or the re-hook.
  Captions hide under the banner, under z 8 cards and during transitions.
- **On the word.** Visuals land 2 f before the trigger word and are fully on within ±5 f; orb taps land within ±2 f of the
  spoken action verb ("tap", "turn on", "hit", "go to"); a verdict colour lands on its verdict word (±2 f), never before;
  counters land within ±5 f of the number word. Caption lead ≤ 150 ms.
- **Say what was said.** Every number on screen is in `plan/figures.json` with provenance `script`, `creator` (their own
  screen) or `spoken@t`, and is shown exactly as said. Illustrations may use made-up but realistic numbers, names and
  screens with no label (`illustrative: true`). Never present an invented metric ("VIRAL RATE 79%"), revenue, payout,
  testimonial, receipt or DM as the creator's real result.
- **Promise integrity.** A count in the banner equals the items shown; every "I'll show you" is shown; the CTA keyword is
  typed in the pill and readable ≥ 1.5 s.
- **Spelling.** App, menu and button names exact, in the app's own case ("Professional dashboard", "Trial"); the creator's
  product names exact; profanity masked on every text system.
- **Privacy.** Emails, phone numbers, account and card numbers, payment details, other people's handles, faces and avatars
  in DMs or comments are blurred (18 px) for their whole time on screen. A created chat uses initials avatars and generic
  names ("Viewer 1"), never a real person's name, face or handle.
- **Readable.** Text holds ≥ 0.25 s per word and titles ≥ 10 f after they finish building. Red and green text sit on dark
  ground only (§4.3). Meaning text stays inside x 64–1016, y 110–1500 and out of Instagram's bands: the top 110 px, the
  bottom 380 px, and the right 110 px between y 900 and 1540.
- **Audio.** −14 LUFS integrated, true peak ≤ −1.5 dBTP, the bed ≥ 18 dB under the voice, a hard end ≤ 6 f after the last
  word, no black tail. Cuts sit on word boundaries; no dead air except the one deliberate breath (≤ 0.3 s) before the
  re-hook or the verdict.

**Never in this style:**
- Fake proof: invented dashboards, counters, follower numbers, revenue or payouts presented as real. "You've received
  $5,000" appears only when it's the creator's own real notification.
- A platform logo you drew. Brand glyphs are the real logo file (the creator's, else fetched from the brand's site, source
  noted); when none can be found, the platform name is set in type, in its brand gradient (`gradients.platform`) on that
  word only.
- Stock clichés: a stock hand holding a phone, hooded hackers, money rain, rocket emojis, bills or confetti flying through
  the lens. Use the created phone mock (P-IN-HAND), the creator's own clip, or T-14 with the reel's own graphic.
- Red, green or gold used as decoration. Neutral emphasis uses the primary glow; verdict colours appear only on verdict
  beats.
- A caption on the row being tapped. On L-ui the step pill carries the words (§3.2).
- Raw, unframed full-bleed screenshots of somebody else's content. A screenshot (the creator's, or captured from the web)
  goes through `fx.shot` with its highlight; only when none can be found does it become a created card.
- The real room behind the presenter, a green-screen fringe, or a set brighter than the presenter's face.
- Effect packs: RGB-split packs, film burns, lens-flare PNGs, light leaks. RGB slices live only inside the seeded glitch
  devices (P-BANNER-GLITCH, P-UI-GLITCH-SWAP, T-12). A new move is welcome when it's built in this style's language.
- An emoji in the banner (glyphs like → ✓ ⚠ are type, fine in captions and labels).
- More than three bright hues in a frame. A red-vs-gold card pair takes CS-BAD or CS-WIN captions, never a fourth hue.

---

## §3 Worlds, layouts, stage moves, safe zones

### 3.1 Worlds
| ID | Kind | Look | Carries | Enter / exit |
|---|---|---|---|---|
| **W-set-skyline** (default) | backdrop | Night city: vertical gradient `#070B16 → #101A33 → #1B2240`, a warm glow `#FFB65C` at 10 % (r 520, at x 760, y 520) drifting ±12 px, soft bokeh window lights (28–40 discs, Ø 20–60 px, `#FFB65C` / `#FFE2B0` / `#F4F1EA` at 20–45 %, blurred 6–14 px, in the upper 60 % of the frame, y 0–1150; never a regular dot grid, which reads as a pixel skyline), or the creator's own blurred city plate as `texture`; noise 0.03, vignette 0.35 | Hook, claims, opinions, the CTA | P-SET-SWAP: hard switch (0 f) on a cut point or phrase boundary |
| **W-set-neon-red** | backdrop | Studio with a red rim light: radial `#7A0F1A → #2A060A → #0B0204` centred (540, 560), red glow `#FF2D2D` 16 %, vignette 0.45 | The wrong way, warnings, "never do this" | P-SET-RELIGHT, hard (0 f) from any set |
| **W-set-neon-blue** | backdrop | Same studio, blue rim: radial `#123E8C → #081A3A → #02060E`, glow `#2F80FF` 16 %, vignette 0.45 | The fix, the feature, "here's what you do" | P-SET-RELIGHT, hard (0 f) |
| **W-set-warm** | backdrop | Warm room (kitchen / lounge feel): `#2B1E14 → #3A2A1C → #140E09`, warm glow `#FFB65C` 12 % at (300, 600), noise 0.04, vignette 0.40 | Personal story, lifestyle asides, CS-SOFT sections | P-SET-SWAP |
| **W-ui-dark** | stage | `#08090D` flat | Screen recordings and created dark UIs (L-ui), the thumbnail wall | T-3 / T-5 / T-10 |
| **W-ui-light** | canvas | `#F6F7F9` flat (light: text flips to ink) | Articles, light-mode app screens | T-2 |
| **W-stage** | stage | `#0B0B10` + a cyan glow 8 % at (540, 860), r 520 | Funnels, donuts, countdowns, hero counters, people grids | T-3 / T-4 |
| **W-verdict-red** / **W-verdict-green** | void | Radial red `#5C0610 → #200205 → #060001` / green `#0B5C1C → #032008 → #010602` around (540, 900) | The verdict pair (P-VERDICT-WORLD): what's wrong, then what's right | T-8 hard flip on the verdict word |

**How a set is drawn.** With the stage `full`, the world never shows, so a set is a **`behind: true` scene** (`z: 1`,
full frame 1080×1920) painted from the world's tokens (`ctx.tokens.worlds["W-set-…"]`: gradient, glow, bokeh); the engine
draws the presenter's cut-out over it. The scene sits inside the footage group, so camera punches scale the set with the
presenter like a real room. Paint bokeh and window lights at `ctx.rngStable(seed)` positions (static) with a drift of
≤ 0.3 px/frame. During L-set-dim, draw the set at 60 % glow. Never paint text in a set.

### 3.2 Layouts
| ID | Engine | Presenter | Graphic area | Caption | When |
|---|---|---|---|---|---|
| **L-set** (home) | `full` | Full frame, cut out on the set; head top y 300–420, chin y 700–820 | Chest band y 900–1100 (banner, captions, verdict words); proof band y 1130–1500; side slots x 64–364 / 716–1016 at y 360–894 (side cards) | `fixed_y` cy 1000 | Claims, opinions, the hook, the CTA: the reel's home |
| **L-set-dim** | `full` | Full frame, dimmed (blur 10 px, luma −0.4) | One chest card y 860–1300, x 120–960 (profile chip, UI card, transcript block) | `fixed_y` cy 1420 | A card that needs the creator behind it |
| **L-ui** | `hidden` | none | Full bleed: the recording or created UI, 1080 wide, y 0–1920; step pill at y 150–230 | the step pill carries the words; hide the captions for the run (`captions.hide`); if they stay up they sit at cy 1430 | Every screen step |
| **L-bubble** | `pip` circle | Ø 400 at (540, 560), 3 px `paper` ring, shadow 0.5 | Under the bubble: the dimmed clip being torn down (full frame, 45 % luma) and the transcript block y 860–1200 | `fixed_y` cy 1380 when no block is up | Teardowns; long screen runs that need the face |
| **L-in-app** | `card` | x 90, y 640, w 900, h 1280, radius 40 (it bleeds into the bottom band, footage only); the engine's card framing (face 0.30, eye 0.42) | y 120–620: created platform chrome above the presenter (story bar, feed header, stat pill) | `inside_footage` (cy 1360), clamped to the safe floor | "You post it and…" lines, feed and story talk |

**Home and away.** L-set is home. Leave it on a proof noun or an action verb; come back on the payoff word. A screen run
lasts as long as the step and no longer; a face run as long as the claim. When a walkthrough would keep the face away for
more than about ten seconds, cut back for a beat or drop the creator into the bubble, because people came for a person.
The bubble stays up for the whole teardown.

### 3.3 Stage moves
| ID | Move | Recipe | Use |
|---|---|---|---|
| **G-1** | Cut to UI | `via: cut` from L-set to L-ui on a word boundary, paired with T-3 or T-5 on the recording scene | Into every step |
| **G-2** | Return | `via: cut` back to L-set + a Z-1 cut reframe on the payoff word (or T-12 in place of the plain cut) | After every step's proof |
| **G-3** | Dim under card | `via: dim` 8 f: the presenter dims as the chest card rises 40 px + fades in over 8 f | Profile chips, UI cards over the presenter |
| **G-4** | Bubble shrink / grow | `pip-shrink` 10 f (ease back): the footage shrinks into the Ø 400 circle at (540, 560) while the clip under it fades up from 0 → 45 % luma; `pip-grow` 10 f back | Teardowns, long UI runs that need the face |
| **G-5** | Into the app | `shrink-to-card` 12 f to L-in-app; the platform chrome (story bar, stat pill) settles in above over 8 f; `grow-from-card` 12 f out | "You post it and…" lines, feed and story talk |
| **G-6** | Set swap / relight | P-SET-SWAP / P-SET-RELIGHT: a **hard switch (0 f)** on the phrase boundary, on the caption-swap frame (v01 @ 23.58 blue → red; v04 @ 6.2 red → blue with a reframe) | Section changes, the wrong → right turn |

### 3.4 Layout diagrams
```
L-set (home)                                L-ui (screen proof)
┌─────────────────────────┐ 0              ┌─────────────────────────┐ 0
│  IG top UI (keep clear) │ ← y 0–110      │  IG top UI              │ ← y 0–110
│     virtual set         │                │   ╭ Step pill ╮         │ ← y 150–230
│   (side card x 716–1016 │ ← y 360–894    │   recording / created UI│
│    away from the face)  │                │   full bleed, push 1.00 │
│      ( presenter )      │ ← head 300–420 │   → 1.06 per step       │
│      (   face    )      │   chin 700–820 │        ◉ orb Ø 84       │
│ ═══ GLOW BANNER / CAPS ═│ ← chest band   │   rows outside the      │
│ ═══  LINE 2 (GLOW)  ════│   y 900–1100   │   target dim to 35%     │
│  ┌────┐   ┌────┐        │ ← proof band   │                         │
│  │card│   │card│ 1.2M   │   y 1130–1500  │                         │
│  └────┘   └────┘        │                │                         │
│  (desk, hands)          │ ← y 1540+ UI   │  (UI band, no text)     │
└─────────────────────────┘ 1920           └─────────────────────────┘ 1920

L-bubble (teardown)                         L-set-dim (card over presenter)
┌─────────────────────────┐ 0              ┌─────────────────────────┐ 0
│   dimmed clip (45%)     │                │  set + presenter dimmed │
│        ╭──────╮         │ ← Ø 400 at     │       ( face )          │ ← head stays clear
│        │ face │         │   (540, 560)   │                         │
│        ╰──────╯         │                │  ╭────────────────────╮ │ ← chest card
│ IF YOU'RE A SNACKER AND │ ← transcript   │  │ ◯ Name | Niche     │ │   y 860–1300
│ YOU SHOP AT THE STORE   │   block        │  │  151  164K  162    │ │
│ ▌BLESS YOU WITH SOME ⚠ │   y 860–1200   │  ╰────────────────────╯ │
│                         │                │      CAPTION cy 1420    │
└─────────────────────────┘ 1920           └─────────────────────────┘ 1920

L-in-app (you, inside the platform)
┌─────────────────────────┐ 0
│  IG top UI              │ ← y 0–110
│  story bar · stat pill  │ ← chrome y 120–620
│ ╭─────────────────────╮ │ ← card top y 640
│ │      ( face )       │ │ ← face centre y ≈ 1178
│ │      ( chin )       │ │ ← chin ≈ y 1370
│ │   CAPTION CHUNK     │ │ ← y ≈ 1308–1500
│ │                     │ │
└─┴─────────────────────┴─┘ 1920 (card bleeds off the bottom)
```

### 3.5 Safe zones and bands
- Meaning text: x 64–1016, y 110–1500.
- **Chest band:** cy 1000, 200 px tall (y 900–1100): the banner in the hook, captions after it, verdict words and the
  re-hook. One occupant at a time.
- **Proof band:** y 1130–1500: card pairs, carousels, stat pills, the DM pill when it isn't at the chest.
- **Side card slots:** 300×534 at x 64 or x 716, y 360: only in the half away from the face centre (face cx < 540 → right
  slot; > 540 → left slot). When the face is centred (cx 440–640) the side slots stay empty; put the proof in the proof
  band instead.
- **Step pill:** y 150–230, centred.

### 3.6 The person
The creator is the anchor of the control room. Nothing in front of them ever touches their face, hair or the room above
their head unless the moment wants it; on full-frame layouts the caption engine moves a chunk off the face, and on the
windows you place it.
- **L-set (full frame):** setup A puts the head top at y 300–420 and the chin at y 700–820, face centre x 420–660. The
  CS-1 caption at cy 1000 spans about y 904–1096 for a two-line chunk (96 px, line height 1.0), so it starts ≥ 84 px
  under the lowest chin. The banner (cy 1010, lines 64–120 px) keeps its top ≥ 80 px below the chin. A punch never pushes
  the chin below y 880; the set scales with the presenter because it lives inside the footage group.
- **L-in-app (the card):** the card is x 90, y 640, w 900, h 1280, radius 40, framed with the engine's card default (face 0.30,
  eye 0.42): the face is about 384 px tall (0.30 of the card's height) and centred at y ≈ 1178 (0.42 down the card), so
  the chin sits around y 1370 and the head top well below the card's top edge (no breakout: nothing of the head draws
  above y 640). The platform chrome above ends at y 620, 20 px clear of the card. The caption is anchored inside the card and
  clamped to the safe floor: a two-line chunk sits at about y 1308–1500, over the chin and the chest; a one-line chunk
  at y 1404–1500, under the chin. Keep the face clear unless the moment wants it (`captions.overrides` moves a chunk).
- **L-bubble:** the circle spans y 360–760; the face fills about two-thirds of it. The transcript block starts at y 860,
  100 px under the ring; the caption (cy 1380) only shows when no block is up.
- **L-set-dim:** the chest card (y 860–1300) sits on the body, under the chin; keep the head clear of its top edge. Keep
  captions to one line here: a two-line chunk at cy 1420 clamps to y 1308–1500, just under the card's bottom edge at 1300.
- **Returns** are cuts (G-2), never a fade back to the face.
- **Behind the head:** the set is a `behind: true` scene by definition; text may sit behind the presenter too, but in
  this style nothing needs to.

---

## §4 Colour system

### 4.1 Role palette
| Role | Hex | Its one job | Text on it | Contrast |
|---|---|---|---|---|
| `primary` **Signature glow** | `#F5F000` | The banner's glow line and the default caption keyword glow. **Type only**, never a card fill | `ink` | 16.2:1 |
| `accent` **UI accent** | `#1F6FEB` | Step pills, toggles switched on, highlighter boxes | `paper` | 4.6:1 |
| `data` **Orb cyan** | `#5CE1E6` | The cursor orb, tap ripples, link glyphs, the tech / feature keyword glow (CS-DATA) | `ink` | 12.5:1 |
| `winner` **Gold** | `#FFC83D` | The winning card, number or option: gold border, gold counter, flare sweep. Proof elements only | `ink` | 12.7:1 |
| `bad` **Wrong red** | `#FF2D2D` | The wrong way, the losing card, ⚠ icons, the red verdict | `ink` | 5.3:1 |
| `good` **Right green** | `#39FF4A` | The fix, ✓ marks, the green verdict | `ink` | 14.6:1 |
| `send` **Send violet** | `#6060E0` | The DM / comment pill's send button and the in-app Post button (sampled v04 @ 0:46, v05 @ 0:05) | `paper` | — |
| `box_blue` | `#2AAEEB` | The CS-BOX keyword box behind a caption chunk (a cyan-blue gradient `#20A8E8 → #68D8F8`, v01 @ 0:08) | `paper` | — |
| `box_yellow` | `#DCD22C` | The CS-HYPE box behind one payoff word (v01 @ 0:10 "LEGENDARY") | `ink` | — |
| `ink` | `#0B0B10` | Text on bright fills, deep shadows | — | — |
| `paper` | `#FFFFFF` | Caption and banner white, light UI cards | — | — |
| `night` / `panel` | `#08090D` / `#16181F` | UI world; dark UI surfaces (phone cards, pills, notifications) | `paper` | 19.9 / 17.7:1 |
| `muted` | `#8B9099` | Ghost cards before the verdict, inactive rows, the loser's counter at rest | — | — |
| `canvas` | `#F6F7F9` | The light article world | `ink` | 18.3:1 |

Gradients: `platform` `#F58529 → #DD2A7B → #8134AF` (only on the word naming a platform that uses it), `winner`
`#FFF1B8 → #FFC83D → #C98A00` (gold borders and flares), `good` `#B9FFC3 → #39FF4A → #12B82A` and `bad`
`#FF9A9A → #FF2D2D → #B30012` (glow ramps). A creator's brand colour may replace `primary` and `accent` in their copy;
red, green, gold and cyan never change, because they're the meaning.

### 4.2 Meanings
- **The axis is red → green, and gold crowns the winner.** Wrong = red, right = green, the best result = gold. A verdict
  colour lands on its verdict word (±2 f) as a 1–2 f hard flood with a glow bloom that settles over 6 f, never before
  (v02 @ 1.50 red, @ 2.21 gold).
- **Primary (yellow) = "read this":** the neutral keyword, the banner's glow when the banner carries no verdict.
- **Cyan = the tool and the tap:** the orb, ripples, links, feature names.
- **Blue accent = the interface:** pills, toggles, highlighters. Violet is only the send button.
- **Brand colours only on brand names** (the platform gradient on "INSTAGRAM"); never on cards or captions otherwise.
- **The banner's line-2 colour is chosen by meaning:** a warning ("NEVER POST") → `bad`; a result or win ("DID IT!") →
  `good`; a secret or feature ("CHEATCODE", "UPDATE") → `primary`, or the platform gradient on the platform word; a pair
  ("BAD → GOOD") → each word in its own role.

### 4.3 Rules
- One fixed meaning axis, no theme packs: variety comes from the sets (§3.1), which never change a role. No grades either:
  footage keeps its look, with only exposure and white balance matched to the set (a warm set gets a +200 K nudge at
  most). The "relight" is the set's glow, never a grade on the face.
- Three bright hues in a frame at most.
- Red and green text sit on dark ground only. Measured against the set centres, `bad` text is 4.7:1 on W-set-skyline,
  5.0:1 on W-set-neon-red, 4.6:1 on W-set-neon-blue but **3.7:1 on W-set-warm**, so a `wrong` beat always relights to
  W-set-neon-red first (never red text on the warm set). On W-ui-light, verdict words go inside a filled chip (`bad` /
  `good` fill, `ink` text).
- Glow is the style's finish: type glows (`text-shadow 0 0 18px <role>, 0 0 42px <role>@50%`), cards glow by border
  (`box-shadow 0 0 28px <role>@60%`). Nothing else glows.

---

## §5 Type and captions

### 5.1 Font map
| Slot | Family | Weights | Used for |
|---|---|---|---|
| `banner` | **Montserrat** | 900, tracking −0.01 | The glow banner (the hook headline) |
| `display` | **Montserrat** | 800–900 | Verdict words, the re-hook, outline stats, CS-HYPE |
| `body` | **Montserrat** | 800 | Captions CS-1…CS-WIN, transcript blocks |
| `ui` | **Plus Jakarta Sans** | 500–800 | Recreated UIs, step pills, notifications, the DM pill, CS-SOFT, CS-BOX |
| `numeric` | **Inter Tight** | 500–800, tabular | View counters, hero counters, the countdown, donut percents |
| `script` | **Pinyon Script** | 400 | The one celebration word (P-CELEBRATE) |
| `mono` | **JetBrains Mono** | 500 | Viewfinder REC / timecode (decorative) |

The banner face is Montserrat Black, checked against the original reels at full resolution (v01 "NEVER POST / INSTAGRAM",
v04 "YOU FINALLY / DID IT!", v05 "INSTAGRAM / CHEATCODE"). Only a single word like "CHEATCODE" used a techno face, which
has no bundled match: keep Montserrat. Brand wordmarks and app glyphs are image files from the creator, never fonts.

### 5.2 The headline element: the glow banner (`kind: banner`, z 8)
| Property | Spec |
|---|---|
| Block | Centred at **x 540, cy 1010** (measured 1011 v05, 1025 v01, 1053 v04), **820 px** wide. No slab, no stroke, no box: type and glow only |
| Line order | Either line may carry the glow: white over colour (v01, v02, v04), or the platform word in the platform's gradient on top with a white line under it (v03, v05). The white line may be a smaller second tier (0.55×, v03) |
| Line 1 | `paper` (or the glowing line, see order), Montserrat 900, caps, tracking −1 %, **auto-sized so the line spans 780 px**, clamped 64–120 px |
| Line 2 | Same face, auto-sized to 780 px (clamped 64–120 px), colour by meaning (§4.2), glow `0 0 18px` + `0 0 42px @50%` in that colour |
| Both lines | `line-height 0.98`, drop shadow `0 6 18 rgba(0,0,0,.55)`. Fit-width means a short line gets bigger type: "YOU FINALLY" ≈ 92 px over "DID IT!" ≈ 120 px |
| Words | ≤ 5 words in total, exactly 2 lines, no emoji; `→ ✓` allowed as glyphs; profanity masked (S**T); reads in ≤ 1.25 s |
| Brand glyph | Optional, only the creator's logo file: an 88 px square after the longer line, 16 px gap, same glow |
| f0 | Fully built and readable on frame 0. It **floats** ±6 px on a 2 s sine (it rides with the presenter) |
| Life | One event in the hook: **P-BANNER-IGNITE** on its spoken word, or **P-BANNER-TILT** (−4° in 3 f, back in 4 f; v03 @ 1.23–1.43) on a punch word. v03 does both on the same word; that's the one stack that works |
| Exit | Gone between 2.6 and 3.6 s: **P-BANNER-GLITCH** (17 f, for warning and news hooks; v01 @ 2.12–2.83) or **P-BANNER-BLUR-UP** (6 f, the default) |
| Lifetime | The hook only. After it the chest band belongs to captions |
| Captions | Hidden while the banner is up (CS hide `under_z8`) |
| Contrast | ≥ 3:1 against the set at ≥ 96 px, 4.5:1 below |

`kind: "banner"` scene fields: `z: 8` (not 10: the core's top-banner camera clamp must not push the face), `text_content`
= both lines, `lines: 2`, `chips: [{text: <line 2>, role: <its role>}]` (documentation; the chip count isn't enforced in
this style).

### 5.3 Caption profiles (CS-…)
All profiles extend `lib:devin`. The CS-1 family differs only in the emphasis colour; CS-SOFT, CS-BOX and CS-HYPE change
the skin. Switch profiles per tone run, never per word: `captions.overrides: [{t: [a, b], profile: "CS-BAD"}]`, and keep a
profile for at least two chunks so the colour reads as a section, not a flicker.

| Group | CS-1 (default) |
|---|---|
| Mode | `full`, `support`, `mute_safe` |
| Chunking | `group`, 1–4 words: mostly a 2-line chunk of 2–4 words ("HOW SHOULD / YOU USE IT?", "THIS FEATURE / SO GOOD?"), with 1-word punches ("SO", "EVERYTIME"); ≤ 12 characters per line, ≤ 2 lines; never split a name, number or unit; punctuation breaks; a pause ≥ 0.9 s always breaks; end punctuation stripped |
| Timing | Lead 1 f; ≥ 0.25 s per word; chunks hold 0.4–1.6 s (measured); tail 0.12 s; **swap `hard` (0 f): the next chunk replaces the last on one frame, no pop, no scale** (v01 @ 22.00, 23.58); no pause hold |
| Skin | Montserrat 800, **96 px** (measured ≈ 110 px for one-word chunks, v05 @ 0:30 / 0:35), CAPS (lower-case chunks also occur, v05 "everytime"), tracking +1 %, line-height 1.0, `paper`, shadow `0 4 14 rgba(0,0,0,.65)`, no container |
| Position | `fixed_y` **cy 1000** (the chest band) on L-set; cy 1420 on L-set-dim; cy 1380 on L-bubble (when no transcript block); cy 1430 on L-ui (when not hidden); `inside_footage` (cy 1360) on L-in-app, clamped to the safe floor; `avoid_face: true` (a chunk that would touch the head moves under the chin) |
| Emphasis | `glow` in `primary`, glow 18 px, size ×1.08, span `phrase`: the glow runs across the keyword's adjacent content words, so line 2 often glows whole ("SERIES POSTS"), and the glowing line has a vertical gradient fill, a pale tint of the role on top to the full role colour at the bottom (v01 @ 21.0 "SO GOOD?"). About every other chunk has no keyword at all (plain white). Select number > name > glossary > topic noun, never stop-words, one keyword per chunk at most, and let them breathe (about one every two seconds) |
| Hide | Under z 8 scenes (banner, verdict words, re-hook), during transitions and stage morphs, and for L-ui runs |
| Language | Latin script; English terms kept verbatim; **profanity mask `inner`** (S**T, F**K, D**N); glossary = app, menu and product names |

| Profile | Differs from CS-1 | Used on tone |
|---|---|---|
| **CS-BAD** | emphasis `bad`, glow 20, key verbs selectable | `wrong` |
| **CS-GOOD** | emphasis `good`, glow 20, key verbs selectable | `right` |
| **CS-DATA** | emphasis `data` (cyan), glow 20 | `proof` (feature and tool lines) |
| **CS-WIN** | emphasis `winner`, glow 22, ×1.10 | `win` (the result number) |
| **CS-SOFT** | Plus Jakarta Sans 700, 66 px, as spoken (sentence case), one line, 1–3 words, the whole chunk in `primary` with a soft glow (`0 0 18 rgba(245,240,0,.45)`), no keyword, cy 1040; **swap `fade`**: 6 f in, 8–10 f out (v03 @ 34.7, 37.2) | `story` (personal asides on W-set-warm) |
| **CS-BOX** | A feature or product name said as the beat's subject: white Plus Jakarta Sans 600, 64 px, as spoken, one line, 1–3 words, in a `box_blue` box (`#2AAEEB`, radius 10, padding 10/22, soft 24 px glow), cy 1050; replaces the glow on that chunk (v01 @ 0:08 "Linking Reels", box x 265–792) | the feature's name |
| **CS-HYPE** | One payoff word: Montserrat 900, 88 px, `ink` caps in a flat `box_yellow` box (`#DCD22C`, radius 0, padding 8/26), one line, 1–2 words, cy 1060 (v01 @ 0:10 "LEGENDARY", box x 160–922, y 996–1120). A masked swear word may sit above it in the marker face (Permanent Marker). It's the reel's loudest caption, so it's saved for the one word that earns it | the hype payoff |

### 5.4 Other text
| System | Recipe | Hold |
|---|---|---|
| **Step pill** (SM-1) | `accent` fill, radius 18, padding 12/28, Plus Jakarta Sans 700 46 px `paper`, glow 24 px accent@60 %, centred at y 190; pop 7 f (scale 0.7 → 1.06 → 1). After an article, the highlighted phrase itself **becomes the pill**: T-13 carries it out onto the presenter at the chest, and it drifts about 1 px/f (v01 @ 8.13–8.50) | ≥ 1.0 s; swaps on each new screen with a 4 f cross-fade |
| **Card counter** | Eye glyph + compact number, Inter Tight 700 48 px, in a `panel` chip (radius 14) at 64 % of the card's height; loser `muted` → `bad`, winner `paper` → `winner` | Rolls 18 f, lands on the spoken number |
| **Hero counter** | Inter Tight 700, 120–200 px, `paper` with a 22 px glow in its role; the unit word under it, Plus Jakarta Sans 600 48 px | ≥ 1.2 s after landing |
| **Transcript block** | Montserrat 800 44 px caps, left-aligned at x 120, 3–6 lines, 1.15 line height; each line becomes a red or green box (`bad` / `good` 3 px border + 18 px glow + 15 % fill) on its verdict | The whole teardown section |
| **Verdict word** | Montserrat 900 72–110 px caps, role colour + glow 16–36 px, centred in the chest band | ≥ 0.8 s |
| **Celebration word** | Pinyon Script 120–150 px, `winner` + 20 px glow | 1.5–2.0 s |
| **Countdown** | Inter Tight 500 150 px, tracking +6 %, `paper`; unit labels HOURS / MINUTES / SECONDS Plus Jakarta Sans 600 40 px `muted` | ≥ 1.5 s |
| **Notification card** | `panel` card 900×150, radius 32, glyph square 72 px, title 40 px 700, body 40 px 500 | ≥ 1.5 s |
| **DM / comment pill** | See P-DM-KEYWORD (§8.3): a dark translucent pill, avatar, the keyword in sentence case, violet send button | Keyword fully typed ≥ 1.5 s |
| **UI chrome** | Menu text, status bars and body copy inside a recording or created UI (18–34 px) | Never carries the point; the pill or the caption does |
| **Viewfinder** | JetBrains Mono 500 26 px: ● REC, HD 4K, 00:00:00:00 | Section texture |

### 5.5 Language and numbers
- App, menu and button names exact, in the app's own case ("Professional dashboard", "Trial"), in pills and captions; they
  go in the glossary.
- Numbers: international grouping, K / M compact with 1 decimal ("1.2M", "540K", "12.5K"); currency `$` by default. For
  an Indian audience the copy sets `indian`, `₹` and lakh / crore ("₹12.5 L"); counters and labels follow `ctx.fmtNum`.
- Hinglish captions (`hinglish/Latn`): CAPS stays; English UI terms stay in English. Hindi (`Deva`): captions in Noto Sans
  Devanagari 800 (no caps), the emphasis glow unchanged; the banner stays English unless the copy says otherwise.
- The profanity mask runs on every text system, not only captions.

---

## §6 Hook system

**The hook title is a promise.** In this style the title is the glow banner at the chest, and it promises the viewer
something: a secret they don't have ("INSTAGRAM / CHEATCODE"), a mistake they're making ("NEVER POST / AT NIGHT"), a result
they want ("YOU FINALLY / DID IT!"). It doesn't have to repeat the spoken words; it has to be true to what the reel proves.
And it never stands alone: the proof is already rising under it on frame 0, so the viewer gets the promise and the start of
the evidence in the same glance. Write 8–10 banners (§6.5), score them on outcome, curiosity, who it's for and brevity,
check the best against the stopper test, and pick; the next two go to the storyboard as alternates. A title shown as
someone's words (in quotes) stays word for word.

### 6.1 The stopper test
| Test | This style's version |
|---|---|
| Thumbnail | At 25 % scale the banner lines are ≥ 16 px tall and the proof (two cards, a toggle) is visible |
| Mute | The first 3 s read without sound: the banner says the topic, the proof shows the verdict (red loser, gold winner, toggle on) |
| Motion at f0 | The proof element is entering on f0; the banner floats |
| Read time | ≤ 5 words → ≤ 1.25 s |
| Payoff | The verdict (winner flash, counter landing, toggle on) lands by 2.5 s |

### 6.2 HA-02 Headline + proof (default)
The opening is dense in time and calm in space: the cards land, the loser bleeds red, the winner flashes gold and its
number rolls, the banner tilts or ignites, and every event lands while the last one is still settling.

| t | Visual | Caption | Layout / camera | Cue moment |
|---|---|---|---|---|
| **f0 (0.00)** | Presenter on W-set-skyline (or the set of the topic). **Glow banner fully built** at the chest. **Proof element entering** under it in the proof band: a phone-card pair, ghosted (`muted` tint, 55 % opacity), rising 40 px | — (hidden under the banner) | L-set; no camera move | hook (f0 hit) |
| 0.00–0.27 | Cards land (8 f rise + fade, the second card 3 f later) | — | — | — |
| 0.3–1.4 | The presenter says the claim; the banner floats ±6 px. Optional P-SETTING-REVEAL (a settings row unblurring over 24 f) or P-CARD-CAROUSEL settling | — | — | — |
| **≈ 1.5** (the "bad" word) | **Loser lands:** the left card floods red (2 f, v02 @ 1.46–1.54), its counter rolls to its small number (or stays at "0"). Or P-BANNER-IGNITE when the banner carries the verdict | — | Z-1 cut reframe only if the banner doesn't tilt | reveal |
| **1.9–2.5** (the "good" word / the number) | **Winner lands:** a hard gold flood on one frame with a wide gold bloom (halo ≈ 1.5× the card) that settles over 6 f (v02 @ 2.21), gold border 4 px + 28 px glow, its counter **rolls 18 f to the real number**, a flare sweeps across it (12 f). Payoff ≤ 2.5 s | — | — | reveal (counter landing) |
| 2.5–3.0 | Hold the verdict; one banner event (P-BANNER-TILT on the punch word) if none happened yet | — | — | — |
| **2.6–3.6** | The banner exits (P-BANNER-BLUR-UP, or P-BANNER-GLITCH for warnings and news). The cards either slide down 60 px + fade (6 f) or **evolve** into beat 1 (T-11: the winner card grows into L-ui) | The first caption chunk cuts on (hard) on the next word | T-3 / T-11 into beat 1 | transition |

The hook is over fast: by 3.6 s the first step is arriving while the promise is still fresh.

### 6.3 Alternate hooks
| ID | Use it when | f0 | Payoff | Beats |
|---|---|---|---|---|
| **HA-01 Result pair** | The reel compares a bad and a good version of the same thing (a weak vs a strong opener, a bad vs a good budget) | Banner line 2 = "BAD → GOOD" with each word in its role (S**T → GOLD) + the ghosted card pair + presenter | Gold winner ≤ 2.5 s (the bad state ≤ 1.7 s) | As §6.2; the loser's word is red in the banner from f0, the winner's word ignites gold on its spoken word |
| **HA-07 Live number** | A result or milestone is the story ("you finally went viral") | Banner + **P-CARD-CAROUSEL** sliding in at f0 (counters visible from 0.3 s) | The winning counter centred and gold by 1.0 s | 0.0 the carousel slides in from the right, motion blur 10 f · 0.5 settles, counters readable · 1.0 the winner centres, scales 1.0 → 1.15 over 8 f, gold border · 1.3–2.8 the flare sweeps, the others dim to 45 % · 3.0 P-CELEBRATE or exit |
| **HA-05 Claim lockup** | A hidden setting, feature or "cheat code": the proof is a switch, not a number | Presenter + banner + **one settings row** (blurred, toggle off) in the proof band | The toggle flips on (P-TOGGLE-FLIP) ≤ 2.0 s | 0.0 row blurred 14 px · 0.0–0.8 unblurs (P-SETTING-REVEAL) · 1.0 banner float · 2.0 toggle flips on: knob 6 f, `accent` fill, 4 sparks · 3.0 T-2 bloom flash out of the toggle into beat 1 |
| **HA-18 Borrowed clip** | A teardown of a clip (the creator's own, or one they hold and supply) | The clip in a 9:16 side or centre card with its view counter + banner; the presenter moves to the bubble from ≈ 3 s | The clip's counter lands ≤ 3.0 s | 0.0 the clip card plays, counter at "0" · 1.5 the counter rolls to its views · 2.5 the banner exits · 3.0 G-4 bubble shrink: the presenter's face in the Ø 400 bubble over the dimmed clip. Created fallback: P-TEARDOWN-BUBBLE with the clip's words as a transcript block (`quote_card`) |

### 6.4 Hook pairs by topic
The pair for HA-02 and HA-05 is **promise → proof**; for HA-01 it's **bad → good result**; for HA-07 **subject → reveal**.

| Topic | Banner (line 1 / line 2) | Proof visual | Payoff word |
|---|---|---|---|
| A hidden posting setting | INSTAGRAM / CHEATCODE | Settings row → toggle on (P-SETTING-REVEAL + P-TOGGLE-FLIP) | "on" |
| Weak opener vs strong opener | YOUR HOOK / S**T → GOLD | Two cards of the creator's own posts: "3" views red vs "1.2M" gold | "million" |
| A new platform feature | INSTAGRAM / BIG UPDATE | The creator's article screenshot, highlighter on the feature name (else a headline card) | the feature name |
| A post went viral | YOU FINALLY / DID IT! | Carousel of the creator's posts, the viral one gold | the number |
| A fee you're paying | STOP PAYING / THIS FEE | The statement line highlighted red, then the setting that removes it (green) | the fee amount |

The machinery travels to any niche where proof lives on a screen: "YOUR BANK / HIDES THIS" over the app's settings row and
a "Round-ups" toggle flipping on is the same hook as the Instagram cheat code (§14.2 builds a full finance reel).

### 6.5 Banner writing
**Formula:** line 1 (white) = the subject the viewer already knows (the platform, the thing, "YOU"); line 2 (glow) = the
twist: the verdict, the secret, the result. 2–5 words in total, every word in caps.

| Template | Shape |
|---|---|
| Warning | NEVER POST / [THING] |
| Secret | [PLATFORM] / CHEATCODE · [APP] / HIDDEN SETTING |
| Pair | [THING] / BAD → GOOD |
| Result | YOU FINALLY / DID IT! |
| News | [PLATFORM] / BIG UPDATE |
| Stop | STOP [HABIT] / [CONSEQUENCE] |

- Write 8–10, pick by the thumbnail and read-time tests, keep two alternates. The line-2 colour follows §4.2.
- Never: emoji, more than 5 words, "game changer", a count you don't deliver, a claim the reel doesn't prove, unmasked
  swearing.

### 6.6 Hook sound
The hook may carry cues (§11): an f0 hit, the loser flood, the winner flash or counter landing, and the banner exit. The
bed enters after the banner exits.

### 6.7 CTA
| Device | Spoken pattern | On screen | Hold / placement |
|---|---|---|---|
| `dm` (default) | "DM me **KEYWORD** and I'll send you the full guide" | **P-DM-KEYWORD**: the input pill at the chest (cy 980), already on screen on the frame the reel glitch-cuts (T-12) back to the presenter: the creator's avatar, the keyword typing at **one character per 4 f (≈ 8 characters/s)** from the spoken keyword (v04 @ 44.80–45.13), the violet send button pulsing (1.0 → 1.12 → 1.0, 6 f), then the pill sends: it rises 60 px and fades (8 f) | The typed keyword holds ≥ 1.5 s; the last 2–4 s of the reel |
| `comment_keyword` | "Comment **KEYWORD** below" | **P-COMMENT-PILL**: the same pill with a comment glyph and a heart instead of the send button; the heart fills `bad` on send | Same |

The CTA beat is on L-set with a Z-3 pull-out; captions hide while the pill shows the keyword. No silence is needed before
it; the voice stays dry over the pill. The keyword is the reel's `meta.keyword`. The pill is the end: no end card after it.

**Series and sponsors (only when the creator's copy turns them on).** A series shows a "PART {n}" tag in the step pill's
style at y 150 for the first 2 s after the banner exits. A sponsor appears as a P-NOTIFY card with the brand's logo
(theirs, else fetched from their site) and a "Paid partnership" line (Plus Jakarta Sans 700 24 px caps, tracking 12 %, `paper` @ 80 %) held ≥ 2 s.

---

## §7 Structure and rhythm

### 7.1 Structure: a tutorial
| Variant | Arc | Evidence |
|---|---|---|
| **Walkthrough** (default) | HOOK (claim + proof) → PROBLEM (why the usual way fails, red) → REHOOK ("HERE'S WHAT YOU DO") → STEP-1…n (screen + orb, each ending in proof) → PROOF (the result counter / before-after) → CTA | v01, v05 |
| **Teardown** | HOOK (pair) → CLIP (what it is, its numbers) → WHY IT WORKS → WRONG (red) → RIGHT (green rewrite) → WHO IT'S FOR (people grid) → CTA | v02 |
| **Funnel / framework** | HOOK → the model (P-FUNNEL, one layer lit per section) → each layer's tactic with proof → CTA | v03 |
| **Result → cash in** | HOOK (the win) → the warning (red) → the countdown (P-COUNTDOWN) → the steps → proof → CTA | v04 |

### 7.2 Markers (SM-…)
**SM-1 Step pill**: at every step the pill names the screen or setting ("Settings → Trial") on the screen's name ±2 f. No
numerals: the original creator never numbers steps; in a teardown the colour axis marks the turns instead (red section →
green section). `numbering: none`.

### 7.3 The step ritual (every STEP, in frames)
1. **Claim on L-set** (CS-1 or CS-DATA): the keyword glows; a Z-1 cut reframe or a Z-2 push on it, not both.
2. **The step pill** pops at y 190, 2 f before the screen's name (7 f pop).
3. **Into L-ui** on the action verb: G-1 cut + T-3 whip-in (4 f), T-2 into a light page, or T-5 (6 f) between two
   recordings.
4. **The orb** travels to the target (10–16 f, ease in-out) → the rest of the screen dims to 35 % (6 f, P-FOCUS-DIM) →
   **press + ripple on the spoken verb ±2 f** (6 f press, 10 f ripple) → the result state (toggle on, sheet up, number
   visible).
5. **The proof holds ≥ 1.0 s** (a counter rolls, a toggle is on, a sheet is open).
6. **Return** to L-set on the payoff word by the **T-12 glitch cut** (default, v01 @ 37.42, v04 @ 44.73), the **T-13
   iris carry** after an article, G-2 (a plain cut + Z-1), or **T-11**, which shrinks the screen into a side card that
   stays beside the presenter for 1.5–3 s.

The ritual is the one deliberate repeat in this style: the viewer learns it by the second step and starts anticipating the
tap, which is exactly the trust you want.

### 7.4 Open loops and the re-hook
- Loops: the **promise loop** ("here's how" → the steps), the **countdown loop** ("you have 72 hours" → the clock), the
  **verdict loop** (red first, green paid later). Every promise is paid on screen; the CTA deliverable is named in the
  pill's spoken line.
- **The re-hook** lands somewhere in the middle of the reel: **P-HERE-CARD** "HERE'S WHAT YOU DO" (or "BUT HERE'S THE
  CATCH" / "HERE IS THE PART THAT…"). Measured, it's quieter than a card: a T-12 glitch cut back from the UI, a 1-word
  chunk "SO" held ≈ 0.3 s, then the line as a plain 2-line CS-1 chunk (v01 @ 37.42–37.88); with a relight and a reframe on
  the same frame (v04 @ 6.2) when a new section starts. A long reel (past about 80 s) earns a second re-hook (P-COUNTDOWN, a
  new proof pair, or another P-HERE-CARD) so the viewer is never more than about 40 s from a fresh promise. Mark the beat
  `rehook: true` (kind `rehook` on the card).
- The hook is over by 3.6 s, so the first step arrives while the promise is fresh.

### 7.5 Rhythm, by feel
- **The energy curve:** hype from frame 0, steady explaining through the steps, a peak at the proof (the biggest counter,
  the gold card, the celebration), and a clean, confident CTA. The last step escalates: a full proof screen (L-ui with the
  result), the hero counter, or the verdict world.
- **The speech is the rhythm.** It never sits still, but it's never random: something new arrives when the words give it a
  reason. The caption swap is the pulse; overlays land on proof nouns and numbers; the live presenter is motion enough
  between them. Dense in time, never in space: one proof idea per screen, the previous one gone before the next arrives.
- **Holds are part of the proof.** A counter that lands needs a beat to be read; a toggle that snaps on needs a moment on
  screen. Hold the verdict, then move.
- **Contrast keeps attention:** the loud verdict frames (red flood, gold flash, glitch cut) earn their loudness because the
  explaining stretches around them are clean: white captions, a still set, an orb gliding.
- **Light comedy** (`comedy: light`): a thought bubble, the celebration word, an object cut-out, a banner tilt. Every gag
  carries information (the viewer's real thought, the real dish), never two in a row, never in the CTA, never near the
  face. Spend them where the viewer would smile anyway; the reel is a proof first.
- For reference, measured on the five reels (a description, not a target): scene cuts 5.0–10.1/min, median shot
  2.6–7.9 s (p90 10–20 s), visual events 5.5–7.9 per 10 s, caption chunks 0.4–1.6 s; the longest still stretch on the
  presenter is ≈ 3 s (v01 @ 67). The cut count is a side effect of overlay editing, not a goal.

---

## §8 Visual system: B-roll and patterns

### 8.1 How the graphics behave
- Graphics and UI carry the argument; the creator carries the trust. Every claim has its proof (§1, D2).
- **Numbers become proof:** a spoken number is a counter, a card pair, a donut or a people grid, landing on the number word.
  Never a bare number in a caption alone when it *is* the claim.
- **One proof idea per screen:** one pair, one screen, one chart. The previous proof exits before the next enters.
- Variety comes from the moment, never from a quota; the step ritual (P-PILL-LABEL + P-SCREENREC-ORB) is the one
  deliberate repeat.

### 8.2 Families (B-…)
| ID | Family | The creator's own | Built when missing (third-party screens are fetched first, §12.4) |
|---|---|---|---|
| **B-1** | Glow type (banner, verdict words, re-hook) | — | — |
| **B-2** | Proof cards and counters | SH-2 results screens, SH-3 own covers | Dark gradient cards with the post title in type; numbers only from the script (FB-2, FB-3) |
| **B-3** | Screen proof (recordings, orb, UI chrome) | SH-1 recordings, SH-4 articles (else captured from the web) | `fx.appUI` settings / list / chat / browser (FB-1); `fx.headlineCard` (FB-4) |
| **B-4** | Verdict (red / green marks, transcript blocks, grids, funnels, progress) | SH-5 the clip being torn down | Transcript block of the clip's verbatim words + silhouette (FB-5) |
| **B-5** | Beat devices (re-hook, countdown, celebration, outline stat, viewfinder) | — | — |
| **B-6** | Set and camera (sets, relight, thumbnail wall, punches, object cut-outs) | SH-3, SH-7, the matte | Set painted from tokens; icon card for objects (FB-7) |
| **B-7** | CTA pills | — | — |

### 8.3 Pattern specs (P-…)
All motion at 30 fps. "f" = frames. Box coordinates are on the 1080×1920 frame.

**B-1 Glow type**
| ID | Type | On screen | Motion recipe | When | Needs |
|---|---|---|---|---|---|
| **P-GLOW-BANNER** | overlay | The two-line banner of §5.2 at cy 1010 | Built on f0; float `y = 1010 + 6·sin(2π·t/2)`; gone between 2.6 and 3.6 s | Every hook | z 8, kind `banner` |
| **P-BANNER-IGNITE** | overlay event | Line 2 floods from `muted` to its role colour, glow 0 → 42 → 30 px, scale 1.0 → 1.06 → 1.0 | Colour flood hard in 1–2 f, then the glow bump and scale over 8 f, on line 2's spoken word | The banner holds the verdict (warning, result) | event on the banner scene |
| **P-BANNER-TILT** | overlay event | The whole banner tilts | 0 → −4° in 3 f (ease out), back to 0 in 4 f (ease back) (measured v03 @ 1.23–1.43) | A punch word in the hook ("BIG", "NEVER") | event |
| **P-BANNER-GLITCH** | exit | Both lines flip to `bad` (red fill + red glow) on one frame; thin dark fracture lines spread through the letters; then the block breaks into 7 seeded horizontal slices with RGB fringes and is gone | 17 f (measured at 24 fps, v01 @ 2.12–2.83): f0 hard red flip · f1–13 fractures grow (the banner keeps floating) · f14–16 slices shift ±24 px with ±6 px R/B offsets · f17 gone | The exit of warning and news banners | `cuts` declared at the exit |
| **P-BANNER-BLUR-UP** | exit | The banner rises 40 px, blurs 0 → 12 px and fades | 6 f ease-in | The default exit | — |
| **P-VERDICT-WORD** | overlay | One or two verdict words at the chest ("WRONG DESIRE", "PROBLEM SOLVED ✓") in `bad` / `good` with glow | Pop 7 f (0.7 → 1.06 → 1) + a hard colour flood (1–2 f) with the bloom settling over 6 f; out blur 5 f | The verdict sentence of a teardown or a step | z 8 |

**B-2 Proof cards and counters**
| ID | Type | On screen | Motion recipe | When | Needs |
|---|---|---|---|---|---|
| **P-PHONE-PAIR** | figure | Two 9:16 cards 208×370, radius 22, `panel` with a 2 px `muted`@40 % border, centred with a 56 px gap (x 290–498 and 582–790), y 1130–1500; each shows a creator cover (SH-3) or a dark gradient + the post title; a counter chip at 64 % height | Rise 40 px + fade 8 f (stagger 3 f), ghosted 55 % + desaturated until the verdict; loser: `bad` flood 35 % + border + 16 px glow in 2 f; winner: a 1 f `winner` flood (30 %), 4 px border, a 28 px glow that blooms to ≈ 1.5× the card and settles over 6 f, counter rolls 18 f; flare sweep 12 f (a 60 px white bar at 20°, 40 % opacity) | Comparing two versions, the hook proof | figures for both counters; one scene |
| **P-CARD-CAROUSEL** | figure | 4–6 cards 200×356, gap 24, in the proof band; one winner | The strip slides in from x +600 with 14 → 0 px horizontal blur over 10 f (`ctx.blur(px, 0)`, directional); settles 4 f; the winner centres and scales 1.0 → 1.15 over 8 f, gold border; the others dim to 45 % | A result among results ("one of these went viral") | figures; one scene |
| **P-COUNTER-ROLL** | state | Eye glyph + compact number in a fixed-width chip | Each digit column scrolls with an 8 px vertical blur, 18 f, lands on the spoken number ±5 f; optional Z-4 shake on landing | Any view, follower or money number | `exception: E6` (`data-slot` chip), figure, `lands` |
| **P-LINKED-CARDS** | figure | Two cards joined by a glowing chain-link glyph (`data`, 120 px) that pulses 1.0 → 1.12 → 1.0 every 1 s | Cards rise 8 f; the link draws 8 f; the right card's counter rolls when "linked" is said. **Card push:** on W-ui-dark the scene pushes 1.0 → 1.45 over 18 f (ease in-out) and pans onto the card being named, then pulls back over 18 f (v01 @ 14.5, 16.6). Exit: the cards shrink to the centre (1 → 0.4, 4 f) while the link glyph sweeps in (T-14) | "Connect X to Y", "link this to that" | figures |
| **P-HERO-COUNTER** | figure | A big centred counter (120–200 px) + unit word, over the blurred thumbnail wall (P-THUMB-WALL) on W-ui-dark | Steps roll 18 f each on their number words (6K → 9K → 81K) | Growth over time | figure with steps, `lands` |
| **P-STAT-PILL** | figure | A `bad`-filled notification pill (radius 32) with 2–3 icon counts (comments / likes / follows) above a feed card or the L-in-app frame | Pop 7 f (spring), counts roll 12 f | "Your comments / likes blew up" (the creator's real numbers) | figures |
| **P-DONUT-SHIFT** | figure | A ring Ø 260 (28 px stroke) + its percent (Inter Tight 700 64 px) + a label (48 px), beside a phone mock | The ring sweeps 18 f; on the shift word it recolours (`accent` → `data`) and re-sweeps to the new percent | "Who sees it" splits, any percentage that changes | figure (percent) |
| **P-VERSUS-TAG** | figure | Two labelled cards ("Normal" / "Trial") and a tilted tag on the winner ("FREE", "BETTER") | The tag stamps: scale 1.6 → 1.0 in 5 f, rotate −20°, `winner` fill | Two options, one wins | figures if numbers show |
| **P-SIDE-PROOF** | overlay | One 9:16 card 300×534 in the side slot away from the face (§3.5), the post or screen being described, optional gold border | Slide 40 px from the outer edge + fade 8 f; out 5 f | "Like this post", "this one did X" while the presenter keeps talking | creator asset or created card |
| **P-IN-HAND** | overlay | A created phone mock (rounded 64 px, 12 px bezel) tilted 6°, floating ±8 px, playing the creator's own clip | Rise 12 f with a 6° → 0° → 6° settle | Stands in for "a phone in a hand" (no stock hands) | creator clip (`ctx.videoFrame`) |

**B-3 Screen proof**
| ID | Type | On screen | Motion recipe | When | Needs |
|---|---|---|---|---|---|
| **P-SCREENREC-ORB** | overlay + anchor | L-ui: the creator's recording full-bleed (1080 wide), slow push 1.00 → 1.06 per step; the **cursor orb**: Ø 84 (measured ≈ 80–100 px with its ring, v05 @ 0:07), white core 40 %, `data` ring 4 px, a wide 48 px `data` glow halo, opacity 0.9; the recording is pushed in so the tapped row is ≥ 60 px tall | The orb travels between keyframes (10–16 f, ease in-out, ≤ 84 px/frame); idle drift ±3 px; **press**: scale 1 → 0.82 → 1 (6 f); **ripple**: a `data` ring Ø 64 → 160, opacity 0.8 → 0 (10 f) | Every "go to / tap / turn on / select" | anchors (§8.6), insert record (origin creator) |
| **P-FOCUS-DIM** | annotation | Everything except the target row or button dims to 35 % luma; the target keeps full brightness and a 2 px `data` outline | 6 f in, before the tap; holds until the next target | Every tap on a busy screen | anchor `focus_row` |
| **P-TAP-RIPPLE** | annotation | The orb's ripple on a created UI (no recording) | As above | Taps inside `fx.appUI` | anchor |
| **P-TOGGLE-FLIP** | state | An iOS-style switch 120×72 (or the real one highlighted): the knob slides, the track fills `accent`, 4 white sparks | Knob 6 f (ease back), fill 6 f, sparks 8 f | "Turn this on" | event on the spoken "on" |
| **P-UI-GLITCH-SWAP** | state | One UI label inside the recording (a button or a row) glitches into the creator's aside ("Post" → "Wait! ✋") while the orb rests on it | 7 f of seeded RGB slices (±8 px) on that element only, then the new label holds ≥ 1 s (v05 @ 7.00–7.23) | A "but wait / don't tap yet" beat during a step; a surprise, so it works once | `exception: E6` (`data-slot` = the button) |
| **P-SETTING-REVEAL** | overlay | A settings row (icon + label + switch) blurred 14 px | Unblurs 14 → 0 px over 24 f; the label is sharp before the switch flips | Hook of HA-05, "a setting you didn't know" | row text ≥ 40 px |
| **P-PILL-LABEL** | overlay | The step pill (SM-1) at y 190 | Pop 7 f; the text swaps with a 4 f cross-fade | Every new screen; replaces captions on L-ui | — |
| **P-ARTICLE-HIGHLIGHT** | overlay | The creator's article screenshot via `fx.shot` on W-ui-light (or `fx.headlineCard` created); an `accent` highlighter box wipes over the spoken phrase | Enters by T-2 (a white resolve); a slow drift 1.0 → 1.25 over ≈ 0.75 s, then a **fast push to ≈ 4×** onto the phrase over 18 f (ease in-out, motion blur in the middle 6 f); the highlighter wipes L → R in 8 f once the push lands (a glowing `accent` box); hold ≥ 0.6 s; exit **T-13 iris carry** (v01 @ 5.5–8.3) | "Instagram announced…", "the bank's own page says…" | insert record; the beat carries `source {masthead, date, headline}` and `highlight_spans`; the headline quoted word for word |
| **P-PROFILE-CHIP** | overlay | A glass chip at the chest (L-set-dim): avatar Ø 96, "Name &#124; Niche" 40 px, three stats 40 px; a `winner` highlighter wipes over the niche phrase | Rise 10 f; the highlighter 8 f on its word | Introducing an account (the creator's own, or an illustrative one: `illustrative: true`, no label) | numbers in figures |
| **P-TIMER-RING** | state | A ring stopwatch Ø 120 beside the chip: 01:00 → 00:59, the ring depletes | 1 tick per second (E6 digits), the ring sweeps linearly | Only when the script states a time ("in 60 seconds") | `exception: E6`, figure |
| **P-NOTIFY** | overlay | A generic notification card 900×150 at y 240, app glyph square (the creator's logo file, or initials), title + body | Drops from y 110 to 240 with a spring (10 f), holds ≥ 1.5 s, slides up 6 f | A real event from the creator's own screen; created from the script's words when it illustrates | insert record |
| **P-IN-APP** | stage | L-in-app: the presenter in a 900×1280 card at y 640, platform chrome above (story progress bar, an avatar row, a P-STAT-PILL) | G-5 shrink-to-card 12 f; the chrome settles 8 f | "When you post it…", "people see this in their feed" | created chrome |
| **P-DM-THREAD** | overlay | `fx.appUI(kind: "chat")`: bubbles type in, `accent` bubbles for "me", grey for others, initials avatars | One bubble per spoken line (typing dots 8 f → bubble pop 6 f) | "They DM you…", "reply with…" | created; no real names |
| **P-SHEET-SLIDE** | state | A bottom sheet slides up inside a created UI (rounded 36 px top, `panel`) with 3–5 options; the chosen one gets the orb | Sheet 10 f (ease out); option highlight 4 f | Menus and pickers in created UIs | created |

**B-4 Verdict**
| ID | Type | On screen | Motion recipe | When | Needs |
|---|---|---|---|---|---|
| **P-WRONG-MARK** | annotation | A glowing `bad` square 120×120 (3 px border, 18 px glow) with ⚠ beside the wrong element; the element gets a `bad` box | The square pops 7 f; the box draws 8 f (perimeter) on the wrong word | "This is the mistake" | event |
| **P-RIGHT-MARK** | annotation | The same in `good` with ✓ | Same, on the fix word | "This is the fix" | event |
| **P-TRANSCRIPT-BLOCK** | overlay | The clip's or claim's words as a 3–6 line caps block at x 120, y 860–1200 (L-bubble / L-set-dim); a neon underline (4 px `primary`) runs under the active line | Words type in on their spoken onsets (from the clip's transcript or the script); verdict lines turn into `bad` / `good` boxes (8 f) | Teardowns, quoting a caption or script | quoted word for word |
| **P-TEARDOWN-BUBBLE** | stage | L-bubble over the dimmed clip (45 % luma) + P-TRANSCRIPT-BLOCK | G-4 10 f; the clip keeps playing underneath | Teardown sections | insert record (creator or created) |
| **P-VERDICT-WORLD** | stage | The world flips to W-verdict-red, then to W-verdict-green, carrying the B-4 graphic of that verdict | T-8 hard flip on the verdict word + a 4 f flash (≤ 40 % luma change) | The reel's one big wrong → right turn, as a single pair | — |
| **P-PEOPLE-GRID** | figure | A 12×14 grid of person icons (24 px, `muted`), a bracket label above ("ALL WANT TO LOSE WEIGHT", 40 px), a subset lit in the verdict colour | Icons fade in by row (1 f stagger); the subset lights 8 f; the bracket draws 8 f | "Who this is for", audience splits | the lit count is a stated number, or the grid is `illustrative: true` |
| **P-THOUGHT-BUBBLE** | overlay (light comedy) | A cloud bubble 300×200 beside the head (above the shoulder, never over the face or hair): the viewer's doubt in `bad` ("HEALTHY SWAPS?"), then the real desire in `good` ("I WANT SKINNY") | Squash pop 7 f; the text swaps with a 6 f colour flood | The audience's inner thought | text 44 px |
| **P-PROGRESS-BAR** | state | A video timeline bar at the chest (x 120–960, 10 px track, playhead dot) with "END"; label above: "PROBLEM SOLVED ✓" (`good`) | The playhead runs to END (24 f), the track fills `good`; then a `bad` segment grows past END with "NEW PROBLEM ⚠" | Open loops: "solve one problem, raise the next" | `progress` state var |
| **P-FUNNEL** | figure | 3 stacked trapezoids (top 520 wide, 120 tall each, 16 px gaps) labelled from the script (VIEWS / FOLLOWS / SALES), the active layer lit (`accent` / `data` / `good`) with ▶ ◀ arrows, the others ghosted 30 % | Layers drop in with a 6 f stagger; the active layer lights 6 f and scales 1.06; **never fully still**: the whole funnel drifts in 3D (tilts 5–10°, the layers spread 10–20 px over 0.6–1 s, ease in-out; v03 @ 60.8–61.5) | Models and stages; one layer per section | labels ≥ 44 px |

**B-5 Beat devices**
| ID | Type | On screen | Motion recipe | When | Needs |
|---|---|---|---|---|---|
| **P-HERE-CARD** | overlay (re-hook) | "HERE'S WHAT YOU DO" (or "BUT HERE'S THE CATCH") as a plain 2-line caps chunk at the chest, the CS-1 skin, white | Hard on (0 f) after a 1-word "SO" beat (≈ 0.3 s); holds ≥ 0.8 s; a relight and a Z-1 reframe on the same frame only when a section starts (§7.4) | The mid-reel re-hook | kind `rehook` |
| **P-COUNTDOWN** | state | W-stage black: "72:00:00" in the countdown type, unit labels under it | Swipes in with a 10 f blur slide; ticks 1 per second (E6) | Only a time limit the script states | `exception: E6`, figure / state `countdown` |
| **P-CELEBRATE** | overlay (light comedy) | The script's word ("Congratulations") at the chest in `winner`, 24 seeded spark bursts at the top corners (y 150–400, away from the face) | The word writes on with a 10 f L → R mask; sparks burst 18 f | The win the whole reel builds to; there's only one | — |
| **P-OUTLINE-STAT** | figure | A huge outline percent ("99%", 4 px `paper` stroke, no fill, 220 px) + a two-line caps label to its right | The stroke draws 10 f, the label pops 7 f | A shocking percentage from the script | figure (stated value) |
| **P-VIEWFINDER** | overlay (texture) | Camera brackets in the 4 corners (60 px arms, 4 px `paper`@70 %), "● REC" (red dot), "HD 4K", a running timecode | Fade 6 f; the REC dot blinks 15 f on / 15 f off | Sections about filming and creating content | z 5 |

**B-6 Set and camera**
| ID | Type | On screen | Motion recipe | When | Needs |
|---|---|---|---|---|---|
| **P-SET-SWAP** | stage | The `behind` set scene changes world (W-set-*) | Hard switch (0 f) on a cut point or phrase boundary | A section change: rare enough that each one feels like a new chapter | matte |
| **P-SET-RELIGHT** | stage | The set's glow colour changes (neutral → `bad` red rim, → blue rim) | **Hard switch (0 f)** on the caption-swap frame (v01 @ 23.58, 31.13; v04 @ 6.2); stack it with a Z-1 reframe, or hide it behind a T-14 sweep. Never a cross-fade | The wrong / right turns, a new section | matte |
| **P-THUMB-WALL** | stage | The set becomes a 3-column wall of the creator's own covers (SH-3), blurred 4 px, at 45 % brightness, drifting up 0.3 px/frame | 8 f cross-fade in; behind the presenter | "My content", "these posts", "people like me" | creator media only |
| **P-PUNCH** | camera | Z-1 cut reframe on a phrase boundary; Z-2 push / Z-3 pull between them | Z-1 1.0 → 1.18 on one frame (1.35 with 4K), held; Z-2 +14 % over 13 f; Z-3 −15–20 % over 16 f (§10.2) | Lounge or sofa takes move often, in and out; desk takes barely move (measured) | — |
| **P-OBJECT-CUTOUT** | overlay | The creator's object photo (cut out) at the chest, in front of the body, never the face; soft shadow `0 20 40 rgba(0,0,0,.5)` | Drop 30 px + fade 8 f; float ±4 px | The script names a physical thing (a product, a dish, a device) | creator asset (SH-7) or icon card |

**B-7 CTA**
| ID | Type | On screen | Motion recipe | When | Needs |
|---|---|---|---|---|---|
| **P-DM-KEYWORD** | overlay | The DM input pill at the chest (§6.7): the creator's avatar (Ø 84) left, a dark translucent pill (`#1B1B1B` @ 85 %, radius 48, x 200–940, cy ≈ 980), the keyword in **sentence case, Plus Jakarta Sans 500 58 px** as typed, and a `send` violet button (`#6060E0`, 124 × 84, radius 28) right (v04 @ 0:46) | The pill is on when the T-12 cut lands (or rises 10 f after a plain cut); the keyword types one character per 4 f, ≈ 8 cps (E6 inside the pill); send pulses 6 f; sends: rise 60 px + fade 8 f | CTA (`dm`) | kind `cta-keyword`, `exception: E6` |
| **P-COMMENT-PILL** | overlay | The comment variant (comment glyph + heart) | Same; the heart fills `bad` on send | CTA (`comment_keyword`) | kind `cta-keyword` |

### 8.4 Line → pattern lookup
Vocabulary, not a decision table: it tells you what this style reaches for. Ask what proves this moment, then use it.

| Line type | For example | Primary | Alternates |
|---|---|---|---|
| The claim / promise | "This one setting tripled my reach" | P-PHONE-PAIR + P-COUNTER-ROLL | P-HERO-COUNTER, P-VERSUS-TAG |
| A result over time | "6K, then 9K, then 81K followers" | P-HERO-COUNTER | P-CARD-CAROUSEL |
| A setting / feature exists | "There's a setting called Trial" | P-SETTING-REVEAL → P-TOGGLE-FLIP | P-PILL-LABEL |
| Where to click | "Go to your Professional dashboard" | P-PILL-LABEL + P-SCREENREC-ORB + P-FOCUS-DIM | P-SHEET-SLIDE (created UI) |
| A platform / company announced it | "Instagram is rolling out…" | P-ARTICLE-HIGHLIGHT | `fx.headlineCard` (created) |
| A specific post / item | "Like this post right here" | P-SIDE-PROOF | P-IN-HAND |
| The wrong way | "Most people post it like this" | CS-BAD + P-WRONG-MARK (+ P-SET-RELIGHT red) | P-VERDICT-WORD, P-PROGRESS-BAR (new problem) |
| The right way | "Instead, do this" | CS-GOOD + P-RIGHT-MARK (+ relight blue) | P-VERDICT-WORD "PROBLEM SOLVED ✓" |
| Quoting a caption / script / clip | "His hook says: if you're a snacker…" | P-TEARDOWN-BUBBLE + P-TRANSCRIPT-BLOCK | P-TRANSCRIPT-BLOCK on L-set-dim |
| What the viewer thinks | "You're thinking: healthy swaps?" | P-THOUGHT-BUBBLE | P-VERDICT-WORD |
| Who it's for | "Everyone in your audience wants X" | P-PEOPLE-GRID | P-OUTLINE-STAT |
| A model / stages | "Views, then follows, then sales" | P-FUNNEL | P-PROGRESS-BAR |
| A percentage that shifts | "83% followers → 100% non-followers" | P-DONUT-SHIFT | P-OUTLINE-STAT |
| Two options, one wins | "Normal vs Trial" | P-VERSUS-TAG | P-PHONE-PAIR |
| Linking two things | "Link your new reel to the old one" | P-LINKED-CARDS | P-SCREENREC-ORB |
| A time limit | "You have 72 hours" | P-COUNTDOWN | P-TIMER-RING |
| An incoming event / payment | "They'll DM you", "your refund lands" | P-NOTIFY (the creator's real one) | P-DM-THREAD (created) |
| Your content / you as the example | "Look at my page" | P-THUMB-WALL | P-PROFILE-CHIP |
| A physical object | "a salad", "this mic" | P-OBJECT-CUTOUT | `fx.card` icon card |
| The win | "You finally did it" | P-CELEBRATE | P-HERO-COUNTER + CS-WIN |
| Personal aside / story | "Last year I…" | P-SET-SWAP to W-set-warm + CS-SOFT | SH-6 aside clip |
| Filming / creating talk | "When you record your video…" | P-VIEWFINDER | — |
| The re-hook | "Here's what you do" / "But here's the catch" | P-HERE-CARD | P-COUNTDOWN |
| CTA | "DM me GUIDE" | P-DM-KEYWORD | P-COMMENT-PILL |

A moment the table doesn't cover gets a new device built from these families, in this style's language.

### 8.5 Data and truth
- Every counter, donut, outline stat, hero number and people-grid count is a figure in `plan/figures.json`.
- **Provenance:** `creator` (their own screen; the screenshot asset is named in the input's `said`), `script` (`said` =
  the words), `spoken@t`. A view count from somebody else's post is shown only from the creator's own screenshot of it.
- **Formulas:** `sum`, `diff`, `ratio`, `percent_change`, `per_period`, `unit_convert`; most counters are stated values.
- **Same scale:** a card pair or a versus tag compares one metric over one period; two bars share a `scale_id`.
- **Format:** K / M with 1 decimal, `$` (₹ lakh / crore for an Indian audience); written with `ctx.fmtNum`, never typed.
- **Illustrations** (a created profile "Your Name | Your Niche", a sample settings page, "Coffee $3.40 → $4.00") are
  `illustrative: true` in figures.json and carry no label. They explain; they never stand in for the creator's result.
  Never a made-up "viral rate", engagement score, payout or follower count presented as theirs.
- Counters land within ±5 f of the spoken number word.

### 8.6 Running state and anchors
| Var | Type | Display | Rules |
|---|---|---|---|
| `views` | counter | P-COUNTER-ROLL chips, P-HERO-COUNTER | One value per card; a counter only changes on an op on its number word; it never shows a value the creator didn't show or say |
| `countdown` | timer (`time_base: set`, no jumps) | P-COUNTDOWN, P-TIMER-RING | Starts at the stated limit ("72 hours" → 72:00:00) and ticks down 1 per second of edit time; shown only while the limit is the topic |
| `progress` | progress | P-PROGRESS-BAR | 0 → 100 % across its beat; the "new problem" segment is a second op |

Ops per beat: `state_ops [{var, op: set | tick_to, value, at}]`. Displayed values equal the state and the figures; the
countdown only ever goes down.

**Anchors.**
- **Targets:** `orb` (the cursor position per tap), `tap` (the tapped element's box), `highlight` (an article phrase's
  box), `focus_row` (the row kept bright by P-FOCUS-DIM).
- **Keyframes:** in the anchor pass, read each recording's frames (`veos sheet`) and for every tap write `{t, x, y, w, h}`
  of the target in screen pixels into `plan/anchors.json`. The recording is 1080 wide on L-ui, so recording px × (1080 /
  recording width) = screen px; add the push scale of P-SCREENREC-ORB. The orb scene interpolates between keyframes with
  the orb travel recipe, and lands within 24 px of the tapped element.
- **Fallback** (`static_near_target`): when a target moves (a scroll), place the orb at the target's position at the tap
  time and hold it there; don't track.
- **The head:** anchored elements stay 40 px clear of the head region (it matters on L-bubble and L-in-app, where the face
  shares the frame).

### 8.7 Comedy layer (`comedy: light`)
- The gags: P-THOUGHT-BUBBLE, P-CELEBRATE, P-OBJECT-CUTOUT used playfully, a P-BANNER-TILT. Each carries information.
- Never two in a row, never in the CTA, beside the face and hair rather than on them. No meme sounds (§11), no stickers, no freeze-frame
  roasts: this style is hype and proof, not a roast.

### 8.8 Assets
- Real captures first: the creator's recordings and results screens beat any created UI (§1 step 2).
- A real article, post or product page the creator doesn't have: the real one, captured from the web (§12.4).
- Created UIs are generic and unbranded (`fx.device`, `fx.appUI`): no look-alike logos, no real usernames.
- Logos: the creator's files first, else the real logo fetched from the web; `fx.logoPlate` (the name set in type) only
  when none can be found.
- Redact personal identifiers in every recording (blur 18 px, for their whole time on screen) (§2).
- Third-party moments: fetch the real thing, source noted (§12.4).

---

## §9 Transition system

### 9.1 Library
| ID | Transition | Frames | Recipe | Cue role |
|---|---|---|---|---|
| **T-1** | Hard cut | 0 | On a word boundary ±1 f; set swaps and L-ui ↔ L-set returns | — |
| **T-2** | Bloom flash + white resolve | 5 + 6 | A UI element (toggle, pill) blooms into a white glare: glare scale 1 → 4, opacity 0 → 0.95 over 5 f, then cut to white; the next page **resolves out of the white** over 6 f (content opacity 0 → 1, blur 12 → 0 px, scale 0.92 → 1) (v01 @ 4.29–4.75). Into a light page without a glowing element, the white resolve alone follows a hard cut (v03 @ 9.43–9.60). **Built-in:** the white is a core `flash` transition, `{"t": <cut>, "type": "flash", "colour": "#FFFFFF", "peak": 0.95, "pre": 5, "frames": 11}` (rises over the 5 f glare, peaks on the cut, decays over the 6 f resolve); the glare sprite on the UI element and the page's own 6 f entry (blur 12 → 0, scale 0.92 → 1) stay in the scenes | transition |
| **T-3** | Whip-in | 4 | The incoming screen slides in from the right edge over 4 f with 40 → 0 px horizontal motion blur, over the outgoing frame, which holds (v04 @ 19.03). **Built-in:** the incoming scene takes `in: "slide-r", in_frames: 4` (opaque from its first frame, over the held outgoing frame) and paints its own directional blur, `filter:${ctx.blur(40 * (1 - e), 0)}` (e = the entry's eased progress); the outgoing scene's `t_out` sits 4 f after the incoming `t_in`. `smear: true` is the quick form, but its velocity smear caps at 24 px | transition |
| **T-4** | Scale-blur push | 6 | Outgoing scales 1 → 1.25 with 0 → 16 px blur and fades; incoming 0.85 → 1 with 12 → 0 px blur | transition |
| **T-5** | Screen cross-fade | 6 | Two recordings or UI states cross-fade (the orb stays on top, continuous) | — |
| **T-6** | Dim down | 8 | `via: dim` (G-3) while the chest card rises | — |
| **T-7** | Bubble shrink / grow | 10 | `pip-shrink` / `pip-grow` (G-4), ease back | transition |
| **T-8** | Verdict flip | 0 + 4 | The world hard-flips red ↔ green on the verdict word; a 4 f luminance pulse of ≤ 40 %: built-in `{"t": <verdict word>, "type": "flash", "peak": 0.4, "pre": 0, "frames": 4}` | reveal |
| **T-9** | Glitch shatter | 17 | P-BANNER-GLITCH (the banner exit only) | transition |
| **T-10** | Zoom-through | 10–12 | The camera dives into a phone card 1 → 5× (radial blur on the last 4 f: the `zoom-through` preset's built-in radial camera `blur`, keyed to its last 4 frames); the card's screen becomes the L-ui recording | transition |
| **T-11** | Shrink-to-card | 12 | The L-ui screen shrinks into a 9:16 side card (P-SIDE-PROOF) as the stage cuts back to L-set; ≤ 84 px/frame of travel | — |
| **T-12** | Glitch cut | 2–5 | Over the cut: 5–9 seeded horizontal slices shift ±30 px with ±8 px R/B fringes; the last frame is clean (v01 @ 37.42 2 f, v05 @ 21.83 5 f). **Built-in** (core draws it over the composited frame, under the captions): `{"t": <cut>, "type": "glitch", "frames": 2-5, "pre": 1-2, "slices": 7, "offset": 30, "rgb": 8, "posterize": 0}` (posterize off: the measured picture stays near-clean, so the slices and the RGB split carry the cut; the 8 px mosaic blocks are not drawn). Variant when leaving a chat or DM screen: 3 f of scanlines + 10 px blur (v04 @ 44.73) = built-in `{"type": "blur-through", "px": 10, "frames": 3, "pre": 1}` | transition |
| **T-13** | Iris carry | 4 | A circle mask centred on the highlighted phrase shrinks the article (Ø ≈ 800 → 0 in 4 f, ease-in) to reveal the presenter underneath; the highlight box itself stays and becomes the step pill at the chest (v01 @ 8.13–8.29) | transition |
| **T-14** | Graphic sweep | 6 | The next beat's own icon (a link glyph, an arrow, a card) whips diagonally across the frame, top-right → chest, with motion blur (the glyph scene paints `filter:${ctx.blur(px, angle)}` along its travel: angle ≈ 117°, px ≈ 0.3 × its per-frame travel, ≤ 40); the outgoing graphic shrinks to the centre (4 f) and the set relight or cut happens on the frame it passes the face (v01 @ 30.83–31.17) | transition |

### 9.2 Grammar
| Boundary | Use | Never |
|---|---|---|
| Frame 0 | The banner already built + the proof entering | A fade-in from black, a static first frame |
| Hook → beat 1 | T-9 (warning / news) or T-3; T-11 evolve when the winner card becomes the first screen | A cross-fade of the whole frame |
| L-set → L-ui (into a step) | T-3; T-2 into an article or light page; T-10 into a phone card | A slow dissolve |
| Screen → screen | T-5 (the orb persists), a hard cut on the tap result, or T-3 | T-2 twice in a row |
| L-ui → L-set (proof done) | **T-12** (default), T-13 after an article, T-1 + Z-1, or T-11 | A fade back to the face |
| Graphic → graphic on the presenter, with a relight | T-14 | Two sweeps in a row |
| Into a card over the presenter | T-6 | Covering the face |
| Into / out of a teardown | T-7 | — |
| The wrong → right turn | T-8 (with P-VERDICT-WORLD) or P-SET-RELIGHT | Cutting the verdict colour before its word |
| Set change | P-SET-SWAP / RELIGHT, hard, on the caption-swap frame at a section boundary | A swap mid-sentence, a cross-fade |
| Last word | Hard end ≤ 6 f after the last word | A black tail > 0.2 s |

### 9.3 How the moves breathe
- The glitch cut is this style's comma: it snaps the viewer back from a screen to a face, so it lives at the end of a
  step, where proof hands over to trust. It loses its snap if it lands everywhere.
- The bloom and the white resolve mean "a new page opens": into articles and light screens, never two in a row.
- The banner shatter happens once, at the hook, because there's one banner. The verdict flip is the reel's one big turn.
- The sweep hides a relight; the whip-in starts a step; the zoom-through dives into a phone. Each move carries a meaning,
  so pick it for that meaning, and change the move from one boundary to the next unless the same meaning repeats (T-5
  inside one multi-screen step).
- Inside a step, the orb is the motion. Let it travel, press and ripple without a transition fighting it.

---

## §10 Motion tokens, camera and zoom, layers, finishing

### 10.1 Motion tokens (30 fps)
| Token | Value |
|---|---|
| Lead | 2 f before the trigger word |
| Entries | `cubic-bezier(0.22, 1, 0.36, 1)`, 6–10 f |
| Exits | `cubic-bezier(0.64, 0, 0.78, 0)`, 5–6 f |
| Pop / back | `cubic-bezier(0.34, 1.56, 0.64, 1)`, 7 f, overshoot 6 % |
| Card rise | 40 px + fade, 8 f, stagger 3 f |
| Colour flood | 1–2 f hard, then the glow bloom settles over 6 f |
| Caption swap | 0 f (hard); CS-SOFT fades 6 f in, 8–10 f out |
| Set relight / swap | 0 f, on the caption-swap frame |
| Glitch cut / white resolve / iris / whip-in | 2–5 f / 6 f / 4 f / 4 f |
| Graphic drift (W-stage, W-ui-dark) | Never fully still: 3D tilt 5–10° and layer spread 10–20 px over 0.6–1 s, ease in-out |
| Flare sweep | 12 f, 60 px white bar at 20°, 40 % |
| Counter roll | 18 f (hero steps 18 f each), lands ±5 f on the number word |
| Orb travel | 10–16 f, ease in-out, ≤ 84 px/frame |
| Orb press / ripple | 6 f / 10 f |
| Toggle | 6 f knob + 6 f fill + 8 f sparks |
| Glitch (banner exit) | 17 f: red flip, fractures, 3 f slice shatter |
| Typewriter | 1 character per 4 f (≈ 8 characters/s) |
| Banner float | ±6 px, 2 s sine |
| Stage morphs | dim 8 f, pip-shrink / pip-grow 10 f, shrink-to-card / grow-from-card 12 f, fade-through 10 f |
| Holds | titles ≥ 10 f after built; text ≥ 0.25 s per word |

### 10.2 Footage camera (`zoom_policy: presets`)
| ID | Preset | Recipe | Tone / use |
|---|---|---|---|
| **Z-1** | `snap-punch` | A **cut reframe**: 1.00 → 1.18 on one frame, pushed **off-centre toward the free side** (preset `origin: "free_side"`, built-in; measured 1.15–1.35, v03 @ 35.4, v04 @ 6.2), held to the next move; no zoom tween, no blur | `hype`, `win`, `right`; a section start (with the relight and the caption swap on the same frame) |
| **Z-2** | `push-drift` | 1.00 → 1.14 over 13 f, ease out (preset `ease: "out"`; the engine's push-drift is linear otherwise) (v03 @ 34.7) | `explain`, `story`, `proof`, a claim building |
| **Z-3** | `pull-out` | 1.18 → 1.00 over 16 f, ease out: −15–20 % (measured −19 %, v03 @ 37.0). After a Z-1 on a cut it eases the punch back over 15–17 f (v04 @ 6.2–6.7); preset `from: "inherit"` starts it from the current crop and pivot, so no snap | Releasing a punch, the CTA, revealing a side card |
| **Z-4** | `shake` | ±8 px, 6 f, 1.02 bump | A `wrong` verdict landing, a counter landing on a big win |
| **Z-5** | `zoom-through` | 1 → 5× over 10–12 f with a radial blur on the last 4 f (= T-10) | Into a phone card |

**The camera follows the take.** On a lounge or sofa take with gestures (v03, v04) the camera breathes in and out: a cut
reframe or a push in, then a pull back out, often enough that the frame feels alive. On a desk take (v01, v02) it barely
moves, because the graphics carry the motion. Change the kind of move from one to the next so it never feels mechanical,
and never stack two moves on top of each other (keep about 0.4 s between them). Never a 3 f zoom tween with blur (it's
not in the original reels). The set scales with the presenter because it's drawn inside the footage group. Pushes into
articles and recordings are scene-level scale (`fx.shot` push, the P-SCREENREC-ORB push), not a canvas camera.

**Limits that protect the picture:** a punch never goes past 1.18 on a 1080p source (1.35 needs 4K, §12.3) and never pushes
the chin below y 880, where it would collide with the chest band.

### 10.3 Tone decides the treatment
| Tone | Caption | Set | Camera |
|---|---|---|---|
| `hype` | CS-1 | keep | Z-1 snap-punch |
| `explain` | CS-1 | keep | Z-2 push-drift |
| `proof` | CS-DATA | W-stage or L-ui | Z-2 push-drift |
| `wrong` | CS-BAD | W-set-neon-red relight | Z-4 shake |
| `right` | CS-GOOD | W-set-neon-blue relight | Z-1 snap-punch |
| `win` | CS-WIN | keep | Z-1 snap-punch |
| `story` | CS-SOFT | W-set-warm | Z-2 push-drift |
| `cta` | CS-1 | keep | Z-3 pull-out |

### 10.4 Layer order (back to front)
1. The set backdrop: `behind: true` scene, z 1, inside the footage group
2. Footage, then the presenter cut-out (engine)
3. The world (visible only when the stage is `hidden` / `pip` / `card`); L-ui recordings and created UIs at z 3
4. Proof cards, charts, chest cards (z 3–4)
5. Counter chips, the step pill, labels (z 5); the viewfinder texture (z 5)
6. The cursor orb, ripples, ⚠ / ✓ squares, highlighter boxes (z 6)
7. Captions (z 7)
8. The glow banner, verdict words, the re-hook, the DM pill (z 8)
9. Light comedy: the thought bubble, the celebration (z 9)
10. Flare sweeps, glitch sparks on single elements (z 11, momentary). T-2 / T-8 flashes and T-12 glitch cuts are core
    transitions (`timeline.transitions[]` with a `type`), drawn over the picture under the captions: never z 11 scenes

### 10.5 Finishing
- Glow only on type (the banner, verdict words, caption keywords), proof borders (winner / loser / right / wrong), the orb
  and the step pill.
- The sets carry noise 0.02–0.04 and a 0.35–0.45 vignette; the footage gets no grain and no grade.
- Cards: radius 22 (phone cards), 32–40 (chips, UI cards); soft shadows `0 20 50 rgba(0,0,0,.55)`; no hard offset
  shadows.

---

## §11 Sound

| Line | Decision |
|---|---|
| **Cue moments** | `hook` (the f0 hit, the loser flood, the winner flash), `reveals` (counter landings, toggles on, verdict colours, the celebration), `transitions` (T-2 riser into the white, T-3 / T-14 whoosh, T-9 / T-12 glitch, T-10 whoosh), `cta` (a key tick per typed character and the send). Orb taps take a cue only when they change the screen. No list cue |
| **Meme cues** | None: the comedy is light and visual |
| **Music bed** | On; enters when the banner exits (after the hook) |
| **Ducking** | The bed sits ≥ 18 dB under the voice; the audio of the clip in a teardown plays ducked under the voice, and only when the presenter is silent |
| **Loudness** | −14 LUFS integrated, true peak ≤ −1.5 dBTP, hard end ≤ 6 f after the last word |

The bundled SFX pack and its global rules choose the sounds; every cue sits on a visible event you declared in a scene's
`events`. Sound marks a landing; it never decorates. If a moment's proof is quiet (an orb gliding to a row), let it be
quiet.

---

## §12 Footage handling

### 12.1 Setups
| Setup | Spec |
|---|---|
| **A (main)** | Seated at a desk, chest-up, lens at eye height ~1 m away. Head top y 300–420, chin y 700–820, face centre x 420–660 on the 1080×1920 frame. Key light 45°, a rim light behind (it sells the cut-out against the dark set). Plain dark top (no stripes, no green). Any background: it's replaced. 30 fps, 4K preferred (punches) |
| **B (aside, optional)** | The creator using their phone, or in a second room: 2–4 s clips for story asides |

### 12.2 Shots and fallbacks
| ID | Shot | Spec | How much | Must / optional |
|---|---|---|---|---|
| SH-1 | Screen recordings of the app or tool taught | Portrait, native resolution, dark mode if the app has it, notifications off, one recording per step, 4–12 s each, no fast scrolling | One per step | must |
| SH-2 | Own proof screens | Analytics, dashboards, results with the real numbers being claimed (screenshot or recording) | One per claimed result | must |
| SH-3 | Own covers / thumbnails | 6–20 images of the creator's own posts | For card pairs, carousels, the wall | optional |
| SH-4 | Article / announcement screenshot | The creator's, else the real page captured from the web (source noted), full width | One per news claim | optional |
| SH-5 | The clip being torn down | The creator's own clip or one they hand over, else the real one fetched from the web (source noted) | One per teardown | optional |
| SH-6 | Aside clip (setup B) | 2–4 s | One per story aside | optional |
| SH-7 | Object photo | PNG or plain background, the object the script names | One per object | optional |

| ID | For | What the engine does instead | What it costs | Result |
|---|---|---|---|---|
| FB-0 | The cut-out | Keep the real room: no set swap; P-SET-RELIGHT becomes a 20 % colour wash over the frame edges (vignette mask, face untouched) | The virtual set is lost | degraded |
| FB-1 | SH-1 | `fx.appUI` (settings / list / browser / chat) recreating the described screen generically, orb taps on the named rows | Not the real product UI; exact menu positions can't be copied | degraded |
| FB-2 | SH-2 | Counters and cards only from numbers stated in the script (`from: script`), neutral dark card faces | No real screenshot behind the number | degraded |
| FB-3 | SH-3 | Dark gradient cards with the post's title in type (the creator's own titles from the script) | Covers read as a pattern, not a portfolio | degraded |
| FB-4 | SH-4 | No page to be found: `fx.headlineCard`, the outlet set in type, the verbatim headline, `accent` highlight bars | No real masthead | holds |
| FB-5 | SH-5 | No clip to be found: `fx.quoteCard` / a transcript block of the clip's verbatim lines + `fx.silhouette` for the person | No moving source clip | degraded |
| FB-6 | SH-6 | P-SET-SWAP to W-set-warm + Z-1 on setup A | No second location | holds |
| FB-7 | SH-7 | `fx.card` icon illustration of the object on a glass card at the chest | No photographic object | holds |

When you show the storyboard, name every fallback used and why.

### 12.3 Props, the reaction bank, the cut-out, resolution
- **Props:** the creator's phone, to hold up on "this app" (then P-IN-HAND isn't needed).
- **Reaction bank** (2 s each, recorded at the shoot): an excited "you did it" grin, a wince, pointing down at the chest
  band, pointing to the side (the side-card side), counting on fingers.
- **The cut-out:** required, for the whole take. Feather 2 px, choke 1 px, temporal smoothing. Check the hair edge at
  200 % on three frames (the start, a gesture, the end); a cut-out with holes or a halo over 3 px on the hair means FB-0.
- **Resolution:** a 1080p source allows punches up to 1.18; 1.35 and the tight reframes of the original reels (≈ 1.5×)
  need a 4K source.

### 12.4 Third-party moments: fetch the real thing
When the script names a real article, announcement, post, clip, product or brand, the viewer should see the real one.
This style's usual moments: **an announcement or article** (P-ARTICLE-HIGHLIGHT), **another creator's clip**
(P-TEARDOWN-BUBBLE), **an app's UI** you didn't record (P-SCREENREC-ORB), **a notification or payment** (P-NOTIFY), **a DM
or comment thread** (P-DM-THREAD), **a brand logo**.
1. **The creator's own files** in their folder come first.
2. **Otherwise search the web and fetch it:** the real article or announcement (captured and framed on the headline), the
   real post or clip, the real product page, the real logo. Note where it came from.
3. **Use it as it is** (crop, frame, highlight, redact identifiers), never altered to say something it doesn't; a post or
   headline is shown word for word.
4. **Nothing usable to be found, rebuild it from its exact words:** article → `fx.headlineCard`; clip → transcript block +
   `fx.silhouette` / `fx.quoteCard`; app UI → `fx.appUI`; notification → a generic P-NOTIFY with the script's words;
   DM → `fx.appUI(kind: "chat")` with initials avatars; logo → `fx.logoPlate`. No labels, no credit lines.
5. **Proof stays the creator's.** A notification, payment, DM or result shown as theirs comes only from their own screen;
   a fetched or created screen is never passed off as the creator's own capture.

### 12.5 Frame rate and audio
30 fps CFR, 1080×1920, BT.709. One voice track: high-pass 80 Hz, de-ess, light compression, −14 LUFS.

---

## §13 What your plan should settle

Your `ideas.md` is a page or two, for you. In this style it has decided, before any code:
1. **The tone of every line,** and so every beat's caption profile, set and camera move (§10.3).
2. **The hook:** the archetype, the banner (with its two alternates) and its line-2 colour, the proof element at f0, every
   hook beat to the frame, the loser and winner words, the frame the verdict lands on (by 2.5 s), the banner's exit.
3. **The claim → proof table:** every claim, its proof, its source (recording / screenshot / fetched / created / stated
   number), the word it lands on; unproven claims proven or cut, and named when you show the storyboard.
4. **The sets:** the world of every beat, every relight and swap on its caption-swap frame.
5. **The axis per beat:** `bad` · `good` · `winner` · `none`, and the word its colour lands on.
6. **Every step:** the pill text, the move into the screen, the orb keyframes (from the anchor pass), the focus row, the
   tap word, the proof that holds, the return.
7. **The numbers and the state:** a figure with provenance for every counter, donut, grid count and hero number; the
   state ops for `views`, `countdown` and `progress`; `exception: E6` on counter, countdown and typing scenes.
8. **The re-hook,** the escalated last proof, and the moves between scenes in exact numbers (§9).
9. **The inserts** (the creator's / fetched, with the source / rebuilt) and the fallbacks used.
10. **The sound:** the cue moments and the bed's entry.
11. **The CTA:** the device, the keyword (`meta.keyword`), the deliverable named in the spoken line.
12. **The moments you'll look at hardest on the storyboard:** f0 (the thumbnail: the banner readable, the proof entering, the head clear of
    the banner); the winner flash (≈ 2.3 s); one L-ui tap with the orb on its row; one verdict beat; the re-hook; one
    L-in-app frame if used (the caption under the chin, the chrome above the card); the CTA pill.

The reel header and one hook, fully decided:
```yaml
meta:
  format: F-A
  hook_archetype: HA-05          # or HA-02 / HA-01 / HA-07 / HA-18
  structure: tutorial            # variant: walkthrough | teardown | funnel | result-cash-in
  keyword: "TRIAL"
  sets: [W-set-skyline, W-set-neon-red, W-set-neon-blue]
  figures: [views_normal, views_trial]
  state: {views: counter, countdown: null, progress: null}
  mask_words: []                 # extra words to mask beyond the default list

hook:
  name: "Hidden setting, toggle proof"
  archetype: HA-05
  banner: {line1: "INSTAGRAM", line2: "CHEATCODE", line2_role: primary, platform_gradient_on: "INSTAGRAM"}
  alternates: ["INSTAGRAM / HIDDEN SETTING", "FREE REACH / NOBODY USES"]
  pair: {promise: "a setting that shows your reel to non-followers first", proof: "Settings row -> Trial toggle on"}
  storyboard: "f0 banner + blurred row | 0.8 row sharp | 2.0 toggle on + sparks | 3.0 T-2 bloom into L-ui"
  sound: [hook hit f0, reveal on the toggle, transition on the bloom]
  stopper: {thumbnail: pass, mute: pass, read_s: 0.5, payoff_s: 2.0}
```

---

## §14 Worked examples

Times are estimates; the real onsets come from the cut. Each one shows the standard: match it, then beat it.

### 14.1 Social-media growth, walkthrough, HA-05: "The setting that shows your post to strangers first"
**Banner:** INSTAGRAM / CHEATCODE (line 2 `primary`; "INSTAGRAM" in the platform gradient). **Keyword:** TRIAL.
**Length:** ≈ 48 s. **Assets:** SH-1 two recordings (settings, drafts), SH-2 one insights screenshot with the two view
numbers.

| t (s) | Spoken | Tone | Visual | Caption | Camera / layout | Cue moment |
|---|---|---|---|---|---|---|
| f0 | — | hype | W-set-skyline; banner built; settings row "Trial" blurred under it (P-SETTING-REVEAL) | — | L-set | hook |
| 0.0–0.8 | "There's a setting on Instagram…" | hype | The row unblurs 24 f | — | — | — |
| 1.3 | "…almost nobody uses" | hype | P-BANNER-TILT on "nobody" | — | — | — |
| 2.0 | "…and it's free reach" | proof | **P-TOGGLE-FLIP** on "free": knob, `accent` fill, sparks | — | — | reveal |
| 3.0 | "You didn't even know…" | hype | T-2 bloom out of the toggle; banner blur-up; P-SET-RELIGHT to blue | CS-1 "YOU DIDN'T / EVEN KNOW" | Z-1 | transition |

| Section | Spoken (gist) | Tone | Layout / set | Patterns |
|---|---|---|---|---|
| PROBLEM 3–9 s | "Normally your post goes to followers first, and if they don't bite, it's dead" | wrong | L-set, W-set-neon-red relight | CS-BAD; P-DONUT-SHIFT (the followers' slice from SH-2, `from: creator`) in the side slot away from the face; P-WRONG-MARK on "dead" |
| REHOOK 9–11 s | "Here's what you do" | hype | L-set, relight blue | **P-HERE-CARD** + Z-1 (`rehook: true`) |
| STEP-1 11–19 s | "Make your reel, hit next, scroll down" | explain | L-ui (SH-1 #1) | P-PILL-LABEL "New reel → Next"; P-SCREENREC-ORB: the orb to "Next" (14 f), press on "hit"; T-5 to the options screen; P-FOCUS-DIM on "Trial" |
| STEP-2 19–25 s | "Turn on Trial" | right | L-ui | Orb press on "turn on" → the real toggle; P-TOGGLE-FLIP highlight; step pill "Trial: ON" |
| PROOF 25–34 s | "Same post. Normal got 34K, Trial got 134K" | win | T-11 back to L-set; the side card, then the proof band | **P-VERSUS-TAG** Normal vs Trial cards, both counters roll (figures `from: creator`), the "FREE" tag stamps on Trial; CS-WIN |
| WHY 34–42 s | "Because strangers see it first, so it's judged on the content, not your follower count" | explain | L-set, W-set-skyline | P-DONUT-SHIFT 83% followers → 100% non-followers (stated), CS-DATA |
| CTA 42–48 s | "DM me TRIAL and I'll send you my posting checklist" | cta | L-set, Z-3 | **P-DM-KEYWORD** "TRIAL", typed ≥ 1.5 s |

State and figures: `views_normal` (34,000, creator), `views_trial` (134,000, creator), `share_followers` (83%, script),
`share_non` (100%, script). Inserts: none fetched or rebuilt (all the creator's own).

### 14.2 Personal-finance apps, result pair, HA-01: "Your bank app hides this toggle"
**Banner:** SAVINGS / BAD → GOOD ("BAD" red from f0, "GOOD" ignites gold on its word). **Keyword:** ROUNDUP.
**Length:** ≈ 62 s. **Assets:** SH-2 two balance screenshots (the creator's own savings pot before and after six months,
$0 and $406), no recording of the settings (→ FB-1, a created settings UI).

| t (s) | Spoken | Tone | Visual | Caption | Camera / layout | Cue moment |
|---|---|---|---|---|---|---|
| f0 | — | hype | W-set-skyline; banner; **P-PHONE-PAIR** ghosted: left = the empty savings pot, right = the same pot six months later | — | L-set | hook |
| 0.0–0.27 | — | — | The cards land | — | — | — |
| 1.4 | "This is my savings pot before…" | wrong | The left card floods red, counter "$0" | — | — | reveal |
| 2.2 | "…and this is it six months after one toggle" | win | The right card: a hard gold flood, the counter rolls to "$406" (`from: creator`), flare sweep; "GOOD" ignites | — | Z-1 on "toggle" | reveal |
| 3.2 | — | hype | Banner blur-up; the cards slide down 60 px + fade | CS-1 "ONE / TOGGLE" | — | transition |

| Section | Spoken (gist) | Tone | Layout / set | Patterns |
|---|---|---|---|---|
| PROBLEM 3–12 s | "Most people say they'll save what's left at the end of the month. There's never anything left" | wrong | L-set → W-set-neon-red relight | CS-BAD; P-THOUGHT-BUBBLE: "I'LL SAVE LATER" (red) → "THERE'S NOTHING LEFT" stays red; P-PROGRESS-BAR: the month runs to END, the balance segment empty |
| REHOOK 12–14 s | "But here's the catch" | hype | relight blue | **P-HERE-CARD** "BUT HERE'S / THE CATCH" (`rehook: true`) |
| STEP-1 14–24 s | "Open your app, go to Settings, then Savings" | explain | L-ui, **created** settings UI (FB-1) | P-PILL-LABEL "Settings → Savings"; `fx.appUI(kind: settings)` + P-TAP-RIPPLE on each spoken menu; P-SHEET-SLIDE |
| STEP-2 24–31 s | "Turn on round-ups. Every purchase rounds up to the next dollar" | right | L-ui (created) → L-set-dim | P-TOGGLE-FLIP on "on"; then T-6 → a P-PROFILE-CHIP-style chest card showing "Coffee $3.40 → $4.00, +$0.60 saved" (numbers from the script, `illustrative: true`, no label) |
| WHY 31–43 s | "60 cents doesn't feel like anything. That's the point. 26 purchases a week…" | explain | L-set, W-set-skyline | CS-DATA; **P-HERO-COUNTER** steps $15.60 a week → $68 a month → $406 by month six (figures: `per_period` from the script's inputs; the six-month step is the creator's screenshot value, and 26 weeks × $15.60 = $405.60 rounds to it) |
| PROOF 43–52 s | "And that's my actual pot" | win | T-11 the hero counter → a side card of the SH-2 "after" screenshot (gold border) | P-SIDE-PROOF; CS-WIN; P-CELEBRATE is **not** used here (it waits for a bigger win) |
| ASIDE 52–56 s | "I didn't change a single habit" | story | W-set-warm swap | CS-SOFT |
| CTA 56–62 s | "Comment ROUNDUP and I'll send you the 3 settings I turn on first" | cta | L-set, Z-3, W-set-skyline | **P-COMMENT-PILL** "ROUNDUP" |

Figures: `pot_before` 0 (creator), `pot_after` 406 (creator screenshot), `per_buy` 0.60 (script), `buys_week` 26
(script); `week` = 0.60 × 26 = 15.60; `month` = `per_period` (52 / 12) → 67.60, shown "$68" (`round_to` 1); `six_months` =
15.60 × 26 weeks = 405.60, shown "$406" and equal to `pot_after` at display precision. Rebuilt inserts: I1 settings UI
(`recreated_ui`, standing in for the bank app's settings screen, which the web can't show for their account).

### 14.3 Fitness coaching, teardown, HA-18: "Why this coach's clip got 1.2M views"
**Banner:** CLIENT HOOK / S**T → GOLD. **Keyword:** HOOKS. **Length:** ≈ 75 s. **Assets:** SH-5 the creator's own
client's clip (the creator's file, with permission: origin creator), its view count from the creator's screenshot (1.2M), the
client's first version of the clip (3 views).

| t (s) | Spoken | Tone | Visual | Caption | Camera / layout | Cue moment |
|---|---|---|---|---|---|---|
| f0 | — | hype | W-set-skyline; banner (S**T red, GOLD `muted` until its word); **P-PHONE-PAIR** ghosted: version 1 / version 2 of the client's clip, both playing (`ctx.videoFrame`) | — | L-set | hook |
| 1.5 | "Same coach, same video: this one got 3 views…" | wrong | The left card red, counter "3" | — | — | reveal |
| 2.2 | "…this one got 1.2 million" | win | The right card gold, the counter rolls to "1.2M"; "GOLD" ignites | — | — | reveal |
| 3.0 | "The only difference? The hook" | hype | Banner blur-up; the gold card scales up to fill the frame (12 f) and becomes the dimmed clip under the bubble as the stage shrinks to L-bubble | CS-1 "THE / HOOK" | G-4 at 3.4 | transition |

| Section | Spoken (gist) | Tone | Layout / set | Patterns |
|---|---|---|---|---|
| CLIP 3–14 s | The client's opening line plays, then "Listen to how it starts" | proof | **L-bubble** over the dimmed clip | **P-TEARDOWN-BUBBLE** + P-TRANSCRIPT-BLOCK typing the clip's verbatim words; P-PROFILE-CHIP of the client (their own account, the creator's screenshot) with the niche highlighted |
| WRONG 14–26 s | "Version one opens with 'healthy swaps'. Nobody wakes up wanting healthy swaps" | wrong | L-bubble | The transcript line "HEALTHY SWAPS" turns into a red box + P-WRONG-MARK; **P-VERDICT-WORD** "WRONG DESIRE" |
| THOUGHT 26–31 s | "What they actually think is: I want to look good" | right | T-1 to L-set (setup B aside if recorded, else setup A) | **P-THOUGHT-BUBBLE**: "HEALTHY SWAPS?" red → "I WANT TO LOOK GOOD" green |
| RIGHT 31–44 s | "Version two says: 'low-calorie snacks that actually taste good'" | right | L-bubble | The transcript block re-types the new line, green boxes + P-RIGHT-MARK; CS-GOOD when the presenter speaks over it |
| REHOOK 44–46 s | "And here's why that matters" | hype | L-set, relight blue | **P-HERE-CARD** "HERE'S / WHY" (`rehook: true`) |
| WHO 46–62 s | "Out of everyone who sees it, only some are snackers… but all of them want to lose weight" | explain → right | **P-VERDICT-WORLD**: W-verdict-red, then W-verdict-green | P-PEOPLE-GRID: the lit subset in red is `illustrative: true` (no stated count), the full grid lights green on "all of them" (T-8) |
| PROOF 62–69 s | "Speak to the desire, not the method" | win | L-set, W-set-skyline | P-SIDE-PROOF of the gold card; CS-WIN |
| CTA 69–75 s | "DM me HOOKS and I'll send you 20 openers like this" | cta | L-set, Z-3 | **P-DM-KEYWORD** "HOOKS" |

Inserts: I1 the client's clip (`creator`, the creator's file), I2 the client's profile chip (`creator` screenshot). Without
them: I1 → a transcript block + `fx.silhouette` (FB-5); counters only from the creator's stated numbers (FB-2).

---

## §15 Your look at the storyboard: the checklist

Watch it once as a stranger with a thumb over the next reel, then once as the editor whose name is on it. Fix what
bothers you, in one pass.

**The style (does it feel like §The feel?)**
- Frame 0: the creator on a set, the glow banner fully built and readable, the proof already entering; the verdict by
  2.5 s; the first three seconds read on mute.
- Every claim has its proof within a breath, and the proof gets bigger toward the end.
- Every step follows the ritual: pill → screen → the orb gliding, dimming, pressing on the verb → proof that holds →
  back to the face.
- Colour means something every time it appears: red wrong, green right, gold winner, cyan the tap; three bright hues at
  most; primary only in type.
- The right caption profile per tone run; captions hard-swap, 1–4 caps words, one glowing keyword at most.
- Sets change at section boundaries, hard, on the caption-swap frame; the real room never shows.
- The camera follows the take (alive on a sofa, nearly still at a desk), never past 1.18 on 1080p.
- The re-hook lands in the middle; the last proof is the biggest; the reel ends on the pill.
- Start to end: at every moment you could point at the proof of what's being said.

**Craft (by eye, in context)**
- The creator's face reads whenever the moment is about them: the banner below the chin on L-set; the L-in-app chrome
  above the card; nothing over the bubble. Nothing chops the head or buries the face by accident.
- No text over text by accident: one occupant in the chest band; captions out of the way under the banner, z 8 cards and
  on L-ui.
- Every visual lands on its word; orb taps on the verb; verdict colours on their word, never before; counters on the
  number word; cuts on word boundaries; nothing teleports, nothing lingers after its point.
- Every number is what was said, in K / M (or ₹ lakh / crore) format; illustrations carry no labels; nothing invented,
  fetched or created is presented as the creator's result.
- Names, apps and menus spelt exactly; profanity masked everywhere; the banner's count = the items shown; every "I'll
  show you" shown; the CTA keyword typed, readable and equal to `meta.keyword`.
- Identifiers blurred in every recording; created chats use initials and generic names; quotes, fetched posts and
  transcript blocks word for word.
- Meaning text inside x 64–1016, y 110–1500 and out of Instagram's bands; red and green text only on dark ground.
- The file itself (1080 × 1920, 30 fps, −14 LUFS, the bed under the voice, a hard end ≤ 6 f after the last word, no black
  tail) is the render's job; it checks it.

---

## §16 Build notes

- **Fonts:** Montserrat 800/900, Plus Jakarta Sans 500–800, Inter Tight 500–800 (tabular), Pinyon Script 400, JetBrains
  Mono 500, Permanent Marker (a masked swear word over CS-HYPE), Noto Sans Devanagari 800. Pre-paint → ✓ ⚠ ● ₹.
- **Determinism:** every particle, flare, bokeh disc and glitch slice comes from `ctx.rng(seed)` / `ctx.rngStable(seed)`;
  no `Math.random`, timers or CSS animations in scenes.
- **E6 hard swaps:** counter digits, countdown digits and the typed keyword change inside a fixed container (`data-slot`,
  the rect constant within 4 px); the container's own entry and exit stay eased. Declare `exception: "E6"` on those
  scenes (P-COUNTER-ROLL, P-COUNTDOWN, P-TIMER-RING, P-UI-GLITCH-SWAP, P-DM-KEYWORD, P-COMMENT-PILL).
- **Scene building blocks** (write them as helpers at the top of `plan/scenes.js`, then reuse them across the reel):

| Block | Role |
|---|---|
| `Set` | The `behind: true` z 1 scene painted from `ctx.tokens.worlds[...]` (gradient, glow, seeded bokeh, noise, vignette); hard switches for swaps and relights; 60 % glow under L-set-dim |
| `GlowBanner` | `kind: "banner"`, z 8, two fit-width lines, the float, ignite / tilt events, blur-up or glitch exit (P-GLOW-BANNER, P-BANNER-*) |
| `PhoneCards` | The card pair and carousel with ghosting, floods, the gold bloom, flare sweeps and counter chips (P-PHONE-PAIR, P-CARD-CAROUSEL, P-COUNTER-ROLL) |
| `ScreenOrb` | The recording full-bleed with its push, the orb travelling between `plan/anchors.json` keyframes, press, ripple and focus-dim (P-SCREENREC-ORB, P-FOCUS-DIM, P-TAP-RIPPLE) |
| `StepPill` | The pill at y 190 with its pop and cross-fade swap (P-PILL-LABEL) |
| `Verdict` | Marks, verdict words, transcript boxes and the verdict world (B-4) |
| `KeywordPill` | `kind: "cta-keyword"`, the typed keyword, the send pulse and the send (P-DM-KEYWORD, P-COMMENT-PILL) |
| Camera and cuts | Z-1…Z-5 = `timeline.camera` presets; T-2 / T-8 / T-12 = `timeline.transitions` entries (`flash`, `glitch`, `blur-through`); stage moves = `timeline.stage` with `via` |

---

## Appendix A. Evidence map
The full map (every element → `vNN @ m:ss`), the fidelity audit (2026-10-06), the completeness pass at full frame rate
(2026-10-07) and the unverified list are in `evidence.md`. In short:
| Element | Source |
|---|---|
| The banner on f0 at the chest | v01–v05 @ 0:00–0:03; block cy 1011 (v05), 820 px wide; Montserrat Black |
| The red / gold card pair with counters | v02 @ 0:00–0:03 (red 1.46–1.54, gold 2.21), v04 @ 0:00–0:03, v01 @ 0:13–0:19 |
| Cursor-orb recordings | v01 @ 0:39–0:53, v04 @ 0:40, v05 @ 0:05–0:21 |
| Sets and hard relights | v01 red → blue @ 0:00–0:04 (hard at 23.58, 31.13), v03 skyline → kitchen @ 0:21, v04 @ 6.2 |
| Glowing-keyword caps captions, hard swaps | v01 @ 0:20–1:15 (swaps at 22.00, 23.58), v02 @ 1:23–1:39 |
| DM keyword pills | v02 @ 1:40, v03 @ 1:08, v04 @ 0:45 (typing 1 character per 4 f) |

Not copied from the original reels: invented-looking metrics and receipts presented as real ("VIRAL RATE 79%", payment
notifications, DMs from named public figures), stock hand-held phone footage, a drawn platform glyph, money rain. Not
verifiable: the speech language (no transcripts), all sound.

## Appendix B. Hook-title bank
Slots in brackets are filled per reel. Line 1 / line 2 (glow colour).

| # | Banner | Archetype | For example |
|---|---|---|---|
| 1 | NEVER POST / [THING] (`bad`) | HA-02 | NEVER POST / AT NIGHT |
| 2 | [PLATFORM] / CHEATCODE (`primary`) | HA-05 | INSTAGRAM / CHEATCODE |
| 3 | [THING] / BAD → GOOD (`bad` → `winner`) | HA-01 | YOUR HOOK / S**T → GOLD |
| 4 | YOU FINALLY / DID IT! (`good`) | HA-07 | a viral post |
| 5 | [PLATFORM] / BIG UPDATE (`primary`) | HA-02 | INSTAGRAM / BIG UPDATE |
| 6 | STOP [HABIT] / [RESULT] (`bad`) | HA-02 | STOP DELETING / OLD POSTS |
| 7 | [N] VIEWS / → [M] VIEWS (`winner`) | HA-01 | 3 VIEWS / → 1.2M VIEWS (the creator's real numbers) |
| 8 | HIDDEN / [FEATURE] (`data`) | HA-05 | HIDDEN / ROUND-UPS |
| 9 | WHY THIS / WENT VIRAL (`winner`) | HA-18 | a teardown of a real clip (the creator's, else fetched) |
| 10 | [TIME] TO / CASH IN (`primary`) | HA-07 | 72 HOURS / TO CASH IN |
