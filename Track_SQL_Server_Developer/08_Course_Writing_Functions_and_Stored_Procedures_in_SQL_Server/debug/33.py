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
            SELECT @ReturnCode AS ReturnCode;
        END TRY
        BEGIN CATCH
            SELECT 
                ERROR_NUMBER() AS Error_Number,
                ERROR_SEVERITY() AS Error_Severity,
                ERROR_STATE() AS Error_State,
                ERROR_MESSAGE() AS Error_Message,
                ERROR_LINE() AS Error_Line;
        END CATCH;
    """)

    # Fetch results
    while True:
        if cursor.description:
            columns = [column[0] for column in cursor.description]
            rows = cursor.fetchall()
            df = pd.DataFrame.from_records(rows, columns=columns)
            results.append(df)

        if not cursor.nextset():
            break

except pyodbc.Error as e:
    print(f"Database error: {e}")

finally:
    cursor.close()
    conn.close()

# Print all results
for i, df in enumerate(results, start=1):
    print(f"Result Set {i}:\n{df}\n")
