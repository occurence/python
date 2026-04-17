import runpy
import os

scripts_to_run = [
    "00 schema drop create.py",
    "00 schema migrate.py",
    # "01 schema information.py",# --
    "02 schema create table.py",
    "03 schema alter column.py",
    "04 schema alter rename column.py",
    "05 schema alter drop column.py",
    "06 schema migrate professors.py",
    "07 schema migrate universities.py",
    "08 schema migrate organizations.py",
    "09 schema migrate affiliations.py",
    # "10 schema drop migrate origin.py",# --
    "11 datatypes.py",
    # "12 cast.py",# --
    "13 alter type.py",
    "14 alter using.py",
    "15 constraint not null.py",
    "16 constraint unique.py",
    # "17 count distinct.py",
    # "18 minimal superkey.py",# --
    "19 constraint primary key.py",
    "20 constraint surrogate key serial.py",
    "21 schema migrate cars.py",
    "22 constraint surrogate key concat.py",
    "23 constraint creation.py",
    "24 constraint foreign key.py",
    # "25 constraint foreign key insert error.py",# --
    "26 constraint foreign key insert success.py",
    # "27 constraint foreign key join.py",# --
    "28 relationship nm.py",
    "29 populate reference column.py",
    "30 drop referenced column.py",
    "31 referential integrity on delete.py",
    # "32 query join count.py",# --
    # "33 query join all.py",# --
    # "34 query join all filter.py",# --
]

SCRIPT_DIR = "D:\\STUDY\\python\\Track_SQL_Server_Developer\\02_Course_Introduction_to_Relational_Databases_in_SQL\\"

# Execute each script in the list
for script in scripts_to_run:
    script_path = os.path.join(SCRIPT_DIR, script)
    print(f"Executing: {script_path}")
    
    try:
        runpy.run_path(script_path)
    except Exception as e:
        print(f"Error in {script}: {e}")
