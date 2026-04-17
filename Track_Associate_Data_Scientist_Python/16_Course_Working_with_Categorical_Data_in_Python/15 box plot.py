import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

reviews = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\16_Course_Working_with_Categorical_Data_in_Python\datasets\lasvegas_tripadvisor.csv')

# Set the font size to 1.25
sns.set(font_scale=1.25)

# Set the background to "darkgrid"
sns.set_style('darkgrid')

# Create a boxplot
sns.catplot(data=reviews, x='Traveler type', y='Helpful votes', kind='box')

plt.show()