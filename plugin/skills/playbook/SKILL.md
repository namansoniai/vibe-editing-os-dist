---
name: playbook
description: Set up (or revise) a creator's personal editing playbook for Vibe Editing OS (one person can have several, e.g. one per account) — interview them about their reels, study their editing inspiration, write a full editing playbook for their niche (same depth as the reference playbook), show a visual glimpse to confirm, and save it. Use when the user runs /playbook, is new to Vibe Editing OS, says "set up my editing style", or wants to change how their reels are edited.
argument-hint: "[creator name or handle]"
---

# Build the creator's editing playbook

The playbook is the brain of every edit. It must be as deep and decisive as the reference playbook (`reference_playbook` from `veos paths`), but written for **this creator's** content. The creator answers questions and confirms. **They never write it.**

Run `veos paths` first. You need:
- `playbooks`: where this user's playbooks live (write here)
- `playbook_template`: the template folder
- `reference_playbook`: the reference playbook (read-only)
- `repo_root`

**Also read `<repo_root>/playbooks/_global/GLOBAL-RULES.md`.** Every playbook you write must obey it (G1 no overlapping, G2 no clutter, G3 smooth motion, G4 high quality).

## Step −1: New playbook or revise an existing one
1. Run `veos workspace get`. It shows the playbook linked to this folder, if any, and all existing playbooks.
2. Ask in one question (skip it if there are no playbooks yet):
   - **Create a new playbook** (e.g. for another account).
   - **Revise** `<existing one>`.
3. **New:** get a unique id with `veos playbook new-id --name "<creator or account name>" --handle <handle>`.
   - **Never overwrite an existing playbook folder.**
   - One person can own several playbooks; each is fully independent (its own style, brand, learned rules).
4. **Revise:** jump to the step they want to change (interview answers, inspiration, a section, colours…), then do Steps 4–6 again.

## Step 0: Choose the setup path (one question)
- **A. Start from a famous editing style.**
  - The creator picks one of the ready-made style templates in `<repo_root>/playbooks/_styles/`. Each is a full playbook template with its own preview.
  - Then ask **only** the short brand + content questions (Step 1, rounds 1 and 4) and **skip inspiration**.
  - Write their playbook = the template with their niche's result pairs, line → pattern lookup, brand tokens and language filled in.
  - **Status: coming soon.** If `_styles/` has no templates yet, say so in one line and use path B.
- **B. Build my own playbook** (the full flow below: interview → inspiration → playbook → glimpse → confirm).

## Step 1: Interview (plain language, 2–3 rounds of questions, multiple-choice where possible)
Ask with the AskUserQuestion tool (≤ 4 questions per round; always allow free text):
1. **Content:** niche and topics (ask for 3–5 recent or upcoming reel ideas), the audience, what viewers should feel/learn, and recurring formats (listicles, tutorials, stories, rants, reviews, before/after).
2. **Voice and language:** spoken language (e.g. Hinglish / English / Hindi), the caption language and script (romanised or native), humour level (none / light / roast and meme), and energy (calm / balanced / hype).
3. **Shooting:** camera setups (selfie / tripod / desk / walking / kitchen / gym…), background, whether they record screen recordings or B-roll, and typical raw length.
4. **Brand:** name and handle, primary + accent colours (hex, or "pick for me"), fonts they like (or "pick for me"), logo file, CTA habits (comment keyword → DM, follow, link in bio, community name), anything they **never** want on screen.
5. **Assets:** do they have B-roll clips, product shots, screen recordings, or a sound-effects library they're licensed to use? Where are they?

Write the answers to `<playbooks>/<id>/profile.md` (id from `veos playbook new-id`).

## Step 2: Editing inspiration
Ask: "Share 1–5 reels whose **editing** you love (video files, ideally downloaded; links alone can't be analysed reliably), and optionally 2–3 of your own past reels."

For each video file, do a style extraction (the reference process P1). Use the `vibe-editing-os:veos-runner` agent for the heavy commands:
- `veos sheet <out> --video "<file>" --frames <2 fps list>` for overview contact sheets.
- Scene cuts with ffmpeg (`select='gt(scene,0.25)',showinfo`), then frame-by-frame strips around 3–5 transitions (`veos sheet --video … --frames …`).
- Look at the sheets yourself and note:
  - layout grid and caption styles (font feel, size, colour, position, animation)
  - the hook construction in the first 3 s
  - B-roll families and how they relate to the words
  - transition recipes (frames, direction, colour)
  - zoom habits, pacing (cuts and changes per second), colour palette, sound feel if obvious
