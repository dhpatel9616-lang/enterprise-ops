-- Let the public studio-videos bucket also hold The Sovereign podcast:
-- episode MP3s, the cover image, and the podcast feed (studio/podcast.py).
-- Project: Enterprise, skakrtljfaeopfqigyww. NEVER PoolParty (tzebfwmrmzhkeoptwkzy).
-- Still public-read and service-key-only writes (see 20260928210000_studio_videos_bucket.sql).

update storage.buckets
   set allowed_mime_types = array['video/mp4', 'video/quicktime', 'audio/mpeg', 'image/jpeg', 'application/rss+xml']
 where id = 'studio-videos';
