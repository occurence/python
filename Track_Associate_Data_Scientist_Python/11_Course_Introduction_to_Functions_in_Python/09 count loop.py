# Import pandas
import pandas as pd

# Import Twitter data as DataFrame: df
df = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\11_Course_Introduction_to_Functions_in_Python\datasets\tweets.csv')

# Initialize an empty dictionary: langs_count
langs_count = {}

# Extract column from DataFrame: col
col = df['lang']

# Iterate over lang column in DataFrame
for entry in col:

    # If the language is in langs_count, add 1 
    if entry in langs_count.keys():
        langs_count[entry] += 1
    # Else add the language to langs_count, set the value to 1
    else:
        langs_count[entry] = 1

# Print the populated dictionary
print(langs_count)