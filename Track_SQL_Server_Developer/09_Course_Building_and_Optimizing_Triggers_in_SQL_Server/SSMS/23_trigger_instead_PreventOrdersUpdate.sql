-- Create the trigger
DROP TRIGGER IF EXISTS PreventOrdersUpdate;
GO
CREATE TRIGGER PreventOrdersUpdate
ON ORDERS
INSTEAD OF UPDATE
AS
	RAISERROR ('Updates on "Orders" table are not permitted.
                Place a new order to add new products.', 16, 1);

/*
SELECT 
    name, 
    type_desc, 
    OBJECT_DEFINITION(object_id) AS definition
FROM sys.triggers
ORDER BY name;
*/