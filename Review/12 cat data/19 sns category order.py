import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

reviews = pd.read_csv(r'D:\STUDY\python\Review\12 cat data\datasets\lasvegas_tripadvisor.csv')

# Create a bar chart
sns.set(font_scale=.9)
sns.set_style("whitegrid")
sns.catplot(x="User continent", y="Score", data=reviews, kind="bar")
plt.show()

# Print the frequency counts for "User continent"
print(reviews['User continent'].value_counts())

# Convert "User continent" to a categorical variable
reviews["User continent"] = reviews["User continent"].astype('category')
sns.catplot(x='User continent', y="Score", data=reviews, kind="bar")
plt.show()

# Reorder "User continent" using continent_categories and rerun the graphic
continent_categories = list(reviews["User continent"].value_counts().index)
reviews["User continent"] = reviews["User continent"].cat.reorder_categories(new_categories=continent_categories)
sns.catplot(x="User continent", y="Score", data=reviews, kind="bar")
plt.show()