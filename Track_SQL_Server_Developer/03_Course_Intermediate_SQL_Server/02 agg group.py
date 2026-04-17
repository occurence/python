import psycopg2
import pandas as pd

DB_PARAMS = { "dbname": "datacamp", "user": "postgres", "password": "postgres", "host": "localhost", "port": "5432", }

try:
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()

    sql_script = """
    """

    info_query = """
    -- Calculate the aggregations by Shape
    SELECT Shape,
        AVG(DurationSeconds) AS Average, 
        MIN(DurationSeconds) AS Minimum, 
        MAX(DurationSeconds) AS Maximum
    FROM Incidents
    GROUP BY Shape
    -- Return records where minimum of DurationSeconds is greater than 1
    HAVING MIN(DurationSeconds) > 1
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