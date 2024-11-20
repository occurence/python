import pandas as pd
avocados = pd.read_pickle(r'D:\STUDY\python\Course_Data_Manipulation_Pandas\avoplotto.pkl')

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Get the total number of avocados sold on each date
nb_sold_by_date = avocados.groupby('date')['nb_sold'].sum()

# Create a line plot of the number of avocados sold by date
nb_sold_by_date.plot(kind='line')

# Show the plot
plt.show()