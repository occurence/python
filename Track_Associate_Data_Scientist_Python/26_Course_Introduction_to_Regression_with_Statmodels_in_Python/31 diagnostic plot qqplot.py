import pandas as pd
from statsmodels.formula.api import ols
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

taiwan_real_estate = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\26_Course_Introduction_to_Regression_with_Statmodels_in_Python\datasets\taiwan_real_estate2.csv')
mdl_price_vs_conv = ols('price_twd_msq ~ n_convenience', data=taiwan_real_estate).fit()

# Import qqplot
from statsmodels.api import qqplot

# Create the Q-Q plot of the residuals
qqplot(data=mdl_price_vs_conv.resid, fit=True, line="45")

# Show the plot
plt.show()