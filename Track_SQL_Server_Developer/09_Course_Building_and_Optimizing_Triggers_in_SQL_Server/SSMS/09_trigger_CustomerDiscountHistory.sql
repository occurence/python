-- Create the trigger
DROP TRIGGER IF EXISTS CustomerDiscountHistory;
GO
CREATE TRIGGER [CustomerDiscountHistory]
ON [Discounts]
AFTER UPDATE
AS
	INSERT INTO [DiscountsHistory] ([Customer], [OldDiscount], [NewDiscount], [ChangeDate])
	SELECT [i].[Customer], [d].[Discount], [i].[Discount], GETDATE()
	FROM [inserted] AS [i]
	INNER JOIN [deleted] AS d ON [i].[Customer] = [d].[Customer];

/*
SELECT 
    name, 
    type_desc, 
    OBJECT_DEFINITION(object_id) AS definition
FROM sys.triggers
ORDER BY name;
*/