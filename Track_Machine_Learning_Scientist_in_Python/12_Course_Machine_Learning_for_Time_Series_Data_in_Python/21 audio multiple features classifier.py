import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from librosa.core import stft, amplitude_to_db
from librosa.display import specshow
from librosa.feature.rhythm import tempo
import librosa as lr

from sklearn.svm import LinearSVC
from sklearn.model_selection import cross_val_score

sfreq = 2205

audio_df = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\12_Course_Machine_Learning_for_Time_Series_Data_in_Python\datasets\audio_60.csv', index_col=0)
audio = audio_df.iloc[:, 0].values
labels = np.array(pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\12_Course_Machine_Learning_for_Time_Series_Data_in_Python\datasets\labels.csv', header=None))

# === Rectify and Smooth === #
audio_rectified = np.abs(audio_df)
audio_rectified_smooth = audio_rectified.rolling(50).mean()

# === Calculate Basic Stats === #
means = np.mean(audio_rectified_smooth, axis=0).values
stds = np.std(audio_rectified_smooth, axis=0).values
maxs = np.max(audio_rectified_smooth, axis=0).values

# === Tempo Features === #
tempos = []
for col, i_audio in audio_df.items():
    # Calculate tempo per channel/column
    tempo_vals = tempo(y=i_audio.values, sr=sfreq, hop_length=2**6, aggregate=None)
    tempos.append(tempo_vals)

tempos = np.array(tempos)

tempo_mean = tempos.mean(axis=-1)
tempo_std = tempos.std(axis=-1)
tempo_max = tempos.max(axis=-1)

# === STFT & Spectral Features === #
HOP_LENGTH = 2**4
spec = np.abs(stft(audio, hop_length=HOP_LENGTH, n_fft=2**7))

# Spectral centroid and bandwidth (computed on magnitude spectrogram)
centroids = lr.feature.spectral_centroid(S=spec)[0]
bandwidths = lr.feature.spectral_bandwidth(S=spec)[0]

# === Optional: Plot for sanity check === #
spec_db = amplitude_to_db(spec)

# Plot raw audio and spectrogram
fig, axs = plt.subplots(2, 1, figsize=(10, 10), sharex=True)
axs[0].plot(audio_df.index, audio)
specshow(spec_db, sr=sfreq, x_axis='time', y_axis='hz', hop_length=HOP_LENGTH, ax=axs[1])
plt.show()

# Plot spectral features over the spectrogram
fig, ax = plt.subplots(figsize=(10, 5))
specshow(spec_db, sr=sfreq, x_axis='time', y_axis='hz', hop_length=HOP_LENGTH, ax=ax)
ax.plot(np.linspace(0, len(audio) / sfreq, num=len(centroids)), centroids, label="Centroid")
ax.fill_between(np.linspace(0, len(audio) / sfreq, num=len(bandwidths)),
                centroids - bandwidths / 2, centroids + bandwidths / 2,
                alpha=0.5, label="Bandwidth")
ax.legend()
ax.set(ylim=[None, 6000])
plt.show()

# === Prepare Final Feature Set === #
# Flatten spectral features to fit in X (optional: you could also compute stats instead)
centroids_mean = np.mean(centroids)
centroids_std = np.std(centroids)
bandwidths_mean = np.mean(bandwidths)
bandwidths_std = np.std(bandwidths)

n_samples = means.shape[0]  # should be 60

# Repeat scalar spectral stats for each row (match the row count)
centroids_mean_arr = np.full((n_samples,), centroids_mean)
centroids_std_arr = np.full((n_samples,), centroids_std)
bandwidths_mean_arr = np.full((n_samples,), bandwidths_mean)
bandwidths_std_arr = np.full((n_samples,), bandwidths_std)

# Combine all features into X
X = np.column_stack([
    means, stds, maxs,                # rectified stats
    tempo_mean, tempo_std, tempo_max, # tempo stats
    bandwidths_mean_arr, bandwidths_std_arr,
    centroids_mean_arr, centroids_std_arr
])


y = labels.reshape(-1, 1)

# === Train and Evaluate === #
model = LinearSVC(max_iter=10000)  # Increased iterations just in case
percent_score = cross_val_score(model, X, y.ravel(), cv=5)
print(f'Mean cross-validation score: {np.mean(percent_score):.4f}')
