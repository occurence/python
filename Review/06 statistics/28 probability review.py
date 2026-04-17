import pandas as pd
from scipy.stats import uniform, rv_discrete

restaurant_groups = pd.read_csv(r'D:\STUDY\python\Review\06 statistics\datasets\restaurant_groups.csv')
size_dist = restaurant_groups['group_size'].value_counts(normalize=True).reset_index()
size_dist.columns = ['group_size', 'prob']

xk = size_dist['group_size'].values   # possible outcomes
pk = size_dist['prob'].values         # probabilities

custom_dist = rv_discrete(name='custm', values=(xk, pk))

# Discrete
print('DISCRETE')
print('P(X <= 6)', custom_dist.cdf(6))
print('P(X >= 6)', 1 - custom_dist.cdf(5))
print('P(4 <= X <= 6)', custom_dist.cdf(6) - custom_dist.cdf(3))
print('P(2 <= X <= 6)', custom_dist.cdf(6))

# Continuous
print('Continuous')
print('P(X <= 7)', uniform.cdf(7, 0, 12))
print('P(X >= 7)', 1 - uniform.cdf(7, 0, 12))
print('P(4 <= X <= 7)', uniform.cdf(7, 0, 12) - uniform.cdf(4, 0, 12))
print('P(0 <= X <= 12)', uniform.cdf(12, 0, 12))

min_time = 0
max_time = 30
print('P(X < 5)', uniform.cdf(5, min_time, max_time))
print('P(X > 5)', 1 - uniform.cdf(5, min_time, max_time))
print('P(10 <= X <= 20)', uniform.cdf(20, min_time, max_time) - uniform.cdf(10, min_time, max_time))