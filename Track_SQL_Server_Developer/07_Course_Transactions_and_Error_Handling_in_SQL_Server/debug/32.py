import pyodbc
import pandas as pd

conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=Arc-PC;"
    "DATABASE=tehandling;"
    "Trusted_Connection=True;"
)
cursor = conn.cursor()

select_query = """
SET XACT_ABORT ON;
BEGIN TRY
    BEGIN TRAN;
        INSERT INTO customers VALUES ('Mark', 'Davis', 'markdavis@mail.com', '555909090');
        INSERT INTO customers VALUES ('Dylan', 'Smith', 'dylansmith@mail.com', '555888999');
    COMMIT TRAN;
END TRY
BEGIN CATCH
    IF XACT_STATE() <> 0
        ROLLBACK TRAN;
    
    -- Return an error message as a result set
    SELECT 'TESTSLKEJTLKSJLT' AS ErrorMessage;
END CATCH;
"""

try:
    cursor.execute(select_query)

    # Fetch first result
    message_row = cursor.fetchone()
    if message_row:
        print(f'Message: {message_row[0]}')
    else:
        print('No error message returned')

except pyodbc.DatabaseError as e:
    print(f"Database Error: {e}")

select_query = """
SELECT * FROM customers WHERE email IN ('markdavis@mail.com', 'dylansmith@mail.com');
"""
cursor.execute(select_query)

columns = [column[0] for column in cursor.description]
rows = cursor.fetchall()
df = pd.DataFrame.from_records(rows, columns=columns)

print(df)

cursor.close()
conn.close()
