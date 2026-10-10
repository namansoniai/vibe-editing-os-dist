# Long-form Re-cut Style Playbook (template v2)

## The feel

This reel is a documentary you walked into mid-sentence. Frame 0 is already moving: a render gliding round a machine, the
creator mid-gesture, a guest turning the object in their hands. Two or three white serif words sit low in the frame,
already talking. Nobody says hello. The first sentence is a paradox or a problem so complete on its own that the viewer
needs the answer, and the only way to get it is to stay.

What holds them is the argument, not the edit. One question opens on the first words and closes on the last: a problem,
how it works, the proof that it works, why it matters. Inside that arc the picture is calm: the creator's own shots, held
as long as the master held them, while the captions swap on every breath of the voice. Still picture, moving words. That
contrast is the pulse of the style, and it's why a long render never feels long.

The creator is treated as an authority, not as content. Their footage is never decorated, regraded or zoomed; it's
reframed with care, so the face, the object and every baked number survive the turn to vertical. A diagram that can't
survive the crop sits whole as a band over a soft copy of itself. When someone else speaks, the words turn gold, even
while the picture shows the creator listening, so the viewer always knows whose voice it is.

Restraint is the brand. No banners, no stickers, no sound effects, no punch-ins: the only thing the edit adds is the
words. The one lift is the proof landing ("And it works."). The end is quiet and certain: the line that says why it
matters, then it stops, with no goodbye. Gold means another voice and nothing else, always.

**The test:** pause on any frame and you see only the creator's own picture, kept whole, and a few serif words whose
colour tells you who is talking; anything the editor drew to get attention is wrong.

## What this playbook is

You're turning a creator's own finished long-form video into one vertical short of about two minutes, and you have the
authority to make it the short that sends people to the long one. This playbook is the style, pulled from three of
Veritasium's vertical re-cuts of its own long-form videos (v01 the antiproton decelerator, v02 the portable antimatter
trap, v03 falling into a black hole) and measured at full resolution and full frame rate. Read it all, every time. Here
the best edit of your life is mostly invisible: the craft is choosing the argument, choosing the first sentence,
reframing every shot and captioning every voice. Your instinct to add something will usually be wrong; your instinct to
choose better is always right.

**Who it's for and what it needs.** Creators who publish edited long-form explainers, documentaries, interviews or essays
and want shorts from them: science, engineering, money, history, anything with an argument. Input: the finished 16:9
master (4K crops sharpest; 1080p works, softer), the cast (who the host is, who the guests are) and, for the optional end
line, the long-form's exact title. Nothing is shot and nothing is built except captions: the master is the product (§12).
No cut-out. Captions follow the master's language (English verbatim by default; Hinglish romanised; Hindi in a Devanagari
serif, §5.5). Reels run 110–150 s, one format (F-A, "Master re-cut"). Machine values live in `tokens.json`; where this
text gives a number tokens also holds, they agree.

### Style directives (non-negotiable)
| # | Directive | Where it lives |
|---|---|---|
| D1 | **One argument, whole.** The reel is one self-contained sub-story (problem → mechanism → proof → implication) of 110–150 s, cut from the master. It never refers to anything outside itself | §12.4, §7.1 |
| D2 | **Walk in mid-thought.** Frame 0 is moving master picture with the caption already running. No title, no banner, no hook graphic | §6.2 |
| D3 | **Reframe, don't redraw.** Never rebuild, regrade or decorate the master's visuals. Crop, follow or band them | §3.3, §8.3 |
| D4 | **The voice decides the colour.** Host white, guests gold, decided per word from the diarised voice, never from the face on screen | §5.3, §9.3 R-3 |
| D5 | **The master's cuts are the reel's cuts.** No added cuts, re-crops, punch-ins or zooms; the only new cuts are splices between master spans at sentence boundaries | §9.3 |
| D6 | **Captions carry the pace.** Word groups swap hard on the voice, timed to the speech and never snapped to the cuts; the master's pauses up to 2.0 s stay as blank-caption breaths | §5.3, §7.5 |
| D7 | **Silence of graphics.** Nothing is drawn on the master but the captions, a rare italic object title and, when the creator chose it, one end line | §5.4, §8.1 |
| D8 | **End on the implication.** The last sentence is the "why it matters" line; hard end ≤ 6 f after its last word | §7.1, §8.3 P-LAST-LINE-END |

### Quick index
| § | What |
|---|---|
| §1 | Procedure: how to approach a reel in this style |
| §2 | Hard rules: the craft and the style's never-list |
| §3 | Worlds, layouts, reframe classes RF-1…RF-4, stage moves, safe zones, the person |
| §4 | Colour: the voice axis, white and gold |
| §5 | Type and captions: CS-1 voice-coded serif captions, object titles, the end line, created cards |
| §6 | Hook system: stopper test, HA-14 Cold authority (a, b, c), HA-10, HA-15, hook pairs, the first line, CTA |
| §7 | Structure and rhythm: the explainer arc, the world rotation, open loops and re-hooks, rhythm by feel |
| §8 | Visual system (B-roll and patterns): families, 4 overlay patterns, 19 cut and reframe patterns, line → pattern lookup, truth, assets |
| §9 | Transition system: T-CUT, T-DISSOLVE, T-END, T-END-FADE; shot grammar R-1…R-10 |
| §10 | Motion tokens, footage camera, layers, finishing |
| §11 | Sound: the master's mix, nothing added |
| §12 | Footage handling: the master, shots and fallbacks, reading the master, finding the argument (SS-1…SS-8), third-party spans |
| §13 | What your plan should settle |
| §14 | Worked examples (3) |
| §15 | Your look at the storyboard: the checklist |
| §16 | Build notes |
| App. A / B | Evidence map / post-title and first-line bank |

---

## §1 Procedure: how to approach a reel in this style

You watch, listen, plan, build and look at the storyboard yourself; the edit skill has the mechanics. This style's
craft is three decisions, and everything else is light: **which argument** to lift out of the master, **which sentence**
opens it, and **how every master shot turns vertical**. The rules for finding the argument live in §12.4, for whoever
makes the cut; when the cut arrives already made, read it with the same eyes, and say so if it fails a test.

1. **Know the master** (§12.3). Its resolution (4K crops stay sharp; a 1080p master upsamples its crops up to 1.78×,
   FB-2), its chapters if it has them, its cast (who narrates, who the guests are), and its own cut list: every reel cut
   comes from it.
2. **Find the argument** (§12.4). One self-contained span of 110–150 s that passes all eight tests, SS-1…SS-8. Rank the
   passes by the strength of the first image, then by how many worlds the span visits (host, render, guest: more is
   better). The best goes forward; keep the next two as alternates.
3. **Choose the in-point** (§6). Every sentence in and around the span that could open it, ranked by the stopper test:
   HA-14a image-first when a render opens it, HA-14b host-first, HA-14c guest-first, HA-10 or HA-15 when the master hands
   you one. Keep the best and two alternates, and write the post title (8–10 candidates, App. B).
4. **Give every voice its colour** (§5.3). Name the host and the guests; then listen to every handover and every shot
   where the picture shows someone other than the speaker. The colour follows the voice.
5. **Reframe every master shot** (§3.3). One class per shot, the first that fits: follow the face, centre the window,
   band it, or treat the two-shot. Look at every centre-crop's middle frame after the render; if the subject or its baked
   text is cut, band it.
6. **Feel the tone of each sentence:** `explain` (the default) · `awe` (a reveal, a striking image) · `warn` (a risk, a
   failure) · `win` (it works, the record) · `cta` (only the end line). Tones choose nothing visual here; they show you
   where the one lift is and where the reel goes quiet.
7. **Walk the span as a viewer** (§7). Does the world rotate? Does something new arrive whenever attention could sag? Does
   the question opened at frame 0 stay open until the proof? Mark the re-hook beats.
8. **Keep the third-party spans as the master has them** (§12.6): they're the real thing, already published. Name them
   in a line when you show the storyboard; blur any legible identifier.
9. **Decide the few overlays, usually none:** an object title where the master shows an object it never names; the end
   line, if the creator chose it.
10. **Decide the ending:** a hard end on the implication's last word, or the 5 f fade when the last shot is a render whose
    narration has already ended.

---

## §2 Hard rules: the craft and the style's never-list

**Craft, by eye** (judge it on the storyboard, in context, the way an editor does):
- **Keep the person whole and clear.** On every face the reel shows, keep the head region (face, hair and the room above
  the head) clear of the layers in front: the caption, an object title, a card. A head in the caption band usually means
  the crop is wrong; fix the crop rather than push the caption up over the head. Keep the top of the head inside the
  crop, and never cut the face at the eyes or forehead. What's never fine is a head chopped or a face buried by accident.
  The geometry is in §3.7.
- **No text over text.** One caption line; an object title or end line sits in its own band clear of the caption (§3.6);
  never two speakers in one chunk.
- **In sync with the voice.** A chunk appears 1 f before its first word (lead at most 0.15 s, lag at most 0.10 s) and never
  leaves before its last word ends. Chunks are voice-timed and run across master cuts. The master's sound is never
  offset; a splice carries the engine's 8 ms equal-power crossfade.
- **The right colour on the right voice.** Every chunk holds one speaker's words: host and narrator white, every other
  voice gold, checked by ear on every shot where the picture and the voice belong to different people.
- **Say what was said.** Captions are verbatim; numbers exactly as spoken ("16.2 million", "99.9%", "614 days"). A splice
  never re-orders or re-attributes a quote or a number, and never attaches a number to a different subject.
- **The master as published.** Nothing in it is altered. Its third-party spans are the real thing and stay as the master
  has them; only a span the creator has ruled out for shorts is trimmed, or covered by a created card that quotes the
  script word for word (§12.6).
- **Baked text survives.** A crop never cuts a baked label, number or title in half ("16,200,000" cut to "6,200,00"): it
  stays whole inside the crop with a 24 px margin, or the shot is banded.
- **Reframe integrity.** One fit per master shot for its whole duration; fits change only on master cuts or splices;
  upscale never beyond 2.0×.
- **Promise integrity.** A cross-promo end line names the long-form's exact title and stays on screen ≥ 2.0 s.
- **Spelling.** Names, units and technical terms exact in the captions (the glossary, §12.3).
- **Privacy.** An email, phone number, address, ID or key legible in the master is blurred for its whole time on screen
  (P-REDACT).
- **Readable.** Captions 70 px with the hairline stroke and soft shadow, so white and gold both read on bright labs, white
  renders and maps.
- **Audio.** −14 LUFS integrated, true peak ≤ −1.5 dBTP; the reel ends ≤ 6 f after the last word, with no black tail
  longer than 0.2 s.

**Never in this style:**
- Redrawing, recolouring, regrading, sharpening, stylising or "enhancing" the master: no LUTs, grain, vignette or glow.
- A banner, headline slab, sticker, emoji, progress bar, chapter marker, logo bug, subscribe button or arrow.
- A zoom, punch-in, shake, whip, speed ramp, freeze-frame or re-crop jump inside a master shot.
- A caption coloured by the face on screen; two speakers in one chunk; an emphasised word (no bold, colour, size or italic
  change inside a caption).
