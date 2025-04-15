import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import chisquare

late_shipments = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\29_Course_Hypothesis_Testing_in_Python\datasets\late_shipments_freight.csv')
hypothesized = pd.DataFrame({
    "vendor_inco_term": ["CIP", "DDP", "EXW", "FCA"],
    "prop": [0.05, 0.10, 0.75, 0.10]})
incoterm_counts = pd.DataFrame({
    "vendor_inco_term": ["CIP", "DDP", "EXW", "FCA"],
    "n": [56, 100, 732, 111]})

# Find the number of rows in late_shipments
# n_total = len(late_shipments)
n_total = incoterm_counts['n'].sum()

# Print n_total
print(n_total)

# Create n column that is prop column * n_total
hypothesized['n'] = hypothesized['prop'] * n_total

# Print the modified hypothesized DataFrame
print(hypothesized)

# Plot a red bar graph of n vs. vendor_inco_term for incoterm_counts
plt.bar(incoterm_counts['vendor_inco_term'], incoterm_counts['n'], color='red', label="Observed")
# plt.legend()
# plt.show()

# Add a blue bar plot for the hypothesized counts
plt.bar(hypothesized['vendor_inco_term'], hypothesized['n'],
alpha=0.5, color='blue', label="Hypothesized")
plt.legend()
plt.show()

# Perform a goodness of fit test on the incoterm counts n
gof_test = chisquare(f_obs=incoterm_counts['n'], f_exp=hypothesized['n'])


# Print gof_test results
print(gof_test)