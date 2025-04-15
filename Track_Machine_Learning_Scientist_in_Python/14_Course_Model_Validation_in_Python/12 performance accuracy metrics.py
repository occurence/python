import numpy as np
from sklearn.metrics import mean_absolute_error as mae

y_test = np.array([53, 51, 51, 49, 43, 42, 42, 41, 41, 37, 36, 31, 29, 28, 20, 67, 61, 55, 51, 51, 47, 43, 41, 40, 34, 33, 32, 31, 26, 24])
predictions = np.array([60, 62, 42, 42, 30, 50, 52, 42, 44, 35, 30, 30, 35, 40, 15, 72, 58, 60, 40, 42, 45, 46, 40, 35, 25, 40, 20, 34, 25, 24])
labels = np.array(['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'])

# Find the East conference teams
east_teams = labels == "E"
west_teams = labels == "W"

# Create arrays for the true and predicted values
true_east = y_test[east_teams]
preds_east = predictions[east_teams]
true_west = y_test[west_teams]
preds_west = predictions[west_teams]
west_error = mae(true_west, preds_west)

# Print the accuracy metrics
print('The MAE for East teams is {}'.format(
    mae(true_east, preds_east)))

# Print the West accuracy
print('The MAE for West conference is {}'.format(
    west_error))

print("It looks like the Western conference predictions were about two games better on average. Over the past few seasons, the Western teams have generally won the same number of games as the experts have predicted. Teams in the East are just not as predictable as those in the West.")