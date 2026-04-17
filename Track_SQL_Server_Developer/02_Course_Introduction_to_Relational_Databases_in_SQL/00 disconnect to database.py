import psycopg2
import pandas as pd

DB_PARAMS = { "dbname": "datacamp", "user": "postgres", "password": "postgres", "host": "localhost", "port": "5432", }

try:
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()

    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

    sql_script = """
    -- SELECT pg_terminate_backend(procpid) FROM pg_stat_activity WHERE datname = 'datacamp';
    SELECT pg_terminate_backend(PID) FROM pg_stat_activity WHERE datname = 'datacamp';
    """

    info_query = """
    """

    # cur.execute(info_query)
    
    # for row in cur.fetchall():
    #     print(row)

    cur.execute(sql_script)
    conn.commit()

    # cur.execute(info_query)
    
    # for row in cur.fetchall():
    #     print(row)

    cur.close()
    conn.close()

except psycopg2.Error as e:
    print(f"Error: {e}")