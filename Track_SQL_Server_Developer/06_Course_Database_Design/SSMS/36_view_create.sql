DROP VIEW IF EXISTS top_15_2017;
GO
CREATE VIEW top_15_2017 AS
SELECT TOP 15 reviews.reviewid,
    reviews.title,
    reviews.score
   FROM reviews
  WHERE (reviews.pub_year = 2017)
  ORDER BY reviews.score DESC;
GO

DROP VIEW IF EXISTS artist_title;
GO
CREATE VIEW artist_title AS
SELECT reviews.reviewid,
reviews.title,
artists.artist
FROM (reviews
    JOIN artists ON ((artists.reviewid = reviews.reviewid)));
GO

SELECT * FROM information_schema.views
WHERE table_schema not in ('pg_catalog', 'information_schema');
