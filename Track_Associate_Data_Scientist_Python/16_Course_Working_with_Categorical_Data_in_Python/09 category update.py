import pandas as pd

dogs = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\16_Course_Working_with_Categorical_Data_in_Python\datasets\dogs_rename.csv')
dogs['likes_children'] = dogs['likes_children'].astype('category')

# Create the my_changes dictionary
my_changes = {'Maybe?': 'Maybe'}

# Rename the categories listed in the my_changes dictionary
dogs["likes_children"] = dogs['likes_children'].cat.rename_categories(my_changes)

# Use a lambda function to convert all categories to uppercase using upper()
dogs["likes_children"] =  dogs["likes_children"].cat.rename_categories(lambda c: c.upper())

# Print the list of categories
print(dogs['likes_children'].cat.categories)