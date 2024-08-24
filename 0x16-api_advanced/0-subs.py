#!/usr/bin/python3
"""module documentation task 0"""


def number_of_subscribers(subreddit):
    """queries the reddit api and return the number of
    subscribers (not active users, total subscribers)
    on a given subreddit"""
    import requests

    response = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "test-User-Agent"},
                            allow_redirects=False)
    if response.status_code >= 300:
        return 0

    return response.json().get("data").get("subscribers")
