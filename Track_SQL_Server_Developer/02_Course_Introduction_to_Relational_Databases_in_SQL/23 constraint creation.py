import psycopg2
import pandas as pd

DB_PARAMS = { "dbname": "datacamp", "user": "postgres", "password": "postgres", "host": "localhost", "port": "5432", }

try:
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()

    sql_script = """
    DROP TABLE IF EXISTS students;

    -- Create the table
    CREATE TABLE students (
    last_name VARCHAR(128) NOT NULL,
    ssn INTEGER PRIMARY KEY,
    phone_no CHAR(12)
    );
    """

    info_query = """
    SELECT *
    FROM students;
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