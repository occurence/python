import psycopg2
import pandas as pd

DB_PARAMS = { "dbname": "datacamp", "user": "postgres", "password": "postgres", "host": "localhost", "port": "5432", }

try:
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()

    sql_script = """
    """

    info_query = """
    -- Count the total number of affiliations per university
    SELECT COUNT(*), professors.university_id 
    FROM affiliations
    JOIN professors
    ON affiliations.professor_id = professors.id
    -- Group by the university ids of professors
    GROUP BY professors.university_id 
    ORDER BY count DESC;
    """

    cur.execute(info_query)
    
    for row in cur.fetchall():
        print(row)

    # cur.execute(sql_script)
    # conn.commit()

    # cur.execute(info_query)
    
    # for row in cur.fetchall():
    #     print(row)

    cur.close()
    conn.close()

except psycopg2.Error as e:
    print(f"Error: {e}")