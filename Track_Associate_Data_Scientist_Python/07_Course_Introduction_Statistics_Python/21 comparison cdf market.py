# Which market is better?
# The key metric that the company uses to evaluate salespeople is the percent of sales they make over $1000 since the time put into each sale is usually worth a bit more than that, so the higher this metric, the better the salesperson is performing.

# Recall that Amir's current sales amounts have a mean of $5000 and a standard deviation of $2000, and Amir's predicted amounts in next quarter's market have a mean of $6000 and a standard deviation of $2600.

# norm from scipy.stats is imported.

# Based only on the metric of percent of sales over $1000, does Amir perform better in the current market or the predicted market?

from scipy.stats import norm

print(1-norm.cdf(1000, 5000, 2000))

print(1-norm.cdf(1000, 6000, 2600))

# Possible answers


# Amir performs much better in the current market.

# Amir performs much better in next quarter's predicted market.

# Amir performs about equally in both markets.