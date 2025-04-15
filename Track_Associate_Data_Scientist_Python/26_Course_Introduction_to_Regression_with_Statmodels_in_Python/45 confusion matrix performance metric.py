import pandas as pd
from statsmodels.formula.api import logit
import matplotlib.pyplot as plt

churn = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\26_Course_Introduction_to_Regression_with_Statmodels_in_Python\datasets\churn.csv')
mdl_churn_vs_relationship = logit('has_churned ~ time_since_first_purchase', data=churn).fit()
conf_matrix = mdl_churn_vs_relationship.pred_table()


# Extract TN, TP, FN and FP from conf_matrix
TN = conf_matrix[0, 0]
TP = conf_matrix[1, 1]
FN = conf_matrix[1, 0]
FP = conf_matrix[0, 1]

# Calculate and print the accuracy
accuracy = (TN + TP) / (TN + FN+ TP + FP)
print("accuracy: ", accuracy)

# Calculate and print the sensitivity
sensitivity = TP / (TP + FN)
print("sensitivity: ", sensitivity)

# Calculate and print the specificity
specificity = TN / (TN + FP)
print("specificity: ", specificity)