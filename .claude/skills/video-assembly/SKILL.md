---
name: video-assembly
description: Build finished videos with free, open-source tools only - ffmpeg rendering, code-generated motion graphics, and SVG puppet characters lip-synced to the owner's voiceover with Rhubarb Lip Sync. Use when turning a recorded voiceover and storyboard into a video for YouTube, Shorts, TikTok, or Reels.
---

# Video assembly (free tools only)

No paid editors, no stock sites without a free licence, no paid APIs here
(paid AI generation lives in `higgsfield-api` and needs a reason).

## Tools
- **ffmpeg** (with librsvg): renders SVG frames, mixes audio, encodes.
- **Rhubarb Lip Sync**: turns a voiceover into mouth shapes A-H, X.
- **Python 3 stdlib**: generates SVG frames (characters + motion graphics).
- Install/refresh all of them: `bash studio/setup.sh`.

## Pipeline
1. **Get the voiceover** (see `voiceover-workflow`); convert to WAV:
   `ffmpeg -i in.m4a -ar 44100 -ac 1 vo.wav`.
2. **Script text** → `dialog.txt`, one caption line per line (same lines the
   owner read). Helps Rhubarb and drives captions.
3. **Captions:** `python3 studio/captions_from_pauses.py vo.wav dialog.txt > captions.json`.
   Spot-check a few timings.
4. **Render the puppet clip:**
   ```
   python3 studio/render_puppet.py --character robot-host --audio vo.wav \
     --dialog dialog.txt --captions captions.json --out clip.mp4
   ```
   Output is 1080×1920 (Shorts/TikTok/Reels). For YouTube long-form, change
   `W, H` to 1920×1080 in the script's call site or add a flag in a PR.
5. **Extra graphics** (title cards, charts, lower thirds): write them as SVG
   in code, render with ffmpeg, and join with the `concat` demuxer or
   `overlay` filter. Keep brand colors from `brand-voice`.
6. **Check before handing off:** watch 3 frames (start/middle/end) as stills,
   confirm length and safe zones (`platform-formats`), CTA and disclosures on
   screen (`monetization`), AI label need (`content-rules`).
7. Update the Notion **Scripts** item to *Assembled* and continue with
   `voiceover-workflow` step 5.

## Characters
Always render characters from `character-bible/characters/<id>/rig.py`;
never redraw them. A new character = a new folder with its own `rig.py`
exposing `draw(mouth, t, blink, wave)`.

## Example
`studio/samples/robot-host-style-test/make.sh` rebuilds the 10-second style test
end to end (with a robot placeholder voice).
