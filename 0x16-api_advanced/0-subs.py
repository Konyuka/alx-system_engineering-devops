python
Copy code
#!/usr/bin/python3
"""
Importing requests module
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent)

    # Check the HTTP status code
    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        return 0

    # Attempt to parse the JSON response
    try:
        all_data = response.json()
    except ValueError as e:
        print(f"Error: Failed to parse JSON response - {e}")
        print(f"Response content: {response.text}")
        return 0

    # Safely extract the number of subscribers
    try:
        return all_data.get('data', {}).get('subscribers', 0)
    except Exception as e:
        print(f"Error: {e}")
        return 0


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 0-main.py <subreddit>")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))