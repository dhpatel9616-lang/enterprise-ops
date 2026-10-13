# Clip Studio (daily ~12:15 PM ET)

Read CLAUDE.md, then ONLY these skills: content-mix (clipping section),
content-rules, platform-formats.

Posts one finished clip a day to the **clip accounts only** (IG
@wadecapitalclips, TikTok @wade.clips3, YouTube @WadeCapitalClips) through
their own Buffer account: `python3 studio/buffer_clips.py`, which needs
`BUFFER_CLIPS_API_KEY`. **Never use the Buffer connector tools here** (they
are the promo/media account), and never post clips anywhere else.

1. Notion → Automation Control → "Autopost — Clips": Enabled = schedule;
   unchecked = Buffer drafts (`--draft`). (View mode or fetch, never SQL.)
2. The clipping work drops finished clips in the Supabase `civic-clips`
   bucket under `queue/<clip-id>/` (ENTERPRISE_SUPABASE_URL /
   ENTERPRISE_SUPABASE_SERVICE_KEY): `instagram.mp4`, `tiktok.mp4`,
   `youtube.mp4` and `clip.json` (title, source, date, one-line context).
   Take the oldest folder. None: note "queue empty" in the row and stop.
3. Check it: public-domain or official public record footage, source named
   on screen and in the caption, nothing edited to change meaning, no
   private person at the center. Fails: move it to `rejected/` with the
   reason and stop.
4. Write the caption: a hook line (what happens, in search words), one line
   of context with the real names, date and venue, the source line, a
   question, and 8–12 hashtags (topic + #history/#politics/#civics +
   community tags like #historytok #politicstok + #WadeCapitalClips). No AI
   disclaimer text. Title under 60 characters.
   Save as a **draft** instead (and say why) if it touches elections,
   candidates or voting, is under 24 hours old, or makes a claim the source
   doesn't show.
5. Public URLs: the bucket is public
   (`<url>/storage/v1/object/public/civic-clips/queue/<id>/<file>`). Post with
   `python3 studio/buffer_clips.py post clip.json` (fill `videos`,
   `caption`, `title`, `when` = today 5:15 PM ET for TikTok-friendly
   evening reach). Then move the folder to `posted/`.
6. Update the row: Last Run, Status, and Notes (the title, or why it was a
   draft/rejected).
