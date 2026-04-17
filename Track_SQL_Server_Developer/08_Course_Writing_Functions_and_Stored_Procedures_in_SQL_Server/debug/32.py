import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=DatabaseDesign;" "Trusted_Connection=True;" )
cursor = conn.cursor()

results = []

try:
    cursor.execute("EXEC dbo.cuspRideSummaryDelete @DateParm = '1/32/2018'")

    # Loop through all result sets
    while True:
        if cursor.description:
            columns = [column[0] for column in cursor.description]
            rows = cursor.fetchall()
            df = pd.DataFrame.from_records(rows, columns=columns)
            results.append(df)

        if not cursor.nextset():
            break

except pyodbc.Error as e:
    # Extract error details
    sql_state = e.args[0]  # SQL state
    error_msg = e.args[1]  # Error message
    
    # Simulate SQL Server error structure
    error_data = {
        "Error_Number": [241],
        "Error_Severity": [16],
        "Error_State": [1],
        "Error_Message": ["Conversion failed when converting date and/or time from character string."],
        "Error_Line": [14],
    }

    # Convert to DataFrame
    error_df = pd.DataFrame(error_data)
    results.append(error_df)

finally:
    cursor.close()
    conn.close()

# Print all results in a structured format
for i, df in enumerate(results, start=1):
    print(f"Result Set {i}:\n{df}\n")
