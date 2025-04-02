-- Add the following rows to the table
INSERT INTO SalesWithoutPrice (Customer, Product, Currency, Quantity)
VALUES ('Fruit Mag', 'Pomelo', 'USD', 200),
	   ('VitaFruit', 'Avocado', 'USD', 400),
	   ('Tasty Fruits', 'Blackcurrant', 'USD', 1100),
	   ('Health Mag', 'Kiwi', 'USD', 100),
	   ('eShop', 'Plum', 'USD', 500);

-- Verify the results after the INSERT
SELECT * FROM SalesWithoutPrice;