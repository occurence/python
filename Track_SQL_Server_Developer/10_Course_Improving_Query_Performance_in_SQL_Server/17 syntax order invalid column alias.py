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
-- First query
/*
SELECT PlayerName, 
    Team, 
    Position,
    (DRebound+ORebound)/CAST(GamesPlayed AS numeric) AS AvgRebounds
FROM PlayerStats
WHERE AvgRebounds >= 12;
*/

-- Second query

-- Add the new column to the select statement
SELECT PlayerName, 
       Team, 
       Position, 
       AvgRebounds -- Add the new column
FROM
     -- Sub-query starts here                             
	(SELECT 
      PlayerName, 
      Team, 
      Position,
      -- Calculate average total rebounds
     (DRebound+ORebound)/CAST(GamesPlayed AS numeric) AS AvgRebounds
	 FROM PlayerStats) tr
WHERE AvgRebounds >= 12; -- Filter rows
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