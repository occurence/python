-- Write a query that returns an aggregation 
SELECT MixDesc, SUM(quantity) AS Total
FROM Shipments
-- Group by the relevant column
GROUP BY MixDesc