#!/usr/bin/python3
"""Request reddit for top 10 hot posts in a subreddit"""
import requests


def top_ten(subreddit):
    """Print titles of top 10 hot posts in `subreddit`
    Args:
        subreddit (str): Name of subreddit to query info
    Returns:
        None
    """
    try:
        base_url = (
            "https://www.reddit.com/r/{}/hot.json?limit=10"
            .format(subreddit)
        )
        res = requests.get(
            base_url,
            headers={"User-agent": 'PostmanRuntime/7.28.4'},
            allow_redirects=False
        )
        for child in res.json().get("data").get("children"):
            print(child.get("data").get("title"))
    except Exception:
        print(None)
    return None
