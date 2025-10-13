# Import pandas as pd
import pandas as pd

# Assign the filename: file
file = r'D:\STUDY\python\Review\13 import data\datasets\titanic_sub.csv'

# Read the file into a DataFrame: df
df = pd.read_csv(file)

# View the head of the DataFrame
print(df.head())