import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=datacamp;" "Trusted_Connection=True;" )
cursor = conn.cursor()

variable_query = """
"""
# cursor.execute(variable_query)
# conn.commit()

select_query = """
SELECT OrderDate, TerritoryName, 
       -- Calculate the standard deviation
	STDEV(OrderPrice) 
       OVER(PARTITION BY TerritoryName ORDER BY OrderDate) AS StdDevPrice	  
FROM Orders
"""

df = pd.read_sql(select_query, conn)
print(df)
cursor.close()
conn.close()