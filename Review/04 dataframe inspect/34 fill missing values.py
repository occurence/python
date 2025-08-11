import pandas as pd
import matplotlib.pyplot as plt

avocados = pd.read_pickle(r'D:\STUDY\python\Review\04 dataframe inspect\avoplotto.pkl')
# avocados_2016 = avocados[avocados['year'] == 2016]
avocados_2016 = pd.read_csv(r'D:\STUDY\python\Review\04 dataframe inspect\avocados_2016.csv', index_col=0)

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