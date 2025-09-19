import pandas as pd
import matplotlib.pyplot as plt

mens_rowing = pd.read_csv(r'D:\STUDY\python\Review\07 matplotlib\datasets\mens_rowing.csv', index_col=0)
mens_gymnastics = pd.read_csv(r'D:\STUDY\python\Review\07 matplotlib\datasets\mens_gymnastics.csv', index_col=0)
fig, ax = plt.subplots()

# Plot a histogram of "Weight" for mens_rowing
ax.hist(mens_rowing['Weight'])

# Compare to histogram of "Weight" for mens_gymnastics
ax.hist(mens_gymnastics['Weight'])

# Set the x-axis label to "Weight (kg)"
ax.set_xlabel('Weight (kg)')

# Set the y-axis label to "# of observations"
ax.set_ylabel('# of observations')

plt.show()