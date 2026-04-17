import psycopg2
import pandas as pd

DB_PARAMS = { "dbname": "datacamp", "user": "postgres", "password": "postgres", "host": "localhost", "port": "5432", }

try:
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()

    sql_script = """
    -- Rename the university_shortname column
    ALTER TABLE professors
    RENAME COLUMN university_shortname TO university_id;

    -- Add a foreign key on professors referencing universities
    ALTER TABLE professors 
    ADD CONSTRAINT professors_fkey FOREIGN KEY (university_id) REFERENCES universities (id);
    """

    info_query = """
    -- Have a look at the table
    SELECT * FROM professors;

    SELECT 
        tc.table_name,
        tc.constraint_name,
        tc.constraint_type,
        kcu.column_name
    FROM information_schema.table_constraints AS tc
    LEFT JOIN information_schema.key_column_usage AS kcu
        ON tc.constraint_name = kcu.constraint_name
        AND tc.table_name = kcu.table_name
    WHERE tc.table_name IN ('professors');
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