import pyodbc
import pandas as pd

# Establish connection
conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=Arc-PC;"
    "DATABASE=DatabaseDesign;"
    "Trusted_Connection=True;"
)
cursor = conn.cursor()

results = []

try:
    # Execute the SQL script
    cursor.execute("""
        SET XACT_ABORT ON;
        BEGIN TRY
            DECLARE @ReturnCode int;
            EXEC @ReturnCode = dbo.cuspRideSummaryDelete @DateParm = '1/32/2018';
            SELECT @ReturnCode AS ReturnCode, NULL AS ErrorMessage;
        END TRY
        BEGIN CATCH
            SELECT 
                NULL AS ReturnCode,
                'Error_Number: ' + CAST(ERROR_NUMBER() AS NVARCHAR) + 
                ' Error_Severity: ' + CAST(ERROR_SEVERITY() AS NVARCHAR) + 
                ' Error_State: ' + CAST(ERROR_STATE() AS NVARCHAR) + 
                ' Error_Message: ' + ERROR_MESSAGE() + 
                ' Error_Line: ' + CAST(ERROR_LINE() AS NVARCHAR) 
                AS ErrorMessage;
        END CATCH;
    """)

    # Fetch first row separately to check for ReturnCode/ErrorMessage
    row = cursor.fetchone()
    while row:
        print(f"ReturnCode: {row.ReturnCode}, ErrorMessage: {row.ErrorMessage}")
        row = cursor.fetchone()

    # Process remaining result sets using DataFrames
    while True:
        rows = cursor.fetchall()
        if not rows:
            break
        columns = [column[0] for column in cursor.description]
        df = pd.DataFrame.from_records(rows, columns=columns)
        results.append(df)

except pyodbc.Error as e:
    print(f"Database error: {e}")

finally:
    cursor.close()
    conn.close()

# Print results in a structured format
for i, df in enumerate(results, start=1):
    print(f"Result Set {i}:\n{df}\n")
