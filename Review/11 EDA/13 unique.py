import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

planes = pd.read_csv(r'D:\STUDY\python\Review\11 EDA\datasets\planes_clean.csv', index_col=0)

# Filter the DataFrame for object columns
non_numeric = planes.select_dtypes("object")

# Loop through columns
for column in non_numeric.columns:

  # Print the number of unique values
  print(f"Number of unique values in {column} column: ", non_numeric[column].nunique())
