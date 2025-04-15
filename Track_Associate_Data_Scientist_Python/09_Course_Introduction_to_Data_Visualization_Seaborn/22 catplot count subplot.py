import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

survey_data = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\09_Course_Introduction_to_Data_Visualization_Seaborn\datasets\young-people-survey-responses.csv')

# Create count plot of internet usage
sns.catplot(x='Internet usage', data=survey_data, kind='count')

# Show plot
plt.show()