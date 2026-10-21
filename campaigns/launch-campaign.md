# Story campaign: The Sovereign + The Global Aggregate (owner, 2026-10-13)

Replaces the launch campaign. The owner's verdict on the first ads:
slideshows of images with quotes are "wildly ineffective". **Every ad is now
a short narrated story in real video**, not ad copy.

**Provocative first (owner, 2026-10-13, all products).** "A speeding ticket
feels bland." Lead with the most charged, talk-about-it story we honestly
have: scandals, outrage, power, money, sex and status, things people argue
about in the comments. Pick each week's stories in this order: (1) the
issue or cluster people are angriest or most divided about right now, (2) a
claim from our own writing that half the audience will push back on, (3)
only then the evergreen explainers. Provocative never means made up: the
facts stay real and sourced, allegations are said as allegations
("accused", "reports say"), and only the most sensitive posts (CLAUDE.md
rule 1: alleged crimes or sexual violence, victims, private people,
elections, unsourced claims) wait as drafts for the owner's OK.

Where it posts: the **promo + media accounts only** (Buffer organization
"My organization" `6ab6c71cddecb7a5c80b918f`; channels Instagram @wadecapitallc
`6ab6cac8ea19ca0bdeea0fba`, TikTok @wadethesovereign `6ab6caf4ea19ca0bdeea114e`,
YouTube @WadeCapital `6ab6d22fea19ca0bdeea4810`). Never a clip account, never
another Buffer organization. Clips have their own accounts (`content-mix`).

Five ads a week (Mon–Fri), alternating brands, each on Instagram + TikTok,
plus YouTube Shorts when the Buffer limit allows. Social Studio schedules one
week at a time.

## What every ad is

A **20–30 second** story with a narrator (35 s at most; owner, 2026-10-18:
first week's reels ran ~35 s and stalled at about 100 views, the platforms'
cold-start floor, so they need to be watched to the end more often), in this
shape:

1. **Hook (0–2 s):** the most charged real detail, said out loud and shown
   on screen. "Seven Cornell students accused of rape. A university accused
   of looking away." Never a brand name or "Check out…" first.
2. **Setup:** who/what/where in one or two lines.
3. **Turn:** the surprise, the contradiction, the question. "By the letter of
   the law, guilty. The judge dismissed it anyway."
