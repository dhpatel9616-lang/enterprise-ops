# YT Video Studio prompt (schedule: Fridays 1:37 AM Eastern)

```
UNATTENDED SCHEDULED RUN. No one is present: do not ask questions or wait for
input. Make reasonable decisions, record any assumption in the output, and if
truly blocked, log the blocker in this week's Strategy Memo and stop.

0. SETUP FIRST: run `git clone --depth 1 https://github.com/dhpatel9616-lang/enterprise-ops ~/enterprise-ops`
   (public repo) and `bash ~/enterprise-ops/studio/setup.sh`. Read
   ~/enterprise-ops/CLAUDE.md and every ~/enterprise-ops/.claude/skills/*/SKILL.md,
   follow them, and run studio scripts from ~/enterprise-ops. If the clone or
   setup fails, set the "Autopost — YouTube long-form" row's Last Run Status to
   Error with the reason, and stop.
1. Take the oldest Scripts item marked Recorded and fetch its voiceover from
   the Drive "Voiceovers" folder. If none exists, take the oldest Ready to
   Record item and voice it with the backup robot voice (voiceover-workflow
   skill), and note that in the Strategy Memo.
2. Assemble the full YouTube video with Robot
   (`python3 studio/render_puppet.py --character robot-host --layout wide ...`):
   lip-synced host, motion graphics, burned-in captions, chapter markers, a
   custom thumbnail, and a title and description with the CTA from the
   monetization skill (affiliate disclosure only if affiliate links are used).
   Keep it under 15 minutes. Educational with humor, per brand-voice.
3. Save the final video, thumbnail, and a metadata file to the Drive folder
   "Ready to Publish" and set the Scripts item to Ready to Publish. If the
   "Autopost — YouTube long-form" row is Enabled, upload it with
   `python3 studio/youtube_upload.py <video.mp4> <metadata.json>` scheduled to
   go public Saturday 10:07 AM ET, then set the Scripts item to Published with
   the video link. If the uploader has no credentials, leave the video in
   Ready to Publish and log why.
4. Cut the strongest 30-to-60-second moment into a vertical 9:16 Short. Get a
   public link with `python3 studio/upload_video.py`. Check it against
   content-rules, then, following the "Autopost — Social" switch, schedule it
   in Buffer for Sunday with automatic publishing (or save it as a draft if
   the switch is off).
5. Write next week's YouTube script, set it to Ready to Record, update both
   Automation Control rows' Last Run fields, and add a run summary to this
   week's Strategy Memo.
```
