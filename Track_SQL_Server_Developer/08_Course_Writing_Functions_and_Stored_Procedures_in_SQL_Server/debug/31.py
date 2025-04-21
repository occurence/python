import pyodbc
import pandas as pd

conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=Arc-PC;"
    "DATABASE=tehandling;"
    "Trusted_Connection=True;"
)
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
        -- SELECT ERROR_MESSAGE() AS ErrorMessage;
        SELECT
        'Error_Number: '+ CAST(ERROR_NUMBER() AS VARCHAR) +
        'Error_Severity: '+ CAST(ERROR_SEVERITY() AS VARCHAR) +
        'Error_State: ' + CAST(ERROR_STATE() AS VARCHAR) + 
        'Error_Message: ' + ERROR_MESSAGE() + 
        'Error_Line: ' + CAST(ERROR_LINE() AS VARCHAR)
    END CATCH;
    """)

    if cursor.description:
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()

        if rows:
            df = pd.DataFrame.from_records(rows, columns=columns)
            print(df)
        else:
            print("No data returned.")
    else:
        print("Executed successfully.")

except pyodbc.Error as e:
    print(f"Database error: {str(e)}")

finally:
    cursor.close()
    conn.close()
