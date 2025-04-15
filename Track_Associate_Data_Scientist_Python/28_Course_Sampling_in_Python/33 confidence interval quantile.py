import pandas as pd
import numpy as np

spotify_population = pd.read_feather(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\28_Course_Sampling_in_Python\datasets\spotify_2000_2020.feather')
spotify_sample = spotify_population.sample(n=5000)
bootstrap_distribution = []
for i in range(2000):
    bootstrap_distribution.append(
    	np.mean(spotify_sample.sample(n=5000, replace=True)['popularity'])
    )

# Generate a 95% confidence interval using the quantile method
lower_quant = np.quantile(bootstrap_distribution, 0.025)
upper_quant = np.quantile(bootstrap_distribution, 0.975)

# Print quantile method confidence interval
print((lower_quant, upper_quant))