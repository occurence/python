import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

audio_df = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\12_Course_Machine_Learning_for_Time_Series_Data_in_Python\datasets\audio_60.csv', index_col=0)
audio = round(audio_df[['0']].iloc[:2205], 3)
labels = np.array(pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\12_Course_Machine_Learning_for_Time_Series_Data_in_Python\datasets\labels.csv', header=None))

# Plot the raw data first
audio.plot(figsize=(10, 5))
plt.show()

# Rectify the audio signal
audio_rectified = audio.apply(np.abs)

# Plot the result
audio_rectified.plot(figsize=(10, 5))
plt.show()

# Smooth by applying a rolling mean
audio_rectified_smooth = audio_rectified.rolling(50).mean()

# Plot the result
audio_rectified_smooth.plot(figsize=(10, 5))
plt.show()






audio_rectified = audio_df.apply(np.abs)
audio_rectified.plot(figsize=(10, 5))
audio_rectified_smooth = audio_rectified.rolling(50).mean()
audio_rectified_smooth.plot(figsize=(10, 5))

from sklearn.svm import LinearSVC
model = LinearSVC()

# Calculate stats
means = np.mean(audio_rectified_smooth, axis=0)
stds = np.std(audio_rectified_smooth, axis=0)
maxs = np.max(audio_rectified_smooth, axis=0)

# Create the X and y arrays
X = np.column_stack([means, stds, maxs])
y = labels.reshape(-1, 1)

# Fit the model and score on testing data
from sklearn.model_selection import cross_val_score
percent_score = cross_val_score(model, X, y.ravel(), cv=5)
print(np.mean(percent_score))

# print(audio_rectified)
# print(audio_rectified_smooth)

# print(np.mean(audio_rectified.iloc[:, 0]))
# print(np.mean(audio_rectified_smooth.iloc[:, 0]))
# print(np.mean(np.abs(audio), axis=0))
# print(np.mean(np.abs(audio_rectified), axis=0))
# print(np.mean(np.abs(audio_rectified_smooth), axis=0))

# audio_float32 = audio.astype('float32')
# means_abs_32 = audio_float32.abs().mean(axis=0)
# print(means_abs_32)


# means = np.mean(audio_rectified_smooth, axis=0)
# print(means)
# print(audio)

print(means)