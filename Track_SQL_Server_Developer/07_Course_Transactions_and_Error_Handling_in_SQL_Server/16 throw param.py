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
    DECLARE @staff_id INT = 4;

    IF NOT EXISTS (SELECT * FROM staff WHERE staff_id = @staff_id)
        -- Invoke the THROW statement with parameters
        THROW 50001, 'No staff member with such id', 1;
    ELSE
        SELECT * FROM staff WHERE staff_id = @staff_id
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
