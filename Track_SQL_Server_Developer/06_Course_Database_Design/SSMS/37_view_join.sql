-- Create a view with the top artists in 2017
DROP VIEW IF EXISTS top_artists_2017;
GO
CREATE VIEW top_artists_2017 AS
-- with only one column holding the artist field
SELECT artist_title.artist FROM artist_title
INNER JOIN top_15_2017
ON top_15_2017.reviewid = artist_title.reviewid;
GO

-- Output the new view
SELECT * FROM top_artists_2017;

SELECT * FROM information_schema.views
WHERE table_schema not in ('pg_catalog', 'information_schema');
