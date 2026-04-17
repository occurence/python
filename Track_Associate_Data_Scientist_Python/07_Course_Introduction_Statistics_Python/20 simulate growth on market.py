import matplotlib.pyplot as plt
from scipy.stats import norm

# Calculate new average amount
new_mean = 5000 + 5000*.2

# Calculate new standard deviation
new_sd = 2000 + 2000*.3

# Simulate 36 new sales
new_sales = norm.rvs(new_mean, new_sd, size=36)

# Create histogram and show
plt.hist(new_sales)
plt.show()