import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

salaries = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\14_Course_Exploratory_Data_Analysis_in_Python\datasets\salaries_response.csv', parse_dates=['date_of_response'])

# Create a bar plot of salary versus company size, factoring in employment status
# sns.barplot(data=salaries, x="Company_Size", y="Salary_USD", hue="Employment_Status")
sns.barplot(data=salaries, x="Company_Size", y="Salary_USD", hue="Employment_Status", order=['S','M','L'])
plt.show()