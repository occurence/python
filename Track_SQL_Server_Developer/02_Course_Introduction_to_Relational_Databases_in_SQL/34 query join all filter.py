import psycopg2
import pandas as pd

DB_PARAMS = { "dbname": "datacamp", "user": "postgres", "password": "postgres", "host": "localhost", "port": "5432", }

try:
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()

    sql_script = """
    """

    info_query = """
    -- Filter the table and sort it
    SELECT COUNT(*), organizations.organization_sector, 
    professors.id, universities.university_city
    FROM affiliations
    JOIN professors
    ON affiliations.professor_id = professors.id
    JOIN organizations
    ON affiliations.organization_id = organizations.id
    JOIN universities
    ON professors.university_id = universities.id
    WHERE organizations.organization_sector = 'Media & communication'
    GROUP BY organizations.organization_sector, 
    professors.id, universities.university_city
    ORDER BY COUNT DESC;
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