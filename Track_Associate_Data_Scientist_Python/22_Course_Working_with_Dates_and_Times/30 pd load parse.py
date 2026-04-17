# Import pandas
import pandas as pd

# Load CSV into the rides variable
rides = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\22_Course_Working_with_Dates_and_Times\datasets\capital-onebike.csv', 
                    parse_dates = ['Start date', 'End date'])

# Print the initial (0th) row
print(rides.iloc[0])