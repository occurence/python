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
	first_name,
	last_name,     
	total_votes
FROM voters
WHERE total_votes > '120'
"""

df = pd.read_sql(select_query, conn)
print(df)
cursor.close()
conn.close()