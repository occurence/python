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
    IF OBJECT_ID('dbo.Earthquakes', 'U') IS NOT NULL
        DROP TABLE dbo.Earthquakes;
    
    CREATE TABLE Earthquakes (
        Date nvarchar(255),
        Time nvarchar(255),
        latitude real,
        longitude real,
        depth real,
        magnitude real,
        place varchar(100),
        NearestPop varchar(30),
        Country varchar(2)
    );
    """
    
    cursor.execute(sql_script)
    conn.commit()
    
    # Load CSV into DataFrame
    file_path = r"D:\\STUDY\\python\\Track_SQL_Server_Developer\\10_Course_Improving_Query_Performance_in_SQL_Server\\datasets\\Earthquakes.csv"
    df = pd.read_csv(file_path)

    # Insert data into SQL Server
    for index, row in df.iterrows():
        cursor.execute(
            "INSERT INTO dbo.Earthquakes(Date,Time,latitude,longitude,depth,magnitude,place,NearestPop,Country) VALUES(?,?,?,?,?,?,?,?,?)",
            row["Date"], row["Time"], float(row["latitude"]), float(row["longitude"]), float(row["depth"]), float(row["magnitude"]), row["place"], 
            row["NearestPop"] if pd.notna(row["NearestPop"]) else None,
            row["Country"] if pd.notna(row["Country"]) else None
        )
    
    conn.commit()
    
    # Retrieve and print data
    info_query = """
    SELECT * FROM dbo.Earthquakes;
    
    SELECT COLUMN_NAME, DATA_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'Earthquakes' AND TABLE_SCHEMA = 'dbo';
    """
    
    cursor.execute(info_query)
    for row in cursor.fetchall():
        print(row)
    
    cursor.close()
    conn.close()
    
except pyodbc.Error as e:
    print(f"Error: {e}")