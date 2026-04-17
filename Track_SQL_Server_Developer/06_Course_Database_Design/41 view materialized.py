import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=DatabaseDesign;" "Trusted_Connection=True;" )
cursor = conn.cursor()

cursor.execute("""
DROP VIEW IF EXISTS genre_count;
""")
conn.commit()

cursor.execute("""
-- Create a materialized view called genre_count 
-- CREATE MATERIALIZED VIEW genre_count AS
CREATE VIEW genre_count
WITH SCHEMABINDING
AS
SELECT genre, COUNT_BIG(*) AS genre_total
FROM dbo.genres
GROUP BY genre;
""")
conn.commit()

cursor.execute("""
CREATE UNIQUE CLUSTERED INDEX idx_genre_count
ON genre_count (genre);
""")
conn.commit()

cursor.execute("""
INSERT INTO genres
VALUES (50000, 'classical');
""")
conn.commit()

select_query = """
-- Get all non-systems views
SELECT * FROM information_schema.views
WHERE table_schema not in ('pg_catalog', 'information_schema');

SELECT * FROM genre_count;
"""

cursor.execute(select_query)

results = []
while True:
    rows = cursor.fetchall()
    if not rows:
        break
    columns = [column[0] for column in cursor.description]
    df = pd.DataFrame.from_records(rows, columns=columns)
    results.append(df)
    if not cursor.nextset():
        break
    
for i, df in enumerate(results, start=1):
    print(f'{i} SELECT STATEMENT\n, {df}\n')
cursor.close()
conn.close()