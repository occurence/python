# Import package
import json

# String of path to file: tweets_data_path
tweets_data_path = r'D:\STUDY\python\Track_Data_Scientist_Python\01_Course_Intermediate_Importing_Data_in_Python\datasets\tweets3.txt'

# Initialize empty list to store tweets: tweets_data
tweets_data = []

# Open connection to file
tweets_file = open(tweets_data_path, "r")

# Read in tweets and store in list: tweets_data
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)

# Close connection to file
tweets_file.close()

# Print the keys of the first tweet dict
print(tweets_data[0].keys())
