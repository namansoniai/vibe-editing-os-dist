---
name: reel-roughcut
description: Rough-cut phase of a Vibe Editing OS project — choose the best takes across all clips, remove false starts, repeats and dead air, write the edit list and apply it. Called by the reel orchestrator after prep.
user-invocable: false
---

# Rough cut (you decide; the engine cuts)

**Goal:** one clean, tight performance in story order, built from every clip.

1. Run `veos context --project "P" --part all`. You get:
   - the sources and their setups (selfie / tripod / screen…)
   - per-source word lists `i:word@t` with `?` for low confidence and `|pause x|` markers
   - the script excerpt, if there is one
2. **Decide segments** (all times in **source** seconds):
   - **Retakes:** when the same sentence is said more than once (same words in different takes or clips), keep the **last complete, fluent take** unless an earlier one is clearly better (no stumble, more energy). Drop the others.
   - **False starts and stumbles:** cut from the start of the abandoned phrase to the start of the restart.
   - **Dead air:** cut pauses longer than 0.35 s inside a segment, down to about 0.12 s. Keep one deliberate pause of ≤ 0.3 s before a punchline or pivot.
   - **Order:** follow the script's order if there is one; otherwise the natural story order (hook → promise/loop → items in ordinal order → payoff → CTA).
   - **Screen recordings and B-roll** aren't part of the speech edit. Leave them out of the EDL; the planner places them as cards.
   - **Cut points:** cut on word boundaries. Start a segment about 0.04 s before its first word, and end it about 0.08 s after its last word.
   - **A single clean take** (no repeats, no long pauses) is one segment, the whole clip. Don't cut for the sake of cutting.
3. Write `P/work/edl.json`:
   ```json
   {"version":1,"fps":30,"segments":[{"src":"A","in":0.41,"out":3.21,"note":"hook, take 2"}]}
   ```
4. Run `veos cut "P/work/edl.json" --project "P"`. Check the summary:
   - `proxy_frames` == `frames`
   - `gaps_ge_150ms` is small (≤ 1 per 15 s, except deliberate pauses)
   - If it's still gappy, tighten the EDL and run it again (at most 2 rounds).
5. `veos project set phase=roughcut --project "P"`. Tell the user in one line: kept duration, takes removed, seconds trimmed.
