# YT Video Studio (Tuesdays and Fridays ~12:30 AM ET; two episodes a week, owner 2026-10-15)

Read CLAUDE.md, then ONLY these skills: content-mix,
voiceover-workflow, video-assembly, character-bible, brand-voice,
content-rules, monetization, platform-formats. Run studio scripts from
the repo root.

Tools: check `command -v ffmpeg rhubarb` and `python3 -c "import kokoro_onnx"`;
only if something is missing run `bash studio/setup.sh` (allow it 10 minutes; the voice tools are ~800 MB) and read its output.
Still missing: set the "Autopost — YouTube long-form" row to Error with the
exact "setup: ..." lines from that output (they name what failed), and stop.

1. In Notion → Scripts, take the oldest item with Status Recorded (use the
   owner's file from Drive "Voiceovers"); if none, the oldest Ready to Record
   item whose Platforms include "YouTube long-form", voiced with
   `python3 studio/ai_voice.py` (voiceover-workflow). If neither exists, write
   the next Robot episode first (content-mix → Robot's long-form series) and
   use it.
2. Build the video: Robot (`studio/render_puppet.py --character robot-host
   --layout wide`), storyboard visuals, burned-in captions, chapters, a
   thumbnail, title, description with sources, the CTA, and the AI-voice
   disclosure. The description's **first two lines are clickable links**
   (the only clickable links we get; Shorts and Instagram captions aren't):
   `https://sovereignnewsletter.substack.com/?utm_source=youtube&utm_medium=video&utm_campaign=ep<N>`
   and `https://globalaggregate.org/?utm_source=youtube&utm_medium=video&utm_campaign=ep<N>`,
   so Substack's and the site's traffic stats show what each episode sends.
   The Short cut in step 4 must be **45 s or less** (`ffprobe`; Ep. 2's ran
   59 s).
3. Save video, thumbnail and metadata to Drive "Ready to Publish"; set the
   item to Ready to Publish. If "Autopost — YouTube long-form" is Enabled,
   upload with `python3 studio/youtube_upload.py` set to go public at 10:07 AM
   ET the next day (Tuesday run → Wednesday, Friday run → Saturday), then set
   the item to Published with the link.
4. Cut the best 30–60 s into a 9:16 Short, get a public link
   (`studio/upload_video.py`), and schedule it in Buffer at an exact time
   (never the queue): Tuesday run → Thursday 9:00 PM ET, Friday run → Sunday
   9:00 PM ET, on YouTube Shorts, Instagram and TikTok (drafts if the Social
   switch is off). Only
   the promo + media channels in Buffer organization `6ab6c71cddecb7a5c80b918f`
   (IDs in `campaigns/launch-campaign.md`); never the clip accounts.
5. Write the next episode from the next brief (content-mix) and set it to
   Ready to Record, so the next run (three or four days away) has a script.
   Write it in the owner's voice (`brand-voice` → "The owner's voice").
   Voice every episode through the quality gate in `routines/social-studio.md`
   (`studio/vo_check.py` must pass; its captions are the ones to burn in).
6. Set Last Run fields on both Autopost rows (one or two lines each).

Keep it lean: render in parallel chunks, don't re-render to check, and don't
read anything the steps above don't need.
