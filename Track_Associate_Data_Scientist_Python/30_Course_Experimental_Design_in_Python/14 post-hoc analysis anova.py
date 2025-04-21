import pandas as pd
from scipy.stats import f_oneway

therapy_outcomes = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\30_Course_Experimental_Design_in_Python\datasets\therapy_outcomes.csv')

# Pivot to view the mean anxiety reduction for each therapy
pivot_table = therapy_outcomes.pivot_table(
    values='Anxiety_Reduction', 
    index='Therapy_Type', 
    aggfunc="mean")
print(pivot_table)

# Create groups to prepare the data for ANOVA
therapy_types = ['CBT', 'DBT', 'ACT']
groups = [therapy_outcomes[therapy_outcomes['Therapy_Type'] == therapy]['Anxiety_Reduction'] for therapy in therapy_types]

# Conduct ANOVA
f_stat, p_val = f_oneway(*groups)
print(p_val)

if p_val <= 0.05:
    print("Reject the null hypothesis. P-value less than the significance level, indicating a significant difference.")
else:
    print("Fail to reject the null hypothesis. P-value greater than significance level, indicating a lack of significant association")