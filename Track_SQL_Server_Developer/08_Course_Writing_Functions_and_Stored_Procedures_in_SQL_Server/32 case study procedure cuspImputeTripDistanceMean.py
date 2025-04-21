import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=DatabaseDesign;" "Trusted_Connection=True;" )
cursor = conn.cursor()

cursor.execute("""
-- Drop cuspImputeTripDistanceMean
DROP PROCEDURE IF EXISTS cuspImputeTripDistanceMean;
""")
conn.commit()

cursor.execute("""
-- Create the stored procedure
CREATE PROCEDURE dbo.cuspImputeTripDistanceMean
AS
BEGIN
-- Specify @AvgTripDistance variable
DECLARE @AvgTripDistance AS numeric (18,4)

-- Calculate the average trip distance
SELECT @AvgTripDistance = AVG(TripDistance) 
FROM YellowTripData
-- Only include trip distances greater than 0
WHERE TripDistance > 0

-- Update the records where trip distance is 0
UPDATE YellowTripData
SET TripDistance =  @AvgTripDistance
WHERE TripDistance = 0
END;
""")

if cursor.nextset():
    message_row = cursor.fetchone()
    if message_row:
        print(f'Message: {message_row[0]}')
else:
    print(f'Commands completed successfully.')
conn.commit()

select_query = """
SELECT 
    name, 
    type_desc, 
    OBJECT_DEFINITION(object_id) AS definition
FROM sys.objects
WHERE type IN ('P')
ORDER BY name;
"""

cursor.execute(select_query)

results = []
while True:
    rows = cursor.fetchall()
    if not rows:
        break
    columns = [column[0] for column in cursor.description]
    df = pd.DataFrame.from_records(rows, columns=columns)
    results.append(df)
    if not cursor.nextset():
        break
    
for i, df in enumerate(results, start=1):
    print(f'{i} SELECT STATEMENT\n, {df}\n')
cursor.close()
conn.close()