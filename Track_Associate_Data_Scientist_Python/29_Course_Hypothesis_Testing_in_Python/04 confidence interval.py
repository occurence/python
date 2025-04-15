import pandas as pd
import numpy as np

late_shipments = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\29_Course_Hypothesis_Testing_in_Python\datasets\late_shipments.csv')
late_shipments_boot_distn = []
for i in range(5000):
    late_shipments_boot_distn.append(
    	np.mean(late_shipments.sample(frac=1, replace=True)['late_delivery'])
    )

# Calculate 95% confidence interval using quantile method
lower = np.quantile(late_shipments_boot_distn, 0.025)
upper = np.quantile(late_shipments_boot_distn, 0.975)

# Print the confidence interval
print((lower, upper))