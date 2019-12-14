# Bot will get replies to the comment and determine asshole or not


import config
import praw
from praw.models import MoreComments

reddit = praw.Reddit(client_id=config.client_id
                     , client_secret=config.client_secret
                     , user_agent='testscript by /u/fakebot3'
                     , username=config.reddit_username
                     , password=config.reddit_password)

posts = {}

for submission in reddit.subreddit('askreddit').controversial(limit=1):
    sub = reddit.submission(id=submission)
    posts[sub.id] = {'title': sub.title, 'ratio': sub.upvote_ratio, 'score': sub.score, 'num_comments': sub.num_comments}

for i in posts:
    print(posts[i]['title'])














