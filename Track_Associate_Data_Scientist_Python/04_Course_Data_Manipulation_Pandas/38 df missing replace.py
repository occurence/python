import pandas as pd
avocados = pd.read_pickle(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\04_Course_Data_Manipulation_Pandas\avoplotto.pkl')
import matplotlib.pyplot as plt
avocados_2016 = avocados[avocados['year'] == 2016]

# From previous step
cols_with_missing = ["small_sold", "large_sold", "xl_sold"]
avocados_2016[cols_with_missing].hist()
plt.show()

# Fill in missing values with 0
avocados_filled = avocados_2016.fillna(0)

# Create histograms of the filled columns
avocados_filled[cols_with_missing].hist()

# Show the plot
plt.show()