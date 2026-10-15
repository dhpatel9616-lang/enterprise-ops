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

**Rule 1 means draft, not skip, and only for the most sensitive posts**
(owner, 2026-10-14). Draft a post only if it alleges a crime or sexual violence against identifiable people, or centers a victim; centers a private (non-public) person; touches elections, candidates or voting; makes a claim you can't source; or fails `content-rules`. It is still made,
then saved as a Buffer draft with a one-line reason, and the owner gets an
email. Everything else schedules normally, including sourced news that names
politicians or public figures, war, and breaking news. Only skip something
that can't be made honestly at all.

**Two sets of accounts (owner, 2026-10-12). Never mix them.**
- **Promo + media accounts** (main Buffer account): Instagram @wadecapitallc,
  TikTok @wadethesovereign, YouTube @WadeCapital. Robot's long-form
  tutorials, promos and ad campaigns for The Global Aggregate, PoolParty and
  The Sovereign. **No clips here.**
- **Clip accounts** (their own Buffer account): Instagram @wadecapitalclips,
  TikTok @wade.clips3, YouTube @WadeCapitalClips (Shorts plus long-form clip
  montages). Only political/historical clips, posted from the clipping
  work, never from these routines.
Each free Buffer account holds 10 scheduled posts, so schedule one week ahead at most.

## Provocative first (owner, 2026-10-13)
For every product, lead with the most charged, engaging real story we have
(outrage, scandal, power, money, status, a claim people will argue with),
not the safest one. A bland explainer is the last pick. Facts stay real and
sourced, allegations stay allegations, and rule 1 still decides draft vs.
automatic: making a draft for the owner's OK is better than playing it safe.

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
  real public figure schedules normally when it's sourced (draft only per
  CLAUDE.md rule 1). Log which issue you used and why others were skipped.
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
  (elections, alleged crimes against identifiable people, private people)
  are made as drafts.
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
  don't use it. Find it with `studio/find_footage.py` (archive, NASA,
  Commons). For press conferences and briefings, use the **government's own
  recording** (White House, Pentagon, State Department, House/Senate floor),
  which is public domain, not a network's broadcast of the same event.
- **TV-network news excerpts (CNN, Fox, NBC…), clip accounts only** (owner,
  2026-10-14): 10 seconds or less per excerpt, with our own commentary or
  context around it, the network credited on screen, never the network's
  whole segment, and always saved as a **draft** for the owner's OK. Never
  on the promo accounts. It's a known copyright risk the owner accepted for
  the clip accounts; if a platform flags one, stop using that network and
  say so in the run notes.
- Never edit a clip to change what someone said or meant; keep enough
  context that the point stands on its own. No AI-altered footage of real
  people, ever (`content-rules`).
- Nonpartisan (`brand-voice`): over a month, balance who is shown, and
  frame each clip around an idea, not a side.
- Clips post **only to the clip accounts**, through Clip Studio
  (`routines/clip-studio.md`, `studio/buffer_clips.py`), automatically
  when "Autopost — Clips" is on; drafts when they touch elections,
  candidates or voting, are under 24 hours old, or can't be sourced
  (owner, 2026-10-13). The clipping work drops finished clips in the
  `civic-clips` bucket under `queue/<clip-id>/`; it never posts to Buffer
  itself.

## Robot's long-form series (two episodes a week, owner 2026-10-15)
Each episode is ONE specific, dramatic real event with a hook title. Mix the
lanes so no two in a row share one: survival guide, history, current events,
cybersecurity, and "strange but true" (declassified oddities, told curious
and dry: what the document says vs what the internet says; never credulous,
never accusing real people of things the record doesn't show). Off the
table: MKUltra ("too mainstream", owner 2026-10-15). Each is a page in
Notion → Scripts; Ep. 1 is a full script, the rest are "(brief)".

1. How Civilization Ends in 72 Hours (survival; pilot)
2. One Leaked Password Emptied the East Coast's Gas Stations (cyber)
3. Every Empire Thought It Was Different. Here's How They All Fell. (history)
4. A 17-Year-Old Hijacked Obama's Twitter With One Phone Call (cyber)
5. One Stuck Ship Held 12% of the World Hostage (current events, supply chains)
6. The Army's Declassified Guide to Leaving Your Body (strange but true: the Gateway Process and the Monroe Institute)
7. She Fell 2 Miles From the Sky and Walked Out of the Amazon (survival guide)
8. One Update Turned the World's Screens Blue (cyber, CrowdStrike 2024)
9. Someone Keeps Cutting the Internet's Cables (current events)
10. Your Weather App Knows Where You Sleep (privacy)

**Writing next week's script** (YT Video Studio step 5): take the lowest-
numbered "(brief)" page, verify every fact against its sources (drop or
soften anything you can't confirm), and add a `## Spoken script` section in
Robot's voice: ~1,400–1,600 words (~10 min), a cold-open hook from a real
moment, chapters, one practical takeaway, and the CTA. Add a `## Storyboard`
and a `## Sources` section, remove "(brief)" from the title, and set it to
Ready to Record. Match Ep. 1's structure and tone, plus the campaign's
tone rules (dry, sharp, never at victims). After Ep. 8, propose the next
four in the Strategy Memo for the owner to pick (one specific real event
each); don't start
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

## The Sovereign podcast
Live on Spotify and Apple Podcasts (owner, 2026-10-14). "The Sovereign, Out
Loud" audiograms and the "Also a podcast" caption line are on (campaign →
podcast section). Feed:
`https://skakrtljfaeopfqigyww.supabase.co/storage/v1/object/public/studio-videos/podcast/sovereign/feed.xml`.

## Open items (ask the owner; don't guess)
- **PoolParty and money.** The app's real screens show dollar stakes ("$…
  total staked", "Mark as Paid", "% paid on time"). The campaign's line "No
  real money. Just bragging rights." would be false. Decide the true
  message before any PoolParty ad runs.
- PoolParty App Store link (at launch).

