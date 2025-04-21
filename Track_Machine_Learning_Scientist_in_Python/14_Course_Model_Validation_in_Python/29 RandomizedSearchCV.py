from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import make_scorer, mean_squared_error

# Finish the dictionary by adding the max_depth parameter
param_dist = {'max_depth': [4, 6, 8, None],
              'max_features': range(2, 10, 2),
              'min_samples_split': range(4, 20, 4)}

# Create a random forest regression model
rfr = RandomForestRegressor(n_estimators=20, random_state=1111)

# Create a scorer to use (use the mean squared error)
scorer = make_scorer(mean_squared_error)

# Import the method for random search
from sklearn.model_selection import RandomizedSearchCV

# Build a random search using param_dist, rfr, and scorer
random_search =\
    RandomizedSearchCV(
        estimator=rfr,
        param_distributions=param_dist,
        n_iter=10,
        cv=5,
        scoring=scorer)

print("Although it takes a lot of steps, hyperparameter tuning with random search is well worth it and can improve the accuracy of your models. Plus, you are already using cross-validation to validate your best model.")