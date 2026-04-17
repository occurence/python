import psycopg2
import pandas as pd

DB_PARAMS = { "dbname": "datacamp", "user": "postgres", "password": "postgres", "host": "localhost", "port": "5432", }

try:
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()

    sql_script = """
    -- Drop the right foreign key constraint
    ALTER TABLE affiliations
    DROP CONSTRAINT affiliations_organization_id_fkey;

    -- Add a new foreign key constraint from affiliations to organizations which cascades deletion
    ALTER TABLE affiliations
    ADD CONSTRAINT affiliations_organization_id_fkey FOREIGN KEY (organization_id) REFERENCES organizations (id) ON DELETE CASCADE;

    -- Delete an organization 
    DELETE FROM organizations 
    WHERE id = 'CUREM';
    """

    info_query = """
    -- Check an organization 
    SELECT * FROM organizations 
    WHERE id = 'CUREM';

    -- Check that no more affiliations with this organization exist
    SELECT * FROM affiliations
    WHERE organization_id = 'CUREM';

    -- Identify the correct constraint name
    SELECT constraint_name, table_name, constraint_type
    FROM information_schema.table_constraints
    WHERE constraint_type = 'FOREIGN KEY';
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