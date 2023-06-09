import tweepy

def post_tweet(content):
    consumer_key = 'your-twitter-consumer-key'
    consumer_secret = 'your-twitter-consumer-secret'
    access_token = 'your-twitter-access-token'
    access_token_secret = 'your-twitter-access-token-secret'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    api.update_status(content)
