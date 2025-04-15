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
    IF OBJECT_ID('dbo.customers', 'U') IS NOT NULL
        DROP TABLE dbo.customers;
    
    CREATE TABLE customers (
        customer_id integer PRIMARY KEY,
        customer_name VARCHAR(128) NOT NULL,
        cars_rented VARCHAR(256),
        invoice_id VARCHAR(256),
        premium_member bit,
        salutation VARCHAR(128)
    );

    """
    
    cursor.execute(sql_script)
    conn.commit()
    
    # Load CSV into DataFrame
    file_path = r"D:\\STUDY\\python\\Track_SQL_Server_Developer\\06_Course_Database_Design\\datasets\\customers.csv"
    df = pd.read_csv(file_path)
    
    # Insert data into SQL Server
    for index, row in df.iterrows():
        cursor.execute(
            "INSERT INTO dbo.customers(customer_id,customer_name,cars_rented,invoice_id,premium_member,salutation) VALUES(?,?,?,?,?,?)",
            row["customer_id"], row["customer_name"], row["cars_rented"], row["invoice_id"], row["premium_member"], row["salutation"]
        )
    
    conn.commit()
    
    # Retrieve and print data
    info_query = """
    SELECT * FROM dbo.customers;
    
    SELECT COLUMN_NAME, DATA_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'customers' AND TABLE_SCHEMA = 'dbo';
    """
    
    cursor.execute(info_query)
    for row in cursor.fetchall():
        print(row)
    
    cursor.close()
    conn.close()
    
except pyodbc.Error as e:
    print(f"Error: {e}")