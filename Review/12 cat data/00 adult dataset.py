import pandas as pd

adult = pd.read_csv(r'D:\STUDY\python\Review\12 cat data\datasets\adult.csv')
list_of_occupations = pd.read_csv(r'D:\STUDY\python\Review\12 cat data\datasets\occupations.csv', header=None)[0].tolist()

# Explore the Above/Below 50k variable
print(adult["Above/Below 50k"].describe())

# Print a frequency table of "Above/Below 50k"
print(adult["Above/Below 50k"].value_counts())

# Print relative frequency values
print(adult["Above/Below 50k"].value_counts(normalize=True))

# Create a Series, default dtype
series1 = pd.Series(list_of_occupations)

# Print out the data type and number of bytes for series1
print("series1 data type:", series1.dtype)
print("series1 number of bytes:", series1.nbytes)

# Create a Series, "category" dtype
series2 = pd.Series(list_of_occupations, dtype="category")

# Print out the data type and number of bytes for series2
print("series2 data type:", series2.dtype)
print("series2 number of bytes:", series2.nbytes)

# Check the dtypes
print(adult.dtypes)

# Create a dictionary with column names as keys and "category" as values
adult_dtypes = {
   "Workclass": "category",
   "Education": "category",
   "Relationship": "category",
   "Above/Below 50k": "category" 
}

# Read in the CSV using the dtypes parameter
adult2 = pd.read_csv(
  r'D:\STUDY\python\Review\12 cat data\datasets\adult.csv',
  dtype=adult_dtypes
)
print(adult2.dtypes)

print(adult['Above/Below 50k'].value_counts())
adult1 = adult[adult['Above/Below 50k'] == ' <=50K']
adult2 = adult[adult['Above/Below 50k'] == ' >50K']

adult_obj = adult.groupby(by=['Above/Below 50k'])
print(adult_obj.mean(numeric_only=True))
print(adult.groupby(by=['Above/Below 50k']).mean(numeric_only=True))

print(adult.groupby(by=['Above/Below 50k'])[['Age', 'Education Num']].sum())
print(adult.groupby(by=['Above/Below 50k']).sum()[['Age', 'Education Num']])

print(adult.groupby(by=['Above/Below 50k', 'Marital Status']).size())