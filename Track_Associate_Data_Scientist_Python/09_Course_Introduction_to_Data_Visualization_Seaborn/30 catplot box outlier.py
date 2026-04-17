import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

student_data = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\09_Course_Introduction_to_Data_Visualization_Seaborn\datasets\student-alcohol-consumption.csv')

# Create a box plot with subgroups and omit the outliers
# g = sns.catplot(x='internet', y='G3', data=student_data, kind='box', hue='location', sym='')
g = sns.catplot(x='internet', y='G3', data=student_data, kind='box', hue='location', showfliers=False)

# Show plot
plt.show()