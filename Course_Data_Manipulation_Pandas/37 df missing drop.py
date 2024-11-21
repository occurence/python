import pandas as pd
avocados = pd.read_pickle(r'D:\STUDY\python\Course_Data_Manipulation_Pandas\avoplotto.pkl')
import matplotlib.pyplot as plt
avocados_2016 = avocados[avocados['year'] == 2016]

# Remove rows with missing values
avocados_complete = avocados_2016.dropna()

# Check if any columns contain missing values
print(avocados_complete.isna().any())