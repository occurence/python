import pandas as pd

adult = pd.read_csv(r'D:\STUDY\python\Review\12 cat data\datasets\adult.csv')

print(adult['Above/Below 50k'].value_counts())
adult1 = adult[adult['Above/Below 50k'] == ' <=50K']
adult2 = adult[adult['Above/Below 50k'] == ' >50K']

adult_obj = adult.groupby(by=['Above/Below 50k'])
print(adult_obj.mean(numeric_only=True))
print(adult.groupby(by=['Above/Below 50k']).mean(numeric_only=True))

print(adult.groupby(by=['Above/Below 50k'])[['Age', 'Education Num']].sum())
print(adult.groupby(by=['Above/Below 50k'])['Hours/Week'].mean())
print(adult.groupby(by=['Above/Below 50k']).sum()[['Age', 'Education Num']])

print(adult.groupby(by=['Above/Below 50k', 'Marital Status']).size())
