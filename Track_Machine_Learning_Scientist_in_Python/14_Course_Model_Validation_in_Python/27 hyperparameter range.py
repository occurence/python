import random
from sklearn.ensemble import RandomForestRegressor

max_depth = [4, 8, 12]
min_samples_split = [2, 5, 10]
max_features = [4, 6, 8, 10]

# Fill in rfr using your variables
rfr = RandomForestRegressor(
    n_estimators=100,
    max_depth=random.choice(max_depth),
    min_samples_split=random.choice(min_samples_split),
    max_features=random.choice(max_features))

# Print out the parameters
print(rfr.get_params())