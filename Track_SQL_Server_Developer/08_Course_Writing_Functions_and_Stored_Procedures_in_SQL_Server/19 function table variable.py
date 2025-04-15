import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=DatabaseDesign;" "Trusted_Connection=True;" )
cursor = conn.cursor()

cursor.execute("""
-- Create @StationStats
DECLARE @StationStats TABLE(
	StartStation nvarchar(100), 
	RideCount int, 
	TotalDuration numeric)
-- Populate @StationStats with the results of the function
INSERT INTO @StationStats
SELECT TOP 10 *
-- Execute SumStationStats with 3/15/2018
FROM dbo.SumStationStats('3/15/2018') 
ORDER BY RideCount DESC
-- Select all the records from @StationStats
SELECT * 
FROM @StationStats
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