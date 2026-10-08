# Long-form Re-cut Style Playbook (template v1)

**Purpose.** You (Claude) receive {{BV-01.name|the creator}}'s own **finished 16:9 long-form video** (the master: edited, graphics, renders and music already baked in). This playbook makes you **mine one self-contained 110–150 s argument out of it, reframe every shot to 9:16, and caption it in voice-coded serif** so the short plays like a calm documentary that started mid-thought. You add almost nothing: the craft is **selection, reframing and captions**, not graphics.

**Input (SW-01 `edited_master`).** One master file (1080p minimum, 4K preferred), plus the cast (who is the host, who are the guests). Nothing is shot for this template.

**Inspired by** Veritasium's vertical re-cuts of its own long-form videos (evidence: `analysis/short/veritasium.md`, App. B). Sound comes from the master's own mix (§11); this template adds no sound design.

### Style DNA `[DNA]`
A Long-form Re-cut looks like **a documentary that you walked into mid-sentence**. Frame 0 is already moving: a render glides, the host is mid-gesture, a guest holds the object. A **white serif caption of two or three words** sits low and centred at y 1380 and swaps hard on the speech, word group by word group. When anyone other than the host speaks, the caption turns **gold**, even when the picture shows the host listening. There is no banner, no sticker, no zoom, no sound effect: every picture is the master's own picture, reframed. Wide diagrams that can't survive a 9:16 crop sit as a **16:9 band on black or on a blurred copy of themselves**, with the caption below the band. Restraint is the brand.

**Copy these 5 things** (and it reads as this style):
1. **Serif speech captions, 1 line, 1–3 words (≈ 2.3 avg), centred at y 1380, Source Serif 4 600 at 70 px, white with a soft black shadow, hard swaps.** §5.3 CS-1.
2. **Voice-coded colour:** white `#FFFFFF` for the host / narrator, the guest colour `{{BV-02.accent|#E8CC28}}` (gold by default) for every guest voice. The colour follows the **voice**, never the face. §5.3, §20, R-3.
3. **Cold open, no graphic:** the reel starts on the master's strongest moving image with the caption already running mid-sentence (HA-14). §6.2.
4. **Reframe, don't redraw:** every shot is the master's own shot, face-followed or centre-cropped to 9:16; shots that can't be cropped become a centred 16:9 band (black or blur-fill) with the caption under it. §3, §8 RF-1…RF-4.
5. **Long, calm shots:** the master's cuts are the reel's cuts (3–14 per minute), cadence comes from caption churn (a new chunk every 0.4–1.0 s) and the master's in-shot camera motion, never from added zooms. §7.6, §9.3, §10.2.

### Fidelity audit corrections (2026-10-06, full-resolution check of v01-v03)
Override older figures below. Evidence: `docs/audit/long-form-recut/audit.md`.
- Captions confirmed: Source Serif 4 600, ≈ 70-72 px, cy ≈ 1377, hard swaps of 2-3 words (~0.4 s). The outline is a hairline at most; the legibility comes from a soft dark drop shadow.
- Gold is more saturated than first measured: **`#E8CC28`**.
- ~~Gold also marks the host on location~~: **withdrawn** by the 2026-10-07 burst check: the host asking on location at CERN is **white** (v01 @ 1:19.3–1:20.3, handheld). The gold over the host at v02 @ 1:30 is a guest's voice over the host's picture (R-3). There is no `field` speaker class.
- Animation-led reels (v03) use a lighter LaTeX-like serif at cy ≈ 1341; use Source Serif 4 400 there.
- All sampled frames are full-bleed 9:16 reframes; letterbox bands did not appear in the 23 frames checked (keep L-band-* as the rare fallback).

### Completeness audit (2026-10-07, every frame at 30/24 fps, 15 bursts + ORB camera measure)
Evidence: `docs/audit/long-form-recut/completeness.md`.
- **No editor camera, confirmed by measurement:** in 17.7 s of host to camera (v02 0:00–0:17.7) and 6 s at v02 1:40–1:46, the background never jumps more than 1.9 % in scale or 1.7 % in position between frames (gesture noise); no punch, push, shake or re-crop jump. **Crops are static per shot** (the bookshelf stays put while the host moves within it); a guest single may leave his face off-centre, even touching the frame edge (v01 @ 0:44.6). So RF-1 = a near-static crop: let the follow move only when the face would leave the frame.
- **Every editor transition is a hard cut (0 f)**, including the splice into the host from another shoot (v03 @ 1:29.87: HUD band → host at night, 0 f, captions swap on the same frame). **T-DIP is retired** (it was a guess). Fit switches (band ↔ full) are hard cuts too (v03 @ 1:33.37 band → band, 1:29.87 band → full).
- **Captions are voice-timed, not cut-timed:** a chunk runs across a master cut (v02 @ 0:20.83 by 3 f; v02 @ 0:35.28 a guest's gold chunk by 4 f over the host's laugh) and a J-cut voice turns the caption gold before the picture changes (v01 @ 0:44.57, 2 f early). Never snap chunk edges to cuts and never hide captions at cuts. Chunks last 0.4–0.6 s in fast speech (v01 @ 1:19.70, 1:20.20), up to ≈ 1 s in slow narration.
- **The band's blurred backdrop is not darkened:** the surround is as bright as the band or brighter (v03 @ 1:29.7: surround luma 150 vs band 104; @ 1:33.5: 69 / 50). `L-band-blur.luma` is now 0.
- **Ending:** v01 (1:54.9) and v02 (2:33.3) hard-end on the last render with the last caption still on; v03 fades the final render to black over **5 f** after the narration has ended (1:49.73–1:49.94, caption already gone). T-END-FADE is that optional ending.
- **Master-made motion stays the master's:** handheld location pans (v01 1:19–1:25 trip the scene detector every ≈ 0.17 s but are one shot), a hard cut into a defocused graphic that racks to sharp over 8 f (v02 @ 0:20.83 p̄ bubble), in-render dissolves (v03 1:10–1:29). Keep them; never imitate them on other shots.
- **Pacing measured:** median shot 2.5 s (v01), 2.8 s (v02), 1.9 s (v03 outside its 79.5 s uncut animation); p90 11.9 / 8.8 / 5.8 s; longest shot 17.1 / 17.8 / 79.5 s; master cuts 1.1–2.2 per 10 s.

### Directives `[DNA]`
| # | Directive | Where it lives |
|---|---|---|
| D1 | **One argument, whole.** The reel is one self-contained sub-story (problem → mechanism → proof → implication) of 110–150 s, cut from the master. It never refers to anything outside itself. | §1 P4b, SS-1…SS-8 |
| D2 | **Walk in mid-thought.** Frame 0 = moving master picture + caption already running. No title, no banner, no hook graphic. | §6.2, H1 |
| D3 | **Reframe, don't redraw.** Never rebuild, re-grade or decorate the master's visuals. Crop, follow, or band them. | §3, §8, N1 |
| D4 | **The voice decides the colour.** Host white, guests gold, decided per word from diarisation. | §5.3, §20, H6 |
| D5 | **The master's cuts are the reel's cuts.** No added cuts, re-crops, punch-ins or zooms; the only new cuts are splices between master spans at sentence boundaries. | §9.3 R-1…R-10 |
| D6 | **Captions carry the pace.** A caption chunk every 0.4–1.0 s, timed to the voice, never to the cuts; blank-caption pauses ≤ 2.0 s are kept as the master's breaths. | §5.3, §7.6 |
| D7 | **Silence of graphics.** At most 3 italic object titles per reel and one end line; nothing else is drawn on the master. | §8.1, §5.4 |
| D8 | **End on the implication.** The last sentence is the "why it matters" line; hard end ≤ 6 f after its last word. | §7.1, P-LAST-LINE-END |

Buyer directives (`BD1…`, `[VAR]`) are added below this table by the buyer; they may only make the style stricter or more specific.

### Quick index
| § | What | Status |
|---|---|---|
| §0 | Style profile (switches) | ON |
| §1 | Procedure: edited-master branch, sub-story mining, shot-by-shot reframe | ON |
| §2 | Hard rules, declared exceptions (E6) | ON |
| §3 | Worlds, layouts, reframe classes RF-1…RF-4, safe zones | ON |
| §4 | Colour (voice axis), no themes, no grades | ON |
| §5 | Serif caption system CS-1, object titles, end line | ON |
| §6 | Hook: HA-14 cold authority (default), HA-10, HA-15 | ON |
| §7 | Explainer structure, re-hooks every ≤ 25 s, cadence | ON |
| §8 | Visual system: 4 overlay patterns + 19 cut/reframe patterns (P-…) | ON |
| §9 | Transitions (cut, dissolve, dip, end), shot grammar R-1…R-10 | ON |
| §10 | Motion tokens, `zoom_policy: source_only`, layers | ON |
| §11 | Sound contract: the master's mix, nothing added | ON |
| §12 | Footage: the master, 4K, cast list; inserts ask-then-create | ON |
| §13 | Output contract (beats, shots, reel header, checkpoint) | ON |
| §14 | Worked examples (3) | ON |
| §15 | QA checklist | ON |
| §16–§19, §21–§25 | Modules | OFF (one line each) |
| §20 | Dialogue (voice-coded captions, cast, angles) | ON |
| Parts C–F | Exceptions & core · personalisation · changes · IDs | ON |
| App. A | Post-title and cold-open line bank | ON |
| App. B | Evidence map (summary; full map in `evidence.md`) | ON |

Formats: **F-A "Master re-cut"** (the only format). Themes: none (`single`).

---

## §0 Style profile `[REQ]`

```yaml
profile:                         # mirrored in tokens.json -> profile
  source_type: edited_master
  presenter: {presence: guest, share: [5, 55], max_absence_s: 90}
  spine: audio
  captions: {mode: full, role: primary, mute_policy: mute_safe}
  graphics: passthrough
  duration: {class: long, target_s: [110, 150]}
  language: {speech: en, captions: {lang: en, script: Latn, transform: verbatim}, on_screen: en, post_title: en,
             supported: [[en, en, Latn], [hinglish, hinglish, Latn], [hi, hi, Deva]]}
  numbers: {grouping: international, currency: "$", compact: k_m_b, units: metric, decimals: 0, style: long}
  tone: {energy: calm, comedy: off, comedy_max: off}
  themes: {policy: single, packs: [], default: null}
  formats: {list: [F-A], default: F-A}
  footage_dependency: total
  cta: {devices: [none, post_only, cross_promo], placement: end, chosen: none}
  modules: {chrome: false, running_state: false, anchors: false, data_figures: false, citations: false,
            dialogue: true, canvas_camera: false, ink: false, continuity: false, series: false, brand: false}
```

Why each value:
- **source_type: edited_master**, because all three evidence reels are vertical re-cuts of finished long-form footage: the CAD fly-overs, CERN interviews and painted animation are baked in (v01–v03).
- **presenter: guest, share 5–55 %, max absence 90 s**, because the host's face is on screen ≈ 40 % (v01), ≈ 55 % (v02) and ≈ 5 % (v03, an animation-led master with the host only at 1:30 and 1:44). The master decides presence; the editor never inserts the host to raise it. V-PRESENCE is off for that reason (the validator can't steer a master).
- **spine: audio**, because the voice (narration + interview) is the timeline: the master's pictures follow the argument, and the sub-story is chosen by its sentences.
- **captions: full / primary / mute_safe**, because captions are on screen 88–92 % of the runtime and are the only text (all three videos); with sound off the captions tell the whole story.
- **graphics: passthrough**, because ≈ 90 % of what you see is source-made; the re-cut layer only adds captions, reframing and (rarely) an italic object title.
- **duration: long, 110–150 s**, because the evidence runs 110.0, 115.1 and 153.3 s.
- **language: English verbatim**, because all three are English with burnt-in captions that match the speech; Hinglish/Hindi masters are supported (Hindi captions use **Noto Serif Devanagari**, see §5.5).
- **numbers: international, long style**, because captions write numbers as spoken ("16.2 million", "99.9%", "614 days").
- **tone: calm, comedy off**, because delivery is a steady ≈ 2.4 words/s and nothing comic is added (laughs come from the master only).
- **themes: single, formats: F-A only**, because the look never changes between reels; only the master does.
- **footage_dependency: total**, because without the creator's own master there is nothing to re-cut.
- **cta: none by default**, because none of the evidence reels has a CTA or end card (they end on the last render). The buyer may choose `post_only` or a one-line `cross_promo` pointer to the full video (§6.7).
- **modules: dialogue only**, because guest voices are the one structural device the editor must handle (speaker-coded captions); everything else is in the master.

### 0.4 Formats `[DNA set]`
| Field | F-A "Master re-cut" |
|---|---|
| When | Every reel: one self-contained 110–150 s argument from one finished 16:9 long-form video |
| Profile overrides | none |
| Layouts | `L-master` (≥ 85 %), `L-band-black` / `L-band-blur` (stage bands for creator-supplied 16:9 clips and vertical masters, each ≤ 15 %), `L-void` (created substitute cards, ≤ 8 %) |
| Hook default | HA-14 Cold authority |
| Structure | explainer |
| Shared DNA | Cold open mid-sentence on the master's strongest moving image; voice-coded serif captions at y 1380; reframe, don't redraw |

### 0.5 Theme packs
OFF (`themes.policy = single`): the master's own picture is the palette; only the guest-caption colour is brandable (§4).

---

## §1 Procedure (follow in order) `[REQ] [DNA]`

The craft steps of this style are **P4b sub-story mining** and **P8b shot-by-shot reframe**. Everything else is light.

