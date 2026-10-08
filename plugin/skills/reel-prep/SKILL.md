---
name: reel-prep
description: Prep phase of a reel project: ingest the source clips, take their sound and transcribe it (or, for a faceless reel, the voice-over). Only the sound before the cut: the picture is converted after it (only the seconds it keeps), and the face is found there. Called by the reel orchestrator before roughcut; not meant to be invoked directly.
model: claude-opus-5-5
effort: high
user-invocable: false
---
# reel-prep

Input: project folder `P` (the `vibe-edit/` folder with project.json). Never hand-edit project.json; use `veos project`.

1. Run `veos project show --project "P"`. Read `clips` (clip paths), `script` (may be null) and `source_type` (`talking_head` when missing). If it fails, stop and tell the user the project is missing.
2. Delegate with the Agent tool: `subagent_type: "vibe-editing-os:veos-runner"`. Prompt it with the project path and these commands, in order:
   - **Talking head:**
     - `veos ingest --project "P"` (no paths: it uses the clips stored in project.json)
     - `veos conform --audio-only --project "P"` (only the sound: no video is converted before the cut)
     - `veos transcribe --project "P"` (append `--script "<script path>"` only if the project has a script)
     - Nothing visual here: the rough cut needs only the words, and its review video and stills are read straight from
       the original clips. The seconds the cut keeps are converted at full quality after it (reel-plan §0), then the
       face is found in them, and the person cut-out is made only if the plan needs it.
   - **Faceless (`voiceover_only`):**
     - `veos ingest --project "P"` (it picks the voice-over from project.json; the picture of a video voice-over is ignored; other clips become B-roll)
     - `veos conform --audio-only --project "P"` (the sound; B-roll pictures are converted after the cut if it uses them)
     - `veos transcribe --project "P"` (append `--script "<script path>"` if the project has a script; the words are aligned to it)
     - no matte: there is no presenter to cut out.

   Tell it transcribe can take minutes (Bash timeout 600000) and to stop at the first failure.

   **Conversation reels** (orchestrator §1b; `P/plan/cast.json` exists or the playbook's `source_type` is
   `multi_speaker`) run this list instead (no matte; N = the number of people in the cast):
   - `veos ingest --project "P"`, then `veos conform --project "P"`
   - **2+ files of the same conversation:** `veos sync --project "P"` (audio-only files are treated as per-person
     mics; it writes the session master `MIX`). Master `M` = `MIX`. **One file:** no sync; `M` = that file's id.
   - `veos transcribe --id M --project "P"` (only the master; add `--script` as above)
   - `veos speakers --num N --project "P"`, then `veos speakers name "S1=<name>:<role>" "S2=<name>:<role>" --project "P"`
     (match ids to people with `role_guess` (host = the one asking) and, for mic mode, the `mic` each id came from)
   - `veos angles --project "P"` (who is on which camera; faux crops from a wide shot)

   A `SYNC_UNRELIABLE` failure means the files don't share sound: tell the user which file could not be lined up and
   ask whether it really belongs to this conversation (a clap at the start of the next recording helps).
3. If its verdict is `failed`: run `veos project set --project "P" last_error="prep: <short reason>"` and stop with a plain-language message (what failed, what the user can try: re-run `/vibe-editing-os:reel` to resume, or run `veos doctor`). Do not continue.
4. Verify the done condition (workflow phase `prep`) with Bash `ls` in the project work folder:
   - **Talking head:** `sources.json` exists, and for every talking-head source `audio/<id>.wav` and `words/<id>.json` exist (no `src/<id>.mp4`, face boxes or matte yet: all come after the cut).
   - **Faceless:** `sources.json` exists with `"source_type": "voiceover_only"`, and `audio/V.wav` and `words/V.json` exist.
   - **Conversation:** `words/<M>.json`, `speakers.json` and `angles.json` exist, and `veos speakers show` lists N speakers with names.

   If anything is missing, treat it as a failure (step 3) and name the missing file.
5. Only now run `veos project set --project "P" phase=prep last_error=""`.
6. Reply to the orchestrator in 2-3 lines: sources found (for a faceless reel: the voice-over length and any B-roll clips), total duration, word count (and the script match rate when there is a script), and that phase is `prep`.

Rules: phases are idempotent and re-use cached outputs, so on resume just run the steps again. Make no creative decisions here.

**Never patch, downgrade or edit the engine, and never ask the user to pick an engine fix.** Report the failing step plainly and suggest `/vibe-editing-os:setup update`.
