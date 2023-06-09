from chatgpt import get_chatgpt_response
from twitter import post_tweet

def main():
    keyword = "your-keyword"
    tweet_content = get_chatgpt_response(keyword)
    post_tweet(tweet_content)

if __name__ == "__main__":
    main()
