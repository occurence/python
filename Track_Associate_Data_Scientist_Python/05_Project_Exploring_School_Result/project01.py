# Re-run this cell 
import pandas as pd

# Read in the data
schools = pd.read_csv(r"Project_Exploring_School_Result\schools.csv")

# Preview the data
print(schools.head())

# Start coding here...
# Add as many cells as you like...

best_math_schools = schools[['school_name','average_math']].sort_values(['school_name','average_math'], ascending=[True,False])
# print(best_math_schools)

schools['total_SAT'] = schools['average_math'] + schools['average_reading'] + schools['average_writing']
top_10_schools = schools[['school_name','total_SAT']].sort_values('total_SAT', ascending=False)
# print(top_10_schools)

# largest_std_dev = schools[]
# print(schools.groupby('borough')['total_SAT'].std())
# schools_borough = schools.set_index('borough')
# schools_borough = schools.reset_index(drop=True)
# schools_borough = schools.groupby('borough')['total_SAT'].std().rename('std_SAT')
schools_borough = schools.groupby('borough')['total_SAT'].std().reset_index(name='total_SAT')
# print(schools_borough)
# print(schools_borough[schools_borough['total_SAT'] == schools_borough['total_SAT'].max()])
max_borough = schools_borough.loc[schools_borough['total_SAT'].idxmax(), 'borough']
print(max_borough)

# print(schools.groupby('borough')['total_SAT'].max())
# print(schools.groupby('borough')['school_name'].count())
# print(schools['total_SAT'].mean())
# print(schools['total_SAT'].std())
# largest_std_dev = schools.groupby('borough')['total_SAT'].std().max(),schools.groupby('borough')['total_SAT'].max().max(),schools['total_SAT'].mean(),schools['total_SAT'].std()
largest_std_dev = max_borough,schools.groupby('borough')['total_SAT'].max().max(),schools['total_SAT'].mean(),schools['total_SAT'].std()

print(largest_std_dev)