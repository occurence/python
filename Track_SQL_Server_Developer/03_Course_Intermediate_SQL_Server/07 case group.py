import psycopg2
import pandas as pd

DB_PARAMS = { "dbname": "datacamp", "user": "postgres", "password": "postgres", "host": "localhost", "port": "5432", }

try:
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()

    sql_script = """
    """

    info_query = """
    -- Complete the syntax for cutting the duration into different cases
    SELECT DurationSeconds, 
    -- Start with the 2 TSQL keywords, and after the condition a TSQL word and a value
        CASE WHEN (DurationSeconds <= 120) THEN 1
    -- The pattern repeats with the same keyword and after the condition the same word and next value          
        WHEN (DurationSeconds > 120 AND DurationSeconds <= 600) THEN 2
    -- Use the same syntax here             
        WHEN (DurationSeconds > 601 AND DurationSeconds <= 1200) THEN 3
    -- Use the same syntax here               
        WHEN (DurationSeconds > 1201 AND DurationSeconds <= 5000) THEN 4
    -- Specify a value      
        ELSE 5 
        END AS SecondGroup   
    FROM Incidents
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