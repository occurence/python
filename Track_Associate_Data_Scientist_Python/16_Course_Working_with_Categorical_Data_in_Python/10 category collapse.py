import pandas as pd

dogs = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\16_Course_Working_with_Categorical_Data_in_Python\datasets\dogs_rename.csv')

# Create the update_coats dictionary
update_coats = {'wirehaired': 'medium',
                'medium-long': 'medium'}

# Create a new column, coat_collapsed
dogs["coat_collapsed"] = dogs['coat'].replace(update_coats)

# Convert the column to categorical
dogs['coat_collapsed'] = dogs['coat_collapsed'].astype('category')

# Print the frequency table
print(dogs['coat_collapsed'].value_counts())