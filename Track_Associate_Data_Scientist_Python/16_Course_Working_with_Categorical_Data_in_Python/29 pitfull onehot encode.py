import pandas as pd

used_cars = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\16_Course_Working_with_Categorical_Data_in_Python\datasets\cars_rating.csv')

# Create one-hot encoding for just two columns
used_cars_simple = pd.get_dummies(
  used_cars,
  # Specify the columns from the instructions
  columns=['manufacturer_name','transmission'],
  # Set the prefix
  prefix='dummy'
)

# Print the shape of the new dataset
print(used_cars_simple.shape)