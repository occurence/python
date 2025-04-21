from sklearn.ensemble import RandomForestRegressor

rfr = RandomForestRegressor(random_state=1111)

# Review the parameters of rfr
print(rfr.get_params())

# Maximum Depth
max_depth = [4, 8, 12]

# Minimum samples for a split
min_samples_split = [2, 5, 10]

# Max features 
max_features = [4, 6, 8, 10]

print("Hyperparameter tuning requires selecting parameters to tune, as well the possible values these parameters can be set to.")