import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

reviews = pd.read_csv(r'D:\STUDY\python\Review\12 cat data\datasets\lasvegas_tripadvisor.csv')
reviews["Traveler type"] = reviews["Traveler type"].astype('category')
categories = ['Friends', 'Business', 'Families', 'Solo', 'Couples']
reviews["Traveler type"] = reviews["Traveler type"].cat.reorder_categories(new_categories=categories)

# sns.set(font_scale=1.4)
sns.set_theme(font_scale=1.4)
sns.set_style("darkgrid")

# Create a catplot that will count the frequency of "Score" across "Traveler type"
sns.catplot(
  x='Score',
  data=reviews,
  kind='count',
  hue='Traveler type'
)
plt.show()