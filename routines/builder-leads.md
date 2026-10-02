# Builder + Leads prompt (schedule: Wednesdays, overnight)

```
UNATTENDED SCHEDULED RUN. No one is present: do not ask questions or wait for
input. Make reasonable decisions, record any assumption in the output, and if
truly blocked, log the blocker in this week's Strategy Memo and stop.

0. SETUP FIRST: run `git clone --depth 1 https://github.com/dhpatel9616-lang/enterprise-ops ~/enterprise-ops`
   (public repo). Read ~/enterprise-ops/CLAUDE.md and every
   ~/enterprise-ops/.claude/skills/*/SKILL.md and follow them (especially
   build-standards, outreach, and ponytail). If the clone fails, write the
   reason at the top of this week's Strategy Memo and stop.
1. BUILD: in the Build Queue, take the Queued item with the highest Priority
   (oldest first on ties). Set it to In Progress, make the smallest change
   that meets its acceptance criteria on a claude/ branch, and open one PR
   explaining in plain English what changed and how the owner checks it.
   Set the item to PR Open with the PR Link. If it can't be finished, set it
   to Blocked and say why in Notes, in plain words.
2. OUTREACH HEALTH CHECK (read only): leads are sourced, emailed, and called
   automatically by GitHub Actions in the Enterprise-leads repo. Do NOT draft
   or send outreach yourself. Instead, read the last 7 days from Supabase
   skakrtljfaeopfqigyww (leads, run logs): leads added, emails sent, bounces,
   replies, AI calls placed and their outcomes, this month's call spend vs.
   budget, and any failed GitHub Actions runs. Read only; never write.
3. Add a run summary to this week's Strategy Memo: the build result, the
   outreach numbers, anything broken, and anything the owner must do (click
   by click, plain words). Never include the mailing address.
```
