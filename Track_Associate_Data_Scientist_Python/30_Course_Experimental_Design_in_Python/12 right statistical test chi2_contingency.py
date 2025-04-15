import pandas as pd
from scipy.stats import ttest_ind
from scipy.stats import f_oneway
from scipy.stats import chi2_contingency

hr_wellness = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\30_Course_Experimental_Design_in_Python\datasets\hr_wellness.csv')

# Create a contingency table
contingency_table = pd.crosstab(
  hr_wellness['Department'], 
  hr_wellness['Wellness_Program_Status']
)

# Perform the chi-square test of association
chi2_stat, p_val, dof, expected = chi2_contingency(contingency_table)
print(f"Chi2-statisc: {chi2_stat}, P-value: {p_val}")

if p_val <= 0.05:
    print("Reject the null hypothesis. P-value less than the significance level, indicating a significant difference.")
else:
    print("Fail to reject the null hypothesis. P-value greater than significance level, indicating a lack of significant association")