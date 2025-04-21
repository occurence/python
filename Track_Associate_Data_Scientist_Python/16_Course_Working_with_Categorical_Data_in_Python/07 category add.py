import pandas as pd

dogs = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\16_Course_Working_with_Categorical_Data_in_Python\datasets\ShelterDogs.csv')

# Check frequency counts while also printing the NaN count
print(dogs["keep_in"].value_counts(dropna=False))

# Switch to a categorical variable
dogs["keep_in"] = dogs["keep_in"].astype("category")

# Add new categories
new_categories = ["Unknown History", "Open Yard (Countryside)"]
dogs["keep_in"] = dogs["keep_in"].cat.add_categories(new_categories)

# Check frequency counts one more time
print(dogs['keep_in'].value_counts(dropna=False))