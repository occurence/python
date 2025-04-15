import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

spotify_population = pd.read_feather(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\28_Course_Sampling_in_Python\datasets\spotify_2000_2020.feather')
spotify_mysterious_sample = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\28_Course_Sampling_in_Python\datasets\spotify_mysterious_sample.csv')

# Visualize the distribution of acousticness with a histogram
spotify_population['acousticness'].hist(bins=np.arange(0, 1.01, 0.01))
plt.show()

# Update the histogram to use spotify_mysterious_sample
spotify_mysterious_sample['acousticness'].hist(bins=np.arange(0, 1.01, 0.01))
plt.show()