import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

student_data = pd.read_csv(r'D:\STUDY\python\Review\08 seaborn\datasets\student-alcohol-consumption.csv')

# Create a box plot with subgroups and omit the outliers
# sns.catplot(x='internet', y='G3', data=student_data, kind='box', sym='', hue='location')
sns.catplot(x='internet', y='G3', data=student_data, kind='box', flierprops={'marker':''}, hue='location')

# Show plot
plt.show()