# Import pandas
import pandas as pd

# Assign spreadsheet filename: file
file = r'D:\STUDY\python\Review\13 import data\datasets\battledeath.xlsx'

# Load spreadsheet: xls
xls = pd.ExcelFile(file)
# xls = pd.ExcelFile(file, engine='xlrd')

# Print sheet names
print(xls.sheet_names)
