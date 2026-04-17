import psycopg2
import pandas as pd

DB_PARAMS = { "dbname": "datacamp", "user": "postgres", "password": "postgres", "host": "localhost", "port": "5432", }

try:
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()

    sql_script = """
    """

    info_query = """
    -- Check the IncidentState column for missing values and replace them with the City column
    -- SELECT IncidentState, ISNULL(IncidentState, City) AS Location
    SELECT IncidentState, COALESCE(IncidentState, City) AS Location
    FROM Incidents
    -- Filter to only return missing values from IncidentState
    WHERE IncidentState IS NULL
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