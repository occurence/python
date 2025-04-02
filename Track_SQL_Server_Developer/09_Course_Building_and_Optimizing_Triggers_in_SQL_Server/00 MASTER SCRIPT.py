import runpy
import os

scripts_to_run = [
    "01 schema migrate discounts.py",
    "02 schema migrate orders.py",
    "03 schema migrate products.py",
    "04 schema migrate productshistory.py",
    "10 schema migrate saleswithprice.py",
    "12 schema migrate saleswithoutprice.py",
]

SCRIPT_DIR = "D:\\STUDY\\python\\Track_SQL_Server_Developer\\09_Course_Building_and_Optimizing_Triggers_in_SQL_Server\\"

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
extract_path = r"D:\STUDY\python\Track_SQL_Server_Developer\09_Course_Building_and_Optimizing_Triggers_in_SQL_Server"
os.makedirs(extract_path, exist_ok=True)
import os
extracted_files = os.listdir(extract_path)
print(",\n".join(f'    "{file}"' for file in extracted_files))
"""