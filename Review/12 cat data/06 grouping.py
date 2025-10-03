import pandas as pd

adult = pd.read_csv(r'D:\STUDY\python\Review\12 cat data\datasets\adult.csv')

gb = adult.groupby(by=['Workclass', 'Above/Below 50k', 'Education']).size()

a = len(adult['Workclass'].value_counts())
b = len(adult['Above/Below 50k'].value_counts())
c = len(adult['Education'].value_counts())
print(len(gb), "groups out of ", a * b * c , "possible groups since no rows exist for some combinations")