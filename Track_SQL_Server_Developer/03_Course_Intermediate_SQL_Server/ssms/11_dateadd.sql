-- Return the DeliveryDate as 5 days after the ShipDate
SELECT OrderDate, 
       DATEADD(DD, 5, ShipDate) AS DeliveryDate
FROM Shipments