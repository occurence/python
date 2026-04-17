import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import kruskal

food_preservation = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\30_Course_Experimental_Design_in_Python\datasets\food_preservation.csv')

# Create a boxen plot for nutrient retention by preservation method
sns.boxenplot(data=food_preservation, 
              x="PreservationMethod", 
              y="NutrientRetention")
plt.show()

# Separate nutrient retention for each preservation method
freezing = food_preservation[food_preservation['PreservationMethod'] == 'Freezing']['NutrientRetention']
canning = food_preservation[food_preservation['PreservationMethod'] == 'Canning']['NutrientRetention']
drying = food_preservation[food_preservation['PreservationMethod'] == 'Drying']['NutrientRetention']

# Perform Kruskal-Wallis test
k_stat, k_pval = kruskal(food_preservation[food_preservation['PreservationMethod'] == 'Freezing']['NutrientRetention'], food_preservation[food_preservation['PreservationMethod'] == 'Canning']['NutrientRetention'], food_preservation[food_preservation['PreservationMethod'] == 'Drying']['NutrientRetention'])
print("Kruskal-Wallis test p-value:", k_pval)