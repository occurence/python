import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=DatabaseDesign;" "Trusted_Connection=True;" )
cursor = conn.cursor()

try:
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
  
    row = cursor.fetchone()
    while row:
        print(f"ReturnCode: {row.ReturnCode}, ErrorMessage: {row.ErrorMessage}")
        row = cursor.fetchone()

except pyodbc.Error as e:
    print("Database error occurred:", e)
except Exception as ex:
    print("An error occurred:", ex)
finally:
    cursor.close()
    conn.close()
