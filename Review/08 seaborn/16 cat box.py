import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

student_data = pd.read_csv(r'D:\STUDY\python\Review\08 seaborn\datasets\student-alcohol-consumption.csv')

# Specify the category ordering
study_time_order = ["<2 hours", "2 to 5 hours", 
                    "5 to 10 hours", ">10 hours"]

# Create a box plot and set the order of the categories
sns.catplot(x='study_time', y='G3', data=student_data, kind='box', order=study_time_order)

# Show plot
plt.show()