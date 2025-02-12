import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=datacamp;" "Trusted_Connection=True;" )
cursor = conn.cursor()

variable_query = """
"""
cursor.execute(variable_query)
conn.commit()

select_query = """
-- Query the right table in information_schema to get columns
SELECT column_name, data_type 
FROM information_schema.columns 
WHERE table_name = 'college' AND table_schema = 'dbo';
"""

df = pd.read_sql(select_query, conn)
print(df)
cursor.close()
conn.close()