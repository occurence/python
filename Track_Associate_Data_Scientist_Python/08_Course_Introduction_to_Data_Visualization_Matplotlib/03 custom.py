import pandas as pd
import matplotlib.pyplot as plt
austin_weather = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\08_Course_Introduction_to_Data_Visualization_Matplotlib\datasets\austin.csv')
seattle_weather = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\08_Course_Introduction_to_Data_Visualization_Matplotlib\datasets\seattle.csv')
fig, ax = plt.subplots()

# Plot Seattle data, setting data appearance
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"], color='b', marker='o', linestyle='--')

# Plot Austin data, setting data appearance
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"], color='r', marker='v', linestyle='--')

# Call show to display the resulting plot
plt.show()