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
	ir.IncidentDate,
	ir.IncidentTypeID,
    -- Fill in two periods ago
	LAG(ir.NumberOfIncidents, 2) OVER (
		PARTITION BY ir.IncidentTypeID
		ORDER BY ir.IncidentDate
	) AS Trailing2Day,
    -- Fill in one period ago
	LAG(ir.NumberOfIncidents, 1) OVER (
		PARTITION BY ir.IncidentTypeID
		ORDER BY ir.IncidentDate
	) AS Trailing1Day,
	ir.NumberOfIncidents AS CurrentDayIncidents,
    -- Fill in next period
	LEAD(ir.NumberOfIncidents, 1) OVER (
		PARTITION BY ir.IncidentTypeID
		ORDER BY ir.IncidentDate
	) AS NextDay
FROM dbo.IncidentRollup ir
WHERE
	ir.IncidentDate >= '2019-07-01'
	AND ir.IncidentDate <= '2019-07-31'
	AND ir.IncidentTypeID IN (1, 2)
ORDER BY
	ir.IncidentTypeID,
	ir.IncidentDate;
"""

df = pd.read_sql(select_query, conn)
print(df)
cursor.close()
conn.close()