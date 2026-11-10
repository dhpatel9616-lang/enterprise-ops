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
   Take the oldest folder. **None: make today's clip yourself** (owner,
   2026-11-04: nothing was filling the queue, so no clip had posted since
   Oct 14):
   - Pick one real, surprising or funny moment from public-domain or US
     government footage: Cold War civil-defense films, newsreels, NASA,
     presidential addresses and press briefings, congressional hearings
     (search with `python3 studio/find_footage.py find "<words>" --source
     archive` or `--source nasa`). Rotate topics; nothing posted in the last
     30 days (check `posted/`). No TV-network footage when making your own.
   - Find the 20–45 seconds worth watching (transcribe a few minutes with
     faster-whisper if it's talking), then
     `python3 studio/find_footage.py get URL seg.mp4 --start S --len N --keep-audio` (keep the
     speech) and
     `python3 studio/clip_reel.py seg.mp4 clip.mp4 --title "<hook>" --credit "<source>"`.
     Look at three frames before posting.
   - Title and caption follow the campaign's Round 4 voice: funny or
     surprising first, never preachy ("In 1951 the government's plan for a
     nuclear blast was: get under your desk").
   - Upload it (`python3 studio/upload_video.py clip.mp4`; it prints the public link)
     and use that one link for all three platforms in step 5; write a
     `clip.json` the same way, plus `source_url`, `start`, `len` and `credit`
     (the Sunday montage re-cuts each clip from these). After posting, save it:
     `python3 studio/upload_video.py clip.json posted/<date>-<slug>/clip.json --bucket civic-clips`.
3. Check it: public-domain or official public record footage (or a short
   network excerpt, see step 4), source named
   on screen and in the caption, nothing edited to change meaning, no
   private person at the center. Fails: move it to `rejected/` with the
   reason and stop.
4. Write the caption: a hook line (what happens, in search words), one line
   of context with the real names, date and venue, the source line, a
   question, and 8–12 hashtags (topic + #history/#politics/#civics +
   community tags like #historytok #politicstok + #WadeCapitalClips). No AI
   disclaimer text. Title under 60 characters.
   Save as a **draft** instead (and say why) if it touches elections,
   candidates or voting, is under 24 hours old, makes a claim the source
   doesn't show, or uses a TV-network news excerpt (allowed here only at 10
   seconds or less, with our commentary and the network credited; reject
   longer ones).
5. Public URLs: the bucket is public
   (`<url>/storage/v1/object/public/civic-clips/queue/<id>/<file>`). Post with
   `python3 studio/buffer_clips.py post clip.json` (fill `videos`,
   `caption`, `title`, `when` = today 5:15 PM ET for TikTok-friendly
   evening reach). Then move the folder to `posted/`.
6. Update the row: Last Run, Status, and Notes (the title, or why it was a
   draft/rejected).

## Sundays: the week's montage (long-form on YouTube @WadeCapitalClips)

Owner, 2026-11-10: clipping runs long-form on YouTube too. After the day's
clip, on Sundays only:
1. Take this week's clips from `posted/` (their `clip.json`: `source_url`,
   `start`, `len`, `title`, `credit`); at least 3, at most 10. Fewer than 3:
   skip and say so.
2. Write `montage.json` (`{"title": ..., "clips": [{"url", "start", "len",
   "title", "credit"}]}`) with a funny-first, search-friendly title (Round 4
   voice), e.g. "The Government Told Kids to Hide Under Desks, and 6 More
   Moments From the Archive". Then `python3 studio/clip_montage.py
   montage.json montage.mp4` and look at three frames.
3. Upload it (`python3 studio/upload_video.py montage.mp4`) and post it to
   **YouTube only** with `python3 studio/buffer_clips.py post` (`videos` has
   just `youtube`; description lists each clip with its source; same draft
   rules as step 4).
