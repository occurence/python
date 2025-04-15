import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=DatabaseDesign;" "Trusted_Connection=True;" )
cursor = conn.cursor()

cursor.execute("""
-- Drop ConvertDollar
DROP FUNCTION IF EXISTS ConvertDollar;
""")
conn.commit()

cursor.execute("""
-- Create the function
CREATE FUNCTION dbo.ConvertDollar
	-- Specify @DollarAmt parameter
	(@DollarAmt numeric(18,2),
     -- Specify ExchangeRate parameter
     @ExchangeRate numeric(18,2))
-- Specify return data type
RETURNS numeric(18,2)
AS
BEGIN
RETURN
	-- Multiply @ExchangeRate and @DollarAmt
	(SELECT @ExchangeRate * @DollarAmt)
END;
""")

if cursor.nextset():
    message_row = cursor.fetchone()
    if message_row:
        print(f'Message: {message_row[0]}')
else:
    print(f'Commands completed successfully.')
conn.commit()

select_query = """
SELECT 
    name, 
    type_desc, 
    OBJECT_DEFINITION(object_id) AS definition
FROM sys.objects
WHERE type IN ('FN', 'IF', 'TF')
ORDER BY name;
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