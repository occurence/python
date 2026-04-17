import pandas as pd
from sklearn.model_selection import train_test_split

cc = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\15_Course_Hyperparameter_Tuning_in_Python\datasets\credit-card-full.csv')
X_train = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\15_Course_Hyperparameter_Tuning_in_Python\datasets\X_train.csv')

X = cc.iloc[:, :-1]
y = cc.iloc[:, -1]

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# sampled = cc.sample(1600, random_state=98170)
# 9012, 14402, 40664, 85841, 98170
# print(sampled.index)
# print(X_train.index)

for seed in range(30000):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=seed)

    # Compare the dataframes after resetting index (to ignore index mismatch)
    if X_train.reset_index(drop=True).equals(X_train):
        print(f"🎯 Found matching random_state: {seed}")
        break
    else:
        print("❌ No matching random_state found in tested range.")