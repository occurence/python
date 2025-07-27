import tweepy

# Step 1: Your credentials from Twitter Developer Portal
api_key = "API"
api_key_secret = "API SECRET"
bearer_token = "BEARER"
access_token = "ACCESS"
access_token_secret = "ACCESS SECRET"

# Step 2: Create an OAuth1 user context (if needed for other actions like posting)
auth = tweepy.OAuth1UserHandler(
    api_key, api_key_secret,
    access_token, access_token_secret
)
api = tweepy.API(auth)

# Step 3: Create your custom streaming client
class MyStreamListener(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(f"New tweet: {tweet.text}")

    def on_connection_error(self):
        print("Connection error occurred.")
        self.disconnect()

    def on_errors(self, errors):
        print(f"Errors: {errors}")
    
    def on_exception(self, exception):
        print(f"Exception: {exception}")
        return super().on_exception(exception)

# Step 4: Initialize stream with bearer token
stream = MyStreamListener(bearer_token)

# Step 5: (Optional) Remove previous stream rules to avoid conflicts
existing_rules = stream.get_rules().data
if existing_rules:
    rule_ids = [rule.id for rule in existing_rules]
    stream.delete_rules(rule_ids)

# Step 6: Add a new rule (change keyword as needed)
stream.add_rules(tweepy.StreamRule(value="Python"))

# Step 7: Start streaming
print("Starting stream...")
stream.filter(tweet_fields=["text"])
