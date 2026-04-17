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
    IF OBJECT_ID('dbo.dim_book_sf', 'U') IS NOT NULL
        DROP TABLE dbo.dim_book_sf;
    
    CREATE TABLE dim_book_sf (
        book_id INT PRIMARY KEY,
        title VARCHAR(256) NOT NULL,
        author_id INT NOT NULL,
        publisher_id INT NOT NULL,
        genre_id INT NOT NULL,
    );

    """
    
    cursor.execute(sql_script)
    conn.commit()
    
    # Load CSV into DataFrame
    file_path = r"D:\\STUDY\\python\\Track_SQL_Server_Developer\\06_Course_Database_Design\\datasets\\dim_book_sf.csv"
    df = pd.read_csv(file_path)
    
    # Insert data into SQL Server
    for index, row in df.iterrows():
        cursor.execute(
            "INSERT INTO dbo.dim_book_sf(book_id,title,author_id,publisher_id,genre_id)VALUES (?,?,?,?,?)",
            row["book_id"], row["title"], row["author_id"], row["publisher_id"], row["genre_id"]
        )
    
    conn.commit()
    
    # Retrieve and print data
    info_query = """
    SELECT * FROM dbo.dim_book_sf;
    
    SELECT COLUMN_NAME, DATA_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'dim_book_sf' AND TABLE_SCHEMA = 'dbo';
    """
    
    cursor.execute(info_query)
    for row in cursor.fetchall():
        print(row)
    
    cursor.close()
    conn.close()
    
except pyodbc.Error as e:
    print(f"Error: {e}")