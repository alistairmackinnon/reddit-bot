# Bot will get replies to the comment and determine asshole or not


import config
import praw
from datetime import datetime
from datetime import timedelta
from praw.models import MoreComments

reddit = praw.Reddit(client_id=config.client_id
                     , client_secret=config.client_secret
                     , user_agent='testscript by /u/fakebot3'
                     , username=config.reddit_username
                     , password=config.reddit_password)

comments = {}

for submission in reddit.subreddit('askreddit').hot(limit=1):
    sub = reddit.submission(id=submission)
    submission.comments.replace_more(limit=0)
    submission.comment_sort = 'top'
    post_time = submission.created_utc

    i = 0
    for top_level_comment in submission.comments:
        if top_level_comment.is_submitter:
            continue
        sec_since_post = top_level_comment.created_utc - post_time
        min_since_post = round(sec_since_post / 60)
        comments[top_level_comment.id] = {'min_since_post': min_since_post
                                            ,  'score': sub.score}
        i += 1
        if i == 10:
            break

print(comments)














