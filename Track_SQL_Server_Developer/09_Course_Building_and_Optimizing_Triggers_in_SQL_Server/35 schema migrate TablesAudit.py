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
    IF OBJECT_ID('dbo.TablesAudit', 'U') IS NOT NULL
        DROP TABLE dbo.TablesAudit;
    
    CREATE TABLE TablesAudit (
        TableName nvarchar(50),
        EventType nvarchar(50),
        UserAccount nvarchar(50),
        EventDate date DEFAULT GETDATE()
    );
    """
    
    cursor.execute(sql_script)
    conn.commit()
    
    # # Load CSV into DataFrame
    # file_path = r"D:\\STUDY\\python\\Track_SQL_Server_Developer\\09_Course_Building_and_Optimizing_Triggers_in_SQL_Server\\datasets\\TablesAudit.csv"
    # df = pd.read_csv(file_path)
    
    # # Insert data into SQL Server~
    # for index, row in df.iterrows():
    #     cursor.execute(
    #         "INSERT INTO dbo.TablesAudit(TableName,EventType,UserAccount,EventDate) VALUES(?,?,?,?)",
    #         row["TableName"], row["EventType"], row["UserAccount"], row["EventDate"]
    #     )
    
    # conn.commit()
    
    # Retrieve and print data
    info_query = """
    SELECT * FROM dbo.TablesAudit;
    
    SELECT COLUMN_NAME, DATA_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'TablesAudit' AND TABLE_SCHEMA = 'dbo';
    """
    
    cursor.execute(info_query)
    for row in cursor.fetchall():
        print(row)
    
    cursor.close()
    conn.close()
    
except pyodbc.Error as e:
    print(f"Error: {e}")