- Write the findings, as reusable rules and not a clip description, into `profile.md` under "Inspiration analysis".

If they have no inspiration files:
- Ask them to **describe** the editing they like: 2–3 creators or reels by name, plus what they like about them.
- Then build the style from that description and their answers.
- Once famous-style templates exist (path A), offer those instead.

## Step 3: Write the playbook
1. Read `<playbook_template>/PLAYBOOK-TEMPLATE.md` (the required structure).
2. Read the reference playbook (`reference_playbook`) **selectively** for depth and format: its header + directives, §2, §6, §8.3–8.4 and §13. Don't copy its content.
3. Write `<playbooks>/<id>/playbook.md` with **every** template section, specific to this creator. §2 starts with the global rules G1–G4:
   - **Directives (D1…)** from what they said matters.
   - **Result-pair table and line → pattern lookup built from their actual topics** (use the reel ideas they gave).
   - **20–60 named visual patterns (P-…) invented for their niche,** each with on-screen content + a motion recipe in frames. These are ideas the editor will build as bespoke code, so describe them concretely; don't limit them to what's easy.
   - **Rules from the inspiration analysis**, translated into tokens (sizes, frames, colours).
   - **The assets list:** what they should record or supply for each B-roll family.
4. Write `<playbooks>/<id>/tokens.json`: **copy the schema of the `tokens.json` that sits next to `reference_playbook` exactly**, with this creator's colours (roles keep their meanings; contrast-safe), font slots (bundled Google/OFL fonts only), type sizes, layout, motion, camera presets, budgets, `creator` (name, handle, language, caption_language, banner_language, cta, glossary) and `tone`.
5. **Sound palette (§11 + `tokens.json` → `sound`):**
   - Read `<sfx_pack>/catalog.json` (from `veos paths`).
   - Pick the vibes, roles and preferred sound ids that fit this creator's energy and humour answers. A calm creator gets soft, premium sounds and no meme hits; a hype creator gets punchier ones; meme sounds only if they chose roast/meme humour.
   - **Use only sounds that are in the catalogue.**
6. Write it in 3–4 large Write calls (header → §1–5 → §6–8 → §9–15 + appendix). Keep the reference's density.

## Step 4: The glimpse (preview page)
Write `<playbooks>/<id>/preview/index.html`: one self-contained page (inline CSS/JS, fonts from `<repo_root>/assets/fonts` via relative `file:` URLs or Google Fonts, no other network). Show 8–14 **animated 9:16 frames** (CSS/JS loops, ~360×640 each) using **their** tokens:
- **Frame 0 / hook:** their banner style + a result pair from their niche + a speaker silhouette. If they shared a raw clip, extract one frame with ffmpeg and use it instead.
- **Their caption systems:** keyword captions + subtitles in their language.
- **5–8 signature B-roll / motion patterns** from §8, each labelled with its P-id and the kind of line it serves.
- **2–3 transitions** and **the zoom feel** (a short loop each).
- **The palette and fonts** strip, and their CTA moment.
- **Their sound palette:** 4–6 play buttons (HTML `<audio>` with relative `file:` URLs into the SFX pack), each labelled with what it marks ("card arrives", "key word pops").

Under each frame, a one-line caption: "Used when you say … (P-xx)". Open the page for them (Windows `Start-Process`, macOS `open`).

## Step 5: Improve (always ask, right after the preview)
Ask: **"Anything you'd like to improve or add to your editing style before we save it?"**
- Offer 3–4 quick options that fit what they just saw (e.g. "Calmer transitions", "Bigger captions", "More motion graphics", "Different colours"), plus free text and **"No, it's good"**.
- For every change: restate it in one line, then update `playbook.md`, `tokens.json` and the preview together.
  - If a request would break a global rule (e.g. "fill the screen with text"), explain in one line and offer the closest clean alternative.
- Re-open the preview and ask again, until they choose "No, it's good".

## Step 6: Save and link this folder
- Add `"confirmed_at"` to `profile.md`.
- Run `veos workspace set --playbook <id>` so **this folder** uses this playbook. Reels edited in this folder or below it pick it automatically.
- Tell them in 3 lines:
  1. Put raw clips in a folder here and run `/vibe-editing-os:reel <folder>`.
  2. For another account, open a different folder and run `/vibe-editing-os:playbook` there.
  3. Feedback they give while editing can be saved into this playbook, and they can revise it anytime with `/vibe-editing-os:playbook`.

**Token note:** this runs once per creator. The playbook is long by design, because it's what makes every future reel good.
