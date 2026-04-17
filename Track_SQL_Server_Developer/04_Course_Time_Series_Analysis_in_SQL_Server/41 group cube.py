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
	-- Use the ORDER BY clause as a guide for these columns
    -- Don't forget that comma after the third column if you
    -- copy from the ORDER BY clause!
	ir.IncidentTypeID,
	c.CalendarQuarterName,
	c.WeekOfMonth,
	SUM(ir.NumberOfIncidents) AS NumberOfIncidents
FROM dbo.IncidentRollup ir
	INNER JOIN dbo.Calendar c
		ON ir.IncidentDate = c.Date
WHERE
	ir.IncidentTypeID IN (3, 4)
GROUP BY
	-- GROUP BY should include all non-aggregated columns
	ir.IncidentTypeID,
	c.CalendarQuarterName,
	c.WeekOfMonth
-- Fill in your grouping operator
WITH CUBE
ORDER BY
	ir.IncidentTypeID,
	c.CalendarQuarterName,
	c.WeekOfMonth;
"""

df = pd.read_sql(select_query, conn)
print(df)
cursor.close()
conn.close()