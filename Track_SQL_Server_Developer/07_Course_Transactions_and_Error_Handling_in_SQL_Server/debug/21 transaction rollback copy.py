import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=tehandling;" "Trusted_Connection=True;", autocommit=True)
cursor = conn.cursor()

select_query = """
-- Use the appropriate setting
SET XACT_ABORT ON;
BEGIN TRY
	BEGIN TRAN;
		INSERT INTO customers VALUES ('Mark', 'Davis', 'markdavis@mail.com', '555909090');
		INSERT INTO customers VALUES ('Dylan', 'Smith', 'dylansmith@mail.com', '555888999');
	COMMIT TRAN;
END TRY
BEGIN CATCH
	-- Check if there is an open transaction
	IF XACT_STATE() <> 0
    	-- Rollback the transaction
		ROLLBACK TRAN;
    -- Select the message of the error
    SELECT 'saldkfjlskjdfsdfsdf' AS Error_message;
END CATCH
"""

try:
    cursor.execute(select_query)
    conn.commit()

    if cursor.nextset():
        message_row = cursor.fetchone()
        if message_row:
            print(f'Message: {message_row[0]}')
    # else:
    #     print(f'No message returned')
    # conn.commit()

except pyodbc.DatabaseError as e:
    print(f"Database Error: {e}")
    conn.rollback()
finally:
    cursor.close()
    conn.close()

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

# cursor.close()
# conn.close()