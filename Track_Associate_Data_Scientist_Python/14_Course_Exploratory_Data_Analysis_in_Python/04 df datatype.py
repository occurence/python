import pandas as pd

unemployment = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\14_Course_Exploratory_Data_Analysis_in_Python\datasets\clean_unemployment.csv')

# Update the data type of the 2019 column to a float
unemployment["2019"] = unemployment["2019"].astype('float')
# Print the dtypes to check your work
print(unemployment.dtypes)