# Social Studio (Mondays ~12:30 AM ET)

Read CLAUDE.md, then ONLY these skills in
.claude/skills/: content-mix, brand-voice, content-rules,
platform-formats, monetization, video-assembly (and higgsfield-api only if a
promo needs realistic people). Run studio scripts from the repo root.

Tools: the environment's Setup script installs them. Check with
`command -v ffmpeg rhubarb`; only if one is missing run
`bash studio/setup.sh`. Still missing: set the "Autopost — Social"
row (Notion → Automation Control) to Error with the reason, and stop.

1. Read the "Autopost — Social" row. Enabled = schedule in Buffer with
   automatic publishing; unchecked = Buffer drafts only.
2. Make this week's promos exactly as content-mix defines them: The Sovereign
   (Tuesday) and The Global Aggregate (Thursday); PoolParty only once
   content-mix says it has launched; clipping ads only if content-mix names a
   reachable source. Real material only. If a source can't be fetched
   (for example globalaggregate.org answers 429 / a Vercel challenge), skip
   that promo and say so in the run notes. Never a text-only reel.
3. Render with `python3 studio/text_reel.py`; public link with
   `python3 studio/upload_video.py`; schedule at a good time for a US Eastern
   audience. Higgsfield spend cap: $5/week, logged.
4. Draft instead of scheduling anything rule 1 says must be a draft.
5. Set Last Run, Last Run Status, Last Run Notes (one or two lines) on the row.

Keep it lean: don't read files or databases you don't need; one attempt per
failing source, then move on.
