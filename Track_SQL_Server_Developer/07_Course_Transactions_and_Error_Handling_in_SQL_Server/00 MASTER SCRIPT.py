import runpy
import os

scripts_to_run = [
    # "00 LIST FILES.py",
    "01 schema database tehandling.py",
    "02 try catch fail.py",
    "03 try catch success.py",
    "04 alter.py",
    "05 try catch nested.py",
    "06 error list.py",
    "07 errors uncaught.py",
    "08 errors compilation.py",
    "09 errors function.py",
    "10 errors function nested.py",
    "11 errors cast.py",
    "12 errors function nested.py",
]

SCRIPT_DIR = "D:\\STUDY\\python\\Track_SQL_Server_Developer\\07_Course_Transactions_and_Error_Handling_in_SQL_Server\\"

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
extract_path = r"D:\STUDY\python\Track_SQL_Server_Developer\07_Course_Transactions_and_Error_Handling_in_SQL_Server"
os.makedirs(extract_path, exist_ok=True)
import os
extracted_files = os.listdir(extract_path)
print(",\n".join(f'    "{file}"' for file in extracted_files))
"""