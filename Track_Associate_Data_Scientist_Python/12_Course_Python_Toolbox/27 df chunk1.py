# Import the pandas package
import pandas as pd

# Initialize reader object: df_reader
df_reader = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\12_Course_Python_Toolbox\datasets\ind_pop.csv', chunksize = 10)

# Print two chunks
print(next(df_reader))
print(next(df_reader))