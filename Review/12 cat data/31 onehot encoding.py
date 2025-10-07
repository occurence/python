import pandas as pd

soda = pd.read_csv(r'D:\STUDY\python\Review\12 cat data\datasets\soda.csv')

soda_onehot = pd.get_dummies(
  soda[["favorite_soda"]], 
  columns=["favorite_soda"]
)

print(soda_onehot.head(3))