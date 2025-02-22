import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=datacamp;" "Trusted_Connection=True;" )
cursor = conn.cursor()

variable_query = """
"""
# cursor.execute(variable_query)
# conn.commit()

select_query = """
-- Round Cost to the nearest dollar
SELECT Cost, 
       ROUND(Cost, 0) AS RoundedCost
FROM Shipments
"""

df = pd.read_sql(select_query, conn)
print(df)
cursor.close()
conn.close()