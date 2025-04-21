import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=DatabaseDesign;" "Trusted_Connection=True;" )
cursor = conn.cursor()

cursor.execute("""
-- Create a new table called film_descriptions
DROP TABLE IF EXISTS film_descriptions;
CREATE TABLE film_descriptions (
    film_id INT,
    long_description TEXT
);
""")
conn.commit()

cursor.execute("""
-- Copy the descriptions from the film table
INSERT INTO film_descriptions
SELECT film_id, long_description FROM film;
""")
conn.commit()

cursor.execute("""
-- Drop the descriptions from the original table
ALTER TABLE film DROP COLUMN long_description;
""")
conn.commit()

select_query = """
-- Join to view the original table
-- SELECT * FROM film 
-- JOIN film_descriptions USING(film_id);
SELECT * FROM film 
JOIN film_descriptions
ON film_descriptions.film_id = film.film_id;
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