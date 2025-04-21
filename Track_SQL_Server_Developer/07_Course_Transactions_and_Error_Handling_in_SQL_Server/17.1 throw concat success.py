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
    DECLARE @first_name NVARCHAR(20) = 'Pedro';

    -- Concat the message
    DECLARE @my_message NVARCHAR(500) =
        CONCAT('There is no staff member with ', @first_name, ' as the first name.');

    IF NOT EXISTS (SELECT * FROM staff WHERE first_name = @first_name)
        -- Throw the error
        THROW 50000, @my_message, 1;
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
