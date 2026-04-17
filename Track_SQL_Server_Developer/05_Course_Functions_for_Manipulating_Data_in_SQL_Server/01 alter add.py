import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=datacamp;" "Trusted_Connection=True;" )
cursor = conn.cursor()

variable_query = """
ALTER TABLE voters
ADD last_vote_date date;

ALTER TABLE voters
ADD last_vote_time time;

ALTER TABLE voters
ADD last_login datetime2;
"""
cursor.execute(variable_query)
conn.commit()

select_query = """
    SELECT COLUMN_NAME, DATA_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'voters';
"""

df = pd.read_sql(select_query, conn)
print(df)
cursor.close()
conn.close()