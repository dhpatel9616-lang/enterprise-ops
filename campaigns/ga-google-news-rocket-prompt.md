# The Global Aggregate: story pages + Google News readiness (Rocket prompt)

Google stopped taking Google News applications in 2024. Sites are picked up
automatically when they look like a real, transparent news publication with
**individual article pages**. As of 2026-10-14, globalaggregate.org has only
the home feed and the sign-up page (the code in the `globalaggregate` repo:
`src/app/page.tsx`, `robots.ts`, `sitemap.ts`), so there is nothing for
Google News to list. This prompt adds one page per story cluster (the
`cluster_id` the ingest already assigns), then the Google News pieces on top.

(The owner's first try on 2026-10-14 re-applied the older SEO-basics prompt;
use this one.)

Honest limits:
- Google News favors original work. Each story page leads with our own
  comparison of how countries covered it, so it isn't just a list of links.
  Inclusion is still Google's call; the pages help normal Google search either way.
- Articles are kept 7 days, so story pages expire with them; that's normal
  for news.

Bonus: our "One Story, Five Countries" ads can link to the exact story page.

## Paste this into Rocket

```
Please add individual story pages to globalaggregate.org and make the site ready for Google
News. Keep the current design and the home feed as they are.

PART 1 - STORY PAGES
1. New page at /story/[cluster_id]: one page per story cluster, using the existing `articles`
   table (fields id, source, country, topic, title, url, published_at, description, cluster_id,
   is_state_media). Render it on the server (so search engines see the full text without
   JavaScript), refreshed at least every 15 minutes.
2. Only clusters covered from at least 3 different countries get a page.
3. Page layout:
   - H1 headline: the headline of the earliest article in the cluster.
   - Line under it: "Covered by N outlets in M countries" + first and latest published time.
   - "How the coverage differs": a short automatic comparison in plain words, built from the
     data (which countries covered it, which outlets, state-affiliated sources flagged with
     the existing badge, and each country's headline side by side). Label it
     "Compiled by The Global Aggregate".
   - Then the headlines grouped by country: country name, outlet, headline, published time,
     link to the original article (opens in a new tab).
   - A "Compare more stories" link back to the home feed.
4. In the home feed, make each clustered article's "also covered in" countries link to its
   story page.
5. If a cluster no longer exists (articles are deleted after 7 days), show "This story has
   expired" with a link to the home feed, and return HTTP status 410.

PART 2 - GOOGLE NEWS READINESS
6. News sitemap at /news-sitemap.xml: every story page published in the last 48 hours, in
   Google's News sitemap format (news:publication name "The Global Aggregate", language "en",
   news:publication_date in ISO 8601 with time zone, news:title). Add story pages to the
   existing /sitemap.xml too. Add a second "Sitemap:" line for news-sitemap.xml in robots.ts.
7. Every story page: one H1, visible "Published" and "Updated" times, byline
   "By The Global Aggregate newsroom" linking to the About page, its own <title> and meta
   description, and JSON-LD of type NewsArticle (headline, description, datePublished,
   dateModified, author and publisher = Organization "The Global Aggregate" with logo and url,
   mainEntityOfPage).
8. Trust pages, linked in the footer of every page:
   - /about: what we do (compare how different countries' outlets report the same story) and
     a short "How we compile stories" section. Do not invent people's names, titles or
     credentials; leave a clearly marked [OWNER TO FILL] note for anything unknown.
   - /contact: a contact form or email address.
   - /corrections: "If we get something wrong, tell us via the Contact page; we correct it and
     note the change on the story page."
   - /editorial-standards: we link every outlet we show, we never change a headline's words,
     state-affiliated outlets are labeled, and our comparisons are labeled as ours.
9. Search engine and link-preview crawlers (Googlebot, Google-InspectionTool, facebookexternalhit,
   Twitterbot, and Buffer) must be able to load every page; make sure no bot-protection or
   security checkpoint blocks them.

When done, list: one example story page URL, the news sitemap URL, and the About, Contact,
Corrections and Editorial standards URLs.
```

## After Rocket publishes: owner steps (about 10 minutes, once)

1. Go to **search.google.com/search-console** and sign in with your Google account.
2. Click **Add property**, choose **Domain**, type `globalaggregate.org`, and follow the
   steps to verify (Google gives you a line to add where your domain is managed; Rocket's
   domain settings can do this).
3. In Search Console, click **Sitemaps** on the left, type `news-sitemap.xml`, click
   **Submit**, then do the same for `sitemap.xml`.
4. Paste Rocket's list of URLs to Claude so it can check the pages.
5. Nothing else to apply for. It can take a few weeks to start showing up in Google News.
