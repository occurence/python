import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

loan_approval_yield = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\30_Course_Experimental_Design_in_Python\datasets\loan_approval_yield.csv')

# Use Seaborn to create the bar graph
sns.catplot(x="LoanAmount", 
            y="ApprovalYield", 
            hue="CreditScore", 
            kind="bar", 
            data=loan_approval_yield)
plt.title("Loan Approval Yield by Amount and Credit Score")
plt.show()