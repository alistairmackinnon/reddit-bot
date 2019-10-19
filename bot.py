# Bot will get replies to the comment and determine asshole or not


import config
import praw
from praw.models import MoreComments
import re

reddit = praw.Reddit(   client_id = 'UgPvUahzEm-iPQ'
                        , client_secret = '-TLSHC-A46k2OvdVl3Educaksck'
                        , user_agent='testscript by /u/fakebot3'
                        , username = config.reddit_username
                        , password = config.reddit_password)

print(reddit.user.me())
opinion_check = re.compile(r'YTA|NTA|ESH|NAH')

submissions = reddit.subreddit('amitheasshole').hot(limit = 1)
comment_details = {}

comment_details['id'] = ''
comment_details['yta_cnt'] = 0
comment_details['nta_cnt'] = 0
comment_details['esh_cnt'] = 0
comment_details['nah_cnt'] = 0

for submission in submissions:
    comments = submission.comments
    for top_level_comment in comments:
        if isinstance(top_level_comment, MoreComments):
            continue
        opinion = opinion_check.search(top_level_comment.body)
        if opinion:
            match_value = opinion.group()
            comment_details['id'] = top_level_comment.id
            if match_value == 'YTA':
                comment_details['yta_cnt'] += 1
            elif match_value == 'NTA':
                comment_details['nta_cnt'] += 1
            elif match_value == 'ESH':
                comment_details['esh_cnt'] += 1
            elif match_value == 'NAH':
                comment_details['nah_cnt'] += 1
    print(comment_details)



