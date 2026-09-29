-- Public bucket for rendered studio videos, so Buffer (and the YouTube
-- uploader) can fetch them by URL.
-- Project: Enterprise, skakrtljfaeopfqigyww. NEVER PoolParty (tzebfwmrmzhkeoptwkzy).
--
-- Public = anyone with a file's URL can download it. Only finished videos
-- meant for posting go here, never drafts with private info.
-- No upload/update/delete policies on purpose: anon and logged-in users can't
-- write. Only jobs holding the service-role key (which bypasses RLS) upload,
-- via studio/upload_video.py.
-- file_size_limit stays null, so the project's global upload limit applies
-- (50 MB on the Free plan).

insert into storage.buckets (id, name, public, allowed_mime_types)
values ('studio-videos', 'studio-videos', true, array['video/mp4', 'video/quicktime'])
on conflict (id) do update
  set public = excluded.public,
      allowed_mime_types = excluded.allowed_mime_types;
