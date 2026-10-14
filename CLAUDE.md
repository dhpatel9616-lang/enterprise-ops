# enterprise-ops: operating rules

This repo is the control room for the owner's autonomous content studio and
night-shift routines. Claude drafts, builds, and publishes automatically behind
kill switches the owner controls in Notion.

Wade Capital is the umbrella. Under it: The Sovereign (media), PoolParty
(app), The Global Aggregate (news platform), and Wade Capital's services.
See the `brand-voice` skill.

## Who does what

- **Claude:** writes scripts, storyboards, captions, outreach, code, and
  videos, and publishes them automatically where rule 1 allows. Opens pull
  requests (PRs).
- **Owner:** merges every PR and controls the kill switches in Notion →
  Automation Control. The owner has no programming experience: anything they
  must do gets explained click by click, in plain words, with no jargon.

## Hard rules (never break these)

1. **Automatic publishing, behind kill switches** (owner's permission,
   2026-09-30). Notion → Automation Control:
   - **"Autopost — Social (IG / TikTok / Shorts)" Enabled:** schedule posts
     in Buffer with automatic publishing. Disabled: Buffer drafts only.
   - **"Autopost — YouTube long-form" Enabled:** upload with
     `studio/youtube_upload.py`. Disabled: leave the video in Drive
     "Ready to Publish".
   - Even when enabled, save as a **draft** only the most sensitive posts
     (owner, 2026-10-14: "only the most provocative posts go to drafts"):
     one that alleges a crime or sexual violence against identifiable
     people or centers a victim, centers a private person, touches
     elections/candidates/voting, makes a claim you can't source, or fails
     `content-rules`. Sourced news that names politicians or public figures,
     war, and breaking news (with a source) schedule normally. Every draft
     gets a reason in the run notes, an email to the owner, and its planned
     time, and every scheduled post an exact time (never Buffer's queue).
   - **"Autopost — Clips" Enabled:** Clip Studio posts clips to the clip
     accounts only, through `studio/buffer_clips.py` (their own Buffer
     account), as drafts when they touch elections/candidates/voting, are
     under 24 hours old, can't be sourced, or use a TV-network news excerpt
     (owner, 2026-10-13 / 10-14).
   - Outreach emails send automatically within the sequencer's daily caps
     (Enterprise-leads repo).
   - **"Autopublish — Website guides (Wade Capital)" Enabled:** the SEO Writer
     routine commits one how-to guide a week straight to the
     wade-capital-website `main` branch (the only automatic push to `main`;
     owner, 2026-10-06). Disabled: it opens a PR instead.
2. **Never touch PoolParty production:** Supabase project
   `tzebfwmrmzhkeoptwkzy`. No reads, no writes, no migrations, no branches, no
   edge functions. If a task seems to need it, stop and ask.
3. **Never merge your own PR.** Work on a `claude/` branch and open a PR.
4. **Never assume brand identity.** Voice, colors, names, taglines, and claims
   come from the `brand-voice` skill. If a section is empty or unclear, ask the
   owner; do not invent it.
5. **Every piece of content names its revenue path and CTA** (see the
   `monetization` skill).
6. **Follow `content-rules`:** AI characters are actors, never fake customers
   or testimonials; label realistic AI content; no real people's likenesses.
7. **Say "for beginners", never "for kids".** Our audience is young,
   digitally literate people (roughly 14-30) who are new to a topic.
8. **Secrets stay secret.** Read credentials (for example `HF_KEY`) from
   environment variables. Never print, log, or commit them.
9. **Notion: query databases only with view mode or fetch, never SQL mode**
   (the workspace SQL quota is exhausted).
10. **Build standards:** follow the `build-standards` skill for any Supabase,
   cron, or migration work.
11. **The mailing address is private.** It lives only in the Supabase
   `settings` row `business_mailing_address` and appears only in outgoing
   Wade Capital service emails to businesses. Never hard-code it or put it in
   this repo (it's public), Notion content, posts, videos, or any other message.
12. **Never create pages at the top level of the Command Center.** Strategy
   Memos go in the **Weekly Log** database; if it can't be read, log the
   problem in **Automation Control** instead.

## Allowed systems

| System | Use |
|---|---|
| Notion, "The Enterprise — Command Center" | Content Ideas, Scripts, Build Queue, Raw Leads Inbox (+ "Outreach Approvals" view) |
| Google Drive, "Voiceovers" folder | Owner's recorded voiceovers |
| Buffer | Promo/media posts via the Buffer connector; clip posts only via `studio/buffer_clips.py` (separate Buffer account, `BUFFER_CLIPS_API_KEY`) |
| Supabase `skakrtljfaeopfqigyww` | Enterprise Leads data (outreach); public `studio-videos` bucket for rendered videos |
| GitHub `enterprise-leads` repo | Outreach sequencer (changes go through PRs) |
| GitHub `wade-capital-website` repo | Wade Capital site (Netlify); weekly guides per rule 1, everything else through PRs |
| Free footage: Internet Archive, NASA, Wikimedia Commons, Pixabay (`PIXABAY_API_KEY`) | Scenes and real footage for ads and clips, searched first (`studio/find_footage.py`); nothing stored |
| Higgsfield API (`HF_KEY`) | Paid generation, last resort, cheapest model that meets the brief |
| Chatterbox (free, open source) | Robot's cloned voice (`studio/ai_voice.py`; reference clip in the private Supabase bucket `voice-samples`) |
| Kokoro (free, open source) | The Sovereign podcast's male AI voice (`studio/podcast.py`, own feed in the `studio-videos` bucket) |

## What we make (`content-mix` skill)

- **Short-form promos** (9:16) for The Sovereign, The Global Aggregate, and
  PoolParty, built from real material from each product. Realistic AI
  people and situations appear only in promos. Stand-alone political and
  historical clips go only to the clip accounts (Clip Studio, rule 1); real
  footage (government briefings, archive film) may appear inside a Global
  Aggregate or Sovereign story ad (owner, 2026-10-14).
- **Long-form** (16:9): Robot tutorials (cartoon) on grid-down survival,
  cybersecurity, history, and politics; and clipping montages.
- **Two sets of social accounts (owner, 2026-10-12):** promo + media
  (IG @wadecapitallc, TikTok @wadethesovereign, YouTube @WadeCapital) for
  Robot's long-form, promos and ad campaigns; clips (IG @wadecapitalclips,
  TikTok @wade.clips3, YouTube @WadeCapitalClips, own Buffer account) for
  clips and clip montages only. Never mix them (`content-mix`).
- Wade Capital services are sold by phone and email outreach only, never on
  social.

## Night-shift loop

1. Read new rows in **Content Ideas** and **Build Queue**.
2. For each idea: write a script and storyboard into **Scripts** (status
   *Ready to Record*) using `voiceover-workflow`, `platform-formats`,
   `brand-voice`, `monetization`, and `content-rules`.
3. For each *Recorded* script: assemble the video with `video-assembly` and
   publish per rule 1.
4. For each Build Queue item: build on a `claude/` branch, open a PR, paste the
   PR link into the item, and set it to *PR Open*.
5. Leave a short plain-language summary of what's waiting for the owner.

## Coding style

@.claude/rules/ponytail.md

(Ponytail by Dietrich Gebert, MIT license, see `.claude/rules/PONYTAIL-LICENSE`.
Its skills live in `.claude/skills/ponytail*`.)
