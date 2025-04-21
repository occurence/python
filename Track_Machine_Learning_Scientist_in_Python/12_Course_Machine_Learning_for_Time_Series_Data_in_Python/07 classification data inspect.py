import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_dir = r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\12_Course_Machine_Learning_for_Time_Series_Data_in_Python\datasets\archive\set_a'

import librosa as lr
from glob import glob

# List all the wav files in the folder
audio_files = glob(data_dir + '/*.wav')

# Read in the first audio file, create the time array
# audio, sfreq = lr.load(audio_files[0])
audio, sfreq = lr.load('D:\\STUDY\\python\\Track_Machine_Learning_Scientist_in_Python\\12_Course_Machine_Learning_for_Time_Series_Data_in_Python\\datasets\\archive\\set_a\\murmur__201108222238.wav')
time = np.arange(0, len(audio)) / sfreq

# Plot audio over time
fig, ax = plt.subplots()
ax.plot(time, audio)
ax.set(xlabel='Time (s)', ylabel='Sound Amplitude')
plt.show()