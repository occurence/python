-- Create the trigger
DROP TRIGGER IF EXISTS SalesCalculateTotalAmount;
GO
CREATE TRIGGER [SalesCalculateTotalAmount]
ON [SalesWithoutPrice]
AFTER INSERT
AS
	UPDATE [sp]
	SET [sp].[TotalAmount] = [sp].[Quantity] * [p].[Price]
	FROM [SalesWithoutPrice] AS [sp]
	INNER JOIN [Products] AS [p] ON [sp].Product = [p].[Product]
	WHERE [sp].[TotalAmount] IS NULL;

/*
SELECT 
    name, 
    type_desc, 
    OBJECT_DEFINITION(object_id) AS definition
FROM sys.triggers
ORDER BY name;
*/