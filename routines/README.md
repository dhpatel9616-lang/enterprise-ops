# Routines

Each routine's prompt in claude.ai/code/routines is the same short text, with
its own file name. The real instructions live in this folder, so changing a
routine only takes a merged PR, never another paste.

| Routine | File | Schedule (Eastern) |
|---|---|---|
| Strategist | `strategist.md` | Sunday ~11:30 PM |
| Social Studio | `social-studio.md` | Monday ~12:30 AM |
| Builder + Leads | `builder-leads.md` | Wednesday ~1:30 AM |
| To-Do Email | (self-contained prompt; Claude edits it directly) | Thursday ~8 AM |
| YT Video Studio | `yt-video-studio.md` | Friday ~12:30 AM |

The prompt to paste (replace FILE with the file name above):

```
UNATTENDED SCHEDULED RUN. Nobody is watching: don't ask questions; make
reasonable decisions and note them. The enterprise-ops repository is already
checked out for you (it's attached to this routine). Do not clone anything.
Open routines/FILE in that checkout and follow it exactly; paths in it are
relative to the repo root. If the checkout is missing, send a push
notification saying "enterprise-ops is not attached to this routine" and stop.
```

Each routine needs **enterprise-ops** under its Repositories (routine
settings), because scheduled runs aren't allowed to `git clone` code
themselves. Builder + Leads also needs **Enterprise-leads** there, so it can
push PRs.

All routines use the same environment. Its Setup script box holds the whole of
`studio/setup.sh`; its variables hold the keys (HF_KEY, ENTERPRISE_SUPABASE_URL,
ENTERPRISE_SUPABASE_SERVICE_KEY, YOUTUBE_*, ELEVENLABS_*). Use Sonnet for every routine; none needs a bigger model.
