#!/usr/bin/python3
"""Get top ten titles from a subreddit using reddit API"""
import requests


def top_ten(subreddit):
    """Get top ten titles of posts from a subreddit"""
    url = 'https://www.reddit.com/r/' + subreddit + '/top.json?limit=10'
    session = requests.Session()
    headers = {
        'User-Agent': 'My User Agent 1.0'
    }
    session.headers.update(headers)
    response = session.get(url, allow_redirects=False)
    if (response.ok is False):
        print('None')
        return
    top_posts = response.json().get('data').get('children')
    titles_list = []
    for post in top_posts:
        titles_list.append(post.get('data').get('title'))
    print('\n'.join(titles_list))
