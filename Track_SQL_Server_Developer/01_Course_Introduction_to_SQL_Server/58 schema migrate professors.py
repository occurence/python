import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=datacamp;" "Trusted_Connection=True;" )
cursor = conn.cursor()

variable_query = """
-- Insert unique professors into the new table
INSERT INTO professors 
SELECT DISTINCT firstname, lastname, university_shortname 
-- FROM university_professors;
FROM college;
"""
cursor.execute(variable_query)
conn.commit()

select_query = """
-- Doublecheck the contents of professors
SELECT * 
FROM professors;
"""

df = pd.read_sql(select_query, conn)
print(df)
cursor.close()
conn.close()