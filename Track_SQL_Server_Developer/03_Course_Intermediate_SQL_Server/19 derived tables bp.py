import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=datacamp;" "Trusted_Connection=True;" )
cursor = conn.cursor()

variable_query = """
"""
# cursor.execute(variable_query)
# conn.commit()

select_query = """
SELECT *
FROM Kidney a
-- Create derived table: select age, max blood pressure from kidney grouped by age
JOIN (SELECT Age, MAX(BloodPressure) AS MaxBloodPressure FROM Kidney GROUP BY Age) b
-- JOIN on BloodPressure equal to MaxBloodPressure
ON a.BloodPressure = b.MaxBloodPressure
-- Join on Age
AND a.Age = b.Age
"""

df = pd.read_sql(select_query, conn)
print(df)
cursor.close()
conn.close()