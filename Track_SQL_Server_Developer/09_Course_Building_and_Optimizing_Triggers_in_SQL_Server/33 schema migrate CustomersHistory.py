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
    IF OBJECT_ID('dbo.CustomersHistory', 'U') IS NOT NULL
        DROP TABLE dbo.CustomersHistory;
    
    CREATE TABLE CustomersHistory (
        CustomerID int,
        Customer nvarchar(50),
        ContractID nvarchar(25),
        ContractDate date,
        Address nvarchar(100),
        PhoneNo nvarchar(25),
        Email nvarchar(100),
        ChangeDate date DEFAULT GETDATE()
    );
    """
    
    cursor.execute(sql_script)
    conn.commit()
    
    # # Load CSV into DataFrame
    # file_path = r"D:\\STUDY\\python\\Track_SQL_Server_Developer\\09_Course_Building_and_Optimizing_Triggers_in_SQL_Server\\datasets\\CustomersHistory.csv"
    # df = pd.read_csv(file_path)
    
    # # Insert data into SQL Server~
    # for index, row in df.iterrows():
    #     cursor.execute(
    #         "INSERT INTO dbo.CustomersHistory(CustomerID,Customer,ContractID,ContractDate,Address,PhoneNo,Email,ChangeDate) VALUES(?,?,?,?,?,?,?,?)",
    #         row["CustomerID"], row["Customer"], row["ContractID"], row["ContractDate"], row["Address"], row["PhoneNo"], row["Email"], row["ChangeDate"]
    #     )
    
    # conn.commit()
    
    # Retrieve and print data
    info_query = """
    SELECT * FROM dbo.CustomersHistory;
    
    SELECT COLUMN_NAME, DATA_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'CustomersHistory' AND TABLE_SCHEMA = 'dbo';
    """
    
    cursor.execute(info_query)
    for row in cursor.fetchall():
        print(row)
    
    cursor.close()
    conn.close()
    
except pyodbc.Error as e:
    print(f"Error: {e}")