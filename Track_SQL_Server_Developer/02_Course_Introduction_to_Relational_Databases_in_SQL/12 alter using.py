import psycopg2
import pandas as pd

DB_PARAMS = { "dbname": "college", "user": "postgres", "password": "postgres", "host": "localhost", "port": "5432", }

try:
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()

    sql_script = """
    ALTER TABLE professors 
    ALTER COLUMN firstname 
    TYPE varchar(16)
    USING SUBSTRING(firstname, 1, 16);
    """

    info_query = """
    SELECT column_name, data_type 
    FROM information_schema.columns 
    WHERE table_name = 'professors';
    """

    cur.execute(sql_script)
    conn.commit()

    cur.execute(info_query)
    
    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()

except psycopg2.Error as e:
    print(f"Error: {e}")