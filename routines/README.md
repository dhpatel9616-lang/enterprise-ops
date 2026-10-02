# Routine prompts (paste-ready)

These routines were created outside Claude, so only the owner can edit them.
They run in the environment named in each routine's settings: that environment
needs the keys (HF_KEY, ENTERPRISE_SUPABASE_URL, ENTERPRISE_SUPABASE_SERVICE_KEY,
YOUTUBE_*), network access to *.supabase.co, *.higgsfield.ai, *.googleapis.com,
and `studio/setup.sh` in its Setup script box. To edit a routine:
open https://claude.ai/code/routines, click the routine, replace its prompt with
the text in the matching file (everything inside the grey box), and save.

| Routine | File | Also change |
|---|---|---|
| YT Video Studio | `yt-video-studio.md` | Schedule: **Fridays 1:37 AM Eastern** (so Thursday-night recordings make it) |
| Social Studio | `social-studio.md` | nothing |
| Builder + Leads | `builder-leads.md` | replace the whole prompt |
| Strategist | `setup-step.md` | add the setup step to the top of the existing prompt |

**Studio tools come from the environment, not the routine.** Scheduled runs
are not allowed to run `setup.sh` themselves (the 2026-10-01 YouTube run was
blocked this way). Paste the whole of `studio/setup.sh` into the Setup script
box of the environment each routine uses (cloud environment menu → Edit →
Setup script). The prompts only run it as a fallback when a tool is missing.
