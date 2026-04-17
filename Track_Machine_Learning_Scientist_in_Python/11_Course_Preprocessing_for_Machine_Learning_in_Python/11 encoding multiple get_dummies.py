import pandas as pd

volunteer = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\11_Course_Preprocessing_for_Machine_Learning_in_Python\datasets\volunteer_opportunities.csv')

# Transform the category_desc column
# category_enc = pd.get_dummies(volunteer['category_desc'])
category_enc = pd.get_dummies(volunteer['category_desc'], dtype=int)

# Take a look at the encoded columns
print(category_enc.head())