import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=DatabaseDesign;" "Trusted_Connection=True;" )
cursor = conn.cursor()

cursor.execute("""
DROP VIEW IF EXISTS top_15_2017;
""")
conn.commit()

cursor.execute("""
CREATE VIEW top_15_2017 AS
SELECT TOP 15 reviews.reviewid,
    reviews.title,
    reviews.score
   FROM reviews
  WHERE (reviews.pub_year = 2017)
  ORDER BY reviews.score DESC;
""")
conn.commit()

cursor.execute("""
DROP VIEW IF EXISTS artist_title;
""")
conn.commit()

cursor.execute("""
CREATE VIEW artist_title AS
SELECT reviews.reviewid,
reviews.title,
artists.artist
FROM (reviews
    JOIN artists ON ((artists.reviewid = reviews.reviewid)));
""")
conn.commit()

select_query = """
-- Get all non-systems views
SELECT * FROM information_schema.views
WHERE table_schema not in ('pg_catalog', 'information_schema');
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