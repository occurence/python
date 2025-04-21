-- Count the number of rows by MixDesc
SELECT MixDesc, COUNT(MixDesc)
FROM Shipments
GROUP BY MixDesc