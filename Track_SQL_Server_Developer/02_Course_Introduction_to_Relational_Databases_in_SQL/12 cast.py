import psycopg2
import pandas as pd

DB_PARAMS = { "dbname": "datacamp", "user": "postgres", "password": "postgres", "host": "localhost", "port": "5432", }

try:
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()

    # sql_script = """
    # """
    # cur.execute(sql_script)
    # conn.commit()

    info_query = """
    -- Calculate the net amount as amount + fee
    SELECT transaction_date, amount + CAST(fee AS INT) AS net_amount 
    FROM transactions;
    """
    cur.execute(info_query)
    
    # for row in cur.fetchall():
    #     print(row)
    rows = cur.fetchall()
    df = pd.DataFrame(rows, columns=["Transaction Date", "net_amount"])
    df["Transaction Date"] = df["Transaction Date"].astype(str)
    print(df.to_string(index=False))


    cur.close()
    conn.close()

except psycopg2.Error as e:
    print(f"Error: {e}")