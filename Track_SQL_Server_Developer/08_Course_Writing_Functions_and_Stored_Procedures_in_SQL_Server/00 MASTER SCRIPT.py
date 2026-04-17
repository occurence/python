import runpy
import os

scripts_to_run = [
    "01 schema migrate CapitalBikeShare.py",
    "02 schema migrate RideSummary.py",
    # "03 date convert.py",
    # "04 date datepart.py",
    # "05 date datename datediff.py",
    # "06 date outlier.py",
    # "07 date variable.py",
    # "08 table variable shifts.py",
    # "09_table_variable_rides.py",
    # "10_date_param.py",
    # "11_date_first_month.py",
    "12 function noparam GetYesterday.py",
    "13 function param SumRideHrsSingleDay.py",
    "14 function params SumRideHrsDateRange.py",
    "15 function params SumStationStats.py",
    "16 function params CountTripAvgDuration.py",
    # "17 function scalar select.py",
    # "18 function scalar exec.py",
    # "19 function table variable.py",
    "20 function schemabinding create or alter.py",
    "21 procedure read.py",
    "22 procedure create.py",
    "23 procedure update.py",
    "24 procedure delete.py",
    # "25 exec output.py",
    # "26 exec return.py",
    # "27 exec output return.py", #
    "28 procedure delete try.py",
    "29 procedure delete catch.py",
    "30 schema migrate YellowTripData.py",
    # "31 case study impossible scenarios.py",
    "32 case study procedure cuspImputeTripDistanceMean.py",
    "33 case study procedure GetTripDistanceHotDeck.py",
    "34 case study function ConvertMileToKm.py",
    "35 case study function ConvertDollar.py",
    "36 case study function GetShiftNumber.py",
    # "37 case study function test.py",
    # "38 case study procedure test hotdeck.py",
    "39 schema migrate TaxiZoneLookup.py",
    "40 case study procedure cuspBoroughRideStats.py",
    # "41 case study procedure test table.py",
    "42 case study procedure cuspPickupZoneShiftStats.py",
    # "43 case study procedure test.py",
]

SCRIPT_DIR = "D:\\STUDY\\python\\Track_SQL_Server_Developer\\08_Course_Writing_Functions_and_Stored_Procedures_in_SQL_Server\\"

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
extract_path = r"D:\STUDY\python\Track_SQL_Server_Developer\08_Course_Writing_Functions_and_Stored_Procedures_in_SQL_Server"
os.makedirs(extract_path, exist_ok=True)
import os
extracted_files = os.listdir(extract_path)
print(",\n".join(f'    "{file}"' for file in extracted_files))
"""