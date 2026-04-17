import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

planes = pd.read_csv(r'D:\STUDY\python\Review\11 EDA\datasets\planes_h.csv')

# Preview the column
print(planes["Duration"].head())

# Remove the string character
planes["Duration"] = planes["Duration"].str.replace("h", "")

# Convert to float data type
planes["Duration"] = planes["Duration"].astype(float)

# Plot a histogram
sns.histplot(data=planes, x='Duration')
plt.show()