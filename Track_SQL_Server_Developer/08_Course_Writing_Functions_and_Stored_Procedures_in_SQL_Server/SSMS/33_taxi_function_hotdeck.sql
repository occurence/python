-- Create the function
CREATE FUNCTION dbo.GetTripDistanceHotDeck()
-- Specify return data type
RETURNS NUMERIC(18,4)
AS 
BEGIN
RETURN
	-- Select the first TripDistance value
	(SELECT TOP 1 TripDistance
	FROM YellowTripData
    -- Sample 1000 records
	TABLESAMPLE(1000 rows)
    -- Only include records where TripDistance is > 0
	WHERE TripDistance > 0)
END;

/*
SELECT 
    name, 
    type_desc, 
    OBJECT_DEFINITION(object_id) AS definition
FROM sys.objects
WHERE type IN ('FN', 'IF', 'TF')
ORDER BY name;
*/