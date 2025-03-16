import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=DatabaseDesign;" "Trusted_Connection=True;" )
cursor = conn.cursor()

cursor.execute("""
-- Create a new table to hold the cars rented by customers
DROP TABLE IF EXISTS cust_rentals;
CREATE TABLE cust_rentals (
  customer_id INT NOT NULL,
  car_id VARCHAR(128) NULL,
  invoice_id VARCHAR(128) NULL
);
""")
conn.commit()

cursor.execute("""
-- Insert data into the new table
INSERT INTO cust_rentals
SELECT DISTINCT
  customer_id,
  cars_rented,
  invoice_id
FROM customers;
""")
conn.commit()

cursor.execute("""
-- Drop two columns from customers table to satisfy 1NF
ALTER TABLE customers
DROP COLUMN cars_rented,
invoice_id;
""")
conn.commit()

# select_query = """
# """

# cursor.execute(select_query)

# results = []
# while True:
#     rows = cursor.fetchall()
#     if not rows:
#         break
#     columns = [column[0] for column in cursor.description]
#     df = pd.DataFrame.from_records(rows, columns=columns)
#     results.append(df)
#     if not cursor.nextset():
#         break
    
# for i, df in enumerate(results, start=1):
#     print(f'{i} SELECT STATEMENT\n, {df}\n')
cursor.close()
conn.close()