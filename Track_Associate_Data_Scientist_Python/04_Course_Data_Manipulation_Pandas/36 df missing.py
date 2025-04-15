import pandas as pd
avocados = pd.read_pickle(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\04_Course_Data_Manipulation_Pandas\avoplotto.pkl')
import matplotlib.pyplot as plt
avocados_2016 = avocados[avocados['year'] == 2016]
# print(avocados_2016)
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