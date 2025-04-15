import pandas as pd
from scipy.stats import ttest_ind
from scipy.stats import f_oneway
from scipy.stats import chi2_contingency

investment_returns = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\30_Course_Experimental_Design_in_Python\datasets\investment_returns.csv')

# Separate the annual returns by strategy type
quantitative_returns = investment_returns[investment_returns['Strategy_Type'] == 'Quantitative']['Annual_Return']
fundamental_returns = investment_returns[investment_returns['Strategy_Type'] == 'Fundamental']['Annual_Return']

# Perform the independent samples t-test between the two groups
t_stat, p_val = ttest_ind(quantitative_returns, fundamental_returns)
print(f"T-statistic: {t_stat}, P-value: {p_val}")

if p_val <= 0.01:
    print("Reject the null hypothesis. P-value less than the significance level, indicating a significant difference.")
else:
    print("Fail to reject the null hypothesis. P-value greater than significance level, indicating a lack of significant association")