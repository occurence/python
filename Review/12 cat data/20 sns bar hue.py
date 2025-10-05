import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

reviews = pd.read_csv(r'D:\STUDY\python\Review\12 cat data\datasets\lasvegas_tripadvisor.csv')

# Add a second category to split the data on: "Free internet"
# sns.set(font_scale=2)
sns.set_theme(font_scale=2)
sns.set_style("darkgrid")
sns.catplot(x='Casino', y="Score", data=reviews, kind="bar", hue='Free internet')
plt.show()

# Switch the x and hue categories
# sns.set(font_scale=2)
sns.set_theme(font_scale=2)
sns.set_style("darkgrid")
sns.catplot(x='Free internet', y="Score", data=reviews, kind="bar", hue='Casino')
plt.show()

# Update x to be "User continent"
# sns.set(font_scale=2)
sns.set_theme(font_scale=2)
sns.set_style("darkgrid")
sns.catplot(x='User continent', y="Score", data=reviews, kind="bar", hue="Casino")
plt.show()

# Lower the font size so that all text fits on the screen.
# sns.set(font_scale=1)
sns.set_theme(font_scale=1)
sns.set_style("darkgrid")
sns.catplot(x="User continent", y="Score", data=reviews, kind="bar", hue="Casino")
plt.show()