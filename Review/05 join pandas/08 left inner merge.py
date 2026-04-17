import pandas as pd

toy_story_dict = {
  "id": [10193, 863, 862],
  "title": ['Toy Story 3', 'Toy Story 2', 'Toy Story'],
  "popularity": [59.995, 73.575, 73.640],
  "release_date": ['2010-06-16', '1999-10-30', '1995-10-30']
}
taglines = pd.read_pickle(r'D:\STUDY\python\Review\05 join pandas\datasets\taglines.p')

toy_story = pd.DataFrame(toy_story_dict)

# Merge the toy_story and taglines tables with a left join
toystory_tag = toy_story.merge(taglines, on='id', how='left')

# Print the rows and shape of toystory_tag
print(toystory_tag)
print(toystory_tag.shape)

# Merge the toy_story and taglines tables with a inner join
toystory_tag = toy_story.merge(taglines, on='id', how='inner')

# Print the rows and shape of toystory_tag
print(toystory_tag)
print(toystory_tag.shape)