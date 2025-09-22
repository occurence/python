import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

survey_data = pd.read_csv(r'D:\STUDY\python\Review\08 seaborn\datasets\young_lonely.csv')

# Change the orientation of the plot
sns.catplot(x="Internet usage", data=survey_data,
            kind="count")

# Show plot
plt.show()

# Separate into column subplots based on age category
sns.catplot(y="Internet usage", data=survey_data,
            kind="count")

# Show plot
plt.show()