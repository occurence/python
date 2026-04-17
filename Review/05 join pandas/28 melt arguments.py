import pandas as pd

inflation = pd.read_csv(r'D:\STUDY\python\Review\05 join pandas\datasets\inflation_melt.csv', index_col=0)

print(inflation.head())

print(inflation.melt(id_vars=['country','indicator'], var_name='year', value_name='annual'))