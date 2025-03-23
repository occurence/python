import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=tehandling;" "Trusted_Connection=True;" )
cursor = conn.cursor()

cursor.execute("""
-- Set up the TRY block
BEGIN TRY  	
	SELECT 'Total: ' + SUM(price * quantity) AS total
	FROM orders  
END TRY
-- Set up the CATCH block
BEGIN CATCH  
	-- Show error information.
	SELECT  ERROR_NUMBER() AS number,
        	ERROR_SEVERITY() AS severity_level,
        	ERROR_STATE() AS state,
        	ERROR_LINE() AS line,
        	ERROR_MESSAGE() AS message;
END CATCH
""")

if cursor.nextset():
    message_row = cursor.fetchone()
    if message_row:
        print(f'Message: {message_row[0]} {message_row[1]} {message_row[2]} {message_row[3]} {message_row[4]}')
else:
    print(f'No message returned')
conn.commit()

select_query = """
SELECT * FROM errors;
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