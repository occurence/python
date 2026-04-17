import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

student_data = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\09_Course_Introduction_to_Data_Visualization_Seaborn\datasets\student-alcohol-consumption.csv')

# Create a scatter plot of G1 vs. G3
sns.relplot(x='G1', y='G3', data=student_data, kind='scatter')

# Show plot
plt.show()