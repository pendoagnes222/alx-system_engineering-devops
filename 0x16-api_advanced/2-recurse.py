#!/usr/bin/python3
"""2-recurse copies all hot articles of a subreddit to a list"""
import requests


def recurse(subreddit, after=None, hot_list=[]):
    """`recurse` populates `hot_list` with all titles in `subreddit`
    Recursively call each page with an `after` query string retrieved from
    previous requests
    Args:
        subreddit (str): Name of subreddit to query info
        after (str, optional): value of query string used to traverse
        paginated json response
        hot_list (list, optional): A list to populate with titles of all
        subreddits
    Returns:
        None
    """
    try:
        if len(hot_list) != 0 and after is None:
            return hot_list
        base_url = (
            "https://www.reddit.com/r/{}/hot.json{}"
            .format(
                subreddit,
                "?after="+after if after is not None else ""
            )
        )
        res = requests.get(
            base_url,
            headers={"User-agent": "PostmanRuntime/7.28.4"},
            allow_redirects=False
        )
        for child in res.json().get("data").get("children"):
            hot_list.append(
                child.get("data").get("title")
            )
        after = res.json().get("data").get("after")
        populated_list = recurse(subreddit, after, hot_list)
        return populated_list
    except Exception:
        return None
