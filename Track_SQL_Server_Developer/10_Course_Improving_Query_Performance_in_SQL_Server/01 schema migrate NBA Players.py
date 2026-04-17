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
    IF OBJECT_ID('dbo.Players', 'U') IS NOT NULL
        DROP TABLE dbo.Players;
    
    CREATE TABLE Players (
        PlayerName varchar(50),
        Age int,
        Height_cm real,
        Weight_kg real,
        Country varchar(30),
        College varchar(50),
        DraftYear int,
        DraftRound int,
        DraftNumber int
    );
    """
    
    cursor.execute(sql_script)
    conn.commit()
    
    # Load CSV into DataFrame
    file_path = r"D:\\STUDY\\python\\Track_SQL_Server_Developer\\10_Course_Improving_Query_Performance_in_SQL_Server\\datasets\\Players.csv"
    df = pd.read_csv(file_path)

    # Insert data into SQL Server
    for index, row in df.iterrows():
        cursor.execute(
            "INSERT INTO dbo.Players(PlayerName,Age,Height_cm,Weight_kg,Country,College,DraftYear,DraftRound,DraftNumber) VALUES(?,?,?,?,?,?,?,?,?)",
            row["PlayerName"], row["Age"], float(row["Height_cm"]), float(row["Weight_kg"]), row["Country"],
            row["College"] if pd.notna(row["College"]) else None,
            row["DraftYear"] if pd.notna(row["DraftYear"]) else None, 
            row["DraftRound"] if pd.notna(row["DraftRound"]) else None, 
            row["DraftNumber"] if pd.notna(row["DraftNumber"]) else None
        )
    
    conn.commit()
    
    # Retrieve and print data
    info_query = """
    SELECT * FROM dbo.Players;
    
    SELECT COLUMN_NAME, DATA_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'Players' AND TABLE_SCHEMA = 'dbo';
    """
    
    cursor.execute(info_query)
    for row in cursor.fetchall():
        print(row)
    
    cursor.close()
    conn.close()
    
except pyodbc.Error as e:
    print(f"Error: {e}")