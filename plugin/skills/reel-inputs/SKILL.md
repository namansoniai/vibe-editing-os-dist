---
name: reel-inputs
description: Inputs phase of a Vibe Editing OS reel — before planning, find the third-party moments in the transcript (veos inserts scan) and ask the creator ONCE whether they have their own clip or screenshot for them, plus screen recordings, graphics and an optional reference reel; import their files with --origin creator for this reel only. Never fetches media. Called by the reel orchestrator after captions.
model: claude-opus-5-5
effort: high
user-invocable: false
---

# Reel inputs (asked before the edit is planned)

**The creator owns every piece of third-party material, or it isn't shown (NC-7).** You never fetch, download, screenshot or search for anyone else's media: no web tools (WebFetch, WebSearch, a browser) for media, ever, and `veos` has no command that downloads media. What the creator doesn't hand over, the planner builds itself from the script's words (a quote or headline card, a recreated generic UI, a logo plate set in type, a silhouette, a diagram).

1. **Read the transcript first:** `veos context --project "P" --part words`. Note where the speaker mentions things that a recording or graphic would show best: tools, apps, websites, products, people, documents, results.
   - **Faceless reel** (`veos project show` → `source_type: voiceover_only`): there is no footage of the creator, so their own clips matter more. Ask the screen-recordings question as **"Any of your own clips to show over the voice-over? (B-roll, screen recordings, photos, your past reels as proof)"**. Clips already in the project folder were ingested as B-roll (`veos context --part sources`): offer to use them. Never fetch media from the web: for anything they don't have, the planner draws it (diagrams, icon cards, recreated generic screens).
   - **Third-party moments:** `veos inserts scan --project "P"` → `plan/inserts.scan.json`: the moments that call for someone else's material (a post read aloud, a news headline, another creator's clip, a chart from somewhere, an event, a person, a product, an app screen), each with its time, the spoken words and a suggested created substitute. Refine the list yourself: merge moments that are one beat, drop the creator's own material (note why; it goes under `dismissed`), and name each moment in plain words.
2. **Ask in ONE AskUserQuestion round** (all optional; yes / no answers only, never file paths). Conversation reels: the cast
   (names, host/guest) was asked by the orchestrator; don't ask again.
   - **The third-party moments (asked once, as one list):** "Do you have your own screenshot or clip for these N moments? If not, I'll make a clean card for each." followed by the N moments in plain language, one line each with its time and words (start from the scan's `question`, edited to your refined list). Options: "Yes, I'll drop the files" / "No, make the cards". Never ask moment by moment.
   - **Screen recordings:** "Any screen recordings to show? (e.g. you mention <tool/app from the transcript> at <time>)". Options: "Yes, I'll give the files" / "No".
   - **Specific graphics:** "Any images, logos or graphics that must appear? (product shots, screenshots, your logo…)". Options: "Yes" / "No".
   - **A reel to copy for THIS video:** "Should this video copy the style of a specific reel? (only this video; your playbook stays the same)". Options: "Yes, I'll give the reel" / "No, use my playbook".
3. **For any "Yes", nobody types a file path:**
   - Create `<clips folder>/inputs` (Bash `mkdir -p`) and open it: Windows PowerShell `Start-Process "<absolute path>"`, macOS `open "<path>"`.
   - Say in one plain message: "I've opened a folder called **inputs**. Drop in <what they said yes to: your screen recordings / images and logos / your files for those moments / the reel to copy>, then reply **done**."
   - When they reply, list the media files in that folder with Bash (video: `.mp4 .mov .m4v .webm .mkv .avi`; images: `.png .jpg .jpeg .webp .gif .svg`; any case). Match each file to what it is from its name, type and the transcript; if that isn't clear, ask once, in one line per unclear file ("Which moment is `IMG_2041.png` for?"). A pasted path still works.
   - Then import them:
   - **Recordings, B-roll, images, logos, and the files for third-party moments:** `veos asset add "<file>" --project "P" --name <short-name> --origin creator` (the origin is recorded in `plan/assets.json`; V-INSERTS only accepts creator-origin files). Only files the creator drops or names on their disk: never a URL.
     - Ask, or infer from the transcript, **where** each one belongs: the words or moment it illustrates.
     - Record that as `{"name", "kind", "show_when": "<spoken words or time>", "note"}`.
   - **A reference reel for this video:** do a quick style extraction:
     - an overview contact sheet: `veos sheet <out> --video "<file>" --frames <2 fps list>`
     - 2–3 transition strips around scene cuts
     - Write **`P/plan/reference-style.md`**: the hook build, captions (look, size, position, animation), visual families, transitions (frames, direction), pacing, colour feel.
     - **This reel only. Never edit the playbook here.** Where it conflicts with the playbook, the reference wins for this reel; the global rules still win over both.
4. **Write `P/plan/inserts.json`** (engine/SPEC.md section 7, Inserts): one record per refined moment, `{id, moment, t0, t1, kind, origin: "creator", file}` for every moment the creator covered and `{id, moment, t0, t1, kind, origin: "created", recipe, substitute_of, quote_text?}` for the rest (recipe = the scan's suggestion unless the playbook's §8 lookup names another; `quote_text` copied word for word from the script or transcript; made-up cards need no label and no credit). Dropped moments go in `dismissed` with a reason; anything the creator typed in reply (an exact headline, a post) goes in `creator_texts`. Put the question and their answer in `asked`. Run `veos inserts check --project "P"` and fix what it reports.
5. Save everything: write `P/plan/inputs.json`:
   ```json
   {"assets": [...], "reference_reel": "<path or null>", "notes": "..."}
   ```
   Then run `veos project set inputs=@P/plan/inputs.json phase=inputs --project "P"`.
6. Tell the user in one line what will be used ("2 screen recordings and your logo; your screenshot for the headline, clean cards for the other 2 moments; style copied from the reel you gave").
   - If they said **No** to everything: `inputs.json` gets empty lists, and you still set the phase.
