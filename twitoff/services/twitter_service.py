import tweepy

import os
from dotenv import load_dotenv

load_dotenv()

TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

if __name__ == "__main__":

    # screen_name = input("Screen name: ")
    user = api.get_user("elonmusk")

    # statuses = api.user_timeline("elonmusk", count=25)
    # for status in statuses:
    #     print(status.text)

    statuses = api.user_timeline("elonmusk", tweet_mode="extended",count=35, exclude_replies=True, include_rts=False)
