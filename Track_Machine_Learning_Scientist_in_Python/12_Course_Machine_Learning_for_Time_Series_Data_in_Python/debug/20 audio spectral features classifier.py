import pandas as pd
import numpy as np
import librosa as lr
import os

HOP_LENGTH = 2**4
N_FFT = 2**7

spectrograms = []

# Path to folder with wav files
folder = 'D:\\STUDY\\python\\Track_Machine_Learning_Scientist_in_Python\\12_Course_Machine_Learning_for_Time_Series_Data_in_Python\\datasets\\specto\\'

# Loop over each file
for file in os.listdir(folder):
    filepath = os.path.join(folder, file)
    # print(filepath)

    spec = np.array(pd.read_csv(filepath))
    spectrograms.append(spec)






#     # Load audio
#     audio, sr = librosa.load(filepath, sr=None)
    
#     # Compute spectrogram
#     spec = np.abs(librosa.stft(audio, hop_length=HOP_LENGTH, n_fft=N_FFT))
    
#     # Add to the list
#     spectrograms.append(spec)

# Now you have a list of specs with shapes like (65, 552)
print(spectrograms)

# print(np.array(pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\12_Course_Machine_Learning_for_Time_Series_Data_in_Python\datasets\specto\spec_59.csv')))

