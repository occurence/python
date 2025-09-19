import pandas as pd
import matplotlib.pyplot as plt

medals = pd.read_csv(r'D:\STUDY\python\Review\07 matplotlib\datasets\medals_by_country_2016.csv', index_col=0)

fig, ax = plt.subplots()

# Plot a bar-chart of gold medals as a function of country
ax.bar(medals.index, medals['Gold'])

# Set the x-axis tick labels to the country names
ax.set_xticklabels(medals.index, rotation=90)

# Set the y-axis label
ax.set_ylabel('Number of medals')

plt.show()