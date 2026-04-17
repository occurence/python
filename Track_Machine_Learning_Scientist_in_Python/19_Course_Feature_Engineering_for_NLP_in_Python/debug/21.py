import pandas as pd
from sklearn.model_selection import train_test_split

reviews = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\19_Course_Feature_Engineering_for_NLP_in_Python\datasets\movie_reviews_clean.csv')
index = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\19_Course_Feature_Engineering_for_NLP_in_Python\datasets\train_250.csv', header=None, index_col=0)
X = reviews.drop("sentiment", axis=1)
y = reviews["sentiment"].values

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.75, random_state=631)
# print(reviews.iloc[446])

X_train = reviews.iloc[index.index]['review']
X_test = reviews.drop(index.index)['review']
y_train = reviews.iloc[index.index]['sentiment']
y_test = reviews.drop(index.index)['sentiment']
# y_train = reviews[['sentiment']].iloc[index.index]
# y_train = y_train.values.ravel()

print(type(X_test))

# print(index.index)