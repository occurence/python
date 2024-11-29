import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

survey_data = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\09_Course_Introduction_to_Data_Visualization_Seaborn\datasets\young_math.csv')

# Create a bar plot of interest in math, separated by gender
sns.catplot(x='Gender', y='Interested in Math', data=survey_data, kind='bar')


# Show plot
plt.show()