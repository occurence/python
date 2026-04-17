import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=datacamp;" "Trusted_Connection=True;" )
cursor = conn.cursor()

variable_query = """
"""
# cursor.execute(variable_query)
# conn.commit()

select_query = """
SELECT
	first_name,
    last_name,
    birthdate,
	first_vote_date,
	-- Find out on which day of the week each participant voted 
	DATENAME(weekday, first_vote_date) AS first_vote_weekday,
	-- Find out the year of the first vote
	YEAR(first_vote_date) AS first_vote_year,
	-- Discover the participants' age when they joined the contest
	DATEDIFF(YEAR, birthdate, first_vote_date) AS age_at_first_vote,	
	-- Calculate the current age of each voter
	DATEDIFF(YEAR, birthdate, GETDATE()) AS current_age
FROM voters;
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