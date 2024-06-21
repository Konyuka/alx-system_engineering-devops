#!/usr/bin/python3
"""Query the Reddit and return the number of subscribers"""

import requests

def number_of_subscribers(subreddit):
  """Function that queries the Reddit API and returns the number of subscribers"""

  if subreddit is None or not isinstance(subreddit, str):
    return 0

  user_agent = {'User-agent': 'My Reddit Subscriber Scraper v1.0 (by your_username@example.com)'}
  url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
  response = requests.get(url, allow_redirects=False, headers=user_agent)

  if response.status_code == 200:
    try:
      all_data = response.json()
      return all_data.get('data', {}).get('subscribers', 0)
    except (ValueError, KeyError):
      print(f"Error: Failed to parse JSON response or missing key for '{subreddit}'.")
      return 0
  else:
    print(f"Error: Received status code {response.status_code} for '{subreddit}'.")
    return 0
