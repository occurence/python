-- Set up the TRY block
BEGIN TRY  	
	SELECT 'Total: ' + SUM(price * quantity) AS total
	FROM orders  
END TRY
-- Set up the CATCH block
BEGIN CATCH  
	-- Show error information.
	SELECT  ERROR_NUMBER() AS number,
        	ERROR_SEVERITY() AS severity_level,
        	ERROR_STATE() AS state,
        	ERROR_LINE() AS line,
        	ERROR_MESSAGE() AS message;
END CATCH