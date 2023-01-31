#!/usr/bin/python3
"""
function that queries the "Reddit API" & prints
titles of the first 10 hot posts of a subreddit
"""
import requests


def top_ten(subreddit):
    headers = {'User-Agent': 'CustomUserAgent'}
    url = ("https://www.reddit.com/r/{}/hot.json?limit=10"
           .format(subreddit))
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            title = post['data']['title']
            print(title)
    else:
        print(None)
