SELECT * FROM information_schema.views
WHERE table_schema not in ('pg_catalog', 'information_schema');

DROP VIEW IF EXISTS genre_count;
GO
CREATE VIEW genre_count
WITH SCHEMABINDING
AS
SELECT genre, COUNT_BIG(*) AS genre_total
FROM dbo.genres
GROUP BY genre;
GO

CREATE UNIQUE CLUSTERED INDEX idx_genre_count
ON genre_count (genre);
GO

INSERT INTO genres
VALUES (5000, 'classical');

-- Refresh genre_count
ALTER INDEX idx_genre_count ON dbo.genre_count REBUILD;

SELECT * FROM genre_count;

select * from genres where genre = 'classical'



-- -- Create a materialized view called genre_count 
-- CREATE MATERIALIZED VIEW genre_count AS
-- SELECT genre, COUNT(*) 
-- FROM genres
-- GROUP BY genre;

-- INSERT INTO genres
-- VALUES (50000, 'classical');

-- -- Refresh genre_count
-- REFRESH MATERIALIZED VIEW genre_count;

-- SELECT * FROM genre_count;