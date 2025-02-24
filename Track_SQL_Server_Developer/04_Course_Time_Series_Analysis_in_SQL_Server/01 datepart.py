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
	@SomeTime DATETIME2(7) = SYSUTCDATETIME();

-- Retrieve the year, month, and day
SELECT
	DATEPART(YEAR, @SomeTime) AS TheYear,
	DATEPART(MONTH, @SomeTime) AS TheMonth,
	DATEPART(DAY, @SomeTime) AS TheDay;
"""

df = pd.read_sql(select_query, conn)
print(df)
cursor.close()
conn.close()