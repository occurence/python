-- Alter the stored procedure
CREATE OR ALTER PROCEDURE dbo.cuspRideSummaryDelete
	-- (Incorrectly) specify @DateParm
	@DateParm nvarchar(30),
    -- Specify @Error
	@Error nvarchar(max) = NULL OUTPUT
AS
SET NOCOUNT ON
BEGIN
  -- Start of the TRY block
  BEGIN TRY
  	  -- Delete
      DELETE FROM RideSummary
      WHERE Date = @DateParm
  -- End of the TRY block
  END TRY
  -- Start of the CATCH block
  BEGIN CATCH
		SET @Error = 
		'Error_Number: '+ CAST(ERROR_NUMBER() AS VARCHAR) +
		'Error_Severity: '+ CAST(ERROR_SEVERITY() AS VARCHAR) +
		'Error_State: ' + CAST(ERROR_STATE() AS VARCHAR) + 
		'Error_Message: ' + ERROR_MESSAGE() + 
		'Error_Line: ' + CAST(ERROR_LINE() AS VARCHAR)
  -- End of the CATCH block
  END CATCH
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