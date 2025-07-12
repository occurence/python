import pandas as pd

train = pd.read_json(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\25_Course_Winning_a_Kaggle_Competition_in_Python\datasets\rentals\train.json')
test = pd.read_json(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\25_Course_Winning_a_Kaggle_Competition_in_Python\datasets\rentals\test.json')
index = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\25_Course_Winning_a_Kaggle_Competition_in_Python\datasets\rentals\index.csv', index_col=0)
train['id'] = train.index
# train = train.assign(id=train.index).reset_index(drop=True)
train = train[['id','bathrooms','bedrooms','building_id','latitude','longitude','manager_id','price','interest_level']].loc[index.index]
train = train.reset_index(drop=True)
# train = train.reset_index().rename(columns={'index': 'id'})
# train = train.sample(n=1000, random_state=123)
# print(train.head())
# print(train.describe())
# print(train.info())

# print(train.loc[9])
# print(train.loc[10])
# print(train.iloc[9])
# print(train.iloc[10])
# print(train[9])
print(train.loc[[10]])
# print(train)