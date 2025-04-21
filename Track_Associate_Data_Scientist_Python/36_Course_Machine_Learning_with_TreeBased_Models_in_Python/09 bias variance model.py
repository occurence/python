import pandas as pd
from sklearn.tree import DecisionTreeRegressor

mpg = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\36_Course_Machine_Learning_with_TreeBased_Models_in_Python\datasets\auto.csv')
SEED = 1
mpg = pd.get_dummies(mpg, columns=['origin'], prefix='origin')
mpg = mpg.astype({col: 'uint8' for col in mpg.select_dtypes(include='bool').columns})
X = mpg.drop('mpg', axis=1).values
y = mpg['mpg'].values


# Import train_test_split from sklearn.model_selection
from sklearn.model_selection import train_test_split

# Set SEED for reproducibility
SEED = 1

# Split the data into 70% train and 30% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=SEED)

# Instantiate a DecisionTreeRegressor dt
dt = DecisionTreeRegressor(max_depth=4, min_samples_leaf=0.26, random_state=SEED)

print(mpg)