import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=DatabaseDesign;" "Trusted_Connection=True;" )
cursor = conn.cursor()

cursor.execute("""
-- Drop SalesCalculateTotalAmount
DROP TRIGGER IF EXISTS SalesCalculateTotalAmount;
""")
conn.commit()

cursor.execute("""
-- Create the trigger
CREATE TRIGGER SalesCalculateTotalAmount
ON SalesWithoutPrice
AFTER INSERT
AS
	UPDATE sp
	SET sp.TotalAmount = sp.Quantity * p.Price
	FROM SalesWithoutPrice AS sp
	INNER JOIN Products AS p ON sp.Product = p.Product
	WHERE sp.TotalAmount IS NULL;
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
FROM sys.triggers
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