import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=DatabaseDesign;" "Trusted_Connection=True;" )
cursor = conn.cursor()

# cursor.execute("""
# """)
# conn.commit()

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
SELECT NearestPop, 
       Country, 
       COUNT(NearestPop) NumEarthquakes -- Number of cities
FROM Earthquakes
WHERE Magnitude >= 8
	AND Country IS NOT NULL
GROUP BY Country, NearestPop -- Group columns
ORDER BY NumEarthquakes DESC;

SELECT DISTINCT(NearestPop),-- Remove duplicate city
		Country
FROM Earthquakes
WHERE MAGNITUDE >= 8 -- Add filter condition 
	AND NearestPop IS NOT NULL
ORDER BY NearestPop;

SELECT NearestPop, 
       Country, 
       COUNT(NearestPop) NumEarthquakes -- Number of cities
FROM Earthquakes
WHERE Magnitude >= 8
	AND Country IS NOT NULL
GROUP BY Country, NearestPop -- Group columns
ORDER BY NumEarthquakes DESC;
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