import tweepy

# Replace with your Bearer Token
bearer_token = "BEARER"

class MyStreamListener(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(f"New tweet: {tweet.text}")

    def on_error(self, status_code):
        print(f"Error: {status_code}")

# Initialize the StreamingClient
stream = MyStreamListener(bearer_token)

# Add rules for filtering (example: track tweets containing "Python")
stream.add_rules(tweepy.StreamRule("Python"))

# Start the stream
stream.filter()