import pandas as pd
import numpy as np

spotify_population = pd.read_feather(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\28_Course_Sampling_in_Python\datasets\spotify_2000_2020.feather')
spotify_sample = spotify_population.sample(n=5000)
sampling_distribution = []
for i in range(2000):
    sampling_distribution.append(
    	np.mean(spotify_population.sample(n=5000, replace=False)['popularity'])
    )
bootstrap_distribution = []
for i in range(2000):
    bootstrap_distribution.append(
    	np.mean(spotify_sample.sample(n=5000, replace=True)['popularity'])
    )

# Calculate the population std dev popularity
pop_sd = spotify_population['popularity'].std(ddof=0)

# Calculate the original sample std dev popularity
samp_sd = spotify_sample['popularity'].std(ddof=1)

# Calculate the sampling dist'n estimate of std dev popularity
samp_distn_sd = np.std(sampling_distribution, ddof=1) * np.sqrt(5000)

# Calculate the bootstrap dist'n estimate of std dev popularity
boot_distn_sd = np.std(bootstrap_distribution, ddof=1) * np.sqrt(5000)

# Print the standard deviations
print([pop_sd, samp_sd, samp_distn_sd, boot_distn_sd])