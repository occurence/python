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
    "13.1 raiserror success.py",
    # "13.2 raiserror fail.py",
    "13.3 raiserror try catch success.py",
    "13.4 raiserror try catch fail.py",
    "14 throw noparam.py",
    "15 throw message.py",
    "16 throw param.py",
    "17.1 throw concat success.py",
    # "17.2 throw concat fail.py",
    "18.1 throw formatmessage string success.py",
    # "18.2 throw formatmessage string fail.py",
    "19.1 throw formatmessage number success.py",
    # "19.2 throw formatmessage number fail.py",
    # "20 transaction commit.py", #
    # "21 transaction rollback.py",
    # "22 transaction begin tran.py", #
    # "23 transaction trancount.py", #
    # "24 transaction savepoint.py", #
    # "25 transaction xact throw.py",
    # "26.1 transaction xact doom XACT_STATE.py",
    # "26.2 transaction xact doom no XACT_STATE.py",
    # "27 isolation read uncommitted.py",
    # "28 isolation read committed.py",
    # "29 isolation repeatable read.py",
    # "30 isolation serializable table.py",
    # "31 isolation serializable range.py",
    # "32 isolation nolock.py",
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