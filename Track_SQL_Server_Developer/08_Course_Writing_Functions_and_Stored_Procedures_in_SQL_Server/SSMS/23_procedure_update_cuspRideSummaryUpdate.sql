-- Create the stored procedure
DROP PROCEDURE IF EXISTS dbo.cuspRideSummaryUpdate;
GO
CREATE PROCEDURE dbo.cuspRideSummaryUpdate
	-- Specify @DateParm input parameter
	(@DateParm date,
     -- Specify @RideHrs input parameter
     @RideHrs numeric(18,0))
AS
BEGIN
SET NOCOUNT ON
-- Update RideSummary
UPDATE RideSummary
-- Set
SET
	Date = @DateParm,
    RideHours = @RideHrs
-- Include records where Date equals @DateParm
WHERE Date = @DateParm
END;

/*
SELECT 
    name, 
    type_desc, 
    OBJECT_DEFINITION(object_id) AS definition
FROM sys.objects
WHERE type IN ('P')
ORDER BY name;
*/