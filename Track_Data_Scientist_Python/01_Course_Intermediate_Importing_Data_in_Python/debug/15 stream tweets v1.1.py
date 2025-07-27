import tweepy, json

# Store credentials in relevant variables
consumer_key = "nZ6EA0FxZ293SxGNg8g8aP0HM"
consumer_secret = "fJGEodwe3KiKUnsYJC3VRndj7jevVvXbK2D5EiJ2nehafRgA6i"
access_token = "1092294848-aHN7DcRP9B4VMTQIhwqOYiB14YkW92fFO8k8EPy"
access_token_secret = "X4dHmhPfaksHcQ7SCbmZa2oYBBVSD2g8uIHXsp5CTaksx"

# Create your Stream object with credentials
stream = tweepy.Stream(consumer_key, consumer_secret, access_token, access_token_secret)

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth)

# # Define listener
# class MyStreamListener(tweepy.StreamListener):
#     def on_status(self, status):
#         print(f"{status.user.screen_name}: {status.text}")

#     def on_error(self, status_code):
#         print(f"Streaming error (status code: {status_code})")
#         return False

# # Create Stream object
# my_listener = MyStreamListener()
# stream = tweepy.Stream(auth=api.auth, listener=my_listener)

# # Filter your Stream variable
# stream.filter(track=['clinton','trump','sanders','cruz'])