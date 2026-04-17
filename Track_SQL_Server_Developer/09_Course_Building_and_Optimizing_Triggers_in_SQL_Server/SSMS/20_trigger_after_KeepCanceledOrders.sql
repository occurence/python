-- Create a new trigger for canceled orders
DROP TRIGGER IF EXISTS KeepCanceledOrders;
GO
CREATE TRIGGER KeepCanceledOrders
ON Orders
AFTER DELETE
AS 
	INSERT INTO CanceledOrders
	SELECT * FROM deleted;

/*
SELECT 
    name, 
    type_desc, 
    OBJECT_DEFINITION(object_id) AS definition
FROM sys.triggers
ORDER BY name;
*/