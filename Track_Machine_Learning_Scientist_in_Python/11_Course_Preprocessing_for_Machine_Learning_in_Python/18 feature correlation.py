import pandas as pd

wine = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\11_Course_Preprocessing_for_Machine_Learning_in_Python\datasets\wine_types.csv')
wine = wine[['Flavanoids','Total phenols','Malic acid','OD280/OD315 of diluted wines','Hue']]

# Print out the column correlations of the wine dataset
print(wine.corr())

# Drop that column from the DataFrame
wine = wine.drop(['Flavanoids'], axis=1)

print(wine.head())