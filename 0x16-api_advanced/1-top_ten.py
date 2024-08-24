#!/usr/bin/python3
"""Module for task 1"""


def top_ten(subreddit):
    """queries the Reddit API and prints the titles of the first 10
    hot posts listed for a given subreddit"""
    import requests

    response = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if response.status_code >= 300:
        print('None')
    else:
        [print(child.get("data").get("title"))
         for child in response.json().get("data").get("children")]
