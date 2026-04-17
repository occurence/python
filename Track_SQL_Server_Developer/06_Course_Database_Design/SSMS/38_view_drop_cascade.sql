SELECT * FROM information_schema.views
WHERE table_schema not in ('pg_catalog', 'information_schema');

-- Which is the DROP command that would drop both top_15_2017 and top_artists_2017?
DROP VIEW top_15_2017; -- CASCADE;
GO

SELECT * FROM information_schema.views
WHERE table_schema not in ('pg_catalog', 'information_schema');
