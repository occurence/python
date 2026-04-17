import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=datacamp;" "Trusted_Connection=True;" )
cursor = conn.cursor()

variable_query = """
-- Set the correct language
SET LANGUAGE English;
"""
cursor.execute(variable_query)
conn.commit()

select_query = """
-- Change the language, so that '12/18/55' is interpreted as a valid date. Select the day of week. Select the year.
DECLARE @date1 NVARCHAR(20) = '12/18/55';

-- Set the correct language
SET LANGUAGE English;
SELECT
	@date1 AS initial_date,
    -- Check that the date is valid
	ISDATE(@date1) AS is_valid,
    -- Select the week day name
	DATENAME(WEEKDAY, @date1) AS week_day,
	-- Extract the year from the date
	YEAR(@date1) AS year_name;
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