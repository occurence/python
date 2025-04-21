import runpy
import os

scripts_to_run = [
    "01 schema migrate NBA Players.py",
    "02 schema migrate NBA PlayerStats.py",
    "03 schema migrate NBA Teams.py",
    "08 schema migrate Earthquakes.py",
    "09 schema migrate Nations.py",
    "10 schema migrate Cities.py",
    "44 schema migrate Orders.py",
    "45 schema migrate Customers.py",
]

SCRIPT_DIR = "D:\\STUDY\\python\\Track_SQL_Server_Developer\\10_Course_Improving_Query_Performance_in_SQL_Server\\"

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
extract_path = r"D:\STUDY\python\Track_SQL_Server_Developer\10_Course_Improving_Query_Performance_in_SQL_Server"
os.makedirs(extract_path, exist_ok=True)
import os
extracted_files = os.listdir(extract_path)
print(",\n".join(f'    "{file}"' for file in extracted_files))
"""