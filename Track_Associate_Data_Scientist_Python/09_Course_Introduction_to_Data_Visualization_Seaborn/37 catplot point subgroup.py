import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

student_data = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\09_Course_Introduction_to_Data_Visualization_Seaborn\datasets\student-alcohol-consumption.csv')

# Create a point plot that uses color to create subgroups
sns.catplot(x='romantic', y='absences', data=student_data, kind='point', hue='school')

# Show plot
plt.show()