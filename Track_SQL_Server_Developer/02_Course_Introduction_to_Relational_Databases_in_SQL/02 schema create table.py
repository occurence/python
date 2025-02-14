import psycopg2
import pandas as pd

DB_PARAMS = { "dbname": "datacamp", "user": "postgres", "password": "postgres", "host": "localhost", "port": "5432", }

try:
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()

    sql_script = """
    DROP TABLE IF EXISTS professors;
    -- Create a table for the professors entity type
    CREATE TABLE professors(
    firstname text,
    lastname text
    );

    DROP TABLE IF EXISTS universities;
    -- Create a table for the universities entity type
    CREATE TABLE universities(
      university_shortname text,
      university text,
      university_city text
    );

    DROP TABLE IF EXISTS organizations;
    -- Create a table for the organizations entity type
    CREATE TABLE organizations(
      organization text,
      organization_sector text
    );

    DROP TABLE IF EXISTS affiliations;
    -- Create a table for the affiliations entity type
    CREATE TABLE affiliations(
      firstname text,
      lastname text,
      university_shortname text,
      function text,
      organisation text
    );
    """

    info_query = """
    -- Print the contents of this table
    SELECT * 
    FROM professors;

    -- Print the contents of this table
    SELECT * 
    FROM universities;

    -- Print the contents of this table
    SELECT * 
    FROM organizations;

    -- Print the contents of this table
    SELECT *
    FROM affiliations;
    """

    # cur.execute(info_query)
    
    # for row in cur.fetchall():
    #     print(row)

    cur.execute(sql_script)
    conn.commit()

    cur.execute(info_query)
    
    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()

except psycopg2.Error as e:
    print(f"Error: {e}")