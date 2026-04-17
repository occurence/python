import os
extract_path = r"D:\STUDY\python\Track_SQL_Server_Developer\09_Course_Building_and_Optimizing_Triggers_in_SQL_Server"
os.makedirs(extract_path, exist_ok=True)
import os
import pandas as pd
extracted_files = os.listdir(extract_path)
print(",\n".join(f'    "{file}"' for file in extracted_files))