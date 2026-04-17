import pandas as pd

dogs = pd.read_csv(r'D:\STUDY\python\Review\12 cat data\datasets\dogs.csv')
dogs["likes_children"] = dogs["likes_children"].astype("category")

# Create the my_changes dictionary
my_changes = {'Maybe?': 'Maybe'}

# Rename the categories listed in the my_changes dictionary
dogs["likes_children"] = dogs['likes_children'].cat.rename_categories(my_changes)

# Use a lambda function to convert all categories to uppercase using upper()
dogs["likes_children"] =  dogs["likes_children"].cat.rename_categories(lambda c: c.upper())

# Print the list of categories
print(dogs["likes_children"].cat.categories)