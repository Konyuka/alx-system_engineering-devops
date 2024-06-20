#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the given subreddit.
            If the subreddit is invalid, returns 0.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    try:
        url = f"https://www.reddit.com/r/{subreddit}/about.json"
        headers = {"User-Agent": "ALX-System_Engineering-Devops/0.1 (https://github.com/Konyuka/alx-system_engineering-devops)"}
        response = requests.get(url, headers=headers)

        # Check if the request was successful
        response.raise_for_status()

        # Extract the number of subscribers from the JSON response
        data = response.json()
        return data["data"]["subscribers"]
    except requests.exceptions.RequestException:
        # Handle exceptions related to the HTTP request
        return 0
    except (KeyError, ValueError):
        # Handle exceptions related to parsing the JSON response
        return 0


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 0-main.py <subreddit>")
        sys.exit(1)
    print("{:d}".format(number_of_subscribers(sys.argv[1])))