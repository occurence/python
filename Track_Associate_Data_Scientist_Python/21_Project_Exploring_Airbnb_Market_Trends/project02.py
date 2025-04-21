# Import necessary packages
import pandas as pd
import numpy as np

airbnb_price = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\21_Project_Exploring_Airbnb_Market_Trends\airbnb_price.csv')
airbnb_room_type = pd.read_excel(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\21_Project_Exploring_Airbnb_Market_Trends\airbnb_room_type.xlsx')
airbnb_last_review = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\21_Project_Exploring_Airbnb_Market_Trends\airbnb_last_review.tsv', parse_dates=['last_review'], sep='\t')

# Begin coding here ...
# Use as many cells as you like

listings = airbnb_price.merge(airbnb_room_type, on='listing_id').merge(airbnb_last_review, on='listing_id', suffixes=('_type2','_review3'))

# What are the dates of the earliest and most recent reviews? Store these values as two separate variables with your preferred names.
first_reviewed = listings['last_review'].dt.date.min()
last_reviewed = listings['last_review'].dt.date.max()
print(f'The earliest review: {first_reviewed}')
print(f'The recent review: {last_reviewed}')

# How many of the listings are private rooms? Save this into any variable.
private_room_count = listings[listings['room_type'].str.lower() == 'private room'].shape[0]
print(f'There are {private_room_count} private rooms')

# What is the average listing price? Round to the nearest two decimal places and save into a variable.
listings['price'] = listings['price'].str.strip('dollars').astype('float')
avg_price = listings['price'].mean().round(2)
print(f'The average price: {avg_price}')

# Combine the new variables into one DataFrame called review_dates with four columns in the following order: first_reviewed, last_reviewed, nb_private_rooms, and avg_price. The DataFrame should only contain one row of values.
review_dates = pd.DataFrame({
    'first_reviewed': [first_reviewed],
    'last_reviewed': [last_reviewed],
    'nb_private_rooms': [private_room_count],
    'avg_price': [avg_price]
})
print(review_dates)