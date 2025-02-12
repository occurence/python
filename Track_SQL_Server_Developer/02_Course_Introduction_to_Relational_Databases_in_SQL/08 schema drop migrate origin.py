import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=datacamp;" "Trusted_Connection=True;" )
cursor = conn.cursor()

variable_query = """
-- Delete the university_professors table
-- DROP TABLE university_professors;
DROP TABLE college;
"""
cursor.execute(variable_query)
conn.commit()

select_query = """
-- Doublecheck the contents of college
SELECT * 
FROM college;
"""

df = pd.read_sql(select_query, conn)
print(df)
cursor.close()
conn.close()