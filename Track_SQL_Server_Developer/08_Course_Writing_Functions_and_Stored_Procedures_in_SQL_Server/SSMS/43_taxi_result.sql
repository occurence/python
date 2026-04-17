-- Create @Borough
DECLARE @Borough AS nvarchar(30) = 'Manhattan'
-- Execute the SP
EXEC dbo.cuspPickupZoneShiftStats
    -- Pass @Borough
	@Borough = @Borough;