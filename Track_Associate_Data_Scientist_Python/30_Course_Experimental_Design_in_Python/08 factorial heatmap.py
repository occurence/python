import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

marketing_data = pd.read_feather(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\30_Course_Experimental_Design_in_Python\datasets\marketing_data.feather')

marketing_pivot = marketing_data.pivot_table(
  values='Conversions', 
  index='Messaging_Style', 
  columns='Time_of_Day', 
  aggfunc='mean')

# Visualize interactions with a heatmap
sns.heatmap(marketing_pivot,
            annot=True,
            cmap='coolwarm',
            fmt='g')

plt.show()