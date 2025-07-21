import pandas as pd

dogs = pd.read_csv(r'D:\STUDY\python\Review\04 dataframe inspect\dogs.csv')

# Methods
print(dogs.head())
print(dogs.info())
print(dogs.describe())
print(dogs.isna().sum())
print(dogs['breed'].value_counts())

# Attributes
print(dogs.values)
print(dogs.columns)
print(dogs.index)
print(dogs.shape)

print(dogs)

# Sort Rows
print(dogs.sort_values('breed', ascending=False).head(5))
# Subset Cols
print(dogs[['birth','height_cm']])
# Subset Rows
print(dogs[(dogs['breed'] < 'Labrador') & (dogs['color'] == 'Black')])
# Subset Rows isin Categorical Variables
canu = ["Labrador", "Poodle", "Chihuahua"]
print(dogs[dogs['breed'].isin(canu)])

# Add/Mutate/Transform/Feature Engineering/convert
dogs['height_m'] = dogs['height_cm'] / 100
dogs['bmi'] = dogs['weight_kg'] / dogs['height_m'] ** 2
dogs_skinny = dogs[dogs['bmi'] < 100]
dogs_skinny_height = dogs_skinny.sort_values('height_cm', ascending=False)
print(dogs_skinny_height[['name','height_cm','bmi']])