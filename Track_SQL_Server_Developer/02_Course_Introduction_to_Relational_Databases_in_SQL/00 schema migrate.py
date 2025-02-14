import psycopg2
import pandas as pd

DB_PARAMS = { "dbname": "datacamp", "user": "postgres", "password": "postgres", "host": "localhost", "port": "5432", }

try:
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()

    sql_script = """
    DROP TABLE IF EXISTS university_professors;
    -- Create a table for the university_professors entity type
    CREATE TABLE university_professors(
    firstname text,
    lastname text,
    university text,
    university_shortname text,
    university_city text,
    function text,
    organization text,
    organization_sector text
    );

    COPY university_professors(firstname, lastname, university, university_shortname, university_city, function, organization, organization_sector)
    FROM 'D:\\STUDY\\python\\Track_SQL_Server_Developer\\02_Course_Introduction_to_Relational_Databases_in_SQL\\datasets\\university_professors.csv'
    DELIMITER ','
    CSV HEADER;
    """

    info_query = """
    -- Print the contents of this table
    SELECT * 
    FROM university_professors;

    -- Query the right table in information_schema to get columns
    SELECT column_name, data_type 
    FROM information_schema.columns 
    WHERE table_name = 'university_professors' AND table_schema = 'dbo';
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