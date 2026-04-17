import tweepy
import time

client = tweepy.Client(bearer_token="BEARER")

while True:
    tweets = client.search_recent_tweets(query="Python", max_results=10)
    for tweet in tweets.data:
        print(tweet.text)
    time.sleep(60)  # wait 1 minute to avoid hitting rate limit
