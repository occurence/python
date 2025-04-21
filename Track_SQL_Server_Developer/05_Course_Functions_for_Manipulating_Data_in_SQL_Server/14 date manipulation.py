import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=datacamp;" "Trusted_Connection=True;" )
cursor = conn.cursor()

variable_query = """
"""
# cursor.execute(variable_query)
# conn.commit()

select_query = """
-- Retrieve the date when each voter had their 18th birthday.
SELECT 
	first_name,
	birthdate,
    -- Add 18 years to the birthdate
	DATEADD(YEAR, 18, birthdate) AS eighteenth_birthday
  FROM voters;

-- Add five days to the first_vote_date, to calculate the date when the vote was processed.
SELECT 
	first_name,
	first_vote_date,
    -- Add 5 days to the first voting date
	DATEADD(DAY, 5, first_vote_date) AS processing_vote_date
  FROM voters;

-- Calculate what day it was 476 days ago.
SELECT
	-- Subtract 476 days from the current date
	DATEADD(DAY, -476, GETDATE()) AS date_476days_ago;
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