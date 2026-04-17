import psycopg2
import pandas as pd

DB_PARAMS = { "dbname": "datacamp", "user": "postgres", "password": "postgres", "host": "localhost", "port": "5432", }

try:
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()

    sql_script = """
    -- Update professor_id to professors.id where firstname, lastname correspond to rows in professors
    UPDATE affiliations
    SET professor_id = professors.id
    FROM professors
    WHERE affiliations.firstname = professors.firstname AND affiliations.lastname = professors.lastname;
    """

    info_query = """
    -- Have a look at the 10 first rows of affiliations again
    -- SELECT * FROM affiliations LIMIT 10;
    SELECT * FROM affiliations ORDER BY firstname, lastname LIMIT 10;
    SELECT COUNT(*) FROM affiliations WHERE professor_id IS NULL;
    """

    cur.execute(info_query)
    
    for row in cur.fetchall():
        print(row)

    cur.execute(sql_script)
    conn.commit()

    cur.execute(info_query)
    
    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()

except psycopg2.Error as e:
    print(f"Error: {e}")