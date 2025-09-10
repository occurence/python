import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

world_happiness = pd.read_csv(r'D:\STUDY\python\Review\06 statistics\datasets\world_happiness.csv')

# Create log_gdp_per_cap column
world_happiness['log_gdp_per_cap'] = np.log(world_happiness['gdp_per_cap'])

# Scatterplot of happiness_score vs. log_gdp_per_cap
sns.scatterplot(x='log_gdp_per_cap', y='happiness_score', data=world_happiness)
plt.show()

# Calculate correlation
cor = world_happiness['log_gdp_per_cap'].corr(world_happiness['happiness_score'])
print(cor)