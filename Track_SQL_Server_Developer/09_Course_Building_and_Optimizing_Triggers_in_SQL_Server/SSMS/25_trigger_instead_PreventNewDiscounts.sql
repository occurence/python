-- Create a new trigger
DROP TRIGGER IF EXISTS PreventNewDiscounts;
GO
CREATE TRIGGER PreventNewDiscounts
ON Discounts
INSTEAD OF INSERT
AS
	RAISERROR ('You are not allowed to add discounts for existing customers.
                Contact the Sales Manager for more details.', 16, 1);

/*
SELECT 
    name, 
    type_desc, 
    OBJECT_DEFINITION(object_id) AS definition
FROM sys.triggers
ORDER BY name;
*/