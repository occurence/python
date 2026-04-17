import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

mpg = pd.read_csv(r'D:\STUDY\python\Review\08 seaborn\datasets\mpg.csv')

# Create line plot of model year vs. horsepower
sns.relplot(x='model_year', y='horsepower', data=mpg, kind='line', ci=None)

# Show plot
plt.show()

# Change to create subgroups for country of origin
sns.relplot(x="model_year", y="horsepower", 
            data=mpg, kind="line", 
            ci=None, style='origin', hue='origin')

# Show plot
plt.show()

# Add markers and make each line have the same style
sns.relplot(x="model_year", y="horsepower", 
            data=mpg, kind="line", 
            ci=None, style="origin", 
            hue="origin", dashes=False,markers=True)

# Show plot
plt.show()