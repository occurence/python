import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

survey_data = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\09_Course_Introduction_to_Data_Visualization_Seaborn\datasets\young-people-survey-responses.csv')

# Assuming survey_data is a pandas DataFrame and has an 'Age' column
survey_data['Age Category'] = survey_data['Age'].apply(lambda x: 'Less than 21' if x < 21 else '21+')

# Separate into column subplots based on age category
sns.catplot(y="Internet usage", data=survey_data,
            kind="count", col='Age Category')

# Show plot
plt.show()