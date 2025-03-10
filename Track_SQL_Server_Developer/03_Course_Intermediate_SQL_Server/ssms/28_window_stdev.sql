SELECT OrderDate, TerritoryName, 
       -- Calculate the standard deviation
	STDEV(OrderPrice) 
       OVER(PARTITION BY TerritoryName ORDER BY OrderDate) AS StdDevPrice	  
FROM Orders