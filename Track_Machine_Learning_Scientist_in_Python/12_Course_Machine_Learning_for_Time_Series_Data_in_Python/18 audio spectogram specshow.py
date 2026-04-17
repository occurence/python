import pandas as pd
import numpy as np

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