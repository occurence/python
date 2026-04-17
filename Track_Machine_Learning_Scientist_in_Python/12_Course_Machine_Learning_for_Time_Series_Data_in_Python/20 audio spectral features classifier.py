import pandas as pd
import numpy as np
import os

audio = np.array(pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\12_Course_Machine_Learning_for_Time_Series_Data_in_Python\datasets\audio_0.csv', header=None))
audio = audio[:, 0]

# Import the stft function
from librosa.core import stft

# Prepare the STFT
HOP_LENGTH = 2**4
# spec = stft(audio, hop_length=HOP_LENGTH, n_fft=2**7)
spec = np.abs(stft(audio, hop_length=HOP_LENGTH, n_fft=2**7))

import matplotlib.pyplot as plt
from librosa.core import amplitude_to_db
from librosa.display import specshow

time = np.array(pd.read_csv(r'Track_Machine_Learning_Scientist_in_Python/12_Course_Machine_Learning_for_Time_Series_Data_in_Python/datasets/abnormal.csv', index_col=0).index)
sfreq = 2205

# Convert into decibels
spec_db = amplitude_to_db(spec)

# Compare the raw audio to the spectrogram of the audio
fig, axs = plt.subplots(2, 1, figsize=(10, 10), sharex=True)
axs[0].plot(time, audio)
specshow(spec_db, sr=sfreq, x_axis='time', y_axis='hz', hop_length=HOP_LENGTH, ax=axs[1])
plt.show()

import librosa as lr

# Calculate the spectral centroid and bandwidth for the spectrogram
bandwidths = lr.feature.spectral_bandwidth(S=spec)[0]
centroids = lr.feature.spectral_centroid(S=spec)[0]

times_spec = np.array(pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\12_Course_Machine_Learning_for_Time_Series_Data_in_Python\datasets\times_spec.csv', header=None))
times_spec = times_spec.flatten()

# Convert spectrogram to decibels for visualization
spec_db = amplitude_to_db(spec)

# Display these features on top of the spectrogram
fig, ax = plt.subplots(figsize=(10, 5))
specshow(spec_db, x_axis='time', y_axis='hz', hop_length=HOP_LENGTH, ax=ax)
ax.plot(times_spec, centroids)
ax.fill_between(times_spec, centroids - bandwidths / 2, centroids + bandwidths / 2, alpha=.5)
ax.set(ylim=[None, 6000])
plt.show()

HOP_LENGTH = 2**4
N_FFT = 2**7

spectrograms = []
folder = 'D:\\STUDY\\python\\Track_Machine_Learning_Scientist_in_Python\\12_Course_Machine_Learning_for_Time_Series_Data_in_Python\\datasets\\specto\\'

for file in os.listdir(folder):
    filepath = os.path.join(folder, file)
    spec = np.array(pd.read_csv(filepath))
    spectrograms.append(spec)

bandwidths = []
centroids = []
means = []
stds = []
maxs = []

for spec in spectrograms:
    spec_db = amplitude_to_db(spec)
    this_mean_bandwidth = np.mean(lr.feature.spectral_bandwidth(S=spec))
    this_mean_centroid = np.mean(lr.feature.spectral_centroid(S=spec))
    bandwidths.append(this_mean_bandwidth)  
    centroids.append(this_mean_centroid)
    # means.append(np.mean(spec))
    means.append(np.mean(spec, axis=0))
    stds.append(np.std(spec, axis=0))
    maxs.append(np.max(spec, axis=0))

from sklearn.model_selection import cross_val_score
from librosa.feature.rhythm import tempo
print(means)
print(stds)
print(maxs)
