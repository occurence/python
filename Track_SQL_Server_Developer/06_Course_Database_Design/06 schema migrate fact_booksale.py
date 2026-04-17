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
    IF OBJECT_ID('dbo.fact_booksales', 'U') IS NOT NULL
        DROP TABLE dbo.fact_booksales;
    
    CREATE TABLE fact_booksales (
        sales_id INTEGER PRIMARY KEY,
        book_id INTEGER NOT NULL,
        store_id INTEGER NOT NULL,
        time_id INTEGER NOT NULL,
        sales_amount FLOAT NOT NULL,
        quantity INTEGER NOT NULL
    );

    """
    
    cursor.execute(sql_script)
    conn.commit()
    
    # Load CSV into DataFrame
    file_path = r"D:\\STUDY\\python\\Track_SQL_Server_Developer\\06_Course_Database_Design\\datasets\\fact_booksales.csv"
    df = pd.read_csv(file_path)
    
    # Insert data into SQL Server
    for index, row in df.iterrows():
        cursor.execute(
            "INSERT INTO dbo.fact_booksales(sales_id, book_id, store_id, time_id, sales_amount, quantity)VALUES (?, ?, ?, ?, ?, ?)",
            row["sales_id"], int(row["book_id"]), int(row["store_id"]), int(row["time_id"]), float(row["sales_amount"]), int(row["quantity"])
        )
    
    conn.commit()
    
    # Retrieve and print data
    info_query = """
    SELECT * FROM dbo.fact_booksales;
    
    SELECT COLUMN_NAME, DATA_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'fact_booksales' AND TABLE_SCHEMA = 'dbo';
    """
    
    cursor.execute(info_query)
    for row in cursor.fetchall():
        print(row)
    
    cursor.close()
    conn.close()
    
except pyodbc.Error as e:
    print(f"Error: {e}")