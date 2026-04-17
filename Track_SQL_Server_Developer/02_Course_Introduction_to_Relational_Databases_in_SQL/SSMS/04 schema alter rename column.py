import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=datacamp;" "Trusted_Connection=True;" )
cursor = conn.cursor()

variable_query = """
-- ALTER TABLE affiliations
-- RENAME COLUMN organisation TO organization
EXEC sp_rename 'affiliations.organisation', 'organization', 'COLUMN';
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