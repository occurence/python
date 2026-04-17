import pandas as pd
import matplotlib.pyplot as plt

seattle_weather = pd.read_csv(r'D:\STUDY\python\Review\07 matplotlib\datasets\seattle_weather_axes.csv')
austin_weather = pd.read_csv(r'D:\STUDY\python\Review\07 matplotlib\datasets\austin_weather_axes.csv')

# Use the "ggplot" style and create new Figure/Axes
plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"])
plt.show()

# Use the "Solarize_Light2" style and create new Figure/Axes
plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.plot(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"])
plt.show()

# Save as a PNG file
fig.savefig(r'D:\STUDY\python\Review\07 matplotlib\graphs\my_figure.png')

# Save as a PNG file with 300 dpi
fig.savefig(r'D:\STUDY\python\Review\07 matplotlib\graphs\my_figure_300dpi.png', dpi=300)

# Set figure dimensions and save as a PNG
fig.savefig(r'D:\STUDY\python\Review\07 matplotlib\graphs\figure_3_5.png')
fig.set_size_inches([3, 5])

# Set figure dimensions and save as a PNG
fig.savefig(r'D:\STUDY\python\Review\07 matplotlib\graphs\figure_5_3.png')
fig.set_size_inches([5, 3])