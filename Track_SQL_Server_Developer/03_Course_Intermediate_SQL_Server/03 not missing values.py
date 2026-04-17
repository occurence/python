import psycopg2
import pandas as pd

DB_PARAMS = { "dbname": "datacamp", "user": "postgres", "password": "postgres", "host": "localhost", "port": "5432", }

try:
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()

    sql_script = """
    """

    info_query = """
    -- Return the specified columns
    SELECT IncidentDateTime, IncidentState
    FROM Incidents
    -- Exclude all the missing values from IncidentState  
    WHERE IncidentState IS NOT NULL
    """

    # cur.execute(sql_script)
    # conn.commit()

    cur.execute(info_query)
    
    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()

except psycopg2.Error as e:
    print(f"Error: {e}")