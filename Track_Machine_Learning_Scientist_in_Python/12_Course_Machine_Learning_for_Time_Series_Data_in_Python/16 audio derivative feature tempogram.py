import pandas as pd
import numpy as np
from librosa.feature.rhythm import tempo

audio = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\12_Course_Machine_Learning_for_Time_Series_Data_in_Python\datasets\audio_60.csv', index_col=0)
sfreq = 2205
labels = np.array(pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\12_Course_Machine_Learning_for_Time_Series_Data_in_Python\datasets\labels.csv', header=None))

# # Plot the raw data first
# audio.plot(figsize=(10, 5))
# plt.show()

# Rectify the audio signal
audio_rectified = audio.apply(np.abs)

# # Plot the result
# audio_rectified.plot(figsize=(10, 5))
# plt.show()

# Smooth by applying a rolling mean
audio_rectified_smooth = audio_rectified.rolling(50).mean()

# # Plot the result
# audio_rectified_smooth.plot(figsize=(10, 5))
# plt.show()







from sklearn.svm import LinearSVC
model = LinearSVC()

# Calculate stats
means = np.array(np.mean(audio_rectified_smooth, axis=0))
stds = np.array(np.std(audio_rectified_smooth, axis=0))
maxs = np.array(np.max(audio_rectified_smooth, axis=0))

# Create the X and y arrays
X = np.column_stack([means, stds, maxs])
y = labels.reshape(-1, 1)

# Fit the model and score on testing data
from sklearn.model_selection import cross_val_score
percent_score = cross_val_score(model, X, y.ravel(), cv=5)
print(np.mean(percent_score))


from librosa.feature.rhythm import tempo

# Calculate the tempo of the sounds
tempos = []
for col, i_audio in audio.items():
    # tempos.append(lr.beat.tempo(i_audio.values, sr=sfreq, hop_length=2**6, aggregate=None))
    tempos.append(tempo(y=i_audio.values, sr=sfreq, hop_length=2**6, aggregate=None))

# Convert the list to an array so you can manipulate it more easily
tempos = np.array(tempos)

# Calculate statistics of each tempo
tempos_mean = tempos.mean(axis=-1)
tempos_std = tempos.std(axis=-1)
tempos_max = tempos.max(axis=-1)

# Create the X and y arrays
X = np.column_stack([means, stds, maxs, tempos_mean, tempos_std, tempos_max])
y = labels.reshape(-1, 1)

# Fit the model and score on testing data
percent_score = cross_val_score(model, X, y.ravel(), cv=5)
print(np.mean(percent_score))