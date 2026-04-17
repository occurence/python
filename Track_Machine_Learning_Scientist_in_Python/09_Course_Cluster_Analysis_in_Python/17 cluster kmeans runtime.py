import pandas as pd
import timeit
from scipy.cluster.vq import kmeans

fifa = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\09_Course_Cluster_Analysis_in_Python\datasets\fifa.csv')

# %timeit kmeans(fifa[['scaled_sliding_tackle', 'scaled_aggression']], 3)

def run_kmeans():
    kmeans(fifa[['scaled_sliding_tackle', 'scaled_aggression']], 3)

# Measure execution time
execution_time = timeit.timeit(run_kmeans, number=10)  # Run 10 times for a better estimate
print(f"Average runtime: {execution_time / 10:.6f} seconds")
print("41 ms +- 1.5 ms per loop (mean +- std. dev. of 7 runs, 10 loops each)")