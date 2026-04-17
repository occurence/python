import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=datacamp;" "Trusted_Connection=True;" )
cursor = conn.cursor()

variable_query = """
"""
# cursor.execute(variable_query)
# conn.commit()

select_query = """
-- Calculate the number of years since a participant celebrated their 18th birthday until the first time they voted.
SELECT
	first_name,
	birthdate,
	first_vote_date,
    -- Select the diff between the 18th birthday and first vote
	DATEDIFF(YEAR, DATEADD(YEAR, 18, birthdate), first_vote_date) AS adult_years_until_vote
FROM voters;

-- How many weeks have passed since the beginning of 2019 until now?
SELECT 
	-- Get the difference in weeks from 2019-01-01 until now
	DATEDIFF(WEEK, '2019-01-01', GETDATE()) AS weeks_passed;
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