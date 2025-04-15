import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=tehandling;" "Trusted_Connection=True;", autocommit=True)
cursor = conn.cursor()

try:
    cursor.execute("""
        SET XACT_ABORT ON;
        BEGIN TRY
            BEGIN TRAN;
                -- This should cause a unique constraint violation
                INSERT INTO customers VALUES ('Dylan', 'Smith', 'dylansmith@mail.com', '555888999');
            COMMIT TRAN;
        END TRY
        BEGIN CATCH
            -- If an error occurs, rollback transaction
            IF XACT_STATE() <> 0
                ROLLBACK TRAN;

            -- Raise error so Python can catch it
            DECLARE @ErrorMessage NVARCHAR(4000) = ERROR_MESSAGE();
            RAISERROR (@ErrorMessage, 16, 1);
        END CATCH
    """)
    conn.commit()

except pyodbc.DatabaseError as e:
    print(f"Database Error: {e}")
    conn.rollback()



# select_query = """
# SELECT * FROM transactions;
# """

# cursor.execute(select_query)

# results = []
# while True:
#     rows = cursor.fetchall()
#     if not rows:
#         break
#     columns = [column[0] for column in cursor.description]
#     df = pd.DataFrame.from_records(rows, columns=columns)
#     results.append(df)
#     if not cursor.nextset():
#         break
    
# for i, df in enumerate(results, start=1):
#     print(f'{i} SELECT STATEMENT\n, {df}\n')

cursor.close()
conn.close()