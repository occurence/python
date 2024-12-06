import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

crimes = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\15_Project_Analyzing_Crime_in_Los_Angeles\crimes.csv', parse_dates=['Date Rptd', 'DATE OCC'], dtype={'TIME OCC': str})
crimes.head()

# Start coding here
# Use as many cells as you need