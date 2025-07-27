import tweepy

# Your Bearer Token (OAuth2)
bearer_token = "BEARER"

# Define your streaming class
class MyStream(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(tweet.text)

    def on_errors(self, errors):
        print("Error:", errors)

# Create the stream instance
stream = MyStream(bearer_token)

# OPTIONAL: Remove old rules first to avoid duplication
rules = stream.get_rules().data
if rules:
    rule_ids = [rule.id for rule in rules]
    stream.delete_rules(rule_ids)

# Add a new rule (keyword-based filter)
stream.add_rules(tweepy.StreamRule("clinton OR trump OR sanders OR cruz"))

# Start streaming
stream.filter()
