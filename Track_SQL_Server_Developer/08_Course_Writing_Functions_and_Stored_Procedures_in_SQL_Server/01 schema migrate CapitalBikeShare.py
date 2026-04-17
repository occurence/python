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
    IF OBJECT_ID('dbo.CapitalBikeShare', 'U') IS NOT NULL
        DROP TABLE dbo.CapitalBikeShare;
    
    CREATE TABLE CapitalBikeShare (
        ID INT, 
        Duration INT, 
        StartDate DATETIME2(7), 
        EndDate DATETIME2(7), 
        StartStationNumber INT, 
        StartStation VARCHAR(100), 
        EndStationNumber INT, 
        EndStation VARCHAR(100), 
        BikeNumber VARCHAR(50), 
        MemberType VARCHAR(50)
    );
    """
    
    cursor.execute(sql_script)
    conn.commit()
    
    # Load CSV into DataFrame
    file_path = r"D:\\STUDY\\python\\Track_SQL_Server_Developer\\08_Course_Writing_Functions_and_Stored_Procedures_in_SQL_Server\\datasets\\bikeshare.csv"
    df = pd.read_csv(file_path)
    
    # Insert data into SQL Server~
    for index, row in df.iterrows():
        cursor.execute(
            "INSERT INTO dbo.CapitalBikeShare(ID,Duration,StartDate,EndDate,StartStationNumber,StartStation,EndStationNumber,EndStation,BikeNumber,MemberType)VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            row["ID"], row["Duration"], row["StartDate"], row["EndDate"], row["StartStationNumber"], row["StartStation"], row["EndStationNumber"], row["EndStation"], row["BikeNumber"], row["MemberType"]
        )
    
    conn.commit()
    
    # Retrieve and print data
    info_query = """
    SELECT * FROM dbo.CapitalBikeShare;
    
    SELECT COLUMN_NAME, DATA_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'CapitalBikeShare' AND TABLE_SCHEMA = 'dbo';
    """
    
    cursor.execute(info_query)
    for row in cursor.fetchall():
        print(row)
    
    cursor.close()
    conn.close()
    
except pyodbc.Error as e:
    print(f"Error: {e}")