import tweepy

# Step 1: Define your credentials
consumer_key = "nZ6EA0FxZ293SxGNg8g8aP0HM"
consumer_secret = "fJGEodwe3KiKUnsYJC3VRndj7jevVvXbK2D5EiJ2nehafRgA6i"
access_token = "1092294848-aHN7DcRP9B4VMTQIhwqOYiB14YkW92fFO8k8EPy"
access_token_secret = "X4dHmhPfaksHcQ7SCbmZa2oYBBVSD2g8uIHXsp5CTaksx"

# Step 2: Authenticate
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Step 3: Define listener class
class MyStreamListener(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(f"New tweet: {tweet.text}")

    def on_connection_error(self):
        print("Connection error. Stopping stream.")
        self.disconnect()

# Step 4: Use a Bearer Token for StreamingClient
bearer_token = "YOUR_BEARER_TOKEN"
stream = MyStreamListener(bearer_token)

# OPTIONAL: Clear previous rules (if running multiple times)
existing_rules = stream.get_rules().data
if existing_rules is not None:
    rule_ids = [rule.id for rule in existing_rules]
    stream.delete_rules(rule_ids)

# Step 5: Add new rules
stream.add_rules(tweepy.StreamRule("Python"))

# Step 6: Start streaming
stream.filter(tweet_fields=["text"])
