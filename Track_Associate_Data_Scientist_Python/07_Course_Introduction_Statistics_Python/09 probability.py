import pandas as pd
import numpy as np

amir_deals = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\07_Course_Introduction_Statistics_Python\datasets\amir_deals.csv')


# Count the deals for each product
counts = amir_deals['product'].value_counts()

# Calculate probability of picking a deal with each product
probs = counts/amir_deals.shape[0]
print(probs)