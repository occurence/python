import pandas as pd
import matplotlib.pyplot as plt

mens_rowing = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\08_Course_Introduction_to_Data_Visualization_Matplotlib\datasets\mens_rowing.csv')
mens_gymnastics = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\08_Course_Introduction_to_Data_Visualization_Matplotlib\datasets\mens_gymnastics.csv')

fig, ax = plt.subplots()

# Add a bar for the rowing "Height" column mean/std
ax.bar('Rowing', mens_rowing['Height'].mean(), yerr=mens_rowing['Height'].std())

# Add a bar for the gymnastics "Height" column mean/std
ax.bar('Gymnastics', mens_gymnastics['Height'].mean(), yerr=mens_gymnastics['Height'].std())

# Label the y-axis
ax.set_ylabel('Height (cm)')

plt.show()