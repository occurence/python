import psycopg2
import pandas as pd

DB_PARAMS = { "dbname": "college", "user": "postgres", "password": "postgres", "host": "localhost", "port": "5432", }

try:
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()

    sql_script = """
    -- Rename the organization column to id
    ALTER TABLE organizations
    RENAME COLUMN organization TO id;

    -- Make id a primary key
    ALTER TABLE organizations
    ADD CONSTRAINT organization_pk PRIMARY KEY (id);

    -- Rename the university_shortname column to id
    ALTER TABLE universities
    RENAME COLUMN university_shortname TO id;

    -- Make id a primary key
    ALTER TABLE universities
    ADD CONSTRAINT university_pk PRIMARY KEY (id);
    """

    info_query = """
    SELECT column_name, data_type
    FROM information_schema.columns 
    WHERE table_name IN ('organizations', 'universities');

    SELECT 
        tc.table_name,
        tc.constraint_name,
        tc.constraint_type,
        kcu.column_name
    FROM information_schema.table_constraints AS tc
    LEFT JOIN information_schema.key_column_usage AS kcu
        ON tc.constraint_name = kcu.constraint_name
        AND tc.table_name = kcu.table_name
    WHERE tc.table_name IN ('professors', 'universities', 'organizations', 'affiliations');
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