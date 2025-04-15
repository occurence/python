import pandas as pd
import numpy as np

volunteer = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\11_Course_Preprocessing_for_Machine_Learning_in_Python\datasets\volunteer_opportunities.csv')
volunteer = volunteer[['vol_requests', 'title', 'hits', 'category_desc', 'locality', 'region', 'postalcode', 'created_date']]
#Feature engineering processes
volunteer = volunteer.dropna(subset=['category_desc'])
volunteer['vol_requests_lognorm'] = np.log(volunteer['vol_requests'])
volunteer['created_month'] = pd.to_datetime(volunteer['created_date']).dt.month
volunteer = pd.concat([volunteer, pd.get_dummies(volunteer['category_desc'], dtype=int)], axis=1)

# Create a list of redundant column names to drop
to_drop = ["locality", "region", "category_desc", "vol_requests", "created_date"]

# Drop those columns from the dataset
volunteer_subset = volunteer.drop(to_drop, axis=1)

# Print out the head of volunteer_subset
print(volunteer_subset.head())