csv_filepath = 'https://assets.datacamp.com/production/repositories/3996/datasets/7ac19e11cf7ed61205ffe8da5208794b8e2a5086/1.2.1_example_csv.csv'

# Import pandas
import pandas as pd

# Create a DataFrame from csv file
df = pd.read_csv(csv_filepath)

# Print the head of df
print(df.head())