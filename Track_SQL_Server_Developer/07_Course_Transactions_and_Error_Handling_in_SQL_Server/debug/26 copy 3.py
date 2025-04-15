import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=tehandling;" "Trusted_Connection=True;", autocommit=True)
cursor = conn.cursor()

try:
    cursor.execute("SET XACT_ABORT ON; BEGIN TRAN;")
    
    # First INSERT
    cursor.execute("INSERT INTO customers VALUES ('Mark', 'Davis', 'markdavis@mail.com', '555909090');")
    
    # Second INSERT (This should fail if Dylan already exists)
    cursor.execute("INSERT INTO customers VALUES ('Dylan', 'Smith', 'dylansmith@mail.com', '555888999');")

    conn.commit()  # Commit only if all INSERTs succeed

except pyodbc.DatabaseError as e:
    print(f"Database Error: {e}")
    conn.rollback()  # Rollback if any error occurs
# finally:
#     cursor.close()
#     conn.close()

select_query = """
SELECT * FROM customers WHERE email IN('markdavis@mail.com', 'dylansmith@mail.com');
"""

cursor.execute(select_query)

results = []
while True:
    rows = cursor.fetchall()
    if not rows:
        break
    columns = [column[0] for column in cursor.description]
    df = pd.DataFrame.from_records(rows, columns=columns)
    results.append(df)
    if not cursor.nextset():
        break
    
for i, df in enumerate(results, start=1):
    print(f'{i} SELECT STATEMENT\n, {df}\n')

cursor.close()
conn.close()