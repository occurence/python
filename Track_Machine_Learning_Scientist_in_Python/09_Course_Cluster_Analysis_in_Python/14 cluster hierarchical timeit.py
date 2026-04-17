import pandas as pd
import random
import timeit
from scipy.cluster.hierarchy import linkage

# Generate random points
points = 100
df = pd.DataFrame({'x': random.sample(range(0, points), points),
                   'y': random.sample(range(0, points), points)})

# Define the function to time
def hierarchical_clustering():
    linkage(df[['x', 'y']], method='ward', metric='euclidean')

# Measure execution time
execution_time = timeit.timeit(hierarchical_clustering, number=10)  # Run 10 times
print(f"Execution time: {execution_time:.5f} seconds")

# %timeit sum([1, 3, 2])