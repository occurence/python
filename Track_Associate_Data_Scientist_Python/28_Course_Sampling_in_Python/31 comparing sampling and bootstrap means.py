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

# Calculate the population mean popularity
pop_mean = np.mean(spotify_population['popularity'])

# Calculate the original sample mean popularity
samp_mean = np.mean(spotify_sample['popularity'])

# Calculate the sampling dist'n estimate of mean popularity
samp_distn_mean = np.mean(sampling_distribution)

# Calculate the bootstrap dist'n estimate of mean popularity
boot_distn_mean = np.mean(bootstrap_distribution)

# Print the means
print([pop_mean, samp_mean, samp_distn_mean, boot_distn_mean])