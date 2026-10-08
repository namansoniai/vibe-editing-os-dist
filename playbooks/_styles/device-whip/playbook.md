# Device Whip Style Playbook (template v1)

**Purpose.** You (Claude) receive {{BV-01.name|the creator}}'s talking-head take with a device in hand, the POV clips they shot of that device, and the script. Use this playbook to plan and build every hook, cut, whip, caption, counter, ring and end card, so the reel feels like a hands-on tech review: you hear the presenter, you *see the real thing* on the real device, and the cut lands on the word.
**Input (SW-01 `talking_head`, spine `hybrid`):** an A-roll take (SH-1) and 4–12 POV clips of the device (SH-2 / SH-5), optionally a hold-up or lean-in hook shot, macro details and native screen recordings. Without POV clips the reel runs on the declared fallbacks (§12.3), and the checkpoint says so.
**What it is not:** a motion-graphics explainer. Graphics are support: one hook title, one counter, one ring, a few chips. The device footage carries the reel.

### Style DNA `[DNA]`
A Device Whip reel looks like a creator who just picked up a gadget and is showing you something about it *right now*. A sharp talking head on a soft, warmly lit, shallow-focus set holds the device up. On f0 the frame **punches in** as the device swings toward the lens, and a heavy **blue italic caps title** pops in phrase by phrase under the device; by 1.3–2.5 s the frame **whips** (zoom, spin or linear blur) **into the device** and you are looking down at it in a hand, a finger doing the thing. From then on the picture alternates between the presenter's face and the hand-held POV every 1–4 s, always full frame, never split; the section changes are whips (into the device and back out), everything else is hard cuts. Small, clean, white one-line captions sit at one height for the whole reel. When the reel counts something, a **red "Label: N" counter** sits right above the captions and rolls up like an odometer across every cut, and the last repetitions come as rapid step punch-ins every 0.5 s. A **cyan light sweep** runs up the device outline once, at the moment you should look at it. The reel ends on a reaction or on a clean black wordmark card.

**Copy these 5 things** (they make it this style):
1. **Face ↔ device alternation:** A-roll with the device in hand, a cut to a full-frame hand-held POV of the real device on the feature word, back to the face for the opinion; one picture at a time, 1.5–4 s each (§3.2, §9.3, §12.2).
2. **The whips:** a blur whip into the device lands by 2.5 s and opens the body; after that a whip marks every section change, into the device *or back out to the face* (zoom-flash T-WHIP, spin T-WHIP-S, linear T-WHIP-L), ≈ 1 every 4–5 s in a list reel (§6.2, §9.1).
3. **Blue italic caps title in the hook:** 2–3 short phrases, Montserrat 900 italic caps, blue gradient, white stroke, dark extrusion, each phrase popping in (2 f, scale + motion blur) at cy 1340 over an f0 punch-in (§5.2, P-01, Z-4).
4. **Small white one-line captions**, sentence case, no keyword colour, one fixed y per reel (§5.3, CS-1).
5. **The red running counter + the cyan sweep:** "Label: N" above the captions for anything repeated, digits rolling up on each tick (§17.1, P-18/P-19), a neon light sweep up the device outline at the moment of attention (§17.2, P-03).

### Fidelity audit corrections (2026-10-06, full-resolution check of v01-v03)
Override older figures below. Evidence: `docs/audit/device-whip/audit.md`.
- Title stagger confirmed (Montserrat 900 italic caps ≈ 77 px, white stroke, hard navy extrusion); band **cy 1340**; fill less saturated: mid `#1570C8`, top `#4A9BE8`.
- Captions are Poppins **600** with a visible black outline (~3 px); 56 px confirmed. Real y wanders (cy 1277 in v03, ≈ 1600 in v02); 1400 stays as the safe-band compromise.
- Counter label is **80 px** `#D80018`, ≈ 120 px above the caption (confirmed).
- The device swing toward the lens on f0 + whip at ≈ 1.3 s is the hook (v02); without a hand-held device shot the style drops to FB-3, which reads as a different style.

### Motion audit corrections (2026-10-07, full-frame-rate bursts + ORB camera tracking of v01-v03)
Override older figures below. Evidence: `docs/audit/device-whip/completeness.md`, `evidence.md` § Motion.
- **Whips go both ways.** 10 blur transitions in the 3 reels: 4 A-roll → POV, 5 POV → A-roll, 1 hook. Three kinds: zoom-flash (T-WHIP, 9–12 f with a +25–30 % exposure lift), spin (T-WHIP-S, 7 f diagonal blur + 5° roll), linear (T-WHIP-L, 6 f horizontal). v02 runs 7 whips in 37 s (≈ 1 per 5 s, 39 % of boundaries); v03 3 in 45 s.
- **f0 punch:** v02 opens with a 1.0 → 1.43 digital zoom-in over f1–f5 (Z-4), held to the whip.
- **Title** pops in over 2 f (scale 0.70 → 1, horizontal motion blur), swaps by a 2 f blurred crossover; no slide or ghost trail. Phrases at 0.07 / 0.33 / 0.70 s, held to the whip at 1.30 s.
- **Counter tick** = odometer roll (digits slide up, 3–4 f), no scale bump. The RS-COUNT finale is step punch-ins on the clamp shot every 0.5 s (+6 to +23 % each) with a tick on each.
- **Ring** = a light sweep running bottom → top along both sides of the device outline in 9 f; no clockwise trace and no hold.
- **POV snap:** a 1.0 → 1.25 zoom on the POV over 6 f on the action word (v02 @ 8.2).
- **Bubble** flies out of the phone (a sliver that stretches left with motion blur, 5–6 f), then drifts with the footage.
- **End card:** hard cut to black (no fade), the wordmark builds in letter by letter with a smear over ≈ 14 f, holds, then smears and zoom-blurs out in 5 f; ≈ 4.9 s in all.
- **Pacing:** v02 median shot 1.6 s (p90 4.0), v03 1.0 s (p90 2.7), 28 and 42 cuts/min; v01 (story) holds one take for 13.8 s under the bubble.

### Directives `[DNA]`
| # | Directive | Where it lives |
|---|---|---|
| D1 | **The device is the hero.** Every sentence that names a feature, setting, button, number on the device or an action on it shows that thing on the real device, landed within ±5 f of the word | §1 P5b, §8.4, H8 |
| D2 | **Whip on the section change.** The hook ends in a whip into the device by 2.5 s. After that, whips mark section changes (a new item, a result, the reaction after a result) in either direction; inside an item every change is a hard cut | §6.2, §9.1, N4 |
| D3 | **One picture at a time.** A-roll or POV, full frame. No splits, no PiP, no cards stacked on the POV beyond the declared overlays (P-18, P-22, P-23, P-25, P-26, P-27) | §3.2, H14, N1 |
| D4 | **Quiet type.** Captions are small, white, one line, never coloured. The only coloured text is the hook title (blue), the counter (red) and a verdict chip | §5, N2 |
| D5 | **Count what you do.** A repeated action is counted on screen with the counter, which persists across cuts and never shows a number the footage has not earned | §17.1, H10 |
| D6 | **Show the real thing.** Real device, real screen, filmed by the creator. Mocks only as declared fallbacks, and labelled | §12.3, NC-6, N6 |
| D7 | **The joke is on the presenter's face.** Humour lands on a reaction shot (SH-9) or a line to camera, with at most one sticker per reel and no meme sounds | §8.6, N7 |
| D8 | **End clean.** Last line → hard cut to black → the wordmark card builds in (≈ 14 f) and holds, ≤ 5 s in all; or a hard end ≤ 6 f after the punchline when the CTA is `none` | §25, P-30, P-32 |

Buyer directives (`BD1…`, VAR) go here when {{BV-01.name|the creator}} adds them. They may only make the style stricter or more specific.

### Quick index
| § | What | Status |
|---|---|---|
| §0 | Style profile (switches) | ON |
| §1 | Procedure (do this in order) | ON |
| §2 | Hard rules (MUST / NEVER) | ON |
| §3 | Worlds, layouts, stage moves, safe zones | ON |
| §4 | Colour | ON |
| §5 | Type, title, captions | ON |
| §6 | Hook system (HA-17 Device whip) | ON |
| §7 | Structure and cadence | ON |
| §8 | Visual system: families, 34 patterns, lookup | ON |
| §9 | Transitions and shot grammar | ON |
| §10 | Motion, camera, layers, finishing | ON |
| §11 | Sound contract | ON |
| §12 | Footage, POV capture checklist, fallbacks, inserts | ON |
| §13 | Output contract | ON |
| §14 | Worked examples (3) | ON |
| §15 | QA checklist | ON |
| §16 | Frame template / chrome | OFF |
| §17 | Running state (counter) and anchored graphics (ring) | **ON** |
| §18 | Data contract | OFF |
| §19 | Evidence and citations | OFF |
| §20 | Dialogue | OFF |
| §21 | Canvas camera | OFF |
| §22 | Ink and annotation layer | OFF |
| §23 | Continuity | OFF |
| §24 | Series furniture | OFF (VAR) |
| §25 | Sponsor, brand and end cards | **ON** |
| Parts C–F | Exceptions, personalisation, what changed, ID index | ON |
| App. A / B | Title and hook bank / evidence map | ON |

**Format:** one, `F-A "Device Whip"`, used by every reel. Reel shapes inside it: `RS-LIST` (a list of tricks or features), `RS-COUNT` (a count-up test), `RS-STORY` (one device moment) (§7.1).

---

## §0 Style profile `[REQ]`

```yaml
profile:                         # mirrored in tokens.json → profile
  source_type: talking_head      # A-roll + POV device clips (the POV is listed in §12, not a second source type)
  presenter: {presence: host, share: [35, 75], max_absence_s: 5.0}
  spine: hybrid                  # A-roll and device POV alternate as equals
  captions: {mode: full, role: support, mute_policy: mute_safe}
  graphics: support
  duration: {class: short, target_s: [28, 50]}
  language: {speech: en, captions: {lang: en, script: Latn, transform: verbatim}, on_screen: en, post_title: en,
             supported: [[en, en, Latn], [hinglish, hinglish, Latn], [hi, hi, Deva]]}
  numbers: {grouping: international, currency: "$", compact: k_m_b, units: metric, decimals: 0}
  tone: {energy: balanced, comedy: light, comedy_max: light}
  themes: {policy: single, packs: [], default: null}
  formats: {list: [F-A], default: F-A}
  footage_dependency: high
  cta: {devices: [end_card, comment_keyword, link_bio, none], placement: end, chosen: end_card}
  modules: {chrome: false, running_state: true, anchors: true, data_figures: false, citations: false,
            dialogue: false, canvas_camera: false, ink: false, continuity: false, series: false, brand: true}
```

