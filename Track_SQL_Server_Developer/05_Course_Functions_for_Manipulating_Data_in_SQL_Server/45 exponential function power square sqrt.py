import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=datacamp;" "Trusted_Connection=True;" )
cursor = conn.cursor()

variable_query = """
"""
# cursor.execute(variable_query)
# conn.commit()

select_query = """
-- Raise the number stored in the @number variable to the power from the @power variable.
-- Calculate the square of the @number variable (square means the power of 2).
-- Calculate the square root of the number stored in the @number variable.

DECLARE @number DECIMAL(4, 2) = 4.5;
DECLARE @power INT = 4;

SELECT
	@number AS number,
	@power AS power,
	-- Raise the @number to the @power
	POWER(@number, @power) AS number_to_power,
	-- Calculate the square of the @number
	SQUARE(@number) num_squared,
	-- Calculate the square root of the @number
	SQRT(@number) num_square_root;
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