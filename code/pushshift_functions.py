"""
The functions in this module will allow one to automate the process of grabbing Reddit posts.
Partially inspired by code from @NotTimBook
"""

import pandas as pd
import requests
import time

# Helper function
def get_subreddit_posts(params):
    """
    Returns posts from a given subreddit as specified in params.
    """
    url = 'https://api.pushshift.io/reddit/search/submission'
    data = requests.get(url, params).json()['data']
    
    if data:
        return data
    else:
        raise RuntimeError('Invalid subreddit')
        

# Helper function
def get_many_posts(subreddit, n_iter):
    """
    Returns a list whose elements are each bundles of 500 subreddit posts.
    """
    posts = []
    oldest_post = None
    
    for i in range(n_iter):
        params = {
            'subreddit': subreddit,
            'size': 500,
            'before': oldest_post
        }
        
        # Update user about status of function
        if (i + 1) % 5 == 0:
            print(f'Grabbing {i + 1}th bundle of posts from /r/{subreddit}...')
        
        # Grab ith bundle of posts, append to list
        posts.append(get_subreddit_posts(params))
        
        # Oldest post will always be from the last element of the posts list by design.
        oldest_post = min([post['created_utc'] for post in posts[-1]])
        
        # Throttle server usage
        time.sleep(5)
        
    return posts


# Helper function
def create_posts_df(subreddit, n_iter):
    """
    Returns a DataFrame representing 500 * n_iter posts from the given subreddit.
    """
    post_list = get_many_posts(subreddit, n_iter)
    df_list = [pd.DataFrame(posts) for posts in post_list]
    return pd.concat(df_list, ignore_index=True)


# Final function to be used for grabbing posts
def create_combined_df(subreddit_1, subreddit_2, n_iter):
    """
    Returns a DataFrame representing 500 * n_iter posts from each of the given subreddits.
    """
    df_1 = create_posts_df(subreddit_1, n_iter)
    df_2 = create_posts_df(subreddit_2, n_iter)
    return pd.concat([df_1, df_2], ignore_index=True)
