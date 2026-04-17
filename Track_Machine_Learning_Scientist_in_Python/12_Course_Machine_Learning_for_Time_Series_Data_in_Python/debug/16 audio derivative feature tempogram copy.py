import pandas as pd
import numpy as np
from librosa.feature.rhythm import tempo

audio = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\12_Course_Machine_Learning_for_Time_Series_Data_in_Python\datasets\audio_60.csv', index_col=0)
sfreq = 2205

# Calculate the tempo of the sounds
tempos = []
for col, i_audio in audio.items():
    # tempos.append(lr.beat.tempo(i_audio.values, sr=sfreq, hop_length=2**6, aggregate=None))
    tempos.append(tempo(y=i_audio.values, sr=sfreq, hop_length=2**6))

# Convert the list to an array so you can manipulate it more easily
tempos = np.array(tempos)

# Calculate statistics of each tempo
tempos_mean = tempos.mean(axis=-1)
tempos_std = tempos.std(axis=-1)
tempos_max = tempos.max(axis=-1)

means = np.mean(audio[['0']])
print(means)
print(np.mean(audio['0']))
print(audio.shape)
print(audio.mean(axis=0))
# print(tempos_mean)


# print(audio)
# # Create the X and y arrays
# X = np.column_stack([means, stds, maxs, tempos_mean, tempos_std, tempos_max])
# y = labels.reshape(-1, 1)

# # Fit the model and score on testing data
# percent_score = cross_val_score(model, X, y, cv=5)
# print(np.mean(percent_score))







print(audio.shape)            # Should be (8820, 60)
print(audio.head())           # If it's a DataFrame
print(audio.iloc[0])          # First row
print(audio.isnull().sum())  # pandas

# Column 0 mean
print('Local:', audio.iloc[:, 0].mean())  # pandas
print('DataCamp:', 0.04352642)

# Column 1 mean
print('Local:', audio.iloc[:, 1].mean())
print('DataCamp:', 0.04553915)



print(audio[['0']])

print(np.mean(audio.iloc[:, 0]))

# pandas
means = audio.mean(axis=0).values  # Should return (60,) array
print(means[0])  # Should match their first value if data is the same

# numpy
means = np.mean(audio, axis=0)
print(means[0])


print(audio.mean(axis=0).values)
print(np.mean(audio.iloc[0]))

print(tempos_mean)

means_abs = np.mean(np.abs(audio), axis=0)
print(means_abs)


print(audio)


# means = audio_rectified_smooth.mean(axis=0, skipna=True)
# stds = audio_rectified_smooth.std(axis=0, skipna=True)
# maxs = audio_rectified_smooth.max(axis=0)
