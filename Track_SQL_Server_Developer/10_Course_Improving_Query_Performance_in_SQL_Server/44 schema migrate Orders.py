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
    IF OBJECT_ID('dbo.Orders2', 'U') IS NOT NULL
        DROP TABLE dbo.Orders2;
    
    CREATE TABLE Orders2 (
        OrderID int,
        CustomerID varchar(5),
        EmployeeID int,
        OrderDate varchar(12),
        RequiredDate varchar(12),
        ShippedDate varchar(12),
        ShipVia int,
        Freight float,
        ShipName varchar(40),
        ShipAddress varchar(60),
        ShipCity varchar(15),
        ShipRegion varchar(15),
        ShipPostalCode varchar(10),
        ShipCountry varchar(15)
    );
    """
    
    cursor.execute(sql_script)
    conn.commit()
    
    # Load CSV into DataFrame
    file_path = r"D:\\STUDY\\python\\Track_SQL_Server_Developer\\10_Course_Improving_Query_Performance_in_SQL_Server\\datasets\\Orders.csv"
    df = pd.read_csv(file_path)
    
    # Insert data into SQL Server
    for index, row in df.iterrows():
        cursor.execute(
            "INSERT INTO dbo.Orders2(OrderID,CustomerID,EmployeeID,OrderDate,RequiredDate,ShippedDate,ShipVia,Freight,ShipName,ShipAddress,ShipCity,ShipRegion,ShipPostalCode,ShipCountry) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            row["OrderID"], row["CustomerID"], row["EmployeeID"], row["OrderDate"], row["RequiredDate"], 
            row["ShippedDate"] if pd.notna(row["ShippedDate"]) else None, 
            row["ShipVia"], row["Freight"], row["ShipName"], row["ShipAddress"], row["ShipCity"], 
            row["ShipRegion"] if pd.notna(row["ShipRegion"]) else None, 
            row["ShipPostalCode"] if pd.notna(row["ShipPostalCode"]) else None, 
            row["ShipCountry"]
        )
    
    conn.commit()
    
    # Retrieve and print data
    info_query = """
    SELECT * FROM dbo.Orders2;
    
    SELECT COLUMN_NAME, DATA_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'Orders2' AND TABLE_SCHEMA = 'dbo';
    """
    
    cursor.execute(info_query)
    for row in cursor.fetchall():
        print(row)
    
    cursor.close()
    conn.close()
    
except pyodbc.Error as e:
    print(f"Error: {e}")