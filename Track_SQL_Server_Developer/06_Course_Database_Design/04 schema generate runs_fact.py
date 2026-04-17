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
    IF OBJECT_ID('dbo.runs_fact', 'U') IS NOT NULL
        DROP TABLE dbo.runs_fact;
    """)
    conn.commit()
    
    cursor.execute("""
    SELECT
        duration_mins, week_id, route_dim.route_id
    INTO runs_fact
    FROM runs
    INNER JOIN route_dim ON route_dim.route_name = runs.route_name
    INNER JOIN week_dim ON CONCAT(week_dim.week, '-', week_dim.month) = CONCAT(runs.week, '-', runs.month);

    SELECT * FROM runs_fact;
    """)
    conn.commit()
    
    # Retrieve and print data
    info_query = """
    SELECT * FROM dbo.runs_fact;
    
    SELECT COLUMN_NAME, DATA_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'runs_fact' AND TABLE_SCHEMA = 'dbo';
    """
    
    cursor.execute(info_query)
    for row in cursor.fetchall():
        print(row)
    
    cursor.close()
    conn.close()
    
except pyodbc.Error as e:
    print(f"Error: {e}")