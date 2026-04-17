-- Create the stored procedure
DROP PROCEDURE IF EXISTS dbo.cuspRideSummaryDelete;
GO
CREATE PROCEDURE dbo.cuspRideSummaryDelete
	-- Specify @DateParm input parameter
	(@DateParm date,
     -- Specify @RowCountOut output parameter
     @RowCountOut int OUTPUT)
AS
BEGIN
-- Delete record(s) where Date equals @DateParm
DELETE FROM dbo.RideSummary
WHERE Date = @DateParm
-- Set @RowCountOut to @@ROWCOUNT
SET @RowCountOut = @@ROWCOUNT
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