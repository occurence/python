import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=DatabaseDesign;" "Trusted_Connection=True;" )
cursor = conn.cursor()

cursor.execute("""
-- Create a new table to satisfy 2NF
DROP TABLE IF EXISTS cars;
CREATE TABLE cars (
  car_id VARCHAR(256) NULL,
  model VARCHAR(128),
  manufacturer VARCHAR(128),
  type_car VARCHAR(128),
  condition VARCHAR(128),
  color VARCHAR(128)
);
""")
conn.commit()

cursor.execute("""
-- Insert data into the new table
INSERT INTO cars
SELECT DISTINCT
  car_id,
  model,
  manufacturer,
  type_car,
  condition,
  color
FROM customer_rentals;
""")
conn.commit()

cursor.execute("""
-- Drop columns in customer_rentals to satisfy 2NF
ALTER TABLE customer_rentals
DROP COLUMN model,
manufacturer, 
type_car,
condition,
color;
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