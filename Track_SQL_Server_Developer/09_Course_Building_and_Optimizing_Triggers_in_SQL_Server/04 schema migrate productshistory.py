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
    IF OBJECT_ID('dbo.productshistory', 'U') IS NOT NULL
        DROP TABLE dbo.productshistory;
    
    CREATE TABLE productshistory (
        Product nvarchar(50),
        Price decimal,
        Currency nvarchar(3),
        FirstAdded date
    );
    """
    
    cursor.execute(sql_script)
    conn.commit()
    
    # Load CSV into DataFrame
    file_path = r"D:\\STUDY\\python\\Track_SQL_Server_Developer\\09_Course_Building_and_Optimizing_Triggers_in_SQL_Server\\datasets\\productshistory.csv"
    df = pd.read_csv(file_path)
    
    # Insert data into SQL Server~
    for index, row in df.iterrows():
        cursor.execute(
            "INSERT INTO dbo.ProductsHistory(Product,Price,Currency,FirstAdded) VALUES(?,?,?,?)",
            row["Product"], row["Price"], row["Currency"], row["FirstAdded"]
        )
    
    conn.commit()
    
    # Retrieve and print data
    info_query = """
    SELECT * FROM dbo.productshistory;
    
    SELECT COLUMN_NAME, DATA_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'productshistory' AND TABLE_SCHEMA = 'dbo';
    """
    
    cursor.execute(info_query)
    for row in cursor.fetchall():
        print(row)
    
    cursor.close()
    conn.close()
    
except pyodbc.Error as e:
    print(f"Error: {e}")