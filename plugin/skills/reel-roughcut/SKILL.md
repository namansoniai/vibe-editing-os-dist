---
name: reel-roughcut
description: Rough-cut phase of a Vibe Editing OS project — choose the best takes across all clips, remove false starts, repeats and dead air, write the edit list and apply it, then show the cut to the user and wait for their approval (changes go back to the rough-cutter). Called by the reel orchestrator after prep.
model: claude-opus-5-5
effort: high
user-invocable: false
---

# Rough cut (the rough-cutter decides; the engine cuts)

**Goal:** one clean, tight performance in story order, built from every clip. The take decisions run on Sonnet.

1. `veos project show --project "P"` → `source_type`, mode, script; `veos paths` → `playbooks` (the playbook folder is `<playbooks>/<playbook id>`).
   **Resumed at the cut gate** (phase still `prep`, but `work/edl.json` and `work/cutmap.json` exist): don't cut again. If the user's message is the approval, approve (step 5); if it is a change, start a new rough-cutter with the project path and the change as `CHANGES:` notes (it reads the current `work/edl.json`); otherwise show the cut and ask (step 5).
2. Delegate with the Agent tool: `subagent_type: "vibe-editing-os:rough-cutter"`, prompt = the project path, `source_type`, mode, the script path (or "none") and the playbook folder. It reads `veos roughcut-candidates` (sentences, take groups, false starts, pauses), decides, compares frames with `veos look --src` only when a line has 2+ takes, writes `work/edl.json` and runs `veos cut`.
3. **Director mode, a conversation longer than 150 s:** it returns 2–3 candidate moments instead. Offer them to the user, then send the choice back to the same agent (SendMessage).
4. `VERDICT: failed`: `veos project set last_error="roughcut: <reason>" --project "P"` and stop with a plain-language message.
5. **The cut gate (every mode, autopilot included):** when `work/edl.json`, `work/cutmap.json` and `work/words.edit.json` exist, show the cut and wait.
   - Open the preview `P/work/cut_proxy.mp4` for the user (a small preview with sound, read straight from the original clips; the full-quality picture is made after the approval):
     - Windows: PowerShell `Start-Process "<absolute path to P/work/cut_proxy.mp4>"`
     - macOS: `open "<path>"`

     If opening fails, just print the path.
   - Tell them in 2–3 plain lines what happened, from its `CUT:` line: how long the cut is (of how much footage), which retakes, false starts and pauses went, and anything you'd want them to check (a take choice that was close). Then ask: "Happy with the cut? Say approve, or tell me what to change."
   - **Approve** ("approve", "ok", "theek hai", "looks good", "next"): `veos project set phase=roughcut --project "P"` and return to the orchestrator.
   - **Changes in plain words** ("keep the first take of the hook", "cut the part where I cough", "put the CTA back in"): restate each in one line, then SendMessage the same rough-cutter agent (its context intact) the notes, prefixed `CHANGES:`. It edits `work/edl.json` and runs `veos cut` again. Show the new cut the same way and ask again. Repeat until approved.
   - The phase becomes `roughcut` only after the approval; on resume with a cut but no approval, show the cut and ask again.