- An in-point after the first word has started (a clipped first syllable); an opening on a band, on black, on a title card
  or on the master's intro or logo sting.
- A sponsor read, ad, mid-roll, merch plug or "link below" span; the master's end screen or subscribe animation.
- B-roll pulled from elsewhere in the master to cover a gap or "fix" the pace. Only whole sentences move, with their own
  pictures (P-SPLICE).
- Music, SFX, risers or a second bed over the master's mix.
- A morph between fits: a band never animates into full frame; fits switch on cuts.
- A created card dressed up as the master's footage: a card is plainly type on black.
- A black tail or an end screen.

---

## §3 Worlds, layouts, stage moves, safe zones

### 3.1 Worlds
| ID | Kind | Look | Carries | Enter / exit |
|---|---|---|---|---|
| **W-master** | footage | The master's own picture, reframed to 9:16 (composed by `veos shots render`) | Everything: host, guests, renders, B-roll, maps | From f0; left only for W-void spans |
| **W-void** | void | `#000000`, nothing else | Created substitute cards (P-SUBSTITUTE-CARD) and the black around letterbox bands | Hard cut in and out |

Inside W-master the master supplies four sub-worlds you track for the re-hooks and the reframe decision (they aren't
separate tokens): the **host world** (the creator to camera in their room, chest-up), the **field world** (handheld
location and interview footage), the **render world** (CAD, animation, simulation) and the **UI world** (HUDs, screen
recordings, diagrams with text).

### 3.2 Layouts
**Stage layouts** (timeline `stage[]`):

| ID | Engine | Rects | Caption |
|---|---|---|---|
| **L-master** | `full` | The composed 9:16 master footage, full frame 0–1080 × 0–1920 | fixed_y, cy 1380 |
| **L-band-black** | `letterbox` | Band x 0–1080, y 656–1264 (`band_h` 608, `cy` 960), fill `#000000`, `face: 0` (fit the whole 16:9 frame), `src` = the inserted clip | fixed_y, cy 1380, under the band |
| **L-band-blur** | `blurfill` | The same band over a blurred copy of itself (`blur_px` 40, `luma` 0: undimmed, measured as bright as the band or brighter, `scale` 1.15) | fixed_y, cy 1380 |
| **L-void** | `hidden` | No footage; W-void black; the card area x 64–1016, y 560–1200 | fixed_y, cy 1380 |

With a 16:9 master the stage is `L-master` for the whole reel: the bands of RF-3 shots are composed **inside** the
footage by `veos shots render`, at exactly the `L-band-*` geometry (a centred 1080 × 608 band at y 656–1264). The
`L-band-*` stage layouts are for creator-supplied 16:9 clips that aren't part of the master, and for vertical masters
(§12.3). `L-void` is used only under a created card.

### 3.3 Reframe classes: the crop for every master shot
One class per master shot. Take the first that fits, in this order:

