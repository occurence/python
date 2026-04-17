import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

amir_deals = pd.read_csv(r'D:\STUDY\python\Review\06 statistics\datasets\amir_deals.csv')

# Histogram of amount with 10 bins and show plot
amir_deals['amount'].hist(bins=10)
plt.show()