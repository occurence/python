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
    DECLARE @product_name AS NVARCHAR(50) = 'Trek CrossRip+ - 2018';
    -- Set the number of sold bikes
    DECLARE @sold_bikes AS INT = 10;
    DECLARE @current_stock INT;

    SELECT @current_stock = stock FROM products WHERE product_name = @product_name;

    DECLARE @my_message NVARCHAR(500) =
        -- Customize the error message
        FORMATMESSAGE('There are not enough %s bikes. You have %d in stock.', @product_name, @current_stock);

    IF (@current_stock - @sold_bikes < 0)
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
