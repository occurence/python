SET STATISTICS IO ON -- Turn the IO command on

-- Example 1
SELECT CustomerID,
       CompanyName,
       (SELECT COUNT(*) 
	    FROM Orders AS o -- Add table
		WHERE c.CustomerID = o.CustomerID) CountOrders
FROM Customers AS c
WHERE CustomerID IN -- Add filter operator
       (SELECT CustomerID 
	    FROM Orders 
		WHERE ShipCity IN
            ('Berlin','Bern','Bruxelles','Helsinki',
			'Lisboa','Madrid','Paris','London'));

-- Example 2
SELECT c.CustomerID,
       c.CompanyName,
       COUNT(o.CustomerID)
FROM Customers AS c
INNER JOIN Orders AS o -- Join operator
    ON c.CustomerID = o.CustomerID
WHERE o.ShipCity IN -- Shipping destination column
     ('Berlin','Bern','Bruxelles','Helsinki',
	 'Lisboa','Madrid','Paris','London')
GROUP BY c.CustomerID,
         c.CompanyName;

SET STATISTICS IO OFF -- Turn the IO command off

/*
Table 'Customers'. Scan count 1, logical reads 2, physical reads 0,...
Table 'Orders'. Scan count 2, logical reads 32, physical reads 0,...

Table 'Customers'. Scan count 1, logical reads 2, physical reads 0,...
Table 'Orders'. Scan count 2, logical reads 16, physical reads 0,...
*/