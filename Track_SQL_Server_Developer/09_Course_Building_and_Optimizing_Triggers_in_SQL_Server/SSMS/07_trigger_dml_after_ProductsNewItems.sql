-- Create a new trigger
DROP TRIGGER IF EXISTS ProductsNewItems;
GO
CREATE TRIGGER ProductsNewItems
ON Products
AFTER INSERT
AS
	-- Add details to the history table
	INSERT INTO ProductsHistory(Product, Price, Currency, FirstAdded)
	SELECT Product, Price, Currency, GETDATE()
	FROM inserted;

/*
SELECT 
    name, 
    type_desc, 
    OBJECT_DEFINITION(object_id) AS definition
FROM sys.triggers
ORDER BY name;
*/