import pandas as pd
import matplotlib.pyplot as plt

seattle_weather = pd.read_csv(r'D:\STUDY\python\Review\07 matplotlib\datasets\seattle_weather_axes.csv')
austin_weather = pd.read_csv(r'D:\STUDY\python\Review\07 matplotlib\datasets\austin_weather_axes.csv')

fig, ax = plt.subplots()

# ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"])
# ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"])
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"], color='b', marker='o', linestyle='--')
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"], color='r', marker='v', linestyle='--')

# Customize the x-axis label
ax.set_xlabel("Time (months)")

# Customize the y-axis label
ax.set_ylabel("Precipitation (inches)")

# Add the title
ax.set_title("Weather patterns in Austin and Seattle")

# Display the figure
plt.show()