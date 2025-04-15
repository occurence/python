import pandas as pd
import numpy as np
from scipy.stats import t

late_shipments = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\29_Course_Hypothesis_Testing_in_Python\datasets\late_shipments.csv')

mean = late_shipments.groupby('late')['weight_kilograms'].mean()
xbar_no = mean.get(0, None)
xbar_yes = mean.get(1, None)
std = late_shipments.groupby('late')['weight_kilograms'].std()
s_no = std.get(0, None)
s_yes = std.get(1, None)
count = late_shipments.groupby('late')['weight_kilograms'].count()
n_no = count.get(0, None)
n_yes = count.get(1, None)
numerator = xbar_yes - xbar_no
denominator = np.sqrt(s_yes ** 2 / n_yes + s_no ** 2 / n_no)
t_stat = numerator / denominator


# Calculate the degrees of freedom
degrees_of_freedom = n_yes + n_no -2

# Calculate the p-value from the test stat
p_value = t.cdf(t_stat*-1, df=degrees_of_freedom)

# Print the p_value
print(p_value)

if 0.05 >= p_value:
    print(f'Alpha 0.05 is greater than or equal to:{p_value} thus Reject the null hypothesis')
elif 0.05 < p_value:
    print(f'Alpha 0.05 is less than:{p_value} thus Fail to Reject the null hypothesis')