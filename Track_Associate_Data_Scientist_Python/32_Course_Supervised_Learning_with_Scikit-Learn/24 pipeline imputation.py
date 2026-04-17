# Import modules
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier

# Instantiate an imputer
imputer = SimpleImputer()

# Instantiate a knn model
knn = KNeighborsClassifier(n_neighbors=3)

# Build steps for the pipeline
steps = [("imputer", imputer), 
         ("knn", knn)]

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
music_df = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\32_Course_Supervised_Learning_with_Scikit-Learn\datasets\music_missing.csv')
# print(music_df.isna().sum().sort_values())
print("Before dropna:", music_df["genre"].value_counts())
music_df = music_df.dropna(subset=["genre", "popularity", "loudness", "liveness", "tempo"])
print("After dropna:", music_df["genre"].value_counts())
music_df["genre"] = np.where(music_df["genre"] == "Rock", 1, 0)
# print(music_df.isna().sum().sort_values())
# print("Shape of the `music_df`: {}".format(music_df.shape))
X = music_df.drop('genre', axis=1).values
y = music_df['genre'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)# stratify=y

# Create the pipeline
pipeline = Pipeline(steps)

# Fit the pipeline to the training data
pipeline.fit(X_train, y_train)

# Make predictions on the test set
y_pred = pipeline.predict(X_test)

# Print the confusion matrix
print(confusion_matrix(y_test, y_pred))

print(f"X_train shape: {X_train.shape}, X_test shape: {X_test.shape}")
print(f"y_train shape: {y_train.shape}, y_test shape: {y_test.shape}")
print("Train class distribution:", np.bincount(y_train))
print("Test class distribution:", np.bincount(y_test))

# Find the test size ratio used in train_test_split
test_size_ratio = len(X_test) / (len(X_train) + len(X_test))
print(f"Test size ratio used: {test_size_ratio:.2f}")