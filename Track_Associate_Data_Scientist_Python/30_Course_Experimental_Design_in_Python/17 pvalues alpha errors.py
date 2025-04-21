import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

toy_durability = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\30_Course_Experimental_Design_in_Python\datasets\toy_durability.csv')

# Calculate mean Durability_Score for each Toy_Type
mean_durability = toy_durability.pivot_table(
  values='Durability_Score', index='Toy_Type', aggfunc=np.mean)
print(mean_durability)

# Perform t-test
educational_durability = toy_durability[toy_durability['Toy_Type'] == 'Educational']['Durability_Score']
recreational_durability = toy_durability[toy_durability['Toy_Type'] == 'Recreational']['Durability_Score']
t_stat, p_val = ttest_ind(educational_durability, recreational_durability)

print(p_val)