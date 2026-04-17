import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

reviews = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\16_Course_Working_with_Categorical_Data_in_Python\datasets\lasvegas_tripadvisor.csv')

# Create a point plot with catplot using "Hotel stars" and "Nr. reviews"
sns.catplot(
  # Split the data across Hotel stars and summarize Nr. reviews
  x='Hotel stars',
  y='Nr. reviews',
  data=reviews,
  # Specify a point plot
  kind='point',
  hue="Pool",
  # Make sure the lines and points don't overlap
  dodge=True
)
plt.show()