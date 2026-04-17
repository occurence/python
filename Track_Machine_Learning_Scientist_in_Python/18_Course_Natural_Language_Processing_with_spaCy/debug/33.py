import pandas as pd
import json

# with open(r"D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\18_Course_Natural_Language_Processing_with_spaCy\datasets\corona.json", "r", encoding="utf-8") as f:
#     # df = list(json.load(f))
#     df = json.load(f)

# training_data = [(item["text"], {"entities": item["entities"]}) for item in data]

df = pd.read_json(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\18_Course_Natural_Language_Processing_with_spaCy\datasets\corona.json')
training_data = [(row[0], row[1]) for row in df.itertuples(index=False)]
# print(type(training_data))
print(training_data)