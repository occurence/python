import pandas as pd

dogs = pd.read_csv(r'D:\STUDY\python\Review\04 dataframe inspect\dogs.csv')
vet = pd.read_csv(r'D:\STUDY\python\Review\04 dataframe inspect\vet_visits.csv')

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

# Sort Rows, Subset Cols, Subset Rows, New Cols
dogs['breed_pop'] = dogs['breed'].map(dogs['breed'].value_counts(normalize=True))
dogs_skinny_breed = dogs[dogs['bmi'] < 100]
dogs_skinny_breed_srt = dogs_skinny_breed.sort_values('breed_pop', ascending=False)
print(dogs_skinny_breed_srt)

# Summary Statistics
print(dogs['weight_kg'].mean())
print(dogs['weight_kg'].median())
# Aggregate Functions
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
print(dogs[["weight_kg"]].agg([iqr,'median']))

# Cumulative Statistics
max_lab = vet[(vet['name'] == 'Max') & (vet['breed'] == 'Labrador')]
max_lab = max_lab.sort_values('date', ascending=True)
max_lab['cum_max_weight'] = max_lab['weight_kg'].cummax()
print(max_lab[["date", "weight_kg", "cum_max_weight"]])

# Count, Remove Duplicates and Categorical
unique_dogs = vet.drop_duplicates(subset=['name','breed'])
print(unique_dogs)
print(unique_dogs['breed'].value_counts(sort=True))
print(unique_dogs['breed'].value_counts(normalize=True))