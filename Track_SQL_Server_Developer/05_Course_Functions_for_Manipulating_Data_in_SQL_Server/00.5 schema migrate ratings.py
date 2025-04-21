import pyodbc
import pandas as pd

DB_PARAMS = (
    "DRIVER={SQL Server};"
    "SERVER=Arc-PC;"
    "DATABASE=datacamp;"
    "Trusted_Connection=True;"
)

try:
    conn = pyodbc.connect(DB_PARAMS)
    cursor = conn.cursor()
    
    sql_script = """
    IF OBJECT_ID('dbo.ratings', 'U') IS NOT NULL
        DROP TABLE dbo.ratings;
    
    CREATE TABLE ratings (
        company NVARCHAR(100) NOT NULL,
        bean_origin NVARCHAR(100),
        cocoa_percent DECIMAL(5,2) NOT NULL,
        company_location NVARCHAR(100) NOT NULL,
        rating DECIMAL(3,2) NOT NULL,
        bean_type NVARCHAR(50),
        broad_bean_origin NVARCHAR(100)
    );

    """
    
    cursor.execute(sql_script)
    conn.commit()
    
    # Load CSV into DataFrame
    file_path = r"D:\\STUDY\\python\\Track_SQL_Server_Developer\\05_Course_Functions_for_Manipulating_Data_in_SQL_Server\\datasets\\ratings.csv"
    df = pd.read_csv(file_path)

    # Insert data into SQL Server
    for index, row in df.iterrows():
        cursor.execute(
            "INSERT INTO dbo.ratings(company,bean_origin,cocoa_percent,company_location,rating,bean_type,broad_bean_origin)VALUES (?, ?, CAST(? AS DECIMAL(5,2)), ?, CAST(? AS DECIMAL(3,2)), ?, ?)",
            row["company"], row["bean_origin"], row["cocoa_percent"], row["company_location"], row["rating"], row["bean_type"] if pd.notna(row["bean_type"]) else None, row["broad_bean_origin"] if pd.notna(row["broad_bean_origin"]) else None
        )
    
    conn.commit()
    
    # Retrieve and print data
    info_query = """
    SELECT * FROM dbo.ratings;
    
    SELECT COLUMN_NAME, DATA_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'ratings' AND TABLE_SCHEMA = 'dbo';
    """
    
    cursor.execute(info_query)
    for row in cursor.fetchall():
        print(row)
    
    cursor.close()
    conn.close()
    
except pyodbc.Error as e:
    print(f"Error: {e}")