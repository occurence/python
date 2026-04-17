import pandas as pd
import numpy as np
from scipy.stats import norm

late_shipments = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\29_Course_Hypothesis_Testing_in_Python\datasets\late_shipments.csv')
late_prop_samp = (late_shipments['late'] == 'Yes').mean()
late_shipments_boot_distn = []
for i in range(5000):
    late_shipments_boot_distn.append(
    	np.mean(late_shipments.sample(frac=1, replace=True)['late_delivery'])
    )
late_prop_hyp = 0.06
std_error = np.std(late_shipments_boot_distn, ddof=1)

# Calculate the z-score of late_prop_samp
z_score = (late_prop_samp-late_prop_hyp)/std_error

# Calculate the p-value
p_value = 1 - norm.cdf(z_score, loc=0, scale=1)
                 
# Print the p-value
print(p_value) 