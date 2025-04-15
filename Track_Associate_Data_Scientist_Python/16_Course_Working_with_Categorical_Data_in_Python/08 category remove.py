import pandas as pd

dogs = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\16_Course_Working_with_Categorical_Data_in_Python\datasets\dogs.csv')
dogs["likes_children"] = dogs["likes_children"].astype("category")

# Set "maybe" to be "no"
dogs.loc[dogs["likes_children"] == "maybe", "likes_children"] = "no"

# Print out categories
print(dogs["likes_children"].cat.categories)

# Print the frequency table
print(dogs["likes_children"].value_counts())

# Remove the "maybe" category
dogs["likes_children"] = dogs["likes_children"].cat.remove_categories(["maybe"])
print(dogs["likes_children"].value_counts())

# Print the categories one more time
print(dogs['likes_children'].cat.categories)