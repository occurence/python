import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=datacamp;" "Trusted_Connection=True;" )
cursor = conn.cursor()

variable_query = """
"""
# cursor.execute(variable_query)
# conn.commit()

select_query = """
SELECT
	-- Determine the week of the calendar year
	c.CalendarWeekOfYear,
	-- Determine the earliest DATE in this group
    -- This is NOT the DayOfWeek column
	MIN(c.Date) AS FirstDateOfWeek,
	ISNULL(SUM(dsv.AmenityUseInMinutes), 0) AS AmenityUseInMinutes,
	ISNULL(MAX(dsv.CustomerID), 0) AS HighestCustomerID,
	COUNT(dsv.CustomerID) AS NumberOfAttendees
FROM dbo.Calendar c
	LEFT OUTER JOIN dbo.DaySpaVisit dsv
		-- Connect dbo.Calendar with dbo.DaySpaVisit
		-- To join on CustomerVisitStart, we need to turn 
        -- it into a DATE type
		ON c.Date = CAST(dsv.CustomerVisitStart AS DATE)
WHERE
	c.CalendarYear = 2020
GROUP BY
	-- When we use aggregation functions like SUM or COUNT,
    -- we need to GROUP BY the non-aggregated columns
	c.CalendarWeekOfYear
ORDER BY
	c.CalendarWeekOfYear;
"""

df = pd.read_sql(select_query, conn)
print(df)
cursor.close()
conn.close()