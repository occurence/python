import pandas as pd

train = pd.read_json(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\25_Course_Winning_a_Kaggle_Competition_in_Python\datasets\rentals\train.json')
test = pd.read_json(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\25_Course_Winning_a_Kaggle_Competition_in_Python\datasets\rentals\test.json')
index = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\25_Course_Winning_a_Kaggle_Competition_in_Python\datasets\rentals\index.csv', index_col=0)
train['id'] = train.index
train = train[['id','bathrooms','bedrooms','building_id','latitude','longitude','manager_id','price','interest_level']].loc[index.index]
train = train.reset_index(drop=True)

print(train.loc[[10]])

# Import StratifiedKFold
from sklearn.model_selection import StratifiedKFold

# Create a StratifiedKFold object
str_kf = StratifiedKFold(n_splits=3, shuffle=True, random_state=123)

# Loop through each split
fold = 0
for train_index, test_index in str_kf.split(train, train['interest_level']):
    # Obtain training and testing folds
    cv_train, cv_test = train.iloc[train_index], train.iloc[test_index]
    print('Fold: {}'.format(fold))
    print('CV train shape: {}'.format(cv_train.shape))
    print('Medium interest listings in CV train: {}\n'.format(sum(cv_train.interest_level == 'medium')))
    fold += 1