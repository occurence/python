import pandas as pd

used_cars = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\16_Course_Working_with_Categorical_Data_in_Python\datasets\cars_rating.csv')

# Print the frequency table of Sale Rating
print(used_cars["Sale Rating"].value_counts())

# Find the average score
average_score = used_cars["Sale Rating"].astype('int').mean()

# Print the average
print(average_score)