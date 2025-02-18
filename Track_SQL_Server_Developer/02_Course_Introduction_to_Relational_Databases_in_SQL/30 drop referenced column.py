import psycopg2
import pandas as pd

DB_PARAMS = { "dbname": "datacamp", "user": "postgres", "password": "postgres", "host": "localhost", "port": "5432", }

try:
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()

    sql_script = """
    -- Drop the firstname column
    ALTER TABLE affiliations
    DROP COLUMN firstname;

    -- Drop the lastname column
    ALTER TABLE affiliations
    DROP COLUMN lastname;
    """

    info_query = """
    -- Query the right table in information_schema to get columns
    SELECT column_name, data_type 
    FROM information_schema.columns 
    WHERE table_name = 'affiliations';
    """

    cur.execute(info_query)
    
    for row in cur.fetchall():
        print(row)

    cur.execute(sql_script)
    conn.commit()

    cur.execute(info_query)
    
    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()

except psycopg2.Error as e:
    print(f"Error: {e}")