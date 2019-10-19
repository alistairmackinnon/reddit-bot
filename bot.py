# Bot will get replies to the comment and determine asshole or not


import config
import praw
from praw.models import MoreComments
import re
import pprint as pp

reddit = praw.Reddit(   client_id = 'UgPvUahzEm-iPQ'
                        , client_secret = '-TLSHC-A46k2OvdVl3Educaksck'
                        , user_agent='testscript by /u/fakebot3'
                        , username = config.reddit_username
                        , password = config.reddit_password)

print(reddit.user.me())
opinion_check = re.compile(r'YTA|NTA|ESH|NAH')

submissions = reddit.subreddit('amitheasshole').hot(limit = 10)
posts = {}

for submission in submissions:
    comments = submission.comments
    submission_id = submission.id
    post_details = {}
    post_details['yta_cnt'] = 0
    post_details['nta_cnt'] = 0
    post_details['esh_cnt'] = 0
    post_details['nah_cnt'] = 0

    for top_level_comment in comments:
        if isinstance(top_level_comment, MoreComments):
            continue
        opinion = opinion_check.search(top_level_comment.body)
        if opinion:
            match_value = opinion.group()
            if match_value == 'YTA':
                post_details['yta_cnt'] += 1
            elif match_value == 'NTA':
                post_details['nta_cnt'] += 1
            elif match_value == 'ESH':
                post_details['esh_cnt'] += 1
            elif match_value == 'NAH':
                post_details['nah_cnt'] += 1
    if post_details['yta_cnt'] > 10 and post_details['yta_cnt'] < post_details['nta_cnt']:
        submission.reply('yta dude')

    posts[submission_id] = post_details

pp.pprint(posts)





