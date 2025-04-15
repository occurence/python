import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=DatabaseDesign;" "Trusted_Connection=True;" )
cursor = conn.cursor()

cursor.execute("""
-- Declare @RideDates
DECLARE @RideDates TABLE(
    -- Define RideStart column
	RideStart date, 
    -- Define RideEnd column
    RideEnd date)
-- Populate @RideDates
INSERT INTO @RideDates(RideStart, RideEnd)
-- Select the unique date values of StartDate and EndDate
SELECT DISTINCT
    -- Cast StartDate as date
	CAST(StartDate as date),
    -- Cast EndDate as date
	CAST(EndDate as date) 
FROM CapitalBikeShare 
SELECT * 
FROM @RideDates
""")

results = []

while True:
    if cursor.description:
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        df = pd.DataFrame.from_records(rows, columns=columns)
        results.append(df)

    if not cursor.nextset():
        break

for i, df in enumerate(results, start=1):
    print(f"Result Set {i}:\n{df}\n")

cursor.close()
conn.close()