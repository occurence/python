-- Create a new table called film_partitioned
DROP VIEW IF EXISTS film_partitioned;
GO
CREATE VIEW film_partitioned AS
SELECT * FROM film_2019
UNION ALL
SELECT * FROM film_2018
UNION ALL
SELECT * FROM film_2017;
GO

-- Create the partitions for 2019, 2018, and 2017
DROP TABLE IF EXISTS film_2019;
CREATE TABLE film_2019 (
    film_id INT,
    title NVARCHAR(255) NOT NULL,
    release_year NVARCHAR(4) CHECK (release_year = '2019')
);
GO

DROP TABLE IF EXISTS film_2018;
CREATE TABLE film_2018 (
    film_id INT,
    title NVARCHAR(255) NOT NULL,
    release_year NVARCHAR(4) CHECK (release_year = '2018')
);
GO

DROP TABLE IF EXISTS film_2017;
CREATE TABLE film_2017 (
    film_id INT,
    title NVARCHAR(255) NOT NULL,
    release_year NVARCHAR(4) CHECK (release_year = '2017')
);
GO

-- Insert the data into film_partitioned
INSERT INTO film_2019 (film_id, title, release_year)
SELECT film_id, title, release_year
FROM film
WHERE release_year = '2019';

INSERT INTO film_2018 (film_id, title, release_year)
SELECT film_id, title, release_year
FROM film
WHERE release_year = '2018';

INSERT INTO film_2017 (film_id, title, release_year)
SELECT film_id, title, release_year
FROM film
WHERE release_year = '2017';

-- View film_partitioned
SELECT * FROM film_partitioned;