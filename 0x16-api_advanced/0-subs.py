#!/usr/bin/python3
"""
Script to query the Reddit API and return the number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.

    Args:
    - subreddit (str): The subreddit name to query.

    Returns:
    - int: Number of subscribers of the subreddit. Returns 0 if the subreddit is invalid or
           if there's any issue with the API request.
    """
    if not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Mozilla/5.0'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    try:
        response = requests.get(url, headers=user_agent)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException as e:
        print(f"Request Error: {e}")
        return 0
    except KeyError as e:
        print(f"KeyError: {e}")
        return 0
    except Exception as e:
        print(f"Error: {e}")
        return 0


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 number_of_subscribers.py <subreddit>")
        sys.exit(1)
    
    subreddit = sys.argv[1]
    num_subscribers = number_of_subscribers(subreddit)
    print(f"{num_subscribers}")