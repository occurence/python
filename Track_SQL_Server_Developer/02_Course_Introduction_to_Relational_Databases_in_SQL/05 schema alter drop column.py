import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=datacamp;" "Trusted_Connection=True;" )
cursor = conn.cursor()

variable_query = """
-- Delete the university_shortname column
ALTER TABLE affiliations
DROP COLUMN university_shortname;
"""
cursor.execute(variable_query)
conn.commit()

select_query = """
-- Print the contents of this table
SELECT *
FROM affiliations;
"""

df = pd.read_sql(select_query, conn)
print(df)
cursor.close()
conn.close()