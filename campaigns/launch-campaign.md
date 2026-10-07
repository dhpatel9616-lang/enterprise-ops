# Launch ad campaign: The Sovereign + The Global Aggregate (owner, 2026-10-06)

Goal: build an audience from zero. No posts exist yet, so everything in the
back catalogue is new to viewers. Five posts a week (Mon–Fri), alternating
brands, each on Instagram Reels, TikTok and YouTube Shorts. Social Studio
schedules one week at a time.

Every ad still meets the content-mix quality bar: a real hook in 2 seconds,
real material on screen, motion, one takeaway, one CTA.

## The Sovereign (CTA: "Read The Sovereign" → sovereignnewsletter.substack.com)

**Format (owner, 2026-10-06): every Sovereign ad is one of two things, never
AI stock scenes with quotes:**
- **(b) Excerpt reel (default):** `studio/excerpt_reel.py`. The newsletter's
  own look (navy, logo, EB Garamond, like Substack's share cards): a 2-second
  hook in big caps (the search phrase, a question), ONE verbatim excerpt
  revealed word by word, then the issue title, subtitle and "Read the full
  issue". Pick the punchiest sentence in the issue, not the first one.
- **(a) A character speaking the words** (Robot or a labeled promo-cast actor
  with the cloned/free voice) once the voice pipeline is set up.

**Captions are never bland:** a hook line people would stop for (an emoji is
fine), one or two vivid specific sentences from the issue (names, numbers,
the real example), the CTA, a question that invites a take, and 5–6 hashtags:
brand + topic tags + one community tag (#philosophytok, #gamertok,
#lawstudent). TikTok title = the hook. No "(AI-generated)" label unless AI
imagery is actually in it.

Rotate these ad types; never repeat the same issue two weeks running.

| Ad type | What it is | Material |
|---|---|---|
| **Issue spotlight** | Hook quote → 2–3 verbatim pull quotes → one-line argument → "Read the full piece" | Any published issue, oldest unpromoted first after the newest |
| **Big idea in 30 seconds** | Explains the issue's central idea for beginners (e.g. Hobbes vs. Locke on the "state of nature", legal positivism) | Issue text; AI-labeled promo-cast scenes |
| **The question** | Opens on a provocative question the issue answers ("Are video games the American boy's first addiction?"), then one quote | Issue subtitle and text |
| **Manifesto** | What The Sovereign is: "Thought, critique, and community, with a dose of good-natured humor." Quotes from Issue 1 (Welcome) | Issue 1, Substack description |

Issue notes (as of 2026-10-06):
- Ready for automatic posting: 1 Welcome, 3 Legal Positivism, 5 Video Games,
  6 Hobbes and Locke, 4 Penn State Fraternities (about the system, not
  named students; check before posting).
- Make, but save as Buffer drafts (rule 1): 2 House votes to end Iran war
  (elections/politicians), 7 The Plagiarism Wars (names a public figure),
  8 Strain Theory and the "Manosphere" (rests on a real case).

## The Global Aggregate (CTA: "Use The Global Aggregate" → globalaggregate.org)

Generic brand ads don't depend on any one news story, so they can always post
automatically. **Every Global Aggregate ad needs real visuals under the
words**: 2–3 AI-labeled scenes (people reading news on phones, a newsroom,
a globe of headlines) or real headline cards from the database. A starfield
or plain background with text is a text reel, and text reels never ship. Story ads use a real cluster and follow rule 1 (draft when
required).

| Ad type | What it is | Material |
|---|---|---|
| **By the numbers** | "Today: N articles from 195 news feeds, side by side" (never "30 countries") | Live counts from the site's database (`articles`, distinct `source` / `country`, last 24 h) |
| **How it works** | Search one event → see every country's headline → spot the framing | Branded walkthrough cards of the real features: trending stories, world map, filter by country, saved filters |
| **Who it's for** | Students writing papers, debaters, anyone who wants to "check it yourself" | Brand cards + real counts |
| **Same story, different world** | 2–3 real headlines about one event from different countries | A real cluster from `trending_clusters`; prefer science, economy, sport, culture, space, health, business. War/crime/election/breaking clusters are still allowed but saved as drafts (rule 1) |

**Buffer's free plan holds 10 scheduled posts at once**, so 5 ads × Instagram
+ TikTok fills it; YouTube Shorts get Robot's Short only until the plan is
upgraded.

## Weekly rhythm

| Day | Brand | Default ad type |
|---|---|---|
| Mon | The Global Aggregate | By the numbers / How it works |
| Tue | The Sovereign | Issue spotlight |
| Wed | The Global Aggregate | Same story, different world (or Who it's for) |
| Thu | The Sovereign | Big idea in 30 seconds / The question |
| Fri | Alternate | Manifesto or How it works |

Robot's Short (from the YouTube episode) posts Sunday on top of these.

## Rules that still apply
- Quotes and headlines word for word; real counts only.
- AI-labeled when realistic AI people appear; ownership disclosure when a
  Sovereign-branded post promotes The Global Aggregate.
- Rule 1 means **draft, not skip**: if a post needs the owner's eye, make it
  and save it as a Buffer draft with a one-line reason.
- Higgsfield spend cap: $5/week.

## Reach: captions, keywords, hashtags (every post)

Search now drives discovery on all three apps: TikTok and Instagram read the
caption, the on-screen text and the spoken words; YouTube reads the title and
description. So every post says what it's about in plain search words.

**Every post has:**
1. **A keyword-first first line** (it's the hook *and* the search phrase):
   "Hobbes vs. Locke explained in 30 seconds", "How 30 countries reported the
   same story". The same phrase appears as on-screen text in the first 2 s.
2. **One or two sentences** of value, then the CTA.
3. **A question** to drive comments ("Which side are you on?", "Which
   headline surprised you?"), in the caption (Buffer's free plan can't post
   a first comment).
4. **Hashtags:** 3–5 per post (Instagram, TikTok), 3 in the YouTube Shorts
   description. One brand tag + two niche tags + one or two topic tags. Rotate;
   never paste the same block every time. Skip #fyp/#viral style tags (no
   signal).
5. **YouTube Shorts title:** under 60 characters, keyword first (the hook
   phrase), no hashtags in the title.
6. **Alt text** on any image post (accessibility, and it's indexed).

**Keyword and hashtag bank** (pick per post; add issue- or story-specific tags):

| Brand | Search phrases to use in captions/on-screen | Hashtags |
|---|---|---|
| The Sovereign | philosophy explained, political philosophy, critical thinking, civics for beginners, history of ideas, law and society, media criticism, education | brand: #TheSovereign · niche: #politicalphilosophy #criticalthinking #civics #historyofideas #prelaw #lawstudent · topic: #philosophy #politics #history #education #substack |
| The Global Aggregate | world news explained, how countries report the news, media bias, news literacy, compare headlines, international news | brand: #TheGlobalAggregate · niche: #medialiteracy #newsliteracy #mediabias #internationalrelations #geopolitics · topic: #worldnews #news #globalnews #journalism #students |
| Robot (Shorts) | survival tips for beginners, emergency preparedness, cybersecurity for beginners, history explained | brand: #RobotExplains · niche: #emergencypreparedness #cybersecuritytips #prepared #historyexplained · topic: #survival #cybersecurity #history |

**Timing (US Eastern), one post per brand per day max:** TikTok 7–9 PM,
Instagram 11 AM–1 PM or 7–9 PM, YouTube Shorts 2–4 PM. Spread the three
platforms across those windows rather than posting all at once.

**Learn and adjust (Strategist, weekly):** from Buffer metrics, name the top
2 posts by reach and by comments, which hook phrase and ad type they used, and
make next week lean that way. Retire hashtags that never appear on top posts.

## Profiles (one-time, owner)
Each profile's name and bio carry the main keyword, because profile text is
searchable too:
- Instagram @wadecapitallc and TikTok @wadethesovereign: name field
  "The Sovereign · World News & Ideas"; bio "Philosophy, politics & world news
  explained for beginners. Compare headlines from 195 news feeds ↓" with the link
  to globalaggregate.org or a link page listing the Substack and the site.
- YouTube channel description: first line "Robot explains survival,
  cybersecurity, history and politics for beginners."
