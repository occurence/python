import pandas as pd
import numpy as np
from statsmodels.formula.api import logit

churn = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\26_Course_Introduction_to_Regression_with_Statmodels_in_Python\datasets\churn.csv')
explanatory_data = pd.DataFrame({'time_since_first_purchase': np.arange(-1.50, 4.25, 0.25)})
mdl_churn_vs_relationship = logit('has_churned ~ time_since_first_purchase', data=churn).fit()

# Create prediction_data
prediction_data = explanatory_data.assign(
  has_churned = mdl_churn_vs_relationship.predict(explanatory_data)
)

# Print the head
print(prediction_data.head())