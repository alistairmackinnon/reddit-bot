# Bot will get replies to the comment and determine asshole or not


import config
import praw
import pandas as pd
import matplotlib.pyplot as plt


reddit = praw.Reddit(client_id=config.client_id
                     , client_secret=config.client_secret
                     , user_agent='testscript by /u/fakebot3'
                     , username=config.reddit_username
                     , password=config.reddit_password)

comments = []
for submission in reddit.subreddit('askreddit').hot(limit=5):
    print(submission.title)
    sub = reddit.submission(id=submission)
    submission.comments.replace_more(limit=15)
    submission.comment_sort = 'top'
    post_time = submission.created_utc


    for top_level_comment in submission.comments:
        sec_since_post = top_level_comment.created_utc - post_time
        min_since_post = round(sec_since_post / 60)
        if min_since_post <= 5:
            band = '01 - 5 mins'
        elif min_since_post <= 15:
            band = '02 - 15 mins'
        elif min_since_post <= 30:
            band = '03 -30 mins'
        elif min_since_post <= 45:
            band = '04 - 45 mins'
        elif min_since_post <= 60:
            band = '05 - 60 mins'
        elif min_since_post <= 90:
            band = '06 - 90 mins'
        elif min_since_post <= 90:
            band = '07 - 120 mins'
        elif min_since_post <= 90:
            band = '08 - 180 mins'
        else:
            continue
        details = (top_level_comment.id,  band, top_level_comment.score)
        comments.append(details)

df = pd.DataFrame.from_records(comments, columns=['id', 'band', 'score'])

df2 = df.groupby('band').median()
df2.sort_index(inplace=True)

print(df2['score'])

pltx = df2.plot(figsize=(10,4), legend=False)
plt.show(pltx)











