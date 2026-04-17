import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=DatabaseDesign;" "Trusted_Connection=True;" )
cursor = conn.cursor()

cursor.execute("""
-- Add the following rows to the table
INSERT INTO SalesWithPrice (Customer, Product, Price, Currency, Quantity)
VALUES ('Fruit Mag', 'Pomelo', 1.12, 'USD', 200),
	   ('VitaFruit', 'Avocado', 2.67, 'USD', 400),
	   ('Tasty Fruits', 'Blackcurrant', 2.32, 'USD', 1100),
	   ('Health Mag', 'Kiwi', 1.42, 'USD', 100),
	   ('eShop', 'Plum', 1.1, 'USD', 500);
""")

if cursor.nextset():
    message_row = cursor.fetchone()
    if message_row:
        print(f'Message: {message_row[0]}')
else:
    print(f'Commands completed successfully.')
conn.commit()

select_query = """
-- Verify the results after adding the new rows
SELECT * FROM SalesWithPrice;
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