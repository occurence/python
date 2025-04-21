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
    IF OBJECT_ID('dbo.Nations', 'U') IS NOT NULL
        DROP TABLE dbo.Nations;
    
    CREATE TABLE Nations (
        CountryName varchar(100),
        Code2 varchar(2),
        Code3 varchar(3),
        Capital varchar(50),
        WorldBankRegion varchar(30),
        UNContinentRegion varchar(8),
        UNStatisticalRegion varchar(50),
        Pop2016 int,
        Pop2017 int,
        Land_km2 real,
        Water_km2 real
    );
    """
    
    cursor.execute(sql_script)
    conn.commit()
    
    # Load CSV into DataFrame
    file_path = r"D:\\STUDY\\python\\Track_SQL_Server_Developer\\10_Course_Improving_Query_Performance_in_SQL_Server\\datasets\\Nations.csv"
    df = pd.read_csv(file_path)

    # Insert data into SQL Server
    for index, row in df.iterrows():
        cursor.execute(
            "INSERT INTO dbo.Nations(CountryName,Code2,Code3,Capital,WorldBankRegion,UNContinentRegion,UNStatisticalRegion,Pop2016,Pop2017,Land_km2,Water_km2) VALUES(?,?,?,?,?,?,?,?,?,?,?)",
            row["CountryName"], 
            row["Code2"] if pd.notna(row["Code2"]) else None, 
            row["Code3"], row["Capital"], row["WorldBankRegion"], row["UNContinentRegion"], row["UNStatisticalRegion"], row["Pop2016"], row["Pop2017"],
            float(row["Land_km2"]) if pd.notna(row["Land_km2"]) else None, 
            float(row["Water_km2"]) if pd.notna(row["Water_km2"]) else None
        )
    
    conn.commit()
    
    # Retrieve and print data
    info_query = """
    SELECT * FROM dbo.Nations;
    
    SELECT COLUMN_NAME, DATA_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'Nations' AND TABLE_SCHEMA = 'dbo';
    """
    
    cursor.execute(info_query)
    for row in cursor.fetchall():
        print(row)
    
    cursor.close()
    conn.close()
    
except pyodbc.Error as e:
    print(f"Error: {e}")