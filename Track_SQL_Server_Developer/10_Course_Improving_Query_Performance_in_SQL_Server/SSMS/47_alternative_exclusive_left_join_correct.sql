-- Second attempt
SELECT c.CustomerID,
       c.CompanyName,
	   c.ContactName,
	   c.ContactTitle,
	   c.Phone 
FROM Customers c
LEFT OUTER JOIN Orders o
	ON c.CustomerID = o.CustomerID
WHERE c.Country = 'France'
	AND o.CustomerID IS NULL; -- Filter condition