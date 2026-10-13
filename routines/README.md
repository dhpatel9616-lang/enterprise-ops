# Routines

Each routine's prompt in claude.ai/code/routines is the same short text, with
its own file name. The real instructions live in this folder, so changing a
routine only takes a merged PR, never another paste.

| Routine | File | Schedule (Eastern) |
|---|---|---|
| Strategist | `strategist.md` | Sunday ~11:30 PM |
| Social Studio | `social-studio.md` | Monday ~12:30 AM |
| SEO Writer | `seo-writer.md` | Monday ~2:30 AM |
| Clip Studio | `clip-studio.md` | Daily ~12:15 PM |
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
push PRs. SEO Writer also needs **wade-capital-website**. Clip Studio needs the
`BUFFER_CLIPS_API_KEY` variable (clip Buffer account → Settings → API) and
`api.buffer.com` under the environment's allowed domains. Social Studio and
Clip Studio search free footage (`studio/find_footage.py`): `PIXABAY_API_KEY`
plus the allowed domains archive.org, images-api.nasa.gov,
images-assets.nasa.gov, commons.wikimedia.org, upload.wikimedia.org,
pixabay.com and cdn.pixabay.com. Social Studio also publishes the podcast
(`studio/podcast.py`, needs sovereignnewsletter.substack.com).

All routines use the same environment. Its Setup script box holds one line,
`bash /home/user/enterprise-ops/studio/setup.sh || true` (so it never goes stale or blocks a run); its variables hold the keys (HF_KEY, ENTERPRISE_SUPABASE_URL,
ENTERPRISE_SUPABASE_SERVICE_KEY, YOUTUBE_*). Use Sonnet for every routine; none needs a bigger model.
