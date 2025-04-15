import runpy
import os

scripts_to_run = [
    "00 schema migrate.py",
    # "01 agg.py",# --
    # "02 agg group.py",# --
    # "03 not missing values.py",# --
    # "04 not missing values impute isnull.py",# --
    # "05 not missing values replace coalesce.py",# --
    # "06 case.py",# --
    # "07 case group.py",# --
    "07.5 schema migrate.py",
    # "08 sum.py",# --
    # "09 count.py",# --
    # "10 datediff.py",# --
    # "11 dateadd.py",# --
    # "12 round.py",# --
    # "13 truncate.py",# --
    # "14 absolute.py",# --
    # "15 square sqrt.py",# --
    # "16 variable.py",# --
    # "17 while loop.py",# --
    # "18 derived tables glucose.py",# --
    # "19 derived tables bp.py",# --
    # "20 CTE glucose.py",# --
    # "21 CTE bp.py",# --
    "21.5 migrate.py",
    # "22 window sum.py",# --
    # "23 window count.py",# --
    # "24 window first.py",# --
    # "25 window lead lag.py",# --
    # "26 window running total.py",# --
    # "27 window row number.py",# --
    # "28 window stdev.py",# --
    # "29 window mode list.py",# --
    # "30 window mode max.py",# --
]

SCRIPT_DIR = "D:\\STUDY\\python\\Track_SQL_Server_Developer\\03_Course_Intermediate_SQL_Server\\"

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
extract_path = r"D:\STUDY\python\Track_SQL_Server_Developer\03_Course_Intermediate_SQL_Server"
os.makedirs(extract_path, exist_ok=True)
import os
extracted_files = os.listdir(extract_path)
print(",\n".join(f'    "{file}"' for file in extracted_files))
"""