| ID | Class | When | `timeline.shots` angle | Result |
|---|---|---|---|---|
| **RF-1** | Face follow | One person is the subject and their face is ≥ 6 % of the frame height for at least half the shot (host to camera, a guest interview single, a walk-and-talk) | that person's single angle (`kind: host_single` / `guest_single` / `single` in angles.json) | 9:16 crop, face at 17 % of frame height, eyes at 36 % of the crop height, dead-zone follow (12 % of the crop, 0.6 s time constant), ≤ 2.0× upscale |
| **RF-4** | Two-shot | Two faces side by side are both the subject (host and guest in one frame) | the two-shot angle (`kind: two_shot`) | A cover crop if both fit 9:16 (they rarely do), else the band |
| **RF-2** | Centre crop | No face is the subject, and the subject **plus any baked text it needs** lies inside the centre window x 0.342–0.658 of the source width (a full-height 9:16 window of a 16:9 frame keeps 31.6 % of its width) | the host single angle (with no face in the shot the compositor holds a centred window sized from the host's median face: full source height on a chest-up master) | A static centred 9:16 window; the master's own camera motion plays inside it |
| **RF-3** | Band | Anything else: baked text, labels or numbers wider than the window, UI and HUDs, screens, diagrams, maps with routes, wide establishing action, two subjects far apart, an off-centre subject | the wide angle (`kind: wide`) | A centred 1080 × 608 band at y 656–1264 over a blurred, undimmed copy (blur-fill); on black renders it reads as a letterbox on black |

- **Check every RF-2 shot.** The compositor searches ±3 s for the angle's face, so a faceless shot near the host's shot can
  be framed on the host's position. After the render, look at each RF-2 shot's middle frame; if the subject or its baked
  text is cut, make it RF-3.
- **The band's backdrop is undimmed.** The real blurred copy is as bright as the band or brighter (v03 @ 1:29.7: surround
  luma 150 vs band 104). `dialogue.blur_dim` is 1.0, so `veos shots render` composes it at full brightness. Never darken
  it (below 1.0 only if a creator's own footage needs it for caption contrast).
- **The band's look:** the compositor applies one fallback to the whole reel, so render with `--fallback blurfill`
  always (on a black-ground render the blurred copy is black, the letterbox look of v02 @ 0:58–1:11). Use
  `--fallback letterbox` only when nearly all of the reel's band shots are bright UI on white grounds and the creator
  prefers bars.
- **The band is the exception.** The style lives full-bleed: every one of the 23 frames sampled in the fidelity audit was
  a full-bleed reframe. Band a shot because the crop would break it, never for variety, and never in the opening
  seconds: the first picture is always full-bleed. A span that needs long runs of band to make sense is a weaker span
  (measured: bands were 14 % of v02 and 22 % of v03).
- **Fits follow the master's shots;** there is no layout rhythm of your own.

### 3.4 Stage moves
| ID | Move | Recipe | Use |
|---|---|---|---|
| **G-1** | Fit switch on a cut | 0 frames: the new shot arrives already in its fit (full or band); measured v03 @ 1:33.37 band → band, 1:29.87 band → full | Every master cut where the fit changes |
| **G-2** | Cross-shoot splice | T-CUT, 0 f, the captions swap on the same frame (measured v03 @ 1:29.87: HUD band → the host at night). No dip | A splice between two different shoots (wardrobe, room or time of day changes) |
| **G-3** | Void card in / out | Hard cut to `L-void` and back, on sentence boundaries | P-SUBSTITUTE-CARD only |

No other stage move exists: no morphs, no panels, no picture-in-picture, no stacks.

### 3.5 Layout diagrams
```
L-master, RF-1 (host or guest)              RF-3 band (blur-fill / black)
┌─────────────────────────┐ 0               ┌─────────────────────────┐ 0
│ (IG top UI, keep clear) │ ← y 0–110        │ blurred copy, undimmed  │
│        head top         │ ← y 150–260      │   of the same shot      │
│      ╭──────────╮       │                  │ (black on black renders)│
│      │  FACE    │       │ ← face ≈ 17 % H  ├─────────────────────────┤ 656
│      │ eyes ≈   │       │   (≈ 326 px)     │   16:9 BAND 1080 × 608  │
│      │ 36 % of  │       │                  │   the master's frame,   │
│      ╰──────────╯       │                  │   whole and uncropped   │
│    shoulders / chest    │                  ├─────────────────────────┤ 1264
│   [object title 1230]   │ ← rare           │  [object title: 590]    │ ← above the band instead
│  ── caption cy 1380 ──  │ ← 70 px serif    │  ── caption cy 1380 ──  │ ← under the band
│                         │                  │                         │
│ (IG bottom UI y > 1540) │                  │ (IG bottom UI y > 1540) │
└─────────────────────────┘ 1920            └─────────────────────────┘ 1920
```
```
RF-2 centre crop (16:9 source → 9:16)       L-void (created card)
source 1920 wide:                           ┌─────────────────────────┐
│░░░░░░░░░░│ window │░░░░░░░░░░│            │  #000000                 │
0         656     1264       1920           │  kicker y 600 (26 px)    │
the subject + its baked text must sit       │  quote/headline 52 px    │
inside x 656–1264 (34.2–65.8 %)             │  y 660–1080, ≤ 3 lines   │
                                            │                          │
                                            │                          │
                                            │  ── caption cy 1380 ──   │
                                            └─────────────────────────┘
```

### 3.6 Safe zones and bands
- Meaning text stays inside x 64–1016, y 110–1500.
- **The caption band:** centre y 1380, one line, max width 900 px (x 90–990); the line occupies about y 1345–1415. The
  same in every layout and fit.
- **The object-title band:** cy 1230 on full-bleed shots (bottom ≤ 1265, ≥ 80 px above the caption's top); cy 590 on band
  shots (above the band's top at 656).
- **The end-line band:** cy 1250 (one line) or 1220 (two lines), for the last 2.0–3.0 s.
- Nothing is drawn below y 1540, above y 110, or right of x 970 between y 900 and 1540 (Instagram's buttons).

### 3.7 The person
- **Presence is whatever the master shows** inside the chosen span: measured, the host is on screen about 40 % of v01,
  55 % of v02 and 5 % of the animation-led v03, with absences up to about 90 s. Never insert host shots from elsewhere to
  raise it. When the render explains, the render gets the screen; when the creator claims, the master already gave them
  the face.
- **The follow crop (RF-1):** the face about 17 % of the frame height, the eyes at 36 % of the crop height (y ≈ 690), the
  head top at y 150–260 (measured v02 @ 0:00–0:17: ≈ 150–230). So there is room above the head, and Instagram's top bar
  (y 0–110) never touches it. On the host the face is centred horizontally. Crops are near-static per shot (the bookshelf
  stays put while the host moves within it), so the follow moves only when the face would leave the frame; a guest single
  may keep its face off-centre, even touching the frame edge, when the master framed it so (v01 @ 0:44.6).
- **The head region and the caption:** on a chest-up crop the chin sits hundreds of px above the caption band (about
  y 1345–1415), which lies on the chest. `avoid_face` is on as a safety net, but when a crop puts any head into the
  caption band, the fix is the crop (band the shot, RF-3), rather than a caption pushed up over the hair or into the room
  above the head. On band shots every face is inside y 656–1264 and the caption's top sits about 80 px under the band.
- **Object titles** (cy 1230 full-bleed, cy 590 on bands) go only on shots where no head reaches their band, 40 px clear.
- **Hands** may leave the crop; a hand pointing at baked content outside the crop is a reason to band the shot.
- **No cut-out,** so nothing is layered behind anyone: there's simply nothing of ours to put there.

---

## §4 Colour

### 4.1 Role palette
| Role | Hex | One job | Text on it | Contrast |
|---|---|---|---|---|
| `primary` | `#FFFFFF` | Host and narrator caption text | `ink` | 21:1 vs the `#000` shadow; holds on footage through the hairline stroke and soft shadow |
| `accent` | `#E8CC28` | Guest caption text: every voice that isn't the host (sampled at full resolution, v01 @ 1:00 / 1:30, v02 @ 1:30) | `ink` | 14.6:1 on `#000`; holds on bright footage through the stroke |
| `ink` | `#000000` | Caption shadow (the stroke is `#111111`), letterbox fill, card ground | — | — |
| `paper` | `#FFFFFF` | Object titles, the end line, created-card text | `ink` | 21:1 on black |
| `night` | `#000000` | The void and the letterbox ground | — | — |
| `muted` | `#B9B9B9` | The card kicker and small text on cards | — | 10.4:1 on black |

The creator's copy may replace the gold with one brand colour, as long as it stays a warm, light, saturated hue that
reads on any footage and can never be mistaken for white (OKLCH L 0.72–0.90, C ≥ 0.10). The host's white never changes.

### 4.2 Meanings
- **The axis is the voice: host → guest = white → gold.** It answers "who is talking?" without a name plate.
- White anywhere else means the editor's own words (an object title, the end line), always in serif.
- The master's colours (renders, sets, maps) are never altered and never echoed in the editor's layer.

### 4.3 Rules
- White and gold are the only colours the edit adds; the footage's own hues don't count against anything.
- Every caption, white or gold, keeps the 1 px `#111111` hairline and the `0 2 8 rgba(0,0,0,.75)` shadow, so gold reads on
  bright maps and white labs (v02 @ 2:24, v01 @ 0:29).
- Gold goes on nothing but a guest's words.
- No themes, no grades: the master is never regraded, and the look never changes between reels; only the master does.

---

## §5 Type and captions

### 5.1 Font map
| Slot | Family | Weight / style | Close alternative | Used for |
|---|---|---|---|---|
| `serif` | **Source Serif 4** (bundled, variable 200–900, opsz 8–60) | 600 captions; 500 end line; 600 card body | EB Garamond 600 | Speech captions, the end line, created-card text |
| `title` | **EB Garamond** Italic (bundled) | 500 italic | Instrument Serif Italic | Object titles |

Only bundled open fonts. A logo is never set as type for a brand that isn't the creator's.

### 5.2 Headline element
None (`type.headline.kind = none`). Frame 0 is the moving master plus the caption (D2); no banner, pill, lockup or title
card ever appears.

### 5.3 The captions: CS-1 voice-coded serif
`captions.profiles.CS-1` extends `lib:veritasium`, tuned to the measured frames. It's the only text that's always there,
and with the sound off it tells the whole story: captions were on screen for 88–92 % of every reference reel.

| Group | Value |
|---|---|
| Mode | `full`, role `primary`, `mute_safe` |
| Chunking | unit `group`; 1–4 words per chunk (the engine settles on 1–3; measured average 2.3); max 22 characters a line; **1 line**; never split a name, number or unit; a sentence end always breaks (`punct_break`); a pause ≥ 0.9 s always breaks |
| Timing | lead **1 frame** before the first word; min hold 0.2 s a word; swap **hard, 0 f** (`exception: "E6"`: the band holds its place within ±4 px while its words change in 0 frames; never used for a new element appearing); after the last word of a phrase the chunk holds 0.3 s (`tail_s`), then the band is **blank** through the pause (`pause_hold_s: 0`). Measured chunks last 0.4–0.6 s in fast speech (v01 @ 1:19.70, 1:20.20), up to about 1 s in slow narration |
| Voice-timed | Chunks follow the voice, never the cuts: a chunk runs across a master cut (v02 @ 0:20.83 by 3 f; v02 @ 0:35.28 a guest's gold chunk by 4 f over the host's laugh), and a J-cut voice turns the caption gold before the picture changes (v01 @ 0:44.57, 2 f early). Never snap chunk edges to cuts; never hide captions at cuts |
| Skin | Source Serif 4, **600**, **70 px** (measured 70–72), case **as spoken** (sentence case, punctuation kept: "kilometers per hour.", "from 96% to 10%"), tracking 0, colour by speaker, **hairline stroke 1 px `#111111`**, soft shadow `0 2 8 rgba(0,0,0,.75)`, line height 1.1, **no container**. The legibility comes from the shadow; the outline is a hairline at most |
| Position | `fixed_y` **cy 1380**, cx 540, max width 900, centred; identical in every layout and fit (full-bleed, under a band, on a card); `avoid_face: true` |
| Speakers | `host` → `primary` white, upright; `narrator` → `primary` white, upright; `guest` → `accent` gold, upright. The keys match the word labels from `veos speakers name … :host / :guest`. One speaker per chunk; an overlapping back-channel ("yeah", "mm") under the other speaker isn't captioned: only the dominant voice is |
| Emphasis | **none**: no bold, colour, size or italic change inside a caption |
| Variants | none (no karaoke, two-tier, duet or kinetic stack) |
| Hide | only during an added T-DISSOLVE (`hide: ["transitions"]`); never at master cuts or splices, never anywhere else |
| Language | Latin script; `keep_english_terms`; no spelling normalisation (verbatim speech); profanity mask `inner` (S**T); the glossary from §12.3 |

**Animation-led masters** (like v03) carry a lighter, LaTeX-like serif: set Source Serif 4 at 400 there (v03 measured its
captions a little higher, cy ≈ 1341; the template keeps 1380).

**The host stays white everywhere,** on location too: at CERN the host asking on a handheld shot is white (v01 @
1:19.3–1:20.3). Gold over the host's face (v02 @ 1:30) is a guest's voice over the host's picture. There's no separate
"field" colour.

**How the chunks read** (what the engine makes of a typical narration): "One thing / that makes / this research / so
tricky / is that antimatter / is relatively slow / to make." → pause, band blank → (gold) "The only / concept basically /
to overcome / this problem / is to move / the particles." → (white) "And it works."

### 5.4 Other text
| System | Recipe | Hold | When |
|---|---|---|---|
| **Object title** (P-OBJECT-TITLE) | EB Garamond Italic 500, 68 px, `paper`, tracking +0.02 em, shadow `0 2 6 rgba(0,0,0,.7)`, centred; cy 1230 on full-bleed shots, cy 590 on band shots; in: opacity 0 → 1 and y +12 → 0 px over **8 f**, expo-out, starting 2 f before the object's name is spoken; out: opacity 1 → 0 over **6 f** | 1.5–4.0 s, ending at or before the next master cut | 1–3 words, 1 line. Only when the master shows the object and does **not** already show its name. Rare: most reels need none, and two never sit close together |
| **End line** (P-CROSS-PROMO) | Source Serif 4 500, 44 px, `paper`, sentence case, shadow `0 2 6 rgba(0,0,0,.7)`, centred at cy 1250 (two lines: cy 1220, line height 1.15), ≤ 36 characters a line; in over 8 f (opacity); no exit (the reel hard-ends under it) | 2.0–3.0 s, over the last sentence | Only when the creator chose the cross-promo end: "Full video: <exact long-form title>" (+ "on YouTube" or the platform they name) |
| **Created card** (P-SUBSTITUTE-CARD) | Kicker: the outlet or source the script names, as a masthead, Source Serif 4 500, 26 px caps, `muted`, tracking 0.12 em, y 600. Body: the verbatim quote or headline, Source Serif 4 600, 52 px, `paper`, ≤ 3 lines × 26 characters, centred in y 660–1080 | The spoken span it covers (≥ 1.5 s) | Only for a third-party span the creator ruled out that can't be trimmed (§12.6) |
| **Redaction** (P-REDACT) | Gaussian blur 24 px over the identifier's rect + a 12 px margin, keyframed every 6 f to follow it | The identifier's whole time on screen | Any email, phone number, address, ID or key visible in the master |

No lower-thirds, name plates, chips, stickers, step chips or hero numbers: the master names its guests in speech, and the
colour says who speaks.

### 5.5 Language and numbers
- **Spelling:** verbatim speech; technical terms, names and units exact (the glossary). Never "correct" the speaker's
  grammar.
- **Numbers:** exactly as spoken and as the transcript writes them ("16.2 million", "99.9%", "614 days"): never
  converted, never compacted, never turned into figures.
- **Hinglish masters:** `[hinglish, hinglish, Latn]` (transliterated, English terms verbatim) or `[hinglish, en, Latn]`
  (translated; a guest's quoted words then keep their meaning exactly). Same skin, same colours.
- **Hindi masters** (`[hi, hi, Deva]`): captions in **Noto Serif Devanagari** 600 at 70 px (`captions.devanagari_family`),
  so the serif look holds in Hindi. No italic in Devanagari: an object title in Devanagari is weight 600 upright.
- **Indian masters:** Indian number grouping only for drawn text (cards); captions stay as spoken.

---

## §6 Hook system

**The hook here is chosen, not written.** There is no on-screen title in this style: the hook is the master's own first
sentence over its own first moving shot, and your job is to find the in-point that makes a stranger need the answer. The
promise lives in the **post title** (the reel's title on the platform, never shown on screen): it promises the viewer
something (an outcome, a curiosity gap, who it's for) and is true to what the span delivers; it needn't repeat the spoken
words. Write 8–10 post-title candidates from App. B and the proven shapes ("Why your X isn't working", "The X nobody
tells you", "How a 1,000-tonne machine steers underground", a number or a contrast), score them on outcome, curiosity, who
it's for and brevity, pick by the stopper test, and keep two alternates.

### 6.1 The stopper test
| Test | This style |
|---|---|
| Thumbnail | Not used: there's no headline. Frame 0 at a quarter size shows a moving subject, which is enough |
| Mute | The captions of the first 3 s state a complete claim or problem on their own |
| Motion at f0 | Live footage is moving at f0: the render's camera, a gesture, a handheld drift |
| Payoff | The strongest image of the opening is on screen by 1.0 s (it is the f0 shot), and the first sentence is complete, with its period, by 3.5 s (≤ 14 words) |

The opening feels dense in time even though the picture holds: the words swap on every breath while the shot develops
(measured 5–6 caption swaps in the first 3 s of v01–v03, a description, not a target).

### 6.2 HA-14 Cold authority (default)
**Formula:** start mid-thought on the master's strongest moving image, with the first caption already running; let the
first sentence state a paradox, a mechanism in action or a problem; hold the shot (no cut) until the second sentence
lands; the first cut changes world.

| t | Picture (the master, reframed) | Caption (CS-1) | Layout / camera | Sound |
|---|---|---|---|---|
| **f0** (0.00) | The in-point frame: a render in motion, the host mid-gesture, or a guest with the object; RF-1 or RF-2 full-bleed, never a band | Chunk 1 (1–3 words) already on: the in-point sits 0.04–0.10 s before the first word | L-master; the master's own camera move (orbit, dolly, handheld) already running | The master's mix from f0; no added hit |
| 0.0–1.0 | Same shot; the in-shot motion continues (a beam pulse, a hand sweep, a drift) | Chunk 1 → chunk 2 (hard swap, about 0.6–0.8 s) | no cut | — |
| 1.0–2.0 | Same shot; the subject noun becomes visible or active (the ring lights, the ship nears the hole) | Chunk 3 lands on the subject noun ("the antiprotons", "a black hole") | no cut | — |
| 2.0–3.0 | Same shot; in an animation master the baked payoff often lands here (v03 @ 2.2–3.0: the red band crushes the ship, the prohibition ring slams in) | Chunks 4–5; the first sentence ends with its period by 3.5 s | no cut | — |
| 3.0–12.0 | The shot holds as the master holds it (v01 11.5 s, v02 17.75 s, v03 4.6 s) | Sentence 2 states the stake or the problem | no cut unless the master cuts | — |
| 4.6–18 | **First cut = the first world change** (render → host, host → field, animation → animation), on a sentence boundary | Continues | G-1 | — |

All three reference reels pass the stopper test this way.

**Three variants** (choose by what the span's first shot is):

| Variant | First shot | First line shape | Evidence |
|---|---|---|---|
| **HA-14a Image-first** (the default when a render exists) | A render or animation in motion, RF-2 | A mechanism in action or a paradox: "<subject> <does something surprising>" | v01 @ 0:00 "Strong electric fields in the accelerator slow down the antiprotons"; v03 @ 0:00 "You can never see anything enter a black hole." |
| **HA-14b Host-first** | The host to camera, mid-gesture, RF-1 | A problem statement: "One thing that makes <field> so <hard> is…" | v02 @ 0:00 "One thing that makes this research so tricky…" |
| **HA-14c Guest-first** (not in the evidence; allowed) | A guest holding or pointing at the object, RF-1, a gold caption at f0 | The guest's strongest one-sentence claim | Use only when the guest's line passes SS-1 better than any host line |

### 6.3 Alternate hooks
**HA-10 Host flash → subject.** The host's first 2–4 words on camera, then the master's cut to the subject by 0.7 s; the
subject image is the payoff. Use it only when the master itself cuts from the host to the subject within 0.7 s of a
sentence start: never add the cut (R-1).

| t | Picture | Caption | For example |
|---|---|---|---|
| f0–0.7 | Host RF-1, mid-word | Chunks 1–2 | "This machine…" |
| ≤ 0.7 | The master's cut to the subject (render, chart B-roll, location), RF-2 or RF-1 | Chunk 3 | the heat pump's cutaway render |
| 0.7–3.5 | The subject holds | The sentence completes | "…moves four times more heat than it uses." |

**HA-15 Atmosphere.** An animation-led master whose first sentence is slow to arrive: the moving picture carries the
first second or two, and the claim lands by 5.0 s. Use it only when no sentence in the span's first 20 s passes SS-1
inside 3.5 s.

| t | Picture | Caption | For example |
|---|---|---|---|
| f0 | Moving render, RF-2 | The first chunk is still on at f0 | "Imagine…" |
| 0–5.0 | The render develops | The claim lands by 5.0 s | "…a city with no power lines." |

### 6.4 Hook pairs by topic (the question the cold open raises → where it's answered)
| Topic | The question the cold open raises | Where the answer lands | First shot |
|---|---|---|---|
| Heat pumps | "How can a machine move more heat than the energy it uses?" | The mechanism render at about 40–70 s; the engineer guest (gold) proves it at about 80 s | Cutaway render of the refrigerant loop, RF-2 |
| Black-hole time | "Why does nothing ever seem to fall in?" | The animation of the slowing clock, about 20–35 s | Animation, RF-2 |
| Tunnel boring machine | "How does a 1,000-tonne machine steer underground?" | The guest operator in the cab, about 50 s | Render of the cutter head turning, RF-2 |
| Index funds | "Why do most professional stock pickers lose to a fund that does nothing?" | The economist guest (gold) at about 45 s; the chart B-roll band at about 70 s | Host mid-gesture, RF-1 |
| Shipping containers | "How did one steel box cut the cost of trade by 90 %?" | Port B-roll and the historian guest, about 60 s | Crane B-roll, RF-2 |
| Inflation | "Where does the money actually go when prices rise?" | The host's whiteboard band, about 50 s | Host to camera, RF-1 |

### 6.5 The first line (instead of a headline)
You don't write the hook; you **choose** it from the master. The first sentence must be:
- **≤ 14 words, self-contained (SS-1), present tense or timeless;**
- one of three shapes: a **paradox** ("You can never see anything enter a black hole."), a **mechanism in action**
  ("Strong electric fields … slow down the antiprotons."), or a **problem** ("One thing that makes this research so tricky
  is…");
- spoken over a moving, full-bleed picture (SS-2).

Never open on a greeting, "In this video", "So,", "Today", "Welcome back", a sponsor line, or a "Did you know…" stacked on
nothing. Find every sentence in and around the span that passes (usually a handful), rank them by the stopper test, and
keep the best with two alternates.

### 6.6 Hook sound
The hook is the master's own mix from f0: no added hit, no riser, no bed (§11).

### 6.7 CTA
| Device | Spoken | On screen | Hold | Where |
|---|---|---|---|---|
| **none** (the default) | nothing | nothing: the reel ends on the implication sentence | — | — |
| **post_only** | nothing | nothing: the post text carries the pointer ("Full video on my channel: <title>") | — | the post |
| **cross_promo** | nothing (never add a voice line) | The end line "Full video: <exact long-form title>" (§5.4), cy 1250, over the last shot | 2.0–3.0 s, ending with the hard end | the last sentence |

The creator's choice is in their copy (`profile.cta.chosen`, default none). Never a subscribe button, the master's end
screen, a keyword card, a QR code or a "link in bio" sticker. If the master's own last line is a channel plug, the span
fails SS-5.

---

## §7 Structure and rhythm

### 7.1 Structure: the explainer arc
| Unit | What it does | Typical world | Evidence (v02, 153 s) |
|---|---|---|---|
| **HOOK** (problem or paradox) | The cold-open sentence and its stake; over fast, so the mechanism arrives while the question is fresh | Render or host | 0:00–0:17 host: "One thing that makes this research so tricky…" |
| **MECHANISM** | How it works, over renders and field footage: the long middle of the reel | Render, field | 0:18–0:58 BASE poster, p̄ render, CPT band, Earth field, lab |
| **PROOF** | The guest shows or says it works; the host reacts | Guest (gold), field | 1:08–1:47 letterbox trap, guest office, "And it works." |
| **IMPLICATION** | Why it matters, what follows; short, certain, ending on a period | Host, render, map | 2:06–2:32 "then why not ship it?" → map "research institutions." |

The master decides the order and the proportions; you make sure all four are inside the span (SS-3). A span that's all
mechanism and no proof is a lecture; a span that ends before the implication is a trailer.

### 7.2 Markers
None: no numerals, chapter chips or progress rails. The master's own baked labels ("ELENA", "16,200,000 km/h", "CERN")
are the only labels (v01 @ 0:33, 0:41; v02 @ 2:07).

### 7.3 The ritual: the world rotation
The style's recurring sequence isn't an item ritual but a **world rotation** inside each unit, which you protect when
choosing the span and placing splices:
1. **The claim in one world** (host to camera, or the narration over a render): one to three sentences, one shot or one
   master cut sequence.
2. **The mechanism in the render or field world:** the picture shows the thing named, held as long as the master holds it
   (P-RENDER-HOLD).
3. **The proof in the guest world** (gold captions), with the master's own host reaction or question in between
   (P-REACTION-KEEP, P-VOICE-OVER-PICTURE).
4. **The return** to the host or the render for the next claim.

A span that sits in one world without a new image for most of a minute goes flat; prefer one that rotates. A long
uncut animation is fine when the animation itself keeps developing (v03 holds one for 79.5 s and never feels static).

### 7.4 Open loops and re-hooks
- **The loops:** the question the cold open raises (§6.4) and the "but…" turn. Both are paid off inside the span (SS-3).
- **A re-hook** is any of:
  1. a **world change** on a sentence start (host → render, render → guest);
  2. a **turn sentence** ("But…", "Here's the thing", "The problem is…", "So why…");
  3. a **question** (host to guest, or rhetorical: "then why not ship it?", v02 @ 2:08);
  4. a **guest's first line** (the first gold caption);
  5. a **new striking image** (a render reveal, a map, a record number baked in).
- They come often enough that attention never sags, which in this calm style is what a re-hook is for: the next reason to
  stay arrives before the last one fades. Mark those beats `rehook: true`. For reference, v02's world changes fall at
  about 0:18, 0:32, 0:58, 1:12, 1:23, 1:40, 2:00 and 2:07, never more than 26 s apart (a description, not a target).

### 7.5 Rhythm by feel
- **The voice is the rhythm.** The picture holds as long as the master held it; the captions swap on every group of words.
  Still picture, moving words: that contrast is the pulse. Never add a cut, a zoom or an event to make it "move".
- **Pauses are breaths.** The master's pauses up to 2.0 s stay whole, the caption band blank, the picture still moving
  (P-PAUSE-BREATH). They're where the viewer thinks. A pause over 2.0 s with no picture change comes down to 1.2 s at the
  cut.
- **Flat-calm, with one lift:** the proof's "it works" moment (v02 @ 1:40 "And it works.") or the biggest render. Then the
  end is quiet and certain: the implication, then the hard end.
- **The speech stays as recorded** (about 2.4 words a second): never speed up the master.
- **Humour only when the master has it** (a guest's laugh, v02 @ 1:30), kept where it was and never cut to.
- For reference, measured on the three reels at full frame rate (a description, not a target): median shot 2.5 / 2.8 /
  1.9 s (v03 outside its 79.5 s uncut animation); p90 11.9 / 8.8 / 5.8 s; longest shot 17.1 / 17.8 / 79.5 s; on average
  one master cut every 4.5–9 s; a new caption chunk every 0.4–1.0 s. The cut rhythm is the master's: you neither add nor
  remove cuts to reach a number.

---

## §8 Visual system: B-roll and patterns

### 8.1 The role of graphics
`graphics: passthrough`. About 90 % of what the viewer sees is the master's own picture; the re-cut adds only captions,
the reframe and, rarely, a drawn element. The drawn layer is four overlay patterns (P-OBJECT-TITLE, P-CROSS-PROMO,
P-SUBSTITUTE-CARD, P-REDACT), and most reels use none or one. The craft lives in the other nineteen: the **cut and
reframe grammar**. "Numbers become pictures" doesn't apply here: numbers stay in the captions as spoken, and only the
master's baked numbers are pictures. No comedy layer (comedy is off; laughs come from the master only).

### 8.2 Families
| ID | Family | Source | What the creator supplies |
|---|---|---|---|
| **B-1** | Host footage (to camera, on location) | baked in the master | the master |
| **B-2** | Guest and interview footage | baked in the master | the master and the guests' names |
| **B-3** | Renders, animation, simulation, CAD | baked in the master | the master |
| **B-4** | Field B-roll (labs, places, objects, details) | baked in the master | the master |
| **B-5** | Baked UI, diagrams, maps, on-screen labels | baked in the master | the master |
| **B-6** | Editor overlays (object title, end line, redaction) | engine | the long-form's title (for the end line) |
| **B-7** | Third-party spans inside the master | baked in the master, kept as published (§12.6); replaced by **B-8** only when the creator rules one out | the master (and any span they don't want reused) |
| **B-8** | Created substitute card (quote, headline, diagram) | engine (created) | nothing |

### 8.3 Pattern specs
Frames at 30 fps.

**Overlay patterns (engine-drawn, z5 / z3):**
| ID | Name | On screen | Motion recipe | When | Needs |
|---|---|---|---|---|---|
| **P-OBJECT-TITLE** | Italic object title | 1–3 words, EB Garamond Italic 500, 68 px, white, centred at cy 1230 (full-bleed) / 590 (band) | In over 8 f (opacity 0 → 1, y +12 → 0, expo-out), starting 2 f before the name is spoken; hold 1.5–4.0 s; out over 6 f, before the next master cut | A line names a specific new object, device or place for the first time, the master shows it, and the master doesn't show its name | nothing |
| **P-CROSS-PROMO** | End line | "Full video: <title>" in serif 44 px, cy 1250 | In over 8 f (opacity); no exit (hard end) | The creator chose the cross-promo end; over the last sentence | the exact title |
| **P-SUBSTITUTE-CARD** | Created card | `L-void` black; the kicker (the source the script names, 26 px caps, `muted`) at y 600; the verbatim quote or headline, 52 px serif, ≤ 3 lines, centred in y 660–1080; captions keep running at 1380 | Hard cut in on a sentence start; the body fades in over 6 f; hard cut out on the next sentence start | A third-party span the creator ruled out that can't be trimmed (§12.6) | the script's exact words |
| **P-REDACT** | Identifier blur | Gaussian blur 24 px over the rect + 12 px | Keyframes every 6 f following the rect; on for the identifier's whole visible time | An email, phone number, address, ID or key is legible in the master | keyframes |

**Cut and reframe patterns (the craft; nothing drawn):**
| ID | Name | What happens | Recipe (frames, rules) | When | Evidence |
|---|---|---|---|---|---|
| **P-COLD-OPEN** | Cold open | The reel's in-point | In-point 1–3 f before the first word's onset; the first shot RF-1 or RF-2; no fade-in, no black frame | Always, at f0 | v01, v02, v03 @ 0:00 |
| **P-HOST-FOLLOW** | Host follow | RF-1 on the host | Face 17 % of H, eyes at 36 % of the crop, dead zone 12 %, 0.6 s spring; ≤ 2.0× upscale | The host to camera or on location | v02 @ 0:00–0:17, 1:40–2:06 |
| **P-GUEST-FOLLOW** | Guest follow | RF-1 on a guest | Same as the host, on the guest's own single angle | Guest interview singles, video-call guests | v01 @ 0:44–0:57 |
| **P-VOICE-OVER-PICTURE** | Voice over another picture | The master shows the host's reaction or B-roll while a guest talks | Keep the master's picture and its fit; the captions stay gold for the guest's words (R-3) | A guest's voice continues over the host or B-roll | v02 @ 1:29–1:30, 2:10–2:15, 2:21; v01 @ 0:54–0:57 |
| **P-CENTRE-CROP** | Centre window | RF-2 on a faceless shot | A static, centred, full-height 9:16 window; the master's own camera motion plays inside; check the frame after the render | Renders and B-roll whose subject sits in x 34–66 % | v01 @ 0:00–0:11.5 |
| **P-BAND** | Band | RF-3 | A centred 1080 × 608 band at y 656–1264 over its blurred, undimmed copy (black on black grounds); hard cut in and out; the caption at 1380 under it | Wide diagrams, UI, baked text, two-shots, routes | v02 @ 0:58–1:11; v03 @ 1:09–1:29 |
| **P-TWO-SHOT** | Two-shot | RF-4 | The two-shot angle; the band when both faces don't fit 9:16 | Host and guest in one frame | — |
| **P-WALK-AND-TALK** | Location follow | RF-1 on handheld field footage | The same follow; if the face is under 6 % of H for more than half the shot, band it instead | The host asks on location, a guest walks and talks | v01 @ 1:05–1:24, v02 @ 1:15–1:22 |
| **P-DETAIL-INSERT** | Detail insert | RF-2 on a macro detail (a part, a label) under narration | The centre window; keep its master length (often 1–3 s) | A detail being named ("this valve") | v01 @ 0:54–1:04 |
| **P-RENDER-HOLD** | Long render hold | A render shot held as long as the master holds it | No cut, no crop change; the captions carry the pace; however long the master held it, it's the master's choice and stays | A mechanism explained over a render | v01 @ 0:00–0:11.5, v03 @ 0:05–1:29 |
| **P-BAKED-TEXT-SAFE** | Baked text kept whole | A shot with a baked label, number or small print | The crop holds the whole text with a 24 px margin, or the shot is banded | Any shot whose baked text the line needs | v01 @ 0:33 "ELENA", 0:41 "16,200,000 km/h"; v03 @ 1:37 the vertical small print at the left edge |
| **P-MAP-FRAME** | Map | A baked map | RF-2 centred on the named place when the line names one place; RF-3 when routes or several places matter | Where, a route, a global spread | v02 @ 2:07–2:32 |
| **P-HUD-BAND** | UI / HUD / simulation | Screen-like content | Always RF-3, the band (blur-fill) | A screen, UI, simulation or chart with text | v03 @ 1:09–1:29, 1:32–1:34, 1:45–1:46 |
| **P-SPLICE** | Splice | A join between two master spans | A hard cut at a sentence boundary, 0.04–0.10 s before the next sentence's first word; the join carries the engine's 8 ms equal-power audio crossfade | Skipping a digression, a sponsor, a repeated point | v03 @ 1:29.87 |
| **P-DIP-SPLICE** | Cross-shoot splice (the id is kept; there's no dip) | A splice across shoots | A hard cut, 0 f, on a sentence boundary; the next caption chunk appears on the same frame | Different wardrobe, room or time of day | v03 @ 1:29 → 1:30, the host from another shoot |
| **P-PAUSE-BREATH** | Pause breath | The master's pause kept | The caption band blank; a pause up to 2.0 s kept whole; longer, it comes down to 1.2 s (only when the picture doesn't change) | Every pause in the master | v03 @ 0:49–0:51, 1:06–1:08 |
| **P-REACTION-KEEP** | Reaction kept | The master's own listener reaction or laugh | Keep it exactly where the master put it; never add, extend or move one | A laugh or an aside in the master | v02 @ 1:15–1:22, 2:10–2:15 |
| **P-HOST-RETURN** | Host return | The implication returns to the host (or a final render) | Prefer a span whose last 8–20 s is the host to camera or the payoff render | The why-it-matters close | v02 @ 1:51–2:06; v03 @ 1:44 |
| **P-LAST-LINE-END** | Last line end | The reel ends | Out-point 3–5 f after the last word ends, the last caption still on; no end screen, no black tail. The variant T-END-FADE, when the last shot is a render whose narration has already ended: the picture fades to black over 5 f, the caption already gone (v03 @ 1:49.73) | Every reel; the fade only where the master's own ending is a render after the last word | v01 @ 1:54.9, v02 @ 2:33.3 |

### 8.4 Line → pattern lookup
Vocabulary, not a decision table: it tells you what this style reaches for. Ask what the moment needs, then use it.

| Line type | Primary | Alternates | For example |
|---|---|---|---|
| Opening paradox / problem | P-COLD-OPEN + P-CENTRE-CROP or P-HOST-FOLLOW | P-RENDER-HOLD | "A heat pump moves more heat than it uses." |
| Mechanism over a render | P-RENDER-HOLD (P-CENTRE-CROP) | P-BAND if the baked labels are wide | the refrigerant loop cutaway |
| Names a new object for the first time | P-OBJECT-TITLE (only if it's unnamed on screen) | none | "the compressor" over its render |
| A number with a unit | the caption only (as spoken); P-BAKED-TEXT-SAFE when the number is baked | — | "a 2 % fee" |
| A guest explains | P-GUEST-FOLLOW | P-TWO-SHOT | the engineer in the plant room |
| A guest's voice continues over B-roll or the host | P-VOICE-OVER-PICTURE | — | the economist over the trading-floor B-roll |
| The host asks on location | P-WALK-AND-TALK | P-BAND | "So where does the heat come from?" |
| Where / a route / a global spread | P-MAP-FRAME | P-BAND | the container routes map |
| A screen, UI, simulation, chart with text | P-HUD-BAND | — | the fund-performance chart |
| A detail being named ("this valve", "the fine print") | P-DETAIL-INSERT | P-CENTRE-CROP | the expansion valve macro |
| A laugh or an aside in the master | P-REACTION-KEEP | — | the guest laughs at the host's guess |
| A digression, sponsor or repeat in the way | P-SPLICE (cut it out) | P-DIP-SPLICE across shoots | the sponsor read |
| Why it matters | P-HOST-RETURN + P-LAST-LINE-END | the final render | "…so the cheapest fund is usually the winning one." |
| A third-party clip or quote inside the master | keep it as the master has it | trim around it, or P-SUBSTITUTE-CARD, when the creator rules it out | a TV interview with a CEO |
| A legible personal identifier | P-REDACT | — | a lab email on a whiteboard |

### 8.5 Data and truth
- No figures, counters or charts are built. Numbers appear only as spoken (the captions) or as baked in the master.
- A baked number stays whole on screen (P-BAKED-TEXT-SAFE), so it's never misread ("16,200,000" cut to "6,200,00").
- Never splice two sentences so that a number or a quote attaches to a different subject or speaker.

### 8.6 Assets
- The master is the only footage. Never pull shots from other videos, stock, or other parts of the master to fill a gap; a
  splice brings whole sentences with their own pictures.
- The only created visuals are P-SUBSTITUTE-CARD and P-REDACT, with no label and no credit line.
- No logos are drawn; the master's own baked logos stay as they are.
- Third-party spans: kept as the master has them, the real thing already in hand (§12.6).
- When nothing needs drawing, nothing is drawn: an empty scenes file is a complete plan in this style.

---

## §9 Transition system

### 9.1 Library
| ID | Transition | Frames | Recipe |
|---|---|---|---|
| **T-CUT** | Hard cut | 0 | The master's cuts and every P-SPLICE join, including fit switches and splices across shoots |
| **T-DISSOLVE** | Cross-dissolve | 10 | Linear opacity cross-fade over 10 f; the captions hide for those 10 f only if a chunk would straddle it |
| **T-END-FADE** | Fade to black at the end | 5 | Linear opacity 1 → 0 to `#000000` over the last 5 f, after the last word, no caption (v03 @ 1:49.73–1:49.94). Built in: write `"end_fade": 5` on the timeline (core fades the whole frame to `#000000`); no scene |
| **T-END** | Hard end | 0 | Out-point 3–5 f after the last word |

Every editor transition measured in the reference reels is a hard cut (0 f), including the splice into the host from
another shoot and every band ↔ full switch (completeness audit). A dip to black was never seen and isn't part of the
style. The master's own dissolves (inside v03's HUD sequence, 1:10–1:29) stay exactly as the master made them.

### 9.2 Grammar
| Boundary | Use | Never |
|---|---|---|
| Frame 0 | P-COLD-OPEN (no transition) | A fade-in, a black frame, a logo sting |
| Inside the master's sequence | The master's own cut (T-CUT) or its own dissolve, kept as is | An added transition |
| A splice, same shoot | T-CUT on a sentence boundary | A cut mid-sentence |
| A splice, different shoot, wardrobe or room | T-CUT (v03 @ 1:29.87) | A dip, a whip, a zoom-through |
| Two renders of the same object joined at a splice | T-DISSOLVE | — |
| Full ↔ band | T-CUT (G-1), on the master's cut | A morph |
| The last word | T-END (or T-END-FADE, §8.3) | A black tail, an end screen |

### 9.3 Shot grammar
| ID | Rule |
|---|---|
| **R-1** | **The master's cuts are the reel's cuts.** No new cut inside a master shot, except a P-SPLICE join at a sentence boundary. |
| **R-2** | **One fit per master shot.** The reframe class (and its angle) changes only at master cuts or splices, ±0 f. No re-crop jumps, no punch-ins. |
| **R-3** | **The colour follows the voice, not the face.** A guest heard over the host's reaction or over B-roll stays gold; the host heard over a guest's shot stays white. |
| **R-4** | **Never cut on a speaker handover the master didn't cut on.** Handovers are shown by colour alone. |
| **R-5** | **Reactions are the master's.** Keep the master's listener cutaways; never insert, extend or move one. |
| **R-6** | **Camera motion is the master's.** Keep its dollies, orbits and handheld; add none (`zoom_policy: source_only`). |
| **R-7** | **Follow calmly.** RF-1 uses the compositor's dead-zone operator (dead zone 12 % of the crop, critically damped, 0.6 s); never hand-keyframe a crop faster than that. Measured, the real crops are near-static per shot (background drift ≤ 2 % a frame, all from gestures; v02 0:00–0:17.7), so prefer a wide dead zone over a centred face. |
| **R-8** | **No flicker.** A master shot shorter than 0.8 s takes the fit of the longer neighbour it belongs to; a flash frame never switches full → band → full. |
| **R-9** | **No ping-pong.** When the master alternates faster than the eye can resettle between full and band (a diagram, the host, the diagram again within a few seconds), band all of them. |
| **R-10** | **Splices are rare and clean.** Each sits on a sentence boundary and passes "would a viewer notice?": same topic, same tense, no dangling reference. A span that needs more than a few joins to hold together isn't one argument; choose another. |

### 9.4 How the moves breathe
The cut is the master's, and the viewer never notices it, because the meaning changes, not the editing. That's the
standard for everything you add: a splice nobody can find, a fit switch that feels like the master always meant it, a
band that looks like the diagram was made for it. A dissolve is the one soft move, kept for two renders of the same object
meeting at a splice; it's so rare that a reel with one is unusual. If a move draws attention to itself, it's wrong.

---

## §10 Motion tokens, camera, layers, finishing

### 10.1 Motion tokens
| Token | Value |
|---|---|
| Caption lead | 1 f before the first word |
| Caption swap | hard, 0 f (E6) |
| Caption tail into a pause | a 0.3 s hold, then the engine's exit |
| Overlay lead | 2 f before the trigger word |
| Object title in / out | 8 f (opacity + y +12 → 0, expo-out `cubic-bezier(0.22, 1, 0.36, 1)`) / 6 f (`cubic-bezier(0.64, 0, 0.78, 0)`) |
| End line in | 8 f, opacity |
| Card body in | 6 f, opacity |
| T-DISSOLVE | 10 f, linear |
| T-END-FADE | 5 f, linear |
| Holds | titles ≥ 1.5 s and ≥ 10 f after they're fully on; text ≥ 0.25 s a word |

### 10.2 Footage camera (`zoom_policy: source_only`)
No zoom presets exist in this style, and none is added: all motion inside the frame is the master's. The only crop
motion is the RF-1 dead-zone follow. The completeness audit measured it: in 17.7 s of host to camera (v02 0:00–0:17.7)
and 6 s at v02 1:40–1:46, the background never jumps more than 1.9 % in scale or 1.7 % in position between frames (the
host's gestures); no punch, push, shake or re-crop jump. No canvas camera either.

**Master-made motion stays the master's:** handheld location pans (v01 1:19–1:25 trip the scene detector every 0.17 s or
so but are one shot), a hard cut into a defocused graphic that racks to sharp over 8 f (v02 @ 0:20.83, the p̄ bubble),
in-render dissolves (v03 1:10–1:29). Keep them exactly; never imitate them on other shots.

### 10.3 Layer order (back to front)
1. The world, W-void (`#000000`).
2. Stage footage: the composed master (`work/multicam/footage.mp4`), with the bands and blur-fill composed in.
3. P-REDACT blurs (z3).
4. P-SUBSTITUTE-CARD text (z5, over `L-void`).
5. P-OBJECT-TITLE / P-CROSS-PROMO (z5).
6. Captions (z7, `__subtitles`).

Nothing sits above the captions.

### 10.4 Finishing
None: no grain, no vignette, no glow, no sharpening, no grade. Output 1080 × 1920, 30 fps.

---

## §11 Sound
| Line | Decision |
|---|---|
| **Cue moments** | **None** (`cue_moments: []`): the master's mix already carries its music and effects. A creator's copy may turn on a soft cue on a splice (`transitions`), never more |
| **Meme cues** | Off (comedy off) |
| **Music bed** | **Off:** never a bed over the master |
| **Ducking** | None needed: the master's mix is the voice track, kept whole |
| **Loudness** | −14 LUFS integrated, true peak ≤ −1.5 dBTP; hard end ≤ 6 f after the last word. Splices use the engine's 8 ms equal-power crossfade; no audio offsets |

The master's mix is the sound design. Laughs, music swells and stings stay where the master put them; a splice that cuts
a music phrase mid-bar is a reason to move the splice to the next sentence boundary.

---

## §12 Footage handling

### 12.1 The master
| Setup | What the style assumes |
|---|---|
| **M: the master** | One finished long-form video the creator owns: 16:9, 2160p preferred (1080p accepted), any frame rate (conformed to 30 fps), one stereo mix with the voice and music, the creator's graphics and renders baked in. The host is typically framed chest-up, the head top in the top 10–15 % of the 16:9 frame, the face roughly centred (so RF-1 crops cleanly) |

Nothing is shot. What helps most: renders and B-roll that keep their subject in the centre third (they reframe full-bleed
instead of banding).

### 12.2 Shots and fallbacks
| ID | Item | Spec | Must / optional |
|---|---|---|---|
| **SH-1** | The finished master | 16:9, ≥ 1080p, the published cut | **must** |
| **SH-2** | A 4K export of the master | 2160p, the same cut, so 9:16 crops never upsample | optional |
| **SH-3** | The cast | the host's name; every guest's name in the chosen part | **must** |
| **SH-4** | The long-form's exact title and platform | for the end line | optional (needed for cross_promo) |

| ID | For | What happens instead | Cost | Result |
|---|---|---|---|---|
| **FB-1** | SH-1 | nothing: without a finished master there is nothing to re-cut | the style can't run | no fallback |
| **FB-2** | SH-2 | crop the 1080p master, upsampling up to 1.78× (the compositor caps at 2.0×); say so with the cut | softer faces and renders; small baked text softer | degraded |
| **FB-3** | SH-3 | diarise; the most-talking voice is the host, every other voice a guest; confirm with the creator | a co-host would be gold | holds |
| **FB-4** | SH-4 | the end falls back to post_only | no on-screen pointer to the full video | holds |

### 12.3 Reading the master
- **Resolution:** 2160p means the crops never upsample; 1080p means FB-2. A full-height 9:16 window of a 16:9 frame is
  0.316 of its width: 2160p gives 1215 × 2160 (downsampled, sharp), 1080p gives 607 × 1080 (upsampled 1.78×). Never crop
  tighter than the full-height window on a 1080p master: it would pass 2.0×.
- **Frame rate:** 23.976, 25 and 60 fps masters are conformed to 30 fps CFR.
- **The master cut list:** the source's scene changes (scene detection) are the master's cuts, listed in master time as
  M1, M2, … (in your notes, `M1: t0–t1`). It's the only place a reel cut may come from (R-1); everything else is a
  splice.
- **Chapters:** if the long-form has chapters (its own sections, or the timestamps the creator published), they're your
  first map. A self-contained argument usually lives inside one chapter, sometimes across the end of one and the start
  of the next, almost never across three.
- **The voices:** transcribe the whole master with a glossary of the creator's technical terms and names, then diarise
  (`veos speakers --mode diarize --num <people who speak>`) and name them (`veos speakers name S1=<host>:host
  S2=<guest>:guest …`). The host is whoever narrates; an off-screen narrator who is the host is `host`; every other voice
  is `guest`, and every guest is gold. At least 95 % of the words must carry a label; overlapping speech keeps the
  dominant talker. With an unknown cast, use FB-3.
- **The angles:** `veos angles` lists the faces and tracks (host single, guest singles, a two-shot, the wide); use the ids
  it lists, never invent one. RF-1 → the speaker's or subject's single; RF-2 → the host single (no face in the shot = a
  centred window); RF-3 → the wide; RF-4 → the two-shot.
- **The shots are yours, by hand:** write one `timeline.shots[]` entry per master shot inside the cut (§13), then
  `veos shots render --fallback blurfill`, and read `compose.json` (every shot's fit, crop and `max_upscale`, never above
  2.0). Never run `veos shots plan` here: its conversation grammar (re-crops every few seconds, a cut on every handover,
  stack openers) breaks R-1, R-2 and R-4. For the same reason the engine's handover-cut check is off in this style's
  tokens: speaker correctness is the caption colour, checked by ear on every handover shot.
- **Vertical masters** (the creator exported 9:16): no reframing; the stage is `L-master` over the conformed source, and
  any 16:9 clips the creator supplies separately use `L-band-black` / `L-band-blur` with `src` = that clip.

### 12.4 Finding the argument
This is the craft of the style. A long-form video holds several shorts; most of its minutes hold none. You're looking for
the one span that plays as a complete, gripping argument to someone who has never seen the long-form.

**Where to look.** Start from the chapters and the turn sentences. `veos shots mine --min 110 --max 150` writes
`plan/clip_candidates.json`: spans bounded by speaker turns, scored for a question start, a complete answer and two or
more speakers. On a single-voice master (pure narration) it may return nothing; then build the candidates yourself from
the sentence boundaries in the words file: every start that follows a pause of 0.35 s or more, or a master cut.

**The eight tests.** Re-score every candidate (and its neighbours one sentence either side) with all eight; a span must
pass every one. Rank the passes by SS-2 (the strength of the first image), then by how many worlds it visits.

| ID | Test | Passes when |
|---|---|---|
| SS-1 | Cold-open line | The first sentence is a complete claim, paradox or problem of ≤ 14 words that needs no earlier context: it doesn't start with *so, and, but, this, that, it, these, which, as I said, remember, now*; no greeting, no "in this video" |
| SS-2 | Strong first image | The picture at the in-point is moving and visual (a render in motion, the host mid-gesture, a guest with the object) and is a full-bleed reframe (RF-1 / RF-2), never a band, black, a title card or a sponsor shot |
| SS-3 | One argument | Problem → mechanism → proof → implication are all inside the span. Nothing refers out of it: *as we saw, earlier, later, in the next section, I'll explain, link below, today's sponsor* |
| SS-4 | It never sags | A world change, a turn sentence (*But…, Here's…, So why…, The problem is…*), a question, a guest's first line or a new striking image keeps arriving all the way through (§7.4); no long stretch of one world with nothing new to look at |
| SS-5 | Implication ending | The last sentence states why it matters or what follows, as a statement ending in a period. Not a question the long-form answers later, not "but first", not a sponsor or channel plug |
| SS-6 | It survives vertical | The span is mostly full-bleed reframes: band shots only where a crop would break the picture, none at the opening, and no long run of them |
| SS-7 | Length | 110–150 s after the cut (a creator's copy on the standard length: 60–90 s) |
| SS-8 | Clean span | No sponsor read, ad, affiliate mention, mid-roll, merch plug or end screen inside it. A span that would need a paid-partnership disclosure fails |

**Cutting it.**
- One to four segments of the master, joined by splices only at sentence boundaries (P-SPLICE).
- **The in-point** 0.04–0.10 s before the first word, so the caption is on screen at f0. **The out-point** 0.10–0.18 s
  after the last word ends (≤ 6 f, D8).
- **Never tighten.** The master is already paced; its pauses up to 2.0 s are breaths (P-PAUSE-BREATH), so never apply
  the cut's automatic tightening or bring pauses down to the talking-head default. A pause over 2.0 s with no picture
  change comes out with a join that keeps 1.2 s of it.
- Splice out a digression, a sponsor read or a repeated point; never a sentence the argument needs. After every splice,
  read the joined sentences aloud: same topic, same tense, nothing dangling.
- When the long-form simply doesn't hold a 110 s argument, say so and offer the strongest shorter one, rather than
  padding a weak span.

### 12.5 Props, matte, reaction bank
None: the master has them all. No cut-out.

### 12.6 Third-party spans: the real thing is already in the master
The master is the creator's own work. Third-party material **inside** it (a news clip, another creator's footage, a photo
with someone else's name on it, a TV interview) is the real thing, already published in the long-form, so the short uses
it as the master has it.
1. **Note the spans** in the chosen part where the picture is visibly someone else's (a watermark, a news ticker, another
   channel's name).
2. **Keep each exactly as the master has it,** never altered; its baked text stays whole (P-BAKED-TEXT-SAFE). Name them
   in a line when you show the storyboard, so the creator can say if one shouldn't be in a short.
3. **A span the creator rules out** (in their brief, their learned rules, or at the storyboard): first move the in- or
   out-point, or splice around it (the tests must still pass). If the sentence is essential, cover the span with
   **P-SUBSTITUTE-CARD** (a quote card, headline card or diagram) showing only what the script says; the captions keep
   running.

No label and no credit line on a created card.

### 12.7 Frame rate and audio
30 fps CFR output, 1080 × 1920, BT.709. The master's audio is the voice track (`veos voice` from the cut map, `veos mix`
to −14 LUFS).

---

## §13 What your plan should settle

Your `ideas.md` is a page or two, for you. In this style it has decided, before any code:
1. **The span:** its segments in master time, every splice and why, its runtime, how it passes SS-1…SS-8, and the two
   alternates it beat.
2. **The cold open:** the archetype and variant (HA-14a/b/c, HA-10, HA-15), the in-point, the first line, the first
   shot and its RF class, the first 3 s of captions, and two alternate in-points.
3. **The post title:** 8–10 candidates, the pick, two alternates.
4. **The cast and the colours:** who is host, who is guest, every shot where the picture and the voice differ (the
   P-VOICE-OVER-PICTURE beats) with the colour the voice gets.
5. **Every master shot's reframe:** its RF class, angle and fit, as `timeline.shots`, with every RF-2 middle frame
   checked and every band and why it's a band.
6. **The re-hooks and the world rotation:** the beats marked `rehook: true`, and the one lift.
7. **The overlays** (usually none): object titles, the end line, redactions.
8. **The inserts:** every third-party span, kept (named for the storyboard), trimmed or carded; the fallbacks used (FB-2,
   FB-3, FB-4) and their cost.
9. **The end:** T-END or T-END-FADE, the last word, the out-point.
10. **The moments you'll look at hardest on the storyboard:** f0 (the moving picture and the first chunk); a host RF-1
    frame with a white caption (head top, room above it, the caption on the chest); a guest frame or a
    voice-over-picture frame with a gold caption; one band frame (the band whole, the caption under it); every RF-2
    middle frame; the last frame (with the end line if used).

**Beat fields this style adds:** `section` (HOOK | MECHANISM | PROOF | IMPLICATION), `trigger {word, at}`, `tone`,
`speaker` (host | guest | narrator), `master {t0, t1, shot: "M17"}`, `rf` (RF-1…RF-4), `angle` (from angles.json),
`cut_reason` (`open` the first shot, `recrop` a master cut, `splice` a join; in `timeline.shots` write `recrop` for master
cuts and splices, since the engine knows only its own reasons), `rehook: true` on re-hook beats, `caption {profile:
"CS-1", overrides: []}` (overrides only for a spelling or a speaker fix: `{i, speaker}`, `{i, text}`),
`exception: "E6"` (the captions inherit it), `layers` (usually `[]`), `sfx` (normally `[]`).

**`timeline.shots[]`** (one per master shot inside the cut, contiguous, frame-aligned, in edit time):
```json
[
  {"t0": 0.0,   "t1": 11.47, "layout": "full", "angle": "A:S1", "subject": null, "step": 1.0, "speaker": "S1", "cut_reason": "open"},
  {"t0": 11.47, "t1": 28.6,  "layout": "full", "angle": "A:S1", "subject": "S1", "step": 1.0, "speaker": "S1", "cut_reason": "recrop"},
  {"t0": 28.6,  "t1": 44.6,  "layout": "full", "angle": "A:W",  "subject": null, "step": 1.0, "speaker": "S1", "cut_reason": "recrop"}
]
```
(The first row: an RF-2 render on the host single angle with no face in the shot; the second: RF-1 on the host; the
third: an RF-3 band.) `step` is always 1.0: no jump re-crops.

The reel header:
```yaml
reel:
  format: F-A
  theme: null
  hook_archetype: HA-14          # HA-14 | HA-10 | HA-15
  hook_variant: HA-14a           # a image-first | b host-first | c guest-first
  structure: explainer
  master: {file: "<master file>", resolution: 2160p, fps_in: 23.976, duration_s: 1260.4}
  span: {segments: [[612.40, 701.85], [745.10, 790.32]], splices: 1, runtime_s: 134.7}
  cast: {S1: {name: "<host>", role: host}, S2: {name: "<guest>", role: guest}}
  bands: [[31.0, 38.5], [101.0, 109.0]]
  cta: none                      # none | post_only | cross_promo
  rehooks: [17.8, 31.9, 52.4, 71.0, 89.6, 106.2, 121.5]
  end: hard                      # hard | fade (T-END-FADE)
```

A cold-open proposal, for the shape:
```yaml
- name: "Image-first: the loop that moves heat"
  archetype: HA-14a
  in_point: {master_t: 612.36, first_word_at: 612.42}
  first_line: "A heat pump moves more heat than it uses."
  first_shot: {mcl: M88, rf: RF-2, what: "cutaway render of the refrigerant loop, camera orbiting"}
  captions_0_3s: ["A heat pump", "moves more heat", "than it uses."]
  storyboard: "f0 render orbiting, chunk 1 on | 0.8 chunk 2 | 1.9 chunk 3 + period | 4.2 'Here's how.' | 9.6 cut to host"
  post_title: "Why a heat pump beats a heater"
  sound: "the master's mix"
  stopper: {mute: pass, motion_f0: pass, payoff_by_s: 0.0}
```

---

## §14 Worked examples

Times are planning estimates; the real ones come from the words file.

### 14.1 Science channel: host, renders and a guest, "Why a heat pump beats a heater" (HA-14a, 132 s, 1 splice)
**Master:** a 21-minute 4K video on heat pumps: the host in his studio, CAD cutaway renders of the refrigerant loop, a
field visit with an installer (guest), an animated house-heat map, a sponsor read at 9:40.
**Span:** master 10:12.36–11:41.85 + 12:25.10–13:10.32 (the splice skips a 43 s history tangent; SS-8: the sponsor at
9:40 is outside).

**Hook table**
| t | Picture | Caption | RF | Notes |
|---|---|---|---|---|
| f0 | Cutaway render of the refrigerant loop, camera orbiting | "A heat pump" (white) | RF-2 (the loop centred) | In-point 2 f before "A" |
| 0.7 | same | "moves more heat" | — | — |
| 1.5 | same; the coil glows (baked) | "than it uses." | — | The sentence complete at 2.1 s |
| 2.6–4.2 | same | "It doesn't make / heat. / It moves it." | — | The stake line |
| 9.6 | **cut** (the master's) to the host to camera, mid-gesture | "Here's the trick." | RF-1 host | Re-hook 1 (world change + turn) |

**Section plan**
| Section | Spoken (gist) | Pictures (the master) | Patterns | Re-hooks |
|---|---|---|---|---|
| HOOK 0–9.6 | the paradox | the loop render's orbit | P-COLD-OPEN, P-RENDER-HOLD, P-CENTRE-CROP | — |
| MECHANISM 9.6–48 | "the refrigerant boils at minus 30… the compressor squeezes it…" | the host (RF-1); the compressor's render (RF-2); P-OBJECT-TITLE "Compressor" at 21.4 (the render shows it unnamed); a pressure-temperature diagram with baked labels (RF-3 band 31.0–38.5) | P-HOST-FOLLOW, P-CENTRE-CROP, P-OBJECT-TITLE, P-HUD-BAND | 9.6, 31.0 (new image) |
| PROOF 48–101 | the installer: "On a cold day this one still gives you three units of heat for one of power" | the installer in the plant room (RF-1 guest, **gold**); the installer's voice over the outdoor-unit B-roll (P-VOICE-OVER-PICTURE, gold); the host's question on location (white, P-WALK-AND-TALK); the splice at 77.2 (same shoot → T-CUT) | P-GUEST-FOLLOW, P-VOICE-OVER-PICTURE, P-WALK-AND-TALK, P-SPLICE | 48.0 (the guest's first line), 70.5 ("But what about…"), 92.3 (question) |
| IMPLICATION 101–132 | "So the cheapest heat in your house might come from outside it." | the animated house-heat map (RF-3 band 101–109, 8 s), the host to camera (RF-1) | P-MAP-FRAME, P-HOST-RETURN, P-LAST-LINE-END | 109.2 (world change + "So…") |

Bands: 7.5 + 8.0 = 15.5 s of 132 s; everything else full-bleed. One object title. CTA: none. Transition map: T-CUT
splice @ 77.2; T-END @ 132.0.

### 14.2 Money documentary: host, a video-call guest and B-roll, "Why most stock pickers lose" (HA-14b, 141 s, 2 splices)
**Master:** a 26-minute 1080p documentary: the host in the studio, an economist on a video call, trading-floor B-roll,
animated fee charts, a TV news clip (third party) at 17:02.
**Span:** 14:05.20–15:58.90 + 16:20.00–16:41.10 + 17:30.40–17:36.80 (the splices skip a repeat and the news clip). FB-2
used (1080p: the crops upsample 1.78×; said with the cut).

**Hook table**
| t | Picture | Caption | RF |
|---|---|---|---|
| f0 | The host mid-gesture, both hands open | "Every year," (white) | RF-1 host |
| 0.6 | same | "most professional / fund managers" | — |
| 1.9 | same | "lose to a fund / that does nothing." | — (complete at 3.1 s) |
| 3.4–12 | the same shot (the master holds it) | "And the reason / isn't that they're / bad at their jobs." | — |
| 12.8 | cut to the trading-floor B-roll | "It's arithmetic." | RF-2 |

**Section plan**
| Section | Pictures | Patterns | Re-hooks |
|---|---|---|---|
| HOOK 0–12.8 | the host, RF-1 | P-COLD-OPEN, P-HOST-FOLLOW | — |
| MECHANISM 12.8–55 | B-roll (RF-2); the animated fee chart with baked percentages (RF-3 band 24–35: "2 %" and "0.05 %" must stay whole, P-BAKED-TEXT-SAFE); the host (RF-1) | P-CENTRE-CROP, P-BAND, P-BAKED-TEXT-SAFE | 12.8, 24.0, 44.1 ("But here's…") |
| PROOF 55–110 | the economist on the video call (RF-1 guest, gold); the economist's voice over the host nodding (gold, P-VOICE-OVER-PICTURE); P-OBJECT-TITLE "Index fund" at 61.2 over the fund-document B-roll; the splice @ 98.4 (a repeat skipped, T-CUT) | P-GUEST-FOLLOW, P-VOICE-OVER-PICTURE, P-OBJECT-TITLE, P-SPLICE | 55.0, 79.6, 98.4 |
| IMPLICATION 110–141 | the host to camera; the splice @ 134.3 across the news clip (the creator's brief rules out the TV clip → trimmed out, not carded); the last line on the host | P-SPLICE, P-HOST-RETURN, P-LAST-LINE-END, P-CROSS-PROMO (the creator chose the cross-promo end: "Full video: Why Stock Pickers Lose", 138.4–141.0) | 110.3, 134.3 |

The TV news clip: spliced out (the creator ruled it out for shorts), so nothing third-party remains to name.

### 14.3 Animation-only master: "What you'd see falling into a black hole" (HA-14a with the HA-15 check, 118 s, 1 cross-shoot splice)
**Master:** a 14-minute painted-animation video with the host's narration and two host-to-camera shots recorded months
later.
**Span:** 2:10.04–3:58.30 + 12:41.20–12:50.90 (the second segment is the host's outro from another shoot → a hard cut,
P-DIP-SPLICE).

| t | Picture | Caption | RF / pattern |
|---|---|---|---|
| f0 | A painted spaceship drifting, the black hole's limb entering | "You can" | RF-2, P-COLD-OPEN |
| 0.3–1.9 | the ship nears the hole | "never see / anything" | — |
| 2.0–3.0 | baked: the ship is stretched and crushed; a red prohibition ring slams in at 3.0 | "enter / a black hole." | P-RENDER-HOLD (no cut for 85 s) |
| 5–85 | the long animation; a baked zoom bubble on the pilot; blank pauses at 49–51 and 66–68 | narration (white) | P-RENDER-HOLD, P-PAUSE-BREATH; re-hooks at 23 (turn), 44 (new image), 66 (question), 79 ("But in…") |
| 69–89 | the "DE-REDSHIFTER" HUD | narration | **P-HUD-BAND** (RF-3, 20 s = 17 %) |
| 108.3 | **hard cut** (0 f) into the host (a different shoot, at night) | "This is just / strange." | P-DIP-SPLICE, P-HOST-RETURN |
| 118.0 | the last word "travel." + 4 f | — | P-LAST-LINE-END |

HA-15 isn't needed: the first sentence completes at 2.3 s (SS-1 passes). Captions in Source Serif 4 400, the lighter
animation-master cut (§5.3).

---

## §15 Your look at the storyboard: the checklist

Watch it once as a stranger with a thumb over the next reel, then once as the editor whose name is on it. Fix what
bothers you, in one pass.

**The style (does it feel like §The feel?)**
- Frame 0: moving master footage, full-bleed, with the first chunk already on; no title, banner or graphic; the first
  sentence a complete paradox, mechanism or problem by 3.5 s.
- It feels like walking into a documentary mid-thought, and you needed the answer.
- One argument, whole: problem, mechanism, proof, implication; nothing refers outside the span; the splices invisible.
- Still picture, moving words: no cut, zoom or event the master didn't make; pauses kept as breaths.
- Full-bleed almost everywhere; every band there because the crop would have broken the picture.
- The world rotates and something new keeps arriving; the one lift lands; the end is the implication, quiet and certain.
- Nothing drawn that the reel didn't need; gold only on another voice.

**Craft (by eye, in context; the facts are in §2)**
- The faces read: the follow crop keeps the head top inside the frame with room above it, never cuts at the eyes or
  forehead, and keeps heads out of the caption band; nothing chops a head or buries a face by accident.
- No text over text. Captions as CS-1 (§5.3), on with their words, running across cuts.
- Every chunk one speaker, coloured by the voice, checked by ear on every voice-over-picture and handover shot.
- Names, units and terms spelt exactly; numbers as spoken; no splice re-attributes a quote or a number.
- One fit per master shot, switching only on cuts; nothing soft from over-upscaling; every RF-2 shot keeps its subject and
  baked text whole, the long ones checked late in the reel too.
- Third-party spans as the master has them, or trimmed or carded (word for word, no label, no credit line); identifiers
  blurred; the end line, if used, shows the exact title long enough to read.
- The master's mix intact, nothing added. The file itself (1080 × 1920, 30 fps CFR, −14 LUFS, the end ≤ 6 f after the
  last word, no black tail) is the render's job; it checks it.

---

## §16 Build notes
- **Usually no scenes:** with no object title, end line, card or redaction, `plan/scenes.js` is empty and loads clean
  (`veos scenes-meta`); never add a placeholder scene.
- **The fade is built in:** T-END-FADE is `"end_fade": 5` on the timeline; no scene.
- **The band's backdrop brightness is built in:** `dialogue.blur_dim` 1.0 in tokens, used by `veos shots render`.
- **Devanagari:** Noto Serif Devanagari is bundled for Hindi captions.
- **Determinism:** every frame is a pure function of its index; no CSS animation in scenes.
- **Crops:** the near-static per-shot crop comes from the compositor's dead-zone follow (an explicit per-shot crop
  override isn't available); a wide dead zone gets closest to the measured look.

---

## Appendix A. Evidence map
| What | Evidence |
|---|---|
| Serif captions, 1 line, 1–3 words, cy ≈ 1380, ≈ 70 px, hard swaps | v02 @ 0:00–0:17 (y 1384, measured 70–72 px), v01 @ 0:00–0:28, v03 @ 0:00–0:03 (y 1345) |
| Gold for every guest voice, by the voice | v01 @ 0:45–0:57, 1:25–1:39; v02 @ 1:29–1:30 and 2:10–2:15 (gold over the host's face) |
| Cold open mid-sentence, no graphic | v01 @ 0:00, v02 @ 0:00, v03 @ 0:00 |
| Bands centred at y 656–1264, the caption under them, the backdrop undimmed | v02 @ 0:58–1:11, 1:46–1:50 (black); v03 @ 1:09–1:29, 1:45–1:46 (blur), surround luma 150 vs band 104 |
| No editor camera, every editor transition a hard cut, ends on the last line | ORB v02 0:00–0:17.7; v03 @ 1:29.87, 1:33.37; v01 @ 1:54.9, v02 @ 2:33.3, v03 fade @ 1:49.73 |

The full map, with every timestamp, the fidelity and completeness audits and what's unverified (speech read from the
burnt-in captions, the exact stroke and shadow, the caption lead, the sound, whether the italic object title is baked in
the master), is in `evidence.md`.

## Appendix B. Post-title and first-line bank
The style shows no headline. These are **post titles** (the reel's title on the platform) paired with the **first line**
to look for in the master. Slots in `<angle brackets>`.

| # | Post title | First line to find (SS-1 shape) | Archetype |
|---|---|---|---|
| 1 | Why a heat pump beats a heater | "A heat pump moves more heat than it uses." (paradox) | HA-14a |
| 2 | You can never see anything fall into a black hole | "You can never see anything enter a black hole." (paradox) | HA-14a |
| 3 | The hardest part of <field> isn't what you think | "One thing that makes <field> so tricky is <constraint>." (problem) | HA-14b |
| 4 | How a 1,000-tonne machine steers underground | "<Machine> <does the surprising thing> every <interval>." (mechanism) | HA-14a |
| 5 | Why most stock pickers lose | "Every year, most professional fund managers lose to a fund that does nothing." (paradox) | HA-14b |
| 6 | The box that made trade 90 % cheaper | "One steel box cut the cost of shipping by ninety percent." (claim) | HA-10 |
| 7 | Where your money goes when prices rise | "When prices rise, the money doesn't disappear." (problem) | HA-14b |
| 8 | <Expert> showed me <object> in their office | (guest) "I just have this <object> here in my office." (guest-first) | HA-14c |
| 9 | What <thing> looks like from the inside | "Imagine standing inside <thing> while it <runs>." (atmosphere) | HA-15 |
| 10 | The record nobody expected: <number> <unit> | "Their current record for <task> is <number> <unit>." (mechanism → proof) | HA-14a |
