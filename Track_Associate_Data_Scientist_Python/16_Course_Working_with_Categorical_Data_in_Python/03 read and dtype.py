import pandas as pd

adult = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\16_Course_Working_with_Categorical_Data_in_Python\datasets\adult.csv')

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
  r"D:\STUDY\python\Track_Associate_Data_Scientist_Python\16_Course_Working_with_Categorical_Data_in_Python\datasets\adult.csv",
  dtype=adult_dtypes
)
print(adult2.dtypes)