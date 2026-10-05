---
name: reel-captions
description: Captions phase of a Vibe Editing OS project — produce the exact on-screen text for every spoken word in the language and script the creator's playbook specifies, with correct names and fixed mis-hearings, then apply it. Called by the reel orchestrator after the rough cut.
user-invocable: false
---

# Captions (display text for every word)

1. **Get the caption rules.**
   - `veos project show --project "P"` → the playbook id.
   - Read `<playbooks>/<id>/tokens.json` → `creator.caption_language`, `creator.glossary`.
   - Read the playbook's **§5** (type and language rules).
2. `veos captions status --project "P"`. If every word is captioned and nothing is low-confidence or in the wrong script, go to step 6.
3. `veos context --project "P" --part words` → edit-time words `i:word@t` (`?` = low confidence), plus the script excerpt.
4. **Write a caption for EVERY index** into `P/work/captions.map.json` as `{"<i>": "text"}`:
   - **Language and script:** follow the playbook exactly.
     - Romanised Hinglish → transliterate any Devanagari word, one-to-one per index.
     - English → keep the spoken English.
     - A native script → keep it in that script.
   - **Never merge or split indices.**
   - **Mis-hearings:** fix them from context, the glossary and the script (product and tool names especially).
     - Fix spelling only. **Never change what was said.**
     - If you can't resolve a word that matters (a name, a number), note it and ask the user once, at the storyboard gate.
   - **Case:** per the playbook (often lowercase subtitles). Brand and tool names always exact. The comment keyword as the playbook says.
   - **Punctuation:** keep sentence-final punctuation on the last word.
   - **Hidden words:** use `""` for a duplicated fragment (e.g. a number split into two tokens).
5. `veos captions apply "P/work/captions.map.json" --project "P"` → it must report `missing: 0` with every word captioned.
6. `veos project set phase=captions --project "P"`.
