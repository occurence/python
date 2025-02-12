import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=datacamp;" "Trusted_Connection=True;" )
cursor = conn.cursor()

variable_query = """
-- Add the university_shortname column
ALTER TABLE professors
-- ADD COLUMN university_shortname text;
ADD university_shortname text;
"""
cursor.execute(variable_query)
conn.commit()

select_query = """
-- Print the contents of this table
SELECT * 
FROM professors;
"""

df = pd.read_sql(select_query, conn)
print(df)
cursor.close()
conn.close()