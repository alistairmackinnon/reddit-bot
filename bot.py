# Bot will get replies to the comment and determine asshole or not


import config
import praw
from praw.models import MoreComments

reddit = praw.Reddit(   client_id = 'UgPvUahzEm-iPQ'
                        , client_secret = '-TLSHC-A46k2OvdVl3Educaksck'
                        , user_agent='testscript by /u/fakebot3'
                        , username = config.reddit_username
                        , password = config.reddit_password)

print(reddit.user.me())
details = {}

submissions = reddit.subreddit('amitheasshole').top(limit = 1)

for submission in submissions:
    comments = submission.comments
    for top_level_comment in comments:
        if isinstance(top_level_comment, MoreComments):
            continue
        print(top_level_comment.body)
