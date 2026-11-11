# Where everything stands (handoff, 2026-11-10)

Written at the end of a long working session so a fresh session starts with
full context. **Read this after CLAUDE.md, before doing anything.** Update it
(same file, same sections) at the end of any session that changes the picture.

## 1. Working with the owner
- No programming experience: every owner step is click by click, in plain
  words, with the exact place to click. Owner merges every PR and runs SQL.
- Prefers you act, then report. Be honest about numbers (they ask "how is X
  doing?" often). Don't re-ask decided questions (below). Use they/them.
- The owner is the writer of The Sovereign; never "a Sovereign writer says".
- Main goal right now (2026-11-10): **social engagement and promotion**
  (clicks, Sovereign readers, Global Aggregate traffic), then revenue from
  Wade Capital services via outreach. Revenue is still $0.

## 2. Decisions already made (don't relitigate)
- **Social voice:** Round 4 in `campaigns/launch-campaign.md`: funny,
  relatable to 18–25, never preachy ("sanctimonious" was the complaint), no
  realistic AI imagery on social, owner's voice (`brand-voice`), roast every
  side, never victims. Every ad: hook in 1.5 s → story → tie back to the
  product by name → humor; product link on screen + caption + "link in bio".
- Robot + AI voice stay for now; the owner will add a self-recorded podcast
  segment. Robot is a small corner bubble, never the focus.
- Drafts (not posts) only for the most sensitive items (CLAUDE.md rule 1).
  Exact times, never Buffer's queue. Higgsfield cap $2/run (Social only).
- Wade Capital services are never promoted on social; they're sold by email
  (and later calls). AI phone calls are paused.
- Outreach = personal notes, not mass email: only law firms (nationally) and
  medical offices (only when their website has a live-checked problem).
- PoolParty gets its own Instagram/TikTok and its own Buffer account
  (`BUFFER_POOLPARTY_API_KEY`), pre-launch posts link to the waitlist page.
  No money, no alcohol, no "gamble/casino/odds".
- Podcast guest outreach: the owner does it personally (the automatic guest
  emails exist but stay off: `outreach-v7` SQL is NOT run).
- Teacher/professor (not librarian) outreach for the Global Aggregate: on.
- Owner can deliver every law-firm service with Claude's help: after-hours
  intake line, website chat assistant, website design, AI use policy.

## 3. Systems map (where things live)
- **This repo (public):** routines (`routines/*.md`), studio scripts
  (`studio/`), campaign rules (`campaigns/`), skills (`.claude/skills/`).
  Routines are owner-created in claude.ai (created via http_api): Claude
  **cannot edit or fire them**; it changes behavior by editing the `.md`
  files they read. Schedules (cron, UTC unless noted):
  Strategist Mon 03:30 · Social Studio Mon 04:30 · Builder + Leads Wed 05:30
  (includes podcast-guest and GA-educator research) · YT Video Studio Tue+Fri
  04:30 (owner may add Mon) · Clip Studio daily 12:15 ET · SEO Writer Sun
  04:30 · Weekly To-Do Email Thu 07:52 ET (Claude can edit this one).
- **Environment "studio"** (all routines + this session): variables
  `BUFFER_CLIPS_API_KEY` (clip Buffer account, now correct), Supabase,
  YouTube (refresh token with full youtube scope: rename/update works),
  `HF_KEY`, `PIXABAY_API_KEY`. Network allowlist includes `archive.org`,
  `*.archive.org`, `*.edu`, NASA, Wikimedia, Pixabay, Supabase, Substack,
  `api.buffer.com`, `www.globalaggregate.org`.
- **Buffer, promo** (connector): org `6ab6c71cddecb7a5c80b918f`; IG
  @wadecapitallc `6ab6cac8ea19ca0bdeea0fba`, TikTok @wadethesovereign
  `6ab6caf4ea19ca0bdeea114e`, YouTube @WadeCapital `6ab6d22fea19ca0bdeea4810`.
- **Buffer, clips** (`studio/buffer_clips.py`, refuses promo channels): YouTube
  "Wade Capital Clips" + IG @wadecapitalclips. **TikTok @wade.clips3 not
  connected yet** (owner to do).
- **Supabase Enterprise `skakrtljfaeopfqigyww`:** `leads`, `settings`
  (outreach copy and switches live in `settings.outreach` and
  `settings.places_queries`), buckets `studio-videos` (public videos,
  podcast feed) and `civic-clips` (`posted/<date>-<slug>/clip.json` = clip
  records for the Sunday montage). **Writing settings from a session is
  blocked by the permission classifier: write SQL files and have the owner
  run them.** Read via REST with the service key is fine.
- **Enterprise-leads repo:** outreach sequencer, lead ingest (Google Places,
  950 searches/month free guard), email enrichment, reply checker, real
  estate lists. Settings SQL files in `enterprise-leads/supabase/`.
- **Notion (view/fetch only, never SQL):** Command Center; Automation Control
  (kill switches + Last Run Notes per routine); Scripts
  (`collection://894c2e0b-cac7-4d7b-8746-6a3d89f42b47`); Weekly Log
  (Strategy Memos); Podcast Guests (`collection://5c31eab0-40f8-4d8a-988b-b08c46fb8746`,
  db `11c77d7cb8ca4a37a6eebf7cd7e0d0ef`); GA Educators
  (`collection://d38e90fe-764c-4aac-aee0-7bc24d3430e7`, db
  `0bf67959e3454c5986037ef63d6b6dfb`). Never create top-level Command Center pages.
- **Global Aggregate:** code in private repo `globalaggregate` (Next.js +
  Supabase project `nikvqivovodrfybfjjka`). **Published by Rocket from
  Rocket's own copy: merging on GitHub does NOT change the live site, and
  there is no Vercel project of ours.** Changes go live only through a
  Rocket prompt.
- **Wade Capital site:** repo `wade-capital-website` (Netlify,
  wadecapital.netlify.app); forms via Web3Forms to the business Gmail.
  PoolParty waitlist: `/poolparty.html`.
- **Podcast:** The Sovereign, Kokoro voice "am_onyx", feed in
  `studio-videos/podcast/sovereign/feed.xml`, live on Spotify and Apple.
- **PoolParty production Supabase `tzebfwmrmzhkeoptwkzy`: never touch.**

## 4. Current state by area (numbers as of 2026-11-10)
- **Social (promo):** ~60–120 views a post, 0 comments in two weeks;
  average watch 2–7 s on ~30 s ads. Best ever: burnout quote audiogram 1,099
  Shorts views, Iran-vote Short 949, Xbox story 934. Round 4 formats started
  with the Nov 9 Social Studio run; a second daily 7–12 s POV meme (TikTok
  12:30 PM, Shorts 1:00 PM ET) starts with the Nov 16 run. Instagram had
  dropped off after Nov 2; rule now says post there daily.
- **YouTube @WadeCapital:** 4,470 views, 3 subscribers. Robot episodes 1–7
  out (Tue/Fri), ~0–1 views each; all renamed to search titles on Nov 5
  ("How to Survive a Power Outage: Your First 72 Hours (Robot, Ep. 1)" etc.).
  Ep. 8 CrowdStrike ready; Ep. 9 cables, 10 weather app, 11 Emu War, 12 casino
  fish tank, 13 Texas freeze (briefs in Notion). Thumbnails can't be set by
  the uploader (owner sets by hand if wanted). Owner should link each Short
  to its episode (Studio → Related video).
- **Clips:** fixed 2026-11-10 (wrong key, archive.org blocked, ffmpeg couldn't
  download, titles cut). First real clip (Duck and Cover 1951) scheduled
  Nov 10 6:15 PM ET on clip YouTube + IG; its record saved. Nov 11: Apollo 15
  hammer-and-feather drop (NASA 1971) scheduled 5:15 PM ET on YouTube + IG;
  `clip_reel.py` now outputs 30 fps (IG refused 15 fps film) and captions with
  whisper `small.en` (`base.en` misquoted the astronaut). Daily clips continue; Sunday long-form montage (`studio/clip_montage.py`) from Nov 15.
- **Outreach (Enterprise-leads):** ~680+ businesses emailed historically, 1
  real reply ever (Boal Mansion museum, Sep 29). Live settings (v10, run
  2026-11-05): first emails only to `legal` + `medical`, 15/day, law firms
  first; law-firm note = after-hours intake + website chat + website + AI
  policy (ABA Op. 512) + a checked website problem line; ingest searches
  only legal + medical, law firms in 42 US metros too. Educator lane (v9)
  live; Builder + Leads researches educators weekly (3 seeded: Elia Powers,
  Alison Burns, Justin Catanoso). No booking link exists: emails say "reply
  with a time and I'll send an invite" (owner declined to make one).
- **Global Aggregate:** zero traffic. Root causes found and fixed in GitHub
  (PR 8, merged) but NOT live: every `/story/*` page returns 500 (duplicate
  `[slug]` route), canonicals/sitemaps point at the non-www domain that
  redirects, homepage is client-rendered, sitemap had 5 URLs, news sitemap
  had escaped tags (Search Console: 112 errors). Fix = a Rocket prompt
  giving Rocket the exact changes from `globalaggregate` main (PR 8): delete
  `src/app/story/[slug]`; `story/[cluster_id]/page.tsx` (redirect old article
  ids, `notFound()` for expired); all URLs to `https://www.globalaggregate.org`;
  new `src/lib/clusters.ts`; `sitemap.ts`, `news-sitemap.xml/route.ts`,
  `page.tsx`, `NewsFeedClient.tsx` (storyLinks prop) copied verbatim; then
  have Rocket confirm a story page returns 200 and both sitemaps are valid.
  (PR 9 removed Vercel analytics; skip it.) The owner had this prompt as a
  file but is locked out of Rocket and emailed support; regenerate it from
  main when they're back in. GA PRD Phase C (country/topic pages, daily archive) is
  next once Rocket works. Bing Webmaster Tools set up.
- **Wade Capital site:** "30 countries" claim removed (PR 5). Owner setting
  up a free Google Business Profile (service-area business, address hidden).
- **PoolParty:** waitlist page live; hype posts wait on the owner creating
  accounts + Buffer + `BUFFER_POOLPARTY_API_KEY`. Handles not yet known.
- **Real estate (Baltimore):** 10,236 vacant properties + 1,079 cash buyers in
  Supabase; no free current foreclosure feed; Maryland foreclosure-purchase
  law (PHIFA) makes owner-occupied foreclosure outreach risky. Recommended
  instead: a free neighborhood vacancy report (Sandtown-Winchester) for
  associations, CDCs and affordable-housing groups. Owner hasn't picked yet.
- **Cold calls:** on hold (owner busy). Call lists exist in past runs only.

## 5. Open items for the owner
1. Connect TikTok @wade.clips3 in the clip Buffer account.
2. Rocket: regain access, then paste the SEO fix prompt; resubmit sitemaps.
3. Google Business Profile (free) for Wade Capital.
4. PoolParty accounts + Buffer key + handles.
5. Optional: YT Video Studio to Mon/Tue/Fri (owner edits routine schedule).
6. Daily 15 min: reply to comments and comment on bigger accounts' fresh
   posts from the brand accounts (the biggest engagement lever; status unknown).
7. Standing: Supabase Security Advisor check (Enterprise + GA projects);
   delete the empty `sovereign-cards` bucket.

## 6. Gotchas learned the hard way
- Check a PR's merged state before telling the owner it's live, and before
  resetting a branch (a PR merged minutes before its last commit once lost
  the law-firm code; it was restored in PR 16).
- `find_footage.py get` must download through urllib (proxy); ffmpeg can't
  reach the web in the sandbox. Clips use `--keep-audio`.
- Classifier blocks: writing Supabase settings, mass storage deletes, probing
  GA keys. Don't work around; hand the owner a SQL file.
- Websites outside the allowlist (e.g. practices' sites) can't be fetched from
  sessions; the outreach Action checks them live on GitHub instead.
- GitHub Actions schedules run hours late; don't read that as failure.
- The YouTube uploader can't set thumbnails; Buffer's long-form YouTube posts
  show the description first (that's where the UTM links are).
- Strategy Memo sometimes repeats stale items (e.g. the IG_USER_ID secret for
  workflows that are intentionally disabled); ignore those.
