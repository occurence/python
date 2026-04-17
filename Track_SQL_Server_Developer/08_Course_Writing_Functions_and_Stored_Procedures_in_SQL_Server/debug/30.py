import pyodbc

try:
    # Connect to SQL Server
    conn = pyodbc.connect(
        "DRIVER={SQL Server};"
        "SERVER=Arc-PC;"
        "DATABASE=DatabaseDesign;"
        "Trusted_Connection=True;"
    )
    cursor = conn.cursor()

    # SQL script that will cause an error
    sql_script = """
    SET XACT_ABORT ON;
    BEGIN TRY
        DECLARE @ReturnCode int;
        DECLARE @ErrorOut nvarchar(max);
        EXEC @ReturnCode = dbo.cuspRideSummaryDelete
            @DateParm = '1/32/2018',
            @Error = @ErrorOut OUTPUT;
        SELECT @ReturnCode AS ReturnCode, @ErrorOut AS ErrorMessage;
    END TRY
    BEGIN CATCH
        SELECT 
            -6 AS ReturnCode,
            'Error_Number: ' + CAST(ERROR_NUMBER() AS VARCHAR) +
            ' Error_Severity: ' + CAST(ERROR_SEVERITY() AS VARCHAR) +
            ' Error_State: ' + CAST(ERROR_STATE() AS VARCHAR) +
            ' Error_Message: ' + ERROR_MESSAGE() +
            ' Error_Line: ' + CAST(ERROR_LINE() AS VARCHAR) AS ErrorMessage;
    END CATCH;
    """
    
    # Execute the SQL script
    cursor.execute(sql_script)
    
    # Fetch and print results
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
