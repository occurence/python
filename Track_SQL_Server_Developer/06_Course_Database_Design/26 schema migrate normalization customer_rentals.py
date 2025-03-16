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
    IF OBJECT_ID('dbo.customer_rentals', 'U') IS NOT NULL
        DROP TABLE dbo.customer_rentals;
    
    CREATE TABLE customer_rentals (
        -- customer_id integer PRIMARY KEY,
        -- car_id VARCHAR(128) PRIMARY KEY,
        -- start_date date PRIMARY KEY,
        customer_id integer,
        car_id VARCHAR(128),
        start_date date,
        end_date date NOT NULL,
        model VARCHAR(128) NOT NULL,
        manufacturer VARCHAR(128) NOT NULL,
        type_car VARCHAR(128) NOT NULL,
        condition VARCHAR(128) NOT NULL,
        color VARCHAR(128) NOT NULL,
        PRIMARY KEY(customer_id, car_id,start_date)
    );

    """
    
    cursor.execute(sql_script)
    conn.commit()
    
    # Load CSV into DataFrame
    file_path = r"D:\\STUDY\\python\\Track_SQL_Server_Developer\\06_Course_Database_Design\\datasets\\customer_rentals.csv"
    df = pd.read_csv(file_path)
    
    # Insert data into SQL Server
    for index, row in df.iterrows():
        cursor.execute(
            "INSERT INTO dbo.customer_rentals(customer_id,car_id,start_date,end_date,model,manufacturer,type_car,condition,color) VALUES(?,?,?,?,?,?,?,?,?)",
            row["customer_id"], row["car_id"], row["start_date"], row["end_date"], row["model"], row["manufacturer"], row["type_car"], row["condition"], row["color"]
        )
    
    conn.commit()
    
    # Retrieve and print data
    info_query = """
    SELECT * FROM dbo.customer_rentals;
    
    SELECT COLUMN_NAME, DATA_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'customer_rentals' AND TABLE_SCHEMA = 'dbo';
    """
    
    cursor.execute(info_query)
    for row in cursor.fetchall():
        print(row)
    
    cursor.close()
    conn.close()
    
except pyodbc.Error as e:
    print(f"Error: {e}")