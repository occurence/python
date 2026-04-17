import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

loan_approval_yield = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\30_Course_Experimental_Design_in_Python\datasets\loan_approval_yield.csv')
customer_satisfaction = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\30_Course_Experimental_Design_in_Python\datasets\customer_satisfaction.csv')

# Merge the two datasets
merged_data = pd.merge(loan_approval_yield, 
                      customer_satisfaction, 
                      on='ApplicationID')

# Use Seaborn to create the scatter plot
sns.relplot(x="ApprovalYield", 
            y="SatisfactionQuality", 
            hue="InterestRate", 
            kind="scatter", 
            data=merged_data)
plt.title("Satisfaction Quality by Approval Yield and Interest Rate")
plt.show()