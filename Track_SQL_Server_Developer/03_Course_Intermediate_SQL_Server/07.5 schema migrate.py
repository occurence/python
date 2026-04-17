import psycopg2
import pandas as pd

DB_PARAMS = { "dbname": "datacamp", "user": "postgres", "password": "postgres", "host": "localhost", "port": "5432", }

try:
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()

    sql_script = """
    DROP TABLE IF EXISTS Shipments;
    -- Create a table for the Shipments entity type
    CREATE TABLE Shipments(
    MixID VARCHAR(255),
    MixDesc VARCHAR(255),
    Plant INT,
    ShipDate TIMESTAMP,
    DeliveryWeight REAL,
    Cost NUMERIC(10,2),
    Quantity REAL,
    OrderDate TIMESTAMP,
    WeightValue REAL
    );

    COPY Shipments(MixID, MixDesc, Plant, ShipDate, DeliveryWeight, Cost, Quantity, OrderDate, WeightValue)
    FROM 'D:\\STUDY\\python\\Track_SQL_Server_Developer\\03_Course_Intermediate_SQL_Server\\datasets\\MixData.csv'
    DELIMITER ','
    CSV HEADER;
    """

    info_query = """
    -- Print the contents of this table
    SELECT * 
    FROM Shipments;

    -- Query the right table in information_schema to get columns
    SELECT column_name, data_type 
    FROM information_schema.columns 
    WHERE table_name = 'Shipments';
    """

    # cur.execute(info_query)
    
    # for row in cur.fetchall():
    #     print(row)

    cur.execute(sql_script)
    conn.commit()

    cur.execute(info_query)
    
    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()

except psycopg2.Error as e:
    print(f"Error: {e}")