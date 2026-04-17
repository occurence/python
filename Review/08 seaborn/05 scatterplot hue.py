import pandas as pd

student_data = pd.read_csv(r'D:\STUDY\python\Review\08 seaborn\datasets\student-alcohol-consumption.csv')

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Change the legend order in the scatter plot
sns.scatterplot(x="absences", y="G3", 
                data=student_data, 
                hue="location", hue_order=['Rural', 'Urban'])

# Show plot
plt.show()