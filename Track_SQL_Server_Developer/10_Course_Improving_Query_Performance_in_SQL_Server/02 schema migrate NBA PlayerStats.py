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
    IF OBJECT_ID('dbo.PlayerStats', 'U') IS NOT NULL
        DROP TABLE dbo.PlayerStats;
    
    CREATE TABLE PlayerStats (
        PlayerName varchar(50),
        Team varchar(3),
        Position varchar(2),
        GamesPlayed int,
        MinutesPlayed int,
        Points3 int,
        Points2 int,
        ORebound int,
        DRebound int,
        Assists int,
        Steals int,
        Blocks int,
        TurnOvers int,
        TotalPoints int
    );
    """
    
    cursor.execute(sql_script)
    conn.commit()
    
    # Load CSV into DataFrame
    file_path = r"D:\\STUDY\\python\\Track_SQL_Server_Developer\\10_Course_Improving_Query_Performance_in_SQL_Server\\datasets\\PlayerStats.csv"
    df = pd.read_csv(file_path)

    # Insert data into SQL Server
    for index, row in df.iterrows():
        cursor.execute(
            "INSERT INTO dbo.PlayerStats(PlayerName,Team,Position,GamesPlayed,MinutesPlayed,Points3,Points2,ORebound,DRebound,Assists,Steals,Blocks,TurnOvers,TotalPoints) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            row["PlayerName"], row["Team"], row["Position"], row["GamesPlayed"], row["MinutesPlayed"], row["Points3"], row["Points2"], row["ORebound"], row["DRebound"], row["Assists"], row["Steals"], row["Blocks"], row["TurnOvers"], row["TotalPoints"]
        )
    
    conn.commit()
    
    # Retrieve and print data
    info_query = """
    SELECT * FROM dbo.PlayerStats;
    
    SELECT COLUMN_NAME, DATA_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'PlayerStats' AND TABLE_SCHEMA = 'dbo';
    """
    
    cursor.execute(info_query)
    for row in cursor.fetchall():
        print(row)
    
    cursor.close()
    conn.close()
    
except pyodbc.Error as e:
    print(f"Error: {e}")