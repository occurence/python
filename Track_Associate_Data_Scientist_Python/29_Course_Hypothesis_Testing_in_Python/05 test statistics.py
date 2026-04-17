import pandas as pd
import numpy as np

late_shipments = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\29_Course_Hypothesis_Testing_in_Python\datasets\late_shipments.csv')

mean = late_shipments.groupby('late')['weight_kilograms'].mean()

# Assign to variables directly
xbar_no = mean.get(0, None)
xbar_yes = mean.get(1, None)

std = late_shipments.groupby('late')['weight_kilograms'].std()

# Assign to variables directly
s_no = std.get(0, None)
s_yes = std.get(1, None)

count = late_shipments.groupby('late')['weight_kilograms'].count()

# Assign to variables directly
n_no = count.get(0, None)
n_yes = count.get(1, None)

# Calculate the numerator of the test statistic
numerator = xbar_yes - xbar_no

# Calculate the denominator of the test statistic
denominator = np.sqrt(s_yes ** 2 / n_yes + s_no ** 2 / n_no)

# Calculate the test statistic
t_stat = numerator / denominator

# Print the test statistic
print(t_stat)