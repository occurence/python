import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

survey_data = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\09_Course_Introduction_to_Data_Visualization_Seaborn\datasets\young_lonely.csv')

# Set the style to "darkgrid"
sns.set_style('darkgrid')

# Set a custom color palette
sns.set_palette(['#39A7D0', '#36ADA4'])

# Create the box plot of age distribution by gender
# sns.catplot(x="Gender", y="Age", 
#             data=survey_data, kind="box")

sns.catplot(x="Gender", y="Age", 
            data=survey_data, kind="box", palette=['#39A7D0', '#36ADA4'])


# Show plot
plt.show()