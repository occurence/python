import pandas as pd
import matplotlib.pyplot as plt

avocados = pd.read_pickle(r'D:\STUDY\python\Review\04 dataframe inspect\avoplotto.pkl')
# avocados_2016 = avocados[avocados['year'] == 2016]
avocados_2016 = pd.read_csv(r'D:\STUDY\python\Review\04 dataframe inspect\avocados_2016.csv', index_col=0)

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Check individual values for missing values
print(avocados_2016.isna())

# Check each column for missing values
print(avocados_2016.isna().any())

# Bar plot of missing values by variable
avocados_2016.isna().sum().plot(kind='bar')

# Show plot
plt.show()