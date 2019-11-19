import json
import collections
import pandas as pd
import plotly.graph_objects as go


with open("step_2.json", 'r') as f:
    ls = json.load(f)

users = []
for dic in ls:
    if 'user' in dic:
        user = dic['user']
        users.append(user['screen_name'])

count_tweets = {}

for user in users:
    if user not in count_tweets:
        count_tweets[user] = 1
    else:
        count_tweets[user] += 1


word_counter = collections.Counter(count_tweets)
lst = word_counter.most_common(10)
df = pd.DataFrame(lst, columns = ['Word', 'Count'])


fig = go.Figure(
    data=[go.Bar(
        x=df['Count'],
        y=df['Word'],
        orientation='h',
        marker_color='deepskyblue',
        marker_line_width=1.5, opacity=0.6,
        text=df['Count'],
        textposition='auto',
    )],
    layout=go.Layout(
        title='Most Frequent Tweeters in 1 Minute Stream',
        xaxis=dict(title='Number of Tweets'),
        yaxis=dict(autorange='reversed'),
        margin=dict(l=40, t=40, b=40),
        paper_bgcolor='azure',
        plot_bgcolor='khaki'
    )
)
fig.write_image('step_4/step_4.png', width=450, height=600)
