import pandas as pd
import matplotlib.pyplot as plt

avocados = pd.read_pickle(r'D:\STUDY\python\Review\04 dataframe inspect\avoplotto.pkl')
# avocados_2016 = avocados[avocados['year'] == 2016]
avocados_2016 = pd.read_csv(r'D:\STUDY\python\Review\04 dataframe inspect\avocados_2016.csv', index_col=0)

# Remove rows with missing values
avocados_complete = avocados_2016.dropna()

# Check if any columns contain missing values
print(avocados_complete.isna().any())