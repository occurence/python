import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

combinations_list = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\15_Course_Hyperparameter_Tuning_in_Python\datasets\combinations_list.csv')
data = combinations_list.values.tolist()
x_lims = [0.01, 1.5]
y_lims = [10, 29]

# learn_rate = np.linspace(x_lims[0], x_lims[1], 100)
# min_samples_leaf = list(range(y_lims[0], y_lims[1]))
# combinations_list = [[x, y] for x in learn_rate for y in min_samples_leaf]

def sample_and_visualize_hyperparameters(n_samples):

  # If asking for all combinations, just return the entire list.
  if n_samples == len(combinations_list):
    # combinations_random_chosen = combinations_list
    combinations_random_chosen = combinations_list.values.tolist()
  else:
    combinations_random_chosen = []
    random_combinations_index = np.random.choice(range(0, len(combinations_list)), n_samples, replace=False)
    # combinations_random_chosen = [combinations_list[x] for x in random_combinations_index]
    combinations_random_chosen = [combinations_list.iloc[x] for x in random_combinations_index]

    
  # Pull out the X and Y to plot
  rand_y, rand_x = [x[0] for x in combinations_random_chosen], [x[1] for x in combinations_random_chosen]

  # Plot 
  plt.clf() 
  plt.scatter(rand_y, rand_x, c=['blue']*len(combinations_random_chosen))
  plt.gca().set(xlabel='learn_rate', ylabel='min_samples_leaf', title='Random Search Hyperparameters')
  plt.gca().set_xlim(x_lims)
  plt.gca().set_ylim(y_lims)
  plt.show()

  # Confirm how many hyperparameter combinations & print
number_combs = len(combinations_list)
print(number_combs)

# Sample and visualise specified combinations
for x in [50, 500, 1500]:
    sample_and_visualize_hyperparameters(x)
    
# Sample all the hyperparameter combinations & visualise
sample_and_visualize_hyperparameters(number_combs)

print("Notice how the bigger your sample space of a random search the more it looks like a grid search? In a later lesson we will look closer at comparing these two methods side by side.")