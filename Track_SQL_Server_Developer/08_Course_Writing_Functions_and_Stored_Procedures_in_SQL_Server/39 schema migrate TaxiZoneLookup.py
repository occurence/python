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
    IF OBJECT_ID('dbo.TaxiZoneLookup', 'U') IS NOT NULL
        DROP TABLE dbo.TaxiZoneLookup;
    
    CREATE TABLE TaxiZoneLookup (
        LocationID int NOT NULL,
        Borough nvarchar(50),
        Zone nvarchar(50),
        ServiceZone nvarchar(50)
    );
    """
    
    cursor.execute(sql_script)
    conn.commit()
    
    # Load CSV into DataFrame
    file_path = r"D:\\STUDY\\python\\Track_SQL_Server_Developer\\08_Course_Writing_Functions_and_Stored_Procedures_in_SQL_Server\\datasets\\taxizone.csv"
    df = pd.read_csv(file_path)
    
    # Insert data into SQL Server~
    for index, row in df.iterrows():
        cursor.execute(
            "INSERT INTO dbo.TaxiZoneLookup(LocationID,Borough,Zone,ServiceZone) VALUES(?,?,?,?)",
           row["LocationID"], row["Borough"], row["Zone"] if pd.notna(row["Zone"]) else None, row["ServiceZone"] if pd.notna(row["ServiceZone"]) else None
        )
    
    conn.commit()
    
    # Retrieve and print data
    info_query = """
    SELECT * FROM dbo.TaxiZoneLookup;
    
    SELECT COLUMN_NAME, DATA_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'TaxiZoneLookup' AND TABLE_SCHEMA = 'dbo';
    """
    
    cursor.execute(info_query)
    for row in cursor.fetchall():
        print(row)
    
    cursor.close()
    conn.close()
    
except pyodbc.Error as e:
    print(f"Error: {e}")