from keys import oauth
import tweepy

def get_api():
    keys = oauth()
    auth = tweepy.OAuthHandler(keys["consumer_key"], keys["consumer_secret"])
    auth.set_access_token(keys["token_key"], keys["token_secret"])

    return tweepy.API(auth)


def get_user(api, nickname):
    return api.get_user(nickname)