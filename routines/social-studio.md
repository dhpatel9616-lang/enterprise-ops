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
   scenes and cards full-frame, Robot only a small corner bubble. Footage in
   the campaign's order: real material and `studio/find_footage.py` (real
   briefings and archive film, then Pixabay stock) before any Higgsfield
   shot. Never a slideshow or text-only reel.
   PoolParty only after content-mix says it has launched. Rule 1 means DRAFT,
   not skip. If a source truly can't be fetched, make a different series'
   story for that day instead of leaving it empty.
   Captions follow the campaign file: hook line, story detail, the product's
   link + "link in bio", a question, 8–12 rotating hashtags, no AI disclaimer
   text (set the platform AI flag only if realistic AI imagery is used).
3. Public link with `python3 studio/upload_video.py`; schedule per the
   campaign's timing.
   **Higgsfield hard cap: $2.00 per run** (Social Studio runs once a week and
   is the only routine that uses Higgsfield; owner, 2026-10-14). That's at
   most **7 Hailuo shots** ($0.28 each). Before every Higgsfield call, add up
   this run's spend; if the next call would pass $2.00, don't make it: use
   free footage or a card instead. Put the run's total in the run notes and
   the cost log.
   **Buffer guard:** only Buffer organization `6ab6c71cddecb7a5c80b918f` and
   only its channels `6ab6cac8ea19ca0bdeea0fba` (Instagram @wadecapitallc),
   `6ab6caf4ea19ca0bdeea114e` (TikTok @wadethesovereign) and
   `6ab6d22fea19ca0bdeea4810` (YouTube @WadeCapital). Never post to any other
   organization or channel (the clip accounts), and never post clips here.
4. Draft instead of scheduling anything rule 1 says must be a draft (with the reason in the Buffer note).
5. **Podcast:** `python3 studio/podcast.py` (voices any new Sovereign issue
   with the free male voice and updates the podcast feed; "no new issue" is
   fine). Run it **before** step 2's rendering when there's a new issue, so
   Thursday can be "The Sovereign, Out Loud" (`studio/audiogram.py`, see the
   campaign's podcast section). **Medium:** for a new issue, add to the run notes: "Medium: import
   <issue link> at medium.com/p/import" (the owner does that by hand).
6. Set Last Run, Last Run Status, Last Run Notes (one or two lines) on the row.
7. **Drafts alert (owner, 2026-10-14; push notifications don't reach them):**
   if this run saved any Buffer drafts, send ONE short email with the Gmail
   connector to the connected account's own address (email yourself: the
   sender on any `in:sent` message). Subject: "Social Studio: N drafts to
   approve". Body, plain text, under 120 words: one line per draft (channel,
   day, the hook line, the one-line rule-1 reason), then "Approve in Buffer:
   https://publish.buffer.com → Drafts" and the run's Higgsfield total. No
   drafts: send nothing. Never email anyone else.

Keep it lean: don't read files or databases you don't need; one attempt per
failing source, then move on.
