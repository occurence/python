import pandas as pd
tweets_df = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\11_Course_Introduction_to_Functions_in_Python\datasets\tweets.csv')

# Select retweets from the Twitter DataFrame: result
result = filter(lambda x: x[0:2] == 'RT', tweets_df['text'])

# Create list from filter object result: res_list
res_list = list(result)

# Print all retweets in res_list
for tweet in res_list:
    print(tweet)