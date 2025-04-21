import pandas as pd
import matplotlib.pyplot as plt

amir_deals = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\07_Course_Introduction_Statistics_Python\datasets\amir_deals.csv')


# Histogram of amount with 10 bins and show plot
amir_deals['amount'].hist(bins=10)
plt.show()