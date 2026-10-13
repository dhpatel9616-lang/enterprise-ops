# Story campaign: The Sovereign + The Global Aggregate (owner, 2026-10-13)

Replaces the launch campaign. The owner's verdict on the first ads:
slideshows of images with quotes are "wildly ineffective". **Every ad is now
a short narrated story in real video**, not ad copy.

Where it posts: the **promo + media accounts only** (Buffer organization
"My organization" `6ab6c71cddecb7a5c80b918f`; channels Instagram @wadecapitallc
`6ab6cac8ea19ca0bdeea0fba`, TikTok @wadethesovereign `6ab6caf4ea19ca0bdeea114e`,
YouTube @WadeCapital `6ab6d22fea19ca0bdeea4810`). Never a clip account, never
another Buffer organization. Clips have their own accounts (`content-mix`).

Five ads a week (Mon–Fri), alternating brands, each on Instagram + TikTok,
plus YouTube Shorts when the Buffer limit allows. Social Studio schedules one
week at a time.

## What every ad is

A 25–45 second **story with a narrator**, in this shape:

1. **Hook (0–2 s):** a real, concrete moment or conflict, said out loud and
   shown on screen. "A Virginia speed trap. Up to $2,500 and jail time."
   Never a brand name or "Check out…" first.
2. **Setup:** who/what/where in one or two lines.
3. **Turn:** the surprise, the contradiction, the question. "By the letter of
   the law, guilty. The judge dismissed it anyway."
4. **Payoff:** the idea, in one sentence a viewer could repeat to a friend,
   plus ONE verbatim line from the product (excerpt or real headline) on
   screen.
5. **CTA (last 3 s):** the product name, what you get, and where: "Read
   'Legal Positivism' in The Sovereign. Link in bio."

**Production (real video, free first):**
- **Voice:** Robot's voice (`studio/ai_voice.py`, Chatterbox clone), script
  80–120 words.
- **Picture:** Robot on screen talking (`studio/render_puppet.py`, tall
  layout, burned-in captions), cut together with the real material:
  excerpt cards (`studio/excerpt_reel.py` look), real headline cards from The
  Global Aggregate's database, real app screens (PoolParty). Add 1–2 short
  AI video shots (Higgsfield image-to-video, cheapest model, ≤ $1 per ad)
  only where a scene needs a place or action ("a highway at night", "a
  courtroom"). Cuts every 2–4 s; captions always on.
- No slideshows of still images, no stock filler, no text-only reels.

**Story series** (people follow series; use the series name on screen and as
a hashtag):

| Series | Brand | The story |
|---|---|---|
| **Philosophy in 30 Seconds** (#PhilosophyIn30) | The Sovereign | A real anecdote or thought experiment from an issue (the speed-trap ticket; "the power goes out forever: Hobbes or Locke?") → the idea → one excerpt → read the issue |
| **The Sovereign Says** | The Sovereign | One provocative claim from an issue ("For many of us, our first real addiction was the video game") → Robot plays devil's advocate in two lines → excerpt → read it |
| **One Story, Five Countries** (#OneStoryFiveCountries) | The Global Aggregate | A real cluster from today's database: the same event, headlines that disagree → "wait, which is true?" → how many outlets covered it → compare them yourself |
| **Headline Duel** | The Global Aggregate | Two real headlines about one event side by side → Robot reads both → what each leaves out → the site shows all of them |
| **Friendly Wagers** | PoolParty (after launch) | Labeled AI actors in a quick scene settling a bet → the real app screen that settles it. Waits for the owner's money message and App Store link |

**Sourcing truth:** every fact, quote and headline is real and word for
word, from the issue or the database. Anecdotes come only from the issues
themselves, told as the writer's story ("one Sovereign writer…"). Global
Aggregate stories follow rule 1: war, crime, election and breaking clusters
are made but saved as drafts. Prefer science, economy, sport, culture,
space, health and business.

Sovereign issue notes: ready for automatic posting: 1 Welcome, 3 Legal
Positivism (the speed-trap ticket), 5 Video Games, 6 Hobbes and Locke, 4
Penn State Fraternities (about the system, not named students). Drafts
(rule 1): 2 House votes to end Iran war, 7 The Plagiarism Wars, 8 Strain
Theory and the "Manosphere".

## Captions (every post)

1. **Hook line** = the story's first beat, keyword first ("Legal positivism
   explained with a speeding ticket 🚔"). Same phrase on screen in the first 2 s.
2. **One or two story sentences** with the specific detail (names, numbers).
3. **The product link, always the right one:**
   The Sovereign → `sovereignnewsletter.substack.com`;
   The Global Aggregate → `globalaggregate.org`;
   PoolParty → its App Store link (after launch).
   Write the plain address plus "link in bio" (Instagram and TikTok captions
   aren't clickable; the bio's Linktree is).
4. **A question** that invites a take.
5. **8–12 hashtags:** brand + series + 3–4 niche + 2–3 topic + 1–2
   community tags (#philosophytok, #historytok, #lawtok, #newstok). Rotate;
   no #fyp/#viral.
6. **No "(AI-generated)" or "(Imagery is AI…)" text in captions** (owner,
   2026-10-13: the platforms add their own label and the caption note looks
   ungenuine). When a post contains realistic AI imagery, set the platform's
   AI flag instead (`isAiGenerated` in Buffer metadata; TikTok/YouTube the
   same). Robot is a cartoon and needs no flag.
7. **TikTok title / YouTube Shorts title:** the hook, under 60 characters.

**Keyword and hashtag bank** (add story-specific tags):

| Brand | Search phrases | Hashtags |
|---|---|---|
| The Sovereign | philosophy explained, legal philosophy, political philosophy, critical thinking, civics for beginners, history of ideas | #TheSovereign #PhilosophyIn30 #philosophy #philosophytok #politicalphilosophy #criticalthinking #civics #lawtok #prelaw #history #substack #newsletter |
| The Global Aggregate | world news explained, how countries report the news, media bias, news literacy, compare headlines | #TheGlobalAggregate #OneStoryFiveCountries #worldnews #newstok #medialiteracy #mediabias #newsliteracy #geopolitics #internationalrelations #journalism #students |
| Robot | survival tips for beginners, cybersecurity for beginners, history explained | #RobotExplains #survival #preparedness #cybersecurity #historytok #learnontiktok |

## Weekly rhythm

| Day | Brand | Default series |
|---|---|---|
| Mon | The Global Aggregate | One Story, Five Countries |
| Tue | The Sovereign | Philosophy in 30 Seconds |
| Wed | The Global Aggregate | Headline Duel |
| Thu | The Sovereign | The Sovereign Says |
| Fri | Alternate | Whichever series performed best last week |

Robot's Short (cut from the YouTube episode) posts Sunday on top of these.
Timing (Eastern): TikTok 7–9 PM, Instagram 11 AM–1 PM or 7–9 PM, Shorts
2–4 PM.

## Rules that still apply
- Rule 1 means **draft, not skip**: make it and save it as a Buffer draft
  with a one-line reason.
- Ownership disclosure when a Sovereign-branded post promotes The Global
  Aggregate (`monetization`).
- Higgsfield spend cap: $5/week. Log every generation.
- Buffer free plan: 10 scheduled posts per organization at once.

**Learn and adjust (Strategist, weekly):** from Buffer metrics, the top 2
posts by reach and by comments, their series and hook, and lean next week
that way. Retire series and hashtags that never show up on top posts.