Why each value:
- **source_type `talking_head`**: every analysed reel is built on one presenter's A-roll (v01, v02, v03); the POV device camera is a second setup of the same shoot (v02 @ 0:02, v03 @ 0:03).
- **presenter `host` 35–75 %, absence ≤ 5.0 s**: face share measured ~35 % (v02), ~45 % (v03), ~75 % (v01); the longest device-only runs are ~4–5 s (v02 @ 0:26–0:30, v03 @ 0:34–0:37).
- **spine `hybrid`**: A-roll and POV alternate as equals (POV ~50–60 % of runtime, v02/v03).
- **captions `full / support / mute_safe`**: every spoken line is captioned in v02/v03; the captions serve the picture (small, no emphasis).
- **graphics `support`**: one title, one counter, a ring, a bubble and an end card illustrate the talk; the device footage carries it. Graphics beyond captions are on screen 15–45 % of runtime (v03's counter, 0:04–0:42, is the maximum case).
- **duration `short` 28–50 s**: the three reels run 27.8 / 36.9 / 45.5 s.
- **language `en`**: the burned-in captions are English and verbatim-looking. Only Latin-script combinations are supported, because the title is italic caps (Latin only).
- **numbers international, `$`**: tech prices and counts; VAR, follows BV-05/BV-06.
- **tone `balanced / light`**: calm explanations, a punchy hook and a self-deprecating joke late in the reel (v03 @ 0:23 "I look like hairy Shrek"); no meme sounds.
- **themes `single`**: one look; the set colour comes from the footage, not from packs.
- **formats one (F-A)**: the three reels share all five "copy these" traits; the trick list, the count-up and the story are reel shapes, not formats.
- **footage_dependency `high`**: the POV of the real device *is* the style (analysis gap G1); every shot has a fallback (§12.3).
- **cta**: v01 ends on a wordmark end card; v02/v03 end on the punchline (`none`). The buyer picks one at setup (BV-08).
- **modules**: `running_state` (the counter, v03), `anchors` (the ring on the device, v03 @ 0:00.3), `brand` (the end card, v01 @ 0:23). Everything else is absent from the evidence.

---

## §1 Procedure (follow in order) `[REQ] [DNA]`

The craft step of this style is **P5b shot pairing**: deciding, sentence by sentence, whether the viewer sees the face or the device, and which POV take shows the exact thing being said.

1. **P1 Inventory.** `ffprobe` every input. Conform VFR phone footage to 30 fps CFR. Register every non-A-roll clip with `veos asset add <file> --origin creator` (they become video assets for `ctx.videoFrame`).
   - **P1b Device capture inventory.** Classify every clip by shot id (§12.2): A-roll SH-1/3/4/8/9, POV SH-2/5/6, screen recording SH-7. For each POV clip write one line: what it shows (feature, setting, result), where the action starts and resolves (clip seconds), its still windows (≥ 0.5 s with the device not moving: ring and tap anchors), and whether its UI text is legible at 1080 × 1920. Use `veos sheet` on each clip. File names follow C-13 (§12.2).
2. **P2 Prepare.** No matte (this style draws nothing behind the head). Measure the device position in the hook shot and in every POV still window you will annotate (the anchor pass, §17.2).
3. **P3 Transcribe** the A-roll with word timestamps; `transform: verbatim` (or the BV-05 choice). Add every device, app and brand name to the glossary with its exact spelling (iPhone, AirPods, Wi-Fi, Wear OS). Mask personal identifiers in captions.
4. **P4 Segment** into `HOOK` (0 → the whip landing), `ITEM-n` (RS-LIST), `REP-n` groups (RS-COUNT), `TURN` (the result), `END` (reaction + CTA). Mark jump-cut points on pauses ≥ 150 ms at word boundaries.
5. **P5 Classify** every sentence with a line type from §8.4 and mark its **trigger word** (the feature noun, the action verb, the number, the result word).
   - **P5b Shot pairing (the craft step).** For each sentence decide A-roll or POV with the device-line rule: a sentence that **names a feature, setting, button, number on the device, or an action on it → POV**; opinion, reaction, joke, setup and transitions → A-roll. Then pick the POV take that shows that exact thing; if none exists, mark the fallback (§12.3). Check the alternation limits (no run > 5.0 s, H4) and split or merge the pairing to respect them.
6. **P6 Tone-tag** every sentence: `hype` · `explain` · `awe` · `win` · `warn` · `joke` · `cta` (treatments in tokens `tone_treatment`).
7. **P7 Hook plan.** Pick the hook variant (H-A title whip, H-B question ring, §6.2) or an allowed alternate (§6.3). Write **3 hook proposals** with their titles (§6.5) and run the stopper tests (§6.1).
8. **P8 Visual plan.**
   - a pattern per sentence (§8.4);
   - **P8b counter plan** (RS-COUNT): the label, every op and its frame (§17.1);
   - **P8c anchor plan**: ring and tap-ripple boxes from the still windows (§17.2);
   - **P8d caption y**: choose `low` (1400) or `mid` (1270) for the whole reel (rule CY, §5.3);
   - the third-party moments (§12.5) and the end card (§25).
9. **P9 Beat sheet** (§13): one beat per trigger, meeting the cadence targets (§7.6).
10. **P10 SFX ledger** (§11: cue moments only) and the **transition map** (§9).
11. **P11 Assets.** Trim POV clips to their action windows, register created substitutes, resolve fallbacks and list which ones were used.
12. **P12 Checkpoint** (§13.5), then **wait for approval.**
13. **P13 Build.** Write `timeline.json` + `scenes.js` act by act; `veos scenes-meta` → `veos measure` → `veos validate`; preview; QA (§15, at most 3 passes); render.

**Module steps:**

| Module | Step |
|---|---|
| `running_state` | **P8b count plan:** the label (one noun, title case, ≤ 12 characters), the start value, one op per counted repetition with its frame; jumps marked |
| `anchors` | **P8c track pass:** for every ring, tap ripple and bubble on a moving device, `veos track --look` the first frame, then `veos track --id <device> --box x,y,w,h` (a tap: `--point x,y`) over the scene's span only; look at the preview; fall back per §17.2 when it is lost |
| `brand` | **End-card check:** the wordmark text (BV-01), the artwork asset (creator) or the created band, the CTA line (BV-08); a sponsor's logo and disclosure if any (NC-12) |

---

## §2 Hard rules `[REQ] [DNA]`

### 2.1 Editing rules (every style)
The ten editing rules in `playbooks/_global/GLOBAL-RULES.md` apply. They are directions, not limits: smooth, seamless motion; nothing overlaps by accident; keep the face clear (behind the speaker is fair game, text included); readable at a glance; one idea at a time; show the thing, not the word; say what was said; hook titles hook; pace like the style, not like a timer; the style decides the look.
- **Facts the engine checks:** accidental overlaps, jumps, the face covered, unreadable text, numbers and quotes that don't match what was said, the promised count. Every count, timing and budget this playbook gives is direction for the edit, not a limit.
- **Picture first, in this style's own look:** every key beat shows the thing being said (an object, a screen or app, a diagram, numbers in motion), not just its word; text supports the picture and never replaces it. When the speaker points with words ("this, this and this", "from this to this", "ye dekho"), show what they mean. Illustrations may use made-up but realistic numbers and names ("212 views", "1.2M views"), with no label; a number or quote the speaker says is shown as said. This overrides any rule below that bans made-up numbers or asks for an example tag: those rules now cover claims (the creator's results, prices, benchmarks, testimonials), not illustrations.
- **Hook titles hook:** the on-screen title promises the viewer something (an outcome, a curiosity gap, who it's for) and is true to what the reel delivers; it need not repeat the spoken words. This playbook sets its shape (§5.2, §6.5: lines, sizes, word limits, case), never its voice (§6).
- **Retired (8 Oct 2026), whatever this playbook says below:** no REPRESENTATIONAL or example labels on made-up cards, no credit lines, no flash limit (flash as often as this style calls for; any "NC-11" cap below no longer applies), and text may sit behind the speaker without an exception.

### 2.2 Declared exceptions
**None declared.** The style fits the global rules as written:
- the title's phrase holds follow G3 (0.25 s per word; the hook is planned around it, §6.2);
- captions are 56 px (G4 floor 54 px), slightly larger than the measured ~48–58 px (App. B), so no E3 is needed;
- counter digits change on declared `events` inside a fixed-width box, so G3 holds without E6.

### 2.3 Style MUST rules
- **H1 Frame-0 stopper.** f0 shows the device (in hand, held up or on its clamp, ≥ 15 % of frame height) **and** the question or title (title phrase 1 entering, or the first caption chunk at f0). check: V-F0
- **H2 Whip by 2.5 s.** The hook whip (T-WHIP-S with a hand-held device, T-WHIP with a clamp) starts by 2.2 s and its cut into the device POV lands by 2.5 s (measured 1.33 s v02, 2.53 s v03) (2.7 s at the latest when the spoken title runs long; then cut the title to 2 phrases). check: V-F0
- **H3 Cadence.** Body 5–10 weighted SCs per 10 s; hook ≥ 5 in 0–3 s; max gap between weight-1 SCs 2.5 s (1.25 s in the hook); nothing static > 2.5 s; 14–45 cuts per minute (measured 28 v02, 42 v03); median shot 1.0–3.2 s (measured 1.6 / 1.0 s; p90 ≤ 4.5 s). check: V-CADENCE
- **H4 Alternation.** No A-roll run longer than 5.0 s and no POV run longer than 5.0 s; minimum run 0.8 s (A-roll) / 0.4 s (POV: the step-punch finale, P-21) / 1.0 s (other POV). A longer device moment is split into two POV takes, an angle or a P-10b snap. RS-STORY may hold one A-roll take up to 8 s when a P-23 bubble or a P-13 wide lands inside it (v01 holds 13.8 s; capped by H3). check: V-LAYOUT
- **H5 Presenter share** 35–75 % of runtime; longest absence 5.0 s (the result climax P-12 included). check: V-PRESENCE
- **H6 Title limits.** Hook only; 2–3 phrases; ≤ 3 words per phrase; ≤ 9 words total; one line per phrase; each phrase held ≥ 0.25 s per word; the whole title ≤ 2.25 s; 0 emoji; one title per reel. check: V-TITLE
- **H7 Dead air.** The A-roll voice runs continuously under POV inserts; at most 1 gap ≥ 150 ms per 15 s, except one deliberate ≤ 0.4 s beat before the result reveal. check: review
- **H8 On the word.** A POV cut lands 2 f before its trigger word and is fully on within ±5 f; a counter tick lands within ±3 f of the repetition's result appearing on screen (or of the spoken number, when it is spoken). check: V-ONWORD
- **H9 Face.** Nothing in front of the face box; the title, counter, chips and bubbles keep 40 px clear of it. check: V-FACE
- **H10 Promise.** A count in the title equals the items shown; a "can it…?" title is answered on screen by the TURN; the counter's final value equals the last repetition shown; the CTA keyword is on screen ≥ 1.5 s. check: V-PROMISE
- **H11 Truth.** Counters count real repetitions in the footage; specs and numbers come from the script or from the device's own screen; no invented benchmarks or ratings. check: review
- **H12 Spelling.** Device, app and brand names are spelled exactly as their makers write them. check: V-CAPTION
- **H13 Device legibility.** When UI text is the point, the device screen fills ≥ 45 % of frame height for ≥ 1.0 s, or a P-27 loupe / P-22 chip carries it. check: review
- **H14 One picture at a time.** F-A uses only L-full, L-pov, L-device-dim (fallback only) and L-endcard; no split, stack or PiP. check: V-LAYOUT
- **H15 Captions at one height.** One caption y for the whole reel (1400 or 1270, rule CY §5.3). check: V-CAPTION
- **H16 Redaction.** Notifications, contact names, phone numbers, emails and account ids on the device screen are blurred for their whole on-screen time, unless they are the creator's own demo data. check: review (NC-14)
- **H17 Audio.** −14 LUFS integrated, true peak ≤ −1.5 dBTP, bed ≥ 18 dB under the voice. check: NC-8 (mix gate)
- **H18 Determinism.** Streaks, ripples and shards come from seeded noise of the frame number. check: NC-9

### 2.4 NEVER
- **N1** Never split the screen, use a PiP bubble, or stack a card over the POV beyond the declared overlays.
- **N2** Never colour, enlarge or bold words inside captions; never chunky or kinetic word-stack captions.
- **N3** Never show the title outside the hook, or two titles in a reel.
- **N4** Never whip inside an item (setup → POV of the same feature after the first, POV → POV, rep → rep): those are hard cuts. Never two whips within 2.5 s, and never the same whip kind 3× in a row.
- **N5** Never use stock footage, manufacturer promo clips or renders of the device. The creator's own POV only.
- **N6** Never present a drawn phone or a recreated UI as the real device.
- **N7** Never meme sounds; never a sticker on the device screen; never more than one sticker per reel.
- **N8** Never more than 3 bright hues in a frame; the title and the counter never share a frame.
- **N9** Never regrade, tint or stylise the POV: the device's real screen colours are the content.
- **N10** Never let captions sit on the UI that is being read: choose the caption y per reel (rule CY) and nudge the POV framing (`focus`, ≤ 80 px); never move the captions mid-reel.
- **N11** Never a black tail > 0.2 s; never an end card > 5 s.
- **N12** Never decorative graphics: no lens flares, light leaks, RGB splits, particle bursts or emoji rain.

Buyer additions (`BN1…`, VAR) go here.

---

## §3 Worlds, layouts, stage moves, safe zones `[REQ] [DNA; coordinates TUNE ±5%]`

### 3.1 Worlds
| ID | Kind | Look | Carries | Enter / exit |
|---|---|---|---|---|
| **W-studio** | `footage` | The creator's own set: warm or coloured practicals, deep shallow-focus bokeh (f/1.8–2.8), the presenter sharp. The background colour comes from the footage (amber library v02, RGB room v01, daylight garden v03) | A-roll: claims, opinions, reactions, setup | Hard cut; the whip leaves it |
| **W-void** | `void` | `#000000` under the full-bleed POV clip and the end card | POV inserts (drawn as P-06/P-07 scenes over it), end card | A whip or T-CUT in and out; hard cut to black into the end card |
| **W-blur-set** | `footage` (blur 36 px, brightness 0.55) | The A-roll itself, blurred and darkened | Fallback only: the drawn phone of P-11 (FB-1/FB-2) | `dim` stage move, 8 f |

The set is never replaced, matted or regraded. Its colour is whatever the creator shot.

### 3.2 Layout library
| ID | Engine | Presenter | Graphic | Caption | Share (F-A) |
|---|---|---|---|---|---|
| **L-full** | `full` | Full frame 1080 × 1920, head top y 160–320 | — (title, counter, chips over it) | CS-1 at the reel's y (1400 / 1270) | 35–75 % |
| **L-pov** | `hidden` | none (absent) | The POV clip full-bleed (x 0, y 0, 1080 × 1920) as a z2 scene | CS-1 at the reel's y | 25–65 % |
| **L-device-dim** | `full` + `dim {blur_px: 18, luma: −0.35}` | Full frame, blurred and dimmed | Drawn phone x 250–830, y 260–1320 (P-11) | CS-1 at the reel's y | 0–30 % (fallback only) |
| **L-endcard** | `hidden` | none | End card (P-32) on W-void | hidden | 0–14 % |

**Layout schedule rule:** alternate L-full ↔ L-pov. Switch on the trigger word (POV in) or on the sentence boundary (back to the face). Max run 5.0 s each; min run 0.8 s (L-full) / 1.0 s (L-pov). Tokens: `layouts.schedule`.

**Why L-pov is `hidden`, not a card:** the POV clip covers the whole frame, so the presenter footage is switched off for that span (presence counts it as absence) and the clip is drawn as a scene (`VEOS.fx.clip`, z2, full-bleed, `kind: "broll"`, `continuous: true`). When the creator spoke the line *while* filming the POV (voice recorded on that take), cut the take into the EDL as its own segment instead: the stage stays `full` and the beat carries `shot_id`.

### 3.3 Stage moves
| ID | Move | Recipe (30 fps) | Use |
|---|---|---|---|
| **G-1** | **Whip-in** | T-WHIP / T-WHIP-S / T-WHIP-L (§9.1) with stage `cut` to L-pov on the landing frame | The hook; the first POV of a new item |
| **G-2** | **Hard return** | T-CUT: stage `cut` to L-full on the first word of the opinion or reaction sentence | Returns to the face inside an item |
| **G-2b** | **Whip-out** | T-WHIP (zoom on the POV, flash, land on the face) or T-WHIP-L / T-WHIP-S, stage `cut` to L-full | After a result, or POV → the next item's setup (v02 @ 17.9, 24.4, 29.8; v03 @ 7.9, 37.9) |
| **G-3** | **POV → POV** | T-CUT between two POV takes (a new action, angle or macro), or a step punch (P-21) on the same clamp shot | A device moment longer than 5 s; each repetition in RS-COUNT |
| **G-4** | **Dim to device** | `via: dim` 8 f: the A-roll blurs and darkens while the drawn phone rises over 10 f (P-11) | Fallback FB-1/FB-2 only |
| **G-5** | **Cut to end** | Hard cut to black (P-30) on the last word's end, stage `cut` to L-endcard, the card builds in (§25) | The end card (§25) |

### 3.4 Layout diagrams
**L-full, hook (H-A title whip):**
```
┌─────────────────────────┐ 0
│  (IG top UI, keep clear)│ ← y 0–110
│        ╭──────╮         │
│   face │device│ (soft)  │ ← device held up 30–40 cm from the lens, y ≈ 280–1200
│  (soft)│ held │         │   face soft behind it (f/2)
│        ╰──────╯         │
│   WHAT THEY             │ ← TITLE phrase, cy 1340, one line, max_w 952, pops in (2 f, blur)
│                         │   (captions hidden until the whip lands)
│                         │
│ (IG bottom UI: y > 1540)│
└─────────────────────────┘ 1920
```
**L-full, body:**
```
┌─────────────────────────┐ 0
│                         │ ← y 0–110 clear
│        (head top        │ ← head top y 160–320, face x 300–780
│         y 160–320)      │
│          FACE           │
│     torso + device      │ ← device in hand visible ≥ 50 % of A-roll time
│      Reframes: 7        │ ← counter cy 1280 (= caption cy − 120), RS-COUNT only
│  small white caption    │ ← CS-1 cy 1400 (low), or 1270 (mid; the counter then at 1150)
│                         │
│ (IG bottom UI: y > 1540)│
└─────────────────────────┘ 1920
```
**L-pov:**
```
┌─────────────────────────┐ 0
│   setting chip (P-22)   │ ← chips cy 250 (top band), POV only
│     ╭───────────╮       │
│     │  SCREEN   │       │ ← device screen 40–65 % of frame height,
│     │  (UI)     │       │   centre x 380–700, centre y 700–1000
│     │           │       │
│     ╰───────────╯ hand  │ ← hand and wrist from a bottom corner
│  small white caption    │ ← cy 1400: the screen must not cross y 1340 with UI to read
│                         │
└─────────────────────────┘ 1920
```
**L-device-dim (fallback):**
```
┌─────────────────────────┐ 0
│ (A-roll blurred 18 px,  │
│   luma −0.35)           │
│      ╭──────────╮       │ ← drawn phone x 250–830, y 260–1320, tilt −6°, float ±6 px
│      │ recording│       │                          24 px under it (y 1330) with FB-2
│      ╰──────────╯       │
│  small white caption    │ ← cy 1400
└─────────────────────────┘ 1920
```
**L-endcard:**
```
┌─────────────────────────┐ 0
│  artwork band y 0–330   │ ← the creator's artwork, else the created band (P-32)
│                         │
│      YOURNAME           │ ← wordmark cy 780, Barlow Condensed 700 caps 110 px, white
│                         │
│  ╭ Comment KEYWORD ╮    │ ← CTA chip cy 1180 (comment_keyword / link_bio)
│  bottom band y 1000–1500│
└─────────────────────────┘ 1920
```

### 3.5 Safe zones and bands
- Meaning text stays inside x 64–1016, y 110–1500 (NC-5: nothing in y > 1540, nothing in the right 110 px between y 900 and 1540).
- **Caption band:** cy 1400 (`low`) or 1270 (`mid`), one line, ~63 px tall. Graphics stay out of cy ± 72 while captions show.
- **Counter band:** cy = caption cy − 120 (1280 or 1150), ~86 px tall.
- **Title band:** cy 1340 (TUNE 1240–1400; measured cy 1340, v02 @ 0:00.4-1.0), hook only; captions are hidden while it shows (H-A).
- **Chip band:** cy 250 (POV only). Verdict chips use the counter band when no counter is on screen.
- **Bubble band:** y 1060–1300 on L-full (above the low caption band with ≥ 40 px of air); with CY `mid` the bubble moves to y 860–1100.

### 3.6 Presenter rules `[COND: presence ≠ none]`
- Share 35–75 %; longest absence 5.0 s; return by a hard cut on the first word of the sentence (G-2).
- Crops: as shot. The A-roll is 9:16 vertical with the head top at y 160–320 and the face at x 300–780. Jump cuts keep the same framing (no punch reframes; Z-3 only on a joke).
- The device is visible in the presenter's hand for ≥ 50 % of A-roll time: it tells the viewer the face and the POV are the same moment.
- Nothing is drawn behind the head; no matte.

---

## §4 Colour `[REQ] [meanings DNA; brandable hex VAR]`

### 4.1 Role palette
| Role | Hex | One job | Text on it | Contrast | Brandable |
|---|---|---|---|---|---|
| `primary` | `#1570C8` | The hook title fill (gradient `title`: `#4A9BE8 → #1570C8 → #1450D6`, top to bottom), the end-card keyword chip | `paper` | 4.9 : 1 | yes |
| `accent` | `#D80018` | The running counter label | `paper` | 5.4 : 1 | yes |
| `highlight` | `#4FE1FF` | The neon ring around the device, tap ripples | `ink` | 12 : 1 | yes |
| `bad` | `#D92D20` | "FAILS / NOPE" verdict chip | `paper` | 4.9 : 1 | fixed |
| `good` | `#1A7F38` | "WORKS / PASSED" verdict chip | `paper` | 5.1 : 1 | fixed |
| `title_top` | `#4A9BE8` | The light top stop of the title gradient (follows primary) | — | — | derived |
| `title_shadow` | `#06143D` | The title extrusion (+4 / +6 px) | — | — | derived |
| `counter_stroke` | `#4A0610` | The 3 px stroke around the counter | — | — | derived |
| `ink` | `#0B0B0F` | Text on chips and bubbles | — | — | no |
| `paper` | `#FFFFFF` | Captions, the title stroke, bubbles, the wordmark | — | — | no |
| `bubble_text` | `#2C2C30` | Message-bubble body text | — | 13 : 1 on paper | no |
| `night` | `#000000` | End card, POV underlay | — | — | no |

This copy's brand colours: `primary` = {{BV-02.primary|#1570C8}}, `accent` = {{BV-02.accent|#D80018}} (the table shows the template defaults; `tokens.json → roles` is the source of truth). When `primary` is branded, `title_top` becomes a tint of it (OKLCH L +0.15) and `title_shadow` a very dark shade of its hue (L* < 15); the same for `accent` → `counter_stroke`.

### 4.2 Meanings
- **Blue = "watch this"**: only the hook title and the CTA keyword.
- **Red = the count**: only the counter label. Red never means "bad" outside the verdict chip.
- **Cyan = "look here on the device"**: only rings and tap ripples, always on the device.
- **Green / red verdicts** are the only good/bad axis, and only as chips.
- Other companies' brand colours appear only inside the creator's own footage (their device, their UI).

### 4.3 Theme packs
OFF (`themes.policy = single`): the look is one system; the set colour comes from the footage.

### 4.4 Grades
OFF (no grade tokens): the look is made at the shoot (warm practicals, shallow depth of field, a sharp presenter). Match exposure and white balance between the A-roll and the POV only; never a LUT, tint or B&W event.

### 4.5 Rules
- `max_bright_per_frame` 3. The blue title, red counter and cyan ring are never all on screen: the title is hook-only, and N8 keeps it apart from the counter.
- The title is never drawn without its white stroke and extrusion (it sits on busy footage).
- The counter is never drawn without its dark stroke.
- Footage is not regraded (N9).

---

## §5 Type and captions `[REQ]`

### 5.1 Font map `[slots DNA; families TUNE within the class]`
| Slot | Family | Weight / style | Used for | Font class (the TUNE boundary) |
|---|---|---|---|---|
| `display` | **Montserrat** | 900 italic, caps | The hook title (P-01) | heavy italic geometric sans caps: Montserrat 900i, Poppins 800i |
| `body` | **Poppins** | 600 | Captions (CS-1) | geometric sans 500–600: Poppins, Plus Jakarta Sans, Inter Tight |
| `label` | **Poppins** | 700 | Counter label, setting chips, verdict chips, CTA chip | geometric sans 700–800: Poppins, Plus Jakarta Sans |
| `numeric` | **Poppins** | 700, tabular figures | Counter digits | geometric sans 700–800 |
| `ui` | **Inter Tight** | 500 / 700 | Message bubbles, notification drops, recreated UI, legal labels | neo-grotesk UI sans 500–700: Inter Tight, Plus Jakarta Sans |
| `wordmark` | **Barlow Condensed** | 700 caps | End-card wordmark | condensed bold caps: Barlow Condensed 700, Anton |

All are bundled OFL fonts. A creator's logo is an image asset (BV-16), never a font. The exact fonts of the evidence could not be identified (unverified); these are the closest bundled matches to the measured shapes (App. B).

### 5.2 Headline element: the Title Stagger (P-01) `[DNA recipe; NICHE text]`
Kind `lockup` (one line at a time), lifetime `hook`.

| Property | Spec |
|---|---|
| Text | The hook title (a promise the reel keeps; it may repeat the spoken hook line or say it better), ALL CAPS, split into **2–3 phrases of ≤ 3 words**, ≤ 9 words total, 0 emoji. Digits for numbers |
| Type | Montserrat 900 italic, **76 px** (TUNE 68–96), line height 1.0, tracking +0.01 em, one line per phrase, centred on cx 540, max width 952 px; a phrase that measures wider shrinks to ≥ 68 px, else it is split |
| Fill | Vertical gradient `title`: `title_top` #4A9BE8 (0 %) → `primary` #1570C8 (55 %) → #1450D6 (100 %), clipped to the glyphs |
| Stroke | 3 px `paper` outside the glyphs (draw a 6 px stroke with `paint-order: stroke fill`) |
| Extrusion | Hard, no blur: `2px 3px 0 title_shadow, 4px 6px 0 title_shadow`, plus a soft `0 8px 18px rgba(0,0,0,.35)` |
| Position | cy **1340** (TUNE 1240–1400; measured v02 @ 0:00.1-1.3), below the held-up device. Frame SH-3 so the device's bottom edge sits above y 1210 (checklist C-9); never over the device screen |
| Entry ("pop") | Phrase 1 appears on **f1–f2**: scale 0.70 → 1.00 about its centre, a horizontal motion blur 12 → 0 px, opacity 0.5 → 1, expo-out; sharp on f3 (v02 @ 0.067–0.10). It lands while the Z-4 open punch is still running |
| Swap | A **2 f blurred crossover**: the old phrase fades 1 → 0 while the new one pops 0.85 → 1.00 with a 10 px horizontal blur; both are on screen for 1 f (v02 @ 0.30–0.37, 0.70–0.73). Each swap is a declared scene `event` |
| Timing | Phrase k enters 2 f before its first spoken word, but never before the previous phrase has held 0.25 s × its words (the source swaps faster, 0.23–0.4 s per phrase; G3 wins) |
| Life | No pulse, no drift. The title is the whole hook |
| Exit | No own exit: it stays up to the whip and is blurred away with the frame (scale 1 → 1.5 about the device point + opacity 1 → 0 over the whip's 3–4 out-frames). Never a pop mid-word |
| Captions | Hidden from f0 until the whip lands (`captions.hide: [[0, t_whip_cut]]`) when the title repeats the spoken hook line; a title in its own words leaves the captions on |
| Budget | One title per reel (H6, N3). It never appears again, not even in the end card |

### 5.3 Caption system: CS-1 "quiet line" `[DNA mechanics; size and y TUNE; language VAR]`
`extends: "lib:mrwhose"`, tuned to the measured frames.

| Group | Fields (CS-1) |
|---|---|
| Mode | `full` / `support` / `mute_safe` |
| Chunking | `unit: line`; **3–6 words** per chunk; `max_chars_line` 30; **1 line**; never split a name, number or unit; a sentence end always breaks (`punct_break`); a pause ≥ 0.9 s always breaks |
| Timing | Lead 2 f before the first word; min hold 0.25 s per word; **hard swap** (0 f; the evidence shows straight swaps); `pause_hold_s` 0.6 (the last chunk stays up through a short pause, then clears); tail 0.12 s after the last word |
| Skin | Poppins **600**, **56 px** (TUNE 54–66), `TC-subtitle`, sentence case (as spoken), tracking 0, line height 1.12, `paper` white, a clearly visible 3 px `#000000` outline (stroke 3) under the fill + shadow `0 3px 10px rgba(0,0,0,.6)`; no container |
| Position | `fixed_y`, cx 540, max width 952, centred; **cy set once per reel** by rule CY: **1400 (`low`, default)** or **1270 (`mid`)**; `avoid_face` on (a chunk that would touch the face box moves below the chin) |
| Speakers | n/a (one presenter) |
| Emphasis | **none**. No colour, no bold, no size change (DNA, N2) |
| Variants | none (no karaoke, tiers, duet, stack) |
| Hide | Under z8 scenes; on the 3 peak frames of a T-WHIP (`captions.hide`); during the H-A title (timeline `captions.hide`); during the end card |
| Language | Latin script; `keep_english_terms`; spelling normalised to the glossary (device and app names exact); profanity masked `inner` by default (S**T) |

**Rule CY (caption y per reel).** At P8d, take the middle frame of every POV clip used in a beat where UI text must be read, plus every SH-5 clamp shot. For each candidate (`low` 1400 / `mid` 1270), sum the beat time in which the caption band (cy ± 40 px) or the counter band (cy − 120 ± 45 px, RS-COUNT only) overlaps (a) UI text being read, (b) the finger's tap point, (c) the device's own on-screen controls being used. Pick the candidate with less overlap; on a tie pick `low`. Write it once: `plan/tokens.override.json` → `{"patch": {"captions.profiles.CS-1.position.cy": 1400}}` (TUNE path, range 1240–1440) and the reel header `caption_y`. The y never changes within a reel (H15).

Measured reference: the evidence placed captions at y ≈ 1607 (v02) and ≈ 1273 (v03). 1607 sits in the IG bottom band (NC-5), so `low` is lifted to 1400; `mid` keeps the v03 placement.

### 5.4 Other text systems
| System | Class | Recipe | Hold |
|---|---|---|---|
| **Counter label** (P-18) | TC-display | "{Label}: {n}", Poppins 700 **80 px** (TUNE 72–88; measured ≈ 80, v03 @ 0:06), `accent` fill, 3 px `counter_stroke` stroke + `0 3px 8px rgba(0,0,0,.45)`; centred cx 540, cy = caption cy − 120; fixed-width box sized for "{Label}: 888" so the rect never moves | From the first counted repetition until 8 f before the result climax (P-12) or the end |
| **Setting chip** (P-22) | TC-label | `paper` pill at 94 % opacity, `ink` Poppins 700 **44 px**, radius 22, padding 10 / 26; cy 250 on POV | ≥ 1.2 s |
| **Verdict chip** (P-25) | TC-label | "WORKS ✓" on `good` / "FAILS ✕" or "NOPE" on `bad`, `paper` Poppins 700 caps **48 px**, radius 24, padding 12 / 30 | ≥ 1.0 s |
| **Message bubble** (P-23) | TC-label | White bubble, radius 34, max width 640, `bubble_text` Inter Tight 500 **42 px** (key noun 700), avatar Ø 112 with a 4 px white ring, meta "Name · 10:37" Inter Tight 600 26 px (TC-legal, 80 % white) under the bubble's right edge | ≥ 2.0 s and the whole spoken line |
| **Notification drop** (P-24) | TC-label | Rounded 36 px banner, `#1C1C1E` at 88 %, a generic app glyph, title Inter Tight 700 40 px + body 500 40 px, white | ≥ 1.5 s |
| **End-card wordmark** (P-32) | TC-display | The creator's name (BV-01) in Barlow Condensed 700 caps, fit to ≈ 820 px wide (110–200 px), white, cy 780 | The end card (≤ 5 s) |
| **CTA chip** (P-33) | TC-display | "Comment" Poppins 700 48 px white + the keyword in a `primary` chip, Poppins 800 caps 64 px, `paper` text, radius 20 | ≥ 1.5 s |
| **disclosure** | TC-legal | Inter Tight 600 caps 24 px, tracking 0.08 em, white at 80 %, under the element it labels | The element's whole hold |

### 5.5 Language and number rules
- Captions are verbatim speech in the BV-05 language (`en` default). Hinglish captions stay romanised; English terms stay as spoken.
- Device, app, setting and brand names are spelled exactly (glossary). Product names keep their maker's case (iPhone, not Iphone).
- The title is ALL CAPS, Latin only (Devanagari has no italic caps; a `hi` speaker gets Hinglish romanised captions and an English or romanised title).
- Numbers: digits on screen ("600", "20"), international grouping (1,200), `$` by default (BV-06 follows the language: Indian creators get ₹ and Indian grouping). Specs keep their units with a thin space ("5 mm", "120 Hz").
- The counter label is one noun in title case, ≤ 12 characters ("Reframes", "Batches", "Drops", "Tries", "Washes").

---

## §6 Hook system `[REQ]`

**Hook title (every style, 8 Oct 2026; above anything below):** the on-screen title promises the viewer something: an outcome they want, a curiosity gap, or who it's for ("How to go viral as a doctor creating content", not the label "Reels for Doctors"). It doesn't have to repeat the spoken words; it has to be true to what the reel delivers. A title shown as someone's words (in quotes) is still word for word. This section sets the title's shape (lines, sizes, word limits, case, the keyword device), never its voice. Write 8–10 candidates from the formulas below plus the proven patterns ("How to X as a Y", "Why your X isn't working", "The X nobody tells you", "Stop doing X", "Your X vs mine", a number or a contrast), score them on outcome, curiosity, who it's for and brevity, check the best against the stopper tests, and pick; any "write 3" below means this, and the next two go to the storyboard as alternates. A style with no on-screen title applies this to its post title.

### 6.1 Stopper tests
| Test | This style's number |
|---|---|
| ST-1 Thumbnail | f0 at 25 % scale: the device is recognisable and the title phrase (76 px → 19 px) or the first caption chunk is readable |
| ST-2 Mute | By 3 s, without sound: a device + a question or claim about it + the whip into it |
| ST-3 Motion at f0 | The device swinging in (H-A) or the presenter leaning to the device (H-B), plus the Z-4 open punch, the title pop or the ring sweep |
| ST-4 Read time | Title ≤ 9 words → ≤ 2.25 s at 0.25 s per word; a question chunk (3–6 words) ≤ 1.5 s |
| ST-5 Change count | ≥ 5 weighted SCs in 0–3 s (`cadence.hook_sc_3s`) |
| ST-6 Payoff-by | The whip into the device by **2.5 s** |

### 6.2 Default archetype: HA-17 Device whip `[DNA]`
Two variants of the engine's HA-17 Device whip (tokens `hooks.variants`: H-A = `HA-17.A`, H-B = `HA-17.B`; `meta.hook_archetype` stays `HA-17`). Pick by the footage: **H-A** when SH-3 (hold-up) exists and the spoken hook is a ≤ 9-word line; **H-B** when the device sits on a clamp (SH-4) or the hook is a question longer than 9 words.

**H-A "Title whip"** (spoken: "What they don't tell you about your phone." ≈ 2.0 s)

| t (s) | Frame | Visual | Title / captions | Layout / camera | SC | Cue moment |
|---|---|---|---|---|---|---|
| 0.00 | f0 | SH-3: the device swinging toward the lens (live, motion-blurred), face soft behind | — | L-full; Z-4 `crash-zoom` 1.0 → 1.4 over f1–f5 (ease-out), held to the whip | (f0) | **hook**: one cue on the punch + title |
| 0.03–0.10 | f1–f3 | The punch runs; the device fills ≥ 30 % of frame height by f12 | P-01 phrase 1 "WHAT THEY" pops in at cy 1340 (f1–f2), sharp f3 | — | event | — |
| 0.40–0.70 | f12–f21 | P-03 sweep up the device outline (only when it is still from f9; otherwise skip it) | — | — | sweep (event) | reveal (optional) |
| 0.50 | f15 | — | Phrase 2 "DON'T TELL YOU" (2 f crossover) | — | event | — |
| 1.25 | f38 | — | Phrase 3 "ABOUT YOUR PHONE" | — | event | — |
| 2.00 | f60 | T-WHIP-S (default when the device is hand-held) or T-WHIP: Z-5 roll / Z-1 zoom, blur pass; the title blurs away with the frame | — | camera | camera | **transition**: whip cue |
| 2.17–2.27 | f65–f68 | Cut: stage L-pov; the item-1 POV clip lands blurred and settles over 3 f | Captions resume on the first sharp POV frame | T-WHIP-S marker, stage cut | transition | — |
| 2.27–4.5 | | Item 1 on the device (P-06 + P-10 push) | CS-1 chunks | L-pov | captions 0.5 each | — |

Weighted SCs in 0–3 s: punch + phrase 1, phrase 2, phrase 3, (sweep), camera, transition + stage (one frame), 1–2 caption chunks → **6–8**. The source lands the whip at 1.33 s (v02); land it as early as the spoken title allows.

**H-B "Question ring"** (spoken: "Can your phone actually see the back of your head?" ≈ 2.3 s)

| t (s) | Frame | Visual | Captions | Layout / camera | SC | Cue moment |
|---|---|---|---|---|---|---|
| 0.00 | f0 | SH-4: the presenter lunging in toward the device on its clamp (live) | Chunk 1 "Can your phone" at f0 | L-full | (f0) | **hook**: one cue on the sweep (0.3 s) |
| 0.30–0.60 | f9–f18 | P-03 sweep runs up the device outline (`kind: "device"`) once the presenter has settled (v03 @ 0.30–0.57) | — | — | sweep @ 0.3 (event) | — |
| 0.83 | f25 | — | Chunk 2 "actually see" | — | 0.5 | — |
| 1.30 | f39 | The presenter presses the device: P-26 tap ripple at the touch point | — | — | event | — |
| 1.67 | f50 | — | Chunk 3 "the back of your head?" | — | 0.5 | — |
| 2.20 | f66 | T-WHIP: Z-1 `zoom-through` 1.0 → 1.6 over 7 f about the device + P-05 radial blur + the flash lift (v03 @ 2.47–2.74) | (hidden across the 3 peak frames) | camera | camera | **transition**: whip cue |
| 2.47 | f74 | Cut to SH-5: the clamped device full frame, finger tapping | Chunk 4 "So using the new…" | L-pov, T-WHIP marker | transition | — |

Weighted SCs in 0–3 s: ring, chunk 2, ripple, chunk 3, camera, transition (+ stage), chunk 4 → **5.5–6**. Max gap between weight-1 SCs: 0.3 → 1.3 → 2.2 → 2.47 (≤ 1.25 s).

**Never skip the whip.** Even when the first POV is a hard cut later in the body, the hook's first entry into the device is a whip by 2.5 s (H2).

### 6.3 Allowed alternates `[DNA list; VAR choice per reel]`
**HA-02 Headline + proof.** Use when the *result* is the hook ("this is what 20 edits do to a photo").

| t | Visual | Text | Payoff |
|---|---|---|---|
| f0 | SH-3 hold-up with the result **already on the device screen** (scene `kind: "device"` on the ring or `satisfies: ["proof"]` on the title) | P-01 phrase 1 | — |
| 0.4–1.9 | Sweep up the device; phrases 2–3 | P-01 | — |
| ≤ 2.3 | T-WHIP into the result full-bleed (P-12, short) | captions resume | proof ≤ 2.5 s |
Example (phones): "THIS PHOTO / WAS EDITED / 20 TIMES". Example (kitchen): "THIS BLENDER / SURVIVED / 20 ROUNDS".

**HA-10 Host flash → subject.** Use when the device action needs no setup and is fast (a 2-second trick).

| t | Visual | Text | Payoff |
|---|---|---|---|
| f0 | A-roll mid-gesture toward the device | Chunk 1 at f0 | — |
| ≤ 0.7 | T-WHIP (6 f version) or T-CUT into the POV of the action | captions continue | subject full frame ≤ 0.7 s |
Example (phones): "Hold the space bar." → POV thumb on the keyboard at 0.6 s. Example (kitchen): "Tap this twice." → POV of the button at 0.6 s.

**HA-14 Cold authority.** Use for RS-STORY (one device moment told as a story).

| t | Visual | Text | Payoff |
|---|---|---|---|
| f0 | A-roll mid-sentence with the device moving in hand (v01 @ 0:00) | Chunk 1 at f0 | — |
| ≤ 1.0 | The strongest image: the device held up to the lens or the POV of the message/result | captions continue | ≤ 1.0 s |
| ≤ 3.0 | First T-WHIP into the device | — | — |
Example (phones): "So my phone did something weird last night." Example (kitchen): "So this coffee machine just texted me."

### 6.4 Hook pairs by topic `[NICHE]` (subject → reveal)
| Topic | First subject (f0) | The reveal (by) | Variant |
|---|---|---|---|
| [NICHE: example] Phone keyboard trick | Phone held up; "WHAT THEY / DON'T TELL YOU / ABOUT YOUR PHONE" | POV: thumb holds the space bar, the cursor glides (2.3 s) | H-A |
| [NICHE: example] Burst-photo limit | Phone on a clamp, ring; "How many photos can one burst take?" | POV: shutter held, the burst number climbing (2.5 s) | H-B |
| [NICHE: example] AI photo edit pushed to the limit | Phone on a monopod, ring | POV: edit 1 result; counter "Edits: 1" (2.5 s) | H-B (RS-COUNT) |
| [NICHE: example] Battery-health myth | Phone held up; "STOP CHARGING / YOUR PHONE / LIKE THIS" | POV: the battery settings screen (2.3 s) | H-A |
| [NICHE: example] Air fryer hidden button | Fryer on the counter, presenter beside it; "THE AIR FRYER / BUTTON NOBODY / PRESSES" | POV: finger long-presses, the display changes (2.3 s) | H-A |
| [NICHE: example] Blender ice test | Blender on the counter, ring; "Can a 30-dollar blender crush ice twenty times?" | POV top-down into the jar, batch 1 crushed; "Batches: 1" (2.5 s) | H-B (RS-COUNT) |
| [NICHE: example] Milk frother trick | Frother held up; "YOU'VE BEEN / FROTHING MILK / WRONG" | POV: the wand angle that makes foam (2.3 s) | H-A |
| [NICHE: example] Knife sharpener test | Sharpener held up, ring | POV: a paper slice after pass 1; "Passes: 1" (2.5 s) | H-B (RS-COUNT) |

The editor appends a row for every new reel (D.6): the device, what f0 shows, what the whip reveals and when.

### 6.5 Title writing `[DNA formula; NICHE text]`
**Formula:** `[setup] / [twist] / [the device]` in 2–3 phrases of ≤ 3 words, ALL CAPS, ≤ 9 words: a promise true to the reel (it need not be the spoken hook line). The device (or its category) is named in the last phrase.

| Template | Example |
|---|---|
| **Secret** (default) | WHAT THEY / DON'T TELL YOU / ABOUT YOUR {DEVICE} |
| **Can it** | CAN YOUR {DEVICE} / ACTUALLY / {DO X}? |
| **Limit** | I PUSHED / {FEATURE} / TO THE LIMIT |
| **Stop** | STOP USING / YOUR {DEVICE} / LIKE THIS |
| **Count** | {N} {DEVICE} TRICKS / YOU NEVER USE |
| **Wrong** | YOU'VE BEEN / USING {X} / WRONG |
| **Price** | THE {PRICE} {DEVICE} / THAT BEATS / {RIVAL} |

- **Write 3 and pick by the stopper tests** (thumbnail, read time, mute).
- **Banned:** "INSANE", "MIND-BLOWING", "YOU WON'T BELIEVE", emoji, a count the reel doesn't deliver, a claim the footage doesn't show.

### 6.6 Hook sound
See §11: the hook carries one cue on the title entry or ring and one on the whip; the music bed enters on the whip landing.

### 6.7 CTA `[DNA device set; VAR choice]`
| Device | Spoken pattern | On screen | Hold | Placement | Silence before |
|---|---|---|---|---|---|
| `end_card` (default) | none needed; the last line is the reaction | P-30 fade → P-32 wordmark card | 2.5–4.0 s | end | 1.0 s with no cue before the card |
| `comment_keyword` | "Comment KEYWORD and I'll send you …" | P-32 + P-33 keyword chip | keyword ≥ 1.5 s | end | 1.0 s |
| `link_bio` | "It's linked in my bio." | P-32 + a "Link in bio" chip (P-33 recipe, no keyword) | ≥ 1.5 s | end | 1.0 s |
| `none` | — | Hard end ≤ 6 f after the last word, on a reaction | — | end | — |

This copy: CTA device `{{BV-08.device|end_card}}`, keyword `{{BV-08.keyword|KEYWORD}}`, wordmark `{{BV-01.name|YOURNAME}}`.

---

## §7 Structure and cadence `[REQ] [DNA]`

### 7.1 Structure type: `list`, in three reel shapes
| Shape | Arc | When | Evidence |
|---|---|---|---|
| **RS-LIST** | hook → items (2–5) by the ritual → best item last → reaction → END | Hidden features, settings, tips, "N things" | v02 (five tricks, no numbering) |
| **RS-COUNT** | hook (question) → setup (what is counted, rep 1) → reps 2…N with the counter → re-hook "let's push it" → TURN (the result held) → reaction → END | "Can it do X?", stress tests, "how many times…" | v03 (Reframes 1 → 20) |
| **RS-STORY** | cold line with the device in hand → the moment on the device (message, result) → context → payoff → END card | One device moment, an invite, an unboxing story | v01 (a message, the wide shot, the end card) |

The reel header declares the shape (`structure.shape`). RS-STORY is a list of one item.

### 7.2 Markers
- **RS-LIST: none (spoken only).** No numbers on screen; each item opens with the cut into the device on the feature noun. The order words ("next", "and this one") are spoken, not shown.
- **RS-COUNT: SM-COUNTER** — the counter label (P-18) is the marker and the structure; numbering ascends.
- **RS-STORY: none.**

### 7.3 Unit ritual (identical for every unit)
**RS-LIST item:**
1. A-roll setup sentence, 0.8–2.5 s, device in hand (P-14 / P-15).
2. Into the device on the feature word, lead 2 f: a **whip** (T-WHIP, T-WHIP-S or T-WHIP-L, rotating kinds) when it opens the item, a T-CUT or T-MATCH otherwise.
3. POV 1.5–4.0 s (P-06 / P-09) with P-10 push; at most one overlay (P-22 chip, P-26 ripple, P-27 loupe or P-03 ring).
4. A second POV take (G-3) when the device moment runs past 4 s.
5. Back to the face for the "why it matters" or the reaction, 0.8–2.5 s: a hard return (G-2) inside the item, a whip-out (G-2b) when the POV just showed the item's result and the next line moves on (≈ every second item, v02).

**RS-COUNT repetition:**
1. POV clamp take (SH-5, P-07), 1.0–3.0 s: the action.
2. The result appears on the device → counter tick (P-19) within ±3 f of it.
3. Every 2–3 repetitions, an A-roll reaction 0.8–2.0 s (P-16); the counter stays up across the cut; a striking result exits to it by a whip-out (G-2b, v03 @ 7.9).
4. Repetitions not shown are skipped with a jump on the cut (P-20, e.g. 5 → 7).
5. **Finale:** the last 4–6 repetitions run as P-21 step punches on one clamp take, one every 0.5 s, then a whip into the TURN.

### 7.4 Open loops and re-hooks
- **Loops used:** the title's question or "can it" (paid at TURN, on screen); "to the limit" (paid by the final count); "the best one is last" (RS-LIST, paid by the last item).
- **Re-hook:** none needed under 45 s (`short`). A reel over 45 s gets one at 45–60 % of its runtime: an A-roll line that raises the stakes ("now let's go to twenty") + a T-WHIP into the next POV.
- **Intro cap:** hook ≤ 15 % of runtime (the whip lands by 2.5 s, so ≤ 9 % of a 28 s reel).

### 7.5 Rhythm and energy
- **Curve:** hook (fast: title or ring, whip) → items steady (alternation every 1.5–4 s) → a joke or reaction beat near the middle (45–65 % of runtime) → **TURN**: the result held longest (2–5 s, P-12; the counter exits first) → reaction 0.8–2 s → END.
- **Entertainment beat** every 8–12 s: a reaction shot (P-16), a self-aware line to camera, at most one sticker (P-29). Never two jokes back to back.
- **Escalate:** RS-LIST saves the best trick for last; RS-COUNT makes the last repetitions faster: 1.0–1.5 s each, then the 0.5 s step-punch run (P-21) before the TURN.

### 7.6 Cadence (state changes)
| Token | Value | How it is reached |
|---|---|---|
| `sc_per_10s` | **5–10** weighted | 3–5 cuts (A-roll ↔ POV, POV ↔ POV, jump cuts) + 7–9 caption chunks × 0.5 + ticks, rings, chips |
| `hook_sc_3s` | **5** | §6.2 tables |
| `hook_max_gap_s` | **1.25** | Title phrases / ring / ripple spaced ≤ 1.25 s |
| `max_gap_s` | **2.5** | A POV over 2.5 s gets an internal event (the UI change, a ripple, a tick) or a second take |
| `max_static_s` | **2.5** | Live footage counts as motion; P-10 push keeps POVs alive |
| `caption_weight` | **0.5** | support captions |
| `cuts_per_min` | **14–45** (DNA) | Measured at full frame rate (blur whips and step punches counted): 28 (v02), 42 (v03); v01 (≈ 7) is the story shape, which meets 14 with jump cuts |
| `median_shot_s` | **1.0–3.2** | Measured 1.6 (v02, p90 4.0), 1.0 (v03, p90 2.7); longest no-cut stretch 4.4 s (v02), 4.7 s (v03), 13.8 s (v01 under the bubble) |

Write every A-roll ↔ POV switch as a `transitions` entry (`T-WHIP`, `T-CUT`, `T-MATCH`, `T-WHIP-L`) so V-CADENCE counts it as a cut; jump cuts inside the A-roll come from the cut map.

---

## §8 Visual system `[REQ]`

### 8.1 Graphics role and budget
- `graphics: support`. The device POV is footage, not graphics; graphics are the overlays that point at it.
- Overlay graphics (title, counter, ring, ripples, chips, bubbles, verdicts, end card) are on screen **15–45 %** of runtime beyond captions.
- **34 patterns** (P-01…P-34) in 12 families; ≥ 4 families per 60 s (B-1, B-2 and ≥ 2 engine families).
- **Numbers become pictures, on the device:** a spoken number in a device beat is visible on the device's own screen (POV) or, when the screen can't be read, on a P-22 chip; a repeated action becomes the P-18 counter. A number is never a free-floating hero graphic in this style.

### 8.2 Families
| ID | Family | Source class | The buyer supplies |
|---|---|---|---|
| **B-1** | A-roll talking head (SH-1/3/4/8/9) | buyer-owned | The main take; optional hold-up, lean-in, wide and reaction shots |
| **B-2** | Device POV (SH-2/5/6) | buyer-owned | 4–12 POV clips (must) |
| **B-3** | Screen recording (SH-7) | buyer-owned | Native recordings of each UI step (backup) |
| **B-4** | Hook type | engine | — |
| **B-5** | Device marks: ring, tap ripple, loupe | engine | — |
| **B-6** | State and verdicts: counter, verdict chips | engine | — |
| **B-7** | Setting chips | engine | — |
| **B-8** | Created UI: drawn phone, message bubble, notification, logo plate, headline card | engine (the created substitutes of §12.5) | — |
| **B-9** | Creator-supplied third-party: a friend's message screenshot, a news screenshot, a brand still the creator holds | creator-supplied; substitute = B-8 | Only if they have it (asked once, §12.5) |
| **B-10** | End card | engine + buyer artwork | Optional logo or artwork (BV-16) |
| **B-11** | Comedy (light) | engine | — |
| **B-12** | Transition passes (whip blur, flash, cut to black: core built-ins) | engine | — |

### 8.3 Pattern specs
Frames at 30 fps. "z" is the scene layer. Every text scene sets `text_class`.

**Hook and transitions**
| ID | Name | Type | On screen | Motion recipe | When | Family / class | Needs |
|---|---|---|---|---|---|---|---|
| **P-01** | Title Stagger | overlay | §5.2 title, one phrase at a time, cy 1340 | Phrase pops in over 2 f (scale 0.70 → 1, horizontal blur 12 → 0 px, opacity 0.5 → 1); swaps by a 2 f blurred crossover; no own exit, blurred away inside the hook whip. z10, `kind: "lockup"`, `satisfies: ["question"]` (+ `"device"` when the f0 frame shows the device ≥ 15 % of frame height) | H-A, HA-02 | B-4 / TC-display | events per swap |
| **P-02** | Question Chunks | overlay | The hook question in CS-1 captions from f0, no title | Caption engine; chunk 1 at f0 | H-B, HA-10, HA-14 | captions / TC-subtitle | — |
| **P-03** | Ring Sweep | annotation | The device outline + 14 px (radius = device corner radius + 14) drawn as a glowing segment ≈ 45 % of the outline height on both sides at once: white 4 px core, `highlight` 8 px stroke, glow `0 0 18px` at 70 % + `0 0 40px` at 35 % | The segment travels **bottom → top** over 9 f (ease-in-out): f1 the bottom corners light, f4–f5 mid sides, f7–f8 the top edge, f9 gone; its tail fades as it climbs; no hold (v03 @ 0.30–0.57). z6, `kind: "device"`, events [0.15] | Hook (H-B always, H-A when the device is still); "look at this", the moment of attention in the body (≤ 3 per reel) | B-5 / — | a `veos track` of the device (§17.2) |
| **P-04** | Hold-up | cut | SH-3: the device swung to 30–40 cm from the lens, face soft behind | The footage itself; the title sits under the device | H-A f0 | B-1 | SH-3 |
| **P-05** | Whip Pass | transition pass | Drawn by core, no scene: T-WHIP = a footage **radial blur** centred on the device point (`timeline.blur` `kind: "radial"`, `at: [x, y]`) + a **white flash** (`timeline.transitions` `type: "flash"`); T-WHIP-S / T-WHIP-L = the built-in **`whip`** transition (directional smear + travel) | Flash (T-WHIP only): white 0 → 28 % over the 4 out-frames, peak on the cut, back to 0 over 3 land frames (measured luma +25–31 %, v02 @ 10.6, v03 @ 2.5). Radial blur over f−2…f+1, the picture fully blurred (measured 3 f) | Inside every whip | B-12 / — | the device point (screen px from `veos track --look`, or the POV screen centre) |

**Device POV**
| ID | Name | Type | On screen | Motion recipe | When | Family / class | Needs |
|---|---|---|---|---|---|---|---|
| **P-06** | POV Hand | cut | SH-2 full-bleed: the device in one hand, screen 40–65 % of frame height, the set blurred behind | `VEOS.fx.clip` z2, `kind: "broll"`, `continuous: true`, `kenburns: [1.0, 1.06]` over the shot, `focus` on the screen centre; enters via T-WHIP or T-CUT | A feature, setting or action is named | B-2 | SH-2 |
| **P-07** | POV Clamp | cut | SH-5 full-bleed: the device locked off on its clamp, a finger enters | No push (stillness shows the change); 1.0–3.0 s per take; the finale switches to P-21 step punches | RS-COUNT repetitions; a step-by-step setting | B-2 | SH-5 |
| **P-08** | Macro Push | footage-treatment | SH-6: an icon, port, button or texture, tilted 15–25° | `kenburns: [1.00, 1.12]` over 3–4 s, eased in-out | A tiny detail is the point ("the clock icon actually ticks") | B-2 | SH-6 |
| **P-09** | Scroll Run | cut | POV of a continuous interaction (scrolling, a dial, a slider) | Holds until the interaction resolves; ≤ 5 s (H4); an `events` mark where the UI changes | "Watch what happens when…" | B-2 | SH-2 |
| **P-10** | POV Push | footage-treatment | Any POV longer than 2.5 s | `kenburns: [1.00, 1.08]` + a declared event at the UI change | Keeps long POVs alive (max_gap 2.5 s) | B-2 | — |
| **P-10b** | POV Snap | footage-treatment | The POV clip jumps closer on the action word (the shutter, the result appearing) | Scale 1.00 → 1.25 over 6 f (≈ 1.05 per frame, ease-out at the end), then hold to the cut; about the screen centre (v02 @ 8.17–8.33) | ≤ 1 per POV, ≤ 3 per reel; the action word of a POV over 2 s | B-2 | a ≥ 1440 px wide POV for no visible softness |
| **P-11** | Drawn Phone | fallback | A generic phone frame (radius 64, 14 px `#111` bezel, a pill-shaped island) 580 × 1060 at x 250, y 260, tilt −6°, float ±6 px on a 3 s sine; the screen plays the SH-7 recording (`ctx.videoFrame`) or a recreated UI (`fx.appUI`) | Rise 12 f + de-blur 12 → 0 px; exit fall 8 f; stage `dim` 8 f underneath (L-device-dim).**3D variant** (no device footage, a still screen): `VEOS.fx.three({box: {x: 220, y: 300, w: 640, h: 1100}, insert: "<insert id>", objects: [{kind: "device", screen: "<screenshot asset>", rot: [0, -24, -6], keys: [{at: 0, rot: [0, -40, -6], scale: 0.9}, {at: 0.4, rot: [0, -24, -6], scale: 1, ease: "expoOut"}]}]})`. No `camera`: the phone fills its box by default (≈ 1050 px tall, the spec size). `insert` is a plain field (V-INSERTS reads it). The screenshot is a phone-size capture: `veos capture <url> --size 390x844@3x` (1170 × 2532) → `veos asset add --origin created`; a recording stays 2D (`screen` takes an image); one 3D scene on screen at a time (≈ 70–95 ms/frame) | FB-1 / FB-2 only | B-8 / TC-legal label | SH-7 or a recreated UI |
| **P-12** | Result Full-bleed | cut | The TURN: the device's output (the photo, the finished batch, the screen result) full frame | `kenburns: [1.00, 1.10]` over 2–5 s; the counter exits 8 f before it; captions continue; no other graphic | The climax / the answer to the title | B-2 | SH-2 / SH-5 |
| **P-13** | Wide Context | cut | SH-8: the presenter using the device in the room | 2–6 s; captions only | RS-STORY context, "so I'm sitting there…" | B-1 | SH-8 |

**A-roll**
| ID | Name | Type | On screen | Motion recipe | When | Family / class | Needs |
|---|---|---|---|---|---|---|---|
| **P-14** | Talk | cut | SH-1: the presenter, device in hand | 0.8–5.0 s; Z-2 push-drift on holds > 3 s | Setup, opinion, why | B-1 | SH-1 |
| **P-15** | Point | cut | The presenter holds up or points at the device on "this / look / here" | The next cut is a T-WHIP into the device | The line before a device beat | B-1 | SH-1 |
| **P-16** | Reaction | cut | SH-9 or a natural A-roll reaction (laugh, disbelief, wince) | 0.8–2.0 s; optional Z-3 snap-punch (≤ 2 per reel) | After a result; tone `joke` | B-1 / B-11 | SH-9 |
| **P-17** | Jump Cut | cut | The A-roll with a pause removed | Hard cut on the word boundary; no reframe | Every pause ≥ 150 ms inside an A-roll run | B-1 | — |

**State, marks and chips**
| ID | Name | Type | On screen | Motion recipe | When | Family / class | Needs |
|---|---|---|---|---|---|---|---|
| **P-18** | Counter Label | state | "{Label}: {n}" (§5.4), centred cx 540, cy = caption cy − 120, fixed-width box | In 8 f (rise 24 px + fade, scale 0.9 → 1) on the first op; persists across every cut; out 8 f fade. z6, `text_class: "TC-display"`, events at every op | RS-COUNT, from repetition 1 | B-6 / TC-display | state var `count` |
| **P-19** | Counter Tick | state event | The value changes 1–2 f after the op's cut | **Odometer roll**: only the digits that change move; the old digits slide up and out of a clipped box while the new ones rise in from one line below, 4 f, ease-out; the label never moves; no scale bump, no flash (v03 @ 40.30–40.40, 40.80–40.87) | Each counted repetition, ±3 f of its result | B-6 | op |
| **P-20** | Counter Jump | state event | Skipped repetitions: 5 → 7 on the cut | One roll straight to the new value; never rolls through skipped values, never counts down | A repetition not shown | B-6 | op |
| **P-21** | Final Run (step punches) | state event + footage-treatment | The last 4–6 repetitions on one locked-off clamp take: each repetition is a hard **step punch** (+6 to +23 % scale, about the screen, no easing) with a counter tick, every 0.5 s (v03 @ 40.23–42.77: 1.00 → 1.10 → 1.16 → 1.43) | Steps on the cut frame; the tick rolls 1–2 f later; the counter exits 8 f before P-12 | RS-COUNT finale, the run-up to the TURN | B-6 / B-2 | ops, SH-5 |
| **P-22** | Setting Chip | overlay | §5.4 chip naming the setting or spec ("Snooze: 9 min", "Burst: 600") | Pop 7 f (scale 0.8 → 1.04 → 1); hold ≥ 1.2 s; out blur 5 f. z5, cy 250, POV only | The UI text is too small to read; a spec is named | B-7 / TC-label | — |
| **P-23** | Message Bubble | overlay (created UI) | §5.4 bubble with avatar initials, the message text, "Name · time" | **Flies out of the device**: starts as a 12 px-high sliver at the device screen, stretches sideways toward its resting x with a horizontal motion blur 16 → 0 px while its height opens, over 6 f (ease-out); the avatar lands last (f5); then it drifts with the footage (`follow_footage: true`: the scene rides the footage transform, drawn in footage px); out fade 6 f. z5, bubble band y 1060–1300, x from 80; ≥ 40 px clear of the face (v01 @ 5.18–5.38) | Someone's message, DM or email is read out | B-8 (or B-9 via `fx.shot`) / TC-label | insert record |
| **P-24** | Notification Drop | overlay (created UI) | §5.4 banner at y 150–330 | Slides from y −200 to 150 over 10 f (expo-out); hold ≥ 1.5 s; out up 8 f. z5 | An alert, reminder or app notification is the point | B-8 / TC-label | insert record |
| **P-25** | Verdict Chip | overlay | "WORKS ✓" (`good`) / "FAILS ✕" or "NOPE" (`bad`) | Stamp-in 5 f (scale 1.4 → 1, rotate −4° → 0); hold ≥ 1.0 s; fade 5 f. z6, counter band when no counter is up, else cy 250 on POV | A test result, a comparison winner (≤ 3 per reel) | B-6 / TC-label | — |
| **P-26** | Tap Ripple | annotation | Two concentric `highlight` rings, 5 px, at the finger's touch point | Ø 40 → 160 px over 10 f, opacity 0.9 → 0, the second ring 3 f later. z6 | A tap or press that matters (≤ 1 per 3 s) | B-5 | anchor (tap point) |
| **P-27** | Loupe | annotation | A Ø 360 circle with a 6 px `paper` ring and a soft shadow, showing the POV frame at 1.8× around a UI point; placed on the opposite side of the point, never covering it | Pop 7 f; hold ≥ 1.2 s; out 5 f. z5 | Tiny UI text is the point (H13) | B-5 | anchor; a 4K POV or the SH-7 recording |
| **P-28** | Two Devices | cut | Both devices in one POV frame (two hands, or side by side on the desk) | Captions only; P-25 on the winner | A comparison ("old vs new") | B-2 | SH-2 |

**Comedy, inserts and end**
| ID | Name | Type | On screen | Motion recipe | When | Family / class | Needs |
|---|---|---|---|---|---|---|---|
| **P-29** | Sticker | overlay (comedy light) | One emoji, 140 px, 8 px white outline, beside the face (never on the face or the device) | Pop 6 f (0 → 1.2 → 1), wobble ±3° over 10 f. z9 | A self-aware joke (≤ 1 per reel) | B-11 | joke tone |
| **P-30** | Cut to Black | transition pass | Full-frame black | Hard cut to black on the last word's end (+2 f); 0–3 f of pure black before the card starts building (v01 @ 22.42) | Into the end card only | B-12 | — |
| **P-31** | Logo Plate | overlay (created insert) | `VEOS.fx.logoPlate`: another product's or company's name set in type (never its logo) | Built-in rise; ≤ 2.5 s; on POV at y 200–520 or on L-device-dim | The script names a product or brand that isn't the creator's device on screen | B-8 / TC-label | insert record |
| **P-32** | End Card | brand | §25: black, the wordmark, an artwork band, the CTA line | Builds in over ≈ 14 f (§25); holds; exit smear 5 f; ≤ 5 s; hard end | CTA `end_card`, `comment_keyword`, `link_bio` | B-10 / TC-display | `kind: "end-card"` |
| **P-33** | Keyword Chip | brand | "Comment" + the keyword chip on the end card (or "Link in bio") | Pops 0.3 s after the card (7 f); ≥ 1.5 s. z6, `kind: "cta-keyword"` | CTA `comment_keyword` / `link_bio` | B-10 / TC-display | BV-08 |
| **P-34** | Headline Card | overlay (created insert) | `VEOS.fx.headlineCard`: outlet name set in type, the exact headline from the script, a highlight bar on the spoken phrase | Built-in rise; ≤ 3 s; on L-device-dim (the A-roll dimmed behind it) | The script quotes a news story or a maker's claim | B-8 / TC-label | insert record |

### 8.4 Line → pattern lookup `[NICHE]`
| Line type | Primary | Alternates | [NICHE: example] phones and apps | [NICHE: example] kitchen and home gadgets |
|---|---|---|---|---|
| Hook claim or question | P-01 or P-02 + P-03 → T-WHIP | P-04 | "What they don't tell you about your phone" | "The air fryer button nobody presses" |
| A feature, setting or button is named | P-06 | P-08, P-22 | "There's a setting called Back Tap" | "There's a shake reminder in the settings" |
| An action on the device | P-06 / P-09 + P-26 | P-07 | "Hold the space bar" | "Press the dial twice" |
| A number shown on the device | P-06 with the number on screen | P-22 (with the number), P-27 | "Bursts are capped at 600" | "It goes up to 230 degrees" |
| A tiny on-screen detail | P-08 | P-27 | "The clock icon actually ticks" | "The display shows the exact grams" |
| A counted repetition | P-07 + P-19 | P-06 + P-19 | "Edit number five" | "Batch number five" |
| Repetitions skipped | P-20 on the cut | — | "…and seven" | "…and twelve" |
| The result / the answer | P-21 run → P-12 | P-25 | "This is twenty edits later" | "Twenty rounds, still crushing" |
| Opinion, why it matters | P-14 | P-15 | "That's genuinely useful" | "That saves you a whole step" |
| Reaction or joke | P-16 | P-29 (≤ 1) | "I look like a cartoon now" | "My kitchen smells like a campfire" |
| A comparison of two devices | P-28 + P-25 | P-06 ×2 (G-3) | "Old phone vs new phone" | "Cheap blender vs expensive one" |
| Works / fails verdict | P-25 | — | "It works" | "It failed" |
| Someone's message read out | P-23 (or B-9 `fx.shot`) | P-24 | "My friend texted me…" | "The machine sent me an alert" |
| A notification or alert | P-24 | P-06 (filmed) | "I got this notification" | "The app pinged me" |
| Another product or brand named | P-31 | — | "Unlike that other brand…" | "Like the famous one…" |
| A news story or maker's claim | P-34 | P-31 | "The maker says it's the fastest ever" | "The box says 1,000 watts" |
| Scene-setting (where, when) | P-13 | P-14 | "So I'm on a train" | "So I'm making breakfast" |
| CTA / end | P-30 → P-32 (+ P-33) | hard end | — | — |

### 8.5 Data and truth rules
- No data module: numbers are the device's own readings, the counter, or spoken specs on a chip.
- The counter counts repetitions that happened in the footage (H11, §17.1).
- Specs on chips are copied from the device screen or the script, with units.
- Recreated UIs and drawn phones (NC-6); they never show numbers the script doesn't state.

### 8.6 Comedy layer (light)
- **Where:** `joke` beats only, about every 8–12 s at most.
- **What:** a reaction shot (P-16), a self-aware line to camera, a Z-3 snap-punch (≤ 2 per reel), one sticker (P-29, ≤ 1 per reel).
- **Never:** meme sounds (comedy is `light`), stamps, freeze-frames, marker scribbles, or anything on the device screen.

### 8.7 Asset rules
- Real captures first: the creator's own device, filmed by the creator (B-2), with native recordings (B-3) as backup.
- Mocks only as fallbacks (P-11), generic and unbranded, labelled.
- No stock footage, no promo renders, no fetched logos (logo plates are type).
- Third-party moments follow ask-then-create (§12.5).
- Blur personal data on device screens (H16).

### 8.8 Density and variety
- 30–60 events per 60 s (captions included).
- ≥ 8 distinct patterns per 60 s in RS-LIST; RS-COUNT may run its repetition ritual (P-07 + P-19) back to back.
- The same POV pattern at most 3 times in a row outside the RS-COUNT ritual.
- ≤ 1 overlay (chip, ripple, loupe, ring, verdict) per POV shot.

---

## §9 Transitions and shot grammar `[REQ] [DNA]`

### 9.1 Library
Measured at 30 fps (v02, v03 bursts; `docs/audit/device-whip/strip-*.jpg`). f0 = the cut frame.
| ID | Transition | Frames | Recipe | Cue role |
|---|---|---|---|---|
| **T-WHIP** | Zoom-flash whip (into the device, or back out to the face) | 10 | f−4…f−1: the outgoing shot zooms 1.0 → 1.6 **about the device point** (ease-in: ≈ +2 %, +2 %, +11 %, +16 % per frame) and brightens; A-roll out = camera Z-1 `zoom-through` (7 f) with `p.origin: {x, y}` = the device point, POV out = the clip scene's own scale about the same point. f−2…f+1: footage radial blur at the device point (`amount` 0.3), the picture fully blurred. f0: stage `cut`; the incoming shot lands at 1.15 → 1.00 with a footage defocus 14 → 0 px and the flash 28 → 0 % over 3 f. Sharp on f+3. Captions hidden on the 3 peak frames. Timeline: §17.4 | whoosh / zoom (transitions) |
| **T-WHIP-S** | Spin whip | 7 | Built in: `{"t": <cut>, "type": "whip", "angle": 60, "frames": 7, "pre": 3, "px": 120, "travel": 880}` (diagonal smear, ≈ 620 px/f at the peak, a 2 f cross-blend, the incoming shot smears in from the other side) + Z-5 `rotation-snap` 5° in 3 f before the cut on an A-roll out (`p.origin` the device point). No flash (v02 @ 1.30–1.57, 29.73–30.03) | whoosh (transitions) |
| **T-WHIP-L** | Linear whip | 6 | Built in: `{"t": <cut>, "type": "whip", "dir": "left", "frames": 6, "pre": 3, "px": 60, "travel": 480}` (the frame slides sideways with a horizontal smear, 160 px/f; `dir: "right"` for the reverse) + a 30 % darkening `VEOS.fx.flash({at: <cut> − 3/30, up: 3, hold: 0, decay: 3, color: "#000000", peak: 0.3, z: 6})` (under the captions); hard cut at f0; captions stay up (v02 @ 5.27–5.43, 24.37–24.50) | swish (transitions) |
| **T-CUT** | Hard cut | 0 | On the word boundary ±1 f | silent |
| **T-MATCH** | Match-motion cut | 0 | A hard cut where the A-roll hand reaching for the device meets the POV hand entering the frame (± 2 f of the reach) | silent |
| **T-JUMP** | Jump cut | 0 | Inside the A-roll on a pause ≥ 150 ms; same framing | silent |
| **T-BLACK** | Cut to black | 0 + ≤ 3 black | P-30 hard cut to black, then the end card builds in (§25) (v01 @ 22.42) | none (the CTA cue sits on the card) |
| **T-DIM** | Dim to drawn phone | 8 | Stage `via: dim`; P-11 rises over 10 f | soft whoosh (fallback only) |

### 9.2 Grammar
| Boundary | Use | Never |
|---|---|---|
| f0 | No transition: open on live footage + the Z-4 punch and title pop (H-A) or the lunge (H-B) | A fade-in or a black first frame |
| Hook → first POV | **T-WHIP-S** (hand-held device) or **T-WHIP** (clamp) by 2.5 s | A hard cut |
| A-roll → POV, opening an item | a whip (rotate kinds) | Two whips within 2.5 s |
| A-roll → POV inside an item | T-CUT or T-MATCH | Any blur |
| POV → A-roll, the item's result just shown | a whip-out (G-2b): T-WHIP, T-WHIP-L or T-WHIP-S | — |
| POV → A-roll, mid-item | **T-CUT** on the first word of the sentence | A whip |
| POV → POV | T-CUT (G-3) or a P-21 step punch | Any blur |
| Repetition → repetition (RS-COUNT) | T-CUT; the finale as P-21 step punches | A whip (save it for the first repetition, a reaction exit and the TURN) |
| Into the TURN (result) | T-WHIP | — |
| Last word → end card | T-BLACK | A fade; a black tail > 0.2 s |
| CTA `none` | Hard end ≤ 6 f after the last word | — |

### 9.3 Shot grammar `[COND: spine hybrid]`
| ID | Rule |
|---|---|
| **R-1** | Alternate face and device every 1–4 s; never > 5.0 s on either (H4). |
| **R-2** | Cut to the device on the trigger word (lead 2 f): the feature noun, the action verb, the number. |
| **R-3** | Cut back to the face on the first word of an opinion, a reaction or a joke. |
| **R-4** | Two POV takes in a row must differ (another action, angle or macro), never the same framing twice. |
| **R-5** | Use T-MATCH when the A-roll hand reaches toward the device and a POV take starts with the hand entering (v03 @ 0:02.5). |
| **R-6** | Jump cuts (T-JUMP) remove every A-roll pause ≥ 150 ms; the framing stays (no punch reframes). |
| **R-7** | The TURN (result) is the longest POV of the reel (2–5 s) and is followed by a face reaction. |
| **R-8** | The reel's last shot is the face (a reaction or the last line) or the end card, never a POV mid-action. |

### 9.4 Budget (per 60 s; scale by duration)
- Whips (all kinds, the hook one included): **6–11 in RS-LIST** (v02: 7 in 37 s, 39 % of boundaries), **4–6 in RS-COUNT** (v03: 3 in 45 s), 1–3 in RS-STORY (v01: none; its end card carries the motion). Never two within 2.5 s; rotate kinds (zoom-flash ≈ 45 %, spin ≈ 30 %, linear ≈ 25 %); the same kind never 3× in a row.
- The flash lift only on T-WHIP, so ≤ 1 flash per 2.5 s. T-BLACK 1 (end card only). T-DIM only with fallbacks.
- At least one T-MATCH per reel when the footage allows it.
- Everything else is T-CUT / T-JUMP / P-21 step punches.
- Cuts sit on word boundaries ±1 f; the audio is never offset.

---

## §10 Motion, camera, layers, finishing `[REQ] [DNA; motion tokens TUNE ±15%]`

### 10.1 Motion tokens (30 fps)
| Token | Value |
|---|---|
| Beat lead | 2 f before the onset |
| Entries | `cubic-bezier(0.22, 1, 0.36, 1)` (expo-out) |
| Exits | `cubic-bezier(0.64, 0, 0.78, 0)`, 3–8 f |
| Title pop / swap | 2 f (scale 0.70 → 1, h-blur 12 → 0 px) / 2 f blurred crossover (new 0.85 → 1) |
| Whips | T-WHIP 4 out + 3 peak + 3 land (1.6×, flash 28 %); T-WHIP-S 7 f (5° roll); T-WHIP-L 6 f |
| Ring sweep | 9 f bottom → top, segment 45 % of the outline height, no hold |
| Tap ripple | 10 f (Ø 40 → 160), second ring +3 f |
| Counter | in 8 f; tick = odometer roll 4 f (digits up, ease-out); out 8 f |
| Bubble | flies out of the device 6 f (sliver → full, h-blur 16 → 0 px), drifts with the footage (`follow_footage: true`) |
| Chip pop | 7 f; verdict stamp 5 f |
| POV push | `kenburns` 1.00 → 1.06 (standard) / 1.08 (> 2.5 s) / 1.10 (TURN) / 1.12 (macro) |
| POV snap / step | 1.00 → 1.25 in 6 f, hold (P-10b) / +6–23 % hard steps every 0.5 s (P-21) |
| End card | build 14 f; exit smear + zoom blur 5 f |
| Holds | Text ≥ 0.25 s per word; titles ≥ 10 f after built |

### 10.2 Footage camera (`zoom_policy: presets`)
| ID | Preset (engine name) | Recipe | Use |
|---|---|---|---|
| **Z-4** | `crash-zoom` | 1.0 → 1.4 over f1–f5 (ease-out: ≈ +6, +11, +10, +9, +1 % per frame), held to the hook whip; the f0 frame is the motion-blurred swing (v02 @ 0.03–0.17) | H-A f0 only (1 per reel) |
| **Z-1** | `zoom-through` | 1.0 → 1.6, 7 f, ease-in, ends on the cut | Only inside T-WHIP (A-roll out) |
| **Z-5** | `rotation-snap` | 5° roll in 3 f | Only inside T-WHIP-S (A-roll out) |
| **Z-2** | `push-drift` | 1.00 → 1.05 over the beat | A-roll holds > 3 s |
| **Z-3** | `snap-punch` | 1.00 → 1.15 in 3 f, motion blur f1–2, hold to the next cut | A joke reaction (≤ 2 per reel); FB-3's hold-up substitute |
| **Z-0** | `reset` | back to 1.0 in 4 f | Written on every return cut after a whip, so two whips are never consecutive camera events |

Rules: never the same preset twice in a row (write Z-0 on the return cut after each whip); never two camera moves within 0.4 s; camera presets move the A-roll only (POV clips move by their own `kenburns`, P-10b snap and P-21 steps). Whip zooms pivot on the device point (`p.origin: {x, y}` on Z-1 / Z-5, or `"device"` with `timeline.canvas_nodes.device` when one device position serves the reel) and the radial blur is centred there, so the read is "into the device", not "into the face". Measured: no continuous digital push on the A-roll; its scale drifts are the presenter and the hand-held camera (live motion is the motion).

### 10.3 Canvas camera
OFF (§21).

### 10.4 Layer order (back to front)
1. W-void / W-studio (z1)
2. POV clip scenes (z2, full-bleed, under a `hidden` stage)
3. Drawn phone (P-11, z5 on L-device-dim) above the dimmed footage
4. A-roll footage (stage)
5. Chips, bubbles, notification, logo plate, headline card, loupe (z5)
6. Counter, verdict chips, ring, tap ripples, CTA chip (z6)
7. Captions (z7)
8. Sticker (z9)
9. Title (z10)
10. The black of P-30 (z11). Whip blur, smear and flash are drawn by core over the picture (under the captions), not as scenes

### 10.5 Finishing
- No grain, no vignette, no LUT.
- Glow only on the ring and the tap ripples.
- Hard shadows only on the title (extrusion); soft shadows on captions, bubbles and chips.
- Exposure and white balance matched between A-roll and POV; nothing else.

---

## §11 Sound contract (minimal) `[REQ] [VAR]`
Sound comes from the bundled SFX pack and its global rules (S1–S6).

| Line | Decision |
|---|---|
| **Cue moments** | `hook` (one cue on the title entry or the ring), `transitions` (every whip: whoosh on T-WHIP and T-WHIP-S, swish on T-WHIP-L; hard cuts and step punches are silent), `reveals` (the ring, the TURN result, a verdict chip), `list_cue` (one tick file for counter ticks: at most one tick cue per `REP-n` section), `cta` (the end card) |
| **Meme cues** | off (comedy `light`) |
| **Music bed** | on; enters on the hook whip landing |
| **Ducking** | the bed sits ≥ 18 dB under the voice while the voice speaks; POV clips are muted (the A-roll voice carries); a POV take cut in as an EDL segment keeps its own voice |
| **Loudness** | −14 LUFS integrated, true peak ≤ −1.5 dBTP; hard end ≤ 6 f after the last word (NC-8) |

Mirrored in `tokens.json → sound`.

---

## §12 Footage, shot list, fallbacks, inserts `[REQ]`

### 12.1 Setups `[DNA what the style assumes; VAR the buyer's setups]`
| Setup | Camera | Framing | Set and light | Notes |
|---|---|---|---|---|
| **A: A-roll** | Main camera on a tripod, 4K, 30 fps (or 60 conformed), vertical | Eye level or slightly low; head top y 160–320; chest and hands in frame so the device shows | Shallow depth of field (f/1.8–2.8); soft coloured practicals or a warm shelf behind, 1.5–3 m back; soft key 45° | Lav mic allowed (visible in all three evidence reels); plain or textured top, no logos |
| **B: POV** | A second camera or a phone at chin height looking down at the device in one hand | Device screen 40–65 % of frame height, centre x 380–700, centre y 700–1000 | The same set, blurred | Muted; the A-roll voice carries it |
| **C: Clamp** | The device on a clamp or monopod at chest height; a locked-off camera on it | Screen 45–80 % of frame height | Same set | For the lean-in hook (SH-4) and repetitions (SH-5) |

### 12.2 Shot list `[DNA]`
| ID | Shot | Spec | Count per 60 s | Must / optional |
|---|---|---|---|---|
| **SH-1** | A-roll talking head | Setup A, device in hand | 6–12 runs | must |
| **SH-2** | Hand-held device POV | Setup B, one take per feature, 2–6 s, hold still 1 s before and after the action | 4–9 | **must** |
| **SH-3** | Hold-up | Device swung toward the lens in ~0.3 s, held still 1.5–2 s at 30–40 cm, face soft behind, device bottom above y 1210 | 0–1 | optional (H-A) |
| **SH-4** | Lean-in | Device on its clamp; the presenter leans in from camera-left, face in the top half | 0–2 | optional (H-B) |
| **SH-5** | Clamp POV | Setup C locked off, one take per repetition, 1–3 s | 0–12 | optional (RS-COUNT) |
| **SH-6** | Macro detail | Icon, port, button or texture, tilted 15–25°, slow forward move 3–4 s | 0–2 | optional |
| **SH-7** | Screen recording | Native recording of every UI step | 0–4 | optional (backup) |
| **SH-8** | Wide context | Presenter using the device in the room, 3–7 s | 0–1 | optional (RS-STORY) |
| **SH-9** | Reaction bank | Laugh, disbelief, wince, shrug, 1–2 s each | 0–2 | optional |

**POV capture checklist** (give this to {{BV-01.name|the creator}} before the shoot):
- **C-1** Clean the screen and the lens. Peel off a glossy screen protector if it glares.
- **C-2** Do Not Disturb on, notifications hidden, a demo contact name; nothing personal on screen (H16).
- **C-3** Screen brightness 70–85 %, auto-brightness off, night-shift/true-tone off; dark mode only if the reel is about it.
- **C-4** POV camera: the same frame rate as the A-roll; shutter 1/60 at 30 fps (1/50 in 50 Hz countries) so the screen doesn't band; expose for the screen (about −0.7 EV) so white UI isn't clipped; focus locked on the screen.
- **C-5** Framing: vertical 9:16, 4K if possible; the screen fills 40–65 % of frame height with its centre at x 380–700, y 700–1000; UI you need to read stays above y 1340 (the caption band).
- **C-6** Background: the same set as the A-roll, blurred (f/2–2.8). Hand and wrist enter from a bottom corner.
- **C-7** One feature = one take: hold the device still for 1 s, do the action at normal speed, hold 1 s on the result. Then do it once more, slower.
- **C-8** Count-ups: lock the POV camera on the clamped device; identical framing for every repetition; one file per repetition.
- **C-9** Hook hold-up: swing the device from your chest toward the lens in about 0.3 s, stop 30–40 cm away, hold 2 s; your face behind at f/2 so it's soft; keep the device's bottom edge above the lower third.
- **C-10** Lean-in: device on a clamp at chest height, lean in from camera-left, face in the top half of the frame.
- **C-11** Macro: tilt 15–25°, push in slowly for 3–4 s, focus on the detail.
- **C-12** Also screen-record every UI step natively (SH-7) as a backup for legibility.
- **C-13** Name files `item01_pov_a.mp4`, `item01_pov_b.mp4`, `rep07_clamp.mp4`, `hook_holdup.mp4` so the inventory (P1b) is instant.
- **C-14** POV takes are silent inserts under the A-roll voice. If you talk while filming the POV, keep the mic on you: that take can be cut in as its own segment.

### 12.3 Fallbacks
| ID | For | What the engine does instead | Fidelity cost | Result |
|---|---|---|---|---|
| **FB-1** | SH-2 | The SH-7 screen recording inside the drawn phone (P-11), tilted −6° with a slow float, over the dimmed A-roll (L-device-dim) | No real hand or device: the POV feel and believability are lost | degraded |
| **FB-2** | SH-2 (no recording either) | A recreated generic UI (`fx.appUI`) inside the drawn phone, for at most 2 beats per reel | The reel shows a mock, not the device | degraded |
| **FB-3** | SH-3 | SH-1 with the device in hand + the title; the whip starts after a Z-3 snap-punch | Less depth in the hook | holds |
| **FB-4** | SH-4 | SH-1; the ring is skipped and the hook is H-A | No lean-in energy | holds |
| **FB-5** | SH-5 | SH-2 hand-held takes, one per repetition | Less consistent framing between repetitions | holds |
| **FB-6** | SH-6 | A 1.35× crop of an SH-2 take with P-08's push (more needs a 4K source) | No macro texture | degraded |
| **FB-7** | SH-8 | Skip the wide; stay on SH-1 | None worth noting | holds |
| **FB-8** | SH-9 / SH-1 extras | The nearest natural reaction in the main take | Fewer reaction beats | holds |

**Rule:** a reel whose device beats are > 50 % FB-1/FB-2 is flagged at the checkpoint ("the device-whip look needs your POV shots; this reel will read as a screen-recording explainer").

### 12.4 Props, reaction bank, matte, resolution
- **Props:** the device; a phone clamp or monopod; a second camera or phone for the POV.
- **Reaction bank (SH-9):** laugh, disbelief, wince, shrug.
- **Matte:** none.
- **Resolution:** a 1.35× punch needs ≥ 1080 × 1920; a 2× crop (P-27 loupe on a POV) needs a 4K POV, else use the SH-7 recording inside the loupe.

### 12.5 Third-party inserts: ask, then create `[REQ always]`
The creator's own device, filmed by the creator, is creator footage, not an insert. Third-party moments in this style are usually: a message someone else sent, a notification from another service, a news story or a maker's claim, another brand's product, another creator's video.
1. **Analyse** the transcript (`veos inserts scan`) and list those moments.
2. **Ask once:** "For these N moments, do you have a screenshot or clip? (drop the files, or say no)".
3. **Supplied:** show it as given with `VEOS.fx.shot` (cropped, framed, highlighted), never altered.
4. **Not supplied — create:**
   - a message → P-23 bubble (`quote_card` recipe; the exact words from the script; initials, never a photo);
   - a notification → P-24 (`recreated_ui`, generic glyph);
   - a news story or maker's claim → P-34 (`headline_card`, exact headline from the script);
   - another product or brand → P-31 (`logo_plate`, name set in type);
   - another creator's video → `fx.appUI({kind: "video"})` on L-device-dim;
   - a person → `fx.silhouette`.
5. **Record** each in `plan/inserts.json` `{id, moment, origin: creator | created, file?, substitute_of?}`.

### 12.6 Frame rate and audio
- 30 fps CFR out; conform VFR phone POVs; 1080 × 1920.
- One voice: the A-roll mic (high-pass 80 Hz, de-ess, compression, −14 LUFS). POV video assets carry no sound into the mix.

---

## §13 Output contract `[REQ] [DNA]`

### 13.1 Beat fields (the first `yaml` block of the edit brief)
```yaml
- id: 7
  section: ITEM-2                 # HOOK | ITEM-n | REP-n | TURN | END
  t0: 7.40
  t1: 10.80
  spoken: "tap the back of your phone twice"
  trigger: {word: "tap", at: 7.52}
  tone: explain                   # hype | explain | awe | win | warn | joke | cta
  line_type: action_on_device     # §8.4
  layout: L-pov                   # L-full | L-pov | L-device-dim | L-endcard
  visual: "POV: two finger taps on the back of the phone, the screenshot thumbnail flies into the corner; ripple on the second tap"
  layers: [pov-07, ripple-07]
  pattern: P-06
  transition_in: T-WHIP           # T-WHIP | T-WHIP-L | T-CUT | T-MATCH | T-JUMP | T-BLACK | T-DIM
  camera: zoom-through            # Z preset name or null
  sfx: [{t: 7.38, id: "<catalog id>", beat: 7, on: "transition@7.38", why: "whip into the device"}]
  caption: {profile: CS-1, overrides: []}
  shot_id: SH-2
  fallback_used: null             # FB-n when a fallback replaced the shot
  state_ops: []                   # RS-COUNT: [{var: count, op: add, value: 1, at: 9.96}]
  anchor: {target: "region", box: {x: 380, y: 760, w: 0, h: 0}, follow: none}   # tap point for P-26
  insert: null                    # {id: I1, origin: creator | created}
```

### 13.2 Conditional fields
| Switch / module | Beat fields |
|---|---|
| captions | `caption {profile, overrides[]}` (no emphasis in this style) |
| running_state | `state_ops [{var: count, op: add \| set, value, at}]` |
| anchors | `anchor {target: object:device \| region, box {x, y, w, h, r} \| point, follow: none}` |
| footage ≥ medium | `shot_id`, `fallback_used` |
| third-party moment | `insert {id, origin}` |
| brand | `sponsor {id, disclosure}` (only when sponsored) |

### 13.3 Reel header
```yaml
meta:
  format: F-A
  shape: RS-COUNT                 # RS-LIST | RS-COUNT | RS-STORY
  hook_archetype: HA-17           # or HA-02 | HA-10 | HA-14
  hook_variant: H-B               # H-A | H-B (HA-17 only)
  structure: list
  caption_y: mid                  # rule CY: low = 1400, mid = 1270 (written to tokens.override.json patch)
  count: {var: count, label: "Batches", final: 20}   # RS-COUNT only
  keyword: null                   # BV-08 keyword when the CTA is comment_keyword
  cta: end_card                   # end_card | comment_keyword | link_bio | none
  fallbacks: []                   # FB ids used anywhere in the reel
```

### 13.4 Hook proposals (3 required)
```yaml
- name: "Title whip: hidden phone tricks"
  archetype: HA-17
  variant: H-A
  title: ["WHAT THEY", "DON'T TELL YOU", "ABOUT YOUR PHONE"]   # = the spoken line, 8 words
  hook_pair: {subject: "phone held up to the lens", reveal: "POV: space-bar trackpad", reveal_by_s: 2.3}
  stoppers: [P-04 hold-up, P-01 title, P-03 ring, T-WHIP]
  storyboard: "f0 hold-up + phrase 1 | 0.4 ring | 0.5 phrase 2 | 1.25 phrase 3 | 2.0 zoom-through + radial blur | 2.27 POV lands"
  sound: [hook cue on the title, whip cue]
  stopper_test: {thumbnail: pass, mute: pass, read_s: 2.0, changes_3s: 6.5, payoff_s: 2.27}
```

### 13.5 Checkpoint (before building)
1. 3 hook proposals with stopper-test results.
2. The beat sheet with tones, layouts and shot ids, and the **shot-pairing table** (sentence → A-roll / POV take).
3. The transition map (every T-… with its frame) and the camera list (Z-1 / Z-0 pairs).
4. The SFX cue list (cue moments only).
5. The count plan (label, ops, final value) and the anchor boxes.
6. The caption y decision (rule CY) with its overlap numbers.
7. The inserts record (creator-supplied vs created) and the fallbacks used, with the > 50 % fallback flag if it applies.
8. Style stills: f0, the whip landing, one POV beat with captions, one counter tick (RS-COUNT), the TURN, the end card.

**Wait for approval.**

---

## §14 Worked examples `[REQ] [NICHE]`
Times are estimates; replace them with `words.edit.json` onsets.

### 14.1 RS-LIST, HA-17 H-A, [NICHE: example] phones: "What they don't tell you about your phone"
**Footage:** SH-1 A-roll; SH-3 hold-up; SH-2 POV × 6 (space-bar trackpad, Back Tap, calculator swipe, burst counter, two takes of Back Tap settings); SH-6 macro of the shutter. **Caption y:** `low` (1400): every POV keeps the screen above y 1300. **CTA:** `end_card`. **Duration:** ~34 s.

**Hook table**
| t (s) | Spoken | Tone | Visual | Text | Layout / camera | Cue |
|---|---|---|---|---|---|---|
| 0.00 | "What they" | hype | SH-3 phone swinging up to the lens; Z-4 open punch 1.0 → 1.4 | P-01 "WHAT THEY" pops in f1–f2 | L-full, camera | hook |
| 0.40 | — | hype | P-03 sweep up the held phone (still from 0.3 s) | — | — | — |
| 0.50 | "don't tell you" | hype | — | "DON'T TELL YOU" | — | — |
| 1.25 | "about your phone." | hype | — | "ABOUT YOUR PHONE" | — | — |
| 2.00 | — | hype | T-WHIP-S: Z-5 roll + diagonal blur pass; the title blurs away | — | camera | transitions |
| 2.20 | "Hold the space bar" | explain | **T-WHIP-S** → P-06: thumb on the space bar, the keyboard turns into a trackpad | captions on | L-pov | — |

**Section plan**
| Section | t (s) | Spoken (gist) | Tone | Layout | Pattern | Transition in | Overlay |
|---|---|---|---|---|---|---|---|
| ITEM-1 | 2.2–4.9 | "Hold the space bar and the keyboard becomes a trackpad" | explain | L-pov | P-06 + P-10 | T-WHIP-S | P-26 ripple on the press (2.5) |
| ITEM-1 | 4.9–6.6 | "Fixing typos is so much faster" | win | L-full | P-14 | **T-WHIP-L** out (G-2b) (+ Z-0) | — |
| ITEM-2 | 6.6–7.4 | "Next one:" | hype | L-full | P-15 (holds the phone up) | — | — |
| ITEM-2 | 7.4–10.8 | "Tap the back of your phone twice… it takes a screenshot" | explain | L-pov | P-06 | T-CUT | P-26 on the 2nd tap |
| ITEM-2 | 10.8–13.0 | "You'll find it under Back Tap in the settings" | explain | L-pov | P-09 (scroll to the setting), 2nd take | T-CUT (G-3) | P-22 "Back Tap" |
| ITEM-2 | 13.0–14.6 | "I set mine to the flashlight" | joke | L-full | P-16 (a grin) | T-CUT (+ Z-0) | — |
| ITEM-3 | 14.6–17.8 | "Typed a wrong digit? Swipe the calculator display" | explain | L-pov | P-06 | **T-WHIP** | — |
| ITEM-3 | 17.8–19.4 | "No more clearing everything" | win | L-full | P-14 | T-CUT (+ Z-0) | — |
| ITEM-4 | 19.4–20.4 | "And the best one:" | hype | L-full | P-15 | T-WHIP-L at 19.4 | — |
| ITEM-4 | 20.4–23.4 | "Slide the shutter left and it shoots a burst" | explain | L-pov | P-08 macro of the shutter → | T-MATCH | P-10b snap on "burst" (22.6) |
| ITEM-4 | 23.4–27.6 | "…and it counts every photo" | awe | L-pov | P-12-style hold on the burst counter climbing (the number is on the device), 2nd take | T-CUT (G-3) | P-27 loupe on the counter (24.4) |
| END | 27.6–30.2 | "The attention to detail is wild." | win | L-full | P-16 | **T-WHIP** out (G-2b) (+ Z-0) | — |
| END | 30.2–30.6 | — | cta | — | P-30 cut to black | T-BLACK | — |
| END | 30.6–34.0 | — | cta | L-endcard | P-32 wordmark | — | — |

Cuts: 13 in 34 s ≈ 23 per minute (14–45 ✓); whips at 2.0 (S), 4.9 (L), 14.6 (zoom), 19.4 (L), 27.6 (zoom out): ≥ 2.5 s apart, no kind 3× in a row. Face share ≈ 38 % (✓). Longest POV run 23.4 → 27.6 split into two takes (4.2 s ✓).

### 14.2 RS-COUNT, HA-17 H-B, [NICHE: example] kitchen gadgets: "Can a $30 blender crush ice twenty times in a row?"
**Footage:** SH-4 lean-in (blender on the counter, presenter beside it); SH-5 locked-off top-down POV into the jar, one file per batch (20 files, 14 used); SH-1 A-roll; SH-9 reactions. **Caption y:** `mid` (1270), because the blender's control dial sits in the low band (y 1360–1480) of the SH-5 frame (rule CY: low 61 % overlap, mid 9 %). The counter therefore sits at cy 1150. **Counter:** `count`, label "Batches", final 20. **CTA:** `comment_keyword`, keyword BLENDER. **Duration:** ~44 s (re-hook at 22 s).

**Hook table**
| t (s) | Spoken | Tone | Visual | Text | Layout / camera | Cue |
|---|---|---|---|---|---|---|
| 0.00 | "Can a thirty-dollar blender" | hype | SH-4 lean-in; P-03 sweep up the blender at 0.3 s (still on the counter), `kind: "device"` | chunk "Can a $30 blender" | L-full | hook |
| 0.90 | "crush ice" | hype | — | chunk "crush ice" | — | — |
| 1.30 | — | hype | Hand presses the pulse button: P-26 ripple | — | — | — |
| 1.60 | "twenty times in a row?" | hype | — | chunk "twenty times in a row?" | — | — |
| 2.20 | — | hype | T-WHIP: Z-1 zoom-through about the jar + P-05 radial blur + flash lift | (hidden on the 3 peak frames) | camera | transitions |
| 2.47 | "Batch one." | explain | **T-WHIP** → P-07 top-down jar, ice shattering | chunk "Batch one." | L-pov | — |
| 3.90 | — | win | The ice turns to snow: **P-18 counter in** "Batches: 1" | — | — | list_cue |

**Section plan and state plan**
| Section | t (s) | Spoken (gist) | Layout | Pattern | Transition | State op |
|---|---|---|---|---|---|---|
| REP-1 | 2.47–5.0 | "Batch one… easy." | L-pov | P-07 | T-WHIP | set 1 @ 3.90 |
| REP-2 | 5.0–6.6 | "Two." | L-pov | P-07 | T-CUT (G-3) | add 1 → 2 @ 6.20 |
| REP-3 | 6.6–8.0 | "Three." | L-pov | P-07 | T-CUT | add 1 → 3 @ 7.60 |
| — | 8.0–10.1 | "The motor's getting warm" | L-full | P-14 (hand on the jug) | **T-WHIP** out (G-2b) (+ Z-0) | (counter stays) |
| REP-5 | 10.1–11.6 | "Five." | L-pov | P-07 | T-CUT | set 5 @ 11.20 (P-20 jump on the cut) |
| REP-6 | 11.6–13.0 | "Six, still crushing." | L-pov | P-07 | T-CUT | add 1 → 6 @ 12.70 |
| — | 13.0–15.2 | "My kitchen sounds like a building site" | L-full | P-16 + P-29 (🔨) | T-CUT | — |
| REP-10 | 15.2–17.0 | "Ten." | L-pov | P-07 | **T-WHIP** | set 10 @ 16.60 |
| REP-12 | 17.0–18.4 | "Twelve." | L-pov | P-07 | T-CUT | set 12 @ 18.00 |
| — | 18.4–22.0 | "Now let's push it all the way to twenty" (re-hook) | L-full | P-14 + Z-2 push | T-CUT (+ Z-0) | (counter stays) |
| REP-15 | 22.0–23.4 | "Fifteen." | L-pov | P-07 | T-CUT | set 15 @ 23.00 |
| REP-16 | 23.4–24.8 | "Sixteen." | L-pov | P-07 | T-CUT | add 1 → 16 @ 24.40 |
| REP-17–20 | 24.8–26.8 | "Seventeen, eighteen, nineteen… twenty." | L-pov | **P-21** step punches on one clamp take, every 0.5 s (1.00 → 1.08 → 1.16 → 1.25 → 1.40) | T-CUT | add 1 @ 24.82 / 25.32 / 25.82 / 26.32 (each a roll, P-19) |
| TURN | 26.8–31.0 | "Look at that. Snow. Every single time." | L-pov | **P-12** (jar close-up, push 1.00 → 1.10); counter out 26.6 | **T-WHIP** | — |
| TURN | 31.0–32.4 | — | L-pov | P-25 "WORKS ✓" in the counter band, on a second take | T-CUT (G-3) | — |
| END | 32.4–37.6 | "Thirty dollars. I'm genuinely impressed." | L-full | P-16 | **T-WHIP** out (G-2b) (+ Z-0) | — |
| END | 37.6–40.0 | "Comment BLENDER and I'll send you the link." | L-full | P-14 | — | — |
| END | 40.0–40.3 | — | — | P-30 | T-BLACK | — |
| END | 40.3–44.0 | — | L-endcard | P-32 + P-33 "Comment BLENDER" | — | — |

Every displayed value equals a batch shown or the jump to it (H10, H11). The counter and the title never meet (H-B has no title).

### 14.3 RS-STORY, HA-14, [NICHE: example] phones and accessories: "My phone told me I'd left my keys at the café"
**Footage:** SH-1 A-roll (phone in hand); SH-2 POV of the tracker alert on the creator's own phone; SH-8 wide of the café walk; the friend's message: the creator supplies a screenshot (else P-23 created bubble). **Caption y:** `low`. **CTA:** `link_bio`. **Duration:** ~29 s.

| t (s) | Spoken (gist) | Tone | Layout | Pattern | Transition | Notes |
|---|---|---|---|---|---|---|
| 0.00 | "So my phone just saved me forty minutes." | hype | L-full | P-14 + P-02 (chunk at f0), phone swinging in hand | — | HA-14: caption at f0 + moving footage |
| 0.90 | — | hype | L-full | P-15: phone held up to the lens (strongest image ≤ 1.0 s) | — | — |
| 2.10 | "I got this alert:" | explain | L-pov | P-06: the "left behind" alert on the creator's phone | **T-WHIP** | filmed on the creator's own device = creator footage |
| 4.6 | "'Keys left behind'" | explain | L-pov | P-27 loupe on the alert text | — | the loupe holds 1.4 s |
| 6.0 | "And then my friend texted me" | explain | L-full | P-23 bubble ("are these yours?", initials "S") in the bubble band | T-CUT (+ Z-0) | insert I1: creator screenshot via `fx.shot`, else created |
| 9.2 | "So I walked back" | explain | L-pov | P-13 wide of the café walk | T-CUT | — |
| 13.0 | "The map was spot on" | awe | L-pov | P-06: the map pin on the phone | **T-WHIP** | — |
| 16.4 | "Two tables from where I sat." | win | L-pov | P-12 hold on the found keys + phone | T-CUT (G-3) | the TURN |
| 19.8 | "Best ten-dollar thing I own." | win | L-full | P-16 | T-CUT (+ Z-0) | — |
| 22.5 | "The tracker's linked in my bio." | cta | L-full | P-14 | — | — |
| 24.9 | — | cta | — | P-30 → P-32 + "Link in bio" chip | T-BLACK | ≤ 5 s card |

---

## §15 QA checklist `[REQ] [DNA]`
**1. Profile conformance**
- [ ] Format F-A; shape declared; caption y declared (V-LAYOUT, review).
- [ ] Presenter share 35–75 %, longest absence ≤ 5.0 s (V-PRESENCE).
- [ ] Duration 28–50 s (review).

**2. Hook**
- [ ] f0: the device ≥ 15 % of frame height + the title phrase or the first caption chunk; something moving (V-F0).
- [ ] Z-4 open punch on f1–f5 (H-A); the hook whip lands by 2.5 s (V-F0).
- [ ] ≥ 5 weighted SCs in 0–3 s; hook gaps ≤ 1.25 s (V-CADENCE).
- [ ] Title: a hook (a promise the reel keeps), ≤ 9 words, 2–3 phrases, ≤ 3 words each, ≥ 0.25 s per word, 0 emoji, rides out in the whip (V-TITLE, review).
- [ ] Thumbnail test at 25 % and the mute test pass (review).

**3. Body and cadence**
- [ ] 5–10 weighted SCs per 10 s; max gap 2.5 s; nothing static > 2.5 s; 14–45 cuts/min; median shot 1.0–3.2 s (V-CADENCE).
- [ ] No A-roll or POV run > 5.0 s (V-LAYOUT).
- [ ] Every device line shows the thing on the device within ±5 f (V-ONWORD).
- [ ] Whips only on section changes (into the device or out after a result), never inside an item, never two within 2.5 s, kinds rotated; Z-0 after each whip (V-CAMERA, review).
- [ ] The best item last / the TURN is the longest POV (review).

**4. Captions**
- [ ] CS-1: one line, 3–6 words, 56 px, white, no emphasis, one y for the whole reel (V-CAPTION, V-TYPE).
- [ ] Sync lead ≤ 150 ms; device and brand names spelled exactly (V-CAPTION).
- [ ] Captions never sit on the UI being read (review, rule CY).

**5. Modules**
- [ ] Counter: appears on the first op, rolls (odometer, 4 f) ±3 f of each result, never decreases, final value = last repetition shown, constant position, gone before the TURN (V-STATE pending → review).
- [ ] Ring sweep (bottom → top, 9 f) and ripples sit on the device / tap point (anchored to a `veos track`, or a still device ≤ 20 px drift), never on the face (V-ANCHOR, V-FACE).
- [ ] End card ≤ 5 s, entered by a hard cut to black, wordmark built in ≈ 14 f; keyword ≥ 1.5 s; black tail ≤ 0.2 s (V-PROMISE).

**6. Truth and inserts**
- [ ] Counts, specs and numbers trace to the footage, the device screen or the script (review).
- [ ] Every third-party moment is creator-supplied or created and recorded; reconstructions labelled (V-INSERTS, V-CITE).
- [ ] Personal data on device screens blurred (review, NC-14).
- [ ] Fallbacks listed; > 50 % fallback beats flagged (review).

**7. Sound contract**
- [ ] Cues only on the hook, whips, reveals, counter list cue and the CTA; no meme cues; bed in after the hook (S1–S6).
- [ ] −14 LUFS, true peak ≤ −1.5 dBTP, bed ≥ 18 dB under the voice (mix gate).

**8. End and export**
- [ ] Hard end ≤ 6 f after the last word (CTA none) or the card ≤ 5 s; 1080 × 1920, 30 fps CFR (review).

---

## §16 Frame template / chrome
OFF (`profile.modules.chrome = false`): nothing persists in a fixed slot except the counter, which is running state (§17), not chrome.

## §17 Running state and anchored graphics `[COND: modules.running_state, modules.anchors] [DNA mechanics]`

### 17.1 State variable: the counter
```yaml
running_state:
  vars:
    count: {type: counter, start: 0, label: "<NICHE noun>", format: "{label}: {n}", display: P-18, persist: across_cuts}
```
- **Ops** are written per beat: `state_ops: [{var: count, op: add, value: 1, at: <s>}]`, or `op: set` for a jump (P-20), and only on a cut frame (the digits roll 1–2 f after it, P-19; whips included: the counter stays sharp through every blur, v03 @ 7.9, 37.9).
- **Display rules:** one position for the whole span (cx 540, cy = caption cy − 120); it changes only on ops; it appears with the first op (value 1, never 0); it never decreases; it never shows a value the footage hasn't reached; it survives every cut (A-roll and POV); it exits 8 f before the TURN (P-12) and never shares a frame with the title or the end card.
- **Label:** one noun, title case, ≤ 12 characters, the thing that repeats ("Reframes", "Batches", "Passes", "Drops", "Washes", "Tries").
- **Build:** one scene spanning the first op → its exit; the shown value is the last op at or before `ctx.t`; the scene declares an `events` entry at every op (so G3 and V-CADENCE see the ticks).

### 17.2 Anchors: the ring and the tap ripple (tracked)
- **When to ask for a track (plan time, P8c):** as soon as a beat's visual says ring / ripple / bubble *on the device* and the device moves more than 20 px over the scene (hand-held swing, a hold-up, a pan). Track only the scene's span plus 0.3 s each side (≤ 10 s per run):
  1. `veos track --project P --at <t_in> --look` → read the device box off `plan/tracks/look_<t>.jpg` (edit-frame px).
  2. `veos track --project P --id phone --at <t_in> --box x,y,w,h --from <t_in − 0.3> --to <t_out + 0.3>` (a fingertip tap: `--point x,y`). Look at `plan/tracks/phone.preview.jpg`.
- **Scene:** `anchor: {track: "phone", scale_with: true, lost: "fade"}` with `box` = the device box at `t_in` + 14 px on every side (corner radius + 14). The ring code draws inside that box; core moves and scales the box with the device (camera zooms included). Tap ripple: `anchor: {track: "tap"}` on a point track.
- **Fallback:** a clamp or a still hand (drift ≤ 20 px over the 9 f sweep) needs no track: use the static box from the look frame. Skip the ring when the preview shows the device lost on more than 20 % of the span (V-ANCHOR `max_lost`), when the device fills or leaves the frame, or when motion blur hides its outline (the H-A swing): never leave a ring on a stale spot.
- Face clearance 40 px: V-ANCHOR fails a ring whose tracked rect would cover the face (a device held next to the face): skip it or shoot it further from the face.

### 17.3 Validator V-STATE
Pending in this engine (E-09). Until it ships, the QA review checks: displayed value = the running sum of ops at every tick frame; ops ascending; the final value equals the last repetition shown; the counter rect is constant ±4 px; the ring sits within 20 px of its device box and never covers the face.

### 17.4 Build notes (scenes.js recipes for this style's signature pieces)
```js
// P-01 Title Stagger: one phrase at a time, 2 f pop-in with horizontal blur, 2 f blurred crossover, blurred away in the hook whip.
const TITLE = { cy: 1340, out: 2.00, phrases: [{ text: "WHAT THEY", at: 0.03 }, { text: "DON'T TELL YOU", at: 0.50 }, { text: "ABOUT YOUR PHONE", at: 1.25 }] };
function titleLayers(ctx, text, s, op, blur) {          // extrusion, white stroke, gradient fill: three stacked copies
  const font = `italic 900 76px/1 ${ctx.fam("display")}`, g = ctx.tokens.gradients.title.stops;
  const base = `position:absolute;left:64px;width:952px;text-align:center;top:${TITLE.cy - 38}px;font:${font};letter-spacing:.01em;text-transform:uppercase`;
  return `<div style="position:absolute;inset:0;opacity:${op};transform-origin:540px ${TITLE.cy}px;transform:scale(${s.toFixed(3)});filter:url(#hb${Math.round(blur)})">
    <div style="${base};color:${ctx.col("title_shadow")};text-shadow:2px 3px 0 ${ctx.col("title_shadow")},4px 6px 0 ${ctx.col("title_shadow")},0 8px 18px rgba(0,0,0,.35)">${ctx.esc(text)}</div>
    <div style="${base};color:${ctx.col("paper")};-webkit-text-stroke:6px ${ctx.col("paper")}">${ctx.esc(text)}</div>
    <div style="${base};background:linear-gradient(180deg,${g[0]},${g[1]} 55%,${g[2]});-webkit-background-clip:text;background-clip:text;color:transparent">${ctx.esc(text)}</div></div>`;
}
const HBLUR = `<svg width="0" height="0" style="position:absolute">${[0, 4, 8, 12].map(b => `<filter id="hb${b}" x="-10%" y="-50%" width="120%" height="200%"><feGaussianBlur stdDeviation="${b} 0"/></filter>`).join("")}</svg>`;
VEOS.scene({ id: "title", t_in: 0, t_out: TITLE.out + 4 / 30, z: 10, in: "none", out: "none", kind: "lockup", satisfies: ["question", "device"],
  text: true, text_class: "TC-display", lines: 1, roles: ["primary"], text_content: TITLE.phrases.map(p => p.text).join(" "),
  box: { x: 64, y: TITLE.cy - 60, w: 952, h: 120 }, events: TITLE.phrases.slice(1).map(p => p.at),
  render(ctx, lt) {
    const F = Math.round(lt * 30), P = TITLE.phrases, q = b => [0, 4, 8, 12].reduce((a, v) => Math.abs(v - b) < Math.abs(a - b) ? v : a, 0);
    let html = HBLUR;
    P.forEach((p, k) => {
      const a = Math.round(p.at * 30), nxt = k + 1 < P.length ? Math.round(P[k + 1].at * 30) : null, f = F - a;
      if (f < 0 || (nxt !== null && F >= nxt + 2)) return;
      const from = k === 0 ? 0.70 : 0.85, pin = ctx.ease.out(ctx.clamp((f + 1) / 2));          // sharp on its 3rd frame
      const pout = nxt !== null ? ctx.clamp((F - nxt + 1) / 2) : 0;                              // 2 f crossover
      const pw = ctx.clamp((F - Math.round(TITLE.out * 30)) / 4);                                 // blurred away in the whip
      html += titleLayers(ctx, p.text, (from + (1 - from) * pin) * (1 + 0.5 * pw), (0.5 + 0.5 * pin) * (1 - pout) * (1 - pw), q(12 * (1 - pin) + 8 * pout + 12 * pw));
    });
    return ctx.html(html);
  } });

// P-18/P-19/P-20 Counter: one scene for the whole span; value = last op at or before t; odometer roll on each op.
const OPS = [{ t: 3.90, v: 1 }, { t: 6.20, v: 2 }, { t: 7.60, v: 3 }, { t: 11.20, v: 5 } /* … from state_ops */];
const CNT = { label: "Batches", cy: 1150, out: 26.60 };
VEOS.scene({ id: "counter", t_in: OPS[0].t, t_out: CNT.out, z: 6, in: "none", out: "none", text: true, text_class: "TC-display",
  roles: ["accent"], text_content: OPS.map(o => `${CNT.label}: ${o.v}`).join(" / "), box: { x: 200, y: CNT.cy - 48, w: 680, h: 96 },
  events: OPS.slice(1).map(o => o.t - OPS[0].t),
  render(ctx, lt, dur) {
    let i = 0; OPS.forEach((o, k) => { if (ctx.t >= o.t - 1e-6) i = k; });
    const v = String(OPS[i].v), pv = i > 0 ? String(OPS[i - 1].v) : v, p = i > 0 ? ctx.ease.out(ctx.clamp((ctx.t - OPS[i].t) * 30 / 4)) : 1;
    const inP = ctx.ease.out(ctx.clamp(lt / (8 / 30))), outP = ctx.clamp((dur - lt) / (8 / 30)), H = 84;
    const st = `font:700 80px/1 ${ctx.fam("label")};font-variant-numeric:tabular-nums;color:${ctx.col("accent")};-webkit-text-stroke:3px ${ctx.col("counter_stroke")};paint-order:stroke fill;text-shadow:0 3px 8px rgba(0,0,0,.45)`;
    const W = Math.max(v.length, pv.length), a = v.padStart(W, " "), b = pv.padStart(W, " ");
    const digits = [...a].map((c, k) => c === b[k] || p >= 1 ? `<span style="display:inline-block;width:.62em;text-align:center">${c.trim()}</span>`
      : `<span style="display:inline-block;width:.62em;height:${H}px;overflow:hidden;vertical-align:bottom;position:relative"><span style="position:absolute;left:0;right:0;top:${-H * p}px">${b[k].trim()}</span><span style="position:absolute;left:0;right:0;top:${H * (1 - p)}px">${c.trim()}</span></span>`).join("");
    return ctx.html(`<div style="position:absolute;left:200px;top:${CNT.cy - 48 + 24 * (1 - inP)}px;width:680px;height:96px;display:flex;align-items:center;justify-content:center;opacity:${Math.min(inP, outP)};${st}">${ctx.esc(CNT.label)}:&nbsp;${digits}</div>`);
  } });

// P-03 Ring Sweep: box from the anchor pass (output px). A glowing segment runs bottom -> top on both sides in 9 frames.
const RING = { t: 0.30, b: { x: 600, y: 470, w: 250, h: 470, r: 46 } };
VEOS.scene({ id: "ring", t_in: RING.t, t_out: RING.t + 10 / 30, z: 6, in: "none", out: "none", kind: "device", roles: ["highlight"],
  box: { x: RING.b.x - 18, y: RING.b.y - 18, w: RING.b.w + 36, h: RING.b.h + 36 }, events: [4 / 30],
  render(ctx, lt) {
    const f = lt * 30, x = RING.b.x - 14, y = RING.b.y - 14, w = RING.b.w + 28, h = RING.b.h + 28, r = RING.b.r + 14, g = ctx.canvas();
    const head = y + h - (h + 0.3 * h) * ctx.ease.inOut(ctx.clamp(f / 9)), seg = 0.45 * h;      // head climbs past the top edge
    const grad = g.createLinearGradient(0, head, 0, head + seg);
    grad.addColorStop(0, ctx.hexA("highlight", 1)); grad.addColorStop(1, ctx.hexA("highlight", 0));
    g.save(); g.beginPath(); g.rect(x - 30, Math.max(y - 30, head - 6), w + 60, seg + 6); g.clip();
    const path = () => { g.beginPath(); g.moveTo(x + r, y); g.arcTo(x + w, y, x + w, y + h, r); g.arcTo(x + w, y + h, x, y + h, r); g.arcTo(x, y + h, x, y, r); g.arcTo(x, y, x + w, y, r); g.closePath(); };
    g.shadowColor = ctx.col("highlight"); g.shadowBlur = 40; g.lineWidth = 8; g.strokeStyle = grad; path(); g.stroke();
    g.shadowBlur = 18; g.lineWidth = 4; g.strokeStyle = "rgba(255,255,255,.95)"; path(); g.stroke(); g.restore();
    return "";
  } });

// POV clip: lands from the whip (land = true), optional P-10b snap at `snap` (clip seconds) and P-21 steps [{at, s}].
function pov(id, asset, t0, t1, povPt, { kb = [1.0, 1.06], offset = 0, land = true, snap = null, steps = [] } = {}) {
  VEOS.scene({ id, t_in: t0, t_out: t1, z: 1, in: "none", out: "none", kind: "broll", continuous: true, box: { x: 0, y: 0, w: 1080, h: 1920 }, // z1 plate: takes the footage blur
    events: [snap, ...steps.map(s => s.at)].filter(x => x != null),
    render(ctx, lt, dur) {
      const L = land ? ctx.ease.out(ctx.clamp(lt / (3 / 30))) : 1, sn = snap != null ? 1 + 0.25 * ctx.ease.out(ctx.clamp((lt - snap) / (6 / 30))) : 1;
      let st = 1; steps.forEach(s => { if (lt >= s.at) st = s.s; });                       // hard steps, no easing
      const s = (1.15 - 0.15 * L) * ctx.lerp(kb[0], kb[1], lt / dur) * sn * st;   // the land blur is the timeline.blur defocus
      return ctx.html(`<div style="position:absolute;inset:0;background:url(${ctx.videoFrame(asset, lt + offset)}) center/cover;transform-origin:${povPt.x}px ${povPt.y}px;transform:scale(${s.toFixed(4)})"></div>`);
    } });
}
```
Timeline entries that go with a T-WHIP at `tCut` (device point `D = {x, y}` in screen px): `"camera": [{"t": tCut - 7/30, "preset": "zoom-through", "p": {"origin": D}}, …, {"t": <return cut>, "preset": "reset"}]` (A-roll out; a POV going out zooms inside its own `pov()` about `povPt`: add a 4 f 1.0 → 1.6 ramp before `t1`), `"blur": [{"t": tCut - 2/30, "kind": "radial", "amount": 0.3, "at": [D.x, D.y], "frames": 4, "shape": "pulse"}, {"t": tCut, "kind": "defocus", "px": 14, "frames": 3, "shape": "decay"}]`, `"transitions": [{"t": tCut, "id": "T-WHIP", "type": "flash", "frames": 7, "pre": 4, "peak": 0.28}, {"t": <return cut>, "id": "T-CUT"}]`, `"stage": [{"t": tCut, "layout": "L-pov", "via": "cut"}, {"t": <return cut>, "layout": "L-full", "via": "cut"}]`. POV scenes are z1 plates, so the footage blur reaches them. T-WHIP-S is a `whip` transition (`angle: 60`) + `rotation-snap` 3 f before the cut (`p.origin: D`); T-WHIP-L a `whip` transition (`dir`) + the 30 % dark `fx.flash`. Never overlap two typed transitions (V-FX); at most 3 flashes per second (V-FLASH). A POV entered by T-CUT uses `pov(..., {land: false})`.

---

## §18 Data contract
OFF (`profile.modules.data_figures = false`): numbers are the device's own readings, spoken specs on chips, or the counter (§17).

## §19 Evidence and citations
OFF (`profile.modules.citations = false`): no source cards or credit lines; third-party moments follow §12.5.

## §20 Dialogue
OFF (`profile.modules.dialogue = false`): one presenter.

## §21 Canvas camera
OFF (`profile.modules.canvas_camera = false`, PV-5): the camera only ever moves footage.

## §22 Ink and annotation layer
OFF (`profile.modules.ink = false`): the ring and the tap ripple are anchored graphics (§17.2), not hand-drawn ink.

## §23 Continuity
OFF (`profile.modules.continuity = false`): no morph chains or motifs; the device is the through-line.

## §24 Series furniture
OFF (`profile.modules.series = false`, VAR). When {{BV-01.name|the creator}} turns it on: a "{name} #{n}" tag in Poppins 700 40 px, `paper` on a 70 % black pill, top-left at x 64, y 140, for the hook only (0–2.5 s), and it counts toward the intro cap.

## §25 Sponsor, brand and end cards `[COND: modules.brand; cta ∋ end_card] [DNA look; VAR assets]`
**End card (P-32):**
- **Enter (T-BLACK):** a hard cut to black 2 f after the last word ends (no fade; v01 @ 22.42), ≤ 3 f of pure black, then the card **builds in over ≈ 14 f**: the wordmark letters appear left → right, each smearing in from a horizontal blur (16 → 0 px, 3 f each, 1 f stagger), while the artwork bands fade and rise 20 px (v01 @ 22.47–22.90).
- **Layout:** W-void black. Wordmark = the creator's name (BV-01) in Barlow Condensed 700 caps, fit to ≈ 820 px wide (110–200 px), white, cy 780, no tracking. Top artwork band y 0–330 and bottom band y 1000–1500: the creator's own artwork or logo (BV-16, `origin: creator`); without it, the created band: the `endcard_band` gradient (primary → `#0A1A4A` → black) with 9 seeded angular shards in `primary` at 30–60 % opacity drifting 20 px/s (deterministic, NC-9).
- **CTA line** (cy 1180): `comment_keyword` → P-33 "Comment" + keyword chip; `link_bio` → "Link in bio" chip; `end_card` alone → no line.
- **Hold:** 2.5–4.4 s after the build (`brand.endcard.max_s` 5.0 in all; v01 ≈ 4.9 s); the keyword ≥ 1.5 s.
- **Exit:** the wordmark stretches sideways with a horizontal smear while the card zoom-blurs (1.0 → 1.5) and darkens to black over 5 f, then a hard end (v01 @ 27.17–27.37).
- `kind: "end-card"` on the card scene; `kind: "cta-keyword"` on the keyword chip.

**Sponsor (when a reel is sponsored):** the sponsor's product is filmed like any device (POV); a "Paid partnership" TC-legal label (BV-14 wording) at x 64, y 140 for ≥ 2 s at the first mention, plus the spoken disclosure (NC-12). The sponsor's logo appears only on the end card's top band, from the sponsor's own file.

---

## Part C. Exceptions and the non-overridable core
- **C.1** NC-1…NC-14 apply unchanged (structure Part C.1). The ones this style must watch: **NC-1** (a title or ring near a held-up device next to the face), **NC-5** (captions lifted from the evidence's y 1607 to ≤ 1440), **NC-6** (drawn phones and recreated UIs are labelled), **NC-14** (personal data on device screens).
- **C.2** Declared exceptions: **none** (§2.2). A buyer who wants smaller captions (< 54 px) needs E3, which is a DNA change (DV-n) with the E3 limits.
- **C.3** Buyers may not add exceptions in the normal flow; any addition is logged as a deviation.

## Part D. Personalisation
**D.1 Branding questions (one round, each with "keep the template default"):**
| BV | Question | Feeds |
|---|---|---|
| BV-01 | Your name and handle | End-card wordmark, placeholders, series tag |
| BV-02 | One or two brand colours | `primary` (the title blue) and `accent` (the counter red); `title_top`, `title_shadow`, `counter_stroke` follow; contrast-nudged |
| BV-05 | Your speech and caption language | `profile.language`, always asked: **English** → English captions (default) · **Hinglish** → romanised Hinglish captions · **Hindi** → Devanagari captions; numbers follow (BV-06). |
| BV-08 | Your call to action | `end_card`, `comment_keyword` (+ keyword), `link_bio`, `none` |

**D.2 Lock summary:**
| Area | Lock |
|---|---|
| Face ↔ POV alternation, the whip, the title recipe, CS-1 mechanics (one line, no emphasis), the counter mechanics, the ring recipe, layouts and moves, the pattern list | DNA |
| Title size 68–96 px, title y 1180–1400; caption size 54–66 px, weight 500–600, y 1240–1440; counter size 64–84 px; motion ±15 %; cadence ±15 %; presenter share ±10 pts; max absence 4–6 s | TUNE |
| Brand colours, language, numbers, CTA choice and keyword, series on/off, brand on/off, comedy off/light, the buyer's setups | VAR |
| Hook pairs (§6.4), lookup rows (§8.4), counter labels, worked examples (§14), App. A, glossary | NICHE |

**D.3 Common tweaks and how they are classified:**
| Buyer says | Change | Class |
|---|---|---|
| "Bigger captions" | `captions.profiles.CS-1.skin.size` up to 66 | TUNE |
| "Captions higher" | `position.cy` down to 1240 | TUNE |
| "Green title" | `roles.primary.default` | VAR |
| "No counter" | turn off RS-COUNT for a reel (use RS-LIST) | per reel |
| "Use a split screen" | a `stack` layout | DNA → DV-n (warned) |
| "Highlight keywords in the captions" | CS-1 emphasis | DNA → DV-n (warned) |
| "Add meme sounds" | comedy `roast` | above `comedy_max` → DV-n (warned) |

**D.4 NICHE slots, filled per reel:** §6.4 (one row per reel: device, f0, reveal), §8.4 (new line types mapped to existing patterns), counter labels, §14 (the first approved reel of each shape becomes its worked example), App. A (approved titles), the glossary (device and app names confirmed in captions).

## Part E. What this template changes vs the reference playbook
| Reference (Naman) | Device Whip |
|---|---|
| Result-first roast hook with a yellow slab banner | HA-17: a blue italic caps title or a question + ring, then a whip into the device by 2.5 s |
| Canvas / Data Stage worlds, panel drops, splits | One picture at a time: the creator's set ↔ the device POV; no splits |
| Chunky captions + lowercase subtitles | One quiet caption profile: one white line, no emphasis, one y per reel |
| Data Theatre (crowds, gauges) | Numbers live on the device's own screen; repetitions live in the counter |
| Comedy layer with meme SFX | Light comedy on the presenter's face; no meme sounds |
| Zoom system Z-1…Z-7 on the face | One f0 open punch (Z-4), whip zooms (Z-1, Z-5), POV snaps and step punches on the device; no punch-in rhythm on the face |
| Many transitions | Three whip kinds on section changes (both directions), hard cuts inside items, a cut to black into the end card |

## Part F. ID index
| Prefix | IDs in this playbook |
|---|---|
| D | D1–D8 |
| H / N | H1–H18 / N1–N12 |
| W / L / G | W-studio, W-void, W-blur-set / L-full, L-pov, L-device-dim, L-endcard / G-1–G-5 (+ G-2b) |
| CS | CS-1 (rule CY) |
| HA / variants | HA-17 (H-A, H-B), HA-02, HA-10, HA-14 |
| RS / SM | RS-LIST, RS-COUNT, RS-STORY / SM-COUNTER |
| B / P | B-1–B-12 / P-01–P-34 (+ P-10b) |
| T / R | T-WHIP, T-WHIP-S, T-WHIP-L, T-CUT, T-MATCH, T-JUMP, T-BLACK, T-DIM / R-1–R-8 |
| Z | Z-0 reset, Z-1 zoom-through, Z-2 push-drift, Z-3 snap-punch, Z-4 crash-zoom (open punch), Z-5 rotation-snap (spin whip) |
| SH / FB / C | SH-1–SH-9 / FB-1–FB-8 / C-1–C-14 (capture checklist) |
| V | V-F0, V-CADENCE, V-TITLE, V-ONWORD, V-SAFE, V-FACE, V-PRESENCE, V-CAPTION, V-TYPE, V-EXC, V-HUES, V-CAMERA, V-LAYOUT, V-PROMISE, V-INSERTS, V-CITE, V-COMEDY, V-NUMFMT, V-REHOOK, V-STATE (pending) |

---

## App. A Title and hook bank `[NICHE]`
Slots in `{braces}` are filled per reel. Each title is the spoken line, word for word.

| # | Title phrases (or the hook question) | Archetype / variant | Shape | [NICHE: example] phones | [NICHE: example] kitchen |
|---|---|---|---|---|---|
| 1 | WHAT THEY / DON'T TELL YOU / ABOUT YOUR {DEVICE} | HA-17 H-A | RS-LIST | …ABOUT YOUR PHONE | …ABOUT YOUR AIR FRYER |
| 2 | Can your {device} actually {do X}? | HA-17 H-B | RS-COUNT | Can your phone actually see the back of your head? | Can your blender actually crush ice twenty times? |
| 3 | I PUSHED / {FEATURE} / TO THE LIMIT | HA-17 H-A | RS-COUNT | I PUSHED / AI EDITING / TO THE LIMIT | I PUSHED / THIS BLENDER / TO THE LIMIT |
| 4 | STOP USING / YOUR {DEVICE} / LIKE THIS | HA-17 H-A | RS-LIST | …YOUR PHONE CAMERA… | …YOUR KETTLE… |
| 5 | {N} {DEVICE} TRICKS / YOU NEVER USE | HA-17 H-A | RS-LIST | 4 PHONE TRICKS / YOU NEVER USE | 3 MICROWAVE TRICKS / YOU NEVER USE |
| 6 | YOU'VE BEEN / USING {X} / WRONG | HA-17 H-A | RS-LIST | …USING SCREENSHOTS… | …FROTHING MILK… |
| 7 | THE {PRICE} {DEVICE} / THAT BEATS / {RIVAL} | HA-02 | RS-LIST | THE $20 EARBUDS / THAT BEAT / MY $250 ONES | THE $30 BLENDER / THAT BEATS / MY $300 ONE |
| 8 | THIS {RESULT} / WAS {MADE} / {N} TIMES | HA-02 | RS-COUNT | THIS PHOTO / WAS EDITED / 20 TIMES | THIS ICE / WAS CRUSHED / 20 TIMES |
| 9 | "{Action}." → straight into the device | HA-10 | RS-LIST | "Hold the space bar." | "Tap this twice." |
| 10 | "So my {device} just {did something}." | HA-14 | RS-STORY | "So my phone just saved me forty minutes." | "So this coffee machine just texted me." |

## App. B Evidence map `[DNA; template only]`
The full source map (every DNA rule → `vNN @ m:ss`), the measurements and the `(unverified)` list are in `evidence.md`. Summary:
- Title stagger with 2 f pop-in, blue gradient, white stroke, dark extrusion, cy ≈ 1340, ≈ 77 px: v02 @ 0:00.07–0:01.33.
- Whips (motion audit 2026-10-07): spin v02 @ 1.30, 29.8; linear v02 @ 5.3, 24.4; zoom-flash v02 @ 10.6, 17.9, v03 @ 2.5, 7.9, 37.9. f0 open punch v02 @ 0.03–0.17; POV snap v02 @ 8.2; step punches v03 @ 40.2–42.8.
- Ring sweep in cyan, bottom → top: v03 @ 0:00.30–0:00.57.
- Counter "Reframes: N", red with a dark stroke, above the captions, persisting across cuts and jumping on cuts (5 → 7, 13 → 15 → 16 → 18 → 20): v03 @ 0:04–0:42.
- Captions one line, white, ~48–58 px measured, y ≈ 1607 (v02) / ≈ 1273 (v03): v02 @ 0:02–0:36, v03 @ 0:00–0:45.
- Message bubble with avatar and "Name · time": v01 @ 0:05–0:13. End card (black, white condensed wordmark, artwork bands): v01 @ 0:22–0:27.
- **(unverified):** sound (not observable); the exact fonts; the speech language (no transcripts; captions are English); whether the backdrops were real sets or composited; whether the POV was a second camera or the same camera.
