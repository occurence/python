# Re-run this cell 
import pandas as pd

# Read in the data
schools = pd.read_csv(r"D:\STUDY\python\Track_Associate_Data_Scientist_Python\05_Project_Exploring_School_Result\schools.csv")

# Preview the data
# print(schools.head())

# Start coding here...
# Add as many cells as you like...

best_math_schools = schools[schools["average_math"] >= 640][['school_name','average_math']].sort_values(['average_math'], ascending=[False])

print(best_math_schools)

schools['total_SAT'] = schools['average_math'] + schools['average_reading'] + schools['average_writing']
top_10_schools = schools[['school_name','total_SAT']].sort_values('total_SAT', ascending=False).head(10)

print(top_10_schools)

schools_borough = schools.groupby('borough')['total_SAT'].agg(["count", "mean", "std"]).round(2)
largest_std_dev = schools_borough[schools_borough['std'] == schools_borough['std'].max()]
largest_std_dev = largest_std_dev.rename(columns={"count": "num_schools", "mean": "average_SAT", "std": "std_SAT"})

print(largest_std_dev)
