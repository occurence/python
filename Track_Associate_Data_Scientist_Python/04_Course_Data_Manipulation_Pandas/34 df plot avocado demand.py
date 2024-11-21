import pandas as pd
avocados = pd.read_pickle(r'D:\STUDY\python\Course_Data_Manipulation_Pandas\avoplotto.pkl')
import matplotlib.pyplot as plt

# Scatter plot of avg_price vs. nb_sold with title
avocados.plot(x='nb_sold', y='avg_price', kind='scatter', title='Number of avocados sold vs. average price')

# Show the plot
plt.show()