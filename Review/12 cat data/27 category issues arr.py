import pandas as pd

used_cars = pd.read_csv(r'D:\STUDY\python\Review\12 cat data\datasets\cars_rating.csv')

# Print the frequency table of Sale Rating
print(used_cars["Sale Rating"].value_counts())

# Find the average score
average_score = used_cars["Sale Rating"].astype(int).mean()

# Print the average
print(average_score)