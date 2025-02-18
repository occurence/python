import psycopg2
import pandas as pd

DB_PARAMS = { "dbname": "postgres", "user": "postgres", "password": "postgres", "host": "localhost", "port": "5432", }

try:
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()

    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

    # Terminate all connections to the 'datacamp' database
    terminate_query = """
    SELECT pg_terminate_backend(pg_stat_activity.pid)
    FROM pg_stat_activity
    WHERE pg_stat_activity.datname = 'datacamp'
      AND pid <> pg_backend_pid();
    """

    cur.execute(terminate_query)
    conn.commit()

    sql_script_drop = """
    DROP DATABASE IF EXISTS datacamp;
    """

    # cur.execute(info_query)
    
    # for row in cur.fetchall():
    #     print(row)

    cur.execute("DROP DATABASE IF EXISTS datacamp;")
    cur.execute("CREATE DATABASE datacamp;")

    # cur.execute(info_query)
    
    # for row in cur.fetchall():
    #     print(row)

    cur.close()
    conn.close()

except psycopg2.Error as e:
    print(f"Error: {e}")