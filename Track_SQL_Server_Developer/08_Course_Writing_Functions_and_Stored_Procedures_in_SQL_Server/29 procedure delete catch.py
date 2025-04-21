import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=DatabaseDesign;" "Trusted_Connection=True;" )
cursor = conn.cursor()

try:
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
        SELECT ERROR_MESSAGE() AS ErrorMessage;
    END CATCH;
    """)
  
    row = cursor.fetchone()
    while row:
        print(f"ReturnCode: {row.ReturnCode}, ErrorMessage: {row.ErrorMessage}")
        row = cursor.fetchone()

except pyodbc.Error as e:
    print("Database error occurred:", e)
except Exception as ex:
    print("An error occurred:", ex)
finally:
    cursor.close()
    conn.close()
