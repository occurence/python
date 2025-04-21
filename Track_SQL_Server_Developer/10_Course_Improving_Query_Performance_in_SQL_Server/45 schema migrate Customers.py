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
    IF OBJECT_ID('dbo.Customers2', 'U') IS NOT NULL
        DROP TABLE dbo.Customers2;
    
    CREATE TABLE Customers2 (
        CustomerID varchar(5),
        CompanyName varchar(40),
        ContactName varchar(30),
        ContactTitle nvarchar(30),
        Address varchar(60),
        City varchar(15),
        Region varchar(15),
        PostalCode varchar(10),
        Country varchar(15),
        Phone varchar(24),
        Fax varchar(24)
    );
    """
    
    cursor.execute(sql_script)
    conn.commit()
    
    # Load CSV into DataFrame
    file_path = r"D:\\STUDY\\python\\Track_SQL_Server_Developer\\10_Course_Improving_Query_Performance_in_SQL_Server\\datasets\\Customers.csv"
    df = pd.read_csv(file_path)
    
    # Insert data into SQL Server
    for index, row in df.iterrows():
        cursor.execute(
            "INSERT INTO dbo.Customers2(CustomerID,CompanyName,ContactName,ContactTitle,Address,City,Region,PostalCode,Country,Phone,Fax) VALUES(?,?,?,?,?,?,?,?,?,?,?)",
            row["CustomerID"], row["CompanyName"], row["ContactName"], row["ContactTitle"], row["Address"], row["City"], 
            row["Region"] if pd.notna(row["Region"]) else None, 
            row["PostalCode"] if pd.notna(row["PostalCode"]) else None, 
            row["Country"], row["Phone"], 
            row["Fax"] if pd.notna(row["Fax"]) else None
        )
    
    conn.commit()
    
    # Retrieve and print data
    info_query = """
    SELECT * FROM dbo.Customers2;
    
    SELECT COLUMN_NAME, DATA_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'Customers2' AND TABLE_SCHEMA = 'dbo';
    """
    
    cursor.execute(info_query)
    for row in cursor.fetchall():
        print(row)
    
    cursor.close()
    conn.close()
    
except pyodbc.Error as e:
    print(f"Error: {e}")