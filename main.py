from chatgpt import get_chatgpt_response
from twitter import post_tweet

def main():
    print("start main")
    keyword = "your-keyword"
    tweet_content = get_chatgpt_response(keyword)
    post_tweet(tweet_content)
    print("finish main")
    return tweet_content