import pandas as pd
import numpy as np
import librosa as lr


audio = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\12_Course_Machine_Learning_for_Time_Series_Data_in_Python\datasets\audio_60.csv', index_col=0)
sfreq = 2205
print(audio)
# lr.beat.tempo(audio, sr=sfreq, hop_length=2**6, aggregate=None)

# Calculate the tempo of the sounds
tempos = []
for col, i_audio in audio.items():
    # tempos.append(lr.beat.tempo(i_audio.values, sr=sfreq, hop_length=2**6, aggregate=None))
    onset_env = lr.onset.onset_strength(y=i_audio.values, sr=sfreq, hop_length=2**6)
    # tempo = lr.beat.tempo(onset_envelope=onset_env, sr=sfreq, hop_length=2**6, aggregate=None)
    tempo = lr.beat.tempo(onset_envelope=onset_env, sr=sfreq, hop_length=2**6)
# print(i_audio.shape)
# print(i_audio.head())

# Convert the list to an array so you can manipulate it more easily
# tempos = np.array(tempos)
tempos.append(tempo.item())

# Calculate statistics of each tempo
# tempos_mean = tempos.mean(axis=-1)
# tempos_std = tempos.std(axis=-1)
# tempos_max = tempos.max(axis=-1)
tempos_mean = np.nanmean(tempos, axis=-1)
tempos_std = np.nanstd(tempos, axis=-1)
tempos_max = np.nanmax(tempos, axis=-1)

print(tempos_mean)
print(tempos_std)
print(tempos_max)
# print(tempos)
# print(i_audio.shape)
# print(i_audio.head())
print(len(tempos))