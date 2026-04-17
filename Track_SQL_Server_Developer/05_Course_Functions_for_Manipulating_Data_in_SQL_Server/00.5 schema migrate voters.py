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
    IF OBJECT_ID('dbo.voters', 'U') IS NOT NULL
        DROP TABLE dbo.voters;
    
    CREATE TABLE voters (
        customer_id INT PRIMARY KEY,
        first_name VARCHAR(255) NOT NULL,
        last_name VARCHAR(255) NOT NULL,
        birthdate DATE NOT NULL,
        gender CHAR(1) CHECK(gender IN('M', 'F')) NOT NULL,
        email VARCHAR(255) NOT NULL,
        country VARCHAR(100) NOT NULL,
        first_vote_date DATE NOT NULL,
        total_votes INT NOT NULL
    );

    """
    
    cursor.execute(sql_script)
    conn.commit()
    
    # Load CSV into DataFrame
    file_path = r"D:\\STUDY\\python\\Track_SQL_Server_Developer\\05_Course_Functions_for_Manipulating_Data_in_SQL_Server\\datasets\\voters.csv"
    df = pd.read_csv(file_path)
    
    # Insert data into SQL Server
    for index, row in df.iterrows():
        cursor.execute(
            "INSERT INTO dbo.voters(customer_id,first_name,last_name,birthdate,gender,email,country,first_vote_date,total_votes)VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            row["customer_id"], row["first_name"], row["last_name"], row["birthdate"], row["gender"], row["email"], row["country"], row["first_vote_date"], row["total_votes"]
        )
    
    conn.commit()
    
    # Retrieve and print data
    info_query = """
    SELECT * FROM dbo.voters;
    
    SELECT COLUMN_NAME, DATA_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'voters' AND TABLE_SCHEMA = 'dbo';
    """
    
    cursor.execute(info_query)
    for row in cursor.fetchall():
        print(row)
    
    cursor.close()
    conn.close()
    
except pyodbc.Error as e:
    print(f"Error: {e}")