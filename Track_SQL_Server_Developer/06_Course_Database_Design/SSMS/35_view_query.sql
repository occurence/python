-- Create a view for reviews with a score above 9
DROP VIEW IF EXISTS dbo.high_scores;
GO
CREATE VIEW high_scores AS
SELECT * FROM REVIEWS
WHERE score > 9;
GO

-- Count the number of self-released works in high_scores
SELECT COUNT(*) FROM high_scores
INNER JOIN labels ON labels.reviewid = high_scores.reviewid
WHERE CAST(labels.label AS VARCHAR(MAX)) = 'self-released';