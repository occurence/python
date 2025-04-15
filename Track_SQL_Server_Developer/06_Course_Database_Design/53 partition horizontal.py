import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=DatabaseDesign;" "Trusted_Connection=True;" )
cursor = conn.cursor()

cursor.execute("""
DROP VIEW IF EXISTS film_partitioned;
""")
conn.commit()

cursor.execute("""
-- Create a new table called film_partitioned
CREATE VIEW film_partitioned AS
SELECT * FROM film_2019
UNION ALL
SELECT * FROM film_2018
UNION ALL
SELECT * FROM film_2017;
""")
conn.commit()

cursor.execute("""
-- Create the partitions for 2019, 2018, and 2017
DROP TABLE IF EXISTS film_2019;
CREATE TABLE film_2019 (
    film_id INT,
    title NVARCHAR(255) NOT NULL,
    release_year NVARCHAR(4) CHECK (release_year = '2019')
);

DROP TABLE IF EXISTS film_2018;
CREATE TABLE film_2018 (
    film_id INT,
    title NVARCHAR(255) NOT NULL,
    release_year NVARCHAR(4) CHECK (release_year = '2018')
);

DROP TABLE IF EXISTS film_2017;
CREATE TABLE film_2017 (
    film_id INT,
    title NVARCHAR(255) NOT NULL,
    release_year NVARCHAR(4) CHECK (release_year = '2017')
);
""")
conn.commit()

cursor.execute("""
-- Insert the data into film_partitioned
INSERT INTO film_2019 (film_id, title, release_year)
SELECT film_id, title, release_year
FROM film
WHERE release_year = '2019';

INSERT INTO film_2018 (film_id, title, release_year)
SELECT film_id, title, release_year
FROM film
WHERE release_year = '2018';

INSERT INTO film_2017 (film_id, title, release_year)
SELECT film_id, title, release_year
FROM film
WHERE release_year = '2017';
""")
conn.commit()

select_query = """
-- View film_partitioned
SELECT * FROM film_partitioned;
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