import pandas as pd

seattle_weather = pd.read_csv(r'D:\STUDY\python\Review\07 matplotlib\datasets\seattle_weather_axes.csv')
austin_weather = pd.read_csv(r'D:\STUDY\python\Review\07 matplotlib\datasets\austin_weather_axes.csv')

# Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt

# Create a Figure and an Axes with plt.subplots
fig, ax = plt.subplots()

# Plot MLY-PRCP-NORMAL from seattle_weather against the MONTH
ax.plot(seattle_weather["MONTH"], seattle_weather['MLY-PRCP-NORMAL'])

# Plot MLY-PRCP-NORMAL from austin_weather against MONTH
ax.plot(austin_weather['MONTH'], austin_weather['MLY-PRCP-NORMAL'])

# Call the show function
plt.show()