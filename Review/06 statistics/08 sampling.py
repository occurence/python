import pandas as pd
import numpy as np

amir_deals = pd.read_csv(r'D:\STUDY\python\Review\06 statistics\datasets\amir_deals.csv')

# Set random seed
np.random.seed(24)

# Sample 5 deals without replacement
sample_without_replacement = amir_deals.sample(5, replace=False)
print(sample_without_replacement)

# Sample 5 deals with replacement
sample_with_replacement = amir_deals.sample(5, replace=True)
print(sample_with_replacement)