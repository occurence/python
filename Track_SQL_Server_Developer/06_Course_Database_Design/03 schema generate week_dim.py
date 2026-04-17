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
    IF OBJECT_ID('dbo.week_dim', 'U') IS NOT NULL
        DROP TABLE dbo.week_dim;
    
    CREATE TABLE week_dim (
        week_id INTEGER PRIMARY KEY,
        week INTEGER NOT NULL,
        month VARCHAR(160) NOT NULL,
        year INTEGER NOT NULL
    );
    """)
    conn.commit()
    
    cursor.execute("""
    WITH DistinctWeeks AS (
        SELECT
        DISTINCT week, month, year,
        MONTH(CAST('1-' + month + '-' + CAST(year AS VARCHAR(4)) AS DATETIME)) AS MonthOrder
        FROM runs
    )
    , RowNumbers AS (
        SELECT
            ROW_NUMBER() OVER (ORDER BY MonthOrder) + 600 AS week_id,
            week,
            month,
            year,
            MonthOrder
        FROM DistinctWeeks
    )
    INSERT INTO week_dim (week_id, week, month, year)
    SELECT week_id, week, month, year FROM RowNumbers;

    SELECT * FROM week_dim;
    """)
    conn.commit()
    
    # Retrieve and print data
    info_query = """
    SELECT * FROM dbo.week_dim;
    
    SELECT COLUMN_NAME, DATA_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'week_dim' AND TABLE_SCHEMA = 'dbo';
    """
    
    cursor.execute(info_query)
    for row in cursor.fetchall():
        print(row)
    
    cursor.close()
    conn.close()
    
except pyodbc.Error as e:
    print(f"Error: {e}")