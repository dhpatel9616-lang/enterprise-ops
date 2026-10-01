---
name: content-mix
description: What we make and when. Short-form promos (9:16) for The Sovereign, The Global Aggregate, and PoolParty built from real material from each product (Substack issues, real Global Aggregate story clusters, real app screens), political/historical "clipping" ads, and the two long-form lanes (Robot tutorials, clipping montages). Use when planning or drafting the week's posts, Buffer drafts, or long-form videos.
---

# Content mix

Source: owner, 2026-10-01. **We promote our three products. We don't
promote Wade Capital services on social** (small-business outreach is phone
and email only; see the Enterprise-leads repo).

| Lane | Format | Who's on screen | Where |
|---|---|---|---|
| **Short-form promos** for The Sovereign, The Global Aggregate, PoolParty | 9:16, 15–45 s | Real material from the product, plus realistic `promo-cast` actors and situations when a scene needs people | IG Reels, TikTok, YouTube Shorts |
| **Clipping ads** (political and historical moments) | 9:16, 15–45 s | Real archival or public footage | Same, always as **drafts** (see below) |
| **Robot tutorials**: grid-down survival, cybersecurity, history, politics | 16:9, 8–15 min, mostly animated | Robot (cartoon, `character-bible`) | YouTube long-form |
| **Clipping montages** | 16:9, long-form | Real footage from the clipping repo, with our narration and context | YouTube long-form |

Realistic AI people and situations are **for promotion only**, never in
long-form content (`character-bible`).

## Weekly short-form slate
Three promos a week, one per product, plus clipping ads when there are good
clips:

| Day | Post | CTA | Link |
|---|---|---|---|
| Tue | **The Sovereign** issue promo | "Read the full piece" | the issue's Substack link |
| Thu | **The Global Aggregate** story promo | "Use The Global Aggregate" | https://globalaggregate.org |
| Sat | **PoolParty** promo (see Blocked) | "Download PoolParty" | App Store link |
| any | Clipping ad (optional, up to 2) | "Watch the full montage" or "Read The Sovereign" | YouTube video or Substack |

Channels (Buffer): Instagram @wadecapitallc and TikTok @wadethesovereign get
every promo; YouTube Shorts gets the Sovereign and clipping posts. Buffer's
free plan holds 10 scheduled posts, so schedule one week ahead at most.

## The quality bar (why the text reels were rejected)
A promo must **show the real thing and teach one real thing**. Plain text
on a background fails both. Every promo has:
1. **A hook in the first 2 seconds** that is a real detail: a striking line
   from the issue, two clashing real headlines, a real app moment.
2. **Real material on screen most of the time**: the issue's own images
   and verbatim quotes, screenshots of the real Global Aggregate page and
   real headlines, real app screens. Data shown as big numbers with their
   source on screen ("28 outlets · 14 countries · source: globalaggregate.org").
3. **Motion**: slow push-ins on images, quotes that type or slide in, cuts
   every 2–4 s, captions burned in, music from a free-licence library.
4. **One takeaway** a viewer could repeat to a friend, then the CTA card.

If the real material can't be fetched (site blocked, no new issue), **skip
the post** and say why in the run notes. Never fall back to a text-only reel
or stock filler.

## The Sovereign promo
- From the newest published issue not yet promoted
  (`https://sovereignnewsletter.substack.com/feed`; images are on
  `substackcdn.com`).
- Beats: hook quote → 2–3 real pull quotes over the issue's images (or a
  realistic `promo-cast` situation that illustrates the topic, AI-labeled)
  → the one-line argument → "Read the full piece" card with the issue
  title.
- Quotes are **word for word** from the published issue. Never invent,
  trim mid-sentence to change meaning, or "improve" a quote.
- Issues that name real private people, or turn on a real public figure,
  go out as drafts (CLAUDE.md rule 1).

## The Global Aggregate promo
- Pick one real story cluster on https://globalaggregate.org that is not
  breaking news or election news (rule 1). Prefer science, economy,
  culture, and world events where countries frame things differently.
- Beats: two or three real headlines about the same event from different
  countries (outlet + country flag + date on screen) → the number of
  outlets and countries covering it → a screen capture of the real cluster
  page → "Use The Global Aggregate".
- Headlines are shown exactly as published, with the outlet's name. Add
  the ownership disclosure when the post is branded as The Sovereign
  (`monetization`).

## PoolParty promo
- Realistic `promo-cast` scenes (`campaigns/poolparty-friendly-wagers.md`)
  plus **real app screens** from the owner's recordings. Never invent app
  screens.
- **Blocked** until the owner settles the money question (see Open items)
  and the App Store link exists. Until then, skip the Saturday post and
  say so in the run notes.

## Clipping ads and montages
- Footage comes from the clipping repo (owner to share which one) and must
  be one of: public domain (US federal government works such as official
  House/Senate floor video, pre-1930 film), openly licensed with
  attribution, or a short excerpt used for commentary that adds our own
  context (fair use). Credit the source on screen. If you can't tell which,
  don't use it.
- Never edit a clip to change what someone said or meant; keep enough
  context that the point stands on its own. No AI-altered footage of real
  people, ever (`content-rules`).
- Nonpartisan (`brand-voice`): over a month, balance who is shown, and
  frame each clip around an idea, not a side.
- Because they show real politicians, **clipping posts are always Buffer
  drafts** for the owner to approve (CLAUDE.md rule 1), even with Autopost
  on.

## Making the videos
- Short-form: `studio/text_reel.py` with `image` scenes (real images with a
  slow push-in, quotes, big numbers); put each week's specs and the
  downloaded source files in `campaigns/<year>-w<week>/`. Realistic scenes
  come from `higgsfield-api` (cheapest model that meets the brief).
- Long-form: `voiceover-workflow` + `video-assembly` (Robot, `--layout wide`).

## Every post
- Voice from `brand-voice`, format from `platform-formats`, honesty rules
  from `content-rules`, revenue path + CTA per `monetization`.
- One CTA per post, exactly as written above.

## Open items (ask the owner; don't guess)
- **PoolParty and money.** The app's real screens show dollar stakes ("$…
  total staked", "Mark as Paid", "% paid on time"). The campaign's line "No
  real money. Just bragging rights." would be false. Decide the true
  message before any PoolParty ad runs.
- PoolParty App Store link (at launch).
- Which repo holds the clipping work.
- Network access for `substackcdn.com` and `globalaggregate.org` in the
  cloud environment (images and screenshots).
