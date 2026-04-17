import runpy
import os

scripts_to_run = [
    "00.5 schema migrate ratings.py",
    "00.5 schema migrate voters.py", 
    "01 alter.py",
    # "02 implicit conversion.py",
    # "03 datatype precedence.py",
    # "04 cast.py",
    # "05 convert.py",
    # "06 datatype.py",
    # "07 system date.py",
    # "08 system date parts.py",
    # "09 function parts extract.py",
    # "10 datename descriptive.py",
    # "11 datename datepart.py",
    # "12 datefromparts.py",
    # "13 arithmetic.py",
    # "14 date manipulation.py",
    # "15 date between.py",
    # "16 isdate dateformat ydm.py",
    # "17 isdate dateformat dym.py",
    # "18 isdate dateformat mdy.py",
    # "19 isdate dateformat dmy.py",
    # "20 language dutch.py",
    # "21 language croatian.py",
    # "22 language english.py",
    # "23 date functions.py",
    # "24 string functions len.py",
    # "25 string functions charindex.py",
    # "26 string functions patindex.py",
    # "27 string functions lower upper.py",
    # "28 string functions left right.py",
    # "29 string functions substring.py",
    # "30 string functions replace.py",
    # "31 string function group strings.py",
    # "32 string function string_agg.py",
    # "33 string function string_agg grouped.py",
    # "34 string function string_agg grouped ordered.py",
    # "35 string function string_split sentence.py",
    # "36 string function string_split word.py",
    # "37 string function all applied function format.py",
    # "38 arithmetic function count sum.py",
    # "39 arithmetic function avg min max.py",
    # "40 analytic function lead.py",
    # "41 analytic function lag.py",
    # "42 analytic function first last values.py",
    # "43 mathematical function abs sign.py",
    # "44 mathematical function round ceiling floor.py",
    # "45 exponential function power square sqrt.py",
    # "46 manipulating numeric data.py",
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