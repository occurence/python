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
    BEGIN TRY
        -- Execute the stored procedure
        EXEC insert_product
            -- Set the values for the parameters
            @product_name = 'Trek Conduit+',
            @stock = 3,
            @price = 499.99;
    END TRY
    -- Set up the CATCH block
    BEGIN CATCH
        -- Select the error message
        SELECT ERROR_MESSAGE();
    END CATCH
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
