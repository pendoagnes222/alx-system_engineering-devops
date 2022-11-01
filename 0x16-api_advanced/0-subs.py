#!/usr/bin/python3
"""Request reddit"""
import requests


def number_of_subscribers(subreddit):
    """Request for subreddit subscribers count
    Args:
        subreddit (str): Name of subreddit to query info
    Returns:
        Number of members of `subreddit`, 0 if subreddit not found
    """
    try:
        base_url = (
            "https://www.reddit.com/api/info.json?sr_name={}"
            .format(subreddit)
        )
        res = requests.get(
            base_url,
            headers={"User-agent": 'PostmanRuntime/7.28.4'},
            allow_redirects=False
        )
        return (
            res.json()
            .get("data")
            .get("children")[0]
            .get("data")
            .get("subscribers")
        )
    except Exception:
        return 0
