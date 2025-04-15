import pyodbc
import pandas as pd

DB_PARAMS = (
    "DRIVER={SQL Server};"
    "SERVER=Arc-PC;"
    "DATABASE=datacamp;"
    "Trusted_Connection=True;"
)

try:
    conn = pyodbc.connect(DB_PARAMS)
    cursor = conn.cursor()
    
    sql_script = """
    IF OBJECT_ID('dbo.Orders', 'U') IS NOT NULL
        DROP TABLE dbo.Orders;
    
    CREATE TABLE dbo.Orders (
        Orderid INTEGER,
        OrderDate DATETIME,
        territoryName NVARCHAR(255),
        YearOrdered INT,
        ExpectedDeliveryDate DATETIME,
        CustomerPurchaseOrderNumber INT,
        PickingCompletedWhen DATETIME,
        OrderPrice DECIMAL(18, 2)
    );
    """
    
    cursor.execute(sql_script)
    conn.commit()
    
    # Load CSV into DataFrame
    file_path = r"D:\\STUDY\\python\\Track_SQL_Server_Developer\\03_Course_Intermediate_SQL_Server\\datasets\\Orders.csv"
    df = pd.read_csv(file_path)
    
    # Insert data into SQL Server
    for index, row in df.iterrows():
        cursor.execute(
            "INSERT INTO dbo.Orders (Orderid, OrderDate, territoryName, YearOrdered, ExpectedDeliveryDate, CustomerPurchaseOrderNumber, PickingCompletedWhen, OrderPrice) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            row["Orderid"], row["OrderDate"], row["territoryName"], row["YearOrdered"], row["ExpectedDeliveryDate"], row["CustomerPurchaseOrderNumber"], row["PickingCompletedWhen"], row["OrderPrice"]
        )
    
    conn.commit()
    
    # Retrieve and print data
    info_query = """
    SELECT * FROM dbo.Orders;
    
    SELECT COLUMN_NAME, DATA_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'Orders' AND TABLE_SCHEMA = 'dbo';
    """
    
    cursor.execute(info_query)
    for row in cursor.fetchall():
        print(row)
    
    cursor.close()
    conn.close()
    
except pyodbc.Error as e:
    print(f"Error: {e}")