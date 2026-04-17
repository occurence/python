-- Get all non-systems views
SELECT * FROM information_schema.views
WHERE table_schema not in ('pg_catalog', 'information_schema');