#!/usr/bin/python3
"""
function that queries "REDDIT API" & returns the no
of subscribers for a given subreddit
"""
import requests

def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'CustomUserAgent'}
    url = ("https://www.reddit.com/r/{}/about.json".format(subreddit))
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    return 0
