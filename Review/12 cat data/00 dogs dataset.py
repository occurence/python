import pandas as pd

dogs = pd.read_csv(r'D:\STUDY\python\Review\12 cat data\datasets\dogs.csv')

print(dogs['coat'].value_counts())