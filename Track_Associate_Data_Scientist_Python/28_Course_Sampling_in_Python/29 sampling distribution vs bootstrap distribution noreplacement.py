import pandas as pd
import numpy as np

spotify_population = pd.read_feather(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\28_Course_Sampling_in_Python\datasets\spotify_2000_2020.feather')
spotify_sample = spotify_population.sample(n=500)

mean_popularity_2000_samp = []

# Generate a sampling distribution of 2000 replicates
for i in range(2000):
    mean_popularity_2000_samp.append(
    	# Sample 500 rows and calculate the mean popularity 
    	np.mean(spotify_population.sample(n=500, replace=False)['popularity'])
    )

# Print the sampling distribution results
print(mean_popularity_2000_samp)