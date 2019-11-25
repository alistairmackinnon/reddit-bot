# Bot will get replies to the comment and determine asshole or not


import config
import praw
import re

reddit = praw.Reddit(   client_id=config.client_id
                        , client_secret=config.client_secret
                        , user_agent='testscript by /u/fakebot3'
                        , username=config.reddit_username
                        , password=config.reddit_password)

opinion_check = re.compile(r'YTA|NTA|ESH|NAH ')

for mention in reddit.inbox.mentions(limit=25):
    post_details = {}
    post_details['yta_cnt'] = 0
    post_details['nta_cnt'] = 0
    post_details['esh_cnt'] = 0
    post_details['nah_cnt'] = 0
    post_details['comments_matched'] = 0

    submission_id = mention.submission
    submission = reddit.submission(id=submission_id)
    comments = submission.comments
    print(submission.title)
    print(mention.body)

    for top_level_comment in comments:
        if submission.num_comments > 100:
            if isinstance(top_level_comment):
                continue
            opinion = opinion_check.search(top_level_comment.body)
            if opinion:
                post_details['comments_matched'] += 1
                match_value = opinion.group()
                if match_value == 'YTA':
                    post_details['yta_cnt'] += 1
                elif match_value == 'NTA':
                    post_details['nta_cnt'] += 1
                elif match_value == 'ESH':
                    post_details['esh_cnt'] += 1
                elif match_value == 'NAH':
                    post_details['nah_cnt'] += 1
                # comments_matched = float(post_details['comments_matched'])
                # post_details['comments_matched']
    perc_yta = post_details['yta_cnt'] / post_details['comments_matched']
    perc_yta = round(perc_yta,2)

    if float(perc_yta,) > 0.50:
        print('Asshole detected')
        # mention.reply('Asshole detected')




"""

submissions = reddit.subreddit('amitheasshole').hot(limit = 1)

for submission in submissions:
    

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



    posts[submission_id] = post_details

pp.pprint(posts)

"""



