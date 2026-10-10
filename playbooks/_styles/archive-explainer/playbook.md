# Archive Explainer Style Playbook (template v2)

## The feel

This reel is a documentary cut down to one minute, and the viewer is never asked to take anyone's word for anything. It
opens on a face from the archive, tight, already drifting, with a black box of white typewriter letters underneath naming
who this is. Before the first sentence is over, the picture has changed again and again: the frame jumps wider, a wall of
banknotes rises up the screen and lifts away, the event is waiting underneath, and then the person nobody expected. By the
end of that first breath the whole story has been told, and all that's left is the why.

Then the receipt. A hard cut to a field of deep blue, empty for a beat, and the headline types itself on, word by word,
faster than the voice. On the spoken figure the rest of the sentence dims and the key words turn lime; a dot pops, and a
thin line runs off toward the people involved. That's the engine of this style: the voice makes a claim and the screen
produces the paper. A name, and there's their face. A place, and a pin drops on it. A year, and the digits roll to it.

The pace is fast because the pictures change, not because anything shouts. No whooshes for their own sake, no shakes, no
memes, no stickers. The voice is calm and certain; the boxed caption carries every sentence, so it works on mute; the
energy lives in the cut. It builds like an investigation: context, receipts stacking up, a question turned back on the
subject's face, a comparison flipping side to side, and then one picture held, the only slow moment, while the answer
lands. Three colours do all the talking: the creator's blue is the world, the black box is the voice, and lime means
"this is the receipt". Lime never decorates.

When it's the creator's own conversation, the same voice goes quiet: two people, a cut on every handover, the line that
works alone at the very first frame, blue boxes under it, and nothing else.

**The test:** pause on any frame and everything on it is the thing being named, the receipt for it, or the person saying it.

## What this playbook is

You're editing a reel in one of two formats that share one visual voice (the boxed caption as the headline, one brand
blue, a branded end card), and you have the authority to make it the most gripping short documentary in the creator's
niche. **F-A Archive explainer** (the default): a voice-over with no presenter becomes a fast documentary short. **F-B
Podcast clip**: a 30–60 s moment from the creator's own two-camera conversation. The style was pulled from the original
creator's reels (v01, v02 archive explainers; v03 a podcast clip) and measured at full frame rate. Read it all, every
time; take what fits this reel, invent where a moment needs more, and never ship a frame that breaks the feel above.

**Who it's for and what it needs.** Creators who explain why something happened, who is behind it and how it works:
business, power, places, history, sport. F-A needs only a voice-over and its script (45–80 s); the creator's own photos,
clips, article screenshots and maps make it a documentary; what they don't have is fetched from the web (the real photos,
articles and maps), and only what can't be found is built (§12). F-B needs two (or three)
synced camera files and one audio track per person, or one wide shot. No cut-out anywhere. Captions follow the creator's
language: English by default, Hinglish romanised in the same boxes, Hindi through the renderer's Noto Sans Devanagari
fallback (the box stays; the mono look is lost on those words, so English or Hinglish keeps the style truest). Numbers
are on the 1080×1920 frame at 30 fps. Machine values live in `tokens.json`; where this text gives a number tokens also
holds, they agree.

### Style directives (non-negotiable)
| # | Directive | Where it lives |
|---|---|---|
| D1 | **The caption is the banner.** Never add a title slab, pill or kinetic headline; the first boxed chunk at f0 is the headline | §5.2, §5.3, §6.6 |
| D2 | **Literal pictures only.** A person is that person (their real photo, or a silhouette plate with their name when none can be found); a place is that place (a photo, a locator card); a number is a figure card or the receipt that states it. Never mood stock | §8.4, §2 |
| D3 | **Receipts, not paraphrase.** A cited claim shows its source exactly as written (outlet, date, headline word for word); the key span turns lime on the spoken word | §7.3, §8.6, P-SOURCE-CARD |
| D4 | **Pictures move on the words.** F-A: every cut and card event lands on a chunk boundary or a noun onset (±2 f), and no picture just sits; F-B: a cut within ±3 f of every handover | §7.5, §9 |
| D5 | **Blue world, black-box captions, lime receipts:** three colour jobs, never a fourth bright hue beyond the comparison chips and the two end-card words | §4 |
| D6 | **Fetch the real thing.** Every third-party picture is the creator's own file, else the real one fetched from the web (source noted), else a created plate; quotes and headlines word for word | §12.4 |
| D7 | **Calm authority.** No memes, stickers, emoji, shakes or crash zooms; the energy comes from the cut, the in-card builds and a rare stinger | §8.7, §10.2, §9.4 |
| D8 | **End on the brand.** Every reel ends on the branded end card, ≤ 3.5 s, with the creator's action readable ≥ 1.5 s | §6.8 |

### Quick index
| § | What |
|---|---|
| §1 | Procedure: how to approach a reel in this style (F-A, then F-B) |
| §2 | Hard rules: the craft and the style's never-list |
| §3 | Worlds, layouts, stage moves G-1…G-7, safe zones, the person |
| §4 | Colour: roles, meanings, archive treatments GR-… |
| §5 | Type and captions: CS-A mono box, CS-B blue boxes, other text, language and numbers |
| §6 | Hook system: stopper test, HA-11 (F-A default), HA-14 (F-B default), alternates, hook pairs, headline chunks, CTA and end cards |
| §7 | Structure and rhythm: the receipt ritual, the comparison ritual, open loops, rhythm by feel |
| §8 | Visual system (B-roll and patterns): families B-1…B-8, 43 patterns, line → pattern lookup, data, citations, assets |
| §9 | Transition system T-01…T-09, grammar, F-B shot grammar R-1…R-8 |
| §10 | Motion tokens, camera, tone, layers, finishing |
| §11 | Sound |
| §12 | Footage handling: setups, shots and fallbacks, resolution, inserts |
| §13 | What your plan should settle |
| §14 | Worked examples (3) |
| §15 | Your look at the storyboard: the checklist |
| §16 | Build notes |
| App. A / B | Evidence map / hook-title bank |

---

## §1 Procedure: how to approach a reel in this style

You listen, plan, build and look at the storyboard yourself; the edit skill has the mechanics. This style lives
or dies on three decisions: the thesis said in the first breath, a picture decision for every caption chunk, and a receipt
for every claim that comes from somewhere.

**Pick the format from the input.** A voice-over file is F-A; two or more camera files of a conversation are F-B. One
format per reel, never mixed: a podcast clip never gets archive cutaways, and an archive explainer never shows the creator
talking.

**F-A (voice-over archive explainer)**
1. **Find the thesis.** One sentence: the subject named concretely, what it just did, and the twist ("The King of FIFA just
   launched a new scheme to make money, and it involves Donald Trump."). Then the turn ("Here's why.") and the answer the
   payoff will show. If the script doesn't say its thesis in the first three seconds, say so when you show the storyboard.
2. **Tag the archive bank.** For each file the creator gave or you fetched, one line: subject (person / place / object / document), date
   or era, look (colour, B&W, sepia, halftone, VHS), aspect. Anything under 1080 px on the short side lives only inside a
   card (P-PHOTO-CARD), never full-bleed.
3. **Fetch the rest** (§12.4): list the people, places, events, headlines and quotes; what the creator didn't give, find
   on the web (the real photo, the real article, the real map) and note the source; build a plate only for what can't be
   found.
4. **Feel the tone of every line:** `explain` · `evidence` · `turn` · `warn` · `awe` · `cta`. Tone picks the world (§10.3):
   evidence goes to the blue, turns and awe go to the archive.
5. **Write the hook** (§6): the archetype, 8–10 chunkings of the thesis, the 3–5 pictures that carry it, the one topical
   stinger object. Pick by the stopper test; keep two alternates.
6. **The picture-per-chunk pass** (this style's core craft). Build the caption chunks first, then give every chunk a
   picture decision: **cut** (a new archive picture or card), **event** (something happens inside the current card: a
   highlight, a pin, a bar, a thumb) or **hold**. A hold is right only when the chunk before it cut; a run of holds is the
   picture going dead. This is where the rhythm is made.
7. **Capture every receipt.** For each cited claim: masthead, date, the headline word for word (from the real article,
   fetched and read, else the script, the transcript or text the creator pasted), the highlight spans, and the article's
   own first sentence for the body. A headline you can't find word for word isn't shown: the caption carries the claim.
8. **Plan the figures.** Every number drawn on a card is in `plan/figures.json` with its spoken words; computed ones show
   their formula (§8.5).
9. **Plan the moves and the sound:** where the stinger goes, where the re-hook turns back on a face, where the comparison
   flips sides, the one held picture before the answer, the bed's drop-out (§9, §11).

**F-B (two-camera podcast clip)**
1. **Choose the moment.** Pick the stretch whose **first sentence is the strongest standalone line** (it has to land in the
   first second) and whose last sentence is a **button**, a quotable conclusion. Trim the in-point to the first word of
   that sentence (±2 f); keep 1.5–2.5 s of non-essential tail after the button (a laugh, "yeah", a breath) for the end
   card (§6.8).
2. **Name the speakers** (host, guest) and map the angles: which camera shows whom; faux crops from the wide where a camera
   is missing.
3. **Write the hook as in-points:** several candidate first sentences, picked by the stopper test (§6.1).
4. **Lay the cut grammar** with the turn generator and this style's cut rules (§9.3), then hand-edit only the wide
   establish (R-4) and a stack exchange (R-5).
5. **Mark the button** and protect it: no cut inside it unless it's a handover.

---

## §2 Hard rules: the craft and the style's never-list

**Craft, by eye** (judge it on the storyboard, in context, the way an editor does):
- **Keep the faces clear.** F-B: keep every speaker's face, hair and the room above the head clear of layers, captions
  included; the geometry is in §3.6. F-A has no presenter, but a face inside an archive picture gets the same respect:
  cards, chips, plates, particles and caption boxes sit off it. Plates sit under the chin or beside the head with ≈ 40 px
  clearance; full-bleed faces are framed in the top 60 % (face centre y 520–900) so the caption band stays below the
  chin. A caption brushing a chin for a beat is editing; a face buried or a head chopped by accident is not. Behind a
  person is fair game, text included (`behind: true`), but this style has no cut-out, so in practice nothing goes there.
- **No text over text.** The caption band (y 1330–1505) belongs to the caption: while a chunk shows, graphics stay above
  y 1290 and nothing else sits in y 1290–1540. Stingers and roll-bys pass *under* the caption. One tag in the top slot at a
  time.
- **On the word.** Every cut or card event lands 2 f before its trigger word and is settled within +5 f; a receipt
  highlight lands on the first word of its span ±3 f; a counter lands within ±5 f of the spoken number. Captions lead by
  1 f and are never on screen more than 0.15 s before their first word. F-B: a cut 1 f before a new speaker's first word,
  within ±3 f, never inside a word.
- **No dead air.** F-A voice-over pauses are tightened to ≤ 0.6 s inside a paragraph and ≤ 1.0 s between paragraphs; the
  caption holds through pauses of 0.4 s or less, and the picture keeps moving (the settle's drift, the follow-push creep).
  F-B keeps the conversation's own pauses, and a listener beat before the button is welcome.
- **Receipts word for word.** Every source card carries masthead, date and headline. The headline is word for word from
  the real article (fetched), the script, the transcript or text the creator pasted, never paraphrased, shortened mid-sentence or re-ordered; every
  highlight span occurs in the headline. Quotes are word for word and attributed. An F-B clip is never re-ordered to change
  a speaker's meaning.
- **Numbers right.** Every number on a card, chart, map or plate comes from `plan/figures.json` (or sits inside a
  word-for-word headline) and is written by `ctx.fmtNum`; captions show numbers as spoken. Illustrations may use made-up
  but realistic detail with no label (`illustrative: true`), but in this style anything that reads as a fact (a figure, a
  date, a headline, a vote count) is real, because in a documentary every number on screen is a claim.
- **Real, and noted.** A third-party picture (a photo of a person or place, an article, a map, a logo) is the creator's
  own file, else the real one fetched from the web with its source noted, else a created plate (§12.4). Never an AI
  image of a real person.
- **Privacy.** Emails, phone numbers and ID numbers visible in any screenshot are blurred for their whole time on screen.
- **Spelling.** Proper nouns exactly as in the glossary (every proper noun in the script goes in it before captions are
  built); outlet names as the outlet writes itself ("Financial Times", not "FT", unless its own masthead uses the short
  form). The source reel's caption typo ("lenghts") would fail.
- **Readable.** Captions 58 px (F-A) and 60 px (F-B); labels 40 px; text holds ≥ 0.25 s per word and labels ≥ 10 f after
  they finish. Meaning text inside x 64–1016, y 110–1500; nothing but picture in the right column (x > 970) between y 900
  and 1540; a top-slot tag never above y 128. Full-bleed pictures are ≥ 1080 px on the short side and never upscaled past
  1.35×.
- **Promise integrity.** Every open loop ("here's why", "now why…") is paid on screen; the end card holds ≤ 3.5 s with
  its action (keyword, URL, QR, Follow) readable ≥ 1.5 s.
- **Determinism.** Particles and stinger rows use `ctx.rng(seed)`; letter resolves use `fx.resolve` with a `seed`; nothing
  reads the clock.
- **Audio.** −14 LUFS integrated, true peak ≤ −1.5 dBTP, the bed ≥ 18 dB under the voice, a hard end ≤ 6 f after the last
  spoken word, a black tail ≤ 0.2 s.

**Never in this style:**
- Stock clichés: spinning globes, typing hands, "business people" handshakes, generic city timelapses. If there's no literal
  picture, build the plate (§12.2).
- A headline, quote or statistic that's paraphrased, cut mid-sentence or re-ordered and still shown as the source's words.
- Memes, emoji, stickers, meme sounds, shakes, crash zooms, RGB splits, light leaks, film burns; dissolves or fades between
  pictures (the cut is the grammar).
- A title slab, pill, lockup or title card. Coloured, bold or bigger words inside captions; a caption without its box; two
  caption styles in one reel (the F-B guest italic is the one exception).
- Lime as decoration (frames, backgrounds, underlines of non-key words); a second highlight colour on receipts; bars, boxes
  or underlines on a created receipt.
- Credit lines, source lines or labels under pictures. The receipt is the citation; a picture is just the picture.
- A map, flag or border drawn from memory as if accurate (fetch the real one); another company's logo drawn (fetch the
  real one); real currency art, mastheads or serial numbers in a stinger; fake photos or AI images of real people.
- Fake UIs or dashboards presented as real; a cross-promo card that shows anything but the creator's own video (no view
  counts).
- Captions on the end card; an end card longer than 3.5 s.
- In F-B: archive cutaways, B-roll, zoom presets, or graphics over the speakers beyond the optional name plate, the HA-03
  question plate and the end card.

---

## §3 Worlds, layouts, stage moves, safe zones

### 3.1 Worlds
| ID | Kind | Look | Carries | Enter / exit |
|---|---|---|---|---|
| **W-blue** | card-world | `primary` `#1A2FAA`, film noise 0.03, no grid, no vignette | Receipts (P-SOURCE-CARD), maps, photo cards, comparison cards, plates set in type | Hard cut on a chunk boundary (T-01); the stinger (T-02) out of the hook |
| **W-archive** | archive | Black `#000000` behind full-bleed archive pictures and created plates (the picture *is* the world) | Faces, places, events, objects, dates: the montage | Hard cut (T-01), stinger (T-02), roll-by (T-03) |
| **W-green** | stage | `data` `#1B473A`, noise 0.03 | Figures: seat arcs, bars, flows, counters, on a `data_card` `#19613B` card | Hard cut |
| **W-white** | canvas (light) | `#FFFFFF` flat | The P-WATCH-FULL cross-promo video card only | Hard cut in, hard cut out to the end card |
| **W-end** | void | `end_bg` `#0A1314`, noise 0.05 | P-END-TAGLINE | Hard cut, then the card builds (T-06) |
| **W-qr** | card-world | `primary`, flat | P-END-QR (F-B, and F-A when the device is `qr`) | Hard cut |
| **W-room** | footage | The creator's own podcast set (F-B) | The speakers | Shot cuts (`timeline.shots`) |

F-A lives between the blue and the archive, drops to the green when a number needs drawing, visits the white only for
the cross-promo card, and ends on W-end or W-qr. Set the world with `timeline.world` on the same frame as the cut that
changes it. Full-bleed archive scenes are z2 and opaque, so W-archive only shows around a letterboxed picture.

### 3.2 Layouts
| ID | Engine | Rects (1080×1920) | Caption | Use |
|---|---|---|---|---|
| **L-A-canvas** | `hidden` (VO reel: no footage) | Scene rects inside it: **card** x 64, y 500, w 952, h 620, r 40 (centre y 810) · **tall** x 64, y 320, w 952, h 952, r 40 · **text** x 64–1016, y 240–1250 (receipts) · **bleed** 0, 0, 1080 × 1920 (archive) | CS-A, cy 1415 | Every F-A frame but the end card |
| **L-B-full** | `full` (the engine composes shots into the footage) | Speaker footage full frame; head top y 140–300; stack shots inside it via `timeline.shots` (seam y 960) | CS-B, cy 1405; on the seam during stack shots | Every F-B frame but the end card |
| **L-end** | `hidden` | End-card graphic x 64, y 160, w 952, h 1300 | captions hidden | The last 2.0–3.5 s of both formats |

F-A writes `"stage": [{"t": 0, "layout": "L-A-canvas"}, {"t": <end card t>, "layout": "L-end", "via": "cut"}]`. F-B writes
`"stage": [{"t": 0, "layout": "L-B-full"}, {"t": <end card t>, "layout": "L-end", "via": "cut"}]` and puts every camera
decision in `timeline.shots` (never in `stage`).

**Rect use (F-A):** one card rect per screen; the card rect and the text rect never share a frame; a **bleed** picture
never shares the frame with a card (cards sit on W-blue or W-green only). **Card** for landscape media and maps, **tall**
for portrait media, square maps and comparison cards, **text** for receipts and quotes.

### 3.3 Stage moves
| ID | Move | Recipe | Use |
|---|---|---|---|
| **G-1** | Hard cut | 0 f; the incoming scene `in: "none"`, `cuts: [0]`; the outgoing scene ends on the same frame | Every archive-to-archive, archive-to-canvas and card-to-card change: most of the reel |
| **G-2** | Card cut-in | The card hard-cuts in fully framed (no rise, no fade: v01 @25.37 green card, @47.84 map card); what moves is *inside* it: the avatar, pins or media build over the next 6–16 f | Every card after an archive run |
| **G-3** | Deck advance | The next comparison card hard-cuts in on top; the previous card stays visible as a 48 px strip at the left edge; the new media window fades up from blue-tinted (G-7). **Side change** (A → B): the old chips and card push up off the top edge in 4 f, the built-in transition `{"t": <side change>, "type": "push", "dir": "up", "frames": 4}` (v02 @34.24) | P-COMPARE-SWIPE sequences |
| **G-4** | Follow-push | When body copy or thumbs arrive, the whole receipt block scales 1.00 → 1.14 (1.10–1.16) and translates up-left so the newest element sits in the upper 60 %, over 24–27 f, sine in-out, then keeps creeping ≈ 1 %/s until the next event (measured v01 @14.52–15.40: ×1.145, −110 / −300 px) | P-SOURCE-CARD |
| **G-5** | Shot cut (F-B) | A `timeline.shots` boundary; 0 f | Handover, reaction, re-crop, wide |
| **G-6** | End cut + build | Hard cut to W-end; the end card builds in place (§6.8) (v01 @76.80, v02 @56.00: no dissolve) | P-END-TAGLINE |
| **G-7** | Inner punch + drift | Inside a map or figure card: a hard ×1.5–1.8 punch toward the focus on the spoken place or person (0 f), then a slow drift for the rest of the hold: pull-out ≈ 0.15 %/f or a pan of ≈ 9 px/f toward the next focus (v01 @29.97 seat arc ×1.8, @49.14 map ×1.52 then a pan south). Media windows fade up from 35 % over `primary` to 100 % in 14–16 f | P-MAP-CARD, P-LOCATOR-CARD, P-SEAT-ARC, P-COMPARE-SWIPE |

### 3.4 Layout diagrams

**F-A card on blue (L-A-canvas / card)**
```
┌─────────────────────────┐ 0
│  (IG top UI, keep clear)│ ← y 0–110
│                         │ ← top tag slot x 64, y 128 (the sponsor's "Paid partnership" only)
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
y 360   Outlet Name · 12 Mar 2025          ← mono 500 40 px, label_dim
y 404   Headline line one $20bn            ← Montserrat 700 70 px; key span lime, the rest muted after the highlight
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
│                         │
│   archive picture       │ ← z2, cover, settle 1.04 → 1.00, drift ≤ 1 %/s
│   (face in the top 60%) │ ← face centre y 520–900, chin above y 1290
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
│     face ~17 % of h     │        │   listener (bottom)     │   (1 line ≈ 913–1007)
│   ▇▇ blue box caption ▇▇│ ←1405  │   head top ≥ y 1050     │
└─────────────────────────┘        └─────────────────────────┘
```

**End cards (L-end)**
```
P-END-TAGLINE (W-end)              P-END-QR (W-qr, primary)
y 150  For more                     y 470  Watch the full conversation
y 290  <topic A> and   ← end_a      y 522  with <Name>
y 430  <topic B>,      ← end_b      y 574  at [ url.chip ]  ← paper box, ink text
y 570  decoded                      y 760  ┌──────────┐
y 920  (●logo) [Follow] [handle]           │   QR     │ 620 × 620, white
                                    y 1380 └──────────┘
```

### 3.5 Safe zones and bands
- Meaning text: x 64–1016, y 110–1500 (`layout.safe`); Instagram's UI takes y 0–110 at the top, the bottom 380 px and the
  right 110 px. The right column x > 970 between y 900 and 1540 carries no text.
- **Caption band:** y 1330–1505 (a CS-A 2-line box spans 1333–1497; CS-B 1316–1494). Graphics stay above **y 1290** while
  a chunk shows.
- **Top tag slot:** x 64, top y 128, one line, mono 22 px. Holds only the sponsor's "Paid partnership" (§6.8) or a series
  plate (§7.6). Never a credit, a source line or an "illustration" label.
- **Card zone:** y 320–1272 (tall) / 500–1120 (card). **Receipt zone:** y 240–1250. **End-card zone:** y 160–1460.

### 3.6 The person (F-B only)
F-A has no presenter: every frame is built, and the only faces are archive faces (§2). In F-B the speakers *are* the
picture, so keep their heads whole and clear.
- **Single (L-B-full):** the face is ≈ 17 % of the frame height, its centre at 36 % of the crop height (the engine
  default); the head top sits at y 140–300; don't crop through the chin or the top of the head. Re-crop step ×1.2 (a 4K
  source gives clean results; a 1080p source caps at ×1.35 in total).
