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
    
    sql_script = """
    IF OBJECT_ID('dbo.runs', 'U') IS NOT NULL
        DROP TABLE dbo.runs;
    
    CREATE TABLE runs (
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

    """
    
    cursor.execute(sql_script)
    conn.commit()
    
    # Load CSV into DataFrame
    file_path = r"D:\\STUDY\\python\\Track_SQL_Server_Developer\\06_Course_Database_Design\\datasets\\Runs.csv"
    df = pd.read_csv(file_path)
    
    # Insert data into SQL Server
    for index, row in df.iterrows():
        cursor.execute(
            "INSERT INTO dbo.runs(duration_mins, week, month, year, park_name, city_name, distance_km, route_name)VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            row["duration_mins"], row["week"], row["month"], row["year"], row["park_name"], row["city_name"], row["distance_km"], row["route_name"]
        )
    
    conn.commit()
    
    # Retrieve and print data
    info_query = """
    SELECT * FROM dbo.runs;
    
    SELECT COLUMN_NAME, DATA_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'runs' AND TABLE_SCHEMA = 'dbo';
    """
    
    cursor.execute(info_query)
    for row in cursor.fetchall():
        print(row)
    
    cursor.close()
    conn.close()
    
except pyodbc.Error as e:
    print(f"Error: {e}")