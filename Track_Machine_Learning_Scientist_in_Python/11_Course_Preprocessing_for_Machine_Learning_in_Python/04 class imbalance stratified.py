import pandas as pd
from sklearn.model_selection import train_test_split

volunteer = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\11_Course_Preprocessing_for_Machine_Learning_in_Python\datasets\volunteer_opportunities.csv')

volunteer = volunteer.drop(['Latitude', 'Longitude'], axis=1)
volunteer = volunteer.dropna(subset=['category_desc'])
# print(volunteer.shape)

# Create a DataFrame with all columns except category_desc
X = volunteer.drop('category_desc', axis=1)

# Create a category_desc labels dataset
y = volunteer[['category_desc']]

# Use stratified sampling to split up the dataset according to the y dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

# Print the category_desc counts from y_train
print(y_train['category_desc'].value_counts())