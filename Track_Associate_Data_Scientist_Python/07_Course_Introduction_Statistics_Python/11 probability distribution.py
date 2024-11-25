import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

restaurant_groups = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\07_Course_Introduction_Statistics_Python\datasets\restaurant_groups.csv')

# Create probability distribution
size_dist = restaurant_groups['group_size'].value_counts() / restaurant_groups.shape[0]
print(size_dist)

# Reset index and rename columns
size_dist = size_dist.reset_index()
size_dist.columns = ['group_size', 'prob']

# Round the 'prob' column to 2 decimal places
size_dist['prob'] = size_dist['prob'].round(1)
print(size_dist)

# Expected value
expected_value = np.sum(size_dist['group_size'] * size_dist['prob'])

# Subset groups of size 4 or more
groups_4_or_more = size_dist[size_dist['group_size'] >= 4]
print(groups_4_or_more)
# Sum the probabilities of groups_4_or_more
prob_4_or_more = np.sum(groups_4_or_more['prob'])
print(prob_4_or_more)