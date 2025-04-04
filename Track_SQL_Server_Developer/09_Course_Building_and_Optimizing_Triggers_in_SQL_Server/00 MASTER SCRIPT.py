import runpy
import os

scripts_to_run = [
    "01 schema migrate discounts.py",
    "02 schema migrate orders.py",
    "03 schema migrate products.py",
    "04 schema migrate productshistory.py",
    "05 trigger instead PreventDiscountsDelete.py",
    "06 trigger after OrdersUpdatedRows.py",
    "07 trigger after ProductsNewItems.py",
    "08 procedure MonthlyOrders.py",
    "09 schema migrate discountshistory.py",
    "10 trigger after CustomerDiscountHistory.py",
    "11 schema migrate saleswithprice.py",
    "12 trigger after SalesCalculateTotalAmount.py",
    "13 schema migrate saleswithoutprice.py",
    "14 insert saleswithprice.py",#
    "15 insert saleswithoutprice.py",#
    "16 schema migrate retiredproducts.py",
    "17 trigger after TrackRetiredProducts.py",
    # "18 delete products.py",#
    "19 schema migrate cancelledorders.py",
    "20 trigger after KeepCanceledOrders.py",
    "21 trigger after CustomerDiscountHistory.py",
    "22 trigger after NewOrderAlert.py",
    "23 trigger instead PreventOrdersUpdate.py",
    # "24 update orders.py",#
    "25 trigger instead PreventNewDiscounts.py",
    "26 schema migrate tableschangelog.py",
    # "27 trigger for TrackTableChanges database.py",#
    # "28 trigger for PreventTableDeletion database.py",#
    "29 schema migrate serverlogonlog.py",
    "30 insert ServerLogonLog.py",
    # "31 trigger for LogonAudit server.py",#
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