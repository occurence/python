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
	it.IncidentType,
    -- Fill in the appropriate expression
	SUM(CASE WHEN ir.NumberOfIncidents > 5 THEN 1 ELSE 0 END) AS NumberOfBigIncidentDays,
    -- Number of incidents will always be at least 1, so
    -- no need to check the minimum value, just that it's
    -- less than or equal to 5
    SUM(CASE WHEN ir.NumberOfIncidents <= 5 THEN 1 ELSE 0 END) AS NumberOfSmallIncidentDays
FROM dbo.IncidentRollup ir
	INNER JOIN dbo.IncidentType it
		ON ir.IncidentTypeID = it.IncidentTypeID
WHERE
	ir.IncidentDate BETWEEN '2019-08-01' AND '2019-10-31'
GROUP BY
it.IncidentType;
"""

df = pd.read_sql(select_query, conn)
print(df)
cursor.close()
conn.close()