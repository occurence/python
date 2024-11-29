# Loading in required libraries
import pandas as pd
import seaborn as sns
import numpy as np

# Start coding here!

nobel = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\10_Project_Visualizing_History_Nobel_Prize_Winners\nobel.csv')
nobel_sex = nobel['sex'].value_counts().index[0]
nobel_country = nobel['birth_country'].value_counts().index[0]
nobel_count = nobel['birth_country'].value_counts()
nobel['flag'] = nobel['birth_country'].map(nobel_count)
nobel['decade'] = (np.floor(nobel['year'] / 10) * 10).astype(int)

# plt.show()

# print(nobel.groupby('category')[['category','sex']].count())
# print(nobel[nobel['sex'] == 'Female'])
print(nobel[nobel['sex'] == 'Female'].groupby('category')['category'].count())