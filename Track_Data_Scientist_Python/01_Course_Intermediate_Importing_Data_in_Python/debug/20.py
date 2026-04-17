import tweepy

class MyStream(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(tweet.text)

bearer_token = "BEARER"
stream = MyStream(bearer_token)

# Clean up old rules
rules = stream.get_rules()
if rules.data:
    stream.delete_rules([rule.id for rule in rules.data])

# Add your rule
stream.add_rules(tweepy.StreamRule("Python"))

# Start stream
stream.filter()
