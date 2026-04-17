import pandas as pd

volunteer = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\11_Course_Preprocessing_for_Machine_Learning_in_Python\datasets\volunteer_opportunities.csv')

# First, convert string column to date column
volunteer["start_date_converted"] = pd.to_datetime(volunteer['start_date_date'])

# Extract just the month from the converted column
volunteer["start_date_month"] = volunteer['start_date_converted'].dt.month

# Take a look at the converted and new month columns
print(volunteer[['start_date_converted', 'start_date_month']].head())