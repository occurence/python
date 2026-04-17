import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=datacamp;" "Trusted_Connection=True;" )
cursor = conn.cursor()

variable_query = """
"""
# cursor.execute(variable_query)
# conn.commit()

select_query = """
-- Write a query to select the voters whose first name contains the letters "rr".
SELECT 
	first_name,
	last_name,
	email 
FROM voters
-- Look for first names that contain "rr" in the middle
WHERE PATINDEX('%rr%', first_name) > 0;

-- Write a query to select the voters whose first name starts with "C" and has "r" as the third letter.
SELECT 
	first_name,
	last_name,
	email 
FROM voters
-- Look for first names that start with C and the 3rd letter is r
WHERE PATINDEX('C_r%', first_name) > 0;

-- Select the voters whose first name contains an "a" followed by other letters, then a "w", followed by other letters.
SELECT 
	first_name,
	last_name,
	email 
FROM voters
-- Look for first names that have an "a" followed by 0 or more letters and then have a "w"
WHERE PATINDEX('%a%w%', first_name) > 0;

-- Write a query to select the voters whose first name contains one of these letters: "x", "w" or "q".
SELECT 
	first_name,
	last_name,
	email 
FROM voters
-- Look for first names that contain one of the letters: "x", "w", "q"
WHERE PATINDEX('%[xwq]%', first_name) > 0;
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