**P1 Inventory.**
- `veos project init <master file> --playbook <this playbook>` (records `source_type: edited_master` from the profile), then `veos ingest <master file>` and `veos conform --id A`.
- Read `work/sources.json`: resolution (2160p → crops never upsample; 1080p → FB-2, crops upsample up to 1.78×, say so at the checkpoint), fps (23.976/25/60 masters are conformed to 30 fps CFR), duration, audio loudness.
- **P1b Master cut list (MCL).** The `segments` of source A are the master's scene changes (scene detection). Copy them into `plan/mcl.json` as `[{id: "M1", t0, t1}]` (master time). The MCL is the only place reel cuts may come from (R-1).
- Register the master as `origin: creator` (it is the creator's own video). Third-party material inside it is handled at P11 (§12.5).

**P2 Prepare.** No matte (`footage.matte: none`): nothing goes behind anyone. Skip.

**P3 Transcribe** the whole master: `veos transcribe --id A` (add `--glossary` with the creator's technical terms and names; for Hinglish masters see §5.5).
- **P3b Diarise:** `veos speakers --mode diarize --num <people who speak>` then `veos speakers name S1=<host name>:host S2=<guest name>:guest …`. The host is whoever narrates; an off-screen narrator who is the host is `host`. Every other voice is `guest` (all guests share gold). Check `work/speakers.json`: ≥ 95 % of words labelled; overlaps keep the dominant talker (the caption engine drops back-channels).
- If the cast is unknown, use FB-3 (the most-talking voice is the host) and ask once at the checkpoint.

**P4 Segment** into the explainer units (§7.1): PROBLEM, MECHANISM, PROOF, IMPLICATION (any order the master uses), sentence by sentence.
- **P4b Sub-story mining (the craft).**
  1. Run `veos shots mine --min 110 --max 150`. It writes `plan/clip_candidates.json` (turn-bounded candidates scored for a question start, a complete answer and 2+ speakers). On a single-voice master (pure narration) it may return nothing: then build candidates yourself from sentence boundaries of `work/words/A.json`, every start that follows a pause ≥ 0.35 s or a master cut.
  2. Re-score every candidate (and its ± 1-sentence neighbours) with the **sub-story tests SS-1…SS-8** below. A candidate must pass all eight. Rank the passes by SS-2 (image strength at the in-point) and then by how many worlds it visits (host, render, guest: more is better).
  3. Present the top 3 at the checkpoint (t0, t1, opening line, last line, worlds, band share). Recommend one.
  4. Write `plan/edl.json`: 1–4 segments of source A (≤ 3 splices). In-point **0.04–0.10 s before the first word** (so the caption is on screen at f0); out-point **0.10–0.18 s after the last word ends** (≤ 6 f, D8). Splices only at sentence boundaries (P-SPLICE). Then `veos cut plan/edl.json`. **Never `--tighten`:** the master is already paced; its pauses ≤ 2.0 s are breaths (P-PAUSE-BREATH). A pause > 2.0 s with no picture change is split out with an EDL join (keep 1.2 s).

| ID | Sub-story test | Pass when |
|---|---|---|
| SS-1 | Cold-open line | The first sentence is a complete claim, paradox or problem of ≤ 14 words that needs no earlier context: it does not start with *so, and, but, this, that, it, these, which, as I said, remember, now*; no greeting, no "in this video". |
| SS-2 | Strong first image | The picture at the in-point is moving and visual (a render in motion, the host mid-gesture, a guest with the object) and is a full-bleed reframe (RF-1/RF-2), never a band, black, a title card or a sponsor shot. |
| SS-3 | One argument | Problem → mechanism → proof → implication are all inside the span. No reference out of the span: *as we saw, earlier, later, in the next section, I'll explain, link below, today's sponsor*. |
| SS-4 | Re-hook every ≤ 25 s | A world change, a turn sentence (*But…, Here's…, So why…, The problem is…*), a question or a guest's first line occurs at least every 25 s (§7.4). |
| SS-5 | Implication ending | The last sentence states why it matters or what follows (a statement ending in a period). Not a question the long-form answers later, not "but first", not a sponsor or channel plug. |
| SS-6 | Reframe budget | Band shots (RF-3) ≤ 25 % of the span; none in the first 3 s; no band run > 12 s. |
| SS-7 | Length | 110–150 s after the cut (TUNE: a buyer on `standard` uses 60–90 s). |
| SS-8 | Clean span | No sponsor read, ad, affiliate mention, mid-roll, merch plug or end screen inside the span (if a disclosure would be required, the span fails: NC-12). |

**P5 Classify** every sentence with a line type from §8.4 and mark its trigger word (the noun that names what the picture shows). In this style the line type mostly decides the **reframe pattern**, and rarely an object title.

**P6 Tone-tag** every sentence: `explain` (default), `awe` (a reveal or a striking image), `warn` (a risk or a failure), `win` (it works / the record), `cta` (only the end line). Tones choose nothing visual here; they feed the storyboard and S2 if a buyer turns sound cues on.

**P7 Hook plan.** Write **3 cold-open variants** (§6, §13.4): each is a different in-point (sentence + first shot) inside the chosen sub-story or one of its neighbours, with its first 3 s table and the stopper tests ST-2, ST-3, ST-5, ST-6. Recommend one.

**P8 Visual plan.**
- **P8b Shot-by-shot reframe (the craft).**
  1. `veos angles` → `work/angles.json` (faces, tracks, the angle list: host single, guest single(s), two-shot, wide; use the ids it lists, never invent one).
  2. For every master shot inside the cut (MCL ∩ EDL, mapped to edit time through `work/cutmap.json`), decide the reframe class (§3.2 RF-1…RF-4) with the decision table in §3.2, and write one `timeline.shots[]` entry per shot (§13.2). Do **not** use `veos shots plan`: its conversation grammar (re-crops every 4 s, cut on handover) contradicts R-1, R-2 and R-4.
  3. `veos shots render --fallback blurfill` → `work/multicam/footage.mp4` + `compose.json`. Read `compose.json`: every shot's fit, crop keys and `max_upscale` (≤ 2.0). For each RF-2 shot, check its mid frame (`veos render --test <frames>` + `veos sheet`): the subject and any baked text it needs are inside the crop; if not, change the shot to RF-3 and render again.
  4. **Vertical masters** (the creator exported 9:16): skip 1–3; the stage is `L-master` over the conformed source, and 16:9 inserts the creator supplies separately use `L-band-black` / `L-band-blur` with `src` = the inserted video asset.
- **P8c Overlays (rare):** object titles (≤ 3, §5.4), the cross-promo line if BV-08 chose it, created substitute cards (P11) and redactions (NC-14).
- **P8d Re-hooks:** mark the beats that re-hook (§7.4) with `rehook: true`; check none is more than 25 s from the previous one (V-REHOOK).

**P9 Beat sheet** (§13): one beat per master shot inside the cut (a shot longer than 8 s gets one beat per sentence), each with speaker, angle, fit, pattern, `visual` sentence and `rehook` flag.

**P10 SFX ledger and transition map.** The SFX ledger is **empty** (`sound.cue_moments: []`) unless the buyer turned cues on (§11). The transition map lists every cut that is not a master cut: splices (T-CUT), dissolves (T-DISSOLVE), and T-END.

**P11 Assets and inserts.** Run `veos inserts scan`. Ask the creator **once** (§12.5) about third-party spans inside the chosen part (news clips, other creators' footage, photos with someone else's credit line). Supplied/confirmed = keep as is (origin creator). Not confirmed = trim around the span (preferred) or cover it with P-SUBSTITUTE-CARD. Record every decision in `plan/inserts.json`.

**P12 Checkpoint** (§13.5), then **wait for approval.**

**P13 Build.** `veos captions build` → write `plan/timeline.json` (stage `L-master` from 0; beats; shots; rehooks) and `plan/scenes.js` (only the few overlays; with none, leave it empty: no placeholder scene) → `veos scenes-meta` → `veos measure --every 10` → `veos validate` → fix → preview + QA (§15, at most 3 passes) → render, `veos voice`, `veos mix`, `veos assemble`, `veos qa`. Note: the G3 motion measure covers the first 90 s only (engine cap; ER-6); review the rest by contact sheet.

---

## §2 Hard rules `[REQ] [DNA]`

### 2.1 Editing rules (every style)
The ten editing rules in `playbooks/_global/GLOBAL-RULES.md` apply. They are directions, not limits: smooth, seamless motion; nothing overlaps by accident; keep the face clear (behind the speaker is fair game, text included); readable at a glance; one idea at a time; show the thing, not the word; say what was said; hook titles hook; pace like the style, not like a timer; the style decides the look.
- **Facts the engine checks:** accidental overlaps, jumps, the face covered, unreadable text, numbers and quotes that don't match what was said, the promised count. Every count, timing and budget this playbook gives is direction for the edit, not a limit.
- **Picture first, in this style's own look:** every key beat shows the thing being said (an object, a screen or app, a diagram, numbers in motion), not just its word; text supports the picture and never replaces it. When the speaker points with words ("this, this and this", "from this to this", "ye dekho"), show what they mean. Illustrations may use made-up but realistic numbers and names ("212 views", "1.2M views"), with no label; a number or quote the speaker says is shown as said. This overrides any rule below that bans made-up numbers or asks for an example tag: those rules now cover claims (the creator's results, prices, benchmarks, testimonials), not illustrations.
- **Hook titles hook:** the on-screen title promises the viewer something (an outcome, a curiosity gap, who it's for) and is true to what the reel delivers; it need not repeat the spoken words. This playbook sets its shape (§5.2, §6.5: lines, sizes, word limits, case), never its voice (§6).
- **Retired (8 Oct 2026), whatever this playbook says below:** no REPRESENTATIONAL or example labels on made-up cards, no credit lines, no flash limit (flash as often as this style calls for; any "NC-11" cap below no longer applies), and text may sit behind the speaker without an exception.

### 2.2 Declared exceptions
| E-id | Name | This style's limits | DNA reason | Evidence |
|---|---|---|---|---|
| **E6** | Hard swap | Caption chunks swap with 0 frames of fade inside the fixed caption band (centre y 1380 ± 4 px, max width 900 px). The caption's first entry after a blank pause and its exit into a pause stay eased by the engine (`tail_s` 0.3). Never used for a new element appearing. | The style's captions are hard-swapped word groups; fading every 0.6–1.0 s would smear them | v01 @ 0:00–0:03, v02 @ 0:00–0:03, v03 @ 0:00–0:03 |

No other exception is used. Captions are 70 px (≥ the 54 px floor), so E3 is not needed.

### 2.3 Style MUST rules
- **H1 Frame 0.** f0 shows moving master footage (reframed full-bleed) **and** the first caption chunk; no headline, banner, title or graphic exists before 3.0 s. *check: V-F0*
- **H2 Cadence.** Weighted state changes per 10 s of the body = **6–15** (captions weight 1.0, master cuts 1.0); 0–3 s ≥ **4**; longest gap between weight-1 changes ≤ **2.5 s**; nothing static (no change and no in-shot motion) > **3.0 s**. *check: V-CADENCE*
- **H3 Payoff.** The strongest image of the opening shot is on screen at f0 and the first sentence is complete by **3.5 s** (≤ 14 words). *check: V-F0 (payoff_by 1.0 s for the image) + review*
- **H4 Headline limits.** None: `type.headline.kind = none`. Object titles ≤ 3 words, ≤ 1 line, ≤ 3 per reel, ≥ 20 s apart. *check: review*
- **H5 Caption sync.** A chunk appears ≤ 1 frame before its first word (max lead 0.15 s, max lag 0.10 s) and never leaves before its last word ends. *check: V-CAPTION*
- **H6 Voice colour.** Every chunk holds words of one speaker; host/narrator chunks are `primary` white, guest chunks `accent` gold; the colour follows the diarised voice, never the face on screen. *check: V-CAPTION (speaker colour) + review on handover shots*
- **H7 Face rule.** No caption, title or card covers a face box (eyebrows to chin); the caption engine's `avoid_face` moves a chunk to the chest or above the head when a crop puts the face in the caption band. *check: V-FACE*
- **H8 Dead air (spine audio).** The master's pauses ≤ 2.0 s are kept (blank caption, the picture keeps moving). A pause > 2.0 s without a picture change is trimmed to 1.2 s at P4b. *check: review (cut summary: gaps ≥ 2.0 s = 0)*
- **H9 Sub-story integrity.** The span passes SS-1…SS-8; no reference out of the span; ≤ 3 splices, each at a sentence boundary. *check: review (checkpoint)*
- **H10 Reframe integrity.** Each master shot has exactly one fit for its whole duration (cover follow, cover centre, or band); fits change only on master cuts or splices; max upscale ≤ 2.0×; no face cut at the eyes; baked text and credit lines the shot needs stay inside the crop. *check: review (compose.json + test frames)*
- **H11 Re-hooks.** A re-hook beat (`rehook: true`) at least every **25 s** after the hook; the hook is ≤ 15 % of the runtime. *check: V-REHOOK*
- **H12 No added camera.** No camera presets, punch-ins, crash zooms, shakes or re-crop jumps; all motion is the master's (`zoom_policy: source_only`). *check: V-CAMERA*
- **H13 Promise integrity.** If the cross-promo line is used, its title is the long-form's exact title (from the creator) and it is on screen ≥ 2.0 s. *check: V-PROMISE + review*
- **H14 Truth & inserts.** Everything shown is the master as published; any third-party span in the chosen part is confirmed by the creator or replaced (§12.5); created cards quote the script verbatim. *check: V-INSERTS, V-CITE*
- **H15 Spelling.** Names, units and technical terms in captions are spelled exactly (glossary from P3); numbers stay as spoken. *check: V-CAPTION spelling list*
- **H16 Audio.** −14 LUFS integrated, true peak ≤ −1.5 dBTP; hard end ≤ 6 f after the last word (NC-8). *check: veos qa*
- **H17 Determinism.** Every frame is a pure function of its index (NC-9); no CSS animation in scenes. *check: veos validate (renderer contract)*

### 2.4 NEVER
- **N1** Never redraw, recolour, re-grade, sharpen, stylise or "enhance" the master's footage. No LUTs, no grain, no vignette, no glow.
- **N2** Never add a banner, headline slab, sticker, emoji, progress bar, chapter marker, logo bug, subscribe button or arrow.
- **N3** Never add a zoom, punch-in, shake, whip, speed ramp, freeze-frame or re-crop jump inside a master shot.
- **N4** Never colour a caption by the face on screen; never mix two speakers in one chunk; never emphasise a word (no bold, colour, size or italic change inside captions).
- **N5** Never cut the reel's in-point after the first word has started (no clipped first syllable) and never open on a band, on black, on a title card or on the master's intro/logo sting.
- **N6** Never include a sponsor read, ad, mid-roll, merch or "link below" span, and never the master's end screen or subscribe animation.
- **N7** Never let a crop cut a baked number, label, title or credit line in half; band the shot instead.
- **N8** Never cover a gap with B-roll from elsewhere in the master to "fix" pacing; reorder only whole sentences with their own pictures (P-SPLICE).
- **N9** Never add music, SFX, risers or a second bed over the master's mix.
- **N10** Never use morphs between fits (a band never animates into full-frame); fits switch on cuts.
- **N11** Never show a created card as if it were the master's footage; it.
- **N12** Never leave a black tail > 0.2 s or an end screen.

Buyer never-items `BN1…` `[VAR]` are added here.

---

## §3 Worlds, layouts, reframe classes, safe zones `[REQ] [DNA; coordinates TUNE ±5%]`

### 3.1 Worlds
| ID | Kind | Look | Carries | Entered / exited |
|---|---|---|---|---|
| **W-master** | footage | The master's own picture, reframed to 9:16 (composed by `veos shots render`) | Everything: host, guests, renders, B-roll, maps | From f0; never left except for W-void spans |
| **W-void** | void | `#000000`, nothing else | Created substitute cards (P-SUBSTITUTE-CARD) and the black around letterbox bands | Hard cut in and out |

Inside W-master the master itself supplies four "sub-worlds" the editor tracks for re-hooks and the reframe decision (not separate tokens): **host world** (the creator to camera in their room, chest-up), **field world** (handheld location / interview footage), **render world** (CAD, animation, simulation), **UI world** (HUDs, screen recordings, diagrams with text).

### 3.2 Layouts and reframe classes
**Stage layouts** (timeline `stage[]`):

| ID | Engine | Rects | Caption | Share |
|---|---|---|---|---|
| **L-master** | `full` | The composed 9:16 master footage, full frame 0–1080 × 0–1920 | fixed_y, cy 1380 | 85–100 % |
| **L-band-black** | `letterbox` | Band x 0–1080, y 656–1264 (`band_h` 608, `cy` 960), fill `#000000`, `face: 0` (fit the whole 16:9 frame), `src` = the inserted clip | fixed_y, cy 1380 (116 px under the band) | 0–15 % |
| **L-band-blur** | `blurfill` | Same band over a blurred copy of itself (`blur_px` 40, `luma` 0: undimmed, measured as bright as the band, `scale` 1.15) | fixed_y, cy 1380 | 0–15 % |
| **L-void** | `hidden` | No footage; W-void black; the card area x 64–1016, y 560–1200 | fixed_y, cy 1380 | 0–8 % |

In the normal (16:9 master) pipeline the stage is `L-master` for the whole reel; the bands of RF-3 shots are composed **inside** the footage by `veos shots render` at exactly the same geometry as `L-band-*` (centred 1080 × 608 band at y 656–1264). `L-band-*` stage layouts are used only for creator-supplied 16:9 clips that are not part of the master and in the vertical-master branch (P8b.4). `L-void` is used only under a created card.

**Reframe classes (one per master shot; decided at P8b):**

| ID | Class | When (decision order: take the first that fits) | `timeline.shots` angle | Result |
|---|---|---|---|---|
| **RF-1** | Face follow | One person is the subject and their face is ≥ 6 % of the frame height for ≥ 50 % of the shot (host to camera, guest interview single, walk-and-talk) | that person's single angle (`kind: host_single` / `guest_single` / `single` in angles.json) | 9:16 crop, face at 17 % of frame height, eyes at 36 % of the crop height, dead-zone follow (12 % of crop, 0.6 s time constant), ≤ 2.0× upscale |
| **RF-4** | Two-shot | Two faces side by side are both the subject (host and guest in one frame) | the two-shot angle (`kind: two_shot`) | Cover crop if both fit 9:16 (they rarely do), else the band |
| **RF-2** | Centre crop | No face is the subject, and the subject **plus any baked text it needs** lie inside the centre window x 0.342–0.658 of the source width (a 9:16 full-height window of a 16:9 frame keeps 31.6 % of its width) | the host single angle (with no face in the shot the compositor holds a centred window sized from the host's median face: full source height on a chest-up master) | Static centred 9:16 window; the master's own camera motion plays inside it |
| **RF-3** | Band | Anything else: baked text/labels/numbers wider than the window, UI/HUD/screens, diagrams, maps with routes, wide establishing action, two subjects far apart, an off-centre subject | the wide angle (`kind: wide`) | Centred 1080 × 608 band at y 656–1264 over a blurred, undimmed copy (blur-fill); on black renders it reads as a letterbox on black |

Rules:
- **RF-2 check (mandatory):** the compositor searches ±3 s for the angle's face; a faceless shot within 3 s of the host's shot can therefore be framed on the host's position. Verify each RF-2 shot's mid frame after render; if the subject or its baked text is cut, make it RF-3.
- **Band backdrop brightness:** the real blurred copy is undimmed (completeness audit: surround luma ≥ band). `dialogue.blur_dim` is **1.0** in tokens, so `veos shots render` composes the blur-fill backdrop at full brightness, matching the creator. Never darken it (no value below 1.0 unless a buyer's own footage needs it for caption contrast).
- **Band look:** today's compositor applies one fallback per reel; use `--fallback blurfill` always (on a black-background render the blurred copy is black, which is the letterbox look of v02 @ 0:58–1:11). Only when ≥ 80 % of the reel's band shots are bright UI on white grounds and the creator prefers bars, use `--fallback letterbox`. (Per-shot choice is engine request ER-1.)
- **Band share:** ≤ 25 % of runtime per reel (SS-6). Evidence: v02 14 %, v03 22 %.
- **Hook:** no band in the first 3.0 s (SS-2).

**Layout schedule rule:** n/a (fits follow the master's shots; there is no layout rhythm).

### 3.3 Stage moves
| ID | Move | Recipe | Use |
|---|---|---|---|
| **G-1** | Fit switch on a cut | 0 frames: the new shot arrives already in its fit (full or band) | Every master cut where the fit changes |
| **G-2** | Cross-shoot splice | T-CUT, 0 f, captions swap on the same frame (measured v03 @ 1:29.87: HUD band → the host at night). No dip. | A splice between two different shoots (wardrobe, room or time of day changes) |
| **G-3** | Void card in/out | Hard cut to `L-void` and back on sentence boundaries | P-SUBSTITUTE-CARD only |

No other stage move exists (no morphs, no panels, no PiP, no stacks).

### 3.4 Layout diagrams
```
L-master, RF-1 (host or guest)              RF-3 band (blur-fill / black)
┌─────────────────────────┐ 0               ┌─────────────────────────┐ 0
│ (IG top UI, keep clear) │ ← y 0–110        │ blurred copy, undimmed  │
│        head top         │ ← y 150–260      │   of the same shot      │
│      ╭──────────╮       │                  │  (black on black renders)│
│      │  FACE    │       │ ← face ≈ 17 % H  ├─────────────────────────┤ 656
│      │ eyes ≈   │       │   (≈ 326 px)     │   16:9 BAND 1080 × 608  │
│      │ 36 % of  │       │                  │   the master's frame,   │
│      ╰──────────╯       │                  │   whole and uncropped   │
│    shoulders / chest    │                  ├─────────────────────────┤ 1264
│   [object title 1230]   │ ← rare, ≤ 3/reel │  [object title: 590]    │ ← above the band instead
│  ── caption cy 1380 ──  │ ← 70 px serif    │  ── caption cy 1380 ──  │ ← 116 px under the band
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
                                            │  y 1140 (24 px)          │
                                            │  ── caption cy 1380 ──   │
                                            └─────────────────────────┘
```

### 3.5 Safe zones and bands
- Meaning text box: x 64–1016, y 110–1500 (NC-5 limits; TUNE ±5 %).
- **Caption band:** centre y 1380 (TUNE 1300–1460), one line, max width 900 px, i.e. x 90–990; ≈ 1345–1415 occupied.
- **Object title band:** full-bleed shots cy 1230 (bottom ≤ 1265, ≥ 80 px above the caption top); band shots cy 590 (above the band top 656).
- **End line band:** cy 1250 (1 line) or 1220 (2 lines), 2.0–3.0 s at the end.
- Nothing drawn in y > 1540, y < 110, or x > 970 between y 900 and 1540.

### 3.6 Presenter rules `[COND: presence ≠ none]`
- Presence is whatever the master shows inside the chosen span (target 5–55 %, longest absence ≤ 90 s). Never insert host shots from elsewhere to raise it.
- RF-1 crops: head top at y 150–260 (evidence: v02 @ 0:00–0:17 host head top ≈ y 150–230), face centred horizontally, never cut at the eyes or forehead.
- Hands that leave the crop are fine (the master's gestures); a pointing hand that points at baked content off-crop is a reason to band the shot (RF-3).
- Nothing ever sits behind the host (no E1).

---

## §4 Colour `[REQ] [roles' meanings DNA; guest colour TUNE]`

### 4.1 Role palette
| Role | Hex | One job | Text on it | Contrast | Brandable |
|---|---|---|---|---|---|
| `primary` | `#FFFFFF` | Host / narrator caption text | `ink` | 21:1 vs the `#000` shadow/stroke; ≥ 4.5:1 on footage via the hairline stroke + soft shadow | no (fixed meaning) |
| `accent` | `#E8CC28` (or the buyer's BV-02 colour) | Guest caption text (every non-host voice) | `ink` | 14.6:1 on `#000`; holds on bright footage through the stroke | **yes** (BV-02), within a warm saturated hue, OKLCH L 0.72–0.90 |
| `ink` | `#000000` | Caption stroke (`#111111`) and shadow, letterbox fill | — | — | no |
| `paper` | `#FFFFFF` | Object titles, end line, created-card text | `ink` | 21:1 on black | no |
| `night` | `#000000` | Void and letterbox ground | — | — | no |
| `muted` | `#B9B9B9` | card kicker | — | 10.4:1 on black | no |

### 4.2 Meanings
- **The axis is voice: host → guest = white → gold.** It answers "who is talking?" without a name plate.
- White everywhere else means "the editor's words" (titles, end line), always in serif.
- The master's own colours (renders, sets, maps) are never altered and never echoed in the editor's layer.
- A buyer's brand colour may replace the gold only; it must stay clearly not-white (TUNE range above). A brand blue or red that fails the lightness range is nudged by `veos templates copy` (contrast) and, if still too dark, rejected at copy time as a DNA change.

### 4.3 Theme packs
OFF (`themes.policy = single`).

### 4.4 Grades
OFF: the master is never re-graded (`grades.footage: null`, no scene grades, no grade events).

### 4.5 Rules
- ≤ 2 editor hues per frame (`max_bright_per_frame: 2`: white + gold); the footage's own hues don't count.
- Coloured caption text always keeps the 1 px `#111111` hairline + `0 2 8 rgba(0,0,0,.75)` shadow, so gold reads on bright maps and white labs (v02 @ 2:24, v01 @ 0:29).
- Never put the gold on anything that isn't a guest's words.

---

## §5 Type & captions `[REQ]`

### 5.1 Font map
| Slot | Family | Weight / style | Font class (TUNE boundary) | Used for |
|---|---|---|---|---|
| `serif` | **Source Serif 4** (bundled, variable 200–900, opsz 8–60) | 600 captions; 500 end line; 600 card body | transitional text serif 500–700 (alternative: EB Garamond 600) | Speech captions, end line, created-card text |
| `title` | **EB Garamond** Italic (bundled) | 500 italic | old-style italic serif 400–600 (alternative: Instrument Serif Italic) | Object titles |

Only bundled OFL fonts. Logos are never set as type for a brand that isn't the creator's.

### 5.2 Headline element
OFF (`type.headline.kind = none`): the style's frame 0 is the moving master + caption (D2). No banner, pill, lockup or title card ever appears.

### 5.3 Caption system profile CS-1 `[DNA mechanics; size, weight, y TUNE; language VAR]`
`captions.profiles.CS-1` extends `lib:veritasium` and tunes it to the measured frames.

| Group | Value |
|---|---|
| Mode | `full`, role `primary`, `mute_safe` |
| Chunking | unit `group`; 1–4 words per chunk (engine settles on 1–3; measured average 2.3); max 22 characters per line; **1 line**; never split a name, number or unit; a sentence end always breaks (`punct_break`); a pause ≥ 0.9 s always breaks |
| Timing | lead **1 frame** before the first word; min hold 0.2 s/word; swap **hard, 0 f** (E6); after the last word of a phrase the chunk holds 0.3 s (`tail_s`), then the band is **blank** during the pause (`pause_hold_s: 0`): blank pauses up to 2.0 s are the style's breaths (v03 @ 0:49–0:51, 1:06–1:08) |
| Skin | Source Serif 4, **600**, **70 px** (TC-subtitle), case **as spoken** (sentence case, punctuation kept: "kilometers per hour.", "from 96% to 10%"), tracking 0, colour by speaker, **hairline stroke 1 px `#111111`**, soft shadow `0 2 8 rgba(0,0,0,.75)`, line height 1.1, **no container** |
| Position | `fixed_y` **cy 1380**, cx 540, max width 900, centred; identical in every layout and fit (above, inside or under a band); `avoid_face: true` |
| Speakers | `host` → `primary` white upright; `narrator` → `primary` white upright; `guest` → `accent` gold upright. Keys match the word labels from `veos speakers name … :host / :guest`. One speaker per chunk; overlapping back-channels are dropped (only the dominant voice is captioned) |
| Emphasis | **none** (no bold, colour, size or italic change inside captions) |
| Variants | karaoke / two-tier / duet / kinetic stack: none |
| Hide rules | hidden only during an added T-DISSOLVE (`hide: transitions`); never hidden or re-timed at master cuts or splices (chunks run across cuts, completeness audit), during stage morphs (none exist), and nowhere else; captions are never hidden under object titles (they don't overlap) |
| Language | Latin script; `keep_english_terms`; no spelling normalisation (verbatim speech); profanity mask `inner` (S**T); glossary from P3 (names, units, terms) |

Worked chunking (what the engine produces from a typical narration, verified on a test transcript): "One thing / that makes / this research / so tricky / is that antimatter / is relatively slow / to make." → pause, band blank → (gold) "The only / concept basically / to overcome / this problem / is to move / the particles." → (white) "And it works."

### 5.4 Other text systems
| System | Class | Recipe | Hold | Limits |
|---|---|---|---|---|
| **Object title** (P-OBJECT-TITLE) | TC-label (68 px ≥ 40) | EB Garamond Italic 500, 68 px, `paper`, tracking +0.02 em, shadow `0 2 6 rgba(0,0,0,.7)`, centred; cy 1230 on full-bleed shots, cy 590 on band shots; in: opacity 0→1 + y +12→0 px over **8 f** expo-out, starting 2 f before the object's name is spoken; out: opacity 1→0 over **6 f** | 1.5–4.0 s, ends at or before the next master cut | ≤ 3 words, 1 line, ≤ 3 per reel, ≥ 20 s apart; only when the master shows the object and does **not** already show its name |
| **End line** (P-CROSS-PROMO) | TC-label (44 px) | Source Serif 4 500, 44 px, `paper`, sentence case, shadow as captions, centred at cy 1250 (2 lines: cy 1220, line height 1.15), ≤ 36 characters per line; in 8 f opacity; no exit (the reel hard-ends under it) | 2.0–3.0 s, the last sentence | Only when BV-08 = `cross_promo`; text "Full video: <exact long-form title>" (+ "on YouTube" or the platform the creator names) |
| **Created card text** (P-SUBSTITUTE-CARD) | kicker TC-legal 26 px; body TC-label 52 px; label TC-legal 24 px | Kicker = the outlet / source name in caps, `muted`, tracking 0.12 em, y 600; body = the verbatim quote or headline, Source Serif 4 600, 52 px, `paper`, ≤ 3 lines × 26 characters, centred y 660–1080; | For the spoken span it covers (≥ 1.5 s) | Only for an unconfirmed third-party span that can't be trimmed |
| **Redaction** (P-REDACT) | — | Gaussian blur 24 px over the identifier's rect + 12 px margin, keyframed every 6 f to follow it | The identifier's whole on-screen time | Any email, phone number, address, ID or key visible in the master (NC-14) |

Lower-thirds, name plates, chips, stickers, step chips and hero numbers: **none** (the master names its guests in speech; the colour says who speaks).

### 5.5 Language and number rules
- **Spelling:** verbatim speech; technical terms, names and units exact (glossary). Do not "correct" the speaker's grammar.
- **Numbers:** exactly as spoken and written by the transcript ("16.2 million", "99.9%", "614 days"); never converted, never compacted, never turned into figures.
- **Hinglish masters:** `[hinglish, hinglish, Latn]` (transliterated, English terms verbatim) or `[hinglish, en, Latn]` (translated; then a guest's quoted words keep their meaning verbatim, NC-13). Same skin and colours.
- **Hindi masters (`[hi, hi, Deva]`):** captions use **Noto Serif Devanagari** 600 at 70 px (`captions.devanagari_family`), so the serif look holds in Hindi. No italic in Devanagari (object titles in Devanagari use weight 600 upright).
- **BV-06:** Indian masters switch number grouping to Indian only for drawn text (cards); captions stay as spoken.

---

## §6 Hook system `[REQ]`

**Hook title (every style, 8 Oct 2026; above anything below):** the on-screen title promises the viewer something: an outcome they want, a curiosity gap, or who it's for ("How to go viral as a doctor creating content", not the label "Reels for Doctors"). It doesn't have to repeat the spoken words; it has to be true to what the reel delivers. A title shown as someone's words (in quotes) is still word for word. This section sets the title's shape (lines, sizes, word limits, case, the keyword device), never its voice. Write 8–10 candidates from the formulas below plus the proven patterns ("How to X as a Y", "Why your X isn't working", "The X nobody tells you", "Stop doing X", "Your X vs mine", a number or a contrast), score them on outcome, curiosity, who it's for and brevity, check the best against the stopper tests, and pick; any "write 3" below means this, and the next two go to the storyboard as alternates. A style with no on-screen title applies this to its post title.

### 6.1 Stopper tests
| Test | Used | This style's number |
|---|---|---|
| ST-1 Thumbnail | **no** | The style has no headline; frame 0 at 25 % shows a moving subject, which is enough (v03 passes, v01/v02 rely on voice) |
| ST-2 Mute | **yes** | The first 3 s of captions state a complete claim or problem on their own |
| ST-3 Motion at f0 | **yes** | Live footage moving at f0 (render camera, gesture, handheld) |
| ST-4 Read time | no | No headline to read |
| ST-5 Change count | **yes** | ≥ **4** weighted SCs in 0–3 s (caption swaps count 1.0; measured 5–6) |
| ST-6 Payoff-by | **yes** | The strongest image of the opening is on screen by **1.0 s** (it is the f0 shot); the first sentence completes by 3.5 s |

### 6.2 Default archetype: HA-14 Cold authority `[DNA]`
**Formula:** start mid-thought on the master's strongest moving image, with the first caption already running; let the first sentence state a paradox, a mechanism in action, or a problem; hold the shot (no cut) until the second sentence lands; the first cut changes world.

| t | Picture (the master, reframed) | Caption (CS-1) | Layout / camera | Sound |
|---|---|---|---|---|
| **f0** (0.00) | The in-point frame: a render in motion, the host mid-gesture, or a guest with the object; RF-1 or RF-2 full-bleed, never a band | Chunk 1 (1–3 words) already on: in-point 0.04–0.10 s before the first word | L-master; the master's own camera move (orbit, dolly, handheld) is running | The master's mix from f0; no added hit |
| 0.0–1.0 | Same shot; in-shot motion continues (a beam pulse, a hand sweep, a drift) | Chunk 1 → chunk 2 (hard swap ≈ 0.6–0.8 s) | no cut | — |
| 1.0–2.0 | Same shot; the subject noun becomes visible or active (the ring lights, the ship nears the hole) | Chunk 3 lands on the subject noun ("the antiprotons", "a black hole") | no cut | — |
| 2.0–3.0 | Same shot; in an animation master the baked payoff often lands here (v03 @ 2.2–3.0: the red band crushes the ship, the prohibition ring slams in) | Chunks 4–5; the first sentence ends with its period by ≤ 3.5 s | no cut | — |
| 3.0–12.0 | The shot holds as the master holds it (v01 11.5 s, v02 17.75 s, v03 4.6 s) | Sentence 2 states the stake or the problem | no cut unless the master cuts | — |
| 4.6–18 | **First cut = first world change** (render → host, host → field, animation → animation) on a sentence boundary | Continues | G-1 | — |

Stopper results on the evidence: v01 changes 0–3 s ≈ 5, v02 ≈ 5, v03 ≈ 6; all pass ST-2/3/5/6.

**Three evidence-drawn variants of HA-14** (choose by what the sub-story's first shot is):
| Variant | First shot | First line shape | Evidence |
|---|---|---|---|
| **HA-14a Image-first** (default when a render exists) | A render or animation in motion, RF-2 | A mechanism in action or a paradox: "<subject> <does something surprising>" | v01 @ 0:00 "Strong electric fields in the accelerator slow down the antiprotons"; v03 @ 0:00 "You can never see anything enter a black hole." |
| **HA-14b Host-first** | The host to camera, mid-gesture, RF-1 | A problem statement: "One thing that makes <field> so <hard> is…" | v02 @ 0:00 "One thing that makes this research so tricky…" |
| **HA-14c Guest-first** (allowed, not in evidence) | A guest holding or pointing at the object, RF-1, gold caption at f0 | The guest's strongest one-sentence claim | Allowed by D4; use only when the guest line passes SS-1 better than any host line |

### 6.3 Allowed alternates `[DNA list; VAR choice per reel]`
**HA-10 Host flash → subject** (the host's first 2–4 words on camera, then the cut to the subject by 0.7 s; the subject image is the payoff):

| t | Picture | Caption | Example (N1 science) | Example (N2 money) |
|---|---|---|---|---|
| f0–0.7 | Host RF-1 mid-word | Chunk 1–2 | "This machine…" | "Every fund manager…" |
| ≤ 0.7 | Master cut to the subject (render / chart B-roll / location), RF-2 or RF-1 | Chunk 3 | (the heat pump cutaway render) | (the trading-floor B-roll) |
| 0.7–3.5 | Subject holds | Sentence completes | "…moves four times more heat than it uses." | "…has to beat a fund that does nothing." |
Use only when the master itself cuts from host to subject within 0.7 s of a sentence start (never add the cut, R-1).

**HA-15 Atmosphere** (an animation-led master whose first sentence is slow to arrive; the moving picture carries 1–2 s, the claim lands by 5 s):

| t | Picture | Caption | Example (N1) | Example (N2) |
|---|---|---|---|---|
| f0 | Moving render, RF-2 | First chunk at f0 (H1 still holds) | "Imagine…" | "In 1975…" |
| 0–5.0 | The render develops | The claim lands by 5.0 s | "…a city with no power lines." | "…one man started a fund that refused to pick stocks." |
Use only when no sentence in the sub-story's first 20 s passes SS-1 inside 3.5 s.

### 6.4 Hook pairs by topic `[NICHE]` (pair type for HA-14: question → answer)
| Topic | The question the cold open raises | Where the answer lands | First shot |
|---|---|---|---|
| [N1: science] Heat pumps | "How can a machine move more heat than the energy it uses?" | Mechanism render at ≈ 40–70 s; engineer guest (gold) proves it at ≈ 80 s | Cutaway render of the refrigerant loop, RF-2 |
| [N1: science] Black-hole time | "Why does nothing ever seem to fall in?" | Animation of the slowing clock ≈ 20–35 s | Animation, RF-2 |
| [N1: engineering] Tunnel boring machine | "How does a 1,000-tonne machine steer underground?" | Guest operator in the cab ≈ 50 s | Render of the cutter head turning, RF-2 |
| [N2: money] Index funds | "Why do most professional stock pickers lose to a fund that does nothing?" | Economist guest (gold) ≈ 45 s; chart B-roll band ≈ 70 s | Host mid-gesture, RF-1 |
| [N2: business] Shipping containers | "How did one steel box cut the cost of trade by 90 %?" | Port B-roll + historian guest ≈ 60 s | Crane B-roll, RF-2 |
| [N2: money] Inflation | "Where does the money actually go when prices rise?" | Host whiteboard band ≈ 50 s | Host to camera, RF-1 |

### 6.5 First-line writing (instead of a headline) `[DNA formula; NICHE examples]`
You don't write the hook; you **choose** it from the master. The chosen first sentence must be:
- **≤ 14 words, self-contained (SS-1), present tense or timeless**;
- one of three shapes: **paradox** ("You can never see anything enter a black hole."), **mechanism in action** ("Strong electric fields … slow down the antiprotons."), **problem** ("One thing that makes this research so tricky is…");
- spoken over a moving, full-bleed picture (SS-2).
Banned openings: greetings, "In this video", "So,", "Today", "Welcome back", a sponsor line, a rhetorical "Did you know…" stacked on nothing.
**Pick 3 candidates and rank them by the stopper tests.** The post title (App. A) is written separately and never shown on screen.

### 6.6 Hook sound
The hook is the master's own mix from f0 (no added hit, no riser, no bed). See §11.

### 6.7 CTA `[DNA device set; VAR values]`
| Device | Spoken | On screen | Hold | Where |
|---|---|---|---|---|
| **none** (template default) | nothing | nothing; the reel ends on the implication sentence | — | — |
| **post_only** | nothing | nothing; the post text carries the pointer ("Full video on my channel: <title>") | — | post |
| **cross_promo** | nothing (never add a voice line) | The end line "Full video: <exact long-form title>" (§5.4), cy 1250, over the last shot | 2.0–3.0 s, ending with the hard end | last sentence |
The buyer's chosen device: **{{BV-08.device|none}}**.
Never: a subscribe button, the master's end screen, a keyword card, a QR, "link in bio" stickers. If the master's own last line is a channel plug, the span fails SS-5.

---

## §7 Structure & cadence `[REQ] [DNA]`

### 7.1 Structure type: `explainer`
| Unit | Share of 110–150 s | What it does | Typical world | Evidence (v02, 153 s) |
|---|---|---|---|---|
| **HOOK** (problem or paradox) | 3–15 s (≤ 15 %) | The cold-open sentence + its stake | Render or host | 0:00–0:17 host: "One thing that makes this research so tricky…" |
| **MECHANISM** | 30–45 % | How it works, over renders and field footage | Render, field | 0:18–0:58 BASE poster, p̄ render, CPT band, Earth field, lab |
| **PROOF** | 25–40 % | The guest shows or says it works; the host reacts | Guest (gold), field | 1:08–1:47 letterbox trap, guest office, "And it works." |
| **IMPLICATION** | 10–20 % | Why it matters / what follows; ends on a period | Host, render, map | 2:06–2:32 "then why not ship it?" → map "research institutions." |

The master decides the order inside these limits; the editor only checks that all four are present (SS-3).

### 7.2 Markers
`markers: none (spoken only)`: no numerals, chapter chips or progress rails. The master's own on-screen labels (baked "ELENA", "16,200,000 km/h", "CERN") are the only labels (v01 @ 0:33, 0:41; v02 @ 2:07).

### 7.3 Unit ritual: the world rotation
The style's recurring sequence is not an item ritual but a **world rotation** inside each unit, which you protect when choosing and splicing:
1. **Claim in one world** (host to camera, or the narration over a render): 1–3 sentences, one shot or one master cut sequence.
2. **Mechanism in the render/field world:** the picture shows the thing named, held 4–15 s per shot (P-RENDER-HOLD).
3. **Proof in the guest world** (gold captions), with the master's own host reaction or question in between (P-REACTION-KEEP, P-VOICE-OVER-PICTURE).
4. **Return** to the host or the render for the next claim.
A sub-story that stays in one world for > 45 s fails SS-4 in practice; prefer one that rotates.

### 7.4 Open loops and re-hooks
- **Loop types used:** the question the cold open raises (6.4) and the "but…" turn. Both are paid off inside the span (SS-3).
- **Re-hooks (long class): every ≤ 25 s** after the hook (`structure.rehook_every_s: 25`). A re-hook is one of:
  1. a **world change** on a sentence start (host → render, render → guest);
  2. a **turn sentence** ("But…", "Here's the thing", "The problem is…", "So why…");
  3. a **question** line (host to guest, or rhetorical: "then why not ship it?", v02 @ 2:08);
  4. a **guest's first line** (the first gold caption);
  5. a **new striking image** (a render reveal, a map, a record number baked in).
  Mark the beat `rehook: true`. Evidence spacing: v02 re-hooks at ≈ 0:18, 0:32, 0:58, 1:12, 1:23, 1:40, 2:00, 2:07 (≤ 26 s apart).
- **Intro cap:** the HOOK unit ≤ 15 % of the runtime.

### 7.5 Rhythm and energy curve
- Information-only beats; humour only when the master has it (a guest's laugh, v02 @ 1:30) and never cut to.
- Energy: flat-calm with one lift: the PROOF unit's "it works" moment (v02 @ 1:40 "And it works.") or the biggest render. The end is quiet and certain: an implication statement, then the hard end.
- Speech rate stays as recorded (≈ 2.4 words/s); never speed up the master.

### 7.6 Cadence (state changes)
| Token | Value | Why |
|---|---|---|
| `sc_per_10s` | **[6, 15]** | Caption swaps (≈ 1 per 0.6–1.0 s, weight 1.0) + master cuts (0.5–2.3 per 10 s); measured 8–13 |
| `hook_sc_3s` | **4** | v01 ≈ 5, v02 ≈ 5, v03 ≈ 6 |
| `max_gap_s` | **2.5** | Blank-caption pauses ≤ 2.0 s plus a 0.3 s tail |
| `max_static_s` | **3.0** | The master's in-shot motion and live footage count as continuous motion; only black holds (v03 @ 1:06–1:08) approach the limit |
| `caption_weight` | **1.0** | Captions are primary |
| `cuts_per_min` / `median_shot_s` | **null** (not checked) | The cut rhythm is the master's (3.3–13.6 cuts/min, median shot 2.3–4.6 s); the editor neither adds nor removes cuts to hit a number |

---

## §8 Visual system: reframe patterns `[REQ]`

### 8.1 Graphics role and budget
`graphics: passthrough`. The editor's drawn layer is limited to **4 overlay patterns** (PV-4 allows ≤ 5 graphic patterns): P-OBJECT-TITLE, P-CROSS-PROMO, P-SUBSTITUTE-CARD, P-REDACT. Their runtime share is ≤ 5 % (titles ≤ 3 × 4 s, end line ≤ 3 s). The rest of this section is the **cut and reframe grammar** (19 patterns of type `cut` / `stage` / `footage-treatment`), which is where the craft is. "Numbers become pictures" does **not** apply: numbers stay in the captions as spoken, and only the master's baked numbers are pictures.

### 8.2 Families
| ID | Family | Source class | What the creator supplies |
|---|---|---|---|
| **B-1** | Host footage (to camera, on location) | source-baked (master) | the master |
| **B-2** | Guest / interview footage | source-baked (master) | the master + guest names |
| **B-3** | Renders, animation, simulation, CAD | source-baked (master) | the master |
| **B-4** | Field B-roll (labs, places, objects, details) | source-baked (master) | the master |
| **B-5** | Baked UI, diagrams, maps, on-screen labels | source-baked (master) | the master |
| **B-6** | Editor overlays (object title, end line, redaction) | engine | the long-form title (for the end line) |
| **B-7** | Third-party spans inside the master | creator-supplied third-party (confirmed at P11), else replaced by **B-8** | confirmation |
| **B-8** | Created substitute card (quote / headline / diagram) | engine (created, labelled) | nothing |

### 8.3 Pattern specs
Frames are at 30 fps. "f" = frames.

**Overlay patterns (engine-drawn, z5/z3; ≤ 5 allowed by PV-4):**
| ID | Name | Type | On screen | Motion recipe | When | Family / class | Needs |
|---|---|---|---|---|---|---|---|
| **P-OBJECT-TITLE** | Italic object title | annotation | 1–3 words, EB Garamond Italic 500 68 px, white, centred at cy 1230 (full) / 590 (band) | In 8 f (opacity 0→1, y +12→0, expo-out) starting 2 f before the name is spoken; hold 1.5–4.0 s; out 6 f before the next master cut | A line names a specific new object, device or place for the first time, the master shows it, and the master does not show its name | B-6, TC-label | none |
| **P-CROSS-PROMO** | End line | overlay | "Full video: <title>" in serif 44 px, cy 1250 | In 8 f opacity; no exit (hard end) | BV-08 = cross_promo, over the last sentence | B-6, TC-label | the exact title |
| **P-SUBSTITUTE-CARD** | Created card | overlay (insert) | `L-void` black; kicker (source name, 26 px caps, `muted`) y 600; verbatim quote/headline 52 px serif ≤ 3 lines centred y 660–1080; captions keep running at 1380 | Hard cut in on a sentence start; body fades in 6 f; hard cut out on the next sentence start | An unconfirmed third-party span that can't be trimmed (§12.5) | B-8, TC-label + TC-legal | insert record |
| **P-REDACT** | Identifier blur | footage-treatment | Gaussian blur 24 px over the rect + 12 px | Keyframes every 6 f following the rect; on for the identifier's whole visible time | An email, phone, address, ID or key is legible in the master (NC-14) | B-6 | keyframes |

**Cut and reframe patterns (the craft; no drawing):**
| ID | Name | Type | What happens | Recipe (frames / rules) | When |
|---|---|---|---|---|---|
| **P-COLD-OPEN** | Cold open | cut | The reel's in-point | In-point 1–3 f before the first word's onset; first shot RF-1/RF-2; no fade-in, no black frame | Always, f0 |
| **P-HOST-FOLLOW** | Host follow | stage | RF-1 on the host | Face 17 % of H, eyes at 36 % of the crop, dead zone 12 %, 0.6 s spring; ≤ 2.0× upscale | Host to camera or on location |
| **P-GUEST-FOLLOW** | Guest follow | stage | RF-1 on a guest | Same as host; the guest's own single angle | Guest interview singles, video-call guests |
| **P-VOICE-OVER-PICTURE** | Voice over another picture | cut | The master shows the host's reaction or B-roll while a guest talks | Keep the master's picture and its fit; captions stay gold for the guest's words (R-3) | v02 @ 1:29–1:30, 2:10–2:15, 2:21; v01 @ 0:54–0:57 |
| **P-CENTRE-CROP** | Centre window | stage | RF-2 on a faceless shot | Static centred full-height 9:16 window; the master's own camera motion plays inside; verify the frame after render | Renders and B-roll whose subject sits in x 34–66 % |
| **P-BAND** | Band | stage | RF-3 | Centred 1080 × 608 band at y 656–1264 over its blurred, undimmed copy (black on black grounds); hard cut in and out; caption at 1380 under it | Wide diagrams, UI, baked text, two-shots, routes |
| **P-TWO-SHOT** | Two-shot | stage | RF-4 | The two-shot angle; band when both faces don't fit 9:16 | Host and guest in one frame |
| **P-WALK-AND-TALK** | Location follow | stage | RF-1 on handheld field footage | Same follow; if the face is < 6 % of H for > 50 % of the shot, band it instead | v01 @ 1:05–1:24, v02 @ 1:15–1:22 |
| **P-DETAIL-INSERT** | Detail insert | stage | RF-2 on a macro detail (a part, a label) under narration | Centre window; keep its master length (often 1–3 s) | v01 @ 0:54–1:04 |
| **P-RENDER-HOLD** | Long render hold | cut | A render shot held as long as the master holds it | No cut, no crop change; cadence from captions; ≤ 20 s (if longer, it is still kept: the master's choice) | v01 @ 0:00–0:11.5, v03 @ 0:05–1:29 |
| **P-BAKED-TEXT-SAFE** | Baked text kept whole | stage | A shot with a baked label, number or credit | The crop must contain the whole text (with 24 px margin) or the shot is banded | v01 @ 0:33 "ELENA", 0:41 "16,200,000 km/h"; v03 @ 1:37 credit lines |
| **P-MAP-FRAME** | Map | stage | A baked map | RF-2 centred on the named place when the line names one place; RF-3 when routes or several places matter | v02 @ 2:07–2:32 |
| **P-HUD-BAND** | UI / HUD / simulation | stage | Screen-like content | Always RF-3 band (blur-fill) | v03 @ 1:09–1:29, 1:32–1:34, 1:45–1:46 |
| **P-SPLICE** | Splice | cut | A join between two master spans | Hard cut at a sentence boundary, 0.04–0.10 s before the next sentence's first word; the join carries the engine's 8 ms equal-power audio crossfade; ≤ 3 per reel | Skipping a digression, a sponsor, a repeated point |
| **P-DIP-SPLICE** | Cross-shoot splice (id kept; no dip) | cut | A splice across shoots | Hard cut, 0 f, on a sentence boundary; the next caption chunk appears on the same frame (measured v03 @ 1:29.87) | Different wardrobe/room/time (v03 @ 1:29→1:30 host from another shoot) |
| **P-PAUSE-BREATH** | Pause breath | cut | The master's pause kept | Caption band blank; pause ≤ 2.0 s kept whole; > 2.0 s trimmed to 1.2 s (only when the picture doesn't change) | v03 @ 0:49–0:51, 1:06–1:08 |
| **P-REACTION-KEEP** | Reaction kept | cut | The master's own listener reaction or laugh | Keep it exactly where the master put it; never add, extend or move one | v02 @ 1:15–1:22, 2:10–2:15 |
| **P-HOST-RETURN** | Host return | cut | The implication unit returns to the host (or a final render) | Prefer a span whose last 8–20 s is host to camera or the payoff render | v02 @ 1:51–2:06; v03 @ 1:44 |
| **P-LAST-LINE-END** | Last line end | cut | The reel ends | Out-point 3–5 f after the last word ends, last caption still on; no end screen, no black tail. Variant T-END-FADE when the last shot is a render whose narration has already ended: fade the picture to black over 5 f, caption gone (v03 @ 1:49.73) | All reels (fade variant ≤ 1 in 3 reels) |

### 8.4 Line → pattern lookup `[NICHE]`
| Line type (niche-neutral) | Primary | Alternates | N1 science example | N2 money/business example |
|---|---|---|---|---|
| Opening paradox / problem | P-COLD-OPEN + P-CENTRE-CROP or P-HOST-FOLLOW | P-RENDER-HOLD | "A heat pump moves more heat than it uses." | "Most fund managers lose to a fund that does nothing." |
| Mechanism over a render | P-RENDER-HOLD (P-CENTRE-CROP) | P-BAND if baked labels are wide | Refrigerant loop cutaway | Animated money-flow diagram |
| Names a new object for the first time | P-OBJECT-TITLE (only if unnamed on screen) | none | "the compressor" over its render | "the index fund" over a fund-document B-roll |
| A number with a unit | caption only (as spoken); P-BAKED-TEXT-SAFE when the number is baked | — | "four kilowatts of heat" | "a 2 % fee" |
| Guest explains | P-GUEST-FOLLOW | P-TWO-SHOT | engineer in the plant room | economist on a video call |
| Guest voice continues over B-roll or the host | P-VOICE-OVER-PICTURE | — | engineer over the outdoor unit B-roll | economist over the trading-floor B-roll |
| Host asks on location | P-WALK-AND-TALK | P-BAND | "So where does the heat come from?" | "So who pays the fee?" |
| Where / route / global spread | P-MAP-FRAME | P-BAND | heat-pump installs by country map | container routes map |
| Screen, UI, simulation, chart with text | P-HUD-BAND | — | thermodynamic simulation | fund-performance chart |
| A detail being named ("this valve", "the fine print") | P-DETAIL-INSERT | P-CENTRE-CROP | the expansion valve macro | the fee line in a prospectus |
| A laugh or aside in the master | P-REACTION-KEEP | — | guest laughs at the host's guess | host's raised eyebrow |
| A digression, sponsor or repeat in the way | P-SPLICE (cut it out) | P-DIP-SPLICE across shoots | a tangent on history | the sponsor read |
| Why it matters | P-HOST-RETURN + P-LAST-LINE-END | final render | "…and that's why your next boiler might be a fridge." | "…so the cheapest fund is usually the winning one." |
| Third-party clip/quote inside the master | keep if confirmed; else P-SUBSTITUTE-CARD | trim around it | a news clip about energy prices | a TV interview with a CEO |
| A legible personal identifier | P-REDACT | — | a lab email on a whiteboard | an account number on a statement |

### 8.5 Data and truth rules
- No figures, counters or charts are built (`data_figures` OFF). Numbers appear only as spoken (captions) or as baked in the master.
- A baked number must stay whole on screen (P-BAKED-TEXT-SAFE) so it is never misread ("16,200,000" cut to "6,200,00").
- Never splice two sentences so that a number attaches to a different subject (NC-6, NC-13).

### 8.6 Comedy layer
OFF (`tone.comedy = off`).

### 8.7 Asset rules
- The master is the only footage. Never pull shots from other videos, stock or other parts of the master to fill a gap (N8); a splice brings whole sentences with their own pictures.
- Created visuals are only P-SUBSTITUTE-CARD (labelled) and P-REDACT.
- Logos: never set or fetched; the master's own baked logos stay as they are.
- Third-party spans: ask, then trim or create (§12.5).

### 8.8 Density and variety
- Drawn overlays: ≤ 3 object titles + ≤ 1 end line per reel; often zero (an empty `plan/scenes.js` validates; never add a dummy scene).
- State changes: from captions and the master's cuts (§7.6); never add events to hit a number.
- Fits: no more than 2 full ↔ band switches in any 6 s (R-9).

---

## §9 Transitions & shot grammar `[REQ] [DNA]`

### 9.1 Library
| ID | Transition | Frames | Recipe | SFX role |
|---|---|---|---|---|
| **T-CUT** | Hard cut | 0 | The master's cuts and P-SPLICE joins | none |
| **T-DISSOLVE** | Cross-dissolve | 10 | Linear opacity cross-fade over 10 f; captions hidden on the 10 f only if a chunk would straddle it | none |
| **T-END-FADE** | Fade to black at the end | 5 | Linear opacity 1 → 0 to `#000000` over the last 5 f, after the last word, no caption (v03 @ 1:49.73–1:49.94). Built in: write `"end_fade": 5` on the timeline (core fades the whole frame to `#000000` over the last 5 f); no scene | none |
| **T-END** | Hard end | 0 | Out-point 3–5 f after the last word | none |

### 9.2 Grammar
| Boundary | Use | Never |
|---|---|---|
| Frame 0 | P-COLD-OPEN (no transition) | A fade-in, a black frame, a logo sting |
| Inside the master's sequence | the master's own cut (T-CUT) or its own dissolve (kept as is) | an added transition |
| Splice, same shoot | T-CUT on a sentence boundary | a cut mid-sentence |
| Splice, different shoot / wardrobe / room | T-CUT (v03 @ 1:29.87) | a dip, a whip, a zoom-through |
| Two renders of the same object joined at a splice | T-DISSOLVE | — |
| Full ↔ band | T-CUT (G-1) at the master cut | a morph |
| Last word | T-END | a black tail, an end screen |

### 9.3 Shot grammar R-…
| ID | Rule |
|---|---|
| **R-1** | **The master's cuts are the reel's cuts.** No new cut inside a master shot, except a P-SPLICE join at a sentence boundary. |
| **R-2** | **One fit per master shot.** The reframe class (and its angle) changes only at master cuts or splices, ±0 f. No re-crop jumps, no punch-ins. |
| **R-3** | **Colour follows the voice, not the face.** A guest heard over the host's reaction or over B-roll stays gold; the host heard over a guest's shot stays white. |
| **R-4** | **Never cut on a speaker handover the master didn't cut on.** Handovers are shown by colour alone. |
| **R-5** | **Reactions are the master's.** Keep the master's listener cutaways; never insert, extend or move one. |
| **R-6** | **Camera motion is the master's.** Keep dollies, orbits and handheld; add none (`zoom_policy: source_only`). |
| **R-7** | **Follow calmly.** RF-1 uses the compositor's dead-zone operator (dead zone 12 % of the crop, critically damped, 0.6 s); never hand-keyframe a crop faster than that. Measured: the real crops are near-static per shot (background drift ≤ 2 % per frame, all from gestures; v02 0:00–0:17.7), so prefer a wide dead zone over a centred face. |
| **R-8** | **No flicker.** A master shot shorter than 0.8 s takes the fit of the longer neighbour it belongs to (a flash frame never switches full → band → full). |
| **R-9** | **≤ 2 fit switches in any 6 s.** If the master alternates faster (a diagram, the host, the diagram), band all three. |
| **R-10** | **Splices are rare and clean:** ≤ 3 per reel, each on a sentence boundary, each passing "would a viewer notice?" (same topic, same tense, no dangling reference). |

### 9.4 Budget
Per reel (110–150 s): added T-DISSOLVE ≤ 2, splices ≤ 3; everything else is the master's. The same added transition never 3× in a row.

---

## §10 Motion, camera, layers, finishing `[REQ] [DNA; motion tokens TUNE ±15%]`

### 10.1 Motion tokens
| Token | Value |
|---|---|
| Caption lead | 1 f before the first word |
| Caption swap | hard, 0 f (E6) |
| Caption tail into a pause | 0.3 s hold, then the engine's exit |
| Overlay lead | 2 f before the trigger word |
| Object title in / out | 8 f (opacity + y +12 → 0, expo-out `cubic-bezier(0.22, 1, 0.36, 1)`) / 6 f (`cubic-bezier(0.64, 0, 0.78, 0)`) |
| End line in | 8 f opacity |
| Card body in | 6 f opacity |
| T-DISSOLVE | 10 f linear |
| T-END-FADE | 5 f linear |
| Holds | Titles ≥ 1.5 s and ≥ 10 f after full; text ≥ 0.25 s per word |

### 10.2 Footage camera
`zoom_policy: source_only`. No Z-presets exist in this style. All motion inside the frame is the master's. The only crop motion is the RF-1 dead-zone follow.

### 10.3 Canvas camera
OFF.

### 10.4 Layer order (back to front)
1. World `W-void` (`#000000`).
2. Stage footage: the composed master (`work/multicam/footage.mp4`), with bands and blur-fill composed in.
3. P-REDACT blurs (z3).
4. P-SUBSTITUTE-CARD text (z5, over `L-void`).
5. P-OBJECT-TITLE / P-CROSS-PROMO (z5).
6. Captions (z7, `__subtitles`).
No z8–z11 elements exist.

### 10.5 Finishing
None: no grain, no vignette, no glow, no sharpening, no grade (N1). Output 1080 × 1920, 30 fps.

---

## §11 Sound contract (minimal) `[REQ] [VAR]`
| Line | Decision |
|---|---|
| **Cue moments** | **none** (`cue_moments: []`): the master's mix already carries its music and effects. A buyer may enable `transitions` only (a soft cue on a splice), never more. |
| **Meme cues** | off (comedy off) |
| **Music bed** | **off**: never add a bed over the master |
| **Ducking** | n/a: the master's mix is the voice track; it is kept whole (the engine conforms it to 48 kHz mono; ER-4 asks for stereo) |
| **Loudness** | −14 LUFS integrated, true peak ≤ −1.5 dBTP; hard end ≤ 6 f after the last word (NC-8). Splices use the engine's 8 ms equal-power crossfade; no audio offsets. |

Mirrored in `tokens.json → sound`.

---

## §12 Footage, shot list, fallbacks, inserts `[REQ]`

### 12.1 Setups `[DNA what the style assumes; VAR the buyer's actual master]`
| Setup | What the style assumes |
|---|---|
| **M: the master** | One finished long-form video owned by the creator: 16:9, 2160p preferred (1080p accepted), any fps (conformed to 30), one stereo mix with voice + music, the creator's graphics/renders baked in. The host's framing is typically chest-up, head top in the top 10–15 % of the 16:9 frame, face roughly centred (so RF-1 crops cleanly). |

Nothing is shot. What helps most: renders and B-roll that keep their subject in the centre third (they reframe full-bleed instead of banding).

### 12.2 Shot list
| ID | Item | Spec | Count | Must / optional | Formats |
|---|---|---|---|---|---|
| **SH-1** | The finished master | 16:9, ≥ 1080p, the published cut | 1 | **must** | F-A |
| **SH-2** | 4K export of the master | 2160p, same cut | 1 | optional | F-A |
| **SH-3** | Cast list | the host's name; every guest's name in the chosen part | 1 | **must** | F-A |
| **SH-4** | The long-form's exact title + platform | for the end line | 1 | optional (needed for cross_promo) | F-A |

### 12.3 Fallbacks
| ID | For | What the engine does instead | Fidelity cost | Result |
|---|---|---|---|---|
| **FB-1** | SH-1 | nothing | the template cannot run | **no_fallback** |
| **FB-2** | SH-2 | crop the 1080p master (upsampling up to 1.78×; the compositor caps at 2.0×) | softer faces and renders; small baked text softer | degraded |
| **FB-3** | SH-3 | diarise; the most-talking voice = host, every other voice = guest; confirm at the checkpoint | a co-host would be gold | holds |
| **FB-4** | SH-4 | CTA becomes `post_only` | no on-screen pointer to the full video | holds |

### 12.4 Props, reaction bank, matte, resolution
- Props, reaction bank: none (the master has them).
- Matte: none.
- **Minimum source for crops:** a 9:16 full-height window of a 16:9 frame is 0.316 of its width: 2160p gives 1215 × 2160 (downsampled, sharp); 1080p gives 607 × 1080 (upsampled 1.78×). Never crop tighter than the full-height window on a 1080p master (it would exceed 2.0×).

### 12.5 Third-party inserts: ask, then create `[REQ always]`
The master is the creator's own work (origin `creator`). Third-party material **inside** it (a news clip, another creator's footage, a photo or an astrophoto with someone else's credit line, a TV interview) was cleared for the long-form, not necessarily for a short.
1. Run `veos inserts scan`; add every span in the chosen part where the picture is visibly someone else's (a credit line, a channel watermark, a news ticker).
2. **Ask once:** "In the part I picked, these N moments show material that isn't yours: <list with times>. Can you use them in a short (yes / no per item)?"
3. **Yes:** keep the span exactly as in the master (never altered); record `origin: creator`.
4. **No:** first try to move the in/out-points or splice around it (SS tests still pass). If the sentence is essential, cover the span with **P-SUBSTITUTE-CARD** (quote_card / headline_card / diagram recipe) quoting only what the script says; captions keep running.
5. Record every decision in `plan/inserts.json` (`{id, moment, origin: creator | created, file?, substitute_of?}`); dismissed scan moments get a reason.
Credit lines baked into a confirmed span stay visible (P-BAKED-TEXT-SAFE).

### 12.6 Frame rate and audio
30 fps CFR output, 1080 × 1920, BT.709. The master's audio is the voice track (`veos voice` from the cut map, `veos mix` to −14 LUFS).

---

## §13 Output contract `[REQ] [DNA]`

### 13.1 Core beat fields
`id`, `section` (HOOK | MECHANISM | PROOF | IMPLICATION), `t0`/`t1`, `spoken`, `trigger {word, at}`, `tone`, `line_type`, `layout`, `visual` (one sentence), `layers` (scene ids, usually `[]`), `pattern`, `sfx` (normally `[]`).

### 13.2 Conditional fields (this style)
| Switch / module | Beat / timeline fields |
|---|---|
| captions | `caption {profile: "CS-1", overrides: []}` (overrides only for spelling or a speaker fix: `{i, speaker}`, `{i, text}`) |
| dialogue / edited_master | `speaker` (host / guest / narrator), `master {t0, t1, shot: "M17"}`, `rf` (RF-1…RF-4), `angle` (from angles.json), `cut_reason` (`open` the first shot, `recrop` a master cut, `splice` a join; in `timeline.shots` write `recrop` for master cuts and splices: the engine knows only its own reasons) |
| rehooks | `rehook: true` on re-hook beats |
| third-party moment | `insert {id, origin: creator | created}` |
| exception | `exception: "E6"` (captions inherit it) |

**`timeline.shots[]`** (one per master shot inside the cut, contiguous, frame-aligned, edit time):
```json
[
  {"t0": 0.0,   "t1": 11.47, "layout": "full", "angle": "A:S1", "subject": null, "step": 1.0, "speaker": "S1", "cut_reason": "open"},
  {"t0": 11.47, "t1": 28.6,  "layout": "full", "angle": "A:S1", "subject": "S1", "step": 1.0, "speaker": "S1", "cut_reason": "recrop"},
  {"t0": 28.6,  "t1": 44.6,  "layout": "full", "angle": "A:W",  "subject": null, "step": 1.0, "speaker": "S1", "cut_reason": "recrop"}
]
```
(First row: an RF-2 render using the host single angle with no face in the shot; second: RF-1 host; third: RF-3 band.) `step` is always 1.0 (no jump re-crops).

### 13.3 Reel header
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
  band_share: 0.14
  cta: none                      # none | post_only | cross_promo
  rehooks: [17.8, 31.9, 52.4, 71.0, 89.6, 106.2, 121.5]
```

### 13.4 Hook proposals (3)
```yaml
- name: "Image-first: the loop that moves heat"
  archetype: HA-14a
  in_point: {master_t: 612.36, first_word_at: 612.42}
  first_line: "A heat pump moves more heat than it uses."
  first_shot: {mcl: M88, rf: RF-2, what: "cutaway render of the refrigerant loop, camera orbiting"}
  captions_0_3s: ["A heat pump", "moves more heat", "than it uses."]
  storyboard: "f0 render orbiting, chunk 1 on | 0.8 chunk 2 | 1.9 chunk 3 + period | 4.2 'Here's how.' | 9.6 cut to host"
  sound: "the master's mix"
  stopper_test: {mute: pass, motion_f0: pass, changes_3s: 5, payoff_by_s: 0.0}
```

### 13.5 Checkpoint
Send, then wait for approval:
1. **The 3 sub-story candidates** (t0/t1 in the master, opening line, last line, worlds visited, band share, splices) with the recommended one and why (SS-1…SS-8 results).
2. **The 3 cold-open variants** with stopper tests.
3. **The beat sheet** (with tones, speakers, RF class per shot) and the `timeline.shots` list.
4. **The transition map** (splices, dips, dissolves) and the SFX ledger (empty unless the buyer enabled cues).
5. **The inserts record** (third-party spans: confirmed / trimmed / created) and the cast (confirm FB-3 if used).
6. **Fallbacks used** (FB-2 1080p upscale, FB-3, FB-4).
7. **Style stills:** f0; a host RF-1 frame with a white caption; a guest frame (or voice-over-picture) with a gold caption; one band frame; the last frame (with the end line if used).

---

## §14 Worked examples `[REQ] [NICHE]`

Example niches: **N1 science & engineering explainer channel** and **N2 money & business documentary channel**. Times are planning estimates; replace them with `words.json` onsets.

### 14.1 N1, host + renders + guest: "Why a heat pump beats a heater" (HA-14a, 132 s, 1 splice)
**Master:** a 21-minute 4K video on heat pumps: host in his studio, CAD cutaway renders of the refrigerant loop, a field visit with an installer (guest), an animated house-heat map, a sponsor read at 9:40.
**Span:** master 10:12.36–11:41.85 + 12:25.10–13:10.32 (the splice skips a 43 s history tangent; SS-8: the sponsor at 9:40 is outside).

**Hook table**
| t | Picture | Caption | RF | Notes |
|---|---|---|---|---|
| f0 | Cutaway render of the refrigerant loop, camera orbiting | "A heat pump" (white) | RF-2 (loop centred) | In-point 2 f before "A" |
| 0.7 | same | "moves more heat" | — | — |
| 1.5 | same; the coil glows (baked) | "than it uses." | — | Sentence complete at 2.1 s |
| 2.6–4.2 | same | "It doesn't make / heat. / It moves it." | — | Stake line |
| 9.6 | **cut** (master) to host to camera, mid-gesture | "Here's the trick." | RF-1 host | Re-hook 1 (world change + turn) |

**Section plan**
| Section | Spoken (gist) | Pictures (master) | Patterns | Rehook |
|---|---|---|---|---|
| HOOK 0–9.6 | the paradox | loop render orbit | P-COLD-OPEN, P-RENDER-HOLD, P-CENTRE-CROP | — |
| MECHANISM 9.6–48 | "the refrigerant boils at minus 30… the compressor squeezes it…" | host (RF-1); render of the compressor (RF-2); P-OBJECT-TITLE "Compressor" at 21.4 (the render shows it unnamed); pressure-temperature diagram with baked labels (RF-3 band 31.0–38.5) | P-HOST-FOLLOW, P-CENTRE-CROP, P-OBJECT-TITLE, P-HUD-BAND | 9.6, 31.0 (new image) |
| PROOF 48–101 | installer: "On a cold day this one still gives you three units of heat for one of power" | installer in the plant room (RF-1 guest, **gold**); installer's voice over the outdoor-unit B-roll (P-VOICE-OVER-PICTURE, gold); host's question on location (white, P-WALK-AND-TALK); splice at 77.2 (same shoot → T-CUT) | P-GUEST-FOLLOW, P-VOICE-OVER-PICTURE, P-WALK-AND-TALK, P-SPLICE | 48.0 (guest's first line), 70.5 ("But what about…"), 92.3 (question) |
| IMPLICATION 101–132 | "So the cheapest heat in your house might come from outside it." | animated house-heat map (RF-3 band 101–109, 8 s), host to camera (RF-1) | P-MAP-FRAME, P-HOST-RETURN, P-LAST-LINE-END | 109.2 (world change + "So…") |

Band share: 7.5 + 8.0 = 15.5 s / 132 s = 12 %. Object titles: 1. CTA: none. Transition map: T-CUT splice @ 77.2; T-END @ 132.0.

### 14.2 N2, host + video-call guest + B-roll: "Why most stock pickers lose" (HA-14b, 141 s, 2 splices)
**Master:** a 26-minute 1080p documentary: host in the studio, an economist on a video call, trading-floor B-roll, animated fee charts, a TV news clip (third party) at 17:02.
**Span:** 14:05.20–15:58.90 + 16:20.00–16:41.10 + 17:30.40–17:36.80 (splices skip a repeat and the news clip). FB-2 used (1080p: crops upsample 1.78×; said at the checkpoint).

**Hook table**
| t | Picture | Caption | RF |
|---|---|---|---|
| f0 | Host mid-gesture, both hands open | "Every year," (white) | RF-1 host |
| 0.6 | same | "most professional / fund managers" | — |
| 1.9 | same | "lose to a fund / that does nothing." | — (complete at 3.1 s) |
| 3.4–12 | same shot (the master holds it) | "And the reason / isn't that they're / bad at their jobs." | — |
| 12.8 | cut to the trading-floor B-roll | "It's arithmetic." | RF-2 |

**Section plan**
| Section | Pictures | Patterns | Rehook |
|---|---|---|---|
| HOOK 0–12.8 | host RF-1 | P-COLD-OPEN, P-HOST-FOLLOW | — |
| MECHANISM 12.8–55 | B-roll (RF-2), animated fee chart with baked percentages (RF-3 band 24–35: "2 %" and "0.05 %" must stay whole, P-BAKED-TEXT-SAFE), host (RF-1) | P-CENTRE-CROP, P-BAND, P-BAKED-TEXT-SAFE | 12.8, 24.0, 44.1 ("But here's…") |
| PROOF 55–110 | economist on the video call (RF-1 guest, gold); economist's voice over the host nodding (gold, P-VOICE-OVER-PICTURE); P-OBJECT-TITLE "Index fund" at 61.2 over the fund-document B-roll; splice @ 98.4 (repeat skipped, T-CUT) | P-GUEST-FOLLOW, P-VOICE-OVER-PICTURE, P-OBJECT-TITLE, P-SPLICE | 55.0, 79.6, 98.4 |
| IMPLICATION 110–141 | host to camera; splice @ 134.3 across the news clip (the creator said no to the TV clip → trimmed out, not carded); the last line on the host | P-SPLICE, P-HOST-RETURN, P-LAST-LINE-END, P-CROSS-PROMO (buyer chose cross_promo: "Full video: Why Stock Pickers Lose", 138.4–141.0) | 110.3, 134.3 |

Inserts record: M3 "TV news clip" → dismissed by trimming (reason: creator declined; span spliced out).

### 14.3 N1, animation-only master: "What you'd see falling into a black hole" (HA-14a / HA-15 check, 118 s, 1 cross-shoot splice)
**Master:** a 14-minute painted-animation video with the host's narration and two host-to-camera shots recorded months later.
**Span:** 2:10.04–3:58.30 + 12:41.20–12:50.90 (the second segment is the host's outro from another shoot → hard cut, P-DIP-SPLICE).

| t | Picture | Caption | RF / pattern |
|---|---|---|---|
| f0 | Painted spaceship drifting, black-hole limb entering | "You can" | RF-2, P-COLD-OPEN |
| 0.3–1.9 | ship nears the hole | "never see / anything" | — |
| 2.0–3.0 | baked: the ship is stretched and crushed; a red prohibition ring slams in at 3.0 | "enter / a black hole." | P-RENDER-HOLD (no cut for 85 s) |
| 5–85 | the long animation; a baked zoom bubble on the pilot; blank pauses at 49–51 and 66–68 | narration (white) | P-RENDER-HOLD, P-PAUSE-BREATH; re-hooks at 23 (turn), 44 (new image), 66 (question), 79 ("But in…") |
| 69–89 | "DE-REDSHIFTER" HUD | narration | **P-HUD-BAND** (RF-3, 20 s = 17 %) |
| 108.3 | **hard cut** (0 f) into the host (different shoot, night) | "This is just / strange." | P-DIP-SPLICE, P-HOST-RETURN |
| 118.0 | last word "travel." + 4 f | — | P-LAST-LINE-END |
HA-15 isn't needed: the first sentence completes at 2.3 s (SS-1 passes).

---

## §15 QA checklist `[REQ] [DNA]`

**1. Profile conformance**
- [ ] Format F-A; runtime 110–150 s (or the buyer's tuned class) (review).
- [ ] The master is the only footage; everything shown is the master or a labelled created card (V-INSERTS).
- [ ] Presence is whatever the master shows (informational; V-PRESENCE off).

**2. Hook**
- [ ] f0: moving footage + caption chunk 1 (V-F0); no headline/graphic before 3.0 s (review).
- [ ] ≥ 4 SCs in 0–3 s (V-CADENCE); first sentence complete by 3.5 s and passes SS-1 (review).
- [ ] The first shot is full-bleed (RF-1/RF-2), not a band (review).

**3. Body and cadence**
- [ ] SC/10 s 6–15; max gap 2.5 s; max static 3.0 s (V-CADENCE).
- [ ] Re-hook every ≤ 25 s; intro ≤ 15 % (V-REHOOK).
- [ ] No cut that isn't a master cut or a splice; ≤ 3 splices on sentence boundaries; every added join a hard cut (no dips) (review, transition map).
- [ ] One fit per master shot; ≤ 2 fit switches in 6 s; band share ≤ 25 %; max upscale ≤ 2.0 (compose.json, review).
- [ ] Every RF-2 frame keeps its subject and baked text inside the window; no face cut at the eyes (test frames).
- [ ] No camera presets or zooms (V-CAMERA).

**4. Captions**
- [ ] CS-1: Source Serif 4 600, 70 px, 1 line, ≤ 22 chars, centred y 1380, hard swaps (V-CAPTION, V-TYPE).
- [ ] Sync: lead ≤ 0.15 s, lag ≤ 0.10 s (V-CAPTION).
- [ ] Every chunk one speaker; host/narrator white, guests gold; colour by voice on every handover shot (V-CAPTION + review of each P-VOICE-OVER-PICTURE beat).
- [ ] Spelling of names, units, terms (V-CAPTION glossary).
- [ ] Captions never cover a face (V-FACE).

**5. Modules: §20 Dialogue**
- [ ] Cast named (or FB-3 confirmed); ≥ 95 % words labelled; back-channels not captioned (review of `work/speakers.json`).

**6. Truth and inserts**
- [ ] SS-3/SS-5/SS-8: no reference out of the span, implication ending, no sponsor or plug (review).
- [ ] Every third-party span confirmed, trimmed or carded; cards verbatim and labelled (V-INSERTS, V-CITE).
- [ ] Identifiers blurred (NC-14, review).
- [ ] Object titles ≤ 3, ≥ 20 s apart, never naming something the master already names (review).

**7. Sound contract**
- [ ] No added SFX or bed (sound.cue_moments empty unless the buyer enabled them); the master's mix intact.
- [ ] −14 LUFS, true peak ≤ −1.5 dBTP (veos qa).

**8. End and export**
- [ ] Ends on the implication sentence; hard end ≤ 6 f after the last word; no black tail, no end screen (veos qa).
- [ ] End line (if used) shows the exact long-form title ≥ 2.0 s (V-PROMISE).
- [ ] 1080 × 1920, 30 fps CFR (veos qa).
- [ ] Seconds 90–150 checked on a contact sheet (G3 measure stops at 90 s).

---

## Conditional modules (§16–§25)

§16 Frame template / chrome: OFF (`profile.modules.chrome = false`): the frame is the master's own picture; no persistent slots.

§17 Running state & anchored graphics: OFF (`modules.running_state = false`, `modules.anchors = false`): no counters or anchored graphics; the master bakes its own.

§18 Data contract: OFF (`modules.data_figures = false`): numbers stay as spoken; no figures are built (§8.5).

§19 Evidence & citations: OFF (`modules.citations = false`): the master's baked credits stay visible (P-BAKED-TEXT-SAFE); the inserts flow (§12.5) still applies.

### §20 Dialogue `[COND: modules.dialogue = true] [DNA]`
**Purpose.** Make every voice identifiable by caption colour in a re-cut where the picture often shows someone other than the speaker.

**Cast table**
| Cast id | Role | Caption style | Preferred angles |
|---|---|---|---|
| `host` | the creator: on camera, on location, or narrating off screen | `primary` white, upright | host single (RF-1) |
| `narrator` | a separate narrator who is the creator (rare; use `host` normally) | `primary` white, upright | — |
| `guest` | every other voice: interviewee, expert, video-call guest, a second presenter | `accent` gold (`#E8CC28` or the buyer's BV-02 colour), upright | that guest's single (RF-1) |

**Angle map.** `veos angles` on the master (one camera source A): the singles of each detected face track (`host_single`, `guest_single`), a two-shot when two faces share frames, and the wide `A:W`. Use only the ids it lists. Mapping: RF-1 → the speaker's or subject's single; RF-2 → the host single (no face in the shot = centred window); RF-3 → the wide; RF-4 → the two-shot.

**Layouts.** `full` only; no `stack` (`dialogue.stack: false`): the evidence never splits the screen between speakers.

**Cut grammar.** R-1…R-10 (§9.3). The conversation defaults of the engine (cut on handover within 3 f, listener cutaway 1.5–3 s, re-crop every 1.2–2 s, stack openers) are **not used**: the master already made its cuts. Therefore `veos shots plan` is not run and **V-SPEAKER is off** (its SPK-3/SPK-4 checks assume cut-on-handover). Speaker correctness is checked by V-CAPTION (one speaker per chunk, the speaker's colour) and by review.

**Captions.** Colour by the diarised voice (R-3); overlapping speech: only the dominant speaker; a back-channel ("yeah", "mm") under the other speaker is not captioned.

**Single-camera fallback.** Not needed (the master is single-source by nature).

§21 Canvas camera: OFF (`modules.canvas_camera = false`; PV-4 forbids it with passthrough graphics).

§22 Ink & annotation: OFF (`modules.ink = false`): no marks on the master.

§23 Continuity: OFF (`modules.continuity = false`): continuity is the master's.

§24 Series furniture: OFF (`modules.series = false`; a buyer may turn it on, but the look would have to stay a TC-legal serif tag; not part of the shipped style).

§25 Sponsor, brand & end cards: OFF (`modules.brand = false`; `cta.devices` has no end_card or product_card). Sponsor spans are excluded from the sub-story (SS-8), so no disclosure is ever needed.

---

## Part C. Declared exceptions and the non-overridable core

### C.1 Non-overridable core
NC-1…NC-14 apply unchanged (`STYLE-PLAYBOOK-STRUCTURE.md` Part C.1). Notes for this style:
- **NC-1 face:** captions move off a face (`avoid_face`); object titles sit at y 1230 / 590 and are checked by V-FACE.
- **NC-6 truth / NC-13 quote integrity:** splices never re-order or re-attribute a quote or a number; a guest's words are always gold and verbatim.
- **NC-7 creator-owned media:** the master is the creator's; third-party spans inside it are confirmed or replaced (§12.5).
- **NC-8 audio:** −14 LUFS, −1.5 dBTP on the master's mix; hard end ≤ 6 f.
- **NC-12 disclosure:** never triggered, because sponsor spans are excluded (SS-8).
- **NC-14 redaction:** P-REDACT.

### C.2 Exceptions used
| E-id | Limits here | Reason | Evidence |
|---|---|---|---|
| E6 Hard swap | caption band rect constant ± 4 px; 0-frame content swaps; never for a new element | hard-swapped serif word groups are the style | v01–v03 @ 0:00–0:03 |

Not used: E1 (nothing behind anyone), E2 (no bursts), E3 (captions are 70 px), E4 (no ambient fields), E5 (no edge-bleed type). A buyer may switch E6 off (captions then fade 3 f), a VAR change that softens the look.

---

## Part D. Personalisation

### D.1 What the buyer is asked (one round, each with "keep the template default")
| BV | Question | Default | Lands on |
|---|---|---|---|
| BV-01 | Your name / channel and handle | "the creator" | `creator.name/handle` |
| BV-02 | One brand colour for **guest captions** (host captions stay white) | `#E8CC28` gold | `roles.accent.default` (TUNE: warm, light, saturated) |
| BV-05 | The language of your long-form videos, and the caption language | English ({{BV-05.speech|en}} → {{BV-05.captions|en}}) | `profile.language`, always asked: **English** → English captions (default) · **Hinglish** → romanised Hinglish captions · **Hindi** → Devanagari captions; numbers follow (BV-06) |
| BV-08 | End of the reel: nothing / a line in the post / an on-screen "Full video: <title>" line | nothing | `profile.cta.chosen` (none / post_only / cross_promo) |

Never asked at setup: footage (the master comes with each reel), fonts (TUNE within the serif classes), duration (TUNE: standard 60–90 s or long 90–180 s).

### D.2 Lock summary (complete map in `tokens.json → locks`)
| Element | Lock |
|---|---|
| source type, spine, graphics passthrough, captions full/primary, footage total, presence | DNA |
| Serif caption mechanics (unit, 1 line, hard swap, no emphasis, voice-coded colour) | DNA |
| Caption size 62–78 px, weight 500–700, y 1300–1460, stroke 0–3 px | TUNE |
| Host caption colour (white) | DNA |
| Guest caption colour | TUNE (BV-02) |
| Serif families | TUNE (Source Serif 4 / EB Garamond; title EB Garamond / Instrument Serif) |
| Reframe classes, layouts, band geometry, zoom policy, shot grammar R-1…R-10 | DNA (band blur and luma TUNE) |
| Cadence numbers, motion tokens | TUNE ±15 % |
| Re-hook interval | TUNE 20–30 s |
| Duration class | TUNE (standard ↔ long) |
| Hook archetype set | DNA; choice per reel VAR |
| CTA device | VAR among none / post_only / cross_promo |
| Sound cue moments, bed | VAR (default none / off) |
| Hook pairs §6.4, lookup §8.4, examples §14, App. A | NICHE |

### D.3 How NICHE slots grow
- **§6.4** gets one row per reel (the question the cold open raises, where it's answered, the first shot).
- **§8.4** gets the buyer's recurring line types (e.g. "a recipe step over the hands" → P-DETAIL-INSERT).
- **§14** is replaced by the first approved reel's plan.
- **App. A** collects approved post titles and first lines.
- **Glossary** collects the channel's names and terms.

### D.4 Typical buyer tweaks and how they classify
| Request | Class |
|---|---|
| "Bigger captions" (to 76 px) | TUNE, applied |
| "Captions higher" (to 1320) | TUNE, applied |
| "Guest captions in my brand teal" | TUNE if light enough, else nudged; a dark navy is a DNA deviation (it must read on footage) |
| "Add a subscribe button at the end" | DNA deviation (N2): warned, logged as DV-n if confirmed |
| "Add zooms to make it punchier" | DNA deviation (D5/N3) |
| "Make it 75 seconds" | TUNE (standard class) |
| "Add background music" | VAR (sound.bed on) but warned: the master already has its mix |

---

## Part E. Changes

| Version | Date | Change |
|---|---|---|
| v1 | 2026-10-06 | First template from the Veritasium evidence (v01–v03). Measured captions (70 px, y 1380, gold `#E8CC28`) replace the caption library defaults (62 px, `#F2C14E`). Graphic patterns limited to 4 (PV-4); the craft is expressed as 19 cut/reframe patterns. |

---

## Part F. IDs used in this playbook

| Prefix | IDs |
|---|---|
| D / BD | D1–D8 / BD… (buyer) |
| SW / PV | §0 switches; PV-1…PV-12 (V-PROFILE) |
| H / N / BN | H1–H17 / N1–N12 / BN… |
| E / NC | E6 / NC-1…NC-14 |
| W / L / G | W-master, W-void / L-master, L-band-black, L-band-blur, L-void / G-1…G-3 |
| RF | RF-1 face follow, RF-2 centre crop, RF-3 band, RF-4 two-shot |
| SS | SS-1…SS-8 sub-story tests |
| CS | CS-1 |
| HA / ST | HA-14 (a, b, c), HA-10, HA-15 / ST-2, ST-3, ST-5, ST-6 |
| P | P-OBJECT-TITLE, P-CROSS-PROMO, P-SUBSTITUTE-CARD, P-REDACT; P-COLD-OPEN, P-HOST-FOLLOW, P-GUEST-FOLLOW, P-VOICE-OVER-PICTURE, P-CENTRE-CROP, P-BAND, P-TWO-SHOT, P-WALK-AND-TALK, P-DETAIL-INSERT, P-RENDER-HOLD, P-BAKED-TEXT-SAFE, P-MAP-FRAME, P-HUD-BAND, P-SPLICE, P-DIP-SPLICE, P-PAUSE-BREATH, P-REACTION-KEEP, P-HOST-RETURN, P-LAST-LINE-END (23) |
| B | B-1…B-8 |
| T / R | T-CUT, T-DISSOLVE, T-END, T-END-FADE / R-1…R-10 |
| SH / FB | SH-1…SH-4 / FB-1…FB-4 |
| F | F-A |
| ER | ER-1…ER-6 engine requests (App. B) |
| V | V-PROFILE, V-F0, V-CADENCE, V-ONWORD, V-SAFE, V-FACE, V-CAPTION, V-TYPE, V-EXC, V-HUES, V-LAYOUT, V-REHOOK, V-NUMFMT, V-INSERTS, V-CITE, V-PROMISE, V-CAMERA (on); V-PRESENCE, V-SPEAKER, V-TITLE, V-COMEDY, V-LEDGER, V-DATA, V-THEME (off) |

---

## Appendix A. Post-title and first-line bank `[NICHE]`
The style shows no headline. These are **post titles** (the reel's caption/title on the platform) paired with the **first line** to look for in the master. Slots in `<angle brackets>`.

| # | Post title | First line to find (SS-1 shape) | Archetype | Niche |
|---|---|---|---|---|
| 1 | Why a heat pump beats a heater | "A heat pump moves more heat than it uses." (paradox) | HA-14a | N1 |
| 2 | You can never see anything fall into a black hole | "You can never see anything enter a black hole." (paradox) | HA-14a | N1 |
| 3 | The hardest part of <field> isn't what you think | "One thing that makes <field> so tricky is <constraint>." (problem) | HA-14b | slot |
| 4 | How a 1,000-tonne machine steers underground | "<Machine> <does the surprising thing> every <interval>." (mechanism) | HA-14a | N1 |
| 5 | Why most stock pickers lose | "Every year, most professional fund managers lose to a fund that does nothing." (paradox) | HA-14b | N2 |
| 6 | The box that made trade 90 % cheaper | "One steel box cut the cost of shipping by ninety percent." (claim) | HA-10 | N2 |
| 7 | Where your money goes when prices rise | "When prices rise, the money doesn't disappear." (problem) | HA-14b | N2 |
| 8 | <Expert> showed me <object> in their office | (guest) "I just have this <object> here in my office." (guest-first) | HA-14c | slot |
| 9 | What <thing> looks like from the inside | "Imagine standing inside <thing> while it <runs>." (atmosphere) | HA-15 | slot |
| 10 | The record nobody expected: <number> <unit> | "Their current record for <task> is <number> <unit>." (mechanism → proof) | HA-14a | slot |

## Appendix B. Evidence map (summary)
Full map, the unverified list and the measurement method are in `evidence.md`.

| DNA element | Evidence |
|---|---|
| Serif captions, 1 line, 1–3 words, y ≈ 1380, ≈ 70 px | v02 @ 0:00–0:17 (y 1384, measured 70–72 px), v01 @ 0:00–0:28, v03 @ 0:00–0:03 (y 1345) |
| Gold for every guest voice, by voice | v01 @ 0:45–0:57, 1:25–1:39; v02 @ 1:29–1:30 and 2:10–2:15 (gold over the host's face) |
| Cold open mid-sentence, no graphic | v01 @ 0:00, v02 @ 0:00, v03 @ 0:00 |
| Bands centred y 656–1264, caption under | v02 @ 0:58–1:11, 1:46–1:50 (black); v03 @ 1:09–1:29, 1:45–1:46 (blur) |
| Long shots, captions carry cadence | v03 6 cuts in 110 s; v02 17.75 s opening shot; v01 11.5 s |
| Italic serif object title | v02 @ 1:08–1:11 "Antimatter Trap" (possibly baked in the master: the object passes in front of it) |
| No CTA, ends on the last line | v01 @ 1:54, v02 @ 2:32, v03 @ 1:49 |

**Engine requests (ER-…)**: ER-1 per-shot `fit` (cover / letterbox / blurfill) and an explicit crop override (x, y keyframes) in `timeline.shots`, with a `master_cut` cut reason; ER-2 `shots mine --story` for single-voice masters (sentence-bounded candidates scored by SS-1/SS-3/SS-5 cues and the master cut list); ER-3 `veos segments` (scene-detect cut list + transcript chapters as `plan/mcl.json`); ER-4 keep the master's stereo mix and skip the voice chain for `edited_master`; ER-5 bundle Noto Serif Devanagari (done); ER-6 extend the G3 motion measure beyond 90 s (E-28); ER-7 make the blur-fill backdrop brightness of `shots render` a token (`compose.BLUR_DIM` is a hard-coded 0.45; this style needs 1.0); ER-8 an `end_fade` frame count for the last shot (T-END-FADE, 5 f).
