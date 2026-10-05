# YT Video Studio (Fridays ~12:30 AM ET)

Read ~/enterprise-ops/CLAUDE.md, then ONLY these skills: content-mix,
voiceover-workflow, video-assembly, character-bible, brand-voice,
content-rules, monetization, platform-formats. Run studio scripts from
~/enterprise-ops.

Tools: check `command -v ffmpeg rhubarb` and `python3 -c "import kokoro_onnx"`;
only if something is missing run `bash ~/enterprise-ops/studio/setup.sh`.
Still missing: set the "Autopost — YouTube long-form" row to Error with the
reason, and stop.

1. In Notion → Scripts, take the oldest item with Status Recorded (use the
   owner's file from Drive "Voiceovers"); if none, the oldest Ready to Record
   item whose Platforms include "YouTube long-form", voiced with
   `python3 studio/ai_voice.py` (voiceover-workflow). If neither exists, write
   the next Robot episode first (content-mix → Robot's long-form series) and
   use it.
2. Build the video: Robot (`studio/render_puppet.py --character robot-host
   --layout wide`), storyboard visuals, burned-in captions, chapters, a
   thumbnail, title, description with sources, the CTA, and the AI-voice
   disclosure.
3. Save video, thumbnail and metadata to Drive "Ready to Publish"; set the
   item to Ready to Publish. If "Autopost — YouTube long-form" is Enabled,
   upload with `python3 studio/youtube_upload.py` set to go public Saturday
   10:07 AM ET, then set the item to Published with the link.
4. Cut the best 30–60 s into a 9:16 Short, get a public link
   (`studio/upload_video.py`), and schedule it in Buffer for Sunday (draft if
   the Social switch is off).
5. Write next week's episode from the next brief (content-mix) and set it to
   Ready to Record.
6. Set Last Run fields on both Autopost rows (one or two lines each).

Keep it lean: render in parallel chunks, don't re-render to check, and don't
read anything the steps above don't need.
