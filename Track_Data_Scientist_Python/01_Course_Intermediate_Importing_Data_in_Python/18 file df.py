# Import package
import pandas as pd
import json

tweets_data_path = r'D:\STUDY\python\Track_Data_Scientist_Python\01_Course_Intermediate_Importing_Data_in_Python\datasets\tweets3.txt'
tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)

# Build DataFrame of tweet texts and languages
df = pd.DataFrame(tweets_data, columns=['text','lang'])

# Print head of DataFrame
print(df.head())