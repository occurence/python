import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

churn = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\26_Course_Introduction_to_Regression_with_Statmodels_in_Python\datasets\churn.csv')


# Draw a linear regression trend line and a scatter plot of time_since_first_purchase vs. has_churned
sns.regplot(data=churn,
            x='time_since_first_purchase',
            y='has_churned',
            line_kws={"color": "red"})

plt.show()