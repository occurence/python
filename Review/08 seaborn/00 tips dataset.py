import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

tips = sns.load_dataset('tips')

# print(tips.head(3))

# Make a small derived time column (sequential visits)
tips = tips.reset_index(drop=True).copy()
tips['visit_id'] = np.arange(len(tips))  # simple sequential index (simulated time)


# Scatter — relationship between two numeric variables
sns.scatterplot(x='total_bill', y='tip', data=tips, hue='day')
plt.title('Scatter: total_bill vs tip (colored by day)')
plt.show()

# Line — trend over a time-like numeric X
# Example: average tip across the sequential visits (smoothed by rolling mean)
tips_sorted = tips.sort_values('visit_id')
tips_sorted['rolling_tip'] = tips_sorted['tip'].rolling(window=10, min_periods=1).mean()

sns.lineplot(x='visit_id', y='rolling_tip', data=tips_sorted)
plt.title('Line: rolling average tip over simulated visits')
plt.xlabel('visit_id (simulated time)')
plt.ylabel('rolling mean tip')
plt.show()


# Histogram (distribution of a numeric)
sns.histplot(tips['total_bill'], bins=20, stat='density')
sns.kdeplot(tips['total_bill'], lw=2)  # optional KDE overlay
plt.title('Histogram + KDE: distribution of total_bill')
plt.show()


# Bar plot — group comparison (category vs summary numeric)
sns.barplot(x='day', y='total_bill', data=tips, estimator=np.mean, ci='sd')
plt.title('Bar: mean total_bill per day (± std)')
plt.show()


# Box plot — distribution of numeric by category
sns.boxplot(x='day', y='tip', data=tips)
plt.title('Box: tip distribution per day')
plt.show()

# Count plot — frequency of categories
sns.countplot(x='size', data=tips)  # how many parties by size
plt.title('Count: frequency of party sizes')
plt.show()


# Point plot — mean per category with confidence/CI
sns.pointplot(x='time', y='tip', hue='sex', data=tips, dodge=True, markers='o', capsize=.1)
plt.title('Point: mean tip by time and sex (with CI)')
plt.show()


# Regression (lmplot) — relational + fitted line
sns.lmplot(x='total_bill', y='tip', data=tips, hue='smoker', aspect=1.2)
plt.title('LMplot: tip vs total_bill with regression by smoker')
plt.show()
