# Loading in required libraries
import pandas as pd
import seaborn as sns
import numpy as np

# Start coding here!
import matplotlib.pyplot as plt

nobel = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\10_Project_Visualizing_History_Nobel_Prize_Winners\nobel.csv')

# What is the most commonly awarded gender and birth country?
top_gender = nobel['sex'].value_counts().index[0]
top_country = nobel['birth_country'].value_counts().index[0]

print('The most awarded gender:', top_gender)
print('The most common birth country is:', top_country)

# Which decade had the highest ratio of US-born Nobel Prize winners to total winners in all categories?
nobel['usa_winner'] = nobel['birth_country'] == 'United States of America'
nobel['decade'] = (np.floor(nobel['year'] / 10) * 10).astype(int)
usa_decade = nobel.groupby('decade', as_index=False)['usa_winner'].mean()
max_decade_usa = usa_decade[usa_decade['usa_winner'] == usa_decade['usa_winner'].max()]['decade'].values[0]

print('The highest ratio of US-born winners:', max_decade_usa)
ax1 = sns.relplot(x='decade', y='usa_winner', data=nobel, kind='line')

# Which decade and Nobel Prize category combination had the highest proportion of female laureates?
nobel['female_winner'] = nobel['sex'] == 'Female'
female_decade = nobel.groupby(['decade','category'], as_index=False)['female_winner'].mean()
max_decade_female = female_decade[female_decade['female_winner'] == female_decade['female_winner'].max()][['decade','category']]

print(f"The highest proportion of female laureates is in decade: {max_decade_female['decade'].values[0]} at category: {max_decade_female['category'].values[0]}")
max_female_dict = {max_decade_female['decade'].values[0] : max_decade_female['category'].values[0] }
ax2 = sns.relplot(x='decade', y='female_winner', hue='category', data=female_decade, kind='line')

# Who was the first woman to receive a Nobel Prize, and in what category?
female_winners = nobel[nobel['female_winner']]
first_woman = female_winners[female_winners['year'] == female_winners['year'].min()]
first_woman_name = first_woman['full_name'].values[0]
first_woman_category = first_woman['category'].values[0]
print(f'The first woman to receive Nobel Prize is: {first_woman_name} in category: {first_woman_category}')

# Which individuals or organizations have won more than one Nobel Prize throughout the years?
# repeat_list
counts = nobel['full_name'].value_counts()
repeats = counts[counts >= 2].index
repeat_list = list(repeats)
print(f'Individuals or organizations who have won more than one Nobel Prize throughout the years are: {repeat_list}')
# plt.show()