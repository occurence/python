import psycopg2
import pandas as pd

DB_PARAMS = { "dbname": "datacamp", "user": "postgres", "password": "postgres", "host": "localhost", "port": "5432", }

try:
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()

    sql_script = """
    DROP TABLE IF EXISTS cars;
    -- Create a table for the cars entity type
    CREATE TABLE cars (
    make varchar(64) NOT NULL,
    model varchar(64) NOT NULL,
    mpg integer NOT NULL
    );

    COPY cars(make, model, mpg)
    FROM 'D:\\STUDY\\python\\Track_SQL_Server_Developer\\02_Course_Introduction_to_Relational_Databases_in_SQL\\datasets\\cars.csv'
    DELIMITER ','
    CSV HEADER;
    """

    info_query = """
    -- Print the contents of this table
    SELECT * 
    FROM cars;

    -- Query the right table in information_schema to get columns
    SELECT column_name, data_type 
    FROM information_schema.columns 
    WHERE table_name = 'cars';
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