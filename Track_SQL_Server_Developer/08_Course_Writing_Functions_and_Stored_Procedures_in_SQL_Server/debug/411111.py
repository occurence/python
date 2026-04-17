import pyodbc
import pandas as pd

# Establish connection
conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=Arc-PC;"
    "DATABASE=DatabaseDesign;"
    "Trusted_Connection=True;"
)
cursor = conn.cursor()

# Execute the stored procedure wrapped in a table variable
cursor.execute("""
-- Create SPResults
DECLARE @SPResults TABLE(
    Weekday nvarchar(30),
    Borough nvarchar(30),
    AvgFarePerKM nvarchar(30),
    RideCount nvarchar(30),
    TotalRideMin nvarchar(30))

-- Insert the results into @SPResults
INSERT INTO @SPResults
EXEC dbo.cuspBoroughRideStats

-- Select all the records from @SPResults
SELECT * FROM @SPResults;
""")

# List to store multiple result sets
results = []

# Fetch all rows from each result set
while True:
    rows = cursor.fetchall()
    if not rows:
        break
    columns = [column[0] for column in cursor.description]  # Extract column names
    df = pd.DataFrame.from_records(rows, columns=columns)
    results.append(df)
    if not cursor.nextset():  # Move to the next result set (if any)
        break

# Combine all result sets into a single DataFrame (if multiple exist)
if results:
    final_df = pd.concat(results, ignore_index=True)
    print(final_df)
else:
    print("No data retrieved.")

# Close connection
cursor.close()
conn.close()
