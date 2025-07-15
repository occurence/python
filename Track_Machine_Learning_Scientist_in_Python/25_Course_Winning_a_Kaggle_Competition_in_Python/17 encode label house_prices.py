import pandas as pd

train = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\25_Course_Winning_a_Kaggle_Competition_in_Python\datasets\house_prices\train.csv')
train = train[['Id','LotArea','OverallQual','YearBuilt','RoofStyle','TotalBsmtSF','CentralAir','1stFlrSF','2ndFlrSF','FullBath','HalfBath','BedroomAbvGr','KitchenAbvGr','TotRmsAbvGrd','GarageCars','GarageArea','SalePrice']].rename(columns={'1stFlrSF': 'FirstFlrSF','2ndFlrSF': 'SecondFlrSF'})

test = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\25_Course_Winning_a_Kaggle_Competition_in_Python\datasets\house_prices\test.csv')
test = test[['Id','LotArea','OverallQual','YearBuilt','RoofStyle','TotalBsmtSF','CentralAir','1stFlrSF','2ndFlrSF','FullBath','HalfBath','BedroomAbvGr','KitchenAbvGr','TotRmsAbvGrd','GarageCars','GarageArea']].rename(columns={'1stFlrSF': 'FirstFlrSF','2ndFlrSF': 'SecondFlrSF'})

# Concatenate train and test together
houses = pd.concat([train, test])

# Label encoder
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

# Create new features
houses['RoofStyle_enc'] = le.fit_transform(houses['RoofStyle'])
houses['CentralAir_enc'] = le.fit_transform(houses['CentralAir'])

# Look at new features
print(houses[['RoofStyle', 'RoofStyle_enc', 'CentralAir', 'CentralAir_enc']].head())