import pandas as pd
import pyodbc

# Define the SQL Server connection
conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=localhost;"
    "DATABASE=master;"
    "Trusted_Connection=yes;"
)

# Read the eurovis.csv file
eurovision = pd.read_csv(r'D:\STUDY\python\Track_SQL_Server_Developer\01_Course_Introduction_to_SQL_Server\datasets\eurovis.csv')

# Create a temporary table (or use an existing one)
eurovision.to_sql("eurovision", conn, index=False, if_exists="replace")

# Query the database
query = """
SELECT TOP (50) country FROM eurovision;
"""

result = pd.read_sql(query, conn)

# Print the result
print(result)

# Close the connection
conn.close()
