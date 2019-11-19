from constants import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import json


class TwitterAuthenticator():

    def authenticate_twitter_app(self):
        auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        return auth


class TwitterListener(StreamListener):

    def __init__(self, file):
        self.file = file

    def on_data(self, data):
        all_data = json.loads(data)
        try:
            print(all_data)
            with open(self.file, 'a') as tf:
                tf.write(',\n')
                json.dump(all_data, tf)
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True

    def on_error(self, status):
        if status == 420:
            return False
        print(status)


class TwitterStreamer():

    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator()

    def stream_tweets(self, fetched_tweets_filename, keyword):
        listener = TwitterListener(fetched_tweets_filename)
        auth = self.twitter_authenticator.authenticate_twitter_app()
        stream = Stream(auth, listener)

        stream.filter(track=keyword)
        time.sleep(5)
