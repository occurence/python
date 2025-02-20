import runpy
import os

scripts_to_run = [
    "00 schema migrate.py",
    # "01 agg.py"# --
    # "02 agg group.py",# --
    # "03 not missing values.py",# --
    # "04 not missing values impute isnull.py",# --
    # "05 not missing values replace coalesce.py",# --
    # "06 case.py",# --
    # "07 case group.py",# --
    "075 schema migrate.py",
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
