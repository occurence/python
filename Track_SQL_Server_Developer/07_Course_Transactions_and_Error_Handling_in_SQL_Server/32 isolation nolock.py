import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=tehandling;" "Trusted_Connection=True;" )
cursor = conn.cursor()

# cursor.execute("""
# """)

# if cursor.nextset():
#     message_row = cursor.fetchone()
#     if message_row:
#         print(f'Message: {message_row[0]}')
# else:
#     print(f'No message returned')
# conn.commit()

select_query = """
SELECT *
	-- Avoid being blocked
	FROM transactions WITH (NOLOCK)
WHERE account_id = 1
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