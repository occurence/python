import psycopg2
import pandas as pd

DB_PARAMS = { "dbname": "datacamp", "user": "postgres", "password": "postgres", "host": "localhost", "port": "5432", }

try:
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()

    sql_script = """
    """

    info_query = """
    -- Try out different combinations
    SELECT COUNT(DISTINCT(firstname, lastname)) 
    FROM professors;
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