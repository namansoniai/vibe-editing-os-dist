---
name: reel-prep
description: Prep phase of a reel project: ingest, conform, transcribe and matte the source clips. Called by the reel orchestrator before roughcut; not meant to be invoked directly.
user-invocable: false
---
# reel-prep

Input: project folder `P` (the `vibe-edit/` folder with project.json). Never hand-edit project.json; use `veos project`.

1. Run `veos project show --project "P"`. Read `clips` (clip paths) and `script` (may be null). If it fails, stop and tell the user the project is missing.
2. Delegate with the Agent tool: `subagent_type: "vibe-editing-os:veos-runner"`. Prompt it with the project path and these commands, in order:
   - `veos ingest --project "P"` (no paths: it uses the clips stored in project.json)
   - `veos conform --project "P"`
   - `veos transcribe --project "P"` (append `--script "<script path>"` only if the project has a script)
   - `veos matte --project "P"`

   Tell it matte and transcribe can take minutes (Bash timeout 600000) and to stop at the first failure.
3. If its verdict is `failed`: run `veos project set --project "P" last_error="prep: <short reason>"` and stop with a plain-language message (what failed, what the user can try: re-run `/vibe-editing-os:reel` to resume, or run `veos doctor`). Do not continue.
4. Verify the done condition (workflow phase `prep`). In the project work folder: `sources.json` exists, and for every talking-head source `src/`, `audio/<id>.wav`, `words/<id>.json`, `matte/<id>*` and `face/<id>*` exist. Check with Bash `ls`. If anything is missing, treat it as a failure (step 3) and name the missing file.
5. Only now run `veos project set --project "P" phase=prep last_error=""`.
6. Reply to the orchestrator in 2-3 lines: sources found, total duration, word count, and that phase is `prep`.

Rules: phases are idempotent and re-use cached outputs, so on resume just run the steps again. Make no creative decisions here.
