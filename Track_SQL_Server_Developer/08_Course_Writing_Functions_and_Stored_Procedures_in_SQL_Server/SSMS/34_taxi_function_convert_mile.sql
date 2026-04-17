-- Create the function
CREATE FUNCTION dbo.ConvertMileToKm (@Miles numeric(18,2))
-- Specify return data type
RETURNS numeric(18,2)
AS
BEGIN
RETURN
	-- Convert Miles to Kilometers
	(SELECT @Miles * 1.609)
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