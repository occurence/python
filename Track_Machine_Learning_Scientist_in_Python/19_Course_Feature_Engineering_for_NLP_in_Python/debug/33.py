import csv
import pandas as pd

# with open(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\19_Course_Feature_Engineering_for_NLP_in_Python\datasets\transcripts.csv', 'r', newline='', encoding='utf-8') as f:
#     writer = csv.writer(f, quoting=csv.QUOTE_ALL)
#     for index, value in writer.items():
#         writer.writerow([index, value])

with open(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\19_Course_Feature_Engineering_for_NLP_in_Python\datasets\transcripts.csv', encoding='utf-8') as f:
    transcripts = f.read()
# transcripts = pd.DataFrame(transcripts)
print(transcripts)
print(type(transcripts))