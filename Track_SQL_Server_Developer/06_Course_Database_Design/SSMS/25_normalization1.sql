-- Create a new table to hold the cars rented by customers
DROP TABLE IF EXISTS cust_rentals;
CREATE TABLE cust_rentals (
  customer_id INT NOT NULL,
  car_id VARCHAR(128) NULL,
  invoice_id VARCHAR(128) NULL
);

-- Insert data into the new table
INSERT INTO cust_rentals
SELECT DISTINCT
  customer_id,
  cars_rented,
  invoice_id
FROM customers;

-- Drop two columns from customers table to satisfy 1NF
ALTER TABLE customers
DROP COLUMN cars_rented,
invoice_id;