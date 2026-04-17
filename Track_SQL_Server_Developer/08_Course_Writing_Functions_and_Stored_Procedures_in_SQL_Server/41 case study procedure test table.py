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

results = []
columns = None

while True:
    if cursor.description:
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        df = pd.DataFrame.from_records(rows, columns=columns)
        results.append(df)

    if not cursor.nextset():
        break

if results:
    final_df = pd.concat(results, ignore_index=True)
    print(final_df)
else:
    print("Commands completed successfully.")

conn.commit()
cursor.close()
conn.close()
