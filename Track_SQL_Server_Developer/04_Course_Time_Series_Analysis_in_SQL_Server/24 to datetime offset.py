import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=datacamp;" "Trusted_Connection=True;" )
cursor = conn.cursor()

variable_query = """
"""
# cursor.execute(variable_query)
# conn.commit()

select_query = """
DECLARE
	@OlympicsClosingUTC DATETIME2(0) = '2016-08-21 23:00:00';

SELECT
	-- Fill in 7 hours back and a '-07:00' offset
	TODATETIMEOFFSET(DATEADD(HOUR, -7, @OlympicsClosingUTC), '-07:00') AS PhoenixTime,
	-- Fill in 12 hours forward and a '+12:00' offset.
	TODATETIMEOFFSET(DATEADD(HOUR, 12, @OlympicsClosingUTC), '+12:00') AS TuvaluTime;
"""

df = pd.read_sql(select_query, conn)
print(df)
cursor.close()
conn.close()