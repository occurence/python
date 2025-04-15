import psycopg2
import pandas as pd

DB_PARAMS = { "dbname": "datacamp", "user": "postgres", "password": "postgres", "host": "localhost", "port": "5432", }

try:
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()

    sql_script = """
    """

    info_query = """
    -- Count the number of rows in universities
    SELECT COUNT(DISTINCT(university)) 
    FROM universities;

    -- Count the number of distinct values in the university_city column
    SELECT COUNT(DISTINCT(university_city)) 
    FROM universities;
    """

    cur.execute(info_query)
    
    for row in cur.fetchall():
        print(row)

    # cur.execute(sql_script)
    # conn.commit()

    cur.close()
    conn.close()

except psycopg2.Error as e:
    print(f"Error: {e}")