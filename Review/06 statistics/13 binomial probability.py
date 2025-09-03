import numpy as np

# Import binom from scipy.stats
from scipy.stats import binom

# Set random seed to 10
np.random.seed(10)

# Probability of closing 3 out of 3 deals
prob_3 = binom.pmf(3, 3, .3)

print(prob_3)

# Probability of closing <= 1 deal out of 3 deals
prob_less_than_or_equal_1 = binom.cdf(1, 3, .3)

print(prob_less_than_or_equal_1)

# Probability of closing > 1 deal out of 3 deals
prob_greater_than_1 = 1 - binom.cdf(1, 3, .3)

print(prob_greater_than_1)


# Expected number won with 30% win rate
won_30pct = 3 * .3
print(won_30pct)

# Expected number won with 25% win rate
won_25pct = 3 * .25
print(won_25pct)

# Expected number won with 35% win rate
won_35pct = 3 * .35
print(won_35pct)