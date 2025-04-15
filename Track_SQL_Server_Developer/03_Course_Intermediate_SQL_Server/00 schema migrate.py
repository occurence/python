import psycopg2
import pandas as pd

DB_PARAMS = { "dbname": "datacamp", "user": "postgres", "password": "postgres", "host": "localhost", "port": "5432", }

try:
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()

    sql_script = """
    DROP TABLE IF EXISTS Incidents;
    -- Create a table for the university_professors entity type
    CREATE TABLE Incidents(
    -- IncidentDateTime datetime,
    IncidentDateTime timestamp,
    City varchar(255),
    IncidentState varchar(50),
    Country varchar(50),
    Shape varchar(50),
    DurationSeconds real,
    Comments varchar(255)
    );

    COPY Incidents(IncidentDateTime, City, IncidentState, Country, Shape, DurationSeconds, Comments)
    FROM 'D:\\STUDY\\python\\Track_SQL_Server_Developer\\03_Course_Intermediate_SQL_Server\\datasets\\Incidents.csv'
    DELIMITER ','
    CSV HEADER;
    """

    info_query = """
    -- Print the contents of this table
    SELECT * 
    FROM Incidents;

    -- Query the right table in information_schema to get columns
    SELECT column_name, data_type 
    FROM information_schema.columns 
    WHERE table_name = 'Incidents' AND table_schema = 'dbo';
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