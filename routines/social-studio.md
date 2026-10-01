# Social Studio prompt

```
UNATTENDED SCHEDULED RUN. No one is present: do not ask questions or wait for
input. Make reasonable decisions, record any assumption in the output, and if
truly blocked, log the blocker in this week's Strategy Memo and stop. The owner
has granted permission for automatic publishing behind the Notion kill
switches (CLAUDE.md rule 1).

0. SETUP FIRST: run `git clone --depth 1 https://github.com/dhpatel9616-lang/enterprise-ops ~/enterprise-ops`
   (public repo). The environment's Setup script installs the studio tools;
   check with `command -v ffmpeg rhubarb espeak-ng` and run
   `bash ~/enterprise-ops/studio/setup.sh` ONLY if one is missing. Read
   ~/enterprise-ops/CLAUDE.md and every ~/enterprise-ops/.claude/skills/*/SKILL.md,
   follow them, and run studio scripts from ~/enterprise-ops. If the clone fails
   or a tool is still missing, set the "Autopost — Social" row's Last Run Status to Error with
   the reason, and stop.
1. Read the "Autopost — Social" row in Notion Automation Control. If Enabled is
   checked, you will SCHEDULE posts; if unchecked, save them as Buffer drafts.
2. Produce this week's short-form promos exactly as the content-mix skill
   defines them: one each for The Sovereign, The Global Aggregate, and
   PoolParty (skip PoolParty while the skill lists it as blocked), plus up
   to 2 clipping ads when good clips exist. Each is a vertical 9:16 video
   built from REAL material (the issue's own quotes and images, real Global
   Aggregate headlines and screenshots, real app screens), meeting the
   skill's quality bar, with platform captions, hashtags, the fixed CTA, and
   AI labels where required. Never post a text-only reel: if the real
   material can't be fetched, skip that post and log why. No Wade Capital
   service promotion on social. Robot is for long-form only.
3. Render with `python3 studio/text_reel.py` (image scenes) and free tools
   first (video-assembly). Use Higgsfield for realistic promo-cast scenes
   (promotion only), at the cheapest model that meets the brief; stop
   generating once this week's logged Higgsfield spend reaches $5.
4. Before scheduling, check each post against content-rules and brand-voice.
   Save as a draft instead (and note why in the memo) any post that names real
   politicians, candidates, or private individuals, references elections or
   breaking news, or makes a factual claim you cannot source. Clipping ads
   are always drafts.
5. Get each video's public link with `python3 studio/upload_video.py`, then
   schedule in Buffer with automatic publishing (Sovereign Tuesday, Global
   Aggregate Thursday, PoolParty Saturday) at each platform's best engagement time for a US Eastern audience.
6. Update Scripts statuses, set Last Run, Last Run Status, and Last Run Notes
   on the Automation Control row, and add a run summary to this week's
   Strategy Memo.
```
