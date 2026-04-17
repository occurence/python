import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
mpg = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\09_Course_Introduction_to_Data_Visualization_Seaborn\datasets\mpg.csv')

# Make the shaded area show the standard deviation
# sns.relplot(x="model_year", y="mpg",
#             data=mpg, kind="line")
sns.relplot(x="model_year", y="mpg",
            data=mpg, kind="line", ci='sd')

# Show plot
plt.show()