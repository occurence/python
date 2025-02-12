import psycopg2
import pandas as pd

DB_PARAMS = { "dbname": "college", "user": "postgres", "password": "postgres", "host": "localhost", "port": "5432", }

try:
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()

    sql_script_char = """
    -- Specify the correct fixed-length character type
    ALTER TABLE professors
    ALTER COLUMN university_shortname
    TYPE CHAR(3);
    """

    sql_script_varchar = """
    -- Change the type of firstname
    ALTER TABLE professors
    ALTER COLUMN firstname
    TYPE VARCHAR(64);
    """

    info_query = """
    SELECT column_name, data_type 
    FROM information_schema.columns 
    WHERE table_name = 'professors';
    """

    cur.execute(sql_script_char)
    conn.commit()

    cur.execute(info_query)
    
    for row in cur.fetchall():
        print(row)

    cur.execute(sql_script_varchar)
    conn.commit()

    cur.execute(info_query)
    
    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()

except psycopg2.Error as e:
    print(f"Error: {e}")