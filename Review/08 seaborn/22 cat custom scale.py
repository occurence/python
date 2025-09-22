import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

survey_data = pd.read_csv(r'D:\STUDY\python\Review\08 seaborn\datasets\young_lonely.csv')

# Set the context to "paper"
sns.set_context('paper')

# Create bar plot
sns.catplot(x="Number of Siblings", y="Feels Lonely",
            data=survey_data, kind="bar")

# Show plot
plt.show()

# Change the context to "notebook"
sns.set_context("notebook")

# Create bar plot
sns.catplot(x="Number of Siblings", y="Feels Lonely",
            data=survey_data, kind="bar")

# Show plot
plt.show()

# Change the context to "talk"
sns.set_context("talk")

# Create bar plot
sns.catplot(x="Number of Siblings", y="Feels Lonely",
            data=survey_data, kind="bar")

# Show plot
plt.show()

# Change the context to "poster"
sns.set_context("poster")

# Create bar plot
sns.catplot(x="Number of Siblings", y="Feels Lonely",
            data=survey_data, kind="bar")

# Show plot
plt.show()