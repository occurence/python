import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

mpg = pd.read_csv(r'D:\STUDY\python\Review\08 seaborn\datasets\mpg.csv')

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create a scatter plot of acceleration vs. mpg
sns.relplot(x='acceleration', y='mpg', data=mpg, kind='scatter', style='origin', hue='origin')

# Show plot
plt.show()