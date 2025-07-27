import tweepy

class MyStream(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(tweet.text)

bearer_token = "BEARER"
stream = MyStream(bearer_token)
stream.add_rules(tweepy.StreamRule("Python"))
stream.filter()
