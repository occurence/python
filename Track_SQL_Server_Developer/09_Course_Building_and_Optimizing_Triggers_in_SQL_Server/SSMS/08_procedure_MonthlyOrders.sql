-- Create the stored procedure
DROP PROCEDURE IF EXISTS MonthlyOrders;
GO
CREATE PROCEDURE [MonthlyOrders]
AS
BEGIN
	SELECT [Product],
		   DATENAME(MONTH, [OrderDate]) + ' ' + CAST(YEAR([OrderDate]) AS NVARCHAR(4)) AS [OrderMonth],
		   SUM(Quantity) AS [MonthlyQuantity],
		   SUM(TotalAmount) AS [MonthlyAmount]
	FROM [Orders]
	GROUP BY [Product], DATENAME(MONTH, [OrderDate]) + ' ' + CAST(YEAR([OrderDate]) AS NVARCHAR(4))
	ORDER BY [Product],
			 [OrderMonth];
END

/*
SELECT 
    name, 
    type_desc, 
    OBJECT_DEFINITION(object_id) AS definition
FROM sys.objects
WHERE type IN ('P')
ORDER BY name;
*/