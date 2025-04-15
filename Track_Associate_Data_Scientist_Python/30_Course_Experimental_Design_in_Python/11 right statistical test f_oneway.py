import pandas as pd
from scipy.stats import ttest_ind
from scipy.stats import f_oneway
from scipy.stats import chi2_contingency

chemical_reactions = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\30_Course_Experimental_Design_in_Python\datasets\chemical_reactions.csv')

print(chemical_reactions.groupby('Catalyst')['Reaction_Time'].mean())

catalyst_types = ['Palladium', 'Platinum', 'Nickel']

# Collect reaction times for each catalyst into a list
groups = [chemical_reactions[chemical_reactions['Catalyst'] == catalyst]['Reaction_Time'] for catalyst in catalyst_types]

# Perform the one-way ANOVA across the three groups
f_stat, p_val = f_oneway(*groups)
print(f"F-statistic: {f_stat}, P-value: {p_val}")

if p_val <= 0.01:
    print("Reject the null hypothesis. P-value less than the significance level, indicating a significant difference.")
else:
    print("Fail to reject the null hypothesis. P-value greater than significance level, indicating a lack of significant association")