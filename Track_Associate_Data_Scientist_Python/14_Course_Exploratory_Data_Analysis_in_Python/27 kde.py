import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

divorce = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\14_Course_Exploratory_Data_Analysis_in_Python\datasets\divorce_age.csv', parse_dates=['marriage_date'])

# Create the KDE plot
sns.kdeplot(data=divorce, x='marriage_duration', hue='num_kids')
plt.show()