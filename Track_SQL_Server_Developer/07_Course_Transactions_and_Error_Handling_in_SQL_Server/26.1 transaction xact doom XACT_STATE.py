import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=tehandling;" "Trusted_Connection=True;", autocommit=True)
cursor = conn.cursor()

try:
    cursor.execute("""
        SET XACT_ABORT ON;
        BEGIN TRY
            BEGIN TRAN;
                INSERT INTO customers VALUES ('Dylan', 'Smith', 'dylansmith@mail.com', '555888999');
                INSERT INTO customers VALUES ('Mark', 'Davis', 'markdavis@mail.com', '555909090');
            COMMIT TRAN;
        END TRY
        BEGIN CATCH
            IF XACT_STATE() <> 0
                ROLLBACK TRAN;

            -- Print error message inside SQL Server
            SELECT ERROR_MESSAGE() AS SQL_Error_Message;
        END CATCH
    """)
    conn.commit()

    if cursor.nextset():
        message_row = cursor.fetchone()
        if message_row:
            print(f'SQL Error Message: {message_row[0]}')
        else:
            print('No error message returned from SQL Server.')

except pyodbc.DatabaseError as e:
    print(f"Database Error: {e}")
    conn.rollback()

cursor.close()
conn.close()