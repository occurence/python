import pandas as pd
mpg = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\09_Course_Introduction_to_Data_Visualization_Seaborn\datasets\mpg.csv')

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create line plot of model year vs. horsepower
sns.relplot(x='model_year', y='horsepower', data=mpg, kind='line', ci=None)

# Show plot
plt.show()