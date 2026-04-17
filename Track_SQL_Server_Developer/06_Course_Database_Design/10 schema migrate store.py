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
    IF OBJECT_ID('dbo.dim_store_star', 'U') IS NOT NULL
        DROP TABLE dbo.dim_store_star;
    
    CREATE TABLE dim_store_star (
        store_id INT PRIMARY KEY,
        store_address VARCHAR(255) NOT NULL,
        city VARCHAR(255) NOT NULL,
        state VARCHAR(255) NOT NULL,
        country VARCHAR(255) NOT NULL
    );

    """
    
    cursor.execute(sql_script)
    conn.commit()
    
    # Load CSV into DataFrame
    file_path = r"D:\\STUDY\\python\\Track_SQL_Server_Developer\\06_Course_Database_Design\\datasets\\dim_store_star.csv"
    df = pd.read_csv(file_path)
    
    # Insert data into SQL Server
    for index, row in df.iterrows():
        cursor.execute(
            "INSERT INTO dbo.dim_store_star(store_id,store_address,city,state,country)VALUES (?, ?, ?, ?, ?)",
            row["store_id"], row["store_address"], row["city"], row["state"], row["country"]
        )
    
    conn.commit()
    
    # Retrieve and print data
    info_query = """
    SELECT * FROM dbo.dim_store_star;
    
    SELECT COLUMN_NAME, DATA_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'dim_store_star' AND TABLE_SCHEMA = 'dbo';
    """
    
    cursor.execute(info_query)
    for row in cursor.fetchall():
        print(row)
    
    cursor.close()
    conn.close()
    
except pyodbc.Error as e:
    print(f"Error: {e}")