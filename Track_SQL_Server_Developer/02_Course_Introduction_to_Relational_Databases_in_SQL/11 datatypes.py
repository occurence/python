import psycopg2
import pandas as pd

DB_PARAMS = { "dbname": "datacamp", "user": "postgres", "password": "postgres", "host": "localhost", "port": "5432", }

try:
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()

    sql_script = """
    DROP TABLE IF EXISTS transactions;
    CREATE TABLE transactions (
        transaction_date date, 
        amount integer,
        fee text
    );

    INSERT INTO transactions (transaction_date, amount, fee) 
    VALUES 
        ('1999-01-08', 500, '20'),
        ('2001-02-20', 403, '15'),
        ('2001-03-20', 3430, '35');

    INSERT INTO transactions (transaction_date, amount, fee) 
    VALUES ('2018-09-24', 5454, '30');
    """
    cur.execute(sql_script)
    conn.commit()

    info_query = """
    SELECT * 
    FROM transactions;
    """
    cur.execute(info_query)
    
    # for row in cur.fetchall():
    #     print(row)
    rows = cur.fetchall()
    df = pd.DataFrame(rows, columns=["Transaction Date", "Amount", "Fee"])
    df["Transaction Date"] = df["Transaction Date"].astype(str)
    print(df.to_string(index=False))

    cur.close()
    conn.close()

except psycopg2.Error as e:
    print(f"Error: {e}")