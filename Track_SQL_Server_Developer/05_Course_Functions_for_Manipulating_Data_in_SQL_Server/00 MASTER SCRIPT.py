import runpy
import os

scripts_to_run = [
    "00.5 schema migrate ratings.py",
    "00.5 schema migrate voters.py", 
    "01 alter.py",
]

SCRIPT_DIR = "D:\\STUDY\\python\\Track_SQL_Server_Developer\\05_Course_Functions_for_Manipulating_Data_in_SQL_Server\\"

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
extract_path = r"D:\STUDY\python\Track_SQL_Server_Developer\05_Course_Functions_for_Manipulating_Data_in_SQL_Server"
os.makedirs(extract_path, exist_ok=True)
import os
extracted_files = os.listdir(extract_path)
print(",\n".join(f'    "{file}"' for file in extracted_files))
"""