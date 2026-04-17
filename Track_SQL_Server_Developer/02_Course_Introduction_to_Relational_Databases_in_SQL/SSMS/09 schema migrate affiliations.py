import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=datacamp;" "Trusted_Connection=True;" )
cursor = conn.cursor()

variable_query = """
-- Insert unique affiliations into the new table
INSERT INTO affiliations 
SELECT DISTINCT firstname, lastname, function, organization 
FROM university_professors;
"""
cursor.execute(variable_query)
conn.commit()

select_query = """
-- Doublecheck the contents of affiliations
SELECT * 
FROM affiliations;
"""

df = pd.read_sql(select_query, conn)
print(df)
cursor.close()
conn.close()