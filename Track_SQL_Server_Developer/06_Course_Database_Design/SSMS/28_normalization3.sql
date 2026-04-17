-- Create a new table to satisfy 3NF
DROP TABLE IF EXISTS car_model;
CREATE TABLE car_model(
  model VARCHAR(128),
  manufacturer VARCHAR(128),
  type_car VARCHAR(128)
);

-- Insert data into the new table
INSERT INTO car_model
SELECT DISTINCT
  model,
  manufacturer,
  type_car
FROM cars;

-- Drop columns in rental_cars to satisfy 3NF
ALTER TABLE cars
DROP COLUMN manufacturer, 
type_car;