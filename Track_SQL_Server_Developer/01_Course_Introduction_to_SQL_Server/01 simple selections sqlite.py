import pandas as pd
import sqlite3

# Load CSV into Pandas
eurovision = pd.read_csv(r'D:\STUDY\python\Track_SQL_Server_Developer\01_Course_Introduction_to_SQL_Server\datasets\eurovis.csv')

# Create an in-memory SQLite database
conn = sqlite3.connect(":memory:")

# Load DataFrame into SQLite
eurovision.to_sql("eurovision", conn, index=False, if_exists="replace")

# SELECT the country column FROM the eurovision table
query = """
-- SELECT the country column FROM the eurovision table
SELECT
  country
FROM
  eurovision;
"""
result = pd.read_sql(query, conn)

# Display result
print(result)

# Close the connection
conn.close()
