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
    IF OBJECT_ID('dbo.cancelledorders', 'U') IS NOT NULL
        DROP TABLE dbo.cancelledorders;
    
    CREATE TABLE cancelledorders (
        OrderID int,
        Customer nvarchar(50),
        Product nvarchar(50),
        Price decimal,
        Currency nvarchar(3),
        Quantity int,
        WithDiscount int,
        Discount int,
        OrderDate date,
        TotalAmount decimal,
        Dispatched int
    );
    """
    
    cursor.execute(sql_script)
    conn.commit()
    
    # # Load CSV into DataFrame
    # file_path = r"D:\\STUDY\\python\\Track_SQL_Server_Developer\\09_Course_Building_and_Optimizing_Triggers_in_SQL_Server\\datasets\\cancelledorders.csv"
    # df = pd.read_csv(file_path)
    
    # # Insert data into SQL Server~
    # for index, row in df.iterrows():
    #     cursor.execute(
    #         "INSERT INTO dbo.CanceledOrders(OrderID,Customer,Product,Price,Currency,Quantity,WithDiscount,Discount,OrderDate,TotalAmount,Dispatched) VALUES(?,?,?,?,?,?,?,?,?,?,?)",
    #         row["OrderID"], row["Customer"], row["Product"], row["Price"], row["Currency"], row["Quantity"], row["WithDiscount"], row["Discount"], row["OrderDate"], row["TotalAmount"], row["Dispatched"]
    #     )
    
    # conn.commit()
    
    # Retrieve and print data
    info_query = """
    SELECT * FROM dbo.cancelledorders;
    
    SELECT COLUMN_NAME, DATA_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'cancelledorders' AND TABLE_SCHEMA = 'dbo';
    """
    
    cursor.execute(info_query)
    for row in cursor.fetchall():
        print(row)
    
    cursor.close()
    conn.close()
    
except pyodbc.Error as e:
    print(f"Error: {e}")