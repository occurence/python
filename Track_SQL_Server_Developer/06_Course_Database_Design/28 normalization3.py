import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=DatabaseDesign;" "Trusted_Connection=True;" )
cursor = conn.cursor()

cursor.execute("""
-- Create a new table to satisfy 3NF
DROP TABLE IF EXISTS car_model;
CREATE TABLE car_model(
  model VARCHAR(128),
  manufacturer VARCHAR(128),
  type_car VARCHAR(128)
);
""")
conn.commit()

cursor.execute("""
-- Insert data into the new table
INSERT INTO car_model
SELECT DISTINCT
  model,
  manufacturer,
  type_car
FROM cars;
""")
conn.commit()

cursor.execute("""
-- Drop columns in rental_cars to satisfy 3NF
ALTER TABLE cars
DROP COLUMN manufacturer, 
type_car;
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