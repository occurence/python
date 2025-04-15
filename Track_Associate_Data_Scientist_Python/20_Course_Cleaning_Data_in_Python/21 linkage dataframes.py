import pandas as pd
import recordlinkage

restaurants = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\20_Course_Cleaning_Data_in_Python\datasets\restaurant_pair.csv')
restaurants_new = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\20_Course_Cleaning_Data_in_Python\datasets\restaurant_new.csv')
indexer = recordlinkage.Index()
indexer.block('cuisine_type')
pairs = indexer.index(restaurants, restaurants_new)

comp_cl = recordlinkage.Compare()
comp_cl.exact('city', 'city', label='city')
comp_cl.exact('cuisine_type', 'cuisine_type', label='cuisine_type')
comp_cl.string('rest_name', 'rest_name', label='name', threshold = 0.8) 
potential_matches = comp_cl.compute(pairs, restaurants, restaurants_new)
print(potential_matches)








# Isolate potential matches with row sum >=3
matches = potential_matches[potential_matches.sum(axis=1) >= 3]

# Get values of second column index of matches
matching_indices = matches.index.get_level_values(1)

# Subset restaurants_new based on non-duplicate values
non_dup = restaurants_new[~restaurants_new.index.isin(matching_indices)]

# Append non_dup to restaurants
# full_restaurants = restaurants.append(non_dup)
full_restaurants = pd.concat([restaurants, non_dup], ignore_index=True)
print(full_restaurants)