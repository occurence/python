import pandas as pd

df = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\12_Course_Python_Toolbox\datasets\tweets.csv')

# Extract the created_at column from df: tweet_time
tweet_time = df['created_at']

# Extract the clock time: tweet_clock_time
tweet_clock_time = [entry[11:19] for entry in tweet_time if entry[17:19] == '19']

# Print the extracted times
print(tweet_clock_time)
