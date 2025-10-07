import pandas as pd
import numpy as np

used_cars = pd.read_csv(r'D:\STUDY\python\Review\12 cat data\datasets\cars_rating.csv')

# Print the "manufacturer_name" frequency table.
print(used_cars["manufacturer_name"].value_counts())

# Create a Boolean column for the most common manufacturer name
used_cars["is_volkswagen"] = np.where(
  used_cars["manufacturer_name"].str.contains("Volkswagen", regex=False), 1, 0
)
  
# Check the final frequency table
print(used_cars["is_volkswagen"].value_counts())