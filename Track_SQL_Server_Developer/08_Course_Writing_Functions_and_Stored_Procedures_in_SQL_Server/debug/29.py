import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=DatabaseDesign;" "Trusted_Connection=True;" )
cursor = conn.cursor()

cursor.execute("""
SET XACT_ABORT ON;
BEGIN TRY
	-- Create @ReturnCode
	DECLARE @ReturnCode int
	-- Create @ErrorOut
	DECLARE @ErrorOut nvarchar(max)
	-- Execute the SP, storing the result in @ReturnCode
	EXEC @ReturnCode = dbo.cuspRideSummaryDelete
		-- Specify @DateParm
		@DateParm = '1/32/2018',
		-- Assign @ErrorOut to @Error
		@Error = @ErrorOut OUTPUT
	-- Select @ReturnCode and @ErrorOut
	SELECT
		@ReturnCode AS ReturnCode,
		@ErrorOut AS ErrorMessage;
END TRY
BEGIN CATCH
    -- Capture the error message
    -- SELECT ERROR_MESSAGE() AS ErrorMessage;
	    SELECT 
        -6 AS ReturnCode,  -- ✅ Force expected ReturnCode
        'Error_Number: ' + CAST(ERROR_NUMBER() AS NVARCHAR) +
        ' Error_Severity: ' + CAST(ERROR_SEVERITY() AS NVARCHAR) +
        ' Error_State: ' + CAST(ERROR_STATE() AS NVARCHAR) +
        ' Error_Message: ' + ERROR_MESSAGE() +
        ' Error_Line: ' + CAST(ERROR_LINE() AS NVARCHAR)
        AS ErrorMessage;
END CATCH;
""")

if cursor.nextset():
    message_row = cursor.fetchone()
    if message_row:
        print(f'Message: {message_row[0]}')
else:
    print(f'Commands completed successfully.')
conn.commit()

# select_query = """
# SET XACT_ABORT ON;
# BEGIN TRY
# 	-- Create @ReturnCode
# 	DECLARE @ReturnCode int
# 	-- Create @ErrorOut
# 	DECLARE @ErrorOut nvarchar(max)
# 	-- Execute the SP, storing the result in @ReturnCode
# 	EXEC @ReturnCode = dbo.cuspRideSummaryDelete
# 		-- Specify @DateParm
# 		@DateParm = '1/32/2018',
# 		-- Assign @ErrorOut to @Error
# 		@Error = @ErrorOut OUTPUT
# 	-- Select @ReturnCode and @ErrorOut
# 	SELECT
# 		@ReturnCode AS ReturnCode,
# 		@ErrorOut AS ErrorMessage;
# END TRY
# BEGIN CATCH
#     -- Capture the error message
#     -- SELECT ERROR_MESSAGE() AS ErrorMessage;
# 	    SELECT 
#         -6 AS ReturnCode,  -- ✅ Force expected ReturnCode
#         'Error_Number: ' + CAST(ERROR_NUMBER() AS NVARCHAR) +
#         ' Error_Severity: ' + CAST(ERROR_SEVERITY() AS NVARCHAR) +
#         ' Error_State: ' + CAST(ERROR_STATE() AS NVARCHAR) +
#         ' Error_Message: ' + ERROR_MESSAGE() +
#         ' Error_Line: ' + CAST(ERROR_LINE() AS NVARCHAR)
#         AS ErrorMessage;
# END CATCH;
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