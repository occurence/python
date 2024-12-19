import pandas as pd

rides = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\22_Course_Working_with_Dates_and_Times\datasets\bike_duration.csv', 
                    parse_dates = ['Start date', 'End date'])

# Import matplotlib
import matplotlib.pyplot as plt

# Resample rides to monthly, take the size, plot the results
rides.resample('M', on = 'Start date')\
  .size()\
  .plot(ylim = [0, 150])

# Show the results
plt.show()