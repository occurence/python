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
    -- Get the prior day's number of incidents
	LAG(ir.NumberOfIncidents, 1) OVER (
      	-- Partition by incident type ID
		PARTITION BY ir.IncidentTypeID
      	-- Order by incident date
		ORDER BY ir.IncidentDate
	) AS PriorDayIncidents,
	ir.NumberOfIncidents AS CurrentDayIncidents,
    -- Get the next day's number of incidents
	LEAD(ir.NumberOfIncidents, 1) OVER (
      	-- Partition by incident type ID
		PARTITION BY ir.IncidentTypeID
      	-- Order by incident date
		ORDER BY ir.IncidentDate
	) AS NextDayIncidents
FROM dbo.IncidentRollup ir
WHERE
	ir.IncidentDate >= '2019-07-02'
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