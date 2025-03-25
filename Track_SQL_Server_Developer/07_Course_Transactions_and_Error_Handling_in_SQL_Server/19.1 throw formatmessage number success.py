import pyodbc
import pandas as pd

conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=Arc-PC;"
    "DATABASE=tehandling;"
    "Trusted_Connection=True;"
)
cursor = conn.cursor()

cursor.execute("""
IF EXISTS (SELECT 1 FROM sys.messages WHERE message_id = 50002)
BEGIN
    EXEC sp_dropmessage @msgnum = 50002, @lang = 'us_english';
END
""")
conn.commit()

try:
    
    cursor.execute("""
    EXEC sp_addmessage @msgnum = 50002, @severity = 16, @msgtext = 'There are not enough %s bikes. You only have %d in stock.', @lang = N'us_english';

    DECLARE @product_name AS NVARCHAR(50) = 'Trek CrossRip+ - 2018';
    --Change the value
    DECLARE @sold_bikes AS INT = 10;
    DECLARE @current_stock INT;

    SELECT @current_stock = stock FROM products WHERE product_name = @product_name;

    DECLARE @my_message NVARCHAR(500) =
        FORMATMESSAGE(50002, @product_name, @current_stock);

    IF (@current_stock - @sold_bikes < 0)
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
