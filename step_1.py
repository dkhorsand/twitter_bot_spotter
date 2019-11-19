from utils import TwitterStreamer

#                                           Twitter Bot Spotter
# ******************FOLLOW THESE STEPS******************

# *****BEFORE STARTING MAKE SURE YOU HAVE FILLED YOUR API KEYS INTO constants.py*****

#       STEP 1
#       Run "step_1.py" and stop it after 1 minute

#       STEP 2
#       In "step_2.json" replace the ',' at the beginning with '[' , then add ']' at the very end to make it a list

#       STEP 3
#       Run "step_3.py"

#       STEP 4
#       Find your new Plotly chart in the "step_4" directory

# ******************DELETE step_2.json BEFORE TRYING AGAIN******************


if __name__ == '__main__':
    # try changing the keyword
    keyword = ['trump']
    fetched_tweets_filename = "step_2.json"
    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, keyword)

