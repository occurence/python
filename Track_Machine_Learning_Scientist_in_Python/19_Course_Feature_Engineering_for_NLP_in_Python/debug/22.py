import pandas as pd
from sklearn.model_selection import train_test_split

reviews = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\19_Course_Feature_Engineering_for_NLP_in_Python\datasets\movie_reviews_clean.csv')
X = reviews.drop("sentiment", axis=1)
y = reviews["sentiment"].values

# Assume X and y are already defined
target_indices = [446, 937, 316]
random_state = 0

while True:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.75, random_state=random_state)
    
    if list(X_train.index[:3]) == target_indices:
        print(f"Found! Random state: {random_state}")
        break
    
    random_state += 1
