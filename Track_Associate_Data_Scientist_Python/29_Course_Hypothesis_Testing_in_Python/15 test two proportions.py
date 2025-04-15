import pandas as pd
import numpy as np
from scipy.stats import norm

late_shipments = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\29_Course_Hypothesis_Testing_in_Python\datasets\late_shipments_freight.csv')
# pd.options.display.float_format = '{:.10f}'.format
p_hats = late_shipments.groupby('freight_cost_group')['late'].value_counts(normalize=True)
p_hats = p_hats[p_hats.index.get_level_values('late') == 'Yes']
# p_hats = late_shipments[late_shipments['late'] == 'Yes'] \
#     .groupby('freight_cost_groups')['late'] \
#     .value_counts(normalize=True)

ns = late_shipments.groupby('freight_cost_group')['late'].count()

# Calculate the pooled estimate of the population proportion
p_hat = (ns['expensive'] * p_hats['expensive'] + ns['reasonable'] * p_hats['reasonable']) / (ns['expensive'] + ns['reasonable'])

# Print the result
print(p_hat)

# Calculate p_hat one minus p_hat
p_hat_times_not_p_hat = p_hat * (1 - p_hat)

# Divide this by each of the sample sizes and then sum
p_hat_times_not_p_hat_over_ns = (p_hat_times_not_p_hat / ns['expensive']) + (p_hat_times_not_p_hat / ns['reasonable'])

# Calculate the standard error
std_error = np.sqrt(p_hat_times_not_p_hat_over_ns)

# Print the result
print(std_error)

# Calculate the z-score
z_score = (p_hats['expensive'] - p_hats['reasonable']) / std_error

# Print z_score
print(z_score)

# Calculate the p-value from the z-score
p_value = 1 - norm.cdf(z_score)

# Print p_value
print(p_value)

print(ns)

print(p_hats)
# print(p_hats.to_string())
# print(p_hats[p_hats.index.get_level_values('late') == 'Yes'])