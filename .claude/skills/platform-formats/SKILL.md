---
name: platform-formats
description: Format specs for YouTube long-form, YouTube Shorts, TikTok, and Instagram Reels, including hooks, lengths, aspect ratios, captions, safe zones, and each platform's AI-content labeling rule. Use when writing a script or storyboard, rendering a video, or preparing a Buffer draft for any of these platforms.
---

# Platform formats

Platform limits change often. Before relying on a number marked (check),
confirm it against the platform's current help page and update this file in
a PR if it changed. Last reviewed: 2026-09.

## YouTube long-form
- **Frame:** 16:9, 1920×1080, 30 fps. Thumbnail 1280×720.
- **Length:** 8–15 min is the target (8+ min allows mid-roll ads).
- **Hook:** first 15 seconds say what the viewer gets and why it matters. No
  logo intros.
- **Structure:** hook → promise → 3–5 chapters → recap → CTA.
- **Chapters:** timestamps in the description starting at `00:00`, at least 3,
  each at least 10 seconds.
- **Captions:** upload an `.srt` file (don't rely only on auto-captions).
- **Title:** under ~60 characters so it isn't cut off; description's first 2
  lines carry the CTA and any disclosures (they show before "more").
- **AI label:** in YouTube Studio, answer "Yes" to *Altered or synthetic
  content* when realistic AI people, places, events, or voices appear.
  Cartoon hosts and AI help with scripts/editing don't need it.
- **Audience setting:** our content is for adult beginners, so "Not made for
  kids" is normally correct. A cartoon host alone doesn't make it for kids;
  if a video might really be aimed at children, ask the owner.

## YouTube Shorts
- **Frame:** 9:16, 1080×1920. **Length:** up to 3 min (check); aim 20–45 s.
- **Hook:** first 1–2 seconds, on screen *and* spoken.
- **Captions:** burned in, large, centered; keep text out of the bottom
  ~20% and right ~15% (buttons cover it).
- **Loop:** end so it flows back into the start.
- **AI label:** same *Altered or synthetic content* rule as long-form.

## TikTok
- **Frame:** 9:16, 1080×1920. **Length:** up to 10 min in-app (check); aim
  21–45 s for a new account.
- **Hook:** first 1–3 seconds; say the payoff up front.
- **Caption:** first line is the hook; 3–5 relevant hashtags; captions burned
  in with the same safe zones as Shorts.
- **AI label:** turn on the *AI-generated content* toggle for realistic AI
  images, video, or audio. TikTok may auto-label files that carry C2PA
  "Content Credentials".

## Instagram Reels
- **Frame:** 9:16, 1080×1920; keep key content inside the center 3:4 area
  (profile grid crop). **Length:** up to 3 min (check); aim 15–45 s.
- **Hook:** first 1–3 seconds.
- **Caption:** up to 2,200 characters; 3–5 hashtags; CTA in the first line.
- **AI label:** use *Add AI label* for photorealistic AI video or
  realistic-sounding AI audio. Meta may auto-label files with C2PA/IPTC data.

## Buffer and labels
Buffer may not expose every platform's AI-label toggle. When a post needs one,
write at the top of the Buffer draft's note: "NEEDS AI LABEL: turn on
[platform toggle] before approving", and put "Made with AI" in the caption.

## Every platform
- Revenue path + CTA per `monetization`.
- Honesty rules per `content-rules`.
- Voice per `brand-voice`.
