import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

reviews = pd.read_csv(r'D:\STUDY\python\Review\12 cat data\datasets\lasvegas_tripadvisor.csv')

# Print the frequency counts of "Period of stay"
print(reviews['Period of stay'].value_counts())

# sns.set(font_scale=1.4)
sns.set_theme(font_scale=1.4)
sns.set_style("whitegrid")

# Create a bar plot of "Helpful votes" by "Period of stay"
sns.catplot(x='Period of stay', y='Helpful votes', data=reviews, kind='bar')
plt.show()