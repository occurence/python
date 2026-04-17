import pandas as pd

train = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\25_Course_Winning_a_Kaggle_Competition_in_Python\datasets\house_prices\train.csv')
train = train[['Id','LotArea','OverallQual','YearBuilt','RoofStyle','TotalBsmtSF','CentralAir','1stFlrSF','2ndFlrSF','FullBath','HalfBath','BedroomAbvGr','KitchenAbvGr','TotRmsAbvGrd','GarageCars','GarageArea','SalePrice']].rename(columns={'1stFlrSF': 'FirstFlrSF','2ndFlrSF': 'SecondFlrSF'})

test = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\25_Course_Winning_a_Kaggle_Competition_in_Python\datasets\house_prices\test.csv')
test = test[['Id','LotArea','OverallQual','YearBuilt','RoofStyle','TotalBsmtSF','CentralAir','1stFlrSF','2ndFlrSF','FullBath','HalfBath','BedroomAbvGr','KitchenAbvGr','TotRmsAbvGrd','GarageCars','GarageArea']].rename(columns={'1stFlrSF': 'FirstFlrSF','2ndFlrSF': 'SecondFlrSF'})

# print(train.head())
# print(test.head())
# print(train['RoofStyle'].value_counts())
# print(train['CentralAir'].value_counts())

# Concatenate train and test together
houses = pd.concat([train, test])

# Label encode binary 'CentralAir' feature
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
houses['CentralAir_enc'] = le.fit_transform(houses['CentralAir'])

# Create One-Hot encoded features
ohe = pd.get_dummies(houses['RoofStyle'], prefix='RoofStyle')

# Concatenate OHE features to houses
houses = pd.concat([houses, ohe], axis=1)

# Look at OHE features
print(houses[[col for col in houses.columns if 'RoofStyle' in col]].head(3))