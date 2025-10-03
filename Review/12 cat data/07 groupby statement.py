import pandas as pd

adult = pd.read_csv(r'D:\STUDY\python\Review\12 cat data\datasets\adult.csv')

# Group the adult dataset by "Sex" and "Above/Below 50k"
gb = adult.groupby(by=['Sex', 'Above/Below 50k'])

# Print out how many rows are in each created group
print(gb.size())

# Print out the mean of each group for all columns
print(gb.mean(numeric_only=True))