4. **Payoff:** the idea, in one sentence a viewer could repeat to a friend,
   plus ONE verbatim line from the product (excerpt or real headline) on
   screen.
   Then Robot **asks one either/or question out loud** ("Which headline
   would you have believed?"), the same one that ends the caption. A
   question people can answer in one word gets comments; comments feed
   "Robot Reads the Comments".
5. **CTA (last 4 s, owner 2026-10-14: "read more, link in bio" is too weak):**
   show the product itself and say what's free and specific.
   - The Global Aggregate: end on the GA end card (`studio/brand/ga-endcard.png`,
     made from the site's own share card, as an `"image"` scene) with the
     voice line "All <N> headlines, side by side, free at globalaggregate dot
     org. Link in bio." (N = the story's real outlet count). Never claim a
     country count (owner, 2026-10-06); the end card has none.
   - The Sovereign: the logo card with the issue title, and "Read
     '<title>' free in The Sovereign. Link in bio."
   - PoolParty: the real app screen that settles the bet.

**Production (real video, free first):**
- **Voice:** Robot's voice (`studio/ai_voice.py`, Chatterbox clone), script
  80–120 words.
- **Picture: the story fills the screen, not Robot** (owner, 2026-10-13:
  "the robot … should not be the focus of the ad"). `studio/story_reel.py`
  puts the scenes and cards full-frame and Robot in a small corner bubble as
  the narrator. Cuts every 2–4 s; captions always on. Big numbers with their
  source.
- **Footage, free first (owner, 2026-10-14: AI scenes add up).** In order:
  1. the product's own material: verbatim excerpt cards, real headline cards
     from The Global Aggregate's database, real app screens (PoolParty);
  2. real footage from `studio/find_footage.py`: government briefings,
     press conferences, hearings and archive film (archive, NASA, Commons).
     **The Global Aggregate and The Sovereign lean on this:** the real
     moment beats a recreation. Use the government's own recording, never a
     TV network's broadcast, on these accounts. Credit it on screen (the
     `credit` field in the story_reel spec). Never cut it to change meaning.
     A sourced post showing a real politician schedules normally;
  3. free stock scenes from Pixabay (`--source pixabay`) for generic places
     and moments ("a campus at night", "a phone feed at 2 a.m.");
  4. only then Higgsfield (Hailuo text-to-video, $0.28 per shot): PoolParty's
     labeled AI actors, or a Sovereign scene nothing above covers. Generic
     people only, never a real person's likeness or a real school's logo.
- No slideshows of still images, no stock filler, no text-only reels.

**Story series** (people follow series; use the series name on screen and as
a hashtag):

| Series | Brand | The story |
|---|---|---|
| **The Sovereign Says** | The Sovereign | The issue's most provocative real story or claim (Cornell and the "manosphere"; "kings, dictators and pundits" as our new gods; "our first real addiction was the video game") → why it's happening, through one big idea → one verbatim excerpt → read it |
| **Philosophy in 30 Seconds** (#PhilosophyIn30) | The Sovereign | A charged dilemma from an issue (fraternity violence and who's responsible; "the power goes out forever: Hobbes or Locke?"; the speed-trap ticket only as a filler) → the idea → one excerpt → read the issue |
| **One Story, Five Countries** (#OneStoryFiveCountries) | The Global Aggregate | The most contested real cluster in the database (war, scandal, a country blamed by its neighbours): the same event, headlines that flatly disagree → "wait, which is true?" → how many outlets covered it → compare them yourself |
| **Headline Duel** | The Global Aggregate | Two real headlines about one event side by side → Robot reads both → what each leaves out → the site shows all of them |
| **Friendly Wagers** | PoolParty (after launch) | A heated, funny real-life argument (the group-chat bet that got out of hand, the friend who never pays up) acted by labeled AI actors → the real app screen that settles it. Waits for the owner's money message and App Store link |

**Sourcing truth:** every fact, quote and headline is real and word for
word, from the issue or the database. Anecdotes come only from the issues
themselves, told as the writer's story ("one Sovereign writer…"). Global
Aggregate stories follow rule 1: war and breaking clusters schedule
normally when sourced; election clusters and alleged crimes against
identifiable people are drafts. Don't steer away from them: a draft the
owner approves beats a bland post that auto-publishes. Make at least two of the
five ads from the week's most charged material.

Sovereign issue notes, most provocative first. **Lead story: 8 Strain
Theory and the "Manosphere"** (Cornell students accused of rape, the
manosphere, 15% of young men with no close friends; a sample was made
2026-10-13). Draft (rule 1: it centers a real victim and an allegation), never
name the students or the victim. Then 9 Men and Gods ("kings, dictators and
pundits"; auto-post if no living person is attacked), 4 Penn State
Fraternities (brawls, hazing, a cocaine bust; about the system, not named
students), 5 Video Games, 2 House votes to end Iran war, 7 The
Plagiarism Wars (draft only if it accuses a private person), 6 Hobbes and Locke, 3 Legal Positivism (filler
only), 1 Welcome.

## The podcast in promotion (owner, 2026-10-14)

The Sovereign podcast (`studio/podcast.py`, voice Onyx) is promoted three ways,
all free:
1. **The Sovereign, Out Loud** (#TheSovereignPodcast): a ~30 s audiogram
   (`studio/audiogram.py`) of the new episode's 4–6 strongest lines, word
   for word, over a moving sound wave with big captions, ending on "Listen
   free on Spotify & Apple Podcasts · link in bio". It takes Thursday's
   Sovereign slot in a week with a new episode (the Buffer limit is 10
   posts, and the five ads already use them). Pick the most provocative
   lines, as with every ad. Same rule-1 draft rules as the issue itself.
2. **Every Sovereign post's caption** adds one line: "🎧 Also a podcast:
   search The Sovereign on Spotify or Apple Podcasts."
3. **YouTube:** the owner adds the podcast feed to YouTube Studio once, and
   YouTube posts each episode on @WadeCapital by itself (no upload work).

The podcast is live on Spotify and Apple (owner, 2026-10-14), so all three are on.

## Tone (owner, 2026-10-15)
- **Write in the owner's voice** (`brand-voice` → "The owner's voice"):
  thoughtful about the human condition, with a dose of humor; a small
  scene, the big idea in plain words, one dry line, a sincere landing.
- **Not every post is an ad.** Most are informative pieces worth watching
  on their own that reference the product they came from in one natural
  line plus the closing CTA (owner, 2026-10-15).
- **Sharpness depends on the story:** properly dry and cutting about
  headlines, media, power and politics; gentle around tragedies. The joke
  is always on the coverage or the system, never on victims; a story with
  deaths gets at most one dry line about how it was covered.
- **Robot's war-veteran backstory** is seasoning, not the meal: at most one
  aside in about one ad in five ("I've survived a war. The comments section
  is harder."). The product and the story stay the focus.
- **Backstory openers and young people's world** (the group chat, the For
  You page, class, the uncle forwarding headlines) beat abstract hooks.
- **Recurring bits:** "Robot Reads the Comments" starts once our posts get
  real comments (answer real pushback, quote it word for word, no usernames
  unless public figures). More bits only once the owner picks them.

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
| Tue | The Sovereign | The Sovereign Says |
| Wed | The Global Aggregate | Headline Duel |
| Thu | The Sovereign | Philosophy in 30 Seconds, or **The Sovereign, Out Loud** when a new episode came out that week |
| Fri | Alternate | Whichever series performed best last week |

**What week 1 showed (Oct 14–18, Buffer numbers):** the Global Aggregate
"two headlines" stories did best (Houthi: 122 Instagram views; diesel: 87
Shorts, 94 TikTok). Sovereign posts that opened on an abstract question did
worst ("Who do you worship?": 19 Instagram, 0 Shorts). TikTok gives every
post ~100 views; nothing has broken out yet and no post has a comment. So:
- **Sovereign posts open on a concrete, current scene or headline**, then
  the issue's idea (the owner's voice: small scene first). Never open on an
  abstract question.
- Friday goes to the best series by **views per platform from last week**
  (Social Studio step 0), not by guess.

**Week 2 (Oct 19–21): the first breakout.** "The House voted to end the war
in Iran. It probably changes nothing" got **875 views and 9 likes on YouTube
Shorts** (the same video: 88 on TikTok, 10 on Instagram). YouTube Shorts is
now our best platform (about 95 views a post vs 37 on Instagram), and the
first real comment arrived there. So:
- **New default shape, "What it actually changes":** a big political or
  world headline from the last 48 hours, then the plain-words answer to
  "does this change anything?" (the vote, the rule, the deal), sourced. Use
  it for at least two of the five ads a week (Global Aggregate or
  Sovereign, whichever has the story).
- Reels still ran 30–34 s after the 20–30 s rule: Social Studio now checks
  the length before scheduling.
- Instagram is weakest: keep posting there (it's where the bio link and the
  Linktree are), but judge ideas by YouTube Shorts and TikTok numbers.

Robot's Short (cut from the YouTube episode) posts Sunday on top of these.
Timing (Eastern): TikTok 7–9 PM, Instagram 11 AM–1 PM or 7–9 PM, Shorts
2–4 PM.

## Rules that still apply
- Rule 1 means **draft, not skip**, for the most sensitive posts only:
  make it and save it as a Buffer draft with a one-line reason and its
  planned time.
- **Exact times, never Buffer's queue** (owner, 2026-10-14: approved drafts
  all landed on one day). One ad per day, each at the timing above
  (Instagram 12 PM, Shorts 3 PM, TikTok 7:30 PM Eastern), set with
  `customScheduled` + `dueAt`.
- Ownership disclosure when a Sovereign-branded post promotes The Global
  Aggregate (`monetization`).
- Higgsfield spend cap: $2/week (owner, 2026-10-14). Log every generation.
- Buffer free plan: 10 scheduled posts per organization at once.

**Learn and adjust (Strategist, weekly):** from Buffer metrics, the top 2
posts by reach and by comments, their series and hook, and lean next week
that way. Retire series and hashtags that never show up on top posts.
