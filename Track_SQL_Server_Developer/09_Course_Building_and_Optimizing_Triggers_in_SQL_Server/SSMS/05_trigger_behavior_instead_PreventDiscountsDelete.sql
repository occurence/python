-- Create a new trigger that fires when deleting data
DROP TRIGGER IF EXISTS PreventDiscountsDelete;
GO
CREATE TRIGGER PreventDiscountsDelete
ON Discounts
-- The trigger should fire instead of DELETE
INSTEAD OF DELETE
AS
	PRINT 'You are not allowed to delete data from the Discounts table.';

/*
SELECT 
    name, 
    type_desc, 
    OBJECT_DEFINITION(object_id) AS definition
FROM sys.triggers
ORDER BY name;
*/