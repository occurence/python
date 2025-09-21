import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

student_data = pd.read_csv(r'D:\STUDY\python\Review\08 seaborn\datasets\student-alcohol-consumption.csv')

# Change to use relplot() instead of scatterplot()
sns.relplot(x="absences", y="G3", 
                data=student_data, kind='scatter')

# Show plot
plt.show()

# Change to make subplots based on study time
sns.relplot(x="absences", y="G3", 
            data=student_data,
            kind="scatter", col='study_time')

# Show plot
plt.show()

# Change this scatter plot to arrange the plots in rows instead of columns
sns.relplot(x="absences", y="G3", 
            data=student_data,
            kind="scatter", 
            row="study_time")

# Show plot
plt.show()