import librosa
import numpy as np
import os

HOP_LENGTH = 2**4
N_FFT = 2**7

spectrograms = []

# Path to folder with wav files
folder = 'D:\\STUDY\\python\\Track_Machine_Learning_Scientist_in_Python\\12_Course_Machine_Learning_for_Time_Series_Data_in_Python\\datasets\\archive\\set_a\\'

# Loop over each file
for file in os.listdir(folder):
    if file.endswith('.wav'):
        filepath = os.path.join(folder, file)
        
        # Load audio
        audio, sr = librosa.load(filepath, sr=None)
        
        # Compute spectrogram
        spec = np.abs(librosa.stft(audio, hop_length=HOP_LENGTH, n_fft=N_FFT))
        
        # Add to the list
        spectrograms.append(spec)

# Now you have a list of specs with shapes like (65, 552)
print(spectrograms)