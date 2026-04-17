import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

world_happiness = pd.read_csv(r'D:\STUDY\python\Review\06 statistics\datasets\world_happiness.csv')

# Scatterplot of gdp_per_cap and life_exp
sns.scatterplot(x='gdp_per_cap', y='life_exp', data=world_happiness)

# Show plot
plt.show()

# Correlation between gdp_per_cap and life_exp
cor = world_happiness['gdp_per_cap'].corr(world_happiness['life_exp'])

print(cor)