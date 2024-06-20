#!/usr/bin/python3
"""
Function to query the Reddit API and return the number of subscribers for a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    
    try:
        response = requests.get(url, headers=user_agent, allow_redirects=False)
        
        # Check the HTTP status code
        if response.status_code != 200:
            return 0

        # Attempt to parse the JSON response
        all_data = response.json()
        
        # Safely extract the number of subscribers
        return all_data.get('data', {}).get('subscribers', 0)
    except requests.exceptions.RequestException as e:
        # Handle any requests exceptions (e.g., network issues)
        return 0
    except ValueError as e:
        # Handle JSON decoding error
        return 0
    except Exception as e:
        # Handle any other exceptions
        return 0

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 0-main.py <subreddit>")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))