SELECT OrderID, TerritoryName, 
       -- Total price for each partition
       SUM(OrderPrice) 
       -- Create the window and partitions
       OVER(PARTITION BY TerritoryName) AS TotalPrice
FROM Orders