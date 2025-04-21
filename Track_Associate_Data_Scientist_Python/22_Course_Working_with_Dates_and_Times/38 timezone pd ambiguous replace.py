import pandas as pd

rides = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\22_Course_Working_with_Dates_and_Times\datasets\bike_duration.csv', 
                    parse_dates = ['Start date', 'End date'])

# Localize the Start date column to America/New_York
rides['Start date'] = rides['Start date'].dt.tz_localize('America/New_York', 
                                						 ambiguous='NaT')

# Print first value
print(rides['Start date'].iloc[0])

# Convert the Start date column to Europe/London
rides['Start date'] = rides['Start date'].dt.tz_convert('Europe/London')

# Print the new value
print(rides['Start date'].iloc[0])