import pandas as pd
import matplotlib.pyplot as plt

seattle_weather = pd.read_csv(r'D:\STUDY\python\Review\07 matplotlib\datasets\seattle_weather_axes.csv', index_col=0)
austin_weather = pd.read_csv(r'D:\STUDY\python\Review\07 matplotlib\datasets\austin_weather_axes.csv', index_col=0)

fig, ax = plt.subplots()

# Add Seattle temperature data in each month with error bars
ax.errorbar(seattle_weather['MONTH'], seattle_weather['MLY-TAVG-NORMAL'], seattle_weather['MLY-TAVG-STDDEV'])

# Add Austin temperature data in each month with error bars
ax.errorbar(austin_weather['MONTH'], austin_weather['MLY-TAVG-NORMAL'], austin_weather['MLY-TAVG-STDDEV']) 

# Set the y-axis label
ax.set_ylabel('Temperature (Fahrenheit)')

plt.show()