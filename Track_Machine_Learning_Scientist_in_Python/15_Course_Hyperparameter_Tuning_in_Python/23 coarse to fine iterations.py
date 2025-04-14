import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from itertools import product
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import GradientBoostingClassifier


# x_lims1 = [0.01, 2.0]
# z_lims1 = [1, 64]
# learn_rate1 = np.linspace(x_lims1[0], x_lims1[1], 150)
# max_depth1 = list(range(z_lims1[0],z_lims1[1]))

# combinations_list1 = [list(x) for x in product(max_depth1,learn_rate1)]

# x_lims2 = [0.001, 1.0]
# z_lims2 = [1, 20]
# learn_rate2 = np.linspace(x_lims2[0], x_lims2[1], 50)
# max_depth2 = list(range(z_lims2[0],z_lims2[1]))

# combinations_list2 = [list(x) for x in product(max_depth2,learn_rate2)]

results_df2 = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\15_Course_Hyperparameter_Tuning_in_Python\datasets\results_df2_1000.csv', index_col=0)
results_df = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\15_Course_Hyperparameter_Tuning_in_Python\datasets\results_df1_500.csv', index_col=0)

def visualize_first():
    for name in results_df.columns[0:2]:
        plt.clf()
        plt.scatter(results_df[name], results_df['accuracy'], c=['blue'] * 500)
        plt.gca().set(xlabel='{}'.format(name), ylabel='accuracy', title='Accuracy for different {}s'.format(name))
        plt.gca().set_ylim([0, 100])
        x_line = 20
        if name == "learn_rate":
            x_line = 1
        plt.axvline(x=x_line, color="red", linewidth=4)
        plt.show()

def visualize_second():
  for name in results_df2.columns[0:2]:
    plt.clf()
    plt.scatter(results_df2[name],results_df2['accuracy'], c=['blue']*1000)
    plt.gca().set(xlabel='{}'.format(name), ylabel='accuracy', title='Accuracy for different {}s'.format(name))
    plt.gca().set_ylim([0,100])
    plt.show()

# Use the provided function to visualize the first results
visualize_first()

# Create some combinations lists & combine:
max_depth_list = list(range(1,21))
learn_rate_list = np.linspace(0.001,1,50)

# Call the function to visualize the second results
visualize_second()