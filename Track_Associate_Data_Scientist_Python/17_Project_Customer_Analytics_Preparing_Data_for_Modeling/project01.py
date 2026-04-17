# Import necessary libraries
import pandas as pd

# Load the dataset
ds_jobs = pd.read_csv(r"D:\STUDY\python\Track_Associate_Data_Scientist_Python\17_Project_Customer_Analytics_Preparing_Data_for_Modeling\customer_train.csv")

# View the dataset
ds_jobs.head()

# Create a copy of ds_jobs for transforming
ds_jobs_transformed = ds_jobs.copy()

# Start coding here. Use as many cells as you like!