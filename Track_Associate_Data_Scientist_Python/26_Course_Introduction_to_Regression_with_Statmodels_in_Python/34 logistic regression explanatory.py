import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

churn = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\26_Course_Introduction_to_Regression_with_Statmodels_in_Python\datasets\churn.csv')

# Create the histograms of time_since_last_purchase split by has_churned
sns.displot(data=churn,
            x='time_since_last_purchase',
            col='has_churned')

plt.show()

# Redraw the plot with time_since_first_purchase
sns.displot(data=churn,
            x='time_since_first_purchase',
            col='has_churned')

plt.show()