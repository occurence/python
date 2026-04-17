import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

reviews = pd.read_csv(r'D:\STUDY\python\Review\12 cat data\datasets\lasvegas_tripadvisor.csv')

# Set the font size to 1.25
# sns.set(font_scale=1.25)
sns.set_theme(font_scale=1.25)

# Set the background to "darkgrid"
sns.set_style('darkgrid')

# Create a boxplot
sns.catplot(x='Traveler type', y='Helpful votes', data=reviews, kind='box')

plt.show()