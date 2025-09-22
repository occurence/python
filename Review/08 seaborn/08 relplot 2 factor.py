import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

student_data = pd.read_csv(r'D:\STUDY\python\Review\08 seaborn\datasets\student-alcohol-consumption.csv')

# Adjust further to add subplots based on family support
sns.relplot(x="G1", y="G3", 
            data=student_data,
            kind="scatter", 
            col="schoolsup",
            col_order=["yes", "no"], row='famsup', row_order=['yes', 'no'])

# Show plot
plt.show()