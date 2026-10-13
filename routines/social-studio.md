# Social Studio (Mondays ~12:30 AM ET)

Read CLAUDE.md and campaigns/launch-campaign.md, then ONLY these skills in
.claude/skills/: content-mix, brand-voice, content-rules,
platform-formats, monetization, video-assembly (and higgsfield-api only if a
promo needs realistic people). Run studio scripts from the repo root.

Tools: the environment's Setup script installs them. Check with
`command -v ffmpeg rhubarb`; only if one is missing run
`bash studio/setup.sh`. Still missing: set the "Autopost — Social"
row (Notion → Automation Control) to Error with the reason, and stop.

1. Read the "Autopost — Social" row. Enabled = schedule in Buffer with
   automatic publishing; unchecked = Buffer drafts only.
2. Make this week's five ads from `campaigns/launch-campaign.md` (Mon–Fri,
   its rhythm table and story series), following content-mix. Every ad is a
   narrated story in real video (hook → setup → turn → payoff → CTA),
   **provocative first** (the campaign's order: the most charged real story
   leads; rule 1 makes it a draft, never a reason to pick a blander one).
   Robot's voice (`studio/ai_voice.py`), the puppet rendered without captions
   (`studio/render_puppet.py --layout tall`), then `studio/story_reel.py`:
   scenes and cards full-frame, Robot only a small corner bubble. 2–3 short AI
   video shots plus real material (excerpt cards, real headline cards). Never
   a slideshow or text-only reel.
   PoolParty only after content-mix says it has launched. Rule 1 means DRAFT,
   not skip. If a source truly can't be fetched, make a different series'
   story for that day instead of leaving it empty.
   Captions follow the campaign file: hook line, story detail, the product's
   link + "link in bio", a question, 8–12 rotating hashtags, no AI disclaimer
   text (set the platform AI flag only if realistic AI imagery is used).
3. Public link with `python3 studio/upload_video.py`; schedule per the
   campaign's timing. Higgsfield spend cap: $5/week, logged.
   **Buffer guard:** only Buffer organization `6ab6c71cddecb7a5c80b918f` and
   only its channels `6ab6cac8ea19ca0bdeea0fba` (Instagram @wadecapitallc),
   `6ab6caf4ea19ca0bdeea114e` (TikTok @wadethesovereign) and
   `6ab6d22fea19ca0bdeea4810` (YouTube @WadeCapital). Never post to any other
   organization or channel (the clip accounts), and never post clips here.
4. Draft instead of scheduling anything rule 1 says must be a draft (with the reason in the Buffer note).
5. Set Last Run, Last Run Status, Last Run Notes (one or two lines) on the row.

Keep it lean: don't read files or databases you don't need; one attempt per
failing source, then move on.
