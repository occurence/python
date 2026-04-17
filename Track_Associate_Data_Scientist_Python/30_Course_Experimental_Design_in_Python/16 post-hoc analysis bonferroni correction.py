import pandas as pd
from scipy.stats import ttest_ind
from statsmodels.sandbox.stats.multicomp import multipletests

therapy_outcomes = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\30_Course_Experimental_Design_in_Python\datasets\therapy_outcomes.csv')

p_values = []

therapy_pairs = [('CBT', 'DBT'), ('CBT', 'ACT'), ('DBT', 'ACT')]

# Conduct t-tests and collect P-values
for pair in therapy_pairs:
    group1 = therapy_outcomes[therapy_outcomes['Therapy_Type'] == pair[0]]['Anxiety_Reduction']
    group2 = therapy_outcomes[therapy_outcomes['Therapy_Type'] == pair[1]]['Anxiety_Reduction']
    t_stat, p_val = ttest_ind(group1, group2)
    p_values.append(p_val)

# Apply Bonferroni correction
print(multipletests(p_values, alpha=0.05, method='bonferroni')[1])

for i, (pair, p_values) in enumerate(zip(therapy_pairs, p_values)):
    print(f"Comparison: {pair[0]} vs {pair[1]}")
    if p_values < 0.05:
        print(f"  Reject the null hypothesis. P-value ({p_values:.4f}) is less than the significance level, indicating a significant difference.")
    elif p_values == 1:
        print(f"  Fail to reject the null hypothesis. P-value is 1, suggesting no difference after correction.")
    else:
        print(f"  Fail to reject the null hypothesis. P-value ({p_values:.4f}) is greater than the significance level, indicating a lack of significant association.")