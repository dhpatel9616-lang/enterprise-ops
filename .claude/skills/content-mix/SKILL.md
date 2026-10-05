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
The launch campaign (`campaigns/launch-campaign.md`) sets the week: five ads
Mon–Fri alternating The Sovereign and The Global Aggregate, each on Instagram
Reels, TikTok and YouTube Shorts, plus Robot's Short on Sunday. PoolParty
joins after launch; clipping ads when a source exists.

**Rule 1 means draft, not skip.** A post that names politicians or private
people, touches elections or breaking news, or makes an unsourced claim is
still made, then saved as a Buffer draft with a one-line reason. Only skip
something that can't be made honestly at all. War, crime, and hard news in
general are not banned; they're drafts when rule 1 applies.

Channels (Buffer): Instagram @wadecapitallc and TikTok @wadethesovereign get
every promo; YouTube Shorts gets the Sovereign, Robot and clipping posts. Buffer's
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
- Pick the newest published issue that hasn't been promoted yet (check
  Buffer's sent and scheduled posts for the issue title). Older issues are
  evergreen: keep working back through the archive
  (`https://sovereignnewsletter.substack.com/feed`) before repeating one.
- Skip an issue only if it can't be promoted honestly (it rests on a private
  person, or on images we have no right to use). An issue that turns on a
  real public figure is still made, but saved as a Buffer draft
  (CLAUDE.md rule 1). Log which issue you used and why others were skipped.
- Visuals: the issue's own images when they load (`substackcdn.com`); most
  issues only carry the newsletter logo, so the default is 2–3 realistic
  `promo-cast` scenes from `higgsfield-api` that illustrate the issue's idea
  (cheapest image model, AI-labeled), never other publishers' charts or
  photos.
- Beats: hook quote → 2–3 verbatim pull quotes over the scenes → the
  one-line argument → "Read the full piece" card with the issue title.
- Quotes are **word for word** from the published issue. Never invent,
  trim mid-sentence to change meaning, or "improve" a quote.

## Robot's Short (channel promotion)
The weekly 30–60 s Short cut from Robot's episode (YT Video Studio) goes to
YouTube Shorts, Instagram and TikTok, with "Full episode on YouTube" as the
CTA. It counts as promotion for the YouTube channel; it doesn't replace the
Sovereign or Global Aggregate promos.

## The Global Aggregate promo
- Data comes straight from the site's own database (globalaggregate.org sits
  behind a bot checkpoint we can't switch off; it's hosted by Rocket).
  Read-only REST on `https://nikvqivovodrfybfjjka.supabase.co/rest/v1/` with
  the public key in `GA_SUPABASE_ANON_KEY` (the same key the site gives every
  visitor):
  `trending_clusters?select=cluster_id,country_count,source_count,article_count,latest_activity&order=country_count.desc&limit=30`,
  then `articles?select=title,source,country,url,published_at&cluster_id=eq.<id>`.
- Story ads: pick a cluster from the last 48 hours with 3+ countries, preferring
  science, economy, sport, culture, space, health, business. Rule 1 clusters
  (elections, breaking news, named private people) are made as drafts.
- Generic brand ads (By the numbers, How it works, Who it's for) need no
  story and can always post; see `campaigns/launch-campaign.md`.
- Beats: two or three real headlines from different countries (outlet +
  country + date, exactly as published) → "covered by N outlets in M
  countries" → "Use The Global Aggregate". Render the headline cards with
  `text_reel.py` image scenes (our own branded cards; no screenshots needed).
- If `GA_SUPABASE_ANON_KEY` isn't set, skip and say so in the run notes.
  Add the ownership disclosure when branded as The Sovereign (`monetization`).

## PoolParty promo
- Realistic `promo-cast` scenes (`campaigns/poolparty-friendly-wagers.md`)
  plus **real app screens** from the owner's recordings. Never invent app
  screens.
- **Paused until PoolParty's initial launch** (owner, 2026-10-01). Target
  launch: **Friday, October 9, 2026**. Until it launches, skip the Saturday
  post and say so in the run notes. Before the first ad, confirm with the
  owner the App Store link and the honest money message (see Open items).

## Clipping ads and montages
- Clipping work currently lives outside this setup (a "clipping" folder on
  the owner's computer, worked on in a separate Claude Code chat; no repo
  yet). Until it has a repo or shared folder we can reach, there are no
  clipping posts. Footage must be one of: public domain (US federal government works such as official
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

## Robot's long-form series (one episode a week)
Owner-approved order (2026-10-03). Each is a page in Notion → Scripts.
Ep. 1 is a full script; Ep. 2–7 are briefs titled "(brief)" with no Status.

1. How Civilization Ends in 72 Hours (pilot)
2. One Password Shut Down the East Coast's Gas
3. Every Empire Thinks It's the Exception
4. When the Sun Attacks (the Carrington Event)
5. Stuxnet, the First Digital Weapon
6. What Happens When Money Stops Working
7. The Hackers Who Turned Off the Lights

**Writing next week's script** (YT Video Studio step 5): take the lowest-
numbered "(brief)" page, verify every fact against its sources (drop or
soften anything you can't confirm), and add a `## Spoken script` section in
Robot's voice: ~1,400–1,600 words (~10 min), a cold-open hook from a real
moment, chapters, one practical takeaway, and the CTA. Add a `## Storyboard`
and a `## Sources` section, remove "(brief)" from the title, and set it to
Ready to Record. Match Ep. 1's structure and tone. After Ep. 7, propose the
next three in the Strategy Memo for the owner to pick; don't start
generic topics (the owner rejected "who runs America", "survival lessons
from history", and "map of everything you depend on" as too generic).

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
- A home for the clipping work that routines can reach (GitHub repo or
  shared Drive folder).