- **The caption against the head:** CS-B centres on y 1405 (a 1-line box ≈ 1358–1452, 2 lines 1316–1494), a long way below
  a head whose top is at 140–300 and whose chin sits around the frame's middle. `avoid_face` is on: if a speaker leans and
  their face drops into the band, the caption moves to the chest. Check it on the storyboard anyway.
- **Stack shots:** the caption box centres on the seam (y 960): one line spans ≈ 913–1007, two lines ≈ 871–1049. The top
  cell's speaker must have their chin above y 870, and the bottom cell's listener their head top at y ≥ 1050 (hair
  included); frame the cells so they do, and keep stack chunks to one line when a head can't sit lower.
- Keep graphics off the faces: the name plate and the question plate sit clear of every head (§8.3 B-8).

---

## §4 Colour system

### 4.1 Role palette
| Role | Hex | One job | Text on it | Contrast |
|---|---|---|---|---|
| `primary` | `#1A2FAA` | Brand blue: the F-A canvas, the F-B caption box, the QR end card | paper | 10.3 : 1 |
| `accent` | `#CCF852` | Receipt lime: the key span, the leader dot, the active pin, the end-card action box | ink | 16.0 : 1 (8.4 : 1 as text on `primary`) |
| `end_a` | `#35CFD2` | End-card tagline word 1 | ink | 10.3 : 1 |
| `end_b` | `#C64D3C` | End-card tagline word 2 (display ≥ 112 px only) | paper | 4.6 : 1 |
| `side_a` | `#BA3221` | Comparison side A chip | paper | 5.9 : 1 |
| `side_b` | `#DDE3DB` | Comparison side B chip | ink | 15.1 : 1 |
| `bad` | `#E5483B` | A blocked route ×, a loss, a closed door | ink | 5.0 : 1 |
| `good` | `#3FBF6B` | An open route, a gain, allowed | ink | 8.3 : 1 |
| `data` / `data_card` | `#1B473A` / `#19613B` | The green figure world / its card | paper | 10.5 / 7.5 : 1 |
| `navy` | `#121B3A` | Map sea, plate backs, inner fills | paper | 16.9 : 1 |
| `land` / `focus` | `#7D8381` / `#E9EDE6` | Map land / the focus region and label chips | ink | 5.1 / 16.6 : 1 |
| `muted` | `#8C9AD8` (the source's `#6478BC` is 2.4 : 1, raised to the large-text floor) | Non-key headline words after the highlight, the leader line, body copy | — | 3.8 : 1 on primary |
| `label_dim` | `#C2D184` | The outlet + date line | — | 6.3 : 1 on primary |
| `end_bg` | `#0A1314` | End-card ground | paper | 18.8 : 1 |
| `ink` / `paper` | `#0B0B0B` / `#FFFFFF` | Text | — | — |
| CS-A box | `#000000` at 60 % (sampled 50–68 % over blue: `#060D37` on `#132595`, `#0D1A51` on `#1C33A5`) | The F-A caption container | paper | ≥ 8.4 : 1 on any ground |

**Brand colours.** `primary` and `accent` become the creator's two brand colours when they have them. `primary` must stay
one deep, saturated hue carrying white text at ≥ 7 : 1 (a pastel or light brand colour is nudged darker in OKLCH
lightness, same hue); `accent` must stay a light highlighter hue at ≥ 7 : 1 on `primary`. If the creator's colours fail
both, keep the defaults and tell them why in one line. `end_a` and `end_b` may follow the brand too; the side, good and bad
colours never change, because their meaning is fixed.

### 4.2 Meanings
- **Blue is this creator's world.** It's the only ground graphics sit on in F-A, and the only box colour in F-B.
- **Lime means "this is the receipt".** It marks the exact words or number the voice is citing, nothing else.
- **`side_a` red vs `side_b` off-white are the two sides of a comparison** (v02: Japan red, US white). The first-named side
  is always `side_a`. Never use them as good / bad.
- **`bad` / `good`** only on routes, doors and outcomes (the × at the end of a blocked route).
- Other companies' brand colours appear only inside their own real logo or picture (§8.8), never as a fill or a chip.

One world, one blue: there are no theme packs in this style; the creator's brand colour replaces `primary` directly.

### 4.3 Archive treatments (GR-…)
| ID | Filter | Use |
|---|---|---|
| **GR-bw** | `grayscale(1) contrast(1.12) brightness(0.98)` | The default for pre-1990 photos and portraits |
| **GR-sepia** | `grayscale(1) sepia(0.55) contrast(1.08)` | Newspaper-era photos, documents |
| **GR-halftone** | `grayscale(1) contrast(1.25)` + a 6 px dot-screen overlay at 22 % (multiply) | Created plates (always), print photos |
| **GR-vhs** | `saturate(0.85) contrast(1.05) blur(0.4px)` | Colour video clips from the 1980s–2000s |
| (none) | as it is | Recent colour photos and clips |

Consecutive archive shots change their look (untreated colour aside): the change of treatment is part of the cut, and in
a hook of three or more archive shots the eye should feel at least two different eras of print (v02 0:00–0:01: colour card
→ B&W → sepia halftone). A treatment never changes what a picture shows: no recolouring flags, no removing people.
Treatments are CSS filters on the scene; look at them on the storyboard.

### 4.4 Rules
- At most three bright hues in a frame: brand blue, lime, plus one of `side_a` / `bad` / `good` / `end_a` / `end_b`.
- Coloured text only on blue (lime, muted, label_dim) or on its own chip; never coloured words on a photo without a box.
- F-B footage is never regraded; archive pictures change only through §4.3.

---

## §5 Type and captions

### 5.1 Font map
| Slot | Family | Weights | Used for |
|---|---|---|---|
| `mono` | **JetBrains Mono** | 400 / 500 / 700 | CS-A captions, outlet lines, chips, name plates, the top tag, QR-card text |
| `display` | **Space Grotesk** | 600 / 700 | Map labels, date plates |
| `body` | **Inter Tight** | 700 / 800 | CS-B captions, end-card pills, video-card titles |
| `endcard` | **Montserrat** | 700 / 800 | The end-card tagline (800) and the receipt headline T-HEAD (700): the source uses one wide heavy grotesk for both, and Space Grotesk is too narrow |
| `numeric` | Space Grotesk | 700 | Counters and figure values |
| `serif` | Space Grotesk | 700 | An alias that keeps the inserts toolkit's masthead slot in style |

Brand wordmarks are image assets (SH-8) or the FB-8 monogram, never a font.

### 5.2 The headline element: none
There's no slab, pill, lockup or title card in either format (`type.headline.kind: none`). The first CS-A / CS-B chunk at
f0 *is* the headline: 2–5 words, readable in a second, naming the subject. Write it like a headline (§6.6).

### 5.3 CS-A: the mono box (F-A; `extends: lib:johnny_a`, tuned to the measured evidence)
| Group | Value |
|---|---|
| Mode | full · primary · mute-safe: every word is captioned, and the story reads on mute |
| Chunking | `unit: phrase`, 2–5 words, ≤ 18 characters per line, ≤ 2 lines; never split a name, number or unit; a new chunk on `. , ? !` (`punct_break`) and on pauses ≥ 0.3 s (`pause_split_s`), always on ≥ 0.9 s |
| Timing | lead 1 f; ≥ 0.25 s per word; tail 0.12 s; **hard swap** (0 f) of the whole chunk, no word build; `pause_hold_s` 0.4 (the last chunk holds through short pauses, so the band is never empty mid-paragraph) |
| Skin | JetBrains Mono **700, 58 px**, case as spoken (sentence case, punctuation kept: "Donald Trump."), tracking 0, white, no stroke, no shadow, line height 1.24 |
| Container | **one `box` per chunk**, as wide as the longest line (a short second line sits centred inside it), fill `#000000` at **60 %** (it reads navy on blue, charcoal on light photos), radius 0, padding 10 × 16 |
| Position | `fixed_y`, **cy 1415** (a 1-line box spans 1369–1461, a 2-line box 1333–1497), centred, max width 952; `avoid_face` on |
| Emphasis | **none**: no coloured, bold or bigger words; the receipt carries the emphasis |
| Hide | on the end card only. The caption stays **on top of** stingers and roll-bys (measured: "just launched / a new scheme" stays readable over the full banknote cover, v01 @1.30–2.13; "and it involves / Donald Trump." over the ball, @4.43–4.84) and over the cross-promo card (v01 @76.4, where it reads as a grey box on white) |
| Language | Latin script; English terms verbatim; spelling normalised; profanity masked `inner` (S**T); the glossary holds every proper noun in the script |

Measured on the 1080 frame, not the 720 px source: "The King of FIFA" spans 590 px in a 0.6 em mono, which is ≈ 61 px;
the "≈ 40 px" in early notes was the source unscaled.

### 5.4 CS-B: the blue boxes (F-B; `extends: lib:johnny_b`)
| Group | Value |
|---|---|
| Mode | full · primary · mute-safe |
| Chunking | phrase, 2–5 words, ≤ 20 characters per line, ≤ 2 lines, the same no-split and break rules (`pause_split_s` 0.35) |
| Timing | lead 1 f; hard swap; `pause_hold_s` 0.6 (conversation pauses) |
| Skin | Inter Tight **800, 60 px**, as spoken, white, soft shadow `0 2 4 rgba(0,0,0,.35)`, line height 1.45 |
| Container | **one box per line** (`box_per_line`, each shrink-wrapped to its line, stacked with no gap; measured v03 @11.40–11.83: "that's one dimension" / "of a place." are two boxes of different widths), fill `primary` at **85 %**, radius 0, padding 6 × 12 |
| Position | `fixed_y`, **cy 1405**; on `stack` shots the box sits on the seam (y 960, dy 0); `avoid_face` on (§3.6) |
| Speakers | host: white upright · guest: white *italic* (`captions.speakers`). The box colour never changes per speaker; italic is the quietest way to tell two voices apart |
| Emphasis | none |
| Hide | on the end card |
| Language | as CS-A; profanity mask `inner` (S**T), on by default |

Both profiles: chunks never mix speakers; captions come from the caption engine, never hand-built (`captions.overrides`
only: `{from, to}` spelling fixes, `{i, break: before}` to move a break so a name stays whole).

### 5.5 Other text
| ID | Element | Recipe | Hold |
|---|---|---|---|
| T-OUTLET | Outlet + date line on a receipt | mono 500 **40 px** (measured ≈ 40–44 px, v01 @0:15), `label_dim`, "Outlet Name · 12 Mar 2025" (the date as the source prints it); letters resolve in seeded random order over 16 f (14–18 f): `VEOS.fx.resolve(text, lt, {at, dur: 0.53, every: 2, order: "random", seed, ctx, font})` | the receipt's life |
| T-HEAD | Receipt headline | `endcard` (Montserrat) 700, **70 px** (64–76 by length: ≤ 3 lines at 952 px; measured ≈ 72 px, v01 @0:15), line height 1.04, tracking −0.03; white, then non-key words → `muted`, key spans → `accent` | ≥ 2.0 s after the highlight lands |
| T-BODY | Receipt body copy | mono 400 20 px, `muted` at 50 %, 3–5 lines, one span in lime (the spoken figure); decorative texture, because the headline beside it carries the meaning | with its receipt |
| T-CHIP | Side / trait chip | mono 700 40 px caps, tracking 0.04, pill radius 18, padding 12 × 24, `side_a` or `side_b` fill, a 44 px monogram disc or icon at the left (never a flag drawn from memory) | its card's life |
| T-MAPLABEL | Map / locator label | display 700 40 px caps, tracking 0.02, on a `focus` chip radius 10, ink text | its map's life |
| T-PLATE | Name plate | mono 700 40 px caps, white on a `#000000` 70 % box, radius 0, padding 8 × 16 (the caption's family) | ≥ 1.2 s |
| T-DATE | Date plate | display 700 140–220 px, white, tracking −0.03, on a halftone plate | ≥ 1.0 s |
| T-FIG | Figure value | numeric 700 72–160 px, white on green | lands on the spoken number, holds ≥ 0.8 s |
| T-TAG | Top-slot tag | mono 500 22 px caps, tracking 0.08, white at 80 %, x 64, y 128: the sponsor's "Paid partnership" or the series plate, nothing else | its segment |
| T-END | End tagline | Montserrat 800, 138 px (128–148), line height 1.0, tracking −0.04, left x 90, off-white `#E4ECE6` | the end card |
| T-QR | QR-card text | mono 700 40 px, white, line height 1.3, centred; the URL in a paper box with ink text | the end card |

### 5.6 Language and numbers
- English captions verbatim; brand and person names exactly as in the glossary; outlet names as the outlet writes itself.
- Numbers in captions are as spoken (the transcript's digits: "$20 billion", "211"); numbers on cards go through
  `ctx.fmtNum` (international grouping, `$`, long style: "$20 billion", "$2 million"), unless they sit inside a
  word-for-word headline ("$20bn" stays "$20bn").
- Hinglish: captions romanised as spoken (`transform: verbatim`) or translated to English; the mono boxes don't change.
  For an Indian creator, ₹ with lakh / crore: "₹1,20,000", "₹12.5 lakh".
- Hindi in Devanagari: the renderer falls back to Noto Sans Devanagari inside the same box; the mono look is lost on those words.
- Units metric; dual units only when the script says both.

---

## §6 Hook system

**The hook title in this style is the caption.** There's no on-screen title: the first one to three boxed chunks are the
headline, and they have to promise something: a person the viewer recognises doing something they didn't expect, and a
twist that makes them need the why. They're true to what the reel delivers and they're the creator's own spoken words, so
the script's first sentence *is* the hook title: when it's weak, say so and offer a stronger opening line. The post title
(outside the video) repeats the thesis in ≤ 9 words and follows the same rule ("How the King of FIFA made Trump his
partner", not "FIFA explained"). Write 8–10 chunkings and post titles, pick by the stopper test, keep two alternates.

### 6.1 The stopper test
| Test | F-A | F-B |
|---|---|---|
| Thumbnail | f0 at 25 % scale shows a literal subject (a face, a place, an object) and the boxed first chunk (58 px → 14.5 px, still a readable dark bar of 1–3 words) | — |
| Mute | the first 3 s of captions state the whole thesis (subject + event + twist) | the first sentence makes sense alone, on mute |
| Motion at f0 | the settle and drift already running on the f0 picture | live speaker footage |
| Read time | each hook chunk ≤ 5 words, readable in ≤ 1.0 s | each chunk readable in ≤ 1.2 s |
| Payoff | the thesis complete by 3.0 s, on a scene tagged `payoff: true` | the strongest line starts at f0 (±2 f), its payoff inside the first second, the sentence complete by 4.0 s |
| Density | the first three seconds feel dense: a re-frame, the stinger rising and covering, a new picture, new chunks, the twist; each lands while the last one settles | calm: the person and the sentence carry it |

### 6.2 HA-11 Thesis montage (F-A default)
Spoken pattern: one sentence that names the subject, what it just did, and the twist; then a turn line ("*<Subject> just
<did a surprising thing>, and it involves <unexpected party>. Here's why.*").

| t | Beat | Tone | Visual (pattern) | Caption (CS-A) | Layer / camera | Cue moment |
|---|---|---|---|---|---|---|
| **f0** | Stopper | turn | **The subject, tight**: the archive photo of the person / place / object, cropped 1.18 so the face fills the top 60 % (P-ARCHIVE-BLEED), slow drift 1.18 → 1.17 (measured ≈ 0.4 %/s, v01 @0.45–1.05); or the created **P-SILHOUETTE-PLATE** | chunk 1 = the subject's name or title, 2–4 words ("The King of FIFA"), first word ≤ 3 f in | W-archive, z2, `in: none` | — (the bed is already under) |
| 0.40–0.50 | Re-crop | turn | **P-RECROP-CUT**: the same picture hard-cuts to 1.00 (wider) (v01 @0.417); the slow drift continues | — | `cuts: [0.45]` | — |
| 0.8–1.2 | Verb | turn | (holds) | chunk 2 = what happened ("just launched / a new scheme") | — | — |
| 1.10–2.45 | **Topical stinger** | turn | **P-STINGER-STACK**: a stacked block of the created topical object (banknote shapes for money, tickets for events, folded newspapers for media, balls for sport, crates for trade) rises from the bottom, accelerating, covers the frame at 1.63 (16 f), holds 6 f, then lifts off upward, decelerating, over 16–18 f, revealing picture 2 already in place underneath (measured v01 @1.09–2.43) | chunk 2 stays on top, readable throughout | z6, `events: [0.53, 0.75]` | **hook cue** on the cover peak (1.63) |
| 1.85–2.45 | Picture 2 | awe | The subject in action (an event photo), revealed bottom-up by the lifting stinger; **P-PARTICLE-OVERLAY** (24–30 seeded flakes in `accent` / gold `#E8C547` at 70 %) only when the line is about winning, money or celebration | chunk 3 = the purpose ("to make money") at 2.18, once the stinger has lifted | z2 + z5 overlay | — |
| 2.6–3.0 | **Thesis lands** | awe | Picture 3: the unexpected party (their photo or a silhouette plate), a slow pull-out; this scene has `payoff: true` | chunk 4 = the twist ("and it involves / Donald Trump.") | z2 | — |
| 3.0–4.0 | Turn | turn | Hard cut to a new archive picture or straight to W-blue | "Here's why." (alone, 1 line) | — | — |
| 4–8 | Context | explain | 3–4 archive pictures, 0.9–1.3 s each, or the first receipt (P-SOURCE-CARD) on W-blue | chunks as spoken | — | — |

At f0 there's the picture, already moving, and the first chunk in its box: nothing else, no other text.

**The flurry variant** (v02): swap the stinger for **P-ARCHIVE-FLURRY** (three stills in 0.9 s: 0.30 / 0.20 / 0.40 s, three
different treatments) followed by a live clip with a punch re-crop at 1.9 s. Use it when the subject is a *place, sport or
era* rather than a person.

**Never** open on W-blue text alone in HA-11 (that's HA-12), never put a title over the f0 picture, and never let the hook
run past 4.0 s before the turn line.

### 6.3 HA-14 Cold authority (F-B default)
| t | Beat | Visual | Caption (CS-B) | Shots |
|---|---|---|---|---|
| **f0** | Mid-thought | The speaker who says the strongest line, single (cam A or B), live; no graphic | chunk 1 at f0 (≤ 2 f) | shot 1, `cut_reason: open` |
| 0–1.0 | Strongest line | Same single | chunks 1–2 | no cut |
| 1.0–6.0 | Development | Same single; a ×1.2 re-crop at 4–6 s if the turn continues (R-3) | as spoken | at most a re-crop |
| first handover | Second voice | Cut to the other person on their first word (R-1) | guest chunks in italic | handover |
| from ≈ 8 s | Rhythm | Handover cuts, 1.2–2.2 s reactions, re-crops when a hold runs long | | |

No music, no title, no zoom preset: the authority is the person and the sentence.

### 6.4 Alternate hooks
**HA-12 Receipt open (F-A)**: when the story *is* a document or an announcement and no strong subject picture exists.
| t | Visual | Caption |
|---|---|---|
| f0 | W-blue; P-SOURCE-CARD, the outlet line resolving in, headline line 1 typing (7 f per line) | chunk 1 at f0 |
| 0.7 | the headline complete | chunk 2 |
| 1.2–2.0 | the key span turns lime on its spoken word; the leader dot + line draw | chunk 3 |
| 2.0–3.0 | the first thumb fades in (the subject), the thesis complete (`payoff: true` on the card) | chunk 4 |
| 3.0 | hard cut to archive (the HA-11 rhythm from here) | "Here's why." |

For example: "<Company> / told investors / it will stop / selling <X>."

**HA-07 Number open (F-A)**: when the thesis is a number ("$20 billion", "211 votes", "3 out of 4").
| t | Visual | Caption |
|---|---|---|
| f0 | W-green; P-COUNTER-CARD rolling from 0 (`kind: counter`) | the claim, chunk 1 |
| ≤ 1.0 | the counter lands on the spoken number (±5 f), the lime rule wipes in 6 f | chunk 2 |
| 1.0–3.0 | hard cut to the subject (archive) + the twist chunk | chunks 3–4 |

For example: "211 countries / vote on this, / and one man / decides."

**HA-19 Place open (F-A)**: when the subject is a place or an era.
| t | Visual | Caption |
|---|---|---|
| f0 | a full-bleed archive clip or still of the place (settle + drift), a place chip (T-PLATE, e.g. "JAPAN, 1870s") at y 1180 | chunk 1 |
| 0.6–2.5 | P-ARCHIVE-FLURRY (3 stills) | chunks 2–3 |
| ≤ 3.0 | the premise complete; P-LOCATOR-CARD may follow at the turn | chunk 4 |

For example: "Japanese baseball / looks a lot / different / than American baseball."

**HA-03 Question over the stack (F-B)**: when the clip starts with one person asking the other a sharp question.
| t | Visual | Caption |
|---|---|---|
| f0 | A stack shot (asker top, answerer bottom, seam y 960) for 2.7–4.0 s (hand-edit `timeline.shots[0]` into a stack: R-5); **P-B-QUESTION-PLATE** above the seam | the question, on the seam |
| 2.7–4.0 | Cut to the answerer's single on their first word | answer chunks |

### 6.5 Hook pairs: thesis → the scene that carries it
| Topic | Thesis (≤ 3 s) | The scene / object that carries it | Stinger object |
|---|---|---|---|
| A company's surprise move | "<Company> just <bought / banned / launched> <X>, and it involves <rival or regulator>." | Founder / CEO photo → the announcement receipt | banknote rows |
| A price that changed | "<Product> costs <2×> what it did in <year>. Here's who's behind it." | Product plate → P-BAR-TRACKS of the two prices | price tags |
| A founder's comeback | "<Founder> was fired from <Company>. <N> years later, they bought it back." | Two dated photos, same face | folded newspapers |
| Why a border is where it is | "<Country A> and <Country B> share a border nobody can cross. Here's why." | Locator card with the line drawn in `bad` | none: a T-03 roll-by of a pin |
| Why a city looks the way it does | "<City> has no <skyscrapers / cars / …>, and it's on purpose." | Archive street photo → date plate of the rule | building blocks |
| An old event still shaping today | "In <year>, <event>. It still decides <present thing>." | Date plate → archive photo → today's photo | ticket stubs |

F-B pairs are in-point choices: "the line that works alone" → "the person who says it, single, at f0".

### 6.6 Headline chunks (the first 1–3 chunks)
**Formula:** `<Subject named concretely> + <what it did, a plain past-tense verb> + <the twist>`, said in the first 3 s,
chunked 2–5 words.
| Template | Example |
|---|---|
| **Name + move + twist** (default) | "The King of FIFA / just launched / a new scheme / to make money, / and it involves / Donald Trump." |
| **Place + difference + why** | "Japanese baseball / looks a lot / different / than American / baseball. / Here's why." |
| **Number + owner** | "$20 billion / is about to / change hands. / Here's who / gets it." |
| **Then / now** | "In 1998, / this was illegal. / Today it's / everywhere." |

The subject is always named (never "this guy", "this company"); the twist is a concrete noun; in F-A the first chunk is
never a question (questions are the re-hook's job); no hype words ("insane", "crazy", "you won't believe"). The calm is
the authority.

### 6.7 Hook sound
F-A: the bed runs from f0 (a documentary pulse under the voice); the only hook cue is on the stinger's cover peak. F-B: dry,
room tone only. See §11.

### 6.8 CTA and the end cards
| Device | Spoken pattern (the last line) | On screen | Hold |
|---|---|---|---|
| `subscribe` (Follow) | "For more <topic A> and <topic B>, decoded, follow <the creator's handle>." | P-END-TAGLINE with the Follow → Following pill | 2.0–3.5 s |
| `end_card` (wordmark only) | the tagline line | P-END-TAGLINE without the pill | 2.0–3.0 s |
| `link_bio` | "The full story is linked in my bio." | P-END-TAGLINE with a lime "link in bio" box (or P-END-QR without the QR) | readable ≥ 1.5 s |
| `comment_keyword` | "Comment KEYWORD and I'll send you <the deliverable>." | P-END-TAGLINE with "Comment" + the keyword in a lime box, mono 700 56 px | ≥ 1.5 s |
| `qr` | "Watch the full conversation at <url>." (or text only, below) | P-END-QR | 2.0–3.0 s |
| `cross_promo` | "Watch the full deep dive over on my channel." | P-WATCH-FULL **before** the end card | 1.5–2.5 s |

The last body sentence ends, then ≥ 0.25 s of air, then the CTA line. One device per reel (a cross-promo may come before
it). One end card per reel, ≤ 3.5 s, the action readable ≥ 1.5 s, captions hidden, the hard end ≤ 6 f after the last word
(the end card's line is the last spoken line, or the card covers a non-speech tail), a black tail ≤ 0.2 s.

**P-END-TAGLINE** (F-A default; F-B when the device is `subscribe`)
| Element | Spec |
|---|---|
| Ground | W-end `end_bg` `#0A1314` + noise 0.05 (a faint 8 % halftone of the reel's last archive picture may sit behind at 6 % opacity) |
| Tagline | Montserrat 800, 138 px (128–148, the longest line fitted to 900 px), line height 1.0, tracking −0.04 (the letters nearly touch), left x 90, top y 150 (measured v01 @1:20: cap top 151, x 93–966), 4 lines in off-white `#E4ECE6`: "For more" / "<topic A> and" (topic A in `end_a`) / "<topic B>," (topic B in `end_b`) / "decoded" (paper). The pattern is `brand.endcard.tagline_pattern`; the creator's own tagline replaces it (`brand.endcard.tagline`, proposed from their niche at the first plan and kept) |
| Wordmark row | top y 920: the logo (SH-8) or the FB-8 monogram in a Ø 280 disc at x 72 (measured Ø ≈ 295, y 925–1220); the action element 40 px right of it, vertically centred on the disc |
| Action: `subscribe` | a white pill "Follow" (Inter Tight 700 40 px, ink, h 84, padding 0 × 40, radius 42) → at +0.8 s it becomes "Following" (fill `#2A2F30`, paper text, a bell glyph) over 6 f with a 6-particle lime sparkle; a ghost pill with the creator's handle (paper 2 px outline) next to it |
| Action: `comment_keyword` | "Comment" (Inter Tight 700 44 px, paper) + the keyword in a lime box (`accent` fill, ink, mono 700 56 px, padding 10 × 22) |
| Action: `link_bio` | "Full story: link in bio", with "link in bio" in the lime box |
| Action: `end_card` | the wordmark row only |
| Motion | T-06 hard cut (no dissolve: v01 @76.80, v02 @56.00); from f0 the tagline is on screen at ≈ 10 % with letters resolving in seeded order (`fx.resolve`, `order: "random"`, `ghost` on), and each line brightens from dim grey (`#4C5252` → `#707474` → `#E4ECE6`) over ≈ 1.5 s, the top line first; topic A turns `end_a` first, topic B turns `end_b` last (v01 @1:16.6–1:20, v02 @0:57–0:59); the whole wordmark row (disc + pills) rises from y +180 to its place over 8–10 f (`ease_entry`) from f0, then creeps up ≈ 20 px over the hold; the Follow → Following change at +0.8 s |
| Hold | 2.0–3.5 s |

**P-END-QR** (F-B default; F-A when the device is `qr`)
| Element | Spec |
|---|---|
| Ground | W-qr (`primary`, flat) |
| Text | mono 700 40 px, paper, line height 1.3, centred at y 470–620, three lines: "Watch the full conversation" / "with <Guest or Show>" / "at [url]", the URL in a paper box (ink text, padding 4 × 12) |
| QR | the SH-10 image (or a QR you generate locally from the creator's URL), a white panel 620 × 620 at x 230, y 760, 40 px quiet zone; the FB-8 monogram disc Ø 120 in the centre only if the QR's error correction is H |
| Without a QR | FB-10: no QR panel; the URL box grows to mono 700 56 px at y 900 |
| Motion | hard cut in (T-01); the text types on at 8 f per line; the QR panel pops in 8 f (0.94 → 1.00) |
| Timing | covers the clip's non-speech tail (a laugh, "yeah", a breath) of 1.5–2.5 s; if the clip has no tail, record a 2 s sign-off line ("Full conversation: link on screen") and put the card under it |

**Sponsor (P-SPONSOR-SOURCE):** a paid segment is built like a receipt, the sponsor's name in the outlet slot and their
line as the headline (key span lime), with the "Paid partnership" T-TAG at x 64, y 128 held through the whole segment
(≥ 2.0 s) and said aloud. No logo in the outlet slot: the sponsor's name is set in type, as every outlet is.

---

## §7 Structure and rhythm

### 7.1 Structure
**F-A `explainer`:** thesis (0–3 s) → turn ("Here's why", 3–4 s) → context (who / where / when) → receipts (the
escalation: two to four sources or named people) → **the re-hook** ("Now why…") → the comparison or the mechanism (side A
vs side B, the money flow, the map) → the payoff (the answer to "why", one card or one picture) → the wrap line → CTA.

**F-B `conversation`:** the strongest line (f0) → development by the same speaker → the second voice (agreement, push-back
or a question) → back to the first voice → the button (the quotable conclusion) → the tail → the end card.

### 7.2 Markers: SM-SIDE-CHIPS
- **SM-SIDE-CHIPS** (F-A) is the only marker: in a comparison every card carries its side chip (`side_a` red / `side_b`
  off-white + the trait word), and the two sides alternate A, B, A, B. Lists inside an explainer are spoken only: no
  numerals on screen.
- F-B: no markers (spoken only).

### 7.3 The receipt ritual (F-A; the same every time)
1. Hard cut to an **empty** W-blue on the chunk that names the source ("reports say", "according to", "a new filing
   shows") (0 f); nothing for 4 f (v01 @7.93–8.05).
2. The headline types on **word by word**: a new word every 2–3 f, each entering at 40 % (`muted`) and brightening to
   white over 4 f (≈ 10 words in 0.75 s, faster than the voice); the outlet line's letters appear in seeded random order
   over 14–18 f alongside it (v01 @8.09–8.80).
3. On the first word of the key span: the non-key words → `muted`, the key span → `accent` (6 f); the lime dot pops (4 f);
   the leader line draws (12 f).
4. On the next named person or figure: the body copy fades in (8 f) with its spoken figure in lime; the thumbs **fade** in
   (0 → 100 % over 6 f, no scale; 4 f stagger) for each named person; the block follow-pushes (G-4, 24–27 f).
5. Hold until the voice leaves the source; hard cut out.

A receipt lives as long as the voice stays on its source (the original held one for 15.3 s, v01 @7.9–23.3), and it is
never still while it's up: a word, a highlight, a body span, a thumb or the push gives the eye something new whenever the
voice names something. When the voice has moved on, the receipt has too.

**The comparison ritual (P-COMPARE-SWIPE):** card A1 (`side_a` chip) → deck advance (G-3) → card A2 → … → side change
(push-up, G-3) → card B1 (`side_b` chip) → …; each card lasts while its trait is being said (2–4 s in the evidence; a
whole comparison ran ≈ 19 s, v02 @25.36–44.52). Each card: the media fades up 14–16 f (G-7), then the chip grows from a
4 px sliver to full width over 6 f, its disc appears, and the trait word's letters resolve in seeded order over 10–12 f
(v02 @29.64–30.12); the media may hard-cut to a second clip inside the frame while the chip stays. The trait word is the
word the voice uses ("CONSISTENCY", "POWER").

### 7.4 Open loops and the re-hook
- **The why loop:** "Here's why." at 3 s, paid by the payoff card.
- **The who loop:** "and it involves …", paid by the receipts.
- **The question re-hook** (P-QUESTION-TURN): "Now why is <subject> …?" over a hard cut back to the subject's face, beat
  `rehook: true`. It comes once, in the middle, at the moment the context has run long enough that the viewer needs a new
  question (v01 put it at 0:24 of 80 s). F-B clips are short enough to need no re-hook.
- The hook is over fast: the turn line arrives while the thesis is still ringing, so context starts before the promise
  goes cold.

### 7.5 Rhythm, by feel
- **The speech is the rhythm.** The cuts land on the caption chunks and the nouns; a picture lasts as long as its phrase,
  so a fast run of names gets a fast run of faces, and a slow sentence gets one picture with something happening inside it.
- **Energy rises through picture density, never volume.** Context moves at the pace of the names; the receipts slow the
  cut but fill it with events; the comparison flips card to card on the traits; then the payoff slows right down to **one
  picture held for two or three seconds**, the only slow moment in the reel, while the answer lands. Then the end card.
  That held picture is the release the whole investigation was building to; don't spend it anywhere else.
- **It never sits still, and it's never random.** Something changes when the words give it a reason: a cut on a name, a
  highlight on a figure, a pin on a place. A picture that has nothing new to show after its phrase is gone.
- **Hard cuts are the grammar; everything else is punctuation.** The stinger and the roll-by are rare enough that each one
  feels like a chapter turning.
- **F-B breathes the other way:** calm holds; the energy is in the handovers; the button line is never cut away from.
- For reference, measured on the three reels (a description, not a target): v01 24.7 cuts/min with a median shot of
  1.08 s, v02 19.2 cuts/min and 1.64 s, v03 (the podcast) 11.2 cuts/min and 3.1 s; F-A captions swap about once a second.

### 7.6 Series (off unless the creator runs one)
A T-TAG plate "PART <n>" (`series.tag_format: "part {n}"`) in the top slot (x 64, y 128), landing on the turn line between
3 and 8 s and held 1.2 s, never inside the hook.

---

## §8 Visual system: B-roll and patterns

### 8.1 How the graphics behave
**F-A, graphics primary:** every frame is a picture or a card, and numbers become pictures (a counter, bars, a seat arc,
or the receipt that states them). The archive montage and the blue receipts share the reel; maps, figures and comparison
cards come in where the words need a where, a how much or a versus. Variety comes from the story (a person, then a
document, then a place, then a number), never from a quota; the receipt and comparison rituals are the deliberate repeats,
and a run of archive faces is fine while their treatments keep changing.

**F-B, graphics minimal:** three recurring devices only: the CS-B captions, the optional name plate on a first appearance,
the end card.

### 8.2 Families
| ID | Family | Source | The creator's own | Otherwise: fetched, else created |
|---|---|---|---|---|
| **B-1** | Archive pictures (full-bleed stills and clips) | the creator's own, else the real ones fetched, else created plates | Photos and clips of the people, places, objects and events named (SH-1, SH-2) | The real photos and clips from the web (press, official pages, public archives), source noted; P-SILHOUETTE-PLATE, P-OBJECT-PLATE, P-DATE-PLATE only when none turn up (FB-1) |
| **B-2** | Receipts (source headlines, quotes) | the real article's exact words typed into the card, or the real page (the creator's screenshot or a capture) | Article screenshots (SH-3) or the pasted headline text | The real article found, read and captured; P-SOURCE-CARD is itself the created recipe (`headline_card`) |
| **B-3** | Maps | engine (schematic today), the creator's own map image, or a real map fetched | Map exports (SH-4) | A real map image (official or public-domain) in the card; else P-LOCATOR-CARD (FB-4) |
| **B-4** | Cards on blue (photo cards, comparisons, strips, plates) | engine frames around the creator's or fetched media, or created plates | Photos (SH-1) | Fetched photos, else created plates, inside the same frames |
| **B-5** | Figures on green | engine (`VEOS.data`, bespoke scenes from `plan/figures.json`) | Numbers in the script (always) | — |
| **B-6** | Stingers and overlays | created objects (vector shapes, never photos of real money or brands) | — | — |
| **B-7** | Brand furniture (end cards, cross-promo, sponsor) | engine + the creator's logo / thumbnail / QR | SH-8, SH-9, SH-10 | Their logo and thumbnail fetched from their own channel or site; else FB-8, FB-9, FB-10 |
| **B-8** | Conversation cuts (F-B) | the creator's own footage | SH-5, SH-6, SH-7 | FB-5, FB-6, FB-7 |

### 8.3 Pattern specs (30 fps; "f" = frames)
Every scene names its pattern in the beat (`pattern`) and its family. Patterns marked † are third-party moments: they
follow §12.4 (the creator's file, else the real thing fetched, else created; no credit lines).

**B-1 Archive**
| ID | Type | On screen | Motion recipe | Use | Needs |
|---|---|---|---|---|---|
| **P-ARCHIVE-BLEED** † | footage-treatment | One archive photo full-bleed (z2, `kind: "archive"`, cover-fit, focus on the face or subject), a treatment from §4.3 | Hard cut in (`in: "none"`, `cuts: [0]`); a quick **settle** 1.04 → 1.00 over the first 5 f (expo-out; v02 @45.15–45.35 measured −3.8 % in ≤ 5 f, then static), then a barely visible drift ≤ 1 %/s, alternating in / out on consecutive shots; hard cut out. No big Ken Burns: the pace comes from the cuts | Every named person, place, object or event with a real picture (the creator's or fetched) | face centre y 520–900 |
| **P-ARCHIVE-CLIP** † | footage-treatment | A creator clip full-bleed (`fx.clip`, z2, `kind: "archive"`), GR-vhs for old colour video | Hard cut in; plays at 1.0×; no added camera move; one **punch** on the action word: a hard cut to a tighter shot of the same action (v02 @1.88 cuts from the wide wind-up to a waist close-up), or, with one clip only, a ×1.25 re-crop (`cuts: [t]`) | Action: a pitch, a speech, a crowd, a launch | — |
| **P-ARCHIVE-FLURRY** † | cut | 3 stills in 0.9 s (holds 0.30 / 0.20 / 0.40 s), three different treatments, the same subject class | Hard cuts; each still settles 1.04 → 1.00 in 5 f | The hook (HA-11 flurry variant, HA-19), era montages | — |
| **P-RECROP-CUT** | cut | The same picture re-framed | A hard cut from crop 1.18 to 1.00 (or 1.00 to 1.18) mid-hold, on a word onset; the drift continues | Hook f0 + 0.45 s; any picture held long enough to go still | — |
| **P-SILHOUETTE-PLATE** † | overlay (created) | A full-bleed `navy` field, a 6 px dot halftone (GR-halftone) silhouette bust (head + shoulders, 760 px tall, centred x 540, top y 360) in `land` with a `focus` rim light, a T-PLATE name under the chin at y 1180 | Hard cut in; a slow push 1.00 → 1.05; the name plate wipes in L → R 8 f at +6 f | A named person with no real photo to be found (FB-1) | `satisfies: ["archive"]`, recipe `silhouette` |
| **P-OBJECT-PLATE** † | overlay (created) | Full-bleed halftone paper (`#D9D4C7` × GR-sepia) or navy, one large line icon from `fx.icon` (420 px, stroke 10, ink or paper) of the object / place type, a T-PLATE caps label (the noun) at y 1180 | Hard cut in; the icon scales 0.96 → 1.00 over the hold, the paper pushes 1.00 → 1.04 | A named object, building, product category or place with no photo | recipe `logo_plate` for products, `diagram` for objects |
| **P-DATE-PLATE** | overlay (created) | A full-bleed halftone navy plate, the year or date in T-DATE (display 700, 180 px, white), centred at y 760; a thin `accent` rule 120 × 6 px under it | Hard cut in; the digits roll from the previous year mentioned (or count up over 8 f) and land on the spoken year (±3 f); hold ≥ 1.0 s | "In 1870 …", "By 2005 …", era jumps | the year from the script (a `figures.json` input) |

**B-2 Receipts**
| ID | Type | On screen | Motion recipe | Use | Needs |
|---|---|---|---|---|---|
| **P-SOURCE-CARD** † | overlay (signature) | On W-blue, no card: T-OUTLET (outlet · date) at y ≈ 360; T-HEAD 70 px, ≤ 3 lines, x 64; a lime dot Ø 18 after the last line; a leader line 3 px `muted` from the dot left to x 300, corner r 36, down 120 px, then left off the frame edge; T-BODY 3–5 lines right of the corner; 0–3 photo thumbs (h 290, square corners, no border, gap 0, centred, max total width 760) | f0–4 f empty blue; the outlet letters appear in seeded order over 14–18 f; the headline types **word by word** (a word every 2–3 f, each 40 % → white over 4 f); the **highlight** on the key span's first word: non-key words → `muted` and the key span → `accent` over 6 f; the dot pops in 4 f (scale 0 → 1.15 → 1); the leader draws in 12 f (stroke-dashoffset); the body fades in over 8 f; the thumbs fade in 6 f each (opacity only), 4 f stagger, on each named person; the **follow-push** (G-4) ×1.14 over 24–27 f, then a ≈ 1 %/s creep; all receipt motion on twos (§10.1) | Every "according to / reports / announced / a filing shows" line; the evidence beat of the receipt ritual §7.3 | `source {masthead, date, headline, highlight_spans}`, `insert`, recipe `headline_card` (created) or `creator_media` (the creator's screenshot, or the real article captured from the web, shown with `fx.shot` inside the text rect instead of the typed headline) |
| **P-SOURCE-SWAP** † | overlay | A second headline replaces the first in place (the same or another outlet) | The old headline + body rise 8 px and fade out over 6 f; the new outlet resolves and the headline types (as P-SOURCE-CARD); the leader re-draws | A second source right after the first (v01 0:39: FT → Guardian) | as P-SOURCE-CARD |
| **P-RECEIPT-RETURN** † | overlay | The same receipt shown again later with a different body span lit | Hard cut in fully built; the new body span turns lime in 6 f on its spoken figure | Coming back to a source with a new detail (v01 0:34) | as P-SOURCE-CARD |
| **P-QUOTE-RECEIPT** † | overlay | On W-blue: the T-OUTLET slot carries the speaker's name + where they said it; the quote in T-HEAD white between curly quotes, the key span lime; the speaker's real photo (or a silhouette) as a thumb (240 × 240) at the left under it | As P-SOURCE-CARD; the quote types on word by word at the voice's pace (9 words/s cap) | A person's exact words read aloud | word for word; recipe `quote_card`, `quote_text` |

**B-3 Maps**
| ID | Type | On screen | Motion recipe | Use | Needs |
|---|---|---|---|---|---|
| **P-MAP-CARD** | overlay | Card rect r 40: `navy` sea, `land` countries, the focus region in `focus`, T-MAPLABEL chips, logo / pin markers | Card cut-in (G-2); an inner punch ×1.5 to the focus on the place word, then a slow pan toward the next focus (G-7; v01 @49.14); a different region is a hard cut to a new map card (v01 @51.6 Eurasia → North America); face cut-outs (no disc) and labels sit on the map from the cut | Any "where" line | **Not available until the geo-map bundle (E-18) ships: use P-LOCATOR-CARD** |
| **P-LOCATOR-CARD** † | overlay (created, today's map) | Card rect (or tall) r 40, `navy` fill, a dotted graticule (dots r 2, pitch 80 px, white 12 %), a north tick "N" (mono 500 24 px) top-right; 1–4 pins (a white disc Ø 28 with a 6 px `primary` ring) in rough relative position (west → left, north → up), each with a T-MAPLABEL chip | Card cut-in (G-2); the graticule fades in over 8 f; the pins pop in 6 f, 4 f stagger, each on its spoken name; the active pin gets a lime ring (6 f); on the second named place an inner punch ×1.5 toward it, then a slow pan (G-7) | Every "where" line until the geo-map bundle ships | recipe `diagram`; no coastlines, no borders, no distances: it reads as a diagram because it is one, so it needs no label |
| **P-ROUTE-LINE** | annotation | A dashed line (dash 18 / gap 12, 6 px) between two pins on a locator or map | Draws over 14 f from origin to destination; ends in a `good` arrowhead (allowed / went there) or a `bad` × (24 px, blocked); the × pops in 4 f | Movement, trade, people on the move, blocked paths (v02 0:17) | — |
| **P-FACE-PINS** † | annotation | Round avatars (Ø 150, a real photo (the creator's or fetched) circle-cropped or a silhouette disc, a 6 px `paper` ring) on pins, a T-MAPLABEL under each | Pop in 6 f, 6 f stagger, on each spoken name | Who is where (v01 0:46–0:52) | — |
| **P-TOKEN-MIGRATION** | state | 3–6 small portrait tokens (90 × 120, a 4 px `side_a` frame) travel along a corridor band (a 40 px `side_a` 35 % stripe) from region A to B | The tokens leave 6 f apart, travel 18 f each (`ease_card`), settle in a cluster at B | People or products moving from one place to another (v02 0:49–0:55) | — |

**B-4 Cards on blue**
| ID | Type | On screen | Motion recipe | Use | Needs |
|---|---|---|---|---|---|
| **P-PHOTO-CARD** † | overlay | One real photo (the creator's or fetched) or a plate inside the card or tall rect, r 40, drifting inside the mask | Card cut-in (G-2), hard cuts between consecutive photo cards; the media fades up 14–16 f (G-7), then drifts ≤ 1 %/s | Two people meeting, an event photo too small to go full-bleed | — |
| **P-PHOTO-STRIP** † | overlay | 2–3 square-cornered photos side by side (h 300–420, gap 0), centred in the card zone | Each pops in 6 f, 4 f stagger, on its name | "<A>, <B> and <C>" lists of people | name plates optional |
| **P-COMPARE-SWIPE** † | overlay (ritual) | A tall-rect card filled with `primary` darkened 25 % (mixed with `navy` 0.35), a soft diagonal light band (140 px, 20°, `primary` lightened 12 %, 40 %) behind; an inner media frame x 235, y 450, w 610, h 640, a 3 px `side_b` border, r 8; T-CHIP centred on the frame's bottom edge (cy 1090) in `side_a` (side A) or `side_b` (side B) with a 44 px monogram disc and the trait word; the previous card peeks 48 px at the left (60 %) | Deck advance / side-change push-up (G-3); the media window fades up 14–16 f with its 3 px border drawn; the chip grows in 6 f, the trait word resolves in 10–12 f (§7.3); the media plays live | Side A vs side B comparisons (v02 0:25–0:44) | the chip carries the spoken word, 40 px |
| **P-NAME-PLATE** | overlay | T-PLATE under a face (a bleed picture or a photo card), x centred on the face, top = chin + 40 px, max y 1250 | Wipes in L → R 8 f (the box first, the text 2 f later); exits with its picture | The first time a person appears on screen | — |
| **P-AVATAR-RING** † | overlay | A circular avatar Ø 200 (a photo or silhouette disc) with a 6 px ring (paper 60 %), entering a figure or map | Rises over 10 f from behind the figure's lower edge (masked, `ease_card`; v01 @25.66–26.03), the ring visible from the start | The person who controls a figure (v01 0:26) | a name plate under it |

**B-5 Figures on green** (every value from `plan/figures.json`, written with `ctx.fmtNum`)
| ID | Type | On screen | Motion recipe | Use | Needs |
|---|---|---|---|---|---|
| **P-SEAT-ARC** | figure | A card rect on W-green (`data_card`, r 40): a half-circle seat chart (centre 540, 1010; r 170–400), wedges per group with T-MAPLABEL-style labels (≤ 6 groups at 40 px; more groups → a legend row), one dot (r 6) per seat; P-AVATAR-RING in the middle | The card hard-cuts in with the arc built (v01 @25.37); the avatar rises on its name; on the member count an inner punch ×1.8 onto the avatar + the nearest wedges, then a pull-out ≈ 0.15 %/f (G-7, v01 @29.97); optional token flow (P-FLOW-TOKENS) | Votes, members, seats, shares of a body (v01 0:25–0:33) | figure `seat`, kind `grid_fill` |
| **P-FLOW-TOKENS** | figure | Small chips (the amount via `fmtNum`, mono 700 40 px on a lighter `data_card` pill) flying from a source to N targets | Each token a 12 f arc, 3 f stagger; the amount lands on the spoken figure | Money or votes moving | figure `flow` |
| **P-BAR-TRACKS** | figure | `VEOS.data.bars` restyled: 2–4 tracks (row h 96, track `data`, bar = `data_card` mixed 45 % with paper, radius 48), an icon or avatar at the left, the value at the bar end (T-FIG 72 px) | The bars grow over 18 f on one shared scale; the values roll and land on the spoken number | Two to four quantities compared (v01 1:12) | one shared scale |
| **P-COUNTER-CARD** | figure | `VEOS.data.counter` on a card: T-FIG 140–160 px white, a mono 700 40 px unit line under it, a 6 px lime rule that wipes under the number when it lands | Rolls over 18 f, lands within ±5 f of the spoken number | One hero number; HA-07 | `kind: counter` |
| **P-TIMELINE-RAIL** | figure | A horizontal rail (6 px `muted`) across the card with year ticks; the active year in a lime pill (mono 700 40, ink) | The pill slides to each spoken year in 10 f; the ticks pop in 4 f | Sequences of dated events (inferred: the evidence uses date captions instead) | years from the script |

**B-6 Stingers and overlays**
| ID | Type | On screen | Motion recipe | Use | Needs |
|---|---|---|---|---|---|
| **P-STINGER-STACK** | transition (created) | 4 overlapping rows of one created topical object filling the frame (generic banknote shapes with no real currency art, ticket stubs, folded newspapers with illegible texture, balls, crates), each row offset 40 px | The stacked block rises from y 1920 as one mass, accelerating (ease-in), covers the frame by f 16, holds 6 f, then lifts off the top decelerating (ease-out) over 16–18 f, no blur; the next picture is cut underneath at the cover and revealed bottom-up; the caption stays on top (measured v01 @1.09–2.43) | The hook's punctuation; in the body only on a real topic turn, rare enough to feel like a chapter | no text; `events` at the cover and the exit |
| **P-ROLL-BY** | transition (created) | One created object (a ball, a coin, a wheel) **bigger than the frame width** (Ø ≈ 1150 px) | Enters from the bottom edge, flies up and slightly right, exits the top in 9 f with ≈ 120° of rotation; the cut happens under it at mid-pass (f 4–5) (v01 @4.43–4.72) | A lighter topic turn inside the body (v01 0:04.5) | no text |
| **P-PARTICLE-OVERLAY** | overlay (created) | 24–30 seeded flakes (confetti strips 14 × 34 px or coins Ø 26) in `accent` / gold `#E8C547` at 70 %, drifting down 60–120 px/s with spin | Continuous over a celebration picture for 1.5–3.0 s, fading out over 8 f | Wins, money, ceremony (v01 0:02–0:04) | z5, ≤ 30 small items; kept off faces |
| **P-QUESTION-TURN** | cut (re-hook) | A hard cut back to the subject's face (bleed) with the question as the caption | Hard cut; settle 1.04 → 1.00 in 5 f, then near-static (v01 @23.27) | The mid-reel re-hook "Now why is …?" (v01 0:24) | beat `rehook: true`, scene `kind: "rehook"` |

**B-7 Brand furniture**
| ID | Type | On screen | Motion recipe | Use | Needs |
|---|---|---|---|---|---|
| **P-WATCH-FULL** † | overlay | W-white; a video card x 120, y 520, w 840: the thumbnail 840 × 472 r 18 (the creator's own thumbnail SH-9, fetched from their channel when not given, or the FB-9 title field), the title in body 700 44 px ink below (y 1020), a channel line in mono 500 26 px `#5A5A5A` (the creator's name, no view counts); a cursor (a 64 px arrow, ink with a paper outline) | The card rises in 9 f; the cursor glides from (900, 1300) to the thumbnail centre over 18 f (`ease_card`) and clicks at +0.6 s: the card scales 0.97 → 1.00 over 6 f | Cross-promo of the creator's long video before the end card (v01 1:14–1:16) | the caption shows as a grey box on white (CS-A, 70 % black) |
| **P-END-TAGLINE** | overlay | §6.8 | §6.8 | F-A end (and F-B with `subscribe`) | — |
| **P-END-QR** | overlay | §6.8 | §6.8 | F-B end (and F-A with `qr`) | — |
| **P-SPONSOR-SOURCE** | overlay | A sponsor segment built like a receipt: the sponsor's name set in type in the outlet slot, their line as the headline (key span lime), the "Paid partnership" T-TAG at y 128 held through the segment | As P-SOURCE-CARD | Paid integrations (inferred) | the disclosure, held ≥ 2.0 s and said aloud |

**B-8 Conversation cuts (F-B)**
| ID | Type | On screen | Motion recipe | Use | Needs |
|---|---|---|---|---|---|
| **P-B-SINGLE-HOLD** | cut | The speaker's single, the face ≈ 17 % of the frame height, head top y 140–300 | Holds 4.0–6.0 s; live footage | The default picture | — |
| **P-B-HANDOVER-CUT** | cut | A cut to the new speaker's single | 0 f, 1 f before their first word (±3 f) | Every handover (R-1) | — |
| **P-B-REACTION** | cut | The listener's single while the speaker continues | 1.2–2.2 s, not in the first 1.0 s of a turn, not in the last 1.0 s before a handover | A back-channel ("right", "yeah"), or a long turn that needs a breath (R-2) | the caption stays the speaker's |
| **P-B-RECROP** | cut | The same angle re-framed ×1.2 (or back to ×1.0) | A hard cut on a word onset | A turn that runs long on one angle (R-3) | — |
| **P-B-WIDE** | cut | The wide two-shot (cam W) | 1.5–4.0 s, once, in the last third, on a sentence start | The room established before the button (R-4, v03 0:32) | — |
| **P-B-STACK** | cut | A 50/50 stack: the speaker top, the listener bottom, seam y 960, hairline 0; the caption on the seam (§3.6) | Generator-placed or hand-edited; 3.0–6.0 s | Rapid exchanges and HA-03 (R-5) | the caption on the seam |
| **P-B-QUESTION-PLATE** | overlay | The question in mono 700 40 px white on a `primary` box (padding 12 × 20), max 2 lines, centred at y 860 (above the seam; clear of the top speaker's chin) | Wipes in L → R 8 f; out with the stack | HA-03 only | — |
| **P-B-NAME-PLATE** | overlay | Two lines at x 64, y 1180: the name (mono 700 40 caps, white on a `primary` box) + the role (mono 500 24 px) | The box wipes L → R 8 f, the text 2 f later; holds 2.0 s; out in 6 f | A speaker's first appearance, only when the clip has a guest the audience may not know (inferred) | below the chin, clear of the caption band |

**43 patterns:** F-A 33, the shared end cards 2, F-B 8.

### 8.4 Line → pattern lookup
This is vocabulary, not a decision table: it tells you what this style reaches for. Ask what the moment needs (what should
the viewer *see* on this phrase?), then use it, or invent something in the same language.

| Line type (what the sentence does) | Primary | Alternates | For example |
|---|---|---|---|
| Names a person ("<Name>, the founder of…") | P-ARCHIVE-BLEED + P-NAME-PLATE (first appearance) | P-SILHOUETTE-PLATE, P-PHOTO-CARD | "the man who signed it" → his face, tight |
| Names a company, product or brand | P-ARCHIVE-BLEED or P-PHOTO-CARD of the real product, storefront or logo (the creator's or fetched) | P-OBJECT-PLATE (`logo_plate`: the name set in type) when nothing turns up | "<Brand>'s best-seller" → the real product, GR-halftone, the name plate under it |
| Names a place ("in <City>", "across the border") | P-LOCATOR-CARD (pins) | P-ARCHIVE-BLEED of the place, a real map fetched in P-PHOTO-CARD, P-MAP-CARD (once the geo bundle ships) | "the river that splits the city" → P-LOCATOR-CARD + P-ROUTE-LINE |
| A date or era ("In 1998…") | P-DATE-PLATE | P-ARCHIVE-FLURRY with GR-sepia | "the 1923 earthquake" → P-DATE-PLATE → P-ARCHIVE-BLEED |
| Cites a source ("reports say", "according to", "announced") | **P-SOURCE-CARD** | P-SOURCE-SWAP, P-RECEIPT-RETURN | "a filing shows…" → the receipt, the figure in lime |
| Quotes someone | P-QUOTE-RECEIPT | P-ARCHIVE-BLEED of the speaker + the caption only | "he called it 'a new era'" → the quote typed on, "a new era" in lime |
| States one number | P-COUNTER-CARD | the receipt that states it (key span = the number) | "They raised $40 million" → the counter lands on "forty" |
| Compares two quantities | P-BAR-TRACKS | P-COUNTER-CARD × 2 on one card | two prices on one scale |
| Shares / votes / members | P-SEAT-ARC | P-BAR-TRACKS | "211 member nations" → one dot per seat |
| Money moves from A to B | P-FLOW-TOKENS | P-ROUTE-LINE with amount chips | "$2 million each" → chips flying to each target |
| People or goods move between places | P-TOKEN-MIGRATION | P-ROUTE-LINE | players leaving Japan for the US |
| Something is blocked / forbidden | P-ROUTE-LINE ending in a `bad` × | P-OBJECT-PLATE + a `bad` rule | "nobody can cross" → the route stops on a red × |
| "A vs B" traits (styles, cultures, strategies) | **P-COMPARE-SWIPE** (SM-SIDE-CHIPS) | P-PHOTO-STRIP with chips | "its two rivals" → the deck, red chip then off-white |
| Who is connected to whom | P-PHOTO-STRIP (thumbs inside a receipt) | P-FACE-PINS | "the three men behind the deal" → three thumbs fading in on their names |
| An action happening (a launch, a match, a protest) | P-ARCHIVE-CLIP | P-ARCHIVE-BLEED + P-RECROP-CUT | the pitch, then the punch to the release |
| Celebration, win, payout | P-ARCHIVE-BLEED + P-PARTICLE-OVERLAY | — | the trophy lift under falling gold |
| Topic turn ("But…", "Meanwhile…") | P-STINGER-STACK (when the turn is big) | P-ROLL-BY, a hard cut | "But there's a catch" → crates rise and lift away |
| The mid-reel question | P-QUESTION-TURN | — | "Now why would he sell?" → back on his face |
| A sequence of dated events | P-DATE-PLATE per date | P-TIMELINE-RAIL | "1998, 2004, 2019" → the digits roll each time |
| "Watch the full…" | P-WATCH-FULL | — | the creator's own thumbnail, clicked |
| The CTA | P-END-TAGLINE / P-END-QR (§6.8) | — | "For more business and power, decoded" |
| **F-B** any line | P-B-SINGLE-HOLD; a handover → P-B-HANDOVER-CUT; a back-channel → P-B-REACTION; a long turn → P-B-RECROP | P-B-STACK for rapid exchanges | "Distribution is the product." → held on the guest, no cut |

### 8.5 Data and truth
- Every counter, bar, seat arc, flow amount, date-plate year and timeline year is a figure (or an input) in
  `plan/figures.json`. Kinds used: `counter` (P-COUNTER-CARD), `bar` (P-BAR-TRACKS, one `scale_id` per card),
  `grid_fill` (P-SEAT-ARC: `value` = seats, `steps` per group), `hero_number` (P-DATE-PLATE uses an input with
  `from: script`); never `table`.
- Formulas from the safe set: `sum`, `diff`, `ratio`, `percent_change`, `per_period`, `unit_convert`, `cagr`. A stated
  value is `formula: none` with `from: script` and `said` = the exact words. Compared figures share one scale.
- Format by `profile.numbers` (international, `$`, long style: "$20 billion"); a figure inside a word-for-word headline
  keeps the headline's own spelling and isn't bound.
- Quantities are drawn countable: one dot per seat up to 600, then one dot per N with a "1 dot = N" legend in small mono.
- An illustrative shape (a schematic trend, a "1 dot = 10 seats" grouping) is `illustrative: true` with no label, and
  carries no number the script doesn't give. No invented view counts, dates or percentages anywhere, the cross-promo card
  included: in this style a number on screen reads as a fact.

### 8.6 Citations
- **The source card** is P-SOURCE-CARD (§8.3), built one of two ways:
  - *Typed* (the default, because the typing is the style): the outlet set in type (T-OUTLET, no masthead logo), the date
    as published, the headline **word for word** from the real article (find it and read it on the web) or the script,
    the transcript or text the creator pasted, 1–2 `highlight_spans` (the words the voice stresses, or the figure), and
    body copy as decorative texture (the article's own first sentence word for word when you have it, otherwise neutral
    illegible mono lines).
  - *The real page*: the creator's screenshot, or the article captured from the web (framed on the headline, source
    noted): `fx.shot({asset, chrome: false, highlights})` placed in the text rect (x 64–1016, y 360–1000), the lime
    highlight box drawn on the spoken span. The leader and thumbs still follow.
- **The highlight:** lime (`accent`) text on the key span with every other headline word dimmed to `muted` (the "lime
  figure" highlight); never bars, boxes or underlines on a created card.
- **No credit lines, no source lines, no figure numbering.** The masthead and date on the receipt *are* the citation; an
  archive picture or a created plate carries nothing under it.
- **Plates for the rest:** P-NAME-PLATE (names), P-DATE-PLATE (dates), T-MAPLABEL (places).
- **No verdict stamps:** the style never stamps a verdict; the voice concludes.
- **One receipt per claim.** A claim whose source you can't find word for word is shown only as a caption (no receipt);
  mention it when you show the storyboard.
- Beat fields: `source {masthead, date, headline, highlight_spans}` and `insert`.

### 8.7 Comedy layer: off
No stickers, stamps, emoji, meme cues or freeze-frames. The style's wit is the receipt arriving exactly on the word.

### 8.8 Assets
- Real pictures first: the creator's own photos and clips, then the real ones fetched from the web, source noted (§12.4).
- Created plates are clearly designed objects (halftone silhouettes, icons, type): never fake photos, never AI images of
  real people.
- Logos of other companies are never drawn: the real logo is fetched (the brand's own site), else the name is set in
  type (P-OBJECT-PLATE `logo_plate`).
- Flags are never drawn from memory: a real flag image is fetched when one is needed; side chips use monogram discs
  (two-letter country or team codes set in type).
- Banknotes, tickets and newspapers in stingers are generic shapes with illegible texture: no real currency, mastheads or
  serial numbers.
- **A label on a moving thing inside an archive clip** (optional): when a line names one moving thing in a full-bleed clip
  ("this man", "that ship") and a label or ring should stay on it, run `veos track` over that scene's span only (≤ 4 s,
  clip-space), check its preview, and give the label scene `anchor: {track, offset, lost: "fade", place}` (it needs a
  `box`). If the track loses the object for more than 20 % of the span, or no single object is clear, drop the label and
  let the caption carry the name (or put a static T-MAPLABEL-style chip in the lower third, clear of the subject). A
  receipt never needs a track: it's built on W-blue.

---

## §9 Transition system

### 9.1 Library
| ID | Transition | Frames | Recipe | Cue role |
|---|---|---|---|---|
| **T-01** | Hard cut | 0 | Incoming scene `in: "none"`, `cuts: [0]`; on a chunk boundary or a noun onset ±2 f | silent |
| **T-02** | Stinger stack | 38–40 | P-STINGER-STACK: rise 16 f (ease-in), hold 6 f, lift-off 16–18 f (ease-out); the cut happens under full cover | a whoosh on the rise, the cue on the cover peak |
| **T-03** | Roll-by | 9 | P-ROLL-BY: an oversized object flies bottom → top; the cut happens under it at f 4–5 | swish |
| **T-04** | Deck advance / side push-up | 0 / 4 | G-3: the next comparison card hard-cuts on top (the previous one peeks left); a side change is the built-in `push` (`dir: "up"`, `frames: 4`) | silent (the chip may carry a reveal cue) |
| **T-05** | Evolve in place | 6–27 | Inside a receipt or card: the word type-on, the highlight, the follow-push, thumbs, pins, the inner punch + drift (G-4, G-7; declared `events`) | a reveal cue on the lime highlight (one per receipt) |
| **T-06** | End cut + build | 0 | Hard cut to W-end; the logo row rises and the tagline resolves (§6.8) | the CTA cue on the pill change |
| **T-07** | Punch | 0 | A hard cut to a tighter shot of the same action (P-ARCHIVE-CLIP), a ×1.18–1.25 re-crop (P-RECROP-CUT), or an inner card punch ×1.5–1.8 (G-7) | silent |
| **T-08** | Handover / shot cut (F-B) | 0 | A `timeline.shots` boundary | silent |
| **T-09** | Hard end | 0 | The last frame ≤ 6 f after the last word; a black tail ≤ 0.2 s | — |

What the original does, for reference (v01 + v02, 58 picture changes): about three in four are hard cuts, one in ten a
punch, a stinger and a roll-by only in v01's first five seconds, the comparison's deck advances, and two end-card cuts.
Between cuts, T-05 evolves carry the long card stretches. There are no dissolves, fades, whips or flashes anywhere in the
evidence: the cut is the grammar.

### 9.2 Grammar
| Boundary | Use | Never |
|---|---|---|
| f0 | An already-moving archive picture + the first chunk (no transition) | A fade-in, a stinger, a title |
| Hook → body | T-02 once (on the verb of the thesis), then T-01 | A cross-dissolve |
| Archive → archive | T-01 on the next chunk boundary; alternate the drift direction and change the treatment | Two pictures with the same treatment and the same drift back to back |
| Archive → receipt (W-blue) | T-01 on the source word ("reports", "according") | A stinger into a receipt |
| Inside a receipt | T-05 evolves only | A cut while the headline is still typing |
| Card → card (same topic) | T-01, or T-04 inside a comparison | Sliding, rising or fading a card in (cards cut; only their contents move) |
| Topic turn ("But", "Meanwhile", "Now") | T-02 for a big turn or T-03 for a light one, or P-QUESTION-TURN for the re-hook | Stingers so close together that they stop meaning "new chapter" |
| A number lands | T-05 (the counter landing + the lime rule) | A cut before the number has held 0.8 s |
| Last body line → end card | T-06 (F-A tagline) or T-01 (F-B / QR) | A dissolve or a black frame between |
| The last word | T-09 | A black tail > 0.2 s |

### 9.3 Shot grammar R-… (F-B; the turn generator with this style's `dialogue.cut_rules`)
| ID | Rule | Numbers |
|---|---|---|
| **R-1** | Cut on the first word of a new speaker | 1 f lead, ±3 f; never inside a word |
| **R-2** | Listener reaction cutaway | 1.2–2.2 s; on a back-channel (≤ 1.6 s long), or once in a long turn; never in the first 1.0 s of a turn or the last 1.0 s before a handover |
| **R-3** | Jump re-crop on the same angle | ×1.2 (step 1.0 ↔ 1.2) when a hold reaches 4.0–6.0 s |
| **R-4** | Wide establish | 1.5–4.0 s, once, in the last third, starting on a sentence start, if cam W (or a faux wide) exists; hand-edit one `timeline.shots` entry to the wide angle with `cut_reason: "recrop"` |
| **R-5** | Stack exchange | 3.0–6.0 s per stack shot; the generator's stack share is `dialogue.stack.share` 0.12; the stack opener is off (`open_s: [0, 0]`): the clip opens on the speaker's single. Hand-edit a stack only for HA-03 or a burst of rapid handovers |
| **R-6** | Max hold | a single holds up to 6.0 s (`max_hold_s`); the generator rotates re-crop → reaction → stack |
| **R-7** | Button protection | No cut in the final sentence (the button) unless it's a handover |
| **R-8** | Min shot | 1.0 s (except a handover) |

F-A has no shot grammar (its spine is the voice); its cut rules are §9.2.

### 9.4 How the moves breathe
- **F-A:** hard cuts carry the reel. The stinger is the hook's exclamation mark; after that it comes back only for a turn
  big enough to deserve a new chapter, and a roll-by does the same job more lightly. The punch (T-07) is for the action
  word and the place word, not for every picture. The end-card build happens once.
- **F-B:** cuts come from the conversation. The wide appears once, the stack only when the exchange gets fast, and the
  button is never cut away from.

---

## §10 Motion tokens, camera and zoom, layers, finishing

### 10.1 Motion tokens (30 fps)
| Token | Value |
|---|---|
| Beat lead | 2 f before the trigger onset (captions 1 f) |
| Entry ease (`ease_entry`) | `cubic-bezier(0.22, 1, 0.36, 1)` (expo-out) |
| Card ease (`ease_card`) | `cubic-bezier(0.33, 0, 0.15, 1)` |
| Exit ease (`ease_exit`) | `cubic-bezier(0.64, 0, 0.78, 0)`, 4–6 f (most exits are hard cuts) |
| Archive settle | 1.04 → 1.00 over 5 f (expo-out) at the cut, then a drift ≤ 1 %/s, alternating in / out; the focus is the face or subject point (measured: v02 @45.15 −3.8 % in ≤ 5 f; v01 hook face 0.4 %/s). There is **no** big per-hold Ken Burns in the evidence |
| Graphics on twos | every graphic scene (receipts, type-on, follow-push, inner pans, chips, avatar, end card) sets `step_fps: 12` (poses held 3 and 2 frames at 30 fps; each pose judged on its own) (v01 receipt and push frames repeat in pairs at 23.98 fps, @8.43–8.76, @14.52–15.40). Archive clips (P-ARCHIVE-CLIP, P-ARCHIVE-STILL) and the built-in transitions run at full rate: no `step_fps` on them |
| Type-on | word by word: a word every 2–3 f, each 40 % → 100 % over 4 f, after 4 f of empty blue; the outlet letters in seeded order over 14–18 f (`fx.resolve`, `dur: 0.53`, `every: 2`) |
| Highlight | a 6 f colour cross-fade (white → muted, white → accent) |
| Leader draw | 12 f; the dot pop 4 f (0 → 1.15 → 1) |
| Thumb in | 6 f opacity 0 → 1, no scale, 4 f stagger |
| Follow-push (G-4) | ×1.14 (1.10–1.16) + a translate that frames the newest element, 24–27 f sine in-out, then a creep of ≈ 1 %/s |
| Inner punch (G-7) | ×1.5 (maps) / ×1.8 (figures), 0 f, then a pull-out of 0.15 %/f or a pan of ≈ 9 px/f |
| Media fade-up | 14–16 f from 35 % over `primary` to 100 % |
| Chip grow | 6 f, width 4 px → full; the trait word's letters resolve over 10–12 f (`fx.resolve`, `dur: 0.4`, seeded) |
| Side push-up | 4 f, the built-in `push` up |
| Counter roll | 18 f, lands ±5 f on the number word |
| Stinger | rise 16 f ease-in, hold 6 f, lift-off 16–18 f ease-out (38–40 f), no blur |
| Roll-by | 9 f bottom → top, Ø ≈ 1150 px, ≈ 120° rotation, the cut at f 4–5 |
| End card | a hard cut in; the logo row rises 180 px over 8–10 f; the tagline from 10 % opacity, brightening over ≈ 1.5 s |
| Idle drift | cards and receipts keep moving through G-4's creep or G-7's drift, so a card on screen is never frozen |
| Hold | titles and labels ≥ 10 f after they finish; text ≥ 0.25 s per word |

### 10.2 Footage camera
- **F-A `zoom_policy: none`:** there's no footage camera; all movement is inside the scenes: the archive settle, re-crop
  cuts (P-RECROP-CUT), the receipt follow-push (G-4) and the inner card punch + drift (G-7). No camera presets, no shake,
  no rotation (under 0.3° on every measured move).
- **F-B `zoom_policy: crop_on_cut`:** the only "zoom" is the ×1.2 re-crop at a cut (R-3). No push-ins, no shakes, no
  crash zooms.
- The canvas camera is off in this style: the camera never travels over the canvas; pictures cut, and the receipt's
  settle-up and the map card's inner pull are the scenes' own motion.

### 10.3 Tone decides the treatment
| Tone | Where it goes |
|---|---|
| `explain` | W-blue (cards, maps, plates) or the archive run |
| `evidence` | W-blue, B-2 receipts |
| `turn` | W-archive, B-1: a hard cut to a picture |
| `warn` | the `bad` colour on the route, the door, the loss |
| `awe` | W-archive, B-1: the event, the twist, the held payoff picture |
| `cta` | W-end (or W-qr) |

### 10.4 Layer order (back to front)
1. World (W-blue / W-green / W-white / W-end / W-qr; F-B footage)
2. Full-bleed archive pictures and plates (z2, opaque)
3. Cards: photo, map / locator, comparison, figure (z3)
4. Receipt text blocks, figure values, inner media (z4)
5. Overlays: particles, name plates, chips, avatars (z5)
6. Stingers and roll-bys (z6, momentary); the top-slot tag when one is used (z6, never near the band)
7. Captions (`__subtitles`, z7): above everything except the end card
8. End card (z10 on L-end)

### 10.5 Finishing
- W-blue and W-green carry 3 % film noise (a static texture); W-end 5 %. No vignette, no light leaks, no bloom, no grain
  on footage.
- Card radius 40 (photo cards, maps, figures); inner media radius 8; thumbs and caption boxes square (radius 0).
- Shadows: cards `0 26px 70px rgba(0,0,0,.28)` on W-blue only; nothing else has a shadow except the CS-B text shadow.

---

## §11 Sound

| | F-A | F-B |
|---|---|---|
| **Cue moments** | the hook (the stinger's cover peak), transitions (stingers and roll-bys only), reveals (the lime highlight of a receipt, one per receipt; a counter landing; a pin on the payoff map), the CTA (the Follow → Following change) | the CTA only (the QR card's entrance) |
| **Meme cues** | off | off |
| **Music bed** | on from f0 (a low documentary pulse under the hook), ducked; it drops out 0.5 s before the payoff picture and comes back on it | off: the room tone of the conversation is the bed (`timeline.audio.bed: null`) |
| **Ducking** | the bed ≥ 18 dB under the voice while it speaks | the creator's dialogue mix is kept; nothing is added under it |
| **Loudness** | −14 LUFS integrated, true peak ≤ −1.5 dBTP, a hard end ≤ 6 f after the last word | the same |

Sparse is the sound of authority: the cut is the drama, and a cue only marks a landing (a receipt turning lime, a number
arriving, a chapter turning). If in doubt, leave it out. Which sounds, and their vibe, come from the bundled SFX pack and
its global rules for a balanced energy.

---

## §12 Footage handling

### 12.1 Setups
| Setup | F-A voice-over (VO) | F-B two-camera conversation (POD) |
|---|---|---|
| Capture | A close dynamic or small-diaphragm condenser mic, 15–20 cm, a pop filter, a dry room (no echo) | Cam A host single and cam B guest single at eye height, 3/4 angles, eyelines off-camera toward each other; an optional cam W wide two-shot; one mic per person (dynamics on arms, visible is fine) |
| Delivery | A steady news read, 2.6–3.0 words per second, sentences of 8–16 words; recorded paragraph by paragraph | Natural conversation; the creator marks the moments worth clipping |
| Framing | — | Head-and-shoulders singles with room above the head; 16:9 4K (or vertical 1080 × 1920) so 9:16 crops keep the head top at y 140–300 |
| Light / set | — | Warm practicals, depth behind each person (shelves, lamps, maps); the set is the archive mood |
| Rate | 48 kHz WAV | 30 fps (or 25/60 conformed), every camera the same rate |

### 12.2 Shots and fallbacks
| ID | Shot | Spec | Must / optional | Format | If missing |
|---|---|---|---|---|---|
| SH-1 | Archive / reference photos the creator owns or holds | ≥ 1080 px short side for full-bleed; faces, places, objects, documents; the more the better (8–15 a minute makes it a documentary) | optional (fidelity) | F-A | FB-1 |
| SH-2 | Archive / B-roll clips the creator owns or holds | 2–8 s each, ≥ 720p (cards) / 1080p (full-bleed) | optional | F-A | FB-2 |
| SH-3 | Screenshots of the cited articles, taken by the creator | the full headline, the outlet and the date visible | optional | F-A | FB-3 |
| SH-4 | Map images the creator exported or owns | locator, route or region; ≥ 1080 px wide | optional | F-A | FB-4 |
| SH-5 | Cam A: host single | 4K 16:9 or vertical 1080p; the whole clip | **must** | F-B | FB-5 |
| SH-6 | Cam B: guest single | the same height and lens as cam A | **must** | F-B | FB-6 |
| SH-7 | Cam W: wide two-shot | locked off, both people, the room | optional | F-B | FB-7 |
| SH-8 | Brand logo (PNG / SVG, transparent) | square-safe, ≥ 512 px | optional | both | FB-8 |
| SH-9 | Thumbnail + title of the creator's own long video | 1280 × 720 | optional | F-A | FB-9 |
| SH-10 | QR image of the creator's URL, or the URL | PNG / SVG | optional | both | FB-10 |

| ID | For | What gets built instead | What it costs | Format holds? |
|---|---|---|---|---|
| FB-1 | SH-1 | The real photos fetched from the web (press, official pages, public archives), source noted; where none turn up, created archive plates: P-SILHOUETTE-PLATE (people), P-OBJECT-PLATE (things, places, products), P-DATE-PLATE (years), all GR-halftone | Plates only: no real faces or places; the montage reads designed rather than documentary | holds (fetched) / degraded (plates) |
| FB-2 | SH-2 | A real clip fetched (news footage, an official upload) when one exists; else a still or a plate with the archive settle and its slow drift (§10.1) | No live motion inside the shot | degraded |
| FB-3 | SH-3 | The created P-SOURCE-CARD (the outlet set in type, the exact headline from the real article, fetched and read, or the script), or the real article captured from the web | None visible: this is the style's own card | holds |
| FB-4 | SH-4 | A real map image fetched (official or public-domain), in a card; else P-LOCATOR-CARD (pins on a graticule, no coastlines) until the geo-map bundle (E-18) ships | Locator only: no coastlines or borders | degraded |
| FB-5 | SH-5 | A faux single cropped from cam W or the one camera there is (two crops of one wide) | A softer image, no angle change on handovers | degraded |
| FB-6 | SH-6 | A faux guest single from cam W | A softer image; reactions share one angle | degraded |
| FB-7 | SH-7 | Skip R-4 (no wide); end on the speaker's single | No room establish | holds |
| FB-8 | SH-8 | Their logo fetched from their own channel or site; else a typeset monogram disc: the creator's initials in Montserrat 800 on a `primary` disc | No logo artwork | holds |
| FB-9 | SH-9 | The real thumbnail fetched from their channel; else a created video card: the long video's title set in type on a `primary` thumbnail field (no image, no view count) | No thumbnail art | holds |
| FB-10 | SH-10 | The URL chip end card (P-END-QR without the QR, or P-END-TAGLINE `link_bio`) | Viewers type the URL | holds |

A reel where **every** archive picture is a created plate still ships, but say so in one line when you show the
storyboard; with the web to fetch from, it should rarely happen.

### 12.3 Resolution
- No props, no reaction bank, no cut-out: F-A has no presenter, and F-B never needs one.
- Full-bleed archive pictures are ≥ 1080 px on the short side, upscaled ≤ 1.35×. F-B re-crops ×1.2 need a 4K 16:9 source
  (a 1080p 16:9 source is already cropped ×3.2 for 9:16: use a vertical 1080 × 1920 camera, or accept softness and set
  `recrop_step` to 1.0).

### 12.4 Third-party moments: fetch the real thing
1. **Scan** the transcript and script for the moments. Typical in this style: an article headline (→ P-SOURCE-CARD), a
   person (→ P-ARCHIVE-BLEED, else P-SILHOUETTE-PLATE), a place (→ P-ARCHIVE-BLEED or P-LOCATOR-CARD), an event
   (→ P-ARCHIVE-CLIP, or P-DATE-PLATE + a picture), a company or product (→ its real photo or logo, else P-OBJECT-PLATE
   with the name set in type), a quote (→ P-QUOTE-RECEIPT), a chart (→ a B-5 figure built from the script's numbers).
2. **The creator's own files come first;** otherwise search the web and fetch it: the real photo of the person or place,
   the real article (captured and framed on the headline, or read for the typed card's exact words), the real map, the
   real logo. Note where each came from.
3. **Use it as it is:** frame it with its pattern; never alter it to say something else (the §4.3 treatments only). No
   labels, no credit lines, on the creator's, fetched or created pictures alike: the receipt is the citation.
4. **Nothing usable to be found:** create it (FB-1…FB-4, P-SOURCE-CARD, P-QUOTE-RECEIPT) from the exact words; a created
   card quotes only what the source or the script states, word for word.

F-B: the conversation itself is the creator's footage. A third-party moment inside it (a speaker mentions an article) is
**not** illustrated unless the creator asks; then use P-SOURCE-CARD as a 3.0 s stack-free cutaway with the speaker's audio
continuing.

### 12.5 Frame rate and audio
30 fps CFR output, 1080 × 1920, BT.709. F-A: the VO chain (high-pass 80 Hz, de-ess, light compression) → −14 LUFS. F-B:
the session mix of the synced mics → the same chain.

---

## §13 What your plan should settle

Your `ideas.md` is a page or two, for you. In this style it has decided, before any code:
1. **The format** (F-A or F-B) and, for F-B, the moment: the in-point sentence, the button, the tail, the cast and angles.
2. **The thesis and the hook:** the archetype, the chunked thesis with its alternates, the f0 picture, the stinger object
   (or the flurry), the scene tagged `payoff: true`.
3. **The picture-per-chunk map:** every caption chunk marked cut / event / hold, with the trigger word each picture lands
   on, and the one held picture before the answer.
4. **The receipts:** for every cited claim, the masthead, date, headline word for word and highlight spans; any claim
   whose source can't be found left to the caption.
5. **The figures:** `plan/figures.json` resolved (shown vs computed), one scale per compared set.
6. **The inserts** (the creator's / fetched, with the source / created) and the fallbacks used.
7. **The moves:** the transition map (where the stinger, the roll-by, the punches, the deck and the side change fall), the
   re-hook, and for F-B the shots (`speaker`, `angle`, `crop`, `cut_reason`).
8. **The sound:** the cue moments, the bed's entry and its drop-out before the payoff.
9. **The end card:** tagline, device, value, wordmark (asset or monogram).
10. **The moments you'll look at hardest on the storyboard:** f0, the thesis payoff (≈ 2.8 s), one receipt fully built, one comparison card
    or map, the end card; F-B: f0, a handover, the stack (if used, with both heads clear of the seam caption), the end card.

Beat fields this style adds: receipts carry `source {masthead, date, headline, highlight_spans}` and `insert`
(e.g. `source: {masthead: "Financial Times", date: "12 Mar 2025", headline: "<exact headline>", highlight_spans:
["$20bn"]}`); figure beats `figure_id`; comparison beats `side: A | B`; the payoff scene `payoff: true`; the re-hook
`rehook: true`.

---

## §14 Worked examples

The examples use **slots** (`<Company>`, `<$X>`) where a real reel puts the script's facts. Times are planning estimates;
the word onsets replace them. Never fill a slot with a fact the script doesn't state.

### 14.1 F-A, business and brands: "Why <Company> just bought its own rival" (62 s, device `subscribe`)
**Script gist:** "<Company> just bought <Rival> for <$X>, and the person who signed the deal used to run <Rival>. Here's
why. … According to <Outlet>, … Now why would <Founder> sell? … For more business and power, decoded, follow <handle>."
**Assets the creator gave:** 4 photos (the founder, the CEO, both storefronts), 1 article screenshot. Not given: the
regulator's announcement → found on the web, its headline typed word for word, source noted; the rival's old CEO → no
usable photo found, a created plate.

| t (s) | Spoken (gist) | Tone | Pattern | Visual | Caption chunks | Cue |
|---|---|---|---|---|---|---|
| 0.00 | "<Company>'s CEO" | turn | P-ARCHIVE-BLEED (creator photo, untreated, crop 1.18) | the CEO's face tight, drifting 1.18 → 1.17 | "<Company>'s CEO" | — |
| 0.45 | — | turn | P-RECROP-CUT | the same photo at 1.00 | — | — |
| 0.90 | "just bought / <Rival>" | turn | (hold) | — | "just bought / <Rival>" | — |
| 1.20 | "for <$X>," | turn | P-STINGER-STACK (banknote shapes) | the rows cover by 1.60, exit by 2.33 | "for <$X>," (on top of the cover) | hook cue at 1.60 |
| 2.10 | "and the man who signed it" | awe | P-ARCHIVE-BLEED (storefront, GR-bw), no particles (not a celebration) | the storefront, a slow pull | "and the man / who signed it" | — |
| 2.70 | "used to run <Rival>." | awe | P-SILHOUETTE-PLATE (the old CEO, created), `payoff: true` | the silhouette + the name plate "<NAME>" | "used to run / <Rival>." | — |
| 3.40 | "Here's why." | turn | T-01 to W-blue | — | "Here's why." | — |
| 4.0–8.0 | context: founded in <year>, in <city> | explain | P-DATE-PLATE → P-LOCATOR-CARD (1 pin) | "<year>" rolls and lands; the pin pops on "<city>" | as spoken | — |
| 8.0–17.0 | "According to <Outlet>, the deal values…" | evidence | **P-SOURCE-CARD** (the creator's screenshot via `fx.shot` in the text rect) | the headline, "<$X>" lime on its word, the leader, 2 thumbs (the CEO, the old CEO) | as spoken | reveal cue on the lime |
| 17.0–22.0 | "it's the third deal this year" | explain | P-COUNTER-CARD on W-green | the counter lands on "third" (the input from the script) | as spoken | — |
| 22.0–24.5 | "Now why would <Founder> sell?" | turn | **P-QUESTION-TURN** (the founder's photo, beat `rehook: true`) | hard cut, the settle | "Now why would / <Founder> sell?" | — |
| 24.5–38.0 | the two strategies | explain | **P-COMPARE-SWIPE** ×4 (A: <Company> "SCALE", B: <Rival> "LOYALTY", A, B) | side chips red / off-white | as spoken | reveal cue on the first chip only |
| 38.0–46.0 | "the regulator approved it in <month>" | evidence | P-SOURCE-SWAP (a created headline card) | the new outlet, "approved" in lime | as spoken | — |
| 46.0–55.0 | the payoff: who gains | awe | P-BAR-TRACKS (two shares on one scale) → P-ARCHIVE-BLEED of the founder (held 2.6 s: the slow moment) | the bars land on the spoken numbers | as spoken | the bed drops out 0.5 s before the founder's photo |
| 55.0–58.5 | "Watch the full breakdown on my channel." | cta | P-WATCH-FULL (SH-9 thumbnail) | the cursor clicks at +0.6 s | "Watch the full / breakdown" | — |
| 58.5–61.8 | "For more business and power, decoded, follow <handle>." | cta | **P-END-TAGLINE** (T-06) | the tagline: "business" in `end_a`, "power," in `end_b`; the logo disc; Follow → Following at +0.8 s | hidden | CTA cue on the pill change |

**Figures:** `fig-deals` (counter, the input "third" from the script = 3), `fig-shares` (two bars, one `scale_id`).
**Inserts:** I1 the CEO's photo (creator), I2 the storefront (creator), I3 the old CEO (created silhouette), I4 the
screenshot (creator), I5 the regulator's headline (fetched, typed as a `headline_card`, source noted).
**The rhythm:** the first three seconds are dense (the re-frame, the banknotes rising and lifting, two new faces, four
chunks); the receipt slows the cut and fills it with events; the comparison flips on each trait; then the founder's face
holds while the bed drops out, and the answer lands in the quiet.

### 14.2 F-A, places and history: "Why <City> has no skyscrapers" (48 s, device `comment_keyword` "SKYLINE")
| t (s) | Spoken (gist) | Tone | Pattern | Visual |
|---|---|---|---|---|
| 0.00–0.90 | "<City> / has no skyscrapers," | turn | **P-ARCHIVE-FLURRY** (3 creator street photos: colour, GR-bw, GR-sepia) | 0.30 / 0.20 / 0.40 s |
| 0.90–1.90 | "and it's / on purpose." | turn | P-ARCHIVE-CLIP (a creator drone clip) with a punch re-crop at 1.6 | street-level motion |
| 1.90–2.80 | "A rule from <year> / still decides" | awe | P-DATE-PLATE "<year>" (`payoff: true` at 2.6: the thesis complete) | the digits land on the year |
| 2.80–3.60 | "Here's why." | turn | T-02 stinger (building-block shapes) into W-blue | — |
| 3.6–10.0 | where and what | explain | P-LOCATOR-CARD: river + old town + new district pins; P-ROUTE-LINE for the height line | the pins pop on their names |
| 10.0–18.0 | the law | evidence | P-SOURCE-CARD (created; the headline word for word from the script's quote of the law's title), the body span lime on "<N> metres" | — |
| 18.0–21.0 | "Now why would a city say no to money?" | turn | P-QUESTION-TURN on a creator photo of the old town | the re-hook |
| 21.0–36.0 | the old town vs the new district | explain | P-COMPARE-SWIPE (A "HERITAGE", B "HEIGHT") ×4 | photo cards (creator) / plates |
| 36.0–43.0 | the cost (rents) | warn | P-BAR-TRACKS (two rents on one scale) | the values from the script |
| 43.0–48.0 | "Comment SKYLINE and I'll send you the map of every height rule." | cta | P-END-TAGLINE with "Comment" + a lime box "SKYLINE" | the keyword readable ≥ 1.5 s |

### 14.3 F-B, a business podcast: a 44 s clip (host + guest, cams A / B / W, device `qr`)
**The moment:** the candidate whose opening line is "Most founders think the product is the hard part. It isn't." and
whose button is "Distribution is the product.", with a 2.0 s laugh tail.

| t (s) | Speaker | Shot (`timeline.shots`) | Pattern | Caption (CS-B) |
|---|---|---|---|---|
| 0.00–5.40 | guest | B single, step 1.0, `open` | P-B-SINGLE-HOLD (HA-14: chunk 1 at f0) | italic: "Most founders think / the product / is the hard part." |
| 5.40–9.80 | guest | B single ×1.2, `recrop` | P-B-RECROP | italic |
| 9.80–11.40 | the guest speaking, the host "right" | A single, `reaction` (1.6 s) | P-B-REACTION | italic (the guest's words) |
| 11.40–14.10 | guest | B single 1.0 | — | italic |
| 14.10–19.80 | host | A single, `handover` | P-B-HANDOVER-CUT | upright |
| 19.80–24.30 | guest ↔ host, rapid | stack (guest top, host bottom), `stack` (4.5 s) | P-B-STACK, the caption on the seam (one line; both heads clear of it) | per speaker |
| 24.30–31.00 | guest | B single, `handover` | — | italic |
| 31.00–34.20 | guest | W wide, `recrop` (R-4) | P-B-WIDE | italic |
| 34.20–41.60 | guest (the button) | B single ×1.2 | R-7: no cut in the button | italic: "Distribution / is the product." |
| 41.60–44.00 | the laugh tail | L-end | **P-END-QR**: "Watch the full conversation / with <Guest> / at [url]" + QR | hidden |

**Craft:** every handover cut within ±3 f; the longest hold 5.7 s, under the 6.0 s the generator allows. **The feel:** the
guest owns the clip; the host's reaction and the one wide are the only breaths; the button plays untouched, and the laugh
carries the QR card out.

---

## §15 Your look at the storyboard: the checklist

Watch it once as a stranger with a thumb over the next reel, on mute, then once as the editor whose name is on it. Fix
what bothers you, in one pass.

**The style (does it feel like §The feel?)**
- Frame 0: a literal subject, already moving, with the boxed first chunk naming it (F-A); the speaker live mid-thought
  (F-B). Nothing else.
- By 3 s the whole thesis is said and captioned; the first three seconds feel dense, and the turn line arrives fast.
- Every picture is the thing being named or the receipt for it; no mood stock anywhere.
- Every receipt follows the ritual: empty blue, the type-on faster than the voice, lime on the spoken words, the leader,
  the push. Lime appears nowhere else but the dot, an active pin and the end-card box.
- Pictures never just sit; every hold follows a cut; consecutive archive shots change their look.
- Comparison sides alternate A / B with the right chip colours.
- One re-hook turns back on the subject's face in the middle; the payoff is one held picture, the only slow moment.
- Calm authority: no memes, stickers, shakes or dissolves; stingers rare enough to mean "new chapter"; sound sparse.
- F-B: calm holds, cuts on handovers, the button untouched, the QR card over the tail.
- On mute, start to end: the story still lands, and you believed it because you saw the paper.

**Craft (by eye, in context)**
- Faces read: F-B speakers clear of the layers (on stacks, both heads clear of the seam caption); F-A archive faces clear
  of cards, plates, chips, particles and caption boxes; nothing chops a head or buries a face by accident.
- The caption band holds the caption; graphics sit above it while a chunk shows; stingers pass under it; no text over
  text by accident.
- Every cut and card event on its word; receipt highlights on their span; counters on the number; F-B handover cuts on
  the new speaker's first word, never inside a word.
- Every receipt has masthead, date and a word-for-word headline; every span occurs in it; quotes word for word and
  attributed; an F-B clip never re-ordered.
- Every number on a card is in `plan/figures.json` and shares a scale with what it's compared to.
- Every third-party picture is the creator's, the real one fetched (source noted) or a created plate; no flags, maps or
  logos drawn from memory; no credit lines, source lines or labels under any picture.
- Proper nouns spelt exactly; outlet names as the outlet writes itself.
- Captions: one box per chunk (CS-A) / per line (CS-B), hard swaps, ≤ 2 lines, readable on a phone; hidden only on the
  end card.
- Full-bleed pictures sharp (≥ 1080 px on the short side, upscaled ≤ 1.35×); personal identifiers in screenshots blurred.
- The end card ≤ 3.5 s with its action readable; every open loop paid.
- The file itself (1080 × 1920, 30 fps, −14 LUFS, the bed under the voice, a hard end ≤ 6 f after the last word) is the
  render's job; it checks it.

---

## §16 Build notes

- **Fonts to pre-load:** JetBrains Mono (400 / 500 / 700), Space Grotesk (600 / 700), Inter Tight (700 / 800), Montserrat
  (700 / 800), and Noto Sans Devanagari when the captions are Hindi.
- **Engine built-ins this style leans on:** `step_fps: 12` on every graphic scene (never on archive clips or built-in
  transitions); `VEOS.fx.resolve` for the outlet line, the chip trait word and the end tagline (always with a `seed`); the
  built-in `push` (`dir: "up"`, `frames: 4`) for the side change, which also carries the incoming card up from below where
  the evidence has it already underneath; `fx.shot` for a creator's screenshot inside the text rect; `fx.clip` for
  archive clips; `VEOS.data.counter` / `VEOS.data.bars` for figures; `fx.icon` for object plates; an optional clip track +
  scene `anchor` for a label on a moving thing (§8.8).
- **What isn't built in:** geo maps (E-18; P-LOCATOR-CARD stays the fallback) and the receipt follow-push as a camera (the
  canvas camera is off here, so G-4 is the scene's own scale + translate, at the measured ×1.14 over 24–27 f).
- **Declare every picture change as a cut** (`cuts: [0]` on the incoming full-bleed or card scene) and every in-card
  change as an `event`, so the engine knows where the picture moved.
- **Performance:** archive stills are single images with a CSS filter; keep particles ≤ 30 and stinger rows to four.

---

## Appendix A. Evidence map
| What | Measured | Where |
|---|---|---|
| CS-A 58 px mono in one black 60 % box per chunk, block centre y 1415 | "The King of FIFA" ≈ 61 px mono; box sampled `#060D37` over `#132595` | v01 @0:00, @0:15; v02 @0:10 |
| The receipt: empty blue, word-by-word type-on, lime `#CCF852` key span, follow-push ×1.145 | ORB scale 1.000 → 1.146 over ≈ 22 f at 23.98 | v01 @7.93–8.80, @14.52–15.40 |
| The hook stinger: covers at 1.63, holds ≈ 6 f, lifts off by 2.43, the caption on top | 38–40 f at 30 fps | v01 @1.09–2.43 |
| Archive settle −3.8 % in ≤ 5 f, then static; hook face drift 0.4 %/s | ORB 0.962 / 0.998 | v02 @45.15–45.95; v01 @0.45–1.05 |
| End tagline ≈ 138 px, tracking ≈ −0.04, x 93, cap top 151; the logo disc Ø ≈ 295 | — | v01 @1:18–1:20; v02 @0:57–0:59 |

The full map, the inferred devices and the unverified list are in `evidence.md`.

## Appendix B. Hook-title bank
Each line is the first 3 s of captions (chunks separated by " / "), with its archetype. The post title repeats the thesis
in ≤ 9 words.

**F-A Archive explainer**
| # | Hook chunks | Archetype |
|---|---|---|
| 1 | "<CEO> / just bought / <Rival> / and it involves / <Regulator>." | HA-11 |
| 2 | "<Brand> / quietly killed / its best-seller. / Here's why." | HA-11 |
| 3 | "$<X> billion / is what <Company> / paid for / a company / with no revenue." | HA-07 |
| 4 | "<Company> / told investors / it will stop / selling <X>." | HA-12 |
| 5 | "<Founder> / was fired / from <Company>. / Then he / bought it back." | HA-11 |
| 6 | "<City> / has no skyscrapers, / and it's / on purpose." | HA-19 |
| 7 | "<Country A> / and <Country B> / share a border / nobody can cross." | HA-11 |
| 8 | "In <year>, / one decision / still decides / how <City> looks." | HA-19 |
| 9 | "<N> countries / vote on this, / and one man / decides." | HA-07 |
| 10 | "<Sport> in <Country> / looks a lot / different. / Here's why." | HA-19 |

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
