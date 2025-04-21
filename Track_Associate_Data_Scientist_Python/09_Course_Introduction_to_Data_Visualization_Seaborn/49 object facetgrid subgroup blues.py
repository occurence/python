import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

survey_data = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\09_Course_Introduction_to_Data_Visualization_Seaborn\datasets\young_pets.csv')

# Set palette to "Blues"
sns.set_palette('Blues')

# Adjust to add subgroups based on "Interested in Pets"
# g = sns.catplot(x="Gender",
#                 y="Age", data=survey_data, 
#                 kind="box", hue='Interested in Pets')
g = sns.catplot(x="Gender",
                y="Age", data=survey_data, 
                kind="box", hue='Interested in Pets', palette="Blues")

# Set title to "Age of Those Interested in Pets vs. Not"
g.fig.suptitle('Age of Those Interested in Pets vs. Not')

# Show plot
plt.show()