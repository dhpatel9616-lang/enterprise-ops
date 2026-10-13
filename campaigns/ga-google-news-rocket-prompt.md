# The Global Aggregate: Google News readiness (Rocket prompt)

Google stopped taking Google News applications in 2024. Sites are picked up
automatically when they look like a real, transparent news publication. This
prompt gives globalaggregate.org what Google looks for. The owner pastes it
into Rocket and publishes (owner, 2026-10-14).

Honest limit: Google News favors original work. Pages that only list other
outlets' headlines rank poorly, so each story page needs our own short
summary of how the coverage differs (the "compare" part is our original
work).

## Paste this into Rocket

```
Please make globalaggregate.org ready for Google News. Keep the current design; add these:

1. News sitemap: a page at /news-sitemap.xml that lists every story page published in the
   last 48 hours, in Google's News sitemap format (news:publication name "The Global Aggregate",
   language "en", news:publication_date in ISO 8601 with time zone, news:title). It updates
   automatically whenever a story is added. Also keep a normal /sitemap.xml listing all
   pages. Add both to /robots.txt as "Sitemap:" lines, and make sure robots.txt allows Googlebot.

2. Every story page:
   - A visible headline (one H1), a visible "Published" date and time, and an "Updated" time
     when it changes.
   - A visible byline: "By The Global Aggregate newsroom" linking to the About page.
   - Our own 2-4 sentence summary at the top, in our words, saying what happened and how the
     outlets' coverage differs. Then the outlet headlines, each linking to its source.
   - Structured data (JSON-LD) of type NewsArticle: headline, description, datePublished,
     dateModified, image (at least 1200px wide), author (Organization "The Global Aggregate",
     url to the About page), publisher (Organization "The Global Aggregate" with logo),
     mainEntityOfPage.
   - A clean, permanent URL with the headline words in it (no IDs-only URLs, no query strings).

3. Pages Google checks for trust, linked in the footer of every page:
   - About: who we are, what we do (compare how different countries' outlets report the same
     story), and how stories are put together. If an About page already exists, keep its text
     and only add a short "How we compile stories" section. Do not invent people's names,
     titles or credentials; if a field is unknown, leave a clearly marked [OWNER TO FILL] note.
   - Contact: a contact form or email address.
   - Corrections policy: "If we get something wrong, tell us via the Contact page; we correct
     it and note the change at the bottom of the story."
   - Editorial standards: we link every outlet we quote, we never change a headline's words,
     and our summaries are labeled as ours.

4. Speed and basics: story pages load fast on phones, every image has alt text, and every page
   has its own <title> and meta description.

When done, list the URLs of the news sitemap, the About, Contact, Corrections and Editorial
standards pages.
```

## After Rocket publishes: owner steps (about 10 minutes, once)

1. Go to **search.google.com/search-console** and sign in with your Google account.
2. Click **Add property**, choose **Domain**, type `globalaggregate.org`, and follow the
   steps to verify (Google gives you a line to add where your domain is managed; Rocket's
   domain settings can do this).
3. In Search Console, click **Sitemaps** on the left, type `news-sitemap.xml`, click
   **Submit**, then do the same for `sitemap.xml`.
4. Nothing else to apply for. It can take a few weeks to start showing up in Google News.
