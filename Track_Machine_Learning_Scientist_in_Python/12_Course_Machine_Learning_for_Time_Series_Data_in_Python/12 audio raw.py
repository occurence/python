import pandas as pd
import matplotlib.pyplot as plt

audio = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\12_Course_Machine_Learning_for_Time_Series_Data_in_Python\datasets\abnormal.csv', index_col=0)
audio = round(audio[['0']].iloc[:2205], 3)

# Plot the raw data first
audio.plot(figsize=(10, 5))
plt.show()