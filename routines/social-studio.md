# Social Studio prompt

```
UNATTENDED SCHEDULED RUN. No one is present: do not ask questions or wait for
input. Make reasonable decisions, record any assumption in the output, and if
truly blocked, log the blocker in this week's Strategy Memo and stop. The owner
has granted permission for automatic publishing behind the Notion kill
switches (CLAUDE.md rule 1).

0. SETUP FIRST: run `git clone --depth 1 https://github.com/dhpatel9616-lang/enterprise-ops ~/enterprise-ops`
   (public repo) and `bash ~/enterprise-ops/studio/setup.sh`. Read
   ~/enterprise-ops/CLAUDE.md and every ~/enterprise-ops/.claude/skills/*/SKILL.md,
   follow them, and run studio scripts from ~/enterprise-ops. If the clone or
   setup fails, set the "Autopost — Social" row's Last Run Status to Error with
   the reason, and stop.
1. Read the "Autopost — Social" row in Notion Automation Control. If Enabled is
   checked, you will SCHEDULE posts; if unchecked, save them as Buffer drafts.
2. Produce this week's 3 posts exactly as the content-mix skill defines them
   (Sovereign article promo from real Substack excerpts; PoolParty or Global
   Aggregate by ISO week; Wade Capital consulting post), each one vertical 9:16
   video under 60 seconds for the channels in the skill's channel map, with
   platform-specific captions, hashtags, the skill's fixed CTA, and AI labels
   where required. Robot is for long-form YouTube only; don't use him here.
3. Use code-generated visuals first (video-assembly). Use Higgsfield only for
   PoolParty campaign ads (promo-cast, campaigns/poolparty-friendly-wagers.md),
   at the cheapest model that meets the brief; stop generating once this
   week's logged Higgsfield spend reaches $5.
4. Before scheduling, check each post against content-rules and brand-voice.
   Save as a draft instead (and note why in the memo) any post that names real
   politicians, candidates, or private individuals, references elections or
   breaking news, or makes a factual claim you cannot source.
5. Get each video's public link with `python3 studio/upload_video.py`, then
   schedule in Buffer with automatic publishing for Tuesday, Thursday, and
   Saturday at each platform's best engagement time for a US Eastern audience.
6. Update Scripts statuses, set Last Run, Last Run Status, and Last Run Notes
   on the Automation Control row, and add a run summary to this week's
   Strategy Memo.
```
