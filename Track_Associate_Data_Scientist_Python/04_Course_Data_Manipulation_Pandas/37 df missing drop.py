import pandas as pd
avocados = pd.read_pickle(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\04_Course_Data_Manipulation_Pandas\avoplotto.pkl')
import matplotlib.pyplot as plt
avocados_2016 = avocados[avocados['year'] == 2016]

# Remove rows with missing values
avocados_complete = avocados_2016.dropna()

# Check if any columns contain missing values
print(avocados_complete.isna().any())