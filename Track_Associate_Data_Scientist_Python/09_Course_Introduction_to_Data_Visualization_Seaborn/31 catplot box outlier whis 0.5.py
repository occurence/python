import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

student_data = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\09_Course_Introduction_to_Data_Visualization_Seaborn\datasets\student-alcohol-consumption.csv')

# Set the whiskers to 0.5 * IQR
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box", whis=0.5)

# Show plot
plt.show()