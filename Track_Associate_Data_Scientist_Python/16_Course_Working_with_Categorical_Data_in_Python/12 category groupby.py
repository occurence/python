import pandas as pd

dogs = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\16_Course_Working_with_Categorical_Data_in_Python\datasets\dogs_rename.csv')
dogs['size'] = dogs['size'].astype('category')

# Previous code
dogs["size"] = dogs["size"].cat.reorder_categories(
  new_categories=["small", "medium", "large"],
  ordered=True
#   ,inplace=True
)

# How many Male/Female dogs are available of each size?
print(dogs.groupby('size')['sex'].value_counts())

# Do larger dogs need more room to roam?
print(dogs.groupby('size')['keep_in'].value_counts())