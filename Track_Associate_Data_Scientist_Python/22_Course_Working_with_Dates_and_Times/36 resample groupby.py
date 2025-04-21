import pandas as pd

rides = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\22_Course_Working_with_Dates_and_Times\datasets\bike_duration.csv', 
                    parse_dates = ['Start date', 'End date'])

# Group rides by member type, and resample to the month
grouped = rides.groupby('Member type')\
  .resample('M', on='Start date')

# Print the median duration for each group
print(grouped['Duration'].median())