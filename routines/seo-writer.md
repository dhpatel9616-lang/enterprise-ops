# SEO Writer (Mondays ~2:30 AM ET)

Read CLAUDE.md, then ONLY these skills: brand-voice, monetization.

One new guide a week for the Wade Capital website, so small business owners
searching Google find us (owner, 2026-10-06). The **wade-capital-website**
repository is attached to this routine.

1. Notion → Automation Control → "Autopublish — Website guides": note whether
   **Enabled** is checked (view mode or fetch; never SQL mode).
2. In wade-capital-website, open `guides/TOPICS.md` and take the first
   unchecked topic. Search the web (at most 3 searches) only to confirm facts,
   menu names in Google's tools, or rules you will state.
3. Write the guide (900–1,300 words) for a busy owner with no tech background:
   - Title = the search phrase, naturally worded ("How to …", "What is …").
   - Short intro on why it matters, then numbered steps with exact clicks,
     a short "simple weekly routine" or checklist, plain words, no jargon.
   - Only true, checkable statements. No invented statistics, customers,
     testimonials or case studies; no prices.
   - Link to one related guide when one exists (`/guides/<file>.html`).
4. Publish it from `guides/_template.html`: copy to `guides/<slug>.html`
   (slug = short, lowercase, hyphens) and fill {{TITLE}}, {{DESCRIPTION}}
   (under 160 characters), {{SLUG}}, {{DATE}} (YYYY-MM-DD), {{DATE_LONG}}
   ("October 7, 2026") and {{BODY}} (indent like the existing guide; h2 for
   sections, p, ul/ol). No {{...}} may remain.
5. Add the guide to the top of the list in `guides/index.html` (after the
   GUIDES:LIST marker, same format as the other lines) and to `sitemap.xml`
   (after the GUIDES:SITEMAP marker, with lastmod). Check the topic in
   TOPICS.md with the file name. Add 2 new topic ideas at the bottom when
   fewer than 5 are unchecked.
6. Enabled → commit to `main` and push (it goes live on Netlify in about a
   minute; the owner approved automatic publishing for guides only). Disabled
   → push a `claude/guide-<slug>` branch and open a PR instead. Never change
   any other page in an automatic run.
7. Update the Automation Control row: Last Run, Last Run Status, and Last Run
   Notes (the guide's title and live link, or the PR link).
