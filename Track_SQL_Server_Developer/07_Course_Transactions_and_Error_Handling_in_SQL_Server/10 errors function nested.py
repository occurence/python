import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=tehandling;" "Trusted_Connection=True;" )
cursor = conn.cursor()

cursor.execute("""
BEGIN TRY
    INSERT INTO products(product_name, stock, price)
        VALUES('Trek Powerfly 5 - 2018', 10, 3499.99);
    SELECT 'Prooduct inserted correctly!' AS message;
END TRY
BEGIN CATCH
    SELECT 'INNER CATCH BLOCK' AS message;
    BEGIN TRY
        INSERT INTO errors
            VALUES('Error from nested function');
        SELECT 'Error from nested function' AS message;
    END TRY
    BEGIN CATCH
        SELECT 'OUTER CATCH BLOCK' AS 'Error_from',
        ERROR_NUMBER() AS Error_number,
        ERROR_MESSAGE() AS Error_message;
    END CATCH
    -- SELECT ERROR_NUMBER() AS Error_number,
    --        ERROR_SEVERITY() AS Error_severity,
    --        ERROR_STATE() AS Error_state,
    --        ERROR_PROCEDURE() AS Error_procedure,
    --        ERROR_LINE() AS Error_line,
    --        ERROR_MESSAGE() AS Error_message;
END CATCH
""")

if cursor.nextset():
    message_row = cursor.fetchone()
    if message_row:
        print(f'Message: {message_row[0]}')
else:
    print(f'No message returned')
conn.commit()

select_query = """
SELECT * FROM errors;
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