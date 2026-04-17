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
    IF OBJECT_ID('dbo.film', 'U') IS NOT NULL
        DROP TABLE dbo.film;
    
    CREATE TABLE film (
        film_id integer PRIMARY KEY,
        title text NOT NULL,
        long_description text,
        rental_duration smallint,
        rental_rate numeric,
        length smallint,
        replacement_cost numeric,
        rating VARCHAR(MAX),
        release_year integer
    );

    """
    
    cursor.execute(sql_script)
    conn.commit()
    
    # Load CSV into DataFrame
    file_path = r"D:\\STUDY\\python\\Track_SQL_Server_Developer\\06_Course_Database_Design\\datasets\\film.csv"
    df = pd.read_csv(file_path)
    
    # Insert data into SQL Server
    for index, row in df.iterrows():
        cursor.execute(
            "INSERT INTO dbo.film(film_id,title,long_description,rental_duration,rental_rate,length,replacement_cost,rating,release_year) VALUES(?,?,?,?,?,?,?,?,?)",
            row["film_id"], row["title"], row["long_description"], row["rental_duration"], row["rental_rate"], row["length"], row["replacement_cost"], row["rating"], row["release_year"]
        )
    
    conn.commit()
    
    # Retrieve and print data
    info_query = """
    SELECT * FROM dbo.film;
    
    SELECT COLUMN_NAME, DATA_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'film' AND TABLE_SCHEMA = 'dbo';
    """
    
    cursor.execute(info_query)
    for row in cursor.fetchall():
        print(row)
    
    cursor.close()
    conn.close()
    
except pyodbc.Error as e:
    print(f"Error: {e}")