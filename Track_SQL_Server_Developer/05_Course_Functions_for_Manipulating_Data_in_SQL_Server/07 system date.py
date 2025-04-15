import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=datacamp;" "Trusted_Connection=True;" )
cursor = conn.cursor()

variable_query = """
"""
# cursor.execute(variable_query)
# conn.commit()

select_query = """
-- Use the most common date function for retrieving the current date
SELECT 
	GETDATE() AS CurrentDate;

-- Select the current date in UTC time (Universal Time Coordinate) using two different functions.
SELECT 
	CURRENT_TIMESTAMP AS UTC_HighPrecision,
	GETUTCDATE() AS UTC_LowPrecision;

-- Select the local system's date, including the timezone information.
SELECT 
	SYSDATETIMEOFFSET() AS Timezone;
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