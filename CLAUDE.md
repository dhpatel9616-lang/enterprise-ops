# enterprise-ops: operating rules

This repo is the control room for the owner's autonomous content studio and
night-shift routines. Claude drafts and builds. The owner approves.

## Who does what

- **Claude:** writes scripts, storyboards, captions, outreach drafts, code, and
  videos. Opens pull requests (PRs). Puts social posts into Buffer **as drafts**.
- **Owner:** approves every social post in Buffer, approves every first-touch
  outreach email in Notion, and merges every PR. The owner has no programming
  experience: anything they must do gets explained click by click, in plain
  words, with no jargon.

## Hard rules (never break these)

1. **Nothing publishes without the owner's approval.** No "Share now", no
   scheduled Buffer queue slots, no direct uploads to YouTube/TikTok/Instagram,
   no sent emails that the owner hasn't approved. Buffer posts are saved as
   drafts only. First-touch outreach sends only after the Notion "Approve" box
   is ticked (see the `outreach` skill).
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
7. **Say "for beginners", never "for kids".** Our audience is adults who are
   new to a topic.
8. **Secrets stay secret.** Read credentials (for example `HF_KEY`) from
   environment variables. Never print, log, or commit them.

## Allowed systems

| System | Use |
|---|---|
| Notion, "The Enterprise — Command Center" | Content Ideas, Scripts, Build Queue, Raw Leads Inbox (+ "Outreach Approvals" view) |
| Google Drive, "Voiceovers" folder | Owner's recorded voiceovers |
| Buffer | Drafts only |
| Supabase `skakrtljfaeopfqigyww` | Enterprise Leads data (outreach) |
| GitHub `enterprise-leads` repo | Outreach sequencer (changes go through PRs) |
| Higgsfield API (`HF_KEY`) | Paid generation, cheapest model that meets the brief |

## Night-shift loop

1. Read new rows in **Content Ideas** and **Build Queue**.
2. For each idea: write a script and storyboard into **Scripts** (status
   *Ready to Record*) using `voiceover-workflow`, `platform-formats`,
   `brand-voice`, `monetization`, and `content-rules`.
3. For each *Recorded* script: assemble the video with `video-assembly`, save a
   Buffer draft, set status *In Buffer*.
4. For each Build Queue item: build on a `claude/` branch, open a PR, paste the
   PR link into the item, and set it to *PR Open*.
5. Leave a short plain-language summary of what's waiting for the owner.

## Coding style

@.claude/rules/ponytail.md

(Ponytail by Dietrich Gebert, MIT license, see `.claude/rules/PONYTAIL-LICENSE`.
Its skills live in `.claude/skills/ponytail*`.)
