import pandas as pd

adult = pd.read_csv(r'D:\STUDY\python\Review\12 cat data\datasets\adult.csv')

# Create a list of user-selected variables
user_list = ['Education', 'Above/Below 50k']

# Create a GroupBy object using this list
gb = adult.groupby(by=user_list)

# Find the mean for the variable "Hours/Week" for each group - Be efficient!
print(gb['Hours/Week'].mean())