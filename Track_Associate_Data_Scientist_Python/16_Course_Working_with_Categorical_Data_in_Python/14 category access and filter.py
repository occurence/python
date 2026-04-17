import pandas as pd

dogs = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\16_Course_Working_with_Categorical_Data_in_Python\datasets\dogs.csv', index_col=0)

# Print the category of the coat for ID 23807
print(dogs.loc[23807, 'coat'])

# Find the count of male and female dogs who have a "long" coat
print(dogs.loc[dogs['coat'] == 'long', 'sex'].value_counts())

# Print the mean age of dogs with a breed of "English Cocker Spaniel"
print(dogs.loc[dogs['breed'] == 'English Cocker Spaniel', 'age'].mean())

# Count the number of dogs that have "English" in their breed name
print(dogs[dogs["breed"].str.contains('English', regex=False)].shape[0])