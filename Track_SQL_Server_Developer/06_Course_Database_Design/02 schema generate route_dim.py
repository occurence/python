import pyodbc
import pandas as pd

DB_PARAMS = (
    "DRIVER={SQL Server};"
    "SERVER=Arc-PC;"
    "DATABASE=DatabaseDesign;"
    "Trusted_Connection=True;"
)

try:
    conn = pyodbc.connect(DB_PARAMS)
    cursor = conn.cursor()
    
    cursor.execute("""
    IF OBJECT_ID('dbo.route_dim', 'U') IS NOT NULL
        DROP TABLE dbo.route_dim;
    
    CREATE TABLE route_dim (
        route_id INTEGER PRIMARY KEY,
        park_name VARCHAR(160) NOT NULL,
        city_name VARCHAR(160) NOT NULL,
        distance_km FLOAT NOT NULL,
        route_name VARCHAR(160) NOT NULL
    );
    """)
    conn.commit()
    
    cursor.execute("""
    WITH DistinctRuns AS (
        SELECT DISTINCT
            park_name,
            city_name,
            distance_km,
            route_name
        FROM RUNS
    )
    , RowNumbers AS (
        SELECT
            ROW_NUMBER() OVER (ORDER BY CASE WHEN city_name = 'Jersey City' THEN 1 ELSE 0 END, city_name, park_name) + 100 AS route_id,
            park_name,
            city_name,
            distance_km,
            route_name
        FROM DistinctRuns
    )
    INSERT INTO route_dim (route_id, park_name, city_name, distance_km, route_name)
    SELECT
        route_id,
        park_name,
        city_name,
        distance_km,
        route_name
    FROM RowNumbers;

    SELECT * FROM route_dim;
    """)
    conn.commit()
    
    # Retrieve and print data
    info_query = """
    SELECT * FROM dbo.route_dim;
    
    SELECT COLUMN_NAME, DATA_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'route_dim' AND TABLE_SCHEMA = 'dbo';
    """
    
    cursor.execute(info_query)
    for row in cursor.fetchall():
        print(row)
    
    cursor.close()
    conn.close()
    
except pyodbc.Error as e:
    print(f"Error: {e}")