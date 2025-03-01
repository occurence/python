import runpy
import os

scripts_to_run = [
    # "01 datepart.py",
    # "02 datepart components.py",
    # "03 datename components.py",
    # "04 leap dateadd.py",
    # "05 leap datediff.py",
    # "06 date round.py",
    # "07 date cast.py",
    # "08 date convert.py",
    # "09 date format d.py",
    # "10 date format D.py",
    # "11 date format string.py",
    "11.5 schema migrate.py",
    # "12 calendar table calendar year.py",
    # "13 calendar table fiscalyear.py",
    "13.5 schema migrate.py",
    "14 calendar table join.py",
    # "15 calendar table join filter.py",
    # "16 datefromparts components.py",
    # "17 datefromparts components filter.py",
    # "18 datetime2fromparts.py",
    # "19 datetimeoffsetfromparts.py",
    "19.5 schema migrate.py",
    # "20 datestring cast.py",
    # "21 datestring convert.py",
    "21.5 schema migrate.py",
    # "22 datestring parse.py",
    # "23 switch offset.py",
    # "24 to datetime offset.py",
    # "25 safe try_convert.py",
    # "26 safe try_cast.py",
    # "27 safe try_parse.py",
    "27.5 schema migrate.py",
    # "28 timezone.py",
    # "29 typesafe try_cast.py",
    # "30 typesafe try_convert.py",
    # "31 typesafe try_parse.py",
    "31.5 schema migrate.py",
    # "32 aggregate timeframe.py",
    # "33 aggregate count distinct.py",
    # "34 aggregate filter case.py",
    # "35 aggregate statistical functions.py",
    # "36 aggregate median.py",
    "36.5 schema migrate.py",
    # "37 downsample day.py",
    # "38 downsample week.py",
    # "39 downsample calendar table.py",
    # "40 group rollup.py",
    # "41 group cube.py",
    # "42 group grouping sets.py",
    # "43 group multiple.py",
]

SCRIPT_DIR = "D:\\STUDY\\python\\Track_SQL_Server_Developer\\04_Course_Time_Series_Analysis_in_SQL_Server\\"

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
extract_path = r"D:\STUDY\python\Track_SQL_Server_Developer\04_Course_Time_Series_Analysis_in_SQL_Server"
os.makedirs(extract_path, exist_ok=True)
import os
extracted_files = os.listdir(extract_path)
print(",\n".join(f'    "{file}"' for file in extracted_files))
"""