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
for submission in reddit.subreddit('askreddit').hot(limit=1):
    print(submission.title)
    sub = reddit.submission(id=submission)
    submission.comments.replace_more(limit=10)
    submission.comment_sort = 'top'
    post_time = submission.created_utc


    for top_level_comment in submission.comments:
        sec_since_post = top_level_comment.created_utc - post_time
        min_since_post = round(sec_since_post / 60)
        details = (top_level_comment.id,  min_since_post, top_level_comment.score)
        comments.append(details)

df = pd.DataFrame.from_records(comments, columns=['id', 'min_since_post', 'score'])

df2 = df.groupby('min_since_post').mean().rolling(5)
df2.sort_index(inplace=True)

pltx = df2.plot(figsize=(10,4), legend=False)
plt.show(pltx)











