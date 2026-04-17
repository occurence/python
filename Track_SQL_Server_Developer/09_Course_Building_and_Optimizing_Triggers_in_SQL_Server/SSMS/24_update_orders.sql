-- Update orders
UPDATE Orders SET Quantity = 700 WHERE OrderID = 425;

-- Verify the output of the orders table
SELECT Quantity FROM Orders WHERE OrderID = 425;