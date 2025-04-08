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
    IF OBJECT_ID('dbo.DatabaseAudit', 'U') IS NOT NULL
        DROP TABLE dbo.DatabaseAudit;
    
    CREATE TABLE DatabaseAudit (
        LogID int NOT NULL,
        EventType nvarchar(50),
        DatabaseName nvarchar(50),
        SchemaName nvarchar(50),
        Object nvarchar(100),
        ObjectType nvarchar(50),
        UserAccount nvarchar(100),
        Query nvarchar(-1),
        EventTime datetime
    );
    """
    
    cursor.execute(sql_script)
    conn.commit()
    
    # # Load CSV into DataFrame
    # file_path = r"D:\\STUDY\\python\\Track_SQL_Server_Developer\\09_Course_Building_and_Optimizing_Triggers_in_SQL_Server\\datasets\\DatabaseAudit.csv"
    # df = pd.read_csv(file_path)
    
    # # Insert data into SQL Server~
    # for index, row in df.iterrows():
    #     cursor.execute(
    #         "INSERT INTO dbo.DatabaseAudit(LogID,EventType,DatabaseName,SchemaName,Object,ObjectType,UserAccount,Query,EventTime) VALUES(?,?,?,?,?,?,?,?,?)",
    #         row["LogID"], row["EventType"], row["DatabaseName"], row["SchemaName"], row["Object"], row["ObjectType"], row["UserAccount"], row["Query"], row["EventTime"]
    #     )
    
    # conn.commit()
    
    # Retrieve and print data
    info_query = """
    SELECT * FROM dbo.DatabaseAudit;
    
    SELECT COLUMN_NAME, DATA_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'DatabaseAudit' AND TABLE_SCHEMA = 'dbo';
    """
    
    cursor.execute(info_query)
    for row in cursor.fetchall():
        print(row)
    
    cursor.close()
    conn.close()
    
except pyodbc.Error as e:
    print(f"Error: {e}")