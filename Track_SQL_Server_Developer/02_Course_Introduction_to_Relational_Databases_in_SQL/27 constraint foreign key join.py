import psycopg2
import pandas as pd

DB_PARAMS = { "dbname": "datacamp", "user": "postgres", "password": "postgres", "host": "localhost", "port": "5432", }

try:
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()

    sql_script = """
    """

    info_query = """
    -- Select all professors working for universities in the city of Zurich
    SELECT professors.lastname, universities.id, universities.university_city
    FROM professors
    INNER JOIN universities
    ON professors.university_id = universities.id
    WHERE universities.university_city = 'Zurich'
    ORDER BY lastname ASC;-- 
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