import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

restaurant_groups = pd.read_csv(r'D:\STUDY\python\Review\06 statistics\datasets\restaurant_groups.csv')

# Create a histogram of restaurant_groups and show plot
restaurant_groups['group_size'].hist(bins=[2, 3, 4, 5, 6])
plt.show()

plt.hist(restaurant_groups["group_size"], bins=range(2, 8), align="left", rwidth=0.8)
plt.xticks(range(2, 8))
plt.show()

# Create probability distribution
size_dist = restaurant_groups['group_size'] / restaurant_groups.shape[0]

# Reset index and rename columns
size_dist = size_dist.reset_index()
size_dist.columns = ['group_size', 'prob']

print(size_dist)

# Expected value
expected_value = np.sum(size_dist['group_size'] * size_dist['prob'])

# Subset groups of size 4 or more
groups_4_or_more = size_dist[size_dist['group_size'] >= 4]

# Sum the probabilities of groups_4_or_more
prob_4_or_more = np.sum(groups_4_or_more['prob'])
print(prob_4_or_more)