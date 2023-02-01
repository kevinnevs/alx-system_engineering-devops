#!/usr/bin/python3
"""
recursive function that queries "Reddit API" & returns
a list containing titles of all hot artciles for subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    headers = {'User-Agent': 'CustomUserAgent'}
    url = ("https://www.reddit.com/r/{}/hot.json".format(subreddit))
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        after = data.get('data').get('after')
        hot_posts = data.get('data').get('children')
        for post in hot_posts:
            hot_list.append(post.get('data').get('title'))
        if after:
            recurse(subreddit, hot_list, after)
        return hot_list
    return None
