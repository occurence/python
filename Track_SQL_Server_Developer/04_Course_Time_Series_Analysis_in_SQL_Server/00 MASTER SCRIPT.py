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