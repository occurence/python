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
    IF OBJECT_ID('dbo.reviews', 'U') IS NOT NULL
        DROP TABLE dbo.reviews;
    
    CREATE TABLE reviews (
        reviewid integer,
        title varchar(MAX),
        url varchar(MAX),
        score real,
        best_new_music integer,
        author varchar(MAX),
        author_type varchar(MAX),
        pub_date varchar(MAX),
        pub_weekday integer,
        pub_day integer,
        pub_month integer,
        pub_year integer
    );

    """
    
    cursor.execute(sql_script)
    conn.commit()
    
    # Load CSV into DataFrame
    file_path = r"D:\\STUDY\\python\\Track_SQL_Server_Developer\\06_Course_Database_Design\\datasets\\reviews.csv"
    df = pd.read_csv(file_path)
    
    # Insert data into SQL Server
    for index, row in df.iterrows():
        cursor.execute(
            "INSERT INTO dbo.reviews(reviewid,title,url,score,best_new_music,author,author_type,pub_date,pub_weekday,pub_day,pub_month,pub_year) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
            int(row["reviewid"]),row["title"] if pd.notna(row["title"]) else None,row["url"],float(row["score"]),int(row["best_new_music"]),row["author"],row["author_type"]  if pd.notna(row["author_type"]) else None,row["pub_date"],int(row["pub_weekday"]),int(row["pub_day"]),int(row["pub_month"]),int(row["pub_year"])
        )
    
    conn.commit()
    
    # Retrieve and print data
    info_query = """
    SELECT * FROM dbo.reviews;
    
    SELECT COLUMN_NAME, DATA_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'reviews' AND TABLE_SCHEMA = 'dbo';
    """
    
    cursor.execute(info_query)
    for row in cursor.fetchall():
        print(row)
    
    cursor.close()
    conn.close()
    
except pyodbc.Error as e:
    print(f"Error: {e}")