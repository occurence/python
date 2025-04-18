import psycopg2
import pandas as pd

DB_PARAMS = { "dbname": "datacamp", "user": "postgres", "password": "postgres", "host": "localhost", "port": "5432", }

try:
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()

    sql_script = """
    -- Insert unique affiliations into the new table
    INSERT INTO affiliations 
    SELECT DISTINCT firstname, lastname, function, organization 
    FROM university_professors;
    """

    info_query = """
    -- Print the contents of this table
    SELECT * 
    FROM affiliations;

    -- Query the right table in information_schema to get columns
    SELECT column_name, data_type 
    FROM information_schema.columns 
    WHERE table_name = 'affiliations' AND table_schema = 'dbo';
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