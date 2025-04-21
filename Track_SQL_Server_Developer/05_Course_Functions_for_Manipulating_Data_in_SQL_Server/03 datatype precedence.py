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
	bean_type,
	rating
FROM ratings
WHERE rating > 3;
"""

df = pd.read_sql(select_query, conn)
print(df)
cursor.close()
conn.close()