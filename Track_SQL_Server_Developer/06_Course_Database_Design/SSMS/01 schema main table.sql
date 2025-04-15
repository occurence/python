USE DatabaseDesign;
GO

DROP TABLE IF EXISTS runs;

CREATE TABLE runs(
	route_id INTEGER PRIMARY KEY IDENTITY(1,1),
	duration_mins FLOAT NOT NULL,
    week INTEGER NOT NULL,
    month VARCHAR(160) NOT NULL,
    year INTEGER NOT NULL,
    park_name VARCHAR(160) NOT NULL,
    city_name VARCHAR(160) NOT NULL,
    distance_km FLOAT NOT NULL,
    route_name VARCHAR(160) NOT NULL
);

SELECT * FROM runs;