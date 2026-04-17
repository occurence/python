import pandas as pd

left_dict = {
  "id": [329, 330, 135397, 331],
  "title": ['Jurassic Park', 'The Lost World: Jurassic Park', 'Jurassic World', 'Jurassic Park III'],
  "popularity": [40.413, 2.502, 418.709, 1.859],
  "release_date": ['1993-06-11', '1997-05-23', '2015-06-09', '2001-07-18']
}
taglines = pd.read_pickle(r'D:\STUDY\python\Review\05 join pandas\datasets\taglines.p')

left_table = pd.DataFrame(left_dict)

one_to_many = pd.read_pickle(r'D:\STUDY\python\Review\05 join pandas\datasets\crews.p')
one_to_many = one_to_many.drop('department', axis=1)
one_to_one = pd.read_pickle(r'D:\STUDY\python\Review\05 join pandas\datasets\taglines.p')

print(left_table.merge(one_to_one, on='id', how='left').shape)
print(left_table.merge(one_to_many, on='id', how='left').shape)