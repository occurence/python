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
    IF OBJECT_ID('dbo.saleswithoutprice', 'U') IS NOT NULL
        DROP TABLE dbo.saleswithoutprice;
    
    CREATE TABLE saleswithoutprice (
        OrderID int IDENTITY(1,1) NOT NULL,
        Customer nvarchar(50),
        Product nvarchar(50),
        Quantity int,
        OrderDate date DEFAULT GETDATE(),
        TotalAmount decimal,
        Currency nvarchar(3)
    );
    """
    
    cursor.execute(sql_script)
    conn.commit()
    
    # # Load CSV into DataFrame
    # file_path = r"D:\\STUDY\\python\\Track_SQL_Server_Developer\\09_Course_Building_and_Optimizing_Triggers_in_SQL_Server\\datasets\\saleswithoutprice.csv"
    # df = pd.read_csv(file_path)
    
    # # Insert data into SQL Server~
    # for index, row in df.iterrows():
    #     cursor.execute(
    #         "INSERT INTO dbo.SalesWithoutPrice(OrderID,Customer,Product,Quantity,OrderDate,TotalAmount,Currency) VALUES(?,?,?,?,?,?,?)",
    #         row["OrderID"], row["Customer"], row["Product"], row["Quantity"], row["OrderDate"], row["TotalAmount"], row["Currency"]
    #     )
    
    # conn.commit()
    
    # Retrieve and print data
    info_query = """
    SELECT * FROM dbo.saleswithoutprice;
    
    SELECT COLUMN_NAME, DATA_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'saleswithoutprice' AND TABLE_SCHEMA = 'dbo';
    """
    
    cursor.execute(info_query)
    for row in cursor.fetchall():
        print(row)
    
    cursor.close()
    conn.close()
    
except pyodbc.Error as e:
    print(f"Error: {e}")