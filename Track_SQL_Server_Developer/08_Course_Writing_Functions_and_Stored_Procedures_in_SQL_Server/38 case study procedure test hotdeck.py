import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=DatabaseDesign;" "Trusted_Connection=True;" )
cursor = conn.cursor()

# cursor.execute("""
# """)

# if cursor.nextset():
#     message_row = cursor.fetchone()
#     if message_row:
#         print(f'Message: {message_row[0]}')
# else:
#     print(f'Commands completed successfully.')
# conn.commit()

select_query = """
SELECT
    -- Select the pickup day of week
	DATENAME(weekday, PickupDate) as DayofWeek,
    -- Calculate TotalAmount per TripDistance
	CAST(AVG(TotalAmount/
            -- Select TripDistance if it's more than 0
			CASE WHEN TripDistance > 0 THEN TripDistance
                 -- Use GetTripDistanceHotDeck()
     			 ELSE dbo.GetTripDistanceHotDeck() END) as decimal(10,2)) as 'AvgFare'
FROM YellowTripData
GROUP BY DATENAME(weekday, PickupDate)
-- Order by the PickupDate day of week
ORDER BY
     CASE WHEN DATENAME(weekday, PickupDate) = 'Monday' THEN 1
         WHEN DATENAME(weekday, PickupDate) = 'Tuesday' THEN 2
         WHEN DATENAME(weekday, PickupDate) = 'Wednesday' THEN 3
         WHEN DATENAME(weekday, PickupDate) = 'Thursday' THEN 4
         WHEN DATENAME(weekday, PickupDate) = 'Friday' THEN 5
         WHEN DATENAME(weekday, PickupDate) = 'Saturday' THEN 6
         WHEN DATENAME(weekday, PickupDate) = 'Sunday' THEN 7
END ASC;
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