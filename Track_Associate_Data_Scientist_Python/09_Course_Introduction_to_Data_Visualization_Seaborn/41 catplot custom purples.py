import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

survey_data = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\09_Course_Introduction_to_Data_Visualization_Seaborn\datasets\young_parents.csv')

# Set the color palette to "Purples"
sns.set_style("whitegrid")
sns.set_palette('Purples')

# Create a count plot of survey responses
category_order = ["Never", "Rarely", "Sometimes", 
                  "Often", "Always"]

# sns.catplot(x="Parents Advice", 
#             data=survey_data, 
#             kind="count", 
#             order=category_order)

sns.catplot(x="Parents Advice", 
            data=survey_data, 
            kind="count", 
            order=category_order,
            palette="Purples")

# Show plot
plt.show()