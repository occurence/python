import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=DatabaseDesign;" "Trusted_Connection=True;" )
cursor = conn.cursor()

cursor.execute("""
-- Create SPResults
DECLARE @SPResults TABLE(
  	-- Create Weekday
	Weekday nvarchar(30),
    -- Create Borough
	Borough nvarchar(30),
    -- Create AvgFarePerKM
	AvgFarePerKM nvarchar(30),
    -- Create RideCount
	RideCount	nvarchar(30),
    -- Create TotalRideMin
	TotalRideMin	nvarchar(30))

-- Insert the results into @SPResults
INSERT INTO @SPResults
-- Execute the SP
EXEC dbo.cuspBoroughRideStats

-- Select all the records from @SPresults 
SELECT * 
FROM @SPresults;
""")

if cursor.nextset():
    message_row = cursor.fetchone()
    if message_row:
        print(f'Message: {message_row[0]}')
else:
    print(f'Commands completed successfully.')
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