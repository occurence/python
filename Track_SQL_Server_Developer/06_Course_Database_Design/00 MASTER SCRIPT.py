import runpy
import os

scripts_to_run = [
    # "00 LIST FILES.py",
    "01 schema migrate runs.py",
    "02 schema generate route_dim.py",
    "03 schema generate week_dim.py",
    "04 schema generate runs_fact.py",
    "05 query dimension.py",
    "06 schema migrate fact_booksale.py",
    "07 alter dimension star fk.py",
    "08 schema migrate book.py",
    "09 schema migrate time.py",
    "10 schema migrate store.py",
    "11 crud dimension snowflake book.py",
    # "12 join star.py",
    "13 schema migrate snowflake book.py",
    "14 schema migrate snowflake author.py",
    "15 schema migrate snowflake publisher.py",
    "16 schema migrate snowflake genre.py",
    "17 schema migrate snowflake store.py",
    "18 schema migrate snowflake city.py",
    "19 schema migrate snowflake state.py",
    "20 schema migrate snowflake country.py",
    # "21 join snowflake.py",
    "22 schema migrate snowflake continent.py",
    "23 alter snowflake country.py",
    "24 schema migrate normalization customers.py",
    "25 normalization1.py",
    "26 schema migrate normalization customer_rentals.py",
    "27 normalization2.py",
    "28 normalization3.py",
    "29 schema migrate reviews.py",
    "30 schema migrate content.py",
    "31 schema migrate artists.py",
    "32 schema migrate labels.py",
    "33 schema migrate genres.py",
    # "34 view view.py",
    "35 view query.py",
    "36 view create.py",
    "37 view join.py",
    "38 view drop cascade.py",
    "38 view drop cascade.py",
    "39 view access.py",
    "40 view redefine.py",
    "41 view materialized.py",
    "42 view materialized refresh.py",
    "50 role.py",
]

SCRIPT_DIR = "D:\\STUDY\\python\\Track_SQL_Server_Developer\\06_Course_Database_Design\\"

# Execute each script in the list
for script in scripts_to_run:
    script_path = os.path.join(SCRIPT_DIR, script)
    print(f"Executing: {script_path}")
    
    try:
        runpy.run_path(script_path)
    except Exception as e:
        print(f"Error in {script}: {e}")

"""
import os
extract_path = r"D:\STUDY\python\Track_SQL_Server_Developer\06_Course_Database_Design"
os.makedirs(extract_path, exist_ok=True)
import os
extracted_files = os.listdir(extract_path)
print(",\n".join(f'    "{file}"' for file in extracted_files))
"""