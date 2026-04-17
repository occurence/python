import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=datacamp;" "Trusted_Connection=True;" )
cursor = conn.cursor()

variable_query = """
DROP TABLE IF EXISTS professors;
-- Create a table for the professors entity type
CREATE TABLE professors(
 firstname text,
 lastname text
);

DROP TABLE IF EXISTS universities;
-- Create a table for the universities entity type
CREATE TABLE universities(
  university_shortname text,
  university text,
  university_city text
);

DROP TABLE IF EXISTS organizations;
-- Create a table for the organizations entity type
CREATE TABLE organizations(
  organization text,
  organization_sector text
);

DROP TABLE IF EXISTS affiliations;
-- Create a table for the affiliations entity type
CREATE TABLE affiliations(
  firstname text,
  lastname text,
  university_shortname text,
  function text,
  organisation text
);
"""
cursor.execute(variable_query)
conn.commit()

select_query = """
-- Print the contents of this table
SELECT * 
FROM professors;

-- Print the contents of this table
SELECT * 
FROM universities;

-- Print the contents of this table
SELECT * 
FROM organizations;

-- Print the contents of this table
SELECT *
FROM affiliations;
"""

df = pd.read_sql(select_query, conn)
print(df)
cursor.close()
conn.close()