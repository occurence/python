import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

mpg_mean = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\09_Course_Introduction_to_Data_Visualization_Seaborn\datasets\mpg_mean.csv')

# Create line plot
g = sns.lineplot(x="model_year", y="mpg_mean", 
                 data=mpg_mean,
                 hue="origin")

# Add a title "Average MPG Over Time"
g.set_title("Average MPG Over Time")

# Add x-axis and y-axis labels
g.set(xlabel='Car Model Year', ylabel='Average MPG')


# Show plot
plt.show()