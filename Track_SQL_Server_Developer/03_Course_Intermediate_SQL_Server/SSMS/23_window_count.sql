SELECT OrderID, TerritoryName, 
       -- Number of rows per partition
       COUNT(TerritoryName) 
       -- Create the window and partitions
       OVER(PARTITION BY TerritoryName) AS TotalOrders
FROM Orders