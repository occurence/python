import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

survey_data = pd.read_csv(r'D:\STUDY\python\Review\08 seaborn\datasets\young_parents.csv')

# Set the style to "darkgrid"
sns.set_style('darkgrid')

# Set a custom color palette
sns.set_palette(['#39A7D0', '#36ADA4'])

# Create the box plot of age distribution by gender
sns.catplot(x="Gender", y="Age", 
            data=survey_data, kind="box")

# Show plot
plt.show()