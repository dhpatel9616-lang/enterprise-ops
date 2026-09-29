---
name: voiceover-workflow
description: The script → owner records → assemble loop. Claude writes the script and a storyboard to the Notion Scripts database, waits for the owner's recording in the Google Drive "Voiceovers" folder, then assembles the video and saves it as a Buffer draft. Use for any video that uses the owner's voice.
---

# Voiceover workflow

## Places
- Notion: **The Enterprise — Command Center → Scripts**
  (data source `collection://894c2e0b-cac7-4d7b-8746-6a3d89f42b47`).
- Google Drive: **Voiceovers** folder
  (id `1894qw4nzqNNxRxWA6Q7JH8Z2PwyY2l6K`).

## Status flow
`Ready to Record` → `Recorded` → `Assembled` → then either
- social (Shorts/TikTok/Reels): `In Buffer` (a draft the owner approves), or
- YouTube long-form: `Ready to Publish` → `Published`. Only the approved
  uploader workflow moves it to Published, and only while Notion → Automation
  Control → "Autopost — YouTube long-form" is Enabled.

Find items with a Notion **view** or **fetch**, never SQL mode (CLAUDE.md).

## 1. Write (Claude)
Create a Scripts item:
- **Title**, **Brand**, **Platforms**, **Revenue Path**, **CTA**
  (`monetization`), link the **Idea** it came from.
- **Voiceover Filename:** `YYYY-MM-DD-short-title` (e.g. `2026-10-02-wifi-basics`).
- **Status:** Ready to Record.
- Page body:
  1. The brief checklist from `monetization`.
  2. **Script to read**, one short line per line (each line becomes a
     caption), hook first, following `platform-formats` and `brand-voice`.
  3. **Storyboard** table: line # | what's on screen | character pose/mouth
     emphasis | on-screen text.
  4. **Recording steps for the owner** (copy this block every time):

> **How to record this (about 5 minutes)**
> 1. Go somewhere quiet. Soft rooms (a closet, a car) sound best.
> 2. Open your phone's voice recorder app (iPhone: *Voice Memos*; Android:
>    *Recorder*). Hold the phone about a hand's width from your mouth.
> 3. Tap record. Read each line above, then **pause for one full second**
>    before the next line. If you stumble, pause and re-read that line.
> 4. Tap stop. Rename the recording to exactly the **Voiceover Filename**
>    shown above.
> 5. Share it to Google Drive: tap *Share* → *Drive* → choose the
>    **Voiceovers** folder → *Upload*.
> That's it; Claude picks it up on the next night shift.

## 2. Wait (Claude, each night)
Search the Voiceovers folder for each *Ready to Record* item's filename (any
audio extension). Not there → leave it. Found → set **Recorded**.

## 3. Assemble (Claude)
Download the file, then follow `video-assembly`. If a line was re-read, keep
the last take and cut the stumble (ffmpeg `atrim`), and note it in Notion.

## 4. Check
Length, captions, CTA, disclosures, AI label need. Set **Assembled**. Upload
the MP4 to Drive next to the voiceover so the owner can watch it.

## 5. Buffer (draft only)
Buffer needs a public link to the video: run
`url=$(python3 studio/upload_video.py <video.mp4>)`. Then create a Buffer
**draft** per platform with that video URL, the caption, CTA, disclosures,
and any "NEEDS AI LABEL" note. Never schedule or publish. Set **In Buffer**
and tell the owner in plain words: "Open Buffer → Drafts, watch it, and click
Approve/Schedule if you like it."
