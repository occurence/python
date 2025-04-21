import pandas as pd
import numpy as np

late_shipments = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\29_Course_Hypothesis_Testing_in_Python\datasets\late_shipments.csv')
late_prop_samp = (late_shipments['late'] == 'Yes').mean()

late_shipments_boot_distn = []
for i in range(5000):
    late_shipments_boot_distn.append(
    	np.mean(late_shipments.sample(frac=1, replace=True)['late_delivery'])
    )

print(late_shipments_boot_distn)
print(late_prop_samp)

# Hypothesize that the proportion is 6%
late_prop_hyp = 0.06

# Calculate the standard error
std_error = np.std(late_shipments_boot_distn, ddof=1)

# Find z-score of late_prop_samp
z_score = (late_prop_samp - late_prop_hyp) / std_error

# Print z_score
print(z_score)