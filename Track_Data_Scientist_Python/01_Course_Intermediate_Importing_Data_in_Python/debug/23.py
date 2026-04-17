import tweepy

# Step 1: Your credentials (from DataCamp or your app)
consumer_key = "nZ6EA0FxZ293SxGNg8g8aP0HM"
consumer_secret = "fJGEodwe3KiKUnsYJC3VRndj7jevVvXbK2D5EiJ2nehafRgA6i"
access_token = "1092294848-aHN7DcRP9B4VMTQIhwqOYiB14YkW92fFO8k8EPy"
access_token_secret = "X4dHmhPfaksHcQ7SCbmZa2oYBBVSD2g8uIHXsp5CTaksx"

# Step 2: Authenticate
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Step 3: API client (optional, but good to confirm connection)
api = tweepy.API(auth)
try:
    api.verify_credentials()
    print("Authentication OK")
except Exception as e:
    print(f"Error during authentication: {e}")

# Step 4: Create a listener using v1.1 Stream
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(f"@{status.user.screen_name}: {status.text}")

    def on_error(self, status_code):
        print(f"Error: {status_code}")
        if status_code == 420:
            return False  # Disconnect to avoid rate limiting

# Step 5: Create stream and filter
listener = MyStreamListener()
stream = tweepy.Stream(auth=auth, listener=listener)

# Start filtering tweets (example: keyword "Python")
stream.filter(track=["Python"])
