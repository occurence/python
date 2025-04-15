import psycopg2
import pandas as pd

DB_PARAMS = { "dbname": "datacamp", "user": "postgres", "password": "postgres", "host": "localhost", "port": "5432", }

try:
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()

    sql_script = """
    -- Add the id column
    ALTER TABLE cars
    ADD COLUMN id varchar(128);

    -- Update id with make + model
    UPDATE cars
    SET id = CONCAT(make, model);

    -- Make id a primary key
    ALTER TABLE cars
    ADD CONSTRAINT id_pk PRIMARY KEY(id);
    """

    info_query = """
    -- Count the number of distinct rows with columns make, model
    SELECT COUNT(DISTINCT(make, model)) 
    FROM cars;

    -- Have a look at the table
    SELECT * FROM cars;

    SELECT 
        tc.table_name,
        tc.constraint_name,
        tc.constraint_type,
        kcu.column_name
    FROM information_schema.table_constraints AS tc
    LEFT JOIN information_schema.key_column_usage AS kcu
        ON tc.constraint_name = kcu.constraint_name
        AND tc.table_name = kcu.table_name
    WHERE tc.table_name IN ('cars');
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