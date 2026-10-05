---
name: reel-inputs
description: Inputs phase of a Vibe Editing OS reel — before planning, ask the creator for screen recordings, specific graphics/images/logos to show, and an optional reference reel whose style this one video should copy; import them for this reel only. Called by the reel orchestrator after captions.
user-invocable: false
---

# Reel inputs (asked before the edit is planned)

1. **Read the transcript first:** `veos context --project "P" --part words`. Note where the speaker mentions things that a recording or graphic would show best: tools, apps, websites, products, people, documents, results.
2. **Ask in ONE AskUserQuestion round** (all optional; allow file paths as free text):
   - **Screen recordings:** "Any screen recordings to show? (e.g. you mention <tool/app from the transcript> at <time>)". Options: "Yes, I'll give the files" / "No".
   - **Specific graphics:** "Any images, logos or graphics that must appear? (product shots, screenshots, your logo…)". Options: "Yes" / "No".
   - **A reel to copy for THIS video:** "Should this video copy the style of a specific reel? (only this video; your playbook stays the same)". Options: "Yes, I'll give the reel" / "No, use my playbook".
3. **For each "Yes",** get the file paths: the user drags files into the chat or types their paths. Then import them:
   - **Recordings, B-roll, images, logos:** `veos asset add "<file>" --project "P" --name <short-name>`.
     - Ask, or infer from the transcript, **where** each one belongs: the words or moment it illustrates.
     - Record that as `{"name", "kind", "show_when": "<spoken words or time>", "note"}`.
   - **A reference reel for this video:** do a quick style extraction:
     - an overview contact sheet: `veos sheet <out> --video "<file>" --frames <2 fps list>`
     - 2–3 transition strips around scene cuts
     - Write **`P/plan/reference-style.md`**: the hook build, captions (look, size, position, animation), visual families, transitions (frames, direction), pacing, colour feel.
     - **This reel only. Never edit the playbook here.** Where it conflicts with the playbook, the reference wins for this reel; the global rules still win over both.
4. Save everything: write `P/plan/inputs.json`:
   ```json
   {"assets": [...], "reference_reel": "<path or null>", "notes": "..."}
   ```
   Then run `veos project set inputs=@P/plan/inputs.json phase=inputs --project "P"`.
5. Tell the user in one line what will be used ("2 screen recordings and your logo; style copied from the reel you gave").
   - If they said **No** to everything: `inputs.json` gets empty lists, and you still set the phase.
