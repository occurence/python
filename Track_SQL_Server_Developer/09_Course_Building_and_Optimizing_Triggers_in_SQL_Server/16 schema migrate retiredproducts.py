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
    IF OBJECT_ID('dbo.retiredproducts', 'U') IS NOT NULL
        DROP TABLE dbo.retiredproducts;
    
    CREATE TABLE retiredproducts (
        Product nvarchar(50),
        Measure nvarchar(10),
        RetiredDate date DEFAULT GETDATE()
    );
    """
    
    cursor.execute(sql_script)
    conn.commit()
    
    # # Load CSV into DataFrame
    # file_path = r"D:\\STUDY\\python\\Track_SQL_Server_Developer\\09_Course_Building_and_Optimizing_Triggers_in_SQL_Server\\datasets\\retiredproducts.csv"
    # df = pd.read_csv(file_path)
    
    # # Insert data into SQL Server~
    # for index, row in df.iterrows():
    #     cursor.execute(
    #         "INSERT INTO dbo.RetiredProducts(Product,Measure,RetiredDate) VALUES(?,?,?)",
    #         row["Product"], row["Measure"], row["RetiredDate"]
    #     )
    
    # conn.commit()
    
    # Retrieve and print data
    info_query = """
    SELECT * FROM dbo.retiredproducts;
    
    SELECT COLUMN_NAME, DATA_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'retiredproducts' AND TABLE_SCHEMA = 'dbo';
    """
    
    cursor.execute(info_query)
    for row in cursor.fetchall():
        print(row)
    
    cursor.close()
    conn.close()
    
except pyodbc.Error as e:
    print(f"Error: {e}")