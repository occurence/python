import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=datacamp;" "Trusted_Connection=True;" )
cursor = conn.cursor()

variable_query = """
-- Insert unique organizations into the new table
INSERT INTO organizations 
SELECT DISTINCT organization, organization_sector
FROM university_professors;
"""
cursor.execute(variable_query)
conn.commit()

select_query = """
-- Doublecheck the contents of organizations
SELECT * 
FROM organizations;
"""

df = pd.read_sql(select_query, conn)
print(df)
cursor.close()
conn.close()