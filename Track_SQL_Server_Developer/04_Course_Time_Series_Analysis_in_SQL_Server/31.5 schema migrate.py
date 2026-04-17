import pyodbc
import pandas as pd

DB_PARAMS = (
    "DRIVER={SQL Server};"
    "SERVER=Arc-PC;"
    "DATABASE=datacamp;"
    "Trusted_Connection=True;"
)

try:
    conn = pyodbc.connect(DB_PARAMS)
    cursor = conn.cursor()
    
    sql_script = """
    IF OBJECT_ID('dbo.IncidentType', 'U') IS NOT NULL
        DROP TABLE dbo.IncidentType;
    
    CREATE TABLE IncidentType(
        IncidentTypeID integer,
        IncidentType nvarchar(255)
    );

    """
    
    cursor.execute(sql_script)
    conn.commit()
    
    # Load CSV into DataFrame
    file_path = r"D:\\STUDY\\python\\Track_SQL_Server_Developer\\04_Course_Time_Series_Analysis_in_SQL_Server\\datasets\\IncidentTypeTable.csv"
    df = pd.read_csv(file_path)

    # Insert data into SQL Server
    for index, row in df.iterrows():
        cursor.execute(
            "INSERT INTO dbo.IncidentType (IncidentTypeID, IncidentType) VALUES (?, ?)",
            row["IncidentTypeID"], row["IncidentType"]
        )
        
    conn.commit()
    
    # Retrieve and print data
    info_query = """
    SELECT * FROM dbo.IncidentType;
    
    SELECT COLUMN_NAME, DATA_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'IncidentType' AND TABLE_SCHEMA = 'dbo';
    """
    
    cursor.execute(info_query)
    for row in cursor.fetchall():
        print(row)
    
    cursor.close()
    conn.close()
    
except pyodbc.Error as e:
    print(f"Error: